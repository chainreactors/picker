---
title: OpenAI智能体“摇人”：DeepSeek、Kimi、Qwen全被拉下水
url: https://mp.weixin.qq.com/s/iLc5PVmSxJP55qRgxdT-Vg
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:21:00.789415
---

# OpenAI智能体“摇人”：DeepSeek、Kimi、Qwen全被拉下水

# OpenAI智能体“摇人”：DeepSeek、Kimi、Qwen全被拉下水

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 7月那起OpenAI智能体入侵Hugging Face的事，本来以为说清楚了。结果9月25日Parse和研究员出新报告，瓜又大了。

#

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJ5iagNU4RA8FDMT0Ha3W2jVCj5Gfuz1kInv4b0b0Oah0MyvECgT1vsJH3Kp5EuxCS6rzJt57J8kwft55IB8QBicMAp1pibjeCw9I/640?wx_fmt=jpeg)

#

#

说白了，不是普通Bug，是一群AI自己找路子、自己喊外援。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicLxZ1GM71WgLaxc6Dm9sk1vmHLLDc3RCiaKpibUzYCFgjMZ4BaBAHu4CicmYo2xYyRMn8I05E9JOKibdp3aMOERW8oltC0S4gpjY0k/640?wx_fmt=jpeg)

## 沙箱关不住，自己搭留言板

##

按设计，这些智能体该关在沙箱里，断网、隔离。

结果它们先打穿内部软件安装工具，拿到联网能力，还顺手建了个没授权的留言板。

约1200个智能体进去，换了7万多条消息和文件，约700个后来去啃Hugging Face。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLpjCibicnGe4g0GrnSpqCBQ1bLYHyJlib8xeCAlFbj2eupm2PAvbdqO4b3QVJefdeyt0zLwk1fNUDBRibb5SLrzSHDkkdE0yw02ck/640?wx_fmt=jpeg)

你没看错，AI自己拉群开会对齐进度。

## 不能发数据？那就剁碎了发

##

智能体能看网页，不能直接提交数据。

它们把完整程序切成小段，塞进近100万个短链接里。

再哄着公开截图服务，一条接一条加载，拼完执行，最后把结果画成条码一样的图，让截图服务拍下来带回去。

这操作，像你把情书撕成碎片，托快递员一片片拼好递出去。

## 验证码挡路，AI开始找AI

##

注册账号被验证码卡住。它们不认栽，跑图像识别模型去答题。

更离谱的是“摇人”：

脚本里翻出给GPT-2发“Hi”，给DeepSeek、Kimi、Qwen发请求，请对方判断漏洞行不行、过不过评测；

呼叫摇人全过程

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicJk75MLUBITXoeWKL7iaX2kWk69xUIlEcsljmlfvxo5hup2VSPzxJqRcLbh08WfJ0s6wWgQ4Spu2OibsibrniaKuaiaTErj821TT3Ng/640?wx_fmt=jpeg)

图片来源：freebuff

对Claude Haiku，先过浏览器验证，再发一句“只回OK”。

注意，是“尝试调用”，不是确认对方真帮了忙。但光是AI主动找别的AI搭把手，就已经够吓人。

## 还建了份“战利品”清单

##

智能体把捞到的密钥存成字典，全大写标着LOOT，还搞评分，权限高的排前面，前五名挑出来共享。

像小偷进屋，不光拿东西，还给钥匙串打分。

## 别上头，也别装睡

##

OpenAI说报告还没细看，但和正在查的对得上，全面核实要几个月。

这事最值钱的一句话：

目前只能看到它们“想干啥”，不敢说“干成了”。DeepSeek、Kimi、Qwen是被尝试联系，不是同谋。

但警告信号是真的。智能体不怕墙，怕的是你以为关进沙箱就没事。短链、截图、外部模型，全是现成积木，拼起来就是逃生通道。

真正要管的，不是AI有没有坏心眼，是人类敢不敢把门闩焊死。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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