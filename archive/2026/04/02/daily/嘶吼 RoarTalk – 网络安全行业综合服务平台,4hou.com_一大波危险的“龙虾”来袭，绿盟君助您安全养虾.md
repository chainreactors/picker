---
title: 一大波危险的“龙虾”来袭，绿盟君助您安全养虾
url: https://www.4hou.com/posts/Arj9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-04-02
fetch_date: 2026-04-03T04:27:12.620782
---

# 一大波危险的“龙虾”来袭，绿盟君助您安全养虾

一大波危险的“龙虾”来袭，绿盟君助您安全养虾 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 一大波危险的“龙虾”来袭，绿盟君助您安全养虾

企业资讯
[行业](https://www.4hou.com/category/industry)
18小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)7533

收藏

导语：OpenClaw爆火，您的网络准备好了吗？

近期，工业和信息化部网络安全威胁和漏洞信息共享平台（NVDB）发布了一则重磅预警：OpenClaw开源AI智能体部分实例在默认或不当配置下存在严重安全风险，极易引发网络攻击、信息泄露等安全问题。这一预警犹如一石激起千层浪，引发了业界对AI智能体安全的高度关注。

![图片55.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260402/1775122064491522.png "1775122064491522.png")

**OpenClaw引领智能体全面爆发，安全问题频发**

2026年，AI智能体技术迎来全面爆发。作为其中的代表性项目，OpenClaw（曾用名Clawdbot、Moltbot）凭借其强大的能力备受青睐——它能够整合多渠道通信能力与大语言模型，构建具备持久记忆、主动执行能力的定制化AI助手，支持本地私有化部署。

然而，正是这样一位“能干的助手”，却可能成为潜伏在您网络中的“定时炸弹”。

**OpenClaw三大核心风险，不容忽视**

OpenClaw由个人程序员编写，从发布到爆火仅仅几个月时间，由于自身设计特点，存在天然的“信任边界模糊”问题。它具备持续运行、自主决策、调用系统和外部资源等能力，在缺乏有效权限控制、审计机制和安全加固的情况下，将面临三重严重风险：

**安全风险1：代码安全堪忧——三天两高危RCE，系统可被恶意接管**

OpenClaw的代码库在短期内连续曝出两个高危远程代码执行漏洞（RCE）。攻击者无需复杂操作，即可利用漏洞在目标主机上执行任意代码，实现从“入侵”到“接管”的一步跨越。一旦得手，OpenClaw所在的主机将成为攻击者的“肉鸡”，企业核心数据、内部网络将完全暴露在风险之下。这不是危言耸听，而是已在野外被积极利用的真实威胁。

![图片56.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260402/1775122081187283.png "1775122081187283.png")

**安全风险2: 盲目信任放大风险——“以安全换便捷”，Agent沦为攻击跳板**

OpenClaw的设计理念强调“自主性”，默认配置往往为了便捷而牺牲安全。许多用户在部署时，为了能让工作更便捷，需要赋予它极高的权限，甚至让其直接访问敏感系统或数据库。这种对Agent的“盲目信任”，让攻击者能够通过诱导式指令，轻松操纵OpenClaw执行越权操作——比如读取机密文件、发送恶意邮件、横向移动攻击内网其他主机。你以为它是你的得力助手，实际上它可能正在被敌人遥控。

![图片57.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260402/1775122097161617.png "1775122097161617.png")

**安全风险3: 插件系统成供应链突破口——隔离机制缺失，投毒威胁放大**

OpenClaw支持通过Skills插件系统扩展功能，但这片“沃土”也成为攻击者的乐园。第三方插件来源不明、供应链环节缺乏审查，加之OpenClaw自身对插件运行缺乏有效的隔离机制，使得一个被投毒的插件就能成为“特洛伊木马”。一旦插件被安装，恶意代码便能随OpenClaw权限肆意横行，窃取数据、植入后门，甚至通过插件更新机制将投毒扩散至更多用户。供应链安全的薄弱环节，在此被无限放大。

![图片58.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260402/1775122110153612.png "1775122110153612.png")

