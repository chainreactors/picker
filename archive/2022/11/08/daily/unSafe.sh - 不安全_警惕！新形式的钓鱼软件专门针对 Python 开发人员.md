---
title: 警惕！新形式的钓鱼软件专门针对 Python 开发人员
url: https://buaq.net/go-134588.html
source: unSafe.sh - 不安全
date: 2022-11-08
fetch_date: 2025-10-03T21:54:21.678173
---

# 警惕！新形式的钓鱼软件专门针对 Python 开发人员

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/58489bc90c4e5bff5ef6e4f8a8bafaae.jpg)

警惕！新形式的钓鱼软件专门针对 Python 开发人员

主站 分类 漏洞 工具 极客
*2022-11-7 19:18:28
Author: [www.freebuf.com(查看原文)](/jump-134588.htm)
阅读量:32
收藏*

---

[![freeBuf](https://www.freebuf.com/images/logoMax.png)](https://www.freebuf.com/)

主站

分类

漏洞

工具

极客

Web安全

系统安全

网络安全

无线安全

设备/客户端安全

数据安全

安全管理

企业安全

工控安全

特色

头条

人物志

活动

视频

观点

招聘

报告

资讯

区块链安全

标准与合规

容器安全

公开课

官方公众号企业安全新浪微博

![](https://www.freebuf.com/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](https://www.freebuf.com/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

![](https://image.3001.net/images/20221107/1667819890_6368e9722baa9cc4b1b62.jpg!small)最近，一种新形式的钓鱼软件专门攻击 Python 开发人员。攻击者通过伪造的 Python 包并使用常规的伪装技术，通过 W4SP Stealer 来感染开发人员的系统。W4SP Stealer 是一种用来窃取加密货币信息、泄露敏感数据并从开发人员系统收集凭据的木马工具。

根据软件供应链公司 Phylum 本周发布的一份报告中说：一名攻击者在 Python 包索引 (PyPI) 上创建了 29 个流行软件包的克隆，给它们包装成合法的软件包名称，这种做法被称为仿冒域名。如果开发人员下载并加载了恶意程序包，安装脚本则会通过一些混淆步骤来误导安装 W4SP Stealer 木马。目前，这些软件包的下载量已高达 5,700 次。

Phylum 的联合创始人兼首席技术官 Louis Lang 表示，虽然 W4SP Stealer 的作用是针对加密货币钱包和金融账户，但当前攻击者最重要目的很有可能是开发者的隐私。

这与我们过去经常遇到的电子邮件网络钓鱼活动的形式一样，只是这次攻击者只针对开发人员。“考虑到开发人员经常可以访问最核心的地方，一旦被成功的攻击那么会对组织造成毁灭性的打击。

该组织对 PyPI 的攻击是针对软件供应链的最新威胁。通过存储库服务分发的开源软件组件，例如 PyPI 和节点包管理器 (npm)，是一种流行的攻击媒介，因为导入软件的需求数量急剧增加。攻击者试图利用生态系统将恶意软件传输到粗心的开发人员系统中，例如2020 年对 Ruby Gems 生态系统的攻击和对Docker Hub 映像生态系统的攻击。而在 8 月，Check Point Software Technologies 的安全研究人员发现了 10 个 PyPI 软件包，它们都为窃取信息的恶意软件。

Phylum 研究人员 在他们的分析中表示：在这次最新的攻击活动中，这些软件包是一种更复杂的尝试，将 W4SP Stealer 传递到 Python 开发人员的机器上。并补充说：“由于这是一个持续的攻击，攻击者通过不断的改变策略，导致我们很难发现。同时，我们怀疑在不久的将来会出现更多类似的恶意软件。

### PyPI 攻击是一种“量化游戏”

这种攻击通过伪装通用软件包名称或使用新软件包来迷惑没有充分审查软件来源的开发人员。例如：一个名为“typesutil”的恶意程序包只是流行的 Python 程序包“datetime2”的副本，并进行了一些修改。

最初，任何导入恶意软件的程序都会在 Python 加载依赖项的设置阶段运行命令并下载恶意软件。后来，由于 PyPI 实施了某些检查，攻击者开始使用大量空格将可疑命令推送到大多数代码编辑器的正常可视范围之外。

Phylum 在其分析中说：攻击者稍微改变了策略，不是仅仅将导入文件放在一个明显的位置，而是将它放在屏幕外，利用 Python 很少使用的分号将恶意代码偷偷放到与其他合法代码的行中。

Phylum 的 Lang 表示，虽然域名仿冒是一种低保真攻击，成功率极低，但与潜在的回报相比，这种成本微乎其微。

这是一场量的游戏，攻击者每天都用大量的恶意软件包污染软件包生态系统。然而相对于回报率来说，成本却极低。

### 令人痛心的 W4SP

攻击的最终目标是安装“信息窃取木马 W4SP Stealer”，它入侵受害者的系统，窃取浏览器存储的密码，针对加密货币钱包，并使用关键字搜索感兴趣的文件，例如‘银行’和‘秘密’ 。

Lang说：除了窃取加密货币或银行信息带来的明显金钱回报外，攻击者还可以利用窃取的一些信息通过访问关键基础设施或借用开发人员的身份来进一步攻击。

目前，Phylum 在识别攻击者方面取得了一些进展，并向正在使用其基础设施的公司发送了报告。

文章来源: https://www.freebuf.com/articles/349072.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)