---
title: Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马
url: https://www.4hou.com/posts/J1GK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-04-08
fetch_date: 2026-04-09T04:30:13.209395
---

# Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马

Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-04-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10317

收藏

导语：从以往案例来看，攻击者往往会迅速借热点公开事件发动机会主义攻击，借机入侵目标设备。

威胁组织正利用近期Claude Code源代码泄露事件，通过伪造GitHub仓库向用户分发Vidar窃密木马。

Claude Code是人工智能公司Anthropic推出的一款终端版AI代理工具，可直接在终端中执行编程任务，作为自主代理实现系统直接交互、大语言模型API调用管理、MCP集成以及持久化记忆等功能。

据悉，Anthropic在发布npm包时因疏忽，意外嵌入了一个大小为59.8MB的JavaScript源码映射文件，导致这款新工具的完整客户端源代码被公开泄露。

此次泄露包含1906个文件、共计51.3万行未做混淆处理的TypeScript代码，暴露了该AI代理的调度逻辑、权限与执行机制、隐藏功能、编译细节以及多项安全相关核心实现。

泄露代码很快被大量用户下载并上传至GitHub，出现数千次复刻分叉。

Zscaler在一份报告中指出，此次源码泄露为威胁组织创造了可乘之机，使其能够向搜索Claude Code泄露内容的用户投放Vidar窃密软件。

研究人员发现，一个由用户“idbzoomh”发布的恶意GitHub仓库上传了伪造的泄露版本，并宣称该版本“解锁企业级功能”且无使用限制。

![图片62.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260403/1775200989166015.png "1775200989166015.png")

GitHub代码库传播恶意软件

为吸引更多流量，该仓库针对搜索引擎做了优化，在谷歌搜索“leaked Claude Code”等关键词时会出现在前列位置。

![图片63.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260403/1775201015366631.png "1775201015366631.png")

恶意GitHub代码库的搜索结果

据研究人员分析，用户下载到一个7-Zip压缩包，其中包含一个名为ClaudeCode\_x64.exe的Rust语言可执行程序。该程序运行后，会释放投放通用窃密木马Vidar，同时安装GhostSocks网络流量代理工具。

Zscaler监测发现，该恶意压缩包会频繁更新，未来不排除被加入其他恶意载荷的可能。

研究人员还发现了第二个代码完全相同的GitHub仓库，但该仓库中的“下载ZIP”按钮在分析期间处于失效状态。Zscaler判断，该仓库由同一威胁组织运营，很可能用于测试不同的投放传播策略。

![图片64.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260403/1775201041172022.png "1775201041172022.png")

第二个与同一威胁者关联的GitHub代码库

尽管GitHub平台具备安全防护机制，仍频繁被攻击者用于以各种伪装方式分发恶意载荷。

在2025年末的多轮攻击活动中，威胁组织就曾针对经验不足的研究人员或黑客，在仓库中谎称存放最新披露漏洞的概念验证（PoC）利用代码。

从以往案例来看，攻击者往往会迅速借热点公开事件发动机会主义攻击，借机入侵目标设备。

文章翻译自：https://www.bleepingcomputer.com/news/security/claude-code-leak-used-to-push-infostealer-malware-on-github/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?19am2ZN5)

#### 你可能感兴趣的

* [![]()

  新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)
* [![]()

  嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)
* [![]()

  Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马](https://www.4hou.com/posts/J1GK)
* [![]()

  嘶吼安全动态｜国家安全部提醒：“囤词元暴富” 背后，暗藏间谍窃取数据陷阱 苹果Mac威胁50.32%来自木马，盗窃用户隐私成主要目的](https://www.4hou.com/posts/YZoA)
* [![]()

  多国联合行动捣毁全球最大DDoS僵尸网络团伙](https://www.4hou.com/posts/kgJv)
* [![]()

  嘶吼安全动态｜工信部NVDB平台发布风险提示：利用苹果iOS漏洞的攻击活动激增 黑客利用React2Shell发起自动化凭证窃取活动](https://www.4hou.com/posts/OGVR)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)
  2026-04-09 12:00:00
* [嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)
  2026-04-09 11:59:00
* [Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马](https://www.4hou.com/posts/J1GK)
  2026-04-08 12:00:00
* [嘶吼安全动态｜国家安全部提醒：“囤词元暴富” 背后，暗藏间谍窃取数据陷阱 苹果Mac威胁50.32%来自木马，盗窃用户隐私成主要目的](https://www.4hou.com/posts/YZoA)
  2026-04-08 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)

  胡金鱼
* [嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)

  胡金鱼
* [Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马](https://www.4hou.com/posts/J1GK)

  胡金鱼
* [嘶吼安全动态｜国家安全部提醒：“囤词元暴富” 背后，暗藏间谍窃取数据陷阱 苹果Mac威胁50.32%来自木马，盗窃用户隐私成主要目的](https://www.4hou.com/posts/YZoA)

  胡金鱼
* [多国联合行动捣毁全球最大DDoS僵尸网络团伙](https://www.4hou.com/posts/kgJv)

  胡金鱼
* [嘶吼安全动态｜工信部NVDB平台发布风险提示：利用苹果iOS漏洞的攻击活动激增 黑客利用React2Shell发起自动化凭证窃取活动](https://www.4hou.com/posts/OGVR)

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