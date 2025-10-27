---
title: urlscan.io 网站被发现泄露了大量用户的敏感 URL
url: https://www.4hou.com/posts/MBqR
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-10
fetch_date: 2025-10-03T22:13:20.631914
---

# urlscan.io 网站被发现泄露了大量用户的敏感 URL

urlscan.io 网站被发现泄露了大量用户的敏感 URL - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# urlscan.io 网站被发现泄露了大量用户的敏感 URL

xiaohui
[新闻](https://www.4hou.com/category/news)
2022-11-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)176872

收藏

导语：urlscan.io 网站被发现泄露了大量用户的敏感 URL，通过自动化工具可以挖掘出文档分享、密码重置以及团队邀请等敏感链接。

![6358304b4951324ae820a732_urlscan_mining_cover-p-1600.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792811640485.png "1667792408132723.png")

urlscan.io 网站被发现泄露了大量用户的敏感 URL，通过自动化工具可以挖掘出文档分享、密码重置以及团队邀请等敏感链接。使用这种配置错误的安全编排、自动化和响应(SOAR)工具的用户，其帐户通过手动触发的密码重置被劫持的风险很高。

**Github数据泄露**

今年2月，GitHub向受影响的客户发送了一封电子邮件，通知他们数据泄露。具体来说，通过Github Pages为私人存储库启用托管的用户的存储库名称以及他们的用户名被泄露。

开发商似乎没有公开承认这一漏洞，我只是通过黑客新闻(Hacker News)的一篇新闻才知道的。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792813887343.png "1667792438524346.png")

GitHub从一名GitHuc员工的内部发现中得知，GitHubPages网站从GitHub上的私人存储库发布，并被发送到urlscan.io用于元数据分析，作为自动化过程的一部分。

GitHub对此的回应是“修复自动发送GitHub Pages网站进行元数据分析的流程，以便只有公开的GitHub Pages网站被发送进行分析”，并要求第三方删除数据。

**urlscan.io是什么?**

urlscan.io是一项免费的网站扫描和分析服务。当一个 URL 被提交到 urlscan.io 时，一个自动化的过程会像普通用户一样浏览到这个 URL 并记录这个页面导航创建的活动。这包括联系的域和 IP、从这些域请求的资源（JavaScript、CSS 等），以及有关页面本身的其他信息。

urlscan.io将自己描述为“网络沙箱”，你可以提交URL，然后通过各种方式对其进行分析和扫描，主要用于检测钓鱼网站等恶意网站。除了分析通过网站提交的URL外，urlscan.io还扫描来自公共数据源的url，并提供一个API将检查集成到其他产品中，这就导致GitHub对私人存储库URL的系统性数据泄漏。

**大量的数据扫描**

在撰写本文时，登陆页面列出了过去24小时内执行的12万次公开扫描，7万次未公开扫描和43万次私人扫描。它还包括一个“最近扫描”视图，这是典型的安全扫描网站。然而，更令人惊讶的是使用广泛的ElasticSearch Query String语法搜索所有历史数据(作为未经身份验证的用户)的选项。GitHub的通知邮件中也提到了这一点：

urlscan.io在大约30秒内执行分析，或使用将在搜索结果中返回分析的查询进行专门搜索。

对于每个扫描结果，该服务都会提供大量信息：

提交的URL（包含所有GET参数）；

重定向时的有效URL；

抓取/扫描URL时执行的任何HTTP请求；

与之通信的IP和域的信息；

扫描时截取的页面截图；

网站的完整HTML响应；

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792815645472.png "1667792447788303.png")

在urlscan上捕获的OAuth2重定向流和其他加载的资源。提交的URL还包含一个UUID, web应用程序可能不希望这个UUID公开。

**大量的集成**

urlscan.io的文档页面列出了26个商业安全解决方案，这些解决方案由Palo Alto、Splunk、Rapid7、FireEye和ArcSight等供应商通过其API集成了服务。GitHub直接在内部使用这个API作为其SaaS产品的一部分，但它没有出现在这个列表中，可能还有更多的企业客户。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792817115518.png "1667792458214385.png")

urlscan集成在多种商业安全工具中

如果这些 tools/API 用户不小心执行了公共URL扫描，这可能导致系统数据泄漏。由于这些先进的安全工具大多安装在大公司和政府机构，泄露的信息可能特别敏感。

除了商业产品之外，集成页面还列出了22个开源项目，其中一些是信息收集工具，其他是简单的库实现，以便更容易地查询API。

