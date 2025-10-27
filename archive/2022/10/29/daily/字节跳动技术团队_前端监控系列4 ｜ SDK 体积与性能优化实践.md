---
title: 前端监控系列4 ｜ SDK 体积与性能优化实践
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247499658&idx=1&sn=c02ab0abc683f9869c1328c9a3873fd4&chksm=e9d33468dea4bd7e1f8f3b8ffa93e2a6a2a9e6d688f3a00bd7e18da218a30f9e3c6a698123ae&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2022-10-29
fetch_date: 2025-10-03T21:14:45.182731
---

# 前端监控系列4 ｜ SDK 体积与性能优化实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5EcwYhllQOh6Z9K59dicHaM3DdhNLmBmAELG91YRKFhrSoDGrJR0ZzBnzyfPP6IkXVxFicjHEymA9UQkXhGngpRg/0?wx_fmt=jpeg)

# 前端监控系列4 ｜ SDK 体积与性能优化实践

嵇晓濛

字节跳动技术团队

**动手点关注**

**![](https://mmbiz.qpic.cn/mmbiz_gif/JaFvPvvA2J063TNzibibGfI89U9UaWNPqYGUFNRVJ1TkA4Bv0Ew946EkhX4dNibLx6ZK9E4ibdtqH01ZGs9a4gvo4w/640?wx_fmt=gif)**

**干货不迷路**

# 背景

字节各类业务拥有众多用户群，作为字节前端性能监控 SDK，自身若存在性能问题，则会影响到数以亿计的真实用户的体验，所以此类 SDK 自身的性能在设计之初，就必须达到一个非常极致的水准。

与此同时，随着业务不断迭代，功能变得越来越多，对监控的需求也会变得越来越多。例如，今天 A 业务更新了架构，想要自定义性能指标的获取规则，明天 B 业务接入了微前端框架，需要监控子应用的性能。在解决这些业务需求的同时，我们会不断加入额外的判断逻辑、配置项。同时由于用户的电脑性能、浏览器环境的不同，我们又要解决各种兼容性问题，加入 polyfill 等代码，不可避免地造成 SDK 体积膨胀，性能劣化。那么我们是如何在需求和功能不断迭代的情况下，持续追踪和优化 SDK 的体积和性能的呢？

# SDK 体积优化

通常而言，体积的优化是最容易拿到收益的一项。

由于监控 SDK 通常作为第一个脚本被加载到页面中，体积的膨胀不仅会增加用户的下载时间，还会增加浏览器解析脚本的时间。对于体积优化，我们可以从宏观和微观两个角度去实现。

微观上，我们会去尽可能去精简所有的表达，剥离冗余重复代码，同时尽可能减少以下写法的出现：

1. **过多的 class 和过长的属性方法名**

Class 的定义会被转换成 function 声明 + prototype 赋值，以及常用代码压缩工具无法对 object 属性名压缩，过多的面向对象写法会让编译后的 js 代码体积膨胀得非常快。例如下列代码：

```
class ClassWithLongName {
    methodWithALongLongName() {}
}
```

经过 ts 转换后会变成：

```
var ClassWithLongName = /** @class */ (function () {
    function ClassWithLongName() {
    }
    ClassWithLongName.prototype.methodWithALongLongName = function () { };
    return ClassWithLongName;
}());
```

压缩后代码为：

```
var ClassWithLongName=function(){function n(){}return n.prototype.methodWithALongLongName=function(){},n}();
```

可以看到以上长命名都无法被压缩。

如果使用函数式编程来代替面向对象编程，能够很好的避免代码无法被压缩的情况：

```
function functionWithLongName() {
  return function MethodWithALongLongName(){}
}
```

经过压缩后变成：

```
function n(){return function(){}}
```

相较于 class 的版本，压缩后的代码减小了50%以上。

2. **内部函数传参使用数组代替对象**

原理同上，对象中的字段名通常不会被代码压缩工具压缩。同时合理使用 TS named tuple 类型可以保证代码可维护性。

```
function report(event, {optionA, optionB, optionC, optionD}: ObjectType){
}
```

改为：

```
function report(event, [optionA, optionB, optionC, optionD]: NamedTupleType){
}
```

3. 在不需要判断 nullable 时，尽可能避免 `?.` `??` `??=` 等操作符的出现。同理，尽可能避免一些例如 spread 操作符、generator 等新语法，这些语法在编译成 es5 后通常会引入额外的 polyfill。

TS 会将这些操作符转换成非常长的代码，例如 `a?.b`会被转换成：

```
a === null || a === void 0 ? void 0 : a.b
```

过多的 nullish 操作符也是代码体积增加的一个原因。

当然，以上只列举了部分体积优化措施，还有更多优化方法要结合具体代码而议。对于我们的前端监控 SDK，为了性能和体积是可以牺牲一些开发体验的，并且由于使用 TS 类型系统，并不会对代码维护增加很多负担。

从宏观上，我们应该思考如何减少 SDK 所依赖的模块，减少产物包含的内容，增加产物的“信噪比”，有以下几个方式：

1. **拆分文件**

我们可以分离出 SDK 中不是必须提前执行的逻辑，拆分成异步加载的文件，仅将必须提前执行的逻辑加入初始脚本。同时将不同功能拆分成不同文件，业务按需加载，这样可以最大程度减少对首屏加载时间的影响。

2. **尽可能避免 polyfill 的使用**

polyfill 会显著增加产物体积，我们尽可能不使用存在兼容性的方法。甚至在不需要兼容低端浏览器环境时，我们可以不使用 polyfill。

3. **减少重复的常量字符串的出现次数**

对于多次重复出现的常量字符串，提取成公共变量。例如

```
a.addEventListener('load', cb)
b.addEventListener('load', cb)
c.addEventListener('load', cb)
```

我们可以将 `addEventListener`和 `load` 提取公共变量：

```
let ADD_EVENT_LISTENER = 'addEventLister'
let LOAD = 'load'
a[ADD_EVENT_LISTENER](LOAD, cb)
b[ADD_EVENT_LISTENER](LOAD, cb)
c[ADD_EVENT_LISTENER](LOAD, cb)
```

此段代码压缩后会变成：

```
let d="addEventLister",e="load";a[d](e,cb),b[d](e,cb),c[d](e,cb);
```

我们还可以使用 TSTransformer 或者 babel plugin 来帮我们自动地完成上述过程。

值得注意的是，这个方法在 web 端并不能取得很好的收益，因为浏览器在传输数据时会做 gzip 压缩，已经将重复信息用最高效的算法压缩了，我们做的并不会比 gzip 更好。但是在需要嵌入移动端 app 的监控 SDK 来说，这一做法能减少约 10 ~ 15% 产物体积。

除了体积优化以外，随着需求不断增加，功能不断完善，不可避免的会影响到 SDK 的性能。接下来，我们介绍如何测量并优化 SDK 的性能。

# 使用工具进行性能衡量

通常来说，监控类 SDK 最有可能影响性能的地方为：

1. 监控初始化时执行各类监听的过程。

2. 监控事件上报请求对业务的影响。

3. SDK 维护数据缓存时的内存使用情况。

接下来，我们着重从以上几个维度来衡量并优化 SDK 的性能。

### 性能衡量过程

使用 Benchmark 性能衡量工具的目的便是为了知道 SDK 运行过程中每一个函数执行的耗时，给业务带来多大的影响，是否会引起 longtask。由于我们的监控 SDK 包含了性能、请求、资源等各类前端监控能力，这些功能的实现依赖对页面各类事件的监听、性能指标的获取、请求对象的包装。除此之外，SDK还提供给用户（开发者）调用的方法，例如配置页面信息、自定义埋点、更改监控行为等能力。根据 SDK 以上行为和能力，我们将测试分为两个模块：

1. 接入 SDK 后自动运行的各类监控，这些行为大部分会在页面加载之初执行，若此部分性能劣化，会严重影响到所有前端业务用户的首屏加载。

2. 用户端（开发者）调用的方法，我们会将此类方法包装成 client 对象以 npm 包的形式给开发者调用，这部分方法的执行由用户控制，可能存在频繁调用的情况，因此也应避免耗时过长的调用出现。

在过往文章[前端监控系列1｜ 字节的前端监控 SDK 是怎样设计的](http://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247497407&idx=1&sn=217376a862e10ca96f7fc6c615429cb1&chksm=e9d33d5ddea4b44bfc654fdf311ae0230c67e396edd729a89aac655d5fb1a444ee9ba51c571b&scene=21#wechat_redirect)中我们讲到，我们的 SDK 在设计时已经做到的尽可能的解耦，各个模块各司其职，这一特点非常便于我们针对各个模块方法进行单独的性能衡量。

下面我们以使用 benny (https://github.com/caderek/benny) 这一开源工具为例，展示一段方便理解 benchmark 过程的伪代码，仅作参考：

benny 是一个非常简单易用的 benchmark 工具，通过 `suite` 方法创建测试用例组合，通过`add`方法添加需要测试的函数，`cycle`方法用于多次循环执行测试用例，`complete`用于添加测试完成之后的回调函数。更多详细的使用说明可以查阅官方文档。

```
const { suite, add, cycle, complete, save } = require('benny')
// 衡量 SDK 各类监控初始化运行性能
suite(
  'collectors setup',
  add('route', () => route(context)),
  add('exception', () => exception(context)),
  add('ajax', () => ajax(context)),
  add('FCP', getFCP),
  add('LCP', getLCP),
  add('longtask', getLongtask),
  cycle(),
  complete(),
)

// 衡量 Client 实例方法耗时
suite(
  'npm client',
  add('set config', () => client.config({pid})),
  add('set context', () => client.context.set({ something })),
  add('send custom pv', () => client.sendPageView(pid)),
  add('send custom event', () => client.sendCustom(ev)),
  // ...
  cycle(),
  complete(),
)
```

通常这类 benchmark 工具都是在 Node 上执行的，但是我们的 SDK 是个前端监控 SDK，依赖了非常多的浏览器环境对象，我们几乎不可能在 Node 环境去创造或模拟这些对象，我们有没有办法在浏览器里去运行这段脚本，做性能自动化测试呢？

### 利用 Puppeteer 在浏览器环境中执行 Benchmark

由于我们的前端监控依赖浏览器环境，我们可以将上述 benchmark 测试代码打包成 commonjs 之后放入 headless chrome 浏览器中执行，并通过 puppeteer 收集执行结果。

> Puppeteer 是一个 Node 模块，提供了通过 Devtool Protocol 控制 Chrome 或者 Chromium 的能力。Puppeteer 默认运行 Chrome 的无头版本，也可以通过设置运行 Chrome 用户界面版。

下面是一段方便理解操作 puppeteer 过程的伪代码，仅作参考，实际情况较为复杂，需要等待未完成的异步请求等：

```
const browser = await puppeteer.launch()
const page = await browser.newPage()
const cdp = await page.target().createCDPSession()

// 用于 benchmark 脚本和 puppeteer 之间的通信，用以收集结果
await page.evaluate(() => (window.benchmarks = []))
// 将 pushResult 方法暴露给浏览器，来将结果收集到 node 端
await page.exposeFunction(
    'pushResult',
    (result: any) => benchmark.results.push(result)
)

await cdp.send('Profiler.enable')
await cdp.send('Profiler.start')

// 开始执行 benchmark
await page.addScriptTag({
  content: file.toString(),
})

await Promise.race([timeout, allBenchmarksDone()])

// profile 可用于绘制火焰图
const { profile } = await cdp.send('Profiler.stop')
await page.close()
```

通过运行以上脚本，我们便可以在无头浏览器中运行我们的性能测试脚本，在测试脚本产出结果后添加调用 pushResult 方法来收集测试结果。

在实际的 benchmark 测试中，我们发现开启性能监听（即运行各个性能监控的 PerformanceObserver.observe 方法）最大耗时达到了21ms，虽然看上去并不久，但若和其他监听同时执行，加上引入业务代码的复杂性和移动端更弱的 CPU 性能，极有可能成为给业务带来 longtask 的罪魁祸首。性能监控性能成为了瓶颈。

接下来，我们将性能监听一个个拆分，用同样的方式单独测试每一个性能监听的耗时。在实际的 benchmark 结果中，我们发现 fp、fcp、lcp、cls 监控耗时最大，加在一起超过了10ms，占了一半以上，是我们之后需要重点优化的地方。

除此之外利用 puppeteer 的能力，我们不仅可以得到 benchmark 的结果，还可以获取到整个 benchmark 过程的 profile 数据，利用 speedscope (https://github.com/jlfwong/speedscope/blob/main/README-zh\_CN.md) 绘制出函数执行过程中的火焰图：

绘制火焰图的具体实现不在本文讨论范围内，感兴趣的同学可以参考 speedscope 官方文档

![](https://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOh6Z9K59dicHaM3DdhNLmBmAXzqhSSaSibbCseIBKJOZFMib97MiarLmhb9bMYJkePicZ1UeXgf8csE8hQ/640?wx_fmt=png)

此处显示的时间为该用例执行总耗时（单次耗时\*次数）

### 如何衡量异步任务性能？

Benny 的 api 是支持异步测试用例的，测量的是每个异步函数从开始执行到 resolve 的时间。但通常这并不是我们想要的衡量的数据，因为异步任务的执行过程中并不是一直占据着主线程。对于一些异步的定时任务（例如 SDK 的崩溃检测、卡顿检测、白屏检测），将他们拆解为一系列可测的同步任务能更直观的展示各个阶段的性能耗时。

例如我们 SDK 的前端白屏检测，由一个 mutationObserver 和触发白屏检测的函数组成。我们可以单独对 mutationObserver 的回调和触发函数做性能衡量。

这两个方法已没有很好的优化方式了。但是根据 benchmark 结果并结合源码可以发现，性能监控所有指标项的开启均为同步执行，每一项指标都会对页面做事件监听或者 PerformanceObserver 监听，且这些原生监听耗时都在毫秒级。于是我们对性能做了如下优化：

1. 性能监控逻辑分片运行，将各项性能指标的监听同步拆为异步，用 requestIdleCallback (https://developer.mozilla.org/zh-CN/docs/Web/API/Window/requestIdleCallback) 做调度并区分优先级。

2. 多个性能指标监听同一事件的公用监听器，例如 CLS 和 LCP 都需要监听 onBFCacheRestore，让他们只做一次 addEventListener。

3. 可以延迟执行的方法延迟执行，例如在高版本的 Chrome 中 PerformanceObserver 是有 buffer (https://www.w3.org/TR/performance-timeline-2/#dom-performanceobserverinit-buffered) 的，可以直接获取到调用之前的性能指标，这些方法调用就可以等待页面完全加载完成之后执行，从而尽可能减少对业务页面首屏影响。

# 通过 Perfsee 的 Lab 结果分析性能问题

以上的 benchmark 流程得到的结果毕竟是一种理想化、单纯的方法调用的性能情况，然而在实际浏览器环境中我们前端监控 SDK 对性能影响有多大呢，对于这一类页面初始化即加载的 SDK 可以通过 Perfsee (https://perfsee.com/) 的 Lab 功能进行性能衡量。

> Perfsee 是一个针对前端 web 应用在整个研发流程中的性能分析平台。提供性能分析报告、产物分析报告、源码分析、竞品分析等模块，定位与梳理性能问题，提供专业的优化方案来渐进地优化产品性能。
...