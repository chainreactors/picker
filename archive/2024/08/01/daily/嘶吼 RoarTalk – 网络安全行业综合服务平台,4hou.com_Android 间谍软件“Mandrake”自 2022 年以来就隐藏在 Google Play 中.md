---
title: Android 间谍软件“Mandrake”自 2022 年以来就隐藏在 Google Play 中
url: https://www.4hou.com/posts/ArPO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-08-01
fetch_date: 2025-10-06T18:01:54.449000
---

# Android 间谍软件“Mandrake”自 2022 年以来就隐藏在 Google Play 中

Android 间谍软件“Mandrake”自 2022 年以来就隐藏在 Google Play 中 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Android 间谍软件“Mandrake”自 2022 年以来就隐藏在 Google Play 中

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-07-31 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)99157

收藏

导语：卡巴斯基确定了五款携带 Mandrake 的应用程序。

Bitdefender 于 2020 年首次记录了 Android 间谍软件“Mandrake”，研究人员强调了该恶意软件复杂的间谍功能，并指出它至少从 2016 年开始就在野外运行。

卡巴斯基最近报告称，具有更好的混淆和规避功能的 Mandrake 新变种已经通过 2022 年提交给 Google Play 的五个应用程序潜入进来。

这些应用程序至少持续可用一年，而最后一个应用程序 AirFS（在受欢迎程度和感染率方面较为突出）于 2024 年 3 月底被删除。

![airfs.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240730/1722331364711126.png "1722321696122947.png")

Google Play 上的 AirFS

卡巴斯基确定了五款携带 Mandrake 的应用程序如下：

**· AirFS** – it9042 通过 Wi-Fi 共享文件（2022 年 4 月 28 日至 2024 年 3 月 15 日期间下载量为 30,305 次）

**· Astro Explorer** 来自 shevabad（2022 年 5 月 30 日至 2023 年 6 月 6 日期间下载量为 718 次）

**· Amber**来自 kodaslda （2022 年 2 月 27 日至 2023 年 8 月 19 日期间下载量为 19 次）

**· CryptoPulsing**来自 shevabad（2022 年 11 月 2 日至 2023 年 6 月 6 日期间下载量为 790 次）

**·Brain Matrix** 来自 kodaslda（2022 年 4 月 27 日至 2023 年 6 月 6 日期间下载量为 259 次）

该网络安全公司表示，大多数下载来自加拿大、德国、意大利、墨西哥、西班牙、秘鲁和英国。

![apps.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240730/1722331366168996.png "1722321794142488.png")

四款应用将 Mandrake 恶意软件植入受害者设备

**逃避侦查**

与将恶意逻辑放置在应用程序的 DEX 文件中的典型 Android 恶意软件不同，Mandrake 将其初始阶段隐藏在本机库“libopencv\_dnn.so”中，该库使用 OLLVM 进行大量混淆。

在恶意应用程序安装后，该库会导出函数以从其资产文件夹解密第二阶段加载器 DEX 并将其加载到内存中。

第二阶段请求绘制覆盖的权限并加载第二个本机库“libopencv\_java3.so”，该库解密证书以便与命令和控制（C2）服务器进行安全通信。

与 C2 建立通信后，该应用程序会发送设备配置文件，并在认为合适时接收核心 Mandrake 组件（第三阶段）。一旦激活核心组件，Mandrake 间谍软件就可以执行各种恶意活动，包括数据收集、屏幕录制和监控、命令执行、模拟用户滑动和点击、文件管理和应用程序安装。

值得注意的是，威胁者可以通过显示模仿 Google Play 的通知来提示用户安装更多恶意 APK，诱骗用户通过看似可信的过程安装不安全的文件。

卡巴斯基表示，该恶意软件还使用基于会话的安装方法来绕过 Android 13（及更高版本）对非官方来源 APK 安装的限制。

与其他 Android 恶意软件一样，Mandrake 可以要求用户授予在后台运行的权限，并在受害者的设备上隐藏植入程序应用程序的图标，从而秘密运行。

该恶意软件的最新版本还具有逃避攻击的功能，可在 Frida（一种在安全分析师中流行的动态检测工具包）中存在。

它还检查设备根状态，搜索与其相关的特定二进制文件，验证系统分区是否以只读方式安装，并检查设备上是否启用了开发设置和 ADB。

Mandrake 威胁仍然存在，尽管卡巴斯基认定为植入程序的五款应用已不再在 Google Play 上提供，但该恶意软件可能会通过新的、更难检测的应用卷土重来。

建议 Android 用户仅安装来自信誉良好的发行商的应用，在安装前查看用户评论，避免授予与应用功能无关的危险权限请求，并确保 Play Protect 始终处于活动状态。

Google 也分享了有关在 Google Play 上发现恶意应用的声明表示，Google Play Protect 会自动保护 Android 用户免受已知版本的恶意软件侵害，该功能在安装有 Google Play 服务的 Android 设备上默认启用。Google Play Protect 可以警告用户或阻止已知表现出恶意行为的应用程序，即使这些应用程序来自 Play 以外的来源。

文章翻译自：https://www.bleepingcomputer.com/news/security/android-spyware-mandrake-hidden-in-apps-on-google-play-since-2022/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6mM43ZXK)

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