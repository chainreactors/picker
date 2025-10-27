---
title: OpenSSL 是什么？
url: https://www.anquanke.com/post/id/289133
source: 安全客-有思想的安全新媒体
date: 2023-06-17
fetch_date: 2025-10-04T11:44:21.756376
---

# OpenSSL 是什么？

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# OpenSSL 是什么？

阅读量**401630**

发布时间 : 2023-06-16 17:49:46

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

# <a name=”**OpenSSL 是什么？**” class=”reference-link”>**OpenSSL 是什么？**

OpenSSL 是开源的程序套件，该套件由三部分组成：

* libcrypto：具有通用功能的加密库，里面包含众多加密算法
* libssl：实现 SSL/TLS 功能
* openssl：多功能的命令行工具，可以实现加密、解密、自建 CA、创建证书、吊销证书等功能
  本文主要介绍如何使用 OpenSSL 自建 CA，生成 SSL 证书、吊销证书。

---

# <a name=”**基础概念**” class=”reference-link”>**基础概念**

**– 非对称加密：**
对称加密算法在加密和解密时，使用同一密钥。非对称加密算法需要两个密钥，即公开密钥和私有密钥，公开密钥和私有密钥是一对。用公开密钥对数据进行加密，只有用对应的私有密钥才能解密；用私有密钥对数据进行加密，只有用对应的公开密钥才能解密。因为加密和解密使用两个不同的密钥，所以这类算法叫非对称加密算法。
在非对称加密中，使用的主要算法包括 RSA、Elgamal、背包算法、Rabin、D-H、ECC（椭圆曲线加密算法）等。
非对称加密的缺点是加密和解密花费时间长、速度慢，只适合对少量数据进行加密
**– Private Key：**
证书的私钥，PEM 格式，通常使用 RSA 算法生成。在生成私钥时，可以指定密码对其进行保护
**– CSR（Certificate Signing Request，证书签名请求）：**
用于申请证书，在制作 CSR 文件时，需要使用私钥文件。CSR 文件必须由 CA 进行签名，才可形成证书（CRT）
**– CRT（数字证书）：**
数字证书是经过证书授权中心（CA）签名的、包含公开密钥拥有者信息和公开密钥的文件。数字证书的一个重要特征是 – 只在特定的时间段内有效。以数字证书为核心的加密技术可以对网络上传输的信息进行加密和解密，数字签名和签名认证，确保传输信息的机密性、完整性、不可抵赖性：

* 保密性 – 只有收件人才能阅读信息
* 认证性 – 确认信息发送者的身份
* 完整性 – 信息在传递过程中不会被篡改
* 不可抵赖性 – 发送者不能否认已发送的信息
  **数字证书的颁发过程一般为：**
* 用户首先产生自己的密钥对
* 将公共密钥和部分个人身份信息传递给证书授权中心
* 证书授权中心在核实用户身份后，将给用户颁发数字证书，其中包含用户的身份信息和公共密钥，同时还附有证书授权中心的签名信息
  **数字证书工作原理：**
* 使用接收双方约定的 HASH 算法对报文计算出固定位数的摘要。在数学上保证：只要改动报文中的任何一位，重新计算出的报文摘要值就与原先的值不相符。这样即可保证报文的不可更改性
* 使用发送者的私钥对报文摘要值进行加密，然后连同原报文一起发送给接收者，加密后的报文摘要即为数字签名
* 接收方收到数字签名后，用同样的 HASH 算法对原报文计算出报文摘要值，然后与使用发送者的公开密钥对数字签名进行解密得到的报文摘要值进行比较，如果相等，则说明报文确实来自所称的发送者
* 之所以对报文摘要进行加密，而不是对原报文进行加密，是因为 RSA 加解密非常耗时，被加密的报文越大，耗时越多
  证书的内容包括：CA 信息、公钥用户的信息、公钥、CA 的签名和有效期等。证书的格式和验证方法普遍遵循 X.509 国际标准
  **– CA（Certificate Authority，证书授权中心）：**
  CA 是负责发放和管理数字证书的权威机构，作为受信任的第三方，承担公钥体系（PKI）中公钥的合法性检查的责任。
  CA 也拥有一个证书（内含公钥）和私钥。用户通过验证 CA 的签名从而信任证书，任何人都可以得到 CA 的证书，用以验证它所签发的证书。
  如果用户想要鉴别证书的真伪，需要用 CA 的公钥对证书上的签名进行验证，一旦通过，认为证书有效
  **– 证书链（Certificate Chain）**
  证书链由两个环节组成：信任锚环节（CA 证书）和已签名证书环节。自签名的证书仅有一个环节的长度：信任锚环节就是已签名证书本身。
  证书链可以拥有任意环节的长度。在三节的证书链中，信任锚证书可以对中间证书进行签名，中间证书的拥有者可以用自己的私钥对另一个证书进行签名。
  证书链是 CA 发出的证书序列，最终以根 CA 证书结束。
  证书最初生成时，是一个自签名证书，自签名证书是签名者（Issuer）和主题（Subjet）相同的证书（即用证书自己的公钥对证书的签名进行认证）。自签名证书是证书链中的最后一个证书。
  证书链中的每个证书都需要使用链中的前一个证书的公钥进行验证，直至达到自签名的根证书
  **– CRL（Certificate Revocation List，证书吊销列表）：**
  用于指定证书发布者认为无效的证书列表。CRL 一定是被 CA 签署的，CRL 中包含被吊销的证书的序列号。
  证书具有指定的寿命，但 CA 可以通过吊销证书缩短这一寿命。CA 通过发布证书吊销列表，列出被认为不能再使用的证书的序列号。CA 可以指定证书被吊销的起始日期，也可以在证书吊销列表中加入吊销证书的理由：
