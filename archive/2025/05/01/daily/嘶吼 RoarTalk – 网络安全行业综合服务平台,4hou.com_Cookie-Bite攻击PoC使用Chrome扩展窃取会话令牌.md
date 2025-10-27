---
title: Cookie-Bite攻击PoC使用Chrome扩展窃取会话令牌
url: https://www.4hou.com/posts/kgNN
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-01
fetch_date: 2025-10-06T22:23:39.318420
---

# Cookie-Bite攻击PoC使用Chrome扩展窃取会话令牌

Cookie-Bite攻击PoC使用Chrome扩展窃取会话令牌 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Cookie-Bite攻击PoC使用Chrome扩展窃取会话令牌

胡金鱼
[技术](https://www.4hou.com/category/technology)
2025-04-30 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)74194

收藏

导语：微软将研究人员在攻击演示中的登录尝试标记为“atRisk”，因为他们使用了VPN，因此监控异常登录是防止这些攻击的关键。

一种名为“Cookie-Bite”的概念验证攻击利用浏览器扩展程序从 Azure Entra ID 中窃取浏览器会话 Cookie，以绕过多因素身份验证（MFA）保护，并保持对 Microsoft 365、Outlook 和 Teams 等云服务的访问。

此次攻击由 Varonis 安全研究人员设计，他们分享了一种概念验证（PoC）方法，涉及一个恶意的和一个合法的 Chrome 扩展程序。然而，窃取会话 cookie 并非新鲜事，因为信息窃取程序和中间人网络钓鱼攻击通常都会将其作为目标。

虽然通过窃取 Cookie 来入侵账户并非新手段，但“Cookie-Bite”技术中恶意 Chrome 浏览器扩展程序的使用因其隐秘性和持久性而值得关注。

**Cookie扩展攻击**

“Cookie-Bite”攻击由一个恶意的 Chrome 扩展程序构成，该扩展程序充当信息窃取器，专门针对 Azure Entra ID（微软基于云的身份和访问管理（IAM）服务）中的“ESTAUTH”和“ESTSAUTHPERSISTNT”这两个 Cookie。

ESTAUTH 是一个临时会话令牌，表明用户已通过身份验证并完成了多因素身份验证。它在浏览器会话中有效，最长可达 24 小时，在应用程序关闭时过期。

ESTSAUTHPERSISTENT 是在用户选择“保持登录状态”或 Azure 应用 KMSI 策略时创建的会话 Cookie 的持久版本，其有效期最长可达 90 天。

应当注意的是，虽然此扩展程序是为针对微软的会话 Cookie 而创建的，但它可以被修改以针对其他服务，包括谷歌、Okta 和 AWS 的 Cookie。

Varonis 的恶意 Chrome 扩展程序包含用于监控受害者登录事件的逻辑，监听与微软登录网址匹配的标签页更新。

当登录发生时，它会读取所有作用域为“login.microsoftonline.com”的 Cookie，应用过滤以提取上述两个令牌，并通过 Google 表单将 Cookie 的 JSON 数据泄露给攻击者。

“在将该扩展程序打包成 CRX 文件并上传至 VirusTotal 后，结果显示目前没有任何安全供应商将其检测为恶意程序，”Varonis 警告称。

![varonis-extracting-cookies.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745393452144885.png "1745393232261523.png")

Chrome扩展窃取微软会话cookie

如果攻击者可以访问设备，他们可以部署一个PowerShell脚本，通过Windows任务调度程序运行，在每次启动Chrome时使用开发者模式自动重新注入未签名扩展。

![powershell.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745393453157084.png "1745393266164631.png")

PowerShell攻击中使用的例子

一旦cookie被盗，攻击者就会将其注入浏览器，就像其他被盗的cookie一样。这可以通过合法的Cookie-Editor Chrome扩展等工具来实现，该扩展允许威胁行为者将被盗的cookie导入到他们的浏览器“login.microsoftonline.com”下。

刷新页面后，Azure将攻击者的会话视为完全经过身份验证，绕过MFA并给予攻击者与受害者相同的访问级别。

![inject.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745393454195307.png "1745393370428487.png")

注入偷来的 cookie

从那里，攻击者可以使用Graph Explorer枚举用户、角色和设备，发送消息或访问Microsoft Teams上的聊天，并通过Outlook Web阅读或下载电子邮件。

通过TokenSmith、ROADtools和AADInternals等工具，还可能进一步利用特权升级、横向移动和未经授权的应用程序注册。

![attack-diagram.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250423/1745393455161316.png "1745393433195518.png")

Cookie-Bite攻击概述

微软将研究人员在攻击演示中的登录尝试标记为“atRisk”，因为他们使用了VPN，因此监控异常登录是防止这些攻击的关键。

此外，建议实施条件访问策略（CAP），以限制对特定IP范围和设备的登录。

关于Chrome扩展，建议执行Chrome ADMX策略，只允许预先批准的扩展运行，并完全阻止用户从浏览器的开发者模式。

文章翻译自：https://www.bleepingcomputer.com/news/security/cookie-bite-attack-poc-uses-chrome-extension-to-steal-session-tokens/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?llIYNzZh)

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