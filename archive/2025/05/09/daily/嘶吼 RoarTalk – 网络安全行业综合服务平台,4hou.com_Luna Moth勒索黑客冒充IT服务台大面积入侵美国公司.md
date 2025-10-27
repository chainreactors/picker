---
title: Luna Moth勒索黑客冒充IT服务台大面积入侵美国公司
url: https://www.4hou.com/posts/1MNV
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-09
fetch_date: 2025-10-06T22:23:43.958872
---

# Luna Moth勒索黑客冒充IT服务台大面积入侵美国公司

Luna Moth勒索黑客冒充IT服务台大面积入侵美国公司 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Luna Moth勒索黑客冒充IT服务台大面积入侵美国公司

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)74307

收藏

导语：数据被盗后，Luna Moth联系受害组织，威胁要在其清晰网域名上公开泄露数据，除非他们支付赎金。

被称为Luna Moth的数据盗窃勒索组织，又名Silent Ransom group，已经加大了对美国法律和金融机构的回调网络钓鱼攻击力度。

据 EclecticIQ 研究员 Arda Büyükkaya 称，这些攻击的最终目的是窃取数据和实施勒索。

Luna Moth，内部称为 Silent Ransom Group，他们之前曾发起 BazarCall 活动，以便为 Ryuk 获取公司网络的初始访问权限，后来又发起 Conti 勒索软件攻击。

2022年3月，随着Conti开始关闭，BazarCall威胁组织从Conti集团中分离出来，成立了一个名为Silent Ransom Group （SRG）的新组织。

Luna moth最近的攻击包括通过电子邮件、虚假网站和电话冒充IT支持人员，并且完全依赖社会工程和欺骗，在任何情况下都没有部署勒索软件。

据安全公司评估，截至2025年3月，Luna Moth可能已经通过GoDaddy注册了至少37个域名，以支持其回调网络钓鱼活动。

这些域名中的大多数都是美国主要律师事务所和金融服务公司的IT帮助台或支持门户，使用的是键入的模式。

![country.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250506/1746502168843002.png "1746501769208709.png")

Luna Moth在过去12个月的目标

elecectiq发现的最新活动始于2025年3月，目标是美国的组织，这些组织发送恶意电子邮件，其中包含假的号码，收件人被敦促拨打电话解决不存在的问题。

一名Luna Moth操作员冒充IT人员接听电话，并说服受害者安装来自假IT帮助台网站的远程监控和管理（RMM）软件，使攻击者能够远程访问他们的机器。

虚假的帮助台网站使用域名，这些域名遵循像[company\_name]-helpdesk.com和[company\_name]helpdesk.com这样的命名模式。

![support-site.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250506/1746502169117455.png "1746501803611237.png")

虚假IT支持网站

在这些攻击中被滥用的工具包括Syncro、SuperOps、Zoho Assist、Atera、AnyDesk和Splashtop。这些都是合法的数字签名工具，所以它们不太可能触发对受害者的任何警告。

一旦安装了RMM工具，攻击者就可以动手访问键盘，允许他们传播到其他设备并搜索本地文件和共享驱动器以获取敏感数据。

找到有价值的文件后，他们使用WinSCP（通过SFTP）或Rclone（云同步）将这些文件泄露到攻击者控制的基础设施中。

数据被盗后，Luna Moth联系受害组织，威胁要在其清晰网域名上公开泄露数据，除非他们支付赎金。每个受害者的赎金金额各不相同，从100万美元到800万美元不等。

![silent-ransom-group-dls.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250506/1746502172143409.png "1746501864670209.png")

Luna Moth的勒索网站

Büyükkaya评论了这些攻击的隐蔽性，指出它们不涉及恶意软件、恶意附件或恶意软件网站的链接。受害者只是自己安装RMM工具，认为他们正在接受帮助台的支持。由于企业通常使用这些RMM工具，因此它们不会被安全软件标记为恶意工具，并允许运行，建议考虑限制在组织环境中不使用的RMM工具的执行。

文章翻译自：https://www.bleepingcomputer.com/news/security/luna-moth-extortion-hackers-pose-as-it-help-desks-to-breach-us-firms/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?V8yAQtvt)

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

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

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

[查看更多](https://www.4hou.com/member/BVMN)

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