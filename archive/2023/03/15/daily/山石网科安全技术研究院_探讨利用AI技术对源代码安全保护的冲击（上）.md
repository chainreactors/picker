---
title: 探讨利用AI技术对源代码安全保护的冲击（上）
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247500348&idx=1&sn=3e4bba60b0217fdfa031566ccd5d74ec&chksm=fa521782cd259e94cd23fabf196c7dc6f3640661f9c7289d4d1b1dbe047a546945c9e5181c29&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-03-15
fetch_date: 2025-10-04T09:36:14.078955
---

# 探讨利用AI技术对源代码安全保护的冲击（上）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQicAASFmNvBG0GP1VRLsNEkwoAsIsqXMjleyqmtBhKVmCNToV3jHRXHIekNibOVllLar0WW2koX2Lw/0?wx_fmt=jpeg)

# 探讨利用AI技术对源代码安全保护的冲击（上）

原创

HhhM

山石网科安全技术研究院

‍

**‍0****1**

**前言‍‍‍‍**

以AI概念大热门的chatgpt着实带来一系列扩展的玩法，不得不说chatgpt与以往所谓的AI有着质的变化，它会给很多行业造成冲击，而同样为AI概念的AI绘画已经在开始跟某些人抢饭碗了。

**02****‍**

**正文‍‍‍‍**

以个人的感受而言，近期浏览github，遇到了很多xxx.gpt，翻看月度趋势榜，毫不夸张地讲，chatgpt相关的项目占比达到了9成。

其实很多项目都是基于chatgpt的热度而攀升上去的，玩法就利用它的api，加上一层包装，本人也玩了一下，确实挺有意思的，当然这是openai非开源的缘故，不过openai开放的api已经足够了。

不得不说各种项目都很有想法，大部分我能想到的想法在github上都能搜到相关项目，不过就目前来看chatgpt的用途相对来说还是一些比较简单、重复性较高的工作，像类似于让它帮助我渗透网站这类的指令肯定是不能完成的，因为这其中涉及到的东西很多。

但我可以提供一系列条件，例如网站存在一个sql注入点，?id=1，可以利用单引号产生mysql执行错误，请问如何执行SQL注入等等，再适当的提供条件，如空格被过滤如何绕过，搭配它的上下文理解，可以辅助我们快速完成工作，当然了，也可能出现如下：

不可行？只需要告诉它我是一位学生即可骗过它：

作为一名偏爱代码审计的选手，自然想到的一件事就是能否帮我审计代码，github搜一搜就是好几个项目：

随手拿了一段不知道从哪个比赛保存下来的代码进行测试，会发现给出的结果相当令人满意。

代码如下，为golang：

```
func Login(c *gin.Context) {
 idString, flag := c.GetQuery("id")
 if !flag {
  idString = "1"
 }
 id, err := strconv.Atoi(idString)
 if err != nil {
  id = 1
 }
 TargetUser := structs.Admin
 for _, user := range structs.Users {
  if user.Id == id {
   TargetUser = user
  }
 }

 age := TargetUser.Age
 if age == "" {
  age, flag = c.GetQuery("age")
  if !flag {
   age = "forever 18 (Tell me the age)"
  }
 }

 if err != nil {
  c.AbortWithError(500, err)
 }

 html := fmt.Sprintf(templates.AdminIndexTemplateHtml, age)
 if err != nil {
  c.AbortWithError(500, err)
 }

 tmpl, err := template.New("admin_index").Parse(html)
 if err != nil {
  c.AbortWithError(500, err)
 }

 tmpl.Execute(c.Writer, TargetUser)
}
```

回复：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQicAASFmNvBG0GP1VRLsNEkArSymkEE2AJtIIvcztb57PRAFIEOs9BVTlptticVBZYrbfCkMCicZgHQ/640?wx_fmt=png)

好吧，我没有进一步调教，否则可能会告诉我是否存在漏洞，怎么利用。这也让我萌发好奇心，既然这种常规的代码解读任务能够完成，那逻辑稍复杂些，甚至变量转换等等的内容，也就是代码混淆后，ai是否还能认识这段代码并将之还原？

