---
title: Linus点名AI漏洞报告！Linux安全列表已被挤爆
url: https://mp.weixin.qq.com/s/hADw9UEwBED_oGvooDT3mw
source: Doonsec's feed
date: 2026-05-18
fetch_date: 2026-05-19T06:00:18.203654
---

# Linus点名AI漏洞报告！Linux安全列表已被挤爆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xKicFZ2TIFt84DaEdgINNgOn4jEp7hXf9Jic6Bql0iaMjkwZ0ULRK0SibVelJR7bGRXZsTbribkdxkDEJicZia9ibnGDe4BPQf6yvialiciaJxvQEBWXas/0?wx_fmt=jpeg)

# Linus点名AI漏洞报告！Linux安全列表已被挤爆

原创

玄月调查小组
玄月调查小组

玄月调查小组

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Linux内核作者，**Linus** 又发邮件了。

主题很普通：**Linux 7.1-rc4**。

但邮件里最扎眼的一段，是 **AI 报告**。

Linus 说，持续涌入的 AI 报告，已经基本让 Linux 的 **安全列表几乎不可管理**。

这里不是论坛水帖，也不是社媒吐槽。这是 Linux 内核邮件列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xKicFZ2TIFtickfgNzySvXt9pII04SXhhPOyCDUDV0y5mdWQTGibuIwnFkxkviabJfacXYQRKnxehTJNwYI1VPicxVFJ6sic9LjE6aRFTfV7NPEfg/640?wx_fmt=jpeg)

问题不在于 AI 能不能找漏洞。

问题在于，一群人用相同工具，找到相同东西，然后把相同报告塞进同一个安全通道。

结果是维护者开始做大量无意义劳动。

他们要把报告转发给真正相关的人。

他们还要一遍遍回复：这个问题一周前、一个月前已经修了。

再把公开讨论链接丢回去。

Linus 直接说了。

**AI 检出的问题，从定义上讲，基本就不是秘密。**

**如果一个工具能扫出来，很可能别人也扫出来了。**

把这种报告塞进私密列表，不仅浪费所有人的时间，还会让重复更严重。

因为报告者彼此看不到对方的报告。

于是，同一个问题继续被一遍遍投递。

同一个维护者继续被一遍遍打扰。

**开源协作的效率，被 AI 制造的重复流量反向吞噬。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKicFZ2TIFt9odVHzTngMgZ5ooOjAHDYhCAokYiaho2YmNVPWjRia1OR7YKkDm5ybf3cL9mnfqVbErNkWibmpjk3t40gCKgXIBlR8ibCXu0VwZ2E/640?wx_fmt=png&from=appmsg)

但 Linus 没有说“别用 AI”。

这点很关键。

他的原话核心是：**AI 工具很好，但前提是它们真的有帮助**。

AI 工具很好，前提是它真的在帮忙。

如果它带来的只是无必要痛苦、无意义的工作，那就不是贡献。

不要只把机器结论转发出去。

不要做那种没有真正理解、随机发送报告的人。

**你要在 AI 之上增加人的价值。**

Linux 文档更新，也把报告门槛写得更高。

![](https://mmbiz.qpic.cn/mmbiz_png/xKicFZ2TIFt9HqHaoclLa4x2M7bA9hz5fHsXCgqUQVniaWEJ87yt8s7GIfp5zKialtmTdOLstTZzm6Ju0JmQmzGNf9EgWO4V27gN6xpV8T4xcI/640?wx_fmt=png&from=appmsg)

AI 辅助报告必须短，必须像人写的报告。

不要扔一篇 Markdown。

不要让维护者翻几页才找到受影响文件、版本和影响。

更关键的是，影响评估必须是**可验证事实**。

不要让 AI 编出一串理论后果。

能复现，就给复现样例。

能修，就给修复方案。

给了修复方案，还要测试，

并按内核提交流程带上 `Fixes:` 标签。

**这才叫贡献。**

AI 可以让更多人找到代码里的问题。

但如果报告质量不跟上，维护者就会被更大的噪音吞没。

AI 找到漏洞，只是第一步。

真正有价值的是验证、复现、理解和补丁。

**没有这些，AI 报告越多，维护者越累。**

*参考资料:https://lkml.org/lkml/2026/5/17/896;  https://www.mail-archive.com/linux-kernel%40vger.kernel.org/msg2627712.html*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

玄月调查小组

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/aYef9qMYLnI1oJLbNAr5LvueJmHqk3QP6T1rCyj8yXXaemcJSs1BunLaQO6icn0ZdKPFHRria6ocSZQEwunKTmZQ/0?wx_fmt=png)

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