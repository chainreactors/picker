---
title: 一个接口顺走全量人员信息：完整利用链复盘
url: https://mp.weixin.qq.com/s/auKX8zT0Ibf7r-fo2Wi2XQ
source: Doonsec's feed
date: 2026-10-13
fetch_date: 2026-10-14T06:51:08.695339
---

# 一个接口顺走全量人员信息：完整利用链复盘

# 一个接口顺走全量人员信息：完整利用链复盘

原创

炫彩之星
炫彩之星

菜鸟学安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

攻防演练中最常见、也最好用的漏洞是什么？很多时候答案就三个字：无鉴权。本文复盘一次授权攻防实战，目标为xx系统：测试中通过JS抓取接口 + 前端代码审计定位到接口统一前缀，批量爆破后仅凭未授权接口，就拉回了 xx 条社区人员信息——姓名、手机号、身份证号、人像照片，甚至还拿到了 OSS 存储桶的临时访问凭证。

下面完整还原这条利用链：接口怎么找、数据怎么泄露、存储桶路径怎么暴露，每一步都附真实请求与截图（数据已脱敏），仅供学习交流。

在某次攻防实战中，发现某平台存在未授权访问漏洞，泄露xx条人员身份信息，包括身份证、姓名、手机号等，以及泄露人像图片等敏感信息。

本次渗透测试总计发现高危漏洞2个，漏洞情况如下表：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 序号 | 系统名称 | 漏洞名称 | 漏洞数量 | 漏洞影响 | 漏洞级别 |
| 1 | https://xx.xx.xx.xx.com | 未授权访问 | 1 | 泄露xx条人员身份信息，包括身份证、姓名、手机号等，以及泄露人像图片等敏感信息。 | 高危 |
| 2 | https://xx.xx.xx.xx.com | 未授权访问 | 1 | 未授权接口泄露OSS存储桶路径。 | 高危 |

# 1 未授权访问

漏洞地址：https://xx.xx.xx.xx.com/api/h\_ll/commbox/v1

漏洞描述：

通过JS抓取的接口做批量未授权测试，并且发现/h\_ll/commbox/v1存在未授权访问漏洞，返回xx条社区人员身份信息，包含身份证、姓名、手机号等，以及泄露人像图片等敏感信息。

前端代码审计获取的前置路由为/api,只需要在根路径拼接上前置路由，再去批量爆破接口，测试未授权即可。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gr0dGRDMRPA10HLvzrqPvh3pL5rgqIliaicHWX7NXSVQXXdhgmLriagRpp47t6ZYC1SGgYB9q50dtOicdDISWFtC4mWdtibw7RGx5bg/640?wx_fmt=png)

图1 前端代码审计定位接口前缀：在 JS 源码中搜索 baseUrl，发现接口统一前缀为 /api（左上为系统登录页）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1grT65ibeIXia70sWkXlYUWSHshgDLk4vb3GhwZZ02fibicLtv2OdVl6hIhhkml46kbxyjvW9V2fp0htoErBcqOrpQowdp7vicpuBs4Y/640?wx_fmt=png)

图2 批量爆破接口发现未授权：Intruder 遍历接口字典，/h\_ll/commbox/v1 未授权返回 xx 条人员数据，响应体中姓名、手机号、证件号及人像图片地址一应俱全（已脱敏）

泄露了所有用户的姓名以及手机号如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gr7XcGDOC175wVc7LNHzeL6zEz3kibGLoNNjMddzg7aWDcicoGySajHOiaf4baDKtWH36BfLTlKtM7LuX3Ju8uI6JDeloRTTNIZvs/640?wx_fmt=png)

图3 泄露的用户账号与姓名数据：敏感信息扫描统计出账号 xx 条、手机号 xx 条、身份证 xx 条（已脱敏）

泄漏了xx条社区人员身份证信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gqm3M7EnIHQO4rl66nhNyiabQL5SymNlrUe8BkhHyhAur1YPAxjeQibW5XaRd126eD25nC3jmWibDJkheCmYeOoCG3FaO9UPTtwKA/640?wx_fmt=png)

图4 泄露的身份证号数据，累计 xx 条（已脱敏）

