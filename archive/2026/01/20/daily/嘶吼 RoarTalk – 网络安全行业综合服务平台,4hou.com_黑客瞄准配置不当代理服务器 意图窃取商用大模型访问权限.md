---
title: 黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限
url: https://www.4hou.com/posts/qogk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-20
fetch_date: 2026-01-21T03:31:35.530983
---

# 黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限

黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)14887

收藏

导语：该扫描基础设施此前曾与广泛的漏洞利用活动有关联，这表明此次枚举是有组织侦察工作的一部分，目的是编目可访问的 LLM 服务。

黑客正在系统性地搜寻配置不当的代理服务器，试图通过这些服务器获取对商用大语言模型（LLM）服务的访问权限。

在这场始于2025年12月下旬的持续攻击活动中，攻击者已探测了超过73个LLM端点，并生成了8万多个会话。

据威胁监测平台GreyNoise称，这些威胁组织使用”低噪声“提示词来查询端点，试图在不触发安全警报的情况下，确认所访问的AI模型类型。

**灰帽行动**

GreyNoise 在一份报告中指出，在过去四个月里，其Ollama蜜罐共捕获了91,403次攻击，这些攻击分属两个截然不同的活动。

其中一个行动始于10月，目前仍在活跃中，在圣诞节前后的48小时内出现了1,688次会话的峰值。该行动利用 服务器端请求伪造（SSRF）漏洞，迫使服务器连接到攻击者控制的外部基础设施。

该行动背后的攻击者通过利用 Ollama 的模型拉取功能，注入恶意注册表 URL，并通过 MediaURL 参数集成 Twilio SMS 网络钩子来实现其目标。

然而，基于所使用的工具可以判断出，该活动可能源自安全研究人员或漏洞赏金猎人，因为他们使用了 ProjectDiscovery 的OAST（带外应用安全测试）基础设施，这通常用于漏洞评估。

遥测数据显示，该活动源自27个国家的62个IP地址，这些地址表现出类似 VPS 的特征，而非僵尸网络操作的迹象。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260112/1768201612611661.png "1768201181353159.png")

 活动时间轴

第二个活动始于12月28日，研究员检测到大规模的枚举行为，旨在识别暴露或配置不当的 LLM 端点。 在11天内，该活动生成了80,469个会话，两个IP地址使用 OpenAI 兼容格式和 Google Gemini API 格式，系统性地探测了73个以上的模型端点。

目标模型列表涵盖了所有主要提供商的产品，包括：

**·**OpenAI (GPT-4o 及变体)

**·**Anthropic (Claude Sonnet, Opus, Haiku)

**·**Meta (Llama 3.x)

**·**DeepSeek (DeepSeek-R1)

**·**Google (Gemini)

**·**Mistral

**·**Alibaba (Qwen)

**·**xAI (Grok)

为了在测试对 LLM 服务的访问时避免触发安全警报，攻击者使用了无害的查询，例如简短的问候语、空输入或事实性问题。

该扫描基础设施此前曾与广泛的漏洞利用活动有关联，这表明此次活动是有组织侦察工作的一部分，目的是编目可访问的 LLM 服务。报告并未声称在发现后观察到了利用、数据盗窃或模型滥用行为，但该活动仍表明存在恶意意图。

研究人员称：8万个枚举请求代表了一种投入，如果没有使用该地图的计划，威胁组织不会以这种规模绘制基础设施地图。

为了防御此类活动，建议将 Ollama 模型拉取限制在受信任的注册表，应用出口过滤，并在 DNS 级别阻止已知的 OAST 回调域。 针对其的措施包括对可疑的 ASN 实施速率限制，以及监控与自动化扫描工具相关的 JA4 网络指纹。

文章来源自：https://www.bleepingcomputer.com/news/security/hackers-target-misconfigured-proxies-to-access-paid-llm-services/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ppolxbiV)

#### 你可能感兴趣的

* [![]()

  国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/Zgk8)
* [![]()

  黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限](https://www.4hou.com/posts/qogk)
* [![]()

  盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)
* [![]()

  BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众](https://www.4hou.com/posts/pn4m)
* [![]()

  云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)
* [![]()

  新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/Zgk8)
  2026-01-21 10:41:50
* [黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限](https://www.4hou.com/posts/qogk)
  2026-01-20 12:00:00
* [盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)
  2026-01-14 12:00:00
* [BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众](https://www.4hou.com/posts/pn4m)
  2026-01-14 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/Zgk8)

  胡金鱼
* [黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限](https://www.4hou.com/posts/qogk)

  胡金鱼
* [盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)

  山卡拉
* [BreachForums黑客论坛再遭数据泄露 用户数据库被公之于众](https://www.4hou.com/posts/pn4m)

  胡金鱼
* [云文件共享平台成为企业数据盗窃攻击的目标](https://www.4hou.com/posts/0MwV)

  胡金鱼
* [新型网络犯罪工具ErrTraffic实现ClickFix攻击自动化 伪造网站故障诱骗用户中招](https://www.4hou.com/posts/YZ1O)

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