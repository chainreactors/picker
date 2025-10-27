---
title: 名为“StaryDobry”的大规模恶意软件活动爆发
url: https://www.4hou.com/posts/wx5r
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-28
fetch_date: 2025-10-06T20:35:31.413968
---

# 名为“StaryDobry”的大规模恶意软件活动爆发

名为“StaryDobry”的大规模恶意软件活动爆发 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 名为“StaryDobry”的大规模恶意软件活动爆发

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-02-27 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)72863

收藏

导语：这些攻击中使用的XMRig连接到私有挖矿服务器，而不是公共矿池，这使得收益更难追踪。

一场名为“StaryDobry”的大规模恶意软件活动以破解游戏《Garry’s Mod， BeamNG》的木马版本为目标，攻击全球玩家。

这些游戏都是Steam上拥有数十万“绝对正面”评价的顶级游戏，因此它们很容易成为恶意活动的目标。

值得注意的是，据报道，在2024年6月，一个带花边的光束模型被用作迪士尼黑客攻击的初始访问向量。

根据卡巴斯基的说法，StaryDobry活动始于2024年12月下旬，结束于2025年1月27日。它主要影响来自德国、俄罗斯、巴西、白俄罗斯和哈萨克斯坦的用户。

攻击者在2024年9月提前几个月将受感染的游戏安装程序上传到torrent网站，并在假期期间触发游戏中的有效载荷，从而降低了检测的可能性。

![timeline(1).webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250219/1739958813205196.png "1739958342112894.png")

StaryDobry活动时间表

**StaryDobry感染链**

StaryDobry活动使用了一个多阶段感染链，最终以XMRig加密程序感染告终。用户从种子网站下载了木马化的游戏安装程序，这些程序看起来都很正常。

![torrent.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250219/1739958814998754.png "1739958435171906.png")

活动中使用的恶意种子之一

在游戏安装过程中，恶意软件卸载程序（unrar.dll）被解包并在后台启动，在继续之前，它会检查它是否在虚拟机，沙箱或调试器上运行。

恶意软件表现出高度规避行为，如果它检测到任何安全工具，立即终止，可能是为了避免损害声誉。

![debug-checks.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250219/1739958815174946.png "1739958486660349.png")

Anti-debug检查

接下来，恶意软件使用‘regsvr32.exe’进行持久化注册，并收集详细的系统信息，包括操作系统版本、国家、CPU、 RAM和GPU详细信息，并将其发送到pinokino[.]fun的命令和控制（C2）服务器。

最终，dropper解密并将恶意软件加载程序（MTX64.exe）安装在系统目录中。

加载程序冒充Windows系统文件，进行资源欺骗，使其看起来是合法的，并创建一个计划任务，在重新启动之间持久化。如果主机至少有8个CPU内核，它将下载并运行XMRig挖掘器。

StaryDobry中使用的XMRig挖掘器是Monero挖掘器的修改版本，它在执行之前在内部构造其配置，并且不访问参数。

矿工始终维护一个单独的线程，监视在受感染的机器上运行的安全工具，如果检测到任何进程监视工具，它将关闭自己。

这些攻击中使用的XMRig连接到私有挖矿服务器，而不是公共矿池，这使得收益更难追踪。

卡巴斯基无法将这些攻击归因于任何已知的威胁组织。StaryDobry往往是一个一次性的活动。为了植入矿工，攻击者通常会实施一个复杂的执行链，利用寻求免费游戏的用户。这种方法可以帮助威胁者能够维持采矿活动的强大游戏机，最大限度地利用了矿工植入物。

文章翻译自：https://www.bleepingcomputer.com/news/security/cracked-garrys-mod-beamngdrive-games-infect-gamers-with-miners/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?RDxC8FBF)

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