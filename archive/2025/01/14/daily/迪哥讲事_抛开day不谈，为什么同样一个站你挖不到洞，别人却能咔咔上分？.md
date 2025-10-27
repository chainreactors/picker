---
title: 抛开day不谈，为什么同样一个站你挖不到洞，别人却能咔咔上分？
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496846&idx=1&sn=446f62009a5b4a78356459656e925b2a&chksm=e8a5feeddfd277fbb42bbd793665bc8de01733bf220a34f8ece1e83142823685a046f1dd4699&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-14
fetch_date: 2025-10-06T20:11:53.708453
---

# 抛开day不谈，为什么同样一个站你挖不到洞，别人却能咔咔上分？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7f51qBhHGIiagTr8CLMUomia0yH0HjWdWoSWFsvqPUdQPP9b5BD4uvqWq3oLxe0AKxErRXrtlrLUOQ/0?wx_fmt=jpeg)

# 抛开day不谈，为什么同样一个站你挖不到洞，别人却能咔咔上分？

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

今天不教技术，教方法论，方法论学会了，往往事半功倍。相信大多数刚入行的老铁经常会有这样的困惑，明明漏洞我都会，什么sql注入，xss，命令执行，文件上传啥的漏洞原理倒背如流，怎么就是挖不到漏洞呢？其实大都由于自身的漏洞框架没有搭建成形导致的。

一般来说，斯叔喜欢把学习web安全的前期过程类比成炼气期，筑基期，金丹期等等。炼气期其实也就是刚刚接触网安的铁子，可能会使用一些工具比方说sqlmap呀，菜刀呀之类的，但是对漏洞没有很深的认知，算是初窥门径，会简单使用所谓的黑客工具。步入到筑基期呢就是开始扎实打牢基础的过程了，学习了解各种常规漏洞的原理，利用方式以及修复方式等等。那么我们知道筑基期想要突破成下一阶段的金丹期，是不是得先内接金丹？在网安里呢，这个内结金丹的过程就可以看作是铁子们对漏洞进行整理归纳搭建属于自己的漏洞框架的过程。金丹期高手可以御丹弑敌，同样的，当你的漏洞框架搭建好了之后挖洞就会得心应手许多，更容易的发现平常不易发现的漏洞。

那么聊了那么多，这漏洞框架到底该怎么搭建呢？其实也就是把平时的挖洞过程分解成场景化的挖洞过程，文字叙述不易理解，下面上案例。

2

Action

登录框，相信经常打攻防演练的老铁并不陌生，给到的资产大多访问过去就是一个登录框。让我来猜猜部分老铁的一般步骤：试试弱口令admin/admin，admin/123456……没有弱口令；看看存不存在shiro，不存在shiro；用没用到其他存在漏洞的框架，啥也没有。Fine，next……然后发现又是登录框，又啥也没有，周而复始，逐渐红温。看看比分，what？xxx队怎么都那么多分了，一定是day，妈的，有day真好；或者一定是人海战术，人多真好。

那么真的是没day就挖不到漏洞了嘛？先然不是的。以下图为例，这是一个典型的登录功能点，假设它没有用到任何存在已知漏洞的框架，那么我们该怎么渗透挖洞呢？老铁们可以三秒钟简单思考一下可测的点。

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY8eibyoKUN81RbvCGe265pTSdPOv5pYu9jYjJ4hwSFYPLmrib8RleNGZW8BKZEd4urPR0IwPgibIhMA/640?wx_fmt=png&from=appmsg)

显而易见的这里出现的功能点有登录、注册、忘记密码，还有一个验证码，那就这么点东西能测的了？Are you sure？显然不，当然还有可以继续测试的地方，我们还可以看它的网页源代码，可能会泄露一些不为人知的东西例如个人敏感信息，注释了的账号密码等，不要觉得遥不可及或者不可思议，因为确实有这样的情况![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY8eibyoKUN81RbvCGe265pTvZdq6fVMCNLl8AtWvyl6mq3DtxBnNxJ5hewO2slzf8njgcy7w3uU4g/640?wx_fmt=png&from=appmsg)

当然，源代码里我们也可以去收集关于网站的接口信息，测试是否会存在一些未授权的接口情况。除了源代码呢？我们还可以扫描网页的目录，一不小心有可能就把网站的源码.zip给扫出来了也不是不可能。

通常来说，一轮又一轮的攻防演练，渗透测试，表面的漏洞（也就是目光所及的功能点可能存在的漏洞）已经被挖滥了，当然这并不意味着这些功能点就不需要测试，也需要测试，但与他人拉开差距的地方很多时候都是出现在那些你看不到的地方。

