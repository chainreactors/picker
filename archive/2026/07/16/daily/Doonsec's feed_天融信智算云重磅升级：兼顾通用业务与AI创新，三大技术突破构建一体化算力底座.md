---
title: 天融信智算云重磅升级：兼顾通用业务与AI创新，三大技术突破构建一体化算力底座
url: https://mp.weixin.qq.com/s/cR7P2hosbmh8gLEwLECAww
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:57:24.970223
---

# 天融信智算云重磅升级：兼顾通用业务与AI创新，三大技术突破构建一体化算力底座

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dSWSuPicfjTc26QiaXS3BHSgzA9hvhXF1BgqOhia9oZUrzuZExicxjYeX8K1qnetgIO2Xpeic9e7A5gxMWWZMNnp2wibKcyG3tBMJqxcP2rUFhWgc/0?wx_fmt=jpeg)

# 天融信智算云重磅升级：兼顾通用业务与AI创新，三大技术突破构建一体化算力底座

天融信

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/nJmicCz2NYxNibMqIOfXMnZxbVBPBGKu3pficMjqFslyVdhUYhSozJ0egjyKoezIaK9qEyYy6ttzMv3T5Kiasiae7icg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

7月16日，以“信创筑基 AI赋能-粤网安护航大湾区高质量发展”为主题的第三届粤网安·网络安全新技术交流大会在广州开幕，会上，天融信智算云平台V3.9.0重磅发布！

