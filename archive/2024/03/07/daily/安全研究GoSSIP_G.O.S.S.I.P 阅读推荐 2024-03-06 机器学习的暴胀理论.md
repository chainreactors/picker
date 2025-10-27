---
title: G.O.S.S.I.P 阅读推荐 2024-03-06 机器学习的暴胀理论
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497464&idx=1&sn=ff9f04407704880d3c069628ff113cf3&chksm=c063d821f714513708fd5ea4ca76b52c0c36ec345b17a5f0fa7dcc4c95d52de4ecbc52b1b9ec&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-03-07
fetch_date: 2025-10-06T17:09:28.541064
---

# G.O.S.S.I.P 阅读推荐 2024-03-06 机器学习的暴胀理论

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxVkUicia5ts8UWpVUicibFLLzlLvk01ofamIE4cMxfFGLMPAWxiaD4HeayVg/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-03-06 机器学习的暴胀理论

原创

G.O.S.S.I.P

安全研究GoSSIP

在宇宙学中有个“暴胀理论”（Inflation Theory），通俗地讲就是宇宙大爆炸后不到一秒钟，经历了一次快速膨胀的过程，使得宇宙的尺度在极短的时间内以指数级增长，从而解决了宇宙学上的一些难题。今天我们介绍的这篇论文，则是讨论了现在对机器学习系统进行实际部署时，面对的存储开销的“暴胀”问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxSH2o04t6cibNicGzHrfqU09b5icJGIDL4cLO77nvMfm7JS7yfCW68Djeg/640?wx_fmt=png&from=appmsg)

下图是当前机器学习生产环境的现状：除了核心的ML code（可能还有核心模型），其余一大堆乱七八糟的组件也需要一起安装进去，这个时候大家就想到了容器。容器是个好东西，让越来越多的运维人员（甚至包括专业开发人员）都搞不清楚程序的组成和依赖，反正就是一股脑的打包了一起运行呗。这种越来越远离计算机底层细节的实践，是不是会导致未来我们对待计算机就像对待生活中的其他设备，只管把它当成一个black box来用就好。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxEOR6wzVxzFiaVhpxZXQoeEhOlUUjNFM7wNDwIyx8rgZzJN5rYgUfCgA/640?wx_fmt=png&from=appmsg)

本文的作者显然不满意这种做法，于是开发了一个叫做`MMLB`（这个名字有点容易产生联想）的分析框架，去测量在实际中部署的机器学习系统的代码膨胀情况。`MMLB`一方面关注那些机器学习相关的容器镜像里面的代码冗余情况，另一方面也关注某些机器学习系统里面的多余和无用的包（package）。

作者首先指出，机器学习系统相关的容器的镜像特别大：下图（a）中展示了机器学习系统容器镜像和通用的其他类型软件容器镜像的体积的比较（CDF是概率分布函数），绿色线条表明机器学习系统的容器镜像都朝着10G往上的体积发展了。。。下图（b）则显示这些机器学习系统容器镜像还在不断变大中。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxQorpc9XhpYDgTKUxrHTaTD5MeaeVMjPaAVJb0qwJjicliaTDNEv2Mcyw/640?wx_fmt=png&from=appmsg)

从机器学习系统的组成，可以看到另外一些变化趋势。拿TensorFlow和PyTorch这两个知名的系统来说，下图展示了它们的代码体积变化趋势：在2019年TensorFlow做过一次大的升级（2.0版本），清理了很多无用代码，结果代码行数骤减；而2018年PyTorch因为合并了Caffe2，代码体积一下子上去了。（这个图是不是很漂亮，有一个工具 Git of Theseus https://github.com/erikbern/git-of-theseus 可以监控特定的Git Repo然后画这个图）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxs0ykJ2lAsmS8Clsvxswsicic3zW2XLjvqj8sj7XdWckJNiaEvicASicrRxw/640?wx_fmt=png&from=appmsg)

