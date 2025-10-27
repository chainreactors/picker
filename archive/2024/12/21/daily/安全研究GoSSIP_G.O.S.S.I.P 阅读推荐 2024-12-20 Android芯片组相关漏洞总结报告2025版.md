---
title: G.O.S.S.I.P 阅读推荐 2024-12-20 Android芯片组相关漏洞总结报告2025版
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499454&idx=1&sn=96a579525a54f7e4000867bcfb7643f3&chksm=c063d067f71459710b20f7f42f409e6a44da03f245ec80005326c7b8b022ed3119efbb022ea8&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-12-21
fetch_date: 2025-10-06T19:39:08.169777
---

# G.O.S.S.I.P 阅读推荐 2024-12-20 Android芯片组相关漏洞总结报告2025版

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwmdbSGMHQJBXyPdYfHDh4kx3icfGQWdu4JjUo52Dhd5mqGLTLlwdvRww/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-12-20 Android芯片组相关漏洞总结报告2025版

原创

G.O.S.S.I.P

安全研究GoSSIP

从Android系统诞生的第一天起，安全研究人员就不停发现和收集安全漏洞（大家可以去考古一下最早的一篇Android安全研究论文是什么时候发表的，而第一台Android手机是什么时候发布的），这一过就是差不多20年了，每到快到新年可能Android厂商都会许愿说明年能不能不要再有新漏洞了，然而实际情况是这几年每年的学术研究会议上都会有文章去回顾最近的Android漏洞发现和修复的“盛况”，今天我们就给大家带来2025年版本的Android安全漏洞总结，当然这篇来自NDSS 2025的论文 *Vulnerability, Where Art Thou? An Investigation of Vulnerability Management in Android Smartphone Chipsets* 有所聚焦，重点关注的是Android设备芯片组的安全漏洞（简称“芯片组相关漏洞”，这些漏洞一般都是高危）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4Idw30zibmeMswiaZRVrp96DzPqwj06MricIaYOkQq7qP83B2tphKLqicsMTmQ/640?wx_fmt=png&from=appmsg)

为什么我们说漏洞总结这种论文已经成了年经帖呢？先看下面这张表你就懂了，参考文献里面覆盖了从2020年到2024年的相关工作（而且年年有）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwicYgGvPTkq5M4veuGiaicfeBCl5iaUXx1pxmH6zWS0K4RibDH51c3Y0Jy1Q/640?wx_fmt=png&from=appmsg)

本文当然胜在更全面，具体来说，作者研究了如下几个方面的问题：

1. 芯片组相关漏洞是怎么被引入的？
2. 谁发现了这些芯片组相关漏洞？
3. 芯片组相关漏洞什么时候被修复？其危害程度又如何？
4. 厂商修复芯片组相关漏洞的流程有什么特点？

先说下作者调研的对象吧，2024年底我们很欣慰地看到现在主流的四大Android SoC厂商中，紫光展锐（Unisoc）赫然在列，要知道时光倒流10年，高通（Qualcomm）、三星和联发科（MTK）还是不可动摇的“御三家”。作者通过多方面的努力，收集了3676个不同的芯片组相关漏洞，覆盖了高通、三星、紫光展锐和联发科的437个不同类型的芯片组，涉及从2009年9月到2024年4月期间生产的Android设备。作者还弄了个很酷的域名，说是以后会持续更新这些漏洞信息：

> https://www.chipsets.org/

不过不要高兴太早，这网站目前还需要http authentication，估计只有审稿人能访问。作者把4个研究问题和芯片组相关漏洞的整个生命周期对应起来了，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwpAwWuu7jDwqImO1ZtZZicwiaRXGLygwc5czttAuo6fiaSwkY7aOFynOjw/640?wx_fmt=png&from=appmsg)

好，我们来看第一个问题，那些芯片组相关漏洞是怎么被引入的？首先作者统计下来发现，平均每个类型的SoC对应204个漏洞（即使是中位数也有149个）！很显然，这些漏洞不太可能是一口气引入的，下图表明，在推出一款新型号的SoC的时候，厂商会把祖传的问题（93%）也一起带过来，而只有7%的问题是新引入的。同时在新产品推出之后，只有9%的漏洞会被发现和修复，而剩下的91%的问题则会继续战未来。因此作者建议，不需要太关注新产品，专注测试古老的型号也能帮助发现“新”问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwDgFlfe0Fvv9NnKSwyvXqS4ODmByicwRQXRQTesNMnXMjy3kxrZFFLsQ/640?wx_fmt=png&from=appmsg)

