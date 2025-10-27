---
title: 案例实践 | 智慧医疗行业API安全解决方案
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496648&idx=1&sn=8545b0d3dfc6557620d77c819aae9489&chksm=c0075e54f770d742bca8f796ba638011d6979909c19b77dd5ef0f689d380fc88018cb9fe39b7&scene=58&subscene=0#rd
source: 星阑科技
date: 2022-12-13
fetch_date: 2025-10-04T01:20:17.601872
---

# 案例实践 | 智慧医疗行业API安全解决方案

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2GM5E19Qhj2DbWwK6TfsbLNDDdjpeiaTNRb0sn1KxYK6ToAlOkObRqicw/0?wx_fmt=jpeg)

# 案例实践 | 智慧医疗行业API安全解决方案

星阑科技

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif)

随着智慧医疗快速发展，网上挂号、在线问诊、电子病历、AI影像等移动医疗为我们带来了诸多便利，沉淀了大量敏感数据的同时，也加剧了医疗数据泄漏风险。尤其是新冠疫情暴发以来，国家对全面健康医疗的重视，进一步促进了新业态的发展，医疗数据逐步实现互联互通，数据的流动性也得到了空前的提高，同时医疗机构也在面临着严峻的网络安全挑战。

**背景介绍**

随着技术进步，实现更加智慧的健康医疗管理成为社会和研究的热点，尤其是智慧医疗和健康管理。尤其是近两年的新冠肺炎疫情，让医疗科普本身从窄众内容成为高频需求。为了更好地解决疫情防控常态化时期，用户对于健康资讯和服务细粒度的需求，很多互联网大厂推出内容开放计划，叠加AI、数字化工具相关能力，协同生态的力量，为用户提供更多的场景延展空间，提升公众健康管理水平。

医疗系统对API依赖性高， 院内业务、监管单位、医保支付等互联互通；医联体、医共体、远程医疗等区域协同；互联网医院、第三方支付、微信小程序和公众号移动类应用的使用都离不开API。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2EqiaHbzgzicHQU838GgTh4GIsDaDo3XTUp3VxADzCDQ8sJr2BtgWMyxg/640?wx_fmt=png)

**需求场景**

**0****1**

**API接口资产理不清**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2XuHHTwUrvPWiaPOJNKxaIAtibtrZhONzYIf2Ycg0muRr6EC2Wd20r8OQ/640?wx_fmt=png)

在API接口安全治理实践中首先面对的就是要知道治理对象“是谁”“有多少”的问题，由于医疗机构业务系统及API接口资产的数量多而且增长快，导致很多医院都不清楚自己拥有多少个API接口，以及API接口处于什么样的状态。在API接口安全治理初期遇到业务系统归属部门多，与外部对接错综复杂，导致API接口资产梳理极其困难,安全责任无法划分实施，不能有效的对API接口资产的生命安全周期进行管理。

**0****2**

**API敏感数据暴露风险无感知**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2XuHHTwUrvPWiaPOJNKxaIAtibtrZhONzYIf2Ycg0muRr6EC2Wd20r8OQ/640?wx_fmt=png)

智慧医院必然拥有着数量众多的在线业务系统，而在实际的业务系统中，API接口是承载各种高价值服务和敏感数据的重要途径。有些API接口的流量虽然很低，却是业务的核心部分，并且这些类型的API接口很可能携带着敏感数据，但是相关从业人员却不能及时有效的监测API接口数据传输过程中的安全风险，不清楚业务系统API接口是否应该携带这些敏感数据，其数据处理方式是否合法以及涉敏数据是否被恶意使用。

**0****3**

**API接口安全暴露面广，被攻击风险大**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2XuHHTwUrvPWiaPOJNKxaIAtibtrZhONzYIf2Ycg0muRr6EC2Wd20r8OQ/640?wx_fmt=png)

