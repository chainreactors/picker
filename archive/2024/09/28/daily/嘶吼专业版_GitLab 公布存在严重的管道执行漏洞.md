---
title: GitLab 公布存在严重的管道执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247578221&idx=2&sn=69bbe929a17138a57a3de2a5cf92b578&chksm=e9146257de63eb4184599261d7c268a8569d8cfa24bdfd47ef37f96857e5238ec7531f68be85&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-09-28
fetch_date: 2025-10-06T18:28:34.767946
---

# GitLab 公布存在严重的管道执行漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29EheOeJb5lH3aFpR7A5k9iblfPhBHOQZVcPiaZgib3uGAicTEMqYJRlNCxCDbJo347tD8Mhz5vnYnttw/0?wx_fmt=jpeg)

# GitLab 公布存在严重的管道执行漏洞

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

GitLab 发布了关键更新以解决多个漏洞，其中最严重的漏洞 (CVE-2024-6678) 允许攻击者在特定条件下以任意用户身份触发管道。

此版本适用于 GitLab 社区版 (CE) 和企业版 (EE) 的 17.3.2、17.2.5 和 17.1.7 版本，并作为每两个月 (计划) 安全更新的一部分修补了总共 18 个安全问题。

CVE-2024-6678 漏洞的严重程度评分为 9.9，该漏洞可能使攻击者能够以停止操作作业的所有者的身份执行环境停止操作。

该漏洞的严重性在于其可能被远程利用、缺乏用户交互以及利用该漏洞所需的权限较低。GitLab 称，该问题影响 CE/EE 版本 8.14 至 17.1.7、17.2 至 17.2.5 之前的版本以及 17.3 至 17.3.2 之前的版本。他们强烈建议所有运行受下述问题影响的版本的安装尽快升级到最新版本。

GitLab 管道是用于构建、测试和部署代码的自动化工作流程，是 GitLab CI/CD（持续集成/持续交付）系统的一部分。它们旨在通过自动执行重复任务并确保对代码库的更改进行一致测试和部署来简化软件开发流程。

GitLab 近几个月多次解决任意管道执行漏洞，包括 2024 年 7 月修复 CVE-2024-6385、2024 年 6 月修复 CVE-2024-5655 以及 2023 年 9 月修补 CVE-2023-5009，均被评为严重。

该公告还列出了四个严重性较高的问题，评分在 6.7 到 8.5 之间，这些问题可能会让攻击者破坏服务、执行未经授权的命令或破坏敏感资源。这些问题总结如下：

**·CVE-2024-8640**：由于输入过滤不当，攻击者可以通过 YAML 配置将命令注入连接的 Cube 服务器，从而可能损害数据完整性。从 16.11 开始影响 GitLab EE。

**·CVE-2024-8635**：攻击者可以通过制作自定义 Maven 依赖代理 URL 来向内部资源发出请求，从而利用服务器端请求伪造 (SSRF) 漏洞，从而危害内部基础设施。从 16.8 开始影响 GitLab EE。

**·CVE-2024-8124**：攻击者可以通过发送较大的“glm\_source”参数触发 DoS 攻击，从而使系统不堪重负并不可用。从 16.4 开始影响 GitLab CE/EE。

**·CVE-2024-8641**：攻击者可以利用 CI\_JOB\_TOKEN 获取受害者 GitLab 会话令牌的访问权限，从而劫持会话。从 13.7 开始影响 GitLab CE/EE。

参考及来源：https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-pipeline-execution-vulnerability/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29EheOeJb5lH3aFpR7A5k9ib2qzZtia2UibAXFhXcv9ZE1LRIUbqJeDEfv1KutnkckHUY00NdD2fkRrA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29EheOeJb5lH3aFpR7A5k9ibaiael7aWkiavicYDrengSlUyxJysic22ZDSg9VicHa1T2TibibzteaKzyBgwA/640?wx_fmt=png&from=appmsg)

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