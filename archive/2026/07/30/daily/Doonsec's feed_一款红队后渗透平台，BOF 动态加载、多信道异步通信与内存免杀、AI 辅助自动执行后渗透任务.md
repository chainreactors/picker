---
title: 一款红队后渗透平台，BOF 动态加载、多信道异步通信与内存免杀、AI 辅助自动执行后渗透任务
url: https://mp.weixin.qq.com/s/jSrhvl1NmPENlUMlsQSH6Q
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:29:42.796513
---

# 一款红队后渗透平台，BOF 动态加载、多信道异步通信与内存免杀、AI 辅助自动执行后渗透任务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMKnFpz6fou774YbZwGQWTqBCrReibdyZkQE9xAl96kvAt84BvLBwx00T1zUnEvmREiatPnmiamzdXze1wwRF6rTTdOFgSlKRKA14U/0?wx_fmt=jpeg)

# 一款红队后渗透平台，BOF 动态加载、多信道异步通信与内存免杀、AI 辅助自动执行后渗透任务

1y0n
1y0n

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍

Oktos 是一款红队后渗透平台，作为 XRED.TEAM 的一部分。它采用了模块化设计，支持 BOF 动态加载、多信道异步通信与内存免杀，内置的 AI 助手可辅助编排或自动执行后渗透任务，为红队提供隐蔽、高效、智能的作战能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMLN1x7Dl7bwCDxYhRboIic66LnvV4YbcEYKalgafWuxYjialz5cMZIaeAb1FghPjtHB6XiaZzhPjSh3EzZosicNmmZM4yZZcPVkaMI/640?wx_fmt=webp&from=appmsg)

你可以在 release 页面 获取下载链接，然后在终端/命令提示符中启动 teamserver 即可，默认管理端口是 8080，可通过 --port 参数指定。

如果你发现了 bug （会很常见），欢迎提交 issue（需要写明具体的复现步骤），我将会在未来一段时间内将更多精力投入到 bug 修复和新版本发布中，欢迎随时回来查看。当然，如果有功能或用户体验上的优化建议，也欢迎提交，根据时间酌情修改。

这个项目为经过授权的红队行动设计，不适用于黑灰，拒绝为黑灰提供任何帮助，所有为黑灰、钓鱼、捆绑、定制等提供便利的 issue 都会被忽略，故也无法开源。

因为集成了 mimikatz 等工具，所以 teamserver 本身会被杀软报毒，需将 teamserver 本体添加到杀软白名单。

为避免被捆绑木马，项目内置了简单的防篡改机制，但无法确保100%安全，所以运行前请检查程序的 SHA256 与发布页面是否一致。

第一次启动时会生成配置文件和默认密码，登录管理页面在“用户管理”处修改密码。运行过程中的配置文件未做加密，注意保护。

使用前建议先在“配置管理”中启用 AI ，以解锁全部功能。已测 deepseek-v4-flash，其他的可自测。后期会增加对 MCP 的支持。

## 工具获取

点击关注下方名片进入公众号

回复关键字【260730】获取下载链接

## 往期精彩

[VulnFlanker 漏洞监测平台 | WatchVuln 高价值漏洞采集与推送

2026-07-29

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMJtcIbUtgluQ445b0FGhn8B7cNlVE1hqsibJSY1eHgcicahAIxr9vTx0TmllGswgmfSGxia45BQwicPmHueoHLiavOLcOZIWYwySvyA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497296&idx=1&sn=c2ca94e81d744b899939cffcb4b125df&scene=21#wechat_redirect)[穷尽一切手段，扒光 CDN 的底裤，找到真实 IP。

2026-07-28

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMI0BwMSbuqyibcNWictWHL1u7PnjTcUju6MvAr3Gt7uP7UKSgib77iccSnUuz59icnXxFt1sxh4BpwKQEcXMD3dow1thcrjBhhxMjXE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497289&idx=1&sn=d50f40bd94b4dbfd1bd56db63bde33f4&scene=21#wechat_redirect)[存储桶遍历漏洞利用工具V2.0  | 存储桶内容搜索、文件预览、文件下载和媒体解码

2026-07-27

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMKf7afhLARLXAic7vqKbEwPIlFn4TtfUQ5JOgeQGQYpiaPIgGsKMT83JyWGWhxxP5YEPDcJnKnRvLgUYp5MmyXh9Q76iaHq2DYaEE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497278&idx=1&sn=3e8169537e95d31ae22ecf0829c2e71c&scene=21#wechat_redirect)[红队多协议跳板代理管理平台 | 支持策略调度、规则分流、健康检查、REST API / WebSocket 自动化

2026-07-24

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLImBfgx6mAy5y7z8NiaKgVr5ibKYflwy2VCS5RFKrtr7mic1awbxDUajO9OmfQN9OFJMgGmQMzLOPwOln4GOSian6Rk3VfdbE05Is/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497272&idx=1&sn=9970aa4122cd9aaa21705b980d4b8581&scene=21#wechat_redirect)[面向 AI 代码审计的本地客观源码读取覆盖率工具，同时支持 Codex、Claude Code 和 OpenCode

2026-07-23

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKZEdJU5LIrzkRrU2FqK9MagZ88tTGnfGfNZlCCicmuETYjcaffgFL0sUlIx5h6yLecwfibewdyxxk0Wc4wCn3oawekWj8QdOHoQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497262&idx=1&sn=b509f84b7d2dde31b866b390a88d2223&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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