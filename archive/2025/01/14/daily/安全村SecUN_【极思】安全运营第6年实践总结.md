---
title: 【极思】安全运营第6年实践总结
url: https://mp.weixin.qq.com/s?__biz=MzkyODM5NzQwNQ==&mid=2247496429&idx=1&sn=379e57e4ac389d0afadd44e65168dfcd&chksm=c21bd3dff56c5ac935b25b0568822053fb5bed39a4db28a35ffa2ea0c7ede3755f7071dd353f&scene=58&subscene=0#rd
source: 安全村SecUN
date: 2025-01-14
fetch_date: 2025-10-06T20:11:35.520838
---

# 【极思】安全运营第6年实践总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBGOTYvyw4v9oygA3zU03hMlqTt85W0OTIaNyxJ6Gy8MkIa9h7jCU9E2Q/0?wx_fmt=jpeg)

# 【极思】安全运营第6年实践总结

安全村SecUN

以下文章来源于极思
，作者刘亦翔 Sven

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5C9zw6tOQDoPWvmvc5ibTWPB8mLD0usOr8TcibJIoZ9OVw/0)

**极思**
.

A9 Team 攻防团队创始人。某头部证券安全运营负责人。AntSRC、ASRC、JSRC的Top白帽子。

# 前言

感谢还在关注的你们，比心。跟大家说声抱歉，原计划发总结后发各模块的实践，但由于公司调整+孩子上小学+风控更严格等原因，2024年共发了2篇文件，创下近7年最少。好在质量很不错，感谢同学们捧场阅读量12K以上。今天凌晨把《安全运营全景图》第二版调整完成，为表歉意今天分享，孩子放假家人回老家才有时间写，近期有时间把之前欠的补上。

![](https://mmbiz.qpic.cn/mmbiz_jpg/hojPFbfiayfwJnw3dhPI5sUdOCYKHibqeRRNQPlueEjnW7hEMKCWKDFZ4GK4WvJ9OECcqYg2IRicvT4RYwa4KwP0w/640?wx_fmt=jpeg&from=appmsg)

# 一、安全运营整体逻辑

第一次看到此文章的同学，请移步《[【极思】五年安全运营实践总结与未来思考](https://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484966&idx=1&sn=14d39c7d3d4b9a9830e8aef79d72c1a2&scene=21#wechat_redirect)》，很多设计的逻辑在前文中已说明，本文章主要介绍变化和变化的思考。逻辑架构设计部分未调整。主要调整的是安全运营全景图。

# 二、安全运营全景图

安全运营全景图调整的原因：一是公司在文化、部门、人员方面调整，导致有些部分不再适用；二是2024年针对安全运营规划开会讨论过多次，部分逻辑和内容有变化；三是安全运营工作范围有变化，需要进行合并、增加；四是经过2024年的实践，个人的观点有变化，需要更新。调整后的安全运营全景图如：

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBGomSbL8Ut8MVCqOaibVa9JCZp6Z09QbP6hcDj3PkeplsVqBHqPPjt6EA/640?wx_fmt=png&from=appmsg)

整体的逻辑请参考上一篇文章《【极思】五年安全运营实践总结与未来思考》。本文详细介绍各个模块和调整的原因。改名安全运营全景图的原因，是希望可以通过一张图讲明白安全运营工作，让CIO、业务、研发、运维、分支等核心客户更方便、更容易的理解安全运营工作。而不是像传统的方式一样，安全规划一份、风险评估一份、运营逻辑一份、技术架构一份，如果只是讲安全运营逻辑，使用IPDRRVL即可。

## 1、安全管理

安全负责人必修，目的是向CISO讲清楚安全运营工作的逻辑和核心模块。此部分更新较大，也是2024年个人成长较大的部分。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBGmNcXXwUrjchuxibfnWQBHw9MGMcvuibZf64l1VPggBWmneYEsobT30Nw/640?wx_fmt=png&from=appmsg)

此模块的主要作用是承上启下，将需求方的需求（具体见图）翻译成CIO能轻易理解的方案。要注意的是CIO极少有安全出身，这个部分非常重要。需求子块，通过每年更新安全规划的方式，收集各个需求方的需求，优先级从上左到右，从上到下排列。规划子块，优先顺序同上，运营逻辑部分非常重要，要环环相扣，不是安全出身的领导主要看逻辑。策略子块，安全规范是安全运营执法依据公司越大越重要；例外管理，安全策略效果好的必要手段，管不好例外策略执行不可能到位；新工作自己先做，形成SOP，是自动化的基础，也是将工作交于他人执行的基础。执行子块，任务层层分解，建议使用飞书表格、任务、日程管理。评价子块，度量是眼睛，考核是驱动力，汇报是信息同步。

## 2、安全场景

运营负责人必修课，目的是向CISO、安全负责人讲清楚面临的主要问题，也是安全运营工作核心需求源。此部分更新较大，触发改动的原因是领导让我们整理应急预案，其实我们内部的运营流程很完善，思考两者区别后发现，CIO并不关心详细的运营流程，关心的是较大的安全风险场景有没有预案。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBGLH8jj461QT0CvLNzkLVibcgNhC1HiaYOblg1kWibbEqQe4riadUlPV7vCQ/640?wx_fmt=png&from=appmsg)

合规子块，分享个技巧，将各种法律法规文件收集起来，使用AI+RAG形成知识库，很好用。攻击子块，调整逻辑是只将需求方关注的高风险场景放进来，抓大放小是必修课。演练子块，没有前两个子块重要，但占用时间和精力非常多，有必要放进来。

