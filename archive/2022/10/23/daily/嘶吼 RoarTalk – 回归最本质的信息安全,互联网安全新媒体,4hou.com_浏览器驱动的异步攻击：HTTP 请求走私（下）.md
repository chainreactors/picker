---
title: 浏览器驱动的异步攻击：HTTP 请求走私（下）
url: https://www.4hou.com/posts/KE7R
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-23
fetch_date: 2025-10-03T20:40:24.417976
---

# 浏览器驱动的异步攻击：HTTP 请求走私（下）

浏览器驱动的异步攻击：HTTP 请求走私（下） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 浏览器驱动的异步攻击：HTTP 请求走私（下）

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-10-22 11:44:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)129735

收藏

导语：HTTP/1.1 的明文性质使它看起来很简单，并使开发人员实现自己的服务器。

![60a7-article-browser-powered_desync_attacks_article.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320699913343.jpeg "1661753402183753.jpeg")

[浏览器驱动的异步攻击：HTTP 请求走私（上）](https://www.4hou.com/posts/JXK2 "https://www.4hou.com/posts/JXK2")

**示例探究**

通过自动检测 CSD 漏洞，我确定了一系列真正的易受攻击的网站。在这一节中，我将研究其中四个更有趣的方法，并看看这种方法是如何发挥作用的。

**Akamai——堆栈****化HEAD**

在第一个案例中，我们将利用一个简单的漏洞影响许多基于 Akamai 构建的网站。作为示例目标，我将使用 www.capitalone.ca。

当 Akamai 发出重定向时，它会忽略请求的 Content-Length 标头，并将任何消息正文留在 TCP/TLS 套接字上。 Capitalone.ca 使用 Akamai 将对 /assets 的请求重定向到 /assets/，因此我们可以通过向该端点发出 POST 请求来触发 CSD：

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320699113486.png "1661753455118634.png")

为了构建一个漏洞利用，我们将使用 HEAD 方法将一组 HTTP 标头与 text/html 的 Content-Type 和一个由反映 Location 标头中的查询字符串的标头组成的'body'组合起来：

![27.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320700143120.png "1661753465157436.png")

如果这是服务器端异步攻击，我们可以在就此打住。然而，要想成功实现客户端异步，我们需要解决两个复杂问题。

第一个问题是初始重定向响应。为了执行注入的JavaScript，我们需要受害者的浏览器将响应呈现为 HTML，但是 301 重定向会被浏览器自动跟踪，从而阻止攻击。一个简单的解决方案是指定模式：'cors'，它会故意触发 CORS 漏洞。这可以防止浏览器跟随重定向并使我们能够通过调用 catch() 而不是 then() 来恢复攻击序列。在 catch block中，我们将使用 location = 'https://www.capitalone.ca/' 触发浏览器导航。我们可能倾向于使用iframe来进行导航，但可以使用跨网站攻击缓解措施，例如同网站 cookie。

第二个复杂的问题是所谓的“堆栈响应问题”。浏览器有一种机制，如果接收到的响应数据多于预期，则删除连接。这极大地影响了对多个响应进行排队的技术的可靠性，例如我们在这里使用的HEAD方法。为了解决这个问题，我们需要延迟对 HEAD 请求的 404 响应。幸运的是，在这个目标上，我们可以很容易地实现这一点，方法是添加一个具有随机值的参数来充当缓存攻击器，触发缓存未命中并产生约 500 毫秒的延迟。利用结果如下所示：

![28.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320700155845.png "1661753485153139.png")

已向 Akamai 报告了此漏洞，但我不确定何时修复。

**Cisco Web VPN——客户端缓存攻击**

我们的下一个目标是 Cisco ASA WebVPN，它可以忽略几乎所有端点上的 Content-Length，因此我们只需向主页发出 POST 请求即可触发异步。为了利用它，我们将使用 Host-header 重定向小工具：

![29.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320700139484.png "1661753495137500.png")

