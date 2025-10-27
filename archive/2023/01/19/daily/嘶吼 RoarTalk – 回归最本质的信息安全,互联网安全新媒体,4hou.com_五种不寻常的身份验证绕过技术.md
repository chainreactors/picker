---
title: 五种不寻常的身份验证绕过技术
url: https://www.4hou.com/posts/jJPz
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-19
fetch_date: 2025-10-04T04:14:58.330424
---

# 五种不寻常的身份验证绕过技术

五种不寻常的身份验证绕过技术 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 五种不寻常的身份验证绕过技术

gejigeji
[技术](https://www.4hou.com/category/technology)
2023-01-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)229804

收藏

导语：身份验证绕过漏洞是现代web应用程序中普遍存在的漏洞，也是隐藏最深很难被发现的漏洞。

身份验证绕过漏洞是现代web应用程序中普遍存在的漏洞，也是隐藏最深很难被发现的漏洞。

为此安全防护人员不断在开发新的认证方法，保障组织的网络安全。尽管单点登录(SSO)等工具通常是对旧的登录用户方式的改进，但这些技术仍然可能包含严重的漏洞。无论是业务逻辑错误还是其他软件漏洞，都需要专业人员来分析其中的复杂性。

我们将在本文中介绍五种真实的身份验证绕过技术。

**技术1——刷新令牌终端配置错误**

在这种情况下，一旦用户使用有效凭证登录到应用程序，它就会创建一个在应用程序其他地方使用的承载身份验证令牌。该认证令牌在一段时间后过期。就在过期之前，应用程序在终端/refresh/tokenlogin中向后端服务器发送了一个请求，该请求在标头和HTTP主体部分的用户名参数中包含有效的身份验证令牌。

进一步的测试表明，删除请求上的Authorization标头并更改HTTP主体上的用户名参数将为提供的用户名创建一个新的有效令牌。利用此漏洞，拥有匿名配置文件的攻击者可以通过提供用户名为任何用户生成身份验证令牌。

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537242931169.png "1664537070111825.png")

**技术2 ——SSO配置不正确**

大多数应用程序都使用SSO系统，因为与处理许多身份验证门户相比，SSO系统更容易安全管理。但是简单地使用SSO并不能自动保护系统，因为SSO的配置也应得到保护。

现在，一个应用程序使用Microsoft SSO系统进行身份验证。当访问internal.redacted.com URL时，web浏览器会重定向到单点登录系统：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537244169612.png "1664537078982554.png")

乍一看，它似乎是安全的，但对后端请求的分析显示，应用程序在重定向响应上返回了异常大的内容长度(超过40000字节)

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537245247644.png "1664537087911402.png")

为什么应用程序要这样做呢？当然是配置错误。在将用户发送到SSO的重定向时，应用程序向每个请求泄露了其内部响应。因此，可以篡改响应，将302 Found头更改为200 OK，并删除整个Location标头，从而获得对整个应用程序的访问。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537246136481.png "1664537096208754.png")

此外，可以通过在Burp Suite中添加Match & Replace规则来自动删除标题并自动更改值，从而实现这个过程的自动化。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537246122742.png "1664537105899430.png")

**技术3——基于CMS的访问漏洞**

内容管理系统(CMS)，如WordPress、Drupal和Hubspot也需要进行安全配置，以免它们在使用中中引入漏洞。

在发现的一个示例中，在一个内部应用程序中使用了一个流行的CMS平台Liferay。该应用程序只有一个不需要身份验证就可以访问的登录页面，所有其他页面都在应用程序UI中受到限制。

对于那些不熟悉Liferay的人来说，CMS为应用程序工作流使用了portlet，它的参数是数字中的p\_p\_id。对于该应用程序，可以通过将参数值更改为58来访问登录portlet。在正常的登录页面中，只有登录表单是可访问的。然而，通过直接访问portlet，可以达到Create Account功能，然后在不需要适当的授权情况下就可以进行自注册并访问内部应用程序。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537247711241.png "1664537115139945.png")

请注意，虽然Liferay以前使用过这个工作流，但它的最新版本使用了portlet名称而不是数字ID。不过，也可以通过更改名称来访问其他portlet。

**技术4 ——JWT令牌的使用**

JWT令牌或JSON web令牌，在新的web应用程序中很流行。但是，虽然它们默认具有安全机制，但后端服务器配置也应该是安全的。

我的一项任务是在他们的内部应用程序中使用SSO身份验证。当直接访问时，应用程序将用户重定向到Microsoft SSO web页面。到目前为止，一切顺利。

然而，一些JS文件不需要身份验证就可以访问。测试显示，该应用程序使用了安全登录后通过Microsoft SSO系统发送的JWT令牌。在后端机制上，存在一个安全错误配置，即不检查是否为特定的应用程序生成了JWT令牌。相反，它接受任何具有有效签名的JWT令牌。因此，使用来自微软网站的JWT令牌示例如下：

![7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537248567392.jpeg "1664537125134906.jpeg")

在通用值内：

![8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537249121114.jpeg "1664537135210830.jpeg")

有可能访问内部终端，泄露公司数据。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537250198907.png "1664537146458603.png")

**技术5——将身份验证类型更改为Null**

在此情况中，应用程序通过 base64 编码的 XML 请求向 HTTP 发布数据上发送所有请求。在登录机制上，它将用户名作为参数别名发送，将密码作为scode发送。scode 参数内的值已进行哈希处理。分析显示，它使用了所提供密码值的 md5 值。请求中还有另一个有趣的标志：scode 有一个属性，其类型值为 2。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537250116949.png "1664537163194419.png")

我尝试将该值赋值为1，它将接受明文密码。成功了！因此，在明文值中使用暴力攻击中是可能的。没什么大不了的，但这标志着我走对了路。把它赋值给空值怎么样？或者其他值，如-1、0或9999999999？大多数都返回了除0之外的错误代码。我用属性0做了几次尝试，但没有成功，直到我将密码值作为空值发送出去。

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220930/1664537252160578.png "1664537173187299.png")

我意识到只需提供用户名和密码即可访问任何帐户。事实证明，这是一个很大的错误。

**总结**

复杂的身份验证机制可能成为攻击者使用的最具隐蔽性的攻击手段，特别是在容易出现业务逻辑漏洞的应用程序上。因为自动扫描器大多无法进入这类漏洞，所以仍然需要手工来找到它们。鉴于现代软件环境的复杂性，没有任何一个安全研究人员能够发现所有可能的漏洞或攻击载体。

本文翻译自：https://www.synack.com/blog/exploits-explained-5-unusual-authentication-bypass-techniques/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?j2QlUGbl)

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

![](https://img.4hou.com/FpAB1n2wt6I0zw18n_Sz-3Nj9Ctg)

# [gejigeji](https://www.4hou.com/member/mqy0)

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

[查看更多](https://www.4hou.com/member/mqy0)

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