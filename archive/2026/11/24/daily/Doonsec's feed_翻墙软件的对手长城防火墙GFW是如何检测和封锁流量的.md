---
title: 翻墙软件的对手长城防火墙GFW是如何检测和封锁流量的
url: https://mp.weixin.qq.com/s/8L02aZ6R1UnZNlXFbVUDGg
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:40:02.943099
---

# 翻墙软件的对手长城防火墙GFW是如何检测和封锁流量的

# 翻墙软件的对手长城防火墙GFW是如何检测和封锁流量的

原创

佚名
佚名

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 背景介绍

## 长城防火墙

> * 防火长城（英语：Great Firewall，GFW），中国国家防火墙，或简称为墙、防火墙等，中国网信办称其为数据跨境安全网关，是该国政府过滤国际互联网出口内容的软硬件系统集合。防火长城不是中国特有的一个专门单位，而是由分散部门的各服务器和路由器等设备，加上相关公司的应用程序构成，其监控所有经过国际网关的通讯，对认为不符合中国官方要求的传输内容，进行干扰、阻断、屏蔽。由于中国网络审查广泛，中国大陆内含有“不合适”内容的网站，会受到政府直接的行政干预，故防火长城主要作用在于分析和过滤中国境外网络的信息。自本世纪初以来，防火长城由国家计算机网络与信息安全管理中心（CNCERT）运营和维护。

> * 随着防火长城逐渐为人熟知，“墙”一词有时也被用作动词，“被墙”即指网站内容被防火长城所屏蔽，“翻墙”也被引申为突破网络审查浏览中国大陆境外被屏蔽的网站或使用服务的行为。

长城防火墙首要设计者为北京邮电大学原校长方滨兴，被称为“国家防火墙之父”。基于这套系统，国家可以屏蔽我们大陆之外的任何非法网站，使其不能被国内所访问。而我们所讲的域名被墙，通俗的来讲就是域名被国家防火墙列入了黑名单，或者网站IP被列入了GFW的黑名单里。

## 传输控制协议

> 传输控制协议（英语：Transmission Control Protocol，缩写：TCP）是一种面向连接的、可靠的、基于字节流的传输层通信协议，由IETF的RFC 793定义。在简化的计算机网络OSI模型中，它完成第四层传输层所指定的功能。用户数据报协议（UDP）是同一层内另一个重要的传输协议。

> 在因特网协议族（Internet protocol suite）中，TCP层是位于IP层之上，应用层之下的中间层。不同主机的应用层之间经常需要可靠的、像管道一样的连接，但是IP层不提供这样的流机制，而是提供不可靠的包交换。

> 应用层向TCP层发送用于网间传输的、用8位字节表示的数据流，然后TCP把数据流分割成适当长度的报文段（通常受该计算机连接的网络的数据链路层的最大传输单元（MTU）的限制）。之后TCP把结果包传给IP层，由它来透过网络将包传送给接收端实体的TCP层。TCP为了保证不发生丢包，就给每个包一个序号，同时序号也保证了传送到接收端实体的包的按序接收。然后接收端实体对已成功收到的包发回一个相应的确认信息（ACK）；如果发送端实体在合理的往返时延（RTT）内未收到确认，那么对应的数据包就被假设为已丢失并进行重传。TCP用一个校验和函数来检验数据是否有错误，在发送和接收时都要计算校验和。

# GFW使用的主要技术

## 深度包检测

**深度包检测（Deep packet inspection, DPI）** 是一种于应用层对网络上传递的资料进行侦测与处理的技术，被广泛用于入侵检测、流量分析及数据挖掘。就字面意思考虑，所谓“深度”是相对于普通的报文检测而言的——相较普通的报文检测，DPI可对报文内容和协议特征进行检测。

DPI是GFW检测关键词及嗅探加密流量的基础，借助硬件设施、适宜的检测模型和模式匹配算法，它能够精确且快速地从实时网络环境中判别出目标流量，并作出审查者所期望的应对措施。

被认为在GFW部署了的深度包检测包括：

