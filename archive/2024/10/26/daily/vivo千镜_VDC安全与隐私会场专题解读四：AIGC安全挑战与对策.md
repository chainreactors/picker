---
title: VDC安全与隐私会场专题解读四：AIGC安全挑战与对策
url: https://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491949&idx=1&sn=77e8b5fb0f8f8c033a63a91f0e1274d3&chksm=e9bac701decd4e170cb3cef31d751177c87795e5ef30acfffb30b78da5480a67457eea45d077&scene=58&subscene=0#rd
source: vivo千镜
date: 2024-10-26
fetch_date: 2025-10-06T18:53:29.712013
---

# VDC安全与隐私会场专题解读四：AIGC安全挑战与对策

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghdjaZg0vXhrxbwpXW7QHzqfGv9glt0e4PFRWlWYsZ4wG256EMbYxjUQ/0?wx_fmt=jpeg)

# VDC安全与隐私会场专题解读四：AIGC安全挑战与对策

vivo千镜

# AIGC的迅猛发展给我们的日常工作生活带来了一场生产力革命，vivo作为一家以用户为导向的科技公司，在积极拥抱AIGC的同时也高度重视它带来的新的安全挑战。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghI1I0WLRpRibHdfq69v5SbgvpmooYX98ic7svia2kYEEbV5hc1Fcae0dicw/640?wx_fmt=jpeg&from=appmsg)

vivo安全合规高级经理-吴佳颖

AIGC风险场景包含有由其特性衍生的数据风险和模型风险，以及由产品特性所决定内容风险和运营风险，这四类风险在系统&应用联动效应和用户多元使用需求下相互影响、相互制约，共同构成了完整的风险矩阵。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghGCBHAziaicklZ2EDlv3icib1ETI7b8D1cOiccvwia7QZO1jkIondFBUcQPFg/640?wx_fmt=png&from=appmsg)

**积极应对风险挑战，构建业务安全体系**

想要解决风险就必须要摸清风险，vivo开展治理的第一步是构建风险度量模型。通过解读、融合相关政策法规和技术指导文件，vivo内部制定了**《大模型安全风险评估基准》**，从数据安全、模型安全、内容安全、运营安全四个板块来度量大模型全生命周期的安全水位。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghj6Qs1Ls7Uhh7PJPCiad5D5eg06CSdsbuZM8JcKTRiaz8W30EvvxjD6LQ/640?wx_fmt=png&from=appmsg)

在《基准》的方法论指导下，vivo从最初的训练语料环节，到最终的产品上线环节，通过一条流水线把所有关键环节和关键角色都串联在一起，组成AIGC业务的安全架构，上下游各司其职，共同保障产品安全质量和用户体验。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghdapETHnX8ibZFd3rFX7AX6aJytYQcxhE0ticJGglJ3terq5bHWEOH8RA/640?wx_fmt=png&from=appmsg)

在安全架构的实践层面，**vivo内部通过一套流程和两个平台进行实现**。

产品安全开发流程通过将安全管控节点融入其中，从需求策划到设计开发阶段，针对风险场景做成因倒推，提出各阶段相应的安全需求，以内部的成熟规范引导、约束，严格把关各个环节的交付质量。

同时，**vivo构建了大模型管理平台**来隔离上层业务与底层大模型的直接通路，所有产品接入AIGC能力都需要通过大模型管理平台来验证其安全措施的落实程度，以此保障整个上下游的产品安全。此外，位于大模型管理平台下游的**内容安全策略平台**集成了内容审核、用户管理和策略运营模块，为AIGC产品提供统一的内容管理策略，既能守住最底线的通用标准，又能根据实际场景和用户反馈进行尺度微调。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghK28h29ttGXj19VdZHCGXA30AeYDncOgOKjgSUIntCdYBLHumakJ4nQ/640?wx_fmt=png&from=appmsg)

在内容风险方面，**vivo构建了合适的内容标签体系**，以监管层面的正常应答、红线必达、红线拒答三类要求，以及业务层面的文本、图片、音频等多模态场景的实践需求来组成整个标签体系， 共18类400多个细管控场景。

基于内容标签体系，vivo安全团队针对管控场景结合变异攻击手法**又构建了内容质量评测集**，并开展内容安全质量评估。评估从原始问题维度、绕过率维度和高级攻击手法维度，输出大模型内容安全质量评估报告，而这份报告也将成为vivo所有大模型是否准入的金标准。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghZicerN5kVicstRShRWqyrqFR60N4388V4MZLapSOBvSzxwPawwoQibqHQ/640?wx_fmt=png&from=appmsg)

