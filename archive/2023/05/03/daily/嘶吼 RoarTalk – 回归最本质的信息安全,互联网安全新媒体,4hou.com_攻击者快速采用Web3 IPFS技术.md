---
title: 攻击者快速采用Web3 IPFS技术
url: https://www.4hou.com/posts/qpj3
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-05-03
fetch_date: 2025-10-04T11:38:47.745721
---

# 攻击者快速采用Web3 IPFS技术

攻击者快速采用Web3 IPFS技术 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻击者快速采用Web3 IPFS技术

luochicun
[技术](https://www.4hou.com/category/technology)
2023-05-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)119188

收藏

导语：IPFS是一种全新的超媒体文本传输协议，可以把它理解为一种支持分布式存储的网站。

![微信截图_20230421165743.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071418178319.png "1682070583198159.png")

2022年，unit42观察到，IPFS(InterPlanetary File System,星际文件系统)被广泛用作恶意工具。IPFS是一种全新的超媒体文本传输协议，可以把它理解为一种支持分布式存储的网站。

与任何技术一样，IPFS也可能被攻击者者滥用。然而，由于IPFS上的托管内容是去中心化和分布式的，因此在定位和删除生态系统中的恶意内容方面存在挑战，这使其类似于 bullet-proof 托管。

从2021第四季度到2022年第四季度末，Palo Alto Networks检测到IPFS相关流量增加了893%。调查还显示，病毒总数在同一时期增长了27000%以上。IPFS相关流量的增加伴随着恶意活动的显著增加。检测发现，2022年的许多攻击活动涵盖了网络钓鱼、凭证盗窃和恶意有效负载传播。

**整体流量增加**

从2022年第一季度开始，Palo Alto Networks的IPFS流量显著增加，如下图所示。2022年第一季度，研究人员检测到IPFS流量与2021年最后一个季度末的记录相比增长了178%。

之后流量继续增加：

第二季度增长85%；

第三季度增长62%；

2022年最后一个季度增长了19%；

这相当于整体增长了893%。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071419192881.png "1682070737118348.png")

与IPFS相关的流量在2022年第一季度的VirusTotal上也出现了类似的增长，与2021年第四季度相比增长了6503%

之所以会出现这种增长，是因为采用了IPFS技术。新技术出现后总会有人恶意使用它。研究人员在Palo Alto Networks和VirusTotal提交的IPFS流量中观察到的显著增加也包括使用IPFS的恶意活动的大幅增加。

研究人员观察到，攻击者经常为他们的诈骗服务做广告，使用各种宣传。也就是说，由于IPFS分布式文件系统的性质，IPFS为他们的活动提供了持久性。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071420382305.png "1682070759285913.png")

攻击者使用客户IPFS链接销售诈骗服务

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071421214455.png "1682070773127572.png")

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071422160366.png "1682070782174435.png")

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071422144217.png "1682070801209213.png")

攻击者出售IPFS网络钓鱼页面

攻击者正在使用公共IPFS网关作为传递其恶意内容的方式。如果没有这些互联网可访问网关，攻击者将无法将IPFS网络作为其攻击活动的一部分。这一趋势在许多网络钓鱼和网络犯罪活动中使用互联网可访问的IPFS链接中可以看到，这些活动的初始攻击媒介通常是电子邮件诱饵。

接下来，我们将详细介绍在分析恶意使用IPFS技术时看到的一些攻击活动。

**网络钓鱼**

下图显示了IPFS与网络钓鱼相关的网络流量呈指数级增长，尤其是在今年最后一个季度。与托管在网络上的传统网络钓鱼页面不同，托管提供商或管理机构无法轻松删除IPFS网络钓鱼内容。

一旦发布到IPFS网络，任何人都可以在自己的节点上获取并重新发布内容。网络钓鱼内容可以托管在多个节点上，并且必须向每个主机发出删除内容的请求。如果任何一个主机不同意删除，那么内容几乎不可能被删除。

由于网站所有者、托管提供商或版主删除或暂停内容，网络钓鱼活动的生存时间（TTL）通常比其他类型的网络犯罪更短。IPFS的结构使攻击者能够通过使其更具抵御能力来延长他们的活动。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071423192557.png "1682070822544176.png")

IPFS网络钓鱼URL

IPFS网络钓鱼活动与传统网络钓鱼活动类似，攻击者模仿合法服务和软件（如DHL、DocuSign和Adobe）来增加进入某人收件箱的可能性。阻止这些诱惑的能力取决于接收组织的电子邮件安全性。虽然一些组织在其安全电子邮件网关和其他安全产品中制定了非常严格的规则，，但其他组织没有这样做，因为担心合法的电子邮件会受到影响。

请注意，下面显示的名称和徽标是攻击者试图冒充合法组织的作品，攻击者的模仿并不意味着合法组织的产品或服务存在漏洞。

在下面的示例中，模仿DHL品牌的电子邮件诱饵包含一个附件。在该附件中，有一个指向实际网络钓鱼页面的IPFS链接。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071424658533.png "1682070837766309.png")

DHL主题的电子邮件诱饵，附件已提交给VirusTotal

一旦用户点击下图所示的附件，就会预览一张模仿Adobe PDF标识的假发票。“打开”按钮实际上是一个IPFS链接，将用户重定向到实际的网络钓鱼页面，而不是打开PDF。这个页面可以通过IPFS网关访问。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071425358633.png "1682070851127853.png")

附有DHL诱饵链接的附件

IPFS URL通过IPFS[.]io将用户重定向到Adobe网络钓鱼页面，然后尝试窃取用户的登录凭据。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071427476893.png "1682070861158894.png")

在DHL主题诱饵的附件中发现了IPFS钓鱼链