哪些敏感数据可以被泄露？

由于此API的集成类型（例如，通过一个安全工具扫描每个传入的电子邮件并对所有链接执行urlscan），以及数据库中的数据量，匿名用户可以搜索和检索各种敏感数据。

**urlscan.io dorks**

请在下面找到一组可点击的“urlscan.io dorks”和编辑过的示例结果，请注意，在将我们的发现报告给urlscan.io后，他们为下面的许多dorks添加了删除规则。

**密码重置链接**

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792818547235.png "1667792468171760.png")

Instagram密码重置确认页面，请求用户输入两次新密码

**帐户创建链接**

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792819668978.png "1667792478208765.png")

Zendesk上NBC新闻账户的初始密码设置页面

**API密钥**

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792820893553.png "1667792487173182.png")

包含有效VirusTotal API密钥的链接

**Telegram Bot**

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792821176356.png "1667792497326155.png")

Telegram API URL包含一个长的秘密标识符，可用于在机器人上调用不同的API方法。

**DocuSign签名请求**

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792822156584.png "1667792505211085.png")

DocuSign签名请求通常包含带有敏感信息的合同文件

**共享的Google Drive文档**

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792824194190.png "1667792514221790.png")

**Dropbox文件传输**

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792825118972.png "1667792524113750.png")

**Sharepoint invite**

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792827189711.png "1667792537112315.png")

由于SharePoint工作区与组织相关联，子域已经给出了邀请的目的。

**Discord invite**

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792828157858.png "1667792546148503.png")

搜索查询返回了超过7000个不同社区的Discord邀请代码。

**Government Zoom invite**

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792829993533.png "1667792555134736.png")

比Discord邀请更敏感的可能是Zoom邀请，尤其是法庭听证会。

**WebEx会议记录**

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792832134550.png "1667792565118893.png")

**PayPal invoice**

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792834120475.png "1667792579654264.png")

PayPal托管的发票显然包含有效发票所需的所有（个人）信息，任何知道其ID的人都可以检索到。

**Paypal money claim request**

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792835424539.png "1667792591142315.png")

Paypal money claim request“仅”预先填写目标的电子邮件地址（连同金额和收件人），泄露的信息比发票少一点。

**包裹跟踪链接**

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792837207869.png "1667792602163890.png")

还可以找到各种邮政服务的包裹跟踪链接。有趣的是，DHL似乎意识到了跟踪代码泄露的风险，在显示收件人的地址之前，会询问收件人的邮政编码。注意：由于在德国只有8000个邮政编码，而且从包裹跟踪可以知道总体区域，因此代码可能是可猜测的。

**亚马逊礼品配送链接**

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792839914158.png "1667792611127312.png")

亚马逊礼品配送链接会泄露送礼者的姓名和礼物

**退订链接**

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792840548837.png "1667792623345729.png")

HIBP取消订阅链接，允许取消域的违规通知，该域本身没有显示在页面上

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792842109150.png "1667792642185995.png")

在PayPal退订页面上，用户的电子邮件地址完全显示出来。一些其他服务至少部分编辑了退订页面上的电子邮件地址。

有趣的是，当我在2月份进行首次搜索时，我可以找到很多苹果域名的有趣URL：

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792844841052.png "1667792654120608.png")

一个允许设置新密码的Apple开发者ID激活页面

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792845140279.png "1667792664848341.png")

一个允许设置密码的Apple ID最终页面，看起来像是Gamestop账户

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792846175711.png "1667792677537059.png")

家庭共享邀请，允许使用他人购买的订阅，甚至可以访问家庭的照片和设备的位置

![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792847961873.png "1667792688173074.png")

仅限企业的在线活动邀请

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792848182923.png "1667792699145387.png")

当然，iCloud也可以创建公共共享链接，这些链接是通过urlscan.io泄露的。

![27.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792849173789.png "1667792709141285.png")

对于iCloud日历邀请，苹果似乎也创建了一个包含所有信息的链接。

同时，这些信息似乎已从数据库中隐藏或删除：

![28.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221107/1667792851183592.png "1667792719183573.png")

搜索apple.com及其子域名现在只返回两个结果

然而，当持续监控上述结果页面时，有时会发现一些新的附加条目，这些条目在大约10分钟内再次消失。

我们后来发现，苹果同时要求从扫描结果中排除他们的域名，这是通过定期删除所有符合特定规则的扫描...