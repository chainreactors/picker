---
title: TLS 1.2 协议解析流程学习（一）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247498844&idx=1&sn=c078c2019741cbe1556ba52cd6c08c65&chksm=fa5229e2cd25a0f4b71a07ba434821c945be84a2078b1821e53c16b3cd719679d169bdc04754&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-12-14
fetch_date: 2025-10-04T01:28:16.932403
---

# TLS 1.2 协议解析流程学习（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRHUMYezliaPVMLJ73kIrX0Gau7iaIrciboMhiaNuicnibFaDvCvOr3mclELfmXnmUe8tCYnDt75DZ7ickwA/0?wx_fmt=jpeg)

# TLS 1.2 协议解析流程学习（一）

原创

核心基础实验室

山石网科安全技术研究院

之前学习了很多与密码学相关的理论，但其实一直忽视了密码学在实际生活，尤其是网络世界中的应用，未知攻，焉知防。但是连其本身的体制流程都不了解，又如何攻呢？于是在学习密码学这个方向上的漏洞挖掘之前，还想了解一下当前密码学的实际应用场景。那么自然是先从我们的网络通讯协议TLS入手。参考网站The Illustrated TLS 1.2 Connection，其本身已经是对 TLS 1.2 细致入微的解读了，因此笔者也只是稍添一点自己的解读，方便读者也方便自己理解其流程的背后逻辑。‍

**0****1**

**TLS 1.2 完整流程**

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRHUMYezliaPVMLJ73kIrX0GzxicZw07djlf7c1xj2iaxjiaQB0fDv5olJZsXbV76bpUUnlbQctBdibn5g/640?wx_fmt=png)

上述是从未建立过 TLS 连接的客户端与服务端完整的通讯流程。

1. 首先用户发出握手消息，请求建立连接。
2. 服务端收到消息后，首先会发送自己的证书给用户，证明自己是用户想要连接的对象。然后会在本地生成一个交换密钥，用于生成通讯密钥（对于熟悉DH密钥交换协议的读者应该不难理解），并发送给用户。
3. 用户收到服务端的证书并验证后，本地生成一个交换密钥，随后利用服务端的交换密钥计算生成通讯密钥，并用该通讯密钥加密一段验证消息，这段验证消息包含在此之前握手阶段所发送所有握手消息的哈希值。最后将用户端的交换密钥和加密后的验证消息发送给服务端。用户端握手阶段完毕，准备进行加密通讯。
4. 服务端收到用户的交换密钥后也计算生成通讯密钥并解密用户端发来的密文，随后也会用这个通讯密钥加密一段验证消息发送给用户。这段验证消息同样是在此之前握手阶段所发送所有握手消息的哈希值。服务端握手阶段完毕，准备进行加密通讯。
5. 用户收到服务端发来的验证密文，利用通讯密钥解密后，如果解密明文通过验证，那么加密通讯开始。
6. 通讯结束后，由用户端发出关闭连接的告警消息，该告警消息也是加密的。

至此，一次完整的加密通讯就完成了。

在粗略的熟悉了流程后，也许读者会有诸多疑问？是不是每一次通讯都要协商密钥呢？握手信息里都有些啥呢？我们继续往下，对 TLS 进行一个”庖丁解牛“。

### 客户端请求（Client Hello)

示例：`16 03 01 00 a5 01 00 00 a1 03 03 00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 00 00 20 cc a8 cc a9 c0 2f c0 30 c0 2b c0 2c c0 13 c0 09 c0 14 c0 0a 00 9c 00 9d 00 2f 00 35 c0 12 00 0a 01 00 00 58 00 00 00 18 00 16 00 00 13 65 78 61 6d 70 6c 65 2e 75 6c 66 68 65 69 6d 2e 6e 65 74 00 05 00 05 01 00 00 00 00 00 0a 00 0a 00 08 00 1d 00 17 00 18 00 19 00 0b 00 02 01 00 00 0d 00 12 00 10 04 01 04 03 05 01 05 03 06 01 06 03 02 01 02 03 ff 01 00 01 00 00 12 00 00`

客户端最开始的请求包括以下内容

* protocol version （协商协议版本）
* client random data (used later in the handshake) （客户端随机数）
* an optional session id to resume （可选项，已建立的会话id）
* a list of cipher suites（使用的密码学组件）
* a list of compression methods（使用的数据压缩方式）
* a list of extensions（拓展项列表）

**记录标头 Record Header** ：`16 03 01 00 a5`

0x16：握手记录的标识符

0x03 0x01：表示协议 3.1 版本，即 TLS 1.0；但我们这里不是TLS 1.2 协议么？这是为了兼容部分服务器，如果协议版本高于 TLS1.0，可能会握手失败）

0x00 0xa5：长度——接下来将有 165 字节的握手消息

**握手标头 Handshake Header**：`01 00 00 a1`

0x01：客户端请求（ Client Hello）的标识符

