---
title: 两块网卡=4倍速？揭秘Windows Server网卡绑定的那些坑与技巧
url: https://mp.weixin.qq.com/s/gEmfvg_xOs_r1CG9hSjKAA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:44.065032
---

# 两块网卡=4倍速？揭秘Windows Server网卡绑定的那些坑与技巧

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QukEKibHZiapNMvpxsIGfQVicEniatClhHBYLsPdNxBzQUKChrSoqtUV8FOQ/0?wx_fmt=jpeg)

# 两块网卡=4倍速？揭秘Windows Server网卡绑定的那些坑与技巧

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/f5u8u3lDeLchGaIcFTOuEzUYJyA2UibBrCNnQdjVEpYaZthELRW8oaiaUPXweZu61lAcOx0bWAPzhgJMibtaLaHVA/640?wx_fmt=gif)

正文共：1024 字 12 图，预估阅读时间：1 分钟

单丝不成线，独木不成林。在服务器运维的世界里，网络的稳定性就是生命线。

在网络设备上，为了提高可靠性，一般会配置**链路聚合（Link Aggregation）****（****[网络之路28：二层链路聚合](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458854396&idx=1&sn=2365f28bc244dfc0970e4b24912f4058&chksm=fc98aaf1cbef23e7b57595e5a10dd06dc6ad219ebb12f9db47a07d6d9f3e692ec83df4745502&scene=21#wechat_redirect)****）**，同样的，在服务器上也有**网卡绑定（bonding）**的技术。我们前面介绍了CentOS如何将两个或多个物理网卡通过bonding技术绑定在一起，从而创建一个虚拟的、逻辑上的网络接口，实现网络接口的聚合**（****[CentOS 7配置Bonding网卡绑定](http://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458854346&idx=1&sn=a850270bb426709b8311d98e87be378a&chksm=fc98aac7cbef23d11fe5073ba5a7c12f347688180724d2032eb33045f80409fbbfd04b58b43f&scene=21#wechat_redirect)****）**。

Windows系统日常使用也比较多，那Windows是否可以配置网卡绑定呢？我们今天以Windows Server 2019来操作一下。

在Windows Server中，网卡绑定通常称为**“NIC组合”**或**“NIC Teaming”**，用于实现带宽汇聚或冗余的效果。

配置前提：我们要确保服务器上配置NIC组合的两块或多块网卡型号一致、驱动版本一致，因为我是在虚拟环境进行配置，不涉及此问题，使用物理设备时一定要注意。如果是和交换机对接的情况下，需要在交换机设备侧也配置相应的聚合协议。

首先，我们在服务器管理器中，在**“本地服务器”**页面的**“属性”**区域，找到**“NIC 组合”**，默认处于禁用状态，点击右侧的**“已禁用”**按钮。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuwFbXrDceOLCMlelsgXqB8dP05tbCEgoa4oic0Uy5HkJ9o8fXKxu0C8A/640?wx_fmt=png&from=appmsg)

在打开的**“NIC 组合”**窗口的**“组”**区域，点击**“任务”**下的**“新建组”**按钮，创建一个新的NIC组合。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QubicKKbF6882wl9aam9Mibx7uFm150vaxo3Qj8S2FBeCDLianUU6f2xebw/640?wx_fmt=png&from=appmsg)

为NIC组合制定一个组名称，从可用的网卡列表中选择要加入组合的网卡，比如我现在展示的Ethernet0和Ethernet1。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuFfq1xibS2XpHy5owiccQ81x6a1HlRKKlZ97FNcqQvaiaUic2S6dS7dfbibA/640?wx_fmt=png&from=appmsg)

在这个页面，还可以配置其他高级属性：

成组模式默认配置为**“交换机独立”**，这是最省心的模式。网卡们在服务器内部抱团，完全不care交换机怎么想，甚至可以连在不同的交换机上，堪称自由恋爱；此外，还可以配置为**“静态成组”**，对应静态链路聚合，需要你在交换机上手动配置聚合，讲究一个门当户对；**“LACP”**模式则对应动态链路聚合，网卡和交换机之间会通过协议眉目传情，自动协商聚合，最智能但也最挑剔。

换句话说，交换机独立就像服务器和就交换机两个人各自打怪升级，不需要对方配合；而LACP就像两个人组队打副本，需要交换机开启LACP协议。

负载平衡模式默认配置为**“动态”**，指基于服务器的实时负载状态信息来决定流量的分配方式，比较灵活；此外，还可以配置为**“地址哈希”**，指利用报文特征（如源IP地址、目的IP地址、源端口、目的端口）计算一个哈希值，然后根据这个值将流量分配到不同的网络接口；还有**“Hyper-V端口”**模式，指利用Hyper-V虚拟机管理软件来搭建的负载均衡环境，适用于基于VMQ分配流量的虚拟化环境。

当成组模式为**“交换机独立”**时，还可以配置备用适配器，即配置成员网卡是工作在主备模式还是负载模式。

配置完成后，点击**“确定”**。此时，在NIC组合配置页面，我们可以看到已经创建好的NIC10组合接口，右侧则展示了处于NIC组合中的两个网卡的信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30Quc8DaFZAUY5xal5NhgIUznJicohh1ibSvGiaCINbllzlMcH2nxnxVURkDg/640?wx_fmt=png&from=appmsg)

