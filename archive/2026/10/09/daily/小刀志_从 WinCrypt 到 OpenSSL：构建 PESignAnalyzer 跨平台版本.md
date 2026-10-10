---
title: 从 WinCrypt 到 OpenSSL：构建 PESignAnalyzer 跨平台版本
url: https://xiaodaozhi.com/security/526.html
source: 小刀志
date: 2026-10-09
fetch_date: 2026-10-10T07:56:32.171835
---

# 从 WinCrypt 到 OpenSSL：构建 PESignAnalyzer 跨平台版本

![小刀志](/logo.png)

网站首页

友情链接

关于本站

站点地图

管理中心

![小刀志](/logo.png)

小刀志

稻草小刀的在线笔记。记录所有事情，并写给自己。

# 从 WinCrypt 到 OpenSSL：构建 PESignAnalyzer 跨平台版本

![avatar](/!avatar/X/120/f585929a3a7de3e707639a048fff1324)

[稻草小刀](/author/1/)

昨天

0

分享

AI 总结

本文记录了将 Windows PE 数字签名分析工具从 WinCrypt 迁移到 OpenSSL 以构建跨平台版本（PESignAnalyzer）的工程实践，核心结论是跨平台验签的难点不在密码学运算本身，而在摘要范围界定、ASN.1 包装层差异、时间戳兼容策略以及证书来源与信任环境的重建。项目按 PE 读取、PKCS#7 解析、摘要计算、签名与时间戳验证、信任处理分层，将原由 CryptQueryObject 等 API 承担的职责重新分配，平台差异集中在证书来源与路径处理。关键事实包括：Authenticode 摘要须按文件顺序跳过校验和、安全目录项与证书表，并覆盖节间空洞、原始填充及证书表后数据，普通整文件 SHA-256 无法通过验证；SPC/CTL 内容取 ASN.1 序列内容部，而 RFC 3161 时间戳须保留 OCTET STRING 内完整 TSTInfo DER，统一剥离外壳会破坏时间戳；真实 Microsoft 样本存在 TSA 证书 timeStamping 用途非 critical 及额外 ESS 引用无法核验的情况，需在严格模式外保留兼容分支并记录原因；吊销检查须区分已吊销与证据未知，后者汇总为 indeterminate；运行包需自带十四个 DLL，并启用 CURLSSLOPT\_NATIVE\_CA 从系统读取 TLS 信任根，否则独立环境 HTTPS 验证失败；默认解析需额外从系统证书库补全根证书以对齐原版输出。

[分类：安全](/category/security/)

