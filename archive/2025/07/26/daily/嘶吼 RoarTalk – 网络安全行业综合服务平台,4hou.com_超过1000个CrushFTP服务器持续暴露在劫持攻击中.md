---
title: 超过1000个CrushFTP服务器持续暴露在劫持攻击中
url: https://www.4hou.com/posts/33gM
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-26
fetch_date: 2025-10-06T23:16:33.830905
---

# 超过1000个CrushFTP服务器持续暴露在劫持攻击中

超过1000个CrushFTP服务器持续暴露在劫持攻击中 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 超过1000个CrushFTP服务器持续暴露在劫持攻击中

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-07-25 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)91563

收藏

导语：近年来，像CrushFTP这样的托管文件传输解决方案一直是勒索软件团伙的高价值目标。

在网上暴露的超过1000个CrushFTP实例易受劫持攻击的威胁，这些攻击利用了一个严重的安全漏洞，提供对网页界面的管理员访问权限。

该安全漏洞（CVE-2025-54309）是由于错误处理AS2验证，并影响10.8.5和11.3.4\_23以下的所有CrushFTP版本。该供应商在7月19日将该漏洞标记为在野外被积极利用，并指出攻击可能更早开始，尽管它尚未找到证据来证实这一点。

7月18日上午9点，CrushFTP在野外发现了一个0day漏洞。它可能持续了更长的时间。黑客显然对其代码进行了逆向工程，发现了一些CrushFTP已经修复的bug。

但CrushFTP最近表示，保持最新状态的服务器不容易受到攻击，并指出使用非军事区（DMZ）实例隔离其主服务器的客户不会受到此漏洞的影响。

该公司还建议审查上传和下载日志中的异常活动，以及启用自动更新和服务器和管理访问的白名单ip，以进一步减少利用企图。

根据安全威胁监控平台Shadowserver的扫描，大约有1040个CrushFTP实例仍然没有针对CVE-2025-54309打补丁，很容易受到攻击。

ShadowServer通知CrushFTP客户，他们的服务器不受正在进行的CVE-2025-54309攻击的保护，将其内容暴露给数据盗窃企图。

虽然目前还不清楚这些正在进行的攻击是部署恶意软件还是用于窃取数据，但近年来，像CrushFTP这样的托管文件传输解决方案一直是勒索软件团伙的高价值目标。仅Clop网络犯罪团伙就与针对Accelion FTA、GoAnywhere MFT、MOVEit Transfer以及最近的Cleo软件的零日漏洞的多次数据盗窃活动有关。

据悉，2024年4月，CrushFTP还修补了一个被积极利用的零日漏洞（追踪为CVE-2024-4040），该漏洞允许未经身份验证的攻击者逃离用户的虚拟文件系统（VFS）并下载系统文件。

当时，网络安全公司CrowdStrike发现有证据表明，针对多个美国组织的CrushFTP实例的攻击可能出于政治动机，主要目的是收集情报。

文章翻译自：https://www.bleepingcomputer.com/news/security/over-1-000-crushftp-servers-exposed-to-ongoing-hijack-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ufm5pK1n)

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