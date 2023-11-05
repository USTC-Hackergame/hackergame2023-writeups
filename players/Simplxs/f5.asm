
extrn puts:proc
extrn memcmp:proc
extrn scanf:proc


.data

HACKERGAME      db  7Fh,2,57h,0EDh,0E0h,0C6h,0A3h,0A2h,0CBh,0C2h,0ABh,0D6h,0CAh,0BEh,82h,0BEh,2Ch,0AAh,5Bh,19h,10h,0Ah,9,47h,0B2h,22h,0EEh,12h,0FCh,0Bh,26h,44h
HACKERGAME0     db 'Please input the flag:',0
HACKERGAME1     db  '%s',0
HACKERGAME2     db 'Congratulations!!!',0
HACKERGAME3     db 'Flag is not correct!',0

flag1 db 'flag{',0
flag2 db '}'

f772f24 db 0,0,0,0,0,0,0,0


.code

main            proc

var_1AD         = byte ptr -1ADh
var_1AC         = dword ptr -1ACh
var_1A8         = dword ptr -1A8h
var_1A4         = dword ptr -1A4h
var_1A0         = dword ptr -1A0h
var_19C         = dword ptr -19Ch
var_198         = dword ptr -198h
i2         = dword ptr -194h
i4         = dword ptr -190h
var_18C         = dword ptr -18Ch
FlagOffset         = byte ptr -188h
var_17C         = dword ptr -17Ch
var_178         = dword ptr -178h
tmpi2         = dword ptr -174h
var_170         = dword ptr -170h
var_16C         = dword ptr -16Ch
TMPI         = qword ptr -168h
var_160         = qword ptr -160h
var_158         = qword ptr -158h
var_150         = qword ptr -150h
var_148         = qword ptr -148h
var_140         = qword ptr -140h
tmpFlagOffset         = qword ptr -138h
var_130         = qword ptr -130h
var_128         = qword ptr -128h
var_120         = qword ptr -120h
var_118         = qword ptr -118h
var_110         = qword ptr -110h
Buf1            = byte ptr -108h
var_D8          = xmmword ptr -0D8h
var_C8          = xmmword ptr -0C8h
var_B8          = xmmword ptr -0B8h
var_A8          = xmmword ptr -0A8h
var_98          = xmmword ptr -98h
var_88          = xmmword ptr -88h
var_78          = xmmword ptr -78h
var_68          = xmmword ptr -68h
var_58          = xmmword ptr -58h
var_48          = xmmword ptr -48h

    push    r15
    push    r14
    push    r13
    push    r12
    push    rsi
    push    rdi
    push    rbx
    sub     rsp, 1A0h
    movaps  [rsp+1D8h+var_48], xmm15
    movaps  [rsp+1D8h+var_58], xmm14
    movaps  [rsp+1D8h+var_68], xmm13
    movaps  [rsp+1D8h+var_78], xmm12
    movaps  [rsp+1D8h+var_88], xmm11
    movaps  [rsp+1D8h+var_98], xmm10
    movaps  [rsp+1D8h+var_A8], xmm9
    movaps  [rsp+1D8h+var_B8], xmm8
    movaps  [rsp+1D8h+var_C8], xmm7
    movaps  [rsp+1D8h+var_D8], xmm6
    lea     rcx, HACKERGAME0 
    mov     [rsp+1D8h+var_18C], 0
    call    puts
    lea     rdx, [rsp+1D8h+Buf1]
    lea     rcx, HACKERGAME1
    mov     r8d, 27h 
    call    scanf
    lea     rcx, [rsp+1D8h+Buf1] 
    lea     rdx, flag1 
    mov     r8d, 5          
    call    memcmp
    cmp     eax, 0
    jnz     near ptr loc_1400013B7
    lea     rax, [rsp+1D8h+Buf1]
    add     rax, 25h 
    lea     r8, flag2 
    mov     r8w, [r8]
    mov     r9w, [rax]
    xor     eax, eax
    sub     r9w, r8w
    setnz   al
    cmp     eax, 0
    jnz     near ptr loc_1400013B7
    lea     r10, [rsp+1D8h+Buf1]
    lea     rbx, [rsp+1D8h+FlagOffset]
    add     r10, 5
    mov     [rbx], r10
    mov     [rsp+1D8h+i4], 0

