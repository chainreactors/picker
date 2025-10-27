---
title: KimJongRAT攻击再次来袭：新的PE和PowerShell变种通过cdn窃取加密和浏览器数据
url: https://www.anquanke.com/post/id/308598
source: 安全客-有思想的安全新媒体
date: 2025-06-19
fetch_date: 2025-10-06T22:47:51.635922
---

# KimJongRAT攻击再次来袭：新的PE和PowerShell变种通过cdn窃取加密和浏览器数据

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

# KimJongRAT攻击再次来袭：新的PE和PowerShell变种通过cdn窃取加密和浏览器数据

阅读量**85535**

发布时间 : 2025-06-18 15:55:10

**x**

##### 译文声明

本文是翻译文章，文章来源：securityonline

原文地址：<https://securityonline.info/kimjongrat-returns-new-pe-powershell-variants-steal-crypto-and-browser-data-via-cdns/>

译文仅供参考，具体内容表达以及含义原文为准。

Unit 42 发现了 KimJongRAT 恶意软件的两个新进化变体，一个使用传统的 PE（可移植可执行文件）文件，另一个使用基于 PowerShell 的脚本来渗透系统、窃取数据并泄露敏感的浏览器、电子邮件和加密货币钱包信息。

KimJongRAT 最初于 2013 年和 2019 年再次记录，现已重新出现，具有更高的隐身性和先进的多级交付机制，利用合法的内容交付网络 （CDN） 来掩盖其恶意负载。正如 Unit 42 研究人员[所强调](https://unit42.paloaltonetworks.com/kimjongrat-stealer-variant-powershell/)的那样，这些最新版本标志着“*一个明确且持续的威胁*”，展示了威胁行为者如何继续增强他们的工具包。

这两种变体的感染链开始相似：用户被诱骗打开 Windows 快捷方式 （LNK） 文件——通常伪装成官方文档，从 CDN 子域 cdn.glitch[.] 下载 HTA（HTML 应用程序）文件。全球。

在 PE 变体中，此 HTA 会放置一个诱饵 PDF、一个加载程序 （sys.dll） 和一个带有其他有效载荷 URL 的文本文件。PowerShell 变体遵循类似的路径，但将加载程序替换为 PowerShell 脚本和包含混淆窃取程序和键盘记录器模块的 ZIP 存档。

![KimJongRAT，信息窃取者]()

最新 KimJongRAT PE 变体的恶意软件执行链 |图片： Unit 42

PE 变体是有条不紊地制作的：

1. HTA 文件会放置一个 Base64 解码的 DLL，然后：
2. 检查沙盒环境，确保它仅在真实系统中运行。
3. 下载其他加密组件，反射式加载窃取程序 （net64.log），并最终执行强大的编排器 （main64.log）。

此 Orchestrator 能够：

* 通过 HTTP POST 方法上传被盗文件和剪贴板数据
* 通过 GET 请求接收后门命令
* 搜索敏感文档格式，包括 .hwp、.pdf、.docx 和 .zip
* 泄露浏览器凭据、FTP/电子邮件客户端数据和键盘日志

Unit 42 指出，该恶意软件的编排能力非常强大，编排器使用多个线程进行键盘记录、剪贴板监控和持续数据盗窃。

“*网络通信是在无限循环中实现的，该循环上传收集的数据并从 C2 服务器请求命令*，”研究人员解释说。

相比之下，PowerShell 变体更集中。它通过 ZIP 存档中的嵌入式脚本部署其窃取程序和键盘记录器。值得注意的是，它对浏览器数据进行了全面监控，尤其是对于加密货币钱包扩展。

根据 Unit 42 的说法，“*这项新分析揭示了 PowerShell 变体对加密货币的特别关注*”，识别并定位 MetaMask、Trust Wallet、TronLink、Exodus Web3 Wallet 和其他 30 多个加密钱包的浏览器扩展。

窃取者通过添加 Windows 注册表项 （WindowsSecurityCheck） 并持续扫描以下内容来实现持久性：

* 饼干
* 保存的登录凭证
* 已安装的扩展和浏览器活动
* 加密货币钱包数据
* 最近访问的文档和存档文件

Unit 42 的取证分解显示，窃取者甚至停止浏览器进程以安全地复制敏感文件，对其进行加密，并使用计划作将它们发送到攻击者的命令和控制 （C2） 服务器。

两种变体都具有几个高级特征：

* 滥用受信任的 CDN 进行有效负载交付
* 通过 Base64 和 XOR 加密进行混淆
* 分段执行以逃避检测的多阶段加载器
* 使用 certutil.exe、rundll32.exe 和 mshta.exe 等合法工具

也许最引人注目的是 KimJongRAT 的适应性，它从 2019 年与“巨人婴儿行动”相关的活动演变而来，现在以现代化的基础设施和对加密货币盗窃的日益重视重新出现。

本文翻译自securityonline [原文链接](https://securityonline.info/kimjongrat-returns-new-pe-powershell-variants-steal-crypto-and-browser-data-via-cdns/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/308598](/post/id/308598)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/kimjongrat-returns-new-pe-powershell-variants-steal-crypto-and-browser-data-via-cdns/)

如若转载,请注明出处： <https://securityonline.info/kimjongrat-returns-new-pe-powershell-variants-steal-crypto-and-browser-data-via-cdns/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=170061)

[安全客](/member.html?memberId=170061)

这个人太懒了，签名都懒得写一个

* 文章
* **2096**

* 粉丝
* **6**

### TA的文章

* ##### [英国通过数据访问和使用监管法案](/post/id/308719)

  2025-06-20 17:11:10
* ##### [CISA警告：严重缺陷（CVE-2025-5310）暴露加油站设备](/post/id/308715)

  2025-06-20 17:09:03
* ##### [大多数公司高估了AI治理，因为隐私风险激增](/post/id/308708)

  2025-06-20 17:05:02
* ##### [研究人员发现了有史以来最大的数据泄露事件，暴露了160亿个登录凭证](/post/id/308704)

  2025-06-20 17:02:15
* ##### [CVE-2025-6018和CVE-2025-6019漏洞利用：链接本地特权升级缺陷让攻击者获得大多数Linux发行版的根访问权限](/post/id/308701)

  2025-06-20 16:59:36

### 相关文章

* ##### [再添数字政府新名片！深圳“深治慧”平台入选2025数博会创新案例](/post/id/311777)

  2025-09-02 15:37:49
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/310525)

  2025-07-24 10:24:57
* ##### [ISC.AI 2025国际人工智能发展高峰论坛：凝聚全球共识，点亮AI未来](/post/id/310510)

  2025-07-24 09:47:17
* ##### [ISC.AI大咖来了——国家网络安全守卫者 周鸿祎](/post/id/310504)

  2025-07-24 09:43:28
* ##### [攻击者在“PoisonSeed”钓鱼攻击中通过降级手段绕过FIDO2多因素认证（MFA）](/post/id/310339)

  2025-07-21 17:41:39
* ##### [掌握AI+安全双刃剑，ISC训练营助你成为企业疯抢的黄金人才！](/post/id/309947)

  2025-07-11 16:10:36
* ##### [报名开启！ISC.AI训练营助力AI与数字安全人才培养](/post/id/309827)

  2025-07-10 17:42:56

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