最简单的攻击是使用此重定向感染套接字，将受害者导航到 /+CSCOE+/logon.html，并希望浏览器尝试使用感染的套接字导入/+CSCOE+/win.js，然后被重定向，最终从我们的网站导入恶意 JS。不幸的是，这是非常不可靠的，因为浏览器很可能会使用被感染的套接字进行初始导航。为了避免这个问题，我们将执行客户端缓存攻击。

首先，我们使用重定向感染套接字，然后将浏览器直接导航到 /+CSCOE+/win.js：

![30.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320700807186.png "1661753504273276.png")

请注意，此顶级导航对于绕过缓存分区至关重要 - 尝试使用 fetch() 将攻击漏洞的缓存。

浏览器将使用被感染的套接字，接收恶意重定向，并将其保存在本地缓存中以供 https:/redacted/+CSCOE+/win.js 使用。然后，它将遵循重定向并返回我们的网站 https://psres.net/+webvpn+/index.html。我们将浏览器重定向到登录页面 https://redacted/+CSCOE+/logon.html，当浏览器开始出现登录页面时，它会尝试导入 /+CSCOE+/win.js 并发现它已经将其保存在其缓存中。资源加载将遵循缓存的重定向并向 https://psres.net/+webvpn+/index.html 发出第二个请求。此时，我们的服务器可以使用一些恶意 JavaScript 进行响应，这些 JavaScript 将在目标网站的上下文中执行。

为了使这种攻击起作用，攻击者的网站需要在同一端点上同时提供重定向和恶意 JS。我采取了一种懒惰的方法，并使用 JS/HTML 多语言解决了这个问题——Chrome 似乎并不介意不正确的 Content-Type：

![31.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320701184309.png "1661753522180709.png")

我在 2021 年 11 月 10 日向思科报告了这个问题，他们最终在 2022 年 3 月 2 日宣布弃用该产品，他们不会修复它，但仍会为其标记为 CVE-2022-20713。

**Verisign——碎片化的chunk**

在寻找不同步矢量时，最好不要超出探测有效端点的范围，而是鼓励服务器使用不同寻常的代码路径。在尝试使用像 /..%2f 这样的半格式漏洞的 URL 时，我发现我可以通过 POST 到 /%2f 来触发 verisign.com 上的 CSD。

我最初尝试使用基于 HEAD 的方法，类似于之前在 Akamai 上使用的方法。不幸的是，这种方法依赖于基于 Content-Length 的响应，并且服务器向所有没有正文的请求发送分块响应。此外，它拒绝了包含 Content-Length 的 HEAD 请求。最终，经过测试，我发现服务器会对 HEAD 请求发出基于 CL 的响应，前提是它们使用了 Transfer-Encoding: chunked。

这在服务器端异步中几乎没有用，但是由于受害者的浏览器在我的控制之下，我可以准确地预测下一个请求的大小，并在单个 chunk中使用它：

![32.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320701901048.png "1661753535132874.png")

此攻击是使用以下 JavaScript 触发的：

![33.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320702533843.png "1661753587519862.png")

此漏洞于 2022 年 7 月 21 日被成功修复。

**Pulse Secure VPN**

Pulse Secure VPN会忽略对静态文件（如 /robots.txt）的 POST 请求的Content-Length。就像 Cisco Web VPN 一样，这个目标有一个主机标头重定向小工具，我将使用它来劫持 JavaScript 导入。但是，这次的重定向是不可缓存的。因此客户端缓存攻击是不可用的。

由于我们的目标是资源负载并且没有攻击客户端缓存的预期，因此攻击时机至关重要。我们需要受害者的浏览器成功加载目标网站上的页面，然后使用攻击连接加载 JavaScript 子资源。

固有的竞争条件使这种攻击不可靠，所以如果我们只有一次尝试，它注定会失败——我们需要设计一个环境，可以进行多次尝试。为了实现这一点，我将创建一个单独的窗口，并在攻击者页面上保留一个句柄。

