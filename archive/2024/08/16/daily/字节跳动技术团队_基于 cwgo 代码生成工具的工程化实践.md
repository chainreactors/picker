---
title: 基于 cwgo 代码生成工具的工程化实践
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508846&idx=1&sn=5b03b0bfc7de23b410453c527471f022&chksm=e9d3688cdea4e19a14965d58191678b5f202cf7838280cbb0f9f0809268af961fe9c7e5335c7&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-08-16
fetch_date: 2025-10-06T18:04:49.742555
---

# 基于 cwgo 代码生成工具的工程化实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh9Ce0uqBHdTNurI1eUicmfwBicibJ3SWCKe20GQM8wrGAxUicEaKlE0FpN4N3fBw3AsXVOtdrgrCn1RA/0?wx_fmt=jpeg)

# 基于 cwgo 代码生成工具的工程化实践

鹿瑞超

字节跳动技术团队

## **01** **开发背景与功能概览**

cwgo 是 CloudWeGo 社区的一站式代码生成工具。hz 是 Hertz 的脚手架工具，kitex 是 Kitex 的脚手架工具，在开发 cwgo 之前，这两个脚手架工具之间是相对独立的，使用方式是存在差异的，针对 IDL 的要求也存在差异。hz 要求 IDL 中需要存在 http 相关的注解，kitex 就没有该要求。用户在使用时需要遵守对应框架的所有要求和规范，用户跨组件学习成本就高了起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5s4IwpibuezAiaFfbGeMZzsiboaZoDV33EGZyc02LWTdYTPicTkIFGRAV79A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

此外，组件各自的工具缺少一个全局视角，如果我们想开发一个完整的微服务项目的话，那么工具的代码生成就会涉及到若干个子命令和 flags，配合的复杂度较高，且在不断引入更多新能力后，复杂度将进一步提升。用户学习门槛会不断提高，削弱了用户的使用体验效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5saRullO5HkbtU0ZuSH40QYCmgflibnfU0u93picMErkQEHb0iaXNjpIylw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

cwgo 就是围绕以上背景进行开发的，cwgo 是 CloudWeGo 社区提供的用于生成代码的一个命令行工具，它整合了包含了 hz、kitex 在内的各个组件的优势，覆盖了用户所需要的各类代码生成的需求，比如服务端/客户端生成代码，数据库生成代码等等，所以说 cwgo 是 CloudWeGo 社区提供的 **All in One 的代码生成工具**。cwgo 可以给用户提供全面的、完备的、易用的**研发体验**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5sIVf9iaCu2llIymIDJ3rNCaicanFofouF0APeF9GUcW3zENEDTb7iajQug/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**目前 cwgo 支持 thrift 和 protobuf 的 IDL 生成，支持 server 端和 client 端的代码生成，同时也支持 mysql 和mongodb 等 crud 的代码生成。**cwgo 工具并不直接生成代码，而是构造好模板后调用相应工具的生成函数。比如server，client 命令，http 类型使用 hz 进行生成，rpc 类型使用 kitex 生成，mysql 代码通过 gorm/gen 生成，mongodb代码有些不同，它是通过 thriftgo/protoc 解析 IDL 后通过构建抽象语法树然后生成的代码。所以相对应工具的注意事项也需要遵守， 如生成 rpc 代码时 kitex 的注意事项和生成 http 代码时 hz 的注意事项。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5su2iaDC7hlL8BlpoRponEl71Tib68iaV6t1Uia5HTfCJfQMDmae9ztPg2kQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **02** **服务端/客户端代码生成**

cwgo 工具通过整合 hz/kitex 工具，从而支持使用  IDL (thrift/protobuf) 生成 Server/Client 端的代码，极大简化了项目开发的过程，提升了用户的体验。

## **Server/Client 命令**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5ssb1PRGFU3z8LLhzWjz6NSwbsMJ9wzKQ821jiceGR2dxX33kiaFTgRx2A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在开发一个微服务项目时，只需通过执行三个命令，即可生成一个微服务项目所需要的桩代码。

