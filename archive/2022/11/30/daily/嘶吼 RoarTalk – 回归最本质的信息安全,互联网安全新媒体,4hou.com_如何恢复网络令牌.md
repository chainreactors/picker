---
title: 如何恢复网络令牌
url: https://www.4hou.com/posts/QL8M
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-11-30
fetch_date: 2025-10-04T00:03:11.474336
---

# 如何恢复网络令牌

如何恢复网络令牌 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 如何恢复网络令牌

luochicun
[技术](https://www.4hou.com/category/technology)
2022-11-29 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115340

收藏

导语：在这篇文章中，我将介绍我在逆转Office的身份验证机制时发现的两个问题，并提供一些不需要删除内存的POC工具来帮助恢复存储的令牌。

在这篇文章中，我将介绍我在逆转Office的身份验证机制时发现的两个问题，并提供一些不需要删除内存的POC工具来帮助恢复存储的令牌。

**微软账户服务**

我必须承认，当我第一次开始研究这个问题时，删除我正在运行的Word进程的内存并没有发现文档签名eyJ0eX。这是当前工具用来识别活动令牌的主要方法，我在Windows登录时使用Microsoft 365帐户。

事实证明，Microsoft Account (MSA)的身份验证令牌处理方式与通常的Azure AD SSO帐户不同。

让我们从查看经过MSA验证的Office会话开始，启动Microsoft Office并查看加载的DLL。其中最突出的是MicrosoftAccountWAMExtension.dll。将这个DLL加载到Ghidra中，我们可以开始寻找为MSA帐户生成身份验证令牌的原因。

如果我们在这个DLL中寻找RPC调用，就可以看到一堆被定向到名为wlidsvc的服务：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580744686741.png "1666580744686741.png")

不幸的是，微软并没有为RPC调用此服务提供IDL(或者根本没有提供很多信息)，所以我们将不得不做一些逆向工程来解决这个问题。

让我们将WinDBG附加到wlidsc并监视正在进行的RPC调用。在任何Office进程中进行身份验证之后，我们看到第一个调用是RPC方法WLIDCCreateContext以创建上下文，然后是WLIDCAcquireTokensWithNGC，最后是一系列其他调用，我们将暂时忽略这些调用。

如果我们在后一种方法中添加一个断点，那登录到Office中的MSA帐户会导致命中：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580753136486.png "1666580753136486.png")

步进式（Stepping ）直到我们点击ret并检查填充的参数，在参数12的内存区域中会显示一些有趣的东西。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580764819441.png "1666580764819441.png")

对我来说，这确实是一个象征！如果我们打开像Fiddler这样的代理，我们会看到它与Office访问web服务时使用的身份验证令牌格式相匹配：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580773196818.png "1666580773196818.png")

那么，我们如何从我们自己的工具中调用它呢？让我们使用James Forshaw的NtObjectManager生成一个可以使用的存根。

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580784177804.png "1666580784177804.png")

生成的RPC存根根据Windows版本的不同而不同，这是毫无价值的，例如，在Windows 10中，我们发现字段计数在输入结构上发生了变化，因此，如果你收到可怕的(0x800706F7) - The stub received bad data. 错误，请多家留意。

使用RPC客户端存根创建一个快速的C#应用程序，我们将重播我们之前观察到的入站RPC调用，并添加参数，这将给我们提供如下内容：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580794387400.png "1666580794387400.png")

如果我们称之为：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580803176077.png "1666580803176077.png")

由于这是MSA身份验证请求，我们将不得不使用Substrate等服务来访问Microsoft 365服务。旋转一个代理并在Office中导航是确定调用什么以及这些web服务采用什么参数的最佳方式。但你可以看到，passport令牌返回后，我们可以很好地进行身份验证和交互：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580813983441.png "1666580813983441.png")

**令牌缓存**

现在我们已经了解了如何恢复MSA，那么Azure AD呢？通过Lee Christensen的帖子知道，我们可以很容易地按需请求新令牌，但是我们在Office进程中看到的缓存令牌被转储了，它们是如何在启动时加载的呢？

让我们提供一个新的主机并将我们的用户帐户与AzureAD相关联，然后登录到Office，再尝试找出令牌存储的位置。

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580823126312.png "1666580823126312.png")

为了确保我们在正确的轨道上，让我们从内存中转储一些字符串，并确保eyJ0eX签名存在。

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580832732714.png "1666580832732714.png")

我们再次深入搜索dll，但这次我们将重点关注Windows.Security.Authentication.Web.Core.dll。

这是一个WinRT库，因此我们需要深入Ghidra了解正在发生的事情。

AddWebTokenResponseToCache方法如下：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580844335106.png "1666580844335106.png")

如果我们进一步研究，会发现此方法实际上负责将凭据缓存到序列化文件，这些文件可以在%LOCALAPPDATA%\Microsoft\TokenBroker\Cache中找到。

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580855212001.png "1666580855212001.png")

好的，让我们看看这些TBRES文件：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580865333840.png "1666580865333840.png")

如果我们使用ProcMon，我们会看到这些文件确实在进程启动时被Office访问：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580875845256.png "1666580875845256.png")

可以看到，这就是我们的身份验证信息存储的地方！查看JSON会发现一个IsProtected字段。在WinDBG中，我们将附加到Office，在CryptUnprotectData上添加断点并重新启动。果然，我们发现base64解密数据的内容被解密了。

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580887596920.png "1666580887596920.png")

JSON文件中我们特别感兴趣的字段是ResponseBytes，我添加了一个带有快速工具的repo，该工具可以解密这些文件，可以在这里找到。

在使用ProtectedData.Unprotect解密此数据后，我们看到了明文JWT。果然，解密它们会得到我们之前从内存中看到的相同信息：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221024/1666580896619867.png "1666580896619867.png")

来自不同提供者和应用程序的其他令牌也存储在这些文件中，包括MSA令牌，这也是毫无价值的。

现在我们知道了，Windows和Office用于Live和Azure的认证和缓存会话的几种不同方法。

POC可以在https://github.com/xpn/WAMBam上找到。

本文翻译自：https://blog.xpnsec.com/wam-bam/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6zA2tW97)

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

![](https://img.4hou.com/wp-content/uploads/2017/07/6cfb327dad8fe371f6fa.jpg)

# [luochicun](https://www.4hou.com/member/aOZG)

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

[查看更多](https://www.4hou.com/member/aOZG)

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
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png...