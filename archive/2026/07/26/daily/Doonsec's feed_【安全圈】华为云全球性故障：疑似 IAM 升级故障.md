---
title: 【安全圈】华为云全球性故障：疑似 IAM 升级故障
url: https://mp.weixin.qq.com/s/8vri9ycg2R1P3y2xLUnRAg
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:39:33.051572
---

# 【安全圈】华为云全球性故障：疑似 IAM 升级故障

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyFUsQUZKQ5HxUDcIu1s5b6nJGIZicyZPcIFZo9yxicPAC9BPac2zOvsfC8ia4UVRAcp2Jv2HiaSKiaxadKbV7NpXaNh2RU3lOt57VVI/0?wx_fmt=jpeg)

# 【安全圈】华为云全球性故障：疑似 IAM 升级故障

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

华为云

7月26日凌晨，华为云国际站出现大范围服务异常，部分用户遭遇账号登录失败、云资源管理操作失败、资源异常冻结以及服务器无法访问等问题。公开报障涉及阿根廷、土耳其、巴西、埃及、泰国、墨西哥、智利等多个海外市场，呈现出明显的跨区域特征。

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyFHHBSMeNzic2sU7ribXaFNos9ib7FuJ3Wvw8GeYou1aDBouLd1mhTwRks7OMHqhx5fnqrLKmno7S3HzXjgLZVa9osjaOib2Bkw10I/640?wx_fmt=png&from=appmsg)

根据现有监测信息，北京时间7月26日2时49分，华为云官方监测到“国际账号异常”，并于3时34分前后在国际站官网发布相关通知。第三方云服务监控平台StatusGator则于3时32分检测到异常，此后陆续收到大量用户报障。截至当日上午8时15分，过去24小时内的报障数量已超过450条，异常持续时间超过4小时。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyFt46dujB04V8cT5QbXPOfo6ZHNib257bd9JibSMpIfYBuvAeOOWCqfyzicr6LXxLYP29F1zGUmiaW7d1yicVM6ibBHY51z7vUG0liceE/640?wx_fmt=png&from=appmsg)

从用户反馈看，本次事件的影响并不局限于账号登录。一些用户表示无法正常进入华为云控制台，另一些用户则遇到资源创建、修改和管理操作失败。还有用户报告云服务器被异常冻结或无法访问，表明异常可能同时影响身份认证、资源管理及部分业务访问。目前，公开报障主要来自华为云国际站，尚未发现中国区域出现同等规模的集中故障报告。

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyFRlb0jAUP9ibq09I1cGJM61GFLGxeibEba8wOkic8Otv0dZlkzZqy0Wq4kgK4FT194m36L9c1HZHEqhKgY6tyUdnVoxrPC3VSLYw/640?wx_fmt=png&from=appmsg)

值得注意的是，本次异常与华为云此前公布的统一身份认证服务升级窗口高度重合。

华为云于7月17日发布公告，计划在北京时间7月26日2时至4时对统一身份认证服务IAM进行升级。公告显示，升级期间，用户通过IAM控制台或API进行身份认证管理操作，以及使用部分云服务管理面功能时，可能出现短暂的概率性失败。

![](https://mmbiz.qpic.cn/mmbiz_png/sbq02iadgfyHSXqk8wMkULFCYfuxp2AdjrQb5Kd77TLNOksWyxBCRJhicvtFBD1vA0pDh6ZhsxNagicq2jMicoYZw4Vu6oAtTmR738vL5js2PU8/640?wx_fmt=png&from=appmsg)

IAM是云平台账号登录、身份认证和权限校验的重要基础服务。如果相关系统在升级过程中出现异常，影响可能进一步传导至控制台、API和云资源管理等环节。不过，华为云原公告预计的影响主要是短时间操作失败，而此次用户报障持续数小时，并出现资源冻结、服务器不可达等现象，实际影响范围可能已经超出原定维护预期。

目前尚无充分证据证明此次异常由IAM升级直接引发，也不能排除其他共享控制面、账号系统或区域基础设施同时发生异常的可能。维护窗口与故障时间重合，只能说明两者存在较高关联，具体原因仍有待华为云进一步调查。

对于受到影响的用户，建议暂时减少资源删除、重建、关机、权限修改等高风险操作，避免在系统状态不稳定期间反复提交请求。同时，应保存错误代码、请求ID、异常截图、资源状态和监控记录，并通过官方工单渠道反馈，以便后续排查和申请相应的服务补偿。

截至发稿，相关异常仍未完全恢复，华为云尚未公布完整的故障原因、具体影响范围及预计恢复时间。本文关于IAM升级与异常关联的判断仅基于公开时间线进行推测，若后续官方通报与本文分析不符，应以华为云官方说明为准。

***END***

阅读推荐

[【安全圈】马斯克为了安全，要把"X"完全开源？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077986&idx=1&sn=c72b731dda33c8916f4096cf332615db&scene=21#wechat_redirect)

[【安全圈】每单收超千元服务费，上海警方抓获 3 名外挂代拍违法犯罪人员](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077986&idx=2&sn=11aa39242de4b5b0197f8676b1c497ea&scene=21#wechat_redirect)

[【安全圈】新型 Dolphin X 恶意软件利用 AI 对高价值目标进行评分排名](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077986&idx=3&sn=7212e4b798829226046df566ed3e65d8&scene=21#wechat_redirect)

[【安全圈】数百万辆车可被远程熄火！这个漏洞比你想的更恐怖](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077973&idx=1&sn=c5a357c37a1b18979e6b3c93d7117066&scene=21#wechat_redirect)

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