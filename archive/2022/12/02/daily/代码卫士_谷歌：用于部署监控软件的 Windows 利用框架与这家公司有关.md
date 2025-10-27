---
title: 谷歌：用于部署监控软件的 Windows 利用框架与这家公司有关
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514853&idx=3&sn=88e11980665711f94e6ef7db974fda3d&chksm=ea948b8fdde30299af08619d2c5695a764b70368dcea1be39e1c5ec304023e9e61ad3731c8eb&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-12-02
fetch_date: 2025-10-04T00:18:07.129715
---

# 谷歌：用于部署监控软件的 Windows 利用框架与这家公司有关

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIRR7yRwH596WmicDdfXJeX2HicURbhPox6WahKpaJkm9EXnBRDdweiaQNg/0?wx_fmt=jpeg)

# 谷歌：用于部署监控软件的 Windows 利用框架与这家公司有关

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIrIkntER4Tr90Zhj3SLRHO8EwI0rmzhQiavicAGEMsVwk4Jy5d3nPiaf9g/640?wx_fmt=gif)

**谷歌威胁分析团队 (TAG) 指出，西班牙软件公司Variston IT 提供的一个利用框架和现已修复的位于 Chrome、Firefox web 浏览器和微软 Defender 安全应用中的多个漏洞之间存在关联。**

该团队指出，Variston IT公司和其它商业监控厂商一样，并非其官方声称的那样仅仅提供定制化安全解决方案。

谷歌 TAG 团队的研究员 Clement Lecigne 和 Benoit Sevens 在本周三提到，“今天，我们继续披露关于一个可能与 Varison IT 公司相关的利用框架。这家公司声称是定制化安全解决方案提供商。他们提供的 Heliconia 框架利用了位于Chrome、Firefox 和微软 Defender 中的多个 nday 漏洞，并提供所有必需工具，在目标设备上部署 payload。”

该利用框架由多个组件构成，每个组件都针对目标设备上软件中的具体安全漏洞：

* **Heliconia Noise****：**一个web框架，用于部署Chrome 渲染 bug 利用，之后部署Chrome 沙箱投医，在目标设备上安装代理。
* **Heliconia Soft****：**一个 web 框架，部署包含Windows Defender exploit CVE-2021-42298的PDF。
* **Heliconia Files****：**适用于 Linux 和 Windows 的一系列Firefox 利用，编号为CVE-2022-26485。

对于 Heliconia Noise 和 Heliconia Soft 而言，这些利用将最终在受陷设备上部署名为 “agent\_simple” 的代理。然而，分析该框架的样本发现，该框架中包含一个在无需执行任何恶意代码就运行并退出的代理。谷歌认为该框架的客户提供自己的代理或它是研究员无法访问的另外一个项目的组成部分。

即使目前尚未有证据表明这些安全漏洞已遭活跃利用，且谷歌、Mozilla和微软在2021年以及2022年末就已修复这些漏洞，但研究人员表示，“这些漏洞可能是已遭在野利用的0day。”

Variston IT 公司尚未就此事置评。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIVaY1fOYLVWGvP4CuibqxH9d9Ndxfk4C8oF4W0w711dbyLuoiaEhcw8ww/640?wx_fmt=png)

**谷歌追踪监控厂商**

今年6月份，谷歌TAG团队也提到意大利监控软件厂商 RCS Labs 在某些互联网服务提供商的帮助下，在意大利和哈萨克斯坦安卓和iOS 用户设备上部署商用监控工具。

在这些攻击活动中，目标被提示在路过式下载过程中安装伪装成合法移动运营商应用的恶意应用，以便在ISP切断用户的网络后重新连网。

一个月之后，谷歌TAG团队披露了另外一起监控活动，攻击者利用五个0day 安装由商用监控开发者 Cytrox 开发的 Predator 监控软件。当时谷歌称正在积极追踪30多个厂商，这些厂商公开程度和复杂程度不同，都在向受政府支持的威胁组织或行动者出售监控能力或利用。

谷歌TAG团队指出，“监控软件行业的增长将用户置于风险之中且导致互联网的安全性降低，而且虽然按照国家法律或国际法律来说该监控技术是合法的，但它们通常被滥用于对某些组织的数字化间谍活动中。这些滥用对网络安全造成严重风险，而这也是谷歌和TAG继续对商用监控软件公司采取相关措施并发布相关报告的原因所在。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[谷歌三星安卓摄像头应用含高危漏洞变身监控器，影响数亿设备（PoC）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247491631&idx=1&sn=2dbcff0f4622f31817c83b024eec1aee&chksm=ea94d145dde35853b554042a08b83e636227d0d6e429633240adb7506285d76049d497feca2e&scene=21#wechat_redirect)

[美国国防部和谷歌合作分析无人机监控录像](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247486615&idx=6&sn=8fdcb837cb18e792a7264b629e358014&chksm=ea973dfddde0b4eb4f4e84d044da12f950fb031b3028567b575613c06bfaeddfe23f7399074b&scene=21#wechat_redirect)

[谷歌发现隐藏3年之久的安卓监控软件Chrysaor](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485553&idx=3&sn=4383542dbecdf48b6ff651c9a2128776&chksm=ea97391bdde0b00d35608e3b8b0b1bd165cb0e8365b7aab4ed8658d61c2773f2e15f406b9898&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/google-discovers-windows-exploit-framework-used-to-deploy-spyware/

题图：Pexels License‍

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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