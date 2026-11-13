---
title: 以前网工排障靠经验，现在有了 AI，效率真的不一样了
url: https://mp.weixin.qq.com/s/OnLhhR9HwpgwJaQRibgTHw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:04:46.280076
---

# 以前网工排障靠经验，现在有了 AI，效率真的不一样了

# 以前网工排障靠经验，现在有了 AI，效率真的不一样了

原创

wljslmz瑞哥
wljslmz瑞哥

网络技术联盟站

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

做过网络工程师的都知道，配置网络设备其实不算最头疼的事情，真正让人头疼的是排障。

交换机突然不通、OSPF 邻居建立失败、VLAN 无法互访、ACL 配置后业务中断……这些问题看起来都不复杂，但真正遇到时，往往需要花不少时间才能找到原因。

以前遇到这种情况，基本靠经验。

先登录设备，查看接口状态，再检查 VLAN、路由表、ARP 表，接着翻配置、看日志，必要时还得抓包分析。有时候查了一圈，发现只是一个简单的配置遗漏。

现在不一样了，AI 开始成为网工手里的一个新工具。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba0669NYYKoL9uN3iaaaKJ5eNT44z9R32BUDscVtJ6CIojT5BRKkqJAVdN1ibXt8ZO8ouMAYEK0D9m1mJhrHgHQXSENdAsogavMk3s/640?wx_fmt=png&from=appmsg)

## 以前排障，先从一堆命令开始

举个很常见的例子。

某台交换机上配置了 VLAN 20，终端也接入了对应端口，但终端始终无法访问网关。

按照传统方式，工程师需要逐项检查：

```
display vlan 20
display interface brief
display current-configuration
display mac-address
display arp
```

如果是思科设备，对应的命令又有所不同：

```
show vlan brief
show interfaces status
show running-config
show mac address-table
show ip arp
```

这些命令相信网工都不陌生。

问题在于，设备配置可能有几百行甚至上千行，接口数量也不少。排障时需要把多个命令的输出放在一起对照，才能逐渐缩小故障范围。

对于经验丰富的工程师来说，这些工作已经形成了习惯。但对于刚入行的网工，光是确定应该执行哪些命令，就可能花费不少时间。

## 现在，把配置交给 AI 分析

还是刚才那个 VLAN 故障。

我们可以把设备配置、接口状态和相关命令输出提供给 ChatGPT、DeepSeek 等 AI 工具，让它协助分析。

例如，可以这样提问：

```
你是一名资深网络工程师。

目前有一台华为交换机，VLAN 20
中的终端无法访问网关。

请帮我分析以下配置：

1. 检查 VLAN 是否创建
2. 检查接口是否加入正确 VLAN
3. 检查 Trunk 是否允许 VLAN 20 通过
4. 检查网关配置是否存在问题
5. 给出下一步排查命令

以下是设备配置：
（粘贴配置内容）
```

AI 会根据提供的信息梳理配置关系，指出可能存在的问题，并给出下一步检查方向。

如果发现接口 VLAN 配置不一致，它可以提示检查 Access VLAN；如果涉及 Trunk 链路，也可以提醒检查允许通过的 VLAN 列表。

以前需要自己从大量配置中寻找线索，现在可以先让 AI 帮忙缩小范围。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04gTaicxLpaO0QaSfHStelBt0kSPNjUozLhPxOQkgqydTHtDQPOHrtgpficv7gpeFT4Fibn2v6Y6W8rff0HSMLG1zGZlVBlT3NxTk/640?wx_fmt=png&from=appmsg)

当然，AI 并不能仅凭一段配置就确认真实故障。设备运行状态、链路连接、对端配置等信息，仍然需要工程师进一步验证。

---

AI 对网工的帮助并不局限于故障分析。

日常工作中，还有很多重复性的任务可以让 AI 参与。

比如，配置交换机 VLAN，可以让 AI 根据需求生成命令；需要部署 OSPF，可以让 AI 按照网络拓扑生成基础配置；需要批量巡检，也可以让 AI 辅助编写 Python 脚本。

甚至遇到不同厂商的设备，需要查询命令时，也可以直接描述需求，让 AI 给出华为、华三、思科对应的命令参考。

这些工作以前需要查手册、翻资料，现在多了一个随时可以咨询的助手。

但有一点需要注意：AI 生成的配置不一定完全正确，不同设备型号、软件版本和命令环境都可能存在差异。尤其是生产环境，不能复制命令后直接执行，必须先检查、测试，再决定是否应用。

## AI 能提高效率，但替代不了网工的经验

我认为，AI 给网络工程师带来的最大变化，不是让网工不用学习命令了，而是让很多原本耗时的工作有了更高效的处理方式。

以前遇到故障，可能需要先查资料，再一点点分析；现在可以先让 AI 帮忙梳理思路，再结合设备实际情况验证。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04ibZIEraNsJzl1ibvXJuzoLvvs8ib91eTOpeBcdlHtOjkLND9PHoLnic7JM6ZiaiayZX9jSymDn3pXCOk7QCnPOA2qXqc4lNDcicEciaE/640?wx_fmt=png&from=appmsg)

但网络排障始终离不开基本功。

AI 可能会误判故障原因，也可能根据不完整的信息给出错误建议。对于涉及路由调整、ACL 修改、设备重启等操作，更不能盲目相信 AI。

未来的网工，既要懂网络原理，也要会使用 AI 工具。

**会配置、会排障是基本功，会利用 AI 提高工作效率，或许会成为网工新的竞争力。**

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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