---
title: 从JS代码审计到GraphQL利用的管理账户接管
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496534&idx=1&sn=493cff035c6dde66c5b31d96de6f3834&chksm=e8a5f935dfd270237e7b42da910e0224b5439e203ff4fc5b2b4f02e4594d10e5e1c81cc20aa3&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-07
fetch_date: 2025-10-06T19:40:36.580127
---

# 从JS代码审计到GraphQL利用的管理账户接管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj6PicZbVR3akBp2ggo4Aufu6anRNsdoXfENL13ktgXFJicCArfedTvFlNbHeIAHfAHQOWlSx3tk5gxQ/0?wx_fmt=jpeg)

# 从JS代码审计到GraphQL利用的管理账户接管

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

通过前期信息收集，发现一处登录页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PZe7wzs3lcctLpdFIbZ6BID72KJ04PErUJM8c0EypvEYj9HjXlJpAPw/640?wx_fmt=png&from=appmsg)

只有登录，没有注册、忘记密码等入口。

那就试着对端点进行Fuzz看看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PrMnib6yicMW166bCYyZLjy2guxicIiayibsreb02tAAJ37CtnHqbYYFCwhg/640?wx_fmt=png&from=appmsg)

然后将登录请求替换为注册看看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PExN06cS9uN9c8KdrAtZaxsJY1ff5MvO5wG4pBaIq1n7pR5dgVAe8bg/640?wx_fmt=png&from=appmsg)

失败。

查看Wappalyzer插件会有什么启示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3Pib4SQZygOcpum7c3xXzdKSKRdlVQYcibOLTu5jziahqgJXpZXAE5eZjrg/640?wx_fmt=png&from=appmsg)

有 GraphQL、React、Next.JS，要知道GraphQL通常很容易受到逻辑漏洞攻击，但发现这些漏洞并不容易，往往需要 JavaScript 的动态调试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PxibyzmvWnzHsdkuN2icuQY7vMaB4LmbJm1ctpmia9CgBZLD3Hib5TUJpjg/640?wx_fmt=png&from=appmsg)

在控制台仔细查看后，可以看到认证过程中的 GraphQL 错误，React 与后端之间也是照常进行交互。

那么只能尝试从 JavaScript 文件中“翻翻”了。使用`user` 关键词进行搜索：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PIMKCENaPeib0gOlTdZxjicEheswjVjvC1icXWiaX7aH7wWMyEgxIX7VZ2w/640?wx_fmt=png&from=appmsg)

找到6个JS文件，尝试使用`login`关键词进行搜索：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PgkCyvB1oo3ibW4nGm9zib3DUcSLicnAe8lHSrGuqTdADNqgyiaMqQLQGNQ/640?wx_fmt=png&from=appmsg)

发现 2 个 mentula 文件：

`next/static/chunks/pages/users-b48829712ecbd6a6.js`

使用 `JS Beutify` 插件查看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3Psj7fDxicONYmrkBSMUAbuK0ia1nUw28HRnFP93KyzySOAaTUibUhYuV0A/640?wx_fmt=png&from=appmsg)

对代码进行反混淆后，再提交给 ChatGPT 进行审查，然后编写所有可能的 GraphQL 变更和操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PAcvic6XzUgyUErpP9ndlDmDhBEh810Inl5sGPChZIy2chCd0p1ictRsA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PAcvic6XzUgyUErpP9ndlDmDhBEh810Inl5sGPChZIy2chCd0p1ictRsA/640?wx_fmt=png&from=appmsg)

再次将尝试添加用户并测试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PYLrUTK4aDvwWLmEoeMZJjuPTG9M6picicrs5391RETaQeUU354DpZrog/640?wx_fmt=png&from=appmsg)

通过报错信息，发现是由于用户角色为 ADMIN 而非 Administrator：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PzXm5NnicfFWx5kiaXVjMvRpKw3JGWZXvtPETrkhuhaFbYYichUwXyejicw/640?wx_fmt=png&from=appmsg)

将角色修改为Administrator，再次测试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3PUibMXBibicI95wZzAInqQoJicQQ76V4tALHibf93wIO96crn0eXU9ibdg5LA/640?wx_fmt=png&from=appmsg)

Nice！成功添加管理员账户，登录管理面板：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jl3OWfpE2HnPNH3LIqqAS3Pql2qOibWZ5ULxwtjBMialxLDtEk6s5x5o9KkiaV5CJ1DKuB3DIITdqribg/640?wx_fmt=png&from=appmsg)

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

以上内容由骨哥翻译并再创作。

原文：https://medium.com/@0xbugatti/js-review-and-abuse-graphql-result-10xbac-admin-panel-ato-0f013fe471ea

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