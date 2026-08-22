---
title: 从 PE 到 PKCS#7：深入理解 Windows PE 数字签名机制
url: https://xiaodaozhi.com/security/482.html
source: 小刀志
date: 2026-08-21
fetch_date: 2026-08-22T02:50:51.529776
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

6 天前

1

分享

AI 总结

PESignAnalyzer作为十年前开发的Windows PE数字签名分析工具，其实现路径揭示了Authenticode技术的完整层次：PE文件通过IMAGE\_DIRECTORY\_ENTRY\_SECURITY定位到文件末尾的Attribute Certificate Table，其中存放WIN\_CERTIFICATE容器，实际载荷为PKCS#7/CMS格式的SignedData；该结构经CryptQueryObject交给Windows CryptoAPI解析后，获取CMSG\_SIGNER\_INFO并反序列化为SignerInfo结构，其中Issuer与Serial Number用于在证书集合中匹配对应X.509证书，进而构建从签名证书经中间CA到根CA的证书链。工具设计的关键在于将标准ASN.1/DER结构交由CryptoAPI处理，仅对Nested Signature和RFC 3161时间戳等特殊Unauthenticated Attributes自行遍历DER字节，通过轻量级TLV解析器在8字节对齐约束下提取内层签名。此外，该工具支持Catalog Signature回退机制，当文件无内嵌签名时通过CryptCATAdminCalcHashFromFileHandle计算文件哈希，再从系统目录中枚举匹配的.cat签名记录。作者强调解析成功不等于签名有效，签名数学验证不等于证书可信，证书链建立不等于Windows信任，这四个层次分别对应格式解析、密码学验证、链验证和WinVerifyTrust平台信任评估，而OpenSSL只能替代前者的密码学与格式解析部分，无法复刻Windows的Certificate Store和信任策略体系。

[分类：安全](/category/security/)

