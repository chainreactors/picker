---
title: VS Code 供应链攻击事件：19 款恶意扩展借拼写欺骗与隐写术投放 Rust 木马
url: https://www.anquanke.com/post/id/313771
source: 安全客-有思想的安全新媒体
date: 2025-12-15
fetch_date: 2025-12-16T03:22:08.584261
---

# VS Code 供应链攻击事件：19 款恶意扩展借拼写欺骗与隐写术投放 Rust 木马

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

# VS Code 供应链攻击事件：19 款恶意扩展借拼写欺骗与隐写术投放 Rust 木马

阅读量**13899**

发布时间 : 2025-12-15 17:38:25

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/vs-code-supply-chain-attack-19-extensions-used-typosquatting-steganography-to-deploy-rust-trojan/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款技术成熟的恶意软件攻击行动在**Visual Studio Code（VS Code）应用市场**中被曝光，这一事件为开发者群体揭示了供应链风险的全新层面。逆向实验室（ReversingLabs，简称 RL）的研究人员已确认，有**19 款恶意扩展程序**通过将载荷深藏于依赖文件夹中的方式，成功绕过了标准检测机制。

该攻击行动自 2025 年 2 月起处于活跃状态，并于 12 月 2 日被正式发现。攻击者巧妙结合 \*\*“类拼写欺骗” 策略与隐写术 \*\*，以此感染开发者的终端设备。研究人员指出：“恶意文件盗用一款合法的 npm 软件包来规避检测，并构造了一个包含恶意二进制文件的压缩包，将其伪装成图片文件 —— 也就是一个后缀为 PNG 的文件”。

此次攻击的高明之处，在于利用了 VS Code 扩展程序的组件运行机制。与标准 npm 项目需要实时获取依赖包不同，VS Code 扩展程序会预先打包一个`node_modules`文件夹，内含运行所需的全部类库。这种架构虽然能让扩展程序实现 “开箱即用”，却也为攻击者提供了绝佳的藏匿空间。

在本次攻击行动中，威胁攻击者盯上了下载量超 90 亿次的高人气软件包 \*\*`path-is-absolute`\*\*—— 他们并未篡改 npm 官方仓库中的这款软件包，而是对植入恶意扩展程序内的捆绑版本进行了本地修改。

报告指出：“通过这种方式，威胁攻击者将一款广受欢迎且原本安全的软件包，变成了一颗定时炸弹。只要用户启用任意一款恶意扩展程序，这颗炸弹就会立即引爆”。由于开发者与安全工具通常会默认信任`node_modules`文件夹的内容，认为其与公开的安全版本完全一致，因此其中的恶意代码得以长时间隐匿。

为进一步掩盖踪迹，攻击者还植入了一个名为`banner.png`的欺骗性文件。该文件看似是用于扩展程序应用市场展示的标准图片，实则是一个经过武器化改造的压缩包。

研究人员证实：“事实证明，这个名为`banner.png`的文件根本不是图片。它本质上是一个压缩包，内含两个恶意二进制文件”。

完整的攻击链路如下：

1. 受感染的依赖包中，`index.js`文件会在 VS Code 启动时自动运行；
2. 该文件触发一个隐藏类，从一个名为`lock`的文件中解码出一段 JavaScript 下载器；
3. 随后，这个下载器会从伪造的 PNG 文件中提取恶意载荷。

恶意软件被释放后，并非直接运行，而是会利用系统自身的工具来实施攻击。解码后的下载器会调用 \*\*`cmstp.exe`**执行恶意二进制文件 —— 这是微软官方的 “连接管理器配置文件安装程序”，属于黑客常用的**“就地取材二进制文件（LOLBIN）”\*\*，可被用于绕过安全防护机制。

其中一个二进制文件负责通过模拟按键操作管理执行流程，而另一个则是 \*\*“功能更为复杂的 Rust 木马”\*\*，其完整功能目前仍在研究人员的分析中。

研究人员还指出，尽管大部分恶意扩展程序都利用了`path-is-absolute`软件包，但有 4 款扩展程序采用了不同的攻击载体：它们篡改了`@actions/io`软件包，并将恶意载荷隐藏在 TypeScript 文件（`.ts`）与源码映射文件（`.map`）中，而非伪造的图片文件。

报告最后总结道：“大多数情况下，用户会想当然地认为这个文件夹中的依赖包代码，与 npm 官方托管的代码完全一致，因此会盲目信任，不会进行任何验证”。这也暴露出当前开发者安全实践中存在的一大关键盲区。

本文翻译自securityonline [原文链接](https://securityonline.info/vs-code-supply-chain-attack-19-extensions-used-typosquatting-steganography-to-deploy-rust-trojan/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313771](/post/id/313771)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/vs-code-supply-chain-attack-19-extensions-used-typosquatting-steganography-to-deploy-rust-trojan/)

如若转载,请注明出处： <https://securityonline.info/vs-code-supply-chain-attack-19-extensions-used-typosquatting-steganography-to-deploy-rust-trojan/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p5.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **810**

* 粉丝
* **6**

### TA的文章

* ##### [类人智能赋能：谷歌翻译获 Gemini 升级，实现俚语精准翻译与语气还原](/post/id/313754)

  2025-12-15 17:42:30
* ##### [高危 pgAdmin 远程代码执行漏洞（CVE-2025-13780）绕过此前修复：可通过恶意数据库恢复实现服务器接管](/post/id/313757)

  2025-12-15 17:41:52
* ##### [新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联](/post/id/313760)

  2025-12-15 17:41:05
* ##### [攻击组织 SHADOW-VOID-042 仿冒趋势科技发起钓鱼攻击，目标直指关键基础设施](/post/id/313762)

  2025-12-15 17:40:27
* ##### [高危 Plesk 漏洞（CVE-2025-66430）风险通告：可通过本地权限提升与 Apache 配置注入实现服务器完全接管](/post/id/313765)

  2025-12-15 17:39:47

### 相关文章

* ##### [类人智能赋能：谷歌翻译获 Gemini 升级，实现俚语精准翻译与语气还原](/post/id/313754)

  2025-12-15 17:42:30
* ##### [高危 pgAdmin 远程代码执行漏洞（CVE-2025-13780）绕过此前修复：可通过恶意数据库恢复实现服务器接管](/post/id/313757)

  2025-12-15 17:41:52
* ##### [新型后门程序 NANOREMOTE：滥用谷歌云端硬盘 API 实现隐秘命令与控制通信，且与 FINALDRAFT 间谍组织存在关联](/post/id/313760)

  2025-12-15 17:41:05
* ##### [攻击组织 SHADOW-VOID-042 仿冒趋势科技发起钓鱼攻击，目标直指关键基础设施](/post/id/313762)

  2025-12-15 17:40:27
* ##### [高危 Plesk 漏洞（CVE-2025-66430）风险通告：可通过本地权限提升与 Apache 配置注入实现服务器完全接管](/post/id/313765)

  2025-12-15 17:39:47
* ##### [Apache StreamPark 漏洞风险通告：硬编码密钥与 AES ECB 模式致数据解密及令牌伪造风险](/post/id/313768)

  2025-12-15 17:39:22
* ##### [新型 BlackForce 钓鱼工具包：攻击者借浏览器中间人（MitB）攻击窃取凭证并绕过多因素认证（MFA）](/post/id/313774)

  2025-12-15 17:37:50

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