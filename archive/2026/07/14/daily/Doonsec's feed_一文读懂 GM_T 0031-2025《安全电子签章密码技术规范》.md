---
title: 一文读懂 GM/T 0031-2025《安全电子签章密码技术规范》
url: https://mp.weixin.qq.com/s/wqp_Ht5OlU_hDIZ_1t1-GA
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:45:27.614890
---

# 一文读懂 GM/T 0031-2025《安全电子签章密码技术规范》

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZaibroIiatwe3qzcsu9Kn4iafFqtiaPyVkibY47fWeewAGn5oqbx0yTIzOZSPXWGeLMVGvXALfjhu7ib2S0oiaNNnlvhzety4fU9kNB0UXhOsEweLE/0?wx_fmt=jpeg)

# 一文读懂 GM/T 0031-2025《安全电子签章密码技术规范》

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一文读懂 GM/T 0031-2025

《安全电子签章密码技术规范》

电子印章 · 电子签章 · 时间戳 · ASN.1 · SM2签名

01

PART

密码应用安全机制

SECURITY MECHANISM

本标准主要按照《电子签名法》的要求，采用密码技术从安全数据格式定义以及安全处理流程两个方面来规范并保障电子印章、电子签章的安全性。

首先，安全电子印章和电子签章的数据结构安全性是基于 PKI 公钥密码技术，采用数字签名等技术应用来统一定义。

其次，电子印章和电子签章的生成和验证流程需要遵循严格的数据格式定义，经历严谨的密码运算过程，环环相扣，从而确保电子印章和电子签章的真实性、数据完整性，以及制章或签章行为的不可否认性。

安全电子签章是通过采用 PKI 公钥密码技术，将数字图像处理技术与电子签名技术进行结合，以电子形式对加盖印章图像数据的电子文档进行数字签名，以确保文档来源的真实性以及文档的完整性，防止对文档未经授权的篡改，并确保签章行为的不可否认性。

为了确保电子印章的完整性、不可伪造性，以及合法用户才能使用，需要定义一个安全的电子印章数据格式，通过数字签名，将印章图像数据与签章者等印章属性进行安全绑定，形成安全电子印章。在使用印章过程中，应对电子印章进行安全性验证。

在使用电子印章对各种文档进行电子签章过程中，签章者通过数字签名对文档数据进行签章处理，从而达到与传统纸质文件盖章操作相同的可视化效果，同时又利用数字签名技术保障了文档数据的真实性、完整性以及签章者行为的不可否认性。

02

PART

密码应用协议

CRYPTOGRAPHIC PROTOCOL

2.1 电子印章

2.1.1 数据格式

2.1.1.1 印章数据结构

电子印章由**印章信息、制章者证书、签名算法标识、签名值、时间戳**等部分组成，其数据结构如下。

电子印章数据的 ASN.1 定义为：

...asn1

SESeal ::= SEQUENCE {

eSealInfo SES\_SealInfo, -- 印章信息

cert OCTET STRING, -- 制章者证书

signAlgID OBJECT IDENTIFIER, -- 签名算法标识

signedValue BIT STRING, -- 签名值

timeStamp [0] BIT STRING OPTIONAL -- 对签名值的时间戳 [新增]

}

**说明**：与 GB/T 38540-2020 相比，SESeal 结构中新增了 timeStamp 可选字段，用于对签名值加盖时间戳，增强印章的时效性保障能力。

2.1.1.2 印章信息

2.1.1.2.1 数据结构

印章信息 eSealInfo 由**印章头、印章标识、印章属性、印章图像数据、自定义数据**等部分组成。

印章信息 eSealInfo 的 ASN.1 定义如下：

...asn1

SES\_SealInfo ::= SEQUENCE {

header SES\_Header, -- 印章头

esID IA5String, -- 印章标识

property SES\_ESPropertyInfo, -- 印章属性

picture SES\_ESPictureInfo, -- 印章图像数据

extDatas ExtensionDatas OPTIONAL -- 自定义数据

}

2.1.1.2.2 印章头

印章头由**头标识、版本号和厂商标识**等组成。

印章头的 ASN.1 定义为：

...asn1

SES\_Header ::= SEQUENCE {

ID IA5String, -- 头标识

version INTEGER, -- 印章版本号

Vid IA5String -- 厂商标识

}

