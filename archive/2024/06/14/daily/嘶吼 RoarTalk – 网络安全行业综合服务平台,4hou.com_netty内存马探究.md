---
title: netty内存马探究
url: https://www.4hou.com/posts/1pxV
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-06-14
fetch_date: 2025-10-06T16:55:23.482293
---

# netty内存马探究

netty内存马探究 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# netty内存马探究

盛邦安全
[技术](https://www.4hou.com/category/technology)
2024-06-13 14:30:33

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)159934

收藏

导语：基于netty动态创建pipeline的特性，其内存马的构造思路与tomcat有一定的区别，目前网上有关netty内存马的文章都围绕CVE-2022-22947和XXL-JOB两种场景展开，并未对其做更为详细的分析。

**0x01 前言**

基于netty动态创建pipeline的特性，其内存马的构造思路与tomcat有一定的区别，目前网上有关netty内存马的文章都围绕CVE-2022-22947和XXL-JOB两种场景展开，并未对其做更为详细的分析。本文就以上述两种场景为始，尝试从源码角度探究netty内存马的部分细节，以供大家参考。

**0x02 Netty介绍**

I/O事件：分为出站和入站两种事件，不同的事件会触发不同种类的handler。

Handler (ChannelHandler)：handler用于处理I/O事件，继承如下几种接口，并重写channelRead方法完成请求的处理，功能类似于filter。

```
ChannelInboundHandlerAdapter 入站I/O事件触发该
handlerChannelOutboundHandlerAdapter 出站I/O事件触发该
handlerChannelDuplexHandler 入站和出站事件均会触发该handler
```

Channel (SocketChannel)：可以理解为对 Socket 的封装, 提供了 Socket 状态、读写等操作，每当 Netty 建立了一个连接后，都会创建一个对应的 Channel 实例，同时还会初始化和 Channel 所对应的 pipeline。

Pipeline (ChannelPipeline)：由多个handler所构成的双向链表，并提供如addFirst、addLast等方法添加handler。需要注意的是，每次有新请求入站时，都会创建一个与之对应的channel，同时channel会在io.netty.channel.AbstractChannel#AbstractChannel(io.netty.channel.Channel)里创建一个与之对应的pipeline。

![QQ截图20240613133905.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257620127978.png "1718257319109553.png")

构造netty内存马的一个思路，就是在pipeline中插入我们自定义的handler，同时，由于pipeline动态创建的特性，如何保证handler的持久化才是关键，本文以此为出发点，尝试探究netty内存马在不同场景下的利用原理。

**0x03 CVE-2022-22947**

先来简单回顾一下CVE-2022-22947是如何注入内存马的，文中的核心是修改reactor.netty.transport.TransportConfig#doOnChannelInit，在reactor.netty中，channel的初始化位于reactor.netty.transport.TransportConfig.TransportChannelInitializer#initChannel。

关键点如下：

![QQ截图20240613133921.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257621545196.png "1718257340108556.png")

config.defaultOnChannelInit()返回一个默认的ChannelPipelineConfigurer，随后调用then方法，进入到reactor.netty.ReactorNetty.CompositeChannelPipelineConfigurer#compositeChannelPipelineConfigurer，从函数名也能够看出，这个方法用于合并对象，将当前默认的ChannelPipelineConfigurer与config.doOnChannelInit合二为一，返回一个CompositeChannelPipelineConfigurer。

随后调用CompositeChannelPipelineConfigurer#onChannelInit，在此处循环调用configurer#onChannelInit，其中就包括我们反射传入的doOnChannelInit#onChannelInit。

![QQ截图20240613134233.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257622104882.png "1718257359384485.png")

c0ny1师傅给出的案例，就在onChannelInit内完成handler的添加，由于反射修改了doOnChannelInit，后续有新的请求入站，都会重复上述流程，进而完成handler的持久化。

```
public void onChannelInit(ConnectionObserver connectionObserver, Channel channel, SocketAddress socketAddress) {     ChannelPipeline pipeline = channel.pipeline();          pipeline.addBefore("reactor.left.httpTrafficHandler","memshell_handler",new NettyMemshell()); }
```

另外，从reactor.netty.transport.TransportConfig#doOnChannelInit的路径也能看出，该场景依赖 reactor.netty，并不适用纯io.netty的环境，如xxl-job等场景。

**0x04 XXL-JOB**

