---
title: 新一轮银狐攻击_管控终端再成控制工具
url: https://mp.weixin.qq.com/s/K_J65T1viZ6gctVX_iKtRQ
source: Doonsec's feed
date: 2026-07-30
fetch_date: 2026-07-31T05:28:35.643932
---

# 新一轮银狐攻击_管控终端再成控制工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH3HCkBdJx0iafKlRNel0WXyCISEHK2eLjibKiaOKzWqQTad25HNYJFZ342ic43sEGVNnjYyftvrVMn2kbpcgrnzY5BfRZlLot4icGYc/0?wx_fmt=jpeg)

# 新一轮银狐攻击\_管控终端再成控制工具

欢迎关注→
欢迎关注→

安全客

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

01

终端管理系统被利用已成常态

近期，360监测发现此前曾被“银狐”（Silver Fox）黑产团伙利用的某“统一终端管理系统”再次遭恶意利用。作为企业级IT运维常用的终端管理平台，该系统此前就因具备远程控制、软件分发等“便利”功能，而多次成为“银狐”家族木马的传播载体与控制通道。针对潜在的被利用风险，该系统官方在新版的客户端中新增了人机验证码（CAPTCHA）校验，试图提升自动化入侵门槛。然而，根据我们对最新样本所进行的分析，攻击者实际上已找到了绕过人机验证的有效手段。目前，该管理系统的客户端依旧在部分攻击链条中被当作隐蔽的远控后门使用，相关防护仍需进一步加固。

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibSPs7H4FtyXFf4JJiaQiao4TAHwLF63BuRLX65SRJOlyMhkLd07V9wsL2p9zEshtlDwjGj4RVJIB2OPfD4KAFt1WZykpYaJgECs8/640?from=appmsg)![]()![]()

图1. 银狐木马典型钓鱼页面

02

木马分析

我们的安全分析人员从“银狐”钓鱼页面上下载了伪装成某音乐播放器的恶意压缩包，解压后可以看到，该压缩包中包含了一份说明文档和一个木马安装程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g5KiabmYVDH3RFTtpnGS6IfkoRK9UjclB1eoadlbicG5R2zoJXsU49DXCTVlcgGNsoFk9QxNBzJhpo3qbUZaLp3qXoyiaibomc1voYYicT1zibNFo/640?wx_fmt=png&from=appmsg)

图2. 伪装为某音乐播放器的木马安装程序

钓鱼木马攻击者精心构造了名为“音乐最新版本安装说明.txt”的社会工程学话术文档，用来诱导用户执行同压缩包内的木马程序。该木马针对被利用的统一终端管理系统客户端新增的人机校验机制，提示用户“\*\*音乐最新版本客户端需输入官方证书4位验证码以完成安装”，并要求用户在遭遇杀毒软件拦截时一律选择“允许”。伪装成正常软件的安装流程提示，不仅显著降低了用户的防范意识，同时也有效引导用户在受控主机上主动运行木马，并绕过了终端管理系统的人机校验机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g5KiabmYVDH0iahVkfk69HYfw1AH8OzDAEMdd6UvteiaxxobKUCQk00ia4PibEnS3pibAwVYpKjlYemSq2k9ReQMa1IiaDxnMcoNPj9kuiakgb5O9VM/640?wx_fmt=png&from=appmsg)

图3. 精心构造社会工程学话术误导受害用户的“说明文档”

当用户在执行“音乐最新版本客户端64x2026226.exe”时，会弹出人机验证码。该验证码的作用是确保安装操作是“真人”手动执行，而非由某些恶意脚本、自动化工具或木马病毒在后台静默安装该管理客户端。如果有程序或脚本试图在系统后台安装该终端软件，则会因为无法“看懂”并输入这个不断变化的验证码，导致安装直接中断。

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibRh8ibHCuzmDMrvqBjryWxwAZBuBqEiaoGEicfOicg5JSh4J7tia6Axibs4vtcKVRcxZhxQZNibFMlcSS0dcibiaKOsjvN3pHdxtMibIfd3E/640?from=appmsg)![]()![]()

图4. 用于防范自动静默安装的人机验证码

当受害用户被诱导完成安装后，木马会将用于远控上线的IP地址，直接写入系统注册表。我们分析的样本写入的IP地址为：156.251.16.226。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibQysG1ia1jZ2aVqupTGkzv8VvEIbCk5fq02kJiaVYaZS5QAjcKkSIkibzDyiaqMsgdtGb6kmnC7Cx7bgdKaSy9ahiaiaAQ2jjGpoFuhM/640?from=appmsg)

图5. 木马在注册表中写入的上线IP地址及其他配置

该远控模块沿用了该统一终端管理系统的完整运维功能集。攻击者可借此实现对受害主机的深度控制，典型能力包括：带屏幕录制的远程桌面接管、文件上传下载、实时语音/视频通话、任意自定义脚本执行以及远程关机、重启与磁盘清理等系统操作。此外，客户端会在本地生成详尽的日志文件，日志文件中记录了代理与管控端的通信链路状态、软件/补丁部署结果、服务与进程启停事件、策略下发与执行情况等，为攻击者提供持续的用户行为监控与木马执行反馈闭环。

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibQx3phzJCmyOKSdyfbgfGBF6INDCEdEYubEEbkUVUF4F90B5hRoJSxN7MC6YMNCOMicchHB71DsLwaqCpsf5mLCFN8yuBsDibNOc/640?from=appmsg)

