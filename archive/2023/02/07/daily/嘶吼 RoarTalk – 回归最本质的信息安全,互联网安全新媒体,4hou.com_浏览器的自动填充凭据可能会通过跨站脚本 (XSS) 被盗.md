---
title: 浏览器的自动填充凭据可能会通过跨站脚本 (XSS) 被盗
url: https://www.4hou.com/posts/l665
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-07
fetch_date: 2025-10-04T05:49:24.336569
---

# 浏览器的自动填充凭据可能会通过跨站脚本 (XSS) 被盗

浏览器的自动填充凭据可能会通过跨站脚本 (XSS) 被盗 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 浏览器的自动填充凭据可能会通过跨站脚本 (XSS) 被盗

lucywang
[漏洞](https://www.4hou.com/category/vulnerable)
2023-02-06 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)162998

收藏

导语：跨站脚本 (XSS) 是一个目前很流行的漏洞，它已经存在了很长时间，可用于窃取会话、创建虚假登录和以其他人的身份执行操作等。

跨站脚本 (XSS) 是一个目前很流行的漏洞，它已经存在了很长时间，可用于窃取会话、创建虚假登录和以其他人的身份执行操作等。

此外，许多用户没有意识到与浏览器的凭据自动填充功能相关的潜在危险。这种攻击向量并不新鲜，但很多人都不知道，其潜在的危害非常大。在这篇文章中，GoSecure Titan Labs 团队将演示使用具有自动填充功能的浏览器密码管理器可能会在易受 XSS 攻击的 Web 应用程序中暴露你的凭据。

大多数浏览器都添加了一个通常称为“自动填充”的功能，可以简化 Web 应用程序的登录过程。此功能将自动填写你保存的给定 Web 应用程序的凭据，而无需交互。此功能在大多数常用浏览器（如 Firefox、Chrome、Edge、Opera、Internet Explorer）上默认启用，有时根本无法禁用。这意味着无法阻止凭据自动填充基于 Chromium 的浏览器，例如 Chrome 和 Edge，因为没有禁用它的选项。防止在这些浏览器上自动填充的唯一方法是根本不保存你的凭据。对于那些浏览器来说，这是一种要么全有要么全无的情况。因此，即使你禁用了“保存密码的提议”，但凭据仍会被保存，这些浏览器仍将自动填充。

那攻击者如何通过 XSS 攻击窃取它？当浏览器在任何时候发现一个“密码”类型的输入标签时，它会自动用密码填充它。因此，对于 XSS 攻击，你可以简单地在页面主体的某处添加密码字段，等待浏览器自动填充它，然后获取该字段内的值以将其发送到你的服务器。

当然，上面的技术似乎很容易执行，但操作起来并不那么容易，因为它取决于许多变量，例如受害者是否保存了该来源的凭据、他们使用的浏览器、他们为该来源保存了多少凭据以及是否他们启用了自动填充选项。应该注意的是，如果启用了自动填充功能，密码管理器也可能会受到此攻击向量的影响，而大多数密码管理器默认都没有启用自动填充。

此外，这种攻击向量并不新鲜。目标是让更多人了解这种攻击向量，并帮助人们了解使用自动填充的影响，大多数浏览器默认启用自动填充功能。测试的环境尽可能真实，这意味着它使用 HTTPS 并具有有效证书。

**攻击向量**

现在，让我们来看看通过简单的XSS攻击窃取凭据是多么容易。首先，当你在页面中的任何位置（仅使用一组凭据）添加类型等于“password”的输入字段时，Firefox 的反应如下：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137581443622.png "1661137581443622.png")

现在考虑到受害者在 Firefox 上拥有一组给定来源的凭据，让我们创建一个有效负载来提取密码。

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137589199210.png "1661137589199210.png")

在行动中：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137597428019.png "1661137597428019.png")

可以看到，同样的漏洞利用有两组凭据：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137605119756.png "1661137605119756.png")

因此，在 Firefox 上使用两组凭据时，它不会自动填充任何凭据。Chrome浏览器呢？

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137614326834.png "1661137614326834.png")

![5.2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137659114944.png "1661137659114944.png")

如果 Chrome 之前存在用户名字段，Chrome 似乎只会填写密码字段，正如你在上图中看到的那样，它没有填写密码字段。请注意，浏览器 Edge 和 Opera 的反应方式与 Chrome 相同。

现在，让我们尝试使用与 Firefox 相同的有效负载来提取凭据。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137741164883.png "1661137741164883.png")

如你所见，无法访问凭据，这很奇怪。经过一番研究，我们偶然发现了一篇博文，简而言之，它解释说 Chrome 需要在窗口中进行任何交互才能粘贴值。这意味着，对于Chrome和其他基于相同引擎的浏览器来说，它需要像点击或按键（key press）这样的交互。因此，有效负载需要适应使用某种用户交互，而不是使用超时。为简单起见，让我们使用 body 上的“on-click”事件，这样每当受害者点击页面以跟随链接或专注于某事时，有效负载就会执行。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137750180313.png "1661137750180313.png")

这种方法行之有效。点击页面后，执行有效负载，并将凭据发送到恶意服务器。就像Firefox一样，在 Chrome 中拥有多组凭据的行为是什么？

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137758108323.png "1661137758108323.png")

