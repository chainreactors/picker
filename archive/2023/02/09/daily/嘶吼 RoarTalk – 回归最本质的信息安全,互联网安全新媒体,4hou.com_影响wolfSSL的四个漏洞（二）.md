---
title: 影响wolfSSL的四个漏洞（二）
url: https://www.4hou.com/posts/l6qg
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-09
fetch_date: 2025-10-04T06:05:21.189169
---

# 影响wolfSSL的四个漏洞（二）

影响wolfSSL的四个漏洞（二） - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 影响wolfSSL的四个漏洞（二）

xiaohui
[漏洞](https://www.4hou.com/category/vulnerable)
2023-02-08 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)213444

收藏

导语：wolfSSL是一个轻量级的 SSL 实现，主要应用于嵌入式系统。

**Dolev Yao追踪**

Dolev Yao追踪建立在Dolev Ya模型之上，并使用术语代数来象征性地表示消息。就像在Dolev Yao模型中一样，加密原语被视为黑盒。这允许fuzzer关注逻辑错误，而不是测试加密原语的正确性。

让我们从臭名昭著的Needham Schröder协议的一个示例开始。Needham Schröder是一种身份验证协议，允许双方通过可信服务器建立共享秘密；然而，它的非对称版本因易受MitM攻击而臭名昭著。该协议允许Alice和Bob通过可信的第三方服务器创建共享密钥。该协议通过向服务器请求一个共享密钥来工作，该密钥对Bob和Alice分别加密一次。Alice可以向服务器请求一个新的秘密，并将收到一条加密消息，其中包含共享秘密和一条发送给Bob的进一步加密消息。Alice将把消息转发给Bob。Bob现在可以解密消息，还可以访问共享秘密。协议中的漏洞允许冒名顶替者通过首先启动与Alice的连接，然后将接收到的数据转发给Bob来冒充Alice。

在下面的Dolev Yao追踪T中，我们对两个名为a和b的代理之间的Needham Schröder协议的一个特定执行进行了建模。每个代理都有一个底层实现，追踪由一系列步骤组成，这些步骤由一个点分隔。分两步：输入和输出。输出步骤由代理名称上方的一个栏表示。

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675011495133325.png "1675011495133325.png")

Needham Schröder协议的Dolev Yao追踪

现在，让我们来描述追踪T的语义。在第一步中，我们将术语pk(sk\_E)发送给代理a。代理a将序列化该术语并将其提供给其底层实现Needham-Schröder。

接下来，我们让代理a输出一个位字符串并将其绑定到h\_1。依照Dolev Yao追踪中的步骤，我们可以观察到我们现在将术语aenc(adec(h\_1, sk\_E)， pk(sk\_B))发送到代理b。

接下来，我们让代理b的底层实现输出一个位字符串，并将其绑定到h\_2。接下来的两个步骤将消息h\_2转发给代理a，并将其新的输出绑定到h\_3。最后，我们对不同的输入（即h3）重复第三步和第四步，并将h3项发送给代理a。

这样的追踪允许我们对加密协议的任意执行流进行建模。上面的追踪模拟了最初由Gavin Lowe发现的MitM攻击。该协议的一个固定版本被称为Needham Schroeder-Lowe协议。

**TLS 1.3握手协议**

在提供现代加密协议示例之前，我想快速解释一下TLS握手的不同阶段。

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675011510131432.png "1675011510131432.png")

TLS握手阶段概述

密钥交换：建立共享密钥并选择加密方法和参数。此阶段中的两条消息都未加密。

服务器参数：交换不再以明文发送的其他参数。

服务器身份验证：通过确认密钥和握手完整性来验证服务器。

客户端身份验证：可选地，通过确认密钥和握手完整性来验证客户端。

就像在Needham Schröder示例中一样，TLS握手的每个消息都可以用一个符号术语表示。例如，第一个客户端Hello消息可以表示为术语fn\_client\_hello(fn\_key\_share, fn\_signature\_algorithm, psk)。本例中fn\_key\_share、fn\_signature\_algorithm和psk为常量。

**模糊Dolev Yao追踪**

