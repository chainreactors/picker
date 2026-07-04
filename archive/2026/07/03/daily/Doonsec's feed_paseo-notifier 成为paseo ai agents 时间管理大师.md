---
title: paseo-notifier 成为paseo ai agents 时间管理大师
url: https://mp.weixin.qq.com/s/3kPHQx9kPNSVcbwVQloRxA
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:45:34.258601
---

# paseo-notifier 成为paseo ai agents 时间管理大师

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fL1TQ0l0Qw11RxXiaOEZia4VuB6hkJaZKqF6HomDWw4FFpADQ4Se2iaomI6uzA09pFjOEu2HcwJTiaxcrRibpicMPh8WhVwBOuEk434wicHguh41icw/0?wx_fmt=jpeg)

# paseo-notifier 成为paseo ai agents 时间管理大师

原创

酒零
酒零

NOVASEC

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近AICoding用的越来越多，试了很多个agent，最后感觉如果能远程就更能提升效率 (能从5\*12小时打工牛马升级7\*24小时纯牛马)。

目前主要用两个远程agent:

1 Trae Work  国产闭源，app适配度比较好，缺点就是对非主流部分模型没有针对性优化，然后因为429这种问题导致任务中断也不会自动继续重试，移动端连接会有一点同步延迟，不知道是不是因为用户太多。

2 Paseo  社区开源，优势是支持多种agent cli，算是一个多Agent cli的封装器，支持远程操作。缺点就是同步信号也不太好，但是可以自建中继服务器。还有就是兼容性问题导致无法播放出通知声音，任务写完没有通知，导致经常不知道写完了没有，影响效率。

Paseo。

官网： https://paseo.sh/

开源地址：

 https://github.com/getpaseo/paseo

Paseo 的运行逻辑：

1  PC 本地运行 Agent，代码和环境依然在自己的电脑上。

2  手机作为控制器，通过扫码连接，默认支持内网穿透，可以自建中继加快访问速度。

中继问题通过paseo-relay项目自建了一个服务器，加快了手机端同步电脑🖥️。

zenghongtu/paseo-relay:

https://github.com/zenghongtu/paseo-relay

paseo任务完成后让手机能够进行声音通知这里设置了很久都没有成功，不知道什么原因，查日志好像是打包后导致的驱动问题。

周折许久，最后发现通过调用paseo本地服务的MCP可以查询到相关agent的运行状态。因此又实现了一个监听服务，在任务完成时可以通过钉钉 飞书之类聊天工具的进行消息提醒。

paseo-notifier:  Paseo 状态通知器
https://github.com/winezer0/paseo-notifier

![](https://mmbiz.qpic.cn/mmbiz_jpg/fL1TQ0l0Qw2l8aEEJuAbSNiciacGJb0BUzA0Wr2A3TIYsTlpqPhZgllfs3bzFFHL0Ra7FzdAdjQcmo4BbW9CgoYxQaSLeYCu8Lmr04UemKAfQ/640?wx_fmt=jpeg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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