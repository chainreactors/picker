---
title: 如何黑掉Hackerone
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247494560&idx=1&sn=b4180bfa487b8cb6798d75a10ff60591&chksm=e8a5e1c3dfd268d587c0496816c5eb1c8b44beae3e405498e16bc6e3357653abc3e02cb8e1da&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-05-08
fetch_date: 2025-10-06T17:17:17.371752
---

# 如何黑掉Hackerone

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJJKiaJElS3ROs8XibBiaR9UBBwSo0Wj9gbxTtUG5TMLAjVCIdicrl2pAWqg/0?wx_fmt=jpeg)

# 如何黑掉Hackerone

迪哥讲事

以下文章来源于一个不正经的黑客
，作者一个不正经的黑客

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Ye8K1LdT6vUsuNeKr1S2DofpqlI98Xh2GQVibnXy64mg/0)

**一个不正经的黑客**
.

以黑客之荣耀，执0day之利剑，击溃所有的防护，势必划破无尽的黑暗！

# ![](https://mmbiz.qpic.cn/mmbiz_gif/bL2iaicTYdZn7YJ40j5Eya8ZwUTIgZwE6ANQC7LOyibH9gafBmice7coFucD5aodpJiam6td2SZ8zNpiaGUBToR9AumQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

**免责声明**

请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请后台告知，我们会立即删除并致歉，谢谢！

1

#

### 漏洞细节

这是我作为漏洞赏金平台上直接向上游提交重要漏洞的经历故事。

“Alhamdulillahi rabbil alamin”（感谢真主，全世界的主宰）无疑是我要说的第一句话！

这是我作为漏洞赏金平台上直接向上游提交重要漏洞的经历故事。

我是如何找到那些重要漏洞的呢？让我们首先谈谈基础知识。

你有 web/app 编程的先验经验吗？

当然你对 CRUD 是熟悉的！但如果你对此还不了解，CRUD 用于将数据处理到数据库中 [1]。

CRUD 代表创建（Create）、读取（Read）、更新（Update）和删除（Delete），这对于使用关系数据库实现健壮应用至关重要 [2]。然而，如果应用程序过于复杂，其背后的系统就不再是简单的 CRUD。

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJgn1uXibEZZBicsWnQD5xpot3rYx9Vx9Zce7UtGSMOCEoC9AvOiaLW1EfA/640?wx_fmt=png&from=appmsg)

CRUD（创建、读取、更新、删除）概念与发现漏洞相关，因为它提供了一种有结构的方式来与应用程序中的数据进行交互。通过了解如何创建、读取、更新和删除数据，您可以识别出应用程序行为中的潜在漏洞或不一致之处。

让我们更仔细地看看我如何应用 CRUD 基础知识来绘制一个菜单/功能的映射，特别是“报告”菜单。以下是它包括的内容：

* **创建报告**：识别创建新报告的功能。
* **编辑报告**：查看如何修改现有报告。
* **关闭报告**：调查关闭或完成报告的流程。
* **创建评论**：理解用户如何向报告添加评论。
* **编辑评论**：评估修改现有评论的能力。
* **创建摘要**：分析创建摘要的方式。

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJCMhaXbXGVL9eAicwC61IHicvy4ks2pdCqXS1IcbSl7ptGya1C8rjhNgA/640?wx_fmt=png&from=appmsg)

我是否一贯地做到了呢？我是否应该在一个菜单上测试各种操作中的漏洞？是的，这就是几天前我经常在 HackerOne 上四处潜伏（侦察）的原因，每天都专注于一个菜单。我想找到 IDOR！以下是我对可能发生的 IDOR 的假设（这些只是假设！）：

* IDOR 编辑受害者报告
* IDOR 关闭受害者的报告
* IDO 创建对受害者报告的评论
* IDOR 删除评论
* 直到 IDOR 编辑受害者报告摘要。

现在你刚刚看到了我为 IDOR 攻击创建的攻击场景是什么样的（关键：在受害者不知情的情况下执行相同的操作，对吧？）。

在涉及 VAPT（漏洞评估与渗透测试）时，这个阶段属于“信息分析和规划”。

在信息分析和规划阶段，测试人员分析扫描期间识别出的风险，以确定一旦受害者被利用，风险将发生的原因和后果。

渗透（利用）阶段则专注于外部真实风险 [3]。然而，在漏洞发现的背景下，我分析了报告的特性，并制定了直接攻击的计划（如果上下文有些远离，我很抱歉）。

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJDzdCoQHYTbbNE9wwUqLG2F7DWBHUQuel853tfJ4PwlPy4dvzoLC6zA/640?wx_fmt=png&from=appmsg)

