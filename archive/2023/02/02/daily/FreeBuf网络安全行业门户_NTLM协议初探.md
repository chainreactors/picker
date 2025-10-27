---
title: NTLM协议初探
url: https://www.freebuf.com/articles/network/355594.html
source: FreeBuf网络安全行业门户
date: 2023-02-02
fetch_date: 2025-10-04T05:29:23.298177
---

# NTLM协议初探

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

NTLM协议初探

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

NTLM协议初探

2023-02-01 10:02:22

所属地 重庆

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。（本文仅用于交流学习）

## 简介

NTLM使用在Windows NT和Windows 2000 Server（or later）工作组环境中（Kerberos用在域模式下）。
NTLM即可用于工作组也可用于域环境进行身份验证，也可以为上层协议提供身份验证（SMB、HTTP、LDAP、MSSQL、SMTP等）
NTLM采用一种质询/应答（Challenge/Response）消息交换模式。
NTLM协议具有NTLM v1、NTLM v2两个版本，但是目前使用最多的是NTLM v2。
Windows的系统密码Hash组成

```
#用户名:RID:LM Hash:NTLM Hash
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

## LM Hash

LM Hash的本质是DES加密，但是现在基本都已经没有使用LM Hash（从Windows Server 2008、Windows Vista开始就默认禁止使用），
可以将LM Hash填0(LM hash可以为任意值)，即

```
00000000000000000000000000000000:NTLM Hash
```

#### LM Hash的生成

* 用户的密码被限制为最多14个字符；
* 将用户的口令全部转换为大写；
* 将转换为大写的明文密码转换为16进制字符串，不足14Byte（长度28）将会用0来再后面补全。
* 密码的16进制字符串被分成大小7Byte的两组，每部分转换成比特（即二进制，长度为7 \* 8 = 56b），长度不足使用0在左边补齐长度；
* 然后将上面的每组中再按7bit分为一组，一共8组，每组末尾加一个0（8位），然后分别将其转换为16进制；
* 上步骤得到的8Byte二组，分别作为DES加密的key对"KGS!@#$%"进行加密。
* 将二组DES加密后的编码拼接，得到最终LM HASH值。

我们利用python编写实现

#### 代码实现

```
import binascii
from pyDes import *

def DesEncrypt(str, Des_Key):
    Iv = None  # 偏移量
    k = des(Des_Key, ECB, Iv, pad=None)
    EncryptStr = k.encrypt(str)

    return binascii.b2a_hex(EncryptStr)

def LM_Encode(Password):
    #转换为大写
    Password = Password.upper()
    #验证密码长度是否超过14位
    if(len(Password) > 14):
        print("密码长度错误")
        exit(1)
    # 转换为16进制字符串，不足用0补全
    Hex_Password = bytes(Password,'UTF-8').hex()
    if(len(Hex_Password) != 28):
        Hex_Password = Hex_Password + "0" * (28 - len(Hex_Password))
    #分为两组（每组7B），分别转换为二进制（每组长度56）
    bite = ""
    i = 0
    j = 2
    while j <= len(Hex_Password):
        state_16 = Hex_Password[i:j]
        state_10 = int(state_16, 16)
        state_2 = '{:08b}'.format(state_10)
        bite = bite + state_2
        i += 2
        j += 2
    #分为两组
    bite_1 = bite[0:56]
    bite_2 = bite[56:]
    #分为8组（每组长度为7），末尾加0，再转换为16进制
    Hex_1 = ""
    Hex_2 = ""
    i = 0
    j = 7
    while j <= len(bite_1):
        Hex = bite_1[i:j] + "0"
        HHex = bite_2[i:j] + "0"
        H1 = hex(int(Hex, 2)).replace("0x", "")
        H2 = hex(int(HHex, 2)).replace("0x", "")
        #不足两位前面补0
        if len(H1) != 2:
            H1 = "0" + H1
            Hex_1 += H1
        else:
            Hex_1 += H1
        if len(H2) != 2:
            H2 = "0" + H2
            Hex_2 += H2
        else:
            Hex_2 += H2
        i += 7
        j += 7
    if(len(Hex_1) < 16 or len(Hex_2) < 16):
        Hex_1 = Hex_1 + "0" * (16 - len(Hex_1))
        Hex_2 = Hex_2 + "0" * (16 - len(Hex_2))

    #使用作为密钥使用DES对KGS!@#$%进行加密
    Hex_1 = binascii.a2b_hex(Hex_1)
    Hex_2 = binascii.a2b_hex(Hex_2)
    LM_1 = DesEncrypt("KGS!@#$%", Hex_1).decode()
    LM_2 = DesEncrypt("KGS!@#$%", Hex_2).decode()
    #得到LM-Hash
    LM = (LM_1 + LM_2).upper()

    print("LM Hash is:{}".format(LM))

