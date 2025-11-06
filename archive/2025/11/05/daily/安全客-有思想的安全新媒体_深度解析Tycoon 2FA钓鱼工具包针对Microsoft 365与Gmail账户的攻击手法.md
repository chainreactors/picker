---
title: 深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法
url: https://www.anquanke.com/post/id/313007
source: 安全客-有思想的安全新媒体
date: 2025-11-05
fetch_date: 2025-11-06T03:12:14.458786
---

# 深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法

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

# 深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法

阅读量**21401**

发布时间 : 2025-11-05 17:54:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/attack-techniques-of-tycoon-2fa-phishing-kit/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

**Tycoon 2FA钓鱼工具包**自2023年8月问世以来，已成为最复杂的“钓鱼即服务”（Phishing-as-a-Service）平台之一，专门设计用于绕过Microsoft 365和Gmail账户的**双因素认证（2FA）** 和**多因素认证（MFA）** 保护。

这一高级威胁采用**中间人攻击（Adversary-in-the-Middle）** 手法，利用反向代理服务器托管高度逼真的钓鱼页面——这些页面完美复制合法登录界面，同时**实时捕获用户凭证和会话Cookie**。

根据Any.run 恶意软件趋势追踪数据，Tycoon 2FA今年已导致**超64,000起报告事件**，成为当前最普遍的钓鱼威胁之一。

攻击通过多种分发渠道传播，包括恶意PDF文档、SVG文件、PowerPoint演示文稿以及包含钓鱼链接的电子邮件。

威胁行为者还利用**Amazon S3存储桶、Canva和Dropbox等云存储平台**托管伪造登录页面，使传统安全解决方案更难检测。

该攻击活动的特别危险性在于，即使启用了双因素认证，它仍能**窃取验证码**，使这一安全措施在工具包的复杂拦截技术面前形同虚设。

Cybereason分析师发现，该钓鱼工具包实施**多重重定向前检查**作为反检测防御机制，包括域名验证、CAPTCHA挑战、机器人与扫描工具检测，以及主动识别安全研究员代码分析的调试器检查。

这些检查确保只有真实受害者会进入最终钓鱼页面，而自动化安全工具和分析师则被重定向至良性网站。

工具包还通过分析登录尝试的错误消息，展现出对组织安全策略的深入理解，使攻击者能够**定制攻击活动以实现最大效果**。

其技术复杂性还体现在使用模板动态生成伪造登录页面——基于Microsoft服务器的实际响应，创造无缝体验诱导用户输入MFA验证码，这些验证码随后被**实时转发至合法服务器**，成功绕过这一关键安全层。

### **多阶段JavaScript执行与凭证窃取**

攻击通过复杂的**多阶段JavaScript执行链**展开，旨在规避检测并窃取凭证。
![]()

#### **第一阶段：内存中解压与执行**

初始HTML页面包含一个JavaScript文件，其中的base64编码载荷使用**LZ-string算法压缩**，在内存中解压并执行隐藏载荷。

#### **第二阶段：DOM消失术（DOM Vanishing Act）**

第二阶段采用“DOM消失术”技术：恶意JavaScript代码在执行后**从文档对象模型（DOM）中自我删除**，使检查页面代码的安全工具无法发现痕迹。

脚本包含三个不同的base64编码载荷，每个设计用于特定条件下运行：

* **第一个载荷**使用XOR密码混淆，仅当`window.location.pathname.split` 包含感叹号或美元符号时执行——确认用户通过预期恶意链接而非自动化扫描到达页面。

![]()

#### **凭证窃取与数据加密流程**

* **电子邮件提取**：在受害者电子邮件地址后附加“WQ”生成自定义字符串，通过POST请求发送至C2服务器的`/zcYbH5gqRHbzSQXiK8YtTbhpNSGtkZc6xbMyRBGazbWU8fjfq`端点，服务器响应使用CryptoJS库解密的AES加密载荷。

当受害者在伪造登录页面输入凭证时，作为中间人的攻击者立即接收信息并提交至合法Microsoft服务器。

随后，受害者的网页基于服务器响应通过webparts动态更新，使钓鱼尝试显得无缝且高度可信。

最终JavaScript载荷收集浏览器信息（如`navigator.userAgent` ）并发送请求至地理位置服务，使用硬编码密钥加密收集的数据，然后传输至攻击者的`/tdwsch3h8IoKcUOkog9d14CkjDcaR0ZrKSA95UaVbbMPZdxe`端点，完成凭证窃取操作。

**防御建议**：

1. 警惕异常链接和附件，尤其是要求“紧急登录”或“验证账户”的邮件。
2. 启用**硬件令牌（如YubiKey）** 替代短信/应用验证码，降低中间人攻击风险。
3. 部署能够检测DOM操作异常和内存中恶意脚本的高级端点保护工具。
4. 对员工进行钓鱼识别培训，强调验证登录页面URL和SSL证书的重要性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/attack-techniques-of-tycoon-2fa-phishing-kit/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/313007](/post/id/313007)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/attack-techniques-of-tycoon-2fa-phishing-kit/)

如若转载,请注明出处： <https://cybersecuritynews.com/attack-techniques-of-tycoon-2fa-phishing-kit/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **653**

* 粉丝
* **6**

### TA的文章

* ##### [一文读懂香港金融科技周：DART将带领香港金融科技驶向何方？](/post/id/313039)

  2025-11-05 18:35:34
* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [深度解析Tycoon 2FA钓鱼工具包针对Microsoft 365与Gmail账户的攻击手法](/post/id/313007)

  2025-11-05 17:54:36
* ##### [新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷](/post/id/313012)

  2025-11-05 17:54:19
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59

### 相关文章

* ##### [WordPress的AI引擎插件中存在严重漏洞（CVE-2025-11749），可致网站被攻击者完全控制](/post/id/313004)

  2025-11-05 17:54:53
* ##### [新型NGate NFC恶意软件通过中继受害者手机的EMV数据与PIN码，对ATM实施盗刷](/post/id/313012)

  2025-11-05 17:54:19
* ##### [CISA发布关键漏洞紧急警报：Gladinet LFI/RCE漏洞与控制面板CWP管理员权限接管漏洞正遭积极利用](/post/id/313015)

  2025-11-05 17:53:59
* ##### [全球网络间谍组织利用ZipperDown漏洞及Android零日漏洞，通过邮件客户端实现一键远程代码执行与账户接管](/post/id/313018)

  2025-11-05 17:53:37
* ##### [React Native CLI 中存在严重漏洞（CVE-2025-11953，CVSS 9.8），攻击者可经由暴露的Metro开发服务器实现RCE](/post/id/313021)

  2025-11-05 17:53:18
* ##### [Bugcrowd收购自动化测试工具Mayhem，以强化其应用安全测试平台能力](/post/id/313024)

  2025-11-05 17:52:48
* ##### [Open VSX扩展市场中出现新型“SleepyDck”恶意软件，允许攻击者远程控制Windows系统](/post/id/313027)

  2025-11-05 17:52:17

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