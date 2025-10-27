---
title: 【极思】全量安全资产管理-进阶实践
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247488283&idx=1&sn=5b421b63a8f144be698485621ffec178&chksm=fad4ce0ccda3471a62531aa634ae19db389b5bed00a54f06611332664e409758d20056f2ba03&scene=58&subscene=0#rd
source: NOVASEC
date: 2022-12-17
fetch_date: 2025-10-04T01:47:14.521442
---

# 【极思】全量安全资产管理-进阶实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hojPFbfiayfz8mFProQ6enNUdSicQYlr6e0c6q0qTsVUUdbjSO8GHznIKGr7wq4ZLTKlFhCh9hHKG5akeUdGPrFQ/0?wx_fmt=jpeg)

# 【极思】全量安全资产管理-进阶实践

NOVASEC

以下文章来源于极思
，作者刘亦翔 Sven

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5C9zw6tOQDoPWvmvc5ibTWPB8mLD0usOr8TcibJIoZ9OVw/0)

**极思**
.

A9 Team 攻防团队创始人。某头部证券安全运营负责人。AntSRC、ASRC、JSRC的Top白帽子。

## 一、前言

感谢依然还在的你，90余天未更新，关注量未降反增。努力多分享能一起成长的内容，不负大家的关注。比❤️。

每一个做安全资产管理的同学们，都一个终极梦想，那就是掌握所有信息资产。为什么要掌握所有的安全资产呢，因为做防守的同学们有一个逻辑，掌握全量资产才有可能掌握资产上的风险和隐患。为什么说是梦想呢？每一代想挑战安全资产管理的人也不少，关于安全资产管理的实践也多如牛毛，但至今未见圈内有最佳实践。可见做好安全资产管理的难度不是一般的大。此前有些实践基础，文章定名进阶实践。可参考文章如下。

