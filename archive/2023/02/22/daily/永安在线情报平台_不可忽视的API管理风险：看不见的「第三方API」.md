---
title: 不可忽视的API管理风险：看不见的「第三方API」
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247495525&idx=1&sn=92cb01a5d69166f5a8731aceddc24b35&chksm=eb12c95edc654048d3a08907d06b592f9be16dda6dac8f4b5ebf1885d1ceac7188087b433138&scene=58&subscene=0#rd
source: 永安在线情报平台
date: 2023-02-22
fetch_date: 2025-10-04T07:43:54.148543
---

# 不可忽视的API管理风险：看不见的「第三方API」

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4mAgZtBianqGWiaWPiclQhmqwxxpSZfNxXjLRDhELmR27LDP6ibXCibv4aP52KCSBmyMZo4xib80fT8FrVgIoWmpCMZQ/0?wx_fmt=jpeg)

# 不可忽视的API管理风险：看不见的「第三方API」

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/mmbiz_gif/4mAgZtBianqEAMZCKOk2hWqCfyHibLZbpsRxZEjfRuFptuU3ZwV5d1VLMglrldNwCwo76cJHqbfq08Vr7Y82zOZg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

数字转型计划、云迁移项目等持续深化，

API快速迭代，使用数量大幅上升，

API成为更多企业访问数据/服务的接口，

也成为了众多黑产团伙攻击的“靶心”。

许多企业开始重点关注，如何基于API全生命周期实施合理的安全策略，API资产管理与防护往往始于**“可见”**，企业难以掌控那些难以被发现、看不见摸不着的API安全状况，**例如第三方API**。

第三方API通常由外部人员开发编写并引入内部组织，往往运行在不可见的技术平台和基础设施中。大部分第三方API由于缺乏“可见性”，**难以被统一管理、监督**，给企业带来无法量化的风险。

**2022年6月**，威胁猎人情报平台监测到某客户系统内存在**第三方编辑器**的安全隐患。

攻击者利用第三方编辑器漏洞获取到系统服务器操作权限，对客户系统进行内部横向探测。经排查发现，攻击者利用第三方编辑器的**“文件上传”漏洞**成功上传了Webshell恶意脚本，并将其开放在互联网，大大增加了风险暴露面。

通常，第三方API是以何种形式进入企业内部，又是如何扩展其潜在攻击面的？

**第三方API进入企业内部的主要渠道**

据威胁猎人情报实验室研究调查，第三方API进入企业内部的主要渠道包括以下几种：

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGWiaWPiclQhmqwxxpSZfNxXj0vlqmWrWdO8RF3KD393vh4f7nFPyr3Z6BUnXcTDDll8fqRGcoHia2ww/640?wx_fmt=png)

不少企业内部业务依赖大量的第三方API，**第三方API来源渠道较多、涉及功能广泛**，且大部分分散在多个系统或技术平台，常常处于企业正常业务及API管控之外。

企业不仅要面对愈加复杂、隐蔽的新型攻击，还要在人员、资源有限的情况下应对高强度安全运营工作。

**如何避免第三方API的“潜在风险”**，在冗杂繁重的API资产梳理中做到“疏密有致”？

**实现第三方API“可视”的关键要素**

为帮助企业清晰了解第三方API具体位置、相关属性，以及与它们交互的数据类型，**将第三方API纳入自动化的API资产管理**，成为实现第三方API“可视”的关键：

***1.*****全自动无效流量过滤，快速摸清真实资产**

攻击者常常会对企业API暴露面发起扫描攻击，这个过程会产生**大量的扫描攻击流量**，导致无效API资产过滤不彻底，不仅难以摸清真实资产、影响风险的识别处理，还会大大增加运营成本。

威胁猎人API安全管控平台内置资产梳理模块，通过**“API提取模型”**从海量未知流量中准确识别并筛除扫描流量，还能快速识别并排除非正常流量（如：请求404，502等非正常响应）对于资产识别的干扰，确保资产梳理全面有效。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGWiaWPiclQhmqwxxpSZfNxXjGaPD9wJHIQ560J5Mc2rfdt5Tws2yBfpBhnbm622rAVGlfbfvMhuvOg/640?wx_fmt=png)

***2.*****合理规约及拆分，精准管理API资产**

API资产的识别过程中还会面临**“合理规约及拆分”**问题，每一个应用背后有着不同的开发团队、不一样的开发语言及程序框架，因此API资产的识别就具备了多样性的特征。

API 资产中，存在众多参数变量类似、路径高度重合的API端点，如不进行合理的规约，将产生**庞大的同属性资产**和海量冗余数据；而对于诸多接口类型参数化的API端点，如未进行API资产的合理拆分，则会导致**API安全特征模糊**，难以实现安全管理的细粒度。

合理规约及拆分的缺失使得针对GraphQL、Dubbo、phalapi等主流API协议的资产梳理更加难以实现。

威胁猎人安全管控平台API资产识别引擎，基于图模型专利技术以及每日数亿的情报数据能力，支持**Restful、GraphQL、Soap、Dubbo、Xml-RPC、Json-RPC、phalapi**等多种主流API协议的资产梳理，从整体上提高API资产管理精准度。

***3.*****应用资产分级分类，高效识别第三方系统/组件**

第三方系统和组件存在0day漏洞等高危缺陷的情况并不少见，基于业务流量特征自动化梳理API及API上流动的敏感数据，对应用资产进行分级分类，可以帮助客户对第三方组件进行**持续、自动化特征识别**，清晰了解第三方组件具体属性（如：网络属性、场景属性等）及部署位置，更好地应对第三方系统和组件的API风险。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGWiaWPiclQhmqwxxpSZfNxXjEGSicXiaQYmEV6ibEb2lKA4FTwAfhy83QLJUva85ZPhCarpcORLw80sUw/640?wx_fmt=png)

威胁猎人API安全管控平台资产梳理模块，通过对应用资产进行自动化分级分类，确保数据资产持续更新和可见，支持**SpringBoot Acuator、XXL-JOB、Web应用、ERP、客服系统等170余种**常用组件的识别，还能及时对组件关联API进行有效梳理。

**API资产管理是API安全防护的第一要务。**基于流量对已上线的API及API上流动数据资产进行整体梳理，实现对所有API资产及流动敏感数据的可视，再基于情报进行持续的API缺陷评估及攻击威胁感知，可以更好地帮助企业解决**第三方API安全“可见性”问题并做到API安全整体可控**，为企业数字化建设打造坚实的安全底座。

2023年1月5日，永安在线进行品牌焕新，正式更名为**“威胁猎人”**（详见：[成立6周年，威胁猎人焕新回归](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247495229&idx=1&sn=08d55c289fd0fc700a5da2d57c361ce6&chksm=eb12c806dc654110208d965813d11524f5ccad88633401518208d21c52aeaf1822a66ade2f64&scene=21#wechat_redirect)）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

威胁猎人Threat Hunter

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

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