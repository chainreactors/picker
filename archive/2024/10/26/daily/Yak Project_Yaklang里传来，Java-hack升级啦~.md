---
title: Yaklang里传来，Java-hack升级啦~
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247523461&idx=1&sn=634e74f61a83e153a14323be11d4745d&chksm=c2d1e021f5a66937934b55942c3c4abc1ce7f7a4fbb89d6e1625f3bd0a3d96555368e0b8acdb&scene=58&subscene=0#rd
source: Yak Project
date: 2024-10-26
fetch_date: 2025-10-06T18:56:56.479903
---

# Yaklang里传来，Java-hack升级啦~

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxuDRIKgnKPYLa1icjE0WQe5dE0avich2rgIviaXXK8W3LLcDrIN4ucFmDkQ/0?wx_fmt=jpeg)

# Yaklang里传来，Java-hack升级啦~

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

Yaklang里传来，Java-hack升级啦~

隔壁抽鞭子的黑工厂里，牛牛更新了吗~?

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxu7j6S9W4W43aNseMgdyBDuYeaVicrVRGSctesNFBadrA5XcaiczLO75aw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZd02pV7rv5ibedRLvBZj5YebhzCe2rqkZoPgYHyTR0Q8XbQ2WsTfZTLGLHsQCbFHfSYW84YGvUk6wg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxu51UibpPv4DXO81nEmdLC8c0FicgJGQ6iaW0aPPU38A8ThTve8oOybl34w/640?wx_fmt=png&from=appmsg)

#

**TemplatesImpl 类：**TemplatesImpl对象的成员方法有一段类字节码，在反序列化时会加载并实例化这个类。通过构造序列化链使得成功反序列化**包含恶意类的 TemplatesImpl 对象**，从而实现任意代码执行的效果。

**Transformer 类：**Transformer 是一个接口，其成员只有一个 transform 方法，参数和返回值都是 Object 类型，用于将一个对象按照某种规则转换为另一个对象。**通过实现类 InvokerTransformer**可以实现对任意对象方法的调用，再通过 ChainedTransformer 可以将多个 Transformer 串联，实现类似链式调用的操作。

通过对比两种方式可以看出，基于TemplatesImpl 类构造的链可以通过修改TemplatesImpl 对象内的字节码，也就是恶意class实现各种功能。而Transformer链需要构造多个Transformer对象实现。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxukAzEG78GGURICeGseqCGibgriaFdjCcr2ghWr6AxBomJBvq0FDBOKJKA/640?wx_fmt=png&from=appmsg)

#

java在序列化一个对象时，会先递归处理成员对象，再序列化这个对象，但在递归过程可能会遇到循环引用的问题，例如：

```
Object node1 = new Node();Object node2 = new Node();node1.Parent = node2;node2.Child = node1;
```

在序列化node1的时候会先序列化成员Parent，开始序列化对象node2这时又会开始序列化成员Child，开始序列化对象node1......，为了防止递归过程中出现循环引用，每个对象第一次序列化时会生成一个handle值（从0x7e0000开始计数，依次递增），后面再遇到这个对象直接用handle值代替。而且不仅对象有handle，类也有handle，也就是每个类的描述也只会出现一次。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxumGiaiaP77rf6e8kiaq3rmpc8AibnzibBOVGAg89gRMJianic6kQr1kQhTQmFg/640?wx_fmt=png&from=appmsg)

#

所以如果简单的对序列化数据中的对象进行替换，会导致handle table错乱（例如同一个class在不同的序列化数据中的handle值不同）

一种解决方案是在序列化一个模板对象时，把handle table提出来，再在序列化其它transform 链之前把handle table赋值进去，这样就能保证两次序列化中，相同class的handle值相同。另一种办法就是对于一些关键类，即使重复出现也不使用handle值，但这样可能导致序列化数据体积变大。最稳妥的办法就是对替换对象的handle table重构。

最后一个简单的办法就是把所有transform 链都生成，再压缩，压缩后发现可能压缩算法会对这种高度相似的数据采取类似引用数据块的办法，使得压缩率特别高。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxuYoOW8Nia7pfTfwnUyYuTlN5tPucgzdeZJIuvTfp115E3VcP9smib941Q/640?wx_fmt=png&from=appmsg)

#

加入transform链后，链子数量骤然增多，有些链子还需要搭建jdk环境，显然增加了测试的成本，所以需要写个自动化的测试。也就是需要编写一个java程序作为靶场，这个靶场需要包含所有payload的运行环境。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxuNib9icLBmKx09VWW8yB8xBCspfvS0queY6wr1p0ncCiapzcpumHmNMmew/640?wx_fmt=png&from=appmsg)

##

