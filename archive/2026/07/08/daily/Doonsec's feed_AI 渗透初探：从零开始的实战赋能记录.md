---
title: AI 渗透初探：从零开始的实战赋能记录
url: https://mp.weixin.qq.com/s/YuTWMWHyJr_GlL_Y52iffQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:56:33.470350
---

# AI 渗透初探：从零开始的实战赋能记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RBe5hMcdh0OuwrOufYXvU79u5Hibwd9t94o8HhiciayicHFbeOOnCYrDwBgSxHcwMneyKreP4micOsRgYvuPGKfZUwu49fyzBM5icyria42Ph5QnM8/0?wx_fmt=jpeg)

# AI 渗透初探：从零开始的实战赋能记录

福Us1r

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于月的造梦星球
，作者月

![](http://wx.qlogo.cn/mmhead/ibkKkoaQFco5pQeXibaCYf7M9wfmBa82WiaGBGtUbYqyWNIX7E2fPhbjCYr9qlfUV2UHWZElnmEdpI/0)

**月的造梦星球**
.

临渊羡鱼 不如退而结网

## 我的AI测试方法论

      我并没有对`AI`做过深入研究，更多是在实战中慢慢摸索出一些提效的小思路，主要用来简化信息收集和业务理解的时间。大部分场景下，也就寥寥几句`Prompt`，用来梳理业务逻辑、提取全量`JS`接口、扒路由表，以及做接口参数追踪和`Fuzz`构造。

       初次渗透时，我会先让`AI`宏观地去收集网站的整体信息架构，尽量发挥`AI`本身的渗透能力，同时给它设定好行为边界和明确目标，让它在规则之内无限推理。与此同时我也会同步进行人工测试，一旦发现可疑的攻击面，再引导`AI`针对性落地测试，效果往往更好。尤其是接口参数缺失导致的未授权访问和信息泄露这类问题，AI的识别效率已经远超人工，`JS`接口的追踪能力更是堪称恐怖。

       再懒人一点的打法，就是创建场景化的`Skill`并设定好边界红线。以登录框为例，其实可测的点非常多：经典的`JS`接口提取加爆破、业务接口`Fuzz`、响应字段`AB`复用、`Vue`路由守卫查找、`React`路由表查找、空白页面的`base`地址探测……黑盒测试下，只要自身的攻击思路越丰富，写出来的`Skill`就越细致。这种方法对我来说，更像是把自己的经验蒸馏成可复用的逻辑，而不是简单地套报告模板，本质上是把测试`Toolist`完整走了一遍。虽然这样会限制`AI`的泛化能力，但好处也很明显——不需要过多干涉，给个域名就能无脑完整跑一遍 (

### 设定边界行为

    边界可以用法律来形容，禁止去踩红线，去越过红线，在这一点，`AI`渗透，攻防是必不可少的一步。我们可以去写一个`prompt`，比如客户下发的攻击方手册当中的**攻击方行为规范**这一部分内容（做好脱敏），去写成`prompt`，去约束他做一些测试

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0PFILGtpqj2y7r9YwQlkoBqV9mcC3EAz35FZoShNXHje84pjj5DuqpDgRjoxic54YjXE04ZQibhj7icse7W0Byhgkco80RXkKKiaick/640?wx_fmt=png&from=appmsg "null")

     也可以去利用上述思路做成一个`skills`。如果不知道怎么写`skills`，可以将**约束思路**喂给`AI`，让他去写一个`skills`，然后自己去审查，看有无漏掉的东西，或者未做好约束的部分，然后循环往复的去解决即可

### 设定一个目标，规则内，无限推理

此思路来源于前段时间**腾讯云黑客松智能渗透挑战赛** 当中的某位师傅的作品：**Cairn AI**

作者：淚笑，大家可以去关注他的公众号去学习

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0MkhMvfjGFgZovt9Df2VT6OgADeTXJm4UictW2Nfonu9lDp2XXtUWEhXYibX5wOEEKkI0iaS69SvLUTewnml9BHBVBYO6siaWvJYSY/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0Ota75N9Im9TuIbjGkGwBe7pG134Cg0z3Ac6Q4lM8MN4xB8XFYj1chowwlpLfnw1yRo35YA9fIeNXgydPaBvHjxRF2tLBJfBNk/640?wx_fmt=png&from=appmsg "null")

   他的一个大致设计思路就是：给出一个目标，给出一个任务，然后无限去推理，最终达成目标

   当下，我认为大部分模型的推理能力去做渗透已经完全够用，`AI`的思路是丰富的，所以，在测试过程中我们不必去给他去说怎么对一个**点**去进行测试，而是给他一个任务，给他一个目标，去做出一步步的推理，最终完成目标。

