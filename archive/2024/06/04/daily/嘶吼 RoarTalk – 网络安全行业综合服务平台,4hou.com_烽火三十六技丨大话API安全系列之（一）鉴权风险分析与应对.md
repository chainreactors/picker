---
title: 烽火三十六技丨大话API安全系列之（一）鉴权风险分析与应对
url: https://www.4hou.com/posts/7yvy
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-04
fetch_date: 2025-10-06T16:55:17.798449
---

# 烽火三十六技丨大话API安全系列之（一）鉴权风险分析与应对

烽火三十六技丨大话API安全系列之（一）鉴权风险分析与应对 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 烽火三十六技丨大话API安全系列之（一）鉴权风险分析与应对

盛邦安全
[行业](https://www.4hou.com/category/industry)
2024-06-03 14:53:30

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)107874

收藏

导语：API的主要安全问题集中在攻击绕过、权限提升和数据泄露等方面，本期我们将重点探讨API鉴权相关的风险。在介绍鉴权风险之前，首先可以看一下API的分类。

数据要素目前已经成为推动数字经济高质量发展的新型生产要素，围绕数据安全的攻防博弈也逐渐成为当下网络安全建设的主旋律之一，API接口作为数据互通和共享的主要技术手段，首当其冲要面临入侵渗透和数据窃取的威胁，因此API安全也成为数据安全的重要抓手。

API的主要安全问题集中在攻击绕过、权限提升和数据泄露等方面，本期我们将重点探讨API鉴权相关的风险。在介绍鉴权风险之前，首先可以看一下API的分类。

API（应用程序编程接口）的标准概念是一些预先定义的函数，目的是提供应用程序与开发人员基于某软件或硬件得以访问一组例程的能力。随着云计算、移动互联网、物联网的蓬勃发展，越来越多的开发平台和第三方服务快速涌现，应用系统与功能模块复杂性不断提升，应用开发深度依赖于API之间的相互调用。按照不同的角度划分，API接口可以概括为如下类型：

![QQ截图20240603135457.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240603/1717394375172055.png "1717394098545663.png")

从安全的角度出发，由于API接口既能够起到连接服务的功能，又可以用来传输数据，因此API的安全防护至关重要。同时，目前面向互联网开放的应用服务类API，主要以HTTP协议通道来承载，因此Web类API是目前需要优先关注的类型，从下图的对比可以直观说明，API接口的开放将进一步缩短攻击路径。

![QQ截图20240603135523.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240603/1717394376129669.png "1717394279127869.png")

接下来我们再看下Web类API接口常用的几种鉴权设计：

**1、Cookie+Session**

最传统的API鉴权方式，用户登录成功后，服务端会生成一个session来保持状态，每个session都有唯一的session\_id存储在客户端的cookie中，可以用来标识用户登录信息，这样客户端每次访问都带着session\_id，服务端就可以做鉴权判断了。这种方式实现简单但性能不高，而且cookie可以被劫持篡改，主要适用于传统的web网站。

**2、API密钥**

API密钥指的是服务器为每个客户端生成一对API Key/API Secret并告知客户端，客户端请求时需要携带这些密钥，只有资源、API Key和API Secret都匹配才可以访问服务器的资源。这类鉴权方式实现相对简单，但密钥容易被截取和冒充，所以存储和管理非常重要，并且如果业务复杂，相应的维护工作量也会很大，所以更适用于做一些聚合类的数据获取。

**3、OAuth**

OAuth是一个安全、开放的标准，可以提供相互认证的框架，通常存在用户端、服务端和第三方服务这三类角色，由用户端授权第三方服务使用自己的某些权限去访问服务端的资源，比如用自己的社交平台账号来快捷登录其他应用，或者让手机上的一个APP来共享访问其他应用数据。这类鉴权方式安全性更高，但设置相对复杂，并不适用于所有场景。

**4、JWT**

