---
title: 不许动，你被劫持了！
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247525424&idx=1&sn=8b545e6944b395e31bed96ee13d491e0&chksm=c2d11894f5a69182f49978fa0dde77a3d06e598cd26c8abce533c961868226bb163e69793f30&scene=58&subscene=0#rd
source: Yak Project
date: 2024-11-22
fetch_date: 2025-10-06T19:17:22.610102
---

# 不许动，你被劫持了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdfricLK2n9Xn0ibMeWzuGfnqSy994d3KZBuMGDKPByRQiaRH61h88En8aA/0?wx_fmt=jpeg)

# 不许动，你被劫持了！

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

**“Stop！Yak MITM Open The Door！”**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdMWCg0ODibowOev4ooxDkfs8Z1iaqmgGM1gaRWywIUCVW8xeriaPaPH30w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdBj05VV5yoJoict5hgubGYGmMtwQvPauAY9Xd6Z2xbJo9FagFdLuImHnrYzTsBTVjicFNNv6DkowKA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmd2ib36XoQeiaPfI0s2Zic8q85SboEEzblaMLZcpTj3iaTFWz2Wxdg2GCk3w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdQ0xtxmLrZuOKTWvmODk9XDUyRHTGy0BdbQamsYiblFr7nXFOksOyANQ/640?wx_fmt=png&from=appmsg)

**新的HTTP请求**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

对于每个进入MITM的HTTP请求，MITM服务器会启动一个**新的线程**来对其进行处理。

**过滤器**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

之后，流量会先进入过滤器，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdxJWdDDF1Cnibg5vf5WVHibicSribict1xHDaGBKv9KDiaKDWK8SBGNbreqdg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdlH7UQxs5s8MrxgCsKvBtNZgMjoQU1ebgjYNcKCeX89GRY8CI8BK5vA/640?wx_fmt=png&from=appmsg)

**过滤器决定请求是应该被过滤（即自动放行）还是应该继续进入后续的流程。**

对于请求来说，过滤器支持对Hostname（主机名）、URL路径、请求方法进行过滤。

被过滤器过滤的请求会自动放行（直接流向目的服务器/代理服务器），并返回响应，中途不会再经过绝大多数模块（Yakit劫持，内容规则）的处理。

**检测请求方法**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

对于没有过滤的请求，会再单独检查请求方法，对于Connnect请求方法，MITM服务器会特殊处理，而其他方法则进入到下一个模块中。

**内容规则**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

然后，请求会进入内容规则模块的处理，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdX4nQufhFM5YeZFXGLdwnn2pxvAX2ER4ibicjjLicbjVOMtViayAH7zuSBQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmd1hspIicmkU7IqUe9uga4aHtTXOuu1AXS9ibaQROvPDZxSea28H1icdHlQ/640?wx_fmt=png&from=appmsg)

请求会经过每一个处理请求的规则（会优先经过需要替换的规则），并会对该流量进行提前的染色或者添加标签。需要特殊注意的是，**如果某个规则对请求进行了丢弃，就不会再进入后续的流程。**

**方法：hijackRequest**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

接下来，请求会进入插件/热加载中的hijackRequest方法进行处理，**经过处理的请求可能会被丢弃（不会再进入后续的流程）**，或者被修改。

```
// hijackHTTPRequest 每一个新的 HTTPRequest 将会被这个 HOOK 劫持，// 劫持后通过 forward(modified) 来把修改后的请求覆盖// 如果需要屏蔽该数据包，通过 drop() 来屏蔽hijackHTTPRequest = func(isHttps, url, req, forward /*func(modifiedRequest []byte)*/, drop /*func()*/) {}
```

**Yakit前端**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

接着，请求会进入到Yakit前端，Yakit前端有三个模式，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdfZZHuLrugXHHl4mIsFISVwuBWSyuN8aQsicgtwgOswf7eKjWGtcTljQ/640?wx_fmt=png&from=appmsg)

除了手动劫持以外，**剩下的两个模式都会将请求自动放行（直接流向目的服务器/代理服务器）并记录在History中**。对于手动劫持的请求，用户可以手动为其添加颜色或标签，修改请求，提交数据或丢弃数据，**丢弃数据后不会再进入后续的流程。**

**方法：beforeRequest**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

后续，请求会进入插件/热加载中的beforeRequest方法进行处理，经过处理的请求可能被修改。

```
// beforeRequest 允许发送数据包前再做一次处理，定义为 func(origin []byte) []bytebeforeRequest = func(req) {}
```

