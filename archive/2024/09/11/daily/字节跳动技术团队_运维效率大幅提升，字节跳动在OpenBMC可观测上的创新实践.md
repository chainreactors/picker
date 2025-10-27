---
title: 运维效率大幅提升，字节跳动在OpenBMC可观测上的创新实践
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247510098&idx=2&sn=bde62b143b86c8973041fb9baa3b8941&chksm=e9d363b0dea4eaa63b137f1d0102f394a943b6bf02b9b2d368d8bb03c34aa9de677fc88a2977&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-09-11
fetch_date: 2025-10-06T18:29:47.978186
---

# 运维效率大幅提升，字节跳动在OpenBMC可观测上的创新实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOjZKEowbUAvn4gPzz4hROgKvZZpwJOBzzgHnACibreKMlWSvLy7jk375Rc5BiagsxtG3CKdICyhN7EA/0?wx_fmt=jpeg)

# 运维效率大幅提升，字节跳动在OpenBMC可观测上的创新实践

溜达兔

字节跳动技术团队

在日前举办的 2024 开放计算中国峰会上，字节跳动获得了 OCP 组织颁发的开放计算最佳实践奖，这代表了 OCP 乃至整个行业对于字节跳动在推动开放计算发展层面的认可，也侧面说明了字节跳动在数据中心基础设施领域的深厚实力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nPoNzfB8iaFYjPV0qVQaKXkXq1aQqK1ehMoDmzIoibGNlnibib87RIGicljKvQyptuxibWWbW7q9MZYuiauicXomDfUDNw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

提起字节跳动，许多人可能会直接联想到“抖音”或者“豆包”，如今这些应用已经深入我们的生活与工作，变得多彩和高效。但其实除了这两款应用之外，字节跳动也在不断推动更多好的、酷炫的创意应用落地，不断优化网友们的应用体验。这些应用之所以能够稳定、安全地运行，其中基础设施提供了坚实的技术支撑。

随着应用覆盖范围的进一步扩大、用户群体的持续增多，字节跳动需要维护的基础设施服务器数量已达百万级别，并且仍有不断增长的态势。在此情形下，怎样高效、稳定且安全地管理服务器，成为了系统运维面临的首要问题。在此次峰会上，字节跳动固件架构师郏春辉分享了字节跳动在 BMC 可观测技术方面的探索创新：在开源 OpenBMC 方案基础上，结合  Perfetto 和 Kernel trace 两种技术手段增强可观测性。

