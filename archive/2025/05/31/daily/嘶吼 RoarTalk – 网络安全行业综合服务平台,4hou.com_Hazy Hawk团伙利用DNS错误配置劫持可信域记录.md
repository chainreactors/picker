---
title: Hazy Hawk团伙利用DNS错误配置劫持可信域记录
url: https://www.4hou.com/posts/YZ9M
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-31
fetch_date: 2025-10-06T22:23:34.746234
---

# Hazy Hawk团伙利用DNS错误配置劫持可信域记录

Hazy Hawk团伙利用DNS错误配置劫持可信域记录 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Hazy Hawk团伙利用DNS错误配置劫持可信域记录

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)75218

收藏

导语：使用这种技术，威胁者劫持多个域名来掩盖恶意活动，托管诈骗内容，或将它们用作诈骗操作的重定向中心。

一个名为“Hazy Hawk”的黑客劫持了被遗忘的DNS CNAME记录，这些记录指向被抛弃的云服务，并接管了政府、大学和财富500强公司的可信子域名，以分发诈骗、虚假应用程序和恶意广告。

根据Infoblox研究人员的说法，Hazy Hawk首先扫描带有指向废弃云端点的CNAME记录的域，他们通过被动DNS数据验证来确定。

接下来，他们注册一个与废弃CNAME中的名称相同的新云资源，导致原始域的子域解析到威胁者的新云托管站点。

使用这种技术，威胁者劫持多个域名来掩盖恶意活动，托管诈骗内容，或将它们用作诈骗操作的重定向中心。

被劫持域名的部分值得注意的例子包括：

**·**cdc.gov -美国疾病控制和预防中心

**·**honeywell.com-跨国企业集团

**·**berkeley.edu -加州大学伯克利分校

**·**michelin.co.uk -米其林轮胎英国

**·**ey.com、pwc.com、deloitte.com——全球四大咨询公司

**·**ted.com –著名的非营利媒体组织（TED演讲）

**·**Health .gov.au -澳大利亚卫生部

**·**unicef.org -联合国儿童基金会

**·**nyu.edu -纽约大学

**·**unilever.com -全球消费品公司

**·**ca.gov -加利福尼亚州政府

一旦攻击者获得对子域的控制，他们就会在子域下生成数百个恶意url，由于父域的高信任度，这些url在搜索引擎中看起来是合法的。

点击url的受害者会被重定向到多个层次的域名和TDS基础设施，这些基础设施会根据他们的设备类型、IP地址、VPN使用情况等对他们进行分析，以确定受害者的资格。

![overview.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250521/1747811377524376.png "1747810644270997.png")

Infoblox的报告称，这些网站被用于技术支持诈骗、虚假的防病毒警报、虚假的流媒体/色情网站和网络钓鱼页面。且允许浏览器推送通知的用户即使在离开诈骗网站后也会收到持续的警报，这可以为Hazy Hawk带来可观的收入。

![push-not.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250521/1747811379870789.png "1747810683102522.png")

同样的研究人员之前报告了另一个威胁者——“Savvy Seahorse,”，他也滥用CNAME记录来建立一个非典型的TDS，将用户重定向到虚假的投资平台。

CNAME记录很容易被忽视，因此它们容易被暗中滥用，似乎越来越多的威胁者意识到这一点，并试图利用这一点。

在“Hazy Hawk”的案例中，该行动的成功还依赖于组织在云服务退役后未能删除DNS记录，这使得攻击者可以在没有身份验证的情况下复制原始资源名称。

文章翻译自：https://www.bleepingcomputer.com/news/security/hazy-hawk-gang-exploits-dns-misconfigs-to-hijack-trusted-domains/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?q1ez6ZG0)

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