---
title: 证书透明度机制详解
url: https://mp.weixin.qq.com/s/tARv6BZ9P-PhtolxFpU1EA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:47.003602
---

# 证书透明度机制详解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSgeMYj2aM3POXZDJwl5krjDDmFpo5t1EBKlEsYNJAVDwtLB39DwhBBPgeI8Y9v8Wwc9LFzfeiacsOOU3U2IIv5EElQsKusv8RXc/0?wx_fmt=jpeg)

# 证书透明度机制详解

latedeployment
latedeployment

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://latedeployment.github.io/posts/certificate-transparency-101/ | latedeployment |

*本文是 Certificate Transparency 系列的第一部分*。

Certificate Transparency (CT) 是一个公开的、仅追加的 TLS 证书日志系统。它的设计目的是让证书签发过程变得可观察，从而能够快速、独立地检测错误签发行为。CT 不再仅仅依赖信任，而是让任何人都可以审计某个域名被签发了哪些证书，以及这些证书何时出现在公开日志中。

## CT 解决的问题

在 CT 出现之前，证书生态系统存在一个根本性的信任问题：你必须相信证书颁发机构 (CA) 在正确地履行职责，但却没有简便的方法来验证这一点。如果某个 CA 签发了一张欺诈性证书——例如由于系统被入侵或操作失误——通常只有在损害已经造成之后才会被发现。

参见 *DigiNotar\_、\_Comodo*和 *CCNIC*事件。

在所有这些案例中，检测都很缓慢，基本上只能靠运气。

CT 通过公开证书签发过程来解决这个问题。每张公开受信任的证书在被浏览器接受之前，都必须被记录到公开的、可审计的日志中。

因此，有了 CT：

* 域名所有者可以监控日志中是否出现意料之外的证书。
* 研究人员可以分析整个生态系统中的签发模式。
* 错误签发行为可以被直接发现。

## 什么是 Certificate Transparency

Certificate Transparency 是一组公开的日志，这些日志接收证书并返回密码学证明，以证实证书已被记录。

这些日志具有以下特性：

* **仅追加**

  ：一旦证书被记录，它将永久保留在日志中。条目不能被修改或删除。
* **公开可审计**

  ：任何人都可以验证日志的一致性和包含证明。读取日志内容无需身份验证。
* **由独立组织运营**

  ，以降低单点故障风险。没有任何单一实体控制所有日志。
* **可密码学验证**

  ：证明基于 Merkle 树构建，客户端无需信任日志运营者即可验证其声明。

该系统还涉及几个关键角色：

* **证书颁发机构 (CA)**

  在签发流程中将证书 (或预证书) 提交到 CT 日志。
* **日志**

  返回签名证书时间戳 (SCT)——这是一个签名承诺，表示该证书将被纳入日志中。
* **浏览器**

  要求公开受信任的证书必须携带 SCT，并执行 CT 策略。
* **监控者**

  监视日志中是否存在可疑或意外的签发行为，并向域名所有者发出警报。
* **审计者**

  验证日志行为是否正确，确保没有遗漏条目。

## 理解 Merkle 树

CT 日志基于 Merkle 树构建，这是一种用于密码学哈希的数据结构。

### 什么是 Merkle 树？

Merkle 树是一种二叉树，其中：

* 每个叶子节点包含一个数据项的哈希值 (在 CT 中，数据项就是证书)。
* 每个内部节点包含其两个子节点拼接后的哈希值。
* 根哈希代表对树中所有数据的密码学承诺。

![Merkle tree structure](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7Wahic1gibLsrkgIcA9n5NaJiadKuUsUbvwJIsPATWSs4ibO6REn0eQI5pLROYUdph53ZPyybOUFUFORJwZUnqX99mUibaD8x0OrPJsQ6Twn4yIyw/640?wx_fmt=svg&from=appmsg)

Merkle tree structure

这种结构支持两个关键操作：

**包含证明**：给定一张证书，证明它存在于日志中，而无需下载整个日志。你只需要从叶子节点到根节点路径上的哈希值——对于包含 n 个条目的树，只需 O(log n) 个哈希值。

例如，要证明 Cert B 存在于上面的树中，你只需要：

1. H(A)——H(B) 的兄弟节点
2. H(CD)——H(AB) 的兄弟节点
3. 根哈希

然后你可以验证：Root = H(H(H(A) || H(B)) || H(CD))

**一致性证明**：证明日志的较新版本是较旧版本的有效扩展——即没有条目被修改或删除。

### 树头与签名

日志会定期发布签名树头 (STH)，其中包含：

* 树的大小 (条目数量)。
* 时间戳。
* 根哈希。
* 日志对上述值的密码学签名。

## 日志记录的内容

一张典型的 X.509 证书包含：

### 主体与签发者信息

* **主体可分辨名称 (DN)**

  ：可能包括组织名称、地理位置、通用名称等。
* **签发者 DN**

  ：标识签发该证书的 CA。

### 域名

* **通用名称 (CN)**

  ：主域名。
