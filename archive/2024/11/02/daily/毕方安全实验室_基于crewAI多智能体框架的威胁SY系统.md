---
title: 基于crewAI多智能体框架的威胁SY系统
url: https://mp.weixin.qq.com/s?__biz=MzI1MTE3MDAwMw==&mid=2650436262&idx=1&sn=2ae51c1d9e58580c11ac00addae059c8&chksm=f1f9cf1ac68e460c446ed23e946cc7d094a214709ab300dedcb29a533a7ee253caef68084a81&scene=58&subscene=0#rd
source: 毕方安全实验室
date: 2024-11-02
fetch_date: 2025-10-06T19:18:24.349703
---

# 基于crewAI多智能体框架的威胁SY系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y0KTl5fJqTU7r7QVxUAjp9l3mFibJ3Hd8QibFS5lfnMib4G0Rs8Zuh7ybanEJiae8IPOK4Wh93x90ibf8jEuJvYrAvw/0?wx_fmt=jpeg)

# 基于crewAI多智能体框架的威胁SY系统

be4c0n

毕方安全实验室

刷到黑哥写的[《大模型时代已经来临！AI Agent进入2.0时代..》](https://mp.weixin.qq.com/s?__biz=Mzg5OTU1NTEwMg==&mid=2247484242&idx=1&sn=8c3ca9e7cc7175b192756f908109651f&scene=21#wechat_redirect)，文章中举例了kimi在情报挖掘获取方面的能力，刚好前不久在测试使用crewAI多智能体系统，来完成针对某个ID的SY报告，当时只完成了1部分，用了2个智能体：SY智能体和报告撰写智能体。后续可以考虑使用kimi在这方面的能力对想发进行迭代优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y0KTl5fJqTU7r7QVxUAjp9l3mFibJ3Hd8HlRaiaF6YUMPFNeZwPm5rgPwgVcQ8DtcNib9QbfNhHWhFx5SfDP6ciaoQ/640?wx_fmt=png&from=appmsg)

crewAI多智能体框架可以配置多个Agent，将复杂的Task拆分成多个子任务，然后给子任务分配给对应的Agent去实施，最后使用Crew来对整个任务的工作流进行配置，就会由智能体来自动化的完成某一些重复的工作。每个Agent可以使用crew\_tools模块中现有的工具，也可以自定义开发对应的辅助工具。

使用crewAI可以完成简单的SY工作，比如对某个ID进行SY，并完成对应的报告。有2个智能体：SYAgent和报告编写Agent，2个智能体有各自的任务：SYAgent主要基于社交ID关联搜索该ID相关的各种网页历史记录，并对信息进行总结，可能会使用ID搭配prompt中提到的各种关键字组合搜索。报告编写Agent是对汇总的搜索结果进行分析提取输出符合格式的报告。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y0KTl5fJqTU7r7QVxUAjp9l3mFibJ3Hd8sR4rQ8dgE0bAbtFaGficiaFGxmPFzzfQDPkHWIVf2nfeKfZQ2dSuoILQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y0KTl5fJqTU7r7QVxUAjp9l3mFibJ3Hd8RibwlzGgswEy0zTu0TrzYXg5v4Tic8TO6lJRkyd7PuLb1Gbn0eAPdobA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y0KTl5fJqTU7r7QVxUAjp9l3mFibJ3Hd8G0aQKib3k8YNKPIwxTtwF9eXvdgYh2pvMzJBbcaPWeWLibgAFfSdE0qA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y0KTl5fJqTU7r7QVxUAjp9l3mFibJ3Hd8TgDkcNxBahuMeO43U1LAxjwNwtiarbVTZ3LZjWq6ZLicSqia7h9hKmCzg/640?wx_fmt=png&from=appmsg)

测试用的简单小demo，还有很多需要完善的地方，比如可以将智能体更加细化成更多的小任务智能体，以及对报告相关的任务要求进行细化。之前测试调用文心4.0完成上述任务也基本上没有问题，crewAI升级之后对模型的导入进行了迭代，国内的一些模型使用方面可能会有一些问题。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y0KTl5fJqTU5Y2XXgTYvv18icegL4F4EB1Q9d4SbiadnCoY8G8OJPkxSJnYIBjzGIz7Vz5GW10By4nCjdcLyuEvw/0?wx_fmt=png)

毕方安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y0KTl5fJqTU5Y2XXgTYvv18icegL4F4EB1Q9d4SbiadnCoY8G8OJPkxSJnYIBjzGIz7Vz5GW10By4nCjdcLyuEvw/0?wx_fmt=png)

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