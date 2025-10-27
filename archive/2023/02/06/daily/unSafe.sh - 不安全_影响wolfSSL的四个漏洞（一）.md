---
title: 影响wolfSSL的四个漏洞（一）
url: https://buaq.net/go-147998.html
source: unSafe.sh - 不安全
date: 2023-02-06
fetch_date: 2025-10-04T05:47:13.086903
---

# 影响wolfSSL的四个漏洞（一）

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

![](https://8aqnet.cdn.bcebos.com/e2117b838086a5e6750dc824f6f8dba7.jpg)

影响wolfSSL的四个漏洞（一）

导语：wolfSSL是一个轻量级的 SSL
*2023-2-5 12:0:0
Author: [www.4hou.com(查看原文)](/jump-147998.htm)
阅读量:30
收藏*

---

导语：wolfSSL是一个轻量级的 SSL 实现，主要应用于嵌入式系统。

Trail of Bits 安全公司披露了影响wolfSSL的四个漏洞：CVE-2022-38152、CVE-2022-38153、CVE--202-39173和CVE-2022-42905。这四个漏洞的CVSS评分从中等到严重不等，都可能导致拒绝服务（DoS）。wolfSSL是一个轻量级的 SSL 实现，主要应用于嵌入式系统。

DOSC：CVE-2022-38153允许MitM攻击者或恶意服务器通过拦截和修改TLS数据包对TLS 1.2客户端执行DoS攻击，此漏洞影响wolfSSL 5.3.0。

DOSS：CVE-2022-38152是针对使用wolfSSL\_clear函数而不是序列wolfSSL\_free的wolfSSL服务器的DoS漏洞wolfSSL\_new。恢复会话会导致服务器因空指针解引用而崩溃。此漏洞影响wolfSSL 5.3.0至5.4.0。

BUF：CVE-2022-39173是缓冲区溢出导致的，会导致wolfSSL服务器的DoS。这是由于假装恢复会话，并在客户端Hello中发送重复的密码套件引起的。它可能允许攻击者获得特定架构或目标上的RCE。然而，这一说法尚未得到证实。5.5.1之前版本的wolfSSL会受到影响。

HEAP：CVE-2022-42905是由解析TLS记录标头时缓冲区重写导致的。5.5.2之前版本的wolfSSL会受到影响。

**DOSC：拒绝客户服务**

在wolfSSL 5.3.0中，MiTM攻击者或恶意服务器可以使TLS客户端崩溃。该漏洞存在于AddSessionToCache函数中，当客户端从服务器接收到新的会话票据时，将调用该函数。

让我们假设wolfSSL会话缓存的每个存储桶至少包含一个条目。一旦新的会话票据到达，客户端将重用先前存储的缓存条目，以尝试将其缓存在会话缓存中。此外，由于新的会话票据相当大，只有700字节，因此将使用XMALLOC在堆上分配它。

在以下示例中，SESSION\_TICKET\_LEN为256：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675010696179405.png "1675010696179405.png")

此分配导致cacheTicBuff的初始化，因为ticBuff已经初始化，cacheSession->ticketLenAlloc为0，ticLen为700：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675010710166920.png "1675010710166920.png")

cacheTicBuff设置为前一个会话的票据cacheSession->ticket。堆上未分配cacheTicBuff指向的内存；实际上，cacheTicBuff指向cacheSession->\_staticTicket。这是有漏洞的，因为如果cacheTicBuff不为空，它稍后会被释放。

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675010727189372.png "1675010727189372.png")

进程通过执行XFREE函数终止，因为传递的指针没有分配到堆上。

注意，票据长度本身并不是导致崩溃的原因。此漏洞与OpenSSL中发现的缓冲区溢出漏洞Heartbleach截然不同。使用wolfSSL，崩溃不是由缓冲区溢出引起的，而是由逻辑错误引起的。

fuzzer在大约一小时内发现了该漏洞，它修改了NewSessionTicket（new\_message\_ticket）消息，用700字节的大数组（large\_bytes\_vec）替换了实际的票据。否则正常追踪的这种突变会导致对未分配值调用XFREE。这最终导致收到如此大票据的客户端崩溃。

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230130/1675010741111255.png "1675010741111255.png")

