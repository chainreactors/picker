---
title: 从 PE 到 PKCS#7：深入理解 Windows PE 数字签名机制
url: https://xiaodaozhi.com/security/482.html
source: 小刀志
date: 2026-08-15
fetch_date: 2026-08-16T02:55:27.760669
---

# 从 PE 到 PKCS#7：深入理解 Windows PE 数字签名机制

![小刀志](/logo.png)

网站首页

友情链接

关于本站

站点地图

管理中心

![小刀志](/logo.png)

小刀志

稻草小刀的在线笔记。记录所有事情，并写给自己。

# 从 PE 到 PKCS#7：深入理解 Windows PE 数字签名机制

![avatar](/!avatar/X/120/f585929a3a7de3e707639a048fff1324)

[稻草小刀](/author/1/)

16 小时前

1

分享

AI 总结

大约十年前开发的PESignAnalyzer旨在解析Windows PE文件数字签名，揭示签署者、算法、证书链及时间戳。实现中，发现PE签名并非文件末尾简单RSA，而是存于Certificate Table的PKCS#7/CMS数据，需沿PE→Authenticode→PKCS#7→SignerInfo→X.509→Certificate Chain→Timestamp/Windows Trust链路逐层解析。核心实现依赖Windows CryptoAPI（如CryptQueryObject和CryptMsgGetParam）解析标准格式，但对Nested Signature、RFC 3161时间戳等特殊结构，则自定义轻量级DER遍历器（如ParseDERType和SafeToReadNBytes）处理，并强调长度字段安全性。技术要点包括：SignerInfo通过Issuer和Serial Number与证书关联；区分文件Hash、Authenticode Hash（排除Certificate Table参与）、证书Thumbprint和签名；并识别Embedded Signature与Catalog Signature两种模式。关键认知分层：解析成功不等于签名有效，数学验证不等于证书可信，证书链建立不等于Windows信任，且无Embedded Signature的文件可经Catalog验证。工程核心是利用平台API处理标准格式，同时自行补充关键细节，形成CryptoAPI与自研DER解析的协同。

[分类：安全](/category/security/)

