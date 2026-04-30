---
title: Ghost Bits，Java WAF之殇？
url: https://mp.weixin.qq.com/s/JaxVrys8tqGnXsWhfFzAPw
source: Doonsec's feed
date: 2026-04-29
fetch_date: 2026-04-30T05:28:08.943203
---

# Ghost Bits，Java WAF之殇？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gIBYXIMwxtsgIV3KAAn190EmGuNtw7nNc8PV57cXURXtjj9Lk2VBvUT3LiabeEkTSW4kPsbp7dbCV2I0b3syFkgjILggpria5b7pjYqJAsFao/0?wx_fmt=jpeg)

# Ghost Bits，Java WAF之殇？

原创

LoRexxar
LoRexxar

LR的安全自留地

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

在前两天的BlacksetHat Asia 2026上，@浅蓝和@1ue分享一个非常有趣的议题，Java中的GhostBits漏洞

* • https://i.blackhat.com/Asia-26/Presentations/Asia-26-Bai-Cast-Attack-Ghost-Bits-4.23.pdf

探究深度非常深，影响范围非常之广，内容非常有意思

# 什么是Ghost Bits？

Ghost Bits这个概念的来源太久很难深究，甚至在软件领域之前就已经有类似的概念。**Ghost Bits主要是指那些在莫名其妙的位置影响到软件运行的位，所以形容像幽灵一样。**

在这个议题中，**Ghost Bits主要指的是在某些类型转换过程中被不小心丢掉的高位，导致原字符串内容变化。**

最经典的场景就是**char类型和byte类型的转换**，也是Java的经典场景。

**char类型是16位（2字节），byte类型是8位（1字节）**，如果发生char强制转换为byte就会丢弃高8位，**只保留低8位**。其中的8位就像幽灵一样消失了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gIBYXIMwxtsT9fJPIh0vWrWIajIYpTsqUYIz10vlND7PqDqaLicqMhHxzYnWecHaia5TzatojDtdVeYbMlmBwOxcJ6G9aV4icgun5AtnXTuREA/640?wx_fmt=png&from=appmsg "null")

在Java中，**有4种非常常见的写法**都会有该问题

* • `(byte) ch`：显式的byte强制类型转化
* • `ch & 0xFF`：位掩码，保留低8位
* • `OutputStream.write(int)`：写入流时被截断
* • `DataOutputStream.writeBytes()`：官方JDK方法，在文档中明确写明会丢弃高8位

