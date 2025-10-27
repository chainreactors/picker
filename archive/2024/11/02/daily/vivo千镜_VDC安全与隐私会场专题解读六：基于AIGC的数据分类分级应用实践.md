---
title: VDC安全与隐私会场专题解读六：基于AIGC的数据分类分级应用实践
url: https://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247492009&idx=1&sn=a95b8cab32185dcdd2a52b4926211a28&chksm=e9bac7c5decd4ed388feddbb9b6b7cf1c91ad6ee777a93dc80ed1b420455627728478528cef4&scene=58&subscene=0#rd
source: vivo千镜
date: 2024-11-02
fetch_date: 2025-10-06T19:17:39.479184
---

# VDC安全与隐私会场专题解读六：基于AIGC的数据分类分级应用实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibtpaZgrdNI1ic2Cx3kfbHMfahoO2hSx89XpuzkFuvdyzEKbaqmniaIMicQ/0?wx_fmt=jpeg)

# VDC安全与隐私会场专题解读六：基于AIGC的数据分类分级应用实践

vivo千镜

#

# 随着人类社会从农业到工业再到当今数字经济的不断发展，以及大数据、 云计算、 AI等技术的日新月异，数据已经成为经济发展的新型生产要素，保障用户数据安全也成为安全行业中重要的研究课题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibswoNLOsgJNicQR5eRujv3QD4ZpamEkAuUibdhOWJxNsdIgcDvvibDj6WQ/640?wx_fmt=jpeg&from=appmsg)

vivo安全工程师-曾志均

**数据分类分级治理**

数据安全不仅仅是单一的管理命题，而是一个需要体系化的治理工程。目前行业内常见的两种治理理论分别是DSMM 框架和数据安全治理（DSG）框架，不管哪种框架， 数据分类分级都是其中极为重要的一环。只有对数据进行了分类分级，建立了清晰的数据资产台账，才能为后续数据安全制定正确的治理策略、 精细化数据安全分类管控打下坚实的基础。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibpbX2VCUIQ3FIXjjCRsryXsibtBicq8eibQf3nkJWHicI0FnJwnmhPoUphQ/640?wx_fmt=jpeg&from=appmsg)

因此，vivo参考行业标准，建立了数据分类分级流程。在资产梳理阶段，vivo基于现有统一的两大数据中台，对数据资产进行了全面、 准确的梳理；并且制定了**《vivo 用户数据分类分级规范》** ，指导后续分类分级工作的开展；同时在实施数据分类分级阶段，**vivo积极探索与实践AIGC在数据识别领域的应用，自研数据识别能力**，助力海量数据分类分级落地。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibwHAv6iaStPxo7rrUBNahF3o0c7xncdt9VcCNdzEOBBdYics2vFuoqKpw/640?wx_fmt=jpeg&from=appmsg)

**数据识别技术探索实践**

**vivo的数据识别能力建设分为传统和智能化两个阶段。**在传统阶段，数据识别系统包含**2个核心服务**，**数据接入服务和数据识别服务**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibRkXP2iaKVFFntmdxAJDrqRer6xjzxods2Vs05aL7r2p3ASp8G7HNYBQ/640?wx_fmt=jpeg&from=appmsg)

数据接入服务负责从数据中台同步各类数据库的元数据等信息，并完成对多源、 异构数据的预处理；数据识别服务基于系统内置或业务自定义的规则来识别分类。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibgtUQbHZaSBLicibcRyOkoYsPJ76rCiaNgiacteiaGwntH97PSNx91JdykUw/640?wx_fmt=jpeg&from=appmsg)

传统数据识别服务的核心在于怎么计算敏感度分数，此阶段需要人工梳理数据特征，并为每种特征设置一定的分数，比如：字段名包含name关键字、内容长度在2-5、以百家姓开头等特征分别设置一定分数，然后综合考虑权重和样本数，最终得出该字段的敏感度得分。理论上， 经过该模型计算， 分数越高，该字段属于某一分类的置信度也越高。

在这一阶段， **vivo实现了自动识别常见分类30类，支持全量、 增量等多种识别模式，成功落地到MySQL、 Hive等结构化数据库的分类分级。**

但传统数据识别能力有三大缺点，一是人工维护规则成本高， 维护工作量较大；二是弱特征分类准确率较低，比如上面的两个字段，字段名都包含name，而且都以姓氏开头，完全命中我们梳理出的规则集，但是实际的分类却不是姓名。三是无语义理解能力，难以支持非结构化数据识别，极大的限制了识别能力的可落地场景。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibqyOU72R0af9mCI4oibiaJBLxenWRD9lb9mAqXaO2NEGjYHdWdzqcwNHg/640?wx_fmt=jpeg&from=appmsg)

为了解决传统识别技术的短板，vivo拥抱AI技术，积极探索大模型在数据识别领域的能力。经过预研，重点关注到大模型的4个特点：

