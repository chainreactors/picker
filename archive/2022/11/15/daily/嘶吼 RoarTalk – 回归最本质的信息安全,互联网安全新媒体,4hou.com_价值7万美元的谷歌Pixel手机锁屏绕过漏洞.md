---
title: 价值7万美元的谷歌Pixel手机锁屏绕过漏洞
url: https://www.4hou.com/posts/jJjB
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-15
fetch_date: 2025-10-03T22:43:42.394585
---

# 价值7万美元的谷歌Pixel手机锁屏绕过漏洞

价值7万美元的谷歌Pixel手机锁屏绕过漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 价值7万美元的谷歌Pixel手机锁屏绕过漏洞

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-11-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)156733

收藏

导语：​研究人员发现一种可绕过谷歌Pixel手机锁屏的方法。

研究人员发现一种可绕过谷歌Pixel手机锁屏的方法。

![Google Pixel Phones](https://thehackernews.com/new-images/img/b/R29vZ2xl/AVvXsEhKeaBPnm6Mq_yeVsYaevt2EHebSnMMj4uqlADp45MXchrazM6QoKjAFCb3Nth8eJE4z1TUWcnmNgEXdZadiarKbVNLHCXo_voVTOIma3tmAJB7nq2UERQw0S2-pNVCgEF8Wm2MHQ4AzYsEKriaQHUVAtc26iHVV7FAHvo87EdFGpmUZNdqzC7ebHiS/s728-e1000/google-pixel-hacking.jpg)

近日，谷歌修复了一个影响所有Pixel 智能手机的高危安全漏洞，漏洞CVE编号CVE-2022-20465。该漏洞是一个锁屏绕过漏洞，攻击者利用该漏洞可以解锁Pixel 智能手机。

从谷歌官方发布的修复代码分析，该漏洞是由错误翻译SIM改变事件引发的不准确系统状态导致的漏洞，会使得锁屏保护无效。

研究人员称，通过以下步骤可以完全绕过Pixel的锁屏保护：

在锁屏的设备上输入3次错误指纹以禁用生物认证；

在不关机的情况下将手机的SIM卡替换为攻击者控制的SIM卡，并事先设置PIN码；

输入错误的SIM PIN码锁定SIM卡；

设备会要求用户输入SIM卡的PUK码以解锁SIM卡，PUK码是一个8位的数字；为攻击者控制的SIM卡输入新的PIN码；

设定自动解锁。

也就是说，攻击者将自己持有PIN锁定的SIM卡和该卡的PUK码就可以解锁Pixel手机。

攻击者利用该漏洞可以在物理接触受害者手机的情况下绕过手机的锁屏保护，包括指纹、PIN码等。

该漏洞是安全研究人员David Schütz在2022年6月发现的，谷歌于2022年11月安卓月度安全更新中修复了该漏洞。谷歌通过漏洞奖励计划向该漏洞的提交者Schütz奖励7万美元。

完整技术分析参见：https://bugs.xdavidhu.me/google/2022/11/10/accidental-70k-google-pixel-lock-screen-bypass/

本文翻译自：https://thehackernews.com/2022/11/hacker-rewarded-70000-for-finding-way.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?0WP2ECTH)

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