DOSC的可视化漏洞(CVE-2022-38153)，每个方框代表一条TLS消息。每条消息由不同的字段组成，如协议版本或密码套件矢量。可视化是使用tlspuffin fuzzer生成的。

由于漏洞驻留在wolfSSL的会话缓存中，因此我们需要让客户端缓存填满以触发崩溃。根据经验，我们发现大约需要30个预先连接才能可靠地使它们崩溃。随机行为的原因是缓存由多个行或桶组成；wolfSSL的默认编译配置包含11个桶。基于TLS会话ID的哈希，会话存储在其中一个桶中。仅当当前存储桶已包含以前的会话时，才会触发DoS。

重现此漏洞是困难的，通常，像wolfSSL缓存这样的全局状态使得模糊处理更加难以应用。理想情况下，人们可以假设，在给定相同输入的情况下，程序的每次执行都会产生相同的输出。如果由于程序使用全局状态而违反了这一假设，则复制和调试将变得更困难。

幸运的是，tlspuffin允许研究人员重新创建一个程序状态，该状态与fuzzer观察到崩溃时的状态类似。我们能够重新执行fuzzer认为有趣的所有追踪，这使我们能够在更受控的环境中观察wolfSSL的崩溃，并使用GDB调试wolfSSL。在分析了导致无效free的调用堆栈之后，很明显该漏洞与会话缓存有关。

DOSC的根本原因在于使用了共享的全局状态。我们惊奇地发现wolfSSL在库的多个调用之间共享状态。从概念上讲，会话缓存的生命周期应该绑定到TLS环境中，该环境已经用作TLS会话的容器。每个SSL会话都与TLS背景共享状态。维护全局可变状态的添加增加了整个代码库的复杂性。因此，它应该只在绝对必要的时候使用。

**BUF：服务器缓冲区溢出**

在5.5.1之前的wolfSSL版本中，恶意客户端可能会在恢复TLS 1.3握手期间导致缓冲区溢出。如果攻击者通过发送恶意构建的Client Hello，然后发送另一个恶意构建的客户端Hello，从而恢复或假装恢复先前的TLS会话，则可能发生缓冲区溢出。至少必须发送两个客户端Hello：一个假装恢复上一个会话，另一个作为对Hello Retry Request消息的响应。

恶意客户端Hello包含一个受支持的密码套件列表，其中至少包含⌊sqrt(150)⌋ + 1 = 13个重复项，总共不超过150个密码。缓冲区溢出发生在握手期间第二次调用RefineSuites函数时。5.

RefineSuites函数需要一个结构WOLFSSL，它包含ssl->suites中可接受的密码套件列表，以及一组对等密码套件。两个输入都由WOLFSSL\_MAX\_SUITE\_SZ限定，等于150个密码组或300个字节。

让我们假设ssl->suites由单个密码套件组成，如TLS\_AES\_256\_GCM\_SHA384，并且用户可控制的peerSuites列表包含重复13次的相同密码。RefineSuites函数将在peerSuites上迭代ssl->suites中的每个套件，如果匹配，则将该套件追加到套件数组中。套件数组的最大长度为WOLFSSL\_MAX\_SUITE\_SZ套件。

使用刚才提到的输入，套件的长度现在等于13。套件数组现在被复制到上面列表最后一行中的结构WOLFSSL。因此，ssl->suites数组现在包含13个TLS\_AES\_256\_GCM\_SHA384密码套件。

在可能恢复的TLS握手期间，如果客户端触发了Hello Retry Request，则会再次调用RefineSuites函数。结构WOLFSSL之间不进行重置，并保留之前的13个密码套件。因为TLS peer控制了peerSuites数组，所以我们假设它再次包含13个重复的密码套件。

RefineSuites函数将在peerSuites上迭代ssl->suites中的每个元素，如果匹配，则将套件附加到套件中。因为ssl->suites数组已包含13个TLS\_AES\_256\_GCM\_SHA384密码套件，总共有13 x 13=169个密码套件写入套件。169个密码套件超过了分配的最大允许WOLFSSL\_MAX\_SUITE\_SZ密码套件。堆栈上的套件缓冲区溢出。

到目前为止，我们还无法利用这个漏洞，例如，无法获得远程代码执行，因为可以溢出套件缓冲区的字节集很小。只有有效的密码套件值才能溢出缓冲区。

