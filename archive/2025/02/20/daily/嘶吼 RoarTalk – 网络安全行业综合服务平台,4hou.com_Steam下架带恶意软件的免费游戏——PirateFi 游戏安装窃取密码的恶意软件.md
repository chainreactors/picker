---
title: Steam下架带恶意软件的免费游戏——PirateFi 游戏安装窃取密码的恶意软件
url: https://www.4hou.com/posts/gyyr
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-02-20
fetch_date: 2025-10-06T20:32:46.123281
---

# Steam下架带恶意软件的免费游戏——PirateFi 游戏安装窃取密码的恶意软件

Steam下架带恶意软件的免费游戏——PirateFi 游戏安装窃取密码的恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Steam下架带恶意软件的免费游戏——PirateFi 游戏安装窃取密码的恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-02-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)81827

收藏

导语：这款游戏在Steam目录中出现了近一周的时间，并被多达1500名用户下载。分发服务正在向可能受到影响的用户发送通知，建议他们重新安装Windows。

最新发现，Steam商店中一款名为PirateFi的免费游戏一直在向用户传播Vidar信息窃取恶意软件。

在2月6日至2月12日期间，这款游戏在Steam目录中出现了近一周的时间，并被多达1500名用户下载。分发服务正在向可能受到影响的用户发送通知，建议他们重新安装Windows。

**Steam上的恶意软件**

上周，Seaworth Interactive在Steam上发布了《PirateFi》，并获得了积极评价。它被描述为一款以低多边形世界为背景的生存游戏，涉及基地建设、武器制作和食物收集。

![steam-pirate.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250217/1739772935125558.png "1739772283149153.png")

PirateFi的Steam页面

本周，Steam发现这款游戏含有恶意软件，但并未指明具体类型。通知中写道：“这款游戏开发者的Steam账户上传了包含可疑恶意软件的构建。”

用户在Steam上玩PirateFi（3476470）时，这些构建是活跃的，所以这些恶意文件很可能在用户的计算机上启动。Steam建议用户使用最新的防病毒软件运行完整的系统扫描，检查他们不认识的新安装的软件，并考虑操作系统格式。

![notification.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250217/1739772937761361.png "1739772610445156.png")

Steam对受影响用户的通知

受影响的用户还在游戏的Steam社区页面上发布了安全提醒，通知其他人不要启动该游戏，因为他们的杀毒软件将其识别为恶意软件。

SECUINFRA Falcon Team的Marius Genheimer获得了通过PirateFi传播的恶意软件样本，并将其识别为Vidar伪造软件的一个版本。

SECUINFRA建议：“如果你是下载这个“游戏”的玩家之一：考虑保存在浏览器、电子邮件客户端、加密货币钱包等中的凭据、会话cookie和秘密被泄露。”建议用户更改所有可能受影响帐户的密码，并在可能的情况下激活多因素身份验证保护。

基于动态分析和YARA签名匹配，该恶意软件被识别为Vidar，隐藏在一个名为Pirate.exe的文件中，作为有效载荷（Howard.exe），与InnoSetup安装程序打包在一起。

攻击者多次修改游戏文件，使用各种混淆技术，并更改命令和控制服务器以获取凭据。研究人员认为，PirateFi名称中提到的web3/ b区块链/加密货币是有意为之，目的是吸引特定的玩家群体。

Steam并没有公布有多少用户受到了PirateFi恶意软件的影响，但游戏页面上的统计数据显示，可能有多达1500人受到了影响。

![PirateFi_Steam_dlds.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250217/1739772939118101.png "1739772685154970.png")

恶意软件渗透Steam商店并不常见，但也不是没有先例。在2023年2月，Steam用户受到了恶意Dota 2游戏模式的攻击，该模式利用Chrome n-day漏洞在玩家的计算机上执行远程代码执行。

2023年12月，当时很受欢迎的独立策略游戏《Slay the Spire》的一个mod被黑客入侵，黑客将“Epsilon”信息传输器注入其中。

目前Steam已经引入了其他措施，如开启短信验证等，以保护玩家免受未经授权的恶意更新，但PirateFi的案例表明，目前这些措施还远远不够。

文章翻译自：https://www.bleepingcomputer.com/news/security/piratefi-game-on-steam-caught-installing-password-stealing-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?MaoAIE3t)

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