* DNS协议。GFW检测所有经过骨干网国际出口路由的位于TCP与UDP的53端口上的域名查询请求，等待和处于域名黑名单中的相匹配的。
* HTTP协议。GFW检测包含用户访问的网站的域名的HTTP头中的Host字段和发送和回复全文，但对回复的检测在2008年末终止。详见：***Weinberg, Zachary; Barradas, Diogo; Christin, Nicolas. 《Chinese Wall or Swiss Cheese? Keyword Filtering in the Great Firewall of China》(PDF)*** 和 ***Jong Chun Park; Jedidiah R. Crandall. 《Empirical Study of a National-Scale Distributed Intrusion Detection System: Backbone-Level Filtering of HTML Responses in China》(PDF)***
* Tor协议。GFW无法提取出任何加密前的原始内容，但可以分辨出疑似流量。一般之后以主动探测的形式确认（详见下文#主动探测）。
* SMTP协议。GFW不仅可以检测邮件的发送人（MAIL FROM）和收件人(RCPT TO)，还可以检测邮件全文内容中的关键字，fqrouter作者将这称为“深包中的深包检测”。

![深包中的深包检测](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQqovAEW572Hrr52AX3zVkvFWa0u91MlaKCWU8tpx1aguohFz9l196vl40LV2fL8lYdIlovb5m1P71J8qgibBovWFvqtzQ2LzaNI/640?wx_fmt=webp&from=appmsg)

深包中的深包检测

* TLS协议。早期TLS版本中，服务器握手响应，包括证书，是未被加密的，GFW可以嗅探它而得知访问站点，自TLS版本1.3开始，ServerHello之后的握手信息，包括站点证书，也会被加密后传输，一般可以认为能防止对证书信息的检测；另外，SNI是TLS的一个扩展协议，该协议下，客户端在握手过程开始时告诉服务器其连接的域名，以便运作多个HTTPS网站的服务器选择并提供对应证书。而该扩展也未被加密。

## DNS污染

**DNS污染**或**网域服务器缓存污染（DNS cache pollution）**，是指由于GFW自动执行DNS劫持攻击导致DNS服务器缓存了错误记录的现象。而域名服务器缓存投毒（DNS cache poisoning）和DNS缓存投毒指由GFW执行的DNS劫持攻击，若递归DNS解析器查询上游时收到错误回复，所有下游也会受影响。

等待到深度包检测章节中的“和处于域名黑名单中的相匹配”的域名后，GFW会向查询者注入虚假DNS回复，比真的更早到达。

![GFW向查询pornhub.com的DNS请求注入伪造回复](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQomu9uYHKg5MWhUGicpWicnGNuTibibhwDG20yZshvft7RVN2ER9xZqKoVKfFnne9AOhNPCbm6Y374ApMPiaEJc6cH86l0WicgaCLVDY/640?wx_fmt=webp&from=appmsg)

GFW向查询pornhub.com的DNS请求注入伪造回复

![A记录为早已被污染的IP](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQrEoHX1kPuuNiaFl7wiahHU4JicC6LpQ9HtCTfHZfuuicyRCg6hXeA2DSNNZ0Jo9tcsYtFRe3BpicjkBc1Bpyj2wTB9DOnZEzYQTK5k/640?wx_fmt=webp&from=appmsg)

A记录为早已被污染的IP

![Dropbox公司](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpuNp3BOT9PeSJWCUVHiaQQjWCFTKT2mRVxhfb45zY3iczYAfj1kqzUfpOsBI2oibxBBGjWkyta4mHGhAibv5eR18r6sJicAWxCLwUg/640?wx_fmt=webp&from=appmsg)

Dropbox公司

![真实的DNS记录](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqfYBF0E9AYwH3ibdvDGyo58TBDthLDmoCdOncENt7JQ9dlN9UwUlyxl1H83eUZiaBXzvr2MgHoZ9KO08MUCibXpnJltAeNyA0tas/640?wx_fmt=webp&from=appmsg)

真实的DNS记录

![Reflected Networks, Inc.](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQprbnonBHQhCLTA201dpGJwoM8dlStico8bKCYVodFNPSTVdAq9DwuoPrn0Xk3HjJZj1CKJMFPFmoTGEWDCKsOfiaeTsXKkT5hzg/640?wx_fmt=webp&from=appmsg)

Reflected Networks, Inc.

由于通常的域名查询没有任何认证机制，而且域名查询通常基于的UDP协议是无连接不可靠的协议，查询者无法验证返回结果的正确性，客户端接受其伪造回复，并尝试连接其中的IP，结果往往是超时，或者出现无效TLS证书之警告。而其对TCP协议的查询则使用TCP重置攻击（详见下文#TCP重置攻击）来阻止获得任何正确结果。

此种行为自2002年开始以来有相当明确的特征。

