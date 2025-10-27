---
title: Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响
url: https://www.4hou.com/posts/MBz1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-28
fetch_date: 2025-10-03T23:54:42.080075
---

# Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响

Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Mali GPU漏洞补丁已发布，数百万安卓用户仍受到影响

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-11-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)156642

收藏

导语：​谷歌研究人员发现5个可被利用的Arm Mali GPU驱动漏洞在补丁发布数月后仍未修复。

谷歌研究人员发现5个可被利用的Arm Mali GPU驱动漏洞在补丁发布数月后仍未修复。

谷歌Project Zero安全研究人员在2022年6月发现了影响Arm Mali GPU驱动的多个安全漏洞，漏洞CVE编号为CVE-2022-33917、CVE-2022-36449。

CVE-2022-33917漏洞允许非特权用户进行不当GPU处理操作来访问空闲的内存空间。漏洞影响Arm Mali GPU kernel驱动Valhall r29p0版本到 r38p0版本。

CVE-2022-36449漏洞允许非特权用户访问释放的内存空间，进行缓存越界写，以及泄露内存映射细节。漏洞影响Arm Mali GPU kernel驱动Midgard r4p0版本到r32p0版本，Bifrost r0p0到r38p0版本、r39p0版本，Valhall r19p0到r39p0版本。

目前芯片厂商已经发布补丁。但研究人员发现在芯片厂商发布补丁数月后，相关漏洞仍然未被修复，数百万安卓用户设备受到影响，涉及谷歌、三星、小米、OPPO等其他手机厂商。相关品牌用户正在等待补丁到达终端用户。

芯片厂商发布补丁后，设备厂商需要时间来测试补丁并在其品牌的设备上实现，这一过程使得芯片厂商发布补丁到终端用户安装补丁之间存在时间差。

相关漏洞的验证等级为中，表明漏洞可被利用，而且会影响大量的安卓设备。Valhall驱动应用于Mali G710、G610、G510芯片中，而这些芯片应用在谷歌Pixel 7、Asus ROG Phone 6、红米Note 11、红米Note 12、荣耀Honor 70 Pro、RealMe GT、小米Xiaomi 12 Pro、Oppo Find X5 Pro、 Reno 8 Pro、Motorola Edge和OnePlus 10R中。

![Android devices using the Mali G710 chip](https://www.bleepstatic.com/images/news/u/1220909/devices/G710.png)

图 使用Mali G710芯片的安卓设备

Bifrost驱动应用于Mali G76、G72、G52芯片（2018年左右）中，采用这些芯片的设备有三星Galaxy S10、S9、A51和A71，红米Redmi Note 10、华为Huawei P30 、华为P40 Pro、荣耀Honor View 20、Motorola Moto G60S和 Realme 7。

Midgard驱动使用的芯片包括Mali T800和T700系列芯片，使用的设备包括三星Galaxy S7、Note 7、Sony Xperia X XA1、华为Mate 8、Nokia 3.1、LG X、红米Note 4。

目前，Arm的补丁尚未达到OEM厂商，安卓和Pixel也正在测试补丁。未来几周内，安卓将向相关厂商发布补丁，随后厂商将负责实现补丁并向用户推送。目前终端用户唯一能做的就是等待厂商提供补丁。

更多参见：https://googleprojectzero.blogspot.com/2022/11/mind-the-gap.html

本文翻译自：https://www.bleepingcomputer.com/news/security/mali-gpu-patch-gap-leaves-android-users-vulnerable-to-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?tpJvTh0n)

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