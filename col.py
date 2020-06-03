import struct
from pwn import *

ssh = ssh(host='pwnable.kr', user='col', password='guest', port=2222)

firstfour = 0x6c5cec8
last = 0x6c5cecc

proc = ssh.process(['/home/col/col', struct.pack('<L', firstfour) * 4 + struct.pack('<L', last)])

print(proc.recv(timeout = 0))


# by reading col.c we can see lines from 4-11 a loop for deviding the value we enter into 5 peices and the should in total == hex(0x21DD09EC)=568134124

# print 'value of hashcode 0x21DD09EC in int = 568134124 \n'
#
# print '142033531 * 4 == 568134124 is True '
#
# print ' hex (142033531) = 0x0877427b'
# '''
#
# >>> 113626824 * 4 + 113626828
# 568134120
#
# >>> hex(113626824) = '0x6c5cec8' * 4 + hex(113626828) = 0x6c5cecc
# '''
