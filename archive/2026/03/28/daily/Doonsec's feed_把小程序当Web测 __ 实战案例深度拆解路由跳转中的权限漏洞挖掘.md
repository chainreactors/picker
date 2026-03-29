---
title: 把小程序当Web测 || 实战案例深度拆解路由跳转中的权限漏洞挖掘
url: https://mp.weixin.qq.com/s/bHhudgL_P2Fqb9lW8-E2TA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:32:08.649932
---

# 把小程序当Web测 || 实战案例深度拆解路由跳转中的权限漏洞挖掘

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEm5sEmiaqm1jaRqKTVS577GHiaxAJ6PblP1x2CfVx6LBTT4siaNvmhPDOw/0?wx_fmt=jpeg)

# 把小程序当Web测 || 实战案例深度拆解路由跳转中的权限漏洞挖掘

进击的HACK

![]()

在小说阅读器中沉浸阅读

以下文章来源于Daylight庆尘
，作者庆尘

![](http://wx.qlogo.cn/mmhead/OM4v0FU2h0s97hBneksdKoudzI5qAtzW7vQkBZYfJUTGnoBob4kroP77siaBiapntIBYJ6PKDaXbQ/0)

**Daylight庆尘**
.

专注于代码审计与企业SRC漏洞挖掘思路与案例分享，想了解SRC漏洞挖掘培训的可以联系我，本人亲带

挺久没发文章了，看最近大家对小程序讨论的挺多的，也来凑凑热闹，以下内容纯个人愚见，如有不同想法，欢迎各位师傅交流讨论

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mn2KTdu2R372TBnK8icoZ6npicWKw1K7VwAIrPTdiaRGOpwfaML0dAGXTulE7kyzNFEKnicqcLqqAu0ZDfalrPy6Uw/640?from=appmsg)

*1*

引言

在微信小程序生态中，路由跳转逻辑高度依赖 **URL 路由 + Query 参数** 的方式传递数据。这种设计虽然灵活，但也极易造成**越权、未授权**等漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CpsnZicm5ibzk372TtsuiblpKB3EfsDCib2qqlh4wIFZaPn6nc7IWUv7Hz3gbQktUiaQ2ic95U9Ncx2ibJQiaaUu2OlA3g/640?from=appmsg)

今天这篇文章我们就讲讲怎么快速又精准的完成对路由的测试，从获取完整路由列表，到分析参数，再到完成路由跳转与接口测试，直接把小程序当Web测！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mn2KTdu2R372TBnK8icoZ6npicWKw1K7VwAIrPTdiaRGOpwfaML0dAGXTulE7kyzNFEKnicqcLqqAu0ZDfalrPy6Uw/640?from=appmsg)

为什么小程序路由是测试的关键入口

小程序中常见的页面跳转代码

1、wx.navigateTo

```
# 保留当前页面，跳转到应用内的某个页面wx.navigateTo({  url: '/pages/detail/detail?id=123',  success: function(res) {    // 成功回调  },  fail: function(err) {    // 失败回调  }})
```

2、wx.redirectTo

```
# 关闭当前页面，跳转到应用内的某个页面# 不会保留原页面，适用于登录后跳转等场景wx.redirectTo({  url: '/pages/login/login'})
```

3、wx.switchTab

```
# 跳转到 tabBar 页面，并关闭其他非 tabBar 页面。wx.switchTab({  url: '/pages/index/index' // 必须是 tabBar 中配置的页面路径})
```

这几种跳转方式各有各的特性和适用场景，这些 URL 中的 `id`、`petId` 等参数，跳转之后往往直接作为后端查询接口的参数，如果对应接口的权限校验策略存在问题，则可能导致越权或未授权（本文只探究路由和权限问题）

因此，**全面掌握小程序的所有路由及其参数规则**，是漏洞挖掘的第一步。

但问题来了：**怎么测才最有效？**

*2*

获取路由列表

首先是反编译，这一步必不可少，反编译有很多工具，我这里用的是e0e1，师傅们用自己习惯的工具做反编译就行，无需深究反编译过程，我们只需知道通过反编译工具可提取出小程序的路由配置文件（一般是app.json文件）。而 `app.json` 中的 `pages` 字段，**列出了所有注册的页面路径**，例如我们启动工具后随便对一个小程序进行反编译，结果如下

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEPXzV8ZB2OK0Aa3MnrBRt0eytw4HicqFyI0gvjicTzOoOfeaoSKjOwRaQ/640?wx_fmt=png&from=appmsg)

反编译结果如下

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEupzuU226rQS0x8ANV89lqeOllkyhAwiaIibiaBsiazViaxaNK1rjz6zmMtA/640?wx_fmt=png&from=appmsg)

> 💡 提示：部分动态路由可能未在此列出，但 90% 以上的核心功能页面都会注册于此。

有了这个，我们就知道哪些页面值得深入测试，在测试时可以更关注高价值高风险页面，比如pages/manageUser/manageUser这种路由。

