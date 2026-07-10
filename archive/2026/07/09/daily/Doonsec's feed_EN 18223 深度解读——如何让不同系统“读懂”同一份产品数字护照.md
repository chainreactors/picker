---
title: EN 18223 深度解读——如何让不同系统“读懂”同一份产品数字护照
url: https://mp.weixin.qq.com/s/beq0dSnp3VgWcz8TPMUr4Q
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:55:30.592995
---

# EN 18223 深度解读——如何让不同系统“读懂”同一份产品数字护照

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NSKgl3moHDMduK0PV21n0icIXfOUlUf9b4ekgickNLu7bJ4gpU4YVkticElYhcMK1va3QyKjNVex1nriblENrClUEJibwDhtchsezSf8qiaXgjX0M/0?wx_fmt=jpeg)

# EN 18223 深度解读——如何让不同系统“读懂”同一份产品数字护照

工业互联网标识智库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/DSmmCibR6DZPYg8dgBWhE35bNNNEQafsWaxr5s6lpPia7DcHvvGKFSaicFFRgJtdW3ozdTB43nGsJ2uFlRcgFib1rg/640?wx_fmt=gif&from=appmsg#imgIndex=0)

2026年5月，CEN/CENELEC JTC 24 发布产品数字护照（Digital Product Passport，DPP）系列基础标准，围绕唯一标识符、数据载体、数据交换协议、生命周期管理API、数据存储归档与持久性、系统互操作性等关键环节提出要求。其中，EN 18223《产品数字护照——系统互操作性》**重点规范DPP的共同信息模型、数据元素结构、语义引用和机器可读表达方式。**

不同企业、行业平台和服务商都可能建设DPP系统。系统之间即使能够传输数据，也不代表数据可以直接使用：同一个字段可能名称不同、单位不同，甚至含义完全不同。**EN 18223所要处理的，就是数据传过去以后，怎样让不同系统仍能按照一致的结构和语义理解它。**

