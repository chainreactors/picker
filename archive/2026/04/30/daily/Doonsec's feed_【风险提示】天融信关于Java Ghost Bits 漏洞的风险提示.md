---
title: 【风险提示】天融信关于Java Ghost Bits 漏洞的风险提示
url: https://mp.weixin.qq.com/s/KI-n1SESpCUA4hqJQ78Oog
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:37:33.564674
---

# 【风险提示】天融信关于Java Ghost Bits 漏洞的风险提示

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TWq54w4h0qRMPq2VYbtxwpUCCL06Bz6f08p7LgndCaB7NGHt1osd1TDv2ibDN12foNkfKn5xS5TRtTwQFo1iasYfzlFaRTrH5cGYy2f5sd6KY/0?wx_fmt=jpeg)

# 【风险提示】天融信关于Java Ghost Bits 漏洞的风险提示

天融信应急响应
天融信应急响应

天融信阿尔法实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/TWq54w4h0qSV9hZUPsetrokELuYqr6XIiaSzCFy49VDpZcJ6k3icaGAn41PYNt5ZhRBcTq2mCoPoYWgrtMBG6ua3UaZgdnW5NVQW7r72n7KZg/640?wx_fmt=png&from=appmsg)

**0x00 背景介绍**

---

近日，天融信阿尔法实验室监测到安全研究员披露了Java生态中的一种新型安全问题，通常被称为Ghost Bits（幽灵比特），其根源在于“字符视图”与“字节视图”不一致，可能引发部分安全防护产品绕过、路径穿越、文件上传绕过、CRLF 注入、反序列化绕过等风险。该问题不是单一 CVE，而是一类底层编码与解析逻辑缺陷，影响面较广，建议受影响用户尽快排查并修复。

**0x01 漏洞描述**

---

Java 是目前应用最广泛的编程语言之一，从 Web 服务器、企业应用到嵌入式系统都有其身影。Java 的类型系统中，char类型为 16 位 Unicode 代码单元，而byte类型仅为 8 位。当代码中发生char -> byte的强制类型转换、位运算掩码、OutputStream.write(int)、DataOutputStream.writeBytes(String) 等时，高 8 位会被静默丢弃，只保留低 8 位，被丢弃的高位数据即被称为 "Ghost Bits"。

Ghost Bits 风险的核心在于，上层安全检查看到的字符串语义，与底层最终执行的字节语义可能不一致。上层按字符语义做校验时看到的是安全字符串，而底层按字节语义执行时，低 8 位可能折叠成危险的 ASCII 字节，从而触发真实漏洞。经过身份认证的攻击者可通过精心构造的 Unicode 字符输入，绕过业务校验、路径检查等安全机制，实现文件上传绕过、路径穿越、任意文件读取、认证绕过、SMTP 注入、HTTP 请求走私、Header 注入等多种攻击。该风险已在 Tomcat、Spring Framework、Jetty、Fastjson、Jackson、Openfire、Jira、Confluence 等多个主流 Java 组件中被证实存在实际可利用的漏洞。

**0x02 漏洞编号**

##

---

暂无

**0x03 漏洞等级**

---

高危

**0x04 受影响版本**

##

---

所有存在以下高危代码写法的 Java 应用和组件：

1、(byte) ch - char 到 byte 的强制类型转换

2、ch & 0xff / ch & 255 / 0xff & ch - 位运算截断

3、baos.write(ch) - 直接将 char 写入字节流

4、DataOutputStream.writeBytes(String s) - 按字节写入字符串

5、OutputStream.write(int) - 直接写入 int 值的低 8 位

6、StringBufferInputStream.read() - 字符流到字节流转换

7、String.getBytes(int, int, byte[], int) - 过时的字节获取方法

8、RandomAccessFile.writeBytes() - 按字节写入

9、URLDecoder.decode() - URL 解码相关处理

已知受影响的 Java 组件：

Apache Tomcat、Spring Framework、Eclipse Jetty、Fastjson、Jackson、Openfire、Apache HttpClient、Angus Mail / Jakarta Mail、Jira、Confluence、GeoServer

**0x05 修复建议**

---

1、临时缓解措施

如果暂时无法完成代码修复和组件升级，可采取以下缓解措施：

（1）对用户输入进行严格的字符范围校验，拒绝包含高Unicode字符的关键输入字段（文件名、路径、邮箱地址、HTTP Header 等）。

（2）若非必要，避免在互联网上暴露存在风险的 Java 应用服务。

2、代码修复

（1）禁止隐式 char -> byte 截断：避免使用(byte) ch等强制类型转换写法，改用显式的字符编码转换，如StandardCharsets.UTF\_8.encode()。

（2）统一校验与执行语义：先把输入还原成最终会被执行的字节语义，再进行安全校验，确保检查和执行在同一语义空间。

（3）输入规范化：在输入校验阶段前对输入进行统一的编码规范化处理。

（4）升级受影响组件：将受已知漏洞影响的 Java 组件按照官方安全公告升级至安全版本。

## **0x06 声明**

---

天融信阿尔法实验室拥有对此公告的修改和解释权，如欲转载，必须保证此公告的完整性。由于传播、利用此公告而造成的任何后果，均由使用者本人负责，天融信阿尔法实验室不为此承担任何责任。

天融信阿尔法实验室成立于2011年，一直以来，阿尔法实验室秉承“攻防一体”的理念，汇聚众多专业技术研究人员，从事攻防技术研究，在安全领域前瞻性技术研究方向上不断前行。作为天融信的安全产品和服务支撑团队，阿尔法实验室精湛的专业技术水平、丰富的排异经验，为天融信产品的研发和升级、承担国家重大安全项目和客户服务提供强有力的技术支撑。

![](https://mmbiz.qpic.cn/mmbiz_png/H6W1QCHf9dGfIEDOlNXXDTqOpRkEkicJakNxM37lzr8eRJRibEfxkwBibg9KpVh6nibXHoG4xC6KyGFtTd4TOe6GyA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/H6W1QCHf9dGfIEDOlNXXDTqOpRkEkicJawf8nKyKatopPJiaayibAUCvfTVFKfxVDInq2TiaUib6xhmhpLK4Zqscgyg/640?wx_fmt=jpeg)

天融信

阿尔法实验室

长按二维码关注我们

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/H6W1QCHf9dGDWkSzfzMzTbO3A3TNOlV25ib6QxMqggGr0xEsDy3YnQUDt6zApFEp9LEAiaLctFdghjstu66PUWzA/0?wx_fmt=png)

天融信阿尔法实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/H6W1QCHf9dGDWkSzfzMzTbO3A3TNOlV25ib6QxMqggGr0xEsDy3YnQUDt6zApFEp9LEAiaLctFdghjstu66PUWzA/0?wx_fmt=png)

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