---
title: 大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求
url: https://www.4hou.com/posts/l01l
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-26
fetch_date: 2025-10-02T20:42:08.699490
---

# 大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求

大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)48245

收藏

导语：该团伙通过Google Play商店中的224款恶意应用，日均发起23亿次广告请求。

一个名为“SlopAds”的大规模Android广告欺诈团伙已被瓦解。此前，该团伙通过Google Play商店中的224款恶意应用，日均发起23亿次广告请求。

这一广告欺诈活动由HUMAN公司的Satori威胁情报团队发现。据报告，这些恶意应用的下载量超过3800万次，且通过代码混淆和隐写术隐藏恶意行为，规避谷歌的检测与安全工具的扫描。

SlopAds的影响范围覆盖全球，来自228个国家的用户曾安装过相关应用。该团伙日均发起23亿次广告竞价请求，其中广告曝光量最高的地区为美国（占比30%），其次是印度（10%）和巴西（7%）。

研究人员将该活动命名为“SlopAds”，一方面是因为相关恶意应用表面看似批量生成，类似AI粗制内容；另一方面，也是参考了威胁者命令与控制（C2）服务器上托管的一系列AI主题应用及服务。

![slopads-apps.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250917/1758093012157557.jpg "1758092605585362.jpg")

与SlopAds广告欺诈活动相关的Android应用程序

**SlopAds广告欺诈活动的技术细节**

为规避谷歌的应用审核流程与安全软件检测，SlopAds的广告欺诈机制包含多层逃避策略，具体攻击流程如下：

**1. 根据安装来源判断行为模式**：若用户从Play商店“自然安装”该应用（非通过团伙投放的广告跳转），应用会伪装成正常应用，执行其宣称的功能（如工具类、娱乐类功能）；

![slopads-diagram.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250917/1758093013530919.jpg "1758092674103546.jpg")

SlopAds 广告欺诈恶意软件工作流程

但如果检测到用户是通过点击团伙投放的广告安装应用，就会通过Firebase远程配置下载一个加密配置文件——该文件包含广告欺诈恶意模块的URL、提现服务器地址及JavaScript载荷。

**2. 设备环境验证**：应用会进一步判断自身是否安装在“真实用户设备”上，以避开研究人员或安全软件的分析环境。

**3. 通过隐写术加载恶意模块**：若通过上述所有检测，应用会下载4张PNG图片——这些图片通过隐写术隐藏了恶意APK（安卓应用安装包）的碎片。

![slopads-steganography.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250917/1758093014155725.jpg "1758092702208009.jpg")

使用隐写术将恶意代码隐藏在图像中

图片下载完成后，设备会对其解密并重组，生成完整的“FatModule”恶意软件，该软件是实施广告欺诈的核心组件。

**4. 发起广告欺诈并获利**：FatModule激活后，会通过隐藏的WebView（网页视图）收集设备与浏览器信息，随后跳转到攻击者控制的广告欺诈（提现）域名。

这些域名伪装成游戏网站或新闻网站，通过隐藏的WebView界面持续加载广告，日均生成超20亿次欺诈性广告曝光与点击，为攻击者创造非法收益。

**后续处置与风险预警**

HUMAN指出，SlopAds的基础设施包含多个C2服务器及300多个相关推广域名，这表明威胁者原本计划在已发现的224款应用之外，进一步扩大攻击范围。

目前，谷歌已从Play商店下架所有已确认的SlopAds恶意应用，且Android系统的“Google Play Protect”功能已完成更新——若用户设备中仍存在此类应用，该功能会发出警告，提示用户卸载。

根据此次广告欺诈活动的技术复杂度表明，威胁者很可能会调整攻击方案在未来发起新的欺诈活动，用户应随时保持警惕态度。

文章翻译自：https://www.bleepingcomputer.com/news/security/google-nukes-224-android-malware-apps-behind-massive-ad-fraud-campaign/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?eQuuirVt)

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