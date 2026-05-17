---
title: 如何让自己的博客爆闪别人
url: https://mp.weixin.qq.com/s/CwLNyXWNTM1ccSq0QBURgg
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:16.615656
---

# 如何让自己的博客爆闪别人

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ULOszTo2RiaDpFBz6rr8vpQmEibp7NKibHiaIHe64LJYnWLwibDyIkHdpjMqs5uI5GiacJam3XRolHI2tCX41kfAdiaPiaxgBVtGJA2MArIgQ8s7cF0/0?wx_fmt=jpeg)

# 如何让自己的博客爆闪别人

IceCliffs
IceCliffs

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如何让自己的博客闪爆别人

熟悉我博客的朋友应该知道，我博客接入了很多有意思的小功能，无限 Debugger、JS 反编译、部分代码混淆、多用户鼠标跟踪、CTF 题目、数据埋点、**开屏爆闪**

今天要来说的就是 **开屏爆闪** 这个小功能，本质上是利用了显示屏的 HDR 功能，如果你不知道这是什么，下面这张图闪到你了说明你的设备支持 HDR 显示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCaicbxcotZIL7BmGSibswlQNhGMeylmqDqUzIMwlFTrgMJsID97yPibYoicFh0A1KIuycEzR86icflBeyELwKKWuCiaYfA1gexskQcU/640?wx_fmt=png&from=appmsg "null")

如果你用带有 HDR 功能的显示屏访问我的博客，那效果会是这样子的

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ULOszTo2RiaDw9h7FMGlkshiaBsBjibrGyaLJRxCpiafwPO9lGXB8ydZS1hRzzibWibjEmBYcDcK3w8QmCet1KzqibCozbGia6JRgoh5ge1PXrG8wmE/640?wx_fmt=gif&from=appmsg "null")

这么看效果不是很明显，但如果我们关上灯，再来看看效果

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/ULOszTo2RiaBm8s7ZXVIXicUwVZ6D8JOz1iaDWNJZyBzNjyj1vPLqg9iaKTdulxyCtqnslLTbakUa01wT7BcHb3QpYPWESBU5RqVIqlyjJMDtAo/640?wx_fmt=gif&from=appmsg "null")

看着应该明显多了，具体还是得实际体验才知道，在开始之前我们先知道一下 HDR 的具体工作原理

在传统的 **显示技术（SDR，标准动态范围）** 中，亮度是有天花板的，普通的 SDR 显示器，亮度标准通常在 100-300 nits（尼特），在代码的世界里，白色就是 `rgb(255, 255, 255)`，整前端的应该对 `#000000` 非常熟悉，在 SDR 模式下，系统会告诉显示器，请把这个像素点开到你目前允许的最大亮度，所以无论你屏幕本身多亮，SDR 内容的白色永远只是那个标准亮度的峰值，它无法突破

但是 HDR 可不一样了，HDR 技术打破了这个限制，它不仅增加了色彩深度（比如从 8bit 升到 10bit），最核心的变化是亮度的绝对值控制，**HDR 显示器** （尤其是高规格的，如 HDR 1000）峰值亮度可以达到 1000 nits 甚至更高，在 HDR 模式下，视频或图像文件包含了一组元数据（Metadata），它告诉显示器，这一块像素，我要它达到 1000 尼特的绝对光强！

比如笔者这台 MacBook 最高峰值可以达到 `1,600 nits`，在做到伤害别人的眼睛的同时也伤害了自己的眼睛，属于是杀敌一千自损八百

那么接下来来说说这么实现吧，实际上很简单，无非就两种，第一种你可以直接在 CSS 全局样式的背景里塞入一张 HDR 图片，这是最快的做法，参考代码如下

```
body {
margin: 0;
min-height: 100vh;
background-color: #fff;
color: #000;
font-weight: 400;
font-size: 15.5px;
font-family: 'Noto Sans SC', sans-serif;
line-height: 1.625;
text-rendering: geometricPrecision;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
background-image: url("data:image/avif;base64,AAAAIGZ0eXBhdmlmAAAAAGF2aWZtaWYxbWlhZk1BMUIAAADybWV0YQAAAAAAAAAoaGRscgAAAAAAAAAAcGljdAAAAAAAAAAAAAAAAGxpYmF2aWYAAAAADnBpdG0AAAAAAAEAAAAeaWxvYwAAAABEAAABAAEAAAABAAABGgAAACQAAAAoaWluZgAAAAAAAQAAABppbmZlAgAAAAABAABhdjAxQ29sb3IAAAAAamlwcnAAAABLaXBjbwAAABRpc3BlAAAAAAAAAIAAAACAAAAAEHBpeGkAAAAAAwoKCgAAAAxhdjFDgQBMAAAAABNjb2xybmNseAAJABAACQAAAAAXaXBtYQAAAAAAAAABAAEEAQKDBAAAACxtZGF0EgAKCRgZv/9ihIgEgjIVEZACSSSRALSDWh0OcWLT/Laowj+g");
}
```

这种效果基本上可以把别人的眼睛闪瞎

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCAx2VOxYj7YsVZxn6iaduqAhz1CN42lU8vibvw6j0st5FiaiaVH8NSuFaBmAmXEGQjOCBkh5a58tqOqicRjfmg3Al8HSmwicbO8ruK8/640?wx_fmt=png&from=appmsg "null")

第二种就是通过带有 hdr 的视频，同样通过 html 标签或者别的姿势内嵌进去，也可以爆闪别人，但这个不是很推荐做，对于患有光敏性疾病的读者，这种高频强光切换是真的会诱发疾病的，例如我之前就用过 `setInterval` 来延迟闪别人，具体效果就是别人访问我网站 1-4s 后，在他们阅读文章时突然闪一下，后面把自己闪成傻X了就没再用了

## 受害者展示

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCdsYW111ZonYqeJ7ahFOLM7wtoRm8skz1pzFVqBvrrrmReGhnbIRzVxEWlpO1BibzQq2btG80jKOHwjneV1txQOpjia8XBTO3ys/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCDjQuBTUzJ7dzs4YMjfXlliaenjm6ylYjZxHw5KbYgZTglcv5icEL7aLu7Ey9DoIscN6RLCTQJfMxtwgAkL9cOibZXElmKpYVyRU/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaBWJqkBdUS0BUiaWDe6Q58farv3ViccM3Ya8YaGXMibxj9icjXszXk4ulHbNoQibQdZqHkicibJ2oMQ8wEZx4TyPmVMSLib9gdZe6p65DM/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaD62326DJP1Y2OFiaomkjZSNNd3eR2Zm0Vmv1TbwOCh9dOpX0GicKLiceXGPmynDAiccgodjKzqCtR6BPIKQ9mEKKe4Nl21dNZO8pg/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaD4bq3A2MQrfZv7GveUnd9BVoudmlJZ87G0OsKFz2PNjmgpMtzzBn0o7IvtU6thZWickFiblsvTmB7uW82dS9YJtzgydrrCRrcyw/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCNtYhlXRa9GSwIkYtGvLH4kt2tFOwUGlDRzcGNL1xX7EBsVricWATU01jbe5m1vHTaelA51mOUbk9YZHCYiaQFEYZZhDcOwaaGA/640?wx_fmt=png&from=appmsg "null")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

Gh0xE9

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

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