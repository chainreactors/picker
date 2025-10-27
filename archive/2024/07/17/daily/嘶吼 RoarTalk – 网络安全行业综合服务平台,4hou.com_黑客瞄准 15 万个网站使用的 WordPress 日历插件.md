---
title: 黑客瞄准 15 万个网站使用的 WordPress 日历插件
url: https://www.4hou.com/posts/jBRl
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-07-17
fetch_date: 2025-10-06T17:41:00.957219
---

# 黑客瞄准 15 万个网站使用的 WordPress 日历插件

黑客瞄准 15 万个网站使用的 WordPress 日历插件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客瞄准 15 万个网站使用的 WordPress 日历插件

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-07-16 12:01:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)103265

收藏

导语：Wordfence 报告称，黑客已试图利用该问题进行攻击，并在 24 小时内阻止了 100 多次攻击尝试。

研究发现，黑客正试图利用现代事件日历 WordPress 插件中的漏洞（该漏洞存在于超过 150,000 个网站上），将任意文件上传到易受攻击的站点并远程执行代码。

该插件由 Webnus 开发，用于组织和管理现场、虚拟或混合活动。

攻击中利用的漏洞被标识为 CVE-2024-5441，并获得了高严重性评分（CVSS v3.1：8.8）。该漏洞由 Friderika Baranyai 于 5 月 20 日在 Wordfence 的 Bug Bounty Extravaganza 期间发现并报告。

在一份描述安全问题的报告中，Wordfence 表示，安全问题源于插件的“set\_featured\_image”函数缺乏文件类型验证，该函数用于上传和设置事件的特色图片。

该函数获取图像 URL 和帖子 ID，尝试获取附件 ID，如果未找到，则使用 get\_web\_page 函数下载图像。

它使用 wp\_remote\_get 或 file\_get\_contents 检索图像，并使用 file\_put\_contents 函数将其保存到 WordPress 上传目录。

现代事件日历版本（直至 7.11.0）不检查上传的图像文件中扩展名的文件类型，允许上传任何文件类型，包括有风险的 .PHP 文件。

一旦上传，这些文件就可以被访问和执行，从而可以在服务器上执行远程代码，并可能导致完全的网站接管。

任何经过身份验证的用户（包括订阅者和任何注册会员）均可利用 CVE-2024-5441。如果插件设置为允许非会员（没有帐户的访问者）提交事件，则无需身份验证即可利用 CVE-2024-5441。

Webnus 近日发布了现代事件日历 7.12.0 版本修复了该漏洞，可有效避免网络攻击风险的推荐升级。

然而，Wordfence 报告称，黑客已试图利用该问题进行攻击，并在 24 小时内阻止了 100 多次攻击尝试。

鉴于正在进行的攻击活动，现代事件日历和现代事件日历精简版（免费版）的用户应尽快升级到最新版本或禁用该插件，直到他们可以执行更新。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-target-wordpress-calendar-plugin-used-by-150-000-sites/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?AaeU9ncq)

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