---
title: 挖不到高危就去“捡垃圾”
url: https://mp.weixin.qq.com/s/KRkjbrtMyjpYT8C0JTMPUw
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:27:03.327970
---

# 挖不到高危就去“捡垃圾”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JnmoqeNZZwTSCwUgJ6SollUDDicZWM9yKw2ibHltg8e64iaeGOZJP0gfuGhlia2EWeCNXibF6jOKgOsa02uzeGg5eoWDNgqKmY0uS0icYVTiaABM68/0?wx_fmt=jpeg)

# 挖不到高危就去“捡垃圾”

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于隐雾安全
，作者隐雾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

📝 **编者语**

很多刚开始挖漏洞的朋友，经常会遇到一个问题：

高危看不懂，中危挖不倒，感觉整个项目都没有洞。

那就去捡垃圾，

但别小看这些垃圾。

有时候一袋垃圾，也能换不少钱。

今天这篇文章，就用一个简单的案例，带大家看看 “捡垃圾式挖洞” 的思路，以及一些常见、好挖、通过率高的低危漏洞类型。

1

常见“垃圾”类型

***一、SQL 报错信息泄露***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nwjsW6nE1DdsqsKqYokZjUBPEAFhTib16baS8n2Qm9mqSDFV8YnhdPYA7afnoqVWcDWuFSlia52mP3VPoxhic3VvJEGa6f9bqGmg/640?wx_fmt=png&from=appmsg)

测试位置

* 表单提交接口
* 查询接口
* 搜索接口
* 登录接口

测试方法

常见方式是直接对参数做异常输入，例如：

'"\

或者构造异常参数值。

如果服务器在 SQL 执行异常时没有做处理，就可能直接返回数据库报错信息。

常见泄露内容

* SQL 查询语句
* 数据库名称
* 表名 / 字段名
* 数据库类型（MySQL / Oracle / SQLServer）

常见风险点

* 为 SQL 注入提供结构信息
* 暴露数据库设计
* 暴露服务器路径

***二、用户名枚举***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4nhdVYPzGETG1o3lOdCaYGrs2xBK7uhCSt0AqvBkH3Bo9YrOmgfXicAWsFtL2HR3ZJGIWNroGqAqFElKJItevtlb0cibtP3tcrpg/640?wx_fmt=png&from=appmsg)

测试位置

* 登录接口
* 注册接口
* 找回密码接口
* 验证用户名接口

典型现象

系统对不同情况返回不同提示，例如：

用户名不存在密码错误

攻击者可以通过返回信息判断：

某个账号是否真实存在。

常见风险点

* 批量枚举系统账号
* 为撞库攻击提供账号列表
* 为社工攻击提供目标

***三、Swagger 接口文档泄露***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4mzzXwjByFjJIgrRAvsHBnFZlMZjbh54dlBjZBgadnQGtucyvG4UicjicDPNeVhZib2H7yhgzYVJ3yqgly7CCgDnI8PyMC1hWHibr8/640?wx_fmt=png&from=appmsg)

很多系统在开发阶段会开启 Swagger 接口文档，如果上线后没有关闭，就会直接暴露 API。

常见访问路径

/swagger/swagger-ui.html/doc.html/v2/api-docs/api-docs

常见风险点

* 所有 API 接口结构泄露
* 参数结构公开
* 内部接口暴露
* 管理接口泄露

有些情况下甚至可以直接通过 Swagger 调用接口。

***四、备份文件泄露***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4kia0Ryc7gGCal24fg6Cpq7LaibMNSoRCbKConbUab3Un5iarmgCls2OvB00vfoOFIfpvg6KqhRwlOZRia8eRbIOiaNfe8RO4ae9ZwI/640?wx_fmt=png&from=appmsg)

这是出现频率非常高的一类漏洞。

开发人员经常会把备份文件留在 Web 目录中。

常见备份文件

index.php.bakwww.zipbackup.tar.gzsite.rardatabase.sql

常见敏感文件

config.php.envdb.sqlbackup.zip

