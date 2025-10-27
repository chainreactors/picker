---
title: TouchEn nxKey键盘加密应用程序出现的许多漏洞很容易使其被黑化
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247557874&idx=2&sn=411077d6fe9d41b32dcf5c269764b9e2&chksm=e91432c8de63bbde60d3e18c87ded130bb48a571d22ee82320934c997db116ab58942d686144&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-23
fetch_date: 2025-10-04T07:52:22.986390
---

# TouchEn nxKey键盘加密应用程序出现的许多漏洞很容易使其被黑化

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXGDWwMP1sA5RFicduJibhFQ9aJByeMfibicdpLY8qVMZe0LiaPb2U7Ne0f7g/0?wx_fmt=jpeg)

# TouchEn nxKey键盘加密应用程序出现的许多漏洞很容易使其被黑化

luochicun

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

TouchEn nxKey是韩国安全软件公司Raonsecure开发的端到端加密应用程序，用于保证键盘使用时的全方位安全，目前这个应用程序主要用于韩国的金融业务，在韩国几乎所有电脑上都安装了这款软件。如果你想在韩国操作网上银行业务，就必须使用它。不过韩国人对它的安全性并不认可，TouchEn nxKey确实在设计上包含了关键日志记录功能，但它未能充分限制外界对它的访问。此外，研究人员发现其中存在的七个安全漏洞，可以让攻击者实现从简单的拒绝服务攻击到远程代码执行攻击。

2005年韩国一个黑客组织通过远程访问木马从人们的银行账户中窃取了5000万韩元(当时约合5万美元)。通过这种方式，他们不仅获得了用户的登录凭证，还获得了他们安全卡上的信息。这种安全卡类似于索引TAN，这是一种第二因素认证方法，2012年在欧盟被禁止，原因是很容易被银行木马攻破。

那用户的计算机是如何被这个恶意应用程序攻击的？这听起来像是在用浏览器访问恶意网站时进行的驱动程序下载，很可能是浏览器漏洞被利用了。但是也有可能是用户被诱导安装了应用程序。如今，上述攻击场景已经不那么常见了，一是网络浏览器变得更加安全，二是银行已经完全采用了双因素验证。至少在很多国家，你通常需要另一台设备来确认交易。并且在确认时可以看到交易细节，因此不会贸然确认向其他人转账的信息。

韩国则在2006/2007年强制银行交易使用TouchEn Key，当你在网页中输入数据时，该应用程序声称可以保护你的敏感数据。最终，TouchEn nxKey被扩展到支持非微软浏览器的使用场景中。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXaqOpDcYwJIaVStoAQpfqStBmfeFfOicnWYpct3kI1p7BkSQvAj1u64A/640?wx_fmt=png)TouchEn nxKey的实际用处

TouchEn nxKey是通过加密键盘输入来预防键盘记录。

依赖TouchEn nxKey的网站运行nxKey SDK，该SDK由两部分组成：一组运行在网站上的JavaScript代码和一些服务器端代码。下面是它的工作原理：

1.在使用nxKey SDK的网站上输入密码字段；

2.nxKey SDK的JavaScript代码会检测到它并通知你的本地nxKey应用程序；

3.nxKey应用程序在Windows内核中激活它的设备驱动程序；

4.设备驱动程序现在拦截所有键盘输入，键盘输入不是由系统处理，而是被发送到nxKey应用程序。

5.nxKey应用程序加密键盘输入并将其发送给nxKey SDK的JavaScript代码；

6.JavaScript代码将加密的数据放入隐藏的表单字段中。实际的密码字段只接收虚拟文本。

7.输入完登录凭证后，点击“登录”；

8.加密的键盘输入与其他数据一起发送到服务器。

9.nxKey SDK的服务器端部分对其进行解密，并从中检索纯文本密码。常规登录程序接管。