对于纯粹的io.netty环境，在XXL-JOB内存马中给出的答案是定制化内存马，核心思想是修改com.xxl.job.core.biz.impl.ExecutorBizImpl的实现，由于每次请求都会触发ServerBootstrap初始化流程，随即进入.addLast(new EmbedHttpServerHandler(executorBiz, accessToken, bizThreadPool));，而EmbedServer中的executorBiz在仅在启动时触发实例化，在整个应用程序的生命周期中都不变，使用动态类加载替换其实现，就能完成内存马的持久化。

![QQ截图20240613134332.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257623123377.png "1718257418148049.png")

在文章开头，作者也曾尝试反射调用pipeline.addBefore，依然是上面所提到的问题，不过很容易发现，通过ServerBootstrap所添加的EmbedHttpServerHandler能够常驻内存，如果我们想要利用这一特性，还需进一步分析io.netty.bootstrap.ServerBootstrap的初始化过程。

**0x05 ServerBootstrap**

限于篇幅，这里仅截取关键代码，直接定位到pipeline创建完成之后的片段，首先io.netty.bootstrap.ServerBootstrap#init在pipeline中添加了一个ServerBootstrapAcceptor，需要注意一下这里的childHandler，这也是一种持久化的思路，后续会继续提到。

![QQ截图20240613134401.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257624154451.png "1718257447821607.png")

此时pipeline在内存中的情况如下，可以看到已经添加了ServerBootstrapAcceptor。

![QQ截图20240613134442.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257625937862.png "1718257498117965.png")

netty介绍部分提及过handler的channelRead方法用于处理请求，因此可以直接去看io.netty.bootstrap.ServerBootstrap.ServerBootstrapAcceptor#channelRead的实现，这里ServerBootstrapAcceptor把之前传入的childHandler添加到pipeline中。

![QQ截图20240613134450.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257626434872.png "1718257514187170.png")

childHandler由开发者所定义，通常会使用如下范式定义ServerBootStrap，也就是添加客户端连接时所需要的handler。

```
ServerBootstrap bootstrap = new ServerBootstrap();bootstrap.group(bossGroup, workerGroup)        .channel(NioServerSocketChannel.class)        .childHandler(new ChannelInitializer            @Override            public void initChannel(SocketChannel channel) throws Exception {                channel.pipeline()                        .addLast(...)                        .addLast(...);            }        })
```

由开发者所定义的ChannelInitializer最终会走到ChannelInitializer#initChannel进行初始化，调用栈如下：

![QQ截图20240613134545.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20240613/1718257627109718.png "1718257551205592.png")

总结一下该流程，每次请求都将触发一次ServerBootstrap初始化，随即pipeline根据现有的ChannelInitializer#initChannel添加其他handler，若能根据这一特性找到ServerBootstrapAcceptor，反射修改childHandler，也完成handler持久化这一目标。

**0x06 内存马实现**

在探究netty的过程中，发现这样一篇文章: xxl-job利用研究，作者给出的EXP已经很接近完整版了，在文章的最后抛出两个问题，一是"注册的handler必须加上@ChannelHandler.Sharable标签，否则会执行器会报错崩溃"，二是"坏消息是这个内存马的实现是替换了handler，所以原本执行逻辑会消失，建议跑路前重启一下执行器"。

这两个问题很容易解决：

1、对于需要加入@ChannelHandler.Sharable这点而言，实测是不需要的，由于我们自定义的handler是通过new的方式创建的，理论上来讲就是unSharable的。

2、反射修改ChannelInitializer导致执行器失效的问题，只需要给bootstrap添加一个EmbedHttpServerHandler就能保留其原有功能。

```
setFieldValue(embedHttpServerHandler, "childHandler", new ChannelInitializer    @Override    public void initChannel(SocketChannel channel) throws Exception {        channel.pipeline()                .addLast(new IdleStateHandler(0, 0, 30 * 3, TimeUnit.SECONDS))  // beat 3N, close if idle                .addLast(new HttpServerCodec())                .addLast(new HttpObjectAggregator(5 * 1024 * 1024))  // merge request & reponse to FULL                .addLast(new NettyThreadHandler())                .addLast(new EmbedServer.EmbedHttpServerHandler(new ExecutorBizImpl(), "", new ThreadPoolExecutor(                    0,                    200,                    60L,                    TimeUnit.SECONDS,                    new LinkedBlockingQueue                    new ThreadFactory() {                        @Override                        public Thread newThread(Runnable r) {                            return new Thread(r, "xxl-rpc, EmbedServer bizThreadPool-" + r.hashCode());                        }                    },                    new RejectedExecutionHandler() {                        @Override                        public void rejectedExecution(Runnable r,...