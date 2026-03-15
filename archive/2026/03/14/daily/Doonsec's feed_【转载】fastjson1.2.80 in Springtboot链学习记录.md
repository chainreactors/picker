---
title: 【转载】fastjson1.2.80 in Springtboot链学习记录
url: https://mp.weixin.qq.com/s/4jEARB2Ddcn7LFGaaq7H_g
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:30:19.067510
---

# 【转载】fastjson1.2.80 in Springtboot链学习记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DJX1rNqJe4m6xVoKZZtkEAlMFvuG3jfSq1ibSkGrIzPDr0pWaUAQzQqOgeOElFzRqjMKrnRSw7y03dF0wQy82hh3wzat6GTkKy20RJI0pvQc/0?wx_fmt=jpeg)

# 【转载】fastjson1.2.80 in Springtboot链学习记录

ph0ebus
ph0ebus

隐雾安全

![]()

在小说阅读器中沉浸阅读

好文推荐

文章作者：先知社区(ph0ebus)

文章来源：https://xz.aliyun.com/news/16145

# 前言

所有依赖 Fastjson 版本 1.2.80 或更早版本的程序，在应用程序中如果包含使用用户数据调用 `JSON.parse` 或 `JSON.parseObject` 方法，但不指定要反序列化的特定类，都会受此漏洞的影响。

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPJ4pXicsXP7kCaQaj1POSamQFHAkZUs4aSxdAeZeMdso9ibzkTA8iby0Vg/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=0)

在之前的研究中针对fj1.2.80已经有了三种常见的利用场景

GitHub - su18/hack-fastjson-1.2.80

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPfzcqvuib7MdCJLfssibp2GhEakj41UQSrV2XpVqhBViaVdmCstrJcebDw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic#imgIndex=1)

# 漏洞复现

需要的依赖

* jackson
* commons-io

思路

1. 将InputStream放入fastjson缓存
2. 读取/tmp文件下的文件，找到docbase的文件名。
3. 往${docbase}/WEB-INF/classes/路径下写入恶意类
4. 通过fastjson触发类加载

GitHub - ph0ebus/CVE-2022-25845-In-Spring: exploit by python

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dP1upVdxbw6OPVibSAmPUVuWyAKAaXKwRyKQd3HqQYyBClDU63o9kdib4Q/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

# 漏洞分析

# cache

这个新链子也是利用缓存机制

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPoInrk8gMx5ibhSlzTuCIibkPY98o9RFwk2jJyf6PDGZj0Hwib8bQjdaYg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

**fastjson反序列化符合条件的期望类时，会将setter参数、public字段、构造函数参数加到缓存中**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPS4ELuzLP4XjPvcSlRbqNdDXSNTDXA6owqibLhVPbn4kNbAF5LOYCrQw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

**先分析一下添加缓存的过程，以下面payload为例**

```
{"@type":"java.lang.Exception","@type":"com.fasterxml.jackson.core.exc.InputCoercionException"}
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPYrt8CmlkWa8kzbibpXDYjt9giczkuicHA39bxTXXNn9BbmIoFsicsrmdUg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

**在`TypeUtils.getClassFromMapping()`尝试从缓存中获取`java.lang.Exception`类**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPGYGiaOSEsF586kt010Eia6EYMxGmrN4Ck6CtwzqoLh7YuwEcWaicAIqKw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

**在`com.alibaba.fastjson.util.TypeUtils#addBaseClassMappings`初始化中默认添加了一些作为缓存了的类，其中就包含`Exception.class`**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPreoVFNBnicdVwHIpyCyaNPiaxVLOXk4U5ItBibEgkk7ceZ21AcR33jxgA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

**可以看到有95个缓存过的类**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPARZSfrmV70ODgUehRR7ljAybbS5YjsxmwHQbvQkTaAKYIJaJAKNVbw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=8)

从缓存中获取class后返回，然后继续恢复其字段信息

`com.alibaba.fastjson.parser.ParserConfig#getDeserializer`先通过获取到的class获取对应的反序列化器

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dP5FaCo8lJxGicmWydxuaYnlOWO4mwoEviawOAVu0RYAIpRR85mj7oJuZA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=9)

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPakPN46mlGiccLDkt0q2ic7h4hLVAto0icw4OO6Sz85ibIibCcqBfAJ3h0Ew/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=10)

**可以跟踪到这行关键代码**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPwibVnyNnib2tWtlFnLCIslopEV2nqic51dWb2NxDejicL8l9ZyRM1Ssf6A/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=11)

**根据异常处理类的继承关系可以发现，`java.lang.Exception`类符合这个判断条件，于是反序列化器被设置为`ThrowableDeserializer`**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dP3ZMWnlYaBzM2HTG15kBN9b5GORIAxFG2vfibLwNT7E66JaicFViaBY3fw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=12)