tlspuffin fuzzer实现了Dolev Yao追踪，并允许在具体的模糊目标（如OpenSSL、wolfSSL和libssh）中执行这些追踪。

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675011526483798.png "1675011526483798.png")

tlspuffin的结构，它遵循LibAFL定义的最佳实践

tlspuffin的设计基于进化fuzzer LibAFL。fuzzer使用了几个概念，这些概念将在以下章节中进行说明。我们将追踪他们从种子语料库中被挑选出来的过程，直到他们被变异、执行、观察，最终生成攻击追踪。

**种子语料库**

最初，种子语料库包含一些代表一些常见攻击场景的手工追踪，例如，客户机/服务器是攻击者或MitM是攻击者。

**调度程序和突变阶段**

调度程序根据启发式方法选择种子；例如，调度程序可能更喜欢更短、更精简的追踪。之后，提取的追踪会发生突变。这意味着消息被跳过或重复，或其内容被更改。因为我们使用Dolev Yao模型来表示消息，所以我们可以通过交换子项或更改函数符号来更改消息字段。

**执行程序、反馈和目标**

追踪发生变异后，将其发送给执行程序。执行程序负责在OpenSSL或wolfSSL等实际实现中执行追踪，在这些实现中，追踪可以在同一进程中执行，也可以在每个输入的fork中执行。执行程序还负责收集有关执行的观察结果。如果观察包含关于新发现的代码边缘的信息，则将其归类为反馈。例如，如果追踪使模糊目标崩溃或见证了身份验证绕过，则将追踪分类为目标。然后将观察结果添加到种子语料库或基于其分类的客观语料库中。

最后，我们可以重复这个过程，开始从种子语料库中提取新的追踪。该算法在模糊处理中很常见，与经典AFL fuzzer的方法密切相关。

目前，tlspuffin已经支持对OpenSSL的几个版本（包括易受Heartbleach攻击的1.0.1版本）和LibreSSL进行模糊处理。我们设计了一个接口，增加了模糊任意协议库的功能。通过实现wolfSSL的接口，我们能够添加对模糊化wolfSSL 4.3.0到5.4.0的支持，即使wolfSSL与OpenSSL或LibreSSL不兼容。因为接口是用Rust编写的，所以为wolfSSL实现它需要我们创建Rust绑定。这样做的好处是，可以在嵌入式软件项目的tlspuffin外部重用wolfSSL绑定。我们在GitHub上发布了开源的wolfSSL绑定。

以前，tlspuffin绑定到OpenSSL API，只有LibreSSL和OpenSSL支持该API。有了这个接口，就可以支持未来任意的模糊目标。

**支持更多协议**

虽然tlspuffin是专门为TLS协议设计的，它具有支持其他格式的能力。事实上，任何在Dolev Yao模型中形式化的协议都应该可以通过tlspuffin实现模糊化。我们添加了对SSH的支持，这要求我们对某些协议原语(如消息、消息解析、术语代数和知识查询)进行抽象。我们为TLS选择的抽象在很大程度上也适用于SSH。但是，由于协议数据包的有状态序列化，SSH协议需要进行一些调整。

为了测试SSH抽象，我们添加了对模糊化libssh的支持（不要与libssh2混淆）。与wolfSSL一样，我们的首要任务之一是创建Rust绑定。

**安全检测**

对于协议fuzzer来说，检测除分段错误、缓冲区溢出或释放后使用之外的安全违规是必不可少的。在fuzzer环境中，oracle决定被测程序的特定执行是否达到了某个目标。

当使用像AddressSanitizer这样的安全检测工具时，缓冲区溢出或过度读取可能会导致程序崩溃。在传统的模糊化中，oracle决定经典目标“程序崩溃”是否实现。这使得oracle不仅可以检测由分段错误导致的程序崩溃，而且可以检测与内存相关的漏洞。

TLS库中的许多安全漏洞（如身份验证绕过或协议降级）不会因崩溃而凸显出来。为了解决这个漏洞，tlspuffin提供了一个更复杂的oracle，可以检测特定于协议的漏洞。这使得tlspuffin不仅可以重新发现Heartbleed 或CVE-221-3449等漏洞，还可以发现FREAK等逻辑错误。出于检测目的，研究人员还扩展了安全违规oracle的功能，包括身份验证检查，这使他们重新发现了wolfSSL中的两个身份验证漏洞（CVE-2022-25640和CVE-2022-205638）。这表明tlspuffin在没有人类交互的情况下自动发现了这些漏洞。