然后我们通过运行**“ncpa.cpl”**打开**“网络连接”**页面，可以看到已经多了一个名为**“NIC10”**的网卡。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuNcNknQiaETjicyhpF5B0aiaQC5lguUb2O2P1LOzGPVuibQCQubAlf34FPg/640?wx_fmt=png&from=appmsg)

网卡的型号描述为**“Microsoft Network Adapter Multiplexor Driver”**，右击查看网卡状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuZwtdFr9xzafkl8km4QWmn73MEwmMvEGEDHVXeFoFicz68KUZrTuicX6A/640?wx_fmt=png&from=appmsg)

显示速度为2.0 Gbps，是两个成员网卡的总和。查看**“详细信息”**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuEjwqia3dvD1SOdwOkFUt4KmDZkcTEerh3uZvQPCpYMwqMPpT54TbWZg/640?wx_fmt=png&from=appmsg)

可以看到，网卡状态与之前完全一致，默认可以正常通过DHCP获取IP地址。

查看成员端口属性，现在仅使用了**“Microsoft网络适配器多路传送器协议”**，其他选项全都取消勾选了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuiaLVCibFm2HzUQ0icYDNUGvknbaXussQgJkmde71QYa0HQfPhQBFnyJew/640?wx_fmt=png&from=appmsg)

而正常使用的网卡，只有这一项没有勾选。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuORQy7FAh8q09p6fvn20iaIQbx3VmYNKWscvEedQjfnWz9fMsX6tmic1g/640?wx_fmt=png&from=appmsg)

为了不让IPv6拖后腿，我们还是把它雪藏起来吧。我们禁用网卡的IPv6选项，配置IPv4属性为静态IP地址，如下所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30Qu7Om7c5kkfhfII1JBO8coibkDKD9S16RbBNZnzXCMvrPZjCpVSb1X8Yw/640?wx_fmt=png&from=appmsg)

使用ipconfig命令查看网络配置，仅能看到NIC组合的配置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30QuB5nJ72UrIfRxLEB8QBuXGQyws2C8HJ3wOpusbzFF0VEtmPztU1udpg/640?wx_fmt=png&from=appmsg)

然后使用远程桌面连接服务器，测试一下网络访问。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5fL4uXAOMM6QWMxpHFhWbckPGRyv30Qu4QHVDX7ECiavyvQcSVq2VqETFOTUiauI8vN801kDJk5RYJsNmRVdZiaHQ/640?wx_fmt=png&from=appmsg)

网络连通性正常，服务和应用程序均能够通过新的NIC组合正常通信。

\*\*\*推荐阅读\*\*\*

[我们的WireGuard管理系统支持手机电脑了！全平台终端配置，支持扫码连接，一键搞定](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864213&idx=1&sn=ec85efce2a3b76ba244c71ccbdc09347&scene=21#wechat_redirect)

[保姆级教程：一条命令部署OpenVPN管理系统V4版，支持Win/Mac/安卓/iOS全平台接入](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864329&idx=1&sn=32eef6d6ce107136b389e05a4f206060&scene=21#wechat_redirect)

[成本省下99.7%！用40元的腾讯云服务器自建IPsecVPN，成功对接企业级飞塔防火墙](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864080&idx=1&sn=2de5d9d701d53b2c613b0c852329afb2&scene=21#wechat_redirect)

[别再乱选VPN了！实测数据告诉你：为什么L2TP是个“坑”](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865859&idx=1&sn=39ed55e57690feb1583a1a5bfb032b72&scene=21#wechat_redirect)

[SRv6部署第一坑：为什么配置了Locator却Ping不通？](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866771&idx=1&sn=cdee955a5a41b28b66e860c02ba78891&scene=21#wechat_redirect)

[嫌一键部署不过瘾？带你手搓Hermes智能体，主打一个通透](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866216&idx=1&sn=5826ca934825750b5bd102f9c53a4e2d&scene=21#wechat_redirect)

[十倍性能提升！Ubuntu 26.04深度实测：当VPP遇上OpenVPN，带宽直接冲破 6.5Gbps！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458867090&idx=1&sn=44e25115066e7a4d90ae3c019fd0472d&scene=21#wechat_redirect)

[VPP转发性能从10G暴增至24G？揭秘OpenEuler虚拟机的极限压榨术](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866146&idx=1&sn=3d1d7cbcb43967a986cb3e28bcef610b&scene=21#wechat_redirect)

[性能暴涨670 %！当WireGuard遇上VPP，带宽直冲7.4 Gbps！](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458867159&idx=1&sn=0c79b0c464c5fd41239fd16935067575&scene=21#wechat_redirect)

[手机也能跑DeepSeek-R1/Qwen3了：零成本搭建AI推理平台](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865100&idx=1&sn=ff8219a72e9800481c1e23911037e804&scene=21#wechat_redirect)

[2048卡昇腾910C集群算力集群交付工程手册](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458863852&idx=1&sn=ac753705858b85d06703dab5c42a3856&scene=21#wechat_redirect)

[2048卡H100算力中心100G无阻塞存储网建设方案](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458862851&idx=1&sn=7eabab449575723128152249370b069a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/5fL4uXAOMM7kUuIMJ8JGRicTGrVN3LAad2qWVLSLkZvOL0KSCibicfllib6L4g7Clp5vaZUhAgWoiahdV3kAHa2Wk6A/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

铁军哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5fL4uXAOMM65ich03QCp6qic3cwTmicnHZA49U7FN4y6cb4bY57OvvctIZH4ftcY5quyNfmPOvACGfVU5upxylUnQ/0?wx_fmt=png)

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