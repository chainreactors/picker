---
title: 密码学 ｜TLS 1.2 协议（二）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247499452&idx=1&sn=30eb25a81e332ad09d68358f0fd09319&chksm=fa522b02cd25a214e4af33e7d7b20512e0327d21acbe5e9ae68b870ae3e3a9e6b938c780e516&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-01-11
fetch_date: 2025-10-04T03:32:49.661159
---

# 密码学 ｜TLS 1.2 协议（二）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSzic6jwquTKKMiaib0ZJBK3PN8PXc4jzH3pxRfFm0iaY2zpUI7jbKgwJgZ8J7voH2097Mnpng061djkQ/0?wx_fmt=jpeg)

# 密码学 ｜TLS 1.2 协议（二）

V

山石网科安全技术研究院

上一篇我们分析了下 TLS 1.2 协议的各个细节，这一篇我们将使用 wireshark 对一次连接（访问 www.baidu.com ）进行抓包并尝试分析。

这里我根据 client hello 包确定了baidu.com 的ip 是 220.181.33.11，于是设定过滤规则 tls，得到

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTmTf2T1CwiccJKoguMqojdqSqBswDbBLR8IBSAlPysQ6gXWF2YNvPyBVicFWQ1MjWTefjtKIfX71pQ/640?wx_fmt=png)

**客户端请求**

**（Client hello）**

报文：