[#Windows](/tag/Windows/)

[#PE文件](/tag/PE%E6%96%87%E4%BB%B6/)

[#安全](/tag/%E5%AE%89%E5%85%A8/)

[#数字签名](/tag/%E6%95%B0%E5%AD%97%E7%AD%BE%E5%90%8D/)

[#证书](/tag/%E8%AF%81%E4%B9%A6/)

[#跨平台](/tag/%E8%B7%A8%E5%B9%B3%E5%8F%B0/)

[#OpenSSL](/tag/openssl/)

上一篇[《从 PE 到 PKCS#7：深入理解 Windows PE 数字签名机制》](/security/482.html)写了如何找到、解码 Windows PE 文件的签名数据，再检查证书链和信任关系。文章最后提到，可以把格式解析和密码学处理移到 OpenSSL，让工具离开 Windows 也能运行。这次接着做这件事。

<!--more-->

![从 WinCrypt 到 OpenSSL：构建 PESignAnalyzer 跨平台版本]( "从 WinCrypt 到 OpenSSL：构建 PESignAnalyzer 跨平台版本")

项目地址：<https://github.com/leeqwind/PESignAnalyzer/tree/master/openssl>

分析对象仍是 Windows PE 文件，分析程序则希望能在 Windows、Linux、macOS 上构建。把一个 EXE 复制到 Linux 服务器后，也应当能读出签名者、证书和时间戳，并继续检查文件摘要、签名和证书链。

写下去以后，“怎样调用 OpenSSL”很快让位于具体的排查：文件摘要为什么对不上？Windows 接受的时间戳为什么在 OpenSSL 中失败？已经识别出 Catalog 签名，为什么还会报出警告？验证时有完整证书链，默认解析为什么却少了根证书？

## 一、拆分 Windows API 原来承担的工作

原版 PESignAnalyzer 使用 Windows CryptoAPI。`CryptQueryObject`、`CryptMsgGetParam`、证书存储和构链接口承担了不少工作：调用方能直接拿到解码后的消息、证书上下文，还能从证书库里继续查找发行者。换成 OpenSSL 后，要先重新分配这些入口的职责。

OpenSSL 能解释 PKCS#7/CMS 和 X.509，计算摘要、验证公钥签名和证书路径。PE 的 Certificate Table 在哪里、Authenticode 摘要覆盖哪些字节、Catalog 从哪里找、系统信任根怎样取得，都要由项目处理。证书来源尤其容易被忽略：Windows 上能查到的 Microsoft 根证书，换到另一个平台，未必就在 OpenSSL 的默认 CA 集合里。

OpenSSL 版本按这些职责拆开：PE 读取处理文件布局，PKCS#7 解析展开消息和元数据，摘要计算确定 PE 字节范围，验证处理签名和时间戳，信任处理查找证书、构建路径并检查吊销证据。平台差异尽量放在证书来源和路径处理里。

![PE 格式、消息解析和密码学运算各自处理一层，平台接口继续提供证书来源]( "PE 格式、消息解析和密码学运算各自处理一层，平台接口继续提供证书来源")

后面的排查用上了这个划分。文件摘要失败就查摘要流；时间戳失败就沿着 token、签名绑定和 TSA 证书链查下去。OpenSSL 返回错误时，至少能先确定问题落在哪一层。

## 二、从文件字节开始，先做出第一版

第一版先打通一条路径：读取 PE，定位 Security Directory，取出 `WIN_CERTIFICATE` 的载荷，再交给 OpenSSL 解码 SignedData。

这里沿用了原版的做法：标准 CMS 和证书结构交给成熟库，项目补充 Authenticode 特有的结构。自己写的 DER 读取器只解释 SPC 摘要、嵌套签名属性和 Catalog 成员，没有继续做成通用 ASN.1 框架。

读取 PE 时，不能因为“只是读取”就省去布局检查。Security Directory 给出的是文件偏移，PE32 和 PE32+ 的目录位置不同；证书记录有长度和对齐规则，一个文件还可能带着多条记录。使用偏移前，必须检查越界、溢出和区域重叠。[Microsoft 的 PE 格式说明](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format)给出了这些基础规则，代码还需要补齐对应的失败路径。

在 [pe\_reader.cpp](https://github.com/leeqwind/PESignAnalyzer/blob/master/openssl/src/pe_reader.cpp) 文件中，先确认整个证书表有效、当前至少剩余八字节记录头，然后继续检查记录长度和对齐填充：

CPP

```
const std::size_t length = reader.u32(cursor);
if (length < 8) {
    throw ParseError("WIN_CERTIFICATE length is smaller than its header");
}
if (length > table_end - cursor) {
    throw ParseError("WIN_CERTIFICATE extends beyond the certificate table");
}
// Round using the remaining length, without length + 7 overflow.
const std::size_t padding = (8 - (length & 7U)) & 7U;
if (padding > table_end - cursor - length) {
    throw ParseError("WIN_CERTIFICATE alignment padding exceeds the certificate table");
}
```

对齐时先求填充量，再检查剩余空间，没有直接计算 `length + 7`。正常记录很难看出区别，异常长度才会触发这些检查，让程序在越界前停下来。

第一版的输出要把消息展开：外层是什么内容类型，有多少签名者，签名者通过什么身份关联证书，哪些属性里还有内层签名或时间戳。

读出这些信息后，我没有顺手把它们标成“有效”。`Subject`、`Issuer` 和时间戳日期都是可解析的元数据，是否可信还要经过验证。因此，结果结构从一开始就分别保存解析信息和验证状态。

多签名也分别保留。不同 `WIN_CERTIFICATE`、同一消息中的不同 SignerInfo，以及嵌套消息，都有各自的结果和父级关系。后面要查“到底是哪一个签名失败”，就能沿着这些索引找到对应记录。

![展开记录、签名者和属性后，每条信息都有来源，后续验证也能定位到具体对象]( "展开记录、签名者和属性后，每条信息都有来源，后续验证也能定位到具体对象")

## 三、第一个难点：摘要算法没错，摘要范围可能已经错了

证书信息能读出来了，接下来验证文件内容。拿到 SHA-256 的 OID，再调用 EVP 摘要接口，只完成了计算这一部分。

摘要能否对上，取决于传给它的字节范围。普通的整文件 SHA-256 无法直接用于 PE Authenticode 验证。校验和字段、安全目录项和证书表本身都要排除，否则加入签名数据就会改变被签名对象。节表与磁盘上的实际字节之间，还可能有空洞、填充和附加数据。

对照原版实现、真实文件和独立测试后，摘要处理还要覆盖几种布局：节头排列与节的文件偏移顺序不同，节间有字节，原始节长度与文件对齐边界不整齐，证书表后仍有数据。

只按节头逐个拼接，或把各节长度之和当成后续数据的起点，都可能漏算或重复计算一段区域。这类错误不影响证书解析，CMS 签名本身的数学验证甚至也可能通过，文件完整性检查却会失败。

本项目最终采用了与原 WinCrypt 实现对齐的文件顺序摘要流：先检查布局，再按顺序处理文件字节，跳过校验和、安全目录项和证书表。节间数据、原始填充和证书表后的内容都继续参与计算。

[digest.cpp](https://github.com/leeqwind/PESignAnalyzer/blob/master/openssl/src/digest.cpp) 把下面这些区间送进 EVP。各个偏移已经过布局检查，摘要上下文也已初始化：

CPP

```
const auto hash = [&](std::size_t start, std::size_t end) {
    if (end < start) throw ParseError("Invalid Authenticode digest interval");
    layout.require(start, end - start);
    if (end > start &&
        EVP_DigestUpdate(context.get(), bytes.data() + start, end - start) != 1)
        throw ParseError("Cannot update Authenticode digest");
};
hash(0, checksum);
if (has_security) {
    hash(checksum + 4, security);
    hash(security + 8, cert_size ? cert_offset : bytes.size());
} else hash(checksum + 4, bytes.size());
if (cert_size) {
    hash(cert_offset + cert_size, bytes.size());
}
```

最后一次 `hash` 不能省略：跳过证书表后，文件未必已经结束。表后若还有字节，当前实现仍把它们送进摘要流。

![橙色区域跳过，绿色区域按文件顺序计算摘要，节间空洞、原始填充和证书表后数据也在计算范围内]( "橙色区域跳过，绿色区域按文件顺序计算摘要，节间空洞、原始填充和证书表后数据也在计算范围内")

这套规则由当前样本和回归测试约束。特殊或不规范的 PE 布局，还需与目标平台和更多签名工具交叉核验；几个样本通过，不能证明所有布局都兼容。

回归测试分别构造了节头顺序反转、节间空洞、未对齐的原始节长度和证书表后的附加数据，再修改这些位置中的一个字节，确认摘要检查能发现变化。这样能直接检查“这一个字节到底有没有被算进去”，也防止后续改动漏掉这些区域。

## 四、第二个难点：ASN.1 多包一层，签名就可能验不过

文件摘要处理好以后，CMS 验签又遇到了字节范围问题，这次差别藏在 ASN.1 的包装层里。PE 摘要检查文件，SignedData 内容摘要则把消息内容与签名者签过的属性关联起来。两者处在不同层次，即使都用 SHA-256，输入也完全不同。

传统 Authenticode 的 SPC 内容和 Catalog 的 CTL 内容使用自定义 ASN.1 `SEQUENCE`。计算消息内容摘要时，需要的是序列的内容部分；若把整个 DER 编码值连同外层 tag 和 length 一起算进去，结果就可能与签名中的 `messageDigest` 不一致。

RFC 3161 时间戳不能照用这个处理。它的 CMS 内容由 `OCTET STRING` 承载，值字节里面是完整编码的 `TSTInfo`，这份内部 DER 必须保留。

![SPC/CTL 取序列内容，RFC 3161 取 OCTET STRING 值中的完整 TSTInfo DER，两条路径需要保留的包装层不同]( "SPC/CTL 取序列内容，RFC 3161 取 OCTET STRING 值中的完整 TSTInfo DER，两条路径需要保留的包装层不同")

代码因此分开保存“编码值”和“实际参与内容摘要的字节”，再按消息类型选择。统一用“去掉 ASN.1 外壳”函数处理所有消息，会在修好 SPC 路径的同时破坏时间戳的输入。

[verification.cpp](https://github.com/leeqwind/PESignAnalyzer/blob/master/openssl/src/verification.cpp) 的 PKCS#7 内容读取函数分别返回 `encoded` 和 `content`，后者才用于消息内容摘要：

CPP

```
bool signed_content(PKCS7* p7, Bytes& encoded, Bytes& content) {
    PKCS7* inner = p7 && p7->d.sign ? p7->d.sign->contents : nullptr;
    if (!inner) return false;
    if (PKCS7_type_is_data(inner)) {
        encoded = content = bytes(inner->d.data);
        return encoded.data != nullptr;
    }
    if (!PKCS7_type_is_other(inner) || !inner->d.other) return false;
    encoded = attribute_bytes(inner->d.other);
    if (!encoded.data || encoded.size > max_payload) return false;
    if (inner->d.other->type == V_ASN1_SEQUENCE)
        return sequence_body(encoded, content);
    if (inner->d.other->type == V_ASN1_OCTET_STRING) {
        content = encoded;
        return true;
    }
    return false;
}
```

`sequence_body` 会解析、检查长度编码，不能固定跳过两个字节。`attribute_bytes` 取 `OCTET STRING` 的值字节，保留其中的内部 DER；RFC 3161 专用验证路径通过 `CMS_get0_content` 取得 token 中完整的 `TSTInfo`。

signed attributes 还要单独检查。属性集合有自己的 DER 编码规则，`contentType` 必须与消息一致，`messageDigest` 必须与实际内容一致。重复或畸形的关键属性，也不能挑出一份就继续接受。[CMS 标准](https://www.rfc-editor.org/rfc/rfc5652.html)规定了这些关系。

做到这里，验证流程才串起来：先比对 PE 摘要与消息声明，再核对消息内容摘要和 signed attributes，最后检查签名值。OpenSSL 负责密码学运算，项目仍要确定输入范围，并检查各层数据之间的关系。

## 五、时间戳：标准里的严格要求，与真实 Windows 签名的习惯

时间戳是这次移植中最能体现平台差异的一部分。原版已经支持 PKCS#9 Counter Signature 和 RFC 3161。移植时，除了读出日期，还要逐项核对：时间戳是否绑定当前签名者的签名值，token 自身的签名是否成立，TSA 证书身份是否正确，证书链是否满足要求。

这些检查通过以后，才能用时间戳给出的历史时刻验证签名者证书链。签名者自己声明的 `signingTime` 没有同等证明能力，不能凭这个日期让一张过期证书重新变成可信。

检查真实 Microsoft 签名的时间戳时，又遇到了两个兼容问题：

先是扩展密钥用途。[RFC 3161](https://www.rfc-editor.org/rfc/rfc3161.html#section-2.3) 要求 TSA 证书具有时间戳用途，且这一扩展必须标为 critical。但实际 Authenticode 样本中，有些 TSA 证书只有 `timeStamping` 用途，扩展却不是 critical。对它们直接使用严格的时间戳 purpose 检查，就可能得...