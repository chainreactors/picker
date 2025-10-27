---
title: ssrf挖掘利器
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496683&idx=1&sn=c39bd8f48193f4180671637c0d19589a&chksm=e8a5f988dfd2709ebb89d822b2ad981378c28bdb9a37c2e0172e5efa0dd07bc08cc78b60801c&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-27
fetch_date: 2025-10-06T19:38:29.151761
---

# ssrf挖掘利器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4qUxrGfdic0yBf3BBnkdUJ6fOcz2icicLAGCZREicHcYcNKZAzXKVqbr2zSYLqnMzYdJ01jOP8IbGrxg/0?wx_fmt=jpeg)

# ssrf挖掘利器

迪哥讲事

以下文章来源于跟着斯叔唠安全
，作者跟着斯叔唠安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM71BddGyNDhcnRiaPT7QXjlY4LPZlr1kjTkctThFFtib9LA/0)

**跟着斯叔唠安全**
.

一个专注于安全资讯分享的家伙

**·引言**

    今天斯叔来给各位老铁推荐一个burp插件，个人认为挖掘ssrf漏洞的效果很给力。

    你以为我是给你推荐这个项目？

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8UGwHjsHRuCp5Bqyr58vcYEdwmE6lt3m59ZLbWU5IphCgyEGlVb6sGRg/640?wx_fmt=png&from=appmsg)

    no！no！no！这个工具固然很好，覆盖面很广集成了100多种可能存在ssrf的场景，但是也正是这个原因，他会给服务器发送大量的请求包，很容易导致我们的ip被封禁，因此不是我们今天的主角。

    We need 一个小巧的，不容易被发现的，扩展性更强的替代工具辅助我们的渗透测试工作内容。为什么这里加上了扩展性更强的特点呢？众所周知burp增加插件的越多越有可能影响工具的性能，就像这样。

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8UiaibFLvZB9NkkNR0icmLQWUNJCH7tFxw5tAqt0tbRSHRPEsNdGNlibIzNQ/640?wx_fmt=png&from=appmsg)

    不过到底有多影响性能，就不得而知了，但是大红色的高度预警看着总归是让人心有余悸的。

**·show time**

    不多说了，让我们先来看看今天的主角界面长什么样子~当当当当

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8ULkxWIV3icicNvd0lPtXXvYvTZuNKK3l1KcicphnJHv6rFuicyiaeiaUScmMg/640?wx_fmt=png&from=appmsg)

    整个插件的界面被分成了四个区域，左上角显示的内容是匹配到规则的url情况，右上角是自己设置的匹配规则内容，左下角和右下角是显示的查看左上角url的详细报文情况，主要分为原始报文和修改报文。

    这个工具的原理其实很简单，就是通过自己设置的规则（一般是正则表达式），然后匹配burp的代理流量看看有没有匹配上的内容，如果匹配上了就自动替换成想要替换的内容。

    至此思路就清晰了，我们正常测试ssrf的方法是让目标应用向 dnslog 发起请求，然后通过dnslog记录帮助测试者判断 SSRF 漏洞是否存在。那么这个工具的用法就是通过编辑正则表达式将匹配到的内容自动替换成我们的dnslog，不就完成自动对ssrf漏洞点的探测了嘛，然后时不时看一下dnslog平台是否有记录产生，躺着收洞。那么how to do？

    首先准备一个dnslog记录

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8UD1SxdaIXAItUQWLvPnuouQbJ6mHnj33IUnkwsK9d6tRhCWpO2rUoBw/640?wx_fmt=png&from=appmsg)

    再准备两个正则表达式

```
(?i)^(https|http|file)://.*(?i)^(https|http|file)%3A%2F%2F.*
```

    然后点击插件界面的添加按钮tpye这里选择Request Param Value，Match部分填上我们的其中之一正则表达式，Replace填上我们的dnslog地址，前面可以跟上ssrf1这样的前缀，用来区分是哪一个正则表达式触发的漏洞，which选择Replace all，最后填上规则的名称以及勾选正则匹配的按钮就完成一个规则的创建了。照着这个方法，创建两个ssrf的规则。

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8UicVTL1jhiahSLqy5wGOqNH5y9xa7yE8m43x3gtEiaib0c1yN2PqnkrrO5A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8UzO02EarJcnW7Sja5hT1ickziaibMqg5BekayicU1LLVONicVv7mrPQF5NoQ/640?wx_fmt=png&from=appmsg)

    创建完规则之后就可以正常测试了，只要时不时观察一下dnslog平台就行，坐等ssrf![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_45@2x.png)

    附上一个斯叔做项目上捡到的一个ssrf给各位老铁冲喜。

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8UI9x5qaicoAp4hibDAuDtrIu69rYEpzyn8icxLHLfkcCsibrIWrYcQBNVDA/640?wx_fmt=png&from=appmsg)

    当然斯叔只是介绍了这个工具的其中之一玩法，可以看到在type部分能匹配的内容还是很多的，所以也可以用他来做例如未授权，越权之类的测试。

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY97LGHmGvibmib9p85tbxo8UeXJrC4dxNiavtAibv1HqGU5ldkFVrFlQPywWwt9VtkE9VCuYHcXuJWbQ/640?wx_fmt=png&from=appmsg)

    更多玩法等待老铁们的开发，赶快应用起来吧~

**·END**

感谢各位老铁的支持！工具获取方式可后台私信斯叔，私信暗号“ssrf工具”。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

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