```
cwgo server --type RPCcwgo client --type RPCcwgo server --type HTTP
```

cwgo 的服务端和客户端调用代码生成的功能主要是通过解析命令行参数然后透传给 hz/kitex 工具进行实现的，如果想使用 hz/kitex 的一些进阶参数有两种方式：一种是通过 pass 参数来把额外参数传递给 hz 或是 kitex，另一种是 cwgo 支持回退功能，允许回退为 kitex 或是 hz，对于用户存量的 Kitex/Hertz 项目，工具需要保持兼容。回退后，命令行工具表现将与 kitex 或 hz 保持一致，区别就是在前面加上了cwgo fallback。

```
cwgo server --type HTTP --pass "-handler_dir ./handler"cwgo fallback hz new -module cwgo -idl hello.thrift
```

## **Hex 计划**

cwgo server 命令支持**在一个端口同时启用 http 服务和 rpc 服务**，这就是 cwgo 的 Hex 能力。Hex 的实现原理主要是通过实现 Kitex 的传输模块扩展来获取 bytebuffer 中的数据，分析出是 http 还是 rpc 请求再使用 Hertz 或是 Kitex 进行请求处理。如下是 Kitex 对 Netpoll 同步 IO 的扩展，分别实现了 Extension、ByteBuffer、TransServer 接口，这三个接口实现了 TransHandler，TransHandler 是对消息的处理接口，ByteBuffer 是读写接口。相同的 IO 模型下 TransHandler 的逻辑通常是一致的，Kitex 对同步 IO 提供了默认实现的 TransHandler，针对不一样的地方抽象出了 Extension 接口，所以在同步 IO 的场景下不需要实现完整的 TransHandler 接口，只需实现 Extension 即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5sAGZPzL5JdibzkBFRIbAticYtSeJa5eoQhnVoJdDs8osLib5NFpoStqQlA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **模板生成**

cwgo 默认提供了 **MVC Template** 生成 Server 代码，若默认模板不满足用户的需求，可自定义自己的模板。cwgo 工具目前支持仅生成 MVC Layout，未来还会拓展更多的模板供用户使用。使用 cwgo 工具生成 server 代码时会自动生成 MVC layout。

HTTP 项目目录如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5s4CO8R24RJZSBiaYf5BNODmn17k3PjEbEHykHVzvEd5paEyuia8kdibQ5w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

RPC 项目目录如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5s67s36mkkQYVic1saE2CtgPraWMkIFRMwHENPznyIIy10fcvO0Saib4Vg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

cwgo 支持从本地或 git 中读取模板。其中 git 支持 https 或 ssh 的形式，通过 -template 指定模板路径，-branch 指定模板分支（默认为主分支）。cwgo 除了支持 **go template** 默认模板函数外，还集成了 **sprig** 模板扩展函数，进一步满足了用户需要高度定制模板的需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5s5PZYhicw35KPS1HsG01egxUBRbN5AXXRzmIEIK6q8velFRMswa9BXng/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **03** **数据库代码生成**

cwgo 的数据库代码生成能力包括两部分：

1. doc 命令生成 **mongodb** crud 代码

2. model 命令生成**关系型数据库** sql 代码

其中，model 命令依赖 gorm/gen 工具生成代码，doc 命令基于 IDL 的注解以及 IDL 代码生成工具的插件机制生成代码。目前，IDL 支持 thrift 和 protobuf，底层使用的 IDL 代码生成工具为 thriftgo 和 protoc。

## **model**

cwgo 集成了 gorm/gen 用于帮助用户生成 model 代码以及基础的 crud 代码，用户无需再自行封装繁琐的 crud 代码，极大的提高了用户的开发效率。用法示例如下：

