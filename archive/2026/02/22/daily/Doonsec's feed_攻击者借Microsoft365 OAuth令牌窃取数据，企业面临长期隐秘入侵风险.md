---
title: 攻击者借Microsoft365 OAuth令牌窃取数据，企业面临长期隐秘入侵风险
url: https://mp.weixin.qq.com/s/PA3fwVJQTKnUE8g533XnQg
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:16:38.006911
---

# 攻击者借Microsoft365 OAuth令牌窃取数据，企业面临长期隐秘入侵风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX21WvydXb75KHaGHuFica8Kicr5IhybeJnEFwpxdGIveBRlD0ic8aGIuk4Hjh5F0OlnAibMpcWibqdlI7z4Gr1xsGNx02lu8EDvxsib8/0?wx_fmt=jpeg)

# 攻击者借Microsoft365 OAuth令牌窃取数据，企业面临长期隐秘入侵风险

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2AzoOX4EFGGdV5ficuhvjT4VmEZ5TJIpIJXStbxw77T60QfaibHdcRJh0dwUyrvFEbRiaUM9dgtV7Ciaibw2GpBycwHYUeozXHB5BY/640?wx_fmt=jpeg&from=appmsg)

##

一项针对Microsoft365用户的钓鱼攻击活动正在持续进行，攻击者通过滥用OAuth令牌获取企业数据的长期访问权限。该活动主要针对北美地区的商业用户，旨在入侵Outlook、Teams和OneDrive账户，且无需直接窃取密码。

与传统攻击方式不同，攻击者并非通过伪造登录页面实施攻击，而是诱骗受害者在微软官方设备登录门户完成真实登录流程，这使得用户和基础安全工具都更难识别攻击行为。一旦得手，攻击者就能悄无声息地读取、发送和管理电子邮件及文件，对内部通信和敏感文档构成严重威胁。

##

**Part01**

## ****攻击手法分析****

KnowBe4威胁实验室研究人员于2025年底发现该攻击活动，追踪到攻击者将逼真的钓鱼邮件与OAuth 2.0设备授权许可流程相结合，从而绕过强密码和多因素认证（MFA）。分析显示，攻击者高度依赖具有说服力的社会工程手段，使用付款确认、奖金相关文件和语音邮件提醒等主题，诱使忙碌的专业人士快速采取行动。

由于受害者是在合法的微软页面上完成登录，许多人误以为该过程是安全的，但实际上他们最终授予了攻击者控制的恶意应用程序访问权限。

**Part02**

## ****攻击流程详解****

当用户在微软设备登录页面输入攻击者提供的设备代码后，微软身份平台会颁发与该受害者账户绑定的有效OAuth访问令牌和刷新令牌，攻击者随即实时捕获这些令牌。这些令牌使入侵者能够维持持久访问权限，且通常不会在传统的凭据监控中触发明显警报。受影响组织可能会发现未经授权的邮箱操作、文件访问和潜在的数据外泄，所有这些行为都看似来自合法用户上下文。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX38jianAXUB5ePWZwicLDAm2AiaVzY4hownPW0nGicr1gyz6yFDGAW5WbB1Zp8UuRrTvtX1NHVSBsInOsombtUiahr5ABaialn8fcUAI/640?wx_fmt=jpeg&from=appmsg)

该攻击流程完整展示了从初始钓鱼诱饵到设备代码滥用，再到令牌窃取和长期账户访问的完整攻击链。该活动的核心在于滥用OAuth设备授权许可流程——该功能本是为输入选项有限的设备设计，但在此被攻击者重新利用以规避常规防御措施。

**Part03**

## ****技术实现细节****

攻击者首先在Microsoft365中注册一个OAuth应用程序，并生成与该应用映射的唯一设备代码。随后将该代码嵌入精心设计的钓鱼邮件中，引导受害者访问攻击者控制的登录页面，诱使用户输入电子邮件并遵循"安全认证"步骤。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2drHWzXpU5L9U3j17Th2MiaLdnOtqpDI3Wo8G8bGnRw5JdLfqvwczN219pibmzAz07XAL6f1M3ciateicE6ltg6HC6fOne14h8PRg/640?wx_fmt=jpeg&from=appmsg)

当受害者按照指示访问合法的microsoft.com/devicelogin门户并提交提供的代码后，攻击者会持续轮询令牌端点，一旦微软批准会话，便立即劫持颁发的OAuth访问令牌和刷新令牌。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2iabfCGf21TBX6OKh286Bj3Y3xqbm0LJD5QicTaPjZHofGTyhq4HDfsrGKMvgZr0SBaicl90j7umSTFOPjNia6jJkZ4W2RXsjvyR0/640?wx_fmt=png&from=appmsg)

**Part04**

## ****防御建议****

为降低风险，安全团队应采取以下措施：

* 阻断与该活动相关的已知恶意域名和云存储URL
* 在电子邮件日志中搜索已识别的发件人地址和主题模式
* 紧急审核最近同意的OAuth应用程序中的可疑条目

在业务允许的情况下，管理员应考虑完全禁用设备代码流程，或通过条件访问策略严格限制其使用，同时审查Azure AD登录日志中异常的设备代码活动和地理位置异常。结合针对紧急付款通知、意外文档共享和语音邮件警报的持续用户安全意识教育，这些措施可帮助组织在造成更深层次损害之前检测并遏制类似的OAuth令牌窃取企图。

**参考来源：**

Ongoing Campaign Targets Microsoft 365 to Steal OAuth Tokens and Gain Persistent Access

https://cybersecuritynews.com/ongoing-campaign-targets-microsoft-365/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

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