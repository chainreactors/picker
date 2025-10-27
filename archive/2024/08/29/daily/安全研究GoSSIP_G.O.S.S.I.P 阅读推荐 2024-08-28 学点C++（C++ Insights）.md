---
title: G.O.S.S.I.P 阅读推荐 2024-08-28 学点C++（C++ Insights）
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498776&idx=1&sn=c9827c2f345dbb20a3394bcaebb89480&chksm=c063d2c1f7145bd79b94c2dab60313a9ca6e77a92d977a57b0446f9c1b01c9d1a0647d8cf562&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-08-29
fetch_date: 2025-10-06T18:04:57.101474
---

# G.O.S.S.I.P 阅读推荐 2024-08-28 学点C++（C++ Insights）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRWFBVC5GGz6XzYolz9YzBDbQibtCxeFT6jAX1CznYaDNcg8ndYG4K6Y3w/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-08-28 学点C++（C++ Insights）

原创

G.O.S.S.I.P

安全研究GoSSIP

转眼间，1979年出生的C++语言已经步入中年，这位大叔年轻的时候就有点复杂，这几年愈发的开始“一人千面”，关于这门语言的争论一直没有停止，不过正如它的发明者Bjarne Stroustrup所说，世上只有两种编程语言：一种被人骂，一种没人用。

Bjarne Stroustrup在2020年写了一篇叫做*Thriving in a Crowded and Changing World: C++ 2006–2020*的文章，回顾了一下从2006年到2020年C++标准的演化过程，主要涉及到了2011、2014、2017和2020四个大版本的ISO C++ standard的修订情况，当然也简单回顾了历史，包括在此之前还有1998和2003年的两个标准，上个世纪学编程的同学是不是还记得那个对标准支持得非常糟糕的坑爹VC 6.0编译器？

> https://dl.acm.org/doi/pdf/10.1145/3386320
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRW2QYRvzaJtzC6R7Me5Vmn9ZjJexPe8Z4J3yibGJGGBT32Ff4SpntIxJQ/640?wx_fmt=png&from=appmsg)

到了2023年7月，C++ 23这个新标准都已经确定下来了。说到C++标准的演化，一般人可能很难跟上标准化委员会那帮人的步伐，新特性越来越多，学习曲线越来越陡，先来看一个代码示例：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRWfibtMmDKicgwLdGkYRL5BeZviaicKPzsJibgXqXzLr0Gfw28HiaeD39KdX3Q/640?wx_fmt=png&from=appmsg)

你对这个代码示例理解多少？实际上，只需要找到一个支持C++ 11标准的编译器就可以对它进行编译。这种对原始复杂代码的简化（一般我们管这种做法叫做“语法糖，可以参考 *https://www.luogu.com.cn/article/l86yn4aw* [*从 C++98 到 C++20，寻觅甜甜的语法糖们*] 这篇文章看看），把实现的细节都遮盖起来，如果你一开始就学了这种风格，虽然代码更加简洁了，但是对于底层的实现可能就只是“囫囵吞枣”；而如果你是大龄程序员，也许完全不懂这种风格，看了也会一头雾水。

遇到这种问题，当然可以求助编译器（虽然C++编译器的提示信息的易读性那可是臭名昭著），为了帮助大家更好理解编译器对语法糖的“拆解”，今天我们就要给大家安利一个学习网站——C++ Insights

> C++ Insights网站：https://cppinsights.io/

这个网站能够把一些“魔法代码”的编译器理解版本给你来个“低维展开”，让你看清楚更多的细节，例如上面那个例子，你在C++ Insights网站上让它帮忙处理一下，就会得到编译器处理后的版本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRWEaNknJqX6sI3ImyVWGSmibWTjCznQs23AoYbGaXicLYEG68gb1Dj8ldg/640?wx_fmt=png&from=appmsg)

怎么样，是不是瞬间就容易理解了，尽管代码规模膨胀了许多，但是你也不会拿整个工程去测试是不是？

在C++ Insights网站上还有一系列的学习资料，比如网站的开发者Andreas Fertig的技术报告：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRWEObJ5xctVsibdwAJTA0DcoOHL6NC8df6wNUEQ8jgzmza7p9QgVJsCTg/640?wx_fmt=png&from=appmsg)

Andreas Fertig还在YouTube上发布了一系列教学视频，大家有兴趣可以去深入学习：

> https://www.youtube.com/watch?v=NhIubRbFfuM&list=PLm0Dc2Lp2ycaFyR2OqPkusuSB8LmifY8D
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRWLCuJibXRlRN5GyBz9bdWVSziaBfFA1gTOV73TX8ia2owHeibk8pL30RtfQ/640?wx_fmt=png&from=appmsg)

希望通过这个网站，能够帮助你更好了解C++的新特性，而不是还停留在《C++程序设计语言》特别版那个古老的标准上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRWEW7gBlOMuZPkZMrSmicJCibiaMOrpoCNvm39v7tDXtCuubpgAbCvbk9oQ/640?wx_fmt=png&from=appmsg)

最后，也希望我们的读者们反馈一下，大家在大学里面现在学的是哪个标准的C++呢？是已经用上了C++20标准，还是只会做下面的茴香豆题目？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GJdnJGB1icJkMzyhr9v1bRWSVqZGP69kaCXpDWQIwCICibCSYlDtDMvtXff2ZQ4kbvTDjdw0muZM0g/640?wx_fmt=png&from=appmsg)

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