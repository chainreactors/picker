---
title: 财信证券基于RASP技术的API以及数据链路安全治理研究
url: https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650849874&idx=1&sn=6f95f1d8162503ee9289b3866626153f&chksm=80dba1f7b7ac28e136c025ca74be3d711886038d6d97a19ca6597d65ef966584c385bdb025cb&scene=58&subscene=0#rd
source: 青藤云安全
date: 2024-12-28
fetch_date: 2025-10-06T19:39:46.208863
---

# 财信证券基于RASP技术的API以及数据链路安全治理研究

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7EpcyTBK4P0PvTVFXiceIcHLH4BFXCCxic9rtdl4TwVQWNKENOEV4okBIWIicXnmQJq444WIyYql9DeAnLdvjYoEA/0?wx_fmt=jpeg)

# 财信证券基于RASP技术的API以及数据链路安全治理研究

青藤云安全

以下文章来源于中国金融电脑
，作者孙文渊 等

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM56vJqFuozjpm0uMzn29UAGS7ic0wk0kKUpQOtk87Lw1lQ/0)

**中国金融电脑**
.

《中国金融电脑》是由中国工商银行主管、创刊于1989年的一本全国性金融科技专业应用期刊（月刊）。期刊围绕金融科技管理、创新、实践等方面，为业界提供探索交流的平台，也为IT企业提供展示的舞台。

以下文章来源于中国金融电脑 ，作者 孙文渊 刘洋 陈飞虎

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/7EpcyTBK4P0vnoCXcIYKVgWqcCdCs164VlHscJqFoAVx8ZRgSP4ngahc5ncNgQGdReluKL02yCezlWX8KCrVgw/640?wx_fmt=gif&from=appmsg)

**来源：中国金融电脑**

**作者：财信****证券股份有限公司  孙文渊 刘洋 陈飞虎**

当前，数据已成为企业和组织的重要资产，其蕴含的价值不断攀升。然而，数据在收集、存储、传输、使用和共享等各个环节也面临着严峻的安全威胁，如数据泄露、篡改、滥用等问题频发，给个人隐私、企业利益乃至国家安全带来了巨大风险。

本文聚焦证券行业，深入探究基于应用内生的RASP代码插桩技术在信息系统数据安全治理方面的实践，围绕数据资产清点、API清点及防护、风险监测及异常管控等关键能力展开专项研究，旨在提升数据链路安全性，应对网络安全挑战。

**一、API以及数据链路安全治理挑战**

黑客攻击、内部人员疏忽或数据管理不当都有可能导致敏感数据的泄露，如何在数据流通过程中保护个人隐私、在合规的前提下实现数据的安全流通是企业信息安全面临的主要挑战。在数据流通过程中，API是主要的数据传输载体，把握API的数据安全是保障企业整体信息安全的核心和关键。当前，API以及数据链路安全治理面临着诸多挑战：

**一是应用程序内的API获取不全面。**边界安全设备难以对加密流量的访问、静态API资产及东西向的API链路进行全面清点，且无法满足云环境或容器业务中的监控需求。

**二是API对数据的调用关系不可视。**基于流量数据的检测设备无法洞察API间的层级关系，特别是程序内部的调用关系，难以构建连续的API访问链路图谱，以致于无法从全局把握公司业务数据的流通链路，形成有效的管理基线。

**三是API接口传输敏感数据管理薄弱。**业务人员对涉及敏感数据管控不力，敏感API与通用API的数据处理和调用方式相同，导致数据泄露事件时有发生。

**四是API风险的监测和防护力度不足。**传统的安全检测方式难以适用于API领域，针对API的攻击检测与敏感数据传输通道管控能力严重不足。

**二、RASP技术在**

**API及数据链路安全治理中的应用**

财信证券股份有限公司（以下简称“财信证券”）结合当前API及数据安全现状，针对API和数据链路安全治理中遇到的API清点难、敏感数据与调用不可视以及API检测防护能力不强等上述挑战进行调研论证，基于RASP技术开展了一系列实践探索，取得了相应成果，其中与青藤云安全联合提交的“基于RASP技术的API及数据链路安全治理”项目成功入选中国信息通信研究院主办的第四届“金信通”金融科技创新应用案例评选。