`MMLB`的分析流程如下图所示，不过这部分其实比较枯燥，也没什么特别的，我们略过细节，直接去看看数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxDWYnl9W2uDZ156jFgIlrzQIuRKe8YcJ9S2egBXbE0b3Uz74WKuPTyQ/640?wx_fmt=png&from=appmsg)

作者针对如下这些机器学习系统进行了调查分析：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxrtWb4IVZz6mIR3OwiaicVPCWAribZsWTnhBic4n8ttSOYUYnnxeTjkQh0w/640?wx_fmt=png&from=appmsg)

经过分析发现，这些镜像都可以进行“减肥”（debloating，不知道大家有没有用过以前那种“精简版”Windows），可以减掉的尺寸如下（贾玲见了都要佩服）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxVmMzafwEIRnO50X8QwTKntOHMo9QQGiatDKFBeWdibdialqQTyEaKDMZA/640?wx_fmt=png&from=appmsg)

相比而言，一些通用的软件相关的容器镜像，可能就会更加compact：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxUwdiawr7Fy6I9NTc2LoKEN48UUs1UFibb0GOnjNv6h4oAvd0xne0Qiahg/640?wx_fmt=png&from=appmsg)

作者对容器的镜像进行了进一步的深入分析，看看里面哪些冗余的包导致了体积的增长（还记得我们上周那个新闻 [G.O.S.S.I.P 八卦篇 2024-02-29 iOS版“地震预警”APP体积暴涨之谜](http://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247497391&idx=1&sn=31bad183535b521528b7ed6794c33011&chksm=c063d876f7145160c8653634f38448553bb8b35edf833f2446fc9d3bc05a11ed5898eadc86a4&scene=21#wechat_redirect) 吗？）结果显示APT、PIP和Conda这三个包管理系统引入的冗余度（论文里面Definition 3.2和Definition 3.3分别定义了容器镜像的冗余度和package的冗余度，不清楚的可以去看看）都很高：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxiaDHyP3ka0csVwRrddYhuGeODibfGPxbGKmjGib6qGAzLYYN4kWoQjX7w/640?wx_fmt=png&from=appmsg)

当然你可以说机器学习系统的开发维护人员没有那么专业，再说了只要能方便使用，现在手机都可以存上百G的数据了，何必在乎这点点bloating？作者可不这么认为，他们统计了在debloating前后，代码中包含的漏洞的变化情况，可以看到很多CVE都可以通过去除冗余代码而去除：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxvwmOTkJ8aJmOkLLM0Wdq2qpZM7VnIxt8XkEedFShialk6OsWduF4akA/640?wx_fmt=png&from=appmsg)

其实除了本文，我们还想要介绍其他的一些内容，首先是新闻一则：

> JFrog 安全团队在 AI 模型共享平台 Hugging Face 上发现了至少 100 个恶意 AI ML 模型，部分恶意模型能在受害者机器上执行代码，提供持久后门。安全研究人员扫描了平台上的 PyTorch 和 Tensorflow Keras 模型，发现了 100 个含有恶意功能的模型，如名叫 baller423 的用户上传的模型能指定主机 210.117.212.93 建立反向 shell，该模型已被删除。研究人员表示部分恶意模型可能是出于安全研究的目的上传的，旨在发现漏洞获取赏金。
> https://www.bleepingcomputer.com/news/security/malicious-ai-models-on-hugging-face-backdoor-users-machines/

不要以为机器学习的代码没有被黑客盯上，人家美国医疗公司Change Healthcare刚刚支付了2200万美元赎金（然而被勒索的数据并没有得到解密），机器学习在进化出超过人类黑客的智慧之前，是逃不掉被攻击的。

另外还有一篇非常好的文章，强烈推荐大家（特别是有志于深入理解计算机系统的你）阅读：

> https://tonsky.me/blog/disenchantment/zh/
> ![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21Hb2xrVEdN7PL92KjUxAwIxUwhHT04zMVuOtMOCWpRszbAKhCJKKIZO7tx3IU49Zw07uaPzscNzNg/640?wx_fmt=png&from=appmsg)

---

> 论文：https://dl.acm.org/doi/pdf/10.1145/3639032

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