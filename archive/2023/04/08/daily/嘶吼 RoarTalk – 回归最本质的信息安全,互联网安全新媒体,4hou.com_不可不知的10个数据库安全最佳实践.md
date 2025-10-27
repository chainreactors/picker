---
title: 不可不知的10个数据库安全最佳实践
url: https://www.4hou.com/posts/kjQx
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-08
fetch_date: 2025-10-04T11:29:36.313410
---

# 不可不知的10个数据库安全最佳实践

不可不知的10个数据库安全最佳实践 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 不可不知的10个数据库安全最佳实践

布加迪
[趋势](https://www.4hou.com/category/observation)
2023-04-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)173105

收藏

导语：本文介绍的10个数据库安全最佳实践可以帮助贵组织加强敏感数据的安全性。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230407/1680833896170871.jpeg "1680393170201332.jpeg")

据Flashpoint公司的《2022年年度回顾报告》显示，2022年1月到12月间约有390亿条数据记录被盗。虽然这个结果令人相当吃惊，但也明确地传达出了组织需要采取有效的数据库安全措施这一讯号。

数据库安全措施与网站安全实践略有不同。前者涉及物理措施、软件解决方案，甚至员工安全教育。然而，保护站点尽量减少网络犯罪分子可能利用的潜在攻击途径同样重要。

下面列出了10个数据库安全最佳实践，可以帮助贵组织加强敏感数据的安全性。

**1. 部署物理数据库安全措施**

数据中心或自有服务器很容易遭到外部人员或者甚至恶意内部威胁的物理攻击。如果网络犯罪分子能够接触物理数据库服务器，就能盗取数据、破坏数据，甚至植入有害的恶意软件以获取远程访问权。如果缺乏额外的安全措施，常常难以检测这种类型的攻击，因为它们能够绕过数字安全规程。

如果贵组织保管自己的服务器，强烈建议增添物理安全措施，比如摄像头和锁具，并配备安保人员。此外，还应将任何访问物理服务器的活动记入日志，只允许特定人员访问，从而缓解恶意活动的风险。确保服务器机房物理安全的标准包括如下：

ISO 27001

ISO 20000-1

NIST SP（SP 800-14、SP 800-23和SP 800-53）

美国国防部信息保证技术框架

SSAE 18 SOC 1 Type II、SOC 2 Type II和SOC 3

**2. 隔离数据库服务器**

数据库需要采取专门的安全措施来免遭网络攻击。此外，将数据与网站放到同一台服务器上也将数据暴露在了针对网站的不同攻击途径的面前。

假设你在运营一家在线商店，并且把网站、非敏感数据和敏感数据统统放在同一台服务器上。当然，你可以利用托管服务供应商提供的安全措施以及电子商务平台的安全功能来防范网络攻击和欺诈。然而，你的敏感数据现在很容易因这个网站和在线商店平台而遭到攻击。攻陷网站或在线商店平台的任何攻击都使网络犯罪分子也有可能访问你的数据库。

想要缓解这些安全风险，不妨将你的数据库服务器与其他一切系统隔离开来。此外，采用实时安全信息和事件管理（SIEM），这种解决方案专门用于确保数据库安全，让组织在有人企图攻击时可以立即采取行动。此外，漏洞管理解决方案有助于组织准确地评估每一个网络资产的安全风险。

**3. 搭建HTTPS代理服务器**

在工作站访问数据库服务器之前，代理服务器负责评估从工作站发出的请求。这样一来，代理服务器充当守门员，旨在挡住非授权请求。

最常见的代理服务器基于HTTP。然而，如果你在处理敏感信息，比如密码、支付信息或个人信息，那就应该搭建一台HTTPS服务器。这样一来，透过代理服务器传输的数据也经过加密，从而增添了一层安全。

**4. 避免使用默认网络端口**

TCP协议和UDP协议用于服务器之间传输数据的时候。设置这些协议时，它们会自动使用默认网络端口。

由于默认端口很常见，它们常常用于蛮力攻击中。如果不使用默认端口，盯上你服务器的网络攻击者就必须尝试不同的端口号，不断试错。由于需要费更大的劲，这会打消攻击者企图攻击你的念头。

然而，在分配新端口时，记得查一下互联网号码分配机构（IANA）的端口注册库，确保新端口没有被其他服务占用。

**5. 使用实时数据库监控**

主动扫描数据库检查有无企图攻击的活动，这可以夯实安全，并有助于应对潜在攻击。

可以使用Tripwire的实时文件完整性监控（FIM）之类的监控软件，记录数据库服务器上的所有活动，一发现异常就发出报警。此外，确立逐级上报流程以应对潜在攻击，从而让敏感数据更安全。

另一个需要考虑的方面是定期审计数据库安全，并组织进行网络安全渗透测试。这些措施有助于发现潜在的安全漏洞，在数据泄露发生之前打上补丁。

