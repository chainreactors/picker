---
title: 密码学大模型：玄知大模型V4发布
url: https://mp.weixin.qq.com/s/2tBLIPBPYsxbTUdOVElNOg
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:58:15.981179
---

# 密码学大模型：玄知大模型V4发布

# 密码学大模型：玄知大模型V4发布

信息安全最新论文技术交流

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年8月29日，在西部网络安全大会上，西安电子科技大学计算机科学与技术学院沈玉龙教授团队正式发布**玄知大模型V4。**

一年前，团队在这里发布首个面向密码学领域的大语言模型[密码学大模型——玄知大模型V3.0升级](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492068&idx=1&sn=f5692b5c181bc92703a7571b82870bf0&scene=21#wechat_redirect)；一年后，玄知从“能够理解和回答密码问题”，进一步走向“能够持续推进复杂密码任务”，全面升级为**基于CryptoHarness的可验证密码智能科研系统。**

点击视频，*了解玄知V4如何从“会回答”走向“能完成任务”：*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/uy0ju4nn6IicSnPb246CvnaibNJR37HZPcuJiblOygIoEXXWVcSD1K0V095JWThLsxibnQczlpzufzZ6gwMtpnjXJg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

**从V1到V4：四代持续演进**

密码学科研任务通常具有**长链条、多工具、强约束**的特点。一个安全结论，不仅需要模型理解和推理，还需要代码、工具、标准与专家共同验证。

* **V1：密码大模型基座**。 让密码知识进入大模型。
* **V2：子领域专项突破**。 让知识转化为专业任务能力。
* **V3：****多智能体协同**。 让不同密码能力协同完成任务。
* **V4：可验证智能科研系统**。 让复杂任务持续运行、受控执行，并形成可复核成果。

V3解决了“有哪些专业能力、这些能力如何协同”；V4进一步解决“复杂任务如何持续推进、如何接受验证、如何完成交付”。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/uy0ju4nn6IicSnPb246CvnaibNJR37HZPcuJiblOygIoEXXWVcSD1K0V095JWThLsxibnQczlpzufzZ6gwMtpnjXJg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

**为什么需要CryptoHarness？**

通用Harness主要解决模型如何连接工具、组织流程；密码科研还必须回答更多问题：任务依据什么安全目标和攻击者模型开展？工具调用是否受到权限约束？结论是否有代码、测试或形式化证据支持？任务中断后能否从正确状态继续？

为此，玄知V4构建了面向密码科研的CryptoHarness：

**玄知V4 = CryptoLLM + CryptoHarness + CryptoVerifier**

* **CryptoLLM**负责理解任务、分析问题、制定计划与生成方案。
* **CryptoHarness**负责组织智能体与技能（Skill），管理状态、工具、权限、执行与恢复。
* **CryptoVerifier**通过代码、测试向量、形式化工具、标准规则和专家审核提供校验依据。

**三者协同，带来三项核心升级**

* **执行升级：** 通过任务契约和持久状态，让复杂任务可以暂停、恢复、分叉和重放。
* **可信升级：** 工具在权限、沙箱和审计约束下运行，任务结果由预设条件、机器证据与专家复核共同判定。
* **进化升级：** 记录失败轨迹与上下文，用于重新规划、回归评测和系统优化。

V4最终交付的不再只是一段回答，而是包含**分析报告、运行代码、形式化规约、攻击轨迹、工具结果**和**验证记录**的任务级成果包

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wBNKsKdglKGoLLAm4W2o2jTzf72mRpH1jC9T4lBu4px01u3mg6QYKEzBkUhibucD9DsDqicvuZ9ibiakOZw4wafhOEY5YmL7GY0fUKUw1ggt7r4/640?wx_fmt=jpeg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=5)

模型负责理解与推理，CryptoHarness负责组织与执行，CryptoVerifier负责检验与判定

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/uy0ju4nn6IicSnPb246CvnaibNJR37HZPcuJiblOygIoEXXWVcSD1K0V095JWThLsxibnQczlpzufzZ6gwMtpnjXJg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

**现场实测：**

**让系统能力接受专家检验**

