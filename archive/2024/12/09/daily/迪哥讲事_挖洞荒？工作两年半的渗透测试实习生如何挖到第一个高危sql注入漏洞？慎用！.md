---
title: 挖洞荒？工作两年半的渗透测试实习生如何挖到第一个高危sql注入漏洞？慎用！
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496542&idx=1&sn=786c2ef243463b972253ad6ccf7dc2eb&chksm=e8a5f93ddfd2702ba5c86f55216742d9780d1504c5cf7b55d57e37f741241abc0f83e72d204d&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-09
fetch_date: 2025-10-06T19:38:10.476283
---

# 挖洞荒？工作两年半的渗透测试实习生如何挖到第一个高危sql注入漏洞？慎用！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj51GAhCmXAgeMribtOEQJo59rfec56K59ERekVYjCiar4ubfiaCPLnQTCAUTAtv4GNgJ8TJtLCZdQ6ibQ/0?wx_fmt=jpeg)

# 挖洞荒？工作两年半的渗透测试实习生如何挖到第一个高危sql注入漏洞？慎用！

迪哥讲事

以下文章来源于跟着斯叔唠安全
，作者跟着斯叔唠安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM71BddGyNDhcnRiaPT7QXjlY4LPZlr1kjTkctThFFtib9LA/0)

**跟着斯叔唠安全**
.

一个专注于安全资讯分享的家伙

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

1

Start

今天聊点歪门邪道。跟刚入行还是实习生的小伙子交流的时候经常会提到一个问题，就是刚从靶场转变成了项目，死活挖不到漏洞，明明漏洞都会，但就是挖不到。学安全的时候最先学的漏洞就是sql注入，实际项目中就没见过哪个系统有sql注入，想想也是，都什么年代了，怎么可能存在sql注入，预编译专治各种不服。

以上大概是实习小伙跟我吐槽的内容，其实也能理解，这种东西就能足球一样，你踢前锋位置，经常不进球久而久之自己就会对自己产生怀疑，这时候往往需要一个点球来打破自己的进球荒，重塑信心。同样的，作为攻击手的我们在遇到挖洞荒的时候，如何破局呢？首先声明，以下内容慎用，仅可在授权渗透的情况下使用。

2

Action

其实呢理清楚一个关系事情就明朗多了，点球这个行为无外乎两个结果，选对方向--进球，选错方向--被扑出。同样的我们在挖洞的时候是否有类似的情况呢，选对功能点就能出漏洞，选错功能点就没有漏洞？说到这里是不是觉得这个跟扫描器有点类似了。那么提到sql注入，你第一个会想到什么扫描器呢？没错就是sqlmap。

这里仅介绍斯叔的见解哈，仅代表个人观点。对于初学者而言，“我”并不知道哪里容易出现sql注入，哪里一般不会存在sql注入，对于这种情况，直接掏出sqlmap梭哈。

把每次扫出来sql注入的功能点整理起来，慢慢的就会知道什么地方容易出现sql注入了，当然，搭配代码审计食用更佳，用开发者的角度去看待业务，非常有助于渗透测试工程师挖掘漏洞。

言归正传，具体如何操作呢？

首先准备一个burp插件，将burp与sqlmap联动起来：sqlmap4burp。直接burp加载这个插件就好。然后一个一个功能点去点击，burp记录劫持的数据包，再将所有数据包全部用插件发送给sqlmap进行扫描。（这里用百度的报文为例演示工具的使用）![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UZl3iaYWqXdclOkSBfcR3icsfS2wpu5QdRXpF71Y5gcXe8A20XO0sZFCiaLLKF8JC6HHj5BMREIMibdDQ/640?wx_fmt=png&from=appmsg)

加载插件，配置sqlmap的地址以及参数情况，参数我一般喜欢--batch --random-agent，然后level5 risk3直接拉满，主打一个不出漏洞誓不罢休![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UZl3iaYWqXdclOkSBfcR3icsfYS1ADFcAzibEgGFTkaR07z3b8q6SCI057ffOKbHWLHg70guog88RKEg/640?wx_fmt=png&from=appmsg)

然后你就会在你的电脑界面看到这样的场景![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UZl3iaYWqXdclOkSBfcR3icsfIGnTUJeyxpSu5jCu0xFxKmuqvMOGRwCoibGxMxB6pibrY5icmic8P5kakg/640?wx_fmt=png&from=appmsg)

下面把舞台交给时间与运气，静静等待结果![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UZl3iaYWqXdclOkSBfcR3icsf9ryj8534ZkNA2W2PwmYlcrPC6EbPV1aER8GJmLJqMWfibib3EExDgibXg/640?wx_fmt=png&from=appmsg)

当然这个方法是有前提的，不是说什么场景都能用的：

1、首当其冲的就是需要是正规的授权行为渗透

2、需要对方服务器性能不差，毕竟在这个过程中需要发送大量的请求包的（谨慎使用，给甲方服务器干崩了就得让领导道歉了）

3、需要本身的测试电脑性能以及网络过关，也是因为需要发送大量的请求包的原因

4、最好是对方没有部署waf之类的防火墙设备，不然大部分情况下sqlmap的请求包都是会被拦截了的，没什么效果。不过一般作为刚入职的实习生不会交付太高难度的作业，这种场景还是很容易遇见的。

3

END

感谢各位老铁的支持![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_64@2x.png)如果觉得斯叔内容还可以，还请各位老铁动动发财的小手，多多转发，多多推荐哈![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_14@2x.png)。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[暴力破解的艺术-- ffuf的不常见用法](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496510&idx=1&sn=301387411202a23df80e519fdae81d9c&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

后台私信暗号“sqlmap4burp”，获取插件下载链接。

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