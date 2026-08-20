---
title: 一个公共软件漏洞，批量击穿几十家大厂
url: https://mp.weixin.qq.com/s/T5RqQ6lQ54lG6KVnfVClHw
source: Doonsec's feed
date: 2026-08-19
fetch_date: 2026-08-20T02:53:07.145219
---

# 一个公共软件漏洞，批量击穿几十家大厂

# 一个公共软件漏洞，批量击穿几十家大厂

Laurel
Laurel

内生安全联盟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2ZmL5d0ic88X0Qp8c2BicuKl1JBkRib9e6PLzhgY7UKeRia4eRw9YvSjrfKeHjTXRqwCsgXvonicagGB8yvnOQwUrRLIIQStiagt8Nh0Yk1hzlm1Q/640?wx_fmt=gif&from=appmsg)

近日，黑客组织 Clop 声称从全球近50家公司窃取大量数据，涉及Shell、Philips、GE、Fiserv等大型企业。相关企业已经启动调查，目前攻击者声称的数据窃取规模尚未得到完全独立验证。

公开报道显示，Clop 勒索团伙正针对互联网暴露的 PTC 系统的 Windchill 和 FlexPLM 实例开展数据窃取勒索活动，相关攻击利用 CVE-2026-12569。

![](https://mmbiz.qpic.cn/mmbiz_jpg/2ZmL5d0ic88WicUzZ2EPXgVk1FbIMe13fcyXfzUEFTsLcPP5KFR2MaZRF9QUvyId4PUicCKE4ssZe1K1xSACPTpCtw3UhcIET4a03qQk0EKgL0/640?wx_fmt=jpeg&from=appmsg)

攻击的关键特征不是逐家入侵，而是利用广泛部署的企业工程/产品生命周期管理软件漏洞，一次触达大量组织。

PTC Windchill于28年前首次发布，全球拥有超过150万用户，客户包括宝马、洛克希德·马丁、波音和英伟达等公司。FlexPLM 则是专为零售、鞋类、服装和消费品行业设计的版本，承载产品设计、制造、供应链与客户资料，是工业、制造业巨头的核心管理系统，一旦被入侵，可能同时造成核心数据外泄、业务勒索和供应链协作中断。

现代大型企业越来越依赖ERP、CRM、PLM、Cloud等公共软件平台，攻击者因此获得了一种非常高杠杆的打法：

* 找到公共软件漏洞 → 自动化扫描 → 批量突破大厂

实际上，PTC于6月17日就关于该漏洞向客户发出警报并提供了“缓解”指南。随后的两天内，该公司还发布了针对Windchill 版本13.1.1、13.0.2、12.1.2、12.0.2、11.2.1、11.1 M020和11.0 M030的补丁，以及失陷指标（IoC）。尽管如此也没能遏止攻击者的攻击进度。

更要命的是，补丁只能阻止后续利用，无法证明补丁前系统没有被入侵，系统突然变成了薛定谔的黑盒，没人知道它遭遇了什么。

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

[薛澜：人工智能发展下半场的关键任务](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539663&idx=1&sn=9dc39af03aa385dd6c053cbdec7131cf&scene=21#wechat_redirect)

[《2026人工智能时代的科学、技术与创新研究报告》](https://mp.weixin.qq.com/s?__biz=Mzg4MDU0NTQ4Mw==&mid=2247539675&idx=1&sn=da3b41df4048cc8db8908c1c62999091&scene=21#wechat_redirect)

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