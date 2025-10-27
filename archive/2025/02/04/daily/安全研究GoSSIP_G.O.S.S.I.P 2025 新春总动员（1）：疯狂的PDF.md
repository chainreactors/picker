---
title: G.O.S.S.I.P 2025 新春总动员（1）：疯狂的PDF
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499652&idx=1&sn=589b1778aa04f72cdc07c947be4bc17c&chksm=c063d15df714584b9680831e04f60a8d775211b89366d6125e8a337aa07a891760a5f272c4ba&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-04
fetch_date: 2025-10-06T20:39:08.046461
---

# G.O.S.S.I.P 2025 新春总动员（1）：疯狂的PDF

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21HIlLfW715adqIlINIZhQJWsTJ7m3O7icKIyBnj2DKMXB1Gic02wDwnbVMx0Y4aF4uQUJNZdmxFVf0g/0?wx_fmt=jpeg)

# G.O.S.S.I.P 2025 新春总动员（1）：疯狂的PDF

原创

G.O.S.S.I.P

安全研究GoSSIP

去年春节我们发布了一篇文章《[G.O.S.S.I.P 春节总动员之制作二向箔](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497277&idx=1&sn=28aa44f01ce7f048a7c2a9ddb3cd9f06&scene=21#wechat_redirect)》，后来还写了一篇《[G.O.S.S.I.P 阅读推荐 2024-09-05 用PDF做点坏事](https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498814&idx=1&sn=bd3fba594bf73147a5f0b8daf2a7d39b&scene=21#wechat_redirect)》的文章，都是关于PDF的奇怪用法。在蛇年春节假期行将结束之际，我们延续去年的主题，继续给大家介绍更多疯狂的PDF！

---

首先请访问如下的PDF（安全风险自负，哈哈）：

> https://th0mas.nl/downloads/pdftris.pdf

你看到了什么？哈哈哈，办公摸鱼！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HIlLfW715adqIlINIZhQJW8U5fibP2weh7CZoK4hEm5kpmVibMJL7Yw3hKZm1qTqVHKEZgJ5gvLvzw/640?wx_fmt=png&from=appmsg)

这实际上是一个叫做 **Tetris in a PDF**的有趣项目：

> https://th0mas.nl/2025/01/12/tetris-in-a-pdf/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HIlLfW715adqIlINIZhQJWFGiaDbKl8CsBO7EU11ta42ZdI6OJHpzNYS46Ppmz2fLg3VxBzh1S9Nw/640?wx_fmt=png&from=appmsg)

不过你以为在PDF里面只能玩玩俄罗斯方块？错，我们还可以用下面的PDF来玩1994年的大型3D射击游戏——DOOM！

> https://doompdf.pages.dev/doom.pdf

请看如下视频

实际是这又是一个有趣的开源项目，来自

> https://doompdf.pages.dev/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HIlLfW715adqIlINIZhQJWvwnPBx8rIDoQs0qdB0qN4mTibAtHlTKb0icd4CGKiboh1suqzwA8VKwXg/640?wx_fmt=png&from=appmsg)

（其实前面那个Tetris in a PDF项目的作者也有一个类似的项目：

> https://github.com/ThomasRinsma/pdfdoom

---

当然，这并不是宇宙的终点，毕竟盗梦空间是要层层嵌套的，既然可以玩游戏，那么干脆装一个操作系统来玩游戏吧！

> https://linux.doompdf.dev/linux.pdf

注意这些PDF都只支持基于Chromium内核的浏览器（而且在Windows 10上的Edge好像并不能正常运行）。当然，为什么这些PDF能够用来搞一些稀奇古怪的事情呢，还不是因为鬼知道什么时候开始PDF规范就开始支持JavaScript了，加上**程序员之神——****Fabrice Bellard**写了一个能用JS来运行的模拟器TinyEMU (https://bellard.org/tinyemu/)，一切都水到渠成了。

---

最后，要给大家安利的是一个叫做 horrifying-pdf-experiments 的项目，由Omar Rizwan完成，在2020年疫情刚刚开始的时候就放出来了，估计也是在家里憋得慌：

> https://cdn.jsdelivr.net/gh/osnr/horrifying-pdf-experiments@master/breakout.pdf

这个项目里面的PDF，可以玩经典的打砖块游戏，由此也启发了后来者不断在PDF上面搞些奇奇怪怪的玩意。

> 原视频：https://www.youtube.com/watch?v=6rbJu10Telc

我们注意到，在2020年的时候PDF specification文档就已经有1310页之多了，除了支持JS，还有各种乱七八糟的特性包括：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HIlLfW715adqIlINIZhQJW9FY9z5JeuOLEtIwiah3PSsyALtuZY0WiatsDNg7W5eXl8dCeHnFq6ScA/640?wx_fmt=png&from=appmsg)

请问让这一切更加复杂是为了什么呢？我们不就是为了看篇论文吗？

---

最后的最后，为了保持本公众号阴阳怪气的特色，我们考据了一下DoomPDF的作者`ading2210`，发现这家伙还是一个高中生 (https://github.com/ading2210)，估计大概率不是在我国这种高度激烈竞争的环境里面成长起来的，因为这几个作品太没有科学含金量了，在上海市青少年科技创新大赛这种级别的竞赛都没有办法拿到什么奖吧~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21HIlLfW715adqIlINIZhQJWeUBXzpKicqySSMLgPic6rqctzsep027BV1sp7fnYQM2OUHdYEzelBfHw/640?wx_fmt=png&from=appmsg)

给大家拜个晚年辣！

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