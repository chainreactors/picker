---
title: 集中式网关和分布式网关有啥区别？
url: https://mp.weixin.qq.com/s/Ku0vXNdTj0A3dPXU4Vgojg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:15:18.560014
---

# 集中式网关和分布式网关有啥区别？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vf29dJy0S59lkFCRgX2W5NkXoicMBz4W161EjibMibkIeiapdQZMc1Bp6PibsXsemUUlAutpvMXicVuraQEl5jficXnWIHVNibPR1PQw1SY2NugM51c/0?wx_fmt=jpeg)

# 集中式网关和分布式网关有啥区别？

原创

圈圈
圈圈

网络技术干货圈

![]()

在小说阅读器中沉浸阅读

点击上方 网络技术干货圈，选择 设为星标

优质文章，及时送达

![](https://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT9z1qCg1V9MbsCSdmUBkOicVRmk5T6j0m8Z8L9YdmdU0crxLkBG4994IkXaZTrSnJAZksCicKaqO43g/640?wx_fmt=png)

> 转载请注明以下内容：
>
> **来源**：公众号【网络技术干货圈】
>
> **作者**：圈圈
>
> **ID**：wljsghq

在数据中心网络中，网关通常指**三层网关（L3 Gateway）**，负责虚拟网络（Overlay）和物理网络（Underlay）之间的路由互通。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ibVpWCDeQAv2tws9UR9NPywibAq8KOh9A450t3KWGrkelS0yHQNfo4s4MBHiabyff83wsoZficVHWQqy89V52WDmK004C21Q9xNpY/640?wx_fmt=png&from=appmsg)

具体来说：

虚拟机/容器所在的VLAN 或 VXLAN 网络（通常是租户隔离的Overlay网络）需要和外部（其他租户、互联网、上层服务）通信时，必须经过三层网关完成路由。

网关既要终结Overlay封装（比如VXLAN解封装），又要完成IP路由，还要处理NAT、防火墙、负载均衡等策略。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ibhiavSKd9g954IWricFf8fLwQkIphIY78yXIZjIC2HPX2EAMebTDxG1UumOgDtyPfQundo5qHkI3cVcYsttcYHUJT6UGSJa1Gq0/640?wx_fmt=png&from=appmsg)

网关可以分为两类实现方式：

**集中式网关**：

所有南北向流量（进出Overlay网络的流量）都必须经过少数几个专用的网关节点处理。

**分布式网关**：

每个计算节点（Hypervisor 或宿主机）都具备网关功能，南北向流量可以就近在本地完成路由和封装处理。

## 集中式网关

集中式网关的典型形态是：部署几台专用设备或虚拟机作为网关节点（可以是硬件 appliance，如Cisco ASR、Juniper MX，也可以是虚拟网关，如VMware NSX Edge、OpenStack Neutron L3 Agent）。

所有租户的南北向流量必须被“吸引”到这些网关节点：

* Overlay网络内部的路由协议（如BGP EVPN）会把默认路由或外部路由通告给集中网关。
* 计算节点上的虚拟交换机（OVS、Linux Bridge）会把未知目的地的流量通过隧道发送到网关节点。
* 网关节点完成解封装 → 路由 → 再封装 → 发送到Underlay或外部。

典型拓扑示意：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5icaicMd1Bz9UW1ScBb6X3NJZBBsEF222F6rzYqgIRfjavA50D8dkUwW80Joq2nrmFxk1Qziciacy0edibSMbfGHDLd3icvxMDnUvoibw/640?wx_fmt=png&from=appmsg)

### 优点

1. **管理简单**：所有策略（ACL、NAT、QoS、LB）都集中在少数节点，配置、审计、排查问题非常直观。
2. **功能集中**：容易在网关上堆叠高级特性（如状态防火墙、DPI、IDS/IPS、Service Chain），因为资源可以集中分配。
3. **实现成本低**：早期OpenStack、NSX等方案默认就是集中式，很多传统网络工程师上手快。
4. **适合中小规模**：当租户数量不多、流量不大时，性能完全够用。

### 缺点

1. **单点故障风险**：即使做了HA（Active/Active或Active/Standby），网关节点仍是流量汇聚点，一旦故障影响面极大。
2. **性能瓶颈**：所有南北向流量都要经过网关，网关的CPU、内存、网卡带宽成为整个网络的咽喉。常见现象是网关节点网卡打满、CPU 100%，而计算节点还很空闲。
3. **东西向+南北向混合拥塞**：在Underlay网络中，计算节点到网关的隧道流量和东西向流量争抢带宽，导致延迟抖动。
4. **扩展困难**：需要新增网关节点时，涉及路由通告调整、隧道重建、状态同步，操作复杂且有风险。
5. **跨AZ/Region延迟高**：如果网关放在一个AZ，其他AZ的VM访问外部要跨区绕行，延迟明显增加。

## 分布式网关

分布式网关的核心思想是“把网关功能下沉到每一个计算节点”。

每个宿主机（Hypervisor）上都运行轻量级的网关实例（通常是OVS或VPP里的路由进程 + BGP/EVPN Agent），它们通过控制平面（如BGP EVPN）从集中控制器或路由反射器学习到外部路由。

当VM发出南北向流量时：

* 本地宿主机的网关实例直接完成路由决策。
* 本地完成VXLAN封装/解封装。
* 直接通过Underlay路由发送到外部网络或目标宿主机。

关键点在于：**外部路由被通告到每一个计算节点**，所以每个节点都拥有完整的路由能力。

