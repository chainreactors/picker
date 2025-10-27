---
title: 奇安信代码安全实验室研究成果成功入选国际顶会USENIX Security 2023
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514605&idx=1&sn=cd8bd055b332966958daeed4d0e4efa8&chksm=ea948887dde30191455382cb0afea31ac5c7045a891bf7b460f0b60dffb5e78edf3150f282ce&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-11-12
fetch_date: 2025-10-03T22:34:20.844314
---

# 奇安信代码安全实验室研究成果成功入选国际顶会USENIX Security 2023

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRc7SIYlxCoCULZPJjWxrAS89v0ZwAySzgcpErBqXgBgU89AVCsokicFQ6CZl5qEH32w75JI9kUk7g/0?wx_fmt=jpeg)

# 奇安信代码安全实验室研究成果成功入选国际顶会USENIX Security 2023

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**日前，奇安信代码安全实验室研究员张之义以共同一作身份与天津大学王俊杰教授团队完成学术论文《FuzzJIT: Oracle-Enhanced Fuzzing for JavaScript Engine JIT Compiler》，被信息安全领域四大顶级会议之一USENIX Security 2023录用。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMRc7SIYlxCoCULZPJjWxrASYEdhFcKiaZbF4icwGoR2RTGarR2vSHkbYRLE5n9lGKzOAeibZDlYiaO7pA/640?wx_fmt=png)

该论文提出了一种寻找主流JavaScript引擎JIT (Just In Time) 编译器编译优化缺陷的思路，并通过模糊测试的方式进行了实现。

近些年在国内外的顶级破解大赛中，使用JavaScript引擎JIT编译器的漏洞成功攻破浏览器的案例越来越多。针对JIT编译器优化的研究也变得越来越重要。JavaScript引擎是用于执行网站中的JavaScript代码，其中JIT编译器引擎主要是加快引擎的执行速度，但同时也要确保执行结果是正确的。目前主流引擎的JIT编译优化均采用多级优化的机制层层优化IR中间代码，进而动态生成native代码。但在层层优化的过程中可能会一些未考虑到的情况。为了挖掘此类缺陷我们从触发JIT编译器优化，到针对优化策略变异，最后捕获JIT编译器bug这三个主要方面进行实现。截至论文成稿之前，成功在主流浏览器 Chrome (Edge-based Chromium) 浏览器的V8引擎，Safari浏览器的JavaScriptCore引擎，Firefox浏览器的SpiderMonkey以及Edge浏览器ChakraCore引擎中发现30多个和JIT编译器优化相关bug。

**参考链接**

https://www.usenix.org/conference/usenixsecurity23/summer-accepted-papers

**关于代码安全实验室**

奇安信代码安全实验室是奇安信集团旗下，专注于软件源代码安全分析技术、二进制漏洞挖掘技术研究与开发的团队。实验室支撑国家级漏洞平台的技术工作，多次向国家信息安全漏洞库（CNNVD）和国家信息安全漏洞共享平台（CNVD）报送原创通用型漏洞信息并获得表彰；帮助微软、谷歌、苹果、Cisco、Juniper、Red Hat、Ubuntu、Oracle、Adobe、VMware、阿里云、飞塔、华为、施耐德、Mikrotik、Netgear、D-Link、Netis、ThinkPHP、以太坊、Facebook、亚马逊、IBM、SAP、NetFlix、Kubernetes、Apache基金会、腾讯、滴滴等大型厂商和机构的商用产品或开源项目发现了数百个安全缺陷和漏洞，并获得公开致谢。目前，实验室拥有国家信息安全漏洞库（CNNVD）特聘专家一名，多名成员入选微软全球TOP安全研究者、Oracle安全纵深防御计划贡献者等精英榜单。在Pwn2Own 2017世界黑客大赛上，实验室成员还曾获得Master of Pwn破解大师冠军称号。

基于奇安信代码安全实验室多年的技术积累，奇安信集团在国内率先推出了自主可控的软件代码安全分析系统——奇安信代码卫士和奇安信开源卫士。奇安信代码卫士是一套静态应用程序安全测试系统，可检测2600多种源代码安全缺陷，支持C、C++、C#、Objective-C、Swift、Java、JavaScript、PHP、Python、Cobol、Go等20多种编程语言。奇安信开源卫士是一套集开源软件识别与安全管控于一体的软件成分风险分析系统，通过智能化数据收集引擎在全球范围内广泛获取开源软件信息和漏洞信息，帮助客户掌握开源软件资产状况， 及时获取开源软件漏洞情报，降低由开源软件带来的安全风险，奇安信开源卫士目前可识别9000多万个开源软件版本，兼容NVD、CNNVD、CNVD等多个漏洞库。奇安信代码卫士和奇安信开源卫士目前已经在数百家大型企业和机构中应用，帮助客户构建自身的代码安全保障体系，消减软件代码安全隐患，并入选国家发改委数字化转型伙伴行动、工信部中小企业数字化赋能专项行动，为中小企业提供软件代码安全检测平台和服务。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSAib18FcZgPnzx1sdNbYvIN0WZJpnMMy5JnlPiboiaoTbmnKxUXzH15ZdXNC7OKXuGl1mWYGzC1ubXA/640?wx_fmt=jpeg)

---

**推荐阅读**

[奇安信代码安全实验室研究成果入选Black Hat和POC安全大会议题](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514220&idx=1&sn=750a288be57eb8452af469145908204b&chksm=ea948906dde3001079435980a74be8cd2323e4db3b1658dd30655296b28c8fa54cacfd9002d3&scene=21#wechat_redirect)

[奇安信代码安全实验室三人入选“MSRC 2022全球Top 100最具价值研究者”榜单](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513481&idx=1&sn=83b9a6b6887a3d6a63ff809bc4cfbc94&chksm=ea9484e3dde30df53fb368288bdea125e203c56f7d0359a34c6f61f707b6a1154d1ac526b340&scene=21#wechat_redirect)

[奇安信代码安全实验室研究员入选“2021微软 MSRC 最具价值安全研究者”榜单](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506794&idx=1&sn=963c32557110d553de4cb65278e9b0ac&chksm=ea94ea00dde36316d9a6837bd0c6c0b1f6fc123f5ead77738d9404d0445a3fe80d6eb6e6c946&scene=21#wechat_redirect)

[奇安信代码安全实验室帮助谷歌修复高危漏洞，获官方致谢](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247504133&idx=1&sn=b495682ba589704ef76014370e8ce548&chksm=ea94e06fdde36979545e7e9cf0b639c3bc09580fa372cb2203557da01622b2877f96dfb26304&scene=21#wechat_redirect)

[奇安信代码安全实验室帮助微软修复远程内核级漏洞，获官方致谢](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247503429&idx=2&sn=13f9adc1c5a3abd69c7ecaa3b88d245d&chksm=ea94ff2fdde3763987342daf5ce4a64a1548a52f8ea68a474b51ea53f3109f9cf2cd3a81dd76&scene=21#wechat_redirect)

[奇安信代码安全实验室帮助谷歌修复高危漏洞，获官方致谢](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247503245&idx=1&sn=fecff8cc3a6944e4271b8bc96504fdda&chksm=ea94fce7dde375f168a2201ee571d0a5c47ebf3131995e9fbff039f13bb1db42f8c3188bef01&scene=21#wechat_redirect)

**转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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