```
16·0301·0200·01·0001fc·0303·614380d83e548c46492a96347a353e8efd4f43f114afdf7a41f01423ebe65245·20·f12bbc673f3b62d31f63366790d12e1c13a043d829cfa98bfc9487dbd27e574f·0020·8a8a130113021303c02bc02fc02cc030cca9cca8c013c014009c009d002f0035·01·00·0193·0a0a·00·00·0000·0011·000f·00·000c·686d2e62616964752e636f6d·0017·0000·ff01·0001·00·000a·000a·0008·6a6a001d00170018·000b·0002·01·00·0023·0000·0010·000e·000c·02·6832·08·687474702f312e31·0005·0005·01·0000·0000·000d·0012·0010·04030804040105030805050108060601·0012·0000·0033·002b·0029·6a6a·0001·00·001d·0020·1d2d75215d350b351a289937a974c8b1a1f8430b2c4516a9e03329528cefba5f·002d·0002·01·01·002b·0007·06·5a5a·0304·0303·001b·0003·02·0002·4469·0005·0003026832·caca·0001·00·0015·00cb·0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

16：Handshake

0301：TLS 1.0

0200：length

01：Client Hello

0001fc：length

0303：TLS 1.2

614380d8（GMT Unix Time) 3e548c46492a96347a353e8efd4f43f114afdf7a41f01423ebe65245（Random Bytes）：Random Number

20：length of session ID

f12bbc673f3b62d31f63366790d12e1c13a043d829cfa98bfc9487dbd27e574f：session ID

0020：length of Cipher Suites

8a8a130113021303c02bc02fc02cc030cca9cca8c013c014009c009d002f0035：list of Cipher Suites

01：length of Compression Methods

00：null

0193：length of  Extensio

0a0a：Reserved

00：length

0000：server\_name

0011：length

000f：length

00：host\_name

000c：length of host\_name

686d2e62616964752e636f6d：hm.baidu.com

0017：master\_secret

0000：length of master\_secret

ff01：renegotiation\_info

0001：length of renegotiation\_info

00:：length of renegotiation\_info extension

000a：supported\_groups

000a：length of supperted groups

0008：length of supperted groups list

6a6a001d00170018：4 groups

000b：ec\_point\_formats

0002：length of ec\_point\_formats

01：length of formats

00：uncompressed

0023：session\_ticket

0000：length of session\_ticket

0010：application\_layer\_protocol\_negotiation

000e：length of application\_layer\_protocol\_negotiation

000c：length of ALPN Protocol

02：length of  ALPN string

6832：h2

08：length of  ALPN string

687474702f31：http/1.1

0005：status\_request

0005：length of status\_request

01：Certificate Status Type：OSCP

0000：length of Resonder ID list

0000：length of Request Extension

000d：signature\_algorithms

0012：length of signature\_algorithms

0010：length of Signature Hash algorithms

04030804040105030805050108060601：8  algorithms

0012：signed\_certificate\_timestamp

0000：length of signed\_certificate\_timestamp

0033：key\_share

002b：length of key\_share

0029：length of Client Key Share

6a6a：Reserved

0001：length of Key Exchange

00：Key Exchange

001d：x25519

0020：length of Key Exchange

1d2d75215d350b351a289937a974c8b1a1f8430b2c4516a9e03329528cefba5f：Key Exchange

002d：psk\_key\_exchange\_modes

0002：length of psk\_key\_exchange\_modes

01：length of PSK key Exchange Modes

01：PSK with (EC)DHE key estabishment

002b：supported\_versions

0007：length of supported\_versions

06：lenth of supported versions

5a5a：Unknown

0304：TLS1.3

0303：TLS1.2

001b：compress\_certificate

0003：length of compress\_certificate

0002：length of Algorithms

0002：brotli

4469：Unknown

0005：length of Unknown‘s data

0003026832：data

caca：Reserved

0001：length of Reserved’s data

00：data

0015：padding

00cb：length of padding

00…..000：padding

我们可以看到，Clinet Hello 请求连接的服务域名是 hm.baidu.com，并且之前是连接过的，所以携带了32字节的 Session ID；并且32字节随机数也不是完全随机的，前面4个字节代表 GMT UNIX 时间戳。

**服务端回应**

**（Server hello）**

```
16·0303·004a·02·000046·0303·6386f0d1954bb3362f237169b4c06155e3a3397487790c08ba7e9420c0edaead·00·c02f·00·001e·0023·0000·ff01·0001·00·0010·000b·0009·08·687474702f312e31·000b·0002·01·00
```

16：Handshake

0303：TLS 1.2

004a：length of Handshake

02：Server Hello

000046：length of Server Hello

0303：TLS 1.2

6386f0d1（GMT Unix Time）954bb3362f237169b4c06155e3a3397487790c08ba7e9420c0edaead（random bytes）：Random

00：length of session ID

c02f：Cipher Suite: TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256 (0xc02f)

00：Compression Method: null (0)

001e：length of Extensions

0023：session\_ticket

0000：length of session\_ticket

ff01：renegotiation\_info

0001：length of renegotiation\_info

00：length of Renegotiation info extension

0010：application\_layer\_protocol\_negotiation

000b：length of application\_layer\_protocol\_negotiation

0009：length of ALPN Protocol

08：length of  ALPN string

687474702f31：http/1.1

000b：ec\_point\_formats

0002：length of ec\_point\_formats

01：length of formats

00：uncompressed

服务端发送响应的回应包，但是注意到这里服务端的回应是不带Session ID的。然后，服务端将会返回一个包含 **服务端证书、服务端发送交换密钥、服务端回复完毕** 的包。

**服务端证书**

**（Server Certificate）**

具体证书的格式这里我们暂不细究，应该也许会开另一篇文章专门分析。

证书的报文结构：

16：Handshake

0303：TLS 1.2

12ca：length of Handshake

0b：Certificate

0012c6：length of Server Hello

00…70：Specific data of Certificate

**服务端发送交换密钥**

**（Server Key Exchange）**

在服务端发送交换密钥之前，服务端本地肯定是要先生成交换密钥的，不过这个过程肯定是没办法在抓到的数据包中体现的。

```
16·0303·012c·0c·000128·03·001d·20·84890a5d3dd07f92a099e20e5990b8512803f84a90409e7c2802d9509e3f3d67·0804·0100·8d8765a013acab1283f5bd691120c89012432abc9e1f169187bd0a3bf4af50b4bfc44f5d26e7ce17d3b943297c5fb8aa6435515a43ce0de426e5b4bf9d86263a023b0f710fd74f2962dbf449fc46872560f4c9b0dcd2c60bf616cac071f2a48dd69ceb42810556403f1447b9a488d0e4f96d98174f5f4d6dc5df9d9b4ddae2eec67155e277a3fe8627ac790d7fb035c0e8d28f932ee3806c72ddaf7e05fa87f64b863036012e78ec6191c385874dafe86b84a53e253d8874b59619296d865c2927edbea3cd2260da84129813f30408fca64e71e37a82a86407626483933b40c2a00d70abdf56daf41cb9938ab646861659832de8861d511942d3eb7b55bd2049
```

报文结构：

16：Handshake

0303：TLS 1.2

012c：length of Handshake

0c：Server Key Exchange

000128：length of Server Key Exchange

03：named\_curve

001d：曲线x25519

20：length of publickey

84890a5d3dd07f92a099e20e5990b8512803f84a90409e7c2802d9509e3f3d67：publickey

0804：signature algorithm-rsa\_pss\_rsae\_sha256

0100：length of signature algorithm

8d…..49：signature

总共报文就只有300字节，光签名就占了256字节。

**服务端回复完毕**

**（Server Hello Done）**

```
16·0303·0004·0e·000000
```

报文结构：

16：Handshake

0303：TLS 1.2

0004：length of Handshake

0e：Server Hello Done

000000：length of Server Hello Done

下一个包一次性包含三段报 文，分别是 客户端发送交换密钥；客户端启用加密通讯；握手完毕并发送一段用于验证的加密握手信息

**客户端发送交换密钥**

**（Client Key Exchange）**

客户端发送交换密钥的报文格式同服务端发送交换密钥

```
16·0303·0025·10·000021·20·7f59d0486f3e6d18824128937a23dcd332c3d0ecab36c82adbc8dbbc40074d22
```

报文结构：

16：Handshake

0303：TLS 1.2

0025：length of Handshake

10: Client Key Exchange

000021：length of Client Key Exchange

20：length of Publickey

7f59d0486f3e6d18824128937a23dcd332c3d0ecab36c82adbc8dbbc40074d22：Publickey

**客户端启用加密通讯**

**（Client Change Cipher Spec）**

客户端提示服务端，接下来的报文将使用通讯密钥进行加密

14·0303·0001·01

报文结构：

14：Change Cipher Spec

0303：TLS 1.2

0001：length of Change Cipher Spec

01：Cipher Spec Message

**加密的握手信息**

**（Encrypted Handshake Message）**

```
16·0303·0028·0000000000000000·c96711c338789358217e5806a5862f53d6a8e6307a6ff6f6bbc0ac0a49f3a2f4
```

报文结构：

16：Handshake

0303：TLS 1.2

0028：length of Handshake·

0000000000000000c96711c338789358217e5806a5862f53d6a8e6307a6ff6f6bbc0ac0a49f3a2f4：加密消息的密文，其中，前十六字节是IV向量，这里是十六个字节的0向量。正确解密应该会得到与之前所有握手消息的 SHA256 相关的一段验证信息。

随后客户端会发送正常的用于通讯的但被加密的消息

服务端也会有相应的动作，下一份服务端发送的包...