一个试图记录输入到这个网站的数据的键盘记录器只能看到加密的数据。它可以看到网站使用的公钥，但没有相应的私钥。所以没有办法解密，密码是安全的。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXaqOpDcYwJIaVStoAQpfqStBmfeFfOicnWYpct3kI1p7BkSQvAj1u64A/640?wx_fmt=png)网站如何与TouchEn nxKey通信？

网站如何知道计算机上安装了特定的应用程序呢？它是如何与之沟通的？

最初，TouchEn nxKey需要安装其浏览器扩展。该浏览器扩展使用本机消息将请求从网站转发到应用程序，并将响应发送回网页。

然而，使用浏览器扩展作为中间体已不再是最先进的技术。目前的最佳方法是网站使用WebSockets API直接与应用程序通信，不再需要浏览器扩展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXS3UlxKhLJia10oUjuIqUT7vVIsIgokASU3zKjpw9r41sXtuuhZQ1Xcg/640?wx_fmt=png)

虽然花旗银行韩国分行等一些网站专门使用新的WebSocket方法，但釜山银行等其他网站仍然运行完全依赖浏览器扩展的旧代码。

这不仅仅意味着用户仍然需要安装浏览器扩展，它还解释了软件安装后仍无法识别的频繁投诉。这些用户安装的是不支持WebSocket通信的旧版本软件。没有自动更新，目前韩国一些银行仍然提供这些旧版本的下载。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXaqOpDcYwJIaVStoAQpfqStBmfeFfOicnWYpct3kI1p7BkSQvAj1u64A/640?wx_fmt=png)滥用TouchEn扩展攻击银行网站

TouchEn浏览器扩展真的很小，它的功能是最少的。通过它的代码，我们看到了这样的评论：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXVNAHUaVmwmQKpRxmibaR5PV88HFExgxskr7Blm20rBZZbmd2ze0kaCQ/640?wx_fmt=png)

目前，危险的eval()调用已经从浏览器扩展中被清除了。

研究人员在回调机制中发现了这样一个问题，网站可以向应用程序发送一个setcallback请求来注册一些事件。当此类事件发生时，应用程序将指示扩展调用页面上已注册的回调函数。从本质上讲，页面上的任何全局函数都可以通过名称调用。

恶意网页是否可以注册其他网页的回调？有两个障碍：

目标网页需要有一个含有id="setcallback"的元素；

回调函数被传递到特定的选项卡；

第一个障碍意味着只有使用nxKey SDK的网站会受到攻击。当通过浏览器扩展进行通信时，这些扩展将创建必要的元素。通过WebSockets进行通信不会创建这个元素，这意味着使用更新nxKey SDK的网站不会受到影响。

第二个障碍似乎意味着只有加载在当前选项卡中的页面才会被攻击，例如加载在框架中的页面。除非nxKey应用程序在其响应中设置了错误的tabid值。

事实验证，这非常容易。虽然应用程序使用适当的JSON解析器来处理传入数据，但响应是通过调用sprintf\_s()生成的，不执行转义。因此，操纵一些响应属性并向其添加引号可以注入任意JSON属性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXOWZDzQFM0ahUDPjKJ1QRuK5K1nJibFia3ej2mFDIr0ajrsF63vdkY5tg/640?wx_fmt=png)

id属性将被复制到应用程序的响应中，这意味着响应会突然获得一个名为x的新JSON属性。此漏洞允许将tabid的任何值注入到响应中。

恶意页面如何知道银行选项卡的ID？它可以使用自己的标签ID (TouchEn扩展有助于暴露)，并尝试猜测其他标签ID。或者它可以简单地将此值留空，在这种情况下，扩展很有帮助：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXHQCr8fbKf2jGgtcrLXHotlZrCbpLiaPrW9boAMBWGjOssZibczxesQew/640?wx_fmt=png)

因此，如果tabid值为空，它将向当前活动的选项卡传递消息。

这意味着会发生如下可能的攻击：

1.在新选项卡中打开银行网站，它将成为活动选项卡；

2.等待页面加载，这样id="setcallback"的元素就出现了；

