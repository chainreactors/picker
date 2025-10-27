---
title: 黑客利用旧版 Microsoft Office 0 day 实施 Cobalt Strike
url: https://www.4hou.com/posts/m0AG
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-05-07
fetch_date: 2025-10-06T17:15:35.272397
---

# 黑客利用旧版 Microsoft Office 0 day 实施 Cobalt Strike

黑客利用旧版 Microsoft Office 0 day 实施 Cobalt Strike - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用旧版 Microsoft Office 0 day 实施 Cobalt Strike

山卡拉
[新闻](https://www.4hou.com/category/news)
2024-05-06 16:46:48

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)102092

收藏

导语：建议各企业组织定期更新其系统以修补 CVE-2017-8570 等已知漏洞。

黑客利用旧的 Microsoft Office 漏洞 CVE-2017-8570 部署臭名昭著的 Cobalt Strike Beacon，目标是乌克兰的系统。

**CVE-2017-8570：初始向量**

该漏洞于2017年首次发现，允许攻击者通过特制文件执行任意代码，使其成为初始访问的有力工具。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714449270108360.png "1714448439166801.png")

活动概览

攻击者使用恶意 PPSX（PowerPoint 幻灯片）文件，伪装成旧的美国陆军扫雷坦克刀片说明手册。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714449271211752.png "1714448480436317.png")

PPSX内容

该文件经过巧妙设计，可以绕过传统的安全措施。它包括与外部 OLE 对象的远程关系，在 HTTPS URL 之前使用“script:”前缀来隐藏有效负载，避免磁盘存储并使分析复杂化。这种技术凸显了攻击者的复杂性以及对隐秘性和持久性的关注。

Deep Instinct Threat Lab在发现和分析此次网络攻击方面发挥了至关重要的作用。但尽管进行了详细分析，但该行动仍无法归因于任何威胁分子，而了解对手对于预测和缓解他们的策略和技术又至关重要。

**Cobalt Strike Beacon：定制装载机**

此次活动的核心是为 Cobalt Strike Beacon 使用自定义加载程序，Cobalt Strike Beacon 因其强大的命令与控制 (C&C) 功能以及部署更多有效负载的灵活性而成为网络攻击者中流行的工具。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240430/1714449271102390.png "1714448526185812.png")

装载机出口表

此次攻击中使用的 Cobalt Strike Beacon 被配置为与 C&C 服务器进行通信，该服务器在托管条件下，巧妙地伪装成流行的摄影网站。

Beacon 的配置包括软件的破解版本（license\_id 为 0）以及 C&C 通信的详细说明，包括域名、URI 和用于加密交换的公钥。

这种设置有助于对受感染系统进行强有力的控制。

**影响和建议**

此次攻击凸显了对网络安全领域保持警惕以及拥有先进检测能力的重要性，建议各企业组织定期更新其系统以修补 CVE-2017-8570 等已知漏洞。

本文翻译自：https://gbhackers.com/hackers-exploit-old-microsoft-office/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?FQocDEsX)

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