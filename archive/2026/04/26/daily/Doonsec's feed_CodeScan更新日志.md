---
title: CodeScan更新日志
url: https://mp.weixin.qq.com/s/apbUORUxGFaJ14fCVB-o2Q
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:05:00.096221
---

# CodeScan更新日志

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zmF08GSBtAYmjkmibUVD8wzGTHOu3X8Et92nQOyPOGm6KrFxq37IptMOysQMfhnfj6lLGicAcbMsuU5B3XVKxleIcqt0Y5icce79JENFkTkFuk/0?wx_fmt=jpeg)

# CodeScan更新日志

原创

现在你看到我的ID了
现在你看到我的ID了

E条咸鱼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 更细方向

之前的版本，扫中小项目还行，但是在测试new-api(20w)和sub2api(60w) 这种量级的，就发现特别吃力，于是就打算，改一下

主要是这两类：

* • 单线程
* • 工具效率

# LangGraph

针对"单线程"用户挨个手动点，现在让LangGraph写了一个流程，现在路由扫描完成后，会自动开展后面的阶段扫描，每个阶段扫描完后，也会进行自动验证漏洞（同时4个）
PS: 有一个阶段执行错误了，是反代那边的问题
![](https://mmbiz.qpic.cn/sz_mmbiz_png/zmF08GSBtAa7Bx44T3jSdl8HdJBDwUSVReUREynV6vicJpjgFdpUxJ5XDibnBjH60fk22yGiaRxicDziayenmfbJWicFdayDlY3sI9UIkUFvUlEUQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/zmF08GSBtAZjOueorZy0ORMGrNq3natjzKI0HwX2ibouialZrVt3PfGH3WmZ9PttWN7yIIKOaicxoupjib3znfficK5tDRXI2D4k1iabnRlVUp9Io/640?wx_fmt=png&from=appmsg "null")

# 工具效率

现在把grep匹配文件内容，给修改成了优先用rg(ripgrep)，如果没有就回退go自己实现的，所以需要先系统先装一个这玩意
同时以前是模型返回后，一个一个执行工具调用的，现在改成并行了，加快了点执行速度

现在至少都能正常审计完了（

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/597X6b5pKffETricr1okBCV7yKJLpXWW0zcP1icmMDq5YYu5ibQ44D2w3S9cA2crAwMGmFWFvhSWLJzIWjX3fM2FQ/0?wx_fmt=png)

E条咸鱼

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/597X6b5pKffETricr1okBCV7yKJLpXWW0zcP1icmMDq5YYu5ibQ44D2w3S9cA2crAwMGmFWFvhSWLJzIWjX3fM2FQ/0?wx_fmt=png)

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