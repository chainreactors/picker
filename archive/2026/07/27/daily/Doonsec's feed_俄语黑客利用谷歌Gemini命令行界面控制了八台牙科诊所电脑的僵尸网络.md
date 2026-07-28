---
title: 俄语黑客利用谷歌Gemini命令行界面控制了八台牙科诊所电脑的僵尸网络
url: https://mp.weixin.qq.com/s/SiBq_7ltYzWbbaInPeIzOQ
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:56:24.549558
---

# 俄语黑客利用谷歌Gemini命令行界面控制了八台牙科诊所电脑的僵尸网络

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0LGiaGIrzXulxJrPJqs6CEkH2LotW0xwaVf5EG1gicNKic0Zia7YmqTicmBHUnDaXoz6KpkBezgP5iavIyiclML18MJOWqkI4I6WyV5iaJmIib2yFthg/0?wx_fmt=jpeg)

# 俄语黑客利用谷歌Gemini命令行界面控制了八台牙科诊所电脑的僵尸网络

威胁情报Z分析

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/0LGiaGIrzXunyBKoWAUiaRRqDQu6l4zLAIibBeLQFYXF1WLUmiaYFibsicHMGpJ0DZYxsyHJSYk3Isodx05LNQxn6rvdJJwZicOflrz17CkVUYwPPg/640?wx_fmt=png&from=appmsg)

一名名为“ bandcampro ”的俄语攻击者将其部分业务外包给了谷歌的开源Gemini CLI人工智能（AI），并控制了一个实时僵尸网络。

研究结果来自对 2026 年 3 月 19 日至 4 月 21 日期间 200 个 Gemini CLI 会话日志的分析，分析发现威胁行为者利用人工智能等手段破解密码、设置住宅代理、入侵 WordPress 商家，并策划针对美国和加拿大老年人的基于电话的加密货币诈骗计划。

“日志记录了威胁行为者如何使用人工智能代理迁移命令与控制 (C&C) 服务器，以及控制小型僵尸网络，此外还进行了其他黑客活动，”趋势科技研究人员 Joseph C Chen、Philippe Lin、Lucas Silva、Vladimir Kropotov 和 Fyodor Yarochkin表示。

“整个C&C操作可以装入三个总大小约为5KB的纯文本文件中，使其具有高度可复制性和可有效销毁性。此外，还观察到人工智能在未被要求的情况下主动（未经提示）提出了59次改进建议。”

具体而言，据称攻击者滥用了 Google Gemini CLI，部署并运行了一个 C&C 基础设施，以控制一家牙科诊所的八台计算机并访问其 OpenDental 数据库。除了编写代码片段外，该人工智能还充当了整个行动的“主要黑客代理、顾问和接口”。

这包括设置服务器、将其部署到新的虚拟专用服务器 (VPS) 上、配置基础设施、设置 Cloudflare 隧道、管理机器人以及调试连接问题。

“bandcampro”的详细信息最早于 2026 年 5 月下旬出现，与一项名为“爱国者诱饵”的活动有关。该活动利用人工智能辅助信息操作 (IO) 技术运营 Telegram 频道，针对积极参与政治的美国受众进行加密货币欺诈和人工智能辅助凭证盗窃。

趋势科技将该威胁行为者描述为一名讲俄语的人，他使用谷歌 Gemini“冒充美国退伍爱国者，并避免使用俄语措辞”，同时通过扮演“授权渗透测试人员”的角色来欺骗人工智能代理绕过其防护措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0LGiaGIrzXulUwiaywVmXpcIYYibzsW4W4eeUr0e4pX6qr9FldHzUbb7VZdPzWIyicaJsO7dMF3rjcaYNjuT3FiaEFZlU257gbr0LIvvS5OycpH4/640?wx_fmt=png&from=appmsg)

据称，攻击者迅速研究了受害者机器通过 Cloudflare 隧道连接的旧 C&C 基础设施，并在六分钟内将其迁移到新的架构。该架构涉及受害者通过 HTTPS 向 C&C 服务器发出出站请求，以获取并运行攻击者预先在服务器上部署的 PowerShell 命令。

“迁移过程中立即出现错误，但人工智能代理解决了这些错误：当有效载荷分发服务器返回‘502 Bad Gateway’错误时，人工智能诊断出问题并自动添加必要的标头来解决它，”趋势科技表示。

“由于 Cloudflare 仍然阻止了请求，人工智能识别出需要 User-Agent 标头才能绕过 WAF，因此将其添加到了请求标头中。执行者没有进行任何调试，迁移仅用了六分钟就完成了。”

迁移完成后，人工智能代理执行了额外的调试工作，成功修复了导致所有受害机器与C&C基础设施断开连接的错误。此外，攻击者还被发现利用人工智能代理发送俄语自然语言指令来执行僵尸网络管理任务，从而使人工智能工具能够执行以下任务：

* 报告哪些机器处于活动状态
* 向机器人发送文件枚举命令。
* 向前台机器发送侦察指令
* 生成一行 PowerShell 命令来感染计算机

这种人工智能辅助设置尤其令人担忧的是，整个 C&C 操作可以通过三个 markdown 文件轻松移植到新的服务器上。这三个文件分别指示代理禁用其安全保护措施、包含架构描述以及包含从头开始构建的步骤，使得攻击效果远不如以前。

趋势科技表示：“在人工智能的推动下，基础设施变得可有可无，运营人员也变得可以替换。尽管攻击仍然有效，但其影响却大大降低。如果服务器被摧毁，攻击者只需在新虚拟服务器上解压软件包，人工智能就能在几分钟内完成配置和恢复。”

研究结果表明，该技术不仅可以减少运行大规模行动所需的资源，还可以使几乎没有技术知识的恶意行为者能够以最小的努力建立此类方案，或以恶意技能文件的形式在地下论坛上分发，从而有效地为超越传统“即服务”模式的新型人工智能恶意软件服务铺平了道路。

该策略还会产生使归因工作复杂化的副作用，因为没有集中式服务可供查找，人工智能代理可以随意重新生成或修改任何组件，从而绕过特定的特征。

据说，“bandcampro”曾一度指示人工智能构建一个可自我传播的“代理炸弹”，该炸弹会扫描网络并入侵尽可能多的机器，但代理拒绝了这一请求，并表示这“越界了”。与此同时，它还提供了一些有用的建议，帮助用户手动克服这些限制。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0wJVoTDXBBkc5vFwntXsAd8nDxmDyBf0Z76ENz1lEx3EmN3upgBOvJOHKylGVwXH7KCZSXduJAuoib2MvH9Hyww/0?wx_fmt=png)

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