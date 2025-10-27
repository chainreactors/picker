---
title: 黑客在有针对性的攻击中部署人工智能编写的恶意软件
url: https://www.4hou.com/posts/YZM0
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-09-30
fetch_date: 2025-10-06T18:20:09.930414
---

# 黑客在有针对性的攻击中部署人工智能编写的恶意软件

黑客在有针对性的攻击中部署人工智能编写的恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客在有针对性的攻击中部署人工智能编写的恶意软件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-09-29 16:21:24

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)114463

收藏

导语：即使他们没有使用人工智能来构建功能齐全的恶意软件，黑客在创建更高级的威胁时也会依靠这项技术来加快他们的工作速度。

在一起针对用户的电子邮件活动中，研究人员发现了恶意代码，分析后发现是在生成人工智能服务的帮助下创建的，用于传播 AsyncRAT 恶意软件。

尽管供应商实施了保护措施和限制，但人工智能工具依然可能被滥用来创建恶意软件。安全研究人员在真实的攻击中发现了人工智能创建的恶意软件的可疑案例。

今年早些时候，网络安全公司 Proofpoint 发现了一个恶意 PowerShell 脚本，该脚本可能是使用人工智能系统创建的。

随着技术含量较低的恶意分子越来越依赖人工智能来开发恶意软件，惠普安全研究人员在 6 月初就发现了一次恶意活动，该活动使用的代码评论方式与生成式人工智能系统创建的方式相同。

该活动利用 HTML 走私来提供受密码保护的 ZIP 存档，研究人员通过暴力破解来解锁该存档。

HP Wolf Security 报告称，技术技能较低的网络犯罪分子越来越多地使用生成式 AI 来开发恶意软件，2024 年第二季度的“威胁洞察”报告中提供了一个例子。

6 月初，惠普发现了一项针对法国用户的网络钓鱼活动，采用 HTML 走私提供包含 VBScript 和 JavaScript 代码的受密码保护的 ZIP 存档。

![javascript.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240929/1727594379186986.png "1727423205173858.png")

JavaScript 中的 AES 加密实现

在暴力破解密码后，研究人员分析了代码，发现“攻击者对整个代码进行了巧妙的注释”，这在人类开发的代码中很少发生，因为威胁分子通常希望隐藏恶意软件的工作原理。

据HP Wolf Security 的报告显示：“这些注释准确地描述了代码的作用，就像生成式人工智能服务可以创建带有解释的示例代码一样” 。

VBScript 在受感染的计算机上建立了持久性，创建计划任务并在 Windows 注册表中写入新密钥。研究人员指出，指向人工智能生成的恶意代码的一些指标包括脚本的结构、解释每行的注释、选择函数名称和变量的本地语言。

![comments.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240929/1727594381800368.png "1727423300102284.png")

VBScript 代码中的注释

在后期阶段，攻击会下载并执行 AsyncRAT，这是一种开源且免费提供的恶意软件，可以记录受害者计算机上的击键并提供加密连接以进行远程监视和控制。该恶意软件还可以提供额外的有效负载。

![diagram.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240929/1727594382140007.png "1727423344119029.png")

完整的感染链

HP Wolf Security 报告还强调，根据其可见性，归档是今年上半年最流行的交付方式。生成式人工智能可以帮助较低级别的威胁参与者在几分钟内编写恶意软件，并针对针对不同区域和平台（Linux、macOS）的攻击进行定制。

即使他们没有使用人工智能来构建功能齐全的恶意软件，黑客在创建更高级的威胁时也会依靠这项技术来加快他们的工作速度。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-deploy-ai-written-malware-in-targeted-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YplvO1ZE)

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