## 非预期漏洞挖掘

    对应标题，什么是非预期漏洞挖掘？一个点，在我们进行人工测试之后，然后就得出结论：渗透结束，非常安全！现在有了`AI`，我们就可以做到：人工一步---->`AI`一步---->人工判断---->分析总结，但在`AI`这步往往能发现更多人工没有注意的信息，再配合`AI`本身庞大的知识面使用部分非预期方法对设立的目标无限推理直至完成

### `code`报错导致接管

通过对资产进行信息搜集拿到一个小程序,功能点需要内部账户才可使用，尝试对小程序进行反编译，获取`page`路由和接口

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0OI0WrA357Sz2sdtrBBQHE7uc25zg1OoZ1ibNxYfVgygv0icOBPzwMulyl3lnRX2pfibVcBITMrKrVvQgNjyGLiaic5MzfgaGrnrHes/640?wx_fmt=png&from=appmsg "null")

拿到源码后对泄露接口进行审计分析，发现此接口`/wechat/miniapp/getTokenByWechat` 对业务敏感的师傅一眼可以认出这是拿到某个`token`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0Oa5cDT9nfPUspJO4Zb3lGibib5zhZ2GXEkvyx3OXIo1Rx26WvVyT1ZDMpJQlF8OmgXGBkJuSwJTfRYhQiblMyDrIURyOGmwsFYKc/640?wx_fmt=png&from=appmsg "null")

通过`AI`进行源码审计，寻找`Base`地址构造接口和所需参数

`{"appid":"wx4eb5","code":"xxxxxxxxxxxx"}`,人工该接口值进行模糊测试，但无果

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0NmMIOdtYLBteDOTkrmquEMlqPG9r78iaIB57Xaggt1Tyr2JXsf7WLb47FrzLR5Hibksw6UmlnqvuPE9W8bOt7iauAr1mntMzZR5M/640?wx_fmt=png&from=appmsg "null")

最终交给`AI`做模糊测试提示词目标是找出可用的`code`值获取小程序`token`，`AI`将`code`改为：**`x\n\r`，**类似于让某个参数后端报错**，最终获取**`access_token,secret`\*\*

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0PU9WSCRIP5xMlHagG19758tL0B6CHVhbuibzR73lWdHKSAAa9r1hFX7GAdLEMM8FwfJGFy6uflxfjuTnQBVfu0JlrS4BTxHbNM/640?wx_fmt=png&from=appmsg "null")

后利用深情哥的小程序`access_token`测试工具，进行测试,证明`access_token`有效，从而进行小程序接管，我原以为会正常按`fuzz`思路找出正确的值从而接管，但它却另辟蹊径通过报错来让目标达成，使用了非预期方式达成目标

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0OWzQY8ZsemQ6HcMxQw9BAGj3KXp89KKRNgAjLlUyJnVf12lGlCZqrrHcX6Ieh6MYdzhuKe2hxgxhbsq0iaSNrKNSbpSZfpyvRM/640?wx_fmt=png&from=appmsg "null")

### `credentials`认证缺陷接管