其中：

ID：固定值 "ES"。

version：电子印章数据结构版本号，本标准设定数值为 5，代表当前版本为 v5。

Vid：电子印章厂商标识，在互联互通时，用于识别不同的软件厂商实现。

**说明**：与 GB/T 38540-2020 相比，version 从 4（v4）升级为 5（v5）。

2.1.1.2.3 印章标识

esID：区分电子印章的唯一标识编码，用于查找和索引其他信息。

2.1.1.2.4 印章属性

印章属性由**印章类型、印章名称、签章者证书信息类型、签章者证书信息列表、制作时间、有效期起始时间、有效期终止时间**等部分组成。

印章属性的 ASN.1 定义为：

...asn1

SES\_ESPropertyInfo ::= SEQUENCE {

type INTEGER, -- 印章类型

name UTF8String, -- 印章名称

certListType INTEGER, -- 签章者证书信息类型

certList SES\_CertList, -- 签章者证书信息列表

createDate GeneralizedTime, -- 印章制作时间

validStart GeneralizedTime, -- 印章有效期起始时间

validEnd GeneralizedTime -- 印章有效期终止时间

}

其中：

type：代表印章类型，可根据业务需要自定义。

name：印章名称，如"××公司财务专用章"，对于在公安部门进行备案的印章，其印章名称与备案的名称保持一致。

certListType：签章者证书信息类型，1——数字证书，2——数字证书的杂凑值。

certList：签章者证书信息列表，一个或多个签章者证书或签章者证书杂凑值组成的列表。

createDate：印章制作时间。

validStart：印章有效期起始时间。

validEnd：印章有效期终止时间。

...asn1

SES\_CertList ::= CHOICE {

certs CertInfoList, -- 签章者证书

certDigestList CertDigestList -- 签章者证书杂凑值

}

CertInfoList ::= SEQUENCE OF Cert

CertDigestList ::= SEQUENCE OF CertDigestObj

Cert ::= OCTET STRING

-- Cert 符合 GB/T 20518 中 Certificate 定义，按 DER 编码格式存放

CertDigestObj ::= SEQUENCE {

type ObjType, -- 自定义类型

value CertDigestValue -- 证书杂凑值

}

ObjType ::= PrintableString

CertDigestValue ::= OCTET STRING

2.1.1.2.5 印章图像数据

印章图像数据由**图像类型、图像数据、图像显示宽度和图像显示高度**等部分组成。

印章图像数据的 ASN.1 定义为：

...asn1

SES\_ESPictureInfo ::= SEQUENCE {

type IA5String, -- 图像类型

data OCTET STRING, -- 图像数据

width INTEGER, -- 图像显示宽度

height INTEGER -- 图像显示高度

}

其中：

type：印章图像数据格式类型，如 GIF、BMP、JPG、PNG、SVG 等。

data：印章图像数据，机构的电子印章宜采用相关国家管理部门指定的印模。

width：图像显示宽度，单位为毫米（mm）。

height：图像显示高度，单位为毫米（mm）。

2.1.1.2.6 自定义数据

自定义数据包含一系列自定义属性字段，可用于支持电子印章扩展特性，其 ASN.1 定义为：

...asn1

ExtensionDatas ::= SEQUENCE SIZE (0..MAX) OF ExtData

ExtData ::= SEQUENCE {

extnID OBJECT IDENTIFIER, -- 自定义扩展字段标识

critical BOOLEAN DEFAULT FALSE, -- 自定义扩展字段是否关键

extnValue OCTET STRING -- 自定义扩展字段数据值

}

2.1.1.3 制章者证书

cert：对电子印章进行签名的制章者的数字证书，应符合 GB/T 20518 中 Certificate 定义，按 DER 编码格式存放。

2.1.1.4 签名算法标识

signAlgID：代表签名算法 OID 标识，应符合 GB/T 33560 的规定。

示例：基于 SM2 算法和 SM3 算法的签名 OID 为 1.2.156.10197.1.501。

2.1.1.5 签名值

signedValue：制章者对电子印章格式中印章信息域 SES\_SealInfo，按 SEQUENCE 方式组成的信息内容进行数字签名所得的结果。

