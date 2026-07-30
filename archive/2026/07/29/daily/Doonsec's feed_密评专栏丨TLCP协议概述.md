---
title: 密评专栏丨TLCP协议概述
url: https://mp.weixin.qq.com/s/JbZo_7UIiann_145aL1LrA
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:48:07.456172
---

# 密评专栏丨TLCP协议概述

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dqQlX2VCwTxicqU9lJTXpeic96AtRswcibBIlLhreaFiaczFsSPFCyttI16IziaMXrlxFiczRUADr17XhQS6aquqjiaxB1ZMv5fIa9stxceUpaMibt8/0?wx_fmt=jpeg)

# 密评专栏丨TLCP协议概述

创信华通

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**TLCP（Transport Layer Cryptography Protocol，GB/T 38636）**是一种基于国产密码算法体系设计的安全通信协议，其主要功能包括：

* 通信双方身份认证；
* 会话密钥协商；
* 数据机密性保护；
* 数据完整性校验；
* 抗重放攻击保护。

TLCP在整体架构上继承了TLS协议成熟的设计思想，同时结合国产密码算法体系进行了适配和扩展，形成了一套符合我国商用密码应用要求的传输层安全协议。与 TLS 相比，TLCP最大的特点是支持SM2、SM3、SM4等国产密码算法，并引入双证书体系（签名证书和加密证书）以满足我国密码管理要求。

## TLCP握手过程

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dqQlX2VCwTzj49YvEpqUC92CaQFp1z2asyspFUMAjQDiamcd3CJs3vzF6sWKxLDv1aeoqAOEyhy8srjxHabWficg9gcDwVtF1E8Naqhib9OjXo/640?wx_fmt=webp&from=appmsg)

## Client Hello

客户端hello消息结构定义如下：

```
struct {
    ProtocolVersion client_version:
    Random random;
    SessionID session_id :
    CipherSuite cipher_suites(2..2^16-1) :
    CompressionMethod compression_methods(1..2^8-1);
} ClientHello;
```

Client Hello用于向服务端发起会话请求，client\_version表示客户端支持的最高TLCP协议版本（0x0101），random 为客户端产生的随机数信息，session\_id 为客户端连接使用的会话标识，cipher\_suites 为客户端所支持的密码套件。

#### TLCP与TLS版本号对比

|  | TLCP | TLS1.0 | TLS1.1 | TLS1.2 | TLS1.3 |
| --- | --- | --- | --- | --- | --- |
| 版本号 | 0x0101 | 0x0301 | 0x0302 | 0x0303 | 0x0304 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/dqQlX2VCwTxGIs4iciayC0jBUTJe7ywbFBQqbJ3zxhExMOhq00MBpCFOqbHRlStf0jCkJ0u0ef3Z1gTvWQqF52OjN7gc4icOhXQWcjKrUcTN9k/640?wx_fmt=webp&from=appmsg)

## Sever Hello

Sever Hello用于响应Client Hello的请求，server\_version 表示服务端支持的最高TLCP协议版本，random 为服务端产生的随机数，session\_id 为服务端连接使用的会话标识，cipher\_suite 为服务端从 ClientHello 中选取的一个密码套件，compression\_method 为服务端从 ClientHello 中选取的一个压缩算法。

服务端hello消息结构定义如下：

