---
title: 详细讲解kerberos认证全过程、黄金、白银票据
url: https://www.freebuf.com/defense/375342.html
source: FreeBuf网络安全行业门户
date: 2023-08-19
fetch_date: 2025-10-04T12:00:26.512370
---

# 详细讲解kerberos认证全过程、黄金、白银票据

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

详细讲解kerberos认证全过程、黄金、白银票据

* ![]()
* 关注

* [攻防演练](https://www.freebuf.com/articles/defense)

详细讲解kerberos认证全过程、黄金、白银票据

2023-08-18 09:23:16

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

Kerberos认证在域渗透的作用不容小觑，刚开始学的时候觉得挺复杂、挺难记的，仔细学了一段时间，自己梳理了整个流程之后对Kerberos认证具有更多的、更深入的认识，以下是我对与Kerberos认证的理解，内容包含了我在学习过程中的一些困惑，希望有助于各位对于Kerberos认证流程、黄金票据、白银票据的学习与记忆。
参与Kerberos认证的有三个角色：客户端（client简写c）、服务端（server简写s）、DC（域控），而DC中有一个叫密钥分发中心的组件即KDC，它负责处理用户身份验证和授权请求。KDC包含两个主要子组件：认证服务（AS）和票证授予服务（TGS）。以下是我画的Kerberos认证整个流程图，不好看大家见谅！！

![1692321518_64dec6eecb3741684ddfa.png!small](https://image.3001.net/images/20230818/1692321518_64dec6eecb3741684ddfa.png!small)
第一步：客户端向DC的AS请求

![1692321536_64dec7008a05c21cf3a01.png!small](https://image.3001.net/images/20230818/1692321536_64dec7008a05c21cf3a01.png!small)

此时客户端本机的Kerberos服务会向KDC的AS认证服务发送AS-REQ认证请求，请求内容包括了客户端的个人信息即principal如用户名，以及说明要请求什么服务、目标服务的主机名等信息，也告诉AS自己将与TGS通信。除此之外为了防止别人伪造这个客户端的身份，还要求发送一个认证因子authenticator，这个认证因子需要使用客户端的hash来加密一个时间戳。
为什么需要用自己的hash加密时间戳？
因为如果不用客户端的hash进行加密，那么攻击者可以伪造任意客户端的身份进行Kerberos认证，但是加上客户端hash进行加密，DC再进行解密，这使得攻击者的攻击加大难度，只有获取了用户的hash才能伪造客户端的身份。另外DC是域控，肯定是有客户端的hash的。
时间戳的作用是什么？
是为了一定程度上防止攻击者进行重放攻击。请求接收方会对这个时间戳做一个验证，在请求发送到请求接收的一定时间内，假设为5分钟，在这5分钟内接收方收到了请求，那么就相信其为安全的请求，反之如果超过了5分钟则怀疑受到了重放攻击。
第二步：DC的AS向客户端的请求做出响应

![1692321571_64dec7233947091311172.png!small](https://image.3001.net/images/20230818/1692321571_64dec7233947091311172.png!small)

此时AS收到了客户端的请求之后，由于AS是在DC上面的，DC是有客户端的hash的，此时会查询AD目录找到该客户端的hash，然后对时间戳进行解密，如果解密失败说明用于加密的hash是错误的，同时验证是否为受到了重放攻击。
在AS验证通过之后，AS会生成一个login session key，并且使用用户的hash加密这个login session key，然后AS还会生成一个TGT，同使用过hash加密后的login session key以及一些其他相关信息打包发送给客户端。
什么是TGT？
是Kerberos认证中的一种加密票据，是由Kerberos认证服务器（AS）生成并加密的，该TGT包含了用户的身份信息、有效期限、密钥（login session key）和其他相关信息，不过这些信息是使用的krbtgt的hash进行加密的，不在是用户的hash了。
什么是krbtgt？
krbtgt是Kerberos中的一个特殊账户，用于存储和管理Ticket Granting Ticket（TGT）。在Kerberos认证系统中，krbtgt账户是一个系统级别的账户，用于生成TGT和使用自己的hash（krbtgt hash）加密TGT，并提供给用户进行身份验证和获取服务票据。那么如果攻击者获取到了这个hash（krbtgt hash），那么就可以任意的伪造TGT了，也就是黄金票据，拥有了黄金票据就可以跳过AS验证了。
为什么TGT要用krbtgt的hash加密？
因为在攻击者未获取krbtgt的hash时，使用krbtgt的哈希加密可以防止TGT在传输过程中被篡改或伪造。如果使用明文，还可能被中间人窃取数据包，获取一些敏感信息。
第三步：客户端向DC的TGS请求

![1692321627_64dec75b1a5083d9f17c9.png!small](https://image.3001.net/images/20230818/1692321627_64dec75b1a5083d9f17c9.png!small)

此时客户端收到了DC的的响应包之后会将收到的TGT存储在本地，并使用自己的hash将对应使用自己的hash加密的信息进行解密，获取到AS生成的login session key，然后客户端使用login session key去加密时间戳然后与收到的TGT、需要的服务名字、自己的相关信息一同打包发送到DC的TGS。
为什么客户端收到TGT之后还要发送回去？
客户端发送TGT是发送给TGS的，在AS发送给客户端TGT之后，客户端需要将其发给TGS之后，TGS才会给客户端授予服务票据。
为什么客户端收到TGT之后要存储起来？
因为TGT是具有时效性的，不是永久的，也不是一次性的。只要在TGT过期之前，可以直接请求TGS申请服务票据，而不用在每次访问服务的时候都向AS请求TGT，减少了与AS的通信，提高了系统的性能和效率。
第四步：DC的TGS向客户端的请求做出响应

![1692321638_64dec766502dd792e32d3.png!small](https://image.3001.net/images/20230818/1692321638_64dec766502dd792e32d3.png!small)

当TGS接收到请求之后，会检查自身是否存在客户端请求的服务，如果存在就会拿ktbtgt hash解密TGT（由于TGS是在DC上的，所有具有krbtgt的hash），解密到的信息中包含了login session key，别忘了客户端发过来的时间戳就是利用login session key加密的，此时就可以用其解密获取到时间戳了，然后验证时间戳。
然后KDC会生成一个新的名叫service session key，用于客户端和服务端直接的安全通信，并且为客户端生成ST服务票据，该票据是由客户端信息+service session key打包后用后用服务端的hash加密的（KDC在DC上，故DC拥有服务端的hash）。除此之外会将service session key用之前是login session key加密同ST一同打包发送给客户端。
为什么service session key要用login session key加密？
因为是service session key是要发给客户端的，客户端拥有login session key，可以解密后获取到service session key，也保证了service session key的安全性。
为什么要生成一个service session key？
这个是为了用于接下来的客户端与服务端的安全通信，作用类似于login session key。
为什么要用服务端的hash加密service session key？
因为为了保证service session key不被窃取不可明文传输且后期客户端和服务端要使用service session key进行安全通信，而服务端没有login session key，DC就使用服务端的hash进行加密，同时还可以防止非目标服务器窃取这个service session key，因为只有知道服务端的hash才能获取service session key，进一步保证了service session key的安全。如果攻击者窃取了服务端的hash那么就可以任意伪造ST也就是白银票据了，就可以不经过KDC了。
第五步：客户端向服务端请求

![1692321650_64dec772053f4aed2bf1b.png!small](https://image.3001.net/images/20230818/1692321650_64dec772053f4aed2bf1b.png!small)

此时客户端接收到了TGS的响应，然后利用login session key解密获取到service session key，然后用于与服务端通信，同时将ST存储起来，然后客户端用service session key加密客户端信息和时间戳同ST（服务端hash加密的相关信息+service session key）打包一起发送给服务端验证。
第六步：服务端向DC的KDC的请求

![1692321659_64dec77b592f76b92d5ce.png!small](https://image.3001.net/images/20230818/1692321659_64dec77b592f76b92d5ce.png!small)

客户端收到服务端发送过来的信息之后，用自己的hash即服务端hash解密ST，而ST中包括有service session key，那么再用service session key去解密使用service session key加密的信息包括有客户端相关信息和时间戳，再去验证这个时间戳，判断是否安全，判断是否为真实身份。
除此之外服务端还要向DC请求，使用PAC（Privilege Attribute Certificate）将客户端的属性信息发送给KDC进行验证客户端是否安全是否具有获取该服务的资格。
什么是PAC？
PAC是一个包含了客户端属性信息的数据结构，它包括了客户端的授权信息、组成员资格和其他相关属性。服务端在收到客户端的票据后，会从票据中提取出PAC，并将其发送给KDC进行验证。
验证过程是什么？
1.服务端从客户端的票据中提取出PAC。
2.服务端将PAC发送给KDC，请求对客户端的属性信息进行验证。
3.KDC收到PAC后，会验证其中的属性信息是否与KDC中存储的客户端属性信息一致。
4.如果属性信息一致，KDC将返回一个验证成功的响应给服务端。
5.服务端根据KDC的响应，判断客户端的属性信息是否有效，并根据需要进行授权或其他操作。
第七步：DC的KDC向服务端响应

![1692321678_64dec78ec6fc61b0e0c8d.png!small](https://image.3001.net/images/20230818/1692321678_64dec78ec6fc61b0e0c8d.png!small)

此时KDC将会对服务端发来的PAC进行一个验证，验证流程如下
1.KDC首先会检查PAC中的票据（Ticket）是否有效，即检查票据的签名是否正确、是否过期等。这是基本的票据验证过程，确保票据本身是合法的。
2.KDC会从PAC中提取出客户端的属性信息，如授权信息、组成员资格等。
3.KDC会与自身存储的客户端属性信息进行比对，以验证PAC中的属性信息是否与KDC中存储的信息一致。这样可以确保客户端的属性信息没有被篡改或伪造。
4.如果PAC中的属性信息与KDC中存储的信息一致，KDC将认为PAC是有效的，并返回一个验证成功的响应给服务端。反之如果PAC中的属性信息与KDC中存储的信息不一致，KDC将认为PAC是无效的，并返回一个验证失败的响应给服务端。
第八步：服务端向客户端响应

![1692321689_64dec7998bf206f4a1cf6.png!small](https://image.3001.net/images/20230818/1692321689_64dec7998bf206f4a1cf6.png!small)

此时服务端会生成一个票据，该票据包括客户端身份信息，以及服务端的身份信息，并使用之前获得的service session key去加密该票据信息并发送给客户端，然后客户端就可以正常获取到服务端的服务了。
为什么要使用service session key去加密该票据信息？
因为之前KDS已经给客户端发送过了service session key，而service session key就是用来二者安全通信的，故客户端可以使用service session key去解密获取到票据信息。service session key加密同时也保障了票据信息不被窃取和修改伪造。

# 渗透测试 # 网络安全 # 系统安全 # 内网渗透 # 网络安全技术

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.m...