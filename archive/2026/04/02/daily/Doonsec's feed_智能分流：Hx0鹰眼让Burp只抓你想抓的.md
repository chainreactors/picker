---
title: 智能分流：Hx0鹰眼让Burp只抓你想抓的
url: https://mp.weixin.qq.com/s/P3TrGKCsLt_optRbtIwEUg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:22:49.246528
---

# 智能分流：Hx0鹰眼让Burp只抓你想抓的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PUTQGRQ4GOicnqsKbicHVe3kHwQQyQbelFXCLE18IKJ5Omfc7tN3SDIoPI2XeWSzXgjM1TWMSNgPpClwQyavuIDIfLq4uEhn8fT4E17KEfoA8/0?wx_fmt=jpeg)

# 智能分流：Hx0鹰眼让Burp只抓你想抓的

Hx0战队

![]()

在小说阅读器中沉浸阅读

编者荐语：

以前开Burp测试，刷个B站都卡成狗。现在用智能分流器，测试流量走代理，摸鱼流量直连，互不干扰。

以下文章来源于Hx0极客圈
，作者asaotomo

![](http://wx.qlogo.cn/mmhead/rqvn1hjHytedfdS681PB4EroprjS2nmYaD5EibbpYicfwoZVQiaiavVZEBTaybhia7ZibDxjt0LMcWS8s/0)

**Hx0极客圈**
.

我们致力于将 AI 赋能于安全，用极客精神重塑工具。

# 场景：一边刷B站，一边测系统

> 你正在测试客户的系统，Burp开着，代理设好了。这时候你想摸鱼刷个B站放松一下——
>
> **问题来了**：B站的流量也全跑Burp里了，视频卡得要命，还把一堆无关请求记进去了。
>
> 你只能：要么关掉代理（测试中断），要么忍受B站卡顿（摸鱼不爽）。
>
> **要是能只让客户系统的流量走Burp，B站正常直连就好了...**

这就是智能代理分流器解决的问题：**测试流量走Burp，摸鱼流量直连，互不干扰。**

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOibib8FFJnpq2QveVQv0icuk8GQSM1VsNAxkuaGhPPOibw2IpNZ0sSPoN5UeEoKia8Mj1Or3bibtqmGLQhdqOMADyOWKEQNl9Qchm51k/640?wx_fmt=png&from=appmsg)

## 传统做法的痛点

以前开Burp测试时，所有流量都被代理：

* 访问测试系统 → 走Burp ✅ 正常
* 刷B站 → 走Burp ❌ 卡顿
* 查文档 → 走Burp ❌ 慢
* 开会用的OA系统 → 走Burp ❌ 可能还打不开

**开代理影响其他网站，关代理又影响测试，左右为难。**

## 解决方案：智能代理分流器

把它想象成门口的"智能调度员"：

```
你要访问 target.com → 走Burp，被记录分析
你要访问 baidu.com → 直接连接，正常访问
你要访问 bilibili.com → 直接连接，正常访问
```

**只代理你指定的网站，其他照常访问。**

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GOicxS7X5lK7fNhiazgvYpLw3LSujmTg0MgeLGBg3PkJ9iaVkw6DSNJbqbjZ2IMHFLKBSUusUuib7N3Q09Dfnj2UMkjD9gzgwtX5nhI/640?wx_fmt=png&from=appmsg)

## 效果对比

### 没有分流器

| 访问的网站 | 流量走向 | 速度 |
| --- | --- | --- |
| target.com | Burp → 目标服务器 | 正常 |
| baidu.com | Burp → 百度服务器 | 慢 😓 |
| github.com | Burp → GitHub服务器 | 慢 😓 |
| bilibili.com | Burp → B站服务器 | 慢 😓 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOicV3cLMOiabzbBl9Xtp5Iu0TfVR6U9n6sVOLtILmjPibRia0YZia1h0nxZTK2LjiaLdwQENYBdxQ5LF2wGaAv86xN2SiamS6jFvYhCH0/640?wx_fmt=png&from=appmsg)

### 有分流器

| 访问的网站 | 流量走向 | 速度 |
| --- | --- | --- |
| target.com | Burp → 目标服务器 | 正常 ✅ |
| baidu.com | 直接 → 百度服务器 | 快 ✅ |
| github.com | 直接 → GitHub服务器 | 快 ✅ |
| bilibili.com | 直接 → B站服务器 | 快 ✅ |

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOicQliakjBqicKNUIac1qW2RublmEich7lpYyHIogtEuE4CZKJsugic5PEF0QaHahS43oBF7PFYKN2aGwFiaemmaAh3TCMs5cib54hyRY/640?wx_fmt=png&from=appmsg)使用方法

### 第一步：开启功能

在扩展里打开"智能代理分流器"开关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GOict3RyPDdLAx5eE0XY7hZuuybjjJUHJOjoIYHnicXwsDoCHnRw95tZndWDoqa7Rlm75xggqBlC6uznfHX3eAxjTQSalaXibWY4Ao/640?wx_fmt=png&from=appmsg)

### 第二步：配置代理地址（无需开启FoxyProxy或Proxy SwitchyOmega）

