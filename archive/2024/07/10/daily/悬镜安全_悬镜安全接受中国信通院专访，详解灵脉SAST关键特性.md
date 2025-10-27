---
title: 悬镜安全接受中国信通院专访，详解灵脉SAST关键特性
url: https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791155&idx=3&sn=514d03daefb4b9f5a14dcc4f1c1ae146&chksm=87709e64b0071772c328dfd0b9a945e514f9e8562d8cd51a8cbef19d88a85a616d3584e17e91&scene=58&subscene=0#rd
source: 悬镜安全
date: 2024-07-10
fetch_date: 2025-10-06T17:46:34.201228
---

# 悬镜安全接受中国信通院专访，详解灵脉SAST关键特性

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGhftAc2IJF9GeQ3pzJmnwCrXXicUUicpbznxYg7AtYLsDiaF2ibaY4UaZNTyce1GPgPnUpL9R1UtQibozg/0?wx_fmt=jpeg)

# 悬镜安全接受中国信通院专访，详解灵脉SAST关键特性

Xmirror

悬镜安全

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGj56PMu0icIF7jYduLbYTpshJC1x89TawLCeibYDfBNPKicmHF2ibBc98oiaKiax0bTs9Vk5mQT9wYuCLhw/640?wx_fmt=gif&from=appmsg)

（本文转载自中国信通院）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dKIg2Xb8Rz5AkdSxgnOI8dMsIKEFJrFo9fhoASianQMpZFTK2f1GsOMXIDiczavWYZVP4Wt03qKvicKkVGc21ZWoA/640?wx_fmt=png&from=appmsg&wxfrom=13)

***Background***

**背景**

随着数字化的推进，软件应用服务正在潜移默化的改变着生活的各个方面，渗透到各个行业和领域，其自身的安全问题也愈发成为业界关注的焦点。通过自动化安全平台、工具，将安全融入软件服务的全生命周期，适应当前的开发模式是业界共识，也是实现研发运营安全的必要途径。**静态应用程序安全测试（SAST）工具**通过分析源代码或二进制文件等来发现程序代码存在的安全漏洞和缺陷，可以帮助开发人员在代码编写过程中提早发现和修复安全问题，从而提高应用程序的安全性。

2024年7月3日，中国信息通信研究院在“2024全球数字经济大会—云和软件安全论坛”上隆重公布了评估结果，**悬镜安全（北京安普诺信息技术有限公司）**顺利通过**“静态应用程序安全测试（SAST）工具能力评估”。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dKIg2Xb8Rz5AkdSxgnOI8dMsIKEFJrFoKDwx7cavkqX2ZE9hu77nHFc05aicqfJD8SpAs76PiapKAFBuNnd4oAwA/640?wx_fmt=jpeg&from=appmsg&wxfrom=13)

本次我们采访了**悬镜安全CTO宁戈**，分享悬镜安全的静态应用程序安全测试（SAST）工具及参与评估的收获。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dKIg2Xb8Rz5FUgibnnLfzHBoibCc1Wxt6WqImyYgLpqKIAPiaBUicPQzSicicib0J8KPPLfiaW5MjDD1p1S3tAODtho4GQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**Q：宁戈您好，请介绍一下您的企业。**

悬镜安全，起源于北京大学网络安全技术团队”XMIRROR”，创始人子芽。专注以“代码疫苗”技术为内核，凭借原创专利级“全流程数字供应链安全赋能平台+敏捷安全工具链+供应链安全情报服务”的第三代DevSecOps数字供应链安全管理体系，创新赋能金融、车联网、能源通信、政企等行业用户，构筑起适应自身业务弹性发展、面向敏捷业务交付并引领未来架构演进的共生积极防御体系，守护数字供应链安全。

**Q：请介绍一下您企业的SAST安全工具。**

灵脉SAST白盒代码审计平台基于是AI多引擎驱动的新一代智能代码审计平台，提供源代码缺陷检测、源代码合规检测、源代码溯源检测三大能力，帮助企业从编码源头解决软件开发过程中的安全缺陷、质量缺陷和编码规范缺陷，确保研发团队高质量交付。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dKIg2Xb8Rz5AkdSxgnOI8dMsIKEFJrFozdPMx1nrhYDOGJLIHBgO6GtvBvSV6ppicAPsQ3L6XepLHEqcRIFu9Gw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**Q：请介绍一下您企业SAST安全工具的应用场景及功能特点。**

灵脉SAST可应用于研发团队安全编码规范落地、软件安全测试、安全代码审计、数字供应链安全审查、DevSecOps及SDL落地等场景。基于业界领先的程序分析引擎和AI分析引擎，支持污点分析、符号执行、各类敏感性分析、指针分析、代码AI自动修复等能力，灵脉SAST可提供全面精准的检测能力；深度融合SCA软件成分分析能力，并支持组件洞可达性分析，提供数字供应链安全审查并实现供应链安全能力支撑；联动XSBOM数字供应链安全情报能力，可实时精准个性化推送漏洞风险、投毒事件、许可证风险、断供风险等安全事件信息，帮助企业和用户及时应对数字供应链安全风险。

**Q：请问通过本次标准评估对您的企业带来了什么帮助？**

