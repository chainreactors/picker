---
title: 勒索软件团伙滥用 Microsoft Azure 工具窃取数据
url: https://www.4hou.com/posts/OG8g
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-25
fetch_date: 2025-10-06T18:23:40.693785
---

# 勒索软件团伙滥用 Microsoft Azure 工具窃取数据

勒索软件团伙滥用 Microsoft Azure 工具窃取数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 勒索软件团伙滥用 Microsoft Azure 工具窃取数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-24 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)108588

收藏

导语：研究人员发现，威胁分子在使用存储资源管理器和 AzCopy 时启用了默认的“信息”级别日志记录。

BianLian 和 Rhysida 等勒索软件团伙越来越多地使用 Microsoft 的 Azure 存储资源管理器和 AzCopy 从受感染的网络窃取数据并将其存储在 Azure Blob 存储中。

Storage Explorer 是 Microsoft Azure 的 GUI 管理工具，而 AzCopy 是一个命令行工具，可以促进与 Azure 存储之间的大规模数据传输。在网络安全公司 modePUSH 观察到的攻击中，被盗数据随后被存储在云中的 Azure Blob 容器中，威胁分子随后可以将其传输到他们自己的存储中。

![storage.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240918/1726638151103323.png "1726638003155524.png")

Azure 存储资源管理器界面

然而，研究人员指出，攻击者必须进行额外操作才能使 Azure 存储资源管理器正常工作，包括安装依赖项和将 .NET 升级到版本 8。此举也表明勒索软件操作越来越关注数据盗窃，这是威胁分子在随后的勒索阶段的主要手段。

**为什么选择 Azure**

虽然每个勒索软件团伙都有自己的一套泄露工具，但勒索软件团伙通常使用 Rclone 与各种云提供商同步文件，并使用 MEGAsync 与 MEGA 云同步。

Azure 是企业经常使用的受信任的企业级服务，不太可能被企业防火墙和安全工具阻止。因此，通过它进行的数据传输尝试更有可能顺利通过且不被发现。

此外，Azure 的可扩展性和性能使其能够处理大量非结构化数据，当攻击者试图在最短的时间内窃取大量文件时，这一点非常有益。

modePUSH 表示，它观察到勒索软件参与者使用多个 Azure 存储资源管理器实例将文件上传到 blob 容器，从而尽可能加快这一过程。

**检测勒索软件泄露**

研究人员发现，威胁分子在使用存储资源管理器和 AzCopy 时启用了默认的“信息”级别日志记录，这会在 %USERPROFILE%\.azcopy 处创建一个日志文件。

该日志文件对于事件响应人员特别有价值，因为它包含有关文件操作的信息，使调查人员能够快速确定哪些数据被盗（UPLOADSUCCESSFUL）以及可能引入了哪些其他有效载荷（DOWNLOADSUCCESSFUL）。

![success.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240918/1726638152109212.png "1726638132122268.png")

数据传输成功日志

防御措施包括监控 AzCopy 执行情况、到“.blob.core.windows.net”或 Azure IP 范围的 Azure Blob 存储端点的出站网络流量，以及对关键服务器上的文件复制或访问中的异常模式设置警报。

如果企业已经使用 Azure，建议选中“退出时注销”选项以在退出应用程序时自动注销，防止攻击者使用活动会话进行文件窃取。

文章翻译自：https://www.bleepingcomputer.com/news/security/ransomware-gangs-now-abuse-microsoft-azure-tool-for-data-theft/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?58pRx2Rs)

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