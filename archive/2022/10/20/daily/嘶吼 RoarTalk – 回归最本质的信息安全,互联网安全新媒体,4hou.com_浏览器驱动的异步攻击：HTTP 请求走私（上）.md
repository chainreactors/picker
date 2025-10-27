---
title: 浏览器驱动的异步攻击：HTTP 请求走私（上）
url: https://www.4hou.com/posts/JXK2
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2022-10-20
fetch_date: 2025-10-03T20:20:53.010750
---

# 浏览器驱动的异步攻击：HTTP 请求走私（上）

浏览器驱动的异步攻击：HTTP 请求走私（上） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 浏览器驱动的异步攻击：HTTP 请求走私（上）

xiaohui
[技术](https://www.4hou.com/category/technology)
2022-10-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)186028

收藏

导语：我将在本文介绍如何将受害者的 Web 浏览器变成一个异步的传播平台，通过暴露一个独立的服务器网站和内部网络来转移请求走私的边界。

![60a7-article-browser-powered_desync_attacks_article.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752702199586.jpeg "1661752702199586.jpeg")

我将在本文介绍如何将受害者的 Web 浏览器变成一个异步的传播平台，通过暴露一个独立的服务器网站和内部网络来转移请求走私的边界。你将学习如何将跨域请求与服务器漏洞相结合，以攻击浏览器连接池、安装后门，并释放异步攻击。使用这些技术，我将攻击包括 Apache、Akamai、Varnish、Amazon 和多个 Web VPN 在内的目标。

接下来我将分享一种结合浏览器特点和自定义开源工具的方法。除此之外，我还将介绍一种黑盒分析策略，该策略解决了长期存在的异步障碍，并揭示了一种极其有效的新颖异步触发器。由此产生的后果将包括客户端、服务器端甚至 MITM 攻击。最后，我将介绍修改 HTTPS 以在 Apache 上触发 MITM 驱动的异步。

本文使用的术语“浏览器驱动的异步攻击”表示可以通过 Web 浏览器触发的所有异步攻击。这包括所有客户端异步攻击，以及一些服务器端攻击。

本文的示例都是取材于真实网站。本文中引用的所有漏洞均已报告给相关供应商，并已修补，除非另有说明。

**连接状态攻击**

如果你没有尝试请求走私攻击，很容易忘记 HTTP 连接重用并将 HTTP 请求视为独立对象。毕竟，HTTP 应该是无状态的。然而，下面的层（通常是 TLS）只是一个字节流，很容易找到实现不佳的 HTTP 服务器，假设通过单个连接发送的多个请求必须共享某些属性。

在野外看到的主要漏洞是服务器假设通过给定 TLS 连接发送的每个 HTTP/1.1 请求都必须具有相同的预期目标和 HTTP Host 标头。由于网络浏览器符合这个假设，所以在有人使用 Burp Suite 之前一切都会正常工作。

我发现了两个不同的场景，这个漏洞均造成了很大的安全后果。

**第一个请求验证**

反向代理通常使用 Host 标头来识别将每个请求路由到哪个后端服务器，并有一个允许人们访问的主机白名单：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752837171962.png "1661752837171962.png")

但是，我发现一些代理只对通过给定连接发送的第一个请求应用此白名单。这意味着攻击者可以通过向允许的目的地发出一个请求来访问内部网站，然后通过相同的连接向内部网站发出一个请求：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752849882614.png "1661752849882614.png")

幸运的是，这种漏洞非常罕见。

**第一个请求路由**

第一个请求路由是一个密切相关的漏洞，发生在前端使用第一个请求的 Host 标头来决定将请求路由到哪个后端，然后将来自同一客户端连接的所有后续请求路由到同一后端连接。

这本身不是一个漏洞，但它使攻击者能够使用任意 Host 标头攻击任何后端，因此它可以与 Host 标头攻击链接在一起，例如密码重置攻击、Web 缓存攻击以及获得对其他虚拟主机的访问权限。

