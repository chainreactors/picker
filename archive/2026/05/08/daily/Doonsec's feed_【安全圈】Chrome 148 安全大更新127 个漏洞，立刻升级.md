---
title: 【安全圈】Chrome 148 安全大更新127 个漏洞，立刻升级
url: https://mp.weixin.qq.com/s/I5Fgf3Jy_vlp864XImL9tA
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:05:33.942812
---

# 【安全圈】Chrome 148 安全大更新127 个漏洞，立刻升级

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyH6IN2pSzcceEoBZZzK12MXcJDXrVIEeqTNZxiaF4ZHDJNW39nqIYqTpnfeY0hWUV9ibtj2dzSaYZvKQ0eboqibclA6keEtUztjFE/0?wx_fmt=jpeg)

# 【安全圈】Chrome 148 安全大更新127 个漏洞，立刻升级

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyHfYp6nVriaZU2NqRywibZjjgPzkLAxgriaMYwqxsl6qTaq49nJAbPbiceCt5NaDqWBXKzRFq9Dl29fcdx8sSZPI7icWtG3nLCKdrBM/640?wx_fmt=webp&from=appmsg)

谷歌已正式将 Chrome 148 版本推广至 Windows、Mac 和 Linux 的稳定版渠道，Linux 版本号为 148.0.7778.96，Windows 和 Mac 版本号为 148.0.7778.96/97。这是该浏览器近期历史上安全级别最高的版本之一，一次更新就包含了 127 项安全修复。

在已解决的 127 个漏洞中，有 3 个被评为“严重”，24 个被评为“高”，还有相当一部分属于“中”和“低”类别。

谷歌向负责任地披露漏洞的外部研究人员发放了超过 10 万美元的漏洞赏金，其中一名研究人员因报告V8 中一个高危越界读写漏洞而获得了 5.5 万美元的奖励。

## **Chrome 浏览器严重漏洞已修复**

三个被评为“严重”级别的漏洞风险最高。CVE-2026-7896 是 Blink 渲染引擎中的一个整数溢出漏洞，由外部研究人员于 3 月 18 日报告，并获得了 43,000 美元的赏金。

CVE-2026-7897 和 CVE-2026-7898 都是释放后使用漏洞，一个在移动组件中，一个在 Chrome 远程桌面（Chrome Remote Desktop）中，这两个漏洞分别于 4 月 18 日和 4 月 20 日由 Google 内部报告。

释放后使用漏洞尤其危险，因为它们可能允许攻击者通过操纵已释放的内存区域来执行任意代码。

高危漏洞涵盖了广泛的攻击面。CVE-2026-7899 是Chrome V8 JavaScript 引擎中的一个越界读写漏洞，由 Project WhatForLunch (@pjwhatforlunch) 报告，并获得了此次更新中最高的个人奖励 55,000 美元。

CVE-2026-7900 和 CVE-2026-7901 是ANGLE（图形抽象层）中的堆缓冲区溢出和释放后使用漏洞，每个漏洞的奖励金额为 16,000 美元。

此外，KAIST黑客实验室的JunYoung Park报告了V8中的越界内存访问漏洞CVE-2026-7902，并因此获得了8000美元的奖励。总而言之，这些V8和ANGLE漏洞对通过恶意构造的网页进行“路过式攻击”构成了重大风险。

除了顶级缺陷之外，Chrome 148 还解决了 SVG、DOM、全屏、GPU、WebRTC、Skia、密码、ServiceWorker、PresentationAPI、WebAudio 等一系列释放后使用漏洞。

中等严重性问题还包括 V8 中的对象生命周期问题 (CVE-2026-7936)、WebRTC 中的类型混淆 (CVE-2026-7988) 以及 DevTools、Extensions 和 DirectSockets 中的策略执行不足。

值得注意的是，CVE-2026-8022 是 MHTML 中一个低严重性不当实现，它可能允许远程攻击者通过精心构造的 MHTML 页面泄露跨域数据，当用户被诱骗执行特定的 UI 手势时，攻击者可以利用该漏洞。

Google 对数十位独立研究人员表示感谢，其中包括来自 KAIST 黑客实验室、腾讯安全玄武实验室、国立阳明交通大学安全与系统实验室以及 Theori 的贡献者。

根据 Chrome 的公告，检测到的漏洞是使用 AddressSanitizer、MemorySanitizer、UndefinedBehaviorSanitizer、libFuzzer 和 AFL 等自动化模糊测试和清理工具发现的，这凸显了谷歌主动安全测试基础设施的规模。

Windows、Mac 和 Linux 用户应立即更新至 Chrome 148.0.7778.96/97 以修复这些漏洞。

下一个稳定版本 Chrome 149 计划于 2026 年 6 月 2 日发布。用户可以通过“设置”→“帮助”→“关于 Google Chrome”进行更新，这将触发自动下载和安装。

***END***

阅读推荐

[【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076218&idx=1&sn=38a3aaf6dc9ce8f8a4c69044d68a8236&scene=21#wechat_redirect)

[【安全圈】供水设施遭入侵，Claude AI 助力黑客锁定 OT 资产](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076218&idx=2&sn=1777c0b96b34a5c5c86af01090010f49&scene=21#wechat_redirect)

[【安全圈】基于 Mirai 的 xlabs\_v1 僵尸网络利用 ADB 劫持物联网设备发动 DDoS 攻击](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076218&idx=3&sn=0fb288079b71e898e51fe38b9fec7073&scene=21#wechat_redirect)

[【安全圈】安卓高危0Day漏洞可远程获取Shell访问权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652076197&idx=1&sn=f04ddcae84cf9ff13b2696de01ec65eb&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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