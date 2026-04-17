---
title: 企业赏金SRC实战案例二
url: https://mp.weixin.qq.com/s/akio6fzsiu8Vg1kYfR_mkw
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:48:50.688303
---

# 企业赏金SRC实战案例二

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tOrb0WDic7ichrFMtQ8XrUWicrM8HQhHiaa2mKoZvbwZTmdJTmBXjKhRFYxqVBkjN8AGqbvmbhavWDxKAV1qpmO8E2au0Hroy5l0Yj41lTmOstg/0?wx_fmt=jpeg)

# 企业赏金SRC实战案例二

原创

信通云服
信通云服

信通云服

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下分享在企业SRC一个简单的实战案例，内容进行打码，和图片内容替换，漏洞均已提交修复。

**漏洞挖掘案例**

先进入平台，后发现使用功能需要账号实名认证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icgaN0ls3XAQfQHzpibar7eFibuTplXxzFCEPSE872iahofJiayqOAZRdia6cC0rmZV4W49wj2payViaVMWhM2r8H0zKgEcfLdDzhdjFI/640?wx_fmt=png&from=appmsg)

进行个人身份认证

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tOrb0WDic7iciaFjzfr3BRU1RkiaaSIzUzfvX5MOJGImEOFxBL1iaT5XZWjjqkxuDUDiaqJyqr3DnvH9bibgAhwZLkjicfsPkyHBibmm3vp08clmkfWE/640?wx_fmt=jpeg)

这一步只需要生成一个身份证照片就行，名字和身份证号随意，符合格式就行。

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7icjVgMWh8xf4saymYqPkicS0TOUhdHsVsStgZU5Hz0HPjhMzw9mWp6cXO9zG3FGGa3VAV2QBibjkib5icaQSvRcq7s8137fKLWgF6c0/640?wx_fmt=png&from=appmsg)

进入扫描二维码人脸识别认证，抓包

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7iciana3r9E7oAOWx2k1kzGwR2ib35dyfvibaZ6ecxTeNxIXY1BGnfibI73htvSN788ZU9qlaqUdFIQjUlw0wJRYQPpmq6yegEjnv6Xg/640?wx_fmt=png&from=appmsg)

抓包发现存在对应校验包，修改返回包对应参数，false为true绕过人脸认证。

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7icgAHXBGBlbcLIkgIaP0YxsWIb7nG1c1n0sVpz8LuLbVG3X8ONAiceVmNc2Nhiaxw9vkRauEsH67iaR1d8AiaQQnZesTyibzibBGy1pEo/640?wx_fmt=png&from=appmsg)

修改返回包发现已经真人验证成功，可提交

![](https://mmbiz.qpic.cn/mmbiz_png/tOrb0WDic7icgpVasGUviaeGHvko2PL1Dcm6odhZ1IYcECDXNSKctpV8XDK9gWYdZlRvRcdHOkkLicE7GMy2ezIat1IPdjsuFuhYrff6w4MIDLk/640?wx_fmt=png&from=appmsg)

然后提交认证，最后成功激活账户。绕过人脸识别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tOrb0WDic7icgeEcadmE7BPicYuGorSnibibPCXGl1QThG2JuCucf897tgfZibc2DfzTNpfF6ia0LnI5uu1AjdJ1rRnhXXtlVrca5kQpXH4sPsFF6c/640?wx_fmt=png&from=appmsg)

最后实现绕过人脸识别认证，可伪造他人身份证进行批量注册账户，用于黑灰产，新用户奖励，薅羊毛等。对平台造成长期影响与安全隐患。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/LI0hzbSc8PbZj0wlf4RzQLdk7nrUiczuKr7Ev999EricU2FxD6zGW2My69yUaycXdf8wJAaeNoevYB0KBO7rRbqA/0?wx_fmt=png)

信通云服

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/LI0hzbSc8PbZj0wlf4RzQLdk7nrUiczuKr7Ev999EricU2FxD6zGW2My69yUaycXdf8wJAaeNoevYB0KBO7rRbqA/0?wx_fmt=png)

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