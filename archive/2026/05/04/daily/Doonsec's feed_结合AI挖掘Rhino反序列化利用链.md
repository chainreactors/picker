---
title: 结合AI挖掘Rhino反序列化利用链
url: https://mp.weixin.qq.com/s/dr7qc2b-KOVtX-Mmm-4EqA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:00.194289
---

# 结合AI挖掘Rhino反序列化利用链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KA5KNdck7pd6B5xfr4JwiaLib500hRibMwKqGsfwh54UfIDiajWvZ5m7bEI4icgLyibQ9wAOdwRgZNibxdYianrB3LP8JaoyzzJGOq6Z7YAyxDuroeg/0?wx_fmt=jpeg)

# 结合AI挖掘Rhino反序列化利用链

原创

ptr
ptr

UpRoot

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 起

最近为了证明自己是否能够对大型产品进行挖掘前台RCE，我找了一款集团、金融等单位所常用的最新版产品；经过大量时间的审计，我对这套产品后台有了很多种R法，但是前台却没有，当我准备告诉自己你现在能力还不够的时候，让我感到柳暗花明又一村的是我在最开始审计的那个部分找到了能让我前台组合拳R的点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pc4Et0w9ldWTicPtXDdKt0o7FlxRWlLt4tQ389jTeCSzVuqHWskLVp3bhgMYBtyHQWs4rBR6rRXibB32EjysaurW3r6X6a4Q24C0/640?wx_fmt=png&from=appmsg)

当我URLDNS链收到回显的时候，我感叹我的时间没有白花、我的努力没有白费！

产品内置CB1.9.4，当我尝试用CB打内存马的时候，产品控制台却给我回显禁止"TemplatesImpl"参与反序列化，我当时想着，这都是小case，应该是存在一个hook，hook到了我的TemplatesImpl，我打二次反序列化或者JNDI就是了，CB链给予我们getter的能力走SignedObject\LdapAttribute都是可以的，但是让我再次陷入懵圈的地方的是我发现其`System.getSecurityManager()!=null`，这意味着我最喜欢的TemplatesImpl没法用了。

没关系，我还有JDBC姿势，我还可以打表达式、我还有JS引擎可打！然而目标不存在Mysql、H2、Derby，有pqsql但还不是漏洞版本...

那不能就这样算了吧，沉没成本那么大，凭什么倒在没有利用链这一步，没有利用链我就自己挖一条。

### 承

没法用TemplatesImpl挺好的，rasp本就会hook到这个点，这也是我这个阶段想去探究的难点，正好在这次一并解决了。

TemplatesImpl好用的地方在于可以直接defineClass加载字节码，要想找到一款平替，倒也不是很难，我曾经看过两篇文章分别是《记一次离谱的内存马getshell》、先知上面的《NC6.5反序列化回显绕过》，都有提到过一个点Rhino的“org.mozilla.javascript.DefiningClassLoader”也可以进行defineClass。

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pf3icpE1ekOSZJfzgjcGEWTicibfqDjGQXhzAFpmmz0bOpxQETNPYXJPxTVdZHWkKGI4LhsI4CRcXdlvM000khArdpuhu4WJj2UZc/640?wx_fmt=png&from=appmsg)

我的环境里面正好也存在Rhino，于是我想深入探究下，但是截至目前我就看过一篇文章是关于Rhino的，那篇文章里面告诉我，Rhino存在gadget可以调用任何类的无参方法，但前提是具备我得toString的能力。

toString能力倒是不用担心，EventListenerList#readObject就可以实现调用任意对象的toString，并且在JDK高版本下也适用。

但是我再把那篇文章拿出来拜读的时候，我发现其最后还是用到了TemplatesImpl来加载字节码，不能直接拿过来用，需要去改链，但他的思路给了我不少的启发。

因为文章写的相对浅显，我没法去深追其中的利用链，于是，我把文章里面的poc给到了AI，让AI去把其中的调用链整理出来，我再去研究。

```
BadAttributeValueExpException.readObject()
    ↓
val.toString()
    ↓
NativeError.toString()
    ↓
读取 "name" 属性
    ↓
ScriptableObject.getProperty(nativeError, "name")
    ↓
GetterSlot.getValue()
    ↓
getter.call(...)
    ↓
NativeJavaMethod.call(...)
    ↓
沿 prototype 找到 NativeJavaObject
    ↓
NativeJavaObject.unwrap()
    ↓
TemplatesImpl tmpl
    ↓
tmpl.newTransformer()
    ↓
TemplatesImpl 加载 _bytecodes
```

作者的思路是利用BadAttributeValueExpException提供toString触发点，利用NativeError.toString提供属性读取点，GetterSlot把属性读取变成函数调用；NativeJavaMethod把Rhion函数调用变成Java反射调用，NativeJavaObject提供真正的TemplatesImpl示例。

我不喜欢去追利用链，我就找到我想要的就是了，下面这段Gadget就是我想要的：

```
NativeError.toString()
    ↓
GetterSlot
    ↓
NativeJavaMethod
    ↓
调用某个无参 Java 方法
```

可以赋予我调用任意类无参方法的能力。

于是我尝试让AI把我梳理下是否可以替换sink点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pdPm0XDwt60Ca7tGOmJW1JAJr4iavbvjOvZPCvRZmXiaKSOngfCa0hetEkHibnbArz1dFcJOhDciaBIAEOFTpwuNm5cMhLeVqJAkFI/640?wx_fmt=png&from=appmsg)