如果签名算法使用 SM2，应符合 GB/T 35276 的规定。

2.1.1.6 时间戳 【新增】

timeStamp：对签名值 signedValue 的时间戳，应符合 GB/T 20520—2025 的规定，时间戳格式按 DER 编码存放。该字段为可选字段。

时间戳令牌（TimeStampToken）采用 ContentInfo 结构封装，内部为 SignedData 结构，核心时间信息定义在 TSTInfo 结构中。TSTInfo 包含版本号（v2）、TSA 安全策略 OID、消息摘要（MessageImprint，其 hashedMessage 为 signedValue 的杂凑值）、时间戳序列号、可信时间 genTime（UTC 格式）、时间精度 accuracy、随机数 nonce 等字段。完整的数据结构定义及签名验签过程见附录 B。

**说明**：本字段为 GM/T 0031-2025 相比 GB/T 38540-2020 的新增内容，在电子印章数据格式层面引入时间戳机制，为印章的创建时间提供可信证明。

2.1.2 电子印章生成流程

电子印章生成流程如下：

a) **验证制章者证书的有效性**。验证项至少包括：**制章者证书信任链验证、制章者证书有效期验证、制章者证书是否被撤销、密钥用法是否正确**。如果制章者证书验证失败，返回错误代码并退出生成流程。

**说明**：本步骤为 GM/T 0031-2025 相比 GB/T 38540-2020 的新增步骤，在生成印章前先验证制章者证书，确保制章者身份的合法性。

b) 按 2.1.1.2 定义的数据格式，将**印章头、印章标识、印章属性、印章图像数据、自定义数据**等数据按 SEQUENCE 方式组成印章信息；

c) 根据签名算法标识 signAlgID，对上述步骤 b) 的印章信息域进行数字签名运算，形成签名值；

d) **生成时间戳**。利用上述签名值产生相应的时间戳。

**说明**：本步骤为 GM/T 0031-2025 相比 GB/T 38540-2020 的新增步骤，在印章生成过程中增加时间戳，为印章创建时间提供可信证明。

e) 将上述步骤 b)、c) 和 d) 的数据以及制章者证书、签名算法标识组成 2.1.1.1 定义的电子印章数据格式。

2.1.3 电子印章验证流程

电子印章验证流程如下：

a) **验证电子印章数据格式的正确性**

按照电子印章格式解析电子印章，验证是否符合 2.1.1 定义的电子印章数据格式。

如果电子印章数据格式不正确，则验证失败，返回错误代码并退出验证流程。

b) **验证电子印章签名值是否正确**

根据**印章信息、制章者证书、签名算法标识**来验证电子印章中的签名值是否正确。

如果电子印章签名验证失败，返回错误代码并退出验证流程。

c) **验证制章时间的有效性** 【新增】

根据印章属性中的印章制作时间 createDate，验证在制章时间点上电子印章数据是否有效。

如果制章时间验证失败，返回错误代码并退出验证流程。

**说明**：本步骤为 GM/T 0031-2025 相比 GB/T 38540-2020 的新增步骤，确保印章在制作时间点是有效的。

d) **验证电子印章制章者证书的有效性** 【增强】

验证制章者证书的有效性，验证项至少包括：**制章者证书信任链验证、制章者证书有效期验证、制章者证书是否被撤销、密钥用法是否正确**。

如果制章者证书验证失败，需结合制章时间综合判断：

若制章者证书因有效期过期或吊销导致验证失败，但在制章时间点上制章者证书是有效的，则记录为提示信息，继续进行后续验证；

若在制章时间点上制章者证书也是无效的（已过期或已吊销），则返回错误代码并退出验证流程；

若制章者证书因信任链验证或密钥用法不正确导致验证失败，则返回错误代码并退出验证流程。

**说明**：与 GB/T 38540-2020 相比，本步骤细化了证书失效的判定逻辑。GB/T 38540-2020 原逻辑为"如果制章者证书验证失败，返回错误代码并退出验证流程"，未区分失效原因和时间点。GM/T 0031-2025 增加了制章时间点的综合判断，区分了证书过期/吊销场景，使验证逻辑更加精细合理。

e) **验证电子印章的有效期**

根据印章属性中的印章有效期起始时间 validStart 和有效期终止时间 validEnd，验证电子印章是否过期。