*![](https://mmbiz.qpic.cn/sz_mmbiz_png/nPoNzfB8iaFYjPV0qVQaKXkXq1aQqK1ehzIE1fWB2yqyQzsBPZdVja6WdPF6bFGyGHQ1b8dia9sjuOvoCuz5f5Rw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)字节跳动固件架构师 郏春辉*

**拥抱开源，积极推进技术升级与创新**

正如我们前面所提及的，像字节跳动这类的互联网大厂，由于众多业务布局的缘故，通常拥有数量庞大的服务器设备，线上问题通常有并发时序复杂、配置复杂、调试受限等困难。然而，伴随着应用场景的增多，这些设备的管理与运维也变成了棘手的难题。

“传统 BMC 存在灵活性和选择范围受限、交付周期长等缺点，在当下服务器开发越来越多样化的场景下，难以满足业务的交付需求。”在谈到传统 BMC 缺陷的时候，郏春辉解释说。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nPoNzfB8iaFYjPV0qVQaKXkXq1aQqK1ehSnKc5LaABLjKMGo3RxiaNiaTDlh1Rzyib8Ah9ILvYPInjAovbt8NbHXMA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

其实不仅仅是字节跳动，其他互联网公司也都遇到了类似的问题，而大家也希望在开源框架下找到一款灵活、开放、稳定、安全的固件解决方案，于是大家都将目光瞄准了 OpenBMC 。

OpenBMC 的历史最早可以追溯到 2014 年某次黑客松的活动上，但真正作为一个项目进行推广并成功落地，还要等到 2018 年 3 月——彼时 OpenBMC 正式成为 Linux Foundation 项目，包括微软、英特尔、IBM、谷歌、Facebook（现改名 Meta ）等众多科技大厂都为其摇旗呐喊，也才有了今天欣欣向荣的发展势头。

究其原因，还是 OpenBMC 自身打破了传统 BMC 的诸多弊端。首先，其开源的优势在于能够接受来自业界不同企业与个人的代码贡献，并且可以吸纳业界的先进理念和应用。这也使得 OpenBMC 具备架构灵活、兼容性强、安全稳定等特性，社区成员的贡献也使其能够快速迭代、快速响应，非常适合当下互联网与数字化的应用需求。

综上所属，传统 BMC 虽然可以实现部分管理，但是在快速迭代的当今尤其是在 AI 技术的驱动下，存在开发周期长、交付困难、应用单一等难题，在遇到问题的时候很难复现，配置复杂技术相对落后。而开源 OpenBMC  的出现提供了架构灵活、兼容性强的新选择，整个行业也都开始转型，可以更好的迎合业务需求。

**软硬结合，让故障排查立竿见影**

字节跳动以开源 OpenBMC 方案为基础，持续开展技术创新，重点关注固件可观测性，即对固件运行状态、性能表现以及内部各种活动进行有效监测和理解。如此一来，字节跳动的固件团队可以通过观测问题发生时的软硬件状态，定位和解决问题。要想实现这一点，必须双管齐下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nPoNzfB8iaFYjPV0qVQaKXkXq1aQqK1ehRCMSx6yeibqucJuVicPWUjQ1FZSx6qoZL5X6Qslh0q3dAPn0Ryw8F8xA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

字节跳动在固件可观测层面分别从硬件和软件两个维度准备。软件维度使用的 Perfetto，这是一款用于系统跟踪和性能分析的工具，可以实现内核跟踪、空间跟踪和系统服务集成。这样，每一个 OpenBMC 组件都可以通过 Perfetto 将数据通过共享内存的方法先统一存储在本地，之后传输到远端的服务器上进一步分析处理。

“我们之所以选用 Perfetto 的重要一个原因，是为嵌入式场景所设计的，在设计之初的时候考虑到了低开销的需求，因此在内部采用像 ProtoBuf 和 String interning 这样的技术减少重复字符串，基本上来讲可以使得采集的开销达到最小”，郏春辉解释说。

当然除此之外，字节跳动也还有非常灵活的数据采集策略，可以通过自定义的方式指定对某个系统范围的某方面数据进行抓取，进而在特定的进程上采集数据，不需要重新编译固件本身。之后对数据的进一步处理，既可以通过 UI 的方式可视化地分析采集到的数据，也可以通过脚本的方式做处理。

最后，设计实现了系统里面各种高精度事件的采集和记录，包括 CPU 的调度、IO 活动等等，时间精度可以达到纳秒级别，在定位问题的时候可以看到问题发生前后精确的顺序，以及了解它背后隐含的依赖关系。

得益于 Perfetto trace 本身就二进制数据的特性，天然就具备了开销低的特点，因此无论是保存在内存数据库中还是通过外部的分析程序调用，都可以达到高效、低成本的优势，从而实现了自动化分析的目的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nPoNzfB8iaFYjPV0qVQaKXkXq1aQqK1eh9XOCRP43rpQjxOoNheRpibnjwpyBNXictia815qz9hCGUR4w7j9PCkiaxQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

除了软件维度之外，在硬件接口维度，字节跳动也携手浪潮信息进行了进一步的优化。主要采用了 Kernel Trace的解决方案，可以通过 trace-enable 模块并配置一键日志的方式快速收集，大大提升了应用效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nPoNzfB8iaFYjPV0qVQaKXkXq1aQqK1ehUvpmNfRFibuPs8ic4H8BIff2uvPTpAa9oTcuvgHesMWPMicibQticmM3nUw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

每当遇到硬件故障或者报警时，在 BMC 层面都可以记录 BMC 和传感器之间所有的原始通讯信息，并基于这些信息快速判断，快速判断究竟是软件 Bug、传感器故障亦或是链路异常，整个处理过程也可以达到秒级响应。确定了具体的问题之后，会有专业的硬件工程师进行排除，借助于系统的精准定位快速解决。

事实证明，这种软硬件结合的方式非常有效。在引入了 Perfetto 和 Kernel trace 以后，每个 Bug 或者故障都实现了可观测。正所谓“知己知彼百战不殆”，将故障“透明化”之后，处理故障的效率也随之大大提升。其中，问题定位分析时间，由原有的数小时乃至数天，降低至平均 1 小时以下；问题一次定位分析准确率，由 40% 提升至 80% 以上，效率提升非常明显。

基于上述可观测技术，字节跳动面向百万规模服务器管理运维难题得以有效应对，运维时间大幅缩减，运维难度显著降低。不过，固件可观测的优势远不止于此。在展望未来时，郏春辉指出，字节跳动未来还会在问题分析定位层面更进一步，尤其是借助AI 技术的长处，引入大数据分析，细化不同场景下的问题定位，充分发挥自动化优势，让故障无处遁形。

由此看来，OpenBMC 已经成为互联网大厂不可或缺的开源技术，确实让超大规模数据中心的运维变得更为简单、高效。面向未来，字节跳动将持续推进 OpenBMC 的应用，并与浪潮信息等社区成员携手，加强合作与交流，共同推动整个行业的技术创新和应用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

字节跳动技术团队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5EcwYhllQOhkoWTP1gVm0Lqs480XOARyoSYjPEsRVCSF35cbWIp6cliaYic8KUfNfiaSjVnruzTQUTCA0lmv9vUmw/0?wx_fmt=png)

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