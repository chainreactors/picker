---
title: NASA严重安全漏洞，可导致黑客向飞船发送任意指令
url: https://mp.weixin.qq.com/s/ksVPDWmLnacL4HSHpsA2gg
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:51:14.227167
---

# NASA严重安全漏洞，可导致黑客向飞船发送任意指令

# NASA严重安全漏洞，可导致黑客向飞船发送任意指令

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88UdPQ1Q7qEbcpnremIIJBTQia4Rf49egXJ7Q0aCUW5HRTuiawia9AMLlCWGpED2Juxb5Oxx8jzyrN9kiaUROia1qRowa32rr1gSlH9A/640?wx_fmt=gif&from=appmsg)

安全公司 Cycode 发文，称 NASA 地面数据系统框架 AMMOS Instrument Toolkit 的网页控制界面 AIT-GUI 存在严重安全漏洞，相应漏洞 GitHub 漏洞追踪编号为 GHSA-p9r8-2q67-fp86，CVSS 严重性评分达到 9.4 分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2ZmL5d0ic88Upq6rEX9xWEG9qYGr3LXvicDnG2aUczuHB4icVw7luA9KkOASB1bHZGc5xibNFLOoLzkoDJgLJXa6PQ3lvvibbice2TAoFOv6Uk090/640?wx_fmt=png&from=appmsg)

据悉，AMMOS Instrument Toolkit 系统框架由美国 NASA 与喷气推进实验室（JPL）开发，主要用于地面站与航天器、科学仪器之间的指令上传以及遥测数据下载等功能。

本次曝出的安全漏洞主要源于 AIT-GUI 缺少身份验证、权限控制以及跨站请求伪造（CSRF）防护，同时服务器默认会监听所有网络接口，**因此黑客甚至无需直接入侵系统，只需通过钓鱼方式诱导操作员打开恶意网页，就可能利用浏览器触发 AIT-GUI 执行操作**。

研究人员指出，黑客可以利用该漏洞向飞船和科学仪器的指令总线下达任意指令，同时还能够执行服务器端脚本和命令。如果相关系统被部署在能够访问外部网络的环境中，漏洞可能进一步扩大攻击面，对地面站以及与其连接的航天器、科学仪器造成潜在风险。

目前，开发团队已于 8 月 12 日发布修复漏洞的 2.5.2 版本，解决了相应问题。

来源：安全圈

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2ZmL5d0ic88VEzjic1f7B8a9prz3icdEgQpXH1gOGyCYoZHyUAicqvDfdkVCKTCYm9qicEVTGF7fAosbaxdibXgxBT9na3DsrMjxBOyiadNzFvx5Po/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[【征稿启事】2026 IEEE网络韧性与内生安全国际会议（IEEE CRESS 2026）相约南京，诚邀投稿！](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539413&idx=1&sn=477a535cc1c5dd21ac667eff0f60c271&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/2ZmL5d0ic88Xr95JLPMCj3IEsZGAL0znMgDYy7QcmFibtBvxLR6nTbq4W4vTMnUhAdaobhKG9mibWfVugG7kFoImZBUEf8MqpF5H8AibmLbk1eI/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[欢迎报名！“联盟货架” 征集工作正式启动](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538143&idx=1&sn=923217fe75c1c36cf9de5e5ac894ad10&scene=21#wechat_redirect)

[聚力协同发展 | 中国质量认证中心有限公司南京分公司正式加入联盟，成为副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

2026-06-17

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88XRibsIKXF2TFo31YtyfTpzRKp3lqA3JpyMFdGWKGGVtONQDgr2Hfm8pibrCwAiaQn5RWPJxTgelQxwFln0ZDrAwK8YuDWUgNaxFE/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538421&idx=1&sn=3ba126c3e04109879df4448e076a3494&scene=21#wechat_redirect)

[携手共建产业生态 | 紫光恒越正式升级联盟副理事长单位](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

2026-06-18

[![图片](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88Ug4pM2QBleSEh81Xt2icXIibBY5o6icibpSFMbFcu4TN9eNvibibict0BCDx8nCYrYViclCu2KGMdx7RnIAdrEvuSGtxKa20mBqH9IPhI/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538467&idx=1&sn=e66939c008f88f0003ccbc5fd9c08b81&scene=21#wechat_redirect)

****| 往期回顾****

**[AI4E如何重构数字生态系统网络发展范式？](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247532455&idx=1&sn=ee5102d94087e9440ede67b18386c621&scene=21#wechat_redirect)**

**[资料下载 | 十五五规划建议全文及说明](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247534593&idx=2&sn=7f9516f40cbafbcb1012d5999612157a&scene=21#wechat_redirect)**

**[《科技日报》整版访谈邬江兴院士：将“安全基因”植入人工智能系统](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247537206&idx=1&sn=2ce618202d759560ecee6aeca93b8c24&scene=21#wechat_redirect)**

[里程碑时刻：智己LS9 Hyper搭载原创内生安全技术](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247538132&idx=1&sn=77e4efcb6eea205e082f79b82336cc65&scene=21#wechat_redirect)

[邬江兴院士：构建内生安全质量检测体系，筑牢人类可控可信 AI 根基](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539044&idx=1&sn=1791fd1aad5f130fe5d87c46cc4b8687&scene=21#wechat_redirect)

[工信部定调：6G是"十五五"重中之重，商用时间表首次明确](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539882&idx=1&sn=ba4669e35b87fe44673807be8f1832d4&scene=21#wechat_redirect)

[倒计时！一文掌握《公安机关网络空间安全监督检查办法》核心要点，10月1日生效](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539917&idx=1&sn=3b444d9f11c86980921625ba0c82c62f&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/jRRfTC292pXGqHBACsK1cVtpyTB5F8VFsEY3paWnfS3dichupP4OknoSrNN3c6YviaDsLwKnfHwj1OibB7lWFvbibQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/jRRfTC292pX7QK5QfSb6k3uQJ3EsDmeCnsG6veyEXTXsbCcuuTJ7LWzo0tPv2ezibrAF07JXGxYs8zSXgXibLX2Q/0?wx_fmt=png)

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