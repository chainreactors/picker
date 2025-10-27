---
title: 俄罗斯SolarWinds攻击者发起新一轮的网络间谍攻击
url: https://www.4hou.com/posts/WKnW
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-04-19
fetch_date: 2025-10-04T11:32:39.591184
---

# 俄罗斯SolarWinds攻击者发起新一轮的网络间谍攻击

俄罗斯SolarWinds攻击者发起新一轮的网络间谍攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 俄罗斯SolarWinds攻击者发起新一轮的网络间谍攻击

~阳光~
[新闻](https://www.4hou.com/category/news)
2023-04-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)141498

收藏

导语：俄罗斯情报部门再次雇用黑客组织Nobelium/APT29，要求其针对乌克兰的基础设施进行入侵，这次攻击目的是为了监视北约成员国的外交部和外交官，以及欧盟和非洲的其他目标。

这一时间也恰好在针对加拿大基础设施发起新的一波攻击，这些攻击被认为与俄罗斯有关。

4月13日，波兰军事反间谍局和波兰的CERT团队向可能受间谍活动影响的目标发出了威胁警报，并且同时还表现出了妥协的迹象。这个被微软称为Nobelium的组织，也被Mandiant称为APT29，该组织常年活跃于民族国家的间谍活动中；三年前，它曾发起过臭名昭著的SolarWinds供应链攻击。

波兰军方和CERT警告说，APT29现在使用了一套全新的恶意软件工具重新回归了，据说它的任务是渗透到支持乌克兰的国家外交使团中。

**APT29使用新的工具重新回归**

根据波兰的通知，高级持续性威胁（APT）总是会以巧妙的鱼叉式网络钓鱼电子邮件来开始其攻击。

当局解释说，他们会伪造欧洲国家大使馆的电子邮件发送到外交机构的特定人员手中，这些信件中都包含了一个会议或共同处理文件的邀请。

收件人接下来会被要求按照指示点击一个链接或下载一个PDF文件，以查看大使的日历或获得会议的相关信息。这两种行为都会将目标引向一个恶意的网站，该网站加载了威胁集团的 "签名脚本"，报告称其为 "Envyscout"。

波兰官员补充说："网页利用了HTML-smuggling技术，即当网页被打开时，放在网页上的恶意文件会被JavaScript解码，然后下载到受害者的设备上。这使得恶意文件在存储它的服务器端更难被发现。

恶意网站还通过其他消息通知受害者，他们已经下载了正确的文件。

SlashNext的首席执行官Patrick Harr说，当信件的内容写得非常有迷惑性，使用大量的个人信息来证明发件人对目标很熟悉，并且发信人看起来来源很合法时，鱼叉式网络钓鱼攻击就会非常容易成功，这么看起来，这个间谍活动符合所有的成功标准。

例如，有一封钓鱼邮件声称是来自波兰大使馆。波兰当局还注意到，在观察活动期间，Envyscout程序已经被修改了三次，并且使用了更好的混淆技术。

根据波兰的警报，该组织一旦被渗透，就会采用修改后的Snowyamber下载器、Halfrig（其中嵌入了Cobalt Strike代码）和Quarterrig（与Halfrig共享代码）。

鉴于这一点，各国政府、外交官、国际组织和非政府组织（NGO）应保持高度警惕。

伴随着波兰网络安全当局的警告，加拿大总理贾斯汀-特鲁多最近公开表示，最近有一波与俄罗斯有关的针对加拿大基础设施的网络攻击。这些攻击包括对电力公司Hydro-Québec、魁北克港和劳伦森银行的网站的拒绝服务攻击。据特鲁多说，加拿大对乌克兰的支持是遭受到网络攻击的一个重要因素。

虽然加拿大的基础设施没有受到破坏，但加拿大网络安全中心主任Sami Khoury在上周的新闻发布会上强调，威胁是实实在在存在的。你必须保护好你的系统，如果你在运行重要的系统，为我们的社区供电，为加拿大人提供互联网接入，提供医疗保健，或在运营任何加拿大人所不能离开的服务,一定要注意你的网络设施的安全,及时实施缓解措。

本文翻译自：https://www.cysecurity.news/2023/04/russian-solarwinds-attackers-launch-new.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Q6gb7zGz)

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