0x00 0x00 0xa1： 长度——接下来将有161字节的请求消息

**客户端所用协议版本：**`03 03`

0x03 0x03：TLS 1.2

**客户端随机数（32字节）：** `00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f`

0x00 0x01 0x02 … 0x1f：随机数

**会话 ID （Session ID）**：`00`

0x00：长度——接下来将用 0 个字节表示会话ID的长度（如果之前建立过连接，那么就会有一个会话ID，32字节）

**可选密码学组件 Cipher Suites：** `00 20 cc a8 cc a9 c0 2f c0 30 c0 2b c0 2c c0 13 c0 09 c0 14 c0 0a 00 9c 00 9d 00 2f 00 35 c0 12 00 0a`

0x00 0x20：接下来将用 32 个字节表示可选密码学组件

0xcc 0xa8：TLS\_ECDHE\_RSA\_WITH\_CHACHA20\_POLY1305\_SHA256

0xcc 0xa9：TLS\_ECDHE\_ECDSA\_WITH\_CHACHA20\_POLY1305\_SHA256

0xc0 0x2f：TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256

0xc0 0x30：TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384

0xc0 0x2b：TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256

0xc0 0x2c：TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384

0xc0 0x13：TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA

0xc0 0x09：TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_CBC\_SHA

0xc0 0x14：TLS\_ECDHE\_RSA\_WITH\_AES\_256\_CBC\_SHA

0xc0 0x0a：TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_CBC\_SHA

0x00 0x9c：TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256

0x00 0x9d：TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384

0x00 0x2f：TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA

0x00 0x35：TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA

0xc0 0x12：TLS\_ECDHE\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA

0x00 0x0a：TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA

**数据压缩方法：**`01 00`

0x01：长度——接下来将用 1 个字节表示数据压缩方法

0x00：不压缩，压缩的特性会削弱加密数据的安全性（参见CRIME）。因此，该功能已从未来的TLS协议中删除。

**拓展项：**

0x00 0x58：长度——接下来会使用 88 个字节表示拓展内容；

1. **服务器名称（Server Name）**

   `00 00 00 18 00 16 00 00 13 65 78 61 6d 70 6c 65 2e 75 6c 66 68 65 69 6d 2e 6e 65 74`

   客户端提供了它联系的服务器的名称，也称为SNI（服务器名称指示）。

   如果没有此扩展，HTTPS服务器将无法为单个IP地址（虚拟主机）上的多个主机名提供服务，因为在协商TLS会话并发出HTTP请求之前，它无法知道要发送哪个主机名的证书。

   0x00 0x00：Server Name 的标识符

   0x00 0x18：长度——Server Name 将占用24个字节

   0x00 0x16：长度——列表第一个（也是唯一一个）元素将占用22个字节

   0x00：列表类型是 “DNS hostname”

   0x13：长度——hostname 将占用 19 个字节

   0x65 0x78 0x61 ... 0x6e 0x65 0x74 ：具体的hostname："example.ulfheim.net"
2. **状态请求 (Status Request ):**

   `00 05 00 05 01 00 00 00 00`

   客户端允许服务器在其响应中提供OCSP信息。OCSP可用于检查证书是否已被吊销。

   但是由于服务器是根据客户端的拓展项一一进行回复的，所以客户端在这里需要发送一个该扩展的空内容，这样服务器在返回时就可以用数据填充该扩展然后进行回复。

   0x00 0x05：Status Request的标识符

   0x00 0x05：长度——Status Request 将占用 5 个字节

   0x01：证书状态类型：OCSP

   0x00：回复者ID信息的长度：这里是客户端，所以是0

   0x00：所请求的消息的拓展消息的长度：这里是客户端，所以是0
3. **（密码学体制）支持的群结构 (Supported Groups)：**

   `00 0a 00 0a 00 08 00 1d 00 17 00 18 00 19`

   客户端表示它支持4条曲线的椭圆曲线（EC）加密。此扩展最初命名为“椭圆曲线”，但已重命名为“Supported Groups”，以便与其他密码类型通用。

   0x00 0x0a：Supported Groups的标识符

   0x00 0x0a：Supported Groups的具体内容将占用 10 个字节

   0x00 0x08：长度——曲线列表将占用 8 字节

   0x00 0x1d：表示曲线 "x25519"

   0x00 0x17：表示曲线 "secp256r1"

   0x00 0x18：表示曲线 "secp384r1"

   0x00 0x19：表示曲线 "secp521r1"
4. **椭圆曲线表示形式 (EC Point Formats)：**

   `00 0b 00 02 01 00`

   在椭圆曲线（EC）加密过程中，客户端和服务器将以压缩或未压缩的形式交换所选点的信息。此扩展表示客户端只能解析来自服务器的未压缩信息。

   在TLS的下一版本中，不存在协商点的能力（而是为每条曲线预先选择一个点），因此不会发送此扩展。

   0x00 0x0b：EC points format 的标识符

   0x00 0x02：长度——EC points format 的具体内容将占用 2 个字节

   0x01：长度——所支持格式列表中元素占用 1 个字节

   0x00：表示格式：不压缩
