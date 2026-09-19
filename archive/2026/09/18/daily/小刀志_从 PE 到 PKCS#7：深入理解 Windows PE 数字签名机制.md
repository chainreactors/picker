---
title: 从 PE 到 PKCS#7：深入理解 Windows PE 数字签名机制
url: https://xiaodaozhi.com/security/482.html
source: 小刀志
date: 2026-09-18
fetch_date: 2026-09-19T07:00:19.302383
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

2026-08-15 16:01:46

3

分享

AI 总结

PESignAnalyzer作为十年前开发的Windows PE数字签名分析工具，其实现路径揭示了Authenticode技术的完整层次：PE文件通过IMAGE\_DIRECTORY\_ENTRY\_SECURITY定位到文件末尾的Attribute Certificate Table，其中存放WIN\_CERTIFICATE容器，实际载荷为PKCS#7/CMS格式的SignedData；该结构经CryptQueryObject交给Windows CryptoAPI解析后，获取CMSG\_SIGNER\_INFO并反序列化为SignerInfo结构，其中Issuer与Serial Number用于在证书集合中匹配对应X.509证书，进而构建从签名证书经中间CA到根CA的证书链。工具设计的关键在于将标准ASN.1/DER结构交由CryptoAPI处理，仅对Nested Signature和RFC 3161时间戳等特殊Unauthenticated Attributes自行遍历DER字节，通过轻量级TLV解析器在8字节对齐约束下提取内层签名。此外，该工具支持Catalog Signature回退机制，当文件无内嵌签名时通过CryptCATAdminCalcHashFromFileHandle计算文件哈希，再从系统目录中枚举匹配的.cat签名记录。作者强调解析成功不等于签名有效，签名数学验证不等于证书可信，证书链建立不等于Windows信任，这四个层次分别对应格式解析、密码学验证、链验证和WinVerifyTrust平台信任评估，而OpenSSL只能替代前者的密码学与格式解析部分，无法复刻Windows的Certificate Store和信任策略体系。

[分类：安全](/category/security/)

