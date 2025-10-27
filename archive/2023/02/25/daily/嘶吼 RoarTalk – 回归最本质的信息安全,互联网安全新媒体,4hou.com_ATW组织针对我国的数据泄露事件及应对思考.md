---
title: ATW组织针对我国的数据泄露事件及应对思考
url: https://www.4hou.com/posts/GKL8
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-25
fetch_date: 2025-10-04T08:02:31.643369
---

# ATW组织针对我国的数据泄露事件及应对思考

ATW组织针对我国的数据泄露事件及应对思考 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# ATW组织针对我国的数据泄露事件及应对思考

安天
[行业](https://www.4hou.com/category/industry)
2023-02-24 10:01:18

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)124921

收藏

导语：该黑客组织从受害单位窃取了大量信息系统源代码数据并在境外黑客论坛RaidForums上进行非法售卖。

![封面图.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677204010884300.png "1677051897164518.png")

名为“AgainstTheWest”（ATW）的黑客组织自2021年10月以来攻击SonarQube、Gitblit、Gogs等平台，窃取了包含国内多家企事业单位的代码和数据，在境外黑客论坛进行非法售卖，约150余家单位受到影响，涉及金融、医疗、政府、部队、高校等多个行业。该黑客组织从受害单位窃取了大量信息系统源代码数据并在境外黑客论坛RaidForums上进行非法售卖。

基于该团伙常用攻击手法以及泄露数据等相关信息分析，被攻击单位或者供应链单位多因为相关代码质量管理/存储平台和自动化代码构建/测试平台存在安全漏洞而导致关键代码和数据被窃取。ATW组织早期在2021年主要攻击目标是SonarQube代码质量管理平台，后续在2022年初其攻击目标又扩大到了Gitblit、Gogs等代码存储管理平台。

ATW组织是带有强烈政治倾向的高度亲西方化的境外黑客组织，在俄乌冲突期间，以“#FreeUkraine”的名义针对俄罗斯、白俄罗斯等国家发起网络攻击。

ATW组织选取具备一定影响力和敏感性的单位，将上游供应商代码被窃取事件炒作为敏感用户关键信息被窃取事件，并且其发布的数据泄露相关信息中带有明显的包装色彩，试图夸大事件的严重性。此类数据泄露事件一定程度上形成了由网空域延展到认知域的放大连锁效应。我国是网络大国，也是面临网络安全威胁最严重的国家之一。

近年来，由第三方供应商引入的安全风险一直没有停止，网络攻击者通过入侵软硬件供应商，实现对下游政企应用场景的连锁突破，已经成为常态化攻击方式，利用网络攻击造成的信息窃取和破坏事件亦呈现增长趋势。在当前复杂的国际形势背景下，如果ATW组织广泛将目前手中已经窃取的全部源码广泛分享给全球其他攻击组织，将会带来诸多连锁风险。因此需要冷静应对，避免过度恐慌；同时需要深入系统梳理关联风险、统一部署、加强防范。

从软件供应链安全事件中暴露的典型问题来看，一是政企用户方面缺少对上游供应链网络安全视角的统一工作机制和流程规范，对供应商资质入围缺少网络安全层面的整体要求，缺少对软硬件设备安全入网的管理要求、操作规范和对应检查机制，以及系统中存在的不安全配置和过度开放的访问权限策略；二是开发安全方面软件代码安全工程能力较差，普遍缺少全生命周期的代码安全工程能力、缺少原生融合的出厂安全机制，易于出现严重安全漏洞，甚至存在低级问题，接入政企网络后，难以支撑可管理性、可防御性的要求。三是软件研发环境方面综合防护能力薄弱，在设计、开发、编译、测试、签名、分发等场景缺少针对性防护措施，导致相关环境和流程被攻击者入侵，软件被植入脆弱性代码、捆绑恶意代码等，带来系列严重风险。

针对政企事业单位和软件供应厂商，安天产品推进中心建议：

**1． 全面自查自测风险隐患**

全面分析内外部资产分布、来源、可控性等因素，加强账号安全管理及自查，避免发生弱口令、访问权限被盗或外泄，同时防范撞库攻击等账户安全风险。

**2． 积极引入先进软件安全方法**

采取SecDevOps等先进的软件安全开发方法，建立健全与之匹配的代码安全策略，并持续运营，以安全运营视角在代码全生命周期中的每一个环节增强代码安全性。

**3．完善供应链安全标准规范体系**

完善软件安全性能评测及安全事件处置流程。针对外部服务商实施安全审查及跟踪，建立供应商安全评估和准入机制，确保软件产品（工件、制品）所用开源代码、第三方库等成分透明化，及时处理外部代码组件安全漏洞，确保发现安全漏洞时能及时对资产进行跟踪和排查，确保供应链安全。

**4．加强软件系统上线安全检测**

在系统上线前用漏洞扫描设备、恶意代码检测系统、软件组成分析系统和应用安全检测系统来检测WEB应用中的恶意代码和脆弱性，使用静态分析安全测试系统和动态安全分析测试系统检查API接口是否存在漏洞、越权、溢出和访问控制不当等问题，增加内部平台的多重安全访问机制，防止敏感信息非受控传输。并定期对已上线应用进行复查，以确保相关安全技术措施持续有效。

**5．强化软件研发环境安全防护**

全面识别软件研发环境的代码和数据等执行体并进行细粒度的管控，建立操作系统和应用软件所包含可执行体的元数据化属性和系统行为集合，并建立配套的持续监控机制，通过全生命周期的识别分析产生综合性分析结论及生僻的特征统计，及时发现潜在隐患、正在发生的异常和威胁事件并有效处置。

针对此类事件，安天向政企客户和软件供应商提供代码安全检测和软件研发环境安全治理解决方案。该方案集成了安天软件组成分析系统、安天静态应用安全测试系统、安天代码安全检测系统和软件开发环境的执行体治理服务。

安天软件组成分析系统能够有效识别项目中的非安全组件，并输出软件构成清单（SBOM），为项目建立“静态快照”。安天静态安全测试系统能够识别源代码中潜在的漏洞和后门，帮助研发人员及时发现问题并进行修复。安天代码安全检测赋能企业安全开发按流程，解决前期开发流程中代码安全问题，系统支持接入持续集成和持续交付（CI/CD）流程，为企业的代码安全建立持续化监控，有效提高企业对代码风险的应对能力。

![图1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677204010742785.jpeg "1677051354296764.jpeg")

图1-安天代码安全检测系统输出物料清单界面

![图2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677204011329149.jpeg "1677051329486732.jpeg")

图2-安天代码安全检测系统检测出源码漏洞界面

解决软件被植入脆弱性代码、捆绑恶意代码等软件供应链安全风险，除了软件开发安全环节的举措之外，还需要全面识别和管控软件研发环境的代码与执行体（包括研发、测试过程中不断迭代产生的新执行体），强化软件研发环境的自身安全防护能力。以执行体治理为主要工作抓手，建立操作系统和应用软件所包含执行体的元数据化属性和系统行为集合，通过全生命周期的识别分析产生综合性分析结论及生僻的特征统计，及时发现和有效处置潜在隐患和正在发生的不安全事件。安天智甲的执行体治理增值服务，可为安天智甲终端安全检测产品和其他终端安全产品赋能终端执行体治理能力，实现差异化终端场景下的执行体全要素信息采集，精细化识别，安全基线构建和细粒度管控。执行体治理模块联动安天威胁情报子系统和安天执行体信誉识别子系统，结合安天安全服务人员和应急响应人员为政企客户和软件供应商的网络环境提供专属的、自动化的、全面的、可持续化运营的执行体治理解决方案。

![图3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230224/1677204011102159.jpeg "1677051299148878.jpeg")

图3-某软件研发企业-全量执行体治理概览视图

做好执行体细粒度管控工作，方能实践软件研发环境“识别、塑造、防护、检测、响应”等关键安全防御动作。

识别：能够有效澄清系统环境、业务环境：掌握执行体的行为与业务之间的支撑关系；理解执行体及其所需权限；识别执行体具备的能力及其与脆弱性、暴露面的对应关系等。

塑造：管控连接，依据目的管控连接；收敛暴露面，管控执行体开放服务及存在执行更新能力的通道；减少信息外溢，识别访问隐私数据行为，管控传输用户隐私动作。

防护：识别执行体的资源访问、连接、创建、写入、执行的客体，判断其行为目的，及时拒绝、阻断或制止违规行为。

检测：基于执行体分布和行为监测，筛选出值得关注的、未知的执行体；提供异常行为依据；基于执行体行为和用户操作，推断用户行为及其目的。

响应：基于执行体的潜在和激活能力、创建信道等手段，支撑追溯攻击来源；基于攻击执行体的行为和潜在行为，支撑环境和数据恢复、策略调整。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?E18tj9zn)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/wp-content/uploads/2017/10/a4d310d551660a09a8f6.jpg)

# [安天](https://www.4hou.com/member/e3QQ)

这个家伙很懒,什么也没说!

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/e3QQ)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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