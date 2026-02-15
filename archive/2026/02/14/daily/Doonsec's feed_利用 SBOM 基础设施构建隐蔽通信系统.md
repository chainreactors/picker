---
title: 利用 SBOM 基础设施构建隐蔽通信系统
url: https://mp.weixin.qq.com/s/aAI5bgiaHoS1QxXIIbO8XA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:20:00.270721
---

# 利用 SBOM 基础设施构建隐蔽通信系统

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSj7KrB4Oicevbic1qmF2IOpFzamyTVicKqCc28gDURCaKhWYibFEkrE0BmAEYWsxK8kVZewCX0Yh0zkpzvZ8fHic9CmwCYyyiavllAm0/0?wx_fmt=jpeg)

# 利用 SBOM 基础设施构建隐蔽通信系统

latedeployment
latedeployment

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://latedeployment.github.io/posts/sbom-as-messaging-system/ | latedeployment |

*本文是 Certificate Transparency 系列的第四部分。*

另请参阅前几部分：

* Part 1: Certificate Transparency 101
* Part 2: Certificate Transparency Info Leaks
* Part 3: Certificate Transparency as Communication Channel

# 引言

本文描述了一种利用存储 SBOM (`Software Bill of Materials`，软件物料清单) 证书的基础设施，通过 sigstore 数据库分发消息的方法。

# 简要流程

* 发送方生成一个口令短语：`4-karma-eagle-kettle-horizon`
* 使用由口令短语派生的密钥加密数据
* 加密数据被分块并隐藏在 RSA 公钥的模数中
* 每个分块作为签名条目上传到 `rekor`
* 接收方输入相同的口令短语，搜索 `rekor`，提取并解密数据
* **发送方与接收方之间从未建立任何直接连接**

# 背景

正如 Part 3: Certificate Transparency as Communication Channel 中所描述的，可以在证书的公钥中"隐藏"小块数据。

我们使用 `rekor`配合数据分块作为数据库来分发消息，接收方通过 `sigstore`API 读取数据，因此双方之间不存在任何直接通信。

## Sigstore 与 Rekor

Sigstore 是一个开源项目，旨在提升供应链安全性，使软件制品的签名、验证和身份认证变得简单。它允许任何人对构建制品或容器镜像进行签名，并让其他人验证该签名。

Sigstore 使用 Rekor 作为其透明度日志实现。Rekor 的运作方式与常规的 Certificate Transparency 日志类似，不同之处在于它用于软件供应链元数据 (签名、SBOM、证明等)。每当使用 Cosign 生成签名或元数据时，就会产生一个条目。这类似于 *Let's Encrypt*签发证书的过程，只不过在这里是调用者自己提供数据。

## Magic-Wormhole 模式

magic-wormhole 是一个用于在两台计算机之间安全传输文件的工具。发送方和接收方使用一次性口令 (如 `7-horse-battery`) 进行连接。双方输入口令后，wormhole 通过直连或中继将两台计算机链接起来，文件以端到端加密方式传输。

我们在这里所做的是将公钥操纵技术与 magic-wormhole 的一次性口令理念相结合，在 `rekor`透明度日志之上构建一个消息传递系统。

## Rekor 条目结构

Rekor 条目称为 `hashedrekord`，其 schema 定义在这里。

条目包含：

* 一个**制品哈希**(被签名的内容)
* 对该哈希的**签名**
* 用于签名的**公钥**

注意，公钥就在条目中，而我们从 Part 3 已经知道可以在 RSA 公钥模数中隐藏数据……

## 在公钥中隐藏数据

我们使用的公钥操纵技术与 Part 3 中描述的完全相同。核心思路很简单：RSA 公钥包含一个模数 `n = p * q`，其中 `p`和 `q`是大素数。我们可以构造一个密钥，让其中一个素数编码我们的隐藏数据：

1. **将数据嵌入素数**

   ：生成一个素数 `p`，使其低位包含我们的分块数据
2. **生成配对素数**

   ：找到另一个素数 `q`，使得 `n = p * q`构成有效的 RSA 模数
3. **接收时提取**

   ：解析公钥，获取模数 `n`，直接读取隐藏的比特位

由于 `rekor`在每个条目中存储完整的公钥，接收方可以提取模数并获取隐藏的分块数据，无需私钥。

> **深入解析**：关于该技术的详细说明，包括数学原理、代码和逐步操作指南，请参见 How to Hide Encrypted Data Inside RSA Public Keys。

# "架构"

系统的工作方式如下：

1. **发送方**

   生成一个口令短语
2. 从口令短语同时派生出加密密钥和制品哈希
3. 数据经过加密、分块后，作为多个 `rekor`条目上传
4. **接收方**

   输入口令短语，通过派生的哈希进行搜索，然后解密

