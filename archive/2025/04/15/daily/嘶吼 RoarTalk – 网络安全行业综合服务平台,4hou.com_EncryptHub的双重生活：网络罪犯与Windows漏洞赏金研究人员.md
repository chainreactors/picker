---
title: EncryptHub的双重生活：网络罪犯与Windows漏洞赏金研究人员
url: https://www.4hou.com/posts/kgP6
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-04-15
fetch_date: 2025-10-06T22:04:05.546652
---

# EncryptHub的双重生活：网络罪犯与Windows漏洞赏金研究人员

EncryptHub的双重生活：网络罪犯与Windows漏洞赏金研究人员 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# EncryptHub的双重生活：网络罪犯与Windows漏洞赏金研究人员

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-04-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)53326

收藏

导语：EncryptHub还与利用微软管理控制台漏洞CVE-2025-26633的Windows零日攻击有关。

据悉，臭名昭著的威胁分子EncryptHub向微软报告了两个Windows零日漏洞，揭示了介于网络犯罪和安全研究之间的矛盾人物。

报告的漏洞是CVE-2025-24061 （Web绕过标记）和CVE-2025-24071（文件浏览器欺骗），微软在2025年3月的补丁星期二更新中解决了这些漏洞，并承认报告者为“SkorikARI与SkorikARI”。

![MS.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744098472109214.png "1744096044597830.png")

错误报道

Outpost24研究人员的一份新报告现已将EncryptHub威胁者与SkorikARI联系起来，据称该威胁者感染了自己并暴露了他们的凭证。

这种暴露使研究人员能够将威胁者与各种在线账户联系起来，并暴露出在网络安全研究人员和网络罪犯之间摇摆不定的人的个人资料。

其中一个被曝光的账户是SkorikARI，黑客利用这个账户向微软披露了上述两个零日漏洞，从而提高了Windows的安全性。

Outpost24的安全分析师Hector Garcia表示，SkorikARI与EncryptHub的联系是基于多个证据，构成了一个高可信度的评估。最确凿的证据是，EncryptHub从自己的系统中窃取的密码文件中，既有与EncryptHub相关的账户，比如仍在开发中的EncryptRAT的凭据，也有他在xss上的账户。

对SkorikARI来说，这就像访问自由职业网站或他自己的Gmail账户。

此外，另一个证实两者之间联系的重要证据是与ChatGPT的对话，可以观察到与EncryptHub和SkorikARI相关的活动。

EncryptHub对零日攻击并不新鲜，威胁者或其中一名成员试图在黑客论坛上向其他网络罪犯出售零日攻击。

![zeroday-darkweb.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744098474745847.png "1744096149854143.png")

EncryptHub试图在地下论坛上出售零日漏洞

Outpost24深入研究了EncryptHub的经历，指出这名黑客反复在自由开发工作和网络犯罪活动之间转换。

尽管他有明显的IT专业知识，但据报道，这名黑客成为了opsec实践的受害者，导致他的个人信息被曝光。

这包括黑客使用ChatGPT来开发恶意软件和网络钓鱼网站，集成第三方代码，以及研究漏洞。

这位威胁者还与OpenAI的LLM聊天机器人进行了更深入的个人接触，在一个案例中，他描述了自己的成就，并要求人工智能将他归类为酷黑客或恶意研究人员。

根据提供的输入，ChatGPT将他评估为40%黑帽，30%灰帽，20%白帽和10%不确定。

同样的冲突也反映在他未来对ChatGPT的计划中，黑客要求聊天机器人帮助组织一场大规模但“无害”的活动，影响数万台计算机进行宣传。

![future-plan.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744098475487378.png "1744096248348146.png")

公开ChatGPT讨论

**EncryptHub是什么**

EncryptHub是一个威胁分子，与RansomHub和BlackSuit等勒索软件团伙有一定联系。

然而，最近，威胁者通过各种社会工程活动、网络钓鱼攻击和创建基于powershell的自定义信息窃取器“善变窃取者”而出名。

威胁者还以进行社会工程活动而闻名，他们为虚构的应用程序创建社交媒体配置文件和网站。

在一个例子中，研究人员发现，威胁者为一个名为GartoriSpace的项目管理应用程序创建了一个X帐户和网站。

![gatorispace-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250408/1744098476127972.png "1744096330102051.png")

假冒GartoriSpace网站

该网站通过社交媒体平台上的私人信息进行推广，这些信息将提供下载该软件所需的代码。当下载软件时，Windows设备会收到一个安装了善变窃取软件的PPKG文件[VirusTotal]，而Mac设备会收到一个AMOS信息窃取软件[VirusTotal]。

EncryptHub还与利用微软管理控制台漏洞CVE-2025-26633的Windows零日攻击有关。该漏洞在3月份被修复。总的来说，威胁者的活动似乎是为他们工作的，据报告称，威胁者已经破坏了600多个组织。

文章翻译自：https://www.bleepingcomputer.com/news/security/encrypthubs-dual-life-cybercriminal-vs-windows-bug-bounty-researcher/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?IBtms65U)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

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