* **主体备用名称 (SANs)**

  ：证书有效覆盖的域名和 IP 地址的权威列表。

SANs 示例：

```
DNS:example.com
DNS:www.example.com
DNS:api.example.com
DNS:staging.internal.example.com
DNS:10-0-1-42.pods.cluster.local
```

### 有效期

* **Not Before**

  ：证书生效时间。
* **Not After**

  ：证书过期时间。

### 公钥

证书中包含其公钥。

### 扩展

各种 X.509 扩展，包括：

* 密钥用途约束。
* 基本约束 (该证书是否为 CA 证书？)。
* 证书策略。
* 颁发机构信息访问 (在哪里获取签发者的证书和 OCSP)。

## 证书与预证书

CT 日志接受两种类型的条目：

### 证书

标准 X.509 证书。在签发后记录证书意味着该证书可以立即使用。

### 预证书

预证书是一种特殊的类证书结构，它：

* 包含与最终证书完全相同的信息。
* 包含一个 "毒药" 扩展 (OID 1.3.6.1.4.1.11129.2.4.3)，将其标记为对 TLS 无效。
* 由签发 CA 或专用的预证书签名证书签署。

预证书的工作流程：

1. CA 使用所有最终证书的详细信息创建预证书。
2. CA 将预证书提交到 CT 日志。
3. 日志返回 SCT。
4. CA 创建最终证书，并将 SCT 嵌入其中。
5. CA 将最终证书签发给订阅者。

这使得 SCT 可以直接嵌入证书中，这是最简洁的分发机制。

预证书和最终证书的信息完全一致，区别仅在于：

* 毒药扩展被移除。
* SCT 列表扩展被添加。
* 签名不同 (覆盖了修改后的扩展)。

在搜索 CT 日志时，你可能会找到证书的其中一个版本或两个版本同时存在。

## 签名证书时间戳 (SCT)

SCT 是日志对将证书纳入日志的承诺。它包含：

* **Log ID**

  ：日志公钥的 SHA-256 哈希值。
* **Timestamp**

  ：日志收到提交的时间。
* **Extensions**

  ：保留供将来使用 (目前为空)。
* **Signature**

  ：日志对上述字段加上证书的签名。

## CT 日志 API

CT 日志公开了一套 HTTP API。RFC 9162 定义了 v2 版本的端点：

### 提交端点

**`POST /ct/v2/submit-entry`**

提交证书或预证书以进行日志记录。返回 SCT。

```
{
"submission": "base64-encoded-cert-or-precert",
"type": 1,
"chain": ["base64-encoded-issuer", ...]
}
```

`type`字段指示提交的内容类型：

* `1`

  表示证书 (`x509_entry_v2`)
* `2`

  表示预证书 (`precert_entry_v2`)

### 查询端点

**`GET /ct/v2/get-sth`**

获取当前的签名树头。

响应：

```
{
"tree_size": 123456789,
"timestamp": 1705123456789,
"sha256_root_hash": "base64-encoded-hash",
"tree_head_signature": "base64-encoded-signature"
}
```

**`GET /ct/v2/get-sth-consistency?first=X&second=Y`**

获取两个树大小之间的一致性证明。

**`GET /ct/v2/get-proof-by-hash?hash=X&tree_size=Y`**

获取叶子哈希的包含证明。

**`GET /ct/v2/get-entries?start=X&end=Y`**

按索引检索日志条目。监控者通过此接口下载证书。

**`GET /ct/v2/get-all-by-hash?hash=X&tree_size=Y`**

在单次请求中同时获取包含证明和一致性证明。

**`GET /ct/v2/get-roots`**

获取该日志可接受的根证书列表。

## crt.sh

crt.sh 是一个公开网站，它将 CT 日志中的数据聚合到一个可搜索的数据库中。你可以通过域名、组织名称或证书哈希来查找证书。这是一种无需直接查询日志就能探索日志内容的便捷方式。

## CT 日志运营者

CT 生态系统包含由多个组织运营的日志：

| 运营者 | 主要日志 |
| --- | --- |
| Google | Argon, Xenon, Icarus, Pilot, Rocketeer |
| Cloudflare | Nimbus |
| DigiCert | Yeti, Nessie |
| Let's Encrypt (ISRG) | Oak |
| Sectigo | Sabre, Mammoth |
| TrustAsia | Trust Asia Log |

## 时间线与历史

* **2011**

  ：DigiNotar 事件。
* **2013**

  ：RFC 6962 发布；Google 启动试点日志。
* **2015**

  ：Chrome 开始要求 EV 证书必须支持 CT。
* **2018**

  ：Chrome 要求所有新签发的证书都必须支持 CT (4 月 30 日)。
* **2021**

  ：RFC 9162 发布。
* **至今**

  ：CT 在主流浏览器中已成为所有公开受信任证书的强制要求。

## 延伸阅读

* RFC 6962: Certificate Transparency
* RFC 9162: Certificate Transparency Version 2.0
* Chrome CT Policy
* crt.sh
* Certificate Transparency website

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