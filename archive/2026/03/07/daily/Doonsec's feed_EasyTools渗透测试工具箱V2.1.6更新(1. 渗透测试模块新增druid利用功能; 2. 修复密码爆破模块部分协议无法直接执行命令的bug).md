---
title: EasyTools渗透测试工具箱V2.1.6更新(1. 渗透测试模块新增druid利用功能; 2. 修复密码爆破模块部分协议无法直接执行命令的bug)
url: https://mp.weixin.qq.com/s/WNsMCQdCf5mp3HO-5qT0Zg
source: Doonsec's feed
date: 2026-03-07
fetch_date: 2026-03-08T04:03:54.094894
---

# EasyTools渗透测试工具箱V2.1.6更新(1. 渗透测试模块新增druid利用功能; 2. 修复密码爆破模块部分协议无法直接执行命令的bug)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfO0XCNPrNolHDq2cB4dq6fzfGoQCcwIuf6Do47wgjyfVxJZjNIPm8IEjbWsGC6hib8u4WicD2k6fXazibU8lnbRthib6ibHKRU9WKVhZ1rMLl7M/0?wx_fmt=jpeg)

# EasyTools渗透测试工具箱V2.1.6更新(1. 渗透测试模块新增druid利用功能; 2. 修复密码爆破模块部分协议无法直接执行命令的bug)

沐寒
沐寒

渗透云记

![]()

在小说阅读器中沉浸阅读

**免责声明**

由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJZJ4pVQHOicqtkQntqLduTfPaVvVnZ4iaGc0DaBeQqNoicYUrzzyOpIsJWbSgNUqV3SodRwKFOIq3Lw/640?wx_fmt=png&from=appmsg)

欢迎关注本公众号，长期推送技术文章

## 前言

开工第一更，在此汇报一下更新进度：

1. 渗透测试模块新增druid利用功能，自动提取并支持一键发送到便携发包模块进行测试;
2. 修复密码爆破模块部分协议无法直接执行命令的bug

## 新增功能

#### 1. 渗透测试模块新增druid利用功能

以往找到druid未授权或者弱口令之后，需要手动打开复制session或url进行单个测试，现在支持一键批量将存在的session或url发送到便携发包模块进行测试，大致效果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNqVC16s34icnlheoqa68O15t34icQrpiaqZESHicgicoXCViaOVJ3DdOxdLC0bicHsP4sFpYjOe9LDNa1NNWxCd7jXDpq27N335BdXkI4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNribu099tMVGOdydFLMu7FicibibIb7HVln0MG7DHWINXiaRB57DI3g8Qde3iahcypOvbv9JbVHbYaYAMFFBViaVoqA8bcpSdpb3dHofc/640?wx_fmt=png&from=appmsg)

支持单个session进行发包，也支持批量批量session进行发送，需要咱们先手动配置一下baseurl，然后点击批量测试即可，配合burpsuite或者yakit更香哦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNoB8C59uDp0rb1rpMtx9XiaJl9yeksyKiaWrICVu729uDJg0hZrZTRJNQfAicUj2tcAXticaibUNKqFiabUbuk9AynONvBtUGCsUlSX4/640?wx_fmt=png&from=appmsg)

#### 2. 优化密码爆破模块

密码爆破模块现在支持简练助手中存在的一键发送过去进行连接（早已实现），
支持zookeeper等协议的右键执行命令（最新实现），效果如下：

这些功能离线均可使用，无需登录，请放心食用

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNo444Q8sO1icxQIwyOX4rXHl4SlsEkIcxr6RjMIxhfF4rwsPvtAxYYicttLGX2gicHQcO8tZ8asdUAyjwwKnINVMiaNDTeVOtInxK4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpT8Qic3h6Oicwb2cunASdzSnfnvjg5eBhY4G6eelptZcQibeeA4iaC0fTqNrz3kfhFaibQOhja0k6RY7OKC3rhiaicWc1LzWSRicYx3Ec/640?wx_fmt=png&from=appmsg)

## 功能完善

空间测绘平台，支持第三方fofa接口的自定义配置，效果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNqdLt0aV11xdAKMXp262uNu2eQJdvaI2ZIsLhiaETZbdjAADyIeoJhVqMk3yE7icicHfyQc7XfLff8WQEVXY8BYFP2jMjInaiafGpw/640?wx_fmt=png&from=appmsg)

## 下载地址

公众号回复：EasyTools

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLbE8HiaQapVkBwypwXhsmWWEwZyOx2Frhw9bDjyRnVSMtubJkZJY9NX2Hw8Igx7fDmuZnYXzPUvDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK0JBUq0N1g9hpXvZiaWm32V2kibRficfdehadlNxb8ibickibcgHFOr9FXF5qibRy3pDw984iaZP8InvejUQ/640?wx_fmt=png&from=appmsg)

往期精彩：

[今日时事，一个快捷全面的信息流获取平台，告别信息焦虑，让你一眼看尽天下事](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484750&idx=1&sn=87d33a3442b6fc12fe10f48443efacda&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.1.4更新(优化资源桶遍历功能，支持kkfileview预览，新增空间测绘、AI版域名收集功能等诸多功能)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484743&idx=1&sn=6a427ce97be0e6c2ee8e803edb82ee14&scene=21#wechat_redirect)

[【工具分享】Webshell\_Generate v2.0 ai自动生成webshell，现已支持docker自动部署测试环境并上传阿里云进行查杀](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484728&idx=1&sn=1a3f0494ea2d8f85f1d0f32e8e53a8e6&scene=21#wechat_redirect)

[【工具分享】Webshell\_Generate v1.0 一款简单的ai自动Webshell生成小工具](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484721&idx=1&sn=58adda6510127bf2c47f887a683afb0a&scene=21#wechat_redirect)

---

鄙人的一个小博客 渗透云记，

官网地址：www.encenc.com

博客地址：b.encenc.com

目前已集成EasyTools渗透测试工具箱的登录，Webshell\_Agent AI自动生成平台的登录等，一个账号，多平台联动使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK5R6NYcibf6ADO4U7BvUHupNyYDu3RwMYRL9ickjZNUMoHeGcAS7fgF2zcyWaODWcOuqjqkeAibjkPQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

渗透云记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

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