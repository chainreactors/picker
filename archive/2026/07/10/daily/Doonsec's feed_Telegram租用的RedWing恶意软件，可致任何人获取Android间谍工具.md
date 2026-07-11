---
title: Telegram租用的RedWing恶意软件，可致任何人获取Android间谍工具
url: https://mp.weixin.qq.com/s/tGWTZih5IYM5uutcfb9HRQ
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:42.307313
---

# Telegram租用的RedWing恶意软件，可致任何人获取Android间谍工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX08T6eo1vicU2b7Kkl5aBu2dtY2kIJyhD86xFvffpVoSfQmuYwtMoJWy8PqbiahVobMwDtf2YAibVQRFibHmTPgVcicRCh8X6EVaTVQ/0?wx_fmt=jpeg)

# Telegram租用的RedWing恶意软件，可致任何人获取Android间谍工具

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1s6c1mFdHJEXLYrDKsgMx3w0YAgxPSG6icxDOiaSiadsJkOsMNKqia6yG1jo3GF49jTtbMEuhk6J2ZHqb4RyEBjIaNBIaHHgFzUUo/640?wx_fmt=gif)

![RedWing恶意软件示意图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3YlwKbKfgibb5ZWnGH4o3ewjwTOXNIUAagBTIo1AGJ6Jo5JLoHVVQWVSQSpf6HoegtcdLELLcicH3icGk27hzMr2nalpHFqY6UPU/640?wx_fmt=jpeg)

Part01

月费低于咖啡订阅的

Android银行木马

Zimperium的zLabs团队发现名为RedWing的Android间谍软件通过Telegram以订阅制形式出售，该恶意软件与俄罗斯威胁组织存在关联，其技术根源可追溯至Oblivion恶意软件家族。该服务提供完整文档、教学视频、推荐奖励计划，以及按需生成定制恶意应用的机器人系统，使用者无需具备任何恶意代码编写能力。

Zimperium在报告中指出："RedWing绝非普通网络售卖的简易恶意软件，而是配备卖家文档、视频教程和机器人订阅模式的成熟商业级MaaS（恶意软件即服务）产品，极大降低了攻击新手的入门门槛。作为佐证，其APK定制化/混淆/生成功能均可通过Telegram全流程实现。"

![RedWing服务界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2Sb3vI6UlQrLUyOuq8b25PiaKicUTWnWWymDcPl3Rew7ysYv85grxmmpSricyA9Iic4iaAgBZvKQkH3Xtqb97hEWkVibUHRhHL4v4n0/640?wx_fmt=jpeg)

Part02

多阶段渗透与权限劫持机制

感染始于钓鱼链接引导至伪造应用商店页面。其安装包生成器可完美仿冒Google Play、三星Galaxy Store或华为AppGallery，包括虚假评分、评论及下载量数据。

报告进一步披露："其C2控制面板配备精密的'引导构造器'。在'窃密模块'配置中，攻击者可部署具有欺骗性的'WebView+卡片'界面。该机制在后台加载看似正常的网页建立可信度，同时从屏幕底部依次叠加定制化的权限诱导卡片。通过精准设计的社会工程话术，恶意软件胁迫用户授予三项关键系统权限：禁用电池优化（确保后台持续运行）、设置应用为默认短信处理器（用于拦截双因素认证码）以及获取通知读取权限。"

安装后，恶意软件会分步引导受害者完成"常规设置"，依次获取上述权限。一旦得逞，RedWing将获得深度系统控制权：覆盖银行及加密货币应用界面的虚假登录窗口窃取凭证、拦截短信获取一次性验证码，并利用Android无障碍服务实时捕获屏幕上显示的PIN码、银行卡号及CVV安全码。

Part03

隐蔽通信劫持与远程监控

该恶意代码还会静默启用运营商隐藏代码\_21\_激活来电转移，将所有呼入电话重定向至攻击者控制的号码，此举可同时规避电话双因素认证和银行反欺诈呼叫提醒。

