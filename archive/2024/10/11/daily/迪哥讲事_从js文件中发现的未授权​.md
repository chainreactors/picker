---
title: 从js文件中发现的未授权​
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496096&idx=1&sn=ce34d28b5e7b2a2cfffd894cb6f0f381&chksm=e8a5fbc3dfd272d57a0b9f84200bd6304cb7c4e19c87205ef2283d6e2920367e5646f928890a&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-10-11
fetch_date: 2025-10-06T18:53:34.956663
---

# 从js文件中发现的未授权​

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj5yBsicDWtBycDyRvkpoiau8Nu334dynDXZunURf4qe2ibrodYU8LBtIdhvfmvdlurQqRlCOGL0xbU8w/0?wx_fmt=jpeg)

# 从js文件中发现的未授权​

Omar

迪哥讲事

从js文件中发现的未授权

## 正文

查看某个js文件，手动尝试里面的200个接口(为什么要手动，因为这里每个接口都有特定的参数)，这里花费大量时间去阅读js文件，同时检查它是get还是post请求

同时发现了下面这些:

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5yBsicDWtBycDyRvkpoiau8Nr5RIx2wWZDviaIpZKJjQ5PBMiazhoHZHhiaLXPDS1o5Lq9a44JzGCLNoQ/640?wx_fmt=png)

这是一个接口，用于邮件端发送给用户的广告的类型，并且仅用于使用sso注册的账户，接口本身并没有验证它是sso类型的还是普通类型的，如果你用电子邮件发送请求，他会简单的响应你，暴露出用户的位置,这里它实际上泄露了PII，同时可以修改那个人的关键字来定制发送给他的广告类型.

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5yBsicDWtBycDyRvkpoiau8NVMD0Kn8udfWcicpUCaXZ1HtPzo3T5YN0csM2u5UmVhhMZIh2md0W8QQ/640?wx_fmt=png)

使用GAU和WaybackUrls 来寻找更多使用ID的接口，下面找到了一个:

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5yBsicDWtBycDyRvkpoiau8NB5lq7HRekSH6asXwlTRo4opGiaYJtBLDUYe6KoH9icz5iadQQEd74UBbA/640?wx_fmt=png)

将上面的链接发送到sqlmap以检查id是否容易受到sql注入的攻击,当id=2的时候，按下重置密码时，发现令牌无效

去登录页面->点击重置密码->输入受害者电子邮件->去前面那个给了我们user\_id的接口 ->获取user\_id，前往emailPreview接口，一个未授权到手

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

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

阅读原文

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