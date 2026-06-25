---
title: 原版 OpenClaw 安装过程
url: https://mp.weixin.qq.com/s/0Od-ZYbZbYviL4uvADPvTA
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:02.951840
---

# 原版 OpenClaw 安装过程

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LjdkpgSF7PeEbsiccfl9VT67Bgdv9g8hB2dbWsTtkqtwUMpv7rVHHJPT8S34KnBRfYFF757u7H0ovMDw5lQgapruKgqmHF9yHWe266gtbMYU/0?wx_fmt=jpeg)

# 原版 OpenClaw 安装过程

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

国内 QClaw、WorkBuddy、TreaWork 已经将 OpenClaw 集成的差不多了，基本上没有必要安装 OpenClaw 了。之前 OpenClaw 总是升级后就飞书插件崩溃，后来就把 OpenClaw 卸载了。

今天等到 OpenClaw 官方，发现它的网页出中文版了。尝试安装一下，看有没有新东西。

MacOS/Linux/WSL 下的安装命令：

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

把安装设置过程截个图记录一下：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PedLqJcs92dicPsb4IrTgCRuibbHZzNT9dZnzvnhcb9HIV7icwBxmAWkc4HmTCh4BTUlzLcwj816icWoVYbKg64tRQf0yicpPSfDIMw/640?wx_fmt=png&from=appmsg)

准备环境：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PcvIuX0Igk1Df15bwvWnjxaFZ8VBKKkYIYQmEdic5y3VZ5r25FgaAugk9bzD4CaMF2dB2Xwu0OgwmiaCETzwNFsplJFCdM3eziaIA/640?wx_fmt=png&from=appmsg)

完成安装：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PfUOUc7Z5kGKpCkIFb3AJKoXyIOOmndv65hiaQ1iciaOe55CQRJt4tTbQiacPLfxektX6XuicytUjZXYH4SFYtrjzXZa2qmAenkX3QY/640?wx_fmt=png&from=appmsg)

检查到之前有安装过飞书插件

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PdUdO97tYmiaYqnAh5l8voibXm9DHhOHXOpH205Sx0PVIicEKhJpjNHTtAbo9tMdRzicKeCTia7JscmdPBYWWJtdfFicWrEzt9jwAMmk/640?wx_fmt=png&from=appmsg)

检查多之前有遗留的 key

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PdcV6M3c7YES8dYdUan9cxLibapTQcUB1TsDLibNsHUuk9viaLpkUHmWEq75l0MdJL9LibQib2PdUK9ZVulox5EoDhktdqSYib4dPibWI/640?wx_fmt=png&from=appmsg)

提示是否修复配置？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pcv6bY3xDGWZhQY5CWdUoTlicjNMkiaJo8X77M4XaV7sMWVxb9xibGLDCZGLOdQ2ECZe1dgKyDriaJiaOOGbOestBpwrQx2SHFkAZzA/640?wx_fmt=png&from=appmsg)

重新安装飞书插件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PdN2GicvbGsJZUcRMjlDcdMZMh7rdrnKwvrg25evZ5xfZuKSGQvPibSlpsaGO2G1RoFRRxEBye8XxEurBnSWjPJruL9sP2LhALiaM/640?wx_fmt=png&from=appmsg)

到这里安装完成。后面修复模型 、key等配置，使用如下命令配置：

```
openclaw configure
```

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7PcAoggevQoZtQR0OtNLJ2oEwiahywJOOVltXKHx14hCgMXBspjZBpqH6HQgMhHKqjuKIhQ4ZdQibHudspibCWa6kcgiaV5GT1GibMe8/640?wx_fmt=png&from=appmsg)

配置完重启 gateway，命令：

```
openclaw gateway restart
```

之后就可以在网页上检查 openclaw 状态了。之后可以通过 web 版openclaw 安装飞书插件，就不赘述。

默认网页地址：

```
http://127.0.0.1:18789/
```

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Pe44ZC9FXgvpDujXeqFzq5qQQB5yrdkLUN9XxB8opTnARgL48s7b4xCTrMfN8XMCWj3iaUoibWAIiaiapjdP9dHJkSpeDShia95zFtc/640?wx_fmt=png&from=appmsg)

全文完。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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