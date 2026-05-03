---
title: AI 复现Copy Fail漏洞的一些思考？学了这么多年渗透/代审，会被 AI 一波带走嘛？
url: https://mp.weixin.qq.com/s/GuO9857kVnqYoaVMzrY3-w
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:25:37.851238
---

# AI 复现Copy Fail漏洞的一些思考？学了这么多年渗透/代审，会被 AI 一波带走嘛？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VFFHdyJNWPnt2gu0UYibfeNNRLw03PLqiajZ6tvav0ZICfROKre72HVvqAta7cT17FxTfL9BnrOoyVD5gJP2DlPxvRXR9zcIqPn3bs1AEp4Ec/0?wx_fmt=jpeg)

# AI 复现Copy Fail漏洞的一些思考？学了这么多年渗透/代审，会被 AI 一波带走嘛？

原创

润霖@闪石星曜
润霖@闪石星曜

闪石星曜CyberSecurity

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

近日，谁不想当剑仙@yhy0 师傅用 DeepSeek 复现了AI发现Copy Fail提权漏洞的过程——CVE-2026-31431，一个潜伏Linux内核近十年的逻辑缺陷，732字节Python脚本就能直接拿到root。

复盘中有两句话像钉子一样扎进脑子里：

**"AI是能力放大器。但放大器接在零上面，输出还是零。"**

**"真正稀缺的不是算力，不是参数量，是知道该问什么问题的那个人。"**

这个洞怎么来的？研究员Taeyang  Lee之前搞kernelCTF时盯上了AF\_ALG攻击面，怀疑AF\_ALG+splice的组合有鬼。但crypto子系统6万行代码，人一个个看根本不现实。于是他给了AI 精准 Prompt——锁定攻击面，划定方向——然后AI用一小时穷举，把洞刨了出来。人给了5%的方向，AI补了95%的执行力，合在一起才把潜伏十年的0day曝光。

[CVE-2026-31431：我用 DeepSeek 复现了 AI 发现Copy Fail 提权的全过程](https://mp.weixin.qq.com/s?__biz=MzkzODIwMTIwNg==&mid=2247485268&idx=1&sn=6f0beea01bb8febfbb6d15277c5a43cb&scene=21#wechat_redirect)

### 放大器接零，输出就是零

很多兄弟把 AI 当甩手掌柜。丢个jar包进去指望它标出所有RCE链，丢段代码进去指望它精准定位每个注入点。结果？它告诉你这里有JSON.parse()，但分不清那是不是被业务逻辑封死的伪漏洞；

它告诉你存在反序列化入口，但说不清那个版本的Shiro用了什么加密、有没有二次验证。它说有洞，你就只知有洞；它没说，你就真以为固若金汤。这种盲信，比不懂技术更危险。

Copy Fail的发现者能挖到这个洞，是因为他做kernelCTF时积累了对AF\_ALG攻击面的直觉。没有底层功底，"该让AI往哪跑"这句话都说不出来。给一句"帮我找出所有漏洞"，跟让实习生自学成才没区别。

**方向感，来自你大量的知识储备。**

### AI赋能的底层逻辑是相通的

所以回到渗透测试跟代码审计上，AI到底该怎么用才算真正赋能？

**第一，把底层知识焊在脑子里。** 不懂SQL注入的拼接原理，你驾驭不了AI去生成真正能绕WAF的变体；不懂反序列化链的构造逻辑，你没法指挥AI去梳理几十条gadget之间的调用关系；不懂XXE的防御边界，AI审查XML解析配置漏了东西你也看不出来。底层功夫，是你给AI指方向的底气。

**第二，敢试，但带着方向感去试。** Copy Fail的发现者是人先锁定了AF\_ALG攻击面，才让AI去穷举crypto子系统。放在代码审计里也一样——你得先知道目标系统用的是Shiro还是Fastjson，先知道哪个版本的哪个模块最可疑，再把AI的算力精准地打上去。不是"帮我审这个项目"，而是"这个模块用到了1.2.47版本的Fastjson，autoType默认关闭但我怀疑存在绕过路径，帮我排查相关调用链"。在此精确度上，我们可以继续补充方向感，也许你就能挖掘更多属于自己的0day!

**第三，让AI把你的效率放大，而不是替你思考。** 那些搬砖的活儿——写注释、做版本比对、整理报告、生成payload变体——AI能帮你省大把时间。但判断一个洞到底能不能在业务场景下打出RCE，判断AI说的是对是错，这些事永远需要你自己的脑子。

### 答案不是等出来的，是走出来的

Copy Fail这件事，撕开了一个扎心的现实：真正稀缺的从来不是AI的算力，不是模型的参数量，而是那个"知道该问什么问题"的人。研究员Taeyang  Lee用了近十年积累的攻击面直觉，加上AI一小时穷举6万行代码的执行力，才让一个潜伏近十年的高危洞见了光。两者的合体，是现在真正的降维打击。

**与其在AI时代焦虑的不知所措，不如主动上车，边走边摸索AI。**

技术这玩意儿，早动手早摸透，红利永远留给第一批下水的人。

那个"知道该问什么问题"的人，凭什么不能是你？

如果你也想让AI赋能自己，把这种"人给方向+AI赋能"的实战打法真正嵌入渗透测试和代码审计的链路里，不妨随我一起，从Java代码审计开始，把刀磨快。

关于我的AI Java代码审计实战课程详情可点击下方链接，给自己一个契机，从这开始！（课程还能白嫖~）

[【闪石星曜@ AI Java代码审计课程】如何让AI成为代码审计的超级外挂？降维打击？](https://mp.weixin.qq.com/s?__biz=Mzg3MDU1MjgwNA==&mid=2247487725&idx=1&sn=47f08543e5769f01bf06f5dcce86b947&scene=21#wechat_redirect)

[如何白嫖？？？闪石星曜@AI Java代码审计高阶实战班，一次付费，永久学习，一对一指导，还能狠狠的白嫖！](https://mp.weixin.qq.com/s?__biz=Mzg3MDU1MjgwNA==&mid=2247487786&idx=1&sn=f2ab85abc18afc9027e140ff2624f782&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FFcgFn6WVc0LkDlyV7kOhQCK3lPFFpoiaR90BC70DWJc4gnxzDXaic02Wo3pCiaOicZAVHGhkvaTCfj0ichz5hBiaG7g/0?wx_fmt=png)

闪石星曜CyberSecurity

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FFcgFn6WVc0LkDlyV7kOhQCK3lPFFpoiaR90BC70DWJc4gnxzDXaic02Wo3pCiaOicZAVHGhkvaTCfj0ichz5hBiaG7g/0?wx_fmt=png)

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