常见风险点

* 网站源码泄露
* 数据库结构泄露
* 配置文件泄露
* 密钥信息泄露

***五、CORS 配置不当***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4n6BwTVfbQicfOJesict5HXva96c2Lvy4aicicHVh0Ba8ia6ibY3ZenzHNtfnUjMia0dZmOKyPaU1tg2nsibBoBoejKywVMcYZC8m2a74E/640?wx_fmt=png&from=appmsg)

跨域资源共享（CORS）如果配置错误，也会形成漏洞。

常见问题配置

Access-Control-Allow-Origin: \*

或者服务器对所有来源都信任。

测试思路

构造跨域请求，观察返回头是否允许任意来源。

常见风险点

* 用户数据被跨站读取
* Token 信息泄露
* API 数据被恶意网站获取

在特定条件下可以升级为高危。

***六、开放重定向***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4mWDZDddcM8HjnibzicHJqZe28b9FhoH9EiaWaCbmOLd5QASE7Vnt0bcFYtKdibFCHwkSSmRxnR54ffV4FwO86B1cw26R02rDlERoM/640?wx_fmt=png&from=appmsg)

某些系统会提供跳转接口，例如：

/jump?url=/redirect?target=/login?redirect=

如果没有做域名限制，就可能形成开放重定向漏洞。

测试方法

将参数替换为外部地址，例如：

https://evil.com

常见风险点

* 钓鱼攻击
* 恶意跳转
* 绕过安全检测
* 组合攻击

***七、SPF 邮件伪造***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nPrbeXsEiaU7vm6RK2YLT7SCbpnYzHwXe8I4GRlf5lwwE7n3se4ibMiaydM1DvI3NicPgdB2M4KH0ia2ibEUIxXysKOSQJ8rUkWn4iaE/640?wx_fmt=png&from=appmsg)

SPF 是邮件发送验证机制，如果没有配置 SPF 记录，就可能被伪造邮件。

测试方式

检查域名 DNS 记录是否存在 SPF。

例如：

v=spf1

常见风险点

* 伪造官方邮件
* 钓鱼攻击
* 品牌信誉受损
* 冒充系统通知

***八、目录遍历***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4kU4ueDLYQX7buuLQKL3ocyDh5XPQ7fTv9eiaLeQGSH5pjApw3EGP0fCggw4o7Fql36gJcrDpMPIN9rlYLL3I41PjzN6ArBNYaw/640?wx_fmt=png&from=appmsg)

某些下载接口允许用户指定文件路径，如果没有做路径过滤，就可能读取服务器文件。

典型参数

/download?file=/read?path=/export?filename=

常见测试 payload

../../../../../

常见读取目标

/etc/passwd/web.config/config.php

常见风险点

* 配置文件泄露
* 源代码泄露
* 系统信息泄露

***九、Git 源码泄露***

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4mFWeK4hnHeYYShEMRwyXTeJl9MdPDwhgicFqnRpPuEJp1qpH4D2w5Z4uRUrfCaYAcske2XumoqUxHSs4KgQzNV4F0ic35VJm3dg/640?wx_fmt=png&from=appmsg)

很多开发在部署网站时，会把 .git 目录一起上传到服务器。

攻击者可以通过访问：

/.git/config

判断是否存在 Git 仓库。

如果存在，可以直接下载源码。

常见风险点

* 网站源码泄露
* 提交历史泄露
* 配置文件泄露
* 密钥信息泄露

***十、robots.txt 信息泄露***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4mklrwKibOMzaFIkeLsK3UhptGOCA1udM0xTay6ndiaPjx4l2TVZ0ZaFWPxQsfXt0EONrr5sbXGlo84C8mvhF2KkvuN9wEdPcKmY/640?wx_fmt=png&from=appmsg)

robots.txt 用于告诉搜索引擎哪些路径不允许抓取。

但很多开发会把敏感路径写在这里，例如：

/admin/manage/test/dev

反而暴露了后台入口。

常见风险点