某个`Web`系统，经典的登录框，无注册口，无凭证，通过`AI`进行庞大的`JS`搜集，接口清晰与与测试处理，检索此接口 `/auth/oauth2/token`，以往对该接口的了解，是`oauth`登录获取`token`的接口；该接口往往在之前测试，我的知识面下，我只了解于`oauth`的`1click`劫持`code`与`state`打到的任意用户登录。但将此接口提示给`AI` 它则有不一样的的理解，给出非预期知识（对个人而言陌生的知识）

```
Oauth2有四种授权模式：

password

authorization.code

client.credentials

inplicit
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0NOiawrCFYuboUPy8SwQoadas0wWjlSVv8fruQa87Z0SbzgJGqePE0hkBZiaibVj22gbMTQsmyrJgEuB1iazD18ntZDSKvLztw4CqE/640?wx_fmt=png&from=appmsg "null")

其中第三种`client`.`credentials`模式，由于其本身可能存在缺陷，他是一种服务端对接服务端的一种授权

> `client_credentials`模式关键特点：不需要用户参与，客户端自己就是主体。拿到 `client_id`+ `client_secret`就等于拿到了客户端身份，可以直接拿 `access_token`，而`client_id + client_secret`，往往在系统当中存在弱口令

通过传入指定的授权模式，比如：`grant_type=client_credentials`,然后对`Authorization`进行 `client_id + client_secret base64`编码后的内容爆破弱口令测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0N33glBk36mAWw1ibHrDM1jZW4WUK267hz58bMZM3ibdnqiazicCRZyPMoW3OzAGQibtymvOnmgLyDVKiclvbkgK4iaibGnJLyT5icYAltk/640?wx_fmt=png&from=appmsg "null")

通过后续给出的知识发现，`client_id + client_secret` 一般都是默认对称的，比如`app:app`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0PsUg7qU7XbOYvnGSuZUPFnic7SeGMDibP9MxG1GNyCdtKGEibxqOLgpWFQOJYpKkWicqcPfbUjichGicSTY6fqrK8Q2icibhpnzyTxqXA/640?wx_fmt=png&from=appmsg "null")

既然是通过弱口令经过`base64`编码过的，在此攻击面上让`AI`批量做成了一个弱口令字典落地测试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0OxLN8bFy8ksQ6aupKQlEMqvmv0iaKIZLOnhtpDYE6C7634TodoLPQkGjCMCKTE6RkqESSQWYiaZjUbLSt45FrYqPibVp5DJSD5LM/640?wx_fmt=png&from=appmsg "null")

最终爆破成功，获取有效token

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0PG420nsJoHz9k8j3ricm1GOUFYiaRSOTZNib6QicIqFoSdEnpbGp4pACgneGKIF9Sh7a9niczdUCc3sfVhCUQ0sadpsu3qs12DZpsk/640?wx_fmt=png&from=appmsg "null")

利用获取到的凭证，复用到`JS`收集的其他接口，最终获取后台管理员账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0PvxvnUV2icBcZ9wKxYTJhRzxzXJSgaBsIZPgXicEd4Aab63vQMfDxEwpicLe7415HEv7AVqK4gZAUKhaSXKz8KrNuFg2xNwv6UFw/640?wx_fmt=png&from=appmsg "null")

由于该密码加密，`AI`调用工具解密（如`hashcat`），最终拿到明文密码，接管后台

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0PapiaBSkbtniblfW12UhVgcMJB88mCPw7lWYExq4AOhzC4HPZECOHqfhhbKQvtmCbCJLhdcfpjN0xAAVE7cT2OfcvGKgQu9DSxI/640?wx_fmt=png&from=appmsg "null")

### 存储桶原生端点`Fuzz`

设定目标无限推理,反复引导或者会挖出意向不到的漏洞, 正常文件上传至存储桶`cdn`地址，逐层删除目标发现桶遍历无法`PUT`覆盖 最初想法是翻一翻敏感文件提升危害

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0POy4JlRMDBza0IBf05EaS1muyMNEXqOT5PMGUpK2vgpRO0EJrm3q4librIkIdiaBfdplJbLF6eqY0ibMGDWP9Wibb8yBW5COdXyNQ/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0PYUr0VV44baBGQIeFVImvKozCibxUibnzsjyp8qlzTX17KiaJP10xYwGmLPpB3pkiciao0XCpkoSunNg7NtQknOiapv8zibdzL02GpRI/640?wx_fmt=png&from=appmsg "null")

使用一些存储桶工具想尝试进行翻页,发现均翻不过去,而后手工测试了一些常见的翻页参数\*\*`list-type=2`\*\* `max-keys` 均不可行，无奈丢给了`AI` 测试结果却出乎所料，我原本给的提示词只是翻页存储桶发现更多敏感信息泄露，最开始第一次尝试翻页以失败告终，但我仍是不断给出提示词，类如绕过限制，`Fuzz`翻页参数等等 `prompt`，因为当时我的想法是既然可以遍历`key`没道理不能翻页看，所以一味的让其推理尝试翻页，经过几轮提示对话最终`AI`给出的解释是此为`CDN`层存储桶，阉割`API`没有翻页功能,,

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0Og6vhm2aNLRRoUiawBMwNYX0pYJaNA63uzdDFzCERqzSR7XXKG2o0Teibrcu0Q7tOunoDG8eTFanpKk1qpE2CicLxzVfaCunKdWI/640?wx_fmt=png&from=appmsg "null")

戏剧性开始，在我没有继续给出下一步指令下`AI`仍将翻页功能作为目标尝试各种方式进行绕过，随即对该企业进行信息收集，构造三级域名做为字典碰撞，发现原生未被`cdn`分发的真实存储桶地址，在其后拼接桶名仍可以获取桶内信息并且可以正常使用翻页功能

```
cdn分发域名桶名为deliver
86c0d0f3e1ce0.cdn.xxxxx.com

