---
title: 新型 Vo1d 恶意软件感染了 130 万个 Android 流媒体盒
url: https://www.4hou.com/posts/zA7r
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-14
fetch_date: 2025-10-06T18:24:28.045648
---

# 新型 Vo1d 恶意软件感染了 130 万个 Android 流媒体盒

新型 Vo1d 恶意软件感染了 130 万个 Android 流媒体盒 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新型 Vo1d 恶意软件感染了 130 万个 Android 流媒体盒

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-13 18:30:40

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)91024

收藏

导语：为了防止感染此恶意软件，建议 Android 用户在有新固件更新时检查并安装。

Android 开源项目 (AOSP) 是由 Google 领导的开源操作系统，可用于移动、流媒体和物联网设备。日前，安全研究人员发现威胁者已经用一种新的 Vo1d 后门恶意软件感染了超过 130 万个运行 Android 的电视流媒体盒，从而使攻击者能够完全控制这些设备。

Dr.Web 在一份新报告中表示，研究人员发现，超过 200 个国家/地区有 130 万台设备感染了 Vo1d 恶意软件，其中巴西、摩洛哥、巴基斯坦、沙特阿拉伯、俄罗斯、阿根廷、厄瓜多尔、突尼斯、马来西亚、阿尔及利亚和印度尼西亚等国感染数量最多。

![vo1d-malware-heatmap.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726196005422637.png "1726193345184374.png")

受 Vo1d 感染的电视盒的地理分布

此次恶意软件活动所针对的 Android 固件包括：

**·**Android 7.1.2；

**·**R4 构建/NHG47K Android 12.1；

**·**电视盒构建/NHG47K Android 10.1；

**·**KJ-SMART4KVIP 构建/NHG47K。

根据安装的 Vo1d 恶意软件的版本，该活动将修改 install-recovery.sh、daemonsu，或替换 debuggerd 操作系统文件，这些都是 Android 中常见的启动脚本。

![install-recovery_sh-file.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240913/1726196006212245.png "1726193419154403.png")

修改 install-recovery.sh 文件

恶意软件活动使用这些脚本来保持持久性并在启动时启动 Vo1d 恶意软件。

Vo1d 恶意软件本身位于 wd 和 vo1d 文件中，该恶意软件以这两个文件命名。Android.Vo1d 的主要功能隐藏在其 vo1d（Android.Vo1d.1）和 wd（Android.Vo1d.3）组件中，这两个组件协同运行。

Android.Vo1d.1 模块负责 Android.Vo1d.3 的启动并控制其活动，必要时重新启动其进程。此外，它还可以在 C&C 服务器发出命令时下载并运行可执行文件。反过来，Android.Vo1d.3 模块会安装并启动加密并存储在其主体中的 Android.Vo1d.5 守护进程。该模块还可以下载并运行可执行文件。此外，它还会监视指定目录并安装在其中找到的 APK 文件。

虽然 Dr.Web 不知道 Android 流媒体设备是如何受到攻击的，但研究人员认为它们之所以成为攻击目标，是因为它们通常运行会存在漏洞的过时软件。

Dr.Web 总结道：“一种可能的感染媒介可能是利用操作系统漏洞获取 root 权限的中间恶意软件的攻击。另一种可能的媒介可能是使用内置 root 访问权限的非官方固件版本。”

为了防止感染此恶意软件，建议 Android 用户在有新固件更新时检查并安装。此外，请务必从互联网上删除这些盒子，以防它们通过暴露的服务被远程利用。同样重要的是，避免在 Android 上安装来自第三方网站的 Android 应用程序作为 APK，因为它们是恶意软件的常见来源。

9月12号最新公告表示，受感染的设备并未运行 Android TV，而是使用 Android 开放源代码项目 (AOSP)。

Google 发言人表示：“这些被发现感染的杂牌设备不是经过 Play Protect 认证的 Android 设备。如果设备未通过 Play Protect 认证，Google 就没有安全性和兼容性测试结果记录。”

目前经过 Play Protect 认证的 Android 设备已经经过测试，可确保质量和用户安全。为了用户确认设备是否采用 Android TV 操作系统和经过 Play Protect 认证， Android TV 网站提供了最新的合作伙伴列表，用户可以按照相应步骤检查设备是否经过 Play Protect 认证。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-vo1d-malware-infects-13-million-android-streaming-boxes/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?86xk05Y7)

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