在此示例中，我们希望使用“psres.net”的攻击主机标头攻击 example.com 的后端，以进行密码重置攻击，但前端不会路由我们的请求：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752859172502.png "1661752859172502.png")

然而，通过对目标网站的有效请求开始我们的请求序列，我们可以成功到达后端：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752868105916.png "1661752868105916.png")

希望能给受害者发一封带有钓鱼链接的邮件：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752877608117.png "1661752877608117.png")

你可以使用 HTTP Request 走私中的“连接状态探测”选项扫描这两个漏洞。

大多数 HTTP 请求走私攻击可以描述如下：

发送一个长度不明确的 HTTP 请求，使前端服务器与后端对消息的结束位置产生分歧，从而将恶意前缀应用于下一个请求。此分歧通常是通过混淆的传输编码标头来实现的。

该漏洞是由以下HTTP/2请求触发的，该请求没有使用任何混淆或违反任何RFC。甚至对于长度没有任何歧义，因为 HTTP/2 在帧层中有一个内置的长度字段：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752887158245.png "1661752887158245.png")

此请求触发了来自运行 AWS Application Load Balancer (ALB) 作为其前端的各种网站的非常可疑的间歇性 400 漏洞请求响应。调查显示，ALB在将请求降级为HTTP/1.1转发到后端时，添加了一个“Transfer-Encoding: chunked”标头，而没有对消息正文进行任何更改：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752895183251.png "1661752895183251.png")

我只需要提供一个有效的被chunk对象：

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752904144606.png "1661752904144606.png")

这是一个发现漏洞的完美示例，它让你回溯实际发生的情况和原因。这个请求只有一个不寻常的地方，它没有 Content-Length (CL) 标头。由于前面提到的内置长度字段，在 HTTP/2 中省略 CL 是明确可接受的。然而，浏览器总是发送一个 CL，所以服务器显然不会期望没有CL的请求。

**检测连接锁定的 CL.TE**

有了这两个经验教训，我决定解决我去年在HTTP/2 研究中强调的一个未解决的问题，连接锁定 HTTP/1.1 请求走私漏洞的通用检测。连接锁定是指前端为与客户端建立的每个连接创建一个到后端的新连接的常见行为。这使得直接的跨用户攻击几乎不可能，但仍然留下了其他攻击途径。

要识别此漏洞，你需要通过单个连接发送“攻击者”和“受害者”请求，但这会产生大量误报，因为服务器行为无法与称为HTTP管道的常见无害特性区别开来。例如，给定以下 CL.TE 攻击的请求/响应序列，你无法判断目标是否易受攻击：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752915178904.png "1661752915178904.png")

HTTP 管道在 Burp Repeater 中也可见，它通常被误认为是真正的请求走私：

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752926173645.png "1661752926173645.png")

你可以通过将 requestsPerConnection 设置从 1 增加到自己在 Turbo Intruder 中的测试，这只是要做好误报的准备。

我浪费了很多时间试图调整请求来解决这个问题。但事实证明，上面的响应不能证明存在漏洞，并且解决方案立刻就出现了：

从上面的响应序列可以看出，由于随后的 404 响应，后端正在使用传输编码标头解析请求。但是，你无法判断前端是否使用请求的 Content-Length ，并因此易受攻击，或者是否安全地将其视为许多chunk，并假设橙色数据已通过管道传输。

要排除管道的可能性并证明目标确实易受攻击，你只需在使用 0\r\n\r\n 完成chunk处理请求后暂停并尝试提前读取。如果服务器在你的读取尝试期间做出响应，则表明前端认为该消息还是完整的，因此必须将其安全地分割成很多小块：

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752935120855.png "1661752935120855.png")

如果你的读取尝试被暂停，这表明前端正在等待消息完成，因此必须使用 Content-Length，从而使其易受攻击：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752947157474.png "1661752947157474.png")

这种技术也可以很容易地适应 TE.CL 漏洞。将其集成到 HTTP Request 走私中很快发现了一个在Barracuda WAF 后面运行 IIS 的网站，该网站容易受到传输编码的影响。有趣的是，修复这个漏洞的更新已经出现了，但它是作为一种投机性的修复措施来实现的，所以它没有被标记为安全版本，攻击设备也没有安装它。