JSON Web Token是一种安全标准，可以发布令牌并对发布的令牌做接入验证，以此来实现对资源访问的权限控制。JWT是一种基于JSON格式的安全令牌，常用于需要携带额外信息的鉴权场景，比如单点登录。这类鉴权方式轻量级、可扩展性好，但是密钥一旦泄露，令牌可能会受到威胁。

不同的业务服务可以选择适用的接口鉴权方式，从开发者的视角而言，无论API的应用场景如何，通常也都会设计对应的鉴权机制，但从攻击者的视角而言，再严谨的权限设计仍然无法避免逻辑上可以利用的漏洞风险。

**最后我们看几种常见的接口缺陷示例：**

**1、修改参数提升接口权限**

![QQ截图20240603135635.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240603/1717394377200549.png "1717394195351802.png")

某APP用户管理API接口权限限制不严格，使用任意能通过认证的token，通过修改id值即可获取任意用户信息，通过该token亦可随意调用其他API接口获取非授权用户信息。

**2、修改参数执行批量查询**

![微信图片_20240603150209.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240603/1717398030175264.png "1717398030175264.png")

某系统数据查询API接口未对查询条件和权限进行限制，基于已认证token，通过修改API接口传输参数的pageSize值，即可获取指定数量级的数据，造成敏感数据批量泄露。

**3、系统内部接口非法调用**

某平台程序调用API接口可用于查询账户信息、订单信息等敏感数据，但未对前端应用做强鉴权限制，第三方应用可以违规调用该接口并售卖数据非法获利。

类似的风险案例不在少数，由此可见，即使开发者可以做不同安全级别的API接口权限控制，也可以借助API网关执行严格的发布管理，但攻击者往往只需要找到一个逻辑漏洞作为突破口即可达成目的，因此，从防守者的角度而言，清晰的API接口画像和行为分析是识别API鉴权风险的前提。

盛邦安全API安全防护系统（RayAPI）可以从鉴权分析、风险识别和调用保护三个层面来对API接口进行风险监测与防护。

1、鉴权分析

通过API接口学习与状态监控，对接口及其鉴权情况进行分析。

鉴权要素识别：检查接口请求中是否有token、cookie等鉴权要素。

接口属性画像：识别接口属性，如系统登录、数据查询、数据操作、功能调用等。

![QQ截图20240603135740.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240603/1717394378433920.png "1717394262164034.png")

2、风险识别

通过对API接口请求与响应记录的智能分析，快速识别鉴权风险。

未鉴权风险分析：识别接口无鉴权要素但执行敏感调用的情况，判定为未鉴权风险。

弱鉴权风险分析：识别接口可随机数token访问、同源多token访问等情况，判定为弱鉴权风险。

![QQ截图20240603135919.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240603/1717394379681832.png "1717394362205094.png")

3、调用保护

针对可能存在的未鉴权或弱鉴权安全风险，通过灵活的访问控制策略来进行加固保护。

白名单策略：基于源地址、referer、cookie等条件设定白名单策略，限制非法访问。

多条件策略：按照源地域、接口、请求类型等条件设定组合策略，执行细粒度的接口访问控制。

![QQ截图20240603135938.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240603/1717394379809318.png "1717394379809318.png")

在当前的数字化浪潮中，API安全已经成为数据与网络安全的重要一环。鉴权作为API安全的第一道防线，其重要性不言而喻。通过深入分析和理解鉴权风险，我们可以采取一系列有效的应对策略，降低安全风险，保护企业的数据和网络安全。

当然，API安全并不仅仅局限于鉴权风险。在后续的系列文章中，我们将继续深入探讨API安全的其他重要议题。同时，我们也期待与大家进行深入的交流和讨论，共同推动API安全技术的发展，为企业的数字化转型保驾护航。

[原文链接](https://www.webray.com.cn/skippath/blog/blog_2107.html)

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lhTyGzc1)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/3c8d3af7c49c95c16dd14518142759d6.png)

# [盛邦安全](https://www.4hou.com/member/9ZO4)

让网络空间更有序

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/9ZO4)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

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