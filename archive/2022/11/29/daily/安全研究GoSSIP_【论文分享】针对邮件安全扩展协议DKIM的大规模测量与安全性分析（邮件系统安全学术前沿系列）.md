---
title: 【论文分享】针对邮件安全扩展协议DKIM的大规模测量与安全性分析（邮件系统安全学术前沿系列）
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493411&idx=2&sn=26bc3d8370764f7872b7b262659491df&chksm=c063c9faf71440ec7a61eb8331358d6ff79c1879ed4f2d2a3f648662c8f07cad9c92601097eb&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-11-29
fetch_date: 2025-10-04T00:01:05.410377
---

# 【论文分享】针对邮件安全扩展协议DKIM的大规模测量与安全性分析（邮件系统安全学术前沿系列）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MicoqDk7wVOJfcybugXG0uhBcqhIJLgKxUsYLLsDDOBKqhLnp5goVZWw/0?wx_fmt=jpeg)

# 【论文分享】针对邮件安全扩展协议DKIM的大规模测量与安全性分析（邮件系统安全学术前沿系列）

安全研究GoSSIP

编者荐语：

寒假开始了！！！我们从本周起为大家转载来自NISL实验室的高质量论文笔记！！！

以下文章来源于NISL实验室
，作者王楚涵

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM766Bv1SQgibFlalH9bqtncibzFunlpyJGeVJiaKNlDOeyfQ/0)

**NISL实验室**
.

网络与信息安全实验室(NISL@THU)，专注于网络、系统、应用、人工智能安全教学与研究，在国际四大安全会议发表三十余篇论文，成果在业界产生了广泛影响力。孕育了蓝莲花、紫荆花等知名战队，发起了网安国际学术论坛InForSec。

今天分享的论文主题为邮件协议安全，由来自清华大学、华北计算技术研究所、奇安信及Coremail的研究人员共同完成。DomainKeys Identified Mail（DKIM）是一个用于保护电子邮件内容的完整性认证协议。该协议2011年被正式标准化[2]，目前已被雅虎、谷歌和其他知名电子邮件服务提供商所采用。由于DKIM协议的特性，对其进行大规模测量是非常困难的。因此，DKIM的现实部署情况及可能存在的安全风险长期缺乏客观而严谨的分析研究。论文首次对DKIM协议的部署情况进行了大规模测量，并深入分析其安全问题。论文收集了五年（2015-2022）时间内Passive DNS数据集所有相关的DKIM记录（共950万条）和来自于真实邮件日志中的4.6亿条DKIM签名记录，对这些数据进行了深入分析，并基于分析结果对Alexa前100万个域名的DKIM部署情况及安全缺陷进行了测量研究。研究发现，DKIM协议的密钥管理和签名实现的安全问题在现实世界中广泛存在，即使是全球知名的电子邮件供应商（如Gmail和Mail.ru）也存在相关问题。作者建议邮件服务器管理人员应该更加关注DKIM部署的系统性问题，安全社区也应当从协议设计的角度进一步解决上述问题。论文发表于网络安全领域顶级学术会议USENIX Security 2022（录取率 18.6%）。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MwjLzc88UMLhhicR5gGmLQ27IvmHbOiaDGr27KibNJN9QrYXxLGf8fyQ1g/640?wx_fmt=png)

全文共4200字，阅读时间约12分钟。

*作者介绍：**王楚涵，清华大学网络与系统安全实验室博士研究生，研究方向为网络安全、数据驱动安全，导师为段海新教授与陈建军助理教授。曾在网络安全顶级学术会议USENIX Security上发表多篇论文。目前主要从事电子邮件相关安全研究，研究成果帮助Google，Apple，Yandex 等知名互联网公司修复了漏洞。同时作为清华大学CTF战队Redbud队员，曾获得2020年ByteCTF冠军等奖项。*

*联系邮箱：wch22@mails.tsinghua.edu.cn*

**01**

**【背景介绍】**

电子邮件伪造攻击横行的一个重要原因是邮件协议（SMTP）缺少必要身份验证机制。近年来，研究人员陆续提出了多种用于验证发件人身份的邮件安全扩展协议，其中最具代表性的包括：发件人策略框架（SPF）[1]，域密钥标识的邮件（DKIM）[2]和基于域的消息认证、报告和一致性（DMARC）[3]，分别从发信方 IP 地址、内容完整性和多重身份标识符对齐多个角度对电子邮件的发信人身份进行了保护。已有研究已对SPF协议和DMARC协议部署现状和安全问题进行了讨论[4-6]。因此，本篇论文主要聚焦于DKIM协议。