* 泄漏密钥
* 泄漏 CA
* 从属关系改变
* 被取代
* 业务终止
  CA 吊销证书意味着 CA 在证书正常到期之前撤销其使用该密钥对的有关声明。在吊销的证书到期之后，CRL 中的有关条目会被删除，以缩短 CRL 列表的大小。
  在验证签名期间，应用程序可以检查 CRL，以确定给定证书和密钥对是否可信。如果不可信，应用程序可以判断吊销的理由或日期对使用有疑问的证书是否有影响。如果日期早于该证书被吊销的日期，那么该证书仍被认为有效。
  应用程序在获得 CRL 之后，可以缓存下来，在它到期之前，一直使用它。如果 CA 发布了新 CRL，那么拥有有效 CRL 的应用程序不会使用新 CRL，直到应用程序拥有的 CRL 到期为止
  **– SNI（Server Name Indication）：**
  根据 HTTPS 的工作原理，浏览器在访问 HTTPS 站点时，先与服务器建立 SSL/TLS 连接，建立连接的第一步是请求服务器的证书，而服务器在发送证书时，不知道浏览器访问的是哪个域名，所以不能根据不同的域名发送不同的证书。
  SNI 是解决一个服务器使用多个域名和证书的 SSL/TLS 扩展。它的工作原理是：在连接到服务器，建立 SSL/TLS 连接之前，客户端先发送要访问的站点的域名（HostName），这样服务器就可以根据这个域名返回合适的证书。
  目前大多数操作系统和浏览器都已经很好地支持 SNI 扩展，OpenSSL 0.9.8 已经内置这一功能

---

# 使用 OpenSSL 自建 CA

## 1. 初始化环境

$ mkdir /var/MyCA
$ cd /var/MyCA
$ mkdir certs private
$ chmod g-rwx,o-rwx private
$ echo “01” > serial
$ touch index.txt
创建完成后，目录结构如下：
$ tree .
.
├── cacert.pem # CA 证书
├── certs # 该目录下保存 CA 颁发的所有证书的副本
├── index.txt # 排序数据库，用来追踪已经颁发的证书
├── openssl.cnf # openssl 的配置文件
├── private # 保存 CA 私钥的目录
│ └── cakey.pem # CA 私钥
└── serial # 用来追踪最后一次颁发的证书的序列号

## 2 directories, 5 files

1. 创建 openssl 的配置文件 openssl.cnf
   其内容如下：
   `[ ca ]`
   `default_ca = myca`

`[ myca ]
dir = /var/MyCA
certificate = $dir/cacert.pem
database = $dir/index.txt
new_certs_dir = $dir/certs
private_key = $dir/private/cakey.pem
serial = $dir/serial`

`default_crl_days = 7
default_days = 365
default_md = sha256`

`policy = myca_policy
x509_extensions = certificate_extensions`

`[ myca_policy ]
commonName = supplied
stateOrProvinceName = supplied
countryName = supplied
emailAddress = supplied
organizationName= supplied
organizationalUnitName = optional`

`[ certificate_extensions ]
basicConstraints = CA:false`

## 3. 生成根证书（Root Certificate）

根证书是证书链的最后一个证书，也是自签名证书，即 Issuer 和 Subject 相同的证书。为生成根证书，首先向 openssl.cnf 配置文件中，增加下面的配置信息：
`[ req ]
default_bits = 2048
default_keyfile = /var/MyCA/private/cakey.pem
default_md = sha256
prompt = no
distinguished_name = root_ca_distinguished_name
x509_extensions = root_ca_extensions`
`[ root_ca_distinguished_name ]
commonName = My Test CA # 名称
stateOrProvinceName = BJ # 州或省代码
countryName = CN # 国家代码
emailAddress = test@cert.com # 邮箱地址
organizationName = Root Certification Authority`

`[ root_ca_extensions ]
basicConstraints = CA:true`
将所有必要信息写进配置文件，而不是在命令行输入，这是唯一指定 X.509v3 扩展的方式，也能让我们对如何创建根证书有清晰的把握。
为 openssl 命令指定配置文件有两种方式：

* 通过 OPENSSL\_CONF 环境变量设置
* 通过 -config 命令行选项设置

