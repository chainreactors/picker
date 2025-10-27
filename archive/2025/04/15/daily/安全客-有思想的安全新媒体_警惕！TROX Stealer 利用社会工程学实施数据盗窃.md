---
title: 警惕！TROX Stealer 利用社会工程学实施数据盗窃
url: https://www.anquanke.com/post/id/306520
source: 安全客-有思想的安全新媒体
date: 2025-04-15
fetch_date: 2025-10-06T22:05:07.596286
---

# 警惕！TROX Stealer 利用社会工程学实施数据盗窃

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

# 警惕！TROX Stealer 利用社会工程学实施数据盗窃

阅读量**239218**

发布时间 : 2025-04-14 16:04:08

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/trox-stealer-exfiltrate-sensitive-data/>

译文仅供参考，具体内容表达以及含义原文为准。

一种新被识别出的恶意软件，名为 TROX Stealer，已成为对消费者数据安全的重大威胁，它利用心理操纵手段和复杂的技术来窃取敏感信息。

Sublime Security 的分析师在 2024 年 12 月首次发现了这种恶意软件即服务（MaaS）产品，它的目标是存储的信用卡信息、浏览器凭据、加密货币钱包，以及诸如 Discord 和 Telegram 等平台的会话文件。

该恶意软件采用每周订阅模式运行，能够快速部署短期攻击活动，注重攻击数量而非长期持续性。

TROX Stealer 通过利用基于紧迫性的社会工程学手段而与众不同。

攻击者通过伪装成债务催收通知或法律威胁的电子邮件来发送有效载荷，利用受害者的焦虑情绪来绕过他们的仔细审查。

这些信息通常是使用大语言模型（LLM）生成的，它们会引导收件人访问托管恶意可执行文件的仿冒域名。

有效载荷采用了多层混淆技术，包括将 Python 代码编译成本地二进制文件以及 WebAssembly（Wasm）偷渡技术，以逃避检测。

Sublime Security 的研究人员发现，该恶意软件的基础设施显示出一种有条理的操作安全方法。

像 documents [.] debt-collection-experts [.] com 这样的攻击域名使用了带令牌的下载链接，以防止再次感染并增加分析难度。

该攻击活动的核心依赖于像 89.185.82.34（一个可疑的Tor出口节点）这样的 IP 地址，以及受 Cloudflare 保护的服务器，这表明恶意软件的编写者在匿名化方面下了功夫。

#### ****感染机制：从社会工程学到********无声********执行****

感染链始于一封精心制作的电子邮件，这封邮件敦促收件人立即采取行动以避免法律后果。

一个典型的主题行是 “最后警告：您的账户即将面临法律诉讼”，它会引导受害者点击一个标有 “债务催收法院文件” 的链接。

点击该链接会触发下载一个名为 DebtCollectionCase#######.exe 的可执行文件，其中占位符代表一个唯一的七位数标识符。

下载的可执行文件是使用 Nuitka 将 Python 脚本编译成本地二进制文件的，它会将组件提取到一个临时目录（% Temp%\onefile\_11536\_133873237425638862）中。

这些组件包括：

1.一个模仿合法法律文件的诱饵 PDF 文件（例如 client\_pdf\_case\_388.pdf）

2.一个嵌入恶意 JavaScript 代码的 Node.JS 解释器（node700.exe）

3.像 python312.dll 和 libcrypto-3.dll 这样的支持库

Python 脚本编排文件执行，分析过程中提取的内部文档显示：

def install\_files(user\_profile, target\_dir, source\_dir, exe\_pattern, pdf\_pattern):

# 将 ‘node\*.exe’ 和PDF文件复制到AppData目录

…  def run\_files(user\_profile, target\_dir, exe\_pattern, pdf\_pattern):

# 执行Node.JS二进制文件并打开诱饵PDF文件

…

诱饵 PDF 文件包含元数据工件，例如 “Modified: Copy\040388”，这是通过 PyPDF2 自动生成的签名。

与此同时，Node.JS 二进制文件会执行一个 Base64 编码的 WebAssembly 模块，使 Rust 编译的有效载荷能够在内存中运行：

var bytes = Buffer2.from(“AGFzbQEAAAABvwRHYAJ/fwBgAX8AYAJ/fwF/YAN/f38Bf2ADf39/A…”);  var wasmModule = new WebAssembly.Module(bytes);  var wasmInstance = new WebAssembly.Instance(wasmModule, imports);

这个 2MB 的 Wasm 二进制大对象包含超过 4700 个函数，其中许多函数与系统 API 交互以获取数据。

执行后，该恶意软件会将受害者系统的 JSON 配置文件发送到 172.22.117.177:2777，其中包括硬件规格和操作系统详细信息：

{

“username”: “admin”,

“osType”: “Windows\_NT”,

“cpuModel”: “Intel(R) Core(TM) i5-6400”,

“totalMemoryGB”: “3.99”  }

这个 IP 地址注册在伦敦的 “STARK INDUSTRIES SOLUTIONS LTD.” 名下，解析后指向一台托管有额外有效载荷（.json 和.js 文件）的服务器，这表明它具有动态的命令与控制（C2）能力。

TROX Stealer 使用基于紧迫性主题的诱饵以及快速变化的基础设施，使得传统的基于指标（IOC）的检测变得复杂。

防御者应优先对诸如从临时目录生成 node\*.exe 进程以及与高风险 IP 进行出站连接等行为进行监控。

该恶意软件对 Wasm 和由大语言模型生成的诱饵的依赖，凸显了需要先进的电子邮件安全解决方案，以便能够在社会工程学威胁到达终端用户之前将其拦截。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/trox-stealer-exfiltrate-sensitive-data/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306520](/post/id/306520)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/trox-stealer-exfiltrate-sensitive-data/)

如若转载,请注明出处： <https://cybersecuritynews.com/trox-stealer-exfiltrate-sensitive-data/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [恶意软件](/tag/%E6%81%B6%E6%84%8F%E8%BD%AF%E4%BB%B6)

**+1**6赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=175868)

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

* ##### [InsydeUEFI 漏洞 (CVE-2025-4275)： 安全启动绕过允许 Rootkits 和无法检测的恶意软件](/post/id/308341)

  2025-06-11 16:00:03
* ##### [假冒验证码基础架构 HelloTDS 使数百万设备感染恶意软件](/post/id/308293)

  2025-06-10 13:21:16
* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [ViperSoftX 不断进化： 新的 PowerShell 恶意软件具有隐蔽性和持久性](/post/id/308164)

  2025-06-05 13:29:03
* ##### [Lumma 窃取者恶意软件卷土重来，挑战全球打击行动](/post/id/308100)

  2025-06-04 15:42:31
* ##### [DragonForce 勒索软件集团利用定制负载和全球勒索活动攻击英国零售商](/post/id/307089)

  2025-05-06 14:34:45
* ##### [勒索软件对制造业的威胁日益加剧](/post/id/307053)

  2025-04-30 14:12:31

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