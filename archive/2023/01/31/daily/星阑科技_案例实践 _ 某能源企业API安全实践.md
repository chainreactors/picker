---
title: 案例实践 | 某能源企业API安全实践
url: https://mp.weixin.qq.com/s?__biz=Mzg5NjEyMjA5OQ==&mid=2247496928&idx=1&sn=ecb8460153e660853475aecfb8d0b489&chksm=c007597cf770d06aceb1d91a5351ac29d6994fb800834c6399ad68d07d347dd0a3aa47ef53b9&scene=58&subscene=0#rd
source: 星阑科技
date: 2023-01-31
fetch_date: 2025-10-04T05:14:34.300990
---

# 案例实践 | 某能源企业API安全实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cc8QqLUKOehxlRYupgYgxttibYmbxe8zdpVDXB9ECRJrz8CTtPX5WD7sjmRLRnVYswSPHjUia30NnzSdbphxveKQ/0?wx_fmt=jpeg)

# 案例实践 | 某能源企业API安全实践

星阑科技

![](https://mmbiz.qpic.cn/mmbiz_gif/Cc8QqLUKOeiaFHTFtiatmEIxZQcXOHfyr6GOBM88IeMm28ybjSAHEJKicuQxPxN5L5NFZ5mza2NOnuokf9ant2fUQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

随着智能电网、全球能源互联网、“互联网+电力”、新电改的全面实施，分布式能源、新能源、电力交易、智能用电等新型业务不断涌现，运营模式、用户群体都将发生较大变化，电力市场由相对专业向广域竞争转变，民营等各种主体也参与到电力市场，使得智能电网系统的标准、开放、互联特性进一步增强，同时也使得智能电网网络安全、业务安全和数据安全防护战线不断延伸，给安全防护带来新压力，增加了“一点突破，影响全网”的风险。在本年度国家组织的专项检查中发现，部分电厂生产监控网络和互联网相连，极大增加了系统安全风险。

国家、行业主管部门一直以来高度重视网络与信息安全工作。自2002年以来，公安部、国家能源局、发改委,以及原国家电力监管委员会等国家和行业主管部门陆续颁布实施了《计算机信息系统安全保护等级划分准则》（GB17859-1999）、《信息安全等级保护管理办法》（公通字[2007]43号）、《电力二次系统安全防护规定》（[2004]电监会5号令）等规章制度，构建了较完整的电力行业网络与信息安全法规体系。自2014年起，国家网信办、发改委、公安部、国家能源局等主管部门加大对电力信息安全的重点监督管控，相继颁布了《电力监控系统安全防护规定》(2014第14号令)等一系列法令、制度和标准，进一步明确了电网信息安全的重要性。

**背景介绍**

智能电网建设使得电网发电、输电、变电、配电、用电、调度各环节更为开放，带来大量业务结构的变化，基于互联网的社会服务和公众参与度更高，多种基于互联网的互动化业务应用发展迫切，电网侧、用户侧交互与应用更为频繁，同时，新技术的应用引入新的风险，对传统防护结构带来冲击，具体体现在以下方面：

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOehxlRYupgYgxttibYmbxe8zdpEdqpsZA2YBsUjU0YkUGb89Iv8vcNqZWEaGB1p7Lv9g5DCIJCLeBiag/640?wx_fmt=png)

**智能化业务面临停电破坏威胁**

电力监控系统智能化发展使得停电风险进一步显现，智能变电站系统、配电自动化系统、负荷控制系统等电力监控系统控制功能更加依赖网络通信技术，易遭受控制指令篡改、业务逻辑破坏等网络与信息安全攻击，引发业务故障或是控制指令设置异常，导致停电风险加大。

**网络安全边界面临模糊化不可控风险**

无线局域网、移动通信网络、卫星通信等多种通信方式、多种网络协议并存，电力通信网络更加复杂。网络边界变得模糊，由于业务发展需要和地理位置限制，部分电力终端采用无线网络连接上级系统，使得网络攻击途径有所增加。因此迫切需要正确梳理防护需求，提出适应性更强的网络边界安全防护架构。

**敏感信息面临更高的泄露风险**

信息系统集成度、融合度更高，系统依赖性更强，业务系统之间、业务系统与外界用户实时交互更加丰富与频繁，数据的采集、存储、传输和处理方式发生了新的变化，暴露面扩大，增加了数据泄露的安全风险，对数据安全保护提出了更高要求，一旦数据访问权限设置不当，或业务逻辑设计导致系统缺陷，可能导致用户个人信息等隐私泄露。

**需求场景**

随着电力系统的逐步在线化和智能化，能源企业的业务系统也面临着对外接口的安全问题，需要制定全面计划并及时发现、测试和保护 API，并将 API 安全纳入其整体应用程序安全策略。

针对行内情况实现 API 深度安全防护，具体需求如下：

* 需要系统性摸排各业务API通信链路与技术架构。
* 需要建立持续化API安全监测及溯源能力。
* 需要针对API敏感数据提供有效的监测手段。
* 需要联动WAF对API攻击进行防御。

**方案实现**

通过部署萤火API安全平台一体机，从流量汇聚层采集四层数据，自动梳理形成API资产台账，并通过资产拓扑访问关系展示各业务API通信链路与技术架构。

通过四层流量分析，实时监测针对API的攻击，可发现登录弱密码、接口未鉴权、敏感数据查询接口参数可遍历、返回数据量可修改、伪脱敏、数据库查询接口多种涉及敏感数据泄露风险途径，并将攻击特征、攻击情报同步到WAF进行联动处置。

![](https://mmbiz.qpic.cn/mmbiz_png/Cc8QqLUKOehxlRYupgYgxttibYmbxe8zdAPjNPiaVib5W94Srg5dQIHYQr1w2jibYSo01RxAcL6q0iavtV7UPNNc5PQ/640?wx_fmt=png)

**客户评价**

这两年为了配合国家电力信息化建设，开通很多对外的数据接口，但是关于接口本身包括传输的敏感信息一直没有很有效的安全风险监测手段，星阑科技的解决方案提供了非常良好的解决思路，同时也实现了跟我们现有系统联动的处置能力，让这套系统从合规和安全防护上得到了保证。

**关于星阑**

星阑科技基于AI深度感知和强大的自适应机器学习技术，帮助用户迅速发现并解决面临的安全风险和外部威胁，并凭借持续的创新理念和以实战攻防为核心的安全能力，发展成为国内人工智能、信息安全领域的双料科技公司。为解决API安全问题，公司从攻防能力、大数据分析能力及云原生技术体系出发，提供全景化API识别、API高级威胁检测、复杂行为分析等能力，构建API Runtime Protection体系。

**星阑科技产品——萤火 (API Intelligence) 拥有不同应用场景的解决方案，**适配服务器、容器集群、微服务架构以及云平台等多种架构。**通过API资产梳理、漏洞管理、威胁监测、****开放式数据平台、运营与响应能力，解决企业API漏洞入侵、行为异常、数据泄露等核心风险****。**

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