---
title: npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员
url: https://www.anquanke.com/post/id/313249
source: 安全客-有思想的安全新媒体
date: 2025-11-19
fetch_date: 2025-11-20T03:08:27.900115
---

# npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员

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

# npm供应链攻击预警：黑客利用Adspect伪装技术与虚假加密货币验证码同时欺骗用户与安全研究人员

阅读量**15894**

发布时间 : 2025-11-19 17:37:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos，文章来源：securityonline

原文地址：<https://securityonline.info/npm-supply-chain-attack-hackers-use-adspect-cloaking-and-fake-crypto-captcha-to-deceive-victims-and-researchers/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Socket 威胁研究团队发现了一场高度协同的恶意软件活动，涉及七个 npm 包，均由化名“dino\_reborn”的威胁行为者发布。这些包使用 **Adspect 驱动的 cloaking（伪装）技术**、**反分析 JavaScript** 和**虚假 CAPTCHA 界面**，将毫无防备的受害者引向恶意载荷，同时向安全研究人员隐藏其活动。

最引人注目的发现之一是，攻击者构建了一个完整的**虚假网站**，专门用于迷惑安全研究人员，而真实受害者则会被引导至欺骗性的 CAPTCHA 流程。

正如 Socket 所描述：
“当访问其中一个包构建的虚假网站时，威胁行为者会判断访问者是受害者还是安全研究人员。”

### 针对受害者的攻击流程

如果 Adspect API 判断访问者是合法用户（而非分析代码的研究人员）：

* 他们会看到一个仿冒加密货币平台（如 standx.com 、jup.ag 或 uniswap.org ）的虚假 CAPTCHA。
* 点击 CAPTCHA 后：
  + 3 秒虚假“验证中…”
  + 1 秒虚假“成功…”
  + 随后受害者被静默重定向至恶意载荷。

Socket 明确指出此机制：
“如果返回 ok:true — 显示虚假 CAPTCHA 并保存重定向 URL。”

### 针对安全研究人员的诱饵

安全研究人员则会看到一个逼真的诱饵网站：

“如果返回 ok:false — 显示空白页面。”

这个空白页面是一个名为 **Offlido** 的虚假公司的精致商业网站，包含样板法律文本、流畅的 UI 和隐私政策。

### 受影响的 npm 包

所有七个包均由用户 geneboo@proton[.]me 发布，包括：

1. signals-embed
2. dsidospsodlks
3. applicationooks21
4. application-phskck
5. integrator-filescrypt2025
6. integrator-2829
7. integrator-2830

Socket 确认：
“七个包中有六个包含恶意软件，彼此间差异极小。剩余一个包用于构建恶意网页。”

这些包共享代码、API 和基础设施，在 npm 中形成了一个**完全互联的恶意软件生态系统**。

### 技术细节：指纹识别与对抗分析

威胁行为者使用商业伪装服务 **Adspect** 对用户进行指纹识别。恶意软件收集详细信息字段，包括用户代理、主机、引用页、端口、地区、编码、时间戳和浏览器语言。

Socket 引用了攻击者自己的俄语注释：
“We collect the full data just like in the PHP version.”（我们像 PHP 版本一样收集完整数据。）

并解释其目的：
“这些数据点为 Adspect 提供了高保真指纹……以判断流量来自潜在受害者还是安全研究人员。”

基于此指纹，Adspect 决定：

1. 返回 ok:true → 显示 CAPTCHA → 导向恶意重定向
2. 返回 ok:false → 提供诱饵空白页面
3. 返回错误 → 显示内置备用网站

### 对抗分析措施

这些包极力抵抗检查。Socket 指出代码：
“阻止右键点击、阻止 F12、阻止 Ctrl+U、阻止 Ctrl+Shift+I、检测开发者工具……页面不断刷新。”

这些措施使分析师极难查看：

1. DOM 结构
2. JavaScript 逻辑
3. 网络请求
4. 重定向机制

正如 Socket 所说：
“所有这些策略使安全研究人员极难分析代码。”

### CAPTCHA 设计：伪装与延迟

CAPTCHA 序列故意设计得很慢：

1. 3 秒验证
2. 1 秒成功
3. 然后恶意重定向

研究人员表示：
“CAPTCHA 是重定向的完美伪装……且可能不会被安全系统标记。”

这种设计有助于：

1. 规避自动化扫描工具
2. 欺骗用户相信重定向是合法的
3. 允许攻击者通过 Adspect 动态更新恶意载荷 URL

### 目标：仿冒加密货币平台

虚假 CAPTCHA 显示与真实加密货币交易所相关的徽标或域名：

1. standx.com
2. jup.ag
3. uniswap.org

Socket 指出：
“威胁行为者希望页面看起来像是受害者在向真实交易所验证……因此其目标很可能是窃取加密货币。”

### 诱饵页面：Offlido 虚假公司

第七个包 signals-embed 包含诱饵空白页面的代码——一个名为 Offlido 的虚假公司网站。

其 README 中有俄语解释：
“A single JS with a ‘snapshot’ of the Signals Research website for embedding into Google Sites.”（用于嵌入 Google Sites 的 Signals Research 网站“快照”的单个 JS。）

Socket 澄清其真实目的：
“实际上，这是一个静态伪装载荷……一个旨在看起来合法的虚假品牌网站，同时掩盖攻击者的基础设施。”

Offlido 页面异常精致，包含合规文本、联系表单和完整的隐私政策部分——这在快速制作的恶意软件页面中极为罕见。

恶意包和诱饵页面共享相同的 DOM 容器，实现无缝切换。

Socket 写道：
“安全研究人员和受害者两条路径共享 DOM 框架……伪装内容和载荷无缝嵌入同一界面。”

本文翻译自securityonline [原文链接](https://securityonline.info/npm-supply-chain-attack-hackers-use-adspect-cloaking-and-fake-crypto-captcha-to-deceive-victims-and-researchers/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313249](/post/id/313249)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/npm-supply-chain-attack-hackers-use-adspect-cloaking-and-fake-crypto-captcha-to-deceive-victims-and-researchers/)

如若转载,请注明出处： <https://securityonline.info/npm-supply-chain-attack-hackers-use-adspect-cloaking-and-fake-crypto-captcha-to-deceive-victims-and-researchers/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

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

* ##### [Windows 11 新增云重建与时间点还原系统恢复工具](/post/id/313271)

  2025-11-19 17:41:26
* ##### [Thunderbird新增原生支持，实现对Microsoft Exchange账户的全面兼容](/post/id/313267)

  2025-11-19 17:41:08
* ##### [Cloudflare全球服务中断，引发互联网大面积瘫痪——多家主流网络平台无法访问](/post/id/313258)

  2025-11-19 17:40:41
* ##### [谷歌已修复2025年第7个被积极利用的Chrome零日漏洞](/post/id/313261)

  2025-11-19 17:40:10
* ##### [macOS平台曝出“Nova”钱包窃取程序：通过替换Ledger/Trezor应用为钓鱼克隆版来窃取用户助记词](/post/id/313255)

  2025-11-19 17:39:45
* ##### [新型.NET加载器“隐匿窃密者”通过高级隐写术将LokiBot窃密木马植入BMP/PNG图片](/post/id/313252)

  2025-11-19 17:38:46
* ##### [SolarWinds Serv-U 中存在严重漏洞（CVSS 9.1），可导致已认证的管理员实现远程代码执行并完成路径绕过](/post/id/313245)

  2025-11-19 17:37:15

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