Chrome 将字段设置为最后使用的一组凭据。但是是否有可能获得其他凭据集？使用多组 Firefox 获取一组凭据怎么样？它会自动填充与上一个字段中的用户名匹配的密码吗？让我们在 Firefox 上尝试一下：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137769124763.png "1661137769124763.png")

它会像我们预期的那样自动填充。Chrome浏览器呢？它的表现也是一样的吗？

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137778124445.png "1661137778124445.png")

它也自动填充。这意味着，如果用户名匹配，则可以枚举所有保存的凭据。

**不同浏览器之间的区别**

每个浏览器都是不同的，因为它们要么不是基于相同的引擎，要么在引擎之外提供了额外的安全特性，以防止证书的自动填充。Brave是基于Chromium的浏览器的一个例子，但它不自动填充凭据。

下面的一组图表将通过分析帮助你更好地了解浏览器安全性和自动填充功能。

**Firefox**

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137787699113.png "1661137787699113.png")

Firefox 的优点在于你可以禁用自动填充选项并仍然使用密码管理器功能。禁用后，它需要交互以显示包含该来源的匹配凭据集的弹出窗口。但是，默认情况下启用此选项。需要注意的是，Tor 浏览器也基于与 Firefox 相同的引擎，但默认情况下不要求保存密码，并且默认情况下也不自动填充。另外，手机上的 Tor 浏览器默认有“要求保存密码”和自动填充功能。然而，根据我们的研究和测试，它不再起作用了，因为 Tor 总是打开一个私人标签，因此不会保留任何信息，也不会要求保存密码。此外，Tor 浏览器具有额外的保护，除非允许，否则会阻止脚本。

**基于 Chromium 的浏览器（Chrome、Edge、Opera）**

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137796151065.png "1661137796151065.png")

只有 Chrome、Edge 和 Opera 进行了彻底的测试，但还有其他基于相同引擎的浏览器没有经过测试，因为它们没有被广泛使用。在这些浏览器中，没有禁用自动填充的选项，即使“提供保存密码”功能被禁用，如果为该来源保存了一组匹配的凭据，它将自动填充。有趣的是，移动版 Chrome 和 Edge 浏览器的反应方式与桌面版不同。移动版本根本不自动填充，它们需要交互来显示包含该来源的匹配凭据集的弹出窗口。

**Brave**

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137804157422.png "1661137804157422.png")

Brave 也基于 Chromium，但其运行方式与其他产品不同。无论如何，它都不会自动填充，这阻止了用于凭据泄露的XSS攻击向量。相反，它需要交互来显示包含该来源的匹配凭据集的弹出窗口。

**Internet Explorer（简称：IE）**

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137813189971.png "1661137813189971.png")

Internet Explorer（简称：IE）是微软公司推出的一款网页浏览器。原称Microsoft Internet Explorer（6版本以前）和Windows Internet Explorer（7、8、9、10、11版本）。

无论如何，Internet Explorer 似乎比大多数基于 Chromium 的浏览器更安全，因为它有一个选项，可以禁用证书的自动填充。但是，如果你禁用该选项，你将无法再使用“保存凭据”功能。该选项默认启用。

**Safari**

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220822/1661137821170381.png "1661137821170381.png")

Safari 确实有禁用自动填充的选项，但它不会自动填充。它需要交互来显示包含该来源的匹配凭据集的弹出窗口。

**缓解措施**

**对于 Web 开发人员**

这个问题没有真正的彻底解决方案，但是你可以采取一些措施来帮助缓解跨站脚本 (XSS)漏洞。首先，拥有一个好的内容安全策略 (CSP) 标头将极大地帮助防止恶意脚本被执行，从而使 XSS 攻击更难被利用。也就是说，请记住，CSP 配置仅有助于防止 XSS 攻击，并且有许多已知的绕过方式取决于配置。其次，确保页面中反映的数据经过 HTML 编码、验证或清理。

**对于安全管理员**

一种解决方案是通过组策略对象 (GPO) 或端点管理器禁用浏览器密码保存。这将阻止用户使用浏览器密码管理器功能保存他们的凭据。但是，之前添加的每个密码仍将根据浏览器以及是否仍启用该功能而自动填写。

**对于用户**

对于想要使用密码管理器的终端用户，有两种可行的解决方案，这对于不断扩展的网站和应该唯一的密码很有用。第一个也是最好的解决方案是使用真正的密码管理器，例如 KeePass 或类似的商业解决方案，例如 1Password 或 Bitwarden，它们是著名的、经过测试的并且默认情况下没有自动填充功能。确保你的密码管理器不会自动填写凭据，这样就不会在没有交互的情况下被 XSS 攻击自动获取。第二种解决方案是使用默认情况下不自动填充或允许你禁用已保存密码的自动填充的浏览器。

**总结**

这种攻击方式并不新鲜，但是看看有多少常用的浏览器在默认情况下容易受到攻击是很有趣的。希望这将提高对这个漏洞的认识，并帮助非技术用户改用更好的解决方案，比如密码管理器或更灵活、安全意识更强、用户友好的浏览器。

本文翻译自：https://www.gosecure.net/blog/2022/06/29/did-you-know-your-browsers-autofill-credentials-could-be-stolen-via-cross-site-scripting-xss/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?knGdmGFi)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/uploads/20171229/1514527090244385.gif)

# [lucywang](https://www.4hou.com/mem...