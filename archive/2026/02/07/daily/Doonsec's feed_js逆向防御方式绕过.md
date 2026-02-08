---
title: js逆向防御方式绕过
url: https://mp.weixin.qq.com/s/cqqM_IR2d7mbhSeCprVeBw
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:28:25.550150
---

# js逆向防御方式绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EAbmJhJ6dbeVGIib4KMA6q4UKYiaj1DfRM2YITX5KohJaicm1DLd7QJTycNLW9f1DTNUeibicv4wOsMs6KiaO5tVbbobWN7w872sPxxyicSw8DkUDg/0?wx_fmt=jpeg)

# js逆向防御方式绕过

原创

小白鱼来了
小白鱼来了

Joker One Security

![]()

在小说阅读器中沉浸阅读

/\*本文仅用于技术讨论与学习，利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者及本公众号不为此承担任何责任。\*/

### 场景1：F12无法打开

当访问url时，右键或F12无法打开

解决方法：

* 在访问url前打开F12
* 利用火狐浏览器访问url

### 场景2：无限debugger

当访问url并打开F12时自动触发断点

![](https://mmbiz.qpic.cn/mmbiz_png/EAbmJhJ6dbd9UOySQDB0YGU8JkI8wRnibsRjlZEyWq0FnPMuAodvt6dZMAKYr5sflMMP0pu77hlGmxqQzVicf4OEqekmVypqgEGPAINxe8EMY/640?wx_fmt=png&from=appmsg)

无限循环

* while 循环
* for 循环
* 计时器

for和while循环就是方法体里加debugger。JS中的定时器是setInterval

参数：第一个参数是要定时执行的代码，第二个参数是时间。

#### 方法1

此时选择火狐浏览器,根据自动debugger可以发现其关键作用函数

![](https://mmbiz.qpic.cn/mmbiz_png/EAbmJhJ6dbf1LcdVpzEp8FbCRAFXm2e64uibXN6HnmujNMlI6kutcdBRkZZHpKUffZanicudkYG3nbv7f6cKXN7TqE2E779O1195qhVbSYRmg/640?wx_fmt=png&from=appmsg)

可以发现这里是定时器进行触发debugger的，定位到该处右键选择忽略这行

```
  r.default.config.productionTip = !1,
        setInterval((function() {
            debugger ;console.log("debugger")
        }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EAbmJhJ6dbfZHK9H3VucrrN2A9BuH8r0AsaX4bYv4jIscEkuZfDEs3sExINhkM0icsgnicUGia3RcJsVyKS2qibVG1UhUTpsiaAE34SnicZPicFvxM/640?wx_fmt=png&from=appmsg)

另一js文件的debugger也选择忽略

![](https://mmbiz.qpic.cn/mmbiz_png/EAbmJhJ6dbd0fFSW2bAtvmspU3hv6Kqx5MeZ6fLGOC3GatlA8uibvHhIu66D8hZOr2xT50HIg2dnOF6A4AD93UwQUic4vpMibnSTqktQxAnkEM/640?wx_fmt=png&from=appmsg)

#### 方法2

添加判断语句，将debugger产生判断为false

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EAbmJhJ6dbfFwyxB4hlkbMvXs8gYRnFicULkHicNgkzibkE87A6XURSqDjV8tEYaJbAOvNpQkMbFPPCdbSGtcHSKJic7hgTI9BE7bNpcwnCZzico/640?wx_fmt=png&from=appmsg)

此时设置为false时就不会再产生无限debugger

#### 方法3

禁用关键函数断点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EAbmJhJ6dbedhNwBjItAqG34LFDhLzUldT34zXP14yrYicdjZ5nhq9W8BWZib3licrZJyzDFLEy0AKGtbBd3oW7lLwfUFmJCCcWxshQP8jeicyY/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xr8pIUAaaPvbicPEiahNzcLrRLdSUsdibyBlf0tsuuXjTJOzhvPRJEicImhGcuG1cKln6TsY9NtXDkfbsnpnncQf4A/0?wx_fmt=png)

Joker One Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xr8pIUAaaPvbicPEiahNzcLrRLdSUsdibyBlf0tsuuXjTJOzhvPRJEicImhGcuG1cKln6TsY9NtXDkfbsnpnncQf4A/0?wx_fmt=png)

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