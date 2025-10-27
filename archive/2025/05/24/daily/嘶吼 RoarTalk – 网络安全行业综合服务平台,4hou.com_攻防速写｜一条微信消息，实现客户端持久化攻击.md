---
title: 攻防速写｜一条微信消息，实现客户端持久化攻击
url: https://www.4hou.com/posts/5MzK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-05-24
fetch_date: 2025-10-06T22:27:36.743849
---

# 攻防速写｜一条微信消息，实现客户端持久化攻击

攻防速写｜一条微信消息，实现客户端持久化攻击 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 攻防速写｜一条微信消息，实现客户端持久化攻击

企业资讯
[技术](https://www.4hou.com/category/technology)
2025-05-23 15:21:11

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)113310

收藏

导语：从微信看IM软件客户端背后的安全博弈。

从白宫幕僚到战地记者，即时通讯软件（IM）是无数关键人群不可或缺的沟通工具。无论是WhatsApp、Telegram，还是微信、QQ，它们已经成为现代社会的“数字血管”，承载着数十亿用户的社交、支付与办公等核心业务，其安全性直接关联个人隐私、金融资产，乃至国家安全。

事实上，关于IM的安全研究早已展开。2019年Project Zero披露了iMessage中的CVE-2019-8641漏洞[1]，该漏洞是一个内存破坏问题。iMessage会自动解析消息中的富媒体内容，攻击者仅需发送恶意构造的文件，即可在无需用户交互的情况下实现远程代码执行，完全控制目标iPhone设备。

DARKNAVY将在本文中以微信为例，从URL解析、文件处理、网页访问等典型场景出发，系统梳理即时通讯客户端的关键攻击面，剖析攻防背后的博弈。

**IM攻击面概览**

从体系架构出发，即时通讯软件的攻击面可划分为三个主要维度，分别是客户端层面、通信协议层面以及云端服务层面。本文将重点分析客户端的攻击面，探讨其中可能导致远程代码执行或敏感信息泄露的安全问题。

**1 URL链接**

多数IM客户端支持自定义协议（如 weixin://、tg://）以实现应用内跳转，然而，攻击者可借助构造伪装为合法链接的恶意请求，利用客户端对URL校验不严的漏洞诱导用户访问钓鱼站点。更具隐蔽性的是对一些特殊功能URL的滥用。例如，slack://settings可以实现更改设置的功能，攻击者通过构造特定参数的链接并诱导用户点击，可以实现数据窃取[2]。

![微信图片_2025-05-23_150231_560.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984733554383.png "1747983771186651.png")

使用weixin://协议打开微信

**2 文件解析**

为提升用户体验，IM客户端通常集成自有文件解析逻辑以实现格式预览与内容提取。攻击者可通过构造特制的恶意文件，利用解析功能的漏洞实现远程代码执行。例如，CVE-2019-11932[3]和CVE-2025-30401[4]分别是WhatsApp Android客户端和Windows客户端中的严重漏洞，前者通过恶意GIF文件触发攻击，后者则通过伪装成图像的可执行文件诱导用户执行。

**3 内置浏览器组件**

多数IM客户端内置浏览器以支持网页访问，通常采用基于Chrome的自定义内核。其攻击面主要集中在两类技术路径上：

**一是JSBridge**，若客户端未对暴露给网页接口进行精细化权限控制，则可能被恶意网页调用实现权限滥用；

**二是浏览器内核漏洞**，例如，DARKNAVY团队于2023年发布的预警[5]中指出，源于Chromium内核中libwebp组件的漏洞CVE-2023-41064 & 4863，影响包括微信、钉钉、QQ在内的多个主流IM软件。

![微信图片_2025-05-23_150416_785.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984734163916.png "1747983880183208.png")

CVE-2023-41064 & 4863漏洞影响Windows平台微信客户端

**4 小程序生态**

为拓展服务边界，微信、钉钉等IM客户端纷纷开放小程序平台，赋予第三方开发者丰富的系统权限，如文件系统访问、传感器调用、API接口使用等。然而，若客户端在权限管理或功能实现上存在疏漏，攻击者可借助恶意小程序实施攻击。

**微信攻击面分析**

DARKNAVY团队对微信客户端的攻击面进行了初步调研，下面将从多个维度介绍微信客户端面临的主要安全风险及其应对机制。

**1 微信URL链接**

微信客户端内置了调试链接机制，当用户访问的URL中包含 debugxweb.qq.com 时，会根据URL中的参数触发不同调试行为。例如，传入参数 show\_webview\_version 可在页面上展示当前WebView内核的版本信息及相关配置。

![微信图片_2025-05-23_150457_928.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984735646728.jpg "1747983956115241.jpg")

show\_webview\_version展示的版本信息

