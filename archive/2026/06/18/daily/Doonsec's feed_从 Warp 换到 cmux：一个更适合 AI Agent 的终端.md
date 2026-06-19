---
title: 从 Warp 换到 cmux：一个更适合 AI Agent 的终端
url: https://mp.weixin.qq.com/s/7tnPJez7t-CM5zmR-91O6A
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:06:55.099528
---

# 从 Warp 换到 cmux：一个更适合 AI Agent 的终端

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5naxUv4nJVKxxIFRbiat1jTyDTSBZ6HYYjqMBUerk76R9C1skHHuPDHI2iaicJ2Sy8p404icVelfkniaHs3aLlFIbYxf9h8QOoLSQPsQYaQa3V0A/0?wx_fmt=jpeg)

# 从 Warp 换到 cmux：一个更适合 AI Agent 的终端

crossoverJie

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 背景

最近将终端从 Warp 切换到了 cmux，用了一段时间后，现在已经基本上满足我的所有需求，所以才有这篇安利的文章。

开始之前先回顾下自己的终端使用历史。刚开始工作那时候使用的是 Windows，用得最多的终端就是 xshell，后面切换到 macOS 之后自然就切换到了 mac 上用的最多的 iTerm2。

![](https://mmbiz.qpic.cn/mmbiz_png/5naxUv4nJVL1bINicwBLubrO8AWEkyQn1TNxNibXgMcibiasvrUbX02ia85O335Oy36mcyrRw4DgRgYDnl1pfg9QJG2icF1lzsy88sScKYsMT5AwY/640?wx_fmt=png&from=appmsg)

iTerm2 一直是我的主力终端，用了很多年，直到前些年 Warp 的出现。Warp 提供了 block 块、现代的文本编辑器（支持鼠标移动光标），用上之后就离不开它了。

但是随着这些年的迭代，Warp 功能越做越臃肿，加入了一些我完全不需要的 AI 功能。

加上近期频繁使用 Claude Code、Codex、OpenCode 这些 AI Agent，对终端的依赖性变得更高了。

原本我一开始是想自己做一个的——我其实就是想要一个简化版的 Warp，需要包含以下功能：

* Block 功能，特别是查看大量日志的时候非常有用
* 现代的文本编辑器，而不是每次都用方向键来移动光标
* AI Agent 的管理功能

+ Agent 完成时的通知、当前状态的查看

* 终端状态栏：显示当前路径、git status、git diff 等信息

我大概做了一周多的时间，达到了一个基本可用的版本，但很多细节都没做好。

受限于当时选择的技术栈 Tauri + Rust，一些体验上确实比不上 Swift 的原生开发效果。

于是就继续用 Warp，直到后面在社媒上看到了 cmux。

# cmux

![](https://mmbiz.qpic.cn/mmbiz_png/5naxUv4nJVLnoK3z9g5DtDvriblcOibxHf9w1eGeicib058gggmibWHzldA4q91aribaEIdgicwBbiaibMibr0X0jdrA7bsGqLmPkNGGmbjqJsy0kicnVM/640?wx_fmt=png&from=appmsg)

这是我目前使用 cmux 的截图。现在使用终端其实 90% 的时间都在和 Agent 打交道。

我会同时开启 N 个 Agent 来干活，其中又会将 Agent 按照业务进行分组，这时就得提到 cmux 的工作区和分屏功能了。

cmux 把结构分成 **Window → Workspace → Pane → Surface → Panel**。也就是说，一个工作区里可以有多个分屏，每个 Pane 里还能有多个 Surface，非常适合把主 Claude Code、测试命令、日志、浏览器、子 Agent 放在同一个 context 里。

而且 cmux 还集成了 Agent 通知——普通终端通知往往只告诉你「有进程需要输入」，但不知道是哪个 Agent、哪个项目、哪个分屏。cmux 的 Pane 会出现蓝色通知环，侧边栏 Tab 会亮起，还支持通知面板和 macOS 桌面通知。

> 通知的问题之前我写过一个 SKILLS[1] 来解决，现在终端能原生通知就更好用了。

# 总结

![](https://mmbiz.qpic.cn/mmbiz_png/5naxUv4nJVLVxcw6EGpwElX3DgSbN1Xv7nGLeBX2lo8zgAHKKtDD60lODDgHArZlLnSCuicicvvypycNDHqKXPB5B0UibLpb4U0RN5icgvxmLOY/640?wx_fmt=png&from=appmsg)

如果你是 macOS 用户，还在使用 Warp 甚至是 iTerm2、自带终端的 Coding Agent 重度用户，非常推荐你来试试 cmux[2]，一定会有新的发现。

### 参考资料

[1]

SKILLS: *https://github.com/crossoverJie/skills/blob/main/skills/agent-notifier/SKILL.md*

[2]

cmux: *https://github.com/manaflow-ai/cmux*

往期推荐

[我做了一个 AI 版的 StarRocks 升级风险扫描工具，直接帮我定位到一个风险](https://mp.weixin.qq.com/s?__biz=MzIyMzgyODkxMQ==&mid=2247488952&idx=1&sn=45187814f74f0432df8a01976e4bb16d&scene=21#wechat_redirect)

[Claude Fable 5：Anthropic 将 Mythos 级能力首次推向大众，编码和知识工作全面领先](https://mp.weixin.qq.com/s?__biz=MzIyMzgyODkxMQ==&mid=2247488929&idx=1&sn=1075f8f9d9d005415d9ac7fdeaf935f4&scene=21#wechat_redirect)

[[送码] 用 AI Coding 做了一个 App，谈谈 AI Coding 的真实体验](https://mp.weixin.qq.com/s?__biz=MzIyMzgyODkxMQ==&mid=2247488901&idx=1&sn=16e71b0e0672d186ffb5409c4da1633f&scene=21#wechat_redirect)

[手搓一个 Agent 驱动的项目 Wiki 生成方案](https://mp.weixin.qq.com/s?__biz=MzIyMzgyODkxMQ==&mid=2247488865&idx=1&sn=3d3ecd02cd7537f3a1acc2fcd2faf6b6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/5naxUv4nJVILKqZQcjUr03zJnfF6maicnY1Kt89IXTIZ73qicSY9LnFIbe4Sb73azFCnKDcYESGWpicicorl15b4fM5a8LhxI0VDucpD0n8dcvU/640?wx_fmt=gif&from=appmsg)

**点分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/5naxUv4nJVIV3XRLhVutjBJoJV1hVGX5a5iaxYnic6TJiaHvq9xwLDVbOY2X8nDiawlwB479NEqUibVlibrwnoIWc1Y7PZ0bMzSvstOmjdo1CSEBs/640?wx_fmt=gif&from=appmsg)

**点收藏**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/5naxUv4nJVIhE7rkSuiaSAvYnZDctLp1wQiaXMK8oXIMsDm3Cnrkr3joia7aPyQ7vvdHbdznJ2hOM6SaVmVPd4330vDMAuoO4tKm78RfOZ4dbg/640?wx_fmt=gif&from=appmsg)

**点点赞**

![](https://mmbiz.qpic.cn/mmbiz_gif/5naxUv4nJVJmv7d2Ky4JHscdbWbrJk83FExUSOibW1ibDibdjoIdBO42xUX2xQfjtOK34DGaDrCWcZ07UysYM15BnfgfSWcArNjyGiaEDhL1MAA/640?wx_fmt=gif&from=appmsg)

**点在看**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/csD7FygBVl28UebicaHzCPGibictqgwd1db5v051QqiaaXwkyqy5mF4f7lk5guVk1OrupJCF81qWMFCrO5N1J9nVag/0?wx_fmt=png)

crossoverJie

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/csD7FygBVl28UebicaHzCPGibictqgwd1db5v051QqiaaXwkyqy5mF4f7lk5guVk1OrupJCF81qWMFCrO5N1J9nVag/0?wx_fmt=png)

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