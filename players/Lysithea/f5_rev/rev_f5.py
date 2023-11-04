from pwn import *

# plan:
# 放断点，让gdb去碰，看是否能够进入对应分支？
# 后续可以patch或者hook，让puts输出当前正确匹配字符的数量，然后爆破？

# information: 
# 
# if (*(short *)(in_RAX_input? + 0x25) == *(short *)s_}_exref)
# wide char (short), total length 0x26? FLAG[0x25] == '}'




context.arch = 'amd64'

with open('no_need_for_f5/dump.a','r') as fp:
    asm_code = fp.read()

compiled:bytes = asm(asm_code)
print(compiled.hex())

with open('no_need_for_f5/dump_shellcode', 'wb') as fp:
    fp.write(compiled.ljust(0x3000, b'\x00'))




actual_code = b'\x44\x8b\x30\xbb\x01\x00\x00\x00\x41\x89\xdd\x48\x8b\x1d\x7c\x1c\x00\x00\xff\xd3\x89\x18'


print(disasm(actual_code, byte=False, offset=False))

#=================rev================
from Crypto.Util.number import inverse

final_rev = b'\x9f\x87\xd7\xba\x6d\x6b\x25\x4f\x16\xdb\xac\xdb\x0f\x50\xb1\x33\xaf\xab\x74\x19\x7a\xeb\xa6\x39\xda\x10\x92\x11\x2f\x30\xd0\x87'

buf = list(struct.unpack('B'*len(final_rev), final_rev))
print([hex(d) for d in buf])

for i in range(3,-1,-1):
    key = (i << 1) ^ 0x21
    for j in range(0x20):
        buf[j] = (buf[j] * inverse(key, 256)) % 256

print('R1', [hex(d) for d in buf])
# recover_buf = buf.copy()
# for i in range(4):
#     key = (i << 1)^0x21
#     for j in range(0x20):
#         recover_buf[j] = (recover_buf[j] * key) % 256
# print('recover',[hex(d) for d in recover_buf])


buf_short = list(struct.unpack('H'*(len(final_rev)//2),struct.pack('B'*len(final_rev), *buf)))
print([hex(d) for d in buf_short])

for i in range(0xf, -1, -1):
    buf_short[i] = buf_short[i] ^ 0xcdec

buf_int = list(struct.unpack('I'*(len(final_rev)//4),struct.pack('H'*(len(final_rev)//2), *buf_short)))
print([hex(d) for d in buf_int])

for i in range(3, -1, -1):
    key = i << 2 ^ 0xdeadbeef
    for j in range(7, -1, -1):
        buf_int[j] = (buf_int[j] * inverse(key, 2**32)) % (2**32)

buf_long = list(struct.unpack('L'*(len(final_rev)//8),struct.pack('I'*(len(final_rev)//4), *buf_int)))
print([hex(d) for d in buf_long])

for i in range(3, -1, -1):
    buf_long[i] = buf_long[i] ^ 0x7a026655fd263677

print('before final', [hex(d) for d in buf_long])

for i in range(3, -1, -1):
    for j in range(1, -1, -1):
        # mix
        # DONT IGNORE ZEXT816, SUB168
        # v3 = v1 * v4
        # v1n = v3
        # v2n = (v3>>0x40) + v1*(v4>>0x3f) + v2*v4
        v4 = (i << 4 ^ 0x55aa00ff)
        v4_inv = inverse(v4, 2**64)

        v1n = buf_long[2*j]
        v2n = buf_long[2*j+1]
        
        MUL = ((v2n * 2**64 + v1n) * inverse(v4, 2**128)) % (2**128)
        # assert MUL % v4 == 0, f"{i},{j}"
        v1 = (MUL) % (2**64)
        v2 = (MUL) // (2**64)

        buf_long[2*j] = v1
        buf_long[2*j+1] = v2
        ''
flag = 'flag{'+struct.pack('L'*4, *buf_long).decode()+'}'
os.popen(f'echo -n \'{flag}\'|xclip')
# flag{deCOmpiLeR_IS_NOT_4lW4y5_en0U9h~}


exit(0)


# ========================================

context.log_level = 'info'
for c in range(0x20, 0xff):
    test_c = c.to_bytes(1,'little')
    guess_flag = b'flag{'+ test_c*0x20 + b'}'

    conn = process(['gdb.exe','no_need_for_f5/no_need_for_F5/main_debug.exe'], )

    conn.sendlineafter(b'(gdb) ', b'r')
    conn.sendline(guess_flag)
    addr_line = conn.recvline_contains(b'in ?? ()')

    if b'364' == addr_line.split(b' ')[0][-3:]:
        print(test_c, 'ACC')
        conn.sendline(b'x/2gx $rsp+0x2c')
        stack_res = conn.recvline(keepends=False)
        stack_1ac1a8:bytes = p64(int(stack_res.split(b':')[1].strip().split(b'\t')[0], 16))
        stack_1ac, stack_1a8 = struct.unpack('ii', stack_1ac1a8)
        print(stack_1ac, stack_1a8)
        if stack_1ac != 0:
            print('================', test_c, 'catch!')


    elif b'0f2' == addr_line.split(b' ')[0][-3:]:
    # elif b'186' == addr_line.split(b' ')[0][-3:]:
        # after first segment
        # context.log_level = 'debug'
        conn.sendline(b'p/x {char[0x20]}($rsp+0xd0+5)')
        newline = conn.recvuntil(b'\r\n(gdb) ', drop=True)
        # out_str = newline[newline.index(b'\t'):][1:-1]
        print(newline)

        # conn.interactive()
        # exit(0)

    # else:
    #     print(test_c, 'DEC')
    

    conn.close()

# conn.interactive()