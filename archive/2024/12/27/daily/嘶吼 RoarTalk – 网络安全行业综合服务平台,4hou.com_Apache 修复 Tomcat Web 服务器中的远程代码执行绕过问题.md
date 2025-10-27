---
title: Apache 修复 Tomcat Web 服务器中的远程代码执行绕过问题
url: https://www.4hou.com/posts/1M7G
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-12-27
fetch_date: 2025-10-06T19:33:15.771791
---

# Apache 修复 Tomcat Web 服务器中的远程代码执行绕过问题

Apache 修复 Tomcat Web 服务器中的远程代码执行绕过问题 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Apache 修复 Tomcat Web 服务器中的远程代码执行绕过问题

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-12-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)110718

收藏

导语：新版本中修复的漏洞被追踪为 CVE-2024-56337。

Apache 发布了一个安全更新，解决了 Tomcat Web 服务器中的一个重要漏洞，该漏洞可能导致攻击者实现远程代码执行。

Apache Tomcat 是一种开源 Web 服务器和 Servlet 容器，广泛用于部署和运行基于 Java 的 Web 应用程序。它为 Java Servlet、JavaServer Pages (JSP) 和 Java WebSocket 技术提供运行时环境。

该产品深受运行自定义 Web 应用程序的大型企业和依赖 Java 提供后端服务的 SaaS 提供商的欢迎。云和托管服务集成了 Tomcat 来进行应用程序托管，软件开发人员使用它来构建、测试和部署 Web 应用程序。

新版本中修复的漏洞被追踪为 CVE-2024-56337，并解决了 CVE-2024-50379 的不完整缓解措施，这是一个关键的远程代码执行 (RCE)，供应商已于 12 月 17 日发布了补丁。

人们意识到应用 CVE-2024-50379 的更新不足以保护系统，并决定发布 CVE-2024-56337强调手动操作的必要性。

这两个问题本质上是完全相同的漏洞，但决定使用新的 CVE ID 是为了提高受影响系统管理员的认识。该安全问题是一个检查时间使用时间 (TOCTOU) 竞争条件漏洞，该漏洞会影响启用默认 Servlet 写入（“只读”初始化参数设置为 false）并在不区分大小写的文件系统上运行的系统。

该问题影响 Apache Tomcat 11.0.0-M1 至 11.0.1、10.1.0-M1 至 10.1.33 以及 9.0.0.M1 至 9.0.97。用户应升级到最新的 Tomcat 版本：11.0.2、10.1.34 和 9.0.98。

解决该问题需要采取额外的步骤，根据所使用的 Java 版本，除了升级之外，用户还需要执行以下操作：

**·**对于 Java 8 或 11，建议将系统属性“sun.io.useCanonCaches”设置为“false”（默认值：true）。

**·**对于 Java 17，请确保“sun.io.useCanonCaches”（如果设置）配置为 false（默认值：false）。

**·**对于 Java 21 及更高版本，无需配置。该属性和有问题的缓存已被删除。

Apache 团队分享了即将推出的 Tomcat 版本（11.0.3、10.1.35 和 9.0.99）中的安全增强计划。

具体来说，Tomcat 将在不区分大小写的文件系统上启用默认 servlet 的写访问权限之前检查“sun.io.useCanonCaches”设置是否正确，并在可能的情况下将“sun.io.useCanonCaches”默认为 false。这些更改旨在自动实施更安全的配置，并降低 CVE-2024-50379 和 CVE-2024-56337 被利用的风险。

文章翻译自：https://www.bleepingcomputer.com/news/security/apache-fixes-remote-code-execution-bypass-in-tomcat-web-server/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vv3COUwA)

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