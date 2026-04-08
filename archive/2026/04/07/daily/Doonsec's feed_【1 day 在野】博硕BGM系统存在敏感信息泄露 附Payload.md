---
title: 【1 day 在野】博硕BGM系统存在敏感信息泄露 附Payload
url: https://mp.weixin.qq.com/s/_yQPtROjRtw0H3rIbuDKVw
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:31:54.900689
---

# 【1 day 在野】博硕BGM系统存在敏感信息泄露 附Payload

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquNhI0URPJUkNd2GRKRAS0r6eOGpnx8gCSbAD4JSwJkccpoXcDHN9aiccTHQSeymxJvdH5K7rEV7c3bGbeEnJMtvFTn6EMecPJkA/0?wx_fmt=jpeg)

# 【1 day 在野】博硕BGM系统存在敏感信息泄露 附Payload

原创

阿伟
阿伟

船山信安

![]()

在小说阅读器中沉浸阅读

**免责声明**

由于传播、利用本公众号船山信安所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号船山信安及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

**一、漏洞描述**

**博硕 BGM 系统是一个集销售管理、生产控制、原料管理、车辆调度、实验室管控、财务统计和智能物联网监控于一体的综合数字化管理平台。管理平台某接口处存在未授权方法调用漏洞，接口通过Method参数动态指定后端执行的方法，且未对调用的方法及参数进行严格校验与权限控制。攻击者可构造请求，任意调用后端类方法（如 Sky.PlatForm.Core.clsUser.GetData），获取敏感数据或执行未授权操作。**

****二、影响版本****

****博硕BGM****

******三、360Quake 语法******

****body: "Libs/Platform.lib"****

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMrTA64icl3GmEFGEPq15BlA8DAibCGUkmSzOawaJlyz1YHrUmKryKuMl5iapGLkgFzuCJGcIibeibLl25wqmDwhTWuXP54iaiaDmO4wA/640?wx_fmt=png&from=appmsg)

******四、漏洞复现******

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquPktwMc4YMmASKiboEC2FhCeap8kYdKKiaZ7AgAyCcMVCfwLwfqPxAUic7EgaBb5jA7SuRpO7ibxWAWHlItrbGke7viakbWRdWmOJ9k/640?wx_fmt=png&from=appmsg)

********五、修复建议********

****升级平台版本并应用安全补丁、取消接口中动态方法调用机制或对可调用方法进行严格白名单限制、对请求参数进行合法性校验与过滤、启用安全防护策略并开展全面安全审计、从源头消除安全隐患。****

********六、payload获取********

******后台回复20260407获取Payload******

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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