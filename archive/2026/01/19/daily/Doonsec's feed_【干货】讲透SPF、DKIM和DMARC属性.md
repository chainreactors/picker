---
title: 【干货】讲透SPF、DKIM和DMARC属性
url: https://mp.weixin.qq.com/s/TjgOlegpFXdvCvEppTs1iQ
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:33:10.019254
---

# 【干货】讲透SPF、DKIM和DMARC属性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hGAb3jria8J122d2QP7rUGQb27KSFANbeB0XhflQdwic7icGxQzUo4zEHGIhjOQrnAygCxuzxk0SicbnpCS8XoXdwA/0?wx_fmt=jpeg)

# 【干货】讲透SPF、DKIM和DMARC属性

原创

0xNvyao
0xNvyao

安全随笔

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| 声明：请勿利用本公众号文章内的相关技术、工具从事非法测试，如因此造成一切不良后果与文章作者及本公众号无关！ |

*目录：*

*0x01，*SPF概述和实验**

*0x02，DKIM概述和实验*

**0x03，DMARC概述和实验*

**0x04，综合实验

写完这篇文章后，我掌握了邮件安全的这三个属性，希望你们看到这篇文章后，也能有所收获。***

一、SPF**概述和实验**

1、SPF概述

SPF（Sender Policy Framework）发信方策略框架，是一项基于 DNS 的技术。域名管理员在 DNS 中发布一条 TXT 记录，列出所有被授权代表该域名发送邮件的 服务器 IP 地址或域名。

作用：

* 白名单： 告诉接收方“只有从这些 IP 发出的邮件才是我（域名所有者）发的”
* 防伪造： 如果接收方发现邮件来源 IP 不在 SPF 列表里，就会认为该邮件是伪造的。

工作原理：

* 发件人向接收方发送邮件。
* 接收方检查邮件 Return-Path 中的域名。
* 接收方查询该域名的 DNS SPF 记录。
* 比对发信服务器的 IP 是否在记录中。

2、实验

以monitor@monitor.aliyun.com这个发件地址为例，查询它的spf记录：

使用dig工具：

```
➜  dig txt +short monitor.aliyun.com "v=spf1 include:spf3.ocm.aliyun.com -all"
// 继续查spf3.ocm.aliyun.com➜  dig txt +short spf3.ocm.aliyun.com"v=spf1 include:spf-cn.ocm.aliyun.com include:spf-us.ocm.aliyun.com include:spf-sg.ocm.aliyun.com ip4:47.245.193.0/24 -all"
// 继续查spf-cn.ocm.aliyun.com➜  dig txt +short spf-cn.ocm.aliyun.com"v=spf1 ip4:115.124.22.0/23 ip4:115.124.24.0/23 ip4:115.124.26.0/23 ip4:140.205.208.0/22 ip4:106.11.171.128/25 -all"
```

使用nslookup工具：

```
➜  ssh_key nslookup -type=txt monitor.aliyun.comServer:		10.251.1.1Address:	10.251.1.1#53Non-authoritative answer:monitor.aliyun.com	text = "v=spf1 include:spf3.ocm.aliyun.com -all"Authoritative answers can be found from:➜  ssh_key nslookup -type=txt spf3.ocm.aliyun.comServer:		10.251.1.1Address:	10.251.1.1#53Non-authoritative answer:spf3.ocm.aliyun.com	text = "v=spf1 include:spf-cn.ocm.aliyun.com include:spf-us.ocm.aliyun.com include:spf-sg.ocm.aliyun.com ip4:47.245.193.0/24 -all"Authoritative answers can be found from:➜  ssh_key nslookup -type=txt spf-cn.ocm.aliyun.comServer:		10.251.1.1Address:	10.251.1.1#53Non-authoritative answer:spf-cn.ocm.aliyun.com	text = "v=spf1 ip4:115.124.22.0/23 ip4:115.124.24.0/23 ip4:115.124.26.0/23 ip4:140.205.208.0/22 ip4:106.11.171.128/25 -all"Authoritative answers can be found from:
```

由上面阿里云邮箱的txt记录可以看到，如果发信 IP 实在是太多了，一条 TXT 记录（有 255 字符限制）放不下，所以它做了进一步的拆分。

举个真实例子，找一封阿里云发送的告警邮件，查看邮件头内容，其中有这么一段：

```
Received-SPF: Pass (protection.outlook.com: domain of monitor.aliyun.com designates 140.205.209.137 as permitted sender) receiver=protection.outlook.com; client-ip=140.205.209.137; helo=out209-137.dm.aliyun.com; pr=C
```

注意其中的client-ip=140.205.209.137，这个ip包含在前面我们解析的阿里云txt记录中（ip4:140.205.208.0/22）。

总结下就是接收方在建立连接时，获取发信服务器的 **真实 IP 地址**，然后通过 DNS 查询发送方域名下的 **IP 白名单**；如果该 IP 在名单内，则证明发送服务器是经过域名所有者授权的合法来源。

二、DKIM**概述和实验**

1、DKIM概述

