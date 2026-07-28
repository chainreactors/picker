---
title: 智能自动化漏洞挖掘平台 -- AutoHunter
url: https://mp.weixin.qq.com/s/-8C2V0a_pNmNfZXhcoxpgw
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:56:49.192016
---

# 智能自动化漏洞挖掘平台 -- AutoHunter

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PQNvx9ufMAgrM3xCEqicCjwITJYyYUZjqpiaQObaeNv8NeiadOxmMXxsd0Wym64I9ib3UVXzgvsEgoDvgjRfa3NU5kLWHmzCtrtdjW9LiaaIOSsc/0?wx_fmt=jpeg)

# 智能自动化漏洞挖掘平台 -- AutoHunter

Chris-biu
Chris-biu

网络安全者

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

AutoHunter 把红队自动化和 AI 决策结合起来：你给它一个目标，它像一名渗透测试工程师那样， 自主决定"用哪个工具、打哪个面、查什么漏洞"，把 Burp、Xray、nuclei 这些工具串成攻击链， 最后给你一份对齐 OWASP、诚实标注覆盖盲区、去过误报的报告。核心不实现任何具体攻击——一切皆插件。用户可以零代码(YAML)或低代码(Python)不断接入新工具， 工具库越大，agent 能力越强。

**0x02 安装与使用**

常用命令：

```
pip install -r requirements.txt# 内置 demo 插件 + 自带靶场，端到端跑通整条流水线python -m autohunter scan --target http://demo-shop.local --type website --scope demo-shop.local报告输出到 reports/<任务ID>/report.html。想接真实工具？一条命令下载：python scripts/fetch_tools.py         # 自动下载 Xray / nuclei
```

一定要在虚拟机运行，工具下载链接：

公众号后台回复：20260727

链接仅一天有效，每日更新

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PQNvx9ufMAiafVwpBgXPxhkJfYHmoiafxgzsnebYCqhE4AurfCODou7icJ5SFWA89grH350m6VQBZeoVLfwIydOCicdd0GW1FRy19GuibvJrjBSs/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/mmbiz_jpg/PQNvx9ufMAg72kwqmjiccmjCVo8dPpVabnY9EauQxibgOKK4uh8fMISXibTfibicoG9Kic5GgNAKnCATdUv4eYAibHemhKicpwyvuYd5eGIjaKicSdg4/640?wx_fmt=jpeg&from=appmsg) |

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0JJXjA8siccyMF9RkfYpDn6879qdDPwuSUicNgL09meX6BzicL78PBTD7ue9VFAia6Ye1o1uvXSyXLW7hvhkLmhj9g/0?wx_fmt=png)

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