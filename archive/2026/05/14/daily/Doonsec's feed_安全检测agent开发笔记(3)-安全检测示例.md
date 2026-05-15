---
title: 安全检测agent开发笔记(3)-安全检测示例
url: https://mp.weixin.qq.com/s/kck8IYytv4LZXvc3AgxW6w
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:47:16.655904
---

# 安全检测agent开发笔记(3)-安全检测示例

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kCaGE674k6OD2hhbFiaOUsRh6icKABxkgJQBD8zdgTialWwbGxeeUf0bjRfzQXzEhprtMqT84LXbNEbfRlXlu8dTgMBIqMlTMpIVXgUgvFJnDI/0?wx_fmt=jpeg)

# 安全检测agent开发笔记(3)-安全检测示例

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

1. 站点安全检测

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6PnIY2cQHdelaG33icibLvzu6ibhiaBAH37RHA0x2utyXvg0vQ2qEPO5iazxgpSjgD8MS2ib1XXAzjC9ZnVMzGwdlLamcxVYMljrC9bc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6Nw18TzfqricuHhrO9q0DrdS2FdyF4MAQRyDP6QjibEOL4ntTOHYzFfKial9fbmBx5icjibIL1epYXsN8eCwLiaxSaMJxQybCU19lsB4/640?wx_fmt=png&from=appmsg)

他是通过我的爬虫，或者说你手动chrome接入发财工具获取的那些玩意，包括url、请求api、js总览，对该站点进行安全检测。

因为测试用的也是国内站点，具体结果不方便展示，大概过程如图。

2. 客户端软件检测

客户端这块找了个国外软件简单测试下

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6OkciammPY4mMOZ5Zag2DoFEqGtQqoek9LzdrFCoMH1R7fEDy1gIwbnF0RdRnfTeFgoQovW1YVs09FVuaxnTqC1Zuiaa2dKa1g98/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6P53kktubNicQeSpMibtyOibwKk4hVfZPlWZmN7iaXG1zErg5x8pPW19a2C5mTs3xh47ko7TT4mku1uhVtZvyu5Uc6c5K4ooz5Coyc/640?wx_fmt=png&from=appmsg)

这里的端口出现了点问题，是我后端的agent调用工具时的问题，无伤大雅，等会就改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6MjMf8RgL4DRhwJoZyeXLicGfW0v0wPVeCpotttcJJ4x1tlayJwVgYlCsfIJupklQIP7rbHkWiatecepWsm2LQPII6vib1THkpNZ0/640?wx_fmt=png&from=appmsg)

因为ghidra这玩意反编译dll要一个多小时，让我强行关模型停止了... 反正效果如图。

支持Windows/Android客户端检测，exe/dll/apk/js/html/log等可执行文件，可读文件的检测，Windows客户端给安装目录和缓存目录，Android客户端，给完整的apk路径，这些东西都会上传到Ubuntu配合asar, ghidra, pwndbg, jadx, apktool进行分析。

重点:

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6MuibLpbnUdU7oAawXLXQY4HZIiaVHuOvrSXHhjmyfASRFpHSrQSYmDHia83BYyHmmL3yudkV2EORriczvaicSWCKp82rY7fBWzK8VA/640?wx_fmt=png&from=appmsg)

全程rtx5060ti+32g内存本地模型，我会再给模型扔一个Ubuntu，他随意操控，对于可读代码审计，二进制exe、dll、apk文件都会通过ghidra、jadx、asar、apktool这些工具进行自动处理。

因为是本地小尺寸模型，我还是刻意压缩了不少，本地模型能力弱，不然上下文长了总崩，比如字符单词限额上下文500，XREF限制层数等。

非顶级模型，尤其我是本地模型，直接出结果的概率不是很高，但是会给出不少攻击面，非常利于之后测试。

如对steam Windows客户端的安全检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6OcVv8TJDZnNNVJMzB5rCdJEtms9ocib6JLJJo1ribOeJV7Cbw21miaRjZV6aoUE0Hx3tCDzbzYhXHnhOlB337FCJMfxQ1Fh4oMtA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6OiaV9gfJAyRm6C2dEwyNoY1TibOLYN7tCgDOKianWCgptkW8GzcOZSHK2oOlk5iatSqlDRJ2QpNYGF5dJnBaQFOYQSQLsmO2MDrvc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6NPLHl1k7VyhKRDMcuIBAQDQOT2YNFTps3MrgbBfXWAicKVticj8Pib8nNibIv2m8XJxor8tqxkia7dBWRInloCLMQDibOLs7via3Ud5g/640?wx_fmt=png&from=appmsg)

基本上覆盖Electron/CEF/QT/原生/Android和其他可执行客户端软件。

有时候想想，碳基生物的价值何在意义何在，硅基模型已经远超过人类很多了。

对facai的pro版感兴趣的，联系微信: guimaizi

未完待续...发财发财都发财

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

鬼麦子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hMZ0ictzVvTt7jx7CZw4MSq5nEQtjICjeaVic6ibJpEw74Sls4kFials6YTebNIl4XBYcKHtzcvNtl0NUd3iaqib1TGA/0?wx_fmt=png)

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