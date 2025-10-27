---
title: 首届中国eBPF大会分享 | 基于eBPF的内核漏洞检测实践
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247515489&idx=1&sn=f208a84999443e30c783de0d35733506&chksm=ce463671f931bf67dcdaf64f5af9e851edb97bc1cbe69b54752d58eb8cd56f2e44a9343b0e17&scene=58&subscene=0#rd
source: 深信服千里目安全实验室
date: 2022-11-13
fetch_date: 2025-10-03T22:38:27.620337
---

# 首届中国eBPF大会分享 | 基于eBPF的内核漏洞检测实践

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5wicDV0sIIgI7JgcJG9OEucc3P3dVERbQdKibGloprspDAQrh3YFbxcibNdquCI2MwGOibW4Qe4DcOJLA/0?wx_fmt=jpeg)

# 首届中国eBPF大会分享 | 基于eBPF的内核漏洞检测实践

创新研究院

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5zFObpGGvbWzxnyX6UtTRfibHlJCvfKQGPIDhYFImibr1SvBqtkm7KjzZsHVdzmOMBrQuKeYghpKOHA/640?wx_fmt=gif)

随着智能化、数字化、云化的飞速发展，全球基于Linux系统的设备数以百亿计，而这些设备的安全保障主要取决于主线内核的安全性和健壮性。

传统的内核安全存在周期长、效率低以及版本适配的问题，有没有新的技术能够实现高效检测内核漏洞？

11月12日，由**西安邮电大学**主办，**中国科学院软件研究所**指导的**首届中国eBPF大会**在线上顺利举办！会议邀请到了**中山大学、浙江大学、东南大学等国内名校**及**华为、阿里、字节跳动等众多国内名企**共同探讨eBPF技术发展、在网络安全领域或其他的应用。

**深信服创新研究院高级Linux内核技术专家许庆伟**荣幸受邀参与本次大会。

主会场上，许庆伟与**来自阿里、华为、腾讯的技术专家**，及**来自东南大学的教授、浙江大学的学生**同台针对**「eBPF技术及发展」**进行**圆桌研讨**；在**分会场二「eBPF在网络安全的应用」**中，许庆伟又为线上诸多技术专家及同好分享了**《基于eBPF的内核漏洞检测实践》**议题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhw2Xt0JQ1upqdKkntllf0JxoWs4gTW0dAMaSnZM63Kkibmfj6ibMWicoHg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

以下是许庆伟在本次大会中的分享回顾。

“

**议题分享：**

**基于eBPF的内核漏洞检测实践**

许庆伟从“内核安全策略演进”切入，阐述了传统内核安全存在的问题，并从Seccomp阶段到eBPF阶段为我们分析BPF安全特性的演进。

