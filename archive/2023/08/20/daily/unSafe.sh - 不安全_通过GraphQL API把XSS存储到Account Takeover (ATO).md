---
title: 通过GraphQL API把XSS存储到Account Takeover (ATO)
url: https://buaq.net/go-174815.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:51.717010
---

# 通过GraphQL API把XSS存储到Account Takeover (ATO)

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/26ad446c0acb5aaa52d379e98ad62135.jpg)

通过GraphQL API把XSS存储到Account Takeover (ATO)

导语：去年年底，研究人员在HackerOne上发现了一个极具挑战性的漏洞，该漏洞涉及多个层面的利用，最终导致存储的XSS有效负载能够接管受害者的帐户，该漏洞的危害性极强（CVSS 8.7）。
*2023-8-19 11:10:0
Author: [www.4hou.com(查看原文)](/jump-174815.htm)
阅读量:45
收藏*

---

导语：去年年底，研究人员在HackerOne上发现了一个极具挑战性的漏洞，该漏洞涉及多个层面的利用，最终导致存储的XSS有效负载能够接管受害者的帐户，该漏洞的危害性极强（CVSS 8.7）。

去年年底，研究人员在HackerOne上发现了一个极具挑战性的漏洞，该漏洞涉及多个层面的利用，最终导致存储的XSS有效负载能够接管受害者的帐户，该漏洞的危害性极强（CVSS 8.7）。HackerOne 是排名第一的黑客驱动安全平台，可帮助你在被利用之前发现并修复关键漏洞，HackerOne 正在阻止他们提取漏洞赏金，甚至有人被截留了数千美元。

**设置过程**

我发现最初的漏洞与HackerOne的支付处理API有关，客户（商家）使用它来处理不同国家的信用卡和金融交易。这个品牌是跨国的，所以他们在许多不同的国家处理许多不同类型的交易。该支付处理器支持的一种交易类型是离线支付流，用于处理信用卡不流行、现金交易更普遍的地区。在这些地方，支付处理器允许客户进行电子商务购买，并获得一个唯一的代码（如二维码），他们可以将其带入商店并为交易支付现金。一旦商店确认交易，电子商务商家就会收到货款，顾客就会收到货物。

具体流程是这样的：

**·**当客户下订单时，电子商务商家启动离线支付流程；

**·**电子商务商家为客户提供一个可用于支付的唯一店内代码；

**·**（离线）客户将代码带到支付网络中的商店并用现金支付；

**·**电子商务商家收到付款通知；

**·**电子商务商家向客户发送一个唯一的URL，他们可以访问该URL来确认购买。

**·** 请注意，最后一步中的“唯一URL”是由商家在交易设置时提供的，你可以将其视为传统在线信用卡工作流中的“确认URL”。

**有效负载**

在这种情况下，攻击者是有能力创建这些离线交易的商家（或该商家的用户）。商家将提交一个包含XSS有效负载的确认URL。这种有效负载一旦持久化，就可以在主网站（www.redated.com）的页面下看到。

商家通过GraphQL API在不同的域名payments.redactedtwo.com上提交请求，该域名的有效负载如下：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342845957208.png "1691346078951142.png")

我们可以看到，这个GraphQL API接受一个returnUrl参数，该参数将成为我们的有效负载源。请注意，GraphQL调用是一个完全独立的顶级域上的API。这很有趣，因为它允许在一个域中存储的有效负载会在另一个更关键的域中呈现。提交后，我们可以访问www.redected.com网站上的一个唯一的静态URL，该URL在returnUrl参数中包含我们的有效负载。

让我们看看负载是如何出现在www.redacted.com上的：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342846790718.png "1691346109205670.png")

我们看到这个脚本有一个nonce，注入点 < payload > 在脚本中看起来像是一个非常容易存储的XSS。

nonce的存在将变得很重要，让我们看一下Content-Security-Policy标头。为了便于阅读，我将它分成几行：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342846958328.png "1691346123342783.png")

我们可以看到，这个CSP是相当严格的，我们只能从网站本身获取信息，并且页面上的任何脚本标签都需要nonce。

**尝试1：javascript:// url**

显然，在位置.href=处使用注入点的第一次尝试是简单地放置一个带有有效负载的Javascript方案，例如Javascript://alert(1) 。我很幸运，因为这里没有明显的WAF阻挡像这样简单的有效负载。不过尝试失败了，GraphQL API拒绝了该URL，出现的错误为400。我尝试了很多其他的尝试，比如编码等都不行。API正在验证提供的URL是否以https://开头，并包含后跟/的完整主机名。所以很明显，我们有一个开放的重定向，但我知道这可能被用于存储的XSS。