[#Windows](/tag/Windows/)

[#PE文件](/tag/PE%E6%96%87%E4%BB%B6/)

[#安全](/tag/%E5%AE%89%E5%85%A8/)

[#数字签名](/tag/%E6%95%B0%E5%AD%97%E7%AD%BE%E5%90%8D/)

[#证书](/tag/%E8%AF%81%E4%B9%A6/)

大约十年前我写 PESignAnalyzer 时，最初的目标其实很直接：给定一个 Windows PE 文件，希望能够分析它的数字签名，知道这个文件是谁签署的、使用了什么算法、对应什么证书、证书链是什么，以及签名有没有时间戳。

真正开始实现以后，事情很快变得复杂起来。

![深入理解 PE 数字签名机制]( "深入理解 PE 数字签名机制")

项目地址：<https://github.com/leeqwind/PESignAnalyzer>

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

先解释一下这里出现的几个名词：

* `Authenticode` 是 Windows 用来给 PE、Catalog 等对象做代码签名的一套机制，它规定了签名数据放在哪里、文件哈希怎么算、时间戳和嵌套签名等结构如何表达。
* `PKCS#7` 是一种加密消息封装格式，可以把签名值、签名者信息、证书集合等内容放进同一个 SignedData 结构里。后来 IETF 在它的基础上标准化了 `CMS`（Cryptographic Message Syntax），所以很多上下文里会把 `PKCS#7` 和 `CMS` 放在一起说。
* `SignerInfo` 是 PKCS#7/CMS SignedData 里的签名者记录，它描述签名者是谁、使用了什么摘要算法、签名算法是什么，以及携带哪些 signed/unsigned attributes。
* `X.509` 是证书格式标准，用来表达一个实体的公钥、Subject、Issuer、有效期、扩展字段等信息。
* `Certificate Chain` 是从签名者证书一路追溯到中间 CA、根 CA 的证书路径。
* `Timestamp` 用来证明签名在某个时间点已经存在；`Nested Signature` 则表示一个签名结构中还包含另一份签名结构。
* `Windows Trust` 在本文中主要指 Windows 通过 `WinVerifyTrust` 这类入口做出的平台信任判断，它不等同于单纯的 PKCS#7 签名数学验证。

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

CPP

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

这里的 `ASN.1` 可以理解成一种描述数据结构的语言，负责说明“这个结构里有哪些字段、字段是什么类型、如何嵌套”。`DER` 则是 ASN.1 的一种二进制编码规则，负责把这些抽象结构变成文件里的字节序列。`OID` 是对象标识符，用一串数字表示某个算法、属性或结构类型，例如 signedData、SHA-256 with RSA、CRL Distribution Points 等。PKCS#7/CMS、X.509 证书以及很多 Authenticode 属性，底层都离不开 ASN.1、DER 和 OID。

如果自己从零实现，会很快进入 ASN.1 编解码器、X.509 Parser、PKCS#7 Parser 这些完全不同的工作领域。

Windows 已经提供了这些能力。

PESignAnalyzer 使用的一个重要入口就是 CryptQueryObject。它的意义可以理解为：把文件中的编码对象交给 CryptoAPI，让系统识别和解析它，并返回后续操作需要的密码学对象。

对于 Authenticode 来说，最终最重要的两个对象分别是：`HCRYPTMSG`、`HCERTSTORE`。HCRYPTMSG 可以理解成已经被 CryptoAPI 打开的 PKCS#7/CMS 消息对象，而 HCERTSTORE 则代表这个签名消息所携带的证书集合。这两个对象非常关键，因为接下来 PESignAnalyzer 不需要自己在 DER 数据中寻找 SignerInfo。

代码里对 `CryptMsgGetParam` 做了一个封装，先问大小，再分配，再读结构：

CPP

```
BOOL MyCryptMsgGetParam(
    HCRYPTMSG hCryptMsg,
    DWORD dwParamType,
    DWORD dwIndex,
    PVOID *pParam,
    DWORD *dwOutSize
) {
    DWORD dwSize = 0;
    *pParam = NULL;
    if (!CryptMsgGetParam(hCryptMsg, dwParamType, dwIndex, NULL, &dwSize))
        return FALSE;
    *pParam = (PVOID)LocalAlloc(LPTR, dwSize);
    if (!*pParam)
        return FALSE;
    if (!CryptMsgGetParam(hCryptMsg, dwParamType, dwIndex, *pParam, &dwSize)) {
        LocalFree(*pParam);
        *pParam = NULL;
        return FALSE;
    }
    if (dwOutSize)
        *dwOutSize = dwSize;
    return TRUE;
}
```

它直接通过 CryptMsgGetParam 获取 CMSG\_SIGNER\_INFO：

CPP

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

PESignAnalyzer 中的 `MyCryptMsgGetParam` 使用了 CryptoAPI 常见的两次调用模式：

第一次调用 API 获取需要的缓冲区大小，第二次真正分配内存并读取结构。这并不是 CryptoAPI 特有的技巧，而是 Windows C API 中非常常见的设计，因为 CMSG\_SIGNER\_INFO 后面还有数量不固定的属性数据，其实际大小无法通过一个固定的 sizeof(CMSG\_SIGNER\_INFO) 得到。

拿到 CMSG\_SIGNER\_INFO 以后，PESignAnalyzer 就真正从“PE 文件解析”进入了“签名消息解析”。

## 三、从 SignerInfo 到 X.509：签名者、证书和证书链是怎么关联起来的

这里是 PE 签名分析中非常容易被忽略的一步。很多人看到一个 PKCS#7 文件，会认为：“里面既然有签名者，那里面应该直接有签名者的证书”。从结果上看确实如此，但从数据结构上并不是简单的“SignerInfo 里面放一张 Certificate”。

SignerInfo 中的签名者标识通常是：Issuer 和 Serial Number，而 PKCS#7 SignedData 又包含一个证书集合。所以实际关系是：

TEXT

```
SignerInfo
   ├── Issuer
   └── Serial Number
          ▼
      Certificate Store
          ▼
      X.509 Certificate
```

这就是 PESignAnalyzer 后面需要使用 CertFindCertificateInStore 一类 API 的原因。它不是多余的查找步骤，而是在完成两个不同数据结构之间的关联。

拿到 PCCERT\_CONTEXT 后，才真正进入 X.509 世界。这时候可以读取证书的 Subject、Issuer、Serial Number、Version、Validity、Thumbprint、Public Key 和 Signature Algorithm 等信息。PESignAnalyzer 为此设计了 CERT\_NODE\_INFO 结构：

CPP

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

从这个结构能够非常清楚地看出当时希望最终得到什么信息：证书主体、颁发者、版本、序列号、Thumbprint、有效期、签名算法以及 CRL 地址等...