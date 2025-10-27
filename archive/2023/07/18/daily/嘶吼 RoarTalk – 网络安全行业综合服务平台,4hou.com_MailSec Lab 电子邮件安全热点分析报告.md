---
title: MailSec Lab 电子邮件安全热点分析报告
url: https://www.4hou.com/posts/DZ66
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-18
fetch_date: 2025-10-04T11:51:11.476618
---

# MailSec Lab 电子邮件安全热点分析报告

MailSec Lab 电子邮件安全热点分析报告 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# MailSec Lab 电子邮件安全热点分析报告

网际思安
[技术](https://www.4hou.com/category/technology)
2023-07-17 13:38:20

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)207766

收藏

导语：本周（2023年7月10日~14日），网际思安麦赛安全实验室(MailSec Lab)观察到大量新增的以“电子发票”为主题的特洛伊木马类恶意邮件，并做了详细的风险特征、攻击溯源等技术研究与分析，请各企事业单位及时做好相关的防护。

**本期热点**

******“******电子发票******”******木马******类恶意邮件***激增***

本周（2023年7月10日~14日），网际思安麦赛安全实验室(MailSec Lab)观察到大量新增的以“电子发票”为主题的特洛伊木马类恶意邮件，并做了详细的风险特征、攻击溯源等技术研究与分析，请各企事业单位及时做好相关的防护。

**2023.07.10~2023.07.14**

**0****1****热点描述**

      关于此批“电子发票”为主题的病毒样本邮件，如下图所示：

*图1. “电子发票”为主题的特洛伊木马邮件*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojefftHxoJRSEDwz2kKKQk4T3XaS1qUb9TuSOXCCeSMeGO5AZIDu0MALYgg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

      该邮件通过伪造下载电子发票通知，诱导员工点击邮件正文中的URL超链接，从而下载Trojan Droppers程序。当员工双击触发程序后，该恶意程序将自动连接攻击者搭建的恶意网站，进一步下载特洛伊木马病毒，并对计算机进行远程控制、数据盗窃、内网横向攻击等APT攻击行为。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CKnbv3SJd9CH78xyHt9ib6DmpiaKv4iamib4A5vkOm9hprMqhfag8b82jlYqJsRKCIuQkkt0TXNv93YTtLC1RMicibibw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**思安知识小课堂**

*Trojan Droppers**是一种恶意软件，用于传递和部署其他恶意软件或特洛伊木马（Trojans）。它们通常被设计成看似无害或合法的文件，以欺骗用户进行下载和执行。一旦Trojan Dropper被执行，它会解压或下载其他恶意组件并将其安装到受感染的计算机上，而这些组件可能会执行各种恶意活动，如窃取敏感信息、远程控制计算机、加密文件等。*

*Trojan Droppers**的主要目标是通过绕过安全防护机制，将恶意软件引入目标系统。为了达到这个目的，它们常常采用以下策略：*

* *伪装成合法文件：Trojan Droppers会将自己伪装成常见的文件类型，如图像文件、文档、媒体文件等，以便让用户误以为它们是无害的。*
* *利用安全漏洞：Trojan Droppers可能会利用操作系统或应用程序中的已知漏洞，通过这些漏洞将恶意软件注入目标系统。*
* *社会工程攻击：Trojan Droppers有时会利用社会工程技术，通过欺骗用户进行下载和执行。例如，它们可能会伪装成电子邮件附件、下载链接或弹出广告等形式出现。*
* *多层加密和混淆：为了逃避安全软件的检测，Trojan Droppers通常使用多层加密和混淆技术，使其代码变得难以分析和检测。*

*一旦Trojan Dropper成功投递并安装了其他恶意软件或特洛伊木马，后者可能会执行各种恶意活动，如数据窃取、远程控制、密钥记录、网络攻击等。*

*图2. 点击链接后下载**Trojan Droppers**程序*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeff4bPRcuthnTgnrASFZTPcUfPjiatM24n5SFdfdmJA3PxFJHNicibpNA1qA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**0****2****专家分析**

     MailSec Lab的技术专家从源IP、URL链接、EXE文件风险性、邮件头、邮件内容等方面，对此邮件的风险特征进行了详尽的技术分析。

**PART****0****1****恶意链接的域名**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CKnbv3SJd9CH78xyHt9ib6DmpiaKv4iamib4A5vkOm9hprMqhfag8b82jlYqJsRKCIuQkkt0TXNv93YTtLC1RMicibibw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**提前划重点**

*使用welljoint.com域名的某高科技公司，通过“新网互联”网站购买了域名和邮箱服务。但是该邮箱服务器被黑客攻陷，welljoint.com域名被恶意利用为下载Trojan Droppers程序提供服务。*

*从分析来看，不仅是welljoint.com域名受影响，其他十几个域名也同时受影响，可能被黑客用于攻击活动。*

     通过浏览器直接访问URL链接的域名“welljoint.com”，可以了解到使用该域名的公司为一家位于上海的高科技公司，主要为银行、保险等金融机构提供联络中心系统解决方案，曾获“上海市科技小巨人”和“专精特新中小企业”荣誉。

*图3. 某某科技公司官方网站*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffrxIibKrZ6qq1a7pjEMh6T4icNriaL46k0S52jqCY6xRDmBN0DxhqfLaibw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

     对“welljoint.com”域名的Whois信息进行查询。该域名于2011年5月11日注册，到期时间为2032年4月17日，域名持有者为“Xin Net Technology Corporation”。

