---
title: api漏洞系列-API权限升级
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496152&idx=1&sn=ddedfa05e83130aba8435d365a25e48d&chksm=e8a5fbbbdfd272adf06e30d502c2484eee74f611168c8cafe744e15609ad9ce596e575538e59&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-16
fetch_date: 2025-10-06T18:54:43.963052
---

# api漏洞系列-API权限升级

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6YN7fzOtggj63I1JIGsusnTyvuPtOrSyrVB7OkP5UYOMgcUUicnSyQ9iaTic6ic5XF7ZRadk1KcNTuNQ/0?wx_fmt=jpeg)

# api漏洞系列-API权限升级

迪哥讲事

api漏洞系列-API权限升级

## 前言

声明：文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。

## 主要逻辑

使用能够嵌入Crashlytics的fabric SDK，用twitter登录到他们的Android/IOS应用程序。用户可以在https://fabric.io/dashboard上管理/跟踪仪表板上的报告。

## 漏洞描述

而在仪表板上，我们可以看到两种类型的用户:

* 管理员-可以删除app，添加成员，删除成员
* 成员-不能删除应用、不能添加成员、不能删除成员

登录到Fabric;每个用户都会得到一个访问令牌,使用此访问令牌和会话cookie对每个请求进行身份验证。因此，我们检查成员的访问令牌是否可以用于执行管理请求。

我们从管理员的配置文件中拦截了一个删除请求，用成员的访问令牌和成员的会话cookie替换了访问令牌(**X- CRASHLYTICS-DEVELOPER-TOKEN**:)

类似如下:

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5lgHxZrcmtuMfMibes90mwcJJiahuFd6fLKrZqyCN0jV5IvgpCzDEVBk4HVjFDhSjAovoPFQsE5sRQ/640?wx_fmt=png)

在发送上述请求时，我们得到了一个200状态作为响应，并且成功删除了应用程序。

使用此漏洞，具有普通成员特权的攻击者可以使自己成为管理员，并可以接管该组织。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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