---
title: 【安全圈】欧洲航天局被黑客入侵了，部署JavaScript代码
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066932&idx=2&sn=42e17f836ccd841a15c83e11995c514b&chksm=f36e7834c419f122314a84f2273aad8f88f6d89cc2079ae0448a5b334528810bb9351fe8daec&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-26
fetch_date: 2025-10-06T19:39:15.671240
---

# 【安全圈】欧洲航天局被黑客入侵了，部署JavaScript代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhApEOE1lUNibicgVFDsHUoLiakQZyroRwEeyjkPjIAts6eLUD0FXqaGZP4hGeLFiaa8egvibSaqMwc1WA/0?wx_fmt=jpeg)

# 【安全圈】欧洲航天局被黑客入侵了，部署JavaScript代码

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhApEOE1lUNibicgVFDsHUoLiaPk1xa9MDloxugjkZYBhUTVA8PqFgnsHQ3f79JySZAtebC1yIN6GzSQ/640?wx_fmt=png&from=appmsg)

欧洲航天局（ESA）的官方网络商店遭遇黑客入侵，加载用于生成虚假Stripe支付页面的JavaScript代码。

欧洲航天局每年的预算超过100亿欧元，其主要任务是通过培训宇航员以及建造火箭和卫星来探索宇宙奥秘，进而拓展太空活动的边界。目前，获准销售的ESA商品网络商店已无法使用，页面显示的信息是“暂时失去轨道”。

就在昨天，这段恶意脚本出现在欧洲航天局的网站上，并开始收集客户信息，其中包含在购买流程最后阶段提供的支付卡数据。电子商务安全公司Sansec于昨日察觉到这段恶意脚本，并发出警告称，这家商店看起来是与ESA系统集成的，这可能会给该机构的员工带来风险。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhApEOE1lUNibicgVFDsHUoLiaibjAQzKGBK2Zn3A0exl5d893HNMt3ibLPv3DFRia1zK3BrficzOnxan5tA/640?wx_fmt=jpeg)

Sansec警告ESA商店已被入侵

Sansec发现，用于提取信息的域名与销售ESA商品的合法商店所使用的名称相同，只是顶级域（TLD）有所不同。欧洲机构的官方商店使用的是.com的顶级域名“esaspaceshop”，而黑客使用相同名称但不同顶级域（TLD）的.pics（即esaspaceshop[.]pics），这一点在ESA商店的源代码中能够看到：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhApEOE1lUNibicgVFDsHUoLiaDQ2o7xIdBEPxV2bWPpB2xlJqAP86OP97LHqZJRazvpd2Ortycb2PuA/640?wx_fmt=png&from=appmsg)

ESA网络商店中注入的恶意JavaScript

该脚本包含来自Stripe SDK的混淆HTML代码，当客户试图完成购买操作时，就会加载一个虚假的Stripe支付页面。值得注意的是，这个虚假的Stripe页面看上去并不可疑，特别是当该页面由ESA的官方网络商店提供。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhApEOE1lUNibicgVFDsHUoLia1v3jPA0EdicHDlPUl5DQYqeDl4xTZg9ClLRLZz3yPazZic2icGtO3TDUg/640?wx_fmt=png&from=appmsg)

ESA的网络商店加载虚假的Stripe支付页面

网络应用程序安全公司Source Defense Research证实了Sansec的发现，并捕获到了在ESA官方网络商店中加载的虚假Stripe支付页面。目前ESA官网网络商店已经解决该问题，不再出现虚假的Stripe支付页面，但在网站的源代码中仍然能够看到恶意脚本。

ESA表示，这家商店并非托管在其基础设施上，也不管理其上的数据，所以不用担心会影响ESA相关工作。通过简单的WHOIS查询可确认，这家商店的域名注册信息与ESA的官方域名（esa.int）分离，且注册人的联系方式被隐私保护掩盖。

ESA在线商店的攻击事件是一个典型案例，反映出品牌授权模式在网络安全管理中的潜在风险。特别是当授权的外部平台未能执行严格的安全审查时，品牌自身的声誉和用户的安全都会受到威胁。

参考来源：https://www.bleepingcomputer.com/news/security/european-space-agencys-official-store-hacked-to-steal-payment-cards/

***END***

阅读推荐

[【安全圈】盘点" 崩溃 " 的 2024](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066903&idx=1&sn=36c25e0bcd6b736bef1f2732300088c5&scene=21#wechat_redirect)

[【安全圈】突发！GitLab将停止对中国区用户提供GitLab.com账号服务](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066903&idx=2&sn=864191a625f27c17468da3dfdff3f8f7&scene=21#wechat_redirect)

[【安全圈】日本弹幕网站 NicoNico 向黑客支付 298 万美元勒索赎金](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066903&idx=3&sn=8e77e867c5725aad13410bfad8f64f09&scene=21#wechat_redirect)

[【安全圈】腾讯与跨境汇款平台Ria达成合作 用户可通过Ria将款项汇至微信支付或绑定的银行卡](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066835&idx=2&sn=fde78ad37031b6df96ec87167929947c&scene=21#wechat_redirect)

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