5. **签名算法 (Signature Algorithms)：**

   `00 0d 00 12 00 10 04 01 04 03 05 01 05 03 06 01 06 03 02 01 02 03`

   随着TLS的发展，有必要支持更强的签名算法（如SHA-256），同时仍支持使用MD5和SHA1的早期实现。此扩展指示客户端能够理解哪些签名算法，并可能影响服务器向客户端发送的证书的选择。

   0x00 0x0d：Signature Algorithms 的标识符

   0x00 0x12：长度——Signature Algorithms的内容将占用18字节

   0x00 0x10：长度——支持签名列表中元素将占用 16 个字节

   0x04 0x01：RSA/PKCS1/SHA256

   0x04 0x03：ECDSA/SECP256r1/SHA256

   0x05 0x01：RSA/PKCS1/SHA384

   0x05 0x03：ECDSA/SECP384r1/SHA384

   0x06 0x01：RSA/PKCS1/SHA512

   0x06 0x03：ECDSA/SECP521r1/SHA512

   0x02 0x01：RSA/PKCS1/SHA1

   0x02 0x03：ECDSA/SHA1
6. **重新协商信息 (Renegotiation Info)：**

   `ff 01 00 01 00`

   此扩展是为了防止利用TLS重新协商的攻击类型。

   此协议的下一版本（TLS 1.3）已删除重新协商的功能，因此将来不再需要此扩展。

   0xff 0x01：Renegotiation Info 的标识符

   0x00 0x01：长度——Renegotiation Info 的内容将占用1字节

   0x00：Renegotiation Info 具体内容的长度为 0，因为这是一次新的连接
7. **签名证书时间戳 (SCT，signed certificate timestamp)：**

   `00 12 00 00`

   客户端发送一个空的扩展，这个拓展是用于服务器发送自己签名证书的时间戳，或者根据发送了扩展的客户端更改行为。

   0x00 0x12：SCT 的标识符

   0x00 0x00：长度——接下来 SCT 的内容将占用 0 字节

### 服务端回应（Server Hello）

示例：`16 03 03 00 31 02 00 00 2d 03 03 70 71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e 7f 80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f 00 c0 13 00 00 05 ff 01 00 01 00`

接下来是服务端的回应，想必也是跟客户端一一对应的，包括以下内容

* the selected protocol version（确定选择的协议版本）
* server random data (used later in the handshake)（服务端随机数）
* the session id（可选项，已建立的会话id）
* the selected cipher suite（使用的密码学组件）
* the selected compression method使用的数据压缩方式）
* a list of extensions（拓展项）

报文结构：

**记录标头 (Record Header)** ：`16 03 01 00 31`

0x16：握手记录的标识符

0x03 0x01 ：协议是3.1版本， TLS 1.0；

0x00 0x31：长度——接下来握手消息将占用49字节

握手标头 (Handshake Header)：``02 00 00 2d`

0x02：服务端握手请求 Server Hello）

0x00 0x00 0x2d：长度——接下来的请求消息将占用45字节

服务端所用协议版本 (Server Version)：`03 03`

0x03 0x03： TLS 1.2

**服务端随机数 (Server Random)** ：`70 71 72 73 74 75 76 77 78 79 7a 7b 7c 7d 7e 7f 80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f`

0x70 0x71 … 0x8f：32字节随机数

会话 ID (Session ID)：`00`

00：长度——接下来会话ID将占用 0 字节 （如果之前建立过连接，那么就会有一个会话ID，32字节）

选择的密码学组件 (Cipher Suite)：`c0 13`

0xc0 0x13：TLS\_ECDHE\_RSA\_WITH\_AES\_128\_CBC\_SHA

压缩方式 (Compression Method)：`00`

0x00：从客户端提供的选项中，选择不压缩

拓展项 (Extensions)：`00 05 ff 01 00 01 00`

0x00 0x05：长度——接下来拓展项内容占用 5 字节

**重新协商信息（Renegotiation Info）**：``ff 01 00 01 00`

0xff 0x01：Renegotiation Info 的标识符

0x00 0x01：长度——Renegotiation Info 的内容将占用1字节

0x00：长度——Renegotiation Info 具体内容的长度为 0（因为这是一次新的连接）

### 服务端证书（Server Certificate）

示例：`16 03 03 03 2f 0b 00 03 2b 00 03 28 00 03 25 30 82 03 21 30 82 02 09 a0 03 02 01 02 02 08 15 5a 92 ad c2 04 8f 90 30 0d 06 09 2a 86 48 86 f7 0d 01 01 0b 05 00 30 22 31 0b 30 09 06 03 55 04 06 13 02 55 53 31 13 30 11 0...