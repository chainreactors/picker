---
title: 黑客利用 cookie 插件漏洞攻击 150 万个 WordPress 网站
url: https://www.4hou.com/posts/2q7j
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-06-01
fetch_date: 2025-10-04T11:44:59.629725
---

# 黑客利用 cookie 插件漏洞攻击 150 万个 WordPress 网站

黑客利用 cookie 插件漏洞攻击 150 万个 WordPress 网站 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用 cookie 插件漏洞攻击 150 万个 WordPress 网站

walker
[新闻](https://www.4hou.com/category/news)
2023-05-31 11:18:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)126816

收藏

导语：持续的攻击针对名为 Beautiful Cookie Consent Banner 的 WordPress cookie 同意插件中的未经身份验证的存储跨站点脚本 (XSS) 漏洞，该插件具有超过 40,000 个活动安装。

持续的攻击针对名为 Beautiful Cookie Consent Banner 的 WordPress cookie 同意插件中的未经身份验证的存储跨站点脚本 (XSS) 漏洞，该插件具有超过 40,000 个活动安装。

在 XSS 攻击中，威胁参与者将恶意 JavaScript 脚本注入易受攻击的网站，这些脚本将在访问者的 Web 浏览器中执行。

影响可能包括未经授权访问敏感信息、会话劫持、通过重定向到恶意网站感染恶意软件或完全破坏目标系统。

发现这些攻击的 WordPress 安全公司 Defiant 表示，该漏洞还允许未经身份验证的攻击者在运行未修补插件版本（最高并包括 2.10.1）的 WordPress 网站上创建流氓管理员帐户。

此次攻击活动中利用的安全漏洞已于 1 月份通过 2.10.2 版的发布进行了修补。

“根据我们的记录，该漏洞自 2023 年 2 月 5 日以来一直受到频繁攻击，但这是我们所见过的针对它的最大规模攻击，”威胁分析师 Ram Gall 表示。

“自 2023 年 5 月 23 日以来，我们已经阻止了来自近 14,000 个 IP 地址的近 300 万次针对超过 150 万个站点的攻击，并且攻击仍在继续。”

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685094953412759.png "1685094763180615.png")

尽管这种持续的攻击活动具有大规模性质，但 Gall 表示，威胁参与者使用了一种配置错误的漏洞利用，即使针对运行易受攻击的插件版本的 WordPress 站点，该漏洞也可能不会部署有效负载。

即便如此，建议使用 Beautiful Cookie Consent Banner 插件的网站管理员或所有者将其更新到最新版本，因为即使攻击失败也可能会破坏存储在 nsc\_bar\_bannersettings\_json 选项中的插件配置。

该插件的补丁版本也已更新，以在网站成为这些攻击的目标时进行自我修复。

尽管当前的攻击可能无法向网站注入恶意载荷，但该攻击背后的威胁行为者可以随时解决这个问题，并 potentially 感染仍然暴露的任何网站。

上周，威胁行为者也开始探测运行 Essential Addons for Elementor 和 WordPress Advanced Custom Fields 插件的 WordPress 网站。这些攻击始于发布证明概念 (PoC) 漏洞之后，该漏洞允许未认证的攻击者在重置管理员密码并获取特权访问后劫持网站。

本文翻译自：https://www.bleepingcomputer.com/news/security/hackers-target-15m-wordpress-sites-with-cookie-consent-plugin-exploit/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Nila1ygK)

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

![](https://img.4hou.com/images/u=2076373339,2173673275&fm=26&gp=0.jpg)

# [walker](https://www.4hou.com/member/xyv9)

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

[查看更多](https://www.4hou.com/member/xyv9)

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