典型拓扑示意：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S59gm5WBDeEENIvVQcEhhQKCSibcef8VZgk2AwcEbSibKPicz6HibKGD6jhovE693a3SWNWmntkzsmTzI8sA7N7tIc2jG8BYkfxM4XA/640?wx_fmt=png&from=appmsg)

### 优点

1. **极高的可扩展性**：随着计算节点线性增加，网关能力也线性扩展，没有单点瓶颈。
2. **低延迟**：南北向流量就近处理，无需绕行到专用网关节点，通常能降低5~20ms延迟。
3. **高可用性**：没有集中故障点，单个宿主机故障只影响本地VM，外部路由通过BGP撤回即可。
4. **带宽利用率高**：流量分散在所有Underlay链路上，充分利用叶脊网络的ECMP能力。
5. **跨AZ天然友好**：每个AZ的宿主机都有网关功能，跨AZ访问外部不需要额外绕行。
6. **东西向流量不受影响**：南北向不再和东西向争抢特定链路。

### 缺点

1. **管理复杂度高**：策略需要下发到每一个计算节点，配置一致性、版本同步、审计难度大幅增加。
2. **状态策略支持受限**：有状态防火墙、NAT、LB等需要会话状态同步的功能，在分布式场景下实现成本极高（通常只能做无状态或借助外部Service Node）。
3. **控制平面压力大**：每个节点都要运行BGP/EVPN，会增加控制平面开销，需要强大的Route Reflector或控制器。
4. **调试困难**：问题可能出现在任意节点，排查时需要跨节点追踪流量路径。

## 集中式 vs 分布式

| 维度 | 集中式网关 | 分布式网关 | 胜出方 |
| --- | --- | --- | --- |
| 可扩展性 | 差（受网关节点性能限制） | 优秀（随计算节点线性扩展） | 分布式 |
| 性能（吞吐/延迟） | 中等（有汇聚瓶颈） | 高（就近处理） | 分布式 |
| 高可用性 | 中等（依赖HA集群） | 高（无单点） | 分布式 |
| 管理复杂度 | 低（集中配置） | 高（分布式一致性） | 集中式 |
| 高级功能支持 | 优秀（状态防火墙、LB、DPI易实现） | 受限（有状态功能难实现） | 集中式 |
| 东西向流量影响 | 大（争抢链路） | 几乎无影响 | 分布式 |
| 跨AZ/Region支持 | 差（需额外设计） | 原生支持 | 分布式 |
| 实施难度 | 低（传统方案成熟） | 高（需要EVPN、控制器支持） | 集中式 |
| 适合规模 | 小中型（<500节点） | 大规模（>1000节点） | - |

我之前负责一个金融客户的私有云，初期300节点，用集中式网关（NSX Edge集群），一切正常。后来扩容到1500节点，南北向流量达到80Gbps，Edge节点频繁打满，延迟飙升到15ms。我们最终迁移到分布式Tier-0架构，性能提升3倍，延迟降到3ms以内，彻底解决了瓶颈。

另一个项目是互联网客户，租户多、需要大量状态防火墙和NAT，我们保留了集中式网关+分布式路由的混合模式：东西向和大部分南北向走分布式，只有需要状态策略的流量强制Hairpin到集中网关。

什么时候选哪种方案？

我的决策框架，供大家参考：

1. **规模 < 500节点，流量 < 40Gbps，运维团队小** → 优先集中式，快速上线、易维护。
2. **规模 > 1000节点，或对延迟敏感（如AI训练、游戏）** → 必须分布式。
3. **需要大量有状态服务（状态防火墙、NAT、LB）** → 集中式或混合模式。
4. **多AZ/跨地域部署** → 分布式几乎是唯一选择。
5. **预算充足、团队技术强** → 可以考虑混合架构：分布式处理大多数流量，集中式处理高级功能（类似NSX-T的Active-Standby Edge + Distributed Router）。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S58rTjz4bRwmggn9BcugzeE37Z4gYMFSebsxfYe0ahxfuIWeZmia2UpCMJD7hwF0iay6jchxkicpDKTpN72QIgGBC7Vpz3tbk63Ihc/640?wx_fmt=png&from=appmsg)

集中式网关和分布式网关没有绝对的好坏，只有适合的场景。集中式像“中央枢纽站”，简单可靠但有瓶颈；分布式像“遍地开花的高速公路出口”，高性能高可用但复杂。

在设计网络架构时，一定要结合业务规模、性能需求、运维能力综合评估。选错了，可能要花几倍的代价重构。

希望今天的分享对大家有帮助！欢迎在评论区讨论你们的项目中用的是哪种方案，遇到了什么坑？

# **---END---** **重磅！网络技术干货圈-技术交流群已成立** 扫码可添加小编微信，**申请进****群。** **一定要备注：****工种+地点+学校/公司+昵称****（如网络工程师+南京+苏宁+猪八戒）**，根据格式备注，可更快被通过且邀请进群 ![](https://mmbiz.qpic.cn/mmbiz_jpg/p8No8ScJKT94LpPQZiap0D6hj7eQmHdDUQEvWdRGMD2ic4JQ2Gq8cibgVt0TgPeRfG7OoP3doq9023GkcecKBCW2A/640?wx_fmt=jpeg) ▲长按加群

![](https://mmbiz.qpic.cn/mmbiz_gif/p8No8ScJKT91zHQia5QWRMJhVxUyF4g3ZAuv0YbUEoiaVCzgE2gQT6eQC0Hx6icUE9HQbqFfVP3sSqbIUksF1Ojrg/640?wx_fmt=gif)

预览时标签不可点

内容含AI生成图片

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

网络技术干货圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

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