**全局配置-禁用IP/禁用域名**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

之后，即将发出的请求还会经过系统配置 - 全局配置中的禁用IP/禁用域名，对于禁用的IP或域名，请求会被自动丢弃并且不会再进入后续的流程：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdhickRU9s7aWrllC4oG6QQ43t3IggRX0KiaJs0vTpzMF9Yu8tBBJBYICg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdP9UMyJueoDtUNhaDYbiaXhypAU287xWIdsnYT8YF3oOy8sAAtSpV7FA/640?wx_fmt=png&from=appmsg)

**发起请求，接收响应**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

请求会被发往目的服务器/代理服务器，然后接收到对应的响应。

**再次进入过滤器**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

对于响应，会再次进入过滤器，对于响应来说，过滤器支持对Content-Type，文件后缀进行过滤。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdlH7UQxs5s8MrxgCsKvBtNZgMjoQU1ebgjYNcKCeX89GRY8CI8BK5vA/640?wx_fmt=png&from=appmsg)

**过滤器决定响应是应该被过滤还是应该继续进入后续的流程。**

对于被过滤器过滤的响应，流量不会记录到History中，中途不会再经过绝大多数模块的处理，**只会镜像到插件或热加载中mirrorHTTPFlow方法中。**

**方法：hijackResponse/hijackResponseEX**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

请求与响应会依次进入插件/热加载中的hijackResponseEx，hijackResponse方法。经过处理的响应可能被修改或被丢弃，**被丢弃的流量不会再进入后续的流程。**

```
// hijackHTTPResponse 每一个新的 HTTPResponse 将会被这个 HOOK 劫持，劫持后通过 forward(modified) 来把修改后的请求覆盖，如果需要屏蔽该数据包，通过 drop() 来屏蔽hijackHTTPResponse = func(isHttps, url, rsp, forward, drop) {}
hijackHTTPResponseEx = func(isHttps, url, req, rsp, forward, drop) {}
```

```

```

**第二次：内容规则**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

响应会经过每一个处理响应的规则（会优先经过需要替换的规则）并会对该流量进行染色或者添加标签。需要特殊注意的是，**如果某个规则对响应进行了丢弃，就不会再进入后续的流程。**

**可选：再次进入Yakit前端**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

如果首次进入Yakit前端时设置了劫持响应，那么响应会再次进入Yakit前端。Yakit前端有三个模式，除了手动劫持以外，**剩下的两个模式都会将响应自动放行（跳过此流程，继续后续流程）。**对于手动劫持的响应，用户可以手动为其添加颜色或标签，修改响应，提交数据或丢弃数据，**丢弃数据后不会再进入后续的流程。**

**方法：afterRequest**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

后续，响应会进入插件/热加载中的beforeRequest方法进行处理，经过处理的请求可能被修改。

```
// 在回复给浏览器之前的hookafterRequest = func(ishttps, oreq/*原始请求*/ ,req/*hiajck修改之后的请求*/ ,orsp/*原始响应*/ ,rsp/*hijack修改后的响应*/){}
```

**创建流量**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

根据最终的请求，响应以及前面标注的颜色，标签创建流量，并准备存储进入数据库。

**第三次：内容规则**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

响应会经过每一个规则，对匹配到对应规则的流量进行染色或者添加标签。

**方法：hijackSaveHTTPFlow**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

后续，流量会进入插件/热加载中的hijackSaveHTTPFlow方法再最后进入数据库之前进行处理，用户可以在此对流量进行修改（修改请求/修改响应/添加标签等）或者丢弃。**丢弃的流量不会存储进数据库中。**

```
hijackSaveHTTPFlow = func(flow /* *yakit.HTTPFlow */, modify /* func(modified *yakit.HTTPFlow) */, drop/* func() */) {}
```

**流量进入数据库**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc3Lvia3V1rDstUx0IjX6HdxIRWxia3pKAohgAp53zPBsQCphZrbr586FvcV56vaJiayYzNX7WRbxrGw/640?wx_fmt=png&from=appmsg)

流量在进入数据库之前会等待前序的内容规则/hijackSaveHTTPFlow最多300毫秒，之后若流程完成或超时，都会将非丢弃的流量存储进数据库中。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfOW6F7ZnTy4F1iaCibSVibbmdYyzqBtGUASGxh6ELGDkDIhp3o0fChEWicK2M0sFiawxDBqSMJqGaE7Fg/640?wx_fmt=png&from=appmsg)

![](https:/...