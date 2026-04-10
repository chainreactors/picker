---
title: 好好吃饭 打好基础之初遇wsdl
url: https://mp.weixin.qq.com/s/80LZSVA1G-7ISl-mEirn8w
source: Doonsec's feed
date: 2026-04-09
fetch_date: 2026-04-10T04:44:31.651577
---

# 好好吃饭 打好基础之初遇wsdl

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/jS2mB7OlsdUbx6CAEnFm00D6j6hs6z3mU5SrIVyOOj3bG1ozJHcOEbo2jpRa84TDfoc8zLCjx2ubfskotuniaiabVOojIcLRibrXVnUibbM9eUs/0?wx_fmt=jpeg)

# 好好吃饭 打好基础之初遇wsdl

蚁景网络安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于Tide安全团队
，作者swordlover

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7f2r4cHKV0tKOK4v87qvAYZazjibgqC5HkYyaQeibGau4g/0)

**Tide安全团队**
.

Tide安全团队以信安技术研究为目标，致力于分享高质量原创文章、开源安全工具、交流安全技术，研究方向覆盖网络攻防、Web安全、移动终端、安全开发、物联网/工控安全/AI安全等多个领域，对安全感兴趣的小伙伴可以关注我们。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png)

#### "Nothing happens without a cause." --斯宾诺莎 (Baruch Spinoza)

曾经有一个眼神清澈的青年，他在酒店房间中快速浏览着网页，渐渐的，他面红耳赤、心跳加速、~~荷尔蒙侧漏~~，突然，他看到了一个令他不解的东西，一个条链接的后面赫然挂着?WSDL。这是什么，难道建立这个网站的人想告诉世人，我(W)是(S)大(D)佬(L)吗？为了弄清楚一切，这位青年，开始翻阅起资料......

# 一、扒一扒WSDL的底

WSDL（Web Services Description Language，Web服务描述语言）是一种基于 XML 的语言，用于描述网络服务的具体功能。 它的主要目的是告诉外界：

> “我这里提供了一个服务。” “这个服务可以通过什么方式访问（地址、协议）。” “这个服务里有哪些可以调用的方法（函数）。” “调用这些方法需要传入什么参数，参数是什么类型。” “调用成功后，它会返回什么样的数据。”

文字叙述难以理解，找个有关网站我们看一下：

```
QUAKE:body:"<wsdl:" AND title: "WebService Web 服务"
```

正常打开的界面如下，这也是个特征，.net的基本都长这样。

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdWczUdGO62lu04H26RLoUJ9fwo6VFnseKeJ28QR6ZM8F0BBaGPBgC6EDvxYBthPWjotjk8TS4AFzRJW9iaklK3qLaQZkgextnOI/640?wx_fmt=png&from=appmsg)

然后http://yoururl?wsdl，这样就可以看到XML了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdVNTV1BCicn9ibDqRVyGgwPweTx7m0UX82I8SDOaImasPicRKWpsicsWzORT5ia26UicM80CIQBj5cpXt010j9eIULiacRWvSzicwEcSns/640?wx_fmt=png&from=appmsg)

可以看到打开以后能看到一大片标签（这里就不展开内容了，要打码，打码看多了对身体不好），这些标签的意思大概如下：

> 1. types:定义参数和返回值的数据类型（比如字符串、整数、或是自定义的复杂对象）。
> 2. messages:说明每个功能需要什么输入（参数）和会产生什么输出（返回值）。
> 3. portType:说明服务提供哪些大类功能（操作）
> 4. binding:说明服务使用的通信协议（如 SOAP over HTTP）
> 5. service:如何连接到服务

当然，在任何资料里寻找WSDL都会发现和SOAP密不可分

那他们的关系呢，我们用个例子来说 假设有个服务器，发布了一个WSDL，提供查询开房次数功能

```
<!-- 示例：WSDL中定义的查询开房次数记录操作 -->
<wsdl:operation name="getkaifanglog">
  <wsdl:input message="tns:getkaifanglogRequest"/>
  <wsdl:output message="tns:getkaifanglogResponse"/>
</wsdl:operation>
```

这时候，来一个年轻的女孩叫小美，他看到了这个WSDL，想查询男朋友小帅的开房记录，于是他构造了SOAP请求。

```
<soap:Envelope xmlns:soap="...">
  <soap:Body>
    <getkaifanglog xmlns="http://example.com/xxx">
      <name>小帅</name>
    </getkaifanglog>
  </soap:Body>
</soap:Envelope>
```