DKIM (DomainKeys Identified Mail) - 域名密钥识别邮件 是一种基于数字签名的验证方式。它在邮件的页眉（Header）中添加一个加密签名。

作用：

* 身份校验： 确认邮件确实起源于该域名。
* 内容完整性： 确保邮件在传输过程中没有被篡改。如果邮件正文或关键页眉被改动，签名校验就会失败。

工作原理：

* 发件方服务器使用私钥对邮件内容和部分页眉进行哈希计算并签名。
* 邮件发出，带着这个 DKIM-Signature。
* 接收方服务器通过 DNS 获取该域名的公钥。
* 使用公钥解密签名，比对哈希值。

2、实验

还是以monitor@monitor.aliyun.com这个发件地址的邮件为例，查看邮件头，里面有这么个字段DKIM-Signature，它是电子邮件身份的「数字签名」。

```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;	d=monitor.aliyun.com; s=s1024;	t=1768545992; h=Date:From:To:Message-ID:Subject:MIME-Version:Content-Type;	bh=YApYwrn4cxGT0tgfykTL6FnnRKmpvBxsUfR0wVLzYxc=;	b=Z0fi0hzYam3mHDXb0uSddX/XzFnHW2EdxSwZirnWFYYsTdiXMEobdBYbVI31nT8vZUoILHquyta2qBtYTplCIOq3A2CF08kBgO8G0dbR2DrvnfZ3RyuhgfIhbbxOBtE+ms1ByR7HajatguSB5wSwpxVffar5QXhDuQJ8BkUITFg=
```

这份来自 monitor.aliyun.com（阿里云监控）的 DKIM 签名非常有代表性，它展示了典型的生产环境配置。

| **标签** | **取值** | **安全/技术含义** |
| --- | --- | --- |
| **v=1** | `1` | 协议版本，固定为 1。 |
| **a=rsa-sha256** | `rsa-sha256` | 算法，目前工业界的标准组合（RSA 加密 + SHA-256 哈希）。 |
| **c=relaxed/relaxed** | `relaxed/relaxed` | 规范化模式。允许邮件在传输中发生微小的格式变动（如多一个空格）而不至于导致签名失效。 |
| **d=monitor.aliyun.com** | `monitor.aliyun.com` | **发件域名**。注意这是 `aliyun.com` 的子域名，说明阿里云为其监控系统使用了独立的二级域名进行身份隔离。 |
| **s=s1024** | `s1024` | **选择器**。这暗示了该公钥的长度可能是 **1024位**。你可以通过 `s1024._domainkey.monitor.aliyun.com` 查询。 |
| **t=1768545992** | `1768545992` | **时间戳 (Timestamp)**。这是邮件发送时的 Unix 时间戳。转换后约为 **2026年1月17日**。它有助于防止重放攻击（Replay Attack）。 |
| **h=Date:From...** | `Date:From:To:Message-ID:Subject...` | **保护字段**。列出了哪些 Header 参与了签名。注意这里包含了 `Message-ID`，比之前的更严格，防止邮件标识符被篡改。 |
| **bh=...** | `YApY...Yxc=` | **正文哈希**。邮件正文经过哈希后的“指纹”。 |
| **b=...** | `Z0fi...ITFg=` | **数字签名结果**。由私钥对以上信息加密生成的 Base64 字符串。 |

既然是签名，那必须接收方需要能查到验证签名所需的公钥，然后才能验证签名是否正确，那如何查询发送方的公钥呢？

完整的获取流程：

1、拼接查询地址的公式

接收方不会盲目地去查域名的根记录，而是按照以下标准格式构造一个子域名：

[Selector].\_domainkey.[Domain]

拿你刚才提供的那个 aliyun 签名举例，从DKIM-Signature字段提取出 s=s1024 和 d=monitor.aliyun.com：

• s (Selector) = s1024

• d (Domain) = monitor.aliyun.com

接收方会自动拼接出：s1024.\_domainkey.monitor.aliyun.com

2、发起 DNS 查询：接收方向 DNS 服务器请求 s1024.\_domainkey.monitor.aliyun.com 的 TXT记录

命令方式查询（dig/nslookup）：

```
➜  ssh_key dig txt +short s1024._domainkey.monitor.aliyun.com"v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDFwkfoN5eNZh2nx1qMTAyfYPhG5RfpjSng5aNh6JL6MTa2BABnD+05xZ3o7j9nT7CoVLVL2mEzj12foAG4J23qnCDf3h32lmZSLTs3sZsWFzwFSMKAXjNH3OCV4MFc72BCLy+gv81wFwsmcHInOZ4tMiw5jG4B683P/1KbeKbeswIDAQAB"
➜  ssh_key nslookup -type=txt s1024._domainkey.monitor.aliyun.comServer:		10.251.1.1Address:	10.251.1.1#53Non-authoritative answer:s1024._domainkey.monitor.aliyun.com	text = "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDFwkfoN5eNZh2nx1qMTAyfYPhG5RfpjSng5aNh6JL6MTa2BABnD+05xZ3o7j9nT7CoVLVL2mEzj12foAG4J23qnCDf3h32lmZSLTs3sZsWFzwFSMKAXjNH3OCV4MFc72BCLy+gv81wFwsmcHInOZ4tMiw5jG4B683P/1KbeKbeswIDAQAB"Authoritative answers can be found from:
```

