---
title: 小技巧 | 企业微信H5开启webview调试
url: https://mp.weixin.qq.com/s/4QIPYE193Bl0ZdZqpvcAIw
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:11.844749
---

# 小技巧 | 企业微信H5开启webview调试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnpJmzsEG5B9jUAC2aCxjiaafiaGln6Kpz3SYSodxcibDR0ydL3loCSHyGk9UNnWAznicbAQibGOZrMk6skxrMdTzgfhvFN8dI5cn4Y/0?wx_fmt=jpeg)

# 小技巧 | 企业微信H5开启webview调试

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 613，阅读大约需 4 分钟

## 前言

2025 年的时候，写过一篇**企业微信开启 webview 调试**的文章，最近项目中遇到企业微信的 H5 应用的情况。

发现 `https://debugx5.qq.com/?inspector=true` 503 了。

在网上重新找了资料，更新文章。

## 介绍

安卓端的企业微信的应用是 H5 页面，通过内置浏览器运行的。我们可以开启 webview 调试实现。正常的 APP 内置 webview 的话，可以用 Xposed 插件或者 Frida 脚本调试。

不过，我这里用 Frida 通用脚本没什么效果。当然，也不用这么麻烦，企业微信为了便于开发者调试，也提供了开启调试的方法。

因为企业微信有水印，就不放截图了。造作比较简单，结合给出的引用链接，就能办到。

## Android 端

在 Android 的企业微信启动 webview 调试
在企业微信的内置浏览器中访问 http://debugxweb.qq.com/?inspector=true
如果企业微信中找不到输入链接的地方，那可以使用`扫一扫`功能扫描二维码

比如，在草料 https://cli.im/text ，在线生成一个二维码

新的
![3ca5088934b9b9d3de311be2948bda69.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVletJKJjwAj7pFvje7TI4yPtJ7lzAVnO962dUo3wEKyyy46eib3VjTDzhJic1lYdicVybhxg33Qkewm5BU0EgicQDQKq2T7JZWuVY8/640?from=appmsg "null")

3ca5088934b9b9d3de311be2948bda69.png

随后，手机通过数据项和电脑连接

> 确保手机已经开启开发者模式，并且允许 adb usb 调试

谷歌浏览器访问

```
chrome://inspect/#devices
```

企业微信打开要调试的应用，等待一段时间，等浏览器中出现下图的信息，点击 inspect 即可调试

![ff219eb252ad5c7e465413332b74b210.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkFT09KbRrFyGw8IE0A0WsQXyH6ELDN4JSZ4EfKGMFEZM7iaaZ4EqkHGzc0frubApnANJUkRic3fxo6pibp6KwtYHwGHJgFnm0P3M/640?from=appmsg "null")

ff219eb252ad5c7e465413332b74b210.png

如果 inspect 404 就尝试用 inspect fallback
![e2df8f09f8af41457b658d772b932df5.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkzOqvl2ySbiauVyWofbPPyJTonyg066FuqkAAHv4LL0S7Lt4cyk1ZJ9EIVgJT0MfFheyfvTGEbeOZLKraAO4NfibAJh8j6VZ4CQ/640?from=appmsg "null")

e2df8f09f8af41457b658d772b932df5.png

点击`inspect`时 Chrome 会请求谷歌海外服务器 `chrome-devtools-frontend.appspot.com` 下载对应版本调试面板资源，国内网络无法访问直接返回 404

**解决办法 1**
使用 edge

```
edge://inspect/#devices
```

![6af74ba1d90a62c04a04901b4b891196.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmibYLKiavm0gsxNIiaLTVCf4AHlBLfurI8mPEwZ9aJKWficqsibxDXmG5nFg76Rj36fUOoVZSJREzDN9NmZypGKu96Zku2yWYzqaicY/640?from=appmsg "null")

6af74ba1d90a62c04a04901b4b891196.png

## 小技巧

chrome 或者 edge 当中如何复制请求包

复制，复制为 curl bash
![55251bd17b10898d62218516064df6fd.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkWWysMJsnicJGRHEovkF5LHDtYBB2UofjSDEkVVMVua6ibt2PFzuG31WeUFCnDicczsLm28lSeZwNERrKaGUjnNVEoxMAwx8dM2s/640?from=appmsg "null")

55251bd17b10898d62218516064df6fd.png

在 yakit 的 webfuzzer 当中
![4915593f9993c6d92b0b22c7f8b1b8e5.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnPBX1Q2iaWKoSWZTHNyjIlHh8hhomubjXz9QcYKa5Iicld79jnlazNZnibNfzqdVksEh5vWTk5gm01xnibnXicvMDygK5mtibOMKg0c/640?from=appmsg "null")

4915593f9993c6d92b0b22c7f8b1b8e5.png

就能自动构建完整的请求包了。

如果 H5 页面是 vue 写的可以直接把 URL 拿出来放浏览器里把 Cookie 什么的配置好就能正常用 AntiDebug\_Breaker 了，chrome mcp 什么的也可以直接用

## 其他端

`Win PC端`、`Mac PC端`、`ios端`可以参考：
https://developer.work.weixin.qq.com/community/article/detail?content\_id=16423267377683446505

## 微信开启 webview

微信 Android 端也可以在不 root 的情况下开启 webview
可以参考：小程序逆向之 webview 动态调试 [https://mp.weixin.qq.com/s/9vKWDZ6GFEXDnjCPEj2DlA](https://mp.weixin.qq.com/s?__biz=MzkyNjY3OTI4Ng==&mid=2247484847&idx=1&sn=11b8870f7f0404380d25c17f44ec5b6b&scene=21#wechat_redirect)

但是，我在用手机测试的时候，小程序会出现

## 参考资料

* • https://developer.work.weixin.qq.com/community/question/detail?content\_id=16470394666431078449
* • 企微应用 H5 调试及 vConsole https://developer.work.weixin.qq.com/community/article/detail?content\_id=16423267377683446505

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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