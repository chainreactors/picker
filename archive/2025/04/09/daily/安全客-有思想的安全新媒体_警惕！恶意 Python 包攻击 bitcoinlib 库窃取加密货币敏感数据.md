---
title: 警惕！恶意 Python 包攻击 bitcoinlib 库窃取加密货币敏感数据
url: https://www.anquanke.com/post/id/306274
source: 安全客-有思想的安全新媒体
date: 2025-04-09
fetch_date: 2025-10-06T22:03:43.547675
---

# 警惕！恶意 Python 包攻击 bitcoinlib 库窃取加密货币敏感数据

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

# 警惕！恶意 Python 包攻击 bitcoinlib 库窃取加密货币敏感数据

阅读量**55128**

发布时间 : 2025-04-08 11:03:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/malicious-python-packages-attacking-popular-cryptocurrency-library/>

译文仅供参考，具体内容表达以及含义原文为准。

网络安全专家发现了一种针对加密货币开发者和用户的新威胁。

在 Python 软件包索引（PyPI）上发现了两个恶意的 Python 软件包，它们专门被设计用来攻击使用流行的 bitcoinlib 库的系统。

这两个被识别为 bitcoinlibdbfix 和 bitcoinlib-dev 的软件包，伪装成该加密货币库的合法修复程序，但其包含的代码旨在窃取包含有价值的加密钱包信息的敏感数据库文件。

bitcoinlib 库是开发人员构建加密货币应用程序的关键工具，它为创建和管理加密钱包、与区块链网络交互以及执行比特币脚本提供了必要的功能。

这使其成为寻求破坏加密货币资产或访问敏感区块链数据的攻击者有价值的目标。

ReversingLabs 的研究人员通过他们的 Spectra 平台发现了这些恶意软件包，该平台采用先进的机器学习算法，通过分析行为模式来检测新型恶意软件。

根据他们的分析，这两个软件包都是有针对性的供应链攻击的一部分，延续了 2024 年全年近二十几次类似活动所呈现的令人担忧的加密货币相关软件遭破坏的趋势。

攻击者采用了经典的社会工程学技巧，将他们的恶意软件包伪装成解决 bitcoinlib 中所谓数据库问题的方案。

其中一个软件包声称可以修复 “ValueError: Old database version found (0.5 version database automatically）”错误，引诱那些寻求快速解决方案的开发人员安装这些被篡改的代码。

一旦安装，这些恶意软件包就会通过针对合法的命令行界面工具执行复杂的攻击。

****感染机制分析****

攻击的核心在于用恶意代码覆盖合法的 “clw” 命令行工具。

这些软件包包含的功能首先是使用如下代码删除任何现有的 clw 命令：

def remove\_existing\_clw():

“””如果系统中存在现有的clw命令，则将其删除”””

try:

clw\_path = check\_output([‘which’, ‘clw’], stderr=sys.stderr).decode().strip()

if clw\_path:

os.remove(clw\_path)

except CalledProcessError:

pass

在删除合法工具后，恶意软件会创建一个指向其自身可执行文件的符号链接，使其能够拦截原本用于加密货币钱包管理的命令。

这为攻击者提供了一种持续的机制，用于获取包含私钥和钱包信息的敏感数据库文件，然后这些文件会被泄露到攻击者控制的服务器上。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/malicious-python-packages-attacking-popular-cryptocurrency-library/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306274](/post/id/306274)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/malicious-python-packages-attacking-popular-cryptocurrency-library/)

如若转载,请注明出处： <https://cybersecuritynews.com/malicious-python-packages-attacking-popular-cryptocurrency-library/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**4赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

[安全客](/member.html?memberId=175868)

这个人太懒了，签名都懒得写一个

* 文章
* **376**

* 粉丝
* **1**

### TA的文章

* ##### [mavinject.exe 遭利用，黑客绕过安全防线入侵系统](/post/id/306961)

  2025-04-28 10:48:18
* ##### [Docker 惊现新型加密挖矿攻击，借 Teneo 平台开辟恶意获利新路径](/post/id/306959)

  2025-04-28 10:39:59
* ##### [Cloudflare 隧道遭滥用，恶意 RAT 传播威胁加剧](/post/id/306957)

  2025-04-28 10:34:35
* ##### [xrpl.js 库遭供应链攻击，超 290 万次下载用户私钥成窃取目标](/post/id/306953)

  2025-04-28 10:29:02
* ##### [恶意后门借 ViPNet 更新渗透，俄罗斯多行业数据安全拉响警报](/post/id/306951)

  2025-04-28 10:22:13

### 相关文章

* ##### [Morte僵尸网络被披露：正利用路由器与企业应用漏洞，迅速扩张其“加载器即服务”活动](/post/id/312444)

  2025-09-29 18:04:01
* ##### [Akira勒索软件利用SonicWall VPN账户发起急速入侵](/post/id/312438)

  2025-09-29 18:03:28
* ##### [DarkCloud信息窃取器现新变种：采用VB6混淆技术并新增加密货币钱包窃取功能，威胁显著升级](/post/id/312435)

  2025-09-29 18:02:53
* ##### [TamperedChef恶意软件兴起：欺诈应用利用经过签名的二进制文件与搜索引擎投毒劫持浏览器](/post/id/312432)

  2025-09-29 18:02:25
* ##### [黑客将SVG文件武器化，用于隐秘投递恶意负载](/post/id/312351)

  2025-09-24 16:44:10
* ##### [ShadowV2僵尸网络利用配置错误的AWS Docker容器构建DDoS攻击租用服务](/post/id/312381)

  2025-09-24 16:40:43
* ##### [npm软件包“fezbox”中被发现新型恶意软件，可利用二维码窃取用户凭据](/post/id/312387)

  2025-09-24 16:40:06

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