---
title: 【EDU实战】豆包EDU测试好帮手
url: https://mp.weixin.qq.com/s/XnV4CYDhfZwi2Ki-PxCpUw
source: Doonsec's feed
date: 2026-08-12
fetch_date: 2026-08-13T04:03:07.141108
---

# 【EDU实战】豆包EDU测试好帮手

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DJX1rNqJe4n95wp7ZYnew62ZxK5OKDw10VF9LogMUTTvfGlIsw3HWibqZNmuYcVLdHSeHEHwHdffOPI9KssQw3uoEpg3d02DRTUvwXmqnV3s/0?wx_fmt=jpeg)

# 【EDU实战】豆包EDU测试好帮手

GG安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于隐雾安全
，作者星期五

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM726qqnXD4ibQaXQjLVHp9Gxyv9TJsiaWicUIvUnjPWalVYA/0)

**隐雾安全**
.

隐雾，为您提供职业成功的关键。

## 📖 编者语

最近整理了一次EDU测试记录。

目标是一个校园餐监管平台。

刚开始测试时，我只是从登录功能入手。

页面需要手机号验证。

后续通过抓包分析登录流程，逐步发现了后台接口中的权限问题。

---

# 从登录页面开始测试

进入校园餐监管平台。

首页提供了手机号登录功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4m1dIhAaib0pDb5NeX8mqQ3CFTBq7KrPrku1sriccXEaQ7wBhcyIMSqUfjw6NiajM53sTpOkfY720iamyHR0MZ4ng69uyBWmicglS7A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4laPkbqov7tYtqnrIrVB2o6miaQHmaYibmvVGYqrCnQ0yZ26DRejZicC7fVXQOJdknS5zPdseMNpZgQmbviaEDo5Q7tg4pQsVOpXn4/640?wx_fmt=png&from=appmsg)

看到登录功能以后。

我先测试了一下手机号验证流程。

随便上一个手机号测试,发现会进行验证。

所以联想到学校的食堂负责人电话。

官网或者学校通知应该有,懒得找,直接豆包搜索

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4kp6Us6oNuicLE1CiaCX40sS6ON04G1jvWUUAaDNXhfaScCYOVKUszGzbOXch7RZtFm9MQL5Ab3zDOfjCxia0MtszcgicNxrvPIGU0/640?wx_fmt=png&from=appmsg)

输入手机号后，页面正常进入验证码验证步骤。

这时候开始关注：

系统是如何判断用户身份的。

---

# 测试登录流程

由于平台主要面向学校食堂相关人员使用。

登录账号可能和负责人手机号存在关联。

通过公开信息获取测试手机号后。

继续尝试登录流程。

---

抓取登录请求。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4k5QCibR7Nh01PTYwSlIdnqRefm7aGCEDF3hria5BSdzIHX2wxSBzfhPav5Poia9pbib2ampnp08KzSX0IXYFeej6CBvFZPujUxrdQ/640?wx_fmt=png&from=appmsg)

查看返回数据。

发现部分认证信息直接返回到了前端。

返回内容中包含后续修改密码需要使用的数据。

继续跟踪后面的流程。

尝试使用返回的数据完成密码修改。

---

# 修改密码后进入后台

修改密码成功后。

重新使用账号登录。

成功进入系统后台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4lqolgMfCsIXkawA4mFOYZAcrTb89nqibNtXp6LgaRBttEQEhNPnwghMUOGYetzP95ZBCu11X0iaUZJb9KfHksc023Npl0Kickk7c/640?wx_fmt=png&from=appmsg)

登录之后发现。

移动端和PC端展示的功能并不完全一致。

PC端包含更多管理功能。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4lvreFDoHGHJnZ6EYczYhn9Dwfiat8viceIFLBiaLCupjhlb4dqLhwxP9tIgUW1CdqQ2CQ1Z47MU7FZAJiaCYQ8sHSTaaibSedIib4vk/640?wx_fmt=png&from=appmsg)

后台中可以看到多个业务模块。

包括：

* 用户管理
* 信息管理
* 系统功能
* 数据查看

---

# 从一个接口参数开始分析

进入后台以后。

我没有直接测试功能。

而是先抓取几个接口请求。

其中一个用户信息接口引起了注意。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nT3ibIjJrwlGESbNbSUQeV2bxpZhEOYiadFYtOqelTXuoSr6DjJZpP1fGJLWGO9awWp0l7Q6AgsROMPVBf0SPhzW9fiazoflNMCw/640?wx_fmt=png&from=appmsg)

请求中存在一个用户ID参数。

类似：

```
id=xxx
```

开始尝试修改这个参数。

---

修改ID后重新发送请求。

返回结果发生变化。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nx63WgYzcE2Yl7sndjPcMnjHRvdVyqtqczFtibJaJKKW0kDWDl6rvaeJtyxicmHeqO9wfnOfco6bo1SWC21nmBlknBDrbgiasESI/640?wx_fmt=png&from=appmsg)

继续测试几个不同的ID。

发现返回的数据并不属于当前账号。

---

# 去掉身份信息继续测试

继续分析接口验证逻辑。

尝试删除请求中的Session信息。

重新发送请求。

接口仍然返回数据。

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4kcPAuAXJKuvjTxI0YykOiahYoTiclUhCGI4mCRPGKfVV6UC2n3GBfgyOoFd8DozpV3hvF8KOvAlmmOpJ5xUmvJpsZeCuLqQsTQA/640?wx_fmt=png&from=appmsg)

这说明接口在身份校验方面存在问题。

---

# 漏洞验证过程

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DJX1rNqJe4nkibemxE4hwB5r2efbedrTzibMbGibVuHLhpKTGQytzdQC0UrSRf9tBRleX76vCXVz6chtOJwicNqsND32a1wiciajgeXhvvJ6f4l5s/640?wx_fmt=jpeg)

#

---

# 本次测试记录

![](https://mmbiz.qpic.cn/mmbiz_png/DJX1rNqJe4nLcepiaVvmFiaRMnQ9vOicCZk6eVIkjt7lX7Bce19lJSz3epxR0Lm7KS2YUyyViaDrdYQeJz920qVb3CX0F6KsNkS4BN716L1kr6g/640?wx_fmt=png&from=appmsg)

---

# 最后

这次测试从一个登录页面开始。

最开始只是确认登录流程是否正常。

后续通过分析请求参数和接口返回。

逐步定位到了后台权限控制问题。

漏洞验证过程主要围绕三个方向展开：

   1、 登录流程

    2、接口参数

    3、权限校验

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia30l0vOygMHwGeYQM3b05DgghRuLMrUGfMh444bY02KJYLXXaur6Qp3IicGOTJQ82Dbs5rrIicaNMxSMWFFF5yXQ/0?wx_fmt=png)

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