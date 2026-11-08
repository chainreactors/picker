---
title: 海外SRC漏洞挖掘：\\\\绕过403 + 接口不校验token字段签发JWT
url: https://mp.weixin.qq.com/s/v63HFMNS4Mkk25BLyixshQ
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:52.928731
---

# 海外SRC漏洞挖掘：\\\\绕过403 + 接口不校验token字段签发JWT

# 海外SRC漏洞挖掘：\绕过403 + 接口不校验token字段签发JWT

原创

LL.
LL.

狂做有氧

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

很久没有写东西了 根据平台规则 不能披露细节 见谅 说下思路

利用过程如下：

1. 访问 /api/login-xx 403 利用\绕过 访问 /api\login-xx 400

2. 发送  '{"login":"任意邮箱","token":"任意值",...其他字段}' 返回带jwt字段的json

3. 利用返回的jwt从/api\login-aaa换取登录cookie

4. 利用其他的正常业务接口可以做的操作：全量PII 水平越权敏感信息读写

技巧:

curl的 --path-as-is 选项可以绕过路径规范化 用来测试接口比较好使

![](https://mmbiz.qpic.cn/mmbiz_png/ZibkibejKcK5wYhE9Ox3R4u89lBLTDUxK5qvtMl6penoeMGvp1Fia08KshDj9KVhmurfw4HPV9vUeNYCE0Gg83HsiaI9xdWfice3AQRD5KTrHsbc/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/06wlibGymODqloxx4n0D63t65tGOfsUXLkVbFoWaKWZYOArp0aPCicoWC6gFRlkHH23ZTh9UepiatFQX2LgvmMrCA/0?wx_fmt=png)

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