![](https://mmbiz.qpic.cn/mmbiz_png/gIBYXIMwxtth3suAm266aKOeWFicmQDEJ7p3icv8ARzhxWiaO7DhG4CyEncD1hVuJerBqdoRBkM9lhIicZlREwspanOPGLiaIkKv9xTNKOiaqCgcg/640?wx_fmt=png&from=appmsg "null")

而在unicode中，会有大量的高位内容，经过处理和转换之后就会被截断变成对应的字符
![](https://mmbiz.qpic.cn/sz_mmbiz_png/gIBYXIMwxtvkianNHqK5UUw9eM4nHGicibib49DVLZs35tiaAf4uU2qEtwhdb0Qut85Ky50VSF17peXp0ZZeNa9PDnIaHDliboOZajUPogPct0Oac/640?wx_fmt=png&from=appmsg "null")

要注意的是，这个问题本质上**在源代码层面表现一致，不能单独算作是一个漏洞**，所以在80%的场景下，该问题主要影响的是**和源代码不在同一层的软件，其中最经典的就是waf**！
![](https://mmbiz.qpic.cn/mmbiz_png/gIBYXIMwxtsaLQxt9Og3uiawMvThmmqDbGH7G5nKOwzpPp2HeXSADFibreKAKjb08jZxFb7oNIFWY5n619ruibSnq13fKaZ4aicKkwIXuev5ejQ/640?wx_fmt=png&from=appmsg "null")

# 具体怎么回事？

基础的原理刚才都理解了，其实就是利用高位无效的机制问题，使得**输入的内容在waf和实际源代码处理的时候遇到的是不同的内容**。

比如说中文字阮，经过处理之后源代码获得的就是.

```
字符 '阮' = U+962E = 0x962E
(byte) 0x962E = 0x2E = '.'
```

那你就可以用这种方式绕过WAF的限制

比如说我输入`\u丰丰耳失`，**waf收到这个输入的时候认为没有任何敏感词**，则放行到后端jackson，后端将其转为byte，最终拼接成sql注入语句

![](https://mmbiz.qpic.cn/mmbiz_png/gIBYXIMwxtunVQicLPCRaMkUbefjg5bibR8h3ZrNVbI1rtp8S9HthGOojPEXOzB6micoQRfocLk2fbThf3DSTAE07D1JiaVo8sHSq268pW3ph0s/640?wx_fmt=png&from=appmsg "null")

最神奇的是，这种逻辑的泛用性极强，首先本身高位被抛弃意味着高位可以塞入任意值，那么对于poc就是多对1的转化关系。

以下两种都可以直接转为对应的`../../`，这对于waf来讲就是极强的考验，即便只针对byte的转化关系，waf也非常难处理

![](https://mmbiz.qpic.cn/mmbiz_png/gIBYXIMwxtt6WzZAfn1gPLICGGKeJzevic85WnLicPcw1Iqd0fBQaH2vhUs5TSBEJ80uOzn6ah3EtYD35XRUibt8VDCOfX3xOibhkacEuUIxYPU/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gIBYXIMwxtswB5ZB0SSw47cIov3JTAQBvytFmI4DwUQJKMiayFBmLTzjreRniaAZHkLNS7v9NKGsL0UF1b5LuOCaI9ibXwcZ9Cx2nnK4MssCG8/640?wx_fmt=png&from=appmsg "null")

# 继续拓展？

刚才提到了，在java本身的代码中，char类型和byte类型的转化是非常常用的写法，其带来的问题往往并不能直白的影响到源代码层面，**但对于安全来讲，似乎小概率事件会导致大概率问题**？！

# CVE-2025-41242 Spring框架因Jetty URI解析不一致导致的路径穿越漏洞

刚才我们讨论的是泛用性非常强的waf场景，那么**在Spring框架下**，本身会有一个非常大的问题，就是Spring框架中`StringUtils.uriDecode`和Jetty`URIUtil.encodePathSafeEncoding`的处理方式不一致，导致了底层的路径穿越问题。

* • https://github.com/advisories/GHSA-r936-gwx5-v52f
* • https://github.com/spring-projects/spring-framework/commit/24e66b63

对于Spring框架的`StringUtils.uriDecode`方法

![](https://mmbiz.qpic.cn/mmbiz_png/gIBYXIMwxtutgRQ3wP1bGx5IWa4OtA5HajyKma4IYe9KmnN1jJzTWxUibF707SicCU5v6o2GpSZ9wsRUjqn7ult7y2KyB35tM5mOI9VtrjPJQ/640?wx_fmt=png&from=appmsg "null")

遇到%时会做专门的处理，并调用`ByteArrayOutputStream.write`导致了高位bit丢失，出现Ghost Bits漏洞。

`阮严灵丰丰甲来`会被转为`.%u002e`

这个输入在Spring层面，不但可以通过`isInvalidPath/isInvalidEncodedPath`的路径检查，还不会被识别为正常的%u编码，全部放行

传递到Jetty中，`URIUtil.encodePathSafeEncoding`却会将`%u002e`做unicode解码转为`.`，最终构造成为`../`
![image-20260429181104521](https://mmbiz.qpic.cn/mmbiz_png/gIBYXIMwxttQpe733erxjNsyvGW8Ej5DCxUL0G7iau5Sbs5BLnWicOs2AJficzS5PXUNKtibwqjcicB55X2aBFgsm0xQAg5sUzBd2fUaPBFaVib18/640?wx_fmt=png&from=appmsg "null")

image-20260429181104521

## Openfire CVE-2023-32315 — 认证绕过

转为Byte丢失高位的方案大家都知道，还有一些更邪门的其他漏洞，其实本质上也是类似的问题。

一个很有趣的例子就是**Openfire CVE-2023-32315**，这个漏洞本质上是一个基础的路径穿越漏洞

* • CVE-2008-6508，最早的漏洞只需要..就可以实现路径穿越
* • CVE-2023-32315，发现可以用%u002e，也就是UTF-16来替代%2e实现路径穿越，因为AuthCheckFilter并没有校验对应的输入，但Jetty支持%u解码，导致了漏洞的绕过

poc就是这样的

```
/setup/setup-a/%u002e%u002e/%u002e%u002e/log.jsp
```

很多WAF都加入了%u002e%u002e作为关键字之一，那么你可以使用这个poc来绕过

```
/setup/setup-a/%2>%2>/%2>%2>/log.jsp
```

这里有个比较邪门的点在于，对于大部分框架来说，**他们不会把`%2>`当做url编码去处理，因为`>`并不是合法的url编码**。

但是对于Jetty来说，他会一视同仁，把`>`传入到`convertHexDigit`做处理

```
public static byte convertHexDigit(byte c) {
    byte b = (byte)((c & 0x1f) + ((c >> 6) * 0x19) - 0x10);
    if (b < 0 || b > 15)
        throw new NumberFormatException("!hex " + c);
    return b;
}
```

也就是说即便是符号`>`依旧会经过这一套算法，最终获得结果是14，对应`E`

那么这样一来，**waf收到的请求是`%2>`不合法的url编码不做处理，jetty把他处理转为了`%2E`成功输入`.`绕过waf**。

# 写在最后

其实类似的场景同样非常多，因为许多大型框架中，除了显式的Java类型转化，还会有隐式的框架中的处理导致同样的问题，在原议题中分享了不同框架下涉及到不同漏洞的很多种问题，他们无一都是开发者无意中触发了Ghost bits问题，设计者并没有提前考虑好类型强制转化的额外影响。

正如演讲结尾所说：**"We have only scratched the surface"** — 这才刚刚开始。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/JkQkSjos6UQNVsAuWgicG9bFkyBF1J5UnVg8tWjquOsSUsC1ut56XFmgfjia7723icAUwHx8PRZNVkG3jWCqEUic6A/0?wx_fmt=png)

LR的安全自留地

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JkQkSjos6UQNVsAuWgicG9bFkyBF1J5UnVg8tWjquOsSUsC1ut56XFmgfjia7723icAUwHx8PRZNVkG3jWCqEUic6A/0?wx_fmt=png)

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