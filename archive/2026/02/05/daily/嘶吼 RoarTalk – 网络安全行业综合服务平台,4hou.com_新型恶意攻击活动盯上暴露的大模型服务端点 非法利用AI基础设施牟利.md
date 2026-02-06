---
title: 新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利
url: https://www.4hou.com/posts/pnNm
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-05
fetch_date: 2026-02-06T04:08:32.963346
---

# 新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利

新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8769

收藏

导语：研究人员在40天的监测中，于蜜罐系统上记录到超3.5万次攻击会话，由此发现这起大规模网络犯罪活动。

一款恶意攻击活动正针对暴露在外的大语言模型服务端点展开精准攻击，通过非法获取AI基础设施的未授权访问权限实现商业化牟利。

研究人员在40天的监测中，于蜜罐系统上记录到超3.5万次攻击会话，由此发现这起大规模网络犯罪活动——攻击者通过利用暴露或认证机制存在缺陷的AI服务端点，将非法访问权限变现并实施一系列恶意操作。

研究人员将该攻击活动命名为Bizarre Bazaar，并指出这是首起可明确归因于特定威胁组织的“大模型劫持”（LLMjacking）攻击案例。

研究人员称攻击者通过获取防护薄弱的大模型基础设施端点未授权访问权限，主要实施以下恶意行为：

1. 窃取计算资源用于虚拟货币挖矿；

2. 在暗网市场转售API访问权限；

3. 窃取提示词与对话记录中的数据；

4. 试图通过模型上下文协议（MCP）服务器横向渗透至内部系统。

该攻击活动的常见攻击载体包括：自部署的大模型环境、暴露在外或未做认证的AI接口、公网可访问的MCP服务器，以及分配了公网IP的AI开发/测试环境。

攻击者通常利用各类配置漏洞发起攻击，例如11434端口上未做认证的Ollama服务端点、8000端口上兼容OpenAI协议的未认证接口，以及未做权限校验的生产环境聊天机器人。

研究人员指出，一旦存在配置漏洞的服务端点出现在Shodan、Censys等网络空间测绘平台的扫描结果中，攻击者会在数小时内发起针对性攻击。

这类威胁与传统的接口滥用存在本质区别，被攻陷的大模型服务端点不仅会产生高额成本——大模型推理计算的开销本就居高不下，还会导致企业敏感数据泄露，更会为攻击者提供横向渗透的可乘之机。

此前，GreyNoise的一份报告也曾披露过类似攻击行为，彼时攻击者主要针对商用大模型服务展开信息探测。

而此次研究则发现，这起攻击活动背后形成了一条犯罪供应链，涉及三名威胁者，且三者大概率为同一犯罪团伙协同作案：

第一位通过自动化机器人对全网进行扫描，寻找大模型及MCP服务端点；

第二位体对扫描结果进行验证，测试目标端点的访问权限；

第三位行为体则在Telegram、Discord等平台运营着一个名为silver[.]inc的商业化服务平台，将非法获取的AI服务访问权限以虚拟货币或PayPal转账的方式转售牟利。

该平台还推出了一个名为NeXeonAI的项目，对外宣称是“一体化AI基础设施”，可提供50余款头部厂商的大模型访问权限。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260129/1769670142168078.png "1769669867377595.png")

Bizarre Bazaar行动阶段

研究人员还将这起犯罪活动溯源至一名特定威胁者，该行为体曾使用“Hecker”“Sakuya”“LiveGamer101”等多个别名。

除了聚焦大模型接口滥用的Bizarre Bazaar，还监测到另一起独立的攻击活动，该活动专门针对MCP服务端点展开侦察探测。

针对MCP端点的攻击，能为攻击者创造更多横向渗透的机会——可通过与Kubernetes容器平台交互、获取云服务访问权限、执行Shell命令等方式进一步入侵，其背后的牟利价值远高于单纯利用计算资源挖矿的变现手段。

目前尚无证据表明这起MCP端点攻击活动与Bizarre Bazaar存在关联，但安全研究人员推测，二者或有潜在联系。

文章来源自：https://www.bleepingcomputer.com/news/security/hackers-hijack-exposed-llm-endpoints-in-bizarre-bazaar-operation/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?2a2aMM73)

#### 你可能感兴趣的

* [![]()

  盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)
* [![]()

  新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)
* [![]()

  Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)
* [![]()

  新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)
* [![]()

  豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)
* [![]()

  2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)
  2026-02-06 12:00:00
* [新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)
  2026-02-05 12:00:00
* [Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)
  2026-02-04 12:00:00
* [新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)
  2026-02-03 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)

  山卡拉
* [新型恶意攻击活动盯上暴露的大模型服务端点 非法利用AI基础设施牟利](https://www.4hou.com/posts/pnNm)

  胡金鱼
* [Moltbot AI 助手企业部署引发数据安全隐患 或致API密钥等敏感数据泄露](https://www.4hou.com/posts/omMk)

  胡金鱼
* [新型PDFSider Windows恶意软件瞄准金融企业实施勒索攻击](https://www.4hou.com/posts/W15n)

  胡金鱼
* [豆包手机掀起 AI 风暴：智能便利背后的安全与规则之争](https://www.4hou.com/posts/xyYE)

  山卡拉
* [2026年网络安全预测：AI驱动攻击加剧，防御需更智能、更持续](https://www.4hou.com/posts/rpjW)

  胡金鱼

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