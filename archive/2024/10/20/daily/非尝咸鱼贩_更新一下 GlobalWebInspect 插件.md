---
title: 更新一下 GlobalWebInspect 插件
url: https://mp.weixin.qq.com/s?__biz=Mzk0NDE3MTkzNQ==&mid=2247485483&idx=1&sn=df8749574a7929dac0ca4811f614d343&chksm=c329f6dbf45e7fcd52d7f12a6c0dc0e8881e2c80b5bde816fc76cf1a70c5d572a650ea054d7b&scene=58&subscene=0#rd
source: 非尝咸鱼贩
date: 2024-10-20
fetch_date: 2025-10-06T18:50:39.507157
---

# 更新一下 GlobalWebInspect 插件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6N4b2yN3FOJYk7aNpLYRODkT4n1XdodWuFcjZ1GhaMVfcUqCYQ1TSbZyc54SMvGGOpzXpXo4eSYGXA6ALbUnUA/0?wx_fmt=jpeg)

# 更新一下 GlobalWebInspect 插件

原创

0xcc

非尝咸鱼贩

写了一个可以全局开启 app 的 WebView 和 JavaScriptCore 调试的工具

https://github.com/chichou/globalwebinspect

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJYk7aNpLYRODkT4n1XdodWXDF1IKdIEqKcvibeoPaJCLsS5PTR2HeDXyN0Rw77bke85ZrtQEldJnw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJYk7aNpLYRODkT4n1XdodWOrSibiaicsDNA04jibz6GViapWVKIkAuWVrttO0usE7lJ9qSfwqxKib1oibZA/640?wx_fmt=png&from=appmsg)

iOS 版 Bing 应用，一看这个变量名，应该就是 fork 的 Chromium

Safari 16.4 之后调试的机制更新了，这个插件一直没跟上。本来只要注入 webinspectord 一个进程就够，现在要全局拦截所有链接了 JavaScriptCore 的 App 进程。

新版本的原理是 hook JSGlobalContextCreateInGroup 函数，然后调用 JSGlobalContextSetInspectable。Objective C 的 JSContext 系列 API 最终也会走到这个 C 函数。

而 WKWebView 的处理则是在 \_initializeWithConfiguration:（私有）方法执行完之后调用一次 setInspectable:。

另外这个版本也支持 rootless 环境了。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJePjhDUn7xMMlhZWpLjDwu3WUia32nGS0LiaB64WpyniauGgN9ibRaG1okaRpxswTPwaEgqTlic3aRJrQ/0?wx_fmt=png)

非尝咸鱼贩

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6N4b2yN3FOJePjhDUn7xMMlhZWpLjDwu3WUia32nGS0LiaB64WpyniauGgN9ibRaG1okaRpxswTPwaEgqTlic3aRJrQ/0?wx_fmt=png)

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