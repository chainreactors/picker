---
title: APT36黑客利用Linux .desktop文件在攻击中安装恶意软件
url: https://www.4hou.com/posts/6M19
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-27
fetch_date: 2025-10-07T00:18:03.340991
---

# APT36黑客利用Linux .desktop文件在攻击中安装恶意软件

APT36黑客利用Linux .desktop文件在攻击中安装恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# APT36黑客利用Linux .desktop文件在攻击中安装恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)51094

收藏

导语：最新攻击行动表明APT36的战术正在不断演变，变得更具规避性和复杂性。

APT36网络间谍组织正利用Linux系统的.desktop文件加载恶意软件，对印度政府及国防实体发动新一轮攻击。

该活动已被CYFIRMA与CloudSEK两家机构在报告中记录在案，其目的是实现数据窃取与持续性的间谍访问。此前，APT36就曾在南亚的定向间谍行动中借助.desktop文件加载恶意软件。

这些攻击最早于2025年8月1日被发现，根据最新证据显示，攻击目前仍在持续。

**.desktop文件的滥用情况**

尽管两份报告所描述的攻击所使用的基础设施与样本（基于哈希值）各不相同，但所采用的技术、战术和流程（TTPs）、攻击链以及明显的攻击目标却是一致的。

受害者会通过钓鱼邮件收到ZIP压缩包，其中包含一个伪装成PDF文档的恶意.desktop文件，且文件名也与PDF文档相应匹配。

Linux系统的.desktop文件是基于文本的应用程序启动器，其中包含配置选项，用于规定桌面环境应如何显示和运行应用程序。

用户会误将.desktop文件当作PDF打开，这会触发隐藏在“Exec=”字段中的bash命令——该命令会在“/tmp/”目录下创建一个临时文件名，并将从攻击者服务器或谷歌云端硬盘获取的十六进制编码载荷写入其中。

之后，它会执行“chmod +x”命令使其具备可执行权限，再在后台启动该文件。

为降低受害者的怀疑，该脚本还会启动Firefox浏览器，显示一个托管在谷歌云端硬盘上的良性诱饵PDF文件。

![decoy.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250825/1756105348681828.jpg "1756105237999286.jpg")

攻击中使用的诱饵PDF样本

除了通过操控“Exec=”字段来运行一系列shell命令外，攻击者还添加了“Terminal=false”等字段（用于向用户隐藏终端窗口）以及“X-GNOME-Autostart-enabled=true”字段（用于在每次登录时运行该文件）。

![desktop.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250825/1756105349815055.jpg "1756105297208876.jpg")

恶意桌面文件

通常情况下，Linux系统中的.desktop文件是纯文本快捷方式文件，用于定义图标、名称以及用户点击时要执行的命令。但在APT36的攻击中，攻击者滥用了这种启动机制，本质上将其转变为恶意软件投放器和持久化建立系统，这与Windows系统中“LNK”快捷方式被滥用的方式类似。

由于Linux系统的.desktop文件通常是文本文件而非二进制文件，且对其滥用的情况并未得到广泛记录，因此该平台上的安全工具不太可能将其视为潜在威胁进行监控。

在此次攻击中，畸形.desktop文件所投放的载荷是一款基于Go语言的ELF可执行文件，具备间谍功能。尽管加壳和混淆技术给分析工作带来了难度，但研究人员发现，该文件可被设置为隐藏状态，或者尝试通过cron任务和systemd服务建立自身的独立持久化机制。

它通过双向WebSocket通道与命令控制（C2）服务器进行通信，从而实现数据窃取和远程命令执行。

![attack-overview.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250825/1756105350275409.jpg "1756105339195104.jpg")

攻击概述

网络安全研究员认为，此次最新攻击行动表明APT36的战术正在不断演变，变得更具规避性和复杂性。

文章翻译自：https://www.bleepingcomputer.com/news/security/apt36-hackers-abuse-linux-desktop-files-to-install-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uRm1TmR0)

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