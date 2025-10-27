---
title: src挖掘-记一次幸运至极的验证码绕过
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497199&idx=1&sn=f18245b4024971419364704fcb258f76&chksm=e8a5ff8cdfd2769a89f54c88ba93bdaa03a48bc20365f015efc98f216640e792036859f82649&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-03-01
fetch_date: 2025-10-06T21:59:46.859788
---

# src挖掘-记一次幸运至极的验证码绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7ulA3MeJl72HUMpjT16XGBcxCmLwIgZAxkQEeR9hNCvJsydYxhDmz3EKWMYibfZqclelKNqeRL63g/0?wx_fmt=jpeg)

# src挖掘-记一次幸运至极的验证码绕过

迪哥讲事

以下文章来源于剑客古月的安全屋
，作者月金剑客

![](http://wx.qlogo.cn/mmhead/dibCvqHg4WncsYKQOO8N6HULUqdiclOBngrrMRcia94YODoKo1RdGLzdaGhqoSxXPWDz2g0yZG2Ewk/0)

**剑客古月的安全屋**
.

本科在读，目前大三。曾在多家甲乙方大厂实习。技术栈：移动端(安卓IOS鸿蒙)攻防、web端爬虫、风控、空间测绘与抗测绘、web端基础安全攻防、渗透、安全开发、src挖掘、代码审计、免杀，LLM大模型(NLP，CV)

🌟 ❤️

作者：yueji0j1anke

首发于公号：剑客古月的安全屋

字数：552

阅读时间:    3min

声明：**请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。合法渗透，本文章内容纯属虚构，如遇巧合，纯属意外**

**目录**

* 前言
* 绕过过程
* 后记

## 0x01 前言

最近挖洞比较少，基本每天挖洞时间都只有一个多小时，剩下的时间都在搞一些看起来"高端"的东西，属于是没事挖洞出来解解闷，这里也就当水一水文章了。

## 0x02 绕过过程

逛着逛着主站的小旁站，随便点了点验证码，f12看了看接口

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW1Dw4AEniaKUkx139W58MmlSwa9EA4QvDrsibQWXTmqt6JCktpD66spVveg8v7xsictgYfBUMYdPqzCQ/640?wx_fmt=png&from=appmsg)

发现惊喜

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW1Dw4AEniaKUkx139W58MmlSLMr2njM5HUiarQicodw2PhAbKjvl68M7zYGYcARrf3rtz8pLSdMRNSfg/640?wx_fmt=png&from=appmsg)

验证码回显但又加了密，属于薛定谔态，可能之前存在验证码回显但被修复过

这种密文大概率是aes加密，赌一波前端js存在解密或加密函数

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW1Dw4AEniaKUkx139W58MmlSplP0Bt41Fuyn0OSVsYo6dQEWFh8KxUe6RAA4icGHvJKRycgtUNm0cBA/640?wx_fmt=png&from=appmsg)

别说，还真让我找着了，但加密的密钥是通过请求并进行二次混淆不可逆加密了，反复debug了一下发现每次请求的密钥是不一样的，数据库端那边加密的密钥应该也是在动态变化...

走到这步来了，确实心有不甘，尝试拿域名去看看密钥...

![](https://mmbiz.qpic.cn/mmbiz_png/wF30Z0OMuW1Dw4AEniaKUkx139W58MmlSf1QalcRxsW0WAsIOETMN3XdiaTIYialic3k2cjJZUIV6j91EKRUia4R78A/640?wx_fmt=png&from=appmsg)

......

赌狗赌到最后应有尽有

可利用这个逻辑进行密码加密和code解密发送请求包，造成账密爆破风险漏洞

## 0x03 后记

目前遇到过的站点大部分验证码基本都不回显，即便回显也是层层动态加密...所以在这里发一篇水水文章，真的是幸运至极的一次绕过了。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips‍](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

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