```
struct {
    ProtocolVersion server_version;
    Random random;
    SessionID session_id:
    CipherSuite cipher_suite;
    CompressionMethod compression_method
;} ServerHello;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dqQlX2VCwTxv6I7ylRDG7icvHiaFbJUicADpKJBQHq9MOw6ib7xWw49ohm1S4s2NsdzvtOM2I7bDMLm85b5HlTKQkGiaHrMhoV8G7XB2YoDYdicDI/640?wx_fmt=webp&from=appmsg)

TLCP支持的密码套件如下表所示

| 名称 | 密钥交换 | 加密 | 效验 | 值 |
| --- | --- | --- | --- | --- |
| ECDHE\_SM4\_CBC\_SM3 | ECDHE | SM4\_CBC | SM3 | {0xe0,0x11} |
| ECDHE\_SM4\_GCM\_SM3 | ECDHE | SM4\_GCM | SM3 | {0xe0,0x51} |
| ECC\_SM4\_CBC\_SM3 | ECC | SM4\_CBC | SM3 | {0xe0,0x13} |
| ECC\_SM4\_GCM\_SM3 | ECC | SM4\_GCM | SM3 | {0xe0,0x53} |
| IBSDH\_SM4\_CBC\_SM3 | IBSDH | SM4\_CBC | SM3 | {0xe0,0x15} |
| IBSDH\_SM4\_GCM\_SM3 | IBSDH | SM4\_GCM | SM3 | {0xe0,0x55} |
| IBC\_SM4\_CBC\_SM3 | IBC | SM4\_CBC | SM3 | {0xe0,0x17} |
| IBC\_SM4\_GCM\_SM3 | IBC | SM4\_GCM | SM3 | {0xe0,0x57} |
| RSA\_SM4\_CBC\_SM3 | RSA | SM4\_CBC | SM3 | {0xe0,0x19} |
| RSA\_SM4\_GCM\_SM3 | RSA | SM4\_GCM | SM3 | {0xe0,0x59} |
| RSA\_SM4\_CBC\_SHA256 | RSA | SM4\_CBC | SHA256 | {0xe0,0x1c} |
| RSA\_SM4\_GCM\_SHA256 | RSA | SM4\_GCM | SHA256 | {0xe0,0x5a} |

## Server Certificate / Client Certificate

TLCP采用双证书体系，Certificate消息通常包含：

1. 签名证书（Signature Certificate）
2. 加密证书（Encryption Certificate）

签名证书用于握手签名验证；加密证书用于预主密钥加密

对于证书消息结构如下：

```
opaque ASN.1Cert(1..2^24-1>:
struct {
ASN.1Cert certificate<0..2^24-1>:
} Certificate:
Certificate;
```

IBC标识及公共参数结构：

```
opaque ASN.1IBCParam(1..2²-1>;struct {
 opaque ibc_id(1..21-1);
 ASN.1IBCParam ibc_parameter;
} Certificate;
其中：
a) ibc_id     服务端标识。
b) ibc_parameter    IBC公共参数，遵循ASN.1编码。
```

密钥交换算法和证书密钥交换的关系如下表所示

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dqQlX2VCwTwekadubpcs4MPfSk2hnToko3kjRWriaFH9FCcMPiaUMlOQ679F1mBtS5afMgc5SsATfQ3RBicJnSJM0IyeicCfVLXJiakEaibuwibdgc/640?wx_fmt=webp&from=appmsg)

## Server Key Exchange

该消息传输信息用于客户端计算产生 48 字节的预主密钥

消息结构体如下

```
enum {
    ECDHE,
    ECC,
    IBSDH,
    IBC,
    RSA
} KeyExchangeAlgorithm;

struct {
    select (KeyExchangeAlgorithm) {

        case ECDHE:
            ServerECDHEParams params;
            digitally-signed struct {
                opaque client_random[32];
                opaque server_random[32];
                ServerECDHEParams params;
            } signed_params;

        case ECC:
            digitally-signed struct {
                opaque client_random[32];
                opaque server_random[32];
                opaque ASN.1Cert<1..2^24-1>;
            } signed_params;

        case IBSDH:
            ServerIBSDHParams params;
            digitally-signed struct {
                opaque client_random[32];
                opaque server_random[32];
                ServerIBSDHParams params;
            } signed_params;

        case IBC:
            ServerIBCParams params;
            digitally-signed struct {
                opaque client_random[32];
                opaque server_random[32];
                ServerIBCParams params;
                opaque IBCEncryptionKey[1024];
            } signed_params;

        case RSA:
            digitally-signed struct {
                opaque client_random[32];
                opaque server_random[32];
                opaque ASN.1Cert<1..2^24-1>;
            } signed_params;
    };
} ServerKeyExchange;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dqQlX2VCwTxy210xiaCNE0e9anEcYnj26aAf8we85YKTs7QDe5UEIK1eLSuYVibw3wpXZcWwysOeAibMYUftIA0dfcWR3QhHwVKt5eEbRb19pk/640?wx_fmt=webp&from=appmsg)

## Certificate Request

如果服务端要求认证客户端，则发送此消息，用于让客户端发送自己的证书。

其中结构体如下：

```
struct {
    ClientCertificateType certificate_types<1..2^8-1>;
    DistinguishedName certificate_authorities<0..2^16-1>;
} CertificateRequest;
```

