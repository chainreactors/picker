---
title: 新的 DoubleClickjacking 攻击利用双击来劫持帐户
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247580993&idx=1&sn=9cef8f9e885411deefa3dd1718756bec&chksm=e9146d7bde63e46d6f0696852e5e5dc1ea9b2c6006db56346d548914ef0d50494db9f8fafe58&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-01-28
fetch_date: 2025-10-06T20:10:41.986744
---

# 新的 DoubleClickjacking 攻击利用双击来劫持帐户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaS4rJgpU9Pyv0YXCk6ylUzcuWX9v1dPNFuVq5uCqR8OFjrZxWuK5sRJA/0?wx_fmt=jpeg)

# 新的 DoubleClickjacking 攻击利用双击来劫持帐户

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

点击劫持攻击的一种新变体称为“DoubleClickjacking”，攻击者可以诱骗用户使用双击授权敏感操作，同时绕过针对此类攻击的现有保护措施。

点击劫持，是指威胁者创建恶意网页，诱骗访问者点击隐藏或伪装的网页元素。这些攻击的工作原理是将隐藏 iframe 中的合法网页覆盖在攻击者创建的网页上。这个攻击者创建的网页旨在将其按钮和链接与隐藏 iframe 上的链接和按钮对齐。

然后，攻击者使用他们的网页来诱使用户单击链接或按钮，例如赢得奖励或查看某些图片。但是，当他们单击页面时，实际上是在单击隐藏 iframe（合法网站）上的链接和按钮，这可能会执行恶意操作，例如授权 OAuth 应用程序连接到其帐户或接受 MFA 请求。

多年来，网络浏览器开发人员引入了新功能来阻止大多数此类攻击，例如不允许跨站点发送 cookie 或引入关于站点是否可以构建 iframe 的安全限制（X-Frame-Options 或框架祖先）。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSic0j7jJvZYAeNz2mh4T8bDpNeUpNJ7FQkHVekKaFjibWh8m4KoPCibAKA/640?wx_fmt=png&from=appmsg)新的 DoubleClickjacking 攻击

网络安全专家 Paulos Yibelo 推出了一种名为 DoubleClickjacking 的新网络攻击，该攻击利用鼠标双击来诱骗用户在网站上执行敏感操作。

在这种攻击场景中，威胁者将创建一个网站，其中显示一个看似无害的带有诱惑的按钮，例如“单击此处”查看奖励或观看电影。当访问者单击该按钮时，将创建一个新窗口，覆盖原始页面并包含另一个诱惑，例如必须解决验证码才能继续。

在后台，原始页面上的 JavaScript 会将该页面更改为攻击者想要诱骗用户执行操作的合法站点。新的重叠窗口上的验证码会提示访问者双击页面上的某些内容来解决验证码问题。但是，此页面会侦听 mousedown 事件，并在检测到时快速关闭验证码覆盖层，从而导致第二次单击落在之前隐藏的合法页面上现在显示的授权按钮或链接上。

这会导致用户错误地单击公开的按钮，从而可能授权安装插件、OAuth 应用程序连接到其帐户或确认多重身份验证提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSad9OPgUZdlzhvxoBfnSQdNefw01NnlDTh4yP7Q9vyw938B2kGMHJfw/640?wx_fmt=png&from=appmsg)

DoubleClick劫持攻击流程

之所以如此危险，是因为它绕过了所有当前的点击劫持防御，因为它不使用 iframe，也不会尝试将 cookie 传递到另一个域。相反，这些操作直接发生在不受保护的合法网站上。

Yibelo 表示，这种攻击几乎影响了所有网站，并分享了利用 DoubleClickjacking 接管 Shopify、Slack 和 Salesforce 帐户的演示视频。

研究人员还说，这种攻击不仅限于网页，还可以用于浏览器扩展。“例如，我已经对顶级浏览器加密钱包进行了概念验证，这些钱包使用这种技术来授权 web3 交易和 dApp 或禁用 VPN 来暴露 IP 等，”Yibelo 解释道。

这也可以在手机中通过要求目标‘DoubleTap’来完成。为了防止此类攻击，安全研究员共享了 JavaScript，可以将其添加到网页中以禁用敏感按钮，直到有所反应为止。这将防止双击在删除攻击者的覆盖层时自动点击授权按钮。

除此之外，研究人员还提出了一个潜在的 HTTP 标头，该标头可以限制或阻止双击序列期间窗口之间的快速上下文切换。

参考及来源：https://www.bleepingcomputer.com/news/security/new-doubleclickjacking-attack-exploits-double-clicks-to-hijack-accounts/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSGgwttq0zs7BVkyC3YACmQ5RFmCpxfe45BhooDdVEibLicJCVbiak1Xia9g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28iaXkeTNVxuQBuxq7ljIBiaSuQG6kCJppBXs6DM1Cz0LwbgCniag7Psiaf9IEqCqn4bicTlAJl8Pfbvtw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过