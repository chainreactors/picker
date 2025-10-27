---
title: 数百个美国新闻网站遭到SocGholish供应链攻击
url: https://www.4hou.com/posts/wgNg
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-06
fetch_date: 2025-10-03T21:49:02.893591
---

# 数百个美国新闻网站遭到SocGholish供应链攻击

数百个美国新闻网站遭到SocGholish供应链攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 数百个美国新闻网站遭到SocGholish供应链攻击

布加迪
[新闻](https://www.4hou.com/category/news)
2022-11-05 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)172516

收藏

导语：一伙威胁分子正在利用一家未披露身份的媒体公司受攻击的基础设施，在全美数百家报纸的网站上部署SocGholish JavaScript恶意软件框架。

一伙威胁分子正在利用一家未披露身份的媒体公司受攻击的基础设施，在全美数百家报纸的网站上部署SocGholish JavaScript恶意软件框架，又叫FakeUpdates（虚假更新）。

这起供应链攻击背后的威胁分子（被Proofpoint编号为TA569）将恶意代码注入到一个无害的JavaScript文件中，而该文件被众多新闻媒体的网站加载。

这个恶意的JavaScript文件用于安装SocGholish，这种恶意软件框架可以使用恶意软件载荷感染访问受攻击网站的那些用户，这些恶意软件载荷伪装成虚假的浏览器更新，而这些更新通过虚假的更新提醒以ZIP压缩包的方式来分发，比如Chrome.Uрdatе.zip、Chrome.Updater.zip、Firefoх.Uрdatе.zip、Opera.Update.zip和 Oper.Updte.zip。

Proofpoint的威胁洞察团队今天在Twitter上透露：“Proofpoint威胁研究团队观察到，一家为许多主要新闻机构提供服务的媒体公司受到了间歇性注入。这家媒体公司通过JavaScript向合作伙伴提供内容。”

“通过修改这个原本无害的JavaScript的代码库，它现在被用于部署SocGholish。”

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667425690477679.png "1667425690477679.png")

图1. 恶意JavaScript文件对内容做了混淆处理（来源：BleepingComputer）

据企业安全公司Proofpoint的安全研究人员声称，这个恶意软件安装在了总共250多家美国新闻机构的网站上，其中一些还是大型新闻机构。

虽然目前共有多少家新闻机构影响尚不清楚，但Proofpoint表示，它获悉来自纽约、波士顿、芝加哥、迈阿密、华盛顿特区等地区的媒体机构（包括国家性新闻机构）已受到了影响。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667425680134579.png "1667425680134579.png")

图2.与勒索软件攻击有关联

Proofpoint此前观察到SocGholish活动使用虚假的更新和网站重定向来感染用户，在一些情况下还添加勒索软件载荷。

Evil Corp网络犯罪团伙在一次非常相似的活动中也使用了SocGholish，通过由数十个受攻击的美国报纸网站分发虚假的软件更新提醒，感染了30多家美国大型私营企业的员工。

受感染的计算机随后被用作借机闯入雇主企业网络的跳板，企图部署该团伙的WastedLocker勒索软件。

幸运的是，赛门铁克在一份报告中透露，它阻止了Evil Corp企图加密受攻击网络的活动，这起攻击针对多家私营公司，包括30家美国公司，其中8家还是《财富》500强公司。

SocGholish最近还被用于在感染上了Raspberry Robin恶意软件的网络中植入后门，微软称之为Evil Corp前勒索软件（pre-ransomware）行为。

本文翻译自：https://www.bleepingcomputer.com/news/security/hundreds-of-us-news-sites-hit-in-socgholish-supply-chain-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?yFGrIaLo)

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