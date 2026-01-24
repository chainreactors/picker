---
title: 阿里云 STS泄露导致的接管
url: https://mp.weixin.qq.com/s/dGarHLgpoWfG_aC7T6EEEQ
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:29:31.214104
---

# 阿里云 STS泄露导致的接管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dZiaSuyRDkINPAWwa8uk4icDk2MwxAq9icGHiaeZRxPJWcRicIJx2M5aB91hPZH8kX2fWTOM1phO5FRZelEOWrba9RA/0?wx_fmt=jpeg)

# 阿里云 STS泄露导致的接管

原创

注册随便看看
注册随便看看

希望对技术保存热情

![]()

在小说阅读器中沉浸阅读

这里全是杜撰，如果真实尝试获取到信息于我无关

STS（Security Token Service）是云厂商（AWS / 阿里云 / 华为云等）提供的**临时安全令牌服务**，用于颁发带时效、带权限边界的临时凭证（AccessKeyId/SecretAccessKey/SecurityToken），常被 ECS / 容器 / 函数计算等实例通过**元数据服务**自动获取，实现免 AK/SK 访问云资源。一旦 STS Token 泄露，攻击者可直接接管对应角色权限，实现云资源横向移动、数据窃取、账户接管等高危攻击。

一般在上传的地方出现的比较多，特别是小程序

下面随便举例一个小程序（纯随机点的一个小程序）

北京巨量引擎网络技术有限公司

![](https://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkINPAWwa8uk4icDk2MwxAq9icGjOmYl1iboJBFCEyfY4w8GiaYaYicyqXMA0LHibRBHNlQkibs41ZyZOym81g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkINPAWwa8uk4icDk2MwxAq9icGxSRv5w8go0EYYHjIKyN68j7d19zp8r3WSUMwujMjbaFnWHUC3ZVfpg/640?wx_fmt=png&from=appmsg)

点进去，如果有客服或者头像，重点是客服反馈上传图片很可能返回sts

类似这种接口

![](https://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkINPAWwa8uk4icDk2MwxAq9icG8ZmDdNm8cCia4yoxnLBKPw5vwt12b3xZJX29c1Z9rYic29mPLhc9QPmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkINPAWwa8uk4icDk2MwxAq9icGBu2TPTrvZ0DFX4KFPPj4iboaRVGOTia70RcwdJxlTibxGLoNyBQKfDkKA/640?wx_fmt=png&from=appmsg)

直接返回了sts

oss下载链接

https://azenta-transfer-doc.oss-cn-hangzhou.aliyuncs.com/ossbrowser/download.html

直接oss接管就可以

![](https://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkINPAWwa8uk4icDk2MwxAq9icGOPbrXfnsRbicGkO7cKkIsyBKJ9uI4ibAyPMeefooNGy7Ib1iaq9woOpQQ/640?wx_fmt=png&from=appmsg)

动手就会获得靶场，注意文章的全部，尝试就对了。成功底下评论1

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkIP0OOqvdFXbgPjK5wic9lE6sU2zPOm9furhribFbZvfaSOXOicfPSUhuLicPcqN8bWcmTmJX6Sj5ZiajEg/0?wx_fmt=png)

希望对技术保存热情

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dZiaSuyRDkIP0OOqvdFXbgPjK5wic9lE6sU2zPOm9furhribFbZvfaSOXOicfPSUhuLicPcqN8bWcmTmJX6Sj5ZiajEg/0?wx_fmt=png)

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