由于payload涉及的依赖较多，不能一个个手工导入。而ysoserial.jar既然可以生成payload，那必然包含所有payload的依赖，所以可以将ysoserial.jar作为靶场依赖。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxuoQJFBmlMar6UNIq8gvMujMNFGhQEA7m98pEOB24JjqZspM3M5ePUiaw/640?wx_fmt=png&from=appmsg)

##

ysoserial.jar在生成CB链183版本的时候是用的192版本的BeanComparator，在构造时将serialVersionUID修改为183版本的。所以靶场中是不存在183版本BeanComparator类的，导致CB183链子失败。而同一个类名不能在默认的class loader中加载多次，所以没法添加183的依赖。解决方法是通过agent，根据不同payload加载不同的BeanComparator类，见下文。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxumnuXRFUolvmYSia8YSiajjed5GoQd4ibUWvqK3JRVpF0J27oHkxSAG93g/640?wx_fmt=png&from=appmsg)

##

Jdk7u21和jdk8u20的**jre依赖版本不同**。通过报错信息可以找到问题主要在sun.reflect.annotation.AnnotationInvocationHandler类的更新上，也就是这两条链需要不同版本的AnnotationInvocationHandler类，问题与上面类似。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxuwCG6S1yyEWJH4hq2dbibsxHzwjibt6n2qRrJP5PUU4BRO4lia5gyjnEWw/640?wx_fmt=png&from=appmsg)

##

javaagent可以拦截类加载过程，可以在类加载时修改或直接替换类。所以可以使用agent实现对不同的gadget加载不同的class。

Java agent的入口函数是premain，会被传入命令行参数和Instrumentation对象

```
public static void premain(String args,   Instrumentation instrumentation){    ClassLoggerTransformer transformer   = new ClassLoggerTransformer(args);      instrumentation.addTransformer(transformer);   }
```

通过Instrumentation对象可以设置一些类加载的过程，例如案例中addTransformer，追加了一个ClassLoggerTransformer对象，ClassLoggerTransformer对象实现了transform方法，在加载一个类前会把类信息传给transform方法，返回值是经过处理后的类，用于替换原有类。

```
public byte[] transform(ClassLoader   loader,                        String   className,                        Class<?>   classBeingRedefined,                          ProtectionDomain protectionDomain,                        byte[] classfileBuffer) throws   IllegalClassFormatException {    return xxx                           }
```

所以可以在transform中拦截类加载过程，将指定类替换为当前payload需要的版本。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxucicTuXAYlhrvaRiciaxZjmhIXGzsAxodb6IicFpY4Nx0O01y6V30rayCsQ/640?wx_fmt=png&from=appmsg)

#

被templateImpl加载的类需要继承AbstractTranslet接口，实现transform方法。为了解决这个限制，我让templateImpl加载一个类前先加载一个loader（实现了AbstractTranslet接口），再让loader加载目标类。但这个loader就是压倒header的最后一根稻草，导致gadget过大。执行流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeYIibG4JqSAIUTib5zBf4QjxpLjEoVT0xWNFlXrZiaDYXTEGBtmmz3KBfjEAyQDt1gicAbJsKZmlmBQ/640?wx_fmt=png&from=appmsg)

为了去掉实现AbstractTranslet接口的限制，又不影响payload大小，可以尝试直接改类的属性，修改class文件，给class增加一个父接口而不实现接口。

测试时发现报错，原因是默认构造函数必须调用supper()或this()方法，之前测试类aa没有显示声明父类，默认父类是java.lang.Object。也就是还需要将java.lang.Object.<init>方法的调用改为com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet.<init>调用

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeYIibG4JqSAIUTib5zBf4Qj6Yz7fpNEy4yyp3UKNgxCOYGf5298K9jNzRAfhEMGmFS7OGWHpplkNg/640?wx_fmt=png&from=appmsg)

最终成功实例化测试类，得到dnslog回显，反编译后的源码如图

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeeYIibG4JqSAIUTib5zBf4Qj4Pu4TkAjq7H23pIVMv5ia79umxy2swohBn13ibfiaaoUtKDVp3yJyER8g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxu7CCINZBXXIy77O8xA1xIj4MfQwpGcRxK1rpmJ2AWpicfW6cd4ztecRQ/640?wx_fmt=png&from=appmsg)

#

本文通过 Java Agent 拦截和修改类加载机制，构建了一个 Java 靶场，用于验证和测试各种反序列化 payload。然而，对于更复杂的 Web 环境中的回显测试，仍然需要搭建实际环境进行验证。

文章最后介绍了一个手动修改 class 文件以添加父类的案例，展示了如何在继承抽象类时不实现其所有抽象方法。这证明了 "在继承抽象类时必须实现所有抽象方法" 的规定是在编译期间检测的，而 JVM 在运行时并未对此进行验证（至少在 HotSpot VM 中没有验证）。

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

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