![](https://mmbiz.qpic.cn/mmbiz_png/proiaVFrxfiaEdMaCduhJWsFAp0vNjZfciagsMBStey6NNgOyJVEPujfVsNmnuOuJurheEzRibGddich5nHWbqGsg0A/640?wx_fmt=png&from=appmsg)

**1.RASP技术原理**

首先，利用RASP技术在应用程序内部部署Agent，从而使其具备数据采集和控制能力（如图1所示）。以Java为例，利用instrumentation和Attach注入机制，创建安全模块独立的类加载器，用于加载自身安全防护功能模块，进而在业务模块中嵌入安全防护模块，并使之相互隔离。完成注入后，安全模块可自动接管应用程序的各类底层API接口，一旦应用程序执行了危险操作，安全模块技术会对其进行拦截，并执行相应的安全处理流程，同时在应用程序内部对数据请求进行验证，从而保障应用程序的安全性与稳定性。

![](https://mmbiz.qpic.cn/mmbiz_png/proiaVFrxfiaEdMaCduhJWsFAp0vNjZfciaDnAb2WiajKXpI6zN346fIMr3abx7yTmS6UNbicycHEaYZaHTqQ0IcHzA/640?wx_fmt=png&from=appmsg)

图1  Agent在应用程序内部的部署流程

其次，通过部署好的RASP Agent采集应用系统的程序信息，包括程序组件、动态/静态API信息以及关键方法调用等执行过程信息，同时读取API请求响应过程中的报文信息、数据库的读取写入等业务数据，实现对API资产信息的采集。

再次，基于应用程序和数据资产信息制定数据的分级分类规则，对流通通道进行管控，并开展溯源分析，从而实现对API数据链路和敏感信息传输的管理，形成可视化的链路图谱。

最后，综合API上下文的行为分析结果和安全模块的能力，检测诸如类库加载、命令执行、文件读写等多种0day漏洞行为，实现API安全风险行为检测与防护。

**2.RASP技术应用实践**

**（1）动态、静态API全量清点**

RASP可以在代码函数层面实现API的静态识别，通过扫描API资产，检测出所有可调用的API接口，确保API检测的全面性；同时从应用中传输的流量进行动态API识别，找出有效使用的API资产，二者结合可以有效发现僵尸API或影子API。

**（2）API访问数据全链路监控**

在数据访问层面，RASP可以监控API中传输的数据报文内容，记录API之间的调用层级关系，并分析生成API的访问链路图谱（如图2所示）。在应用系统层，RASP可以从API层面将应用连接行为可视化，生成应用服务访问关系图谱（如图3所示），从而据此判断是否有异常或者不合规的访问连接。在信息系统层，通过构建可视化的数据调用全链路图谱（如图4所示），可以清晰掌握数据在企业内部传输调用的路径，精准追溯数据泄漏，为数据合规审查提供有力支撑；帮助企业了解内部数据传输网络，设立访问合规性，形成通用基线。

![](https://mmbiz.qpic.cn/mmbiz_png/proiaVFrxfiaEdMaCduhJWsFAp0vNjZfciaxPPRuScJia8PUvMqyibNxLSIb8UHlHQLofPDBvOQmKA47lY9qaKnhltQ/640?wx_fmt=png&from=appmsg)

图2  API的访问链路图谱

![](https://mmbiz.qpic.cn/mmbiz_png/proiaVFrxfiaEdMaCduhJWsFAp0vNjZfciaPgfZGKXVoHcyqkwluyTTDaApZSUYfG02NXBBrYtFXeHTBxnKvs7iaRw/640?wx_fmt=png&from=appmsg)

图3  应用服务访问关系图谱

![](https://mmbiz.qpic.cn/mmbiz_png/proiaVFrxfiaEdMaCduhJWsFAp0vNjZfciaiblxCEMsv0sSic9ttSx9UMCGtXREG53rorUuImEuicibUoViajXqR5mC9Yw/640?wx_fmt=png&from=appmsg)

图4  数据调用全链路图谱

**（3）敏感数据识别与清点**

RASP技术可以获取API传输过程中的原文请求和原文信息，避免了部分数据因链路加密而无法识别的问题。基于已经建立的数据分类分级制度和建设思路，针对数据库访问、请求响应和内部程序调用等场景，可根据分级分类规则设置API链路监控，对触发了外发敏感的数据安全事件进行告警或阻止。数据库API读取敏感数据判断逻辑如图5所示。

![](https://mmbiz.qpic.cn/mmbiz_png/proiaVFrxfiaEdMaCduhJWsFAp0vNjZfciaEpmAxibXHqENuN6rP7snC0A81jeLULVzGNnwHx0fqQGT0SMRxnpLnhg/640?wx_fmt=png&from=appmsg)

图5  数据库API读取敏感数据判断逻辑

**（4）API安全风险行为检测与防护**

API的风险检测和防护不应仅局限于敏感数据的泄露问题，还需要从更广泛的视角审视API的安全风险，如在开发设计的前期阶段，应该充分考虑其安全性，并在上线运行阶段进行持续的威胁检测，以确保API在数据和网络层面的全面安全。

在API授权管理方面，攻击者可能会利用正常的API授权访问其权限范围外的资源，从而达到获取或删除其他资源的目的。对此，RASP技术可以通过对调用方进行身份验证和授权，并对访问的资源ID请求实施控制，从程序内部保证用户仅能访问权限范围内的资源。

在敏感数据泄露管控方面，RASP技术可以采用过滤敏感信息或限制通用方法的方式，分类审查数据，确保API响应中仅包含合法且必要的数据；同时，还可以通过分析上下文交互信息，检测诸如密码存储在cookie中、可遍历批量下载文件以及鉴权信息暴露在URL中的情况，帮助提前暴露出业务逻辑中存在的风险。

在API攻击防护方面，RASP技术可以有效捕捉API的0day攻击。攻击者为了绕过边界流量安全设备的检测，通常会采用加密流量或特征变形的方式传输攻击载荷，然而，应用安全系统可通过在关键类和关键方法层面有效抓取恶意特征，利用线程堆栈信息精准定位漏洞利用点，并追溯攻击来源和入口API。此外，RASP具有底层代码调用的控制能力，通过控制API的请求响应参数，从而提供针对漏洞的专项热补丁修复能力，以低成本的方式解决老旧漏洞和0day漏洞难题。

**3.实践成果**

通过应用RASP技术，财信证券在券商业务API以及数据链路安全治理的实践中实现了三大关键成果（如图6所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/proiaVFrxfiaEdMaCduhJWsFAp0vNjZfciaTibKGVsic6r4MQB88ZBQ8kNHAkMcjQ8XYBhhSeQb4A1X77pDwBAOpVzA/640?wx_fmt=png&from=appmsg)

图6  API及数据链路安全治理成果

一是实现应用内部数据流动可见，通过RASP技术采集应用内数据流转的日志，并对流转日志进行聚类分析，呈现应用内数据访问关系的拓扑图，实现数据调用的可视化。这有助于清晰地展现数据在应用内部的流动路径和交互关系，为后续的安全分析和管理提供直观的参考依据。

二是实现应用数据调用风险可查，可有效发现信息系统当前的API接口存在的数据调用风险，如未鉴权访问、传输密码、调试信息泄露、参数中存在敏感信息等风险情况，并可定位到具体的业务代码，排除潜在的安全隐患，保障API调用的安全性。

三是敏感数据泄露时可追踪，可实时清点出包含敏感数据的接口，掌握敏感数据在内部传输的路径，以及是否存在数据外发和外发的目标IP。一旦出现泄露事件，可及时对泄露点进行定位和封堵，最大程度降低数据泄露造成的损失，保障数据安全。

未来，财信证券将持续深入贯彻集团和公司党委“筑牢金融安全防线”的要求，始终秉持“自主可控”的金融安全理念，持续强化金融安全创新能力，积极为金融信息安全事业科学、健康、有序发展作出贡献。

**-完-**

**热门动态推荐**

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7EpcyTBK4P2U0JP5NJz4Hia7B9bpbShgUChWs8boBHSGjxLQiccJmR1QGsoU6fXf3qmnebql7lNs70SzNbHW4S6Q/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650849774&idx=1&sn=96862ae1dfb7ed8ac5f79d4ea78018d9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7EpcyTBK4P0yGibXYiaKUrJZt6ApQJfgkZXflboSwXicUwYib3XmVSkIVMOP2UIx7q0TzU11kXqZuDcKSo6EhWe1KA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650849733&idx=1&sn=2627af42bb68bbbaac870e95c4e64b76&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/7EpcyTBK4P0cK8jd6Yia1OoEe59allkI87bibkMu6SRc04FhvK3NaZ9s0kn3DnAcrgDVu7ToqLEON1HicwWKXFZUw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAwNDE4Mzc1NA==&mid=2650849486&idx=1&sn=98379a0b1cb2fd97b0976e0e81bbc0c4&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/7EpcyTBK4P2a96mDib8UNh5iatSRpDyzpnRAmTSIwYf0UpEQ7ict24MBsOoCwstVYAMTsTnibPWciagggdql3Y0BHzw/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7EpcyTBK4P1WPTQaAScoCKkianCbxMW6Ws340jzw69l94hzH56I696TJ4Z02pPVML9Tf2EVAvUGF99ll2PkO7rg/0?wx_fmt=png)

青藤云安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7EpcyTBK4P1WPTQaAScoCKkianCbxMW6Ws340jzw69l94hzH56I696TJ4Z02pPVML9Tf2EVAvUGF99ll2PkO7rg/0?wx_fmt=png)

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