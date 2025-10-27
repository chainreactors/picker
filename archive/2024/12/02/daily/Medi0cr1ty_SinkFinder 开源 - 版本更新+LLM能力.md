---
title: SinkFinder 开源 - 版本更新+LLM能力
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODE3NTU1OQ==&mid=2247484434&idx=1&sn=53a73fd788799aa73d1b5bf8d884ad50&chksm=c067c33af7104a2cd4e6fbbc098832d56a6dd3766e5d4e15f0f6f0ed443b4321e0717a8ce8d0&scene=58&subscene=0#rd
source: Medi0cr1ty
date: 2024-12-02
fetch_date: 2025-10-06T19:37:01.213681
---

# SinkFinder 开源 - 版本更新+LLM能力

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWhYOG6qmsTHl91apZHhAchc2D4erf8VpvlhvAJicI7Eiav133pFfHbZ8GS6Dk1Xc5VBZoNZkk5N9z8w/0?wx_fmt=jpeg)

# SinkFinder - 版本更新+LLM能力

原创

medi0cr1ty

Medi0cr1ty

![](https://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWhYOG6qmsTHl91apZHhAchcOzxZYTeAcGuIFRy9U0ImVAPWIxzu6OsZEIV6AFxMDGJQbVdX0ADkSw/640?wx_fmt=png&from=appmsg)

**更新内容**

* 更新入口 Source 点判断
* 集成 LLM 能力
* 其他缓存优化

**1. Source 点判断**

* webx 入口实现 com.alibaba.citrus.service.pipeline.Valve 的接口；
* servlet 入口继承自 javax.servlet.Servlet 类
* 实现接口包含 Filter/Interceptor
* spring入口存在 Controller/RestController 注解

**2. LLM 能力集成**

* 接入通义能力
* 将攻击链&上下文代码逻辑提供给大模型，让他给出该路径可信分数，判断主要考虑：是否输入流可最终到达 sink 点；是否存在安全限制，绕过可能性

**3. 代码链接**

https://github.com/Phelaine/SinkFinder

更多内容参考：

[https://mp.weixin.qq.com/s/pKA0eG0B\_yMkeV2-C1edWw](https://mp.weixin.qq.com/s?__biz=Mzg5ODE3NTU1OQ==&mid=2247484406&idx=1&sn=4ebabbc7065f50f5a101437e02b5f55d&scene=21#wechat_redirect)

**欢迎交流&反馈！**

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

Medi0cr1ty

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

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