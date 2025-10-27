---
title: BinaryAI全新代码匹配模型BAI-2.0上线，“大模型”时代的安全实践
url: https://www.anquanke.com/post/id/286194
source: 安全客-有思想的安全新媒体
date: 2023-02-10
fetch_date: 2025-10-04T06:12:11.147183
---

# BinaryAI全新代码匹配模型BAI-2.0上线，“大模型”时代的安全实践

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# BinaryAI全新代码匹配模型BAI-2.0上线，“大模型”时代的安全实践

阅读量**220774**

发布时间 : 2023-02-09 10:00:24

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

Digital binary code backdrop

科恩实验室在2021年8月首次发布二进制安全智能分析平台—[BinaryAI](https://www.binaryai.net)，BinaryAI可精准高效识别二进制文件的第三方组件及其版本号，旨在推动SCA（Software Composition Analysis，软件成分分析）技术在**DevSecOps、威胁情报、安全研究**等应用场景发展。
BinaryAI本次发布产品重要更新，配备创新的算法模型和持续扩展的后台数据。科恩代码匹配模型BAI-2.0和配套算法引擎彻底革新了SCA的表现，配合业界领先的数据集和种种精彩新功能，BinaryAI实现了分析准确性及效率的大幅提升。

## 关于BinaryAI

[BinaryAI](https://www.binaryai.net)对上传文件进行自动化解包、解析后，基于自研SCA算法和后台GitHub全量C/C++库的开源组件数据集，对其进行软件成分分析、函数相似性检索，以业界领先的识别准确率匹配到文件所使用的开源组件，辅助用户完成软件成分分析和恶意软件分析的安全分析工作。BinaryAI算法引擎背后是各种AI算法和经典算法，其中核心的代码匹配模型在行业内具备显著优势。
科恩实验室持续深耕智能软件安全分析研究，联合多所高校和科研院所，在信息安全、软件工程和人工智能领域的多个顶级会议上发表十余篇文章。基于科恩智能软件安全分析的研究沉淀，BinaryAI不断提升其准确分析能力。

## BinaryAI更新亮点

### 后端模型重磅升级

科恩代码匹配模型上线BAI-2.0，顺应了AI模型开发领域向大模型演进的趋势。大模型的出现不仅促进了技术的迭代，还衍生出一批备受关注的大模型应用，如AIGC图像生成应用、ChatGPT工具等。作为领域内的先行者，科恩通过在软件成分分析领域落地应用大模型，适配了该领域的细分场景，提升了BinaryAI的召回效果。

### 准确率步步攀升

BinaryAI基于科恩自研的代码匹配模型BAI-2.0和复杂图的程序分析算法，对可执行文件中的二进制函数使用图算法分析，同时与AI算法相辅相成，在GitHub全量C/C++库中找到匹配的源代码函数。经过多次迭代，BinaryAI的算法引擎提升了算法的准确率，降低了误报，较上个版本更上一台阶。

### 亿级函数数据集持续拓展

BinaryAI已经支持全网主流开源C/C++语言项目，采集了数万代码仓库的百万级版本分支，累计百亿C/C++源代码文件特征数据，去重后包含亿级函数特征。数据能力和算法引擎使得BinaryAI的SCA能够准确定位二进制文件所使用的的开源项目的具体版本，满足查看软件成分清单的需求。数据集已经拓宽对其他开发语言的支持，共计三百多万个代码仓库，未来将支持BinaryAI在其他开发语言、应用场景发挥其成分分析能力。
往期回顾：[BinaryAI功能更新布告｜构建全量开源项目数据集](https://mp.weixin.qq.com/s/M_FbnsD1GjVtEEhVYu2W3w)

### 倾听用户之声

为改善过去BinaryAI提供的插件在客户端上网络请求结果慢、交互体验不佳的问题，BinaryAI在网页平台上新增“BinaryAI函数相似性检索”导出能力，用户可以在平台上传二进制文件并浏览分析结果后，下载结果导入到IDA或Ghidra等二进制分析软件中，继续安全分析工作，这一优化将大幅提升深度分析二进制文件场景的用户体验。
此外，平台增加科恩自研腾讯云二进制软件成分分析产品—BSCA的跳转入口，用户可一键跳转体验漏洞扫描、License审计等特有功能，适用于DevSecOps 制品扫描、软件上线前安全风险识别、检查上下游供应链安全问题等应用场景。

## 最新功能特性展示

点击**“BinaryAI函数相似性检索”**，即可下载结果Json文件，获得插件的GitHub下载链接。

![最新功能展示]( "最新功能展示")

**典型文件示例**：

软件成分分析和函数识别：[示例1](https://www.binaryai.cn/analysis/bbe34331e5068d7dc5b990fbef10002358b4ef8e07ab92c0d5620ed60fc36b30)、[示例2](https://www.binaryai.cn/analysis/914df307b6b9fde62771b20f8d5c6d1fc7fd8d15117cb99cc8bb0a89f9ddca83)

威胁情报（C2样本检测）：[示例3](https://www.binaryai.cn/analysis/289616b59a145e2033baddb8a8a9b5a8fb01bdbba1b8cf9acadcdd92e6cc0562)

威胁情报（挖矿样本检测）：[示例4](https://www.binaryai.cn/analysis/33ead107e7a01e9eb3432baebe14172ae6fe94ce62f41afad9f884e7c9b5dfe7)

### 演示视频

**[最新功能特性演示视频](https://www.bilibili.com/video/BV1CA41167CS/?vd_source=acf29aa086cce1034873d576e87e6adf)**

## 更多业务体验

BinaryAI的算法引擎核心能力已同步落地应用于腾讯安全多款产品：

* **腾讯云二进制软件成分分析**: [BSCA](https://cloud.tencent.com/product/bsca)包月免费活动进行中
* **腾讯威胁情报 TIX**: [TIX](https://tix.qq.com/)
* **腾讯主机安全云镜**: [腾讯主机安全（云镜）兵器库：斩杀挖矿木马的利剑-BinaryAI引擎](https://mp.weixin.qq.com/s/9dwUVyI34fi5lEPCDZJz_Q)

除此之外，科恩实验室始终以积极的姿态探索软件安全领域和前沿AI结合的科研落地，推动成果转化以解决产业痛点问题。

## 加入用户群

微信扫码或搜索并添加“keenlab”为好友，发送“BinaryAI交流群”获得入群链接

![]()

## 了解更多

[[1]腾讯安全科恩实验室推出首款免费在线SCA平台：BinaryAI](https://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247496102&idx=1&sn=7835a7682a921a324d1a1e65a23a9c2d&chksm=fbfecda3cc8944b5a620e57ab9b32272f629bd31c3ecdf56ecbdc66e52ae39eb537dd49182c1&token=1542731443&lang=zh_CN#rd)

[[2]BinaryAI功能更新布告｜构建全量开源项目数据集](https://mp.weixin.qq.com/s/M_FbnsD1GjVtEEhVYu2W3w)

[[3]科恩实验室最新NeurIPS-2020论文解读：基于跨模态检索的二进制代码-源代码匹配](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247484584&idx=1&sn=91a433c6db537caaf0929b447c0860a0&chksm=fbfd38adcc8ab1bb489d26a780413b2e26f49b08b971169017a6f37c7ed351e3cc090aad0dc9&scene=21#wechat_redirect)

[[4]AAAI-20论文解读：基于图神经网络的二进制代码分析](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247484184&idx=1&sn=f647cbb5c23e1f90dd7f7918146dc016&chksm=fbfd3f1dcc8ab60b1c966146191c8f216b7f62b98d8452bfa7b2595dde45d97cffda2133aaaf&scene=21#wechat_redirect)

[[5]腾讯安全科恩实验室二进制安全最新成果入选AAAI-20](http://mp.weixin.qq.com/s?__biz=MzU1MjgwNzc4Ng==&mid=2247484178&idx=1&sn=e58f1623c5a44906356da3ddf9b6a5ba&chksm=fbfd3f17cc8ab6010637d28ffa5f9a4766885c1ad4ec97f503962765b8808d79d80440e7e7a7&scene=21#wechat_redirect)

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**腾讯安全科恩实验室**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/286194](/post/id/286194)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [软件成分分析](/tag/%E8%BD%AF%E4%BB%B6%E6%88%90%E5%88%86%E5%88%86%E6%9E%90)

**+1**0赞

收藏

![](https://p1.ssl.qhimg.com/t01764fce044df00625.png)腾讯安全科恩实验室

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p1.ssl.qhimg.com/t013ac3cf51fd0e3967.png)

[![](https://p1.ssl.qhimg.com/t01764fce044df00625.png)](/member.html?memberId=136069)

[腾讯安全科恩实验室](/member.html?memberId=136069)

腾讯安全科恩实验室是腾讯集团旗下一支国际一流的信息安全团队，在桌面端安全、移动终端安全等领域技术实力和研究成果达到国际领先水平，在智能网联汽车信息安全、IoT 安全、云计算和虚拟化技术安全等领域也取得丰硕的成果，并积极布局如人工智能算法、机器学习、区块链技术等领域的安全研究能力。

* 文章
* **10**

* 粉丝
* **14**

### TA的文章

* ##### [BinaryAI全新代码匹配模型BAI-2.0上线，“大模型”时代的安全实践](/post/id/286194)

  2023-02-09 10:00:24
* ##### [源海拾贝｜科恩二进制文件自动化静态漏洞检测工具正式开源](/post/id/272334)

  2022-04-21 12:00:33
* ##### [Black Hat USA 2021议题解读｜基带利用：远程5G智能手机代码执行](/post/id/249615)

  2021-08-11 12:00:08
* ##### [NeurIPS-2020论文解读：基于跨模态检索的二进制代码-源代码匹配](/post/id/221510)

  2020-11-03 16:30:39
* ##### [招聘 | 腾讯科恩实验室招聘web安全](/post/id/197391)

  2020-01-19 17:30:25

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [广汽集团×火山引擎：出海合规助力企业新增长](/post/id/311498)

  2025-08-26 10:17:09
* ##### [从技术到安全：中科固源拆解车载以太网的演进路径与防护策略](/post/id/310094)

  2025-08-21 21:48:41
* ##### [智能体防御 | 一文了解3种系统提示词加固方法](/post/id/311279)

  2025-08-18 16:34:50

### 热门推荐

文章目录

* [关于BinaryAI](#h2-0)
* [BinaryAI更新亮点](#h2-1)
  + [后端模型重磅升级](#h3-2)
  + [准确率步步攀升](#h3-3)
  + [亿级函数数据集持续拓展](#h3-4)
  + [倾听用户之声](#h3-5)
* [最新功能特性展示](#h2-6)
  + [演示视频](#h3-7)
* [更多业务体验](#h2-8)
* [加入用户群](#h2-9)
* [了解更多](#h2-10)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)