3.通过TouchEn扩展发送setcallback消息以设置对某个函数的回调，同时用"tabid":""和"reply":"malicious payload"覆盖JSON响应属性。

第一个回调调用立即发生。因此，将在银行网站中调用回调函数，并使用来自reply属性的恶意有效负载作为参数。

一个可能的回调函数可以是eval，但还有最后一个障碍：TouchEn通过JSON.stringify()将reply属性传递给回调函数。所以我们实际上得到eval("\"malicious payload\"" ")，但这没有任何作用。

另一方面，也许目标页面有jQuery？调用$('""')将产生预期的结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXHJPWgtJONeKhB1MFRuwF4lvMMSk80XiaG0IyqPWEqCjuWmSRIiaicRbWQ/640?wx_fmt=png)

使用TouchEn nxKey的网站很可能也会使用TouchEn Transkey(一种屏幕键盘)，这依赖于jQuery。总之，所有韩国银行网站似乎都严重依赖jQuery，这及易产生攻击。

但是update\_callback (nxKey SDK的指定回调)也可以被滥用，在传递json字符串化的数据时运行任意JavaScript代码。调用update\_callback('{"FaqMove":"javascript:alert(\'Hi, this is JavaScript code running on \'+document.domain)"}')将尝试重定向到javascript:链接，并运行任意代码进行攻击。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmX4ApmX9orVfOag0pVv3icr7cXt4Hyz1TyOiciaoRxU0ecq1BRvddx8Mv7w/640?wx_fmt=png)

因此，这种攻击允许恶意网站破坏任何依赖TouchEn扩展的网站。韩国银行强制用户安装的“安全”应用程序都没有检测或防止这种攻击。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXaqOpDcYwJIaVStoAQpfqStBmfeFfOicnWYpct3kI1p7BkSQvAj1u64A/640?wx_fmt=png)类似TouchEn的浏览器扩展

当我开始测试时，Chrome Web Store中有两个TouchEn扩展。目前这个不太受欢迎但基本上相同的扩展已经被删除。

研究人员发现了三个几乎相同的扩展：INISAFE的CrossWeb EX和Smart Manager EX以及iniLINE的CrossWarpEX。CrossWeb EX是其中最受欢迎的，目前有超过400万用户。这些扩展同样会使网站受到攻击。

我的第一个想法是RaonSecure和INISAFE属于同一个公司集团。但事实似乎并非如此。

以下是iniLINE软件开发公司的页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXggR36bkz0cSvMuuru53AlCZkqKo8oVc0vpHQK9wicviazNq6U5Ga7wibA/640?wx_fmt=png)

Initech和RaonSecure仅仅是合作伙伴，所以看起来iniLINE是这些浏览器扩展的开发者。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXaqOpDcYwJIaVStoAQpfqStBmfeFfOicnWYpct3kI1p7BkSQvAj1u64A/640?wx_fmt=png)通过网站使用键盘记录功能

现在假设有一个恶意网站。让我们假设这个网站告诉TouchEn nxKey:“你好，用户现在在密码字段，我想要他们输入的数据。”那个网站会得到所有的键盘输入吗？

是的，会的！它将获取用户键入的任何内容，无论当前哪个浏览器选项卡处于活动状态，或者浏览器本身是否处于活动状态。nxKey应用程序只是遵从请求，此时不会检查它是否有意义。事实上，它甚至会向网站提供在用户访问控制提示中输入的管理员密码。

但肯定会有障碍。首先，这样的网站需要一个有效的许可证。在使用任何应用程序功能之前，它需要在get\_versions调用中传递许可证：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXcfbM71qQMJmibGPxfZE8aeCPRjT9NffuM84xEaoCewmZksldicNJwhRQ/640?wx_fmt=png)

此特定的许可证仅对www.example.com有效。所以只能在www.example.com网站上使用。或者被任何声称是www.example.com的网站。