随着医疗行业云化的不断推进，医疗机构API接口需要整合大量系统来实现业务彼此之间的交互，越来越多的个人数据以及敏感数据将存储在云上、使用在云上，根据智慧医院建设标准，需要实现互联互通，这也意味着更多的API接口数据将暴露到互联网中，相对于传统数据中心的单点调用，东西向和南北向都可能成为API接口的攻击面。另外，研发人员常常会因为测试需要、启用第三方开发人员访问以及为合作伙伴演示等不经意原因向外部公开API接口信息，其中不安全的API接口会持续扩大应用程序攻击面，让黑客更容易进行侦察、收集配置信息以及策划网络攻击。

**04**

**传统安全防御部分失效**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2XuHHTwUrvPWiaPOJNKxaIAtibtrZhONzYIf2Ycg0muRr6EC2Wd20r8OQ/640?wx_fmt=png)

回过头来我们再看传统意义上安全工具，如传统防火墙以及Web应用防火墙 （WAF）均缺乏针对API接口脆弱性的有效治理方法，目前不能完全对业务系统API接口风险进行准确感知和防御。传统安全防御工具实现方式是基于已知特征和规则进行风险审计，在这种技术路径下的缺陷在于行为特征规则越复杂，规则的可依赖性就越低。由于业务的不确定性和持续迭代特点，会让行为特征本身的可依赖性降低，这使得无法直接判定风险，且会产生较高的误判率。

**方案实现**

传统的网络安全建设方案难以解决API安全问题。一方面，传统基于TCP及HTTP协议的流量审计方案无法适应复杂的API通信协议以及API差异化的攻击特征；另一方面，在南北向网络或者终端单点构建防护体系，无法适应API无处不在的复杂业务架构，基于割裂的安全防御所产生的API数据也将成为一座座安全孤岛，难以协同共享，导致碎片化的安全认知，只能看见碎片化的局部安全，无法形成统一的整体可视。

因此，星阑科技推出**萤火API安全分析平台**，萤火API安全分析平台具备大数据技术和智能分析的API威胁检测能力,通过**萤火API安全分析平台**协助智慧医疗行业安全决策者建立以下API安全管理目标：

**01**

**持续准确梳理API资产**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2XuHHTwUrvPWiaPOJNKxaIAtibtrZhONzYIf2Ycg0muRr6EC2Wd20r8OQ/640?wx_fmt=png)

API安全体系建设的第一步是实现全面完整的API资产识别与梳理。API安全分析平台从不同流量探针中提取API通信数据，通过解码与智能URL聚合算法，持续计算出同一API的参数结构树，并对接下来的URL流量进行聚合，实时精准的将数以亿计的访问流量聚合出数百或数千个API资产，帮助企业持续准确梳理API资产。

**02**

**全面实时的风险监测体系**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2XuHHTwUrvPWiaPOJNKxaIAtibtrZhONzYIf2Ycg0muRr6EC2Wd20r8OQ/640?wx_fmt=png)

要做到API资产统一威胁管控，必须需要具备多维度的监测、分析体系。API安全分析平台从脆弱性、外部攻击、内部异常进行三大维度的安全实时监测能力构建，来达成全面的检测体系。

**03**

**易运营的告警处置**

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2XuHHTwUrvPWiaPOJNKxaIAtibtrZhONzYIf2Ycg0muRr6EC2Wd20r8OQ/640?wx_fmt=png)

为固化工作流程，简化运维，萤火API安全分析平台构建了一套基于“事前风险收敛、事中检测响应、事后溯源调查”的安全运营逻辑链。在日常工作中，运维人员通过固化的运维流程即可不断推进企业API安全的持续建设。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2apLsMr9EbDoBRWtjhSdziaSFzmN0x32QsfQic5prpecXpQA6h1HODAZQ/640?wx_fmt=png)

**客户反馈**

星阑科技创新推出API安全产品和防护方案，通过API资产梳理、API威胁监测、API数据流动监测三个维度，通过托管服务的方式，为云用户提供了全方位API安全防护能力。除了API数据安全情况排查之外，在API安全评估与治理过程中可以建立安全特征库与业务规则库，对应用接口进行安全态势监测，同时对在线业务与即将上线业务进行风险评估，基于网络资产指纹在自身的设备漏洞库中寻找相匹配的漏洞。

