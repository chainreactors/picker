---
title: G.O.S.S.I.P 阅读推荐 2023-03-06
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247494397&idx=1&sn=e7f78bd1073d636ae2269b96056e7947&chksm=c063c424f7144d32b9cc7ebacd16493b51b1c04b0716280d4c9425e59f24587c20c885c8afe1&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2023-03-07
fetch_date: 2025-10-04T08:49:21.361939
---

# G.O.S.S.I.P 阅读推荐 2023-03-06

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3rYWslnM6ibiclPQgal4VYsUCIMOuFOtiaics3CrVwxKcZRAdicibuEv42f2fQ/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2023-03-06

原创

G.O.S.S.I.P

安全研究GoSSIP

今年NDSS会议上，已经连续多次和大会一起举办的Workshop on Binary Analysis Research（https://www.ndss-symposium.org/ndss-program/bar-2023/）在3月3日如期举行。本次workshop共有两个keynote speak报告，第一个报告 *Unlocking the Potential of Domain Aware Binary Analysis in the Era of IoT*来自我们熟悉的林志强教授，我们今天的阅读推荐就带大家来看看这个报告：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3rucEYAT6tlTrNcpoBN3DfOXWMfzVn5BQfZC7ibhQw0jQhAnDgCPGxBlw/640?wx_fmt=png)

首先，林老师用三张精美的slides带我们从1980年代开始回顾了计算机和网络的发展：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3rXoyiajgqdicXgeVB7DuKWH5NnQn3rU7pJON1kgK2cHSb9nYQZpQthzSQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3rNNGvCPyALtGFVic1HjyWgvO9JnJCbzyRaWdwZPelAyh4lMiby4XRwXzQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3rxaGybby3Um6EfFAA8FfaL9zlv8F4gxvtPgrnG6PwI9NicunBnNASHfQ/640?wx_fmt=png)

随着IoT时代的到来，不仅是开发人员，我们安全研究人员同样需要更好地理解IoT系统的架构，下面两幅图展示了IoT系统架构的一些特点。首先，在第一幅图中，我们除了看到中间部分和传统的计算机软硬件栈类似的分层结构，也看到了IoT系统的两个最重要的交互特性——和移动智能终端的交互，以及同云端服务器的交互。在第二幅图中，我们看到的是IoT生态系统的多样性：在不同类型的硬件基础设备上运行各种软件，同时依赖大量网络协议和近场通信协议，这种多样性是传统的PC、服务器和移动智能设备都不具备的！

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3r7I0cwwg2rraawia1JZs6UpbTJrSZj3ZWxKxB5ogOhWUmicZWRy3MibFaA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3rT2OBicvNVSvocibH5dECxJgTZEnAG9OaWGh7zu5ld9vynvjtia2RRDUkQ/640?wx_fmt=png)

接下来的slides里面，林老师介绍了他们最近几年在IoT系统的代码安全分析（特别是二进制代码分析）方面的研究进展。说到这里，我们不禁要show off一下，2022年如果你每天都在读我们的公众号，那你就完全可以跟上这一页的内容！

[**G.O.S.S.I.P 阅读推荐 2022-11-07 寻找特斯拉彩蛋**](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493169&idx=1&sn=73ee006d8c9a8509fa8db9b89bf7c94a&chksm=c063c8e8f71441fe7e1de3e8ad607bcdff50fdfbeaa9468d735731f9da778f8b3a8b8702a602&scene=21#wechat_redirect)

[**G.O.S.S.I.P 阅读推荐 2022-11-02 AutoMap**](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493120&idx=1&sn=d577eaadf90f76cc2d242a946a634463&chksm=c063c8d9f71441cf5279a2458180dffaf3519ac37fdfb0bb10c7ad0613a76adb9f680758ae0a&scene=21#wechat_redirect)

[**G.O.S.S.I.P 阅读推荐 2022-09-14 IoTSpotter**](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247492708&idx=1&sn=038bd1bbe726e006c1b05dd60a174a53&chksm=c063cabdf71443ab0c1960d2f472d862ed934d9a4da69297a50afb67dedc7aad4705fd09e546&scene=21#wechat_redirect)

[**G.O.S.S.I.P 阅读推荐 2022-07-14 PaymentScope**](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247490741&idx=1&sn=399bc320f52bb8e200d4d12b8e845e72&chksm=c060326cf717bb7aa587e2f3dd0964295afa89ed662204783f238687fb2add3b6808e0bf3711&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3riaicCuCuvGCLS7hWvgzYjQN8geB5cHudwoQny2vTbMtDcEK2iavxic69MA/640?wx_fmt=png)

最后是整个keynote speak的小结：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HUU5JbHbhg1f6WjvIyAu3ruZJK7n8gre711ZqTqR8qMgUfxLib62gCJgr2Lg7cicOX3CnsKrpKqYicA/640?wx_fmt=png)

---

Slides下载：
https://web.cse.ohio-state.edu/~lin.3021/file/talks/BAR23\_keynote.pdf

预览时标签不可点

阅读原文

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