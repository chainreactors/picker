---
title: macOS Sequoia 更新后出现防护软件网络连接错误问题
url: https://www.4hou.com/posts/Dx8B
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-10-12
fetch_date: 2025-10-06T18:47:26.244706
---

# macOS Sequoia 更新后出现防护软件网络连接错误问题

macOS Sequoia 更新后出现防护软件网络连接错误问题 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# macOS Sequoia 更新后出现防护软件网络连接错误问题

胡金鱼
[技术](https://www.4hou.com/category/technology)
2024-10-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)94307

收藏

导语：这仅适用于 Endpoint Security 版本 8.1.6.0 及更高版本以及 ESET Cyber Security 版本 7.5.74.0 及更高版本，因为 macOS 15 不支持任何旧版本。

macOS 15“Sequoia”的用户在使用某些端点检测和响应 (EDR) 或虚拟专用网络 (VPN) 解决方案以及 Web 浏览器时报告网络连接错误。在停用这些工具后问题得到解决，这表明网络堆栈存在不兼容问题。

受影响的用户描述了 CrowdStrike Falcon 和 ESET Endpoint Security 的问题，以及防火墙引起的数据包损坏，从而导致 Web 浏览器 SSL 失败或无法使用“wget”和“curl”。

9 月，苹果发布了 Sequoia，称其为“全球最先进的桌面操作系统的最新版本”。在一份非公开公告中，CrowdStrike 表示由于 macOS 15 Sequoia 的内部网络结构发生变化，建议客户不应升级，直到发布完全支持 macOS 15 Sequoia 的 Mac 传感器为止。

据报道，SentinelOne 支持还警告用户不要立即升级到 macOS Sequoia，因为最近发现了可用性问题。

人们还报告了 Mullvad VPN 以及他们用于远程工作的企业 VPN 产品存在间歇性连接问题，但据了解 ProtonVPN 在最新的 macOS 版本上运行良好。

虽然苹果公司尚未回应有关这些问题的新闻请求，但 据 macOS 15 发行说明显示，该操作系统防火墙中的一项功能已被弃用，这可能是导致这些问题的原因。

```
Application Firewall settings are no longer contained in a property list. If your app or workflow relies on changing Application Firewall settings by modifying /Library/Preferences/com.apple.alf.plist, then you need to make changes to use the socketfilterfw command line tool instead (124405935)
```

谷歌还在最近的 Chromium 错误报告中指出这一变化导致了问题，他们表示需要改变谷歌 Chrome 检测 Mac 防火墙设置的方式，改用“socketfilterfw”。

**可能的解决方案**

ESET 已针对升级到 macOS Sequoia 后遇到连接丢失问题的用户发布了一份咨询报告，建议用户导航至系统设置 > 网络 > 过滤器 > 并从列表中删除 ESET 网络。重新启动系统后，网络连接应可正常运行，ESET 产品应可正常运行。

![eset.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240924/1727162179127902.png "1727162105357273.png")

从 macOS 过滤器中删除 ESET

该安全供应商还指出，这仅适用于 Endpoint Security 版本 8.1.6.0 及更高版本以及 ESET Cyber Security 版本 7.5.74.0 及更高版本，因为 macOS 15 不支持任何旧版本。

有安全研究员在一篇博客文章中提供了一个解决防火墙引起的问题的临时解决方案，但用户需要将其应用于他们使用的每个应用程序。

他强调了内置防火墙无法正确处理 UDP 流量的问题，在许多情况下会导致 DNS 故障，并提出了一个不太理想的解决方案，即“打漏洞”来解除令人困扰的限制。

![toot.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20240924/1727162180882343.jpg "1727162160336850.jpg")

与此同时，Mullvad VPN 表示，他们已经意识到用户在最新的 macOS 版本中遇到的问题，并正在积极努力寻找解决方案。

如果您使用 EDR 安全产品、VPN 或依赖严格的防火墙配置，建议暂时推迟迁移到 macOS 15，直到问题得到解决。

文章翻译自：https://www.bleepingcomputer.com/news/apple/macos-sequoia-change-breaks-networking-for-vpn-antivirus-software/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?XAnbtjGF)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

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