[#Windows](/tag/Windows/)

[#PE文件](/tag/PE%E6%96%87%E4%BB%B6/)

[#安全](/tag/%E5%AE%89%E5%85%A8/)

[#数字签名](/tag/%E6%95%B0%E5%AD%97%E7%AD%BE%E5%90%8D/)

[#证书](/tag/%E8%AF%81%E4%B9%A6/)

大约十年前我写 PESignAnalyzer 时，最初的目标其实很直接：给定一个 Windows PE 文件，希望能够分析它的数字签名，知道这个文件是谁签署的、使用了什么算法、对应什么证书、证书链是什么，以及签名有没有时间戳。

真正开始实现以后，事情很快变得复杂起来。

![深入理解 PE 数字签名机制]( "深入理解 PE 数字签名机制")

PE 文件的数字签名并不是简单地在文件末尾放一段 RSA 签名，然后对整个 EXE 做一次 SHA-256。Windows 的 Authenticode 把签名放进 PE 的 Certificate Table，而 Certificate Table 里面又是一份 PKCS#7/CMS 数据；PKCS#7 中包含 SignedData、SignerInfo、证书集合和各种 Attribute；SignerInfo 再通过 Issuer 和 Serial Number 与 X.509 证书关联起来。继续往下，还可能遇到 Counter Signature、RFC 3161 时间戳、Nested Signature，以及完全不同于 Embedded Signature 的 Catalog Signature。

因此，一个看起来很简单的问题：“这个 EXE 是谁签的？”

实际上涉及了多个不同层次的技术：

TEXT

```
PE
 ↓
Authenticode
 ↓
PKCS#7 / CMS
 ↓
SignerInfo
 ↓
X.509
 ↓
Certificate Chain
 ↓
Timestamp / Nested Signature
 ↓
Windows Trust
```

PESignAnalyzer 当年的实现，基本就是沿着这条链一路往下做解析。

现在重新回头看这份代码，我觉得它比较适合作为一个实际案例，用来理解 Windows PE 数字签名到底是怎么工作的。这篇文章不会把重点放在“API 手册式”的介绍上，而是直接从 PESignAnalyzer 的实现路径出发，解释每一层数据是什么、为什么需要这一层，以及 Windows CryptoAPI 在其中究竟帮我们做了什么。

## 一、从一个 EXE 文件开始：PE 数字签名到底在哪里

理解 Authenticode，第一步不是看证书，也不是看 RSA，而是先回到 PE 文件本身。

一个 PE 文件的基本结构大致是 DOS Header、PE Header、Optional Header、Data Directory 和多个 Section。很多和 Windows PE 相关的功能都通过 Optional Header 中的 Data Directory 描述，例如导入表、资源表、重定位表等。

数字签名对应的是其中一个非常特殊的目录项：`IMAGE_DIRECTORY_ENTRY_SECURITY`，它指向的是 PE 的 Attribute Certificate Table。

这里有一个很重要的细节：IMAGE\_DIRECTORY\_ENTRY\_SECURITY 与普通 PE Data Directory 的语义并不完全一样。普通目录中的地址通常是 RVA，也就是相对于 PE Image Base 的虚拟地址；而 Security Directory 中的 VirtualAddress 实际表示的是文件偏移量。

这意味着 Certificate Table 并不是 PE 映像正常加载后某个 Section 中的一块内存。它实际上是文件中的附加数据，通常位于 PE 文件末尾。

这也是 Windows Authenticode 一个有意思的设计。

假设一个 EXE 的结构是：

TEXT

```
DOS Header
PE Header
.text
.rdata
.data
.rsrc
...
Certificate Table
```

Certificate Table 并不参与正常的代码执行，也不需要被映射成普通 PE Section。它只是作为文件的一部分保存签名相关数据。

Certificate Table 中的基本容器是 WIN\_CERTIFICATE：

TEXT

```
typedef struct _WIN_CERTIFICATE {
    DWORD dwLength;
    WORD  wRevision;
    WORD  wCertificateType;
    BYTE  bCertificate[1];
} WIN_CERTIFICATE;
```

这里最容易产生误解的是 bCertificate 这个名字，它并不意味着这里直接存放了一张 X.509 Certificate。对于 Authenticode 来说，这里的数据通常是：PKCS#7 SignedData。

所以从文件结构的角度来看，可以把它理解成：

TEXT

```
PE 文件
 └── Attribute Certificate Table
      └── WIN_CERTIFICATE
           └── PKCS#7 SignedData
```

到了这里，PE 格式本身已经基本完成了它的任务。PE 只负责告诉 Windows：“这里有一块 Certificate Table 数据”。至于这块数据里面是什么，已经进入密码学和消息封装格式的世界。这也是为什么一个真正的 PE 签名分析器不能只会解析 PE Header。解析到 IMAGE\_DIRECTORY\_ENTRY\_SECURITY 只是第一步，真正复杂的工作才刚刚开始。

## 二、从 CryptQueryObject 到 SignerInfo：PESignAnalyzer 如何解析 Authenticode

PESignAnalyzer 最核心的实现思路之一，是尽可能把标准数据结构交给 Windows 自己的 CryptoAPI 处理，而不是重新实现一遍 PKCS#7 和 X.509。这是一个非常现实的工程选择。因为 PKCS#7 本质上是 ASN.1 定义的数据结构。它不是一个简单的 `Header Length Data Signature` 格式，而是大量 SEQUENCE、SET、OID、Context-specific Tag 以及可变长度数据组合起来的嵌套结构。

如果自己从零实现，会很快进入 ASN.1 编解码器、X.509 Parser、PKCS#7 Parser 这些完全不同的工作领域。

Windows 已经提供了这些能力。

PESignAnalyzer 使用的一个重要入口就是 CryptQueryObject。它的意义可以理解为：把文件中的编码对象交给 CryptoAPI，让系统识别和解析它，并返回后续操作需要的密码学对象。

对于 Authenticode 来说，最终最重要的两个对象分别是：`HCRYPTMSG`、`HCERTSTORE`。HCRYPTMSG 可以理解成已经被 CryptoAPI 打开的 PKCS#7/CMS 消息对象，而 HCERTSTORE 则代表这个签名消息所携带的证书集合。这两个对象非常关键，因为接下来 PESignAnalyzer 不需要自己在 DER 数据中寻找 SignerInfo。

它直接通过 CryptMsgGetParam 获取 CMSG\_SIGNER\_INFO：

TEXT

```
CryptMsgGetParam(
    hCryptMsg,
    CMSG_SIGNER_INFO_PARAM,
    ...
);
```

这一步实际上完成了一次非常重要的抽象。

文件里面原本是一大块 ASN.1 DER：

TEXT

```
30 82 ...
06 ...
31 ...
30 ...
```

经过 CryptoAPI 后，应用程序可以直接看到一个结构化的 CMSG\_SIGNER\_INFO。而 SignerInfo 正是理解 PKCS#7 签名的核心。从概念上看，它大致包含：

TEXT

```
SignerInfo
 ├── Version
 ├── SignerIdentifier
 │    └── Issuer + Serial Number
 ├── DigestAlgorithm
 ├── Authenticated Attributes
 ├── SignatureAlgorithm
 ├── Signature
 └── Unauthenticated Attributes
```

其中最关键的是 SignerIdentifier、算法信息和 Attributes。

Issuer + Serial Number 用来确定“谁是这个签名者”。DigestAlgorithm 和 SignatureAlgorithm 描述签名所使用的密码学算法。而 Attributes 则是后面整个 Authenticode 世界变复杂的主要原因之一。

PESignAnalyzer 中封装的 MyCryptMsgGetParam 也体现了 CryptoAPI 一个很典型的使用方式：

第一次调用 API 获取需要的缓冲区大小，第二次真正分配内存并读取结构。这并不是 CryptoAPI 特有的技巧，而是 Windows C API 中非常常见的设计，因为 CMSG\_SIGNER\_INFO 后面还有数量不固定的属性数据，其实际大小无法通过一个固定的 sizeof(CMSG\_SIGNER\_INFO) 得到。

拿到 CMSG\_SIGNER\_INFO 以后，PESignAnalyzer 就真正从“PE 文件解析”进入了“签名消息解析”。

## 三、从 SignerInfo 到 X.509：签名者、证书和证书链是怎么关联起来的

这里是 PE 签名分析中非常容易被忽略的一步。很多人看到一个 PKCS#7 文件，会认为：“里面既然有签名者，那里面应该直接有签名者的证书”。从结果上看确实如此，但从数据结构上并不是简单的“SignerInfo 里面放一张 Certificate”。

SignerInfo 中的签名者标识通常是：Issuer 和 Serial Number，而 PKCS#7 SignedData 又包含一个证书集合。所以实际关系是：

TEXT

```
SignerInfo
   │
   ├── Issuer
   └── Serial Number
          │
          ▼
      Certificate Store
          │
          ▼
      X.509 Certificate
```

这就是 PESignAnalyzer 后面需要使用 CertFindCertificateInStore 一类 API 的原因。它不是多余的查找步骤，而是在完成两个不同数据结构之间的关联。

拿到 PCCERT\_CONTEXT 后，才真正进入 X.509 世界。这时候可以读取证书的 Subject、Issuer、Serial Number、Version、Validity、Thumbprint、Public Key 和 Signature Algorithm 等信息。PESignAnalyzer 为此设计了 CERT\_NODE\_INFO 结构：

TEXT

```
/// Per certificate node.
typedef struct _CERT_NODE_INFO {
    std::string SubjectName;
    std::string IssuerName;
    std::string Version;
    std::string Serial;
    std::string Thumbprint;
    std::string NotBefore;
    std::string NotAfter;
    std::string SignAlgorithm;
    std::wstring CRLpoint;
} CERT_NODE_INFO, *PCERT_NODE_INFO;
```

从这个结构能够非常清楚地看出当时希望最终得到什么信息：证书主体、颁发者、版本、序列号、Thumbprint、有效期、签名算法以及 CRL 地址等。

与此同时，项目又使用 SIGN\_NODE\_INFO 表示一个签名节点，并把证书信息组织成 CertChain。

TEXT

```
/// Per signature node.
typedef struct _SIGN_NODE_INFO {
    std::string DigestAlgorithm;
    std::string Version;
    SIGN_COUNTER_SIGN CounterSign;
    std::list<CERT_NODE_INFO> CertChain;
} SIGN_NODE_INFO, *PSIGN_NODE_INFO;
```

这个数据结构设计实际上反映了一个很重要的概念：签名和证书不是同一个东西。

一个签名对应一个 SignerInfo；SignerInfo 关联一个签名者证书；签名者证书又可能通过 Issuer 继续找到它的上级 CA。

因此一个正常的软件签名可能形成：

TEXT

```
Code Signing Certificate
        │
        ▼
Intermediate CA
        │
        ▼
Root CA
```

最下面的软件签名证书是 End Entity Certificate，它并不是信任链的根。

所以一个分析器真正有价值的结果，不应该只是：Subject = XXX Corporation，而应该能够继续告诉我们：这个证书由哪个 CA 签发，它是否能够构建到可信根，以及这个证书在签名时是否处于有效状态。

这里还必须区分几个非常容易混淆的概念，例如：

TEXT

```
SHA-256
RSA
sha256WithRSAEncryption
```

它们不是三个不同名字的同一个东西。

* SHA-256 是摘要算法。
* RSA 是公钥密码算法。
* sha256WithRSAEncryption 是将 SHA-256 与 RSA 签名组合起来的算法标识。

PESignAnalyzer 中的 CalculateDigestAlgorithm 和 CalculateCertAlgorithm 就承担了把 OID 转换成人类可读名称的工作。

例如 PKCS#7 中可能看到：`1.2.840.113549.1.7.2`，这是 signedData。

而证书签名算法又可能出现：`1.2.840.113549.1.1.11`，它对应 SHA-256 with RSA。

如果直接把这些 OID 原样输出给用户，分析结果其实并不好用。

因此，PESignAnalyzer 做的事情不仅是“解析”，还包括把底层密码学数据重新组织成分析人员能够理解的信息。

## 四、Authenticode 最麻烦的部分：Nested Signature、Counter Signature 与 RFC 3161

如果 PESignAnalyzer 只需要找到一个 SignerInfo，整个项目其实不会复杂到现在这个程度。真正让 Authenticode 变得有意思的是 Unauthenticated Attributes。

签名本身还可以携带其他签名相关数据，最典型的就是 Nested Signature。

PESignAnalyzer 对 `szOID_NESTED_SIGNATURE` 进行了专门处理。Nested Signature 的本质是：一个签名结构里面又包含另一个签名结构。

也就是说，结构可能变成：

TEXT

```
SignerInfo
 └── Unauthenticated Attributes
      └── Nested Signature
           └── PKCS#7 SignedData
                └── SignerInfo...