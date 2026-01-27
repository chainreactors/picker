---
title: Lazarus黑客积极攻击欧洲无人机制造公司
url: https://mp.weixin.qq.com/s/turJ4YmqIphiCa1NxSX9LA
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:36:23.679082
---

# Lazarus黑客积极攻击欧洲无人机制造公司

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qxQDibicicDUxkIicWmU3w6JGtksia7hKGO2LOicoxcObr9Txic6mCPFOkakq2sMqibZRYtalYD9tdNjaldHw/0?wx_fmt=jpeg)

# Lazarus黑客积极攻击欧洲无人机制造公司

原创

O安全研究员
O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxQDibicicDUxkIicWmU3w6JGtk3dibgelkBdclotxRGPTK4Jo0pR3gF1tPOUo2wc0ibickSNRkfHGS6xzfg/640?wx_fmt=png&from=appmsg)

Lazarus是一个与朝鲜结盟的复杂黑客组织，也被称为HIDDEN COBRA，发起了新一轮针对欧洲无人机制造商和国防承包商的定向攻击。

该活动被称为“梦想行动”，于2025年3月底出现，特别针对中欧和东南欧开发无人机技术的组织。

研究人员认为，这一活动是朝鲜加快国内无人机项目的更广泛战略努力的一部分，尤其是在俄乌冲突中观察到现代战争能力投资增加之后。

该行动标志着网络间谍战术的显著升级，旨在窃取航空航天和国防领域的专有制造信息和知识产权。

三家欧洲公司已被确认为目标，其中至少有两家深度参与设计先进单旋翼无人机和生产目前部署在活跃冲突区的关键无人机部件。

这些袭击的时间点恰逢朝鲜据称正努力大规模生产类似西方型号的MQ-9死神和RQ-4全球鹰的战斗和侦察无人机。

Welivesecurity的分析师和研究人员指出，这些攻击中使用的恶意软件基础设施采用了复杂的传输机制，旨在规避传统安全防御。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxQDibicicDUxkIicWmU3w6JGtkaLyvVDFt4TdVO5B5eSBJoKZjKhhgcIwSvKlpUPFB406YydZyibJWejA/640?wx_fmt=png&from=appmsg)

攻击始于社会工程学，特别是利用虚假的职位邀请诱使员工下载被特洛伊文件化的文件。

一旦执行，恶意软件会部署一系列专门工具，旨在保持持续访问并避免被入侵系统被发现。

## **感染机制**

主要的感染机制依赖于DLL侧载，这是一种利用合法Windows应用程序加载恶意库而不触发安全警报的技术。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qxQDibicicDUxkIicWmU3w6JGtklibTWDXTmn5mSQZdfsC6HFExIjTfPFk4icfJK1kNeh8SLjCBzRzIATmw/640?wx_fmt=png&from=appmsg)

攻击者将他们的恶意软件集成到流行开源软件的木马化版本中，包括TightVNC Viewer、MuPDF阅读器和WinMerge插件。

其中一个特别有暗示的滴管包含了内部文件名DroneEXEHijackingLoader.dll，直接指涉攻击者对无人机技术的宣传。

所有事件中部署的主要有效载荷是ScoringMathTea，一款远程访问木马，为攻击者提供对被攻破机器的完全控制权。

这种复杂的恶意软件提供了大约40种不同的系统作、文件泄露和进一步有效载荷部署命令。

ScoringMathTea特别危险的是它能够在磁盘上完全加密，仅在执行时在内存中解密，这使得传统的基于文件的检测几乎不可能，除非有先进的行为监控。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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