---
title: 研究人员从西门子PLC中提取主加密密钥
url: https://www.4hou.com/posts/zlz7
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-16
fetch_date: 2025-10-03T20:01:53.967317
---

# 研究人员从西门子PLC中提取主加密密钥

研究人员从西门子PLC中提取主加密密钥 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 研究人员从西门子PLC中提取主加密密钥

布加迪
[新闻](https://www.4hou.com/category/news)
2022-10-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)171620

收藏

导语：全局加密密钥被硬编码在一些可编程逻辑控制器产品系列上。西门子建议客户升级所有受影响的设备。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221014/1665718316119530.png "1665627793131926.png")

安全研究人员近日发现了一种方法，可以成功提取被硬编码在多款西门子可编程逻辑控制器（PLC）产品系列的CPU中的全局加密密钥，从而使他们能够破坏其安全通信和身份验证。西门子建议所有客户升级受影响设备的固件以及工程师用来与客户通信、部署程序的TIA Portal软件。

据Claroty公司的安全研究人员声称，大约十年前西门子为其SIMATIC S7-1200/1500 PLC CPU引入了非对称加密技术，以保护其配置、程序和通信。然而，该公司选择为这些产品系列中的所有设备使用硬编码的全局私钥来实现保护，因为当时动态密钥分发和管理不是一种常见的做法，而且对客户而言是潜在的负担。

研究人员在报告中说：“然而自那时起，技术和安全研究方面的进步，加上迅速变化的威胁形势，已经使这种硬编码的加密密钥成为一种不可接受的风险。如果恶意攻击者能够提取全局硬编码密钥，可能会给整个设备产品系列的安全造成不可挽回的破坏。”

**西门子PLC使用加密密钥用于身份验证和代码保护**

据Claroty声称，西门子S7-1200和S7-1500 PLC使用多数密钥。同一产品系统的所有设备都有一个共同的“针对每个系列”的密钥，“针对每个型号/固件”的密钥用于加密配置和维护代码完整性，连接密钥则用于身份验证过程以及加密与客户之间的通信。该连接密钥来自配置密钥，用于基于椭圆曲线的加密。

这意味着如果攻击者获得配置密钥，有可能从PLC的配置中解密用户密码，并发动中间人攻击，即使他们无权读取加密的配置。

问题是，这个面向整个系列的配置密钥并不存储在设备固件（设备上运行的操作系统）中，而是存储在CPU本身中，因此读取它需要通过操作码直接与CPU交互。只需在一台设备上执行一次，因为它们都有共同的密钥。

**研究人员获得了直接访问内存的权限以提取密钥**

去年，Claroty的研究人员发现了一个影响S7 PLC的远程代码执行漏洞（CVE-2020-15782），从而可以在设备上执行本机代码。工程师通过专门的工程软件编写并部署到PLC的程序或逻辑通常在PLC操作系统的沙箱内运行。CVE-2020-15782让研究人员得以绕过这个安全层，对PLC上任何通常受保护的内存地址直接执行读写操作。

研究人员表示，他们使用获得的DA[内存直接访问] 读取权限，成功提取了整个加密的PLC固件（SIMATIC S7-1500），并映射其功能函数。他们在映射过程中发现了一个读取PLC上私钥的函数。一旦他们获得了函数地址，就用他们的shell代码重写了特定的MC7+操作码的功能，迫使它们调用读取私钥的本机函数。然后他们将密钥复制到一个已知的内存地址，并从那里读取它。执行被覆盖的函数为他们提供了PLC的完整私钥。

**密钥导致多种攻击**

与西门子PLC交互需要一个密码，但授予客户端设备的权限由可配置的四个保护级别定义。如果保护级别低于三级，攻击者可以在没有任何特殊权限的情况下从PLC中提取配置。该配置含有密码哈希，但经过加密。然而，如果攻击者拥有全局私钥，就可以解密密码哈希，并使用它针对PLC完成身份验证。

如果保护级别高于四级，攻击者可以使用私钥对合法客户发动中间人攻击。之所以会得逞，是由于攻击者会模仿虚假的PLC，迫使客户试图验证身份以连接到PLC。这将导致客户向虚假的PLC发送经过加密的连接密钥，然后会用攻击者拥有的已提取的全局密钥来解密，并用于连接到实际的PLC。实际的PLC会响应、发出密码质询，攻击者可以将密码质询转发回客户、获得客户的响应。

将质询响应转发给实际的PLC将允许攻击者建立经过身份验证的会话，拥有读取配置（含有密码哈希）的权限。然后可以使用全局私钥对密码哈希进行解密，从而使攻击者将来无需重复中间人会话劫持就可以访问。

研究人员警告，最后，如果攻击者拥有被动访问权，以捕获网络上某个PLC的流量，就可以拦截来自该PLC的配置读/写信息。使用私钥，攻击者可以解密配置，并提取密码哈希。有了密码哈希，攻击者就可以针对控制器完成身份验证，并编写新配置。

**建议用户升级易受攻击的设备和工程软件**

西门子在针对这个问题的新公告中表示，SIMATIC S7-1200、S7-1500 CPU和相关产品以一种不再足够到位的方式保护内置的全局私钥。西门子建议用户将受影响的产品以及相应的TIA Portal项目更新到最新版本。TIA Portal V17和相关的CPU固件版本引入了基于每个设备的独特密码保护机密配置以及保护受TLS保护的PG/PC和HMI通信这种功能。

易受攻击的设备包括：版本低于2.9.2的SIMATIC Drive Controller系列、版本低于21.9的SIMATIC ET 200SP Open Controller CPU 1515SP PC2（包括SIPLUS变体）、版本低于4.5.0的SIMATIC S7-1200 CPU系列（包括SIPLUS变体）、版本低于2.9.2的SIMATIC S7-1500 CPU系列（包括相关的ET200 CPU和SIPLUS变体）、版本低于 21.9的SIMATIC S7-1500软件控制器以及版本低于4.0的SIMATIC S7-PLCSIM Advanced。所有版本的SIMATIC ET 200SP Open Controller CPU 1515SP PC（包括SIPLUS变体）也受到影响，但不是目前没有修复版，就是没有计划修复。

本文翻译自：https://www.csoonline.com/article/3676076/researchers-extract-master-encryption-key-from-siemens-plcs.html如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?GftyMXvy)

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

![](https://img.4hou.com/portraits/10321ac81c30432685d31a710b4220de.jpg)

# [布加迪](https://www.4hou.com/member/VGrO)

IT英汉译匠，字典迷（尤爱英汉字典），酷爱羽毛球

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/VGrO)

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