certificate\_authorities：如果ClientCertificateType是ibc\_params，本字段的内容是IBC密管理中心的信任域名列表。否则是服务端信任的CA的证书DN列表，包括根CA或者二级CA的DN。

## Server Hello Done

用于表示握手过程的 Hello 消息阶段完成

服务端hello完成消息结构如下：

```
struct { } ServerHelloDone;
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/dqQlX2VCwTwGgnIf8kBkAsictA1EabGtgTUnfUianzLQaHtH3gCiaA1GIyRibhqf9QR7XFRAqC6yFtjEpKzOHDkUzFrY6WyolKmFBaOBvyXdfYY/640?wx_fmt=webp&from=appmsg)

## Client Key Exchange

该消息用于传输预主密钥或者传输计算预主密钥所需的客户端密钥交换参数

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dqQlX2VCwTwMe2w7tKbnibXJnbO3O1W1zdDhlgKBiarT13AY57jcOUUAYiaRdxvzHTVicljGLZkSmy4ToibibntuLmxU9rk4Cn7r2Nw2CbKV9llEk/640?wx_fmt=webp&from=appmsg)

消息结构体如下：

```
struct {
select（KeyExchangeAlgorithm）{
 case ECDHE:
  opaque ClientECDHEParams(1..2^16-1):
 case IBSDH :
  opaque ClientIBSDHParams(1..2^16-1);
 case ECC:
  opaque ECCEncryptedPreMasterSecret(0..2^16–1) ;
 case IBC:
  opaque IBCEncryptedPreMasterSecret(0..2^16-1):
 case RSA:
  Opaque RSAEncryptedPreMasterSecret (0..2^16–1) :
 } exchange_keys;
} ClientKeyExchange;
```

## Certificate Verify

当客户端发送 `Client Certificate` 消息，并且该证书具有签名能力时，客户端需要发送 `CertificateVerify` 消息

该消息用于证明客户端确实持有其证书对应的签名私钥，从而完成客户端身份认证。客户端使用自己的签名私钥对此前所有握手消息的摘要值进行签名，服务端收到后使用客户端证书中的公钥进行验证。

证书校验消息的数据结构如下：

```
struct {
 Signature signature;
} CertificateVerify;
```

Signature 的结构如下：

```
enum { rsa_sha256,rsa_sm3,
        ecc_sm3,
        ibs_sm3  SignatureAlgorithm;
struct {
    select（SignatureAlgorithm)
    {
        case rsa_sha256:
         digitally-signed struct {
         opaque sha256_hash[20];
        };
        case rsa_sm3:
         digitally-signed struct {
          opaque sm3_hash[32];
         };
         case ecc_sm3://当ECC为SM2算法时，用这个套件
          digitally-signed struct {
           opaque sm3_hash[32];
        case ibs_sm3:
         digitally-signed struct {
         opaque sm3_hash[32];
        };
} Signature;
```

## Change Cipher Spec

`Change Cipher Spec` 消息用于通知通信对端，

其消息内容固定为：

```
struct {
opaque type = 1;
} ChangeCipherSpec;
```

## Finished

`Finished` 消息用于验证握手过程的完整性和双方是否成功协商出了相同的主密钥（Master Secret）。

握手结束消息数据结构如下：

```
struct {
opaque verify_data[12];
} Finished;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dqQlX2VCwTxalDl1rE542kMAiacwdXibMMQdSoG1FibggFx3aEHcKdr9WXDPvCf0ibnTpbClcle2de6Z2Ug1IFxLFjbvvlG8lMH2SZlZ8qabvOE/640?wx_fmt=webp&from=appmsg)

# 密钥交换协议：

**ECDHE**:

* 工作模式为双向身份认证
* 基于SM2密钥交换协议详见GT/T GBT 35276-2017 9.6
* 要求服务端具有签名密钥、签名证书、加密密钥、加密证书。
* 要求客户端具有身份认证密钥、认证证书、加密密钥、加密证书。
* 密钥交换协议：

+ 通信双方需要相互交换数字证书。
+ 通双方使用加密密钥生成并交换EC临时公钥。
+ 根据GB/T 35276-2017 9.6 计算共享密钥，作为预主密钥。

* 特别的服务端密钥...