使用下面命令：
`$ openssl req -x509 -newkey rsa -out cacert.pem -outform PEM -days 365 -config /var/MyCA/openssl.cnf`
或
`$ OPENSSL_CONF=/var/MyCA/openssl.cnf openssl req -x509 -newkey rsa -out cacert.pem -outform PEM -days 365`
生成根证书（其中 -days 365 是证书的有效期）。
下面验证 CA 根证书：
$ openssl x509 -in cacert.pem -text -noout
Certificate:
Data:
Version: 3 (0x2)
Serial Number: 12778548659037981755 (0xb156864d3f00cc3b)
Signature Algorithm: md5WithRSAEncryption
Issuer: CN=Test 06 29 2016, ST=BJ, C=CN/emailAddress=jordan23nbastar@yeah.net, O=Root Certification Authority
Validity
Not Before: Jun 29 07:08:24 2016 GMT
Not After : Jun 29 07:08:24 2017 GMT
Subject: CN=Test 06 29 2016, ST=BJ, C=CN/emailAddress=jordan23nbastar@yeah.net, O=Root Certification Authority
Subject Public Key Info:
Public Key Algorithm: rsaEncryption
Public-Key: (2048 bit)
Modulus:
00:ce:2c:54:34:2b:a9:30:3e:51:20:c3:ad:21:b7:
21:9e:5c:f8:23:7a:4a:12:0f:9b:30:a8:1b:5f:10:
7e:51:01:ed:64:61:04:bb:28:82:16:05:5b:5a:e8:
5b:b6:21:73:68:eb:d7:89:db:a0:d7:ce:8a:92:f5:
8f:b3:92:ea:cd:d5:05:dd:49:a1:c4:7e:fd:1e:60:
8d:71:a4:e9:d5:35:ad:e8:c7:1a:e8:6d:52:6d:ff:
30:b1:ff:80:7d:59:4c:91:ca:67:c2:56:d6:ad:5b:
8c:58:ea:70:b3:60:97:0e:98:d5:35:46:f3:fb:ad:
57:ef:a6:55:b2:b5:13:f7:47:a8:c1:31:06:86:fc:
8a:ae:08:2e:fd:9e:ae:fe:f7:d5:35:c7:d4:45:de:
79:70:d8:c6:73:bd:47:75:90:24:d0:22:f4:f8:76:
f2:e8:2a:ef:3f:64:16:a7:8d:40:b0:94:76:f3:56:
7f:61:b4:54:c0:76:5f:33:a1:61:97:33:98:21:5c:
ec:88:95:3e:56:f1:2f:be:d9:68:cb:90:84:42:00:
24:49:c0:26:19:0f:f3:09:f7:06:1d:3b:b7:29:ac:
b3:31:ee:23:f5:58:c9:4e:de:5f:82:02:5a:50:87:
fe:72:5d:6c:4c:65:bb:59:1e:42:ab:20:42:c8:6b:
4f:f7
Exponent: 65537 (0x10001)
X509v3 extensions:
X509v3 Basic Constraints:
CA:TRUE
Signature Algorithm: md5WithRSAEncryption
af:9a:28:1b:67:44:87:d1:cc:cb:1f:e7:88:e5:74:f3:cd:d5:
ca:cc:f6:51:f9:e6:31:c2:93:c4:37:18:0a:29:29:68:b2:41:
d7:37:be:40:5d:87:04:d8:b2:03:4a:8e:fc:5e:b0:9a:bc:4c:
2d:88:69:90:63:21:34:16:e2:30:7f:76:c0:b8:64:79:e3:0f:
2e:f6:91:af:a3:fd:c2:45:40:68:5f:19:a0:e3:6e:19:d1:2a:
21:32:76:32:15:03:79:c3:da:aa:1d:1e:97:c4:de:d8:40:4a:
df:75:4f:a6:61:ed:d5:54:40:be:30:f4:0d:ac:86:2a:30:7d:
c3:28:69:e9:7b:b3:c0:19:8e:86:e7:7d:f3:55:04:ee:b1:6f:
98:f8:33:0d:16:4b:bb:d5:3d:e1:0c:31:13:1d:a6:ee:40:1f:
5f:d8:fb:b9:bc:4c:8b:4b:b9:d9:5b:b2:0d:f9:3c:84:16:90:
eb:25:33:af:cf:e5:94:94:dc:a5:64:8b:22:d0:ad:55:a7:50:
fe:e6:91:9e:98:2e:3c:03:04:2d:5a:54:97:7a:a7:c6:9f:dc:
11:86:2d:43:1d:7c:b1:48:27:c9:77:a7:3f:93:d6:ee:96:f5:
ef:27:2c:88:fd:64:30:28:fb:72:4b:cc:be:99:d4:67:00:e4:

```
     c7:21:b4:4b
```

---

使用 OpenSSL 生成证书

* Create key
  `$ openssl genrsa -out prvtkey.pem 2048 #(without password protected)`
  或
  `$ openssl genrsa -des3 -out prvtkey.pem 2048 #(password protected)`
* Create certification signing request
  `$ openssl req -new -key prvtkey.pem -out cert.csr`
  该命令使用上一步生成的密钥文件 prvtkey.pem，生成证书签名请求文件 cert.csr，接下来将使用这个文件去 CA 申请证书
* Send certificate request to Certification Auth...