填写Burp或Yakit的地址： - Burp默认：`127.0.0.1:8080` - Yakit默认：`127.0.0.1:8083`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUTQGRQ4GO9jssMib7ffcXibEDGbRVlib8acOklqEtTE8se4pHlmGWTcU1K761J5cI1QiaXvEVJstL2GZ4PXvmRFRERg34557fId49BvjicPujG8/640?wx_fmt=png&from=appmsg)

### 第三步：添加目标域名

一行一个，支持通配符： `target.com *.test.example.com`

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9YX8okGyXdebDLFaictJxA6BDnus5W4eyic227lPniaOEaLsq0PYlFjOozACKV68QCxI9CxPdcZopcIsgufEozz0KXGlXHoe19hs/640?wx_fmt=png&from=appmsg)

### 第四步：开始测试

访问目标网站（buuoj.cn） → 流量自动进Burp（Burp HTTP history 流量干净明了，没有baidu.com、qq.com、bilibili.com）

访问其他网站 → 一切正常（bilibili.com直播正常、百度、腾讯网页正常使用）

![](https://mmbiz.qpic.cn/mmbiz_png/PUTQGRQ4GO9WlX7GPk5nsLl9oicJtMWv4l2PlnUVYJsZmnVPdcjNKv9BKfWHn8JYic73yPWSgMHIZzE4GAiaEKXrbVCfmc5x6uCVrwoH7yFXHQ/640?wx_fmt=png&from=appmsg)

## 和其他方案对比

| 方案 | 只代理目标站 | 用自己浏览器 | 配合任意工具 | 安全测试友好 |
| --- | --- | --- | --- | --- |
| 系统代理 | ❌ 全部代理 | ✅ | ✅ | ❌ |
| Burp内置浏览器 | ❌ | ❌ | ❌ 只能Burp | ✅ |
| Proxy SwitchyOmega | ✅ | ✅ | ✅ 配置复杂 | ❌ |
| FoxyProxy | ✅ | ✅ | ✅ 配置复杂 | ❌ |
| **Hx0鹰眼智能分流器** | ✅ | ✅ | ✅ 简单易用 | ✅ |

### 各方案简评

**系统代理**：一刀切，所有流量都走代理，不够灵活。

**Burp内置浏览器**：功能强，但必须启动Burp，不能用自己习惯的浏览器和插件。

**SwitchyOmega**：功能强大，但配置项多，学习成本高，不是为安全测试设计的。

**FoxyProxy**：老牌代理扩展，支持规则切换，但界面传统，配置流程繁琐，同样不是安全测试专用工具。

**智能分流器**：专为安全测试设计，开箱即用，自动适配Burp/Yakit。

## 常见问题

**Q：为什么HTTPS网站会提示证书错误？**

A：这是正常的。所有代理工具拦截HTTPS都需要你信任它的证书，在Burp里导出CA证书，导入浏览器即可。

**Q：规则怎么写？**

A： - `example.com` — 精确匹配 - `*.example.com` — 匹配所有子域名 - `*` — 全部流量都走代理

## 一个真实的场景

### 以前的一天

**上午 9:00** — 打开Burp，设置代理，开始测试。一切正常。

**中午 12:00** — 想摸鱼刷个B站，结果视频加载超慢。算了，忍一忍。

**下午 3:00** — 同事让帮忙看个内网系统，结果开了代理根本访问不了。只好关掉代理，看完再重新开。

**下午 5:00** — 测试完成，收拾东西下班。**忘记关代理。**

**第二天上班** — 发现Burp还在后台跑着，昨天晚上所有浏览记录全被记录了...包括搜索记录、登录账号、看的视频 😱

### 现在的一天

**上午 9:00** — 打开分流器，添加规则 `target.com`，开启。测试系统流量自动进Burp。

**中午 12:00** — 刷B站，视频流畅。**分流器自动识别这不是目标站点，直连。**

**下午 3:00** — 帮同事看内网系统，正常访问。**不需要关代理。**

**下午 5:00** — 关掉分流器开关，一切恢复。**没有残留，没有担忧**

## 总结

**一句话介绍**：只让目标站点的流量走Burp/Yakit，其他网站照常访问。

**适合谁**：Web安全测试人员、渗透测试工程师、需要调试HTTP的开发者。

**有什么好处**：不用反复切代理，不用忍受其他网站变慢，不用担心忘记关代理。

**对比总结**：

| 场景 | 以前 | 现在 |
| --- | --- | --- |
| 测试目标站点 | 正常 ✅ | 正常 ✅ |
| 摸鱼刷B站 | 卡顿 😓 | 流畅 ✅ |
| 访问内网系统 | 要关代理 | 正常访问 ✅ |
| 下班忘记关 | 隐私泄露 😱 | 无所谓 ✅ |

Hx0鹰眼轻量级浏览器抓包扩展 *GitHub：https://github.com/asaotomo/Hx0-HawkEye*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OC2Q345raO6FzicO8iasjtiavo2jy3hVzbIr7nVhQthvcpzut0ogYTqUOvZQj0ncoVCJoQ2HicXlmrYoJHDXW9uYjQ/0?wx_fmt=png)

Hx0战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OC2Q345raO6FzicO8iasjtiavo2jy3hVzbIr7nVhQthvcpzut0ogYTqUOvZQj0ncoVCJoQ2HicXlmrYoJHDXW9uYjQ/0?wx_fmt=png)

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