* 伪造回复所包含的IP地址或者是保留地址、或者是固定中国境外IP集合中的一个，这些地址通常已经被屏蔽。
* 伪造回复包有固定类型。一型的TTL值和IPID固定，每次注入出现1个；二型的TTL值周期性增加、IPID递减，每次注入出现3个。两种类型都没有设置“不分片”（Don't fragment）选项。另外，2020年的研究指出有另一种新的IPID和TTL值都随机，带有“不分片”选项的回复存在。

这种注入是双向的，不仅是在中国境内查询境外DNS时、境外的DNS查询途经中国时也会出现，这导致许多国外递归DNS服务器的缓存被污染。

根据2014年的研究（详见 WinterIsComing.《分析防火长城的DNS审查》），长城防火墙的一个计算集群有360个节点，每个节点的平均处理速度是每秒2800个DNS包。
![solidot](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQrtQBaD8frdIeOf26ltjibcqxmqVBDuNVzea0lzvLZrnKLuVoUjEBJ2PqibQYy7ZPgBA6RMcVHLAjLqkTVeUrazRdO7d310ePuic4/640?wx_fmt=webp&from=appmsg)

对于加密DNS，如DoT和DoH，GFW使用基于IP端口和基于SNI的封锁。最早的封锁针对Cloudflare提供的加密DNS服务，据说其一个IP地址1.1.1.1和域名cloudflare-dns.com在2020年末被发现封锁，但是截至目前，测试发现该IP和域名已被封锁。

## TCP重置攻击

重置（reset）是传输控制协议（TCP）的一种消息，例如服务器端在没有客户端请求的端口或者其它连接信息不符时，系统的TCP协议栈就会给客户端回复一个重置通知消息，该功能本来用于应对例如服务器意外重启等情况，而GFW阻止TCP连接的技术实际上就是**比连接双方更快地发送连接重置消息，使连接双方以为对方终止了连接**。

HTTP、SMTP、HTTPS等许多应用协议都基于TCP，GFW对它们也都使用此种攻击方法。

![Connection reset error of Chromium](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQrHPZzcdwHHNxadH7Y7F4GJFRYIu8lzWluWeW0ejxkZUVqtpPV2uPsC5KmQlIJbDaRqEsoMXYoJTkWiaDgCfP96S9fZjKV3wL5A/640?wx_fmt=webp&from=appmsg)

Connection reset error of Chromium

![GFW检测到SNI包含封锁域名即注入伪造的TCP重置包](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQqfhTm2OeNx4mViaGLk81FDp4wFsglp4qZSHPvtXjpGP8YwPGgwy541Ysgmy7OnEiaWeCD4AcABwbKpBjrngzGvOG35upLLsmiaso/640?wx_fmt=webp&from=appmsg)

GFW检测到SNI包含封锁域名即注入伪造的TCP重置包

![GFW发送的重置数据包](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqBibdOxOPjIJL7VVndKqU0B0yelwryaCHVsV8BGS5MiaQVrVY4DGEb1W3xJCx7UiaPXq0iadPPFMATmEWHArmPicDRQBibJH2JnqcT4/640?wx_fmt=webp&from=appmsg)

GFW发送的重置数据包

GFW每次会注入带有一个RST选项的“一型”和多个带有RST/ACK选项的“二型”数据包，这被认为是来自两种同时部署的审查设备。一型IPID为0，具有随机的窗口尺寸，没有设置“不分片”选项；二型则有周期性增加的TTL值和窗口尺寸，并且设置了“不分片”。

## IP封锁

GFW主要采用路由扩散技术封锁特定IP地址，也就是通过将需要拦截的IP地址配置为空路由、黑洞设备或特别配置的自治系统上，在这些黑洞服务器上可以什么也不做，或者对这些报文进行分析和统计，获取更多的信息，甚至可以做出虚假回应。
正常的情况下，静态路由是由管理员根据网络拓扑或是基于其它目的而给出的一条路由，所以这条路由是正确的情况下，可以引导路由器把报文转发到正确的目的地。而GFW的路由扩散技术中使用的静态路由是一条有意配置错误的路由，其目的是**为了把本来是发往某个IP地址的报文引导到一个“黑洞服务器”上**，而不是把它们转发到正确目的地。通过动态路由协议的路由重分发功能，这些错误的路由信息可以发布到整个网络。

## 主动探测

自2011年10月以来（详见 blackhat.《中国刺探加密连接测试新屏蔽方式》），防火长城通过主动探测（Active probing）识别翻墙服务器，并随后将其封锁。其主要针对以下目标。