答案是不行，确实该如此，因为defineClass必须要传入参数。

我陷入了一段时间的思考，我再去查阅文章和AI对话，最终我发现了一个关键的点，Rhino本身就具有执行Java代码的能力，其本身就是一个JS引擎。

那能不能把这个引擎加入到Gadget中呢？继续对话AI,于是有了这条链路：

```
GetterSlot.getValue()
  -> NativeScript.call()
  -> Script.exec()
  -> 执行 Rhino JavaScript
```

然后再去调用defineClass：

```
Script.exec()
  -> 创建/获取 org.mozilla.javascript.DefiningClassLoader
  -> 准备 className
  -> 准备 byte[]
  -> defineClass(className, bytes)
  -> linkClass(clazz)
  -> 触发类初始化或实例化
```

那整个的Gadget就是：

```
toString trigger
  ↓
NativeError.toString()
  ↓
NativeError.js_toString()
  ↓
getString(thisObj, "name")
  ↓
ScriptableObject.getProperty(thisObj, "name")
  ↓
ScriptableObject.get(...)
  ↓
ScriptableObject.getImpl(...)
  ↓
ScriptableObject$GetterSlot.getValue(...)
  ↓
getter instanceof Function
  ↓
NativeScript.call(cx, scope, thisObj, args)
  ↓
script.exec(cx, scope)
  ↓
Rhino JavaScript 执行
```

于是换codex来帮助我写这个exp，出现如下错误：

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7peFSQ2Vu02kN0nAuVn4NYrqjeS6umKegPiau8vCR40dp4HD0Ua4IfELkVFhr840fu8Vc2zmzbN4yDa42ibGjHWzg7CGoib3AG1EFE/640?wx_fmt=png&from=appmsg)

上下文中没有这个线程context。

这个问题我思考了好久，躺在床上脑子里面也在想如何解决这个线程context的问题。

### 转

白天喝的加浓美式劲还没过、躺在床上蚊子还在耳边吵闹。

整夜无眠，反倒是给了我更多的思考时间。

睡醒后我的脑子里面便萌生了一个想法，是否可以通过两个阶段来实现呢？

**一阶段创建线程，二阶段加载字节码！**

说干就干，有AI倒是有了个良师益友，不仅放大了我的能力，还能帮助我把我的一些“不切实际的想法”落地成为现实。

帮助我做好规划，教我下一步如何去实现：

```
已完成：
name getter -> Context.enter()
message getter -> BaseFunction.call()

下一步：
message getter -> NativeScript.call()
               -> script.exec()
               -> 返回 SCRIPT_EXEC_OK

再下一步：
把这个 NativeError 对象放进靶场能触发 toString() 的位置

最后：
处理序列化/反序列化后对象图是否还保持：
  name GetterSlot
  message GetterSlot
  NativeScript.script
  NativeScript.parentScope
```

于是，在我和AI的一步步试错下，整个Rhino反序列化利用链最终呈现了出来。

```
反序列化入口：
ObjectInputStream.readObject()

toString 触发：
EventListenerList.readObject()
  -> 异常信息构造
  -> UndoManager.toString()
  -> NativeError.toString()

Rhino 第一阶段：
NativeError.toString()
  -> getProperty("name")
  -> GetterSlot.getValue()
  -> MemberBox(Context.enter)

Rhino 第二阶段：
NativeError.toString()
  -> getProperty("message")
  -> GetterSlot.getValue()
  -> NativeScript.call()
  -> Script.exec()

Script.exec()
  -> js引擎加载字节码
```

![](https://mmbiz.qpic.cn/mmbiz_png/KA5KNdck7pco2ht1lykzYnKAFjbd57ic0sjUBjCpV8Hvc74TgBMHWRKQCTbaIccaTo8K4N2PjzGy3R7TYPI1TJuiaA9oDYfdndjIZt05e58Bc/640?wx_fmt=png&from=appmsg)

最终也成功绕过了产品对TemplatesImpl的限制：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7peadrTt8YC4seUAHxs7u9o8tP9x7Rb9s8C0u2LH29ztbKJuutP5XyF9ibOegOBZr9B4RHmALiahGKJtagrnUKoxGia5HOtcYmORTs/640?wx_fmt=png&from=appmsg)

武器化并配套内存马：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KA5KNdck7pcJhIsMibvBSJdg9RannxUGfPjJW8TxfuwPkr7K8xianU6D0KAaNAAZWTwN5VUOIOGcia0GYY11d9RticB9YAXbTVRK9r27Il89yhg/640?wx_fmt=png&from=appmsg)

至此，我觉得，我明天可以出去看看风景了，不用在窝在出租屋里面了，你给自己定的目标，已经实现了。

### 合

能看到这里，我想你应该也会对自己有一些严格的要求吧，那我送你们一段话，也送我自己：

“

在做一些有意义的事情的前期，一个人是没有方向、没有思路、没有全局感的，最重要的就是不断投入时间，过一段时间就会突然清晰了。

你要明白你不特殊，大家都一样，在做事的前期都迷茫，但谁能走的更远，靠的不是投机取巧，而是脚踏实地。

”

共勉...

2026.5.4

- END -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

UpRoot

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

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