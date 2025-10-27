---
title: G.O.S.S.I.P 阅读推荐 2025-02-24 你也可以AirTag！
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247499787&idx=1&sn=06e294103dd97ac7fef92bc368423dd9&chksm=c063eed2f71467c4b971cac58f1d6af102d3c7a8005fb239b590719109cac4fc569e69a4444b&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2025-02-25
fetch_date: 2025-10-06T20:38:12.488888
---

# G.O.S.S.I.P 阅读推荐 2025-02-24 你也可以AirTag！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uicdfzKrO21GKNibYYLAZngIS62ksh9H6eWicFxkicP3FLoZXibBJRaWWoqRJBQUmuhWtJkFj1U94QFlnsv1h5Ab7EA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2025-02-24 你也可以AirTag！

有一个朋友

安全研究GoSSIP

今天我们介绍的论文 *Tracking You from a Thousand Miles Away! Turning a Bluetooth Device into an Apple AirTag Without Root Privileges* 来自USENIX Security 2025，由乔治梅森大学研究团队（也是我们公众号的老读者，在此表示感谢！）投稿：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GKNibYYLAZngIS62ksh9H6eQpRNkgzsOBkKnrlFS9Pvh52dSqfdj7Wl8YlXgEicCGQpCRlcmkicUIcw/640?wx_fmt=png&from=appmsg)

作者在先前OpenHayStack（OHS）研究的基础上，对Apple「查找」（又称 Find My） 网络的安全机制进行了突破性研究，成功构建出完整且具备可复现性的新型攻击框架。如标题所述，它主要讲述利用 Find My 的一个漏洞， Linux、Android、Windows设备可能被恶意应用、情报机构或黑产利用，实现长期隐蔽追踪。作者强调他们的工作与以往的不同之处在于这个攻击无需提权，尤其在Linux上几乎无感。作为响应，Apple发布了一系列的安全补丁，在多达6款产品，共计9个系统（iOS 18.2、visionOS 2.2、iPadOS 17.7.3 和 18.2、watchOS 11.2、tvOS 18.2、macOS Ventura 13.7.2/Sonoma 14.7.2/Sequoia 15.2）中进行了修复，并对作者进行了特别感谢。

论文中首先简要介绍了 Apple Find My 的离线查找功能中各个角色的功能，接下来指出了前作、派生研究、甚至Apple所忽视的要点。尽管苹果规范要求使用随机静态地址（Random Static Address）广播丢失消息，但研究发现Find My网络实际接受**所有类型的BLE地址**。这一漏洞被作者发现并利用，绕过传统依赖root权限修改地址的限制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GKNibYYLAZngIS62ksh9H6ePVhLLnfNRGVctD9mOLrbLQvhJmKwbpK0rV2p7juPKHN4ecrK37oZZA/640?wx_fmt=png&from=appmsg)

Apple通过将公钥的**部分比特（46位）编码到BLE广播地址**中实现协议适配，传统方案（如OpenHaystack）需要主动修改蓝牙地址以匹配公钥，这通常需要root权限。而作者在威胁模型中限定为普通用户权限，因此创新性地采用**逆向碰撞思路**：不修改设备地址，转而生成与设备现有地址匹配的公私钥对。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GKNibYYLAZngIS62ksh9H6ekZmY2k5KGLO1ehIRq6c78ZafRm5qcFUE4rQUH0WVfOjthgicaOsKHgQ/640?wx_fmt=png&from=appmsg)

作者在文中指出，前作OHS和其众多派生研究均错误认为BLE 地址的2位最高位MSB即可判断蓝牙地址类型，而 Public Address 和Random Address 必须通过一个额外的标志位进行判断，即 TxAdd。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GKNibYYLAZngIS62ksh9H6eJ0DLy2he4YQsGVZL58UPEk3GuibMtDjBqn0BsoJBgI1icjMFYHx42sGg/640?wx_fmt=png&from=appmsg)

为证明方案可行，作者魔改了一个开源项目并对Apple使用的椭圆曲线SECP224R1进行了首次CUDA实现，使用GPU进行概率为1 / 2^46 的碰撞。作者对市面主流的GPU进行了性能和成本的评测，发现虽然RTX4090、A100、H100确实性能强悍，但是价格过于高昂，而与赛博朋克2077同期发售的RTX 3080 回报率最高。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GKNibYYLAZngIS62ksh9H6eqZRLBnzL1xtIIQM3YQ0Dia01xX9GDTOpFGJvhQicZHjtOhJ3qQ6R8OibQ/640?wx_fmt=png&from=appmsg)

论文中GPU性能对比数据显示，RTX 3080的密钥生成速率（4.9G Key/s）达到专业计算卡A100的54%，而租赁成本仅为A100的12.5%，其成本效益比显著优于其他硬件方案。假若把匹配比喻为抽卡，那么一块RTX 3080每秒可进行49亿抽且每小时成本仅需1.5元。作者使用了按分钟计费的云计算平台，租用200块GPU同时抽，仅需不到3分钟和16元的计算成本，抽到至少一个匹配的概率高达90%。~~比开箱子不知道划算到哪里去了~~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uicdfzKrO21GKNibYYLAZngIS62ksh9H6e7qtz58CxLJnFWxO7g7KgLx6dpUrT79nM4OJjd7B9vPmyicDpzUb8YAg/640?wx_fmt=png&from=appmsg)

在确保方案可行后，作者针对不同操作系统设计了两种攻击方案。其中Linux使用IEEE 分配的固定地址（Public Address）进行广播，导致攻击最易且持久。作者还为Linux的的攻击设计了彩虹表的方案，所有IEEE定义的地址所对应的私钥仅需一块硬盘即可存下，使得一次计算多次使用变得可行。而安卓和Windows由于使用了随机私有地址（Random Private Address）进行广播，导致可追踪的单次时间窗口较短，攻击成本虽更高但仍然现实可行。

作者在Evaluation章节对定位的延迟和精度进行了测试，并得出住宅区平均延迟8.09分钟和精度为3米的结论。 作者还在飞机上进行了追踪，通过19个定位报告结合在线工具推算了飞行轨迹。在论文结束前，作者还讨论了两个Tricks，包括攻击如何避免iPhone弹出被跟踪的提醒，以及如何在用户不知情的情况下打开蓝牙并进行追踪。作者的实验表明12个Linux 系统、安卓12以下，以及Windows 11 的设备均可被无感开启蓝牙。

值得一提的是，作者提及的前作OpenHaystack（OHS）在GitHub开源社区具有广泛影响力。该项目通过逆向工程AirTag的通信协议，创新性地实现了基于普通蓝牙设备的定位追踪方案，使得开发者能够以极低成本构建类AirTag的硬件装置。OHS强调需要使用Random Static Address，并为ESP32和树莓派做了PoC。令作者不解的是，他们的树莓派PoC却是通过修改Public Address的方式实现。该方案实质上无意间利用了今天介绍的这篇Paper提及的漏洞。令人遗憾的是，OHS作者团队仅将其定位为开源硬件项目，未能对底层协议漏洞进行系统性研究，错失了深入探索的机遇。

---

> 项目网站：https://nroottag.github.io/

> 论文地址：https://cs.gmu.edu/~zeng/papers/2025-security-nrootgag.pdf

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