*图4. welljoint.com的Whois信息*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffN1SObz1CA4YodiahKU6YFSadn1WuSHKDia7wQNuAajla6Mu5nVyMUC9A/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

     进一步调查可知，该域名的持有者“Xin Net Technology Corporation”（新网互联）为一家提供域名注册、虚拟主机、网站建设等服务的公司。而通过“天眼查”可以了解到，在welljoint.com域名上建设官方网站的某高科技公司成立于2011年4月21日。结合以上信息，我们可以推断：该高科技公司成立1个月以后，通过新网互联公司注册了域名。

*图5. 通过新网互联注册域名*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeff9ORt4pgCzqRq2BUycPIP1sF6RTmnrvZVUzCupNWZ9cSKeftunKda0g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

     邮件样本中的恶意URL链接为：

http://mail.welljoint.com:81/download/attachment/xxxxxx

     子域名“mail.welljoint.com”被黑客用于放置Trojan Droppers程序。通过查询可知，“mail.welljoint.com”通过DNS的CNAME记录指向“mx171.dns.com.cn”。而“mx171.dns.com.cn”为“welljoint.com”域名的DNS MX记录，用于解析邮件服务器的IP地址。

*图6. 查询mail.welljoint.com的信息*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffJ4hic3lBeOHibuXRJwxOW9WiaNibKianT5viayUePxfYI6vJjmt29gDsWraQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

     进一步追踪“mx171.dns.com.cn”域名可知，新网互联为该公司提供了在线邮箱服务。

*图7. 新网互联提供的在线邮箱服务*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeff96RTeUm8f1hZj7vLIdfK67wia4n6aH3fp487exiayKHyZQYwHWLc3FBA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

     与此同时，通过IP反向查询域名可知，该被攻陷IP不仅为welljoint.com域名提供邮箱服务，还为其他公司的域名也提供邮件箱服务。这些域名都可能被黑客恶意利用，引诱员工下载病毒程序。

*图8. 被攻陷IP下提供邮箱服务的域名*

**PART****0****2****下载的EXE文件**

**提前划重点**

*经过对EXE文件的静态和动态分析可知，员工双击下载的“电子发票.exe”文件后会顺序触发如下恶意行为：*

*（1）**.**运行环境检测。检测程序是否在真实的物理机上运行？若在沙箱中运行，不触发恶意行为；*

*（2）**.**关闭Windows日志记录。通过关闭Windows各种类型的日志记录，隐藏恶意行为；*

*（3）**.**下载木马程序。连接外部的僵死控制服务器，下载木马程序；*

*（4）**.**安装木马程序。自动安装下载的木马程序，并开始对员工计算机的恶意攻击。*

     “电子发票.exe”文件被双击后，首先触发了大量检测注册表中网络相关配置的行为，如下表所示。此类检测，经常被恶意程序用于确定自身的运行环境是否安全。如果恶意程序发现自身是在虚拟环境中执行（例如：沙箱），将不运行病毒行为，从而躲避安全设备的检测。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffBp26790d8JXQX7D215lwVezmkQtej9bde0RkzMGXJDJRKWKrZPLZBA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

*图9.“电子发票.exe”检测注册表中网络相关配置*

      在确定自身是在员工的真实物理机上运行后，“电子发票.exe”通过修改注册表恶意关闭了Windows操作系统的各类日志监控功能，从而隐藏后续的攻击行为。

*图10.“电子发票.exe”恶意关闭各类日志监控*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffsyRRFpjZdndbfPnK3ZicHz3iaPb53Mm7Pgea53jkq8fJnhkZzapbVjpQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

      在成功完成一些系列的准备工作后，“电子发票.exe”连接外网的僵尸控制服务器，尝试下载木马程序（http://134.122.133.51:80/Client.bin）。该僵尸控制服务器位于香港，其所在的邻近公网IP网段（极可能在同一机房），存在大量的类似僵尸控制服务器。

*图11. “电子发票.exe”恶意下载病毒*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffJKkCIu8NYCVLdWco2gxU7EHCMX42SolHbbakKU9zhz8V9mZLRqbClA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

*图12. 134.122.133.0网段存在大量僵尸控制服务器*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffM6n36vhnLQommwM0AysMRO0SKVjIDshbVgpruWoDEicH95W3jYy9RdQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**PART****0****3****源IP地址**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/CKnbv3SJd9CH78xyHt9ib6DmpiaKv4iamib4A5vkOm9hprMqhfag8b82jlYqJsRKCIuQkkt0TXNv93YTtLC1RMicibibw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

**提前划重点**

*此恶意邮件的来源IP地址被列入多达12个RBL黑名单*

      通过对邮件头字段的分析可知，该恶意邮件的来源IP地址是119.28.25.25。

*图13. 邮件头部源IP字段展示*

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/CKnbv3SJd9BWqs6QNrpGqafA7yMojeffdERLqHBSJ8NdSBqJdQRAXjcEu1cnfQza5bnicnD45PZKZLEj0ZqqeeQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

      查询覆盖全球的91个RBL数据源，检测结果如下。此IP地址被列入了多达12个RBL黑名单。

|  |  |
| --- | --- |
| **序列号** | **被列为黑名单的RBL名称** |
| 1 | Abusix Mail Intelligence Blacklist |
| 2 | Hostkarma Black |
| 3 | IMP SPAM |
| 4 | ivmSIP |
| 5 | MAILSPIKE BL |
| 6 | Sender Score Reputation Network |
| 7 | SORBS NEW |
| 8 | SORBS SPAM |
| 9 | SWINOG |
| 10 | UCEPROTECTL1 |
| 11 | UCEPROTECTL2 |
| 12 | UCEPROTECTL3 |

**PART****0****4****发件人域名**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_...