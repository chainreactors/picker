---
title: NPM索引上有数十个恶意软件包正在收集主机和网络数据
url: https://www.4hou.com/posts/8gDg
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-29
fetch_date: 2025-10-06T22:26:15.181893
---

# NPM索引上有数十个恶意软件包正在收集主机和网络数据

NPM索引上有数十个恶意软件包正在收集主机和网络数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# NPM索引上有数十个恶意软件包正在收集主机和网络数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-05-28 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)69944

收藏

导语：恶意分子在发布这些恶意软件时还列出了几个合法的软件包，以建立信任并逃避检测。

最新发现，安全研究人员在NPM索引中发现了60个试图收集敏感主机和网络数据并将其发送到由威胁者控制的Discord webhook的软件包。

根据Socket威胁研究团队的说法，这些软件包从5月12日开始从三个发布者账户上传到NPM存储库。

每个恶意包都包含一个安装后脚本，在‘ npm install ’期间自动执行，并收集以下信息：

**·**主机名

**·**内部IP地址

**·**用户主目录

**·**当前工作目录

**·**用户名

**·**系统DNS服务器

该脚本检查与云提供商相关的主机名，反向DNS字符串，试图确定它是否在分析环境中运行。

Socket没有观察到第二阶段有效负载的交付、特权升级或任何持久机制。然而，鉴于所收集的数据类型，针对性网络攻击的危险是显著的。

**NPM 上仍有可用的软件包**

研究人员报告了这些恶意软件包，根据调查，它们在NPM上仍然可用，并且显示累计下载计数为3000。但不久后，存储库中没有一个是存在的。

为了诱骗开发人员使用它们，恶意分子使用了与索引中合法包相似的名称，如“flipper-plugins”、“react-xterm2”和“hermes-inspector- msgen”，这些通用的信任唤起名称，以及其他暗示测试的名称，可能针对CI/CD管道。

如果用户已经安装了它们中的任何一个，建议立即删除它们并执行完整的系统扫描以消除任何感染残余。

**NPM上的数据擦除工具**

Socket本周在NPM上发现的另一个恶意活动涉及8个恶意软件包，它们通过输入错误模仿合法工具，但可以删除文件、破坏数据和关闭系统。

这些包主要针对React、Vue.js、Vite、Node.js和Quill生态系统，在过去两年里一直存在于NPM上，获得了6200次下载。

避免这种情况在很大程度上是由于载荷是根据硬编码的系统日期激活的，并且它们被设计成逐步破坏框架文件、损坏核心JavaScript方法和破坏浏览器存储机制。

![code(1).webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250526/1748243819983763.png "1748243288365271.png")

脚本用于2023年6月19日至30日删除vue .js相关文件

恶意分子在发布这些恶意软件时还列出了几个合法的软件包，以建立信任并逃避检测。尽管根据硬编码的日期，虽然危险已经过去了，但删除这些软件包同样至关重要，因为它们的作者可能会引入更新，这些更新将在未来重新触发它们的擦除功能。

文章翻译自：https://www.bleepingcomputer.com/news/security/dozens-of-malicious-packages-on-npm-collect-host-and-network-data/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?yrYdZBt3)

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