注意，**制品哈希充当会合点**。发送方和接收方从口令短语独立计算出相同的哈希，这使得接收方只需知道口令短语就能在 `rekor`中找到对应的条目。

# 工作原理

## 口令短语

口令短语可以是任意内容。我选用了 `magic-wormhole`的词表生成方式，格式为 `X-wordA-wordB-wordC-wordD`，但也可以使用任何其他方式。

## 密钥与哈希的派生

从口令短语派生出两个关键要素：加密密钥 (假设使用 PBKDF2) 和制品哈希。

## 发送数据

我们基本上是加密数据，按大小分块，然后上传到 `rekor`并附带哈希值。哈希方式类似于对 `passphrase:chunk:N`进行哈希，但实际上可以使用任何你能想到的方法。

流程大致如下：

![Sender Flow](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5T1zbbIw1408PicB3Qq72MMVv9TfMXTQbM0Eu39kcBuCnuDtW9MJ6MYd25KPovPJnIibvRHXfHY9QuqDHukFic6AiaQwMPOwCyUBG7RicoZkOJrBQ/640?wx_fmt=svg&from=appmsg)

Sender Flow

## 接收数据

接收方同样使用口令短语计算哈希，然后：

1. **搜索**

   ：对序号 0、1、2……逐一计算制品哈希并搜索 `rekor`
2. **提取**

   ：从每个条目中获取 RSA 公钥，从模数中提取隐藏数据
3. **拼接**

   ：按序号排序并拼接所有分块
4. **解密**

   ：使用派生的密钥进行解密

![Receiver Flow](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4juY6R9JazlbkU5Ps2lJx7JG2tRQEFaJODx8vlgG1K5nk3NRoSdicrraythWIxblKRtZbeOXnWcR2sbneGv5dIKJnya7OE0mMBhusHNQpibazw/640?wx_fmt=svg&from=appmsg)

Receiver Flow

## 分块格式

每个分块存储 15 字节，但 RSA 要求模数为奇数 (最低位必须为 1)。为避免数据损坏，我们将数据左移 8 位：

![Chunk Format](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4lKa2Ea2ODic3LsytGicoGkguI0MX3aZ5QLLpCJgQdQLOZkGyqq3TXAt3mZ0JPLiaWHuVibcY1BsRTTrZdicictOTR7ICMOEB9ReficktqxCI5PFJWg/640?wx_fmt=svg&from=appmsg)

Chunk Format

# Rekor API

实现只需要三个 `rekor`API 调用：

## 上传条目

上传一个包含我们构造的公钥的 `hashedrekord`条目：

```
curl -X POST "https://rekor.sigstore.dev/api/v1/log/entries"\
  -H "Content-Type: application/json"\
  -d '{
    "apiVersion": "0.0.1",
    "kind": "hashedrekord",
    "spec": {
      "data": {
        "hash": {
          "algorithm": "sha256",
          "value": "abc123...derived-from-passphrase..."
        }
      },
      "signature": {
        "content": "BASE64_SIGNATURE",
        "publicKey": {
          "content": "BASE64_PUBLIC_KEY_WITH_HIDDEN_DATA"
        }
      }
    }
  }'
```

响应包含条目 UUID：

```
{
"24296fb24b8ad77a...": {
"logIndex": 123456789,
"body": "..."
  }
}
```

## 按哈希搜索

通过制品哈希 (即会合点) 查找条目：

```
curl -X POST "https://rekor.sigstore.dev/api/v1/index/retrieve"\
  -H "Content-Type: application/json"\
  -d '{"hash": "sha256:abc123...derived-from-passphrase..."}'
```

返回匹配的 UUID 列表：

```
["24296fb24b8ad77a..."]
```

## 获取条目

获取完整条目以提取公钥：

```
curl "https://rekor.sigstore.dev/api/v1/log/entries/24296fb24b8ad77a..."
```

响应体 (base64 解码后) 包含带有隐藏数据的公钥：

```
{
"apiVersion": "0.0.1",
"kind": "hashedrekord",
"spec": {
"signature": {
"publicKey": {
"content": "BASE64_PUBLIC_KEY"
      }
    }
  }
}
```

接收方解码公钥，提取 RSA 模数，获取隐藏的分块数据。

# 总结

我们有能力"搭便车"利用 `rekor`数据库，通过公钥操纵在双方之间传递消息。由于 API 是公开的，发送方和接收方都只通过 `sigstore`域名进行通信。计算并上传一条小消息 (如 *"the dog barks too loud, can it be silenced?"*) 大约需要一分钟，而读取消息则相当快。

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过