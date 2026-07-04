---
title: 防火墙到底有哪些类别？从工作原理看懂防火墙的发展
url: https://mp.weixin.qq.com/s/IC3zYz6m6LcTTqcQb9P4DQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:39:23.779595
---

# 防火墙到底有哪些类别？从工作原理看懂防火墙的发展

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BXRyxzSJEtTfEvcXXlrkMkhbxNfkV86HmB4ticpuuSaAI32ichJYmleea5ib3vaic2K8nF4G4F1f9ibR4P71YlVdic0yg3ETE9dKZiaNE3I1AHjvxg/0?wx_fmt=jpeg)

# 防火墙到底有哪些类别？从工作原理看懂防火墙的发展

原创

Zero老Z
Zero老Z

SecLab安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

|  |  |  |  |
| --- | --- | --- | --- |
| |  | | --- | | **> NOTICE:** 欢迎关注我们，获取最新漏洞情报与红队实战技巧。 |  |  |  | | --- | --- | | ● NODE: SEC\_STATION\_0x2F | SYSTEM\_STATUS: ONLINE | |
| 很多人刚开始学防火墙，都会被各种名字绕晕。  Windows Defender Firewall 是防火墙。 FortiGate 也是防火墙。 WAF 也叫防火墙。 云上还有安全组、云防火墙、Web 应用防火墙、数据库防火墙。  名字都叫防火墙，但看起来又完全不是一回事。  所以新手很容易产生一个疑问：  防火墙到底有多少种？为什么不同教材、不同厂商、不同课程里的分类都不一样？  其实原因很简单。  大家不是在回答同一个问题。  有人按部署位置分类，所以会说主机防火墙、边界防火墙、云防火墙。  有人按产品形态分类，所以会说软件防火墙、硬件防火墙、虚拟防火墙。  有人按保护对象分类，所以会说 Web 应用防火墙、数据库防火墙、工业防火墙。  这些说法都没错。  但如果你是想真正理解防火墙，而不是背一堆名词，我建议先按工作原理来学。  因为工作原理回答的是一个更底层的问题：  防火墙到底靠什么判断流量该不该通过？  这个问题想明白了，后面再看各种产品名称，就不会乱。  ![](https://mmbiz.qpic.cn/mmbiz_png/BXRyxzSJEtSd3R7aOjqXUibjYBScUb0DRNbzU8eomicAxkR8qtR0YQ74mKicH0FMzCJsSHHY8LB8M2J2gzIiaK5WEta8vCKqRaKC75jk1kibpCOE/640?wx_fmt=png&from=appmsg) 早的防火墙，只是在看数据包 ![网络安全的守护者:防火墙的五个主要功能解析](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BXRyxzSJEtQbLA0OjHzEKgFIqL6R2z31v4do3tpnudibI8dEYWBQZIX3b5nV2ZjwVpxxFN8MJdDN67ziclzZlmL7AuBDWoMV3Uq3MJVjCecgY/640?wx_fmt=other&from=appmsg)  防火墙刚出现的时候，面对的问题很直接。  网络越来越开放，服务器开始暴露在互联网上。人们需要一个东西守在入口，决定哪些流量可以进来，哪些流量必须挡住。  于是，包过滤防火墙出现了。  它的思路很朴素。  来了一个数据包，防火墙就看几个字段：  源 IP 是谁？ 目标 IP 是谁？ 用的是什么协议？ 访问的是哪个端口？  如果规则允许，就放行。 如果规则不允许，就丢弃。  比如，你可以设置一条规则：  允许内网访问外网的 80 和 443 端口。 禁止外部主机直接访问内网数据库端口。  这就是最早、也最基础的访问控制思想。  包过滤的优点很明显：快，简单，成本低。直到今天，我们在路由器 ACL、安全组、基础防火墙规则里，仍然能看到它的影子。  但它也有一个天然缺陷。  它只看眼前这个数据包。  它不知道这个包从哪里来，也不知道它属于哪一次通信。它更像一个只看身份证和门牌号的门卫，能判断“这个人看起来能不能进”，但不知道这个人是不是刚才已经登记过，也不知道他和前面那个人是不是一伙的。  网络流量不是孤立的数据包。  它是一段连续的对话。  于是，防火墙需要“记忆”。 状态检测让防火墙开始记住连接 ![服务器上如何管理和配置防火墙以控制端口访问？有哪些防火墙规则策略？ - 梦飞idc云平台](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BXRyxzSJEtS4I2NK5MN7SnrplH9VQ0vQTzrNHjtq0g6mzC7ibLZubD2GLXa1VxPXrBEQGLXSm6sARq3QTuQ4ibZgWJliajibT9jCIjR59zKA5bQ/640?wx_fmt=other&from=appmsg)  状态检测防火墙解决的，就是这个问题。  它不再只看一个数据包，而是开始记录连接状态。  谁先发起连接？ 三次握手有没有完成？ 这个返回包是不是属于已经建立的连接？ 这条通信现在处于什么状态？  有了状态检测，防火墙就不只是“看包”，而是在“看连接”。  这一步非常关键。  比如内网用户访问一个网站，客户端先向外发起连接。网站服务器返回数据时，包的方向变成了从外到内。如果只看单个数据包，防火墙可能会觉得：外部流量正在进入内网，应该拦截。  但状态检测知道，这个返回包属于内网刚刚主动发起的一次连接，所以可以放行。  防火墙从这里开始变聪明了。  它不再只是机械地检查 IP 和端口，而是能理解一次通信的上下文。  直到今天，状态检测仍然是企业级防火墙的核心能力。FortiGate、Palo Alto、Cisco ASA、华为 USG 这类产品，本质上都离不开状态检测。  现代防火墙真正管理的对象，已经不是一个个孤立的数据包，而是一条条网络连接。 应用代理让防火墙开始理解协议 但网络继续发展以后，问题又变了。  越来越多业务跑在 HTTP、HTTPS、FTP、SMTP 这些应用协议上。对传统防火墙来说，TCP 80 端口只是 80 端口，TCP 443 端口只是 443 端口。  至于里面传的是正常网页、恶意文件、SQL 注入，还是命令执行攻击，它并不知道。  这就像门卫知道有人进了办公楼，却不知道他进来以后到底在干什么。  于是，应用代理型防火墙出现了。  它不满足于判断“这条连接能不能建立”，而是进一步理解应用协议本身。  HTTP 请求长什么样？ FTP 是怎么建立控制连接和数据连接的？ SMTP 邮件传输里哪些内容可疑？ Web 请求里的 URL、Header、Cookie、参数分别是什么？  应用代理会站在客户端和服务器中间，替双方转发通信，同时检查应用层内容。  这类防火墙的好处是看得更细。  它可以根据应用协议制定更精确的安全策略，而不是只停留在 IP 和端口层面。  代价也很明显：更复杂，更消耗性能，对协议解析能力要求更高。  但从技术演进的角度看，这一步很重要。  防火墙开始从网络层走向应用层。  它不只是问：“谁在访问谁？”  它开始问：“他们到底在说什么？” WAF 为什么也叫防火墙？ 理解了应用代理，就更容易理解 WAF。  WAF，也就是 Web 应用防火墙，它保护的不是所有网络流量，而是 Web 应用。  普通网络防火墙更关心 IP、端口、连接、应用识别。  WAF 更关心 HTTP/HTTPS 请求本身。  比如：  URL 有没有异常？ 参数里有没有 SQL 注入？ 请求体里有没有 WebShell？ Cookie 有没有被篡改？ 接口访问频率是不是异常？  所以 WAF 当然也是防火墙，但它不是传统意义上的边界防火墙。它更像是专门站在 Web 应用门口的检查员。  网络防火墙关心“这条路能不能走”。  WAF 关心“这个请求是不是有问题”。  这也是很多人刚学习时容易混淆的地方。  “防火墙”不是某一种固定设备，而是一类安全控制思想。只要它站在通信路径上，根据规则决定流量是否允许通过，就可以被称为某种意义上的防火墙。  只是它看的层次不同。 下一代防火墙不是推翻前面，而是叠加前面 今天我们经常听到一个词：下一代防火墙，NGFW。  这个名字听起来很新，好像和传统防火墙完全不是一回事。  其实不是。  下一代防火墙并没有抛弃包过滤、状态检测和应用层检查。相反，它是在这些能力之上继续叠加。  一台典型的 NGFW，通常会同时具备这些能力：  它能做基础访问控制。 它能维护连接状态。 它能识别应用。 它能结合用户身份制定策略。 它能做入侵防御、恶意文件检测、URL 过滤、威胁情报联动。  也就是说，NGFW 不只是问：  这个 IP 能不能访问那个 IP？  它还会继续问：  这是什么应用？ 是谁在访问？ 这个行为是否异常？ 里面有没有攻击载荷？ 这个目标是不是已知恶意地址？  防火墙看到的东西越来越多，判断依据也越来越复杂。  从这个角度看，下一代防火墙不是一个突然冒出来的新物种，而是防火墙长期演进的结果。 防火墙的发展，其实是在不断理解流量 回头看这条线，就会清楚很多。  包过滤防火墙看的是数据包。 状态检测防火墙看的是连接。 应用代理防火墙看的是协议内容。 下一代防火墙看的是应用、身份和威胁。  防火墙每进化一次，本质上都是看得更深一点。  最早，它只知道“这个包从哪里来，要到哪里去”。  后来，它知道“这是不是一条已经建立的连接”。  再后来，它能看懂“这条连接里跑的是什么协议”。  到了今天，它还要判断“这个应用行为背后有没有风险”。  所以，防火墙的发展史，其实就是防火墙越来越理解网络通信的历史。  理解了这条主线，再去看不同厂商的产品，就不会觉得那么零散。  主机防火墙、边界防火墙、云防火墙，是部署位置不同。  硬件防火墙、软件防火墙、虚拟防火墙，是产品形态不同。  WAF、数据库防火墙、工业防火墙，是保护对象不同。  包过滤、状态检测、应用代理、下一代防火墙，才是在回答工作原理不同。  这几套分类不是互相冲突，而是在不同角度描述同一类东西。  如果你刚开始学习防火墙，别急着背所有名词。先抓住一条线：  防火墙到底看什么？  看数据包，是包过滤。 看连接状态，是状态检测。 看应用协议，是应用代理。 看应用、身份和威胁，是下一代防火墙。  这条线抓住了，防火墙的分类就不再是一堆名词，而是一段技术发展的过程。  既然包过滤是一切的起点，下一篇我们就从它开始。 |
| |  | | --- | | 历史文章合集 History Archive Collection |  |  |  | | --- | --- | | [渗透与红队攻防](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4399363479745380353#wechat_redirect) | [Web安全应用漏洞](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4399350075873869826#wechat_redirect) | | [漏洞情报与预警](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4331154621957144587#wechat_redirect) | [工具与 OSINT](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4399378218932289539#wechat_redirect) | | [系统与运维安全](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4399421474839773187#wechat_redirect) | [协议与网络基础](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4399402277543919620#wechat_redirect) | | [行业观察与管理哲学专题](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4399443947383734274#wechat_redirect) | | | [周报与随笔](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4063548764156559362#wechat_redirect) | [杂项](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzI5MjY4MTMyMQ==&action=getalbum&album_id=4399444541079076865#wechat_redirect) |  |  | | --- | | --- END\_OF\_SESSION // SEC\_COMPLIANT --- | |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Bvow4Cv9oZ3Niaq1oRhfNZdtUP37c59CqD0UQXxWYSo0Cl4TrNgFhApzDstFhlPtGI6BlPvU4Ttico80OWHDRJ2g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过