---
title: 关于Java中反序列化漏洞的思考
url: https://mp.weixin.qq.com/s/YmADnb8uGuZkN-jRmbjprw
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:27:29.089168
---

# 关于Java中反序列化漏洞的思考

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ULOszTo2RiaCMlV9vlCCkjG0IaInibug6WIOI8BpVqFVBECpiaVibBQcqjDcpe5BprV8wYvIE8TmIOCoeS71Cqgp9AxAIwiaRvCzicPXpAPjdA3xI/0?wx_fmt=jpeg)

# 关于Java中反序列化漏洞的思考

me7eorite
me7eorite

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 问题

刚开始学 Java 反序列化时，很容易被各种链劝退。比如 CC1-CC8、CB、ROME、Hessian、Shiro、Fastjson，每一条链看起来都有很长的调用路径。如果只是按编号去背：

```
CC1 是怎么调用？有什么限制？
CC2 是怎么调用？有什么限制？
CC6 是怎么调用？有什么限制？
```

短期看起来好像学了很多，笔记的文件也在增加，收集了很多调用栈，但过一段时间很容易忘。尤其在 AI 时代，直接问一句“帮我总结一下 CC 链”，AI 可以生成一篇很完整的文章，但是问题在于：

1. 1. 我真的理解了吗？
2. 2. 我能够举一反三吗？
3. 3. 我能够检查AI出错的时候吗？

## 观点

学习反序列化链，不应该只盯着某一条链的完整调用过程，应该思考学习的目的，为的是建立反序列化链的模型。
一些文章常常会读到：`Source -> Sink` 的写法，但是这个路径太短，不适合学习的时候用，可以参考：

```
Source -> Trigger -> Bridge -> Propagator -> Sink

Source -> Trigger -> (Bridge Gadget -> Propagator Gadget -> Sink Gadget -> Sink)
```

这五层分别对应：

* • Source：反序列化时自动执行逻辑的入口。
* • Trigger：Source 自动调用的方法，例如 `hashCode`、`compare`、`toString`、`setValue`。
* • Bridge：将 Trigger 调用转接到 gadget 链的关键对象。
* • Propagator：继续传播调用的对象。
* • Sink：最终产生危险效果的方法。

这样看一条链时，就不是记一长串方法名，而是判断每一层分别由谁承担，后续了解到 CodeQL 也可以继续利用这个思路。

## 方法

CommonsCollections 系列最容易让人误解的地方是：看起来 CC1、CC2、CC3、CC4、CC5、CC6、CC7 都是不同的链，但从分层模型看，它们更多是在不同层里换组件，以下以 CC 链中出现的为例：

Source：

* • `AnnotationInvocationHandler`：CC1 / CC3
* • `HashMap/HashSet`：CC6 / CC3
* • `PriorityQueue`：CC2 / CC4
* • `TreeBag / TreeMap`：CC4 变体
* • `BadAttributeValueExpException`：CC5
* • `Hashtable`：CC7

因为高版本 JDK 改了 AnnotationInvocationHandler 的实现，CC1 原来的触发方式不再稳定。所以更换 Source，本质上是在找新的自动调用点，减少对特定 JDK 版本的依赖，不同 Source 会带来不同 Trigger：

* • `HashMap` 会触发 key 的 `hashCode`
* • `PriorityQueue` 会触发 comparator 的 `compare`
* • `BadAttributeValueExpException` 会触发 `toString`
* • `AnnotationInvocationHandler` 会触发 Map 相关操作

Bridge 和 Propagator(其实还可以细分)：

* • `TransformedMap`：把 `setValue` / 写入 value 转成 `Transformer#transform`
* • `LazyMap`：把 `get` 转成 `Transformer#transform`
* • `TiedMapEntry`：把 `hashCode` / `toString` 转成 `getValue -> map.get`
* • `TransformingComparator`：把 `compare` 转成 `Transformer#transform`

**这里要区分一个点：** `TiedMapEntry` 和 `LazyMap` 经常一起出现，但它们角色不同。

1. 1. CC6 : `HashMap#hashcode -> TiedMapEntry#hashcode -> LazyMap#get`
2. 2. CC5 ：`BadAttributeValueExpException#toString -> TiedMapEntry#toString -> LazyMap#get`
   简而言之，CC5 和 CC6 的中后段其实一样，只是 Trigger 不一样。

Sink 也可以进行区分，有些类本身不是真正的危险点，而是 "Sink的调用器"，可以称为 Sink Gadget。
例如：

* • `InvokerTransformer`：实现反射调用
* • `InstantiateTransformer + TrAXFilter`：实现实例化类

真正的危险点是 Real Sink：

* • `Runtime.exec`
* • `TemplatesImpl#newTransformer`
* • `TemplatesImpl#defineTransletClasses / defineClass`

举个例子： `InvokerTransformer` 不是最终 Sink，它只是反射调用工具。真正的 Sink 要看它最后调用的是 `Runtime.exec`，还是 `TemplatesImpl#newTransformer`。

### 拓展到 CB 和 ROME

这个模型不只适用于 CC，CB 链也可以分析：

```
Source：PriorityQueue
Trigger：comparator.compare
Bridge：BeanComparator
Propagator：PropertyUtils.getProperty -> getter
Sink：TemplatesImpl#newTransformer
```

CB 的重点不是 Transformer，而是 JavaBean 属性访问：

```
compare -> getProperty -> getter -> sink
```

ROME 链也类似：

* • Source：HashMa
* • Trigger：hashCode
* • Bridge：EqualsBean / ObjectBean
* • Propagator：ToStringBean -> JavaBean getter
* • Sink：TemplatesImpl#newTransformer

ROME 的关键点是：

```
hashCode / equals / toString -> JavaBean getter -> sink
```

所以从 CC 到 CB，再到 ROME，可以看到一个共同思路：

1. 1. 反序列化入口自动调用某个普通方法
2. 2. 普通方法被 Bridge 实现
3. 3. 调用进行传播
4. 4. 最后触发危险方法

区别在于**中间的传播方式**不同：

* • CC 主要围绕 `Transformer`(如何调用到 `transform` 方法)
* • CB 主要围绕 `PropertyUtils` 和 getter
* • ROME 主要围绕 `EqualsBean`、`ToStringBean`、`ObjectBean` 和 getter

## 结论

AI 可以快速生成大量链路总结，最快速地检索到大量资料，建立一个框架并以最大能力去往框架里补充和完善内容，我认为是提高学习效率的一个方式。
以反序列化链为例，通过对结构进行拆分：

```
Source -> Trigger -> Bridge -> Propagator -> Sink
```

后续学新链的时候可以补充这个结构，在遇到某个特殊的 Source/Trigger/Sink 或许可以联想到这个在 XX 是否可用，而不是简单的背诵和调试堆栈。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

Gh0xE9

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

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