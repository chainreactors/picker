---
title: G.O.S.S.I.P 阅读推荐 2024-07-08 大破 Xilinx Zynq-7000 SoC
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498385&idx=1&sn=34a4d85dc6b9e28fceba896527b4844b&chksm=c063d448f7145d5e5d4af86e7e445736c9bca21ec0f6a2fc72af59b66b7559bb9a6fdc597b16&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-09
fetch_date: 2025-10-06T17:46:18.816450
---

# G.O.S.S.I.P 阅读推荐 2024-07-08 大破 Xilinx Zynq-7000 SoC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GoicXVfIEpdEAHefmwpicOuEK4NaRl7OxqUSPH2VwJKY5gRK2gLvJBQEBXvEPPmrD9S5oL1Ra17WYA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-07-08 大破 Xilinx Zynq-7000 SoC

原创

石卡库

安全研究GoSSIP

今天我们继续介绍WOOT 2024的论文，在这篇名为*Breaking RSA Authentication on Zynq-7000 SoC and Beyond Identification of Critical Security Flaw in FSBL Software*的论文中，作者对Xilinx Zynq-7000 SoC设备的RSA身份验证进行了深入分析，发现了一个严重的安全漏洞，利用该漏洞可以绕过身份验证功能，将被篡改的程序加载到Zynq-7000上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoicXVfIEpdEAHefmwpicOuEibpGyTezWfSAqeAiaCOoab4EJfr0ThVAM42EevIxqkJa0Wd3Un7omf6w/640?wx_fmt=png&from=appmsg)

什么是Zynq-7000呢？它是赛灵思（Xilinx，不对，现在已经被AMD苏妈收购了，所以应该是AMD）出品的一个非常灵活的硬件可编程平台。它通过FPGA和ARM芯片的组合，实现了比传统的FPGA开发板更强大的工作能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoicXVfIEpdEAHefmwpicOuEoWzzD3ybMchJolINx7qDUwjoHndibibQVJsfB01K8oNl7jrt8Iib5bgdw/640?wx_fmt=png&from=appmsg)

通常情况下，Zynq-7000需要通过存储在Non-Volatile Memory（NVM）中的安全启动镜像来激活。当设备启动时，会对启动镜像进行RSA身份验证，即开启RSA eFUSE功能。启动镜像的结构一般如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoicXVfIEpdEAHefmwpicOuEYEllbZFHE0dv7AhQSwgUfURgJdg6HqkTcazMQ0gicvl2jib0X8zJnffQ/640?wx_fmt=png&from=appmsg)

在这里，我们重点关注其中两个部分：Partition Header Table（PHT）和First Stage Boot Loader（FSBL）：

* PHT包含各种分区的特征信息，每个分区都与PHT中的一个条目相关。
* FSBL是Zynq-7000启动时首先运行的软件，它会从启动镜像中检索PHT并检查RSA验证，验证通过后才根据PHT中的信息加载不同的Programmable System（PS）和Programmable Logic（PL）分区，否则终止启动过程。

Zynq-7000启动时执行的RSA身份认证的过程，由BootROM代码和FSBL共同执行，但BootROM代码存储在一个安全且不可访问的地方，只有FSBL是开源的，因此，作者只能根据FSBL源码分析出RSA的身份认证过程：

1. 首先，FSBL向NVM请求一次PHT数据（把它记为PHT1），然后检查RSA eFUSE这个选项是否被启用。
2. 如果RSA eFUSE被启用，则FSBL再一次向NVM请求PHT，这次请求得到的数据记为PHT2，PHT1和PHT2的区别在于，PHT1这次数据请求没有去获取相关的签名和证书信息，而在PHT2的请求中，会把证书和签名信息都拿回来进行验证。注意，虽然请求了两次，但在正常情况下这两次PHT数据是相同的，即PHT1=PHT2。
3. 验证通过后，加载PHT1中的数据到PS/PL分区中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoicXVfIEpdEAHefmwpicOuE2IEJJPO339baxoGDhKUZuhurK70YjJ5zPibF5ypYNdibAgoVVy2zzU7g/640?wx_fmt=png&from=appmsg)

现在我们可以发现问题所在：FSBL验证了PHT2，加载的却是PHT1的数据。如果攻击者能篡改PHT1，便可以在设备中执行恶意程序。作者发现，FSBL的代码直到2020年4月前都存在这个问题：

> https://github.com/Xilinx/embeddedsw/blob/master/lib/sw\_apps/zynq\_fsbl/src/image\_mover.c

随后，作者便开始设计攻击实验。作者设计了这样一种攻击方法，制作了两个启动镜像，把它们放在两张不同的SD卡中。由于FSBL区域是被加密的，直接修改FSBL比较困难。于是作者将两张SD卡连接至同一个复用器，再用服务器连接Zynq-7000，其中SD1用于发送被篡改的PHT1以及携带未被授权的攻击APP，SD2发送与受害者启动镜像一致的的PHT2。

但是，作者在实验中发现，先让Zynq-7000读取SD1的恶意PHT1后，再切换到SD2时，设备拒绝与其通信。作者猜测*Zynq-7000使用了专门的ID标注SD卡，此时ID发生了变化，导致它仍然与SD1通信*。为了解决这个问题，作者不得不从内存中调用了使FSBL初始化SD卡信息的函数，虽然这在现实场景中难以实现，但确实证实了能从外部NVM绕过RSA身份验证。所以，如果使用能在精确时间点篡改SD卡接口上的数据的专用硬件 (FPGA/ASIC)，则可以轻松克服该限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GoicXVfIEpdEAHefmwpicOuE8iaHgpSeuUqshGL7q33icYOvxice19jqf5Nibk1doAu7Nr17qicse003VXQ/640?wx_fmt=png&from=appmsg)

最后，作者还进一步实施了Starbleed攻击。关于Starbleed攻击的详细介绍，读者可以参考[Usenix Security 2020 的文章

> https://www.usenix.org/conference/usenixsecurity20/presentation/ender

该攻击的唯一要求是攻击者能够访问 FPGA (或PL) 的配置接口，而在Zynq-7000中存在开放的Processor Configuration Access Port（PCAP）接口，因此这就没什么困难了：Zynq-7000要求把DONE信号设置为高电平，然后就可以用PCAP接口读取`WBSTAR`寄存器，于是作者先编写操控PL的代码，把DONE信号提高至高电平，之后将Starbleed攻击比特流传进PCAP接口，再通过PCAP接口的命令读取`WBSTAR`寄存器，成功得到了解密的比特流。

实验中作者还观察到，每当读取一次比特流，PCAP接口就会进入无法响应的状态。因此，单次启动只能恢复一个字的比特流，需要对Zynq-7000循环通电才能恢复完整的比特流。目前的实验结果表明每秒可以恢复32bit，而恢复3.85MB的样本则需要46天（labour work警告）。

---

> 论文：https://eprint.iacr.org/2023/1913

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