loc_1400010EC: 
    cmp     [rsp+1D8h+i4], 4
    jge     loc_140001185
    mov     [rsp+1D8h+i2], 0

loc_1400010FF: 
    cmp     [rsp+1D8h+i2], 2
    jge     near ptr loc_140001174

    lea     edx, [rsp+1D8h+i4]
    lea     r15, [rsp+1D8h+TMPI]

    mov     r9, [rdx]
    shl     r9, 4
    xor     r9, 55AA00FFh
    mov     [r15], r9
    
    lea     rbx, [rsp+1D8h+FlagOffset]
    lea     r14, [rsp+1D8h+i2]

    movsxd  rsi, r15d
    mov     rdi, rsi
    sar     rdi, 3Fh

    mov     r11, rsi
    mov     r13, rdi
    mov     r15, [rbx]
    
    push    rdx
    movsxd  rsi, r14d
    shl     rsi, 4
    mov     rax, [r15+rsi]
    mov     rdi, [r15+rsi+8]
    mov     rbx, rax
    imul    rbx, r13
    mul     r11
    add     rdx, rbx
    imul    rdi, r11
    add     rdx, rdi
    mov     [r15+rsi], rax
    mov     [r15+rsi+8], rdx
    pop     rdx

    lea     r10, [rsp+1D8h+i2]

    mov     ebx, [r10]
    add     ebx, 1
    mov     [r10], ebx

    jmp     near ptr loc_1400010FF


loc_140001174: 
    lea     r10, [rsp+1D8h+i4]

    mov     ebx, [r10]
    add     ebx, 1
    mov     [r10], ebx

    jmp     loc_1400010EC


loc_140001185: 
    mov     [rsp+1D8h+var_198], 0

loc_14000118D: 
    cmp     [rsp+1D8h+var_198], 4
    jge     near ptr loc_1400011D2
    
    lea     r10, [rsp+1D8h+FlagOffset]
    lea     rbx, [rsp+1D8h+var_198]
    lea     r14, [rsp+1D8h+var_160]
    lea     rax, [rsp+1D8h+var_158]

    mov     r8, [r10]
    movsxd  rsi, dword ptr [rbx]
    mov     rdi, rsi
    shl     rdi, 3
    mov     rdx, r8
    add     rdx, rdi
    mov     [r14], rdx
    mov     rdx, [r8+rsi*8]
    mov     [rax], rdx

    mov     rdx, [rsp+1D8h+var_160]
    mov     r10, [rsp+1D8h+var_158]

    push    r15
    push    r13
    push    rax
    sub     rsp, 20h
    mov     r15, 7A026655FD263677h
    mov     r14, r10
    mov     r9, r14
    xor     r9, r15
    mov     [rdx], r9
    add     rsp, 20h
    pop     rax
    pop     r13
    pop     r15

    lea     rax, [rsp+1D8h+var_198]
    push    r12
    push    rdx
    sub     rsp, 28h
    mov     ebx, [rax]
    add     ebx, 1
    mov     [rax], ebx
    add     rsp, 28h
    pop     rdx
    pop     r12

    jmp     near ptr loc_14000118D


loc_1400011D2: 
    mov     [rsp+1D8h+var_19C], 0

loc_1400011DA: 
    cmp     [rsp+1D8h+var_19C], 4
    jge     loc_140001271
    mov     [rsp+1D8h+var_1A0], 0