尽管该机制为调试带来便利，但若攻击者构造恶意URL并诱导用户访问，可能在无用户感知的情况下触发高风险操作，如版本回退或配置变更。为降低风险，微信客户端限制了 install\_embed\_plugin 等敏感操作仅可在开启 bEnableLocalDebug 选项后执行。同时，对于如 set\_config\_url 等可修改获取配置URL的功能，微信也加入了严格的域名与协议校验，仅允许使用 HTTPS 且域名限定为 dldir1.qq.com 或 dldir1v6.qq.com，有效规避了配置被篡改的风险。

![微信图片_2025-05-23_150612_664.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984736132714.png "1747984005115808.png")

set\_config\_url等功能的URL校验

此外，微信支持 weixin:// 协议实现内部跳转，例如 weixin://dl/ 用于页面导航。对于带 ticket 参数的链接，微信客户端会通过 /cgi-bin/mmbiz-bin/translatelink 接口向云端请求真实跳转地址，从而避免攻击者伪造链接诱导用户访问任意页面，有效增强了链接跳转的安全性。

**2 微信内置浏览器组件（XWEB）**

安卓微信使用自研的 XWEB 内核，基于 Chromium 开发。截止本文编辑时，内核开发版的Chromium版本是134.0.6998.136，而现网版本是130.0.6723.103，而Chrome官方浏览器的版本是136.0.7103.93。XWEB保持了相对领先的内核版本，不过仍存在一定的滞后性，有可能受未修复的公开漏洞影响。

为提升浏览器安全性，微信默认启用了多进程沙箱机制。主进程运行在 xweb\_privileged\_process\_0，而渲染进程则隔离于 xweb\_sandboxed\_process\_0，有效缓解了对渲染进程漏洞的攻击利用。

![微信图片_2025-05-23_150734_200.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984737470302.png "1747984130539077.png")

安卓微信客户端的进程隔离

微信还提供了丰富的 JSBridge 接口供网页调用原生功能，例如 sendEmail 可唤起客户端发邮件、scanQRCode 可调用摄像头扫描二维码。

![微信图片_2025-05-23_150902_401.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984738115348.jpg "1747984170508137.jpg")

使用sendEmail进入发邮件界面

为防止滥用，微信客户端在加载网页时会根据URL向云端请求权限列表，以精细化控制每个JSBridge接口是否可用。在某些特定官方测试页面上，大多数接口默认开放，而在其他页面中，仅开放少数接口。此种基于页面来源的权限划分策略，有效限制了潜在恶意网页的破坏能力。

**3 微信小程序安全机制**

微信小程序采用JavaScript开发，架构上分为渲染层与逻辑层，分别在独立线程中运行，相互隔离。其中渲染层负责界面展示，而逻辑层处理业务逻辑。开发者编写的逻辑层的JavaScript脚本不能使用浏览器暴露出来的 DOM API，而渲染层的JavaScript脚本也无法使用开发者的高权限功能。微信客户端给渲染层和逻辑层暴露的JSAPI功能也有所不同，例如渲染层可以调用insertVideoPlayer、insertTextArea等功能，而逻辑层可以调用saveFile、addDownloadTask等功能。这样的隔离防止了攻击者通过小程序的XSS等漏洞在渲染层执行高权限操作。

![微信图片_2025-05-23_151009_913.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984739167112.png "1747984244278244.png")

addToPagePool添加渲染层的JSAPI

![微信图片_2025-05-23_151055_881.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250523/1747984740228062.png "1747984275388546.png")

渲染层可以使用的一些JSAPI

**结语**

微信作为国内最具代表性的IM软件，在安全机制上体现出多层防护与权限细化管理的设计思路，如JSBridge精细授权、浏览器沙箱隔离、小程序双线程架构等，体现出其对安全风险的高度重视。

作为长期关注即时通讯软件安全的研究团队，DARKNAVY始希望通过持续的漏洞研究、攻防分析与技术分享，推动IM生态在保障用户体验的同时，更加稳健、安全、可信地向前发展。

**预告**

本研究内容已入选专注纯粹技术交流的全新网络安全闭门沙龙 deepsec.cc (Deep Security Closed-door Conference)，将于6月16日在现场深入探讨。

**参  考**

[1] <https://googleprojectzero.blogspot.com/2020/01/remote-iphone-exploitation-part-3.html>

[2] <https://medium.com/tenable-techblog/stealing-downloads-from-slack-users-be6829a55f63>

[3] <https://awakened1712.github.io/hacking/hacking-whatsapp-gif-rce/>

[4] <https://www.facebook.com/security/advisories/cve-2025-30401>

[5] <https://mp.weixin.qq.com/s/zqxkYk7vRvDPKxgoVj1PRw>

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?vrlZScW9)

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

![](https://img.4hou.com/images/u=2457118598,2121472893&fm=26&gp=0.jpeg)

# [企业资讯](https://www.4hou.com/member/aQWl)

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

[查看更多](https://www.4hou.com/member/aQWl)

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

![]...