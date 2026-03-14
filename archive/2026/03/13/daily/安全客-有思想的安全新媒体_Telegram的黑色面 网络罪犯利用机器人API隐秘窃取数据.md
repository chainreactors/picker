---
title: Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据
url: https://www.anquanke.com/post/id/315158
source: 安全客-有思想的安全新媒体
date: 2026-03-13
fetch_date: 2026-03-14T04:03:08.880137
---

# Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据

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

# Telegram的黑色面 网络罪犯利用机器人API隐秘窃取数据

阅读量**24941**

发布时间 : 2026-03-13 10:32:51

**x**

##### 译文声明

本文是翻译文章，文章原作者 Ddos ，文章来源：securityonline

原文地址：<https://securityonline.info/the-dark-side-of-telegram-how-cybercriminals-weaponize-bot-apis-for-stealthy-data-exfiltration/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

数以百万计用户使用 Telegram 进行安全即时通讯，然而在网络安全领域，该平台正暴露出黑暗一面。Cofense 最新报告显示，该平台备受关注的机器人功能正**被攻击者频繁滥用**，成为高效的数据窃取**命令与控制（C2）中心**。

通过使用**合法的 Telegram Bot API**，网络罪犯将简单的自动化账号变成窃取数据的 “上帝视角” 入口。

Telegram 提供的丰富 Web API 本意是帮助开发者构建自动化工具，但这些功能也被恶意机器人利用，可在私密聊天中发送消息，并将截图、窃取的凭证压缩包等文件**直接上传到攻击者设备**。

正如报告所指出：**攻击者经常将 Telegram 机器人作为一种数据外带渠道，借助的却是合法合规的服务接口。**

2024 年第一季度至 2025 年第二季度期间，在被分析的所有恶意软件攻击活动中，约**3.8%** 将 Telegram 作为主要 C2 基础设施；在凭证钓鱼攻击中，这一比例为**2.3%**。

这种攻击手段的优势在于**极强的隐蔽性**。由于流量指向 `api.telegram.org`，很容易混入正常网络行为中，绕过基础防火墙检测。

攻击者通常通过三种方式滥用该 API：

* **直接脚本调用**：在受害主机上的恶意脚本直接发起 HTTPS 请求。
* **凭证钓鱼**：受害者在伪造登录页面提交信息后，立即将账号密码发送至机器人。
* **入侵提醒**：受害者点击恶意链接的瞬间通知攻击者，**实时监控攻击效果**。

外泄的数据不只是文本，攻击者还频繁使用 `sendDocument` 方法上传最大**50MB**的文件，其中通常包含**截图与存有被盗凭证的文本文件**。

为应对这种 “合法接口滥用”，安全团队需关注特定 API 特征。大部分恶意请求具有固定格式：

`hxxps[://]api[.]telegram[.]org/bot<token>/METHOD_NAME`

需要重点监控的高频滥用方法包括：

* `sendMessage`：用于外带文本数据与账号凭证
* `sendDocument`：用于上传大容量窃取文件
* `getFile`：用于攻击者从远程环境下载文件

如果企业业务**不使用 Telegram 机器人**，报告建议采取简单但有效的措施：**直接屏蔽 Telegram Bot API 请求**，对 `api[.]telegram[.]org/bot` 接口配置拦截规则。

与往常一样，**第一道防线仍是用户安全意识**。只要用户不与可疑消息、内嵌链接或恶意文件交互，任何机器人都无法窃取数据。

本文翻译自securityonline [原文链接](https://securityonline.info/the-dark-side-of-telegram-how-cybercriminals-weaponize-bot-apis-for-stealthy-data-exfiltration/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315158](/post/id/315158)

安全KER - 有思想的安全新媒体

本文转载自: [securityonline](https://securityonline.info/the-dark-side-of-telegram-how-cybercriminals-weaponize-bot-apis-for-stealthy-data-exfiltration/)

如若转载,请注明出处： <https://securityonline.info/the-dark-side-of-telegram-how-cybercriminals-weaponize-bot-apis-for-stealthy-data-exfiltration/>

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

![](https://p0.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1090**

* 粉丝
* **6**

### TA的文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13

### 相关文章

* ##### [Ally WordPress插件高危SQL注入漏洞 威胁40万个网站](/post/id/315140)

  2026-03-13 10:34:49
* ##### [OpenAI战略调整Sora视频AI将直接接入ChatGPT](/post/id/315145)

  2026-03-13 10:34:23
* ##### [HPE发布Aruba OS高危漏洞预警 可未授权重置密码](/post/id/315148)

  2026-03-13 10:34:00
* ##### [能感知自身正在被测试的AI Anthropic关于Claude自我意识的惊人发现](/post/id/315152)

  2026-03-13 10:33:36
* ##### [GitLab发布紧急安全更新 修复高危XSS与API拒绝服务漏洞](/post/id/315155)

  2026-03-13 10:33:13
* ##### [Armadin获1.9亿美元融资 用AI实现自动化红队攻防](/post/id/315161)

  2026-03-13 10:32:28
* ##### [Splunk修复文件预览功能中的高危RCE漏洞](/post/id/315164)

  2026-03-13 10:32:03

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