## 3、安全能力

运营负责人必修课，目的是向CISO、安全负责人讲清楚如何做、做什么，是安全运营工作开发的核心逻辑。基于2024年的实践经验改动较大，触发点是内部攻防对抗实战演练、行业安全演练、领导说的多演多练。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBGonXD9TMYCmvJBPV9liaZH0oGpl3O63QPY68XfaDbWyURyGOd2nia0mnQ/640?wx_fmt=png&from=appmsg)

识别子块，需求管理是指安全运营工作内容每月评估增删；要持续跟进学习新风险，否则很可能被攻击了才知道，会非常的被动；漏洞情报非常重要，这是黑客知而我不知的漏洞类型，我知黑客不知的漏洞优先级可以降低。防护子块，出网阻断很好用，DNS阻断很好用。监测子块，略。响应子块，实战能力非常重要，每年两次演练的核心目的之一是响应能力，不要小看向及时汇报的影响。恢复子块，很重要只能多演练来提升。溯源子块，略。通用能力子块：策略管理、应急预案、流程指引是管理；漏洞管理主要是隐患清理；告警运营、安全事件是入侵响应；有效验证、安全运营保障安全能力稳定输出；自动化、智能化全局赋能；攻防对抗、复盘改进是持续提升。

## 4、安全工具

运营负责人必修课，这是等于军事布防图，目的是让自己心明眼亮。需要清楚有哪些系统或工具，哪些系统或工具的特长是什么，系统或工具所在位置，是否解决所在位置的问题，还有哪些位置没有防御。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBGqyFgNwr2pvRVGfW02zNZlgnic9XBlrtibc4icmedtplq0DexnESYouehQ/640?wx_fmt=png&from=appmsg)

研发子块，空间原因，还有开源软件、开源组件、供应商管理、合同要求等措施没有写。办公子块，终端上杀毒、EDR、DLP必要；网络上准入、访问控制、NDR必要；邮件上安全网关、DLP必要。生产子块，主机上容器安全、HIDS、防病毒必要；网络访问控制、NDR、漏洞扫描必要；数据安全上API安全网关、数字水印必要。公网子块，WAF、资产监测、API安全必要。通用子块，资产管理、漏洞管理、告警管理、事件管理、自动化、有效性验证、安全例外管理必要。

## 5、信息资产

运营负责人必修课，这个不用解释。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBG1sYG43uqOUde6WtZVUabd4mOwtEhQEMYG9PibvrIRz7xXgpACHsbnow/640?wx_fmt=png&from=appmsg)

# 三、安全运营未来展望

主要观点没有很大变化，详细可以参考《[【极思】五年安全运营实践总结与未来思考](https://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484966&idx=1&sn=14d39c7d3d4b9a9830e8aef79d72c1a2&scene=21#wechat_redirect)》，补充内容如下。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfwJnw3dhPI5sUdOCYKHibqeRJohmRxoqnooaevhkrXlJFPWJ55opCj9tkxSUQcZb7hb3z04zVhsvaA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

最初看到LLM时，我觉得安全运营智能化有戏了。随着LLM应用和技术爆发式发展，现在我相信LLM+RAG等技术，可以解决自动化中的痛苦，决策的问题。2024年我们在安全运营场景下，收集了20个AI应用需求，有10个完成，近期分享出来。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBG1eE9339U33jeogpibBDPpX31Uoib3DqLELeZdCicRBfkS5E009uxmPD1Q/640?wx_fmt=png&from=appmsg)

AI有它的强项，也有它的局限性。上次在行业里交流时，AI存在的几个问题，一是开源模型已经非常强大已经解决了建设的问题，二是LLM能力成长极快不再需要高成本的硬件支撑，三是通过微调和RAG可以解决一本正经的胡说问题，四是LLM写代码能力成长极快相信能解决基于安全运营场景二开的问题。未来是智能安全运营的时代！

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfzh7kBddnLvsTFjvvLbcNBG1fKlmWCaMibaPDw3WXfeaOFr1EW0rY7RGbibjhcl8FwVjSTMNf7zlk1w/640?wx_fmt=png&from=appmsg)

# 四、后期分享计划

如前方中所说，近期有时间写文章了，年终述职完成后，集中输出一下。了却之前的因果。文章中提到的《安全运营进阶实践》、《安全运营自动化实践与智能化探索》完整PPT，以及高清的安全运营全景图，如果有需要可点 在看+转发 此文章后，加我微信领取。

---

****分享最多=赠书一本+****包邮********

**在看+点赞+关注=下期不会走丢哦**

---

《安全运营和攻防实践群》

成员500+已满 入分群加微信

![](https://mmbiz.qpic.cn/mmbiz_jpg/hojPFbfiayfyMf6fHXgBIVPcBXicNIuLMY0vbXkz8HtibRCLaKeyMyrvwddCmTObdQlRKVKM6V1QiaJFmtaKAsDwWg/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzRGMuTrYpXpG6QcU1hu3hPRZuNFOWGNGYBFFTtxeiaiar1T5oJTB5Qo0TTVuCibFZtulDDvHFklutuBQ/0?wx_fmt=png)

安全村SecUN

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kvCk9Nm6FzRGMuTrYpXpG6QcU1hu3hPRZuNFOWGNGYBFFTtxeiaiar1T5oJTB5Qo0TTVuCibFZtulDDvHFklutuBQ/0?wx_fmt=png)

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