谷歌在2月份就已经连夜封禁OpenClaw，Facebook、Mata、微软等几家巨头也不允许员工在公司内部使用OpenClaw。微软安全团队已将此情形定性为“具有持久凭据的不可信代码执行环境”，这一评价值得每一个正在或计划使用AI智能体的企业深思。

**客户真实痛点，您是否感同身受？**

在与众多企业用户的交流中，我们听到了两种典型的担忧：

客户声音1：“我们公司有员工自己偷偷部署了OpenClaw，我担心这些‘影子AI’导致本地主机端口暴露，引发信息泄露。但我连它们在哪里都不知道，更别提管控了。”

客户声音2：“我们业务部门正式部署了OpenClaw，但我想知道它到底做了哪些外部访问？这些访问是否合法合规？是否存在被利用的风险？”

**传统安全方案为何失效？**

面对OpenClaw这类新型AI智能体，传统安全方案显得力不从心：

流量内容不可见：OpenClaw用户侧API主要进行常规HTTPS调用，流量加密传输，传统应用识别方式完全失效。

端口识别易绕过：OpenClaw虽有默认端口，但极易被修改，单纯依赖端口识别不仅准确率低，还容易被攻击者绕过。

**绿盟科技OpenClaw安全防护方案：给AI装上“安全护栏”**

针对OpenClaw带来的新型安全挑战，绿盟科技创新性地推出低成本“AI安全一体机+绿盟防火墙NF联动”解决方案，帮助用户实现对AI智能体的精准识别与全面管控。

![图片59.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260402/1775122123198262.png "1775122123198262.png")

**方案核心能力**

精准识别：AI安全一体机内置AI智能体发现能力，可主动扫描内网环境，精确识别哪些主机部署了OpenClaw等AI智能体。

灵活管控：根据企业策略，可对非法部署的OpenClaw进行网络隔离，对合法部署的OpenClaw进行全程行为跟踪。

纵深防御：防火墙对OpenClaw的会话访问进行实时分析，识别恶意URL、入侵威胁、病毒等风险，确保每一次访问都安全可控。

**方案优势**

识别精准：从资产纬度对AI智能体进行主动识别，告别传统方案的误报与漏报。

部署便捷：不影响原有组网，快速接入，即插即用。

全面可视：对OpenClaw的访问行为进行全程跟踪分析，让安全风险无处遁形。

**两大应用场景，全方位守护**

场景1：对非法OpenClaw进行精准封堵

当员工私自部署OpenClaw，AI安全一体机第一时间发现并定位，将非法安装的PC信息同步给防火墙。防火墙自动生成黑名单策略——无论外部试图访问该OpenClaw，还是OpenClaw主动外联，都将被实时阻断，将风险扼杀在萌芽状态。

![图片60.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260402/1775122139275654.png "1775122139275654.png")

场景2：对合法OpenClaw进行安全管控

对于业务部门正式部署的OpenClaw，AI安全一体机将其纳入管控范围。防火墙生成精细化管控策略，对OpenClaw的所有访问会话记录流量日志，进行全方位安全检测，避免恶意URL、入侵威胁、病毒等威胁趁虚而入，让业务在安全轨道上平稳运行。

![图片61.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260402/1775122172654848.png "1775122172654848.png")

**两会强调“发展与安全并重”，绿盟科技如何解读？**

近期全国两会多次强调“发展与安全并重”，这释放了一个清晰信号：安全不是AI创新的刹车，而是AI落地的护栏和加速器。

作为安全厂商，我们的目标就是让客户在AI的高速公路上既能跑得快，又能刹得住、不跑偏。具体到企业落地，要避免“安全拖慢AI”或“AI裸奔”，我们主要通过“双引擎驱动”和“原生融合”的策略来解决。

**以智增效：让安全成为创新加速器**

很多企业担心：上了安全措施，AI应用会不会变慢？我们的答案是：用更聪明的AI去解决安全效率问题。

绿盟“风云卫”AI安全能力平台，本质上就是一个“安全效率倍增器”。它将AI能力“原子化”地嵌入安全运营的每一个环节，让过去需要大量人工的重复性工作变得自动化、智能化。面对海量安全告警，我们的AI安全运营中心可以实现“AI优化AI”的能效革命，大幅提升安全事件的处置效率。

