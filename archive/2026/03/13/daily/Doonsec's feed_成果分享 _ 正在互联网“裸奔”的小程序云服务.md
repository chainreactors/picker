---
title: 成果分享 | 正在互联网“裸奔”的小程序云服务
url: https://mp.weixin.qq.com/s/avTBfZMWdvrID-j3iVDx4Q
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:47.456320
---

# 成果分享 | 正在互联网“裸奔”的小程序云服务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0mdnIU7wBrqNTx0WRgzuyiaibRGHia4V2P4pjWwa0kopzXRYyCcK2G2PcDlrqVMUWd8mNQWWSSkG46rRPcRY8ia0sUicicPic61dtK64icFNOLiaCsGs/0?wx_fmt=jpeg)

# 成果分享 | 正在互联网“裸奔”的小程序云服务

原创

secsys
secsys

复旦白泽战队

![]()

在小说阅读器中沉浸阅读

微信等超级应用为小程序开发者提供了便捷的云端服务，如云数据库、云存储等，使开发者可以方便高效地管理业务数据。然而，便捷的开发环境并不等同于自动化的安全保障。研究发现，开发者在云资源访问控制实现上的普遍疏忽，正使小程序云端成为了新的安全重灾区。

近期，复旦大学系统软件与安全实验室小程序安全研究小组对小程序云服务进行了系统研究，揭示了数千个小程序存在云资源泄露风险，大量敏感数据在互联网中“裸奔”。该研究成果已发表于网络安全顶会NDSS 2026。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrqDKkLKibgP9ddQick30ibptMVibyTl74zHvWMrhia4ibLMI8C2rBMiaXLOyhmEicjq0NhMe2tAPL4R9jady5ySqQMpd8rgEYH2Ehdvbo4/640?wx_fmt=png&from=appmsg)

研究背景

随着“App-in-App”生态的蓬勃发展，小程序已深入支付、医疗、政务等各类高敏感场景。为支撑日益复杂的业务逻辑，超级应用推出了小程序云开发服务：开发者无需自行搭建和维护服务器，即可便捷地调用云数据库、云存储及云函数，将用户信息、交易流水、甚至核心业务逻辑直接托管于云端。为了保护这些资源，超级应用设计了一套身份管理机制，旨在保障只有经过授权的用户才能访问特定数据，确保数据访问严格遵循“最小权限原则”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBroemXM4FicvgPLCIJROvibwCY25lwHDJoqN9ibXpRUTr67EUwrNT7gFhScm3Iw86E2wzttX5HVehwMEhSKicEMWdia6hsW6ReyRb9MI/640?wx_fmt=png&from=appmsg)

小程序生态中的云资源管理机制

问题核心：脆弱的身份屏障

然而，我们的研究发现，开发者在实际开发过程中往往存在两类普遍的安全问题：

* **身份校验的“形同虚设”：**开发者未能正确核实请求者的真实身份。例如，部分小程序仅依赖用户的身份信息（如邮箱、手机号）作为云端资源的访问凭据，这意味着攻击者只需篡改这些信息，即可轻易地冒充他人身份，越权获取各类敏感隐私。
* **权限分配的“门户大开”：**开发者未能遵循“最小权限原则”，错误地将特权资源（如管理员密钥）或高危业务逻辑（如修改账户余额）的操作权限直接下放给普通用户，使云端数据库沦为毫无防备的“公共账本”。

在分析过程中，我们发现一个网课小程序使用用户填写的“手机号”来检索云数据库（course\_users），进而获取用户的姓名和家庭住址等信息。攻击者只需在请求中篡改手机号，就能批量窃取所有用户的隐私信息。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrrFMAU1YQrQcibpY5ANw5lxynNaNhHCs9HWkZicbYyFy0sseYRSLJDFIgnp12scBKaDM1IQa08DxWQArPgIdmibx19oJpo9x3khXY/640?wx_fmt=png&from=appmsg)

访问云数据库的示例代码

