---
title: Cicada 勒索软件的新变体以 VMware ESXi 系统为目标
url: https://www.anquanke.com/post/id/299729
source: 安全客-有思想的安全新媒体
date: 2024-09-04
fetch_date: 2025-10-06T18:21:54.595901
---

# Cicada 勒索软件的新变体以 VMware ESXi 系统为目标

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

# Cicada 勒索软件的新变体以 VMware ESXi 系统为目标

阅读量**97456**

发布时间 : 2024-09-03 14:23:13

**x**

##### 译文声明

本文是翻译文章，文章原作者 Pierluigi Paganini，文章来源：securityaffairs

原文地址：<https://securityaffairs.com/167897/cyber-crime/a-new-variant-of-cicada-ransomware-targets-vmware-esxi-systems.html>

译文仅供参考，具体内容表达以及含义原文为准。

## 一种名为 Cicada3301 的新型勒索软件即服务 （RaaS） 操作已出现在威胁环境中，并且已经针对数十家公司。

Cicada3301 是出现在威胁环境中的一种新的勒索软件即服务 （RaaS） 操作。该组织似乎非常活跃，自 6 月中旬以来已经在其勒索门户网站上列出了 23 名受害者。下图显示了该团伙在其暗网泄漏网站上发布的受害者名单。

![蝉3301]()

Cicada 3301 是 2012 年至 2014 年间在网上以“3301”为名发布的三组谜题的名称。第一个拼图于 2012 年 1 月 4 日在 4chan 上开始，运行了近一个月。第二轮谜题在一年后的 2013 年 1 月 4 日开始，然后在 2014 年 1 月 4 日在 Twitter 上发布的新线索得到确认后开始第三轮谜题。第三个谜题还没有解开。其明确意图是通过提出一系列有待解决的谜题来招募“聪明人”;2015 年 1 月 4 日没有发布新的谜题。

但是，该操作似乎与 Cicada3301 没有任何联系。

自 6 月以来，Cicada3301 背后的运营商开始在 RAMP 网络犯罪论坛上招募附属公司。

Cicada3301 勒索软件是用 Rust 编写的，以 Windows 和 Linux/ESXi 主机为目标。Truesec 研究人员剖析了一种针对 VMware ESXi 系统的变体，该变体似乎是适用于 Windows 的相同恶意软件的一个版本。专家指出，虽然许多勒索软件组织现在都以 ESXi 系统为目标，但只有少数组织，包括现已解散的 BlackCat/ALPHV 组织，使用了基于 Rust 的勒索软件。分析显示 Cicada3301 的勒索软件与 ALPHV 勒索软件之间存在显着相似之处。

*“Cicada3301 勒索软件与 ALPHV 勒索软件有几个有趣的相似之处。”**报道**Truesec 的*

* 两者都是用 Rust 编写的
* 两者都使用 ChaCha20 进行加密
* 两者都使用几乎相同的命令来关闭 VM 和删除快照[1]
* 两者都使用 –ui 命令参数来提供加密的图形输出
* 两者都使用相同的约定来命名文件，但将 “RECOVER-”ransomware extension“-FILES.txt” 改为 “RECOVER-”ransomware extension“-DATA.txt”[2]
* 如何使用 key 参数解密勒索软件说明

Cicada3301 组织的最初攻击始于使用被盗或暴力破解的凭据通过 ScreenConnect 登录。勒索软件组织使用的 IP 地址与 Brutus 僵尸网络相关联，这种情况表明两者之间可能存在联系。此时间表与 BlackCat/ALPHV 勒索软件组织的明显退出相吻合，这增加了 Cicada3301 可能是 ALPHV 的品牌重塑、与其开发人员的合作或使用修改后的 ALPHV 代码的单独组织的可能性。

Cicada3301 勒索软件支持多个可配置参数，操作员可以使用这些参数在执行过程中更改其行为。这些参数通过库进行管理，包括以下选项：`clap::args`

* **sleep**：将勒索软件的执行延迟指定的秒数。
* **ui**：展示加密过程的实时进度和统计信息，例如加密的文件数。
* **no\_vm\_ss**：加密 ESXi 主机上的文件，而无需关闭正在运行的虚拟机、使用终端和删除快照。`esxicli`