* 任何加密连接，包括SSH和Tor，并不针对特定协议。这是最早出现的探测。每当中国用户尝试加密连接，防火长城发送“垃圾二进制（garbage binary）探针”，一系列伪随机数据，在建立加密连接前先访问目标计算机，其目的在于在用户建立加密连接前嗅探出他们所使用的反审查工具，任何从中国访问境外HTTPS 443端口的连接都会在几乎实时的情况下被刺探。
* Tor。2011年10月起，防火长城的深度包检测设备已能识别Tor指纹。当中国的Tor客户端试图与境外Tor网桥建立连接，防火长城会在每15分钟周期（如15分钟后，30分钟后）内发送探针会尝试与Tor进行SSL协商和重协商，但目的不是建立Tor连接，每次探测持续3分钟。这种探测还会在春节等假期期间停止。而2015年的研究指出，防火长城已经可以实时主动探测Tor网桥，而不是每15分钟执行一次。被探测的网桥类型包括obfs2和obfs3等。
* SoftEther VPN。2015年9月发现。起初使用固定的IP，如210.72.128.200，被屏蔽之后使用亚马逊EC2等云服务发起探测，模仿SoftEther的客户端握手去识别有效的SoftEther的IP。
* AppSpot。2015年9月发现，目的是为了识别并封锁可用的Google的IP，干扰使用该服务翻墙的GoAgent。探测请求有相似的Host头和固定的用户代理。
* Shadowsocks。可能是从2019年5月开始的（详见 Anonymous, Anonymous, Anonymous, David Fifield, Amir Houmansadr. 《Shadowsocks 是如何被检测和封锁的》）。

# 绕过GFW的主要技术

## 全加密协议

**全加密协议** 对数据包有效载荷的每一个字节都进行了加密，不同于像TLS这样的协议以明文握手开始，完全加密（随机化）的协议被设计成**连接中的每个字节都与随机数据没有区别**，以便让流量"看起来什么都不像"。
2021年11月初，GFW部署了一种新的审查技术，这种技术可以实时地被动检测并阻断全加密流量。GFW这一新添的审查能力影响到一大批流行的翻墙协议，包括但不限于Shadowsocks、VMess和Obfs4。虽然GFW长期以来一直采用*主动探测*来识别此类协议，但这次是第一次有关于采用纯*被动检测*来识别全加密流量的报告。

Tschantz等人将混淆翻墙流量的方法分为两类：**隐写(steganography)** 和 **多态(polymorphism)**。

**隐写代理的目标是使翻墙流量看起来像应该被允许的流量；多态性的目标是使翻墙流量看起来不像应该被禁止的流量**。

### 隐写

实现隐写术的两种最常见的方法是**模仿(mimicking)** 和 **隧道传输(tunneling)**，让混淆协议的指纹和正常协议完全一致，从而避免基于协议指纹的检测和封锁。
但这种方式有根本性的缺陷，即使使用隧道传输，翻墙软件的设计者也需要复杂的额外操作。

在2012年开始，GFW部署了深度包检测系统（详见上文#深度包检测），这使基于隐写的协议基本都失效了。因为只要进行额外操作，就会留下痕迹，为了避免这个缺陷，现在活下来的流行软件都选择了多态设计。

### 多态

实现多态性的一个常见方法是：**从连接中的第一个数据包开始，就对其有效载荷进行完全加密**。因为没有任何明文或固定的包头结构指纹，所以GFW没办法简单地使用正则表达式或通过寻找流量中的特定模式来识别代理流量。

这种设计在2009年首次被引入Obfuscated OpenSSH中。此后，Obfsproxy、Shadowsocks、Outline、VMess、ScrambleSuit、Obfs4都采用了这种设计。Geph4、Lantern、Psiphon3和Conjure也部分采用这种设计。

这种加密模式就是完全加密流量，这种流量看上去什么都不像，又没有任何特征，看起来和无意义的随机数据一样，但是事实上，这种流量有一种和其他流量不同的重要特点：没有可识别的头，**整个连接中的流量都是均匀且高熵的，甚至在第一个数据包中就已经如此**。

至于香农熵的概念这里不做过多介绍（其实是我也一知半解），感兴趣的可以自行搜索。

> 2015年，Wang等人利用连接中第一个数据包有效载荷的长度和高香农熵的特点来识别随机流量，比如Obf...