---
title: 高危Chrome漏洞可导致攻击者执行任意代码，无需点击即可中招
url: https://mp.weixin.qq.com/s/fIKUI1cihccTAAZabrv-Pw
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:20.698138
---

# 高危Chrome漏洞可导致攻击者执行任意代码，无需点击即可中招

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3OCyplF8MXxA8m52icYmoibibRhdmM3MZAPgh2rbiaL2IqqRbGaJTs7yiaJ4saty3HSibcic96s3OibTM5z9bvDZX1pKibmdYGkA2OfoX4/0?wx_fmt=jpeg)

# 高危Chrome漏洞可导致攻击者执行任意代码，无需点击即可中招

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX2p5uZyjb8Gtdiav3H9icoxp2ExxzUO3hr4X4Miaib8icrcPib2613RQdEwFCoBErMB9PzVKhcv6EFJNsza4bbYZNu82NKBgPyePo1ZQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX12ia22uSyQbJ4C7TJGsm1QKibnTnJDsBCHAh2ib6vGXtt3C9qIGmFcqjDwviav4W3wzeA1BXTt6GRml6cicOBib6bWJxaP2NnXPPQDA/640?wx_fmt=png&from=appmsg)

Part01

Chrome 漏洞可导致代码执行

谷歌已为其Chrome浏览器发布关键安全更新，修复了多个高危漏洞，攻击者可利用这些漏洞在受影响系统上执行任意代码。由于多个漏洞影响浏览器核心组件，强烈建议用户立即更新。

最新Chrome稳定版已更新至149.0.7827.155/.156（Windows 和 macOS）及149.0.7827.155（Linux）。更新将逐步推送，预计在未来数日或数周内覆盖所有用户。本次更新包含 33 项安全修复，其中多个因可能导致远程代码执行（RCE）而被评为高危。

谷歌已限制部分漏洞的详细技术信息披露，待大多数用户完成更新后再公开。

在已修复的漏洞中，7 个高危漏洞尤为突出，主要涉及"释放后使用"（use-after-free）内存破坏漏洞。攻击者可利用这些漏洞操纵内存并在浏览器上下文中执行任意代码。

关键高危漏洞包括：

* CVE-2026-12437：WebShare 组件中的释放后使用漏洞
* CVE-2026-12438：WebView 组件实现不当
* CVE-2026-12439 与 CVE-2026-12440：数字凭证中的释放后使用漏洞
* CVE-2026-12441：文件输入中的释放后使用漏洞
* CVE-2026-12442：密码管理中的释放后使用漏洞
* CVE-2026-12443：Web 认证中的释放后使用漏洞

释放后使用漏洞会在内存被释放后仍被访问时触发，攻击者可借此破坏内存结构并控制执行流程。在实际攻击场景中，受害者仅需访问恶意网页即可触发漏洞利用，无需其他交互。

除高危漏洞外，谷歌还修复了 WebRTC、扩展程序、安全浏览、GPU 和文件系统访问等多个组件中的大量高危漏洞。

Part02

其他值得关注的漏洞

* WebRTC 中的堆缓冲区溢出（CVE-2026-12447、CVE-2026-1246）
* Chromoting 和 WebRTC 中的越界读取
* 扩展程序、媒体、下载和浏览器中的多个释放后使用漏洞
* 输入处理和扩展程序中的验证不足及策略执行问题

这些漏洞可能导致数据泄露、沙箱逃逸，或与其他漏洞结合形成更复杂的攻击链。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1ZxauOT9ibbsGdjlPs8qBAoQMLq37wTE3ibGWUM7YJvjUfvYU3b42BGAq6I7IibibVyBVQfRCc5icLw1pOObib7gAT6AtFiaZISnd2oc/640?wx_fmt=png&from=appmsg)

谷歌表示，其内部安全工具（包括 AddressSanitizer、MemorySanitizer、libFuzzer 和控制流完整性机制）在发现这些漏洞中发挥了关键作用。这些工具能主动识别内存安全问题，防止漏洞被实际利用。

Part03

防御建议

用户和企业应立即采取以下措施：

* 通过"设置 > 关于 Chrome"更新至最新版本
* 重启浏览器确保补丁生效
* 监控企业环境中过时的浏览器版本
* 实施纵深防御策略，如端点保护和浏览器隔离

鉴于存在大量高危内存破坏漏洞，延迟更新将显著增加被攻击风险。

参考来源：

Critical Chrome Vulnerabilities Allow Attackers to Execute Arbitrary Code – Update Now!

https://cybersecuritynews.com/chrome-vulnerabilities-execute-arbitrary-code/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2cVdntRnNdReFrEC9uicNrkrzxp72OgpNDz7srDyd0sPwPYZejHF5E9TqvpJWJ5qHkqqDtlREdb65n2YIfXD2jnNBFTqRI2LhM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1uQ9xLm3d4ZLoKboK1GHqPxkP2twtDHay11g4CqZnzXFyjmtib8WT7iaP1Libibnib4wCE0UreN6hUMgkYJ6NP9gD2ib8g2RNFTUAj8/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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