与其他Web3技术一样，常用的数据外窃取方法在IPFS网络上是不可能的。攻击者无法接收受害者输入到表单中的数据，从而窃取他们的凭据。

标准的web表单使用HTML前端来显示内容，后端使用表单处理器来收集、处理并将数据发送到web服务器。IPFS不包含相同或类似的技术来处理这些动态功能。

使用IPFS的人只是简单地提取或检索数据的只读副本，而不是与之交互。IPFS网关后面的网络钓鱼页面依赖于许多其他技术。

例如，攻击者可以在收集帐户凭证的网页中使用嵌入式脚本代码。他们还可以使用无头表单，即可以填写和收集的静态用户表单。表单字段被映射到JSON模型，以便通过API发送到后端系统，从而促进API驱动的窃取。这些信息是通过HTTP POST请求收集的，这些请求被发送给攻击者，在那里它可以被用于其他恶意目的。

**Nillis.html中的未转义脚本**

下图显示了一个模仿Microsoft的网络钓鱼示例，它以HTML页面的形式托管。链接此页面的IPFS URL为

```
hxxps[://]bafybeicw4jjag57bk3czji7wjznkkpbocg27qk3fjvqh5krbrfiqbksr2a[.]ipfs[.]w3s[.]link/Nills[.]html.
```

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071429717772.png "1682070874248744.png")

Nills.html的网络钓鱼页面

要了解凭据将如何被窃取的，有必要查看网页的源内容。

下图显示了一个名为WriteHTMLtoJS的函数。此函数的目的是将HTML写入JavaScript (JS)，并对内容进行转义。Unescape JS函数负责用实际的ASCII字符值解码十六进制序列

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071430129713.png "1682070949971969.png")

Nills.html网页的源代码视图

解码和分析未转义的内容会发现一对脚本标签和一个观察到的URL，它是app[.]headlessforms[.]cloud，网络钓鱼页面似乎与此URL有关。

对无头表单的分析表明，此网络钓鱼页面使用的是一种管理用户表单的方法，在该方法中，可以在第三方后端捕获数据，而无需设计或开发前端web应用程序。

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071431532648.png "1682070900111727.png")

Nills.html的解码视图，其中包含凭据泄露的位置

受害者输入帐户用户名和密码凭据后，它将通过HTTPPOST请求发送。URI末尾的字符串（GjCP9S9nke）是与无头表单平台上的攻击者相关联的唯一标识令牌。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071432943843.png "1682070962907142.png")

HTTP POST和捕获的凭据

**new.html中的HTTP POST**

另一个模仿微软的网络钓鱼页面也托管在IPFS上，名为new.html。关联的IPFS钓鱼URL为：

```
hxxp[://]bafybeifm5vcoj35hhuxf7ha3gg6asrrlrwu3bvcysgmrvygnm3qjmugwxq[.]ipfs[.]w3s[.]link/new[.]html?email=
```

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071433970539.png "1682070976708301.png")

new.html钓鱼页面

查看网页源代码会发现一个与前面引用的类似的JS函数，它对内容进行反转义，将其解码为ASCII值。unescape函数如下图所示。

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071434208666.png "1682070991266605.png")

new.html的源代码视图

对内容进行解码后，会发现位于大量代码底部附近的一个感兴趣的片段，如下图所示。

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071435641619.png "1682071004972394.png")

new.html URL

上图中的代码片段显示了注册到提交按钮的点击函数事件的外部URL (fairpartner[.]ru)。此URL将与HTTP POST请求提供的数据联系，如下图所示。

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071436319863.png "1682071015214323.png")

fairpartner.ru的DNS请求

截止发文，研究人员还无法捕获凭证盗窃，因为该域不再可访问，这突出了使用第三方服务(如无头表单)进行攻击的优势。

IPFS不仅被攻击者用于网络钓鱼，它还用于恶意软件攻击集和勒索软件。

众所周知，RansomEXX等勒索软件即服务（RaaS）运营商会使用IPFS网络发布受害者被盗的数据。Smoke Loader、XLoader、XMRig和OriginLogger等恶意软件经常使用IPFS链接进行恶意有效负载传递。IPStorm和Dark实用程序使用IPFS网络作为基础设施。

**攻击过程**

攻击者以几种不同的方式使用IPFS网关。可以将这些方法分类为传播方法，或用作托管或分级有效负载的基础设施，或者用作分散的C2信道。

以下恶意软件家族在2022年全年一直在使用IPFS。恶意软件家族Dark Utilities一直在使用IPFS网关来转移恶意负载。IPStorm使用IPFS网关作为P2P通信的C2信道。

攻击者还使用IPFS网关提供各种恶意软件，例如：

```
OriginLogger
XLoader
XMRig
Metasploit
```

接下来，我们将介绍这些攻击是如何在高级别上运行的，包括IPFS是如何被用来促进恶意操作的。

**OriginLogger**

OriginLogger恶意软件开始于2019年。它是Agent Tesla远程访问木马的迭代版本。它是用.NET编写的，是一个隐蔽性很强的信息窃取程序。这种攻击通常以击键和剪贴板数据为目标，这些数据通过C2通道传送回攻击者控制的服务器。

Unit 42的研究人员发现了一个伪装成逾期发票的电子邮件诱饵，带有XLL附件。打开XLL文件后，会向IPFS URL发送HTTP GET请求：

```
hxxps[://]ipfs[.]io/ipfs/QmXtVwamvHvXZzuEZcMn2xDsPRKN8uS17YCUzTiGx1rYnv?filename=file-05-2022.exe
```

此URL用于通过IPFS网关下载OriginLogger负载。

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230421/1682071437136681.png "1682071025965214.png")

附件

下图显示了OriginLogger的第二个传...