---
title: 通过js进行模糊测试所拿到的一次五千漏洞赏金记录
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496957&idx=1&sn=5ef897f46f3bf16bce1a83b45b0611c3&chksm=e8a5fe9edfd27788ba026eddd3fbb4541a0037c8be19dcb77460d206bd14339fb2c1bd0ebf83&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-28
fetch_date: 2025-10-06T20:10:47.447460
---

# 通过js进行模糊测试所拿到的一次五千漏洞赏金记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4OWf4K62Ir8u2Wn3vUwUVwb0Hw7qRd9Qh8HItTIPjroXVqS48hR0CUvCKzkXKoGI2gWILA4utfJA/0?wx_fmt=jpeg)

# 通过js进行模糊测试所拿到的一次五千漏洞赏金记录

迪哥讲事

以下文章来源于网络安全之旅
，作者小乳酸

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7gOV6xA1v0ib4icvlDwJKiaNEF55z4Lmmd6utIs1DGLFnbA/0)

**网络安全之旅**
.

记录自己网络安全成长之路以及各种奇思妙想，欢迎广大热爱网络安全人士一起交流共勉。

## 0x01 前言

Missing parameter？Parameter is null？一次众测实战教你如何高效的找出缺少的参数。

## 0x02 漏洞背景

一次众测项目，称其为https://uctenter.target.com。

## 0x03 漏洞挖掘过程

前期通过信息收集，找到一处目录organization 状态码返回302，跳转到https://uctenter.target.com/organization/#/，熟悉的空白页面。直接翻js，正则匹配目录，拼接到url后面爆破，全部返回401。

![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEocpROtyRzdFEUkj9pc2j2UbYbv3NFTvKmTVJIehxJAofgewAsuCStBZiaCuzQn32aib432NtYjiaCFA/640?wx_fmt=png)

将其匹配的目录导入到excel，使用/为分割符号进行分列，将其分列后的所有参数保存为字典，导入burp继续爆破。其中一处orgapi目录返回302，跳转到https://uctenter.target.com/orgapi/。

![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEocpROtyRzdFEUkj9pc2j2U2vXP7tBooWWUVeCzbE5aHXlYMZ7QbxYzBpttC9f2wiaPglxR2fhwadg/640?wx_fmt=png)

熟悉的spingboot界面，掏出珍藏的springboot字典，/orgapi/..;/v3/api-docs返回大量接口。继续上续操作，匹配接口，拼接在orgapi/..;/后进行爆破，发现多个接口未返回身份认证失败，说明已经成功绕过身份认证，但是未发现敏感信息。

观察接口信息，发现其中一个接口带有selectuser字段，返回报文为parameter is null。使用Arjun进行参数爆破**，**

使用Arjun自带的字典爆破无果，使用正则将https://uctenter.target.com/organization/#/中的js文件所有单词匹配出来构造字典，去重，大概五万多个。为什么推荐使用arjun进行爆破，假如有一万个参数，正常爆破会发送一万条报文，Arjun会将一万个参数分为25个组合，一个组合为400参数，第一次发送25次请求，只要其中25次请求中，里面有一个参数正确，便会返回不同的响应长度，以此类推，继续分割**，**直到剩下一个参数。

正常使用burp或者其它软件进行爆破，需要发送五万个请求，使用Arjun可发送不到3000个请求。

发现其中一个参数searchId返回不同的响应长度。通过其id值可遍历此厂商所有人员的用户名密码，身份证号码，手机号。

![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEocpROtyRzdFEUkj9pc2j2UH1p8IKB1f9mYTMMCrQhlaZ2gaYUrNynedJb7QLEl5eBZUhuia1uH74w/640?wx_fmt=png)

通过前面获取的code值可获取所有人员的家庭住址。

![](https://mmbiz.qpic.cn/mmbiz_png/pOOKGW9VicEocpROtyRzdFEUkj9pc2j2ULv0eyffxpqtapHicPaYE7wOvFbYx1rsho3iaOZyAFBKLcR5PzkAm9oeA/640?wx_fmt=png)

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

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