服务器查询到了小帅的开房记录，并用SOAP的形式告诉了小美。

```
<soap:Envelope xmlns:soap="...">
  <soap:Body>
    <getkaifanglogResponse xmlns="http://example.com/kaifanglog">
      <number>2,147,483,647</number>
    </getkaifanglogResponse>
  </soap:Body>
</soap:Envelope>
```

小美伤心欲绝，从此发誓要远离渣男，并留下了这么一张图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdUy4GQ7rvqt4QeVId8j9jX1vSmZDM5DX49KfKCqbp2nZLVr2fs4MbIHYbjYZl20Q9jXcOhtSicoibD3WdvymnLTeuVpbrPJA1icmE/640?wx_fmt=png&from=appmsg)

总结一句话：WSDL 是一份基于 XML 的详细说明书，它告诉客户端如何与一个 SOAP Web 服务进行交互，包括服务地址、可用方法和参数格式。

# 二、WSDL相关的一些漏洞利用

以下截图均为个人内网环境靶场！既然提到了wsdl，就有看了看相关的一些漏洞以及佬们用的工具。（此处非常基础，佬们可以小手点点赞然后退出就好了嘿嘿嘿） 1、信息泄露（用户枚举） 个人理解，既然暴露了如何交互，就可以利用它去尝试找可以暴漏用户信息的地方，例如：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdXDpZRibnL6ox9BDiawdCcE6N1uibG3PUWXmtGZEfn8dHpKLGLWGDNt6jAldSibxzicicePibWNHjA7o3ZYohiaeUZk1dKkVrWaq7TiakMM/640?wx_fmt=png&from=appmsg)

2、常见web漏洞如xxe、sql注入:

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdUrAmf87p2EPibib30STRl5NiaFTSLYBeZibZBh3T62FW9O3biavP9P7ZXDDvc3o0DxgAx2d87UbKCE6eP4FYgibZfITxeQOibxrTOfZQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdXBUic1icNjicicWEkXTnLuiaOgvBbRo66bL4dsbtCuxBia83xkZhseeZlmH31ictE6vVVAQf8iaTA0DV5UQCayfMacU5LoRL6XvHuDb6M/640?wx_fmt=png&from=appmsg)

3、一定要写大佬们都推荐的工具-Wsdler burp商店自带，下载非常便捷

![](https://mmbiz.qpic.cn/mmbiz_png/jS2mB7OlsdWcsqI3UYw6gUHFYxicuNSy54icWEjjbGqQicsQJ9qfhPkehMqA2jPtmQubYyPvNxpkKib3DeIbnHWE5shjXWibHj2Wr4ZCYFnh0qmQ/640?wx_fmt=png&from=appmsg)

找到扩展，点击直接使用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdWhGWqud2RUiaePoW7OZqcSaLia6tNNLInyxO9lvJYzGNP01CG8rJWzb4lz9LLfRrutodZryskDPrvfkuvt9xJ9rLTWkBMQbwib6I/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/jS2mB7OlsdV2jf6Ojcnv1t2rGrIPfShHIrQlguFmxjclZ84e610Dqr7g52SzCHvaibe1oVYib7D3tYh9TCiaaRAWbL1icxic779wHgxwBJsaGu3I/640?wx_fmt=png&from=appmsg)

有问题的地方直接就显示出来，可以转发到重发器里自己再搞一搞（非靶场环境下记得做好安全措施哦）

# 三、防御建议

1. 生产环境中禁用或限制WSDL访问（例如，仅允许内网IP访问？wsdl）。
2. 使用严格的XML解析器，禁用DTD、外部实体（resolve\_entities=False）。
3. 对所有输入进行严格的校验和净化（白名单）。
4. 使用预编译的参数化查询（防止SQLi）。
5. 实施严格的基于身份验证和授权的访问控制。

[![](https://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldwoHriaVoyA6JNsGroYQAQp8xrlxS8RibJWibDF8T1pmkgSXqiaWQvmVB43S1IVCFBDOKTEQFDAP0QL5g/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkxNTIwNTkyNg==&mid=2247549615&idx=1&sn=5de0fec4a85adc4c45c6864eec2c5c56&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

蚁景网络安全

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5znJiaZxqldxTbkTSkrHtQAicCy4EPuqw9hf0VFTmn6c4UGChaiaoHSBewgtiblmSAOPRq8CmibczDaBzzpfN5IkrFQ/0?wx_fmt=png)

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