**CL.0 浏览器兼容的异步**

虽然原先将另一个网站标记为最初看起来像连接锁定的 TE.CL 漏洞。但是，服务器没有按预期响应我的手动探测和读取。当我尝试简化请求时，我发现传输编码标头实际上被前端和后端完全忽略了。这意味着我可以完全利用它，发起攻击：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752955175758.png "1661752955175758.png")

前端使用的是 Content-Length，但后端显然完全忽略了它。结果，后端将正文作为第二个请求的方法的开始。忽略CL等同于将其视为值为0，因此这是一个CL.0异步，这是一种已知但较少探索的攻击类。

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752965166171.png "1661752965166171.png")

关于此漏洞的第二个也是更重要的一点是，它是由一个完全有效的、符合规范的 HTTP 请求触发的。这意味着前端防御它的机会为零，甚至可以由浏览器触发。

攻击是可能的，因为后端服务器根本不会接收到 POST 请求。

**amazon.com 上的 H2.0**

对 CL.0/H2.0 异步漏洞实施粗略扫描检查后发现，它们影响了包括 amazon.com 在内的众多网站，亚马逊网站忽略了发送到 /b/ 的请求的 CL：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752976160704.png "1661752976160704.png")

我通过创建一个简单的概念证明 (PoC) 来确认此漏洞，该概念将随机实时用户的完整请求（包括身份验证令牌）存储在我的清单中：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752988764193.png "1661752988764193.png")

在我向亚马逊报告此事后，我意识到我还是错过了一个危害更大的漏洞。攻击请求非常普通，我可以让任何人的网络浏览器使用 fetch() 发出它。通过在亚马逊上使用 HEAD 技术创建一个 XSS 小工具并在受害者的浏览器中执行 JavaScript，我可以让每个受攻击的受害者自己重新发起攻击，并将其传播给其他人。这样就会产生一个异步攻击，一种自我复制的攻击，利用受害者在没有用户交互的情况下发起的攻击，迅速利用亚马逊上的每个活跃用户。

我不建议在你的工作系统上尝试此操作，但在暂存环境中尝试可能会很有趣。

**客户端异步**

传统的异步攻击利用的是前端和后端服务器之间的连接，因此在不使用前端/后端架构的网站上是不可能的。从现在开始，我将把它称为服务器端异步。大多数服务器端异步只能由发出格式漏洞的请求的自定义 HTTP 客户端触发，但是，正如我们刚刚在 amazon.com 上看到的，有时可以创建由浏览器驱动的服务器端异步。

浏览器导致异步的能力会引发一类全新的威胁，我将其称为客户端异步 (client-side desync，CSD)，其中异步发生在浏览器和前端服务器之间。这使得可以利用独立的服务器网站，这很有价值，因为它们通常在 HTTP 解析方面非常糟糕。

CSD 攻击始于受害者访问的感染网站，然后让他们的浏览器向易受攻击的网站发送两个跨域请求。第一个请求的目的是使浏览器的连接异步，并使第二个请求触发有害响应，通常使攻击者控制受害者的帐户：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661752998205617.png "1661752998205617.png")

**攻击方法**

在尝试检测和利用客户端异步漏洞时，你可以重用来自服务器端异步攻击的许多概念。主要区别在于，整个漏洞利用序列都发生在受害者的网络浏览器中，这个环境比专用黑客工具更加复杂和不受控制。这带来了一些新的挑战，这给我在研究这项技术时带来了很大的阻碍。为此，我开发了以下方法：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20220829/1661753009234977.png "1661753009234977.png")

**探测**

第一步是识别你的 CSD 矢量。这个基本原语是漏洞的核心，也是构建漏洞利用的平台。我们已经在 HTTP Request 走私和Burp Scanner 中实现了对这些的自动检测，但是了解如何手动进行检测仍然很有价值。
...