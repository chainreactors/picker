---
title: 还在用百度统计？我发现了一款更轻量、更优雅的网站分析工具：Umami
url: https://mp.weixin.qq.com/s/2nZKegGyLl8AmmxTX12EeQ
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:52:22.862658
---

# 还在用百度统计？我发现了一款更轻量、更优雅的网站分析工具：Umami

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kztGyHFwmfyLDCk1qxTtJxctoXSnibjkeB2xeicRffIeycK7wCvDJ8HD4SjG0KdeXQrgwo7VarElAJxBETbERMz6Kicr37xrgqRYJPwk1nka3k/0?wx_fmt=jpeg)

# 还在用百度统计？我发现了一款更轻量、更优雅的网站分析工具：Umami

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 1403，阅读大约需 8 分钟

如果你还在用`Google Analytics（GA）`，我建议你先停一下。

不是因为它不好，而是——它已经“太重了”。

复杂的配置、烦人的`Cookie`提示、看不懂的报表结构……很多时候你以为你在做数据分析，其实是在被工具折磨。

直到我换成了一个开源工具：

👉 Umami[1]

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyIH8TWiaMKyxqmMCr2qgYfgIuSPN40zfhC3JZsplbUHdIpianKb19TtCHnoYZRmYjE2EbNhdUq8Eh3YAq16ABTE6eO0omlfiaaW0/640?wx_fmt=png&from=appmsg "null")

我才意识到一件事：

> 原来网站统计，可以这么简单。

## 🧠 一个反常识的事实

很多人以为：

> “数据分析工具 = 功能越多越好”

但现实是：

👉 80% 的网站，只需要回答 5 个问题：

* • 今天多少访问？
* • 用户从哪来？
* • 哪些页面最热门？
* • 用户用了什么设备？
* • 有没有转化行为？

而 GA 做的事情是：

👉 给你 200 个维度 + 50 个菜单 + 一堆你永远不会点开的报表

**复杂 ≠ 专业，有时候只是负担。**

---

## ⚡ Umami 是什么？

`Umami`是一个：

> **开源 + 轻量 + 隐私优先的网站统计工具**

它的核心理念只有一句话：

> 不追踪用户，但依然看懂网站。

根据官方介绍，它的特点非常直接：

* • ❌ 不使用 Cookie
* • ❌ 不收集个人信息
* • ❌ 不跨站追踪
* • ✅ 完全 GDPR 合规
* • ✅ 可自建部署
* • ✅ 极轻量（脚本极小）

---

## 它为什么开始被越来越多人替代 GA？

我总结了 3 个原因：

### 1️⃣ 轻到离谱

Umami的统计脚本只有 **2KB 级别**

对比 GA：

👉 一个“统计工具”，却像加载了一个小应用

而 Umami 是：

> “我只做统计，不打扰你的网站”

### 2️⃣ 隐私优先（时代趋势）

现在用户越来越敏感：

* • Cookie 弹窗
* • 数据追踪提示
* • 隐私协议强制同意

而 Umami 的逻辑是：

> 不收集个人身份信息
> 不做用户跨站追踪
> 默认合规

一句话总结：

👉 **它不需要“偷窥用户”，也能完成分析**

### 3️⃣ 数据完全掌控

这是最关键的一点。

Umami 支持：

* • Docker 一键部署
* • 自己的服务器
* • 自己的数据库

也就是说：

> 你的数据，不再属于任何第三方平台

### 💡 它到底能做什么？

很多人误以为“轻量 = 功能少”，但 Umami 并不是这样。

它的能力其实已经覆盖大多数场景：

### 📊 基础统计

* • PV / UV
* • 来源网站
* • 国家 / 地区
* • 浏览器 / 设备

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfxrK9LYycd15abPVmknrCyEBFOw7BuGqMvF3hVnztncSSjIK94mmQJt8VEj5cThsy4PrGeaDJbMQe3lUZ2KibQUAoHoxVzsOzko/640?wx_fmt=png&from=appmsg "null")

### 🧭 行为分析

* • 页面访问路径
* • 停留时间
* • 跳出情况

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwLUUvftv6Q0pCVvr6dV0QLCRibiay9ED3icMPtVDAm8bvgwCJnDFZ7icib5fJxtlgibhMkyr5TvLLHCGzKpVq7Eceic7MzgtY9uKeJrU/640?wx_fmt=png&from=appmsg "null")

### 🎯 事件追踪（重点）

你可以自己定义：

* • 按钮点击
* • 表单提交
* • 下载行为

---

### ⚡ 实时数据

你可以看到：

> “现在正在访问你网站的人”

---

## 🧨最让我震撼的一点

以前我用GA的时候，总有一种感觉：

> 我在“学习工具”，而不是“看数据”

但 Umami 给我的感觉是：

> 数据就是数据，没有多余干扰

没有广告
没有复杂菜单
没有学习成本

只有一张干净的面板：

👉 该看的数据都在，不该看的都不在

## 安装部署