* 管理后台地址泄露
* 测试环境路径泄露
* 内部系统入口泄露

***十一、Debug接口未关闭***

在开发阶段经常会留下测试接口。

常见路径

/debug/test/dev/api/test

这些接口有时会返回系统信息。

常见风险点

* 系统配置泄露
* 调试信息泄露
* API 调试接口暴露

***十二、错误信息泄露***

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4mhAZySUxQtheV3NcB4f39hq3ibsDSf9n0Z6TJwrmgdWSJvt38jgiciaL8Wn0NTG0tfBekYNvF1L94GfBeSNyacJdiaHSvtpXph4Dw/640?wx_fmt=png&from=appmsg)

某些系统在异常处理时，会直接返回完整错误信息。

例如：

* 程序异常堆栈
* 文件路径
* 服务器信息

常见风险点

* 服务器路径泄露
* 技术栈暴露
* 框架版本泄露
* 调试信息泄露

2

为什么会收这些“垃圾”

实际上，在很多 SRC 或企业内部项目中，低危的价值并不低，原因主要有两个：

***第一，项目漏洞数量本身就不多***

有些系统安全性比较成熟，高危漏洞确实很难出现。

这时候很多测试人员会通过低危漏洞来完成交付。

***第二，部分项目低危奖励也很可观***

有些企业的漏洞奖励策略是：

只要漏洞真实有效，就会给予奖励。

甚至有些平台上：

低危的通过率反而更高。

建了个src专项圈子，内容包含**src漏洞知识库**、**src挖掘技巧**、**src视频教程**等，一起学习赚赏金技巧，以及专属微信群一起挖洞

圈子专注于更新src相关：

```
1、维护更新src专项漏洞知识库，包含原理、挖掘技巧、实战案例2、分享src优质视频课程3、分享src挖掘技巧tips4、小群一起挖洞
```

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg41LkR0ezBlmjJY4Lwgg8mr1A5efwqe0yGE9KTQwLPJTe9zyv3wgYnhA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=23)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOXg868PqXyjsACp9LhuEeyfB2kTZVOt5Pz48txg7ueRUvDdeefTNKdg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=24)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuZDDDv3NsbJDuSicLzBbwVDCPFgbmiaJ4ibf4LRgafQDdYodOgakdpbU1H6XfFQCL81VTudGBv2WniaDA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=25 "null")

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuY813zmiaXibeTuHFXd8WtJAOApVm8H605qOibxia5DqPHfbWD6lmcweDjGv4DLl45waD068ugw2Iv2vg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWr5g7s0TNF4tBZqNbdewPNswTDOfvN6PkggCqz8j3mib6Vf3z4ia83asg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=27)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4Bd1oBmTkA5xlNwZM5fLghYeibMBttWrf57h8sU7xDyTe5udCNicuHo8w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=28)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYrUoo5XZpxN9Inq87ic71D6aUeMdaWrKXgYYia2On8nMA7bqWDySa8odAq1a0kkp3WFgf0Zp0Eut0A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=29)图片![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaRqDOYRFjU73rIsVy2ISg4KKlic4yiafWTpLdejicQe3MllEQc24ypeI3anaK7IjJDVyq1WVQN2yKBA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=30)

图片

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWHjP3FUnZpXdrOicRWrCf9MibaglQia7WesCVs0ibtBhC4c2XiaT9HibE1Drg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=32)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuadANlnTubvh6Abe7UZLdQWXytl9Ioah3X7tw7EMlWV96wWXEHFEM4m6NwlvvkcmEcPqcxcE9MQDg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=33)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaDpuFU7U9TMK5eIpY8iaJcXCicmTB6fsRd8icmH7K1X99YbC07GaJbCRReocORsnDGNU7H7PeqcysIA/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=20)

![Image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/JnmoqeNZZwTfs01Kibo9QSpAIZXwz6o6OBibuI5teemoRKWqSRbZTYCL8cIgNfhovS0RdAF9iaec2FgHCkWTXoll1So90FGQUWOS9qphD9ZBWo/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=19)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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