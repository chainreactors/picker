---
title: 更多的网络钓鱼活动在利用IPFS网络协议
url: https://www.4hou.com/posts/7y3w
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-12
fetch_date: 2025-10-04T11:30:32.751086
---

# 更多的网络钓鱼活动在利用IPFS网络协议

更多的网络钓鱼活动在利用IPFS网络协议 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 更多的网络钓鱼活动在利用IPFS网络协议

布加迪
[新闻](https://www.4hou.com/category/news)
2023-04-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)120377

收藏

导语：不妨了解IPFS如何被用于网络钓鱼攻击、为什么清除受影响的网页特别棘手以及如何防范这种安全威胁。

![1.jpeg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230411/1681181227656878.jpeg "1680923252178358.jpeg")

据卡巴斯基的最新研究报告显示，星际文件系统（IPFS）的欺诈性使用现象最近似乎有所增加。自2022年以来，IPFS一直被网络犯罪分子用于发动电子邮件网络钓鱼攻击。

**IPFS是什么？**

IPFS是一种点对点网络协议，旨在提供去中心化的分布式Web。与依赖集中式服务器的传统Web协议不同，IPFS允许用户共享和访问文件，而不依赖任何权力中心。

IPFS通过文件的内容而不是位置来标识文件。每个文件都被赋予了一个唯一的加密哈希，名为CID。内容标识符可用于从网络上存储副本的任何节点检索文件。这使得分发和访问内容变得很容易，即使原始内容源处于离线或不可用的状态。

IPFS还使用一种内容寻址系统，这意味着对文件的任何更改都将导致新的散列。这确保了文件保持不变、防止被篡改。

访问IPFS可以通过专用的应用编程接口（API）或网关来完成，这些接口或网关提供了对IPFS内容的访问，适用于任何Web浏览器。

访问网关的URL含有CID和网关，但可能因网关而异。比如说，它可以是：

https://gateway/ipfs/CID

https://CID.ipfs.gateway

**IPFS如何用于网络钓鱼攻击？**

在平常的网络钓鱼案例中，受害者被引诱访问欺诈性的网络钓鱼网页，钓鱼网页会窃取他们的凭据，可能还窃取其信用卡信息。然而，这个欺诈性网页可能托管在IPFS上，通过网关来加以访问。

使用这种系统让攻击者可以降低托管网络钓鱼网页的成本，并加大了从互联网上清除欺诈性内容的难度，因为内容可能同时驻留在多台计算机上。

如果用户点击了网络钓鱼链接并提供了凭据，尽快更改密码并检查该帐户是否出现任何恶意活动很重要。

**针对性的网络钓鱼攻击也使用IPFS**

据卡巴斯基声称，与通常的网络钓鱼相比，大多数IPFS网络钓鱼攻击并不是太具原创性，但在一些情况下，IPFS用于复杂的针对性攻击（见图A）。

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230411/1681181227104143.jpeg "1680923271181459.jpeg")

图A. 针对性网络攻击钓鱼电子邮件的样本，附有IPFS链接。图片来源：卡巴斯基

从图A和卡巴斯基的描述中可以看出，“攻击针对的是企业采购部门，这些邮件来自现有组织的销售经理。”

**清除网络钓鱼网页对IPFS内容而言比较棘手**

通常的钓鱼网页可以通过要求网站内容提供商或所有者清除来清除。这番操作可能花费相当长的时间，具体取决于托管主机，内容存储在防弹提供商上尤其如此，防弹提供商是非法的托管提供商，他们告诉客户不会回应执法部门的请求，也不会下架内容。

针对IPFS内容的下架操作有所不同，不同之处在于需要从所有节点清除内容的方式。

IPFS网关的提供商试图通过定期删除这些文件的链接来对付这些欺诈性网页，但它并不总是像屏蔽钓鱼网站那样快速。卡巴斯基的研究人员Roman Dedenok在2023年3月27日撰文道，卡巴斯基“观察到2022年10月首次出现的IPFS文件的URL地址，在撰写本文时仍在运行中。”

**IPFS网络钓鱼方面的统计数据**

截至2022年底，每天有2000至15000封IPFS网络钓鱼邮件。2023年，卡巴斯基分析的IPFS网络钓鱼活动开始增加，1月和2月每天多达24000封电子邮件；然而在此之后，数量恢复到与2022年12月几乎相同（见图B）。

![3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230411/1681181228130648.jpeg "1680923292511818.jpeg")

图B. 从2022年底到2023年2月底的IPFS网络钓鱼电子邮件数量。图片来源：卡巴斯基

月度统计数据显示，2月份是忙碌的一个月，有近400000封钓鱼邮件，而11月和12月的钓鱼邮件数量分别约在228000至28000封之间（见图C）。

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230411/1681181229118945.jpeg "1680923307478778.jpeg")

图C. 从2022年11月到2023年2月每月的IPFS钓鱼邮件。图片来源：卡巴斯基

**如何防范这种IPFS网络钓鱼威胁？**

反垃圾邮件解决方案（比如微软Exchange在线保护或梭子鱼电子邮件安全网关）将有助于检测IPFS网络钓鱼并阻止链接，就像对付任何常见的网络钓鱼情形那样。

用户应该了解可以通过即时消息和社交网络等不同方式发送给他们的钓鱼电子邮件或任何类型的钓鱼链接。

实施多因素身份验证，以防止未经授权的访问。这将使攻击者更难获得访问权，即使他们已通过网络钓鱼获得了登录凭据。

本文翻译自：https://www.techrepublic.com/article/ipfs-phishing-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?8KW6mh15)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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