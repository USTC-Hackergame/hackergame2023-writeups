// gcc -fPIC -Wall -shared -o lib.so lib.c

#define _GNU_SOURCE
#include <dlfcn.h>
#include <sys/syscall.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <spawn.h>

int is_flag(const char *pathname) {
    return strstr(pathname, "flag") != NULL;
}

FILE *fopen(const char *restrict pathname, const char *restrict mode) {
    static FILE *(*real_fopen)(const char *restrict, const char *restrict) = NULL;
    if (real_fopen == NULL) {
        real_fopen = dlsym(RTLD_NEXT, "fopen");
    }
    if (is_flag(pathname)) {
        return real_fopen("/fakeflag", mode);
    }
    return real_fopen(pathname, mode);
}

FILE *freopen(const char *restrict pathname, const char *restrict mode, FILE *restrict stream) {
    static FILE *(*real_freopen)(const char *restrict, const char *restrict, FILE *restrict) = NULL;
    if (real_freopen == NULL) {
        real_freopen = dlsym(RTLD_NEXT, "freopen");
    }
    if (is_flag(pathname)) {
        return real_freopen("/fakeflag", mode, stream);
    }
    return real_freopen(pathname, mode, stream);
}

int open(const char *pathname, int flags, ...) {
    static int (*real_open)(const char *, int, ...) = NULL;
    if (real_open == NULL) {
        real_open = dlsym(RTLD_NEXT, "open");
    }
    if (is_flag(pathname)) {
        return real_open("/fakeflag", flags);
    }
    return real_open(pathname, flags);
}

int creat(const char *file, mode_t mode) {
    static int (*real_creat)(const char *, mode_t) = NULL;
    if (real_creat == NULL) {
        real_creat = dlsym(RTLD_NEXT, "creat");
    }
    if (is_flag(file)) {
        return real_creat("/fakeflag", mode);
    }
    return real_creat(file, mode);
}

int openat(int fd, const char *file, int oflag, ...) {
    static int (*real_openat)(int, const char *, int, ...) = NULL;
    if (real_openat == NULL) {
        real_openat = dlsym(RTLD_NEXT, "openat");
    }
    if (is_flag(file)) {
        return real_openat(fd, "/fakeflag", oflag);
    }
    return real_openat(fd, file, oflag);
}

int openat64(int fd, const char *file, int oflag, ...) {
    static int (*real_openat64)(int, const char *, int, ...) = NULL;
    if (real_openat64 == NULL) {
        real_openat64 = dlsym(RTLD_NEXT, "openat64");
    }
    if (is_flag(file)) {
        return real_openat64(fd, "/fakeflag", oflag);
    }
    return real_openat64(fd, file, oflag);
}

int system(const char *command) {
    return 0;
}

int execl(const char *path, const char *arg, ...) {
    return 0;
}

int execle(const char *path, const char *arg, ...) {
    return 0;
}

int execlp(const char *file, const char *arg, ...) {
    return 0;
}

int execv(const char *path, char *const argv[]) {
    return 0;
}

int execve(const char *path, char *const argv[], char *const envp[]) {
    return 0;
}

int execvp(const char *file, char *const argv[]) {
    return 0;
}

int execvpe(const char *file, char *const argv[], char *const envp[]) {
    return 0;
}

int posix_spawn(pid_t *restrict pid, const char *restrict path, const posix_spawn_file_actions_t *restrict file_actions, const posix_spawnattr_t *restrict attrp, char *const *restrict argv, char *const *restrict envp) {
    return 0;
}

int posix_spawnp(pid_t *pid, const char *file, const posix_spawn_file_actions_t *file_actions, const posix_spawnattr_t *attrp, char *const *argv, char *const *envp) {
    return 0;
}

int clone(int (*fn)(void *), void *child_stack, int flags, void *arg, ...) {
    return 0;
}

long syscall(long sysno, ...) {
    return 0;
}

int link(const char *from, const char *to) {
    return 0;
}

int linkat(int fromfd, const char *from, int tofd, const char *to, int flags) {
    return 0;
}

int symlink(const char *from, const char *to) {
    return 0;
}

int symlinkat(const char *from, int tofd, const char *to) {
    return 0;
}

int rename(const char *old, const char *new) {
    return 0;
}

int renameat(int oldfd, const char *old, int newfd, const char *new) {
    return 0;
}

int renameat2(int oldfd, const char *old, int newfd, const char *new, unsigned int flags) {
    return 0;
}