tips:e0e1在反编译时会自动收集所有文件中的路由列表和接口

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEDbm4NtOibf2EQTGWCoVUu7QcQ9eOp5LAYD7XkVVDQHyyOQedeNS0L4w/640?wx_fmt=png&from=appmsg)

内容如下

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fE93dIUkq6fXDDfRZ95iau7B7zo6rhUh1UerceicMjz4t3cLMNuB1VqXvQ/640?wx_fmt=png&from=appmsg)

除了路由列表和接口之外，还能自动收集敏感信息。个人觉得挺好用的

*3*

页面跳转

现在我们已经拿到了这个小程序几乎所有的路由，形如

```
  pages/index/index  pages/archives/archives  pages/archivesDetails/archivesDetails  pages/archivesFirst/archivesFirst
```

到这了是不是心里有疑惑

有了路由那我们该如何访问到路由呢？在测试Web时，发现一个/console/UserManage路由，就可以确认baseurl之后在浏览器直接拼接，但小程序又没有链接输入框，应该如何跳转呢？

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEzCRGxMF8hSX6aCqS5DJEvDLh8dsFxl0O3KZ8mxpeJvT4Th9zSh3TLA/640?wx_fmt=png&from=appmsg)

我看了一些师傅们的跳转手法，有的是通过外部（例如自写工具，自写小程序）做跳板，手动从外部输入路由和参数进行跳转，或者写批量探测工具，直接批量访问反编译后的路由，我个人认为这两个方法都各有优点，但也有需要注意的地方

这里引一个我自己平时测试时，对未授权的分类概念，在我看来未授权分为两种

1、0权到有权：指没有登录的外部用户，能调用本应只有登录后用户才能调用的接口

2、低权到高权：指低权限用户，能调用本应只有高权限用户才能调用的接口

（其实第二种正确的术语应该叫垂直越权，只是师傅们谈到垂直越权，都会想到是拿一个低权限账号和一个高权限账号来测，但这里的垂直越权，我们是只有那个低权限账户的，且测试方法跟单纯的未授权一样，所以我个人测试和给学员们讲课时，喜欢把他定义为未授权）

这里师傅们可以想一下，在测试挖掘未授权时，是第一种场景多，还是第二种的场景多？

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/HkvnVmsSDfIiaaiavwbaZpjicM1Mq6nTqMYPqfhpIHH7iaPRphWRuZhuTXZETh0Bf4THRVXKFh7KQaCeAic6ca3Vxhw/640)

答案是第二种场景更多，两年内，我和学员挖掘了至少三四百个未授权，其中95%以上，都是第二种。那为什么第二种会更常见呢？

因为出现第一种未授权漏洞，代表这个站完全没有做任何的鉴权，或者做的鉴权完全失效，也就是连"卧室大门的锁都没有安装"，但第二种呢？是由于鉴权策略不完善，比如某个接口设计给管理员的，但是没限制普通用户访问，而普通用户又可以被外部正常注册，这就引入了一连串的问题，相当于"两个卧室大门的锁没有做区分"

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEzCRGxMF8hSX6aCqS5DJEvDLh8dsFxl0O3KZ8mxpeJvT4Th9zSh3TLA/640?wx_fmt=png&from=appmsg)

简单来说就是第一种是完全没有做任何鉴权导致的，而第二种是鉴权策略缺陷导致的，这样说师傅们就能理解为什么第二种更多了吧

下面继续回到跳转方法的讨论

1、外部工具跳转

方法：用户通过输入小程序信息，输入路由和参数，然后让跳板进行跳转

优点：能精准携带参数调转到指定路由，如果路由里的接口完全没做鉴权，则会出现未授权问题

缺点：仅能够测试0权场景，相当于不带凭证访问路由，路由中的接口自然也没有凭证，无法测试低权到高权场景

注意点：需要提前打开目标小程序，能登录就登录即可，让登录态保存在本地，这样访问路由时，其内的接口就会自动携带登录态凭证

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEzCRGxMF8hSX6aCqS5DJEvDLh8dsFxl0O3KZ8mxpeJvT4Th9zSh3TLA/640?wx_fmt=png&from=appmsg)

2、批量路由验证

方法：获取反编译后的路由列表，然后用工具批量访问验证

优点：探测速度快，能较快发现明显的问题

缺点：未携带参数，很多路由不会触发数据包，无法测试到对应接口

注意点：非要批量验证的话，建议提前分析路由参数，携带参数再去批量访问

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEzCRGxMF8hSX6aCqS5DJEvDLh8dsFxl0O3KZ8mxpeJvT4Th9zSh3TLA/640?wx_fmt=png&from=appmsg)

3、控制台手动跳转

方法：注入hook之后，console控制台手动输入脚本跳转

优点：测试得更细致，好观察

缺点：测试速度慢，每个路由都要分析

注意点：需要hook

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEzCRGxMF8hSX6aCqS5DJEvDLh8dsFxl0O3KZ8mxpeJvT4Th9zSh3TLA/640?wx_fmt=png&from=appmsg)

控制台手动跳转脚本如下

```
wx.navigateTo({  url: "/pages/archivesDetails/archivesDetails"})
```