在大多数目标页面上，如果试图劫持JS导入失败，将导致浏览器缓存真正的JavaScript文件，在缓存的JS过期之前，该页面不会受到此类攻击。我能够通过定位 /dana-na/meeting/meeting\_testjs.cgi来避免这个问题，它从/dana-na/meeting/url\_meeting/appletRedirect.js加载JavaScript，这实际上并不存在，所以它返回一个404，并没有保存在浏览器的缓存中。我还用一个冗长的标头填充了注入的请求，以缓解堆栈响应漏洞。

这导致以下攻击流程：

1.打开一个新窗口。

2.向目标发出无害的请求以建立新的连接，从而使计时更加一致。

3.将窗口导航到位于 /meeting\_testjs.cgi 的目标页面。

4.120 毫秒后，使用重定向小工具创建三个攻击连接。

5.5 毫秒后，在渲染 /meeting\_testjs.cgi 时，受害者可能会尝试导入 /appletRedirect.js 并被重定向到提供恶意JS的x.psres.net。

6.如果没有，请重试攻击。

最终的攻击脚本如下：

![34.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320702862521.png "1661753599183313.png")

**基于暂停的异步**

如上所述，在 HTTP 请求中间暂停并观察服务器的反应可以揭示通过篡改请求的实际内容无法获得的有用信息。事实证明，暂停还可以通过触发漏洞的请求超时实现来创建新的异步漏洞。

这个漏洞类是不可见的，除非你的工具有比目标服务器更高的超时时间。我非常幸运地发现了它，因为我的工具应该有2秒的超时，但由于一个漏洞，它恢复到10秒的超时。我的管道还碰巧包含一个运行Varnish的单独网站，该网站配置了自定义的 5 秒超时。

**Varnish**

Varnish 缓存有一个称为 synth() 的特性，它可以让你在不将请求转发到后端的情况下发出响应。下面是一个用来阻止访问文件夹的规则示例：

![36.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320703203183.png "1661753611465067.png")

当处理匹配synth规则的部分请求时，如果Varnish在15秒内没有收到数据，它将超时。当这种情况发生时，即使它只从套接字读取了一半的请求，它也会让连接保持打开状态以便重用。这意味着，如果客户机继续处理HTTP请求的后半部分，它将被解释为一个新的请求。

要在易受攻击的前端触发基于暂停的异步，首先发送你的标头，承诺正文，然后等待。最终你会收到一个响应，当你最终发送你的请求正文时，它会被解释为一个新的请求：

![37.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320703199130.png "1661753641184055.png")

**Apache**

在这个发现之后，我碰到了 Turbo Intruder 的请求超时，发现同样的技术也适用于 Apache。与Varnish一样，它在服务器自己生成响应而不是让应用程序处理请求的端点上很容易受到攻击。发生这种情况的一种方法是使用服务器级重定向：

![38.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320703750476.png "1661753655941077.png")

如果你发现一个服务器容易受到基于暂停的异步的影响，你有两个利用它的选项，具体取决于它是前端还是后端。

**服务器端**

如果易受攻击的服务器在后端运行，你可能会触发服务器端异步。为此，你需要一个将请求流传输到后端的前端。特别是，它需要在不缓冲整个请求正文的情况下以HTTP 标头转发。

![39.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320704123019.png "1661753665104013.png")

这里有一个小问题。前端不会读取超时响应并将其传递给我们，直到看到我们发送完整的请求。因此，我们需要发送我们的标头，暂停一段时间，然后在没有提示的情况下继续其余的攻击序列。我不知道有任何安全测试工具支持像这样部分延迟请求，所以我在 Turbo Intruder 中实现了支持。队列接口现在有三个新参数：

pause before指定一个Turbo应该暂停的偏移量。

pauseMarker 是一种替代方案，它采用 Turbo 在发出后应暂停的字符串列表。

pauseTime 指定暂停多长时间，以微秒为单位；

那么，哪些前端实际上具有这种请求流？一个著名的前端是 Amazon 的 Application Load Balancer (ALB)，但还有一个额外的障碍。如果 ALB 收到对部分请求的响应，它将拒绝重用连接。

![40.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221021/1666320704580430.png "1661753691613984.png")

幸运的是，这种机制中有一个固有的竞争条件。你可以...