[【极思】资产管理：安全人员的自救实践](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247483944&idx=1&sn=05b97b3e15d74c18d12d76965641e945&chksm=ea9e2abbdde9a3ad7f77c130002d011d5de6dbdaf86bc5c66f6307d631fbdd00cf0285e5fe90&scene=21#wechat_redirect)

[【极思】安全资产管理痛点思考](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484577&idx=1&sn=d7f1672f7d7f3a82e2b4e3ecbf695237&chksm=ea9e2c32dde9a524091d47fdc3155438223606aa095518b5f54c1e633f36fe6877047d7d7969&scene=21#wechat_redirect)

## 二、为什么要做

#### 第一、解决安全度量中的覆盖率计算问题。

覆盖率计算时，需要全量的资产作为分母。比如，终端上的网络准入、防病毒、EDR等。服务器上的防病毒、HIDS等。统计安全度量数据时，资产是分母。没有全量资产，统计出的度量数据，没有公信力。

#### 第二、解决漏洞情报响应中的资产定位和影响分析问题。

前两年曾设想过，漏洞情报出现时，如果能直接关联资产数据，可直接确定受影响范围，再配合SOAR直接分发工单。受漏洞利用条件、资产数据不完整的影响，一直不曾实现。
在响应过程中，还被质问「我的Java版本不受影响，为啥发工单给我？」。问题是收到漏洞情报响应时，需要有软件、中间件、JAR包的版本号判断影响范围。需要有启动用户、关联软件版本、配置文件、插件版本等资产判断是否可利用。需要互联网开放情况判断处置优先级。天知道你是啥配置啊？

#### 第三、解决告警处置中的人员、资产定位问题，为分析提供支撑。

出现入侵告警时，需要有资产负责人的姓名、电话、IAM账号、人员经理信息，沟通确认是否为攻击行为，排查是否为误报（有可能是员工操作）。若非员工操作，确认为攻击者行为，排查被攻击的漏洞是否存在（有可能是扫描器），需要有软件、中间件、框架、组件、JAR包等资产信息支撑。

#### 第四、解决事件响应中的漏洞定位问题，为分析提供支撑。

如有攻击成功，进入响应阶段。需要排查进程、端口、启动项、文件Hash、文件签名、系统日志等信息，确认是否被安装后门。分析攻击者是否横向移动时，需要排查周边设备的漏洞情况、安全防护情况，分析可能的影响范围。

#### 第五、解决运营过程中资产无法自动化查询的问题。

较多的安全系统都会有资产查询需求，无资产API查询时，只能通过手工查询定位系统的负责人信息。比如，自动化运营场景中，每个流程都有多个步骤，每个步骤有多个查询，任意一个资产信息查询无对应API时，均会导致流程自动化断层，自动化运营系统的价值会大打折扣。

#### 第六、安全运营未来发展和进化支撑。

安全运营的发展和进化，和打游戏时的科技树一样，没有基础能力时，很多高阶能力是无法真正实现的。比如，近期的零信任，前期的态势感知，由于没有强有力的基础能力支撑，被玩成了圈内的笑话。小到安全能力有效性、安全设备巡检，大到实现零信任、安全大脑、智能决策、UEBA等，均会受到影响。

## 三、解决方案思考

事物发展循环：从无到有，从有到多，从多到合。安全资产管理阶段：

阶段一，从无到有，各团队询问更新，自维护本地表格时代。2017

阶段二，表格量大无法维护，升级为简单查询的在线系统。2018

阶段三，系统数据源不够，增加自主发现（扫描和监测）。2019

阶段四，系统+自主发现仍无法覆盖全量资产提出SCMDB。2020

阶段五，大数据平台式解决思路，安全资产管理中心。2021

阶段六，安全资产管理关联漏洞、隐患等的攻击面管理（ASM）。2022

阶段七，设备、用户、系统画像+攻击者画像，全景联动分析。2023

在2019年左右，我们处在阶段四，向阶段五进发，没有理论上可行的思路。有个朋友兴奋的向我介绍 2019年RASC创新沙盒冠军 Axonius ，同时表示打通各系统是个非常难搞定的事，最终放弃了。2020年，我们完成SOAR上对接各种系统和设备，开始与国内多家创业公司接触，期望能共同研发类似的产品，解决资产管理的大痛点。

2021年与多家企业沟通后，在应用场景、产品定位、设计理念、核心能力、同步方式、数据结构等方面达成一致。直到2022年产品才得以落地，经过运营人员实际应用，又对产品进行打磨优化。

## 四、最终实现效果

#### 第一、安全度量支撑，实现终端和服务器覆盖率每日自动统计。

将终端准入、终端防病毒、终端DLP、网络扫描器等数据合并去重，作为分母。各系统自身数据作为分子，自动化计算和安全系统的覆盖率。将HIDS、服务器防病毒、网络扫描器、CMDB、运维自动化、运维监控、系统平台等数据合并去重，作为分母。各系统自身数据作为分子，自动化计算覆盖率。已实现的安全系统见下图。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfz8mFProQ6enNUdSicQYlr6eqaCLRwLONefOBAkCk66FeKvCAHfaV88B2EJdYZlShOictsV3SicYLOdA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfz8mFProQ6enNUdSicQYlr6eE1ZW5EQEMn7AgambyPLVu5ZWDky4nFPEooXeXjSbF6EbDwiaicrZfWNQ/640?wx_fmt=png)

#### 第二、情报响应支撑，一键查询漏洞情报的影响范围。

通过一条查询语句，实现是否开放公网、操作系统版本、软件版本、关联软件版本、启动用户等多条件查询，直接定位实际受影响的资产，再通过SOAR自动化完成工单创建。再也怕别人反问「我的JAVA版本不受影响，为啥发给我？」查询实现截图如下。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfz8mFProQ6enNUdSicQYlr6epIpjkR5n9AS5hW3RoJmk5iaxQK0EGQ2PhHVsu0SFXeq9dEKqiaK7VN8A/640?wx_fmt=png)

第三、告警处置支撑，自动富化工单一眼可知关键信息。

通过SOAR联动查询安全资产管理系统，自动补充系统负责人、联系方式信息，并自动创建告警工单，将判断告警真伪需要的信息富化到工单中。自动化将样本上传至沙箱，获取沙箱检测报告到工单中。实现截图如下。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfz8mFProQ6enNUdSicQYlr6exoqshBVIYaZz5KBw6yx43PhkOm2mGLR1qbLYOZricLpMfFrR4bofWjA/640?wx_fmt=png)

第四、事件响应支撑，一屏掌握资产和漏洞优化级。