![](https://mmbiz.qpic.cn/mmbiz_png/NSKgl3moHDM7FvicFrTdnSsypFxAcdFJjuzFZNzIHzIdcyn4TOddibxK7UJ9B3sBGqnPh7u6fMV2lWZK8fVszIIuGib5Z9l5TG3tW8SBWEfKS8/640?wx_fmt=png&from=appmsg)

**01**

**标准定位：建立共同的数据表达框架**

**EN 18223从组织、语义和技术三个层面讨论系统互操作，并规定DPP共同信息模型、数据元素类型、数据字典引用方式以及JSON、XML序列化规则。**它不是一份具体产品字段清单，也不要求所有行业采用同一套业务系统。

标准提供的是一层通用骨架。不同产品组可以在此基础上扩展材料、环境、维修等行业数据，但核心对象、数据结构和语义引用方式需要保持可理解、可映射。这样，平台之间的差异不会直接演变为数据无法交换和复用。

**02**

**互操作的三个层面：不仅要连得上，还要理解一致**

**组织互操作关注DPP如何进入现有业务环境。**企业、监管机构、服务商和其他价值链主体应能够在各自系统中接入DPP，并按权限通过人工界面或软件系统使用数据。

**语义互操作关注“同一字段是否表达同一含义”。**标准鼓励使用标准化或既有的数据模式语言，复用已有本体、命名空间和跨行业通用概念，减少不同产品组各自定义、彼此无法理解的情况。

**技术互操作关注数据如何被系统处理。**EN 18223通过统一对象结构和序列化规则，将语义模型转换为可交换的JSON或XML，使同一份DPP进入不同平台后仍能保持基本结构一致。

这三层并非相互替代：**接口能连接，只解决了技术入口；字段含义一致，才具备语义基础；真正嵌入业务流程，还需要组织层面的角色、权限和责任配合。**

**03**

**语义模型：把DPP定义为可扩展的数据容器**

标准通过UML类图描述DPP的核心对象及其关系。DigitalProductPassport类作为数字容器，包含DPP实例标识、产品唯一标识、标识粒度、模式版本、状态、更新时间、经济运营者标识、设施标识、内容规范标识以及具体数据元素。

标识粒度可对应型号、批次或单件产品。模式版本和更新时间用于说明一份DPP采用哪一版数据结构、何时发生最近更新；状态信息则支持系统区分当前有效、停用、归档或其他规则规定的状态。

这一设计把DPP的通用属性与产品组特有数据分开。标准固定的是共同骨架，材料构成、环境性能、维修记录等内容通过数据元素扩展，从而在跨行业共性与产品差异之间留出空间。**换言之，EN 18223不替各行业填写内容，而是先规定这些内容应如何被组织。**

**04**

**数据元素和数据字典：让数值与含义保持对应**

EN 18223以DataElement作为数据点的抽象基础，并细分为数据元素集合、单值数据元素、多值数据元素、关联资源和多语言数据元素。重量、再生材料比例等可以作为单值；一组同类记录可以采用多值；多个相关字段则可组成数据元素集合。

关联资源用于连接检测报告、说明书等外部文件，并记录资源地址、媒体类型、标题和语言。多语言数据元素用于表达随语言变化的内容。每个数据元素还可以设置elementId和dictionaryReference，前者用于在DPP实例内定位，后者用于指向正式语义定义。

标准将数据实例与语义定义分开管理：DPP保存具体数值，字段名称、数据类型、单位和受控值等定义放在机器可读的数据字典或语义库中。通过dictionaryReference，同一个字段可以在不同系统中找到共同含义。

这种设计有利于复用和版本维护，**但标准没有指定唯一的数据字典平台。数据字典由谁维护、不同产品组如何共用、已有行业词汇如何映射，仍是后续治理中的关键问题。**

**05**

**技术表达：用JSON、XML承载同一语义模型**

在技术实现方面，EN 18223规定JSON和XML的序列化方式，对类名、属性名以及字符串、布尔值、数值、日期和URI等数据类型的表达作出约束。附录还给出了相关模型示例。

实际交换时，可以采用较紧凑的JSON表达，将部分语义信息放在外部数据字典；需要完整展开时，也可以使用展开式JSON或XML。表达形式可以不同，但都应回到同一语义模型，避免格式差异造成含义漂移。

**06**

**变化管理：不仅理解当前数据，也要知道它如何变化**

标准还提出DPP变化管理要求。影响数据点的变化，应记录相关标识、发生时间、变更主体和具体属性，并与EN 18221的日志和归档要求衔接。这样，不同系统不仅能够读取当前值，也能判断数据何时、由谁、因何发生变化。

这一机制对合规核验尤其重要。若字段定义、单位或字典版本发生变化，系统需要同时保存语义版本和数据变更关系，否则相同数值在不同时间可能代表不同含义。**系统互操作的目标，不只是把一段JSON传过去，而是让数据结构、字段含义和变化记录在不同平台间保持一致。**

**07**

**结语**

**EN 18223解决的是DPP跨系统使用中最容易被忽视的问题：接口连通之后，数据是否仍然能够被正确理解。**共同信息模型、数据元素类型、语义引用以及JSON、XML表达规则，为不同平台建立了可对照、可映射的数据基础。

**但标准给出的是共性框架，并未提供具体产品组的字段清单，也没有指定唯一的数据字典、本体或语义库。**各行业仍需结合产品法规和业务场景，继续明确字段定义、计量单位、受控值、版本管理和字典映射关系。

对企业而言，首先要盘点ERP、PLM、PIM和供应链系统中的现有字段，识别同名不同义、同义不同名以及单位不一致的问题；其次要建立可维护的数据字典和版本机制，将内部字段映射到DPP共同模型；同时确保DPP平台能够输出规范的JSON或XML，并记录字段定义和数据值的变化。只有内部数据治理与共同语义框架真正衔接，DPP才可能被外部系统稳定理解和复用。

**联系方式：**

录老师：15313551063

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/pv1uSl1CtAa0aJmT3jibT9cBia7d5zVXaicXt7hOgqubbQml5JlHFO2TPBMtfaKWKgCcUw6Zm361tHpSRTDC3UGaA/640?wx_fmt=gif&from=appmsg&random=0.06411152754203409&random=0.907896831686954&random=0.5505130419565429&random=0.8311224142095746&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=6)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NSKgl3moHDOKbbpEYgNSItjNFD91nzBwV22FXChCyUM74Em13eLhTjzywXKRyvOTz3bTOJcH4dAMNMhGf0EDW0XGeqWiaGKibnoSvRVWS0ibao/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU1OTUxNTI1NA==&mid=2247593921&idx=1&sn=889470b7c5f559c8c601486ef62cee66&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NSKgl3moHDNREsYP3IFOibK9FbL4w5JrqetSLmoKgg31eF4VAPf9qBMrBKo1EcGDerGPxKwKXwo7McynlO6EsxUz7v7lKKBsQNSgNGjaQjTk/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=MzU1OTUxNTI1NA==&scene=1&album_id=4247809644921733135&count=3#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NSKgl3moHDMe58j1iayAiabnvjD6ksGLRqwGVq7ENN1MNuEdbtxerZg5Nv1IAfYxjRgNsjwd1jcWf5Rcu2gFRibo6p5c9Gr6OxBoVtxVmI3tVs/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU1OTUxNTI1NA==&mid=2247594123&idx=1&sn=3bc636c3480a3fc207082e8f38ad41ec&scene=21#wechat_redirect)![图片](https://mmbiz.qpic.cn/mmbiz_gif/NSKgl3moHDMhRE4SAfoKUON8b33n7pamt4x65j3Usv8bl2Ujh8IcKodg6qibOicrLgPHVXianddzemyKrWHSC71CfF42vjmXaYh58eiaBzCzf9M/640?wx_fmt=gif&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/NSKgl3moHDOOzONSEjl5bmyED1NUgcSIXU5MLTO9VnZhBbs4XrsEZNRccO0bH335ib1uQfEQWvPVMkJPlokjIO4GAKJccW1IJoRkdRdMCA8w/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DSmmCibR6DZOw08aibGCM2Ba16dKgxVUHiclVkmNtxRiaQxX8Wt5lWjiajBT0nollghRq2xHPHCY7d2HZ2YMLKKe0xA/0?wx_fmt=png)

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