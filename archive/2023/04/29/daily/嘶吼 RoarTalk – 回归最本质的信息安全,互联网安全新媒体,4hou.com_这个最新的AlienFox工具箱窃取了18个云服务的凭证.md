---
title: 这个最新的AlienFox工具箱窃取了18个云服务的凭证
url: https://www.4hou.com/posts/yAlV
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-29
fetch_date: 2025-10-04T11:31:33.571050
---

# 这个最新的AlienFox工具箱窃取了18个云服务的凭证

这个最新的AlienFox工具箱窃取了18个云服务的凭证 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 这个最新的AlienFox工具箱窃取了18个云服务的凭证

~阳光~
[新闻](https://www.4hou.com/category/news)
2023-04-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)117777

收藏

导语：威胁者目前可以使用一种名为"AlienFox"的新的模块化工具包来扫描发现那些配置错误的服务器，并窃取大量的基于电子邮件服务的认证秘钥和登录凭证。该工具包会通过一个私人Telegram频道出售给网络犯罪分子，并且该频道已成为了恶意软件作者和黑客的一个常见的交易渠道。

据Sentinel实验室的参与分析AlienFox的研究人员称，该工具可以针对流行服务中常见的在线托管框架，比如Laravel、Drupal、Joomla、Magento、Opencart、Prestashop和WordPress进行攻击。分析师们还发现了三个版本的AlienFox，这表明该工具包的作者正在积极开发和改进这个恶意工具。

**AlienFox是为了窃取你的秘钥**

AlienFox是一个模块化的工具集，分别由不同作者创建的各种定制工具以及各种修改过的开源程序组成。威胁者在安全扫描平台（如LeakIX和SecurityTrails）上用它来收集利用配置错误的云服务器。

然后，AlienFox会使用数据提取脚本搜索配置错误的服务器，寻找那些通常用于存储秘钥的敏感配置文件，如API密钥、账户凭证和认证令牌。

1and1、AWS、Bluemail、Exotel、Google Workspace、Mailgun、Mandrill、Nexmo、Office365、OneSignal、Plivo、Sendgrid、Sendinblue、Sparkpostmail、Tokbox、Twilio、Zimbra和Zoho都是该工具的攻击目标。工具包中还包含了单独的脚本，用于在易受攻击的服务器上建立持久联系并提升权限。

据SentinelLabs称，在野发现的该工具的第一个版本是AlienFox v2，其主要目的是网络服务器配置和环境文件的分析利用。然后，该恶意软件对这些文件进行解析并获取凭证，然后试图在目标服务器上使用Paramiko Python库进行SSH连接。

AlienFox v2还包含一个python脚本（awses.py），该脚本可以自动在AWS SES（简单电子邮件服务）上发送和接收信息，以及对被攻击的AWS账户进行长时间的高权限的访问。最后，AlienFox 2.0还包含了对CVE-2022-31279的利用功能，这个漏洞是Laravel PHP框架中的一个反序列化漏洞。

AlienFox v3增加了从Laravel环境中自动提取密钥和其他敏感信息的功能。该工具包的第三个版本，通过使用初始化的变量、包含模块化函数的Python类以及进程线程，极大的提高了工具的性能。

AlienFox v4目前是最新的版本，它对代码进行了大量的改进，并对脚本插件进行了扩展。这一版的恶意软件的功能很强大，它对WordPress、Joomla、Drupal、Prestashop、Magento和Opencart进行攻击，其中还包含了一个亚马逊零售网站的账户检查器，以及一个针对比特币和以太坊的加密货币钱包种子破解器。

新的"钱包破解器"脚本表明，AlienFox的开发者希望扩大该工具的客户群体或增强该工具的功能，并确保现有客户进行持续的订阅。

管理员必须确保他们的服务器配置了适当的访问控制、文件权限，并删除了不必要的服务，以防止这种不断变化的威胁。此外，尽量使用MFA（多因素认证）以及实时监测账户上的任何异常或可疑活动，这些都可以帮助管理员早期发现入侵的行为。

本文翻译自：https://www.cysecurity.news/2023/03/this-new-alienfox-toolkit-steals.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0HH43nit)

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

![](https://img.4hou.com/portraits/f1cf9065382964bd9f4a9cd061a16d17.jpg)

# [~阳光~](https://www.4hou.com/member/lPjj)

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

[查看更多](https://www.4hou.com/member/lPjj)

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