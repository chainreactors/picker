---
title: 苹果创建 Private Cloud Compute VM 助力漏洞挖掘
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521275&idx=2&sn=19b473f06f7cec3e44d2eaabe7de9012&chksm=ea94a291dde32b87aff71cc0155c176a313b40ce3d7e6f79a0f7ffc2adc898412e8c6a0b0be0&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-26
fetch_date: 2025-10-06T18:54:00.262032
---

# 苹果创建 Private Cloud Compute VM 助力漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQiadzhZU8L1ToyibztB8NGkxjmbZCGAicGRS3v3o0FMjKEqk1dzOmXNwVyaq1cT3QQogsynF84kCxRg/0?wx_fmt=jpeg)

# 苹果创建 Private Cloud Compute VM 助力漏洞挖掘

Ionut Ilascu

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQiadzhZU8L1ToyibztB8NGkxx0MR54icKyOSiciaRV4AZibRfZ82P1ZmWzWcAAsexM3jaWLia1w4FZxJHwA/640?wx_fmt=gif&from=appmsg)

**苹果创建了一个虚拟研究环境，供研究员测试其Private Cloud Compute（PCC，私有云计算）系统的安全，并发布一些“关键组件”的源代码，帮助研究员分析该脚骨的隐私和安全特性。**

苹果公司还希望改进系统安全性，并将其最高漏洞赏金提升至100万美元，条件是这些漏洞可攻陷“PCC的根本安全和隐私保证”。PCC 是一款云情报系统，用于对用户设备中的数据进行复杂的、不会攻陷隐私的AI处理。它通过端对端加密，确保只有用户能够访问（甚至苹果都无法访问）从苹果设备发送给PCC的个人数据。苹果公司发布PCC后，为安全研究员和审计人员开放访问权限，以便他们验证系统的隐私和安全前提。

**虚拟研究环境**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQiadzhZU8L1ToyibztB8NGkxsx156goZJMibibZ0uRzydzgkPVX9R3qpUM9Nelo735wfGvUaUTxGq91Q/640?wx_fmt=gif&from=appmsg)

苹果公司在博客文章中提到，目前PCC的访问权限已公开，任何好奇之士均可查看它的运行原理并检查是否与所承诺的相符。

苹果公司发布了《私有云计算安全指南》，解释了该架构和这些组件的技术详情及其运行方式。苹果公司还发布了虚拟研究环境 (VRE)，在本地复刻了云情报系统，以便对其安全性和问题进行测试和发现。

苹果解释称，“VRE在虚拟机器中运行PCC节点软件，且改动非常小。用户空间软件与PCC节点的运行方式相似，启动流程和内核都为虚拟化进行了调整。”苹果还发布了相关的VRE安装文档。

VRE位于 macOS Sequia 15.1 Developer Preview中，需要具有苹果硅片和至少16GB的统一的存储内存。该虚拟环境中的可用工具可允许用户在隔离环境中启动 PCC 发布，修改和调试 PCC 软件，进行全面审查并对文档模式进行推测。

为便于研究人员工作，苹果公司决定为一些执行安全和隐私要求的 PCC 组件发布源代码：

* CloudAttestation 项目：负责构建和验证 PCC 节点的证明。
* Thimble 项目：包括在用户设备上运行的 privatecloudcomputed 守护进程，并使用 CloudAttestation 执行可验证的透明度。
* Splunkloggingd 守护进程：过滤可从 PCC 节点传播的日志，防止数据的不慎披露。
* Srd\_tools 项目包含 VRE 工具，并可用于了解 VRE 如何运行 PCC 代码。

苹果公司还在安全奖励计划中纳入新的 PCC 类别，应对数据的不慎泄露、来自用户请求的外部攻陷，以及物理或内部访问权限。针对请求数据的远程攻击的最高奖励是100万美元，研究人员需要通过任意权限实现远程代码执行后果。如果演示如何获取用户请求数据或敏感信息的访问权限，则可获得25万美元的赏金。如果能以提升后的权限从网络执行相同的攻击，则可获得5万到15万美元的赏金。不过，苹果表示还考虑对PCC造成重大影响的漏洞，即使这些漏洞并未包含在漏洞奖励计划内。

苹果公司认为其“私有云计算是为云AI计算大规模部署的最高阶的安全架构”，但仍然希望借助研究人员进一步改进其安全性和隐私性。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[苹果修复可导致窃听的 AirPods 蓝牙漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519901&idx=2&sn=3262641607db182c3d651a403a7e8a1f&chksm=ea94bff7dde336e1616ab487b523e96ef95fcc21705f4fa168d534c13bb1ee1a7bc0de09a134&scene=21#wechat_redirect)

[苹果紧急修复已遭利用的两个新 iOS 0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519003&idx=1&sn=87b2f80deede9f2cb8e1092e9732820f&chksm=ea94ba71dde333675f4150799bb36ccc5360912e77c0af8aef77e7426b9b0c244aabb76833e4&scene=21#wechat_redirect)

[苹果 Shortcuts 零点击漏洞可导致数据被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518905&idx=2&sn=89ec572b50147fe28714126b1d8bcb55&chksm=ea94bbd3dde332c507d0bd517efb3a88849ef91c65ed3b863479408bd332068071f546a9914c&scene=21#wechat_redirect)

[苹果 Vision Pro 首发即被黑，内核漏洞触发崩溃](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518831&idx=1&sn=91fdd7a64e5019377ad958272beed267&chksm=ea94bb05dde3321343a784cc3b05ff1f50bca0fe764b046fc5e40d5ebb5195c774c40f83503d&scene=21#wechat_redirect)

[苹果修复2024年遭利用的第1个0day漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518729&idx=1&sn=022dec20b1d19ed71466fd78c5c9b7c1&chksm=ea94bb63dde33275e80731ce7aa70dbb77566e3599abe9f927ae24a32dc66aff5a1acd09f3d5&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/apple/apple-creates-private-cloud-compute-vm-to-let-researchers-find-bugs/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

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