loc_1400011ED: 
    cmp     [rsp+1D8h+var_1A0], 8
    jge     near ptr loc_140001260
    lea     r14, [rsp+1D8h+var_19C]
    lea     r13, [rsp+1D8h+var_150]

    push    rcx
    push    r11
    push    rdi
    push    rax
    sub     rsp, 28h
    mov     rdx, r13
    mov     r14d, [r14]
    mov     ecx, 2
    mov     r15d, ecx
    
    push    rcx
    mov     rcx, r15
    mov     r9, r14
    shl     r9, cl
    pop     rcx
    mov     ecx, 0DEADBEEFh
    mov     r14d, ecx
    mov     r15d, r9d
    
    mov     r9, r14
    xor     r9, r15
    mov     [rdx], r9
    add     rsp, 28h
    pop     rax
    pop     rdi
    pop     r11
    pop     rcx

    mov     r13, [rsp+1D8h+var_150]
    
    lea     r10, [rsp+1D8h+FlagOffset]
    lea     r14, [rsp+1D8h+var_1A0]
    lea     r15, [rsp+1D8h+var_170]
    lea     rcx, [rsp+1D8h+var_130]
    lea     rdx, [rsp+1D8h+var_128]

    mov     [r15], r13d
    mov     rsi, [r10]
    mov     [rcx], rsi
    movsxd  rsi, dword ptr [r14]
    mov     [rdx], rsi

    mov     r13d, [rsp+1D8h+var_170]
    mov     r14, [rsp+1D8h+var_130]
    mov     r15, [rsp+1D8h+var_128]
    
    imul    r13d, [r14+r15*4]
    mov     [r14+r15*4], r13d
    lea     r14, [rsp+1D8h+var_1A0]

    push    rax
    sub     rsp, 20h
    mov     rax, r14
    mov     ebx, [rax]
    add     ebx, 1
    mov     [rax], ebx
    add     rsp, 20h
    pop     rax

    jmp     near ptr loc_1400011ED


loc_140001260: 
    lea     rdx, [rsp+1D8h+var_19C]
    
    push    r14
    push    r13
    push    rbx
    push    rax
    sub     rsp, 28h
    mov     rax, rdx
    mov     r14d, [rax]
    mov     ebx, 1
    mov     r13d, ebx

    mov     rbx, r14
    add     rbx, r13
    mov     [rax], ebx
    add     rsp, 28h
    pop     rax
    pop     rbx
    pop     r13
    pop     r14

    jmp     near ptr loc_1400011DA

loc_140001271:
    mov     [rsp+1D8h+var_1A4], 0

loc_140001279: 
    cmp     [rsp+1D8h+var_1A4], 10h
    jge     near ptr loc_1400012BE
    
    lea     rdx, [rsp+1D8h+FlagOffset]
    lea     r15, [rsp+1D8h+var_1A4]
    lea     r12, [rsp+1D8h+var_148]
    lea     r10, [rsp+1D8h+var_17C]

    mov     r8, [rdx]
    movsxd  rsi, dword ptr [r15]
    mov     rdi, rsi
    shl     rdi, 1
    mov     rdx, r8
    add     rdx, rdi
    mov     [r12], rdx
    movzx   edx, word ptr [r8+rsi*2]
    mov     [r10], edx

    mov     rbx, [rsp+1D8h+var_148]
    mov     r10d, [rsp+1D8h+var_17C]

    push    rcx
    push    r13
    push    r11
    sub     rsp, 20h
    mov     rdx, rbx
    mov     r14d, r10d
    mov     ecx, 0CDECh
    mov     r15d, ecx
    mov     r9, r14
    xor     r9, r15
    mov     [rdx], r9w
    add     rsp, 20h
    pop     r11
    pop     r13
    pop     rcx

    lea     r14, [rsp+1D8h+var_1A4]
    push    rax
    sub     rsp, 20h
    mov     rax, r14
    mov     ebx, [rax]
    add     ebx, 1
    mov     [rax], ebx
    add     rsp, 20h
    pop     rax
    jmp     near ptr loc_140001279


loc_1400012BE: 
    mov     [rsp+1D8h+var_1A8], 0

loc_1400012C6: 
    cmp     [rsp+1D8h+var_1A8], 4
    jge     loc_1400013A1
    mov     [rsp+1D8h+var_1AC], 0