工具设计

针对隐蔽的云端逻辑缺陷，我们研发了自动化探测工具 ICREMiner。该工具首先通过静态分析精准提取代码中的云资源访问操作；随后，针对难以直接观测的隐藏云资源，创新性地引入大模型（LLM）推理与跨小程序关联分析，实现深度“逻辑推演”；最后，利用动态探测技术在不影响业务逻辑的前提下进行实测，从而实现对小程序云资源安全风险的自动化识别。

![](https://mmbiz.qpic.cn/mmbiz_png/0mdnIU7wBrpaXQY8lKeEPxektowMBDBAviciavpibEmf2Ege4BCBicBG3ulEXWk4TvXqlaC4RdrdnS6UxvjYhXKhT4F2xV40DN5ic5Y3fBvCWk5c/640?wx_fmt=png&from=appmsg)

ICREMiner 工作流程

研究成果

研究团队对真实世界中的小程序进行了大规模自动化扫描，识别出 **22,695**个使用云服务的小程序。分析结果显示：

* **漏洞影响广泛：**ICREMiner 成功检测到 **2,815** 个小程序存在严重的云端安全漏洞，共涉及 **8,062** 个高危云操作。
* **敏感隐私“裸奔”：**漏洞导致海量用户的姓名、家庭地址、身份证号、就医记录等敏感信息处于“不设防”状态。受影响的小程序涵盖了医疗健康、在线教育及金融服务等多个敏感领域。
* **推动安全修复：**秉持负责任的披露原则，研究团队已向开发者提交了详细的漏洞报告，积极协助其修复安全隐患，共同筑牢小程序生态的安全防线。

白泽·鉴微小程序安全平台

基于过去在小程序安全领域的一系列研究工作，我们开发并推出了小程序安全检测平台——**白泽·鉴微**。

平台将利用程序分析与代码语义理解等技术，为你的小程序进行一次从内到外的“CT检查”，揪出潜在的安全漏洞！

我们希望通过该平台为开发者提供免费的安全检测服务，提升整个行业对小程序安全的重视与防护水平，欢迎开发者和相关从业者体验与使用！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0mdnIU7wBrpnvynU32mhkhbJD6so1rKZVfXWZEQGeN3DKV3c9v9knGqibhkdhB2aUibj4cics280AuDrywAjqBzwP42icyra57hazSKzZIosjB8/640?wx_fmt=png&from=appmsg)

白泽·鉴微小程序安全平台：

https://security.fudan.edu.cn/miniappplatform

如有兴趣了解平台的更多细节，可参考[往期推文](https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247495505&idx=1&sn=098b4dcf46e48506fc2a20fcea92b2e0&scene=21#wechat_redirect)

研究团队

杨哲慜，复旦大学计算与智能创新学院副教授。研究方向为软件安全攻防技术，在网络安全顶级国际会议上发表论文 20 余篇，多项成果获网络空间安全顶级国际会议焦点论文、杰出论文奖等荣誉。曾获评新耀东方风采人物、上海市科学技术一等奖、中国计算机学会科学技术奖二等奖、上海市计算机学会科学技术奖一等奖。发现数万“零天”安全漏洞，影响谷歌、华为、三星、百度、阿里、腾讯、抖音、小米、高通等国内外知名企业及全球数十亿用户，国家互联网应急中心授予“2021年最具价值漏洞奖”。

个人主页：https://yangzhemin.github.io/

联系方式：yangzhemin@fudan.edu.cn

史一哲，复旦大学计算与智能创新学院博士研究生，本科毕业于复旦大学计算机科学与技术专业。主要研究方向为小程序与移动应用的隐私安全与漏洞挖掘等，在NDSS、IEEE S&P等网络空间安全国际顶会上发表过学术论文，已累计获得上百个CVE和CNVD编号。

素材：史一哲、11

素材：11、崔璐凯、王清宇

责编：董佳仪

审核：杨哲慜、洪赓

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、小红书搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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