星阑科技赋能智慧医疗统一监控管理，确保多租户数据共享效率智能大数据湖，释放医疗数据价值人工智能影像分析，提高突发、广发疾病检查效率。除了第一时间补充互联网上爆发的漏洞信息外，还包含了大量医院内部安全人员发现的漏洞信息，例如大量的接口暴露、组件漏洞、其他漏洞等各类型的漏洞，包括文件读取、信息泄漏、远程代码执行等。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2uGbcGGuEiaC5QLURvc8dfQWAPPogeQx5MA1CRVAicZtA6Kn4OUs83O2w/640?wx_fmt=png)

星阑科技专注API数据安全治理，深耕网络安全领域，通过技术助力医疗行业数字化安全发展，为智慧医疗发展筑牢安全堡垒。

**关于星阑**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOejz8q9DUvIe49hEIXgia3vT2TQmAf9XBbXVN0Ww5cqhCviaia7uib1NlHfNPrichuav3Xnww4WWZoztHKg/640?wx_fmt=gif)

星阑科技基于AI深度感知和强大的自适应机器学习技术，帮助用户迅速发现并解决面临的安全风险和外部威胁，并凭借持续的创新理念和以实战攻防为核心的安全能力，发展成为国内人工智能、信息安全领域的双料科技公司。为解决API安全问题，公司从攻防能力、大数据分析能力及云原生技术体系出发，提供全景化API识别、API高级威胁检测、复杂行为分析等能力，构建API Runtime Protection体系。

**星阑科技产品——萤火 (API Intelligence) 拥有不同应用场景的解决方案**，适配服务器、容器集群、微服务架构以及云平台等多种架构。**通过API资产梳理、漏洞管理、威胁监测、运营与响应能力，解决企业API漏洞入侵、数据泄露两大核心风险。**

**往期 · 推荐**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxP3pibVtoiaCUZGthg56a6z1z2iaMtbvQxDhslcNy0m8SDnJXKC6oEfq0zg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496481&idx=1&sn=34b4f474a19214348695f8cee0ab4541&chksm=c0075ebdf770d7ab73cc7c37967acf1b872f79a3b89cea3e833cfab23695457edc5f114142d4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxP1Cux4Jq5JmBsTgpMZa5VIVkPGf3icyJU8RKTibyicceQXU8SeZia1ZJAQQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496462&idx=1&sn=29d5714db225ce0b4e696d5dab8761db&chksm=c0075e92f770d78488e96475b830f59093b7b57194412b077c3dbdbc3a88b6e3893290db6ddf&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxPauwnqJkiaibLzRyEiaXRIUV2CkJYDfET6dtXYGGhEJ1NKojuSOcvBRItQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496376&idx=1&sn=d450da5b2728e9bdad4e0eda8c6666db&chksm=c0075f24f770d6329bc57fbc5c7f3c6af22651f548d5ed4ded7e1b4e2e0129976abe05acf5d4&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehJtplNtPrjvqD1Oy6KhDxPH6Sl8FGnoPGEObDiaibLTSLhMvDCr05R4h4rePNNAUolWlnBJL0AMf0Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)](http://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496333&idx=1&sn=ad3e2bf315a250313eb12bc9c41332d0&chksm=c0075f11f770d60788921156547538ab7b6113d616e01e8c08e30dbc589dae7d7cafb1cedcd9&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOehwcHoxicoOah5mxDjLHMZ9RHUxNeibERphRXOj3AEupxt7JyOt3LF1RmmWQibYmicTv2DxM93iaEJhLxw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

星阑科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOegqicSqJoUd8bSLhdEYnZt3HwOB3tQXas2d1T2xlXc1K1hVMIl1qLxY6qwm5kFbJ6YURBkoXUtPoiaA/0?wx_fmt=png)

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