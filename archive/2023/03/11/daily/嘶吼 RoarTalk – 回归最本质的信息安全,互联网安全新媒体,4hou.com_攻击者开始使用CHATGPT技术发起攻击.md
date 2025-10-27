---
title: 攻击者开始使用CHATGPT技术发起攻击
url: https://www.4hou.com/posts/vJV5
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-11
fetch_date: 2025-10-04T09:12:43.544334
---

# 攻击者开始使用CHATGPT技术发起攻击

攻击者开始使用CHATGPT技术发起攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者开始使用CHATGPT技术发起攻击

lucywang
[新闻](https://www.4hou.com/category/news)
2023-03-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)173985

收藏

导语：CPR对几个主要地下黑客社区的分析表明，已经有攻击者使用OpenAI开发恶意工具了。

![微信截图_20230107170914.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673082999942740.png "1673082999942740.png")

2022年11月底，OpenAI发布了用于其大型语言模型（LLM）的新界面ChatGPT，这立即引发了人们对AI及其可能用途的关注。这就意味着，ChatGPT也可以被应用到现代网络攻击，因为代码生成可以帮助技术不太熟练的攻击者毫不费力地发动网络攻击。

在上一篇文章《爆火出圈的chatGPT如何在逆向和恶意软件分析中发挥作用》中，我们描述了ChatGPT如何成功地进行了完整的感染流程，从创建令人信服的鱼叉式钓鱼电子邮件到运行能够接受英语命令的反向shell。目前的问题是，这是否只是一个假设的威胁，或者是否已经有攻击者使用OpenAI技术进行恶意攻击了。

CPR对几个主要地下黑客社区的分析表明，已经有攻击者使用OpenAI开发恶意工具了。正如我们所怀疑的，一些示例清楚地表明，许多使用OpenAI的攻击者根本没有开发技能。尽管我们在本报告中介绍的工具非常基础，但基于AI的工具改在成复杂的威胁只是时间问题。

**示例1：创建Infostealer**

2022年12月29日，一个名为“ChatGPT——恶意软件的好处”的帖子出现在一个流行的地下黑客论坛上。该帖子的发布者透露，他正在使用ChatGPT进行实验，以重现在那些被报道过的攻击技术。为此，他分享了一个基于Python的窃取器的代码，它搜索常见的文件类型，将它们复制到Temp文件夹中的一个随机文件夹中，将它们压缩并上传到硬编码的FTP服务器。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673083044112343.png "1673083044112343.png")

攻击者展示他如何使用ChatGPT创建infostealer

我们对示例的分析证实了攻击者的说法，这确实是一个很简单的窃取器，它在整个系统中搜索12种常见的文件类型，如MS Office文档、PDF和图像。如果发现任何感兴趣的文件，恶意软件会将这些文件复制到一个临时目录中，将其压缩并通过网络发送。值得注意的是，攻击者并没有对文件进行加密或安全地发送，因此这些文件也可能落入第三方手中。

这个攻击者使用ChatGPT创建的第二个示例是一个简单的Java代码片段。它下载PuTTY(一种非常常见的SSH和telnet客户端)，并使用Powershell在系统上秘密运行它。当然，可以修改此脚本以下载和运行任何程序，包括常见的恶意软件家族。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673083052126154.png "1673083052126154.png")

证明他如何创建Java程序下载PuTTY，并使用Powershell运行它

该攻击者之前的论坛也共享过几个脚本，比如后利用阶段的自动化，以及一个试图钓鱼获取用户凭据的c++程序。此外，他还积极分享SpyNote的破解版本，这是一款Android RAT恶意软件。因此，总的来说，他似乎是一个以技术为导向的攻击者，他的帖子旨在向技术能力较弱的攻击者展示如何利用ChatGPT进行恶意攻击，并提供他们可以立即使用的真实示例。

**示例2：创建加密工具**

2022年12月21日，一位名叫USDoD的攻击者发布了一个Python脚本，他强调这是他创作的第一个脚本。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673083066175738.png "1673083066175738.png")

被称为USDoD的攻击者发布的多层加密工具

当另一名攻击者评论代码的风格类似于openAI代码时，USDoD证实openAI给了他一个“很好的帮助，以一个很好的范围完成脚本。”

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673083076163661.png "1673083076163661.png")

确认多层加密工具是使用Open AI创建的

我们对脚本的分析验证了它是一个执行加密操作的Python脚本。更具体地说，它实际上是不同签名、加密和解密功能的大杂烩。乍一看，该脚本似乎是良性的，但它实现了多种不同的功能：

脚本的第一部分生成用于签名文件的加密密钥（具体使用椭圆曲线密码和曲线ed25519）；

脚本的第二部分包括一些函数，这些函数使用硬编码的密码以混合模式同时使用Blowfish和Twofish算法对系统中的文件进行加密。这些函数允许用户加密特定目录或文件列表中的所有文件。

该脚本还使用RSA密钥，使用PEM格式的证书，MAC签名和blake2哈希函数来比较哈希值等。

需要注意的是，加密函数的所有解密对应项也都在脚本中实现。该脚本包括两个主要函数：一个用于加密单个文件并将消息认证码（MAC）附加到文件末尾，另一个加密硬编码路径并解密其作为参数接收的文件列表。

当然，上述所有代码都可以良性使用。然而，可以很容易地修改此脚本，以完全加密某人的计算机，而无需任何用户交互。例如，如果脚本和语法问题得到解决，它可能会将代码变成勒索软件。

虽然USDoD似乎不是一个开发人员，技术技能有限，但他是地下社区中一个非常活跃且声望很高的成员。USDoD从事各种非法活动，包括出售被入侵公司和被盗数据库的访问权。USDoD最近共享的一个著名被盗数据库据称是泄露的InfraGard数据库。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673083086178587.png "1673083086178587.png")

USDoD之前涉及发布InfraGard数据库的非法活动

**示例3：使用ChatGPT进行欺诈活动**

另一个使用ChatGPT进行欺诈活动的示例是在2022年新年前夕发布的，它展示了一种不同类型的网络犯罪活动。虽然前两个示例更多地关注于面向恶意软件的ChatGPT使用，但本示例显示了一个标题为“滥用ChatGPT创建暗网市场脚本”的讨论。在这篇文章中，攻击者展示了使用ChatGPT创建暗网市场是多么容易。该市场在地下非法经济中的主要作用是提供一个平台，用于自动交易非法或被盗物品，如被盗账户或支付卡，恶意软件，甚至毒品和弹药，所有支付都使用加密货币。为了说明如何使用ChatGPT实现这些目的，攻击者发布了一段代码，该代码使用第三方API来获取最新的加密货币(门罗币、比特币和以太坊)价格，作为暗网市场支付系统的一部分。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673083100691335.png "1673083100691335.png")

攻击者使用ChatGPT创建暗网市场脚本

2023年初，几个攻击者在其他地下论坛上展开了讨论，讨论的重点是如何将ChatGPT用于欺诈攻中。其中大部分集中于使用另一种OpenAI技术（DALLE2）生成随机艺术品，并通过Etsy等合法平台在线销售。在另一个示例中，攻击者解释如何为特定主题生成电子书或短章节(使用ChatGPT)，并在网上销售这些内容。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230107/1673083110833846.png "1673083110833846.png")

地下论坛中关于如何使用ChatGPT进行欺诈活动的多个线程

**总结**

现在就认定ChatGPT功能是否会成为暗网攻击者最喜欢的新工具还为时过早。然而，生成恶意代码的新趋势已经出现。

本文翻译自：https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?bKu0FG4U)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/member/eXPv)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/eXPv)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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