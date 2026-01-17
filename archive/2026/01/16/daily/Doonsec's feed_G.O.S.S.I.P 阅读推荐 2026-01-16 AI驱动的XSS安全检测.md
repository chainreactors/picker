---
title: G.O.S.S.I.P 阅读推荐 2026-01-16 AI驱动的XSS安全检测
url: https://mp.weixin.qq.com/s/a8MqFGrXkwi0hH9MbeflUg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:22:11.794220
---

# G.O.S.S.I.P 阅读推荐 2026-01-16 AI驱动的XSS安全检测

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmmdMbxN5InjxibYnicBIMjLQTT9iaBYR80pgEbX9zeoK99SJm53Hpqlxrw/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2026-01-16 AI驱动的XSS安全检测

原创

G.O.S.S.I.P
G.O.S.S.I.P

安全研究GoSSIP

![]()

在小说阅读器中沉浸阅读

> 浊酒一杯家万里，燕然未勒归无计。羌管悠悠霜满地，人不寐，将军白发征夫泪。

不知道你还记不记得【[G.O.S.S.I.P 学术论文推荐 2020-12-03](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247483877&idx=1&sn=873e8d5297fb0de7bad35e1a768feb30&scene=21#wechat_redirect)】的内容，转眼5年过去了，世界发生了巨大的变化，而5年前的研究工作也已经推陈出新，我们今天要介绍的NDSS 2025研究工作 *YuraScanner: Leveraging LLMs for Task-driven Web App Scanning* 正是此前工作的续作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmiaib9TzYaMwBr29Y7rM9mFRIEy74t5qeXLibsm1JQX9NU5Xtsyb6wJYjQ/640?wx_fmt=png&from=appmsg)

在AI时代，研究的动机太简单不过了：以前审稿人动不动就喜欢怼作者“你这个过程不能自动化吗？” 现在万事万物给它套上一层大模型或者agent就完了（这些mean的审稿人很快也要被AI审稿给取代了吧）。下图这个例子就很简单，以前的web漏洞分析系统，因为前面的前序步骤没法智能实现，所以探索不到步骤⑤⑥，也就没法发现（可能还算比较明显的）XSS漏洞。而现在呢？前序步骤只需要人工智能一下就OK，那后面的漏洞发现也就更加轻松了~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmagAE81Nm44vOaeib3ItZOdERswQEUGvmrHAalapAZRzRDcPUawDZJGA/640?wx_fmt=png&from=appmsg)

当然说起来简单，未来最大的区别就是你会不会把AI应用到你的工作中（这个话我们从小就听太多了，什么未来不会英语/电脑/开车的人都要被淘汰，结果现在看起来是英语/电脑/开车这些技能都要被淘汰了），那具体怎么样让AI帮助你去完成web安全测试呢？本文设计的`YuraScanner`系统就是这样一个能够运用AI来探索web系统的**deep state**的自动化安全测试工具，它的方法和作者在2020年设计的Black Widow系统的“先建模后探索”方法不同，直接把LLM应用到了web界面分析这个任务上。

也许你会觉得奇怪，LLM怎么能用在web界面点击这种地方呢？实际上已经有很多browsing agent可以做到了，比如一些网页助手可以直接操作浏览器帮你买票（黑产狂喜）。而`YuraScanner`基本上就是作者之前的Black Widow的“AI套壳版”：先用AI实现特定的状态探索，然后再把漏洞挖掘交给Black Widow去做。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmyvXpdxdPDGJ2TevJs82J8hHpbmwA1DC2UssJ5LgoqGEGjcKneCr1Ng/640?wx_fmt=png&from=appmsg)

整个`YuraScanner`的工作流程中，核心创新点是基于人工智能的网页分析和自动化任务（task）执行，先看第一步（task extraction）：这一步完全把对网页的分析交给了LLM去理解和生成相关的（基于自然语言描述的）操作任务：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmJ2uXlLBgrdrd1iaZNlYLia4q8x82zxAtZJyYOL5TFOvOwCI8DWtPiaLsg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmspkyFNtwBhsU3NG6uUlf6GuxqKVI5O6pJhZTYkG1ntGzaGDh2HgUCQ/640?wx_fmt=png&from=appmsg)

有了操作任务之后，依旧使用LLM来分析网页元素，同时将具体的操作指令转换成相关的点击任务：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmm1bstQvGSOlZmFjia4q2Ws6TGJ4hUAWENhicL3YyhsjjT9Rypj23v2dw/640?wx_fmt=png&from=appmsg)

作者表示，AI加成的`YuraScanner`可以探索的状态深度远远超过以前：甚至超过10步的操作序列都能成功去完成（豆包手机助手默默流泪）！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmKSyJmO1dTibSvotUNTXaiatnAG5ibxWcXBibKU2V9eV1m4fCWUykIcl0Nw/640?wx_fmt=png&from=appmsg)

作者使用`YuraScanner`对20个流行的web应用进行了漏洞测试，并对其中10个（下表列出）进行了详细的中间步骤分析：`YuraScanner`为这10个web应用生成了2361个操作任务，其中1818个是有效的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmTkibtSLtLtkoPQkCK48r0ImAwGL1mgE06m4ibFdHtn1D2iaHJDvxCMeBQ/640?wx_fmt=png&from=appmsg)

再进一步，这1818个task中，有37%的task是可以被LLM驱动的agent正常执行的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtm1BWjaOaeeHAUicGOOGEVg7Z2NSacPny3xel47wHRlYTRWnicibgUzNOvg/640?wx_fmt=png&from=appmsg)

不过，在发现漏洞这个环节，结果似乎有点不太好看，大部分的漏洞都是在Redacted上发现的，且不说有17个测试对象上什么问题都没找到，关键是单纯和作者自己的Black Widow比较，也就堪堪打个平手？（看起来`YuraScanner`是专门针对Redacted设计的，在其余的系统上都没什么更好的表现，甚至在Leantime上表现更烂）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmXVxbr2TbOoUhicQqMJiauFUVWMehWTgduMBeGeWY4errictnKlJ7o2I6A/640?wx_fmt=png&from=appmsg)

作者狡猾地在PPT上艺术化地处理了一下，是不是就看不出来weakness了~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmAvjxhsS3b5HjHVh43CSG1OxIiaHW2xA1Pk554iaDSWCPzmibmmBTmt7Wg/640?wx_fmt=png&from=appmsg)

当然作者也展示了一下`YuraScanner`的优势（下图），就是可以比其他的工具探索到更多的state，也因此可以找到更多的攻击面（虽然不一定能找到更多漏洞）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmqIiaFLAQTCRClcYtNXwYp31YFQREmNw3SicK9PUbFAOzTUf0pN7anLkA/640?wx_fmt=png&from=appmsg)

最后要吐槽一下，现在的安全论文都越来越像AI论文了，不写Prompt甚至都不好意思发出来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtm19eZmibicLYj7bKdGL4YOCPL3Z2euzyoPicvH9y8qLYIs0hSiaXPXZiaZAg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21EiaN20oh5KJS9pv5kE9yAtmCejPqow5n9BfUxbWAdykpfH6mGntllAmFF00Duvy7GZRVib6RqcpDkA/640?wx_fmt=png&from=appmsg)

---

> 论文：https://www.ndss-symposium.org/wp-content/uploads/2025-388-paper.pdf
> slides：https://www.ndss-symposium.org/wp-content/uploads/2B-f0388-recktenwald.pdf
> 代码：https://github.com/pixelindigo/yurascanner/tree/ndss25

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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