---
title: 一次意外的接口测试
url: https://mp.weixin.qq.com/s/6wofdUWFUzWy8PN03KpBww
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:12.014039
---

# 一次意外的接口测试

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7xtecWUgCRyhuFjpc6icbMvl5S1shzYyvZKksTUH19QDRF0OpYpSrmNOjFDhNqGoDQFeUoYiceTjzNEFibejALEZKvFjxvkYlTCiar7KX4xkqzM/0?wx_fmt=jpeg)

# 一次意外的接口测试

迪哥讲事

![]()

在小说阅读器中沉浸阅读

以下文章来源于安全无界
，作者pippybear

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6JYvuCl28ECxZCDXDhRa2ibX1JHic6ZC3MJrKD39y4W0IQ/0)

**安全无界**
.

面向年轻的网络安全爱好者，分享网络安全技术、工具和趋势。

声明：请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。

这是之前的一次授权渗透测试了，目标开局的默认页就是一个404，我都怀疑客户是不是没有把服务路由给到我。但是既然如此，也就只能如此。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVty7KIw6N6Hx01mnyfZ7wmJ4dP0Y3LeFaJJ9B1vibNrJ1PQt4xD1cb5x4Z7iczsQSicW3tnibKYLhDSE2lT4lvvdtJtsynjkT4icRE/640?wx_fmt=png&from=appmsg)

话不多说，直接开干，如下就是本次的目标。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPVOIV1Q7MLqI3j3dJ1polWjjE7exOGcA74PDv17ibUY7cPx68rDYn2oYoqpVQtyfXribzTNy8eXdMBm6YdrfMaUdZL80LYhFiaKWQ/640?wx_fmt=png&from=appmsg)

先直接使用dirsearch跑一波目录，看看有没有啥收获。很显然，开发老哥从来都不会负我，soap接口服务可以直接访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVBYLXBVqlgwoogLHwM9ZyVn55c8CKzTiaXMnfkduicxia8CuSvso3ff4k3zib5yqtZia0Ysvd0CiapA12tA1G8uQuPfdQMDxMWn22Kk/640?wx_fmt=png&from=appmsg)

激动的挫大手，emmm，这个可以使用soapUI来获取request报文，就是下面这个。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPUia2XiamPJ5WTEZzQGV5nice1lLgQqXBjEdGFS0D7M9366dk3aKwTe1OREUz76Btw8ZT5ujjkUvOlA09C0aaOR8WibtONYia1LjH3o/640?wx_fmt=png&from=appmsg)

当然也可以使用APIKit burp小插件哈，不过这个都是小问题，相信大家都会，这里就小提一嘴，直接开干。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPWtTqK6MYibLWp2gXn7dicJ7oh4bZnriaKTFHkbaAl5JoYQeSCe76Tf2U1KxxFXzwzGN9ELyleiag6usYgHKldV15u10eQSWJQpx3w/640?wx_fmt=png&from=appmsg)

小试一手，结果就有一个注入，幸福总是来的那么突然。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPUMrbCroD6zEicMhCOmBSPMUianD0njfV7YPJxhbpzMCzo8DzYQDmHImeVCdTVXJKxGibVo3R1DSmgB9WiarYZZUzRn0DsThELwRsg/640?wx_fmt=png&from=appmsg)

小小的试了一下，发现后端基本没有做啥过滤，那还说啥，直接使用sqlmap一把梭哈。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPXiaAt2A2MalA22UySVScOyiblOtr6Xiby2QSL0GG05Hkfx0dvyQub66FWTTibk6EeeoRiczuQMUibYsGO4AdQZw1NKYs34zuU0qe4UI/640?wx_fmt=png&from=appmsg)

嘎嘎舒服，果然还得靠开发大哥赏饭吃呀，类似的注入点还不少，这个先过掉，看看有没有啥未授权的问题。一顿人肉检索后，果然出货不少，不少接口可以直接访问，部分泄露不少敏感数据，如下。

![](https://mmbiz.qpic.cn/mmbiz_png/72I8gAalpPWMzbE5tdfsHSM9CEynqaPLEKQumrE0AqiaD4fqnmOEcP9wItKkTPUqvvxOjeZRawABI2SVjzAyCrrJKqR0m1udLsyQZbYnXBQE/640?wx_fmt=png&from=appmsg)

根据这个接口获取到的user信息，即userID信息，可以在另外一个接口获取用户的敏感信息，这个就不放图了，赶紧写完报告，交差。

如果你是一个长期主义者，欢迎加入我的知识星球，本星球日日更新,包含号主大量一线实战,全网独一无二，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

往期回顾

#

# [如何利用ai辅助挖漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497813&idx=1&sn=c778ad6a4bffd7a0a72a900144ea90ca&scene=21#wechat_redirect)

#

# [如何在移动端抓包-下](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497880&idx=1&sn=b9b980464333074216b55ea94c8a743a&scene=21#wechat_redirect)

#

# [如何绕过签名校验](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247497491&idx=1&sn=a1b00b9a8a54eb96aa3ba8bf23cb7e28&scene=21#wechat_redirect)

#

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[挖掘有回显ssrf的隐藏payload](https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496898&idx=1&sn=b6088e20a8b4fc9fbd887b900d8c5247&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)[‍](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

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