例如https://hackerone.com/将导致以下存储的有效负载：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342847638894.png "1691346160803797.png")

这些是附加到GraphQL API中提供的URL的参数，代表唯一的事务ID，关于客户的信息等-这总是附加一个前导?在单引号内。

出于显而易见的原因，我尝试提交各种形式的不带尾斜杠的https:// URL，这将导致主机名之后的所有内容都被URL编码，并且通常对Javascript上下文中的XSS无用。

**尝试2：附加有效负载**

现在，我们知道负载必须以有效的URL和主机名开始，因此我们以https://hackerone.com/作为负载的开头。

幸运的是，我能想到的下一个最明显的有效负载奏效了。单引号字符没有以任何方式被阻止或编码，因此以下负载实际上生成了一个存储的警报：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342848396410.png "1691346178799140.png")

这生成了一个警报，但当关闭时，用户会立即重定向到提供的URL。已存储带有DOM访问的XSS负载！

**提交**

此时，尝试已经成功，研究人员已向LHE提交了该漏洞。不过该团队回应说，他们觉得CSP和cookie设置在主站点上，不可能将存储的XSS升级到高严重性漏洞。

研究人员觉得不合理，因为有效负载位于< script nonce >环境中，攻击者可以生成想要的任何有效负载，利用它将很容易！

**构建ATO有效负载**

研究人员制作了想象到的最好的存储XSS ATO有效负载。有效负载执行了以下任务，他们在主站点上打开的窗口的开发控制台（F12）中测试了这些任务：

通过对站点主页执行XMLHttpRequest，为用户获取CSRF令牌；

通过解析从fetch调用返回的HTML提取CSRF令牌；

使用XMLHttpRequest进行API调用以更改帐户上的电子邮件地址；

请注意，CSP中的connect-src使你无法尝试使用Javascript将页面中的信息泄露到攻击者域，因此ATO或CSRF的类似行为是我在此处选择的有效负载。

此时，攻击者可以控制电子邮件地址并使用“忘记密码”功能来完成接管，从而获取该帐户。Cookie（甚至是HttpOnly）将在最后一次请求时发送，因为同源策略将允许包含它们（XHR来源于正确的域，www.redated.com）。

大多数人都熟悉编写这种类型的有效负载，我不会在这里详细介绍，因为它非常简单：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342849106586.png)

我在Chrome开发控制台中测试了这一点，并确认它具有ATO的预期效果。

**尝试3：拒绝**

我向GraphQL API提交了有效负载，它看起来很好！一开始没有错误，但后来我点击了存储的XSS页面本身，看到存储的有效负载未呈现。

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342849429531.png)

回到原来的alert(document.domain)有效负载，它开始运行了。所以，在我完整的ATO有效负载中一定有什么东西导致服务器不渲染XSS。

在对工作负载进行多次迭代之后，不幸的是，由于源和接收是不同的事务，并且需要几个中间步骤，我无法使用任何方便的自动化工具，我发现以下所有字符都会导致400错误：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342850111205.png)

请注意，所有空白字符也被拒绝。可能还有其他我不记得内容了，但以下内容肯定没有被阻止：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342851208506.png)

现在，有一个有限的Javascript词汇表要处理。

**尝试4：异步**

研究人员最终重写了大部分有效负载，以排除受限制的字符。请注意，我尝试了所有类型的编码（URL、javascript、十六进制、八进制、双重编码等），但这些都不能用来绕过限制。该过程是非常乏味的，因为错误出现在接收端，而不是源端，所以每次迭代至少浪费一到两分钟。

我甚至得到了使用受限字符集的初始获取请求，比如：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342851137799.png)

现在，我们可以在控制台日志中看到fetch调用中的Response对象。

请记住，我的攻击链需要3个步骤：

**·**进行XHR调用以获取带有CSRF令牌的页面；

**·**从返回的HTML中提取CSRF令牌；

**·** 用CSRF令牌对ATO进行XHR调用；

由于fetch和XMLHttpRequest是异步API，我们需要用lambda函数填充then方法参数，该函数将在Promise解析时异步执行。问题是，如果没有｛｝>字符，我不相信有一种方法可以在Javascript中构建lambda函数，无论是用大括号语法还是箭头语法。