研究人员发现其监控能力更为惊人：RedWing可通过攻击者服务器发送指令远程激活受害者设备的摄像头和麦克风。报告详细说明："恶意软件执行特定命令实现远程监控，例如指令调用设备摄像头拍摄照片，指令则通过MediaRecorder API录制环境音频。所有录音参数（包括持续时间）均由攻击者远程配置。"

攻击者还能通过VNC实现实时屏幕监控、获取键盘记录、访问设备全部文件、通讯录、通话记录及定位信息。

Part04

模块化架构与动态目标更新

技术架构分析揭示了RedWing的运作特点：其通过无障碍服务监控的应用程序列表被直接编译进每个定制APK，意味着每次买家指定目标时都会在服务端生成新安装包；而界面覆盖攻击目标则可通过控制面板随时更新，无需重新分发应用。

Zimperium已识别出82个横跨多行业的攻击目标，其中俄罗斯金融机构占多数。某样本使用伪造的RuStore页面，但攻击者仪表盘可随时调整目标列表。

Part05

防御建议与僵尸网络功能

RedWing无需利用任何Android漏洞（CVE编号），其完全依赖用户从非官方渠道安装应用并批准权限请求。关键防御措施包括：不安装短信或即时通讯应用发送的链接应用；拒绝授予无障碍服务或默认短信权限给无明确需求的应用；警惕安装后隐藏图标的应用。企业设备可集中禁用侧载功能并自动标记可疑权限请求。

值得注意的是，RedWing还能将受感染Android设备组成僵尸网络发动协同DDoS攻击。攻击者通过控制面板可同时操纵多台被控手机对目标网站或服务器发起流量洪泛攻击，在间谍窃密功能外又添破坏性能力。

![RedWing僵尸网络功能](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1VxvAIeN3Lkrib5OBAWvoT56V8gbC5ZQHt7IbsuPQXv1DpRj4icHOP6Sfo0zb4bTSKtiaKGm1wJy9gZZYRF8pTiaAbI3TfwB3ice7w/640?wx_fmt=jpeg)

Part06

MaaS模式带来的新型威胁

由于攻击者可通过控制面板随时更换应用皮肤和攻击目标，仅凭应用名称难以识别，行为特征才是关键指标。

报告总结道："RedWing等恶意软件即服务（MaaS）的迅速崛起，表明攻击者能轻易武器化合法Android组件实现完全设备控制。与传统银行木马仅依赖界面覆盖不同，RedWing整合了定制安装包、实时屏幕流传输、滥用短信处理器角色和无障碍服务等功能，实现数据窃取和实时应用仿冒。这种社会工程与来电劫持的结合，使其在BYOD和消费级环境中尤为危险——这些环境通常默认应用商店的可信度。"

参考来源：

Telegram-Hosted RedWing Malware Lets Anyone Rent Android Spyware Tools

https://securityaffairs.com/194942/malware/telegram-hosted-redwing-malware-lets-anyone-rent-android-spyware-tools.html

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX24B8SGpjtPNurWcSlpApNEFvAvemslibiaNDIP9r5rUpOOr7bldmoTgsRqBAho97xVeKrGPEh3CJHn55QqFCOKZOzMn3CAnUyC0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651341548&idx=1&sn=bb9edaa490d92c0258ff47c5dd29faf4&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX01JzsmUwE4vIMgNU0wJMU6KQJl9dPmQiasQPhk4XicPz5E9aUGGrN6LLALlxxjew7Vks5QabJJwtkIffw9c4OwbItR1tY3qVRbc/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3y34M5GAibwcktqAsbKu2ibamWeibVrPpa709ynHMljYolGiaw7cPCyW5sCvL9sRS4lJVTOahlPKkMD7YuL5JjW6tibNyibD9QErkrc/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1mP5l1EuNKhxEBfV7Pib0NBoPy1gRRFbZoBrlic0HJgw38b2H2OWOIA5oMMDrrl6KqsiaWgnrKF4a6BoqOKcgRmydooUhNqtQDOE/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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