* ****模型可适应性强：****大模型可通过提示词工程适应各种场景，并可针对垂直领域进行微调；
* ****识别效果有提升：****相较于传统识别技术，大模型识别效果在准确率和召回率等方面有更好表现；
* ****语义理解能力强：****大模型具有强大的语义理解能力，能支持非结构化、长文本的数据识别；
* ****数据抽取能力强：****能提取出指定分类数据，稳定输出结构化格式，完成非结构化数据到结构化数据转换。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibthuA736zCfbl7dicyo7OJGWzdZL5uaiaeXEhmbmic8XYJNl750z65B10w/640?wx_fmt=jpeg&from=appmsg)

基于蓝心大模型上述惊艳的表现，**vivo迭代升级了数据识别能力**，在原来规则识别引擎之上又建设了大模型识别引擎，**双引擎驱动分类分级自动化、 智能化**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibRdIial8SVHseT9Bs172nqh0mWIRo6EwaicSNTItFiaZJcYG5j33l5m7gg/640?wx_fmt=jpeg&from=appmsg)

采用双引擎的原因是在实践过程中，vivo发现大模型和规则识别引擎可以优势互补，比如大模型擅长语义理解却有大模型幻觉问题，可能随意捏造一些数据来输出，影响识别准确率，而配合传统的规则识别引擎可以对识别结果进一步校验以规避该问题。再比如， 针对有特定名单或者算法的分类，通过规则识别引擎更具优势。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibFQJiaibu623SicTqEmZOFpUwwz5dZIkEtgasQsRs9YMH2e8uSPm0MpOow/640?wx_fmt=jpeg&from=appmsg)

另外，在引入大模型能力时，需注意大模型成本和性能特点，面对这种海量数据场景，不能对全量数据进行扫描，而需要将量级控制在一定范围内，以达到提升处理效率的同时降低处理成本，比如每天千亿行应用日志的场景，按照多维度聚合等预处理后，将量级控制在千万级。

至此， 乘着AIGC的东风，vivo数据识别能力实现了双引擎驱动，共同构建数据分类分级系统的一体化、自动化和智能化，极大提高数据分类分级的效率。

**数据分类分级应用**

基于数据分类分级的成果，**vivo进一步摸清敏感数据资产分布，并结合数据血缘信息绘制出数据资产链路**。在此基础上，与数据脱敏、 存储加密、数据水印等安全能力协同联动，落地到各个业务场景，实现了联防联控，践行了集中式安全策略管理，分布式安全管控的治理思路。

![](https://mmbiz.qpic.cn/mmbiz_jpg/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibjiajiaT4JtzbzmjPibgcys0Pe7m0YX1E5Knjfxicia6R83zxKft9JIdgiamw/640?wx_fmt=jpeg&from=appmsg)

**数据识别能力未来规划**

未来，vivo会持续投入数据识别能力的建设， 不断提升大模型识别引擎能力，增加数据识别种类；密切关注多模态大模型的发展，根据其能力，在合适的时机引入多模态大模型能力，以期更智能的支持更多的文件类型；同时，持续提升识别准确率和召回率，打造分类分级智能体，积极探索大模型在更多安全领域的应用，赋能更多业务场景，为用户的数据安全保驾护航，持续提高vivo用户的安全体验。

![](https://mmbiz.qpic.cn/mmbiz_png/n5WtWCY9vpC1g7CkVpwzg6RVSWNOJqoibbw1c1jDl7ORSvibYYGQsn4CdbDhGklopgicyV9U0dhu7frWHv2ibFu7WA/640?wx_fmt=png&from=appmsg)

**往期推荐:**

[VDC安全与隐私会场专题解读五：AIGC新技术下安全工具的探索实践](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491965&idx=1&sn=6b23de288bd0380a35e9dcf8b3b0a1e7&chksm=e9bac711decd4e073be4f80f7bf5811e9960eba99c2e6f8a4ea789a63494e203e46a2b6303c0&scene=21#wechat_redirect)

[VDC安全与隐私会场专题解读四：AIGC安全挑战与对策](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491949&idx=1&sn=77e8b5fb0f8f8c033a63a91f0e1274d3&chksm=e9bac701decd4e170cb3cef31d751177c87795e5ef30acfffb30b78da5480a67457eea45d077&scene=21#wechat_redirect)

[VDC安全与隐私会场专题解读三：AI 赋能千镜可信生态](http://mp.weixin.qq.com/s?__biz=MzI0Njg4NzE3MQ==&mid=2247491925&idx=1&sn=ced0db907e22c31e933db218f3b13310&chksm=e9bac739decd4e2f0ca81bccedb4816e7d5432fc23bec1cdae3c132a1fd53a62c286091188ad&scene=21#wechat_redirect)

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