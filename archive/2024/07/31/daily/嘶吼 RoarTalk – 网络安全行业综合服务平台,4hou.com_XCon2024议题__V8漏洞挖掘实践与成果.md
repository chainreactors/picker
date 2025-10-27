---
title: XCon2024议题||V8漏洞挖掘实践与成果
url: https://www.4hou.com/posts/Dx9x
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-31
fetch_date: 2025-10-06T17:41:08.281447
---

# XCon2024议题||V8漏洞挖掘实践与成果

XCon2024议题||V8漏洞挖掘实践与成果 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# XCon2024议题||V8漏洞挖掘实践与成果

XCon组委会
[活动专区](https://www.4hou.com/category/xactivity)
2024-07-30 17:04:41

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)88235

收藏

导语：未来，V8漏洞的挖掘与应用，将在军事与智能领域取得更大的突破。

![微信图片_20240730163657.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240730/1722329190110494.jpg "1722329190110494.jpg")

**循万变·见未来——技术前瞻**

**未来，V8漏洞的挖掘与应用，将在军事与智能领域取得更大的突破。**

**军事化：**

v8漏洞挖掘所需的资源越来越大, 逐渐由大型组织甚至国家接管, 成为攻击高价值目标的重要一环。

**智能化：**

对于语料生成过程, 传统的算法已经捉襟见肘, 基于神经网络的生成式模型或许会来带新的曙光。

**——京东安全实验室**

**安全研究员 TheDog**

V8漏洞是Google Chrome浏览器中V8 JavaScript引擎的安全缺陷。它可能导致数据泄露、恶意代码执行或网页篡改。黑客可利用此漏洞窃取用户的敏感信息，执行远程攻击，或误导用户点击危险链接。

**本届XCon2024大会中，来自京东安全实验室的安全研究员TheDog将带领大家共同探索 JavaScript V8 引擎的世界**。介绍其基本架构以及常见的攻击面，一起揭开V8的神秘面纱，理解其工作机制，了解它可能被利用的各种方式。

演讲中，TheDog还将介绍 Fuzzilli，一款专为揭示 V8 引擎中潜在漏洞而设计的强大工具。深入讨论 Fuzzilli 的工作原理，包括其独特的 FuzzIL 设计，以及如何通过代码生成、代码变异和模板生成多样的测试样例。他将展示 Fuzzilli 在软件安全测试领域的优势，以及它如何帮助安全研究人员找出并解决潜在的安全风险。

同时，演讲者还将分享一些对 Fuzzilli 进行的改进措施。包括提高 fuzz 测试的覆盖面、增强漏洞检测能力、提升 fuzz 测试效率，以及改进覆盖率插桩方式和提高 fuzz 测试的稳定性，展示一些实际挖掘到的 crash 和漏洞利用过程。

最后，将与参会者一道展望未来的 fuzz 测试方向，探讨新的技术和策略如何进一步提高我们的软件安全测试效果。

**议题亮点**

**《V8漏洞挖掘实践与成果》**

**1. 改进代码生成器以提高fuzz覆盖面**

**2. 改进Fuzz策略, 将变异引擎与模板生成引擎进行融合, 提高fuzz效率**

**3. 改进覆盖率插桩方式, 实现对于V8 builtin的覆盖率收集**

**4. 改进fuzz稳定性以提高覆盖率的准确性与crash的可重现性**

**5. 漏洞利用过程与思路**

**演讲人及团队介绍**

**TheDog——京东安全实验室安全研究员**

![微信图片_20240730163112.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240730/1722328368147164.jpg "1722328368147164.jpg")

**TheDog**——主要从事二进制安全研究与java静态分析方面的工作, 曾挖掘出ubuntu、nginx等关键基础设施中多个高危漏洞。

