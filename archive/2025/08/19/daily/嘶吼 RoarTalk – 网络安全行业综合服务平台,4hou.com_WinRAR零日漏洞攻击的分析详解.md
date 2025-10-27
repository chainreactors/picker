---
title: WinRAR零日漏洞攻击的分析详解
url: https://www.4hou.com/posts/kg4X
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-19
fetch_date: 2025-10-07T00:15:20.141775
---

# WinRAR零日漏洞攻击的分析详解

WinRAR零日漏洞攻击的分析详解 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# WinRAR零日漏洞攻击的分析详解

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-08-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)54166

收藏

导语：该漏洞与一个月前披露的另一个WinRAR路径遍历漏洞（追踪编号CVE-2025-6218）相似。

研究人员发布了一份报告，详细阐述了俄罗斯RomCom黑客组织如何利用近期被追踪为CVE-2025-8088的WinRAR路径遍历漏洞，在零日攻击中投放不同的恶意软件有效载荷。

RomCom（又称Storm-0978和Tropical Scorpius）是一个俄罗斯网络间谍威胁组织，擅长利用零日漏洞进行网络攻击，涉及Firefox（CVE-2024-9680、CVE-2024-49039）和微软Office（CVE-2023-36884）等软件。

2025年7月18日，ESET发现RomCom正在利用WinRAR中一个未公开的路径遍历零日漏洞，并通知了这款热门压缩工具的开发团队。

ESET本周发布的新报告解释道：“通过对漏洞利用程序的分析，我们发现了这一漏洞并定为CVE-2025-8088的编号，这是一个借助备用数据流实现的路径遍历漏洞。WinRAR已于2025年7月30日发布了修复版本。”

2025年7月30日，WinRAR发布了针对该漏洞（编号CVE-2025-8088）的修复程序，版本为7.13。不过，随附的公告中并未提及该漏洞存在被主动利用的情况。据悉，当用户打开特制的压缩包时，该漏洞会被用于将危险的可执行文件提取到自动运行路径。

该漏洞与一个月前披露的另一个WinRAR路径遍历漏洞（追踪编号CVE-2025-6218）相似。

ESET的报告称，恶意的RAR压缩包包含多个隐藏的ADS（备用数据流）有效载荷，这些载荷用于隐藏恶意的DLL文件和Windows快捷方式，当目标用户打开压缩包时，这些文件会被提取到攻击者指定的文件夹中。

许多ADS条目指向无效路径，ESET认为，这些条目是被故意添加的，目的是生成看似无害的WinRAR警告，同时隐藏文件列表深处存在的恶意DLL、EXE和LNK文件路径。

![图片19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250812/1754987086179598.png "1754985957921578.png")

恶意RAR存档（顶部）和解压过程中的错误（底部）

可执行文件被放置在%TEMP%或%LOCALAPPDATA%目录中，而Windows快捷方式（LNK文件）则被放入Windows启动目录，以便在用户后续登录时执行。

ESET记录了三条不同的攻击链，均会投放RomCom组织已知的恶意软件家族：

**·**Mythic Agent：Updater.lnk会将msedge.dll添加到一个COM劫持注册表位置，该文件会解密AES shellcode，且仅当系统域与硬编码的值匹配时才会运行。该shellcode会启动Mythic代理，从而实现命令与控制通信、命令执行以及有效载荷投放。

**·**SnipBot：Display Settings.lnk会运行ApbxHelper.exe，这是一个经过修改的PuTTY CAC，带有无效证书。它会先检查是否有不少于69个最近打开的文档，之后再解密shellcode，从攻击者的服务器下载额外的有效载荷。

**·**MeltingClaw：Settings.lnk会启动Complaint.exe（即RustyClaw），该程序会下载一个MeltingClaw DLL，进而从攻击者的基础设施获取并执行更多恶意模块。

![图片20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250812/1754987087433345.png "1754986020131914.png")

Mythic Agent感染链

俄罗斯网络安全公司Bi.Zone也报告称，他们观察到一个单独的活动群，被其追踪为“Paper Werewolf”，该集群在攻击中同样利用了CVE-2025-8088和CVE-2025-6218这两个漏洞。

目前，ESET已在其GitHub仓库中分享了RomCom组织最新攻击的完整入侵指标。

尽管微软在2023年为Windows系统添加了原生的RAR支持功能，但该功能仅在较新的版本中可用，且其功能远不如WinRAR全面。因此，许多高级用户和组织仍依赖WinRAR来管理压缩文件，这使其成为黑客的主要攻击目标。

RarLab表示，他们并不了解CVE-2025-8088漏洞被利用的具体细节，也没有收到任何用户报告，ESET仅向他们分享了开发补丁所需的技术信息。WinRAR没有自动更新功能，因此用户需要从官网手动下载并安装最新版本。

文章翻译自：https://www.bleepingcomputer.com/news/security/details-emerge-on-winrar-zero-day-attacks-that-infected-pcs-with-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?L50aRqZ3)

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