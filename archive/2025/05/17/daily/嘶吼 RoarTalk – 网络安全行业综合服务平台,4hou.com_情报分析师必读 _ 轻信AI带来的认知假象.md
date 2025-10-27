---
title: 情报分析师必读 | 轻信AI带来的认知假象
url: https://www.4hou.com/posts/wxAr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-17
fetch_date: 2025-10-06T22:26:06.058908
---

# 情报分析师必读 | 轻信AI带来的认知假象

情报分析师必读 | 轻信AI带来的认知假象 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 情报分析师必读 | 轻信AI带来的认知假象

RC2反窃密实验室
[行业](https://www.4hou.com/category/industry)
2025-05-16 18:05:53

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)29459

收藏

导语：浅析AI平台与TSCM行业的关联。

![1.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535568650212.jpg "1742535300124429.jpg")

注：以下**内容符合OSINT国际开源情报搜集标准，部分来自杨叔及团队小伙伴的自身储备分享，可能存在认知偏差，**仅供交流与参考**。**

**01 RC2 OSINT情报小组**

RC2自己的OSINT威胁情报团队已默默耕耘了七个年头。团队从零开始，一直在持续挖掘整理着TSCM行业、商业窃密态势和隐私保护领域的数据，从最初的全球TSCM同行竞争性情报数据搜集，到海外一线BUGSWEEP检测团队能力发掘，直到整理出一套属于RC2自己的开源情报体系。

例如，RC2会持续关注国际上最新的商业窃密案例，剖析案例的技术细节，形成文档资料存储，同时选择将其中一部分作为课程PPT分享。

示例：2020年初，伦敦的标志性五星级酒店--丽兹酒店（The Ritz London）以7.5亿英镑的价格出售，这中间爆出了涉嫌商业窃听的大瓜。杨叔早在2020年的Level-2课程里就分享了这个被誉为“**2020年最受瞩目的商业窃密案例。**

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535570137082.png "1742535376122393.png")

**~类似的案例还有很多，为确保学员始终能接触到最新的案例，基本上杨叔保持着每隔两个月升级一轮PPT的动态更新速度。**

**02 AI平台的白名单**

有人问过杨叔关于使用AI平台开展行业研究的可行性，嗯，这个确实要看情况，主要取决于你要关注的数据本身。杨叔分享下自己的经验：

从ChatGPT 2.0 版本开始，杨叔和团队小伙伴们就开始不断尝试使用AI做TSCM行业分析和数据梳理，其结果让人颇有些哭笑不得。

到现在杨叔还记得：

2024年初，在加拿大某地，杨叔基于ChatGPT 3.5版本，通过检索一些行业有名的公司来简单验证下Chatgpt的数据消息更新效率和范围，在查到一家颇有名气的以色列咨询服务公司（行业内有名的情报公司）时，平台居然回复（为方便理解，以下用中文展示）：

因为某些协议限制，无法显示结果。

然后杨叔立刻给出提示，要求列出是哪些协议限制？ChatGPT回复：

因为某些限制无法告知，请开展其他检索。

**What？**见了鬼了，杨叔随即又试了一些“有名”的行业公司，发现大部分都无法检索，于是明白：

「这个AI平台其实存在一个”白名单“，那些多少与美国政府、北约及其它敏感平台有合作的公司或机构数据，都已被过滤。」

好吧，在这种情况下，作为情报分析师而言，先不说ChatGPT的版本更新情况和是否链接外网，也不说储存的数据库是否完整......仅仅对于当前很多强指向性的检索或者提问的回复，是否严谨可信？是否全面准确，还是已被删减？

就已经打了一个大大的问号~

**03 AI平台的“后门设定”**

可能有些人注意过这个新闻，但杨叔想大部分人可能压根没关注过。

以下为新闻原文：

此前，美国知名人工智能公司OpenAI宣布，前美国陆军将军保罗将加入其董事会，成为新设立的安全与保障委员会的一员，OpenAI表示这一举措旨在利用人工智能技术加速识别并应对网络安全威胁，看似这是一次正常的人员任命，但考虑到保罗的背景(保罗曾任职美国国家安全局局长)，此事引起了特别的关注。

其中，爱德华·斯诺登就认为OpenAI已经成为美国情报部门的帮凶，已视其为具有潜在的、广泛侵犯个人权利的行为。

OK，按道理说，所有使用AI的情报分析人员，都应该知道有这样几个“潜规则”：

> 规则1：AI平台会记录所有检索的相关信息
>
> 包括用户信息、语言类型、访问IP、浏览器版本信息、提交查询内容、回复内容、是否通过VPN等。
>
> 规则2：AI平台会分析用户的背景信息
>
> 通过用户检索的内容、提交的关键字信息、关注的行业或领域、查询频次、用语等，来推断用户的年龄、职业、所在行业/部门、是否政府雇员等。