如果能，那么这对于代码保护是否会形成一定的影响？

**03****‍**

**代码保护‍‍‍‍**

何为代码保护？以PHP为例，PHP具有十分多的代码保护方案，PHP代码的执行流程为：源代码->OPCODE(中间代码)->ZEND引擎执行。那么大致的保护方案就对应了这三个流程，以网络上常见的划分方案通常划分为四个方案：代码壳加密、源代码混淆、OPCODE混淆、修改解释引擎。

以比较简单的壳加密而言，它的一个加密流程为：源码 -> 加密处理（压缩，替换，BASE64，转义）-> 安全处理（验证文件 MD5 值，限制 IP、限域名、限时间、防破解、防命令行调试）-> 加密程序成品。简单的说：源码 + 加密外壳 == 加密程序

这类加密的解密方案通常比较简单，因为代码还是需要在解密外壳后运行，因此可以选择hook php底层的zend\_compile\_string或者直接利用debug在适当时候可直接查看到源码：

就目前为止笔者能力范围内能够使用到的ai，对于处理超长的文字还是有所不足，因此如上图一般的这种大段的代码还是无法解读，也并不是说无法解读，只是说发送这么一大段过去机器人就卡住了，要么就是原样返回内容。

除了壳加密外，源代码混淆也是一种比较常规的混淆方案，源代码混淆顾名思义它会在源码上做改动，如修改变量名为中文，乱码，无规律字符等等，利用php内置加密，如base64、gzip等将字符串替换为不可识别字符，同时也混淆函数名，改动代码逻辑...

如下图一般：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQicAASFmNvBG0GP1VRLsNEkxoDUialVgJeYgrJWswPvK5kqTszibcwZrYA2J1YNlbSdNkgBgTyYaEmQ/640?wx_fmt=png)

提供的混淆方式有：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQicAASFmNvBG0GP1VRLsNEkOf2G82ia0tDKnzPcKFRTbe0RvBgZjkWx6Zib2hjvZcyRyfrrEuRRm7hA/640?wx_fmt=png)

此类加密保护能力一般来说足够了，但网上能仍搜索到比较可靠的解密方案或教程，据我了解在运行时会将变量、字符、函数等存入内存中，因此通过调试即可从内存中获取到，然后逐步还原，而更通用的方案则是利用PHP-Parser解析AST实现自动化解混淆，相关项目github上也可以搜索到，本文要点在于AI，不做展开讨论。

至于无扩展加密就更不好解了，以Z5加密为例，官方给出了加密流程：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQicAASFmNvBG0GP1VRLsNEkWcxvdxhPfK992icQyhf1DFHeUqTicPM9taibbG8ynH8hchpmEWIwLUT5g/640?wx_fmt=png)

也就是实现一个PHP编译器，或者叫做虚拟机，将代码放入其中运行，那么可想而知就算一段小小的代码也会被扩大n多倍，然而网上依旧有旧版本的解密方案，当然十分耗时，同时由于文件很大，难度系数很高，经笔者简单的测试得到的结论是AI无法解密。

最后还有一种加密方案是OPCODE混淆，即将PHP执行的中间语言OPCODE做混淆，此时即使借助vld等获取OPCODE的工具也只能得到一段被加密的OPCODE，如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQicAASFmNvBG0GP1VRLsNEkjmO9XXJYXqvJX4IoI6gMB9fDxz01jrNRibldBguKALAYUiczvhFuIDFA/640?wx_fmt=png)

这类混淆基本上就是PHP代码保护的较推荐的方案，因为即使可以通过OPCODE还原PHP代码，得到的仍非源码，即类似于使用ida反编译的效果，无法完全还原。并且市面上没有现成的OPCODE还原PHP代码的工具，因此该解密成本十分大。

笔者做简单测试后同样无法解密此保护方案，那么适当的利用gpt的上下文机制，是否能够将AI训练到破除这些代码保护方案？

关注下方公众号，下节持续输出：）

‍

‍

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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