---
title: 记录一次对校内系统的安全测试
url: https://mp.weixin.qq.com/s/dF64jY2-z_z6jQKAlP1_5g
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:43:14.257970
---

# 记录一次对校内系统的安全测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJS27L4zTOjbNPTgt8g0VB34ibI1bV5caYM8BibgII7RDiafpPvvbedd5SmOdDU5LAAqvFYTtGLUEPk36LKEoWlkIZ4YIc9rQ3NUcw/0?wx_fmt=jpeg)

# 记录一次对校内系统的安全测试

原创

小菜鸟
小菜鸟

智动心域

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明：本文仅为个人网络安全学习实践记录，所有测试均在合法授权范围内完成，未获取、泄露任何师生隐私数据，漏洞已提前提交学校相关部门并完成修复。请勿利用文中内容进行非法测试。

第一处任意文件上传导致getshell,用账号登录，之前这个数据包没留意，这次把里面的url取出来，去掉了参数workitemid去访问

![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJSYDjM8l6Iksq3YD6yel9GU1icMOeKo7prTTYN2uy2aw3icBrgrlKslOVicKDMej6hH3rIziazeRD1hbia9BFKz7ibhAzEfaguQAxtyg/640?wx_fmt=jpeg)

发现一个隐藏功能点

![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJRYiawU38ygfbcMfu4pnGaNy6wIXH3zS0eYOzs3MBy2UKia5yOhjPjBtp1vOscibAxpU4NVkxAeGXBAbicCwguGEOZKd1E9dp98o64/640?wx_fmt=jpeg)

先传了html解析，又传了jsp木马，解析

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJSFcsP0atbREqLgy3UDmucPW8GL0xbJL7IepGs3RpqCFbsCCtyK8ozFedX4nZAhOib6juwYdNCNBLufQpuicl4ict7yefChMe7KCU/640?wx_fmt=jpeg)

第二处逻辑缺陷

访问服务大厅会有很多越权，本人是学生肯定是学生权限的服务，把id改成1002可看到老师权限的服务

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJT8etNicodDY6X1OGiajyIoAFrE8ORwA3Z0A7UPVHCoE5V51aibGbYmnDCQBIeyMVUhVEGz5rcA0d7n9WIhNWfVh6bmIuoc9sshEc/640?wx_fmt=jpeg)

拼接url得到一处含有学校全体教职工信息的页面，前端展示工号，单位，姓名等

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AFmUR0mIsJQ8aU9nbPyfiagfaEu9Aq1lEGHTS9PVohiaYzyxVNiamksibY7LFeu9DkfFM4QpZmzlQhsaRrXibnTfib93hAGrvgHluIgqg21rFGUHQ/640?wx_fmt=jpeg)

f12看网络请求包，还有身份证，手机号等敏感信息，并且未进行数据脱敏

![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJTyqujsVibrmydv8RVajWT0NyT04AQDZUKKNicWVB7DHicatqLiaYT3SkWTVXLlsyuCZic8OhapC8ibejLeY2ltzSfEVYP0k626uqjg0/640?wx_fmt=jpeg)

第三处前台nday RCE

访问此办事大厅系统会跳转到统一身份认证进行统一登录，这里往往在进行安全建设会疏忽，此系统为某元系统，github找到了23年的rce的exp,本质好像是反序列化漏洞，请求头里放入命令，post请求体携带构造好的序列化数据，直接前台rce

![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJTrPsHmrN73eic4jI7cic3R8oe9XlVYZ4CQrJK4Aed3cgQRbicNG76zIiajemrJKdibGia1jU4lyeQvMWOe5V71iaN5k5vRWZkfGMJcq0/640?wx_fmt=jpeg)

最后也是靠这些漏洞成功上分高级白帽子，换了一个tools论坛邀请码

![](https://mmbiz.qpic.cn/mmbiz_jpg/AFmUR0mIsJTDSNYa6uibXbnw75l5Ow4bGhficCVMwgETlzxHLcVno1yIXj9ibibrtSyWH23zM2M4Nx0iacBT1f6LCLHzMKiaqh7kft3lIMgCZRom4/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Ss2ZBltf4c3Iuia91VP9sgOZMVtTMGBIiaNlE1XaPCaZBaTQUrNyabA1ialBrzeLpS2sOdJWXBCTB8Pv2PUYkwExg/0?wx_fmt=png)

智动心域

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Ss2ZBltf4c3Iuia91VP9sgOZMVtTMGBIiaNlE1XaPCaZBaTQUrNyabA1ialBrzeLpS2sOdJWXBCTB8Pv2PUYkwExg/0?wx_fmt=png)

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