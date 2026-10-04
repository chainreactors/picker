---
title: Streamlink：一次重定向，为什么能读到本地文件
url: https://mp.weixin.qq.com/s/J4aEi0dDpFUYwCd9kmodkQ
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:35:54.036624
---

# Streamlink：一次重定向，为什么能读到本地文件

# Streamlink：一次重定向，为什么能读到本地文件

原创

云梦DC
云梦DC

云梦安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026 年 9 月 24 日，Streamlink 披露 GHSA-vf2x-4v53-pm7v（CVE-2026-92164，中危）：HTTPSession 在跟随 HTTP 重定向时没有校验目标 URL 的协议，可以被跳到 file://，把本地文件当响应体读出来。Streamlink 是流媒体下载与播放工具，常被部署在下载器、媒体服务器和自动化脚本里——这些机器上通常有媒体库路径、CDN 签名密钥和云存储凭据。

这类问题的形态在基础设施中非常常见：协议白名单只校验了初始 URL，没有校验每一跳。

![](https://mmbiz.qpic.cn/mmbiz_png/Ft77EUEUqosFHThyqmkKxCvZ2aqzpEY9uQlXKIdcU8ByFWGHkjCYObY4otogITWTEffah1MK4a0vVia09hwuWtWnDCicVgJKnnEFDfQrmNZm0/640?wx_fmt=png&from=appmsg)

## 实验：本机起一个恶意源站

隔离环境里写了一个最小的恶意源站 evilsrv.py，监听 127.0.0.1:8099。它只有一个路由 /playlist.m3u8，对任何请求都回 302，Location 指向 file:///…/\_lab/07\_streamlink/secret.txt。目标文件里放了三行模拟凭据：CLOUD\_STREAM\_TOKEN=sl-live-…、CDN\_SIGNING\_KEY=…。

在 Streamlink 8.5.0 上发起请求：初始 URL 是合法的 http://127.0.0.1:8099/playlist.m3u8，但脚本打印的“最终 URL”已经变成 file:// 开头；unquote 解码后可以看到完整的本地路径；HTTP 状态码 200，Content-Type 为 None，响应正文就是那三行凭据原文。脚本最后的判定行写着“远程重定向成功读取本地文件，敏感内容随响应体返回”。

这条链路里没有任何复杂技巧：HTTP 客户端自己跟随了重定向，而 file:// 由本地的 urllib 处理器负责打开，于是“取一个远程播放列表”就变成了“读一个本地文件”。

## 8.6.0 的修复：把校验放在跟随之前

升级到 8.6.0 后，同一个请求直接失败：PluginError: Unable to open URL: … (Disallowed redirection to file:// URL from http://127.0.0.1:8099/playlist.m3u8)。异常信息把来源 URL 和被拒的目标协议都写清楚了，便于排查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ft77EUEUqovZxWE8d3dicX4D5aY5icCj5m33UaetlIJeMSdsrN2C1sJPiaoJU3ibicx9OoZYtnp5TVHRcFq5v1Wlumt4uwKCHicnQfG1icpXbwyeibg/640?wx_fmt=png&from=appmsg)

值得留意的是修复的位置：它发生在 HTTPSession 的重定向前置检查里，而不是在某个插件内部做条件判断。这个位置选择是对的——所有插件、所有调用路径都共用这一个会话对象，校验放对了地方，就不需要每个功能各自实现一遍，也不会漏掉其中一个。

## 把它当成 SSRF 来治

只要是“用户或第三方给出的 URL，由服务端去取”的功能，都应该按服务端请求伪造来对待。落到实现上至少有五条：协议白名单必须在每一跳校验，只允许 http/https，显式禁止 file、gopher、dict 等；重定向次数设上限，并记录每一次跳转的目标；解析域名后校验实际 IP，拦截回环、私网网段与云元数据地址（169.254.169.254）；不需要出网的功能直接把出口关掉，而不是只在代码里做判断；对下载目录与媒体库挂载路径做权限收敛，不要给运行用户整盘可读。

Streamlink 这类工具往往以有媒体库和对象存储凭据的账号运行，读到的不只是“一个文件”。所以复测时建议顺手做一次“进程可读文件”的核查，而不只是验证漏洞请求被拒绝。

## 复测清单

升级后确认三件事：恶意源站的 file:// 重定向被拒绝；正常的 http → https 重定向仍能跟随，别把订阅源和 CDN 跳转一起挡掉；被读过的敏感凭据已经轮换，尤其是实验里出现过的流媒体 Token 与签名密钥。

## 同一类问题在别处的样子

“跟随重定向时忘了重新校验”不是 Streamlink 独有的实现细节，而是一类非常常见的失误：只在入口处做一次 URL 校验，之后就交给底层 HTTP 客户端自己处理跳转。凡是把协议、主机或路径白名单写在校验函数里的代码，都要回头确认这个校验在每一跳都执行了一遍——包括 301、302、303、307、308 这些不同的状态码，以及跨协议的跳转。

排查时有个捷径：搜代码里 allow\_redirects、follow\_redirects、max\_redirects 这类开关，以及自己实现的跳转循环。每一个打开重定向的地方，都应该紧邻一段“校验目标 URL”的逻辑；如果只有入口处有校验，那里就是同类问题的候选点。

## 一句话总结

“我只允许 http 和 https”这句话，只有在每一次跳转后都再说一遍，才算数。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ndxZsFvkmpznJ7eICiaSkulHmla8V8RPVeTQ5z2uI5iaV9FniaMzXYbodGk9qNSBY6ccvbiaW5XxvKJNp7zLicxwSEQ/0?wx_fmt=png)

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