DKIM协议是一项基于数字签名的身份验证协议，基于哈希算法和非对称加密算法（主要为RSA算法）计算DKIM签名。发信方邮件服务器会将DKIM签名添加到每封电子邮件的信头中，来确保发出的电子邮件不被第三方修改或者伪造。接收方可以通过查询发信人相应域名下的DNS记录获得DKIM公钥并对邮件进行验证。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MKrrzrzeOm5apPFrm0lCTPMZKN3eicEAicL1Fmlk6Ur2Aspibicbc6c1m4w/640?wx_fmt=png)

图表1 邮件头部中的DKIM签名示例

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3M2NDI3cKIOB98h3eZfo0S2ccuYep5q62ZGniamib3xAib2Cq0icDzTtR7Mw/640?wx_fmt=png)

图表2 部署在DNS服务器上的DKIM记录

**DKIM协议的工作流程**

接下来让我们来看一下DKIM的工作流程：

1. 首先，发送方需要部署DKIM协议，即使用非对称加密算法生成一个密钥对，并把DKIM记录（主要是DKIM的公钥信息）部署在一个指定域名（<selector>.\_domainkey.<example.com>）的DNS服务器上；

2.接下来，当发送方发送邮件时，会给发送出的邮件计算一个DKIM签名，计算的内容包括邮件头、邮件正文还有DKIM-Signature自身；

3. 最后，当接收方收到一份含有DKIM签名的邮件后，会先访问发送方相应域名的DNS服务器，提取DKIM公钥记录，并对邮件正文还有邮件全文计算hash值，利用公钥来验证DKIM签名的正确性。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MaDGnxuDc39Qqib4ZgUw8Um8aov4AMoeUuico69qx9dzv3uDCa4mLWbcw/640?wx_fmt=png)

图表3 DKIM协议工作流程示意图

**02**

**【研究方法】**

**论文结合被动分析和主动扫描的方法，对DKIM的部署现状进行了首次大规模和长期的测量研究，主要分为三个阶段：数据收集、数据处理和数据分析。

**![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MIsticfuCI99tgibtphLdQFg72T9qROicRsUG7rWm0cThibzxEZGH4apB6Q/640?wx_fmt=png)**

图表4 DKIM数据获取与分析流程图

首先是数据收集。本篇论文的研究数据主要从工业界合作伙伴处获得。获取DKIM信息主要有两种途径，一种是DKIM Records数据，另一种是DKIM Signatures数据。DKIM Records部署在一个有一定随机性的域名上，很难进行大规模测量。DKIM签名又只存在邮件的头部，因为用户隐私等原因也很难大规模获取。

虽然直接获取相关的数据比较困难，但由于DKIM Records会被部署在DNS服务器上，可以通过Passive DNS数据集来被动收集到相关的数据。完整的邮件头部可能包含很多敏感信息，但是DKIM签名自身是不包含隐私数据的。此外，作者还通过和Coremail公司合作的方式，获得了大量的邮件服务器日志，并由此获得了DKIM签名数据。最终形成了涵盖500万个域名和200万个DKIM选择器的数据集，时间跨度超过5年（2015-2020），如图表5所示。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3M5fiadIToTYr5xNwTNWzmkqF0XgMams6rvV22dOEiaIw2oD14xd42ibKsA/640?wx_fmt=png)

图表5 DKIM数据集总览**

在获取数据后，作者对原始数据进行了清洗、聚合、去重等一系列操作。论文发现，尽管理论上，部署DKIM域名中的<selector>字段由域名所有者任意指定，但实际使用中，大量域名将该字段设置为mail、default、dkim等常见值。因此，作者选取了Passive DNS中分析得的Top 40的selector，对Alexa Top 1M的域名进行了大规模的扫描。

**最后，论文利用扫描得到的结果进行了DKIM部署率分析、语法分析、密钥管理分析还有DKIM签名实现的安全分析。**

**03**

**【主要发现】**

**1. DKIM部署率符合预期，但在不同的顶级域名中差异很大**

