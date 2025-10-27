---
title: G.O.S.S.I.P 阅读推荐 2024-07-29 欢迎观看DH秀！
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247498579&idx=1&sn=ff9785a7de11db86e08420f655b9afd1&chksm=c063d58af7145c9c9f57a302ac734f7abc5b92bcebb1786eeed8176f98d77a2f5abd96d3109c&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2024-07-30
fetch_date: 2025-10-06T17:45:35.352682
---

# G.O.S.S.I.P 阅读推荐 2024-07-29 欢迎观看DH秀！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwq85POY6IyNtOI1HURIB8rUd9xxT7bZyEicuibJ2uDcB0gr9Dx0HWdbicA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2024-07-29 欢迎观看DH秀！

原创

G.O.S.S.I.P

安全研究GoSSIP

经过了暑期学校忙碌的一周，停更许久的 G.O.S.S.I.P 阅读推荐又和大家见面啦！今天要给大家介绍的论文*Diffie-Hellman Picture Show: Key Exchange Stories from Commercial VoWiFi Deployments*来自USENIX Security 2024

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pw4wpDJsPmqsCQ8zJAot8jMsCo6GUEoD2LlPAvwiatEibaBkMsic8ia8PrgQ/640?wx_fmt=png&from=appmsg)

先来看看本文的研究背景：如下图所示，在现代的移动网络中，智能手机（user equipment，UE）的语音通信不再总是使用传统的通信信道，而会基于无处不在的Wi-Fi网络，进行所谓的Voice over Wi-Fi（VoWiFi）通信。这种语音数据的传输信道是在Wi-Fi网络、移动运营商（Mobile Network Operator，MNO）和一个叫做Evolved Packet Data Gateway（ePDG）的节点之间建立基于IPSec的隧道，但是这种通信方式的安全性可能会因为一个小小的因素而遭到完全破坏，这也是本文的核心研究内容，让我们深入到论文中去看看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwqsichDTQHs2fk4icz1atLLoRuwibA26hqTNlQdsRmU3IOG4KUREHj5xng/640?wx_fmt=png&from=appmsg)

作者发现，在上图的通信中，最开始阶段需要执行一个基于Diffie-Hellman（DH）密钥交换协议的密钥协商，而在很多运营商网络中，这个过程并不安全：最典型的问题就是允许降级攻击，完全阻止密钥的协商和后续加密信道的建立。实际上，整个VoWiFi通信过程分为下图所示的三步，而论文只关注了其中的第一步（L1），因为在这一步里面通过DH密钥交换建立起来的可信信道是后续整个通信安全的前提，如果这一步出现了问题，后面的整个安全体系就都破坏了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwx4k5bgUMfHq6pk5EEtS9s2NBvxAI4aIeicfSEDG6Z78B5ByOhCtpvGA/640?wx_fmt=png&from=appmsg)

作者首先调研了VoWiFi的生态，这里面关键的信息之一，是手机（UE）侧的配置文件。其中苹果（iOS）、高通和三星各自有各自的配置（放在固件或者系统文件中），决定了手机如何与不同的运营商进行密钥协商并建立安全信道。而Pixel手机通常使用默认的设置（在Android源码中有），但是也允许运营商的APP（这个APP的签名能够通过sim卡上的一个证书进行验签）来修改相关设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwuibdvxjyzCWvJxol5EPxMYnvJfBWbR4cZAicg9m6OTe5sLslhaCQib5cA/640?wx_fmt=png&from=appmsg)

作者对四台典型的设备——iPhone、高通（用了小米和Oppo手机）、三星的配置文件进行了提取分析，测试它们是否允许降级攻击，下图显示了各家设备安全问题，其中首先值得关注的是除了小米，其他三台设备都允许在连接到某些特定的运营商时使用768-bit的DH密钥交换，而这个密钥长度已经被学术界公认是不安全的！针对更多的运营商，所有四台设备都允许相对来说也不算安全的1024-bit的DH密钥交换，看起来运营商的安全滞后程度还是相当高的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwkEmOELibNq0rXv7FoTiaVAc7XOSp9RbxUJEpz63OW46De78jkJnggX5g/640?wx_fmt=png&from=appmsg)

作者还做了一个有意思的分析，那就是测试在配置文件中找不到对应的运营商时，DH密钥交换使用的默认参数是什么？下表展示了三大Android平台（高通、三星和Pixel）各家设备的情况，可以看到它们居然都允许使用现在已经认为是应该被淘汰（deprecated）的参数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwa7xiamLwTD7hJL6BTbNqq4l0hbc0tozTU7gA3UMXibRWpibzOorlrJ8nA/640?wx_fmt=png&from=appmsg)

针对DH密钥交换协议的攻击，有一个很关键的因素是攻击的时效性。因为DH密钥交换每次协商得到的密钥都是独立的，攻击者针对每一轮的密钥协商要进行独立的攻击。因此作者统计了各个设备在执行完DH密钥交换之后多久会进行密钥的更新，从下图可以看到，40%的三星设备差不多在10小时左右就会进行密钥更新，而iPhone要到至少22小时以后才会更新密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwgwrJraHbZXtGnh1vyf6y7sddMBdQvsibDicf1MIOovXkoamyyia4hloSg/640?wx_fmt=png&from=appmsg)

作者对423家运营商进行了分析，测试了它们的ePDG server，看到底这些服务器允许什么样的DH参数，实验的数据显示（如下图）大部分的ePDG server依然支持768-bit和1024-bit的DH密钥交换（3GPP规范中明确说了不支持这两类参数）。作者于是利用了自己开发的客户端去进行密钥协商测试，在表明客户端支持所有参数的情况下，强制选择1024-bit作为想要使用的参数，结果有41%的运营商服务器就“从了”。更奇怪的是，还有4%的运营商在这个时候不仅不要求客户端用更强的参数，反而会建议客户端选择更加弱鸡的768-bit参数……

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pwM5S5cfkjKp64542tbqvAdwVEgoPh6LA8FbzUHJ03JZAUK0icPFGT9aw/640?wx_fmt=png&from=appmsg)

最后，作者对VoWiFi生态中的各个实现进行了分析，发现了一堆问题，例如有14家ePDG server在DH密钥协商时候不是每次都随机使用相关参数，而是不停复用10个固定的值。而很多联发科（MediaTek）的设备上用来建立IPSec信道的二进制代码是从一个2014年版本的strongSwan编译得到的，而且它家的基带（Baseband）还允许攻击者进行中间人攻击来进行DH参数降级。我们不得不感叹，世界果然是一个巨大的草台班子！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21FVDAAEHKSEGtJT9wZzA5pw28u62ZHNBwhWl5OUd6B1h8xiaN1cgDKw1tr1m6SiarzGPbdVNqyfEkaw/640?wx_fmt=png&from=appmsg)

---

> 论文：https://publications.cispa.de/articles/conference\_contribution/Diffie\_Hellman\_Picture\_Show\_Key\_Exchange\_Stories\_from\_Commercial\_VoWiFi\_Deployments/26367205

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