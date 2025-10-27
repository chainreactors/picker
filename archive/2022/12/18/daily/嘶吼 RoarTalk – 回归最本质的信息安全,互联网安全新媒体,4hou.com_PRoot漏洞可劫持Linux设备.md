---
title: PRoot漏洞可劫持Linux设备
url: https://www.4hou.com/posts/l6w1
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-12-18
fetch_date: 2025-10-04T01:51:04.975026
---

# PRoot漏洞可劫持Linux设备

PRoot漏洞可劫持Linux设备 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# PRoot漏洞可劫持Linux设备

ang010ela
[新闻](https://www.4hou.com/category/news)
2022-12-17 11:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)130808

收藏

导语：攻击者利用 PRoot隔离文件系统漏洞可劫持Linux设备。

攻击者利用 PRoot隔离文件系统漏洞可劫持Linux设备。

BYOF (Bring Your Own Filesystem)攻击是指攻击者在其自有的设备上创建一个恶意文件系统，而该设备上含有用于发起攻击活动的标准工具集。然后将该文件系统下载和挂载到被入侵的机器上，为下一步入侵Linux系统提供一个预配置的工具集。

PRoot是一款Linux 开源工具，融合了'chroot'、'mount --bind'、'binfmt\_misc'命令，允许用户在Linux系统中搭建一个隔离的root文件系统。近日，Sysdig研究人员发现有黑客滥用Linux PRoot工具来发起BYOF攻击活动，影响多个Linux发行版。

默认情况下，PRoot进程活动范围局限在隔离的guest文件系统中。但QEMU模拟可以用来混合host主机和guest程序的执行。此外，guest文件系统中的程序也可以使用内置的mount/bind机制来访问host系统的文件和目录。

Sysdig研究人员发现攻击者利用PRoot在受害者系统中部署恶意文件系统，包括网络扫描工具"masscan"、"nmap"，以及XMRig加密货币挖矿机以及对应的配置文件。

文件系统中包含了用于攻击的所有内容，类似于一个包含了必要依赖的GZIP压缩文件，从DropBox这样的可信云托管服务直接释放。由于包含了所有的依赖，因此无需执行额外的配置命令。

![The malicious guest filesystem](https://www.bleepstatic.com/images/news/u/1220909/Linux/filesystem.png)

图 恶意guest文件系统

由于PRoot 是静态编译的，不需要任何依赖，攻击者只需要从gitlab下载预编译的二进制文件，执行下载的文件提取出文件系统，并挂载到系统上就可以。

研究人员发现在攻击活动中，攻击者将文件系统解压到'/tmp/Proot/' 目录，然后激活XMRig 加密货币挖矿机。

![Launching XMRig on the guest filesystem to mine using host's GPU](https://www.bleepstatic.com/images/news/u/1220909/Linux/xmrig.png)

图 使用host CPU在guest文件系统上启动XMRig加密货币挖矿机

Sysdig指出，攻击者通过PRoot可以下载除XMRig 加密货币挖矿机之外的其他payload，对被入侵的系统引发更加严重的后果。

攻击者通过使用预配置的PRoot 文件系统可以实现跨操作系统配置，而无需将恶意软件修改为特定架构，也无需包含特定依赖和工具。

更多技术分析参见：https://sysdig.com/blog/proot-post-explotation-cryptomining/

本文翻译自：https://www.bleepingcomputer.com/news/security/hackers-hijack-linux-devices-using-proot-isolated-filesystems/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?T4wulJs1)

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