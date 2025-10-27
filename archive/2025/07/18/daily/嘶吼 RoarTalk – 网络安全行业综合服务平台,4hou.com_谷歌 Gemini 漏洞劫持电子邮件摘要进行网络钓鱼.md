---
title: 谷歌 Gemini 漏洞劫持电子邮件摘要进行网络钓鱼
url: https://www.4hou.com/posts/MXPA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-18
fetch_date: 2025-10-06T23:27:54.652645
---

# 谷歌 Gemini 漏洞劫持电子邮件摘要进行网络钓鱼

谷歌 Gemini 漏洞劫持电子邮件摘要进行网络钓鱼 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 谷歌 Gemini 漏洞劫持电子邮件摘要进行网络钓鱼

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-07-17 14:53:24

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)93877

收藏

导语：由于许多用户很可能相信Gemini的输出是谷歌Workspace功能的一部分，因此很有可能将此警报视为合法警告，而不是恶意注入。

谷歌Gemini for Workspace可以被利用来生成看似合法但包含恶意指令或警告的电子邮件摘要，这些指令可能不使用附件或直接链接将用户引导到网络钓鱼网站。

这种攻击利用隐藏在电子邮件中的间接提示注入，而Gemini在生成消息摘要时遵循这些提示注入。尽管自2024年以来一直有类似的快速攻击报告，安全研究人员也实施了防范措施来阻止误导性响应，但该技术仍然是防不胜防的。

**Gemini漏洞攻击**

Mozilla的GenAI漏洞赏金计划经理Marco Figueroa（研究员）发现，谷歌的Gemini模型遭受了一次提示注入攻击。这个过程包括为Gemini创建一封带有无形指示的电子邮件。攻击者可以使用HTML和CSS将字体大小设置为0，颜色设置为白色，将恶意指令隐藏在消息末尾的正文文本中。

![craft.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250717/1752717136665197.jpg "1752648992765542.jpg")

制作恶意邮件

恶意指令不会在Gmail中呈现，并且由于没有附件或链接，因此消息极有可能到达潜在目标的收件箱。如果收件人打开电子邮件并要求Gemini生成电子邮件摘要，谷歌的人工智能工具将解析这个看不见的指令并服从它。

Figueroa提供的一个示例显示Gemini遵循隐藏的指令，并包含关于用户Gmail密码被泄露的安全警告，以及支持电话号码。

![geminisummary.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250717/1752717138837625.jpg "1752649050510535.jpg")

Gemini漏洞总结结果送达用户

由于许多用户很可能相信Gemini的输出是谷歌Workspace功能的一部分，因此很有可能将此警报视为合法警告，而不是恶意注入。

Figueroa提供了一些检测和缓解方法，安全团队可以应用这些方法来防止此类攻击。一种方法是删除、中和或忽略被设计为隐藏在正文中的内容。

另一种方法是实现一个后处理过滤器，该过滤器扫描Gemini输出以查找紧急消息、网址或电话号码，并标记消息以进行进一步审查。

文章翻译自：https://www.bleepingcomputer.com/news/security/google-gemini-flaw-hijacks-email-summaries-for-phishing/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?86Nqu2AT)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

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