![](https://mmbiz.qpic.cn/mmbiz_png/dSWSuPicfjTcQFvO6dicXgXK8HgvTQYyzd7eCbcdOBicarPqZicyBNIFgT43CrdMxoHicl8FniaIBPoo2KIick5LHeAPcKLhPXtMshg58xh73yJk5Q/640?wx_fmt=png&from=appmsg)

如今，生成式AI席卷千行百业，政企单位数据中心正经历一场前所未有的架构变革。一方面，财务、ERP等核心业务需要稳定的通用算力支撑；另一方面，新兴的大模型训练与AI推理工作负载正快速涌现。

面对“通用业务+AI创新”并行的双重挑战，传统烟囱式IT建设极易形成算力孤岛与管理割裂。在此背景下，能够同时承载传统核心业务与AI应用的一体化新型基础设施，已成为政企数字化转型的刚需。

**天融信智算云平台V3.9.0**

**驱动全栈融算能力跃迁升级**

天融信智算云平台V3.9.0正式发布，意味着以此为技术底座的天融信太行云全栈IT基础设施家族全面迈入5.0时代。会上，天融信科技集团产品总监蔡立宇深度解读天融信智算云平台V3.9.0核心能力，并且同步介绍了太行云5.0产品。

![](https://mmbiz.qpic.cn/mmbiz_jpg/dSWSuPicfjTdpvZdKg6ZS3Dib0MhysqYtcQRgHFE24n5nqa0wDNM9qlTP5FibJNfgRsgB0FJ16UugKIwqx0OyfRHb4hwwFUu2MUaVehUHiaD27I/640?wx_fmt=jpeg)

**智算升级：**

**分布式推理能力提升，突破显存与性能瓶颈**

随着企业引入的大模型参数量呈指数级增长，AI推理规模化部署正迎来双重严峻考验：一是单台服务器算力卡显存容量有限，装载完整的超大模型面临“显存墙”瓶颈；二是面对海量业务访问，单机算力往往无法满足高并发性能需求。

天融信智算云平台V3.9.0重点升级了分布式推理能力。产品全新支持“全互联分布式推理”与“多实例弹性推理”两种主流部署模式，企业可根据模型大小、性能要求和成本预算灵活选择，实现算力资源的最优配置：

* 全互联分布式推理，打破物理显存瓶颈：针对超大型AI模型“装不下”的痛点，系统通过高性能网络将多台服务器中的所有算力卡实现全互联。通过将超大规模模型智能切分并分布式部署至多台服务器上，有效突破了单机显存限制，让超大规模参数的大模型也能在集群中稳定运行。
* 多实例弹性推理，横向扩展应对高并发：针对单机能够装载但性能不足的场景，平台提供强大的横向扩展能力。结合“智能路由”与“副本控制器”，系统可根据业务请求量动态增删容器推理副本。

此外，在智能路由调度的基础上，产品新增KV Cache感知、Prefix Cache感知及LoRA亲和等核心调度算法，可实时感知集群负载与缓存资源分布。系统将携带相同上下文或使用同一LoRA权重的推理请求，精准路由至最合适副本节点，高效复用缓存并减少权重切换开销。该双模式方案在保障推理延迟的前提下，显著提升了系统的吞吐量、服务能力与可用性，保障大模型应用的高效顺畅。

**通算破局：**

**智能内存分层，解锁算力“扩容自由”**

在支撑传统业务的超融合通算场景中，政企客户常面临典型的资源错配：CPU算力尚有富余，但昂贵的物理内存（DRAM）却率先耗尽，成为制约虚拟机部署密度、推高硬件成本的短板。

针对这一痛点，天融信智算云平台V3.9.0引入“DRAM+NVMe”智能内存分层技术，将高速固态盘作为物理内存的延伸。系统在虚拟化层通过冷热数据智能识别与动态压力感知，自动将低频访问的冷数据透明下沉至NVMe存储，将宝贵的物理内存留给核心高频业务。

整个过程对业务与虚拟机完全透明，无需任何应用改造，即可在极低硬件成本下显著提升有效内存容量，大幅提高单台宿主机的部署密度。针对核心业务，也可通过精细化的策略配置保障热数据常驻DRAM，在确保性能稳定的同时，最大化资源利用率，真正实现降本增效。

**桌面革新：**

**升级IDV架构，重塑边缘计算体验**

在医疗收费、制造产线等复杂边缘场景中，传统VDI（虚拟桌面）高度依赖网络带宽，且在重载3D渲染及复杂外设兼容性上存在明显短板。

为打通全栈算力的“最后一公里”，天融信智算云平台V3.9.0全面升级IDV（智能桌面虚拟化）架构。IDV秉持“集中管理、分布运算”理念，计算负载直接运行在终端本地。通过充分调用终端的CPU、内存与GPU资源，可流畅支撑AutoCAD、3D建模等图形应用，性能免受云端网络带宽限制。

同时，IDV模式具备天然的离线高可用能力。即使机房网络突发中断，终端也可依托本地镜像持续运行，保障门诊接诊、产线制造等核心业务不断线。在外设适配方面，IDV采用原生接入机制，完美兼容密码键盘、高拍仪、工控串口等专业设备，化解边缘业务的接入难题。

依托“融算一体”架构打破算力壁垒，天融信太行云5.0形成覆盖三大核心场景的完整产品矩阵：面向大模型的智算云、承载传统高并发业务的超融合通算平台、覆盖边缘终端的桌面云。通过从数据中心到边缘端的统一调度，产品为政企客户构建了兼顾稳定与创新的一体化算力体系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dSWSuPicfjTficAo777DKYp3umtibWHICVTR2cplicerKTZO2uPHfgTsCWv5Io7MN2LTm9Aicd62qhsucCMgGr5EicxiboaPkVv2InicNaFB94Hqt68/640?wx_fmt=png&from=appmsg)

从突破大模型部署瓶颈的分布式推理，到提升资源效率的智能内存分层，再到保障边缘业务连续性的IDV架构，天融信太行云5.0以智算云平台V3.9.0为技术内核，持续演进全栈融算能力，为千行百业打造安全、高效、智能的算力底座。

数智浪潮奔涌向前，作为网络安全与智算云解决方案提供商，天融信将紧扣行业发展与技术创新需求，以“安全+智算”双轮驱动，携手产学研用各方力量，共筑繁荣共生的数字生态，助力粤港澳大湾区网络安全产业高质量发展。

近期热点

[全国首批、级别最高！天融信获AI服务安全能力评定“建设+检测”双证](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650990796&idx=1&sn=5bad1cc3358fc23b1de5f65f6514f613&scene=21#wechat_redirect)

[坚如磐石！揭秘一台天融信防火墙连续运行21年背后的硬核技术](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650989764&idx=1&sn=c9d25ea82de1b13161c0d66af1af4430&scene=21#wechat_redirect)

[天融信连续11届获CNCERT最高级支撑单位，重点技术领域入选最多！](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650988569&idx=1&sn=741f5cdd4851841f7bed5522b62b5185&scene=21#wechat_redirect)

[国家级认可！天融信获评CNNVD「核心+一级」技术支撑单位](https://mp.weixin.qq.com/s?__biz=MzA3OTMxNTcxNA==&mid=2650989027&idx=1&sn=699e947882aa0a8e22b38ae598704edb&scene=21#wechat_redirect)

**关注天融信了解更多信息**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/dSWSuPicfjTfMTWicc8vjaOqbhhrKehADyT8bNDMKcj3HRo43hWskicsVDx0v5AIybW780yVwklGZIgsI8d7rU2QveGyUnE08BFQ6YHTiaI2DEs/640?wx_fmt=gif&from=appmsg#imgIndex=2)

![](https://mmbiz.qpic.cn/mmbiz_gif/dSWSuPicfjTch4xDfDkudNeE2ejFmFFlP2aXic9unoe8RnpINgNzfOoczYWndia6D5nLW8jAFAXsXYs9jVVqNozeYE4JshxcpyjlVk1jY6GE84/640?wx_fmt=gif&from=appmsg#imgIndex=3)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/dSWSuPicfjTd2lEcLMGdLD9jnKfdcKH98RiaxZhnQHEHVn3ES0B7975o0vlNOV7iaicXMIq8AsBV8QW6zUnBhtEOJdIhmgPicnISd9yHTPjN504o/640?wx_fmt=gif&from=appmsg#imgIndex=4)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nJmicCz2NYxPiazyASKVba57ReFHFEqicHGum3FRLQza0a8624LIibogluysp3HQgcztqd1HUchOdIDwak46dKT1IQ/0?wx_fmt=png)

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