这里再讲一下为什么需要找参数，而不能把所有路由直接批量访问

举一个例子，我登录了某个小程序，hook之后在控制台输入如下脚本

```
wx.navigateTo({  url: "/pages/archivesDetails/archivesDetails"})
```

访问之后页面如下

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEGRtgf2CwASC15D78Nn0uadiaHdbfFicmXgbDf7ULsAibGgXCM5sFicnWRg/640?wx_fmt=png&from=appmsg)

仅访问到了这个路由框架，此时查看bp，发现没有加载任何数据包

而当我在控制台输入如下脚本，也就是带上参数跳转到路由

```
wx.navigateTo({  url: "/pages/archivesDetails/archivesDetails?petId=1"})
```

跳转之后页面仍无数据，但路由成功被加载，触发接口请求

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEwdKs0ue40sezT7ntPhsCyNneV0HiblhoqiaC1V4yt9jNkjLtb7e1C0DA/640?wx_fmt=png&from=appmsg)

发现接口在请求petId为1的宠物信息，所以收集petId的值，拼接访问，成功越权获取其他用户的宠物信息

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fERcS1lw39ryHhUUVaAyt9XOGicpiaVLyA2DH5hWmwf22vEQdJp3u4jrZg/640?wx_fmt=png&from=appmsg)

这整个过程我想表达的点就是——路由跳转访问必须先分析需要携带的参数，而不是直接把所有的小程序路由直接拿来批量访问

那又进入到下一个问题——如何寻找路由跳转的参数？

*4*

分析路由参数

其实小程序的路由参数分析起来非常方便

每个路由通常对应三个文件：.js、.wxml、.json。其中.js文件最关键。

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEzCRGxMF8hSX6aCqS5DJEvDLh8dsFxl0O3KZ8mxpeJvT4Th9zSh3TLA/640?wx_fmt=png&from=appmsg)

以`/pages/archivesDetails/archivesDetails`为例,其对应的文件就在/pages/`archivesDetails文件下面，如下`

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEQukhtpib113JAg6nspg2alcFQWEfXOdQ3X9FV1NvnZt6g5Nm2UlWRjg/640?wx_fmt=png&from=appmsg)

打开其对应的 `archivesDetails.js`，其中不仅有该页面的完整业务逻辑，还有路由跳转所需参数，实在看不懂可以直接把整个js甩给AI，如下

![](https://mmbiz.qpic.cn/mmbiz_png/mK8kXuuyDkicCuPauHCDBnhTIgPibYS2fEoZiaXxEXBCibz8zWprY2yVW5HEDWCVSA6lxicjSW9B2dVQTXeSDTsgtLw/640?wx_fmt=png&from=appmsg)

这样就能很清晰得知道每个路由访问时需要携带的参数了，从而去构造对应的跳转链接

*5*

总结

小程序的路由测试，其实相对于Web来说，会简单很多，其内所需的各种信息，都很规范的被标明，我们可以通过反编译之后查找特定文件，来很轻松的获取完整信息。

最后，感谢各位师傅的阅读，欢迎一起交流和学习

**——The  End——**

![](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iaZREh6DtDyA9wcDsp0m1RNV9C4uiaagltPDn83s3k6Sw5DbfRWdGc25Q1WDNCpjZLXQpCxFfiaGT5ag/640)

结尾依旧打个广子混口饭，本人亲带SRC漏洞挖掘培训，欢迎感兴趣的师傅咨询，现在插班不仅可以跟着第三期一起上，还可以免费跟第四期

[![](https://mmbiz.qpic.cn/mmbiz_jpg/mK8kXuuyDkib1pd4qDUgFR6Lvndzgvuu1INOWXNHKelQ2DJN3jjiaeuAh8cfRsllJxpdq4oI6NaoxQagNpefh06A/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzg3Mzg3OTU4OQ==&mid=2247493234&idx=1&sn=78f2aa07ca247e24d83adb816efaaf01&scene=21#wechat_redirect)

[别让"入门慢"拖慢你的脚步|庆尘Src三期课程来袭——聚焦独家漏洞挖掘技巧](https://mp.weixin.qq.com/s?__biz=Mzg3Mzg3OTU4OQ==&mid=2247493234&idx=1&sn=78f2aa07ca247e24d83adb816efaaf01&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/mK8kXuuyDkibWejoF6V5RJ7wWDVjNPJNATAAgbFg6HAgJbnicSYQrxXwvagMFBfua5qyyhUa4R5okBOqGsROyHbg/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzg3Mzg3OTU4OQ==&mid=2247493357&idx=1&sn=fd9acebb0a779d6e81db05e57768fd2b&scene=21#wechat_redirect)

[庆尘 Src 9-10 月课程进度总结与后期规划 | 附赏金成果汇总](https://mp.weixin.qq.com/s?__biz=Mzg3Mzg3OTU4OQ==&mid=2247493357&idx=1&sn=fd9acebb0a779d6e81db05e57768fd2b&scene=21#wechat_redirect)

预览时标签不可点

![...