```
cwgo  model --db_type mysql --dsn "gorm:gorm@tcp(localhost:9910)/gorm?charset=utf8&parseTime=True&loc=Local"
```

## **doc**

doc 命令支持基于 IDL (thrift protobuf) 的注解以及 IDL 代码生成工具的插件机制来生成 mongodb 的 crud 代码，用户可以通过命令参数指定 idl 路径、代码生成的位置，若有其他需求，也可以将参数透传给底层的代码生成工具 thriftgo 或 protoc。

以 thrift 为例介绍 doc 命令的实践，在 thrift 文件中，struct 对应 mongodb 中的集合，用户除定义好结构体外，还需定义注解，有两种注解：字段注解和结构体注解。其中字段注解用于指明字段对应的 mongodb go tag，结构体注解由四部分组成：工具解析所用 token、函数名、入参、返回值。token 的编写需遵循工具的规则，例如，首单词为 Insert 表示插入数据，首单词为 Find 表示查询数据，函数名为生成的 crud 代码中对应的函数名，入参和返回值也需遵循工具的规则，通常与对应的 token 有关。

在如下给出了一个用户结构体，在结构体注解中给出了四个 token，代表增删改查四种操作，然后通过 cwgo doc 命令生成对应代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5sk4mHYBO41NicTbMWljbBgu6zib6yLm06mhLD521Ut8icOVlicSibQp233Lg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5smOrcTGCDpIaJnWqUUmDH5ffj8RhnPiabpJcicOHVTGTPBbCNGnG02ic1A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

生成的代码结构如下所示，包含三部分内容：

* user\_repo.go：函数接口文件
* user\_repo\_mongo.go：接口实现及具体 crud 代码
* user.go：thriftgo 生成的桩代码，包含对应的结构体

其中，biz/doc/dao下的代码是 mongodb 的 crud 相关代码，这部分由 cwgo 借助 thriftgo 插件机制生成，biz/doc/model 下生成的是 idl 对应的桩代码，由 thriftgo 工具生成，这里面包含了 mongodb 集合对应的 go 结构体代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5shK7jd8BicRlBarVR8DuKJNBLdhpTuUfGQu48taJccbHGwPRroxjcfyQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

生成的部分代码产物如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5sWg78QPoVpfzfYS3A3cWKXHPvxPahsuepvcYAA4qCYGcv0oyCo2GTxw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5sSuNYViayct8kgvEgSxCuwcwdUicHTSdicceyaJWnSyJnnMROI8HGiaAZtQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

此外，cwgo doc 提供了一个兜底处理：在现有生成代码不满足用户需求时使用基础 mongo 代码，可以为用户省去开发和测试 mongodb 公共库的时间。

使用命令以及生成的代码产物如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5stFmbzsvonT7lIaHPngCbVLjDYosrqsibSYuQuxX0NMxmA2szGNrXsSQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BvYvvlJIDbIBayaWBKxF5mqpwW2H7H5syy1c3qCHwfvIY3ibSLq2PCnetwG3RqtoiaNhZm9GciazhP1xWqXSjncfw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## **04** **未来展望**

CloudWeGo 社区今年在开源之夏编程夏令营开放了 cwgo 相关的项目，包括基于 IDL 生成 swagger 文档，基于 IDL 生成 raw\_sql 代码，基于 IDE 插件一键创建 CloudWeGo 服务等。还有一些 cwgo 未来想做的事情放在了 issue 中，欢迎大家认领并提交 pr。cwgo 已经帮助多个企业用户获得了真实收益，欢迎大家关注 cwgo，参与到 CloudWeGo 社区和 cwgo 项目的开源建设中来。

> cwgo 项目地址：
> https://github.com/cloudwego/cwgo
>
> cwgo 项目文档：
> https://www.cloudwego.io/zh/docs/cwgo/overview/

**项目地址**

GitHub：https://github.com/cloudwego

官网：www.cloudwego.io

# **点击【****阅读原文****】查看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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