此次发布不仅展示了V4的技术架构与研究案例，还设置了实物系统现场测试环节。**孔志印院士及多位专家现场体验了玄知V4**，从任务输入开始，观察系统如何理解需求、制定计划、调用知识与工具，并形成分析与验证结果。

测试过程中，专家重点关注了玄知V4的密码专业能力、复杂任务执行过程、工具协同方式和结果可追溯性，并结合真实科研与工程需求进行了深入交流。**现场测试反馈良好**，专家对V4从“生成答案”走向“推进任务”、从“模型判断”走向“证据校验”的升级给予积极评价，也对系统后续在密码算法分析、协议验证和工程实现等场景中的应用提出了意见与建议。

这次面对面的测试，让玄知V4的能力不再停留在架构图和案例材料中，而是通过可操作、可观察的现场演示，进一步展现了其服务密码科研与工程实践的潜力。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/uy0ju4nn6IicSnPb246CvnaibNJR37HZPcuJiblOygIoEXXWVcSD1K0V095JWThLsxibnQczlpzufzZ6gwMtpnjXJg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

**从系统能力走向典型任务**

发布现场展示了玄知V4在后量子密码、密码工程、安全多方计算、同态加密、差分隐私和区块链等方向的11项研究与工程探索。

**在后量子算法设计中**，团队借助玄知分析HQC密文压缩、错误重量与解密失败率之间的耦合关系，形成NSS-HQC候选方案。初步评估显示，该方案在给定参数与安全假设下有望降低密文传输开销，相关结论仍需进一步验证。团队还围绕多变量签名的结构暴露问题形成Origami候选方案。

**在密码工程审计中**，团队借助玄知分析openHiTLS PQCP中的PolarLAC解封装代码，发现普通`memcmp`可能带来的时序侧信道风险，并提出恒定时间比较函数替换建议。该修复面向单点比较操作，全链路时序行为仍需继续检查。

**在协议分析中，**团队以安全多方计算中的概率截断协议为例，引入白盒分析与形式化证明，对已有安全结论进行复核，形成“协议解析—白盒分析—安全证明—漏洞判定”的审计框架。

此外，V4还围绕BIKE动态阈值优化、CKKS自举协同优化、双边ABE密钥泄露检测、真实CPU环境下的时序侧信道风险，以及区块链交易排序与扩展机制等任务开展探索。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/uy0ju4nn6IicSnPb246CvnaibNJR37HZPcuJiblOygIoEXXWVcSD1K0V095JWThLsxibnQczlpzufzZ6gwMtpnjXJg/640?wx_fmt=png&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

**从模型能力走向科研生态**

V4以“**数学机理 + 高质量数据集**”双轮驱动，持续建设来源可追溯、结构规范、能够验证和迭代的密码专业数据资源。面向保密与合规场景，系统支持本地化部署与一体机形态，并持续完善API、SDK和插件开放能力。

过去一年，玄知相关工作获得openHiTLS社区特别贡献奖和第十四届中国电子信息博览会金奖。团队还在将科研项目转化为教材、实验指导书和配套课程，推动密码学、人工智能与工程实践深度融合。

**玄知大模型V4**

***让复杂任务有序推进***

***让科研结论有据可查***

密码智能的未来，不止于模型能力提升，更在于专家知识、工程工具与验证机制的协同。玄知大模型V4愿成为密码研究者和开发者可信赖的AI科研执行伙伴：

**让复杂任务有序推进**

**让科研结论有据可查**

**共同定义密码智能的未来**

**来源：NSSLab-Xidian**

