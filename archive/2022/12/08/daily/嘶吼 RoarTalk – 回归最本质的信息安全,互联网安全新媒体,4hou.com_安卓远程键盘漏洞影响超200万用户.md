---
title: 安卓远程键盘漏洞影响超200万用户
url: https://www.4hou.com/posts/PJy6
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-08
fetch_date: 2025-10-04T00:51:14.312714
---

# 安卓远程键盘漏洞影响超200万用户

安卓远程键盘漏洞影响超200万用户 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 安卓远程键盘漏洞影响超200万用户

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-12-07 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)144941

收藏

导语：​研究人员在3款远程键盘中发现7个安全漏洞，影响超过200万用户。

研究人员在3款远程键盘中发现7个安全漏洞，影响超过200万用户。

远程键盘APP允许用户将设备通过无线方式连接到计算机。Synopsys研究人员在3款远程键盘APP中发现多个安全漏洞，攻击者利用相关漏洞可以泄露用户键盘输入，并实现远程代码执行。受影响的3款APP在谷歌应用商店累计下载量超过200万次。

![PC Keyboard and Lazy Mouse still available on Google Play](https://www.bleepstatic.com/images/news/u/1220909/Android%20malware/play-store-apps.png)

图 谷歌play中的PC Keyboard和 Lazy Mouse

受影响的APP分别是PC Keyboard、Lazy Mouse、Telepad，受影响的版本既包括免费版，也包括付费版。研究人员在这3款APP中发现了弱认证机制或没有认证授权机制、不安全的通信等问题。漏洞CVE编号分别为：CVE-2022-45477：是Telepad APP中的安全漏洞，CVSS评分9.8分。攻击者利用该漏洞可以在非授权的请求下发送指令给服务器来执行任意代码，而无需认证或授权。

CVE-2022-45478：是Telepad APP中的安全漏洞，CVSS评分5.1分。攻击者利用该漏洞可以发起中间人攻击，并读取所有键盘输入。

CVE-2022-45479：是PC Keyboard APP中的安全漏洞，CVSS评分9.8分。攻击者利用该漏洞可以在非授权的请求下发送指令给服务器来执行任意代码，而无需认证或授权。

CVE-2022-45480：是PC Keyboard APP中的安全漏洞，CVSS评分5.1分。攻击者利用该漏洞可以发起中间人攻击，并读取所有键盘输入。

CVE-2022-45481：是Lazy Mouse APP默认配置中缺乏密码要求引发的安全漏洞，CVSS评分9.8分。未经认证的攻击者利用在漏洞可以在无需认证或授权的情况下执行任意代码。

CVE-2022-45482：是Lazy Mouse服务器弱密码要求，没有实现尝试次数限制。攻击者利用该漏洞可以暴力破解PIN码，并执行任意命令。

CVE-2022-45483：是Lazy Mouse APP中的安全漏洞，CVSS评分5.1分。攻击者利用该漏洞可以执行中间人攻击，并提取键盘输入。

目前，这三款APP都不再维护或支持。Telepad已从谷歌play应用商店移除，但仍然可以从官网下载。

![Telepad is no longer on Google Play, but it's available from the official website](https://www.bleepstatic.com/images/news/u/1220909/Android%20malware/Telepad.png)

继续使用有漏洞的APP可能会暴露用户敏感信息。远程攻击者成功利用漏洞可以在用户设备上执行任意代码。研究人员建议用户在下载远程键盘APP之前首先检查用户评分，阅读隐私政策，并检查是否是最新版本。如果可以的话，还应确认数据的数据是否是加密的。

本文翻译自：https://www.bleepingcomputer.com/news/security/critical-rce-bugs-in-android-remote-keyboard-apps-with-2m-installs/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?RnBznXn4)

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

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

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

[查看更多](https://www.4hou.com/member/e7OO)

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