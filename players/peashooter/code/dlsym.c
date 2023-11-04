#define _GNU_SOURCE
#include <stdio.h>
#include <dlfcn.h>

int main() {
    // Load the original fopen function from the standard C library
    void* handle = dlopen("libc.so.6", RTLD_LAZY);  // Use the appropriate library name
    if (!handle) {
        fprintf(stderr, "Failed to load the C library: %s\n", dlerror());
        return 1;
    }

    FILE* (*reall_fopen)(const char *, const char *) = (FILE* (*)(const char *, const char *))dlsym(handle, "fopen");

    if (!reall_fopen) {
        fprintf(stderr, "Failed to get the original fopen function: %s\n", dlerror());
        return 1;
    }

    // 文件名
    const char *file_name = "flag";
    
    // 打开文件
    FILE *file = reall_fopen(file_name, "r");
    
    if (file == NULL) {
        perror("Failed to open file");
        return 1;
    }
    
    // 逐行读取文件内容并输出到标准输出
    char buffer[1024];
    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("%s", buffer);
    }
    
    // 关闭文件
    fclose(file);
    
    return 0;
}
