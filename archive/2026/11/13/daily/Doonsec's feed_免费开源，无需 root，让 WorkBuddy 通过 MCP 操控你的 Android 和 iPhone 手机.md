---
title: 免费开源，无需 root，让 WorkBuddy 通过 MCP 操控你的 Android 和 iPhone 手机
url: https://mp.weixin.qq.com/s/L9XDxFClARlRMTeDK3SyEw
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:14:03.936610
---

# 免费开源，无需 root，让 WorkBuddy 通过 MCP 操控你的 Android 和 iPhone 手机

# 免费开源，无需 root，让 WorkBuddy 通过 MCP 操控你的 Android 和 iPhone 手机

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0VE9kDxicLUiahBQFTibIM1ozkZdJEDMLjNjJP18GCg8olGUq28CmzyL2ErictQzYtpDPhDQAz6NOxr6Z7N4EjKQayGsJZQouOIFAhicdGeeaCn4/640?wx_fmt=jpeg&from=appmsg)

> 无需root、后台运行、安全审批

Pinky 是一个开源的跨平台桌面AI 应用，让WorkBuddy、千问办公、Codex 等 AI Agent 通过 Pinky 暴露的 MCP 工具操控你真实的 iPhone 或 Android 手机，无需root 权限，所有高风险动作在 Pinky 这一层被拦下来，等你批准后才执行。 Pinky 兼容 macOS、Windows、Linux操作系统。

全平台：兼容 macOS、Windows、Linux操作系统，能操作 Android 10 到 17 和 iOS 17.4 + 的 iPhone手机。

小巧原生：安装包仅 22 MB，窗口由 MyGo 在 GPU 上绘制，无需 Electron 和 webview，在 Mac 上空闲时内存约 70 MB，CPU占用 0%

任何 Agent，一键接入：可以接入WorkBuddy、千问办公、豆包工作、 Claude Code、Codex、Cursor 等智能体应用。

简单的任务，手机自己就能做：手机上的 Pinky 应用可以用你选的 AI 模型自己完成简单的任务，无需要电脑：在手机上写下任务，看着它做就行。

手机锁着也能在电脑上解锁：在 Pinky 里保存一次手机的 PIN 码，之后每次解锁用 Touch ID、Windows Hello 或密钥环密码确认。

开源免费：采用 Apache-2.0 开源协议，无需注册账号。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgfnVF4aG2iamjIU1cfH2JBf4LgMhRGPZaDrTOKOJex4rVb7PdDxBhAwRicdQe8pQYvkOib1DHVJiaUuJVNU9KKRRs0qbJAcQzkJeg/640?wx_fmt=png&from=appmsg)

技术架构

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiauXX44gLib5YEIeZQO2LicKYUhMsSYia3BA25ibbnBqE66dWA0aicCTIU5xg0fLajggMm1tiaSr24IiaAu1m0Qk9d04rNvlJiaOgYlXicI/640?wx_fmt=png&from=appmsg)

Agent 只负责动脑，网关负责把关，设备层只执行被放行的动作。

快速开始

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgnBMR3cIeJdwlreK4GDPWhDJ1JRoA6zlekxr7hlHv3hic5wlrmYATCDpIibCMCRjIXBG2cljNfQyqTKv7LNPyJlNEJ7x7k3Kofw/640?wx_fmt=png&from=appmsg)

下载安装：Mac 选 arm64 / amd64 的 .dmg（或 Homebrew）；Windows 选 setup.exe；Linux 选 .deb 或 .tar.gz。安装包 16–22 MB。

连接手机：「添加手机」按品牌给出步骤：Android 开 USB 调试并授权；iPhone 信任电脑、开开发者模式、挂载磁盘映像。每台手机都有「体检」。

接入 Agent：「设置 › 智能体」点一下「接入」，Pinky 自动写 MCP 配置并装好 SKILL.md；也可用命令手动添加，或走 HTTP 远程连接。