看到上面代码中的origin属性了吗？是的，TouchEn nxKey实际上相信，而不是查看Origin HTTP标头。因此，从一些合法使用nxKey的网站获取许可证并声称自己就是该网站是很简单的。另一个障碍是：恶意网站接收到的数据不会被加密吗？如何解密呢？应该可以使用不同的公钥，即已知私钥的公钥。那么人们只需要知道算法，然后解密数据就可以了。

不过，这些都不是必要的。如果TouchEn nxKey根本没有接收到任何公钥，它释放密钥，这样该网站将接收明文键盘输入。

概念验证页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXObEOlwWxBoXCibG7exjNydTzzAA41wP47PiaTMvFT1icKt8EJ5ibntTLpA/640?wx_fmt=png)

还有第三个障碍，这大大降低了这个漏洞的严重程度，被恶意网页拦截的键盘输入不再到达目的地。当用户开始输入密码时，肯定会感到可疑，但文本字段中却没有显示任何内容。我对nxKey应用程序的分析表明，它只能这样工作：键盘输入要么到达网页，要么到达实际目标，但不能同时实现。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmXaqOpDcYwJIaVStoAQpfqStBmfeFfOicnWYpct3kI1p7BkSQvAj1u64A/640?wx_fmt=png)攻击应用程序

如上所述，编写这个产品JavaScript代码的人并不精通它。但也许是因为他们所有的专家都有c++背景？我们以前已经看到过这种情况，开发人员试图尽快放弃JavaScript，将所有任务委托给c++代码。

遗憾的是，这还只是猜测。与二进制代码相比，我更习惯于分析JavaScript，但应用程序本身似乎也同样充满了漏洞。事实上，它主要使用C而不是c++的典型方法，其中有很多手动内存管理。

上述已经提到过sprintf\_s()的使用，关于像sprintf\_s()或strcpy\_s()这样的函数，有一个有趣的事实，虽然它们是sprintf()或strcpy()函数的“内存安全”版本，不会溢出缓冲区，但使用起来仍然很棘手。如果没有给它们足够大的缓冲区，它们将调用无效的参数处理程序。默认情况下，这会使应用程序崩溃。

nxKey应用程序的缓冲区不够大，也不会改变默认行为。因此，在许多情况下，发送过大的值会使应用程序崩溃。崩溃总比缓冲区溢出好，但崩溃的应用程序无法再执行其任务。这就会造成，用户的网上银行登录表单似乎正常工作，但它现在以明文形式接收你的密码。用户只会在提交表单时注意到某些错误，从而导致错误消息，此漏洞允许拒绝服务攻击。

另一个示例是，在所有的JSON解析器中，nxKey应用程序的开发人员选择了用c编写的解析器。不仅如此，他们还从2014年1月起随机选择了一个存储库状态，并且从未更新过它。空指针解引用在2014年6月修复，现在还在。因此，向应用程序发送](一个方括号)而不是JSON数据足以使其崩溃，这是一个允许拒绝服务攻击的漏洞。

上面提到的应用程序许可是base64编码的数据，应用程序需要对其进行解码。解码器函数如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibTJwN9WoupMyflF4jJibwmX1jiblbSLdKQ70MzXTtyQHKGLRuqPML7YHsT3icBzJRahKffyq5Ehiabkg/640?wx_fmt=png)

我不确定这个函数来自何处，它与CycloneCRYPTO库的base64解码器有明显的相似之处。但是CycloneCRYPTO将结果写入预先分配的缓冲区。因此，缓冲区分配逻辑可能是由nxKey开发人员自己添加的。

这种逻辑是有缺陷的，它明确地假设input\_len是4的倍数。但是对于像abcd==这样的输入，它的计算将导致分配2个字节的缓冲区，尽管实际输出是3个字节。

本文的概念验证页面只是向nxKey应用程序发送随机生成的许可字符串。这足以在几秒钟内使应用程序崩溃。连接调试器显示了内存攻击的明显证据：应用程序崩溃是因为它试图使用虚假内存位置读取或写入数据。

现代操作系统有一些机制，可以使像这样的缓冲区溢出更难转化为代码执行漏洞。但这些机制只有在实际使用时才有帮助。...