悬镜灵脉SAST白盒代码审计平台成功通过信通院“静态应用程序安全测试（SAST）工具能力评估”，一方面标志着灵脉SAST符合《静态应用程序安全测试工具能力要求》标准要求，另一方面也帮助灵脉SAST在测试过程中查漏补缺，优化提升自身能力。同时，灵脉SAST通过第三方权威机构的评估，增加了产品的附加值，有效提升了灵脉SAST的市场竞争力，极大增强了用户对灵脉SAST的信任度和信心，从而为产品带来更多的经济效益。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dKIg2Xb8Rz5AkdSxgnOI8dMsIKEFJrFovl9iciac27ibhdDmAbXCJ56L5C0QGxSsIs4NH0N8gn1WxFZZpnficuJp6g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**静态应用程序安全测试（SAST）工具能力评估（以下简称“评估”）简介**

评估基于**《静态应用程序安全测试工具能力要求》**标准，对于工具的扫描分析能力要求、灵活性能力要求、分析辅助能力要求、开发流程嵌入能力要求、扩展性能力要求、兼容性能力要求、部署能力要求、安全性能力要求、服务支持能力要求**9大部分**进行评估。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dKIg2Xb8Rz5AkdSxgnOI8dMsIKEFJrFoTK0ELRHNQorQ4Sy5qC4AKP4M8ORtJddjHgXgqKYicDCLdTyyPmnMaGA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**企业参评价值**

**获得第三方资质证书，提升市场竞争力**

通过中国信通院组织的工具能力测试评估，获得第三方资质证书，证明企业自身工具已满足标准要求。企业可向客户呈现评估结果，证明工具功能完备、产品自身安全、性能满足基本业务要求，助力企业进一步提升工具的市场竞争力。

**工具能力对标行业标准，助力用户进行选型参考**

标准制定过程中广泛邀请大量业界优秀安全工具厂商专家参与，抽取包括功能项、性能项及安全关键要素，建立工具评价模型。企业可通过评估测试，验证自身工具安全可信，覆盖标准通用能力要求，为用户选择合适的安全工具提供选型指导。

**评估报名机制**

**报名机制：**滚动报名机制

**评估周期：**1-3月

**专家评审&结果发布：**每三个月组织一次专家评审会，为通过企业颁发证书

**报名方式：**

请发送报名邮件至wujiangwei@caict.ac.cn，邮件主题为相关评估报名，正文应至少包括企业名称、联系人、联系方式等内容。

＋

**推荐阅读**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGhftAc2IJF9GeQ3pzJmnwCr4wbUqUGYDickiaNNqIbV0j6kaZHfrlwFc5QSyScrR7ZChS7mhmpCuiaXA/640?wx_fmt=gif&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGhftAc2IJF9GeQ3pzJmnwCrzOWURucPibR7Zuohka5PsW0Jodv5WFZLHtvPnwHibnIlhnBt2BDVZxqw/640?wx_fmt=jpeg&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647791074&idx=2&sn=9d81dcfdfb016ad6e6f64e3b0c8c2afc&chksm=87709db5b00714a3e4a3b925b736ec6e3089f8d92f16b85e02419c06adbbbecafd7fa65799f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGhUERhKfSDYZ3wEfkTraLst97njICLJvgLnkU8lVG4dsibSjicXbtc9uRFSapNfDjcarV26qE9g5xvg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790982&idx=1&sn=36ece411a3b20638b30a5a661ba401d6&chksm=87709dd1b00714c7ce0c555a298cfc317d0dc5f12189cf38fe5949e6d9ca29ecf1ed65d884e6&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgBSdF4QaJgj2ic3qiaibot1JrAQibcGcEdSMeAMwdLAuUy3kMWEAKXPwWkY53QjibvriccJkLgibBLUWeNQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647790604&idx=1&sn=99d6b75e6bd62f4e5e32cacb75856b9f&chksm=87709c5bb007154df4244be90be71ad47c5625b3e757df35bf7a388cbcb15a0e51d9b7cf28a1&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGhftAc2IJF9GeQ3pzJmnwCrLGOic7QamoaGz83KIFRwHbRU9VOF3LGYN3bK2PGCs0iaeHhthPkfApDw/640?wx_fmt=png&from=appmsg)

**关于“悬镜安全”**

悬镜安全，起源于子芽创立的北京大学网络安全技术研究团队”XMIRROR”，作为数字供应链安全和DevSecOps敏捷安全开拓者，始终专注于以“代码疫苗”技术为内核，凭借原创专利级”全流程数字供应链安全赋能平台+敏捷安全工具链+供应链安全情报预警服务”的第三代DevSecOps数字供应链安全管理体系，创新赋能金融、车联网、通信、能源、政企、智能制造和泛互联网等行业用户，构筑起适应自身业务弹性发展、面向敏捷业务交付并引领未来架构演进的共生积极防御体系，持续守护中国数字供应链安全。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgbc11SUokwoUiacpXOWwicJCC2iaPL17Bia4raDLC9kyMgGPBcaicxnw4QbhZ8nyrstrsIbPTicmo0BRwQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiaEbrH3Qvf3yLRbjBVL227eDf2sYupEV9Yfz1GSa972dXGfL4Gc5sbjaTWXnia3OnDNTgCBRIeNTEQ/0?wx_fmt=png)

悬镜安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiaEbrH3Qvf3yLRbjBVL227eDf2sYupEV9Yfz1GSa972dXGfL4Gc5sbjaTWXnia3OnDNTgCBRIeNTEQ/0?wx_fmt=png)

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