一共获取到xx条社区人员详细信息。

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gpP2JPfN3PqfluTsiaDTZYQoVUqajTjPBfDQxOPycekHOia7vPpUEAN87WlA3z3jasQR7buNA8ADMZHk9eIYaZZ1E92giaxdXMmVM/640?wx_fmt=png)

图5 单条人员详细信息：姓名、手机号、住址单元、证件号等字段齐全，totalCount 显示共 xx 条（已脱敏）

同时还可以通过存储桶路径访问人像图片信息。

https://xx.xx.xx.xx.com/admin/account\_info/20230311/8c27ae6be72472c9fd11678519139303.png

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gp1wUU5o4VibmZ9CS9UqD1PugxuBpSG6seIicYicOGSLAeYDBphRNSSV1sAes8bnOaickEb4ia0SiavVTOHNhvB5HJmeq49H8mxWia9ow/640?wx_fmt=png)

图6 未授权泄露的文件路径：浏览器直接访问即可查看人像照片，无需任何登录态（人脸已打码）

# 2 未授权泄露存储桶路径

漏洞位置：https://xx.xx.xx.xx.com/api/startupload/v1

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gqpqyO3xJ95jC3SSFcDichu9ZVVaKzDIQycKeSGm90EKbBBJkFIqHuUzkct3joCG4YfK1csYKl9q7KKAoF8e6MfvicibeG3vmIhibw/640?wx_fmt=png)

图7 系统登录页：漏洞接口位于同一站点，未登录状态下即可直接调用

在burp抓包工具中找到/startupload/v1接口。![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1gptrHpEGsT4TiacaGAHuONP3yvhyF3ibfq9L0YaXUFwE1wZmCT5059Iib0icyadt2Cy4UDn6yLaRa5iaRnxGjA1o0DlXa3SGJjcMnWg/640?wx_fmt=png)

图8 在 Burp 中结合前端 JS 定位到 /startupload/v1 接口定义

拼接访问得到https://xx.xx.xx.xx.com/api/startupload/v1

![](https://mmbiz.qpic.cn/mmbiz_png/oFamj4ye1gphhoPfBtZMOBjlAJialRFicpXeNmQ4o0IhqaJwQZV3rltMYAoavkDnmz1ZEcn8a7xYLZzxT8Il6P895icZYJREWxmBvUsKo0kD2U/640?wx_fmt=png)

图9 未授权请求 /api/startupload/v1 返回 200：响应中直接下发 accessid、security\_token、签名与策略等 STS 临时凭证

泄露OSS存储桶路径：

https://xx.xx.xx.xx.com

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oFamj4ye1godzIFVmRuGAyka7znkiaqUOSiaZCNDkcicHzdGibB2HS0eHp1Sx9iblyNwDQ8icxqqBn6xYZYalHp7L29sDibqjc6YyfWNUD7HX6o7SA/640?wx_fmt=png)

图10 浏览器直接回显凭证 JSON：host 字段即为 OSS 存储桶地址（已脱敏）

回顾整个项目：两个未授权接口，一个全量返回 xx 条社区居民实名信息及人像照片，另一个直接下发 OSS 存储桶的临时凭证，把存储桶地址与读写策略一并暴露。两者叠加，攻击者不仅能“读走”数据，还可能对存储桶内文件进行篡改和删除——在攻防演练中，这已经是核心数据失守的级别。

写在最后：这类漏洞没有复杂的技术含量，却往往造成最直接的危害——一行 baseUrl、一次批量爆破，就可能让大批个人敏感信息裸奔。防高级攻击之前，先把每一扇没上锁的门关好。技术交流之余，数据安全，人人有责。

免责声明：本文所有测试均在授权攻防项目中进行，文中涉及的域名、路径与个人数据均已脱敏处理；内容仅供安全研究与技术学习，严禁用于任何未经授权的测试或非法用途。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HezRQjNneVHy39103FjCvxFaZicO2OgEB05ZbBLwibDiaCTqDJNUHUCC9OXjVeiasG4ibOVR0dg284RCzVquVhvQ3xQ/0?wx_fmt=png)

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