如果电子印章已过期，则验证失败，返回错误代码并退出验证流程。

f) **验证电子印章中时间戳的有效性** 【新增】

如果电子印章数据中包含时间戳（即 2.1.1.1 中 SESeal 的 timeStamp 字段存在），则应进行时间戳的有效性验证。

若时间戳验证不通过，则返回错误代码并退出验证流程。

比对时间戳中的时间与印章制作时间 createDate，若制作时间晚于时间戳中的时间，则返回错误代码并退出验证流程。

**说明**：本步骤为 GM/T 0031-2025 相比 GB/T 38540-2020 的新增步骤，验证印章关联的时间戳有效性。

g) 如果上述步骤都验证成功，则电子印章验证正确有效，可正常退出验证流程。

2.2 电子签章

2.2.1 数据格式

2.2.1.1 签章数据结构

电子签章数据由**签章信息、签章者证书、签名算法标识、签名值、时间戳**等组成。

电子签章数据的 ASN.1 定义为：

...asn1

SES\_Signature ::= SEQUENCE {

toSign TBS\_Sign, -- 签章信息

cert OCTET STRING, -- 签章者证书

signatureAlgID OBJECT IDENTIFIER, -- 签名算法标识

signature BIT STRING, -- 签名值

timeStamp [0] BIT STRING OPTIONAL -- 对签名值的时间戳

}

2.2.1.2 签章信息

签章信息由**版本号、电子印章、签章时间、原文杂凑值、原文属性、自定义数据**等组成。

...asn1

TBS\_Sign ::= SEQUENCE {

version INTEGER, -- 电子签章版本号

eseal SESeal, -- 电子印章

timeInfo GeneralizedTime, -- 签章时间

dataHash BIT STRING, -- 原文杂凑值

propertyInfo IA5String, -- 原文数据的属性

extDatas [0] ExtensionDatas OPTIONAL -- 自定义数据

}

其中：

version：电子签章版本号，该版本号与电子印章版本号保持一致，本标准设定数值为 5，代表当前版本为 v5。

eseal：生成电子签章使用的电子印章。

timeInfo：电子签章对应的时间，可以是 GeneralizedTime 时间。

dataHash：待签名原文的杂凑值。

propertyInfo：原文数据的属性，如文档 ID、日期、段落、原文内容的字节数、指示信息、签名保护范围等，此部分受签名保护。propertyInfo 的具体结构可自行定义，但至少应包含签名保护范围。

extDatas：厂商自定义数据。

**说明**：与 GB/T 38540-2020 相比，version 从 4（v4）升级为 5（v5），与电子印章版本号保持一致。

2.2.1.3 签章者证书

cert：签章者的数字证书，应符合 GB/T 20518 的规定，按 DER 编码格式存放。

2.2.1.4 签名算法标识

signatureAlgID：签名算法标识，应符合 GB/T 33560 的规定，应与签章者证书中的算法声明保持一致。

示例：基于 SM2 算法和 SM3 算法的数字签名 OID 为 1.2.156.10197.1.501。

2.2.1.5 签名值

signature：签章者对签章信息 TBS\_Sign 进行数字签名的结果。注意签名过程中的原文杂凑所采用的算法应与签名算法保持协调，如果签名算法是 SM2，则杂凑算法应采用 SM3 算法。

如果签名算法使用 SM2，应符合 GB/T 35276 的规定。

2.2.1.6 时间戳

timeStamp：对签名值 signature 的时间戳，应符合 GB/T 20520—2025 的规定，时间戳格式按 DER 编码存放。

时间戳令牌（TimeStampToken）采用 ContentInfo 结构封装，内部为 SignedData 结构，核心时间信息定义在 TSTInfo 结构中。TSTInfo 包含版本号（v2）、TSA 安全策略 OID、消息摘要（MessageImprint，其 hashedMessage 为 signature 的杂凑值）、时间戳序列号、可信时间 genTime（UTC 格式）、时间精度 accuracy、随机数 nonce 等字段。验证过程包括：验证时间戳令牌格式正确性、验证签名值、验证 TSA 证书有效性（含 id-kp-timeStamping 扩展密钥用途）、验证摘要匹配、验证时间戳时间。...