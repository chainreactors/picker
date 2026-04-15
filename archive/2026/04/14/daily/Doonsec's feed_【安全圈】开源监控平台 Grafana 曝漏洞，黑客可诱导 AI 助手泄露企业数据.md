---
title: 【安全圈】开源监控平台 Grafana 曝漏洞，黑客可诱导 AI 助手泄露企业数据
url: https://mp.weixin.qq.com/s/FtQ_p2gxVHxHQ4Ibwfot-w
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:41:32.385093
---

# 【安全圈】开源监控平台 Grafana 曝漏洞，黑客可诱导 AI 助手泄露企业数据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHOlbBv27UxMzFM86ubVgV09mJNxFq244mBT0VkX1RA0cJEsibeMwTuBua7tpH23j2jLwxavkNY8L1iaFLbLJwCwAiao3UhkcphAc/0?wx_fmt=jpeg)

# 【安全圈】开源监控平台 Grafana 曝漏洞，黑客可诱导 AI 助手泄露企业数据

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

漏洞

安全公司 Noma 发布研究报告，披露开源监控与数据可视化平台 Grafana 的 AI 助手功能中存在一项名为 "GrafanaGhost" 的安全漏洞，允许黑客利用 " 间接提示注入 "（Indirect Prompt Injection）方式诱导 AI 助手泄露企业敏感数据至外部服务器。

据介绍，Grafana 内置的 AI 助手支持用户通过自然语言查询与分析监控数据。**但研究人员发现，黑客可以在 Grafana 可访问的外部网页中嵌入恶意指令**。当 AI 助手解析这些内容时，可能被误导绕过既有安全机制，并触发对外请求，将敏感信息以 URL 参数形式发送至黑客控制的服务器，由于整个过程不会产生明显报错提示，用户往往难以及时察觉异常。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyGCcHTweVgeDQFzuRQ0oVcTYWk3bgyP3CbE8Er5hCwPb9M0PO21PyGGI3gPD4ZCFjuOXrIlwctXddiaIbQRSEibG8UZdbvuOeqI4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHHSemT2kAO6lGjJGga1ZaVkYeFd0x10KjxiaiayLN8UpF1OsXDHUawleibmIsRpSrwh2Nt6vTOP9ibl8IbZic2AXBbeIIIYQu8VTaI/640?wx_fmt=jpeg&from=appmsg)

对此，安全媒体 Hackread 援引 Grafana 开发方 Grafana Labs 首席安全官 Joe McManus 的说法称，**公司在收到通报后已迅速修复相关问题**。同时其强调，该漏洞并不属于 " 零点击 "（zero-click）或 " 自主攻击 "（autonomous exploit）类型，黑客本身需要先获得用户端权限，才能主动与 AI 助手交互，同时需要多次触发才能实现恶意操作。

Grafana Labs 进一步表示，目前没有证据表明该漏洞已被实际利用，也未发现 Grafana Cloud 有数据泄露的情况。相应问题属于特定条件下、由用户操作触发的风险场景，而非完全自动化、无感知的 AI 攻击，因此呼吁平台用户无需紧张。

***END***

阅读推荐

[【安全圈】黑客利用 Claude 和 ChatGPT 入侵多家墨西哥政府机构](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075617&idx=1&sn=ae5ccccf31e54fadb3a3ae3a96442518&scene=21#wechat_redirect)

[【安全圈】国际联合行动识别超 2 万名加密货币诈骗受害者](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075617&idx=2&sn=e0977dea287f90ca2172e2f363610190&scene=21#wechat_redirect)

[【安全圈】十亿条 CISA KEV 修复记录分析揭示人力安全模式的极限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075617&idx=3&sn=37b38b70dab479d02d3f08d8edad460b&scene=21#wechat_redirect)

[【安全圈】知名电脑检测软件 CPU-Z、HWMonitor 被入侵！安装包被投毒 开发者回应](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652075585&idx=1&sn=beb1c4000130b2ff57bb5d4e98be2556&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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