---
title: 内网搭建画图工具 excalidraw
url: https://mp.weixin.qq.com/s/LEA7d65QOizv95Om-b89XQ
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T07:04:01.552778
---

# 内网搭建画图工具 excalidraw

# 内网搭建画图工具 excalidraw

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

用 excalidraw 画图还是挺方便的，比如画一个 镜像口示意图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pcx6jPOJRJ1DrYj8ibBuEKmBPYazzdk4SaFpxeuz0iczukYtOm7sbwaQrxVXPIecbuXVoDLpLgeJhBqRuafWpFCDbTpicNwthSmqY/640?wx_fmt=png&from=appmsg)

画风和字体的审美都在线，素材比较多，可以添加到本地：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pc06Etq2oFdFicbXG7mICJcm5Cf3I8Yg3wPj9DsGOIO1NuDM2nYVYoXINP0FrA7eUCuHcjkNVsFl0xxTw2wnrn3teibxb2XMGPTk/640?wx_fmt=png&from=appmsg)

docker compose 配置如下：

```
services:  excalidraw:    image: excalidraw/excalidraw:latest    container_name: excalidraw    restart: unless-stopped    ports:      - "3000:80"    environment:      - TZ=Asia/Shanghai    healthcheck:      test: ["CMD", "wget", "-qO-", "http://localhost:80"]      interval: 30s      timeout: 5s      start_period: 10s      retries: 3
```

启动容器：

```
docker compose -f compose.yml start
```

全文完。

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