如果fuzzer发现了所谓的攻击追踪，那么我们必须验证这一发现。验证结果的一个好方法是针对实际目标（如TCP上的TLS服务器或客户端）执行它们。通过使用默认设置，我们可以确保模糊目标的设置不会导致误报。

为此，研究人员开发了一个功能，该功能允许用户通过TCP对客户端或服务器执行Dolev Yao追踪，这允许我们单独测试针对目标的攻击追踪。其中一个目标可能是通过TCP可访问的OpenSSL服务器。每个OpenSSL安装都带有这样一个服务器，可以使用openssl s\_server -key key.pem -cert cert.pem启动。wolfSSL也有类似的测试服务器。现在，我们可以通过tlspuffin执行追踪，并查看服务器是否崩溃、行为不当或仅仅出现错误。

如上所述，这使我们能够验证CVE-2022-38153，并确定只有在使用wolfSSL库的特定设置时才会发生崩溃。

**总结**

Dolev Yao模型引导的模糊化也有缺点。集成新的模糊目标或协议需要大量努力。添加对SSH的支持大约需要五到六周，添加新的模糊目标需要一到两周。最后，需要对fuzzer进行测试，需要解决测试工具中的漏洞，并且需要在合理的时间内运行fuzzer。在上述示例中，发现漏洞又花了一周时间。请注意，让fuzzer的单个实例长时间运行可能不是最好的方法。每隔几天重新启动一次fuzzer是避免fuzzer在覆盖率方面陷入“局部最小值”的好方法。

因此，将Dolev Yao模型引导的模糊化应用于任意密码协议和任意实现的整个过程需要几个月。基于这些估计，模糊化技术最适合于具有TLS或SSH等多种实现的普遍存在的协议。

我们注意到，特定于协议的特性会增加集成的复杂性。例如，TLS使用转录本，这可以显著增加协议消息的大小。我们为tlspuffin中的大型转录本应用了一种变通方法。在SSH的情况下，我们观察到消息编码和解码是有状态的，这意味着消息根据协议状态进行不同的编码（基于协商的参数使用不同的MAC算法）。

相反，通过Dolev Yao模型引导的模糊化测试现有或未来的TLS或SSH实现是非常有前途的。考虑到一旦将一个库集成到tlspuffin中，就可以在多个版本中连续地对它进行模糊处理，这可能需要花费几周时间。

开发人员还可以使用tlspuffin编写测试套件，可以对库运行追踪，以测试是否存在特定的身份验证漏洞。这允许实现回归测试，以确保以前的漏洞不会再次发生。换句话说，tlspuffin可以用于TLS攻击者当前使用的相同任务。

总之，Dolev Yao模型引导的模糊化是一种新的、有前途的模糊测试密码协议的技术。通过重新发现已知的身份验证漏洞并在wolfSSL中发现新的DoS攻击，它已经证明了其可行性。

tlspuffin非常适合于高影响和广泛使用的协议，如TLS或SSH。将一个新的协议集成到tlspuffin需要大量的工作，并且需要对协议的深入理解。在传统的模糊化中，特定领域的知识有时相对不重要，因为标准配置中的简单模糊化可以产生强大的结果。如果tlspuffin用于尚不支持的协议，则失去了这一优势。

尽管如此，tlspuffin在一个已经支持的协议上使用时还是会能够体现出其优势的。互联网严重依赖TLS和SSH协议，影响它们的安全漏洞影响深远。如果TLS或SSH中断，则互联网就会中断。幸运的是，由于世界各地的安全研究人员所做的大量工作，这种情况尚未发生。

本文翻译自：https://blog.trailofbits.com/2023/01/12/wolfssl-vulnerabilities-tlspuffin-fuzzing-ssh/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?XlNrTBXk)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/4645ece03f124d9c2bb9.png)

# [xiaohui](https://www.4hou.com/member/bo2j)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/...