---
title: AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证
url: https://mp.weixin.qq.com/s/PEKUgx_d-u7pvhYmPX0zGg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:21:54.645414
---

# AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fHEm7hZn9HInIiclyZzgfXFHCFhXXUrMGMDKyqoVslIlaUU8PVdWntmYKNia8C0ggZdazgQyfw8cwTYVVNIRRyz74PNUibib5L1le7eAp2Yibs4I/0?wx_fmt=jpeg)

# AiFrame攻击活动：30款恶意Chrome扩展程序伪装成AI助手窃取账号凭证

胡金鱼
胡金鱼

嘶吼专业版

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

超30万的用户安装了共计30 款的恶意 Chrome 浏览器扩展程序，它们伪装成AI助手形式以窃取用户账号凭证、邮件内容与浏览信息。其中部分扩展目前仍上架于 Chrome 应用商店，另有部分扩展安装量相对较小。

研究人员发现这一恶意扩展攻击活动后将其命名为 AiFrame。经分析，所有涉事扩展均归属同一攻击团伙控制，为同一域名 tapnetic.pro 下的攻击基础设施通信。

据研究人员介绍，AiFrame 活动中最流行的扩展为 Gemini AI Sidebar（ID：fppbiomdkfbhgjjdmojlogeceejinadg），用户量达 8 万，目前已从 Chrome 应用商店下架。

但仍有多款用户量达数千的同类恶意扩展继续留在谷歌 Chrome 扩展商店中。值得注意的是，这些扩展名称可能不同，但核心标识一致，包括：

**·**AI Sidebar（gghdfkafnhfpaooiolhncejnlgglhkhe）——7 万用户

**·**AI Assistant（nlhpidbjmmffhoogcennoiopekbiglbp）——6 万用户

**·**ChatGPT Translate（acaeafediijmccnjlokgcdiojiljfpbe）——3 万用户

**·**AI GPT（kblengdlefjpjkekanpoidgoghdngdgl）——2 万用户

**·**ChatGPT（llojfncgbabajmdglnkbhmiebiinohek）——2 万用户

**·**AI Sidebar（djhjckkfgancelbmgcamjimgphaphjdl）——1 万用户

**·**Google Gemini（fdlagfnfaheppaigholhoojabfaapnhb）——1 万用户

研究人员指出，30 款扩展共用相同的内部结构、JavaScript 逻辑、权限配置与后端基础设施。

这些恶意浏览器插件并未在本地实现任何 AI 功能，而是通过全屏 iframe 加载远程域名内容，以此对外提供所谓“AI 服务”。

这种模式本身就存在极高风险：攻击者可随时修改扩展逻辑，无需推送更新即可改变行为（类似微软 Office 插件机制），从而绕过应用商店的重新审核。

在后台，这些扩展利用 Mozilla 的 Readability 库，从用户访问的网页中提取内容，包括敏感的登录认证页面。其中15 款扩展专门针对 Gmail 数据，通过在 mail.google.com 页面加载阶段（document\_start）运行专用脚本并注入界面元素，实现窃取行为。

该脚本直接从 DOM 读取可见邮件内容，并通过 .textContent 持续提取邮件会话文本。研究人员强调，even 邮件草稿也可被完整窃取。

当用户触发 AI 辅助回复、摘要生成等 Gmail 相关功能时，提取到的邮件内容会传入扩展逻辑，并上传至攻击者控制的第三方后端服务器。这将导致邮件正文及相关上下文数据被传出设备，脱离 Gmail 安全边界，上传至远程服务器。

这些扩展还内置远程触发的语音识别与转录功能，通过 Web Speech API 实现录音并回传结果。根据获取的权限不同，扩展甚至可以窃取受害者所处环境的对话内容。

研究人员为此发出安全建议：建议用户及时进行自查，如确认设备已被感染，应立即重置所有账号密码。

文章来源自：https://www.bleepingcomputer.com/news/security/fake-ai-chrome-extensions-with-300k-users-steal-credentials-emails/

![](https://mmbiz.qpic.cn/mmbiz_png/fHEm7hZn9HKJImVGrvOZCy0ClmnFgKLNTeZiaoDvKiclzIShCgXflYEcdToIAOGPty9WM1VbTab8MQE0eBPOjyKjFVY7baricczk0ZuTTwE70g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fHEm7hZn9HLUTaRgKJjUymGs3vSS4TXLXPEYHcaNSsxeDqU6Hmc6VBZS82MSFhiccWzjc471o2XTyxdnJdPSibTMZCjM5w35yN2gUa3kyr7gE/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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