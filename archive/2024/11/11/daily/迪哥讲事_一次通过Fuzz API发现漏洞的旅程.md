---
title: 一次通过Fuzz API发现漏洞的旅程
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496316&idx=1&sn=8a590c6f1202155c857fa00dca4c64b5&chksm=e8a5f81fdfd27109aa6cd4067712ca755580d1f65523c292dd551d62b8f48213cd2bb9c31565&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-11
fetch_date: 2025-10-06T19:16:17.129083
---

# 一次通过Fuzz API发现漏洞的旅程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZj512NN8jkHHFpgI1LTUnonMnJict5lWAC2R8gEdDbricNm7Gcs2O7qMy3r2AYlss3tgLn5w4dibNNASOdL3ibmpg/0?wx_fmt=jpeg)

# 一次通过Fuzz API发现漏洞的旅程

迪哥讲事

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwzfic3VPt0EfMjicnGXzicDLoHEqtz1cP3Iozxf1tSyMxCFNG9Aya8SziaVKhVw7ia6QugE/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

# **背景介绍**

由于漏洞披露原因，暂将目标网站称为“target.com”。在对目标网站进行漏洞挖掘时，首先的一些必要动作包括：

* 重置电子邮件获取密码尝试登录，发现是否存在一些逻辑漏洞
* 在Burp中选择Target -> Scan -> Crawl
* 在目标网站中，点击任何可以点击的地方

# **模糊测试**

在点击了目标网站中所有可点击的地方后，切换至Burp开始分析所有流量，在逐一查看流量的过程中，发现了一处/api/path/data 的“PATCH”请求，并且该请求包中包含了“语言偏好设置”的参数，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkHHFpgI1LTUnonMnJict5lW0XZUHruVHVoFuicDJVlVBEvcnYcEDFUXLsChjCvLA411AlOVuzduGvw/640?wx_fmt=png)

于是开始针对该API接口进行模糊测试：

* Fuzz 请求方法
* 发送无效的JSON内容
* 更改内容类型（Content-Type）
* Fuzz Host、Origin等

不幸的是，每次收到的响应结果都是500…

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkHHFpgI1LTUnonMnJict5lWgcUJhqwHVhFymNtfjpjz2XUXCpf3Y2GtcCEYFu7rTpHSFAfodutDcQ/640?wx_fmt=png)

就在准备查看其它流量的时候，突然发现发送空JSON字符串`{}`后，居然返回了一条错误信息，真可谓“柳暗花明又一村”：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jkHHFpgI1LTUnonMnJict5lWzPAcibjfY0eLcFZuYZFz9JuE1hFkobqLOflLD2Pn3oJEF4YhyVup7mQ/640?wx_fmt=png)

虽然也是500错误，但是错误信息却与之前有所不同。

通过对错误信息格式化后，发现包含一个带有“Bearer eyJxxxx”的授权Header，甚至还包含了请求发送到的地址，地址为“https://application.us.auth0.com/api/v2/users/auth0|652xx”

通过 Google 搜索找到 auth0 管理 API 更具体的文档：

https://auth0.com/docs/api/management/v2/users/patch-users-by-id

在文档页面中输入令牌后，会显示该令牌可用的所有权限。于是尝试获取用户数据和其它端点，例如列出用户、应用程序、更新用户等，尽管目标只是一个临时应用程序，但仍有大约 300 个用户，其中大多数是 user@company.com 电子邮件。

如果你是一个长期主义者，欢迎加入我的知识星球,我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
如果你是一个长期主义者，欢迎加入我的知识星球([优先查看这个链接，里面可能还有优惠券](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247489122&idx=1&sn=a022eae85e06e46d769c60b2f608f2b8&chksm=e8a61c01dfd195170a090bce3e27dffdc123af1ca06d196aa1c7fe623a8957755f0cc67fe004&scene=21#wechat_redirect))，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

##

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

##

## 福利视频

笔者自己录制的一套php视频教程(适合0基础的),感兴趣的童鞋可以看看,基础视频总共约200多集,目前已经录制完毕,后续还有更多视频出品

https://space.bilibili.com/177546377/channel/seriesdetail?sid=2949374

## 技术交流

技术交流请加笔者微信:richardo1o1 (暗号:growing)

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