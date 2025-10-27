---
title: ChatGPT Operator 遭提示注入攻击
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589728&idx=3&sn=a005da20fc0a49c5e16d1ada1109ad46&chksm=b18c2aaa86fba3bc13efec4f0ade8cc48cb172e9486d09bd97b185c29dea9d667a9327beb034&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-19
fetch_date: 2025-10-06T20:47:14.391586
---

# ChatGPT Operator 遭提示注入攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EWD0MdncKREanmoUwqiaOW0b9MUvmiaAquR1v8cN1yRReWaw9e2zLCfymu5N9NfVCEKjRvXKLVvZxg/0?wx_fmt=jpeg)

# ChatGPT Operator 遭提示注入攻击

看雪学苑

看雪学苑

近日，OpenAI旗下的ChatGPT Operator因存在提示注入漏洞而引发广泛关注。作为一款专为ChatGPT Pro用户设计的尖端研究工具，ChatGPT Operator具备强大的网页浏览和推理能力，能够帮助用户完成诸如研究主题、预订旅行以及与网站互动等任务。然而，最新研究显示，该工具可能被恶意利用，从而导致用户敏感信息泄露。

**攻击原理：提示注入如何运作**

提示注入是一种将恶意指令嵌入文本或网页内容中的技术。在ChatGPT Operator的场景中，攻击者通过以下步骤实现数据泄露：

* **劫持Operator：**攻击者将恶意指令托管在GitHub Issues等平台，或嵌入网站文本中。
* **导航至敏感页面：**诱导Operator访问包含敏感个人信息（如电子邮件或电话号码）的认证页面。
* **通过第三方网站泄露数据：**操纵Operator将敏感信息复制并粘贴到恶意网页中，无需表单提交即可完成数据捕获。

在一次演示中，攻击者成功诱骗Operator从用户的YC Hacker News账户中提取私人电子邮件地址，并将其粘贴到第三方服务器的输入字段中。这种攻击方式在Booking.com和The Guardian等多个知名网站上均能无缝执行。

**OpenAI的缓解措施**

面对这一漏洞，OpenAI已经采取了多层次的防御措施：

* **用户监控：**提示用户监控Operator的行为，包括输入的文本和点击的按钮。然而，这种方法高度依赖用户的警惕性，难以完全杜绝风险。
* **内联确认请求：**对于某些操作，Operator会在聊天界面中请求用户确认后再继续执行。尽管这一措施在某些情况下有效，但在早期测试中仍被绕过。
* **带外确认请求：**在跨网站边界或执行复杂操作时，Operator会显示侵入式确认对话框，解释潜在风险。但这些防御措施并非万无一失，仍存在被突破的可能性。

尽管OpenAI采取了上述措施，但由于提示注入攻击具有概率性，攻击和防御都取决于特定条件是否满足，因此这类攻击仍然部分有效。

如果这一漏洞被恶意利用，攻击者将能够访问存储在认证网站上的敏感个人信息。由于Operator会话在服务器端运行，OpenAI可能也会接触到会话Cookie、授权令牌等敏感数据。这些攻击不仅削弱了人们对自主AI代理的信任，还凸显了开发强大安全措施的紧迫性。

资讯来源：cybersecuritynews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibExiboJzOiafqGLvlOkrmU6NIr3qSr7ibpkIo2N5mhCTNXoMl37s2oRSIDw/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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