**獬豸实验室 （Dawn Security Lab）**，是京东旗下专注前沿攻防技术研究和产品沉淀的安全研究实验室，重点关注移动端安全、系统安全、核心软件安全、机器人安全、IoT安全、广告流量反作弊等基础和业务技术研究。实验室成员曾多次获得Pwn2Own冠军，在BlackHat、DEFCON、MOSEC、CanSecWest、GeekCon等顶级安全会议上发表演讲，发现Google、Apple、Samsung、小米、华为、Oppo等数百个CVE并获得致谢。曾获得2022年黑客奥斯卡-Pwnie Awards“最佳漏洞提权奖” ；同时也是华为漏洞奖励计划优秀合作伙伴，CNNVD一级支撑单位，GeekCon优秀合作伙伴。

**XCon2024售票通道现已全面开启**

**【XCon&KCon，3日联票】****¥2069元**，仅限30张

**【循变者】****¥2090元**，XCon2024全场通——含聚焦场演讲+HackingGroup“未来之锋·智创奇迹”技术论坛+展商空间+极客市集

**【聚焦者】****¥2790元**，XCon2024全场通——仅限会议当日现场购买，不支持票券折扣

**【“未来之锋·智创奇迹”技术论坛】****¥0元**，XCon&HackingGroup “未来之锋·智创奇迹”技术论坛+展商空间+极客市集

![11.jpg](https://img.4hou.com/article/wechat/WechatIMG435.jpeg "1722328497529146.jpg")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?b86J2VJe)

#### 你可能感兴趣的

* [![]()

  第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](https://www.4hou.com/posts/QXy7)
* [![]()

  XCon2025完美落幕|在AI革命的浪潮中，筑牢安全堤坝！](https://www.4hou.com/posts/9jZ3)
* [![]()

  新态势·新实战 | CSOP 2025 网络安全运营实战大会在京开幕](https://www.4hou.com/posts/338Q)
* [![]()

  ISC.AI 2025大会圆满落幕：安全与AI融合，人才与产业共进](https://www.4hou.com/posts/nl4R)
* [![]()

  来啦！XCon2025大会日程热力解锁！惊喜票价燃动启售~~](https://www.4hou.com/posts/wxDR)
* [![]()

  重磅官宣 | 2025 CCS成都网络安全技术交流活动定档9月！](https://www.4hou.com/posts/EyEv)

![](https://img.4hou.com/FgeSuF0KtB-UlpRnM5_Lap8oHIWx)

# [XCon组委会](https://www.4hou.com/member/k2wX)

这个家伙很懒,什么也没说!

#### 最新文章

* [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](https://www.4hou.com/posts/QXy7)
  2025-09-24 10:52:53
* [XCon2025完美落幕|在AI革命的浪潮中，筑牢安全堤坝！](https://www.4hou.com/posts/9jZ3)
  2025-08-25 16:30:26
* [新态势·新实战 | CSOP 2025 网络安全运营实战大会在京开幕](https://www.4hou.com/posts/338Q)
  2025-08-21 22:28:39
* [ISC.AI 2025大会圆满落幕：安全与AI融合，人才与产业共进](https://www.4hou.com/posts/nl4R)
  2025-08-08 16:33:21

[查看更多](https://www.4hou.com/member/k2wX)

# 相关热文

* [第三届“天网杯”网络安全大赛收官，夯实网络安全战略人才基石](https://www.4hou.com/posts/QXy7)

  企业资讯
* [XCon2025完美落幕|在AI革命的浪潮中，筑牢安全堤坝！](https://www.4hou.com/posts/9jZ3)

  XCon组委会
* [新态势·新实战 | CSOP 2025 网络安全运营实战大会在京开幕](https://www.4hou.com/posts/338Q)

  企业资讯
* [ISC.AI 2025大会圆满落幕：安全与AI融合，人才与产业共进](https://www.4hou.com/posts/nl4R)

  企业资讯
* [来啦！XCon2025大会日程热力解锁！惊喜票价燃动启售~~](https://www.4hou.com/posts/wxDR)

  XCon组委会
* [重磅官宣 | 2025 CCS成都网络安全技术交流活动定档9月！](https://www.4hou.com/posts/EyEv)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)