攻击与渗透，在这个阶段，我开始直接在目标上进行预先准备的测试场景，例如从“IDOR 编辑报告”到“IDOR 编辑评论同时包含文件”，并尝试绕过防御措施！然而，结果并不如预期（我以为它足够安全！），因为我总是收到“was\_successful”: false 的响应。

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJdRv6kiaJEyaPbcPnABT9WevVcKqqZnJxb8hWkacZ6HgcHLUkER4NDuw/640?wx_fmt=png&from=appmsg)

时间已经很晚了，眼睛也有些疲惫，明天再来吧！

🛌🏻💤 第二天，周末到了，我度过了一个更长的夜晚来完成所有的场景，但是我仍然没有找到漏洞，直到最后一个场景“编辑摘要”，我没想到我能够**使用其他账户的文件附加到攻击者的摘要报告**上，无论是在草稿还是已提交的报告上都是如此。

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJfcNSiaibMAwjWKp1bMTWQ549Iq1HIXQEfODrSwUnXzGWibYNQVL0vSibicg/640?wx_fmt=png&from=appmsg)

我立即写了一份完整的报告，并发送给了 HackerOne 的漏洞赏金计划！

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJtDpCoTqticZYD5HNR1iahB8cMOYJ1vPAdxlDL4LtA4tIVTxEgo0Pmhiag/640?wx_fmt=png&from=appmsg)

之后会发生什么？我一边祈祷，一边劝告自己“这是一个有效的报告！” 但是，我还是不太相信，因为那里的活动非常频繁，即使是顶级感谢的账户也可能对同一个账户多次报告漏洞，你确定我的发现没有被他们报告过吗？你确定没有重复的报告吗？

是的，3天过去了，我问了一下“有更新吗？”考虑到承诺的时间是3天。第四天，我的报告收到了工作人员的评论，我仍然不确定！通常，如果是重复的报告，会立即关闭，幸运的是，我的报告是有效的！

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJodtUnBdVORriaiaia2uW5dmiblObmjLNvxt6ydOibsrSEH1TIvf2y2SxCaw/640?wx_fmt=png&from=appmsg)

第二天，他们给出了一份惊人的赏金！

![](https://mmbiz.qpic.cn/mmbiz_png/cxf9lzscpMoatic9iciao2zVL8vjOdyH2oJE9jN4vW5WqDMWggr0spGcGSvaBNTAGApvgMowFRKnicicbXW5OIiadSdw/640?wx_fmt=png&from=appmsg)

摘要功能是从什么时候开始存在的？我感到非常幸运能在那里找到它。原谅我的啰嗦，这只是一个故事，技术细节在HackerOne报告中。下次再见！

author:  KreSec

Source: https://kresec.medium.com/hackerone-got-hacked-how-can-i-steal-your-poc-01a9132c5aeb

### 漏洞点评

IDOR的本质是逻辑漏洞，跟框架无关，如果开发人员没有对全部功能非常理解，那么很可能在某一个小地方出现问题，导致能够引用到其他地方的资源，造成IDOR(不安全的对象引用），通过这个实际的漏洞案例，相信能增强各位小伙伴挖掘到IDOR漏洞的信心。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款
前面有同学问我有没优惠券，这里发放100张100元的优惠券,用完今年不再发放

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj7N5nMaJbtnMPVw96ZcVbWfp6SGDicUaGZyrWOM67xP8Ot3ftyqOybMqbj1005WvMNbDJO0hOWkCaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 往期回顾

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487187&idx=1&sn=622438ee6492e4c639ebd8500384ab2f&chksm=e8a604b0dfd18da6c459b4705abd520cc2259a607dd9306915d845c1965224cc117207fc6236&scene=21#wechat_redirect)

[Nuclei权威指南-如何躺赚](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247487122&idx=1&sn=32459310408d126aa43240673b8b0846&chksm=e8a604f1dfd18de737769dd512ad4063a3da328117b8a98c4ca9bc5b48af4dcfa397c667f4e3&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试设置功能IV](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486973&idx=1&sn=6ec419db11ff93d30aa2fbc04d8dbab6&chksm=e8a6079edfd18e88f6236e237837ee0d1101489d52f2abb28532162e2937ec4612f1be52a88f&scene=21#wechat_redirect)

[漏洞赏金猎人系列-如何测试注册功能以及相关Tips](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247486764&idx=1&sn=9f78d4c937675d76fb94de20effdeb78&chksm=e8a6074fdfd18e59126990bc3fcae300cdac492b374ad3962926092aa0074c3ee0945a31aa8a&scene=21#wechat_redirect)

点个在看你最好看

PARENTING TRAINING

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