再看看漏洞影响了芯片组的哪些组件，下表显示，和通信、基带相关的代码是重灾区，很有趣的是在机器学习相关的组件（也许是NPU、APU这类？）中也开始发现漏洞了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwvkwDtUibadNZUFJxqprlsQCGc2oicKPVLpEUtqTG6WPNSkwQGQ98iaXwg/640?wx_fmt=png&from=appmsg)

那么到底漏洞是由谁发现的呢？高通和三星这两个老牌厂商相对来说在安全方面投入肯定多一些，2023年的数据统计表明，高通相关芯片组相关漏洞的57%都是内部发现（并披露）的，而三星在这方面的比例是60%（而且2022年三星的这个比例只有25%，考虑到三星2023年组建了芯片安全团队，这个KPI一下子就很香了）；与之相比，紫光展锐和联发科就有点显得投入不够，紫光展锐在这方面的比例只有7%，而联发科也就刚到10%，欢迎这两家厂商招人组建安全团队啊~

从下图我们也可以看到最近几年针对四家厂商的漏洞的变化情况，可以看到随着漏洞数量的增多（例如紫光展锐的指标），市场份额也相应提升（误）。也许确实是只有没人用的产品才没有漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwgQtjwyKAnKEU8U2ciayvC486BfqmIvM1eFkSldRXtao20NvPCvBJmMw/640?wx_fmt=png&from=appmsg)

虽然但是，紫光展锐和联发科在漏洞披露方面还是做得不如三星和高通，在统计漏洞从披露到修复这个数据方面，就没法找到紫光和联发科的信息，作者于是只考虑了三星和高通的，从下图看出，所谓“通知厂商90天后公开漏洞信息”这个安全业界的金标准并不能很好约束厂商，很多漏洞的修复时间远远超过了三个月（不过从图中看出，最近似乎这个拖延症的情况有所缓解）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwE3DhmTNwn8cInW9FiaN94nLwL3Qq5ZE3NUppLGv8TZc9gfHWSVB16lQ/640?wx_fmt=png&from=appmsg)

作者还注意到，AOSP的那个每月安全公告里面并没有把联发科和紫光展锐芯片组相关漏洞考虑进去（Google只关心自己家那个巨烂又巨贵的Pixel），因为这两家厂商不愿意提供相关细节给AOSP安全公告，当然用户也不太会注意到，于是搞间谍软件的以色列公司更开心了。 作者算了一下，当芯片厂商公布了漏洞（和修复方案）后，下游的手机厂商平均还需要2-8个月的额外时间去把产品打上补丁，间谍软件开发人员KPI拉满~~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4IdwqqNKcuxicu6y2Izf9XicFsdCQibRDmiblvwg8tJwPFWYuCUaYrQACn4C1A/640?wx_fmt=png&from=appmsg)

作者统计发现，联发科不同的产品型号之间特别喜欢共享同一个漏洞，而且厂商也喜欢基于MTK的芯片组搞出来一大堆乱七八糟的手机型号，于是经常出现一个安全漏洞影响上千不同型号的情况，你看看人家苹果，产品型号少就是有好处，一个漏洞最多能影响20个不同型号的iPhone就很厉害了~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FvmLS1gyUDkNicTvDTO4Idw1PWCN4jy0Qbt7DFL35TQFu70YN6FCib5yiafWNE1pxr1fgjCAUxbSuCQ/640?wx_fmt=png&from=appmsg)

在回答完四个重要问题后，作者还进行了很多有意思的讨论，比如说他们调查了业界的平均水平后，发现大部分配备了专业安全团队的产品（不管是高通的芯片组，还是Chrome或者FireFox这种大型软件）的安全漏洞差不多有一半以上都是内部安全团队发现的，而紫光展锐和联发科在这方面比例都不到15%，因此还有很多潜力可挖（再次呼吁两家厂商重金招聘安全研究人员）。同时作者也研究了bug-bounty对安全漏洞的减少是否有什么帮助，结果表明针对高通产品的漏洞数量在bug-bounty开启之后没有什么波动，这说明 高通非常有钱 bug-bounty似乎对消除安全漏洞的帮助没那么大，作者猜测可能是对于黑客来说，因为芯片组相关漏洞没那么容易测试？

总之这篇论文特别适合领导阅读，我们因此也要给出的G.O.S.S.I.P推荐指数为：

> Strong Accept

---

> 论文：https://arxiv.org/pdf/2412.06556

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