图6. 终端管理系统的日志文件

03

安全防护与建议

如果用户不幸遭受本轮银狐攻击中的远控木马感染，可以前往360官网下载并安装360安全卫士进行全盘扫描。360安全卫士会自动检出恶意软件，用户只需根据安全扫描结果进行清理修复，最终重启设备便可解决问题。

![](https://mmbiz.qpic.cn/mmbiz_png/ribStUdgfRibRTz0pYS4dKzLg1ePreZRQxyicMwK5OnZvWWAicK3F1UW7vDvhvNHtajicjkNoibUmN4aUWF3zicicjAxGToI0oIOnibLPax9cBAqfSp0/640?from=appmsg)

图7. 360终端安全产品查杀银狐木马

如果在木马攻击前用户已安装360终端安全产品，则不必担心该木马，360安全大脑可对此类木马进行有效拦截和查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ribStUdgfRibS0RP0R0wwtTMA76QzZPoQtH0xBYwvVOj0205D5KXqPdQlRj2KXsuBibny4FYrtqwlYMd11u7XoyfnNeDHeKxq4xmkn9aMntibuQ/640?from=appmsg)![]()![]()

图8. 360安全大脑可拦截和查杀银狐木马

IOCs

1.MD5

d5daa5d9445497438c5bcdf8d0bc7688

2.C2

156.251.16.226

3.URL

hxxps://web.app-qishui.cn/

hxxps://qishuiyinle.oss-cn-hongkong.aliyuncs.com/qishui\_Setup2026.zip

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/o0buL62hK7M8RnVz7mqRVDRkqm2sJeT2icM4WyR7kMkHpLVaicR3tJ4gr5kIb4zje9lXgd5PuOw42Z5KtathltcQ/640?from=appmsg)

**END**

推荐阅读

[OpenAI开源Codex Security CLI：用于发现、验证和修复安全漏洞](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790293&idx=1&sn=3dafe8f68a7666a50c6edd26cfbe7932&scene=21#wechat_redirect)

2026-07-29

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH26Kib6ibyib3ia8icicIPOshAWDvBPBQA1veicBNbsXzcicvMdThKHuljsuqBwmcY79W9tmSnNia2UoOWrYGRG6OHwzWIVnfKGlvicGdicVs/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790293&idx=1&sn=3dafe8f68a7666a50c6edd26cfbe7932&scene=21#wechat_redirect)

[OpenAI 的模型刚黑了 Hugging Face，微软就拿出了"反黑"模型](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790281&idx=1&sn=291dced849b77c06190f144d1f5165c9&scene=21#wechat_redirect)

2026-07-28

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH0rvn9NQEXCQAch9HNzdRBQrlqwT3uLG9zjZVUtiaJ9trrFnL8Lw9M8T2hTuePLPU2hsNLDRR9Qu69TApaiaQf1yC0hUsPy1nNWY/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790281&idx=1&sn=291dced849b77c06190f144d1f5165c9&scene=21#wechat_redirect)

[模型开源，力破西方偏见](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790274&idx=1&sn=a87b5b5f82aef8b972765141b7f504ab&scene=21#wechat_redirect)

2026-07-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH3LbaJXmBubL25SrXU8CnN0N4MUYQNRuaXibg9JwYV6lAFltyaA4RYSyGKJDbBFfr5g7NPQHotQvqKgTEgZZBnCwrBgv82kmsjI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790274&idx=1&sn=a87b5b5f82aef8b972765141b7f504ab&scene=21#wechat_redirect)

[PentesterFlow —— 面向渗透测试人员和漏洞赏金猎人的 AI 自动化工作流工具](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790269&idx=1&sn=f865dda3e4caf7f67ccabcfa99489c0f&scene=21#wechat_redirect)

2026-07-27

[![](https://mmbiz.qpic.cn/mmbiz_jpg/g5KiabmYVDH1buuwrWT4Mv09pYwDu0Kibko3k3Fe6PoD24GyicKrals92bDFNpPFsQm02aTiaM7QXfhJSsdjtbmJsSsY9XLd1Bk22uMQyiczP7BM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790269&idx=1&sn=f865dda3e4caf7f67ccabcfa99489c0f&scene=21#wechat_redirect)

[《AI编程工具“塌房”实录：Grok Build整库上传、Claude Code后门暗桩，哪个更让你睡不着？》](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790269&idx=2&sn=556cf12565f116668a7c0b3baccb8482&scene=21#wechat_redirect)

2026-07-27

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g5KiabmYVDH1gTOdmFbzt4zyspGKaWMP3XLIohkpaG3M8ibQJB5IfSNGh4z8YPuKrGicq3pp3ltib9sjeC4s4ictlqksibibicP4u5ECoLGA0mZq2s4/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649790269&idx=2&sn=556cf12565f116668a7c0b3baccb8482&scene=21#wechat_redirect)

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