这些功能为勒索软件的运行方式提供了灵活性，可能使其在不同场景中更加有效。

Cicada3301 勒索软件使用 OsRng 随机数生成器生成用于加密的对称密钥。勒索软件使用一个名为 to handle file encryption 的函数。此过程涉及提取存储在二进制文件数据部分中的公有 PGP 密钥，该密钥用于加密生成的对称密钥。`encrypt_file`

然后，恶意软件会在每个包含加密文件的文件夹中创建一个标题为“RECOVER-[加密文件结尾]-DATA.txt”的注释。该加密针对特定的文件扩展名，主要与文档和图片有关，这表明勒索软件最初旨在针对 Windows 系统，然后才适应 ESXi 主机。

*“加密完成后，勒索软件使用提供的 RSA 密钥加密 ChaCha20 密钥，最后将扩展名写入加密文件。添加加密文件扩展名 文件扩展名也与 RSA 加密的 ChaCha20 密钥一起添加到加密文件的末尾。“包括此版本恶意软件*

本文翻译自securityaffairs [原文链接](https://securityaffairs.com/167897/cyber-crime/a-new-variant-of-cicada-ransomware-targets-vmware-esxi-systems.html)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/299729](/post/id/299729)

安全KER - 有思想的安全新媒体

本文转载自: [securityaffairs](https://securityaffairs.com/167897/cyber-crime/a-new-variant-of-cicada-ransomware-targets-vmware-esxi-systems.html)

如若转载,请注明出处： <https://securityaffairs.com/167897/cyber-crime/a-new-variant-of-cicada-ransomware-targets-vmware-esxi-systems.html>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全热点](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E7%83%AD%E7%82%B9)
* [行业资讯](/tag/%E8%A1%8C%E4%B8%9A%E8%B5%84%E8%AE%AF)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170338)

[安全客](/member.html?memberId=170338)

这个人太懒了，签名都懒得写一个

* 文章
* **823**

* 粉丝
* **1**

### TA的文章

* ##### [严重的GiveWP漏洞（CVE-2024-8353）影响10万WordPress网站](/post/id/300547)

  2024-09-30 15:03:21
* ##### [Patchwork APT 的 Nexe 后门活动曝光](/post/id/300549)

  2024-09-30 15:03:07
* ##### [用户在一次复杂的钓鱼攻击中损失了价值3200万美元的spWETH](/post/id/300551)

  2024-09-30 15:02:50
* ##### [车牌信息成安全漏洞：起亚汽车远程控制风险揭示联网车辆网络安全问题](/post/id/300553)

  2024-09-30 15:02:09
* ##### [严重SQL注入漏洞影响TI WooCommerce Wishlist插件，超10万WordPress网站面临风险](/post/id/300556)

  2024-09-30 15:01:53

### 相关文章

* ##### [国庆重保+攻防演练大考在即！360大模型安全服务专项方案筑牢AI防线](/post/id/312460)

  2025-09-29 18:06:17
* ##### [Meta 旨在打造机器人领域的“Android”，为下一代人形AI提供通用平台](/post/id/312454)

  2025-09-29 18:05:34
* ##### [谷歌新规强制要求：所有安卓应用须在2025年11月1日前全面支持16KB页面大小](/post/id/312429)

  2025-09-29 18:01:37
* ##### [“天网杯”纳米AI视频创作赛圆满落幕，ISC.AI学苑推动“教育AI+”新范式](/post/id/312373)

  2025-09-24 16:42:53
* ##### [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](/post/id/312360)

  2025-09-24 16:42:36
* ##### [WhatsApp 为 iPhone 和 Android 应用支持消息翻译功能](/post/id/312341)

  2025-09-24 16:38:49
* ##### [Microsoft将在威斯康星州打造“世界最强AI数据中心](/post/id/312314)

  2025-09-22 18:13:49

### 热门推荐

文章目录

* [一种名为 Cicada3301 的新型勒索软件即服务 （RaaS） 操作已出现在威胁环境中，并且已经针对数十家公司。](#h2-0)

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