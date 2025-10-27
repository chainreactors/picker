---
title: 黑客组织同时使用 10 种恶意软件攻击系统
url: https://www.4hou.com/posts/kgQE
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-04
fetch_date: 2025-10-06T17:40:53.171590
---

# 黑客组织同时使用 10 种恶意软件攻击系统

黑客组织同时使用 10 种恶意软件攻击系统 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客组织同时使用 10 种恶意软件攻击系统

山卡拉
[新闻](https://www.4hou.com/category/news)
2024-07-03 12:00:01

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)179342

收藏

导语：安全研究人员建议使用最新的反恶意软件工具，对打包文件进行分析，并提高用户警惕，对可疑的电子邮件保持谨慎。

一个规模巨大的恶意软件活动（可能由同一组织运行）正在使用名为“WEXTRACT.EXE .MUI”的人工嵌套文件进行分发。

全球范围内有超过50,000个文件采用这种方法进行分发，涉及的恶意软件包括Redline、RisePro和Amadey等窃取器和加载器。

一些样本与东欧网络犯罪分子相关的自治系统有关，OutPost24 的网络安全研究人员近日检测到一个新的黑客组织正在同时使用 10 种恶意软件攻击系统。

**同时出现 10 种恶意软件**

“WEXTRACT.EXE .MUI”恶意软件分发系统利用嵌套的CAB文件来分发大量恶意软件样本，例如窃取程序和加载程序。

该方法的执行序列复杂，会以相反的顺序释放和运行恶意软件，从而可能导致绕过安全措施。由于加载器可能会下载更多的恶意软件，因此该技术可能会导致多重感染。

从 2023 年 2 月到 2024 年初，大规模的恶意软件分发活动嵌套了多个恶意软件家族，例如 Redline、Mystic Stealer、RisePro、Amadey 和SmokeLoader。

该活动随着时间的推移而发展，融合了混淆工具和不同的分发方法。超过两千一百个实例的检查显示，一些恶意软件组合可能导致受害者同时感染多种窃取器和加载器。

这表明，此次活动的基础设施和策略背后有一个单一参与者。

![333.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719906948173565.jpg "1719906948173565.jpg")

WEXTRACT 样本的分布步骤

分发名为“Unfurling Hemlock”的恶意软件的活动很可能从其他参与者那里购买分发服务。

其最早阶段存在于电子邮件附件以及从被黑客入侵或欺诈网站下载的内容中。

该基础设施主要基于 AS 203727，使用独有 IP 和共享 IP 来分发 WEXTRACT 和其他恶意软件。这表明只有一个参与者负责该活动，但将其部分分发给其他委托人。

该恶意软件活动使用不同的 C2 URL 和 IP 地址，其中一些是 WEXTRACT 相关恶意软件所特有的，另一些则是其他活动所共有的。

基础设施的多样性支持了这样的推测：该攻击者可能受到经济利益的驱使，提供来自其他活动的样本。

虽然上传地点不一定代表实际的感染地点，但感染源遍布多个国家。

如图所示：

![44.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240702/1719907170165135.jpg "1719907170165135.jpg")

样本来源

与通常的趋势不同，这次大规模恶意软件攻击主要针对包括俄罗斯在内的西方机构。此次行动同时启动了不同类型的恶意软件，以此增加感染的可能性并提高回报。

尽管现在还不够完善，但不排除这种“集束炸弹”方法未来仍有可能被威胁分子采用。

因此，安全研究人员建议使用最新的反恶意软件工具，对打包文件进行分析，并提高用户警惕，对可疑的电子邮件保持谨慎。

本文翻译自：https://gbhackers.com/new-hacker-group-10-malware-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?mueewwhg)

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

![](https://img.4hou.com/FjC8MmzrcnfY_rzJyoXU2_G-O0i9)

# [山卡拉](https://www.4hou.com/member/azxO)

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

[查看更多](https://www.4hou.com/member/azxO)

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