利用从数据集中分析得到的流行的DKIM选择器，论文查询Alexa了前100万个域名的DKIM记录，结果如图表6所示。研究发现，至少有28.1%的域名已经部署了DKIM，这一比例在有MX记录的域名中是37%。但是，DKIM部署率在不同的顶级域名中差异很大：在测试的通用顶级域名（gTLDs）中，.edu域名部署率（71.3%）最高，而在国家代码顶级域名（ccTLDs）中，最高的部署率（58.6%）来自.au（澳大利亚）域名。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3Ms2OsCwS68ZibvRNH8STNpfnhI3ia5Jku4vemCWpmxugnpicExqSBDbdHw/640?wx_fmt=png)

图表6 Alexa前一百万域名中SPF、DKIM、DMARC协议的部署情况

**2. 部分域名的DKIM配置存在语法错误问题**

基于前一阶段DKIM部署率的测量结果，论文进一步对DKIM的部署现状进行了分析。在Alexa排名前100万的域名中，发现有8,147条部署记录由于缺少或不正确的DKIM记录而无法被验证。这些域名占所有支持DKIM的域名的2.9%。更糟糕的是，有3,292个域名被配置了不正常的DKIM字段，这会直接导致DKIM公钥解析错误，进而导致域名无法被DKIM有效保护。

**3. 普遍存在的DKIM密钥管理安全问题**

论文发现，DKIM的密钥管理普遍存在安全缺陷，包括共享DKIM密钥（66.9%）、弱DKIM密钥（84%）、长期（超过5年）未轮换DKIM密钥（8.4%）等，具体介绍如下：

**a)** **大量域名存在密钥生命周期过长的问题。**相关组织建议，DKIM密钥应该一年轮换2次来降低安全风险。但是很少有域名遵守这一实践。下图显示了Alexa Top 100域名的DKIM密钥生命周期的分析结果，黄色部分代表着至少有5年没有更换的密钥个数。结果显示，数据覆盖的54个域名（Alexa Top 100）中有68.5%的域名存在过去五年没有更新过的密钥。考虑到PassiveDNS数据记录并不能完全代表DKIM key的实际生命周期，所以，实际情况往往要更为严重。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3M1he09jSAq883o4TTUmU86WIFV1lSfUDTF0icG2pzia3ichDUzXqU6HYIw/640?wx_fmt=png)

图表7 知名域名的DKIM密钥生命周期统计

**b)弱密钥的使用依旧非常普遍**。早在2010年美国NIST就已建议不要使用小于等于1024位的RSA密钥，RFC 8301同样明确要求建议使用至少为2048位的DKIM密钥。但是，研究结果显示，在Passive DNS数据集中依然有84%的域名使用DKIM弱密钥（长度小于2048）。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MGrJsvia4vYn9icfyfklpibaBwHxG2BCndpSwLXfZpgAVmFDT9ibsAiabHicA/640?wx_fmt=png)

图表8 PassiveDNS中的DKIM密钥强度统计

此外，论文进一步分析了每年新增加的DKIM密钥的长度。可以看到，1024比特的DKIM密钥仍然是当前实践中的主流。长度不超过512比特的密钥的比例正在下降，而2048比特的密钥的比例正在逐步上升。结果表明，邮件管理员在更新DKIM配置时倾向于使用更安全的密钥，但推进过程非常缓慢。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MibM7WYK6icIPZa63Xe6ia02qsqOybJ3BJicB6trIoZNj7oLOKKzputfLqw/640?wx_fmt=png)

图表9 每年新增DKIM密钥的密钥长度统计

**c)DKIM部署广泛存在共享密钥问题。**研究以DKIM密钥（公钥）对域名进行聚类发现，有61,062个DKIM密钥被一个以上的域共享，而使用共享DKIM密钥的域名多达2,427,682个（66.9%）。下表显示了共享DKIM密钥的前10个域名簇。排名第一的DKIM密钥被超过289,120个域名共享，该密钥用于谷歌的电子邮件服务。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MwtFsUljjWW8vQ4SibeYhYT6PWDVfALJr7Jca7ibemyv4FOtl91U9XZcw/640?wx_fmt=png)

图表10 使用共享DKIM密钥的域名集合排名

**4. DKIM的签名实现存在多种安全隐患**

