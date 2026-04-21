---
title: Agent 配置 Jar Analyzer mcp
url: https://mp.weixin.qq.com/s/wC4l-ieBbBgkDdC_oxQ_Pg
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:46:50.936905
---

# Agent 配置 Jar Analyzer mcp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVnjjOBdVYoDQNQvRiaN6GsgpVbqhxZ2hKqspzfZ1aSvtBMRO0bxXvq84Po5ianFpAltqxDHiazWbQr8ib5ib27mh9PVoVWoYOicNWgX0/0?wx_fmt=jpeg)

# Agent 配置 Jar Analyzer mcp

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 185，阅读大约需 1 分钟

## 前言

项目地址：https://github.com/jar-analyzer/jar-analyzer

![2628bdf2a9062619a86dbda07a2c5815.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmzDr1j7GhCgISY3TEbnaOAIcfOzzZ5MoNX6cJTTWh0aBrkbWmyZznAexwgAJm9rEgcI8Cnn96UNj0Vf1f7Szuysp3ibrwXYm1A/640?from=appmsg "null")

2628bdf2a9062619a86dbda07a2c5815.png

官方文档：https://docs.qq.com/doc/DV3pKbG9GS0pJS0tk

![9df7b68b25fa97cf4f13d5bc7c1c1b6b.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVka4cHFCeosNEWYmfPefsILfTrc22AsNmibUAyEQvxmUhPibwibhicIylDX9kAfyovicalPrzU4xS2L09bxAeaicwSj9vme1sg6KJtRw/640?from=appmsg "null")

9df7b68b25fa97cf4f13d5bc7c1c1b6b.png

还是很推荐阅读官方文档的，对自身代码审计也有帮助。

**注意**
jar-analyzer 目前不支持导入源代码，支持 jar 包和 war 包。如果需要对源代码审计，需要先将源代码打包为 jar 或 war 包。

## MCP

http://localhost:10032/sse
![eab52344ae7bb40af78a3a73bc57f019.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl7AAUDrJ2VficV1zvelXK9fLfVM2aktnNmdkG3SZktgL3SibdJCAu7V3C728Y3FNRHdVKahoWGhH0Iv6dXyibK0SwiajXAYlucNac/640?from=appmsg "null")

eab52344ae7bb40af78a3a73bc57f019.png

下载 mcp 工具
![d35556d9599364d0711f272acb1364fd.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnQR89RxKZQicUgQicoPRZRozLLS2WMdd9v5uO9TEAC2oEEvxVIQFlFqgicDWmNGQk3E4QQNfdem5aZ4Gq5TqUhiaPY1ibZrtdmiaL7Y/640?from=appmsg "null")

d35556d9599364d0711f272acb1364fd.png

了解一个 mcp

```
npx @modelcontextprotocol/inspector http://localhost:20032/sse
```

![e21fd0e0744e493711aee3fb32074ca1.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnycqnbnSNwDCEwOQlhCs5KmtQ6rwcWB2AcicguVgNWFupyqxzh236puYtDGwiaVfdjXMCzIRgkEZYTKLg5hPeRicG7ANdwosCRNk/640?from=appmsg "null")

e21fd0e0744e493711aee3fb32074ca1.png

```
mcp_v1.2.2_windows_amd64.exe -port 20032 -url http://127.0.0.1:10032
```

配置 mcp

```
{
  "mcpServers": {
    "Jar-Analyzer": {
      "type": "sse",
      "url": "http://localhost:20032/sse"
    }
  }
}
```

**TRAE CN 配置**
![5e447bae2830c4df05c3f84ea586031c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnlMjvswPqOSCJquLMeXiclkWUHj5sDXA7wiafFvibI4bRKiaib1kspMSQjKs50Va1h00icmVlJOhDkx1FkBLtpibfKoD40K57hS0GmK4/640?from=appmsg "null")

5e447bae2830c4df05c3f84ea586031c.png

**claude code 配置**，在项目根目录下创建`.mcp.json`

![babc1baff7d5ea923af200dbf0821a73.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmIAyddLiaxqdZIr5UBJgjoAnuUWh76UdzSZA9EQ7V9FjrWcp9FysHbWJa1aOPyVPU2PlKrOTpDcH2lR6Q7AI6LgOibmEs6jTRF4/640?from=appmsg "null")

babc1baff7d5ea923af200dbf0821a73.png

```
当前mcp有哪些功能
```

![e4a20725407fe3ef616bd6098e46f11a.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnYPqBbpV98AjScolY797vPnTZibAg9NLC2mAnLQnvTqUFQuG5Qs0BK4AhhQkIZTW4FDuXiaBfyshsx6Q4Io2ibHH99ovBfs7FkC8/640?from=appmsg "null")

e4a20725407fe3ef616bd6098e46f11a.png

## 演示

https://github.com/whgojp/JavaSecLab/releases/download/V1.4/JavaSecLab.jar

![a2d0030d10b456225854d465c8b11255.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVl8ZriauicyItGPxz1JSBM3v2MMOyaecSyAKjVF2GPELeVzlyo1CXsME6m1hqgD3RqJHWaZIWdcyLiaYzEhWHNKVRvv5FxhNHeatY/640?from=appmsg "null")

a2d0030d10b456225854d465c8b11255.png

结果
![abdf4e0a65c416e401caeb46e1b310f0.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk0icfL4xBY8Lwkgbgdia59guqHvIOGBTywqrDKXJUenKiap6BbPJ0447T5v0o6SBHibRv81f738XAO3C42ANEWmFGg5TDR8Bxia9T8/640?from=appmsg "null")

abdf4e0a65c416e401caeb46e1b310f0.png

消耗 Tokens
![26b39ce60623325a71712552cb2b70a4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkZW2xhjH94M06gIo1S0mgmjmOrzHCY5AI7qhI8EbLRHiauE49GgaHiaPBxQWT072KeLs6xv8PVFdBkEAKQ0RyeOqQxMG4u4BcaY/640?from=appmsg "null")

26b39ce60623325a71712552cb2b70a4.png

## 游戏

代码审计累了还能玩两把斗地主
![c6c2965a5cc597e9cd07a7b92415d856.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVklPecdEU3Nfeoicc12iaMmLCdDT9qibpiboUHFjrW0pcGC1ckMMhywI3zBohibk3to3sJKZWn8SUZ87U0oMPbeLcboI4EPKA7nWIlk/640?from=appmsg "null")

c6c2965a5cc597e9cd07a7b92415d856.png

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