为了了解我们是如何发现这些漏洞的，有必要研究一下tlspuffin是如何开发的。

**下一代协议模糊**

加密协议的实现及易出现漏洞，早在2017年，研究人员发现众所周知的WPA2协议存在严重漏洞（KRACK），比如FREAK这样的漏洞，或者像2022年初发现的wolfSSL漏洞(CVE-2022-25640和CVE-2022-25638)这样的身份验证漏洞。

模糊化加密协议是非常困难的，与传统的文件格式模糊化不同，加密协议需要特定的加密和相互依赖的消息流来达到深层协议状态。

此外，检测逻辑错误本身也是一项挑战。AddressSanitizer使安全研究人员能够精确地发现与内存相关的漏洞。对于诸如身份验证绕过或机密性丢失之类的逻辑错误，不存在自动检测器。

AddressSanitizer(简称 ASan) 是一个内存检测工具，它可以自动检测程序运行时(runtime)发生的许多内存访问错误。

上述漏洞都是由fuzzer检测到的，fuzzer由所谓的Dolev Yao模型实现，该模型自20世纪80年代以来一直用于正式协议验证。

**Dolev Yao模型**

形式化方法已成为密码协议安全分析的重要工具。ProVerif或Tamarin等现代工具提供了一个完全自动化的框架来建模和验证安全协议。ProVerif手册和DEEPSEC论文很好地介绍了协议验证。

使用Dolev Yao模型，攻击者可以完全控制通信网络中发送的消息。消息使用术语代数进行符号化建模，该术语代数由一组函数符号和变量组成。这意味着可以通过在变量和其他函数上应用函数来表示消息。

攻击者可以窃听、注入或操纵消息，Dolev Yao模型旨在模拟对这些协议的真实攻击，例如中间人（MitM）攻击。加密原语通过抽象语义建模，因为Dolev-Yao模型专注于查找逻辑协议漏洞，而不关心加密原语的正确性。因为原语是通过抽象语义来描述的，所以没有真正的实现，例如Dolev-Yao模型中定义的RSA或AES。

使用此模型已经可以在加密协议中检测到攻击。TLS规范已经在2006年和2017年通过这些工具进行了各种分析，这导致了RFC草案中的修复。但为了模糊协议的实现，而不是验证它们的规范，我们需要做一些稍微不同的事情。为此，我们选择用包含原语实现的更具体的语义来代替抽象语义。

Tlspuffin fuzzer是基于Dolev-Yao模型设计的，并以符号形式模型为指导，这意味着它可以执行Dolev-Yoo模型中可表示的任何协议流。它还可以生成以前看不见的协议执行。以下部分解释了Dolev Yao追踪的概念，该追踪大致基于Dolev Ya模型。

本文翻译自：https://blog.trailofbits.com/2023/01/12/wolfssl-vulnerabilities-tlspuffin-fuzzing-ssh/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

![](https://www.4hou.com/captcha/flat?8IJFXnva)

#### 你可能感兴趣的

* [![](https://img.4hou.com/images/c38b01a59373405f83ff7878fbe9edc7.png)

  影响wolfSSL的四个漏洞（一）](https://www.4hou.com/posts/kMpN)
* [![](https://img.4hou.com/images/WX20230203-180837@2x.png)

  JIT 漏洞（CVE-2020-9802 ）的缓解措施很容易被绕过](https://www.4hou.com/posts/2JL1)
* [![](https://img.4hou.com/images/WechatIMG624.jpeg)

  漏洞预警|hutool 存在反序列化漏洞](https://www.4hou.com/posts/KEwM)
* [![](https://img.4hou.com/images/WechatIMG618.jpeg)

  漏洞深度分析｜CVE-2023-24162 hutool XML反序列化漏洞](https://www.4hou.com/posts/LBxX)
* [![](https://img.4hou.com/images/1489711813216095488.jpeg)

  ImageMagick：隐藏在网上图像背后的漏洞](https://www.4hou.com/posts/GKpL)
* [![](https://img.4hou.com/images/1672303875747875.jpeg)

  思科Talos报告：威胁分子使用已知的Excel漏洞](https://www.4hou.com/posts/6VEO)

![]()

文章来源: https://www.4hou.com/posts/kMpN
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)