if __name__ == '__main__':
    Password = input("输入明文密码:")
    LM_Encode(Password)
```

![image](https://image.3001.net/images/20230118/1674022212_63c78d4462151fb48678e.png!small)

## NTLM Hash

由于LM Hash加密算法的不安全性，微软后面推出NTLM Hash。其与LM Hash有着不同的加密算法

#### NTLM Hash的生成

* 将明文密码转换为十六进制
* 将ASCII编码的十六进制编码转换为Unicode编码
* 对Unicode编码的字符串进行MD4加密

#### 代码实现

```
import binascii
import hashlib

Password = input("输入密码:")
NTLM = hashlib.new("md4", Password.encode("utf-16le")).digest()
NTLM = binascii.hexlify(NTLM).decode().upper()
print("NTLM Hash is:{}".format(NTLM))
```

![image](https://image.3001.net/images/20230118/1674022271_63c78d7f5290b67e78b19.png!small)

存储位置

```
C:\Windows\NTDS\NTDS.dit			#ntds.dit文件位置
C:\Windows\System32\config\SYSTEM	#system文件位置
C:\Windows\System32\config\SAM		#sam文件位置
```

## Net-NTLM Hash

Net-NTLM Hash用于网络身份认证（NTLM认证），现在主要有两个版本Net-NTLM v1、Net-NTLM v2，但是主要使用Net-NTLM v2

#### 组成

```
#Net-NTLM Hash v1
username:hostname:LM responce:NTLM responce:challenge
#Net-NTLM Hash v2
username:domain:challenge:HMAC-MD5:blob
```

一般获取到Net-NTLM Hash之后，要么利用中继或者破解，无法用于PTH（详细的看后面）

## NTLM认证

NTLM认证可以分为本地认证、网络认证两种（工作组、域环境）

本地认证

* 主要就是与计算机本地的SAM文件中的值进行匹配验证

网络认证大致步骤

* 协商：主要用于确认双方协议版本。
* 质询：就是挑战（Chalenge）/响应（Response）认证机制起作用的范畴。
* 验证：验证主要是在质询完成后，验证结果。

其又分为工作组和域环境下的认证，其实差别不大，只是域环境下的认证需要域控的协助

#### 本地认证

在我们登录自己的电脑时，我们会被要求输入明文密码，然后Winlogon.exe 接收输入后，会将密码交给lsass进程，然后将其转换为NTLM Hash，

与SAM文件中的值进行比较，如果一致则认证成功。

#### 工作组

![image](https://image.3001.net/images/20230118/1674022334_63c78dbe37b9be1403980.png!small)

* 当客户端想要访问某个服务时，此时客户端会在本地缓存一份服务密码的NTLM Hash,然后向服务器发送Negotiate消息。（消息中包含明文表示的用户名与其他协商信息）
* 服务器收到客户端发送的消息后，先判断本地是否有消息中的用户名，如果存在就会提供自己支持的服务内容，回复Challenge消息。（消息中包含一个由服务端随机生成的16位Challenge，服务端也会缓存此Challenge）
* 客户端收到消息后，使用1中本地缓存的NTLM Hash对Challenge进行加密生成Responce，然后将Responce、用户名、Challenge组合得到Net-NTLM Hash，然后发送给服务端。
* 服务端收到消息（Net-NTLM Hash）后，用本地自己密码的NTLM Hash对第二步中本地缓存的Challenge进行加密，然后与收到的Responce进行比较，如果一致就认证成功。

##### 抓包分析

![image](https://image.3001.net/images/20230118/1674022360_63c78dd81c3db7a0a2e9b.png!small)

```
net use \\10.10.10.132\ipc$ /user:administrator 123456Asd
```

主要就是这几个包，前面四个包是协商，我们具体看后面四个包
![image](https://image.3001.net/images/20230118/1674022395_63c78dfb00890ef51b64f.png!small)
Win10向Win7发送信息（主要也是一些响应信息）
![image](https://image.3001.net/images/20230118/1674022418_63c78e1225ceab99c2e86.png!small)
第二步就是Win7向Win10发送响应信息，主要就是Win7随机生成的16位Challenge

NTLM Server Challenge: 6d0601092985aac9
![image](https://image.3001.net/images/20230118/1674022436_63c78e24b4b2b02b28ac9.png!small)
第三步就是Win10收到后，使用1中本地缓存的NTLM Hash对Challenge进行加密生成Responce，然后将Responce、用户名、Challenge组合得到Net-NTLM Hash，然后发送给Win7

我们主要关注以下信息
NTLMv2 Response：他是由NTProofStr + blob组成；
NTProofStr（HMAC-MD5） ：主要用于数据签名的Hash值，保证数据的的完整性；
Session Key：主要是用来协商加密的密钥；
MIC：主要防止数据包被中途篡改；
Domain name、User name、Host name：请求主机的主机名、认证的用户等信息。
![image](https://image.3001.net/images/20230118/1674022469_63c78e453a3e1807718a1.png!small)
最后Win7收到Win10发送来的数据包后，本地自己密码的NTLM Hash对第二步中本地缓存的Challenge进行加密，然后与收到的Responce进行比较，如果一致就认证成功。

我们主要来看看Net-NTLM Hash v2的组成

```
#Net-NTLM Hash v2
username:domain:challenge:HMAC-MD5:blob
```

从上面的抓包我们可以很清晰的拼接出来

```
administrator:DESKTOP-05ROOG9:6d0601092985aac9:bbbfdf054d2e1a45d41566944bf47e33:0101000000000000a0db96074827d90177a9aa1ff20eae4a0000000002000c004800410043004b004d00590001001e00570049004e002d0046004e004c004f004d00540051004400480055005100040014006800610063006b006d0079002e0063006f006d0003003400570049004e002d0046004e004c004f004d005400510044004800550051002e006800610063006b006d0079002e0063006f006d00050014006800610063006b006d0079002e0063006f006d0007000800a0db96074827d901060004000200000008003000300000000000000000000000003000000f6f6fb3536830e194aaa79d5b6a473a4f4f73b9b8a1d28f950ceff9c1acd5d30a001000000000000000000000000000000000000900220063006900660073002f00310030002e00310030002e00310030002e00310033003200000000000000000000000000
```

#### 域环境

![image](https://image.3001.net/images/20230118/1674022513_63c78e71d4fccecf8e1b9.png!small)
由于域环境中密码是存储在域控中的NTDS.dit中的，因此还需要域控进行认证

* 当客户端想要访问某个服务时，此时客户端会在本地缓存一份服务密码的NTLM Hash,然后向服务器发送Negotiate消息。（消息中包含明文表示的用户名与其他协商信息）
* 服务器收到客户端发送的消息后，先判断本地是否有消息中的用户名，如果存在就会提供自己支持的服务内容，回复Chall...