试一试：例如「打开短信，告诉 Sam 我要晚点到」。首次连接会问是否允许该 Agent；付款在窗口里等你点头。没有手机也可用模拟器。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUguxtO1ZvE7JbxVjlKGn3mXtyOAF3JvsV4onraOc6aVf7KkTRPYLnYibkmd5LTSiaDLNTmCr0aDEiacdCsK4ohoBSXE5z47TKOmicA/640?wx_fmt=png&from=appmsg)

安全保护机制

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUh7pJYo9dMjst38j0NZfLX0KbIYfC3xpq2Ficzrpp1HVAqS4FhpzI7fa1iclsF99KFJMRIeAzclzcSw92EwAuzOQSjZt2eSmjaCA/640?wx_fmt=png&from=appmsg)

风险步骤由你批准：付款、交易、转账默认等你点头；发送、下单、删除、打电话、装 App、跳出 App 的链接、改设置都可设为先问，或每步都问。

支付应用屏蔽：银行、钱包、密码管理器类 App 对 Agent 隐身，画面与通知被灰块遮挡；密码框和验证码框不能输入。需要用时按「本次任务」临时放行。

验证码自动打码：短信、邮件、通知里的「您的验证码为 482913」到 Agent 那里是「••••••」；价格、电话号码、日期里的数字保持原样。

随时接管：点一下投屏 Agent 就暂停，直到你交还；Android 上亲手碰手机也会暂停。Android 13+ 的 Agent 在隐藏第二屏工作，主屏仍归你。

PIN 码隔离：PIN 存在 Pinky 里，解锁时由 Touch ID / Windows Hello / 密钥环密码确认，Agent 永远看不到，也不会被写进记录。

记录只在本机存储：步骤、截图、录屏默认保留 30 天；录屏不遮验证码与被屏蔽 App，因此只有你每次明确允许，Agent 才能拿到导出的 MP4。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUhIUVLpaheKFibOZbt43tMyUJ8PEy9iaPKRIy3P1ibm8OcQd0Iwu387qU8e3w8ibOEGBsqZAf4CCTwmL4bRjzSLdB8l8slvfhzBFqE/640?wx_fmt=png&from=appmsg)

开源项目

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUh5fCWg1KulGYPEeqWCVAycDkW3NdXqt5EftZHJMtVo158xJRRBf7sLQ3KravThGquJS59BevhsCKZ7Htb1dO0lLibJFxgbFZtM/640?wx_fmt=png&from=appmsg)

Pinky 作为开源项目，真正做好了 MCP 暴露 、真机操控、安全网关这三件事，不仅能操控手机，而且把安全从 Agent 指令层挪到了基础设施层，靠网关硬隔离，而不是靠提示词；遇到规则识别出的付款、交易、转账等动作，请求会暂停，等用户批准后再执行。Agent 应用永远只能看到它该看到的那部分，验证码掩码、银行支付类应用隐身，让用户放心使用。

Github 项目：DIYgod/pinky

---

点个关注 **🌟，精彩不迷路 ❤️**

**往期推荐**

☞[小赚3万元！全靠这套开源AIoT 企业物联网平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946282&idx=1&sn=ad676c8d5c0785c5915e5c96ba318d82&scene=21#wechat_redirect)

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[5万元斩杀线！ 一网统飞无人机AI巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5bad8c53ff1b7514a5e1146255&scene=21#wechat_redirect)

☞[上班摸鱼， 树莓派DIY智能 AI 视频算法监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

☞[一站式AIoT视频聚合平台，适配国标28181和国密35114协议](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946211&idx=1&sn=0072cf454ac83d98adb64c5767e58901&scene=21#wechat_redirect)

☞[“空中奇兵”无人机多光谱罂粟巡查平台，识别出苗期、花期、果期](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946024&idx=1&sn=6b7d30937351bcce27a0d930c5727726&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请及时告知，我们将尽快处理。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

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