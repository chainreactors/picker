---
title: Anthropic意外泄露Claude Code源代码
url: https://mp.weixin.qq.com/s/8kA_AXYCDQaN91xfzSiMDQ
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:34:31.664163
---

# Anthropic意外泄露Claude Code源代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/DYqn7TU9icq2Zz4eJDbwUq5PdhLpHkQEKDyhoVA6jpz7hgZyiaAkjkYdNNjDrE0zLOacjKW62EY9Nm7mPbAbickDohooLt8RxZW9ZRqbeHVUp4/0?wx_fmt=jpeg)

# Anthropic意外泄露Claude Code源代码

鹏鹏同学
鹏鹏同学

黑猫安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/DYqn7TU9icq2yAUb8g8JxpHYWr0V1gVADLYgf8cJ5iaoZsuhia3fDcbNHBmbUnBHicElPXvwCtLOIVJO9luKe9wslF321SV6M8O5Ok10jiaWwQK4/640?wx_fmt=png&from=appmsg)

**Anthropic在npm公开发布版本中包含大型调试文件后，意外泄露了其Claude Code工具的源代码。该文件暴露了超过50万行代码，在被标记后很快被开发者发现、分享和分析。**

Anthropic发言人告诉VentureBeat：今天早些时候，Claude Code发布版本包含了一些内部源代码。没有涉及或暴露敏感客户数据或凭据。这是由人为错误导致的发布打包问题，不是安全漏洞。我们正在推出措施防止这种情况再次发生。

泄露的Claude Code展示了Anthropic如何在长时间交互中保持其AI专注，避免混淆或错误。它使用分层内存系统，其中小索引跟踪位置而不是存储完整数据，实际信息仅在需要时检索。失败的更新不影响AI的内存，保持其准确性。本质上，模型将其内存视为指南，在采取行动之前根据真实数据检查细节。

泄露还揭示了"KAIROS"——古希腊"在正确时机"的概念——在源代码中被提及超过150次的功能标志。KAIROS代表用户体验的根本转变：自主守护进程模式。当前AI工具主要是被动的，而KAIROS允许Claude Code作为始终在线的后台代理运行。它处理后台会话并采用称为autoDream的进程。在此模式下，代理在用户空闲时执行"内存整合"。

泄露揭示了Anthropic的内部AI路线图，包括Capybara（Claude 4.6）、Fennec（Opus 4.6）和未发布的Numbat。Claude Code泄露不仅损害了Anthropic的知识产权，还暴露了Anthropic的内部架构，为攻击者提供了绕过安全提示的路线图。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

黑猫安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/DYqn7TU9icq0Cqr2KYoUfur4KLeiclhRqlnu9g0qWMQJVEPqRicnicZzBdbaER3Jd1tI4NootkSwZiaruC4ATIbibbuM0riaianEiaRt0dVicRsfUhmI8/0?wx_fmt=png)

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