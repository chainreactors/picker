---
title: 【安全圈】拦截钓鱼网址操作失误致Cloudflare服务中断
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068120&idx=1&sn=ae8350bd62f190fd9ab9a30dfe146983&chksm=f36e7558c419fc4ebb351ce486bb1285a8b37124437a2d34ea72b086d19eec0622decab90add&scene=58&subscene=0#rd
source: 安全圈
date: 2025-02-25
fetch_date: 2025-10-06T20:38:15.462978
---

# 【安全圈】拦截钓鱼网址操作失误致Cloudflare服务中断

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj2W21u1zFszjibSlH20Ikof3xiakXXcvU6tlrLvicicRicKWZGEuCqoNgvjl6eHxcib8ILEl2TKL643Jgw/0?wx_fmt=jpeg)

# 【安全圈】拦截钓鱼网址操作失误致Cloudflare服务中断

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络钓鱼

![Cloudflare](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj2W21u1zFszjibSlH20IkofLa41QAJjApgBcNNiacRFWLLb6hc2xABdlfrS86F3ZVytT7l4u06F6Lg/640?wx_fmt=jpeg&from=appmsg)昨日，Cloudflare 的 R2 对象存储平台在试图拦截一个网络钓鱼网址时适得其反，引发了一场大规模故障，导致多项服务中断近一小时。

Cloudflare R2 是一种类似于 Amazon S3 的对象存储服务，旨在实现可扩展、持久且低成本的数据存储。它提供免费的数据检索、与 S3 的兼容性、跨多个地点的数据复制以及与 Cloudflare 服务的集成。

此次故障发生在昨日，当时一名员工对 Cloudflare R2 平台中一个网络钓鱼网址的滥用报告做出回应。然而，该员工没有拦截特定的端点，而是错误地关闭了整个 R2 Gateway 。

Cloudflare 在事后调查报告中解释称：“在一次常规的滥用整治过程中，对一项投诉采取的行动无意中禁用了 R2 网关服务，而不是与报告相关的特定端点 / 存储桶。”

“这首先是多个系统层面控制措施的失效，其次是操作人员培训的不足。”

该事件持续了 59 分钟，从协调世界时 08:10 至 09:09，除了 R2 对象存储本身，还影响了以下服务：

1.Stream：视频上传和流媒体传输 100% 失败。

2.Images：图片上传 / 下载 100% 失败。

3.Cache Reserve：操作 100% 失败，导致源请求增加。

4.Vectorize：查询失败率达 75%，插入、更新插入和删除操作 100% 失败。

5.Log Delivery：出现延迟和数据丢失，与 R2 相关的日志数据丢失率高达 13.6%，非 R2 交付任务的数据丢失率高达 4.5%。

6.Key Transparency Auditor：签名发布和读取操作 100% 失败。

还有一些服务受到间接影响，出现部分故障。例如，Durable Objects因恢复后的重新连接导致错误率增加了 0.09%；Cache Purge的错误率（HTTP 5xx）增加了 1.8%，延迟飙升至原来的 10 倍；Workers & Pages 的部署失败率为 0.002%，仅影响与 R2 绑定的项目。

![Service availability diagram](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylj2W21u1zFszjibSlH20Ikof0I3XtENic6psmK46dh205KXRTsJo3xtEqwDNnficBVkHq3NgDXdB2qVQ/640?wx_fmt=jpeg&from=appmsg)

服务可用性图
来源：Cloudflare

Cloudflare 指出，人为错误以及缺乏对高影响操作的验证检查等保障措施是此次事件的关键原因。

这家互联网巨头现已立即实施修复措施，比如在滥用审查界面中移除关闭系统的功能，并对Admin API进行限制，以防止内部账户禁用服务。

未来还将实施的额外措施包括改进账户配置、加强访问控制以及对高风险操作实行双方审批流程。

2024 年 11 月，Cloudflare 也曾经历过一次长达 3.5 小时的重大故障，导致该服务中 55% 的日志永久性丢失。

那次事件是由于向公司日志管道中的一个关键组件推送了错误配置，引发了 Cloudflare 自动缓解系统的连锁故障。

***END***

阅读推荐

[【安全圈】马斯克DOGE网站数据库存在漏洞，任何人可随意篡改内容](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068092&idx=1&sn=2aaad093096f88adba585911871847bd&scene=21#wechat_redirect)

[【安全圈】Atos旗下Eviden公司紧急发布安全公告：IDPKI解决方案曝出高危漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068092&idx=2&sn=07ceda3a43b852c9147f82cc1ed039fa&scene=21#wechat_redirect)

[【安全圈】数据泄露警报拉响！2024 医疗行业成重灾区，远超金融行业](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068092&idx=3&sn=feadbe596231da73575f5a1c17b7609a&scene=21#wechat_redirect)

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