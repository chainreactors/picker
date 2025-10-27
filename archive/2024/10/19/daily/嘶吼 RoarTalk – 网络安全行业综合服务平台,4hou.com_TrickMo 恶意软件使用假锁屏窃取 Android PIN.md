---
title: TrickMo 恶意软件使用假锁屏窃取 Android PIN
url: https://www.4hou.com/posts/xyVn
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-19
fetch_date: 2025-10-06T18:46:42.759658
---

# TrickMo 恶意软件使用假锁屏窃取 Android PIN

TrickMo 恶意软件使用假锁屏窃取 Android PIN - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# TrickMo 恶意软件使用假锁屏窃取 Android PIN

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-10-18 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)93768

收藏

导语：TrickMo 于 2020 年首次由 IBM X-Force 记录，但据悉其至少从 2019 年 9 月起就被用于针对 Android 用户的攻击。

TrickMo Android 银行木马的 40 个新变种已在野外被发现，与 16 个植入程序和 22 个不同的命令和控制 (C2) 基础设施相关，具有旨在窃取 Android PIN 的新功能。

Zimperium 是在 Cleafy 之前发布的一份报告调查了当前流通的一些（但不是所有）变种之后报告了这一情况。

TrickMo 于 2020 年首次由 IBM X-Force 记录，但据悉其至少从 2019 年 9 月起就被用于针对 Android 用户的攻击。

**假锁屏窃取 Android PIN**

TrickMo 新版本的主要功能包括一次性密码 (OTP) 拦截、屏幕录制、数据泄露、远程控制等。该恶意软件试图滥用强大的辅助服务权限来授予自己额外的权限，并根据需要自动点击提示。

作为一种银行木马，它为用户提供各种银行和金融机构的网络钓鱼登录屏幕覆盖，以窃取他们的帐户凭据并使攻击者能够执行未经授权的交易。

![overlays.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241015/1728973644211351.png "1728973120170841.png")

攻击中使用的银行覆盖层

Zimperium 分析师在剖析这些新变体时还报告了一个新的欺骗性解锁屏幕，模仿真正的 Android 解锁提示，旨在窃取用户的解锁图案或 PIN。

欺骗性用户界面是托管在外部网站上的 HTML 页面，并在设备上以全屏模式显示，使其看起来像合法屏幕。

当用户输入解锁图案或 PIN 码时，页面会将捕获的 PIN 码或图案详细信息以及唯一的设备标识符（Android ID）传输到 PHP 脚本。

![lock-screen.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241015/1728973645107489.png "1728973179362011.png")

TrickMo 显示的假 Android 锁屏

窃取 PIN 允许攻击者通常在深夜在设备未受到主动监控时解锁设备，以实施设备欺诈。

**受害者分布图**

由于 C2 基础设施安全不当，Zimperium 确定至少有 13,000 名受害者受到该恶意软件的影响，其中大多数位于加拿大，在阿拉伯联合酋长国、土耳其和德国也发现了大量受害者。

![victims.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241015/1728973646656330.png "1728973270118697.png")

TrickMo 受害者分布图

根据 Zimperium 的说法，这个数字相当于“几台 C2 服务器”，因此 TrickMo 受害者的总数可能更高。

据安全研究员分析表明，每当恶意软件成功窃取凭据时，IP 列表文件就会定期更新，在这些文件中已经发现了数百万条记录，表明威胁者访问了大量受感染的设备和大量敏感数据。

Cleafy 此前曾向公众隐瞒了妥协的迹象，因为配置错误的 C2 基础设施可能会将受害者数据暴露给更广泛的网络犯罪社区，但 Zimperium 现在选择将所有内容发布到这个 GitHub 存储库上。

然而，TrickMo 的目标范围十分广泛，涵盖银行以外的应用程序类型（和帐户），包括 VPN、流媒体平台、电子商务平台、交易、社交媒体、招聘和企业平台。

TrickMo 目前通过网络钓鱼进行传播，因此为了最大限度地降低感染的可能性，人们应避免不认识的人通过短信或直接消息发送的 URL 下载 APK。

Google Play Protect 可识别并阻止 TrickMo 的已知变体，因此确保其在设备上处于活动状态对于防御恶意软件至关重要。

文章翻译自：https://www.bleepingcomputer.com/news/security/trickmo-malware-steals-android-pins-using-fake-lock-screen/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0qzr6NR8)

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