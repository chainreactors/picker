---
title: 企业赏金SRC实战案例三
url: https://mp.weixin.qq.com/s/NHFE0OxQ0Am-C-uvlf7Xaw
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:28:55.156681
---

# 企业赏金SRC实战案例三

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tOrb0WDic7ichHCfNWIPic3NxB3V2W6zc9H4PMWICkUqzaplZ2KGiaxVJrH0rBJiac3u2foPuWibhkoXfzAibwfED0vPen5bEYjQEpElJHY1vASJBQ/0?wx_fmt=jpeg)

# 企业赏金SRC实战案例三

原创

信通云服
信通云服

信通云服

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下分享在企业SRC一个简单的实战案例，内容进行打码，和图片内容替换，漏洞均已提交修复。

**漏洞挖掘案例**

还是先登录进去熟悉业务

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7ichFYzoDQ67Q7mQXdHIJN6llKMPlh8O70HtUicQfWKJDL5uX4yUADEMChHcOtW7f3rQjCJQtDuuOvN6RX2ial7hDQLFES23A1ucgw/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=0)

分析是一个客服场景，尝试拉起用户端与客服端。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7ichEMTcj0gJBnVAZn9JX6EKW2NkicEtO0E5eSCSoibNc2uQdVpITOCB9tNrEqKq0yib4iaLGfu0Gwqk5h0MzV9StRg5e5qXUFGgUvHM/640?wx_fmt=png&from=appmsg)

成功拉起聊天后

打开用户端，尝试上传文件html、svg等，发现不解析，打开就下载。

尝试将文件名修改为xss语句上传，发送给客服。

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7ichmicgq3iavics1zliaYFAqXz7G8ndEcbnL9XytyVuDwo4Ujeh2Rysmjcq4Sp9xncU02DxOYWpDS0wHvwaPgIyPhp2BLbZzybAGTS0/640?wx_fmt=png&from=appmsg)

打开客服端，发现成功攻击到客服端

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icjr9FHPEMXGStMBq6YnaUANsPJ4gs3NYjalVeV57MDR1DBhP8j59wUU82oEic7TQgc8WbCEI7icyynLXsEgk7PjibGlXsf8uP27Uo/640?wx_fmt=png&from=appmsg)

当上传特殊文件无效时，可以尝试将文件名修改为xss语句，最后也是成功确认中危

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icgKKYGt8iagcncjDAIV1t5ltuibIY0ibHIku5nrNJl3Uy5ARHjibZoAygmq9hs3AcWPtCwBRmuRSyWpACSYkaRIuU8xMRQxObTXZ6o/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LI0hzbSc8PbZj0wlf4RzQLdk7nrUiczuKr7Ev999EricU2FxD6zGW2My69yUaycXdf8wJAaeNoevYB0KBO7rRbqA/0?wx_fmt=png)

信通云服

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LI0hzbSc8PbZj0wlf4RzQLdk7nrUiczuKr7Ev999EricU2FxD6zGW2My69yUaycXdf8wJAaeNoevYB0KBO7rRbqA/0?wx_fmt=png)

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