---
title: Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行
url: https://www.4hou.com/posts/MXOm
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-04-10
fetch_date: 2026-04-11T04:21:05.671997
---

# Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行

Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-04-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)10981

收藏

导语：由于系统对 HTTP 重定向处理不当，攻击者可直接访问 ShareFile 管理后台界面。

最新发现，企业级安全文件传输解决方案 Progress ShareFile 存在两处漏洞，攻击者可将其组合利用，在无需身份认证的情况下从受影响环境中窃取文件。Progress ShareFile 是一款文档共享与协作产品，广泛应用于大中型企业。

此类文件传输平台历来是勒索软件团伙的重点攻击目标，此前 Clop 勒索组织就曾利用 Accellion FTA、SolarWinds Serv-U、Gladinet CentreStack、GoAnywhere MFT、MOVEit Transfer、Cleo 等产品中的漏洞实施大规模数据窃取攻击。

watchTowr 的研究人员在 Progress ShareFile 5.x 分支的 Storage Zones Controller（SZC，存储区域控制器）组件中，发现了一处认证绕过漏洞（CVE-2026-2699）和一处远程代码执行漏洞（CVE-2026-2701）。

存储区域控制器（SZC）允许用户将数据存储在自有基础设施（本地或第三方云）或 Progress 官方系统中，从而让客户对数据拥有更强的控制权。

在 watchTowr 完成负责任漏洞披露后，Progress 已发布 ShareFile 5.12.4 版本，修复了上述问题。

**攻击原理**

watchTowr 研究人员在最新发布的报告中介绍，整个攻击链首先利用 CVE-2026-2699 认证绕过漏洞。由于系统对 HTTP 重定向处理不当，攻击者可直接访问 ShareFile 管理后台界面。

获取权限后，攻击者可修改存储区域配置，包括文件存储路径、区域密钥及相关敏感安全参数。

随后，攻击者可利用第二个漏洞 CVE-2026-2701，通过滥用文件上传与解压功能，将恶意 ASPX 网页后门放置在应用根目录，从而在服务器上实现远程代码执行。

研究人员指出，要成功利用漏洞，攻击者需要生成合法的 HMAC 签名，并提取和解密内部密钥。但在成功利用 CVE-2026-2699 之后，攻击者可设置或控制与密钥相关的配置项，上述步骤均可实现。

![图片70.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260403/1775203717136196.png "1775203717136196.png")

漏洞利用链概述

**影响范围与暴露情况**

根据 watchTowr 的扫描结果，约有 3 万个存储区域控制器实例暴露在公网。ShadowServer 基金会监测到约 700 台可公网访问的 Progress ShareFile 实例，其中大部分位于美国和欧洲地区。

watchTowr 于 2 月 6 日至 13 日期间发现这两处漏洞并上报给 Progress 公司，并于 2 月 18 日验证了完整攻击链可在 ShareFile 5.12.4 之前版本生效。厂商已于 3 月 10 日在 5.12.4 版本中推送安全更新。

截至本文发布，暂未发现野外在野利用行为。但由于漏洞细节已公开，极易吸引攻击者跟进利用，因此运行存在漏洞的 ShareFile 存储区域控制器版本的系统应立即安装补丁。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-progress-sharefile-flaws-can-be-chained-in-pre-auth-rce-attacks/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ZwwBhhdS)

#### 你可能感兴趣的

* [![]()

  Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行](https://www.4hou.com/posts/MXOm)
* [![]()

  嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码](https://www.4hou.com/posts/8gPj)
* [![]()

  新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)
* [![]()

  嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)
* [![]()

  Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马](https://www.4hou.com/posts/J1GK)
* [![]()

  嘶吼安全动态｜国家安全部提醒：“囤词元暴富” 背后，暗藏间谍窃取数据陷阱 苹果Mac威胁50.32%来自木马，盗窃用户隐私成主要目的](https://www.4hou.com/posts/YZoA)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行](https://www.4hou.com/posts/MXOm)
  2026-04-10 12:00:00
* [嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码](https://www.4hou.com/posts/8gPj)
  2026-04-10 11:59:00
* [新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)
  2026-04-09 12:00:00
* [嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)
  2026-04-09 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Progress ShareFile曝新漏洞 可组合实现未认证远程代码执行](https://www.4hou.com/posts/MXOm)

  胡金鱼
* [嘶吼安全动态|八部门联合发布《 科技数据安全管理暂行规定》，4月10日起实施 黑客利用像素级SVG技巧隐藏信用卡窃密代码](https://www.4hou.com/posts/8gPj)

  胡金鱼
* [新型CrystalRAT恶意软件新增远程控制、数据窃取等功能](https://www.4hou.com/posts/LGMD)

  胡金鱼
* [嘶吼安全动态｜中央网信办召开全国网络法治工作会议 设备码钓鱼攻击暴增36倍，新型攻击工具在网上大肆扩散](https://www.4hou.com/posts/6MLO)

  胡金鱼
* [Claude Code源码泄露遭利用，攻击者借GitHub散播窃密木马](https://www.4hou.com/posts/J1GK)

  胡金鱼
* [嘶吼安全动态｜国家安全部提醒：“囤词元暴富” 背后，暗藏间谍窃取数据陷阱 苹果Mac威胁50.32%来自木马，盗窃用户隐私成主要目的](https://www.4hou.com/posts/YZoA)

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