网页查询（https://mxtoolbox.com/SuperTool.aspx）：

![](https://mmbiz.qpic.cn/mmbiz_png/hGAb3jria8J11kyU7l8k5YqBvzdXMfQHQoicRMVkovklLTXXmEFeIAEcWVyISRyJlw1DCOLUj517wWzHkde8Lt8Q/640?wx_fmt=png&from=appmsg)

3、验证签名

所以总结下DKIM的原理就是，拿到邮件所有原始信息以及邮件头中的DKIM-Signature签名字段后，会通过dns去查询到发送方的DKIM使用的公钥，然后使用公钥去验证签名，如果验证通过说明邮件原始信息没有被篡改而且是真实发送方发件的。

三、DMARC**概述和实验**

1、DMARC概述

DMARC（Domain-based Message Authentication, Reporting, and Conformance）是在 SPF 和 DKIM 之上的管理层。它通过 DNS 记录告诉接收方：如果 SPF 或DKIM 验证失败了，该怎么办？

作用：

1、指挥官角色：定义“生死策略” (Policy)

这些属性直接决定了接收方邮件服务器在发现 SPF/DKIM 验证失败后，该如何处置这封邮件。

* p= (Policy)：主域名的核心策略

+ none：只看不管。仅用于监控，不拦截邮件
+ quarantine：软拦截。将邮件扔进用户的垃圾箱
+ reject：硬拦截。直接退信，让对方根本发不进来

* sp= (Subdomain Policy)：专门针对子域名（如 m.example.com）的策略

+ 作用：如果你主域名想用 none 观察，但想保护子域名不被冒充，可以设置 p=none; sp=reject;

* pct= (Percentage)：策略执行比例

+ 作用：例如 pct=20。如果 100 封伪造邮件进来，只有 20 封会被拦截，另外 80 封放行。这是安全运维中平滑灰度切换的利器。

2、对齐官角色：确保“人皮一致” (Alignment)

这是 DMARC 的精髓，也是它能封杀“李鬼”邮件的关键。

* **`aspf=` (SPF Alignment)**：

+ `r` (Relaxed, 默认)：允许父域与子域匹配（如 `example.com` 和 `mail.example.com`）
+ `s` (Strict)：必须**分毫不差**

* **`adkim=` (DKIM Alignment)**：

+ 作用：确保邮件正文显示的 `From` 域名与底层数字签名的域名是一家人
+ **重要性**：防止黑客用自己合法域名的“真签名”去发送冒充你公司域名的“假邮件”

注意，aspf和adkim两个属性有默认值，一般你查询dns记录看不到这两个字段。

### 3、情报官角色：数据回传与审计 (Reporting)

如果没有这两个属性，你作为安全员就像在黑盒里操作，完全不知道外面的攻击情况。

* **`rua=` (Aggregate Reporting)**：

+ 作用：**统计日报**。接收 XML 格式的汇总报告
+ 价值：可以看到全球有哪些 IP 在尝试发你的邮件，其中 SPF 、DKIM 过没过

* **`ruf=` (Forensic Reporting)**：

+ 作用：**逐封取证**。一旦某封邮件验证失败，立即发一封详细的告警邮件给你
+ 现状：涉及隐私保护，现在很多大型服务商（如 Gmail）默认不再发送此类报告

2、实验：

查询 DMARC 记录的方法与查询 SPF 非常相似，唯一的区别在于 DMARC 记录固定存在于域名的一个特定子域名下，即 \_dmarc.域名

使用 dig (Linux/macOS)：

```
➜  ssh_key dig +short txt _dmarc.monitor.aliyun.com"v=DMARC1;p=none;rua=mailto:dmarc_report@service.aliyun.com"
```

使用 nslookup (Windows/通用)：

```
➜  ssh_key nslookup -type=txt _dmarc.monitor.aliyun.comServer:		10.251.1.1Address:	10.251.1.1#53Non-authoritative answer:_dmarc.monitor.aliyun.com	text = "v=DMARC1;p=none;rua=mailto:dmarc_report@service.aliyun.com"Authoritative answers can be found from:
```

那么monitor.aliyun.com的dmarc记录的解读如下：

| **标签** | **取值** | **详细解读** |
| --- | --- | --- |
| **v=DMARC1** | `DMARC1` | **版本标识**：必须位于记录的最开头，声明这是一条 DMARC 记录。 |
| **p=none** | `none` | **策略 (Policy)**：这是最关键的设置。`none` 表示**不干预/监控模式**。即使邮件没有通过 SPF 或 DKIM 验证，接收方服务器（如 Gmail, Outlook）依然会**放行**邮件并投递到收件箱。 |
| **rua=...** | `mailto:dmarc_report...` | **聚合报告地址**：告诉全球的邮件服务器，每天将验证结果的统计报告（XML 格式）发送到阿里云的这个邮箱。 |

所以总结下，DMARC...