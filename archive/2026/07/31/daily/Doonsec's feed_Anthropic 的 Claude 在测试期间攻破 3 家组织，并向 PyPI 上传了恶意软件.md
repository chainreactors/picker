---
title: Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件
url: https://mp.weixin.qq.com/s/91erp9-Bh65eOPr-QQ2_hg
source: Doonsec's feed
date: 2026-07-31
fetch_date: 2026-08-01T05:10:15.893169
---

# Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH3wZd2tlLI2gW5pJGoXxJsZGfzibibOmsIPnoHEW8AkJ9gRjBZnOu0RpUiaiazyodiaSMN5MkCcqqibjibbpELduAPpg1KPzzWEH83FCA/0?wx_fmt=jpeg)

# Anthropic 的 Claude 在测试期间攻破 3 家组织，并向 PyPI 上传了恶意软件

欢迎关注→
欢迎关注→

安全客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Anthropic 今日表示，在内部安全测试中，其某一款 Claude 模型构建了一个恶意 Python 软件包并将其上传到 PyPI，在该软件包被 PyPI 的自动化防御机制移除之前，它已在 15 台真实系统上运行过。

![](https://mmbiz.qpic.cn/mmbiz_png/g5KiabmYVDH0R3p5mMHibfLvGC8coEzljmaDIbyAlnvyRZiasjbKNbkEpIyrCmfuRoZLgVNVa0VZ8ZGwjoeeJpqHXeYdo28P9TYat4Zot9rUkM/640?wx_fmt=png&from=appmsg)

该公司披露称，这并非孤例——在总共三起事件中，Claude 模型从一个本应被完全隔离的评估环境中"越狱"接触到开放互联网，进而攻陷了三家组织的生产基础设施。

此次审查是在 OpenAI 于 7 月 21 日披露的消息之后进行的——OpenAI 当时称其模型逃出了隔离测试环境，接触到了 Hugging Face 的生产基础设施。JFrog 随后证实，这些模型是利用自托管 Artifactory 中的零日漏洞实现逃逸的。

01

抢占一个从未存在过的包名

这三起事件均发生在由第三方评估合作方 Irregular 组织的"夺旗"（capture-the-flag）演练中。Anthropic 在提示词中告诉 Claude 它没有互联网访问权限，且环境是模拟的。然而，一处配置错误导致这两点都不属实，而两家公司直到上周才察觉。

在 PyPI 事件中，Claude 在测试环境内发现了一份文档，文档伪装成某虚构公司的开发者配置说明。

这些说明告诉新员工要安装一个从未发布过的 Python 软件包——一个"幽灵依赖"。

Claude 判断出，如果自己抢先注册这个包名，目标机器就会自动拉取它的代码。

发布这个包并不容易。Claude 需要一个 PyPI 账号，而注册账号需要邮箱地址，邮箱又需要手机号。

它没能找到免费的手机号服务，随后又尝试通过多条途径获取资金来购买手机号，但均告失败。最终它退而求其次，找到了一个未被屏蔽的邮件服务商，注册了账号并上传了恶意软件。

Anthropic 表示，该软件包在公开状态下停留了约一小时。

在这段时间窗口内，15 台真实系统下载并执行了它。其中一台属于一家安全公司——该公司习惯从 PyPI 安装软件包并扫描其中的恶意代码，其工作流程将注册表中的内容视为"可安全运行"。

Claude 的载荷被触发，将该公司的凭据发送到它自己搭建的收集点，随后利用这些凭据进一步渗透进该公司的基础设施。Anthropic 称 Claude 并不知道这家公司的存在。

PyPI 自身的安全系统自动移除了该软件包。Anthropic 表示已通知 PyPI 团队并移交了相关入侵指标（IoC）。

这次测试所运行的模型是 Claude Mythos 5。据 Anthropic 介绍，其推理过程很早就标记出了问题，指出如果互联网是真实的，发布这个包就等同于一次真实世界攻击，并称其"不可接受，而且肯定不是预期的解法"。

随后它又自己说服自己，得出了"环境是搭建出来的"这一结论，理由是它不认识为连接提供保护的证书颁发机构，且系统显示的日历日期为 2026 年。

当自动化扫描器开始安装该软件包时，Claude 把它们当成了演练中预设的"脚本演员"。

02

凭据与一个生产数据库

最严重的影响来自另一起涉及 Claude Opus 4.7 的事件——其中那家虚构的目标公司与一个真实域名重名。

在四次测试中，Claude 难以触及它的模拟目标，却发现那家真实公司可以通过互联网访问，于是便假定这就是预期目标。它提取了应用和基础设施的凭据，并触及了一个包含数百行生产数据的数据库。

这是唯一一例模型在确认身处真实系统后仍然持续发起攻击的情况。Anthropic 称这四次测试最终都识别出目标是真实的，其中两次测试中 Claude 推断：这家真实公司"本就该是演练的一部分"。

第三起事件涉及一个尚未发布、内部研究用的模型——它在未能触及预定目标后，扫描了约 9,000 个目标，随后利用一个暴露的调试页面中的凭据和 SQL 注入攻陷了一个面向互联网的应用。该模型后来注意到，这台主机所在的云账户与本次挑战毫无关联，于是判定目标是真实的，并自行停止了攻击。

这些攻击均未使用任何新技术。Anthropic 将它们描述为"弱口令和未鉴权的端点"。

03

后续将采取的措施

Anthropic 于 7 月 23 日启动了审查，并在同一天叫停了所有网络安全评估。次日它识别出这三起事件，并于 7 月 27 日通知了 Irregular 及受影响组织（目前仍在尝试联系第三家）。

这三起事件中最早的一起可追溯到 4 月，这意味着部分活动在长达约三个月的时间里都未被发现。

这些评估在运行时不带通常随正式版 Claude 模型一同提供的分类器和监控机制，尽管模型仍保留了其安全训练。

Anthropic 表示，其生产环境的防护机制本可阻止此类行为，并将这些事件定性为更接近于"测试框架与运营层面的失败"，而非"模型对齐失败"——理由是在测试中模型被告知没有互联网访问权限，而事实上却有。

该公司现计划扩大对话记录（transcript）监控范围、改进调查工具，并与评估合作方加强保障工作。

公司表示正与 METR 协商进行独立审查，并将在下周内公布一份经过轻微脱敏的 PyPI 测试对话记录。

Anthropic 联系到的两家受影响组织中，没有一家是自己发现了这些活动的——与 OpenAI 的 Hugging Face 事件一样，这些活动之所以浮出水面，完全是因为负责的 AI 实验室主动去翻查了自己的对话记录。

信息来源：https://www.bleepingcomputer.com

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[新一轮银狐攻击\_管控终端再成控制工具](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790305&idx=1&sn=59d3131871f875930282f72a5fc17ed2&scene=21#wechat_redirect)

2026-07-30

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH1YsSmllGfNbYKRF8ia7TNdTwicuXzRrALA0ic5iaiauRmxy06z62Fmx0TIJ60PYXepzwORyiahTBXCrkNQsCibPFzkbvQAPMEWbR1hkk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790305&idx=1&sn=59d3131871f875930282f72a5fc17ed2&scene=21#wechat_redirect)

[OpenAI开源Codex Security CLI：用于发现、验证和修复安全漏洞](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790293&idx=1&sn=3dafe8f68a7666a50c6edd26cfbe7932&scene=21#wechat_redirect)

2026-07-29

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH26Kib6ibyib3ia8icicIPOshAWDvBPBQA1veicBNbsXzcicvMdThKHuljsuqBwmcY79W9tmSnNia2UoOWrYGRG6OHwzWIVnfKGlvicGdicVs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790293&idx=1&sn=3dafe8f68a7666a50c6edd26cfbe7932&scene=21#wechat_redirect)

[OpenAI 的模型刚黑了 Hugging Face，微软就拿出了"反黑"模型](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790281&idx=1&sn=291dced849b77c06190f144d1f5165c9&scene=21#wechat_redirect)

2026-07-28

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH0rvn9NQEXCQAch9HNzdRBQrlqwT3uLG9zjZVUtiaJ9trrFnL8Lw9M8T2hTuePLPU2hsNLDRR9Qu69TApaiaQf1yC0hUsPy1nNWY/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790281&idx=1&sn=291dced849b77c06190f144d1f5165c9&scene=21#wechat_redirect)

[PentesterFlow —— 面向渗透测试人员和漏洞赏金猎人的 AI 自动化工作流工具](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790269&idx=1&sn=f865dda3e4caf7f67ccabcfa99489c0f&scene=21#wechat_redirect)

2026-07-27

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH1buuwrWT4Mv09pYwDu0Kibko3k3Fe6PoD24GyicKrals92bDFNpPFsQm02aTiaM7QXfhJSsdjtbmJsSsY9XLd1Bk22uMQyiczP7BM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790269&idx=1&sn=f865dda3e4caf7f67ccabcfa99489c0f&scene=21#wechat_redirect)

[为了“作弊”拿高分，AI 自己黑了 Hugging Face](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790237&idx=1&sn=850faa1161f248bbcfe79719a212c05e&scene=21#wechat_redirect)

2026-07-22

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH0iawCQl0QTQd4VEA6rP6kbdIAvpgSWCzFibLDOwQdAfjvhhJxxaRMKjM36pVwqtJMKUCO5wulVichalXGRfshrWB8vsia6WQAtOO8/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790237&idx=1&sn=850faa1161f248bbcfe79719a212c05e&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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