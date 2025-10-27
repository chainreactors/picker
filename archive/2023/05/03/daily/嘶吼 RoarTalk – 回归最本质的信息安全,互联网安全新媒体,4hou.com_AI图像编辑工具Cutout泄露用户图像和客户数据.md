---
title: AI图像编辑工具Cutout泄露用户图像和客户数据
url: https://www.4hou.com/posts/nJ2E
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-05-03
fetch_date: 2025-10-04T11:38:48.106235
---

# AI图像编辑工具Cutout泄露用户图像和客户数据

AI图像编辑工具Cutout泄露用户图像和客户数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# AI图像编辑工具Cutout泄露用户图像和客户数据

布加迪
[新闻](https://www.4hou.com/category/news)
2023-05-02 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)108160

收藏

导语：Cutout所有的一台Elasticsearch服务器总共泄露了多达9 GB的客户数据。

Cutout是一种广受欢迎的人工智能（AI）图像编辑工具，近日遭到一起数据泄密事件，因而泄露了用户图像、用户名和电子邮件地址。这起事件凸显了使用基于云的AI工具处理敏感数据所带来的风险。

Cutout.pro是一款基于互联网的AI图像编辑工具，近日被发现泄露了多达9 GB 的用户数据，其中包含用户名和通过使用特定查询请求的图像。

这起安全事件是由Cybernews发现的，该安全网站发现了一个敞开的ElasticSearch实例含有2200 万条引用用户名的日志条目，其中包括个人用户和企业帐户。

然而，由于日志条目含有重复项，受影响的用户总共有多少就不得而知。该实例还包含用户积分数量、虚拟游戏货币以及用来存储所生成图像的亚马逊S3 存储桶的链接等方面的信息。

由于使用基于AI的工具蔚然成风，出现这样的事件应该不足为奇。AI工具大行其道，这要拜ChatGPT大获成功所赐。ChatGPT如此成功，以至于谷歌被迫发布了自己的AI工具：Bard AI。

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230219/1676764744125744.jpeg "1676764744125744.jpeg")

图1. 泄露的Elasticsearch 集群（图片来源：Cybernews）

这个总部位于中国香港的视觉设计平台允许用户使用基于AI的应用编程接口（API）来处理照片或生成图像。这项功能让用户可以将该公司的服务整合到第三方应用程序中。

正如研究人员特别指出，Cutout.pro自称每个月收到全球超过3亿次的API 请求，峰值期间每秒收到来自5000多个应用程序和网站的4000次请求，还声称与25000多家企业建立了合作伙伴关系。

因此，这起泄露造成的后果对于数据在此事件中泄露的客户来说可能是毁灭性的。据Cybernews报道，其团队还在这个敞开的数据库中发现了两款图像编辑应用程序：Vivid和AYAYA。

“如果Cutout.pro的开发人员之前没有备份数据，这个敞开的实例不仅会导致暂时的拒绝服务，还会导致存储在这个敞开的实例上的数据永久丢失。攻击者可以彻底摧毁这个实例。”

由于未适当配置，这个敞开的实例可能已被威胁分子以多种方式利用。Cybernews 团队推测任何人都可以执行 CRUD（创建、读取、更新和删除）操作。

攻击者可能使用这个初始访问点进入数据库、控制数据，并通过Cutout.pro的API传递数据，从而对这家公司的客户实施危险的供应链攻击。

**错误配置的数据库对隐私构成了威胁**

众所周知，配置错误或不安全的数据库对许多公司和毫无戒心的用户已构成了重大的隐私威胁。2020年，研究人员发现了10000多个不安全的数据库，这些数据库将超过100亿条（10463315645）记录暴露了在公众面前，未采取任何安全身份验证机制，谁都可以访问。

2021年，暴露的数据库数量增加到了399200个。2021年因配置错误而导致数据库泄露事件最多的前10个国家或地区包括如下：

美国：93685 个数据库

中国：54764 个数据库

德国：11177 个数据库

法国：9723 个数据库

印度：6545 个数据库

新加坡：5882 个数据库

中国香港：5563 个数据库

俄罗斯：5493 个数据库

日本：4427 个数据库

意大利：4242 个数据库

本文翻译自：https://www.hackread.com/ai-image-editing-tool-cutout-data-leak/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?QSixRy3w)

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