**加强外部合作，共同推进大模型健康发展**

尽管针对大模型下游的内容进行了一系列管控，但大模型效果提升的原动力，始终是高标准高质量的训练语料。对此，**vivo和百度深度合作**，针对数据及数据源的不同问题进行专项处理，形成了一套**全面的训练语料清洗与质量监测体系**，对大模型训练语料进行提质纠偏。

整个处理会分为两个阶段，首先进行数据源的质量确认，当授权合法性和质量可靠性都满足管控要求后，才会进行具体的数据清洗，而在清洗过程中会不断进行质量监测，及时识别不可靠数据源，最终输出满足质量标准的训练语料。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghusCd941JUFSaUKakheNkM7iauBiad05BXpAyXwzav8SibumZH2qexyqrQ/640?wx_fmt=jpeg&from=appmsg)

百度安全技术委员会主席-包沉浮

**除了不断夯实内部能力，vivo还在行业内持续开展广泛合作。**

在信通院成立AIIA安全治理委员会构建人工智能安全评测体系的过程中，vivo积极参与各项工作并贡献了实践经验。2024年，中国信通院联合vivo等30余家单位发起大模型安全基准测试，从底线红线、社会伦理、信息泄露的角度对大语言模型、多模态大模型进行安全测试分析。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghdWqNROH9GEZdicMTvNf9W0y0Jex2LQGI2AcJCm7nCcchcgwAG1nw1lQ/640?wx_fmt=jpeg&from=appmsg)

中国信息通信研究院人工智能研究所安全部主任-石霖

**今年7月，vivo率先通过了信通院首轮AIIA大模型安全测评。**在测评中vivo以AIIA为抓手，提升了AI全链治理水平，并不断吸收经验、优化内部安全架构。

同时，vivo也不断积极推动行业标准制定，目前已牵头立项团体标准**《移动智能终端端侧大模型安全实施指南》**，将我们在端侧大模型安全实践和研究积累与行业分享，以期望与行业伙伴一起协作，共同提升端侧大模型的安全水位，助力终端AI行业的发展。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghAuHTiaoyV53r39iacmXtoeg2soOoyneOGFJKT5C0lSibE1TIderUs0L6Q/640?wx_fmt=png&from=appmsg)

vivo始终期待与更多的开发者和行业合作伙伴一起，为AI产业的蓬勃发展添砖加瓦。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC3xJXY2vb0NKf2ibibTb1aghHywwkSgCY9jhgLmEibjt4vEOxeiaafzKUoicNV28FLSOf9POe6ArF3UXg/640?wx_fmt=png&from=appmsg)

**往期推荐:**

[VDC安全与隐私会场专题解读三：AI 赋能千镜可信生态](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491925&idx=1&sn=ced0db907e22c31e933db218f3b13310&chksm=e9bac739decd4e2f0ca81bccedb4816e7d5432fc23bec1cdae3c132a1fd53a62c286091188ad&scene=21#wechat_redirect)

[VDC安全与隐私会场专题解读二：强化可信底座，护航智慧服务](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491896&idx=1&sn=0a7ce48d6ed108e27a310cd0ce4321aa&chksm=e9bac754decd4e4271467c9cd01386dee23cdb0fc6b0235d6e7711169c92586a79ab6bbbe070&scene=21#wechat_redirect)

[VDC安全与隐私会场专题解读一：全面拥抱AI，共建可信透明的安全体验](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491875&idx=1&sn=a5f857276557f1efdc1a129bc0fef24e&chksm=e9bac74fdecd4e598583be9d161a3ba0cb28315f4d2105e91ddfb4c29131d5f796a809da3d88&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/n5WtWCY9vpCbcuALBrAW9vFOibfQLzZdKgia4wWosQgojicHRTUwdy9LgKDU7EYkb3bz3TAZic9G8AO0wyPeoIuz7g/640?wx_fmt=gif)

关注我们，了解更多安全内容！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBBxdAlANBjBJZOL2oErJCOrXT8ALOWuVXanAVXQxRqdvg7picyvoOZkCvpmNLBmvEyKhPTkPBJREA/0?wx_fmt=png)

vivo千镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpBBxdAlANBjBJZOL2oErJCOrXT8ALOWuVXanAVXQxRqdvg7picyvoOZkCvpmNLBmvEyKhPTkPBJREA/0?wx_fmt=png)

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