[密码学大模型——玄知大模型V3.0升级](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492068&idx=1&sn=f5692b5c181bc92703a7571b82870bf0&scene=21#wechat_redirect)

[冯登国院士：面向人工智能的密码学未来发展思考](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491424&idx=1&sn=d9e91967ec7091970d84000e5fd2ccf7&scene=21#wechat_redirect)

[郑建华院士: “密码定义安全”的思考与愿景](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492206&idx=1&sn=402fe11a89c1c483c3f3b397e9fab2da&scene=21#wechat_redirect)

[王建华院士：信息技术变革对密码技术发展的思考](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492195&idx=1&sn=0e1e060e546142ea50ece9312d8c137a&scene=21#wechat_redirect)

[CCF A网络安全/软件工程顶会中的Agent安全](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492183&idx=1&sn=db7f15edd495a82b6ca8be17b4e99867&scene=21#wechat_redirect)

[2025年国家最高科学技术奖揭晓](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492174&idx=1&sn=72dcf8363725751dbdb7e04b07c887ac&scene=21#wechat_redirect)

[中国科协 | 2026重大科学问题、工程技术难题和产业技术问题](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492178&idx=1&sn=3cc7d6e128f39b8bce6b852850f0864a&scene=21#wechat_redirect)

[4月9日勘误-CCF推荐国际学术会议和期刊目录(第七版)](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492161&idx=1&sn=f0ecc60d761a803620afe3f5b99d91ba&scene=21#wechat_redirect)

[李国杰院士：基于可判定性理论的人工智能系统安全风险分类](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492073&idx=1&sn=1307cf8825ac2e8dab2388c06752e698&scene=21#wechat_redirect)

[2026年国家自然科学基金安全领域部分题目列表](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247492040&idx=1&sn=effeeb813e13f974d9622c88f9fc4deb&scene=21#wechat_redirect)

[冯登国院士：网络空间安全未来发展思考](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491433&idx=1&sn=645bb18036b15c5248ad58ec8dccbbf7&scene=21#wechat_redirect)

[USENIX Sec 2025：大模型越狱防御框架——JBShield](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491432&idx=1&sn=268c0cc1f7f3a59bd9d88c8a3ea53e7e&scene=21#wechat_redirect)

[2025年国家自然科学基金安全领域部分题目](https://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491411&idx=1&sn=56b1abaffc94f3ebf50ee7a88957ce5d&scene=21#wechat_redirect)

[NIST发布首批3项抗量子密码标准](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491348&idx=1&sn=7b716a864df153c15dd95ddf256f1374&chksm=eaa4f6f3ddd37fe5d85af81235f951d528a42dd160475af9e898a425cbb272d075933226855d&scene=21#wechat_redirect)

[IEEE：后量子密码学之路](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491341&idx=1&sn=54f9fae066a314b8ecdd46ce037621c0&chksm=eaa4f6eaddd37ffcff4629d5e5c1851b67a176e0a1665f367432aa72f8b08d075327ae5a9bc7&scene=21#wechat_redirect)

[NIST抗量子密码算法被爆安全漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247490518&idx=1&sn=4bac214c6c6e81a716c52d41f1cd6069&chksm=eaa4f231ddd37b27e4707250a16d72575726a05230fa67e42663bf644f0959374032a8ecf85a&scene=21#wechat_redirect)

[吴世忠院士：对生成式AI安全研究的九点观察](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491330&idx=1&sn=c4c90f77663ee68f77c575226c6e630b&chksm=eaa4f6e5ddd37ff30f77a1d23e19c1edc872c9ffc137438c92277cc5313efc97ad7571aecca3&scene=21#wechat_redirect)

[去中心化联邦学习：安全和隐私综述](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491279&idx=1&sn=a31c1832715905964546cc7f19a56486&chksm=eaa4f728ddd37e3e9de963a50ffa3b875066ca5a2893b532fe6be11b423208c39da804fd94b7&scene=21#wechat_redirect)

[CCS 23：利用SSH签名错误提取RSA密钥](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247491041&idx=1&sn=06c8eb75cf2ea12eba52860430218a6b&chksm=eaa4f406ddd37d102dcd0be96d40f531ce0647665f9af3dfada28a34a06ef0e80303c75f4f2f&scene=21#wechat_redirect)

[针对大语言模型LLM的对抗](http://mp.weixin.qq.com/s?__biz=MzI2NDg5NjY0OA==&mid=2247490929&idx=1&sn=e0de9cc63dd68812486688f433a4a31f&chksm=eaa4f496ddd37d80fb934f98bea6bb8bc1fbc7f74b4111e80a5973311fbfde3a18e86e58ed00&scene=21#wechat_redirect)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DNNc17Q6tdY06v6DeniaSPLvNv6To7Cxsud5WSjM7lbZZGqlhb3U32c7mUqRyjVUcPqrCQcmoEw2oXicIgg2wV2A/0?wx_fmt=png)

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