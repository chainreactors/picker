---
title: 一则SSRF漏洞的故事
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496304&idx=1&sn=2c8db754f88f6dcc2b2a31ce0784c1c3&chksm=e8a5f813dfd27105ffe5bb66e2b7b6b29c3acaa8ce510cc34d12a3298708abb33f91aa73efea&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-11-09
fetch_date: 2025-10-06T19:21:13.596997
---

# 一则SSRF漏洞的故事

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj4chmpLmjPCczQ6BLu1Ym542NZHJyYTUdEn2Iw9h2FbyNel80k3F1QjwkibBxCqgKLwBB8f5CfjQpw/0?wx_fmt=jpeg)

# 一则SSRF漏洞的故事

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

# 背景介绍

该项目为一个云银行平台，使银行提供商能够根据他们的描述快速创建、推出和服务贷款和存款产品。

# 漏洞发现

白帽小哥正在测试的子域有两个权限Admin&User，他们在这两个权限之中发现了另外两个漏洞，但他们对Process（进程）功能更感兴趣。

顾名思义，该功能允许用户创建一个或一组任务，在它满足用户指定的条件后执行，例如，在x等于y之后执行某件事等。

其中一项任务称为API调用，因此该功能值得对其进行 SSRF 测试。将任务添加到流程后，可以指定主机和方法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOA6WRHwtib8j9VO6cwzy0bgAuPHClFkHaujZlLKOl6gdcV7caOfDl7PQ/640?wx_fmt=png&from=appmsg)

为了快速测试，白帽小哥尝试了GET方法和(http://169.254.169.254)来获取AWS实例元数据，但得到的却是 403 Response：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOA0nqpdJt9Lsib2sDk7WzvZpSic64Hkxj6EZRgTIj1LoN2sXiaQTREcTPQ/640?wx_fmt=png&from=appmsg)

于是白帽小哥尝试了一些绕过方法，例如：

* 利用IPFuscator 进行IP混淆
* 利用redir6a将IPv6重定向到 169.254.169.254
* 利用rebinder的DNS重新绑定攻击

然后白帽小哥使用rebinder工具，通过使用169.254.169.254的Google IP，获得在2个IP之间解析的域名，并在API Call任务中使用它，多次尝试后，白帽小哥获得了第一个不同的响应：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOu5JquESjJByKXk1cIxX5a4LDs9B7MJq3q3x1bEaYlZVNRCL5pG2MhA/640?wx_fmt=png&from=appmsg)

收到的是401响应，但响应header里（server: EC2ws）表示访问了内部AWS实例，于是白帽小哥报告了这个SSRF盲注，但很快厂商拒绝了该报告（没有任何敏感信息泄露，无影响）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOdpzAzZUiaiccfY2BcicTENrLHibBKSiaWkGeem6GbMVOQttN5EljCoqF3qA/640?wx_fmt=png&from=appmsg)

# 再接再厉

三天后，白帽小哥根据文档：

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html

发现可以通过添加标头(X-aws-ec2-metadata-token-ttl-seconds: 21600)来获取令牌，从而使用返回的令牌和标头（X-aws-ec2-metadata-token: TOKEN）。

而且API Call任务允许添加自定义标头：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOzhOjserH2mL0sia7oqj9YFtnSLBbDwXjZVPILT3OaiaWLQ4IA0NV5Bicw/640?wx_fmt=png&from=appmsg)

通过rebinder尝试了新标头后，终于获得了200响应：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOBlVPcNP83IbIFVsSGrZlViaricntJiaNXwuUlSEI4K4WDwjiabWEAntgzQ/640?wx_fmt=png&from=appmsg)

然后使用响应包中标头（X-aws-ec2-metadata-token）的令牌：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOh5wVbz7KNE1VKia38pY7ECssx4AhrnxzkyJLQ5IknjcM11iaiagtiaJLvw/640?wx_fmt=png&from=appmsg)

成功拿到敏感信息。白帽小哥很快更新了漏洞报告，并提供了详细的复现步骤，厂商在对该漏洞讨论后的 3 天给出了回应：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3cFSxbgmibfS4QQYxK2DXOhyfhojRyV7v2BSRvl14XjgmaFSqJG8dgc711Z5XiaYfRUdhcyudyjZw/640?wx_fmt=png&from=appmsg)

白帽小哥在与对方进一步争论后，厂商最终决定奖励 500 美元作为回报。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

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