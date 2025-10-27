---
title: 再聊聊ffuf
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496528&idx=1&sn=a2b2c9736622abc268461d71e4f040d2&chksm=e8a5f933dfd270257349ab86803a8041d616fc38960c7d0351c8f0eadd4c16a676593468fdf4&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-06
fetch_date: 2025-10-06T19:39:44.161286
---

# 再聊聊ffuf

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4xzWcoEPcCALAtT8doRsJPEicicwRUKMEZNFW8ZZTfYnZIxEH30dvnJe7ciadDofpHR1rnKH5Cl7gTQ/0?wx_fmt=jpeg)

# 再聊聊ffuf

迪哥讲事

## 正文

昨天在群里看到有人发了一个图:

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4xzWcoEPcCALAtT8doRsJPhtHXXE4s21Yjia8wiaic46OHLiaHKjQMWPLuNjGS5h45Dy9sWwNFqDiaQMA/640?wx_fmt=png&from=appmsg)

比较好奇,因为和我前两天发的一篇付费文章讲解的都是同一个工具

说实话,学习的过程中难免会查阅一些资料,但是这篇文章我还真没看过

看到这篇文章以后，抱着学习的态度去看了一下,发现这篇文章的作者将ffuf很多技巧都写出来了,但是和我写的那篇文章完全不一样,怎么说呢,ffuf的github官方仓库里面有很多点只是轻描淡写地提了一下,如果说这个作者写的是github里面没有详细展开的part1，,那么我这篇付费文章-[**暴力破解的艺术-- ffuf的不常见用法**](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496510&idx=1&sn=301387411202a23df80e519fdae81d9c&scene=21#wechat_redirect)

写**的就是part2.**

**这篇国外的安全文章非常值得去阅读,后面我会给出链接,最后再次推荐一下我的这篇有关[ffuf用法的付费文章](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496510&idx=1&sn=301387411202a23df80e519fdae81d9c&scene=21#wechat_redirect),在实战中确实很有用（因为这篇文章就是我在实战中和其他白帽子交流中获取的灵感）**

**如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款**

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

## 参考

https://medium.com/h7w/ultimate-ffuf-cheatsheet-advanced-fuzzing-tactics-for-pro-bug-hunters-492598750150

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