**6. 使用数据库防火墙和Web应用防火墙**

防火墙是阻挡有人企图恶意访问的第一道防线。除了防护网站外，你还应该安装防火墙来保护数据库远离不同的攻击途径。

有三种类型的防火墙常用于保护网络安全：

数据过滤防火墙。

有状态数据包检测（SPI）。

代理服务器防火墙。

务必确保防火墙的配置已全面顾及任何安全漏洞。另外，及时更新防火墙也必不可少，因为这样才能保护站点和数据库远离新型网络攻击方法。

**7. 部署数据加密协议**

对数据进行加密不仅对于保护商业机密很重要，对于传输或存储敏感的用户信息、防范勒索软件或者遵守GDPR之类的数据隐私法规同样很重要。

部署数据加密协议降低了数据泄露的风险。这意味着，即使网络犯罪分子获得了你的数据，这些信息也仍然是安全的。这还意味着，你的数据不仅在静态时保持安全，在传输中也保持安全，而传输中的数据常常是最容易受到攻击的。

**8. 创建数据库的定期备份**

虽然为网站创建备份很常见，但定期为数据库创建备份、对一份副本进行加密同样很重要。这么做可以缓解因恶意攻击或数据损坏而导致敏感信息丢失的风险。最佳实践建议遵循3-2-1备份规则：

•••存储数据的三份副本。

使用两种类型的存储介质。

将一份副本存储在异地位置。

CIS控制11：数据恢复（https://www.tripwire.com/state-of-security/cis-control-11）概述了数据恢复计划的步骤，并强调了这么做的重要性：不仅创建备份，还测试团队将备份用于生产环境的能力。关键任务基础设施的备份应定期加以测试。这不仅仅是为了验证备份的完整性。还为了确保工作人员拥有及时恢复所需的知识和经验。

**9. 及时更新应用程序**

研究显示，88%的代码库含有过时的软件组件。此外，过时插件容易招致利用漏洞的恶意软件，并留下敞开的漏洞，黑客可以用来转而进入到组织网络的其他地方。如果考虑一下你用来管理数据库或甚至运行网站的软件，这就带来了重大的安全风险。

虽然你应该只使用值得信赖、经过验证的数据库管理软件，但也应该及时更新这类软件，并在第一时间安装新的补丁。对于窗口组件、插件和第三方应用程序来说也是如此，另外一个建议是避免使用那些没有定期更新的应用程序，对它们要完全避而远之。

**10. 采用强用户身份验证**

据韦里逊（Verizon）的《2022年数据泄露调查报告》显示，去年67%的数据泄露事件由凭据被盗导致。众所周知，单因素身份验证（SFA）方法也不安全，难怪有人认为密码已死。建议对社交媒体网站也要采取最基本的双因素身份验证（2FA），多因素身份验证（MFA）通常被公认为是如今确保安全用户身份验证的标准。它对于帮助组织有资格领取网络保险也起到了关键作用。

然而形势在发生变化，犯罪分子纷纷绕过MFA检查点以访问云资源，大多数组织很快有可能采用无密码。

此外，考虑只允许经过验证的IP地址访问数据库，以进一步缓解潜在的数据泄露风险。虽然IP地址有可能被复制或屏蔽，但这需要攻击者花更大的精力。

**加强数据库安全，缓解数据泄露风险**

用行业标准最佳实践保护数据库为贵组织的零信任方法提供了另一层纵深防御机制。

由于数据泄露事件越来越频繁，威胁分子越来越有可能潜入到贵组织的网络中。事先用存储加密数据做好防备的组织最有可能恢复数据。

本文翻译自：https://www.tripwire.com/state-of-security/database-security-best-practices-you-should-know如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?aq1YDAWv)

#### 你可能感兴趣的

* [![]()

  AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
* [![]()

  2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
* [![]()

  【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
* [![]()

  随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
* [![]()

  关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)
* [![]()

  2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)
  2025-09-30 12:00:00
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)
  2025-09-02 12:00:00
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)
  2025-06-06 16:28:40
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)
  2025-05-09 12:00:00

[查看更多](https://www.4hou.com/member/VGrO)

# 相关热文

* [AI部署热潮下潜在的网络安全风险](https://www.4hou.com/posts/6ME7)

  胡金鱼
* [2025年夏季网络安全攻击事件激增](https://www.4hou.com/posts/mk4O)

  胡金鱼
* [【梆梆安全监测】安全隐私合规监管趋势报告（5月1日－5月16日）](https://www.4hou.com/posts/OGpL)

  梆梆安全
* [随着全球紧张局势加剧，针对能源行业的网络威胁激增](https://www.4hou.com/posts/1MDm)

  胡金鱼
* [关于人工智能钓鱼攻击的分析](https://www.4hou.com/posts/RX7E)

  胡金鱼
* [2024年勒索软件支付下降35%，总计8.135亿美元](https://www.4hou.com/posts/NGG8)

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