总结一下就是，挖掘漏洞之前首先要对自己进行测试的站点有个清晰的规划。这个规划需要尽可能全面的覆盖到可能存在问题的任一方面。那么我们知道了当面对一个普通到不能再普通的登录框的时候，我们有很多可供选择的测试方向：登录框、注册，忘记密码，验证码，网页源代码，网页目录。

大篇幅的文字看着容易犯困，这里上一个实战案例给各位老铁先提一下精神。

开局一个登录框，只有一个登录功能点，弱口令，sql注入测试无果。难道就要放弃了嘛？难道真的要放弃了嘛？![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY8eibyoKUN81RbvCGe265pT635fVaL9E1YVQ5r30ibf8uEevGR6OHa0YIe2RG2H4OPMfxkibibnKvnNw/640?wx_fmt=png&from=appmsg)

柳暗花明的转折点，F12打开网站源码，注意到了一个名叫config.js的文件，里面竟然清晰的罗列着当前系统的所有接口信息，甚至通过前面的英文变量名称几乎能够确定该接口的作用是什么。目光锁定到了一个adduser的接口，显然这是一个增加用户的接口。会不会存在未授权添加用户的情况呢？

![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY8eibyoKUN81RbvCGe265pT10gB7AIdWQo4STa5N6NZsRH4aZYREkFmBcWHTxn6zQQ2VNmX5LQYjA/640?wx_fmt=png&from=appmsg)

带着这样的疑问，访问一下这个接口，响应400好像没戏，再仔细看看，报错提示缺失参数。呕吼，有戏！![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY8eibyoKUN81RbvCGe265pTUbaNbOSZhAibMEyKictmy6aoJZulEWRlqI8YFuZJDdbsX9hPXzzlIiauw/640?wx_fmt=png&from=appmsg)

补齐参数，直接就是一手未授权添加用户。![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY8eibyoKUN81RbvCGe265pTibKPqzYeu8afJqRLmgUicJcvVZW7kcRt2sdPpyYibCJyujlBgyicJtrF7Q/640?wx_fmt=png&from=appmsg)

你看，这不就进来了嘛。![](https://mmbiz.qpic.cn/mmbiz_png/pKCicPnn24UY8eibyoKUN81RbvCGe265pT31QL50mibahzsp0cc64uDWibhjVdgyAfZIpQRXq84qnP6Pc03EJBmRsw/640?wx_fmt=png&from=appmsg)

言归正传，今天的主题是搭建我们那该死的漏洞框架，也就是将漏洞场景化的区分。其实呢这是一个日积月累的过程，通过不断的实践探索，得出xx功能点一般会出现xx漏洞这样的经验。当别人还在思考测什么怎么测的时候，你已经轻车熟路开始针对性测试了，这就是场景化测试的功效。

简单的例子，图形验证码能测些什么？

```
验证码复用验证码返回前端验证码伪随机删除验证码键值绕过验证码校验删除cookie/更改ip绕过验证码校验验证码前端校验验证码分布校验图形验证码大小可控导致拒绝服务简易验证码可识别…………
```

可以看到单单一个图形验证码这边就罗列了9条可测的点，思路清晰，这就是场景化挖掘漏洞的威力，通过对功能点可能存在的漏洞积累的经验，针对性的进行测试，而不是无头脑的四处乱撞，视野瞬间就开阔了起来。减少了盯着验证码测试xss或者sql注入类似的无用功消耗（可能确实会有这样的场景，不过一般不会出现）

同样的，注册功能点可以测试

```
批量提交（绕过分布校验）批量提交sql注入用户名遍历重复注册问题任意用户注册任意角色注册存储型xss…………
```

忘记密码功能点可以测试

```
用户名遍历（绕过分布校验）任意用户密码重置（重置密码链接可猜解）任意用户密码重置（未校验手机号码与用户的一致性）任意用户密码重置（修改用户id/用户名）任意用户密码重置…………
```

登录功能点可以测试

```
用户名遍历弱口令/空口令暴力破解暴力破解（限制绕过）万能密码sql注入反射xss多点认证缺陷前端绕过…………
```

网页源代码可以测试

```
明文密码本地保存未授权访问（源代码泄露接口）敏感信息泄露…………
```

网页目录可以测试

```
备份或测试文件泄露目录浏览默认页面泄露存在可访问的管理后台…………
```

可以看到当你开始面对场景进行针对性测试的时候，视野会变得非常的开阔，可测的点也会变得多了多。这里仅仅以登录点为例给各位老铁简单介绍了一下场景化测试的方式，实战中会遇到很多的场景，这需要大家自己平时多做积累多做总结，才能使得自己的金丹更大，更硬![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_45@2x.png)。

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