**在`com.alibaba.fastjson.parser.deserializer.ThrowableDeserializer#deserialze`反序列化过程中会将Exception作为期望类**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPdiaWiaeF8JdicicAP0VMsria6XnwlNQGjiaHxgfT4dGp8EA0TWNCnss6yDmQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=13)

**然后解析json中的键值对，这里key是`@type`**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPfu6KA3W83SceLIzpxo9FI1LFk9SqZAHE0QubNgSiaibpGptQcoZicYO0g/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=14)

**当key为`@type`时会将`Throwable.class`作为期望类传入`com.alibaba.fastjson.parser.ParserConfig#checkAutoType()`**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPehia3gUmicwkjmuaa6fXSbOK5n6nIYicLAByqC1DWba3RLr8Z0B7LU5GQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=15)

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPic8NVmKNOndia00icGy8yEJeyjV8XGmAdSDpbuiaVCsHGuWc7e2oa7tL9w/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=16)

**需要经过黑名单过滤和白名单校验**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPQmicXb4doibp1IrsVnKOlX6xDw85JAo9QnDlRsp9VhmLVGzVzWoaPCFA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=17)

**继续跟进到这段代码，根据传入的Typename来加载类，加载后，如果是期望类的子类则加入到缓存mapping中**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPKd8vztanf76MQgHbE1o3827mMNwpBME08jDn5pnxNEHmRtziaqeRbPQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=18)

## read

进一步分析一下任意读的payload

```
{  "a": "{    \"@type\": \"java.lang.Exception\",    \"@type\": \"com.fasterxml.jackson.core.exc.InputCoercionException\",    \"p\": {    }  }",  "b": {    "$ref": "$.a.a"  },  "c": "{  \"@type\": \"com.fasterxml.jackson.core.JsonParser\",  \"@type\": \"com.fasterxml.jackson.core.json.UTF8StreamJsonParser\",  \"in\": {}}",  "d": {    "$ref": "$.c.c"  }}
```

利用循环引用尝试将字符串转换为对象并获取对象的值，按作者的话来说，这里是利用JsonPath来忽略本有的异常

接着上面继续分析，恢复好`com.fasterxml.jackson.core.exc.InputCoercionException`后，继续利用`com.alibaba.fastjson.parser.deserializer.ThrowableDeserializer#deserialze`获取字段，根据key实例化出`FieldDeserializer`进一步处理

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dP2h3ICgiaGlmMh2cCkqhogvYyIrEFdkvTogu1CTEmdFwDD3PwLUQrlFw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=19)

**继续，调用`TypeUtils#cast`进行类型转换**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPFhLY8csX5HckUkUeetavDhqS57uPM4dbOAzciaofP5ubnwR8wmDHBicA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=20)

**`com.alibaba.fastjson.util.TypeUtils#cast(java.lang.Object, java.lang.Class<T>, com.alibaba.fastjson.parser.ParserConfig)`会根据传入的obj进行相应的类型转换，这里会进入`Map`类型这个分支**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPYesUmM9CTzzTyzAicqQbKGicuSibyzQ4YZm2u1icdzESWyiaE1icvQbkabsg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=21)

**跟进到`com.alibaba.fastjson.util.TypeUtils#castToJavaBean(java.util.Map<java.lang.String,java.lang.Object>, java.lang.Class<T>, com.alibaba.fastjson.parser.ParserConfig)`，根据构造方法参数类型clazz获取反序列化器，clazz为`com.fasterxml.jackson.core.JsonParser`**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPxVsQngkboqBL097HSA6pgic3x0AbibXVlBXkjUHx7tRVrEBjCdpZJ4pA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=22)

**获取到反序列化器后，调用`putDeserializer`函数`this.deserializers.put(type, deserializer)`**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPev0Q2aiar5mMwe8juSvqSrtR4QGjkSp0URVABuh3qibeoLbK4HulyOYg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=23)

**这里就会将`type`和`deserializer`存入`com.alibaba.fastjson.util.IdentityHashMap#buckets`中**

![图片](https://mmbiz.qpic.cn/mmbiz_png/PJcQz9vmUicmaCl9AkUPkXmG0aR8N59dPyuQQyknC7ZITcFYBAtq3CzQ7OFArhI16qxAtXX8np1LQiaNfwqcTjGg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=24)

**在后续恢复`com.fasterxml.jackson.core.JsonParser`中，调用`this.deserializers.findClass(typeName)`就可以从`com.alibaba.fastjson.util.IdentityHashMap#bucket...