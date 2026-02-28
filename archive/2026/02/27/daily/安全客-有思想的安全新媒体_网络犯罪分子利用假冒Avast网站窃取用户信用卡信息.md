---
title: 网络犯罪分子利用假冒Avast网站窃取用户信用卡信息
url: https://www.anquanke.com/post/id/314875
source: 安全客-有思想的安全新媒体
date: 2026-02-27
fetch_date: 2026-02-28T03:49:49.199728
---

# 网络犯罪分子利用假冒Avast网站窃取用户信用卡信息

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

# 网络犯罪分子利用假冒Avast网站窃取用户信用卡信息

阅读量**22433**

发布时间 : 2026-02-27 10:30:44

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/fake-avast-website/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

网络犯罪分子搭建了一个**高仿假冒 Avast 网站**，发起极具迷惑性的钓鱼攻击，专门窃取毫无防备用户的**信用卡信息**。

该钓鱼页面几乎**完美复刻**了 Avast 官方网站的样式，甚至直接从官方内容分发网络盗用了真实的 Avast 标志。

页面同样显示 “主页”“我的账户”“帮助中心” 等常规导航链接，样式与官网完全一致。

页面正中央有一条醒目的橙色提示，声称用户已被扣除**499.99 欧元**的 Avast 产品费用。

页面胁迫用户必须在**72 小时内取消订阅**，却又同时宣称超过 48 小时的交易无法撤销 —— 这种故意制造的矛盾信息，目的是迷惑并施压受害者。

该网站专门针对**法语区用户**，借助 Avast 的品牌信誉，诱骗用户泄露信用卡号、有效期、安全码等敏感财务信息。

假冒扣费旁的日期会**根据访客系统时间自动更新**，让每个访问者都误以为扣费就发生在 “今天”。

日期会动态变化，但**499.99 欧元**的金额保持不变 —— 这个金额足以引发恐慌，同时又符合高端软件订阅的合理价位。

整个过程**不会产生真实扣费**，攻击目的纯粹是心理恐吓：让受害者误以为信用卡被盗刷，从而主动提交信息申请退款。

### 信息窃取表单

在虚假收据下方，页面放置了一个**退款表单**，要求用户填写完整个人信息，包括姓名、邮箱、电话、地址和城市，声称用于身份验证。

填写完成后会弹出窗口，要求输入**信用卡号、有效期和 CVV 安全码**，谎称是 “退款所需”。

为显得真实可信，该网站甚至使用**Luhn 算法**校验银行卡号，这是银行系统常用的合法验证方式。

用户信息会通过 **POST 请求** 发送到 **send.php** 脚本，所有填写的内容会直接传输到攻击者服务器。

提交后，页面会显示提示：“您的申请正在处理中，感谢您的咨询。”

最后还有一个极具欺骗性的按钮，标注 “卸载 Avast”，进一步伪装并诱导用户卸载真正的安全软件。

为增强伪装效果，假冒网站还嵌入了 **Tawk.to** 在线聊天插件，ID 为：**689773de2f0f7c192611b3bf**。

这让攻击者可以**实时监控**受害者状态并进行对话，借机安抚犹豫的用户，一步步引导其完成虚假退款流程。

该钓鱼攻击可覆盖多种目标人群：

想要退款的真实 Avast 用户、对旧订阅感到困惑的用户、被假扣费吓到的非用户，以及想投机领取 “莫名退款” 的人。

由于网站**从不要求账户信息或授权密钥**，所有类型访客都可能落入同一个陷阱。

本文翻译自gbhackers [原文链接](https://gbhackers.com/fake-avast-website/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314875](/post/id/314875)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/fake-avast-website/)

如若转载,请注明出处： <https://gbhackers.com/fake-avast-website/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p4.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p0.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1030**

* 粉丝
* **6**

### TA的文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [网络犯罪分子利用假冒Avast网站窃取用户信用卡信息](/post/id/314875)

  2026-02-27 10:30:44
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42

### 相关文章

* ##### [瞻博网络PTX路由器曝高危漏洞 可被未授权攻击者获取root权限](/post/id/314874)

  2026-02-27 10:31:04
* ##### [GitHub Copilot遭被动提示注入攻击 可实现代码仓库完全接管](/post/id/314882)

  2026-02-27 10:30:24
* ##### [MoonPay推出Agents为AI系统提供钱包与链上现金流](/post/id/314887)

  2026-02-27 10:30:01
* ##### [Python库ormar曝出高危SQL注入漏洞](/post/id/314890)

  2026-02-27 10:29:42
* ##### [未修补的ActiveMQ漏洞引发二次入侵与LockBit勒索攻击](/post/id/314906)

  2026-02-27 10:29:22
* ##### [Claude Code推出远程控制功能 实现移动端全自主开发](/post/id/314902)

  2026-02-27 10:28:57
* ##### [思科SD-WAN曝出CVSS 10级零日漏洞 已遭UAT-8616组织利用](/post/id/314880)

  2026-02-27 10:28:35

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