[#Windows](/tag/Windows/)

[#PE文件](/tag/PE%E6%96%87%E4%BB%B6/)

[#安全](/tag/%E5%AE%89%E5%85%A8/)

[#数字签名](/tag/%E6%95%B0%E5%AD%97%E7%AD%BE%E5%90%8D/)

[#证书](/tag/%E8%AF%81%E4%B9%A6/)

大约十年前我写 PESignAnalyzer 时，最初的目标其实很直接：给定一个 Windows PE 文件，希望能够知道它由谁签署、使用了什么算法、对应什么证书、证书链是什么，以及签名有没有时间戳。

真正开始实现以后，事情很快变得复杂起来。

![深入理解 PE 数字签名机制]( "深入理解 PE 数字签名机制")

项目地址：<https://github.com/leeqwind/PESignAnalyzer>

最初版本的 PESignAnalyzer 主要解决“把签名信息读出来”这个问题。最近重新整理项目时，我又补上了 Authenticode 内容摘要、CMS 签名、时间戳、证书链、吊销状态和 Catalog 成员关系的验证，并且保留了一个明确约束：**不调用 `WinVerifyTrust`，也不调用任何 `CryptCATAdmin*` API，最终二进制不导入 `Wintrust.dll`。**

因此，现在再回头看这个项目，它已经不只是一个签名信息提取器，也可以作为一个实际案例，用来理解下面几个经常被混在一起的问题：

* 签名数据能不能正确解析；
* 文件内容有没有被修改；
* CMS 密码学签名是否成立；
* 签名者证书链是否可信；
* 时间戳能否证明签名发生在证书有效期内；
* 吊销状态能否确定；
* 一个没有嵌入式签名的文件，是否由系统 Catalog 覆盖。

PE 文件的数字签名并不是简单地在文件末尾放一段 RSA 签名，再对整个 EXE 做一次 SHA-256。Windows Authenticode 把签名放进 PE 的 Certificate Table；Certificate Table 里面通常又是一份 PKCS#7/CMS SignedData；SignedData 中包含 SignerInfo、证书集合和各种 Attribute；SignerInfo 再通过 Issuer 和 Serial Number 与 X.509 证书关联起来。继续往下，还可能遇到 Counter Signature、RFC 3161 时间戳、Nested Signature，以及完全不同于 Embedded Signature 的 Catalog Signature。

因此，一个看起来很简单的问题：“这个 EXE 是谁签的？”实际上涉及多个层次：

![从 PE、Authenticode、CMS、SignerInfo 和 X.509 到 Windows Trust 的处理层次]( "从 PE、Authenticode、CMS、SignerInfo 和 X.509 到 Windows Trust 的处理层次")

先解释几个贯穿全文的名词：

* `Authenticode` 是 Windows 的代码签名机制，它定义 PE 摘要如何计算、签名数据如何封装、时间戳与 Catalog 如何参与验证。
* `PKCS#7` 是一种加密消息封装格式；CMS（Cryptographic Message Syntax）是其后续标准化形式。两者在 Windows API 和日常讨论中经常一起出现。
* `SignerInfo` 是 SignedData 中的签名者记录，包含签名者标识、摘要算法、签名值以及 signed/unsigned attributes。
* `X.509` 是证书格式标准，用来表达公钥、Subject、Issuer、有效期和扩展字段等信息。
* `Certificate Chain` 是从签名者证书，经中间 CA，最终追溯到根 CA 的认证路径。
* `Timestamp` 用来证明某个签名在特定时间已经存在；`Nested Signature` 则表示一个签名结构里还封装了另一份签名。
* `Windows Trust` 是 Windows Trust Provider 根据平台策略得出的结论。它不等同于“PKCS#7 数学签名验证成功”。

本文不会按 API 手册的顺序逐个介绍函数，而是沿着 PESignAnalyzer 当前的实现路径，从 PE 文件一直走到验证结果。

## 一、从一个 EXE 文件开始：数字签名到底在哪里

理解 Authenticode，第一步不是看证书，也不是看 RSA，而是先回到 PE 文件本身。

PE 文件由 DOS Header、NT Header、Optional Header、Data Directory 和多个 Section 组成。数字签名对应 Data Directory 中一个很特殊的目录项：`IMAGE_DIRECTORY_ENTRY_SECURITY`，它指向 Attribute Certificate Table。

这里有一个容易踩坑的细节：普通 Data Directory 中的地址通常是 RVA，而 Security Directory 中的 `VirtualAddress` 实际上是**文件偏移量**。

这意味着 Certificate Table 不属于正常装载到内存的 PE Section。它通常位于文件末尾，只在磁盘文件中保存签名数据：

TEXT

```
DOS Header
NT Headers
.text
.rdata
.data
.rsrc
...
Certificate Table
```

这条路径对应 PE 文件自身携带的嵌入式签名：

![PE 文件经 Certificate Table 保存 Embedded Signature]( "PE 文件经 Certificate Table 保存 Embedded Signature")

Certificate Table 的基本容器是 `WIN_CERTIFICATE`：

CPP

```
typedef struct _WIN_CERTIFICATE {
    DWORD dwLength;
    WORD  wRevision;
    WORD  wCertificateType;
    BYTE  bCertificate[1];
} WIN_CERTIFICATE;
```

`bCertificate` 这个名字并不意味着里面直接放着一张 X.509 证书。对 Authenticode 来说，它通常承载一份 PKCS#7 SignedData：

![PE 文件中的 Attribute Certificate Table、WIN_CERTIFICATE 与 PKCS#7 SignedData 层次]( "PE 文件中的 Attribute Certificate Table、WIN_CERTIFICATE 与 PKCS#7 SignedData 层次")

PE 格式在这里完成的任务只是告诉解析器：“文件的这个偏移处有一块证书表”。至于里面的 SignedData、SignerInfo、证书和属性如何解释，已经进入 CMS、ASN.1/DER 和 X.509 的世界。

## 二、从 CryptQueryObject 到 SignerInfo：让 CryptoAPI 解析标准结构

PESignAnalyzer 的一个基本设计原则，是尽可能把标准 PKCS#7 和 X.509 结构交给 Windows CryptoAPI，而不是自己重新实现通用 ASN.1 解码器。

`ASN.1` 用来描述数据结构，`DER` 是其确定性的二进制编码规则，`OID` 则用数字标识算法、属性和内容类型。PKCS#7/CMS、X.509 证书和 Authenticode 属性底层都大量依赖它们。

如果从零实现，很快就会把项目变成另一个 ASN.1、X.509 和 CMS 库。Windows 已经提供了这些能力，因此项目使用 `CryptQueryObject` 打开签名对象，并取得两个重要句柄：

* `HCRYPTMSG`：已经解码的 PKCS#7/CMS 消息；
* `HCERTSTORE`：消息携带的证书集合。

项目对 `CryptMsgGetParam` 做了一个“两次调用”封装：第一次获取所需大小，第二次分配内存并读取数据。

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

    *pParam = LocalAlloc(LPTR, dwSize);
    if (!*pParam)
        return FALSE;

    if (!CryptMsgGetParam(hCryptMsg, dwParamType, dwIndex,
        *pParam, &dwSize)) {
        LocalFree(*pParam);
        *pParam = NULL;
        return FALSE;
    }
    if (dwOutSize)
        *dwOutSize = dwSize;
    return TRUE;
}
```

通过 `CMSG_SIGNER_INFO_PARAM`，文件中的 DER 字节会被还原为结构化的 `CMSG_SIGNER_INFO`：

![SignerInfo 的主要字段及 SignerIdentifier 的证书定位信息]( "SignerInfo 的主要字段及 SignerIdentifier 的证书定位信息")

这里最重要的内容包括：

* Issuer 和 Serial Number：用于定位签名者证书；
* HashAlgorithm：SignerInfo 使用的摘要算法；
* EncryptedHash：签名值；
* AuthAttrs：参与签名的属性；
* UnauthAttrs：Counter Signature、RFC 3161、Nested Signature 等附加数据。

拿到 SignerInfo，才真正从“PE 文件解析”进入“签名消息解析”。

## 三、从 SignerInfo 到 X.509：证书关联不等于证书链验证

SignerInfo 并不是简单地内嵌一张签名者证书。它通常通过 Issuer 和 Serial Number 指向 SignedData 证书集合中的某张证书：

![SignerInfo 使用 Issuer 和 Serial Number 从证书存储定位 X.509 证书]( "SignerInfo 使用 Issuer 和 Serial Number 从证书存储定位 X.509 证书")

PESignAnalyzer 使用 `CertFindCertificateInStore` 将两者关联起来，取得 `PCCERT_CONTEXT` 后，再读取 Subject、Issuer、Serial Number、Version、有效期、Thumbprint、签名算法和 CRL Distribution Points。

项目使用 `CERT_NODE_INFO` 表示一张证书：

CPP

```
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
} CERT_NODE_INFO;
```

而 `SIGN_NODE_INFO` 表示一份签名及其相关证书：

CPP

```
typedef struct _SIGN_NODE_INFO {
    std::string DigestAlgorithm;
    std::string Version;
    SIGN_COUNTER_SIGN CounterSign;
    std::list<CERT_NODE_INFO> CertChain;
} SIGN_NODE_INFO;
```

从证书的签发关系来看，一条典型的代码签名认证路径由叶子证书开始，经过一个或多个中间 CA，最终到达受信任的根 CA：

![代码签名证书、中间 CA 与根 CA 组成的证书链]( "代码签名证书、中间 CA 与根 CA 组成的证书链")

图中的箭头表示验证时沿 Issuer 方向向信任锚追溯，并不表示把根证书包含在 SignerInfo 中。签名消息通常携带签名者证书和部分中间证书，而根证书是否可信，取决于本机的受信任根证书存储和证书链策略。

这里必须区分两件事：

1. **为了展示信息而按 Issuer 关联证书**；
2. **为了得出信任结论而构建并验证证书链**。

早期版本主要做第一件事。当前版本在 `--verify` 模式下还会调用 `CertGetCertificateChain` 构建证书链，再调用 `CertVerifyCertificateChainPolicy` 应用 `CERT_CHAIN_POLICY_AUTHENTICODE` 或时间戳策略。

因此，“输出里看到了根证书”并不自动意味着 `certificateChain: trusted`。真正的链验证还需要检查签名、用途、有效期、根信任和策略；启用吊销检查时还要处理 CRL/OCSP 状态。

也不要把下面三个概念混为一谈：

* SHA-256：摘要算法；
* RSA：公钥算法；
* sha256WithRSAEncryption：把 SHA-256 与 RSA 签名组合起来的算法标识。

它们都可能出现在同一份签名输出里，但描述的是不同层次。

## 四、Nested Signature、Counter Signature 与 RFC 3161

如果只需要解析一个 SignerInfo，项目并不会复杂到现在这个程度。真正麻烦的是 unsigned attributes 中还可能包含其他签名结构。

### 4.1 Nested Signature

Nested Signature 的本质，是一个签名结构中又包含另一份签名：

![外层 SignerInfo 通过 Unauthenticated Attributes 包含嵌套 PKCS#7 SignedData 及其 SignerInfo]( "外层 SignerInfo 通过 Unauthenticated Attributes 包含嵌套 PKCS#7 SignedData 及其 SignerInfo")

项目会遍历 `UnauthAttrs`，寻找 `szOID_NESTED_SIGNATURE`，再把属性中的 DER 数据送回 CryptoAPI 解码：

![PESignAnalyzer 查找 Nested Signature 并交由 CryptoAPI 解析内层 PKCS#7 的流程]( "PESignAnalyzer 查找 Nested Signature 并交由 CryptoAPI 解析内层 PKCS#7 的流程")

旧版代码还处理了多个嵌套块和 8 字节对齐，避免把整个属性错误地当成单个 PKCS#7 对象。

### 4.2 旧式 Counter Signature

Counter Signature 不是另一份并列的软件签名，而是对主 SignerInfo 的签...