对DKIM签名实现的相关分析发现，现实世界中94.2%的域名存在DKIM签名问题，包括没有保护关键的电子邮件头部字段、在DKIM签名中使用不安全的 "l="标签及使用过时的哈希算法（SHA-1）等。具体介绍如下：

**a) DKIM签名没有保护关键的头字段**。DKIM的RFC6376中只明确要求了From字段一定要被签名，但是一封邮件包含的头部很多，如From、to、subject、Content-Type等等。已有研究表明，若此类关键字段没有被保护，DKIM签名很容易被攻击者用来进行重放攻击。但是协议并未明确定义DKIM签名需要对哪些信息进行保护。因为缺少协议规范，现实中对于邮件头字段的保护往往参差不齐，取决于邮件管理员对于邮件安全的认识。论文统计了数据集中所有的DKIM签名。下表展示了被高频签名的top 10邮件头字段，可以看出，现实中的邮件管理者并没有就此达成共识。共同签名的字段比例下降的非常快，排名第10的reply-to字段仅被不到12%的域名签名保护。并且只有2.2%的域名部署了RFC 6376所推荐的***Oversigning保护机制***。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MKQRIhvOH6yhJiaQBklsdP98B1gF8J1B5N5K5eFqam7OMw2mg3mBSWBw/640?wx_fmt=png)

图表11 被DKIM签名保护的邮件头字段排名

**b) 使用不安全的 "l="标签。**在DKIM记录中，l标签主要是用来表明需要被DKIM签名计算的邮件正文长度。但是 "l=" 标签的滥用可能会导致DKIM协议被绕过，攻击者可以通过结合Content-Type头字段和 "l=" 标签就可以实现对邮件正文内容的替换，可以在不破坏DKIM签名的情况下向终端用户显示虚假的邮件正文。尽管相关风险在RFC 6376中已经有所描述，但是论文发现，至今还有6,860个域名使用这种不安全的l标签，其中有1,273个为Alexa排名前100万的流行域名。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5zLsVDych8pMYRticBKFCLHvoLBxicF3MD3zD0RdCic6KmyXIYd835S4dL9Rl0g1EHdPcVL39Ixdehk8B4hJLv1A/640?wx_fmt=png)

图表12 利用不安全的 "l="标签进行邮件伪造攻击的示例

**c) 使用不够安全的哈希算法（SHA-1）**。哈希算法是创建数字签名的关键，其抗碰撞性可以直接影响数字签名算法的保护效果。SHA-1和SHA-256是DKIM中常用的哈希算法。但是近年来一系列的工作表明，SHA-1的抗碰撞性较差。在2018年，RFC 8301已经建议不再使用rsa-sha1来签署或验证DKIM签名。NIST也在2011年正式废止了SHA-1的使用。但是目前rsa-sha1算法仍然被现实中的邮件服务广泛使用。研究发现，1,451,956（65.9%）个域名仍然使用rsa-sha1来生成DKIM签名，其中3,292个为Alexa排名前100的流行域名。

**04**

**【防御建议】**

作者联系了所有受影响的电子邮件服务管理员，报告了论文发现的安全问题。其中，4家电子邮件供应商和24家相关的电子邮件管理员承认了安全问题的存在，Zoho.com还提供了200美元的漏洞奖励。

作者开发了一个在线测试工具（https://nospoofing.cn），帮助电子邮件管理员验证和部署其DKIM记录，期望改善DKIM部署的现状。论文也对DKIM的协议设计和协议实现提出了两项建议：

**1. DKIM Key Expiration Date。** 在DKIM记录中增加一个DKIM密钥过期日期的字段，帮助缓解过渡期不明确的问题，促进密钥的定期更换。发送服务可以自主决定是否使用这个字段。如果发送方支持该字段，邮件接收方在验证DKIM签名时，应该首先根据这个字段来确定当前收到的邮件的DKIM签名是否有效。

**2. Default Oversigning Mechanism。**Oversigning机制是一种有效保护用户免受DKIM重放攻击的防御机制。但是研究结果显示，现实中采用该机制的邮件服务并不多。因此，最好的方法是改变流行的DKIM库的实现，在签署DKIM签名时默认采用Oversigning策略。

上述两项措施有助于提高DKIM的保护效果，使DKIM签名免受重放攻击的影响，并不会对现有的协议部署产生额外影响。

**05**

**【总结】**

论文首次对真实互联网中DKIM协议的部署现状进行了大规模的测量，揭示了D...