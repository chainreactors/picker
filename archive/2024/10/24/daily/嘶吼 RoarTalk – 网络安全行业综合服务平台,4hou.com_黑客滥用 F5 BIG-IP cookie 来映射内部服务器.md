---
title: 黑客滥用 F5 BIG-IP cookie 来映射内部服务器
url: https://www.4hou.com/posts/mkEA
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-24
fetch_date: 2025-10-06T18:47:09.829331
---

# 黑客滥用 F5 BIG-IP cookie 来映射内部服务器

黑客滥用 F5 BIG-IP cookie 来映射内部服务器 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客滥用 F5 BIG-IP cookie 来映射内部服务器

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-10-23 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)89434

收藏

导语：据了解，F5 还开发了一种名为“BIG-IP iHealth”的诊断工具，旨在检测产品上的错误配置并向管理员发出警告。

CISA 表示，已发现威胁分子滥用未加密的持久性 F5 BIG-IP cookie 来识别和瞄准目标网络上的其他内部设备。

通过绘制内部设备图，威胁者可以潜在地识别网络上易受攻击的设备，作为网络攻击规划阶段的一部分。

据 CISA 表述，“恶意分子可以利用从未加密的持久性 cookie 收集的信息来推断或识别其他网络资源，并可能利用网络上其他设备中发现的漏洞。”

**F5 持久会话 cookie**

F5 BIG-IP 是一套应用程序交付和流量管理工具，用于负载平衡 Web 应用程序并提供安全性。其核心模块之一是本地流量管理器（LTM）模块，它提供流量管理和负载平衡，以在多个服务器之间分配网络流量。使用此功能，客户可以优化其负载平衡的服务器资源和高可用性。

产品中的本地流量管理器 (LTM) 模块使用持久性 cookie，通过每次将来自客户端（Web 浏览器）的流量引导到同一后端服务器来帮助维护会话一致性，这对于负载平衡至关重要。

“Cookie 持久性使用 HTTP cookie 强制执行持久性”F5 的文档解释道。

与所有持久模式一样，HTTP cookie 确保来自同一客户端的请求在 BIG-IP 系统最初对它们进行负载平衡后被定向到同一池成员。如果同一池成员不可用，系统会进行新的负载权衡决定。

这些 cookie 默认情况下未加密，可能是为了保持旧配置的操作完整性或出于性能考虑。从版本 11.5.0 及更高版本开始，管理员获得了一个新的“必需”选项来对所有 cookie 强制加密。

那些选择不启用它的人会面临安全风险。但是，这些 cookie 包含内部负载平衡服务器的编码 IP 地址、端口号和负载平衡设置。

多年来，网络安全研究人员一直在分享如何滥用未加密的 cookie 来查找以前隐藏的内部服务器或可能未知的暴露服务器，这些服务器可以扫描漏洞并用于破坏内部网络。还发布了一个 Chrome 扩展程序来解码这些 cookie，以帮助 BIG-IP 管理员排除连接故障。

据 CISA 称，威胁者已经在利用宽松的配置进行网络发现，并建议 F5 BIG-IP 管理员查看供应商有关如何加密这些持久 cookie 的说明。

请注意，“首选”配置选项会生成加密的 cookie，但也允许系统接受未加密的 cookie。可以在迁移阶段使用此设置，以允许先前发出的 cookie 在强制执行加密 cookie 之前继续工作。

当设置为“必需”时，所有持久 cookie 均使用强 AES-192 加密进行加密。据了解，F5 还开发了一种名为“BIG-IP iHealth”的诊断工具，旨在检测产品上的错误配置并向管理员发出警告。

文章翻译自：https://www.bleepingcomputer.com/news/security/cisa-hackers-abuse-f5-big-ip-cookies-to-map-internal-servers/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vfj8bQVR)

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