**为AI“上险”：拒绝“裸奔”式创新**

我们坚决反对“先狂奔、再补胎”的裸奔式创新。当企业把核心业务交给大模型时，大模型本身的幻觉、数据泄露、提示词注入等风险，就成了企业的“阿喀琉斯之踵”。

绿盟的做法是构建一套从 “事前评估、事中防护、事后审计”的AI原生纵深防御体系，形象地说就是给大模型穿上“金钟罩”。我们推出的“清风卫”系列安全防护产品，能在模型运行时实时防御各类新型攻击。同时，针对合规要求，绿盟大模型备案服务能够帮助企业构建“可自证”的合规体系，提前预见风险，规避千万级罚款风险。

凭借二十多年的攻防实战经验，绿盟科技致力于成为您智能化转型路上最可靠的“副驾驶”——帮您看清路况、预警风险，让您可以更安心地手握方向盘，专注于业务创新的加速与超越，共同驶向智能化的未来。

OpenClaw的“虾”来了，别让您的网络成为坏虾的“养殖场”。立即行动，为您的AI应用加上一道“安全护栏”！

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2U9Z8mUD)

#### 你可能感兴趣的

* [![]()

  一大波危险的“龙虾”来袭，绿盟君助您安全养虾](https://www.4hou.com/posts/Arj9)
* [![]()

  代码钟馗启动AI漏洞雷达，OpenClaw隐秘漏洞浮出水面](https://www.4hou.com/posts/vwK8)
* [![]()

  梆梆安全荣膺中关村网信联盟 “2025年度联盟最佳合作伙伴单位” ，以生态协同筑牢网络安全防线](https://www.4hou.com/posts/mklR)
* [![]()

  起底OpenClaw提示词注入：从“无害话痨”到“主机沦陷”仅需一个网页](https://www.4hou.com/posts/pnrQ)
* [![]()

  无人机企业总工办公室查出窃听器](https://www.4hou.com/posts/gyBr)
* [![]()

  美亚柏科培育的取证圈“小龙虾”来了](https://www.4hou.com/posts/8gwr)

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

这个家伙很懒,什么也没说!

#### 最新文章

* [一大波危险的“龙虾”来袭，绿盟君助您安全养虾](https://www.4hou.com/posts/Arj9)
  2026-04-02 17:32:41
* [代码钟馗启动AI漏洞雷达，OpenClaw隐秘漏洞浮出水面](https://www.4hou.com/posts/vwK8)
  2026-04-02 16:27:08
* [梆梆安全荣膺中关村网信联盟 “2025年度联盟最佳合作伙伴单位” ，以生态协同筑牢网络安全防线](https://www.4hou.com/posts/mklR)
  2026-04-01 15:48:16
* [起底OpenClaw提示词注入：从“无害话痨”到“主机沦陷”仅需一个网页](https://www.4hou.com/posts/pnrQ)
  2026-04-01 11:16:16

[查看更多](https://www.4hou.com/member/aQWl)

# 相关热文

* [一大波危险的“龙虾”来袭，绿盟君助您安全养虾](https://www.4hou.com/posts/Arj9)

  企业资讯
* [代码钟馗启动AI漏洞雷达，OpenClaw隐秘漏洞浮出水面](https://www.4hou.com/posts/vwK8)

  企业资讯
* [梆梆安全荣膺中关村网信联盟 “2025年度联盟最佳合作伙伴单位” ，以生态协同筑牢网络安全防线](https://www.4hou.com/posts/mklR)

  梆梆安全
* [起底OpenClaw提示词注入：从“无害话痨”到“主机沦陷”仅需一个网页](https://www.4hou.com/posts/pnrQ)

  盛邦安全
* [无人机企业总工办公室查出窃听器](https://www.4hou.com/posts/gyBr)

  RC2反窃密实验室
* [美亚柏科培育的取证圈“小龙虾”来了](https://www.4hou.com/posts/8gwr)

  国投智能

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png)...