未被分发真实桶域名,访问deliver目录内容和86c0d0f3e1ce0.cdn.xxxxx.com一致证明未打偏
sxxxx.xxxxxxx.com/deliver
```

![](https://mmbiz.qpic.cn/mmbiz_png/RBe5hMcdh0PfgVvh8cqhagRalB8hJz5tkBdCsJKc68Z5pnjj4XGj6xxhWRUeTNSicicibFhlnoeHAcJPWfpxdJDicanNbcibibrl3Elql1Tan8gtU/640?wx_fmt=png&from=appmsg "null")

到此并未结束，我们可以联想一下既然我们已找到该企业真实未被`cdn`分发地址，众多文件上传内容地址都会传到此域名下，只是存储桶地址不同而已，通过目录爆破思维最终发现挂载的更多存储桶

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0NjOtdRfEtR1yqjjXfhsPQ0RicC76YyMt76xXiafe2A94HiaDsR6tFiaDQhdE9SybO6ZObcT1qbsiaYzVrSfBd6UCNanPsCsUccT7gQ/640?wx_fmt=png&from=appmsg "null")

不出所料挂载了非常多的桶，逐一访问发现`metrics`桶下又记录了所有桶的访问日志检索出`200`多个桶地址，统一收集桶名作为目录反复进行`Fuzz`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBe5hMcdh0PDBKQWGLp9ofcvBE6Sf9aI2ibB0w74yrm6qH2DtKxKlbVePxjVT0y7fZGSZRticA6keJLE7KEOaMjK7BgzTbmw67KGYhLCRmZmM/640?wx_fmt=png&from=appmsg "null")

最终`AI`辅助测试所有桶总结敏感信息提交报告，后续复盘下来也算是误打误撞发现的，本身没有`Skill`局限某个漏洞类型，甚至提示词只是想办法绕过翻页功能，但需要刻意去引导`AI`往既定目标发散思维，不能让他偷懒，反复鞭打直至穷尽思路，但也不能盲目的对某一处死磕,那么受伤的只是自己的`token`，所以鼓励大家用`AI`放大攻击面，如若我没有桶遍历正常是可以...