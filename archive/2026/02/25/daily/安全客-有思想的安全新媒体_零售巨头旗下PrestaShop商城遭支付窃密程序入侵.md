---
title: 零售巨头旗下PrestaShop商城遭支付窃密程序入侵
url: https://www.anquanke.com/post/id/314832
source: 安全客-有思想的安全新媒体
date: 2026-02-25
fetch_date: 2026-02-26T04:09:52.781990
---

# 零售巨头旗下PrestaShop商城遭支付窃密程序入侵

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

# 零售巨头旗下PrestaShop商城遭支付窃密程序入侵

阅读量**24303**

发布时间 : 2026-02-25 14:18:58

**x**

##### 译文声明

本文是翻译文章，文章原作者 Alex Lekander，文章来源：cyberinsider

原文地址：<https://cyberinsider.com/retail-giants-prestashop-store-compromised-by-payment-skimmer/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

全球大型连锁超市之一的线上商城中，安全人员发现了**数字支付窃密程序**。

尽管 Sansec 已多次尝试通报，但截至本文发布时，恶意代码仍**处于活跃状态**。

研究人员表示，该窃密程序于 **2026 年 2 月 16 日 06:13 UTC** 首次在某电商站点被发现。该网站隶属于**全球前十连锁超市**，年收入约 **1000 亿欧元**，在 25 个国家拥有超 10000 家门店。该零售商部分电商系统基于 **PrestaShop** 搭建，这是一款广泛使用的开源电商平台。

Sansec 称，2 月 16 日当天已**六次尝试通知**该企业，包括官网公开邮箱、`security.txt` 中的安全联系方式、以及在 LinkedIn 上直接私信该公司 CISO。截至 2 月 20 日，研究人员未收到任何回复，并确认**窃密程序仍在运行**。

此次攻击使用了一种名为 **“双击窃密（double-tap skimming）”** 的技术。随着商家越来越多地使用符合 **PCI-DSS** 规范的托管支付页面，此类攻击愈发普遍。

根据 PCI-DSS 规则，敏感的银行卡信息必须输入到服务商托管的安全表单中（本次案例为 PayPlug）。

攻击者绕过该限制的方式是：在结账页面**直接插入高度仿真的伪造支付表单**。

受害者会在这个伪造的浮层中输入卡号、有效期和 CVV，随后被无缝跳转到**真实支付页面**并被要求重新输入信息。

大多数用户以为第一次输入失败，便重新完成支付，完全不知情自己的银行卡信息已被盗取。

![]()

Sansec 指出，**生成式 AI** 正在加速此类欺诈行为，攻击者可快速制作**贴合品牌、多语言、本地化**的仿冒支付浮层，适配不同市场。

该窃密程序基于一套**可复用框架**开发，目前看来支持 **WordPress、Magento、PrestaShop、OpenCart** 等多种系统。

在启动前，它会执行多项检查，判断访客是否为**管理员**。

如果是管理员，脚本会记录 `Admin detected` 并中止运行，确保商家在测试结账流程时**看不到恶意表单**。

该框架支持 **7 种注入模式**，包括替换、浮层、弹窗、离屏渲染等，可适配不同结账布局。

其内置 “强力隐藏” 机制 ，即使网站自身 JavaScript 尝试恢复真实支付表单，也会被持续压制。

从技术实现来看，该窃密程序**仅在结账页面激活**，并使用 `localStorage` 管理运行状态。

它通过事件监听器监控所有 `input`、`select`、`textarea` 元素，甚至利用 `MutationObserver` 追踪 `Select2`、`Vue Select` 等动态下拉组件。

窃取的数据以 `mn_` 为前缀存储在 `localStorage` 中，其中银行卡信息明确保存为 `cardNum`、`exp`、`cvv` 字段。

为防止数据被覆盖，脚本对 `localStorage.setItem` 进行 **猴子补丁（monkey-patch）** 劫持，阻止用更短字符串覆盖已保存的卡号。

当受害者点击结账按钮时，恶意程序会校验卡号**至少 13 位**，然后构造包含银行卡、账单信息与浏览器 UA 的 JSON 载荷，进行 **Base64 编码**，并通过 GET 请求发送到 `stylemercedes.top`。

该接口伪装成**分析统计 API**，避免引起怀疑。

数据窃取完成后，恶意代码会清除注入的元素、恢复原始结账页面，移除 `disabled`、`aria-disabled` 等属性与相关 CSS 类以启用支付按钮，然后**自动触发真实支付流程**。

用户可在结账时使用**预充值一次性虚拟卡**，降低支付卡信息被盗的风险。

本文翻译自cyberinsider [原文链接](https://cyberinsider.com/retail-giants-prestashop-store-compromised-by-payment-skimmer/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/314832](/post/id/314832)

安全KER - 有思想的安全新媒体

本文转载自: [cyberinsider](https://cyberinsider.com/retail-giants-prestashop-store-compromised-by-payment-skimmer/)

如若转载,请注明出处： <https://cyberinsider.com/retail-giants-prestashop-store-compromised-by-payment-skimmer/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**3赞

收藏

![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1020**

* 粉丝
* **6**

### TA的文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [零售巨头旗下PrestaShop商城遭支付窃密程序入侵](/post/id/314832)

  2026-02-25 14:18:58
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52

### 相关文章

* ##### [黑客在新型NPM供应链攻击中，将Pulsar远控木马隐匿于PNG图片内](/post/id/314815)

  2026-02-25 14:19:33
* ##### [Android恶意软件运行时调用Google Gemini](/post/id/314819)

  2026-02-25 14:19:27
* ##### [黑客利用BeyondTrust高危漏洞 在多行业部署VShell与SparkRAT](/post/id/314825)

  2026-02-25 14:19:07
* ##### [多款PDF平台曝多个零日漏洞 可触发XSS与一键式攻击](/post/id/314837)

  2026-02-25 14:18:52
* ##### [黑客利用Facebook广告投放虚假Win11更新实施恶意攻击](/post/id/314844)

  2026-02-25 14:18:43
* ##### [银狐APT组织利用BYOVD攻击投放Winos 4.0恶意软件](/post/id/314847)

  2026-02-25 14:18:35
* ##### [CISA警告USR-W610物联网设备存在9.8分高危漏洞且已无补丁支持](/post/id/314851)

  2026-02-25 14:11:13

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