![](https://mmbiz.qpic.cn/mmbiz_jpg/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhMxgD2SQfkQetbS8wx8AqnKSsQxBXYRL1fI8IGwFibYy4nh0DiacTf6Qw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

**最后用一个实例展示eBPF如何快速高效地检测到Rootkit攻击：**

1、为了Hook内核函数，必须首先获得想要钩住的对象访问权，例如，它可以是保存所有系统调用函数地址的系统调用表。然后，保存函数的原始地址并覆盖它；在某些情况下，由于当前位置的内存权限，还需要获取CPU中控制寄存器的权限。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhx42KBuvKBRUUliahzQthUC1auiaNdj2PrFL8hddvBpl2vR1h1yJVbpVw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

2、通过内核的core\_text边界检测来实现这一点。内核中的内存被分为几个部分，其中一个是core\_text段，它保存内核中的原始函数；此部分注册在特定的内存映射区域中，该区域不受更改或操作的影响。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhYWHoVwZQ5VKSb0sxiaAuicDJKDTib9uz9QFn98ZhOOWQH8meVlgS5uOOw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvh6xLL7AO3icaGCicvv2Udx96Hx4cosXohlGsvZqXpiaASA2qOkrk0Hq2Jg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

3、使用libbpf的helper来获取系统调用表地址，并将其添加到事件内核符号依赖项中；

注意，detect\_hooked\_sycalls事件是派生事件。这意味着在我们接收到系统调用的地址并检查它们之后，我们将创建一个新的detect\_hooked\_sycalls事件。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvh3qHyrleoC0sK1AzdAqs54DNwzjgNY9WudDZaCrGubcTgAibqZfPn72Q/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

4、将它与系统调用号一起传递，以便使用BPFMap检查内核空间。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvh18ED3MAtrXf5CpC3w7Rvg3OiaSYPt8fXgJiaqo829ZIEjvcOZVgsOcBg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

5、为了检查内核空间中的那些系统调用，基于security\_file\_ioctl上的kprobe创建一个事件，它是ioctl系统调用的一个内部函数；

这样就可以通过使用用户空间的特定参数触发系统调用来控制程序流，接下来用一个特定的命令触发ioctl:

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhKsFvnOcqiaPiarFSbC2gfeZT2TheUXlOcKsSGjnPGvNeSAgsoaafzC1A/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

6、在内核空间中开始检查ioctl命令是否相同，以及调用该系统调用的进程是否为Tracee。这样就可以验证只有当用户要求Tracee检查时才会发生检测的需求。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhl2je02lPEN8M0a3Q645s084AUe3zOYC5GM5NZ54E18Q3VkDnyLfMPw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

7、遍历系统调用映射，通过使用READ\_KERN()来获取系统调用表的地址。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhF9sibAI12QSiaAJbAB81JYA2LU0Sh0QrsLyaiaZcQdxicmj4EpfeMJb6Wg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

8、在用户空间中，将这些地址与libbpf helpers进行比较。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhvFfiaECaJGsg458DdZt4uLW5iaOiaKgBX6aCvkYP9cj71WaLorVl0bUug/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

9、使用insmod函数加载Diamorphine (.ko)的内核对象文件，目标是查看Tracee的检测结果；

通常，如果选择了detect\_hooked\_sycall事件，Tracee将发送一个hooked\_sycalls事件，以确保系统没有被破坏。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhFOVyBIYJZLJJAMRT0awoyTn706GcvG52ibDoy2L7jkDzdwoXeCYcuxQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

10、Tracee检测到getdents和getdents64这些挂起的系统调用。TNT团队使用它们来隐藏大量加密活动导致的CPU负载过高，以及通常用于从用户空间发送命令来杀死进程的kill函数；

在这种情况下，rootkit使用kill -63作为用户空间和内核空间之间的通信通道。同样，如果再次运行Diamorphine和Tracee使用json输出，参数将显示Diamorphine的恶意钩子。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhIk0poTbkQa7u56QmmMKBywn6BMP93kEkQS224UbvFMKMIl4dSliaBew/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

11、通过Tracee-rules，可以看到有detect\_hooked\_sycall事件的新签名，即检测到异常rootkit攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhjg5TicHI0AH17d56FjibHaq0iaZZTkobIPyBIDw7BGDiau6fveicibDwjqTw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

“

**圆桌环节：**

**eBPF技术及发展**

**Q1 目前正在研究的与eBPF相关的事：**

深信服主要的业务之一是安全，目前市面上的安全策略和安全方案基本都还在应用层。但近年来eBPF基础设施的安全性也越来越重要，现在也常看到有基于eBPF的攻击行为，加上eBPF在云原生的应用，针对内核的攻击行为势必越来越多，内核安全漏洞的危害性也被人们所意识，因此深信服创新研究院把部分研究重心放在内核层，比如我一直在研究的LSM和eBPF的结合。

**Q2 谈eBPF未来的发展：**

我近期也对eBPF做了很多思考，如其他教授、专家所说，目前eBPF也存在着碎片化、不标准的问题。所以对于未来的发展，我这边有2个初步想法：

**1、做一套从底到上的标准：**内核态向上有一层标准接口，应用态也有一层标准接口。虽然eBPF有辅助函数，但也会存在很多编译、语言、代码框架等的问题，因此需要一套从底到上的标准；

**2、针对安全等方面可做统一规范：**从安全的角度看，可观测性的能力还比较弱，都仅处于初级的检测并告警的阶段，如果做出阻断动作，就会影响到业务。因此针对安全等重要方面，可以从可观测性或平台标准化做统一的规范，对整体eBPF的发展也将有很大帮助。

**Q3 eBPF理想的编程语言需要具备是什么特点？**

我的观点是需要建立一套标准。不管从内核态角度和应用态角度看，下发到内核态，都亟需一套标准化的框架和接口。现在我们提出的观点是，希望有更多的初学者能够更深入地使用eBPF，那么就应该降低使用的复杂性，或在复杂性上做个封装，才能够引导更多人来学习和使用eBPF。

![](https://mmbiz.qpic.cn/mmbiz_gif/EJiaEo3Lq9krawm4LicsCq8s6Gz6Es4nvhUlGPNJ5h5ICZhklyaAwGDeVKsXPqXnyaicLdfX76t1xibPBlhqL3Ljuw/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

深信服千里目安全技术中心-创新研究院一直致力于安全和云计算领域的核心技术前沿研究，推动技术创新变革与落地，拥有安全和云计算领域500+ 专利，实现攻击和检测技术的相互赋能，并及时把能力输入到业务线中，实现自身产品的迭代优化。未来，深信服千里目安全技术中心也将不断提高专业技术造诣，深度洞察网络安全威胁，持续为网络安全赋能。

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zFObpGGvbWzxnyX6UtTRfibFXicTzaYOdfAp1NDOmZN6qj1Ib5bMRxNDYTBZTIwzD8DPrs7kS9sPrQ/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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