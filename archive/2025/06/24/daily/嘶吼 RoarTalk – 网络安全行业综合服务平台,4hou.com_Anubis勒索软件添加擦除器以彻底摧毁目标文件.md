---
title: Anubis勒索软件添加擦除器以彻底摧毁目标文件
url: https://www.4hou.com/posts/jBWl
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-06-24
fetch_date: 2025-10-06T22:51:51.493044
---

# Anubis勒索软件添加擦除器以彻底摧毁目标文件

Anubis勒索软件添加擦除器以彻底摧毁目标文件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Anubis勒索软件添加擦除器以彻底摧毁目标文件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-06-23 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)77456

收藏

导语：Anubis攻击始于带有恶意链接或附件的网络钓鱼电子邮件。

Anubis的勒索软件即服务（RaaS）业务在其文件加密恶意软件中添加了一个擦除器模块，可以摧毁目标文件，即使支付赎金也无法恢复。

Anubis（不要与同名的Android恶意软件混淆，该恶意软件有一个勒索软件模块）是一个相对新的RaaS，于2024年12月首次被观察到，但在年初变得更加活跃。

2月23日，运营商在RAMP论坛上宣布了一项联盟计划。KELA当时的一份报告解释说，Anubis向勒索软件附属公司提供了80%的收益分成。数据勒索附属公司获得了60%的分成，初始访问经纪人获得了50%的分成。

目前，Anubis在暗网上的勒索页面只列出了8名受害者，这表明一旦对技术方面的信心增强，它可能会增加攻击量。

在这方面，Trend Micro最近发布的一份报告显示，Anubis的运营商正在积极开发新功能，其中一个不寻常的功能是文件清除功能。

研究人员在他们解剖的最新Anubis样本中发现了这个功能，并认为该功能的引入是为了增加受害者尽快付款的压力，而不是拖延谈判或完全无视。

Anubis与其他RaaS的区别在于，它使用了文件擦除功能，即使在加密后也会破坏恢复工作。这种破坏性倾向增加了受害者的压力，并增加了本已具有破坏性的袭击的风险。

使用命令行参数‘ /WIPEMODE ’激活破坏性行为，这需要发出基于密钥的身份验证。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250616/1750042535180618.png "1750042016167393.png")

Anubis的擦拭模式

激活后，擦除器擦除所有文件内容，将其大小减小到0 KB，同时保持文件名和结构完整。受害者仍然会看到预期目录中的所有文件，但其内容将被不可逆转地破坏，使恢复成为不可能。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250616/1750042536100320.png "1750042113171417.png")

加密前（上）和加密后（下）的文件

趋势科技的分析显示，Anubis在启动时支持几个命令，包括特权提升、目录排除和加密的目标路径。默认情况下排除重要的系统和程序目录，以避免使系统完全不可用。勒索软件删除卷影副本，并终止可能干扰加密过程的进程和服务。

加密系统使用ECIES（椭圆曲线集成加密方案），研究人员指出实现与EvilByte和Prince勒索软件相似。加密的文件被附加在'.anubis的扩展，HTML勒索通知被放置在受影响的目录，恶意软件还执行尝试（失败）更改桌面壁纸。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250616/1750042537191203.png "1750042172645705.png")

Anubis 的勒索信

网络安全公司观察到，Anubis攻击始于带有恶意链接或附件的网络钓鱼电子邮件。

文章翻译自：https://www.bleepingcomputer.com/news/security/anubis-ransomware-adds-wiper-to-destroy-files-beyond-recovery/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?fyDUhf2G)

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