通过资产管理系统，一站式查询问题资产的聚合信息，使用VPT功能分析快速定位入侵点。同时可一站式查询周边设备漏洞情况、防护情况，为下一步工作做好准备。实现截图如下。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfz8mFProQ6enNUdSicQYlr6eyOOSGW3cibJfZa7ZOStnDFWvRtNja2pMZmUAApVTCJSsH3Vicjx0uw1w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfz8mFProQ6enNUdSicQYlr6e5Iz7YO5rab7ObiaibjS1SHqkZ09htuiaYkHhcTf8iayZL7Yq2lrnBEnMXg/640?wx_fmt=png)

第五、自动化运营支撑，未来一定是自动化、智能化的。

安全资产管理系统提供全量API接口，配合SOAR，实现告警处置、安全巡检的全流程自动化。解决流程因资产问题无法自动化的问题。节省人力的同时，让自动化的想象空间可以更大。此处无图。

# 五、未来可期之展望

第一、安全资产管理与BAS。进入安全运营阶段后，安全能力有效性会成为一个焦点。在实践的过程中，掌握资产的漏洞后，可与BAS联动进行测试，实现风险管理的闭环。

第二、安全资产管理与零信任或安全大脑。随着安全运营成熟度的不断提高，最后实现的一定是动态自适应安全，类似零信任的持续认证，动态调整策略。而零信任市场上，直到目前都没有出现一个像样的总控中心。可以类人思考，基于攻击者、应用、主机的画像，实现动态的策略调整。

关注我，一起实践全量安全资产管理！

![](https://mmbiz.qpic.cn/mmbiz_jpg/hojPFbfiayfz8mFProQ6enNUdSicQYlr6etPYhCEgrHUcy3jwdj7ZC6TqIS4wXl5sUOPBGQGdxMOsSp3KpicC16mQ/640?wx_fmt=jpeg)

首页图片如下，拿走不谢。

![](https://mmbiz.qpic.cn/mmbiz_png/hojPFbfiayfz8mFProQ6enNUdSicQYlr6eko5X9YEdhmWvbyg9NBU6LUibNgxDTXXM97WYHS4KtCTCicdDFCaqlAAQ/640?wx_fmt=png)

**# 往期文章**

[【极思】安全从业成长总结（2017-2019）](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484168&idx=1&sn=cb56bb5f48e5eb13b163c7cd184f2021&chksm=ea9e2b9bdde9a28dca1bed82f4cfe66696f9bdd2e5ecf8ea13db604b890b753be8550c3a813d&scene=21#wechat_redirect)

[【安全】安全管理痛点解决实践](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484137&idx=1&sn=c31bcfacf5f95f6d9cef328b651fa327&chksm=ea9e2a7adde9a36c34dc7040c17851bb4416509ab292a8c3df3725289acb1fd495473b8e9a0a&scene=21#wechat_redirect)

[【极思】零信任之微隔离预研](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484293&idx=1&sn=874161bacf7e5587800c6e46a74f9bce&chksm=ea9e2b16dde9a200a0254820814f30a0391a1a78bb6517a33d939827b366b8f1b60c1b81c753&scene=21#wechat_redirect)

[【极思】容器(Docker)安全研究](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484272&idx=1&sn=98021a45193bbce0933c39e3ec53c2cb&chksm=ea9e2be3dde9a2f5ab548429acef86fa3d50db8d76e650991730113505e4ac7e601bd52fe131&scene=21#wechat_redirect)

[【极思】WMIC 攻防研究](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484250&idx=1&sn=6b32fe9ce8c49dc6cec637fccd398186&chksm=ea9e2bc9dde9a2df5642bca4d106865c60e70a7dcb2ec6942eea44188090d81ab1bcf61ac992&scene=21#wechat_redirect)

[【安全】用户实体行为分析研究(UEBA )](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484234&idx=1&sn=54e141f1b3be8ac34129d8af508ba007&chksm=ea9e2bd9dde9a2cfc63a22fcb74566c69e699f9c0a97229d8402b3ffbf0d021a5dd2dc19dc6b&scene=21#wechat_redirect)

【安全】[PRE-ATT&CK：侦查阶段对抗设计和实践](http://mp.weixin.qq.com/s?__biz=MzI2NTMwNjYyMA==&mid=2247484211&idx=1&sn=583d758f371d443ceabb7c8c631a98c0&chksm=ea9e2ba0dde9a2b6a7b1af266955434063a3543d5942e397c84e66d0f1873c6b4e8916be2afd&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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