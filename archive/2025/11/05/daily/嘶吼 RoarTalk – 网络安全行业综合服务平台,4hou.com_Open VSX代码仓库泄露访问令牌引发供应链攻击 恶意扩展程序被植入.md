---
title: Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入
url: https://www.4hou.com/posts/KG4z
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-05
fetch_date: 2025-11-06T03:12:05.610356
---

# Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入

Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)11610

收藏

导语：GlassWorm背后的同一批威胁者已转向GitHub平台，他们采用相同的Unicode隐写术技巧隐藏恶意负载。

目前，Open VSX代码仓库已轮换访问令牌——此前开发者在公共代码库中意外泄露了这些令牌，导致威胁者得以通过供应链攻击发布恶意扩展程序。

此次泄露由Wiz公司研究人员于两周前发现，他们当时报告称，微软VSCode和Open VSX应用市场共暴露了550余个敏感信息。

据悉，其中部分敏感信息可用于访问下载量达15万次的项目，使威胁者能够上传恶意版本的扩展程序，造成严重的供应链安全风险。

Open VSX由Eclipse基金会主导开发，是微软Visual Studio应用市场的开源替代方案，后者为VSCode集成开发环境（IDE）提供扩展程序。 Open VSX作为社区驱动的代码仓库，提供与VSCode兼容的扩展程序，供无法使用微软平台的人工智能驱动衍生工具（如Cursor和Windsurf）使用。

**GlassWorm恶意软件 campaign**

泄露的部分令牌在数日后被用于一场名为“GlassWorm”的恶意软件攻击活动。Koi Security研究人员报告称，GlassWorm将一款自我传播型恶意软件隐藏在不可见的Unicode字符中，试图窃取开发者凭证，并在所有可触及的项目中引发连锁性数据泄露。这些攻击还针对49个扩展程序中的加密货币钱包数据，表明攻击者的动机可能是获取经济利益。

Open VSX团队及Eclipse基金会发布博客文章回应此次攻击活动与令牌泄露事件，称GlassWorm实际上并不具备自我复制能力，但确实以开发者凭证为攻击目标。

Open VSX团队澄清道：“涉事恶意软件旨在窃取开发者凭证，进而扩大攻击者的影响范围，但它不会自主通过系统或用户设备传播。”报告中提到的3.58万次下载量高估了实际受影响用户数量，其中包含攻击者利用机器人和提升曝光度的手段制造的虚假下载量。”

尽管如此，事件在接到通知后迅速得到控制。截至10月21日，所有恶意扩展程序已从Open VSX代码仓库中移除，相关访问令牌也已完成轮换或撤销。

Open VSX目前已确认，事件已完全得到控制，无持续影响，且计划实施额外安全措施以防范未来攻击。

**四、后续安全强化措施**

此次将实施的安全增强措施如下：

1. 缩短令牌有效期，降低泄露后的影响范围；

2. 推出更快速的泄露凭证撤销流程；

3. 扩展程序发布时进行自动化安全扫描；

4. 与VSCode及其他应用市场合作，共享威胁情报。

需要注意的是，有媒体向Eclipse基金会发送邮件，询问总共轮换了多少个令牌，但截至目前尚未收到回应。

与此同时，Aikido公司报告称，GlassWorm背后的同一批威胁者已转向GitHub平台，他们采用相同的Unicode隐写术技巧隐藏恶意负载。

研究人员表示，该攻击活动已扩散至多个代码仓库，其中大部分集中在JavaScript项目。此次转向GitHub表明，该威胁仍在活跃，在被曝光后迅速在开源生态系统中转移攻击目标。

文章翻译自：https://www.bleepingcomputer.com/news/security/open-vsx-rotates-tokens-used-in-supply-chain-malware-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BEoUjs52)

#### 你可能感兴趣的

* [![]()

  Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
* [![]()

  8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)
* [![]()

  黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)
* [![]()

  超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)
* [![]()

  工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)
* [![]()

  新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)
  2025-11-05 12:00:00
* [8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)
  2025-11-05 10:37:58
* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)
  2025-10-31 12:00:00
* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)
  2025-10-29 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Open VSX代码仓库泄露访问令牌引发供应链攻击 恶意扩展程序被植入](https://www.4hou.com/posts/KG4z)

  胡金鱼
* [8项公共安全行业标准获批发布](https://www.4hou.com/posts/OG4G)

  胡金鱼
* [黑客利用基于redtiger的信息窃取工具窃取Discord账户](https://www.4hou.com/posts/mkoA)

  胡金鱼
* [超 26.6 万台 F5 BIG-IP 设备暴露 面临远程攻击风险](https://www.4hou.com/posts/1M83)

  胡金鱼
* [工信部通报20款智能终端存在侵害用户权益行为](https://www.4hou.com/posts/pn01)

  胡金鱼
* [新型恶意攻击瞄准macOS用户 仿冒三大平台植入窃密软件](https://www.4hou.com/posts/ZgJv)

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