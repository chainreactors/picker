---
title: SnowSoul勒索软件样本分析：加密机制与解密研究
url: https://www.anquanke.com/post/id/313279
source: 安全客-有思想的安全新媒体
date: 2025-11-19
fetch_date: 2025-11-20T03:08:11.650332
---

# SnowSoul勒索软件样本分析：加密机制与解密研究

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# SnowSoul勒索软件样本分析：加密机制与解密研究

阅读量**18186**

发布时间 : 2025-11-19 21:35:35

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

近期，360数字安全集团捕获并分析了新近活跃的勒索家族SnowSoul。该家族采用对称加密（AES）与非对称加密（RSA）结合的混合加密机制，具有传播速度快、干扰范围广、对业务系统冲击明显等特点。

为了评估其真实危害与可行的处置方向，研究团队对其样本进行了完整的行为分析、加密流程逆向与密钥管理机制分析。在深入分析过程中，研究团队不仅还原了SnowSoul的攻击链与加密实现细节，还识别出其密码学设计中的关键缺陷，并基于该缺陷开发出有效的解密器，经验证可成功解密被其加密的文件，并已在多个样本与受影响环境中验证，可稳定恢复加密文件。

****【技术分析】****

****运行流程概述****

SnowSoul勒索软件加密前置处理流程图如下：

![]()

图1. SnowSoul勒索加密前处理流程示意图

SnowSoul勒索软件加密流程简图如下所示：

![]()

图2. SnowSoul勒索软件加密流程示意图

****前置操作****

在SnowSoul加密过程中，首先会排除一些目录或文件，这些目录或文件看起来大部分为系统相关目录或文件，但部分名称有所不同，推测可能是拼写错误。

![]()

图3. 排除的目录和文件名称列表

软件运行后，首先会通过修改注册表，禁用系统的任务管理器。接下来，SnowSoul会执行bcdedit命令，禁用系统的恢复模式。完成后，SnowSoul还会像大多数勒索软件一样，删除用于备份系统数据的卷影副本。SnowSoul还会强制删除当前设备备份目录中存储的数据库，这一操作等同于对系统备份目录进行了重置操作。

![]()

图4. SnowSoul勒索软件系统前置操作代码

****驻留系统****

接下来，SnowSoul会尝试实现持久化驻留系统，其函数的作用是把当前可执行文件自身复制到用户的Roaming目录下（通常对应系统环境变量的%AppData%），并以指定的文件名运行。如果目录中已经存在同名文件，则会将其覆盖后再启动，然后退出当前进程。

![]()

图5. 复制到指定%AppData%中并启动

SnowSoul还会尝试停止一些系统服务和进程，防止影响加密操作的占用。此外，被该勒索软件加密的文件扩展名共有532种，覆盖几乎所有常见的文档及数据文件扩展名。在加密文件操作完成后，被加密的新文件会被附加一个随机的加密扩展名。该扩展名是随机的5个字符（随机范围为10个数字和26个小写字母）：

![]()

图6. 随机的加密文件扩展名

SnowSoul的文件加密操作采用了AES-CBC加密算法：

![]()

图7. 文件加密算法及参数

对于上述用来加密文件的加密AES密钥文件，则采用RSA-2048公钥进行加密：

![]()

图8. 密钥文件加密算法

这一加密操作使用的RSA公钥，通过硬编码方式直接内置在程序代码中：

![]()

图9. 硬编码的RSA公钥数据

加密后覆盖原文件为“?”并将原文件删除，这一操作是用来防止对原数据进行恢复的典型数据破坏行为。

![]()

图10. 破坏原文件数据防止恢复

通过分析发现，被加密后的文件固定结构中的前8个字节，为用于加密的AES算法中的IV值。与之对应的，被加密的文件尾部344字节，为RSA加密过的AES密钥再次进行Base64编码后的数据。

完成所有加密操作后，SnowSoul会在受害系统中释放勒索信。

![]()

图11. 被释放到受害者系统中的勒索信

****【数据解密】****

尽管SnowSoul采用了成熟的AES + RSA-2048混合加密方案，理论上安全性较高，但研究团队在其实现逻辑中发现了关键密码学设计缺陷。

基于这一漏洞，研究团队开发了可完全恢复文件的解密工具，并在多份样本与真实感染环境中验证其稳定性，能成功恢复所有被加密文件。

![]()

图12. “SnowSoul勒索解密工具”可有效解密文件并恢复数据

****【写在最后】****

当前，绝大多数勒索软件采用以RSA为核心的混合加密机制。而在未获得攻击者解密私钥的情况下，几乎无法对被加密的文件进行解密恢复。本次研究团队针对SnowSoul的成功解密，源于其加密算法的实现存在缺陷，具有一定的偶发性与针对性，并不代表对此类勒索软件的解密具有通用性。所以，请所有用户——尤其是重要数据的维护人员，务必持续做好离线/不可变备份与基础防护，切勿因个案的解密成功，而放松对数据备份与勒索攻击预防的重视与投入。

****IOCs****

****HASH (SHA256)****

71DB44CCAA100FC6CEF923F069753F6258C807421B94A53E6AC6F01834F93B52

****Discord Group****

theroyalteam963

****RSA PUB KEY****

1ipgguR6wKrENbAIHz9PssjI1/jlD9xZXFpot4p4X3GhX3P05sn7aZrfVEkN0GuJIFOly+u3dQEvQGGzw0/cXjuRAeeJXdsOUQOnJ64ljXF5/ZXGkfGmIhPeKlWYQC4N764s/Un6XweL+534gaMkkqo86Z7Sn1SUct+tAJCv/qbKBPgoxQGZcpQmIKtqlb4D8Q6NM4Y4QCwffprgjqLqWOmKgUOGHBQMnGnws2ZA6KMri8r17sj807fjyu56dyxoa4ql9zbmxHARKSNU/7FTZ9cGvPG1xiIkrbqQwgNehvKtSLMnsgbni+RdZ+ufhKeNthztNLm/VDD2GFogBnzmDQ==

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313279](/post/id/313279)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [勒索病毒](/tag/%E5%8B%92%E7%B4%A2%E7%97%85%E6%AF%92)
* [勒索家族](/tag/%E5%8B%92%E7%B4%A2%E5%AE%B6%E6%97%8F)
* [SnowSoul](/tag/SnowSoul)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **706**

* 粉丝
* **6**

### TA的文章

* ##### [SnowSoul勒索软件样本分析：加密机制与解密研究](/post/id/313279)

  2025-11-19 21:35:35
* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10

### 相关文章

* ##### [地狱猎犬在行动：至少20个俄罗斯组织成为网络攻击的受害者](/post/id/291583)

  2023-12-01 11:00:24
* ##### [麒麟勒索病毒声称攻击汽车巨头延锋](/post/id/291533)

  2023-11-29 11:34:08
* ##### [LockBit 勒索团伙攻击加拿大政府承包商](/post/id/291424)

  2023-11-21 15:24:31
* ##### [FBI ：“分散蜘蛛”勒索组织的策略](/post/id/291401)

  2023-11-17 10:49:33
* ##### [加利福尼亚州长滩市在网络攻击后关闭 IT 系统](/post/id/291399)

  2023-11-17 10:44:55
* ##### [美杜莎勒索软件威胁泄露数据后，丰田证实存在违规行为](/post/id/291394)

  2023-11-17 10:35:15
* ##### [核能、石油和天然气是 2024 年勒索软件组织的主要目标](/post/id/291368)

  2023-11-14 16:30:29

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)