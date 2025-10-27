---
title: 基于泄露的 Kryptina 代码的新型 Mallox 勒索软件 Linux 变种
url: https://www.4hou.com/posts/GA8y
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-11
fetch_date: 2025-10-06T18:45:35.315798
---

# 基于泄露的 Kryptina 代码的新型 Mallox 勒索软件 Linux 变种

基于泄露的 Kryptina 代码的新型 Mallox 勒索软件 Linux 变种 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 基于泄露的 Kryptina 代码的新型 Mallox 勒索软件 Linux 变种

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-10-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)90105

收藏

导语：目前，尚不确定 Mallox Linux 1.0 变体是由单个附属机构、多个附属机构还是所有 Mallox 勒索软件运营商与 Linux 变体一起使用。

Mallox 勒索软件行动的附属机构（也称为 TargetCompany）被发现使用稍微修改过的 Kryptina 勒索软件版本攻击 Linux 系统。

SentinelLabs 表示，此版本与其他针对 Linux 的 Mallox 变体不同，例如 Trend Micro 研究人员去年 6 月描述的变体，这突显了勒索软件生态系统的策略转变。此外，这再次表明，之前只针对 Windows 的恶意软件 Mallox 正在将 Linux 和 VMWare ESXi 系统纳入其攻击范围，标志着该行动的重大演变。

**从 Kryptina 到 Mallox**

Kryptina 于 2023 年底作为针对 Linux 系统的低成本（500-800 美元）勒索软件即服务 (RaaS) 平台推出，但未能在网络犯罪社区引起关注。

2024 年 2 月，其所谓的管理员使用别名“Corlys”在黑客论坛上免费泄露了 Kryptina 的源代码，据推测这些源代码被有意获得可运行的 Linux 变体的随机勒索软件参与者获取。

![leak.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240924/1727163724471455.png "1727163598367302.png")

威胁者泄露源代码

在 Mallox 的一家附属公司遭遇操作失误并暴露其工具后，SentinelLabs 发现 Kryptina 已被该项目采用，其源代码被用于构建重新命名的 Mallox 有效载荷。

![Kryptina_Mallox_19.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240924/1727163725183671.png "1727163649190295.png")

暴露服务器上的 Kryptina 源代码

重新命名的加密器名为“Mallox Linux 1.0”，使用 Kryptina 的核心源代码、相同的 AES-256-CBC 加密机制和解密例程，以及相同的命令行构建器和配置参数。

这表明 Mallox 附属公司仅修改了外观和名称，删除了赎金记录、脚本和文件上对 Kryptina 的引用，并将现有文档转置为“精简”形式，其余部分保持不变。

![ransom-note.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240924/1727163726449406.png "1727163699191122.png")

Mallox Linux 1.0 勒索信

除了 Mallox Linux 1.0 之外，SentinelLabs 还在威胁者的服务器上发现了各种其他工具，包括：

**·**合法的卡巴斯基密码重置工具 (KLAPR.BAT)

**·**CVE-2024-21338 漏洞利用，Windows 10 和 11 上的权限提升漏洞

**·**权限提升 PowerShell 脚本

**·**基于 Java 的 Mallox 有效载荷投放器

**·**包含 Mallox 有效载荷的磁盘映像文件

**·**14 个潜在受害者的数据文件夹

目前，尚不确定 Mallox Linux 1.0 变体是由单个附属机构、多个附属机构还是所有 Mallox 勒索软件运营商与 Linux 变体一起使用。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-mallox-ransomware-linux-variant-based-on-leaked-kryptina-code/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?4ZAfSJUN)

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