loc_1400012D9: 
    cmp     [rsp+1D8h+var_1AC], 20h 
    jge     loc_140001390
    lea     r10, [rsp+1D8h+var_1A8]
    lea     rdx, [rsp+1D8h+var_140]
    
    push    r15
    push    r13
    push    rax
    sub     rsp, 20h
    mov     r14d, [r10]
    mov     r8d, 1
    mov     r15d, r8d
    
    push    rcx
    mov     rcx, r15
    mov     r9, r14
    shl     r9, cl
    pop     rcx
    mov     r8d, 21h 
    mov     r14d, r8d
    mov     r15d, r9d
    
    mov     r9, r14
    xor     r9, r15
    mov     [rdx], r9
    add     rsp, 20h
    pop     rax
    pop     r13
    pop     r15

    mov     rax, [rsp+1D8h+var_140]
    
    lea     r10, [rsp+1D8h+FlagOffset]
    lea     r11, [rsp+1D8h+var_1AC]
    lea     r15, [rsp+1D8h+var_16C]
    lea     rcx, [rsp+1D8h+var_120]
    lea     rdx, [rsp+1D8h+var_1AD]

    mov     [r15], eax
    mov     rax, [r10]
    movsxd  rsi, dword ptr [r11]
    mov     rdi, rax
    add     rdi, rsi
    mov     [rcx], rdi
    mov     al, [rax+rsi]
    mov     [rdx], al

    mov     r15d, [rsp+1D8h+var_16C]
    mov     r14, [rsp+1D8h+var_120]
    mov     al, [rsp+1D8h+var_1AD]
    movzx   r13d, al
    
    lea     r12, [rsp+1D8h+var_1A8]

    movzx   edx, r13b
    imul    edx, r15d
    mov     [r14], dl
    cmp     dword ptr [r12], 3
    jnz     short loc_14000134D

loc_140001381:
    lea     rdx, [rsp+1D8h+var_1AC]
    
    push    r14
    push    r13
    push    rbx
    push    rax
    sub     rsp, 28h
    mov     rax, rdx
    mov     ebx, [rax]
    add     ebx, 1
    mov     [rax], ebx
    add     rsp, 28h
    pop     rax
    pop     rbx
    pop     r13
    pop     r14

    jmp     loc_1400012D9

loc_14000134D: 
    
    lea     r10, [rsp+1D8h+FlagOffset]
    lea     rbx, [rsp+1D8h+var_1AC]
    lea     r14, [rsp+1D8h+var_178]

    mov     rax, [r10]
    movsxd  rdx, dword ptr [rbx]
    movzx   eax, byte ptr [rax+rdx]
    mov     [r14], eax

    mov     r10d, [rsp+1D8h+var_178]
    lea     r13, [rsp+1D8h+var_1AC]
    
    lea     r8, HACKERGAME
    movsxd  r9, dword ptr [r13+0]
    movzx   r8d, byte ptr [r8+r9]
    cmp     r10d, r8d
    jnz     short loc_1400013B7
    jmp     short loc_140001381

loc_140001390: 
    lea     rax, [rsp+1D8h+var_1A8]

    push    r12
    push    rdx
    sub     rsp, 28h
    mov     ebx, [rax]
    add     ebx, 1
    mov     [rax], ebx

    add     rsp, 28h
    pop     rdx
    pop     r12

    jmp     loc_1400012C6


loc_1400013A1: 
    lea     rcx, HACKERGAME2 
    call    puts
    mov     [rsp+1D8h+var_18C], 0
    jmp     short loc_1400013CB


loc_1400013B7: 

    lea     rcx, HACKERGAME3 
    call    puts
    mov     [rsp+1D8h+var_18C], 0

loc_1400013CB: 
    mov     eax, [rsp+1D8h+var_18C]
    movaps  xmm6, [rsp+1D8h+var_D8]
    movaps  xmm7, [rsp+1D8h+var_C8]
    movaps  xmm8, [rsp+1D8h+var_B8]
    movaps  xmm9, [rsp+1D8h+var_A8]
    movaps  xmm10, [rsp+1D8h+var_98]
    movaps  xmm11, [rsp+1D8h+var_88]
    movaps  xmm12, [rsp+1D8h+var_78]
    movaps  xmm13, [rsp+1D8h+var_68]
    movaps  xmm14, [rsp+1D8h+var_58]
    movaps  xmm15, [rsp+1D8h+var_48]
    add     rsp, 1A0h
    pop     rbx
    pop     rdi
    pop     rsi
    pop     r12
    pop     r13
    pop     r14
    pop     r15
    ret
main            endp

END