关于`docker`的部署方式，可以到`Umami Github`上参考部署文档，这里我以`1Panel`面板为例，不了解 `1Panel`的可以去看一下这篇文章[惊喜来袭！1panel迎来v2时代，一键升级畅享新功能](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389111&idx=1&sn=e7c7dc4f5846a2fffe9286bc3e356ad4&scene=21#wechat_redirect)

1. 1. 进入应用商店，搜索关键字：umami，点击安装：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwxpKG1VSmUnFfYpibd96fPW5uxSibvM8KIJz5icpAQ5Ot72hvnbVH7ChNRiaJAQz3U0u1HqTWk9FmVnj3IszGFElusCwP3yo7VVh8/640?wx_fmt=png&from=appmsg "null")

1. 2. 配置好信息，点击确定：

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyts5QqMXKXelcHfH8n6NzNdckVEPrMq9vjLpEp68ib4COIvLRAoibaHJKrpY4Xxkf0IQoWNPBD4iaQUbK5bkFx1qIvGTzP62caHI/640?wx_fmt=png&from=appmsg "null")

> 为了安全性，这里不建议放开外部端口，我们可以使用方向代理的方式进行域名转发。

1. 3. 进入网站-创建网站-反向代理，填入需要代理的域名和地址：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfwg8DYvR9F40LM4OZWqhks55CWU9g8cQdH3n3yp43Kc9SU0MoTGop3msVlDDR9ICEaTzic0IV77SAQHrmTpXrnloP5UyQjneyxc/640?wx_fmt=png&from=appmsg "null")

首次登录默认用户名为：`admin`，密码为：`umami`。

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfw471tbBvoX1FRibfOUsSLzB5o5uWU0r7laXc2alKoA1BWViaSL4ibf7VC7CIdm5uOHiaMPk8wyP4jyfg54cyrJeT2yrazzT8qXqek/640?wx_fmt=png&from=appmsg "null")

## Umami - 网站配置

1. 1. 登录进入后台，可以先设置一下密码、语言、时区等，Umami 支持中文：

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfxHECdKwcU5YWah49x3qJ3dmDmDwC4oC1aicdRAicqz2lqBxX4xiawsQqjjL6bp1TtNwKDNHtia95yA5MfrXLTsfckicqxokm0ib0JNk/640?wx_fmt=png&from=appmsg "null")

1. 2. 设置网站信息，点击设置-网站-添加网站：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyJzHJVc4FnFY41nxU097dfnZeDEKDaUYCpYlhT5VEibNeqoyCM1qd4Gha8LjMKQfiaG6onlxNsgG1PJRCbu8qkyGLvdlD9ibaiabE/640?wx_fmt=png&from=appmsg "null")

1. 3. 点击网站-编辑-跟踪代码，复制跟踪代码放到我们的网站上，建议放在 标签里面：

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfznIzIhQMywI42Js6u1XT3z5bTbhpq7gc8HCrmlWLmdwIwGJ7KglBP6MoKtXZctTKOSMMphO9XOZEroEQBicia6WcLeeXuMfZFgg/640?wx_fmt=png&from=appmsg "null")

1. 4. 访问我们的站点，随便点击几下，回到仪表盘就能看到统计数据拉。

## 效果预览

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyvLWJeEWwyTgXK5cFAFXICK9CHqyJhEVlCtN8oloNiccEvKQtVAXRxXO4VrdmH9HqWRJlSWCghj1yIB25GGmiccn43rL7APHADc/640?wx_fmt=png&from=appmsg "null")

![图片](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfw9dhYzWjj3oJWvNOicRg7QBBaFAAdMo6DvJ82BkKVZr2xlEzvlCDCgTukGSCQ3pBPLI1aY60pnf9YJMBlQusmra7Nk9Lm3OzIk/640?wx_fmt=png&from=appmsg "null")

## 🧠 一个值得思考的问题

工具越来越强之后，我们反而越来越累。

我们到底需要的是：

> 更复杂的数据？
> 还是更清晰的判断？

`Umami`给出的答案很直接：

> **够用，比强大更重要**

## 🚀 总结

最后总结一句我很喜欢的话：

> “好的工具，不是让你看到更多数据，而是让你更快做出判断。”

`Umami`不一定是最强的分析工具，但它可能是：

👉 最适合“现代独立开发者 / 博客 / 小团队”的那个答案

---

推荐阅读

* • [FastAPI后台还在手写？这个开源神器直接帮你“自动生成整个管理系统”](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389782&idx=1&sn=f793dff4ae306bc3ef1566394fbd31da&scene=21#wechat_redirect)
* • [开源 | 告别重复对接，这款消息推送平台全渠道搞定](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389495&idx=1&sn=1baddfa3e060889745d0145270218c18&scene=21#wechat_redirect)
* • [Linux 高危漏洞爆发！普通用户可直接提权 root](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389895&idx=1&sn=338b9fba5bfa9cbda05520d2b42c626c&scene=21#wechat_redirect)

---

#### 引用链接

`[1]` Umami: *https://github.com/umami-software/umami*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

攻城狮成长日记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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