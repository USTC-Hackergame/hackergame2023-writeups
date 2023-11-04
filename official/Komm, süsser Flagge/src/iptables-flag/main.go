package main

import (
	"bytes"
	"io"
	"log"
	"net/http"
	"time"
)

const (
	MaxTokenSize   = 256
	MaxHeaderBytes = 1 << 14 // 16 KiB
)

func main() {
	startServer(":18080", flagHandler(flag1))
	startServer(":18081", flagHandler(flag2))
	startServer(":18082", flagHandler(flag3))
	<-make(chan struct{})
}

// This is a demo source code.
// The actual server has the correct implementation for these 3 functions.
func flag1(token []byte) string {
	return "This is flag 1."
}

func flag2(token []byte) string {
	return "This is flag 2."
}

func flag3(token []byte) string {
	return "This is flag 3."
}

// Implements http.Handler
type flagHandler func([]byte) string

func (h flagHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Connection", "close")
	switch r.Method {
	case "GET":
		http.Error(w, "POST me your token and I'll give you the FLAG", http.StatusOK)
	case "POST":
		defer r.Body.Close()
		body, err := io.ReadAll(r.Body)
		if err != nil {
			log.Printf("Error reading request body: %v", err)
			http.Error(w, "An internal error occurred", http.StatusInternalServerError)
			return
		}
		token := bytes.TrimSpace(body)
		http.Error(w, h(token), http.StatusOK)
	default:
		http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
	}
}

func startServer(addr string, handler http.Handler) *http.Server {
	s := &http.Server{
		Handler:        handler,
		Addr:           addr,
		ReadTimeout:    10 * time.Second,
		WriteTimeout:   10 * time.Second,
		MaxHeaderBytes: MaxHeaderBytes,
	}
	s.SetKeepAlivesEnabled(false)
	log.Printf("Starting server on %s", addr)
	go func() {
		panic(s.ListenAndServe())
	}()
	return s
}
