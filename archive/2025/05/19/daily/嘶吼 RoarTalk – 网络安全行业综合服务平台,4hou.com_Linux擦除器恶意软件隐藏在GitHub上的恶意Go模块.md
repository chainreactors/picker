---
title: Linux擦除器恶意软件隐藏在GitHub上的恶意Go模块
url: https://www.4hou.com/posts/0M7y
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-19
fetch_date: 2025-10-06T22:23:24.324392
---

# Linux擦除器恶意软件隐藏在GitHub上的恶意Go模块

Linux擦除器恶意软件隐藏在GitHub上的恶意Go模块 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Linux擦除器恶意软件隐藏在GitHub上的恶意Go模块

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-18 13:21:59

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)81330

收藏

导语：攻击者可以利用这一点来创建看似合法的模块名称空间，并等待开发人员将恶意代码集成到他们的项目中。

安全研究人员最新发现，供应链攻击的目标是Linux服务器，其磁盘擦除恶意软件隐藏在GitHub上发布的Golang模块中。

该活动于上个月被发现，并依赖于三个恶意Go模块，其中包括“高度混淆的代码”，用于检索远程有效载荷并执行它们。

**磁盘完全销毁**

这种攻击似乎是专门为基于linux的服务器和开发人员环境设计的，因为破坏性的有效载荷——一个名为done.sh的Bash脚本，会为文件清除活动运行一个‘ dd ’命令。

此外，有效负载验证它在Linux环境（运行时）中运行。GOOS == "linux")，然后再尝试执行。

供应链安全公司Socket的一项分析表明，该命令用零覆盖数据的每个字节，导致不可逆转的数据丢失和系统故障。

目标是主存储卷/dev/sda，其中包含关键系统数据、用户文件、数据库和配置。

“通过用零填充整个磁盘，脚本完全破坏了文件系统结构、操作系统和所有用户数据，使系统无法启动和不可恢复”——Socket

研究人员在4月份发现了这次攻击，并在GitHub上发现了三个Go模块，这些模块已经从平台上删除：

**·**github[.]com/truthfulpharm/prototransform

**·**github[.]com/blankloggia/go-mcp

**·**github[.]com/steelpoor/tlsproxy

所有三个模块都包含混淆的代码，这些代码解码成使用‘ wget ’下载恶意数据清除脚本（/bin/bash或/bin/sh）的命令。

根据Socket研究人员的说法，有效负载在下载后立即执行，“几乎没有时间进行响应或恢复。”

恶意Go模块似乎模拟了将消息数据转换为各种格式的合法项目（Prototransform），模型上下文协议（Go -mcp）的Go实现，以及为TCP和HTTP服务器提供加密的TLS代理工具（tlsproxy）。即使最小限度地暴露在分析的破坏性模块中，也会产生重大影响，例如完全丢失数据。

由于Go生态系统的分散性，缺乏适当的检查，来自不同开发人员的包可能具有相同或相似的名称。

攻击者可以利用这一点来创建看似合法的模块名称空间，并等待开发人员将恶意代码集成到他们的项目中。

文章翻译自：https://www.bleepingcomputer.com/news/security/linux-wiper-malware-hidden-in-malicious-go-modules-on-github/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?sN7hZDCZ)

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