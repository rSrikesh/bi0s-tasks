from pwn import *

r = remote('challenges.traboda.com',30840,level='debug') 
for i in range(3):
    r.recvline()
r.sendline(b'madrid')
for i in range(2):
    r.recvline()
r.sendline(b'vincent van gogh')
for i in range(2):
    r.recvline()
r.sendline(b'alan turing')
for i in range(19):
    r.recvline()
data = r.recv()
data1 = data.decode("utf-8")[334:]
numbers = [int(i) for i in data.split() if i.isdigit()][3:]
sum=0
for i in numbers:
    sum += i
dupp = sum/5
x = str(int(sum/5))
y = bytes(x,'utf-8')
r.sendline(b''+y)
data2 = r.recv()
numbers1 = [int(j) for j in data2.split() if j.isdigit()][0]
new_avg = dupp*(numbers1+5)
new_diff = str(int(new_avg-sum))
z = bytes(new_diff,'utf-8')
r.sendline(b''+z)
r.recv()
data3 = r.recv()
numbers2 = [int(k) for k in data3.split() if k.isdigit()]
numbers2.sort()
strn = f"{numbers2[0]} {numbers2[1]} {numbers2[2]} {numbers2[3]} {numbers2[4]} "
k = bytes(strn,'utf-8')
r.sendline(b' ' + k)
for x in range(2):
    r.recv()
#sublevel-1
r.sendline(b'bqxosnz@RBHH^oq0ms3ak2|')
for _ in range(2):
    r.recv()
#sublevel-2
r.sendline(b'pprwr laaqm')
for _ in range(2):
    r.recv()
#sublevel-3
r.sendline(b'\x01\xa5\xe9\xec\x04K$=\x92\xa48\xa02\xd0\x83\x90\x8d\xa4\xa0_\xb0\xa6"\x80q')
for _ in range(2):
    r.recv()

