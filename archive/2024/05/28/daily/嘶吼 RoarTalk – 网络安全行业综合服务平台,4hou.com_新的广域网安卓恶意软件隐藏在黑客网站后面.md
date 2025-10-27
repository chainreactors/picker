---
title: 新的广域网安卓恶意软件隐藏在黑客网站后面
url: https://www.4hou.com/posts/yA0n
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-28
fetch_date: 2025-10-06T16:48:21.250710
---

# 新的广域网安卓恶意软件隐藏在黑客网站后面

新的广域网安卓恶意软件隐藏在黑客网站后面 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 新的广域网安卓恶意软件隐藏在黑客网站后面

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-05-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)181751

收藏

导语：WPEPER的主要功能是窃取数据，这是由其具有13个不同功能的大量命令所组成的。

有安全研究人员在至少两家非官方的应用程序商店中发现了一种名为"Wpeper"的新安卓后门恶意软件，这是一家模仿上端应用程序商店的非官方应用程序商店。

WPEP的突出之处在于它新的使用，即它受损害的语言网站作为其实际的指挥和控制(C2)服务器的中继器是一种逃避机制。

Android 恶意软件是由 QAX 的 XLab 团队于 2024 年 4 月 18 日在检查嵌入到 APK（Android 包文件）中的先前未知的 ELF 文件时发现的，该文件的病毒检测总数为零。

该活动于 4 月 22 日突然停止，大概是为了保持低调并为了避免被安保专业人员和自动化系统发现。

根据谷歌和被动DNS的数据，X实验室推断在WPEPOP发现时，目前已经感染了成千上万的设备，但实际的操作规模仍然未知。

![malicious-APK.webp.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240507/1715067481166241.jpg "1715066531106754.jpg")

第三方应用程序商店的恶意APK

**滥用语言作为C2**

WPEPER的新型C2通信系统是为了充分利用受影响的语言媒体网站和中间中继点，掩盖了其实际C2服务器的位置和身份。

从C2发送给机器人的任何命令都是通过这些站点转发的，它们是另外的AES加密和签名椭圆曲线签名，以防止未经授权的第三方接管。

![wordpress-c2s-decoded.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240507/1715067482265165.jpg "1715066571979710.jpg")

硬编码C2地址

WPEP可以通过相关命令的接收来动态地更新其C2服务器，因此，如果清除了一个语言媒体站点，则可以向僵尸网络发送不同站点上的新中继点。

在不同的主机和地点使用多个受损害的站点，增加了C2机制的复原力，使得关闭操作变得困难，此举甚至破坏了单个受感染的安卓设备上的数据交换。

**恶意软件功能**

WPEPER的主要功能是窃取数据，这是由其具有13个不同功能的大量命令所组成的。

后门恶意软件中的支持命令是：

1.检索受感染设备的详细信息，如硬件规格和操作系统细节

2.收集设备上所有已安装应用程序的列表

3.接收新的C2服务器地址以更新机器人的命令源列表

4.调整与C2服务器的通信频率

5.接收验证命令签名的新公钥

6.从C2服务器下载任意文件

7.检索存储在设备上的特定文件的信息

8.收集设备上特定目录的信息

9.在设备外壳中运行命令

10.下载一个文件并执行它

11.更新恶意软件并执行文件

12.从设备中删除恶意软件

13.从指定的URL下载文件并执行它

目前还不清楚这些被盗数据是如何使用的，但潜在的风险确认包括账户劫持、网络渗透、情报收集、身份盗窃和金融欺诈。

为了避免像wpeper这样的风险出现，建议用户只从官方应用程序商店(谷歌游戏)安装应用程序，并确保操作系统内置的反恶意软件工具“游戏保护”在设备上是活跃的。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-wpeeper-android-malware-hides-behind-hacked-wordpress-sites/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6pRjLWry)

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