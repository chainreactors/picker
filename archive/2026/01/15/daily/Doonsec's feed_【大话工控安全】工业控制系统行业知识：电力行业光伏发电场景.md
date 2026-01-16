---
title: 【大话工控安全】工业控制系统行业知识：电力行业光伏发电场景
url: https://mp.weixin.qq.com/s/Nb9GbNTijcoCYi-ZNwEeZA
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:59.167058
---

# 【大话工控安全】工业控制系统行业知识：电力行业光伏发电场景

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icKb2wsWzy9P5sDaG5YlRuyTxaYEmoVnAIZgMgvRlbSYq8Ejg9Dic68SQQMxyo24vFdEvfs7iazNFhSvjrpibdPRsw/0?wx_fmt=jpeg)

# 【大话工控安全】工业控制系统行业知识：电力行业光伏发电场景

原创

老付话安全
老付话安全

老付话安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9NPowYOibGDTvxBicLHHAStUETOAGJItrJk4egragrk7IjBCjl8oIa2F0wr1DejU4nQibnvGFzcwI6wg/640?from=appmsg)

点击上方蓝字关注我

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9NPowYOibGDTvxBicLHHAStUEXXAzmfJXgB4wTpJq9DBzkS6Q0yyvZxmtzk8wT2WBv1Kf9syurd6lpA/640?from=appmsg)

光伏电站监控系统是以计算机、通讯设备、测控单元为基本工具，为光伏电站生产的实时数据采集、开关状态检测及远程控制提供了基础平台，它可以和检测、控制设备构成任意复杂的监控系统，在光伏电站监控中发挥了核心作用，可以帮助企业消除孤岛、降低运作成本，提高生产效率，加快变配电过程中的反应速度。

光伏电站监控系统包括如下：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 序号 | 业务系统及设备 | 控制区 | 非控制区 | 管理大区 | 备注 |
| 1 | 光伏电站运行监控系统 | 电站运行监控 |  |  | A2 |
| 2 | 无功电压控制 | 无功电压控制功能 |  |  | A1 |
| 3 | 发电功率控制 | 发电功率控制功能 |  |  | A1 |
| 4 | 升压站监控系统 | 升压站监控功能 |  |  | A1 |
| 5 | 相量测量装置PMU | PMU |  |  | B |
| 6 | 继电保护 | 继电保护装置及管理终端 |  |  | B |
| 7 | 故障录波 |  | 故障录波装置 |  | B |
| 8 | 电能量采集装置 |  | 电能量采集装置 |  | A1、B |
| 9 | 光伏功率预测系统 |  | 光伏功率预测 |  | A1 |
| 10 | 天气预报系统 |  |  | 数字天气预报 | A2 |
| 11 | 管理信息系统 |  |  | 管理信息系统 | A2 |

A1:与调度中心有关的电力监控系统

A2:电厂内部监控系统

B:调度中心监控系统有关的厂站测设备

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9P5sDaG5YlRuyTxaYEmoVnABVTiapicibSeKko2OT3bdIa7T3UZ5RX6mr6aibKeW0epJjWSTfWoGHicJLw/640?wx_fmt=png&from=appmsg)

上图为光伏电站监控系统的逻辑架构图，目前电力监控系统主要与调度一平面、调度二平面以及光伏集控中心进行外部纵向连接。

光伏电站按照国家发改委14号令的要求进行安全分区，将电站网络分为生产控制大区和管理信息大区，其中生产控制大区又根据控制实时性划分为控制区（俗称安全Ⅰ区）和非控制区（俗称安全Ⅱ区），生产控制大区与管理信息大区为物理隔离状态。生产控制大区与调度一平面、二平面控制大区采用纵向加密认证装置实现了纵向认证加密；控制区与非控制区进行逻辑隔离，分别接入第一套数据网（一平面）和第二套数据网（二平面）。

光伏电站根据国家发改委14号令的相关划分标准，将电力监控系统中的运行监控系统、综合自动化系统、自动发电控制功能AGC、自动电压控制功能AVC、相量测量装置PMU放置在控制区中，将功率预测系统、故障录波、电能量采集装置放置在非控制中，管理信息大区和OMS工作站单独组网。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9P5sDaG5YlRuyTxaYEmoVnAov6rGsO0p0ImxQvicWRDx4O7BKwq4u6xDESFEn843vzyV2M2AevsVicg/640?wx_fmt=png&from=appmsg)

光伏电站监控系统安全分区示意图：

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9P5sDaG5YlRuyTxaYEmoVnAkWLhSgib5B3wgUjr4QXCBYR7dITBLbXuj868QRCKdG9E76ceCibOLLiaw/640?wx_fmt=png&from=appmsg)

上图为当前光伏电站监控系统安全分区示意图，监控系统严格划分为安全Ⅰ区和安全Ⅱ区，管理信息大区和OMS工作区（OMS工作区的作用：运行与维护管理系统，将光伏电站庞大而分散的物理设备（光伏组件、逆变器、箱变、线路、气象站等）和运维流程，通过数字化、智能化的软件系统进行集中管理和优化的控制台。）。

光伏电站远动信息按照电力系统调度自动化要求和DL/T 5003-2017《电力系统调度自动化设计规程》及各调度端等的要求设定采集量。

光伏场信息采集满足IEC 60870系列、MODBUS等标准，支持DL/T 634.5101-2002、DL/T 634.5104-2009、DL/T 719-2000、CDT451-91等通信规约和协议，适应异构系统间数据交换，实现与不同主站（省调、地调、发电公司）、光伏场内其它设备的数据通信。

光伏场信息上传主要通过综合终端完成，满足《光伏场调度运行信息交换规范》和《并网发电厂调度自动化设备配置规范和信息接入规范》要求，设备应冗余配置，信息直采直送，通信通道采用调度数据网以网络模式传输；本地功率预测子系统主要完成与调度主站关于光伏功率预测结果及相关信息交换。

光伏场与电网调度机构间交换的调度自动化信息，是指在电力调度自动化系统中主站端与光伏场端交换的信息。 按信息传送方向分为：光伏场向主站传输的上行信息、主站向光伏场传输的下行信息以及双向传输的信息。

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9NPowYOibGDTvxBicLHHAStUEvLNwlnoZVcXoAK7a84P4HvLa0kaHS8kl4WUVaKKtlKVLW7icYLbUxZQ/640?from=appmsg)

结束

![](https://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9NPowYOibGDTvxBicLHHAStUEmBNia6ibxaqaDibVk0OdnkkQApqrEWzLwmb5ECeOKQL07urT34HyuE4TQ/640?from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

老付话安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icKb2wsWzy9MFl1LCgCibJeCV1F21OkZHVYX4tY8b7YkTdXSqhre8sozecX77R5KgBpvzygTIrHiaW21ytB2FzvrQ/0?wx_fmt=png)

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