研究人员立刻意识到这是一个巨大的障碍。即使我重写了负载的其余部分以避免所有这些其他字符，也无法定义Promise解析时要调用的lambda函数。不过在Javascript引用中Function对象的文档中，有一个形式Function(var, body)，其中body是字符串!不需要大括号或箭头语法！

在重写有效负载时，研究人员却发现在CSP中遗漏了一些东西，由于CSP缺少不安全的eval指令，因此不允许使用eval。没错，这种形式的Function构造函数使用eval将字符串转换为实际的Javascript函数。

所以解决问题的方法有以下三种：

**·**要成功传递工作负载，就需要绕过被阻止的特殊字符；

**·**研究人员确信他们可以执行任意的Javascript代码，只要注意使用的字符即可；

**·**可以访问DOM中已经存在的 < script > 标记上的nonce的正确值；

于是研究人员决定尝试以下方法：

**·**使用非常简单的Javascript创建一个新的 < script > DOM节点；

**·**将该脚本节点上的nonce设置为与页面上已存在的 < script > 节点的nonce匹配；

**·**想出一种方法来编码负载，这样就可以将新 < script > 节点的innerText设置为一个没有特殊字符的值；

**·**将新 < script > 标记插入DOM，有效负载将执行。

有趣的是，如果 < script > 标记已经开始执行（页面上的一个标记），那么替换innerText将毫无作用。由于CSP，研究人员看不到除了带有nonce的 < script > 标记之外的任何方法来执行负载。

但是，如果页面尚未完成内联脚本的呈现和执行，则可以在内联脚本之后插入一个新的 < script > 节点，该节点将执行。请注意，这仅在页面尚未加载的情况下有效。如果你试图在onload事件触发后插入一个< script > DOM节点，那就太晚了。

我决定用一个看起来像以下这样的简单有效负载来尝试：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342852878598.png)

尝试成功了！警报弹出，并且新标记上的nonce的存在允许我的脚本通过CSP检查。

**尝试5：回避特殊字符**

如果试图只对那些被阻止的字符进行编码，则很难手动完成。因此，研究人员决定采取以下方法：

**·**用Javascript有效负载创建一个文件redacted\_payload.txt；

**·**运行以下shell命令，将文件中的每个字符编码为对String.fromCharCode的一系列调用；

生成的shell命令：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342853194068.png)

输出：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342854119660.png)

研究人员在花费了大量时间后，最终得到了一个非常大的负载，幸运的是，可以存储的URL没有长度限制！

研究人员提交了完整的有效负载，如下所示：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342854142660.png)

但没有成功，这让研究人员想起了一些原来被忽略的事情。

**最后一步：重定向**

注意，我们正在注入的内联脚本是通过设置location.href属性重定向窗口开始的。这会导致浏览器开始导航，此时，它可能不会完成任何进一步的内联脚本的执行，而且它肯定不会等待异步Promise完成，例如XHR或fetch。可以看到的是，编码负载正在运行，但浏览器会立即导航离开页面，整个过程没有机会完成。

还要记住，重定向必须以合法的主机名开始，因此不可能提供浏览器无法导航到的无效重定向。

为了防止系统升级造成的影响，研究人员控制了关于location.href在设置时的行为的Javascript参考，这样研究人员就看到了window.stop()，它被记录为“aborts browser naviagtion（中止浏览器导航）”。这看起来像尝试成功了，所以在URL字符串结束后研究人员立即添加了一个调用，如下所示：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342855209167.png)

这已经达到了阻止重定向的预期效果！

不过，这也停止了任何未完成的获取或XHR请求，且恢复方法很复杂。

为了解决这个问题，研究人员想知道是否再次将location.href设置为其他内容，如果速度足够快，第二个赋值是否会覆盖第一个导航。起初，研究人员尝试使用javascript:URL（这太容易了），最终发现URL foo://a会使浏览器的行为与预期的完全一样：

停止导航到合法URL；

生成错误；

允许继续执行进一步的XHR/fetch请求；

最后的有效负载如下所示：

![通过GraphQL API把XSS存储到Account Takeover (ATO)](https://img.4hou.com/uploads/ueditor/php/upload/image/20230818/1692342856210146.png)

最终，研究人员向ATO提交了有效负载以及成功存储XSS的证据。

**结论**

在所有保护措施到位的情况下，实现这种升级简直不可思议。

本文所用的技巧如下：

当开箱即用的有效负载不起作用时，熟悉Javascript语言和语法会...