无语的是，常常有“缺乏上述常识”的人因此而“暴露”：因为检索了太多关键且敏感的内容，被AI平台溯源、并结合其它数据进行了“画像”工作。

在OPENAI官方于2025年2月更新的《Disrupting malicious uses of our models》报告里，可以看到在具体案例里，第一个就直接列出了“疑似来自中国的账户使用ChatGPT平台作为情报检索工具”的证据：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535571612021.png "1742535440130763.png")

随后，关于“OpenAI公司封禁及移除来自中国、朝鲜可疑行为账户”这个主题就上了网络新闻。

**![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535572496994.png "1742535463537357.png")**

**当然了，OpenAI还移除了其它包括欧洲国家的存在疑似情报搜索等行为的可疑账户，还列举了部分账户作为说明。**

**![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535573175138.png "1742535483493991.png")**

所以说啊，作为合格的开源情报搜集与分析人员，第一要务就是不能在一个平台上开展过多敏感数据的检索，需牢记的主要原因有两个：

原因1：可能会被平台里预定义规则“锁定”，导致自身的暴露，会被溯源、被监控及账户被封锁。

原因见上，已经用实例解释了。

原因2：可能会被“有目的推送”伪造或虚假的信息，混淆判断。

这个道理也很简单，全世界的技术人员都知道AI会帮助完成搜索、整理、总结分析的工作，那么可以试想一下，会有多少情报机构、智库、国际安保公司、第三方情报部门、企业安全部门等在不停地在一遍又一遍地遍历互联网，完成大数据的检索。

那对于某些并不希望外部能够获取相关数据，或者已经采取了对应的安全防护措施的机构来说，“故意释放错误的信息来混淆初始数据”，就是一种很好的选择。尤其是故意提交虚假信息来训练AI，那么这些数据最终会进入到AI的后台大数据库中，变成可以向其他人展示的“成果内容”。

这种攻击方式，现在也被称为“AI污染“或”AI下毒”攻击。

![6.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535574102039.gif "1742535507149907.gif")

**04 AI平台对TSCM行业的影响**

目前，对于**TSCM反窃密**领域而言，由于赛道特殊且非常小众，所以国内的AI平台普遍都没有相关概念，或者只是单纯地重复网上的定义，暂时没有相关的深度和知识积累。

而在以ChatGPT为主的海外AI平台上，虽然通过学习库里大量的累计网络资源，能够检索和分析相关信息，但不知道是算法规则限制，还是关键字过滤的原因，实际上回复的误报率相当高。

比如在ChatGPT上使用该指令：列出美国排名前10的TSCM公司。你会发现在结果里面，有一大半都是安保/安防公司，和TSCM行业关系不大，那些非常有名的专业公司压根没有列出。

还有很多查询指令，通过比对RC2自己积累的「TSCM全球知识情报库」，发现结果匹配度相当低，且一大堆错误数据。尽管也有正确可用的数据，但大多数由于时效性，仅仅只能作为参考罢了。

![7.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535575370191.gif "1742535528552618.gif")

但如果只是询问一些绝大多数AI平台都擅长的那种初级框架性问题，比如：

如何开展办公室的BUGSWEEP检测工作？

这时候，AI就会巴拉巴拉地列出一大堆要检查的位置和注意事项，看似好像挺专业全面，但实际上，这些不过是从网上广为流传的公开资料里汇总给出而已。

只有当你追问一些专业技术细节的时候，如：

--如何检测在弱电线路里暗接的窃听器材？

--列出欧洲最新的防非线探测的窃听器型号？

等这类细颗粒问题时，AI就没办法准确回答，或者用其它电工知识，甚至国外网店上卖的“华强北版本偷拍器材”来糊弄你~

唉，所以啊，网上那些说什么“通过AI平台学习TSCM知识、研究TSCM技术的”，都是不懂装懂的噱头罢了~

**![8.gif](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535550156431.gif "1742535550156431.gif")**

当然，并不能因此说所有的AI平台都对TSCM行业无用，经过特定搭建并投入大量时间心血海量训练的AI平台还是会很有效果的，当然，这就是另一个话题了，这里就不多展开~

2025年5月，**RC²**计划推出“PPES-2XX”系列全新高级课程，比如“PPES-201 智能手机隐私保护实践指南”，及“PPES-202 企业供应链物理安全风险评估”课程。

其中，201课程将包括：

运营商通信监控、手机信号劫持与监听、手机定位与防护、手机周边窃听风险识别、手机远控APP等方面，全面了解当前个人智能手机面临的安全风险及应对措施，敬请期待~

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535575130112.png "1742535575130112.png")

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250321/1742535597517198.png "1742535597517198.png")

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8XRJL53c)

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

![](https://img.4hou.com/portraits/182735b0219b1d7a63869aa0c554f245.png)

# [RC2反窃密实验室](https://www.4hou.com/member/33jn)

专注TSCM，物理安全和隐私保护~

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/33jn)

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

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](...