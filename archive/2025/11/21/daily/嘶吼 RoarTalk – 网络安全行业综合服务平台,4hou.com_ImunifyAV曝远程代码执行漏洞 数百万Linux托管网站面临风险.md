---
title: ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险
url: https://www.4hou.com/posts/rpAk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-11-21
fetch_date: 2025-11-22T03:06:59.490488
---

# ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险

ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/loginIng)
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

# ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)4938

收藏

导语：该漏洞的根源在于AI-bolit组件的反混淆逻辑：当工具尝试解包恶意软件以进行扫描时，会执行从混淆PHP文件中提取的、由攻击者控制的函数名和数据。

Linux服务器专用恶意软件扫描工具ImunifyAV存在远程代码执行漏洞，攻击者可利用该漏洞入侵主机环境。这款工具目前已被数千万个网站采用。

该漏洞影响AI-bolit恶意软件扫描组件的32.7.4.0版本之前的所有版本。该组件集成于Imunify360安全套件、付费版ImunifyAV+，以及免费版恶意软件扫描工具ImunifyAV中。

据安全公司Patchstack透露，该漏洞已于10月底被发现，工具开发商CloudLinux当时已发布修复补丁。目前该漏洞尚未分配CVE编号。

11月10日，开发商将该补丁反向移植到旧版本Imunify360 AV中。在最新发布的安全公告中，CloudLinux警告用户该漏洞属于“高危安全漏洞”，建议“尽快”将软件升级至32.7.4.0版本。

**工具应用范围广泛**

ImunifyAV是Imunify360安全套件的组成部分，主要用于虚拟主机服务商或通用Linux共享主机环境。该产品通常在主机平台层面安装，而非由终端用户直接部署。它在共享主机方案、托管式WordPress主机、cPanel/WHM服务器及Plesk服务器中应用极为普遍。

据Imunify 2024年10月公布的数据，虽然网站管理员很少直接与该工具交互，但它仍是一款无处不在的后台工具，默默为5600万个网站提供防护，且Imunify360的安装量已超过64.5万次。

**漏洞成因与利用条件**

该漏洞的根源在于AI-bolit组件的反混淆逻辑：当工具尝试解包恶意软件以进行扫描时，会执行从混淆PHP文件中提取的、由攻击者控制的函数名和数据。

这一问题的核心是工具使用了“call\_user\_func\_array”函数，但未对函数名进行验证，导致攻击者可执行system、exec、shell\_exec、passthru、eval等危险PHP函数。

Patchstack指出，利用该漏洞的前提是Imunify360 AV在分析环节启用主动反混淆功能——独立版AI-Bolit命令行工具（CLI）的默认配置中，该功能处于禁用状态。

但Imunify360套件中集成的扫描组件，会强制在后台扫描、按需扫描、用户发起扫描及快速扫描中保持“始终开启”反混淆功能，这恰好满足了漏洞利用的条件。

研究人员已公开一个概念验证（PoC）漏洞利用代码：在tmp目录创建一个PHP文件，当杀毒工具扫描该文件时，就会触发远程代码执行。

![poc(1).png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251117/1763360736139842.png "1763360736139842.png")

概念验证利用

这可能导致整个网站被入侵，若扫描工具在共享主机环境中以高权限运行，还可能引发服务器完全被接管的严重后果。

CloudLinux的修复方案新增了白名单机制，仅允许安全、确定的函数在反混淆过程中执行，从而阻止任意函数调用。

尽管开发商未发布明确警告，也未分配便于预警和追踪的CVE编号，但系统管理员仍应将软件升级至32.7.4.0版本或更高版本。

目前，官方尚未提供漏洞入侵检测方法、检测指南，也未确认该漏洞是否已被在野利用。随后，Patchstack研究人员经进一步检测发现，该漏洞的严重程度超出最初预期——存在一种更简易的利用途径，无需上传恶意软件即可发起攻击。

文章来源自：https://www.bleepingcomputer.com/news/security/rce-flaw-in-imunifyav-puts-millions-of-linux-hosted-sites-at-risk/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?CYJdGA9V)

#### 你可能感兴趣的

* [![]()

  ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)
* [![]()

  高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
* [![]()

  Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
* [![]()

  Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)
* [![]()

  QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)
* [![]()

  近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)
  2025-11-21 12:00:00
* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)
  2025-11-19 11:10:33
* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)
  2025-11-06 12:00:00
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)
  2025-11-04 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [ImunifyAV曝远程代码执行漏洞 数百万Linux托管网站面临风险](https://www.4hou.com/posts/rpAk)

  胡金鱼
* [高危runC漏洞曝光 黑客可突破Docker容器逃逸](https://www.4hou.com/posts/XP4l)

  胡金鱼
* [Windows Server WSUS高危漏洞遭在野利用 微软紧急发布补丁](https://www.4hou.com/posts/nlpD)

  胡金鱼
* [Windows SMB高危提权漏洞遭活跃利用 未打补丁设备恐被获取SYSTEM权限](https://www.4hou.com/posts/8g5l)

  胡金鱼
* [QNAP警示ASP.NET Core高危漏洞波及NetBak PC备份工具](https://www.4hou.com/posts/pn0r)

  胡金鱼
* [近7.6万台WatchGuard Firebox安全设备存在漏洞 面临高危远程代码执行风险](https://www.4hou.com/posts/7M5w)

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