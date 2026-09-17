---
title: 德国军工巨头把作战系统核心接口开源了
url: https://mp.weixin.qq.com/s/DBL-ZiPdsb3_-vTgtLTKog
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:53:25.710569
---

# 德国军工巨头把作战系统核心接口开源了

# 德国军工巨头把作战系统核心接口开源了

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Rheinmetall 中文常译作莱茵金属，总部位于德国杜塞尔多夫，是欧洲体量顶尖的综合防务技术集团，公司创立于 1889 年，距今已有超过 130 年发展历史。这家企业从早期机械制造起家，逐步成长为覆盖陆海空天多领域的全栈防务系统供应商，业务不止局限于火炮弹药这类传统硬件，近些年在战场数字化、无人装备、防空系统、仿真训练软件等方向持续加码，也是德国联邦国防军最重要的装备供应商之一。

很多人熟悉莱茵金属，是因为它标志性的 RH‑120 系列 120 毫米滑膛坦克炮，豹 2 主战坦克、美国 M1 系列主战坦克都采用这款火炮，它是全球三代坦克最主流的主炮方案。除此之外山猫 Lynx 步兵战车、KF51 黑豹新一代主战坦克、Skynex 防空系统、BK27 机载航炮也都是它的代表性产品，弹药业务上莱茵金属同时是全球大口径弹药、智能可编程弹药的核心生产商，还在推进高能激光武器这类新概念装备的工程化落地。

和大众印象里只造枪炮的军工企业不同，最近十余年莱茵金属持续发力战场软件与作战系统开发。现代作战早已不是单一装备单打独斗，坦克、战车、无人机、雷达、光电传感器需要互相交换数据协同作战，这就需要一套稳定可靠的底层通信中间件。

2026 年 9 月莱茵金属正式对外公布消息，把 Battlesuite 数字平台首批核心接口规范对外开源，本次开源内容包含 Battlesuite 接口集合当中的 Onboard API 与 Tactical API

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpo4enR0bSClgiaZhThmmx5ZFZesvT6wicCszURN908oazniacAJmQwLD0kVWQ3Dia7Lkyo7ZW1ic1Z0ory74wANb9NYYF5NdsuVvZ0/640?wx_fmt=png&from=appmsg)

对应的项目仓库分别是

github/Rheinmetall/onboardapi

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDraoU2Iut5BIrltdNYUibEqYzHrIFZxHJ8y8l1KHJdVPzPXBhuHR4DgN70s4QDad1iakA2ib06jqjzqTUgKIpRZLUC1mAnHZv78aQ/640?wx_fmt=png&from=appmsg)

github/Rheinmetall/tacticalapi

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoeQY7yDuljYAw6Bhv4E7oI6sSL2h1KdzjgDhRrTOewhDiaPN7L06d1yUxbOWmMRIAJ6aYDpMvwxeOk8ebSz7nH2sLjiaCH6ic120/640?wx_fmt=png&from=appmsg)

这项举措的核心目的，是降低外部开发者对接不同厂商软件、传感器与武器装备的集成难度。

消息一出，很多开发者的第一反应是好奇，一家以坦克、火炮和弹药闻名的军工企业，怎么突然玩起了开源，更有人想知道，这套东西到底能拿来干什么。这篇文章基于官方文档 9.10.0 以及 Defence Industry Europe 的公开报道，把整套 Battlesuite 接口体系的技术细节拆开讲清楚，尽量不绕弯子，也让没有嵌入式背景的读者能看懂。

这套接口规范沉淀自莱茵金属多年防务技术与系统集成项目经验，它为作战平台、传感器、效应器以及指挥控制应用搭建统一技术底座。以往不同厂家的装备在联调阶段经常出现数据不通、协议不匹配的问题，需要投入大量人力做定制化适配。现在供应商可以在产品设计初期就遵循这套接口标准开发兼容产品，减少开发后期的对接难题。

莱茵金属数字系统事业部首席执行官 Timo Haas 表示，Battlesuite 构成莱茵金属数字化与联网作战战略的软件根基，标准化接口能够高效集成各类作战平台、传感器、效应器和指挥控制应用，同时为模块化、可互操作、可扩展的防务系统打下基础。企业的这套思路也契合当前全球防务领域的整体转变，也就是软件定义军用装备，装备可以在不开展大规模重新设计的前提下新增作战能力。

Battlesuite 本身不属于封闭私有平台，它可以充当不绑定设备厂商的数字枢纽，连接传感器、相机、无人机以及其他军用和民用设备。莱茵金属对这套架构的设想并不局限于军事用途，它还可以用于民防、灾害管理与关键基础设施防护场景，同一套架构能够直接部署在纯民用系统当中。

这套接口虽然大众视角会关联坦克装甲车辆，但它的应用范围并不局限于战车，同样可以对接无人机、各类传感器，甚至服务于民防、灾害管理、关键基础设施防护等民用领域。莱茵金属希望借助标准化接口降低不同厂商装备之间的数据集成难度，推动软件定义防务的落地。

Battlesuite 项目负责人 Ervin Kolenovic 介绍，借助 Battlesuite 莱茵金属正在落地软件定义防务的理念，这套接口集合简化不同系统组件的组合过程，不受设备生产厂商限制。这一特性推动软件模块可以跨多个项目复用，也方便现有系统持续灵活迭代升级，借此缩短研发周期，降低系统集成风险，加快新作战能力的落地部署。

开源后的接口规范为行业合作伙伴、科研机构以及客户提供明确路径接入 Battlesuite 架构，莱茵金属称这会减少互操作应用的集成工作量，实现软件模块跨项目复用。简单来说 Onboard API 负责单台作战平台内部各个软硬件组件通信，Tactical API 则面向多平台之间的战术级数据交互。

两者配合，让坦克、无人机、雷达哪怕来自不同厂商也能顺畅交换战场信息。开放接口不等于直接开放全部作战源代码，本次释放的是接口规范，开发者可以基于规范开发适配组件，不用完全掌握莱茵金属整套 Battlesuite 内部实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoJ2RmgmZibLYib7y4PQfRJ0JvWte38OImxHvjkCAV53Y03VgnrCsibbN4wmGicBohbibvcqSGEymByQemsGibJxACib6noichjuvBudibE/640?wx_fmt=png&from=appmsg)

官方文档给onboardapi的定位很直白，它是一个接口库，同时也是中间件（middleware），专门负责传感器系统和软件组件之间的无缝通信。

rheinmetall.github.io/onboardapi‑documentation/9.10.0/index.html

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqIEe5OLEdtaOtJCQDCrwmJAuIwzVZjdOlafyEgbIxIGnKtRHCdQelYvJx7haiazWibXbbvI43kqs5O8DLwCYWVBjDdmxdo7AOmo/640?wx_fmt=png)

图 Rheinmetall官方文档标识（来源：Rheinmetall onboardapi官方文档站）

想象一辆现代装甲车，雷达、光电转塔、激光测距仪、各种摄像头和火控计算机同时挂在车上，这些设备来自不同厂商，操作系统五花八门，数据格式各说各话，想让它们协同工作，难度不亚于让十几个讲不同语言的人同时完成一项精密任务，onboardapi要解决的正是这个“语言不通”的问题。它提供一套标准化的数据模型，确保复杂软硬件环境之间能够互操作，不同设备只要遵循同一套“语法”，就能顺畅对话。

这套库建立在Rheinmetall自研的ddkit软件开发套件之上，底层通信采用OMG（Object Management Group，对象管理组织）制定的DDS标准，全称Data Distribution Service，也就是数据分发服务。DDS是一种以数据为中心的发布订阅（publish-subscribe）架构，和传统的“客户端请求、服务器应答”完全不同，组件之间不需要事先知道对方的地址，谁发布数据、谁订阅数据，大家通过网络上的发现阶段（discovery）自动找到彼此，就像广播电台和听众的关系，电台不需要知道谁在听，听众也不用登记位置，只要频率对得上，数据自然流动，这套机制保证了可靠、低延迟的数据交换，正好满足高需求应用的要求。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpClmTuSc9DLtXMBwha3spfa2TKPuz3zYibcbKrF9iciaW1icMeOMxSDzqeUyUwmHdhicJ31Q0oUax6TOFZcy6yZ4JZ5C22d4JjwoF0/640?wx_fmt=png)

图 Client与Service：客户端向服务发起调用（来源：官方文档Concepts页）

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDrUWMleUyCYiaoI9Oicd4OLVOwF8mTRYSFryk9XQwHr9GZOfjuUgWnVI0ichbMPdRq3AtibYOPouNicBqZ6IVfx9oPFZWAmedSTCRWU/640?wx_fmt=png)

图 一个Service可以向多个Client推送数据（来源：官方文档Concepts页）

为了把通信组织得井井有条，onboardapi把每一个接口都定义成Service或者Client，这个区分说的其实是数据和任务的“归属”，而不只是数据流向。Service是服务提供方（Provider），通常属于管理某个资源的应用程序，比如一个硬件传感器、一台数据库或一台物理设备，它负责把自己的状态分享给所有客户端；Client则是消费方（Consumer），属于想使用这个资源的应用程序，通过“订阅”（subscribe）服务来获取更新或下发指令。反过来，Client也能向Service发数据，比如一条命令，Service也能把一份报告推送给多个Client，角色决定的是话语权和责任，不是单向管道。

文档里给了一个非常直观的例子，一个速度表服务（Speedometer Service）负责读取传感器数据，仪表盘（Dashboard）和数据记录仪（Data Logger）这两个应用程序都实现了速度表客户端接口，各自收到速度更新；如果某个客户端想触发传感器校准，它就调用速度表服务接口上的方法，一来一回，分工清清楚楚。

再往下看，onboardapi为不同的通信需求设计了明确的操作类型（Operation Types），并且直接体现在函数名的前缀上，开发者一眼就能看出数据是怎么被处理的。服务端接口（IService）提供四类操作，Cmd代表客户端向服务下达命令，Config是客户端配置服务，Notify是客户端向服务更新数据，Request是客户端对服务的请求；客户端接口（IClient）也有四类，Report把状态报告共享给所有客户端，Event向所有客户端广播数据事件，Response是对请求的应答，Stream则是不可靠的流式数据传输，专门为速度优化。两种接口的操作类型见图4、图5，文档给出的完整对应关系如下表。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp8gHVicEuwymEPyfn1ztHNyal6rw2hfmHzVtq2ZXqxC2pyJa0yElezw9D8xEe3dH87ibgqxcVWxAxuwz8zZ1n2VI6TWpTeREv2E/640?wx_fmt=png)

图 服务端接口IService的四类操作（来源：官方文档Concepts页）

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDribq9ibJK1c0NbDTnuIRPhHo45ib30m6rWjibH47WlYD7UWN4PvY5gIklklyicJ1xVO69Zb0wPblM2icGJf1iaTH3w6YuK46lUkbFqZg/640?wx_fmt=png)

图 客户端接口IClient的四类操作（来源：官方文档Concepts页）

表1onboardapi操作类型对照（来源：官方文档Concepts页）

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 接口 | 操作 | 说明 | 交付保证 | 迟加入支持 |
| IService | Cmd | 客户端命令服务 | 可靠 | 否 |
| IService | Config | 客户端配置服务 | 可靠 | 是 |
| IService | Notify | 客户端向服务更新数据 | 可靠 | 否 |
| IService | Request | 客户端向服务发起请求 | 可靠 | 否 |
| IClient | Report | 向所有客户端共享状态报告 | 可靠 | 是 |
| IClient | Event | 向所有客户端广播数据事件 | 可靠 | 否 |
| IClient | Response | 对请求的应答 | 可靠 | 否 |
| IClient | Stream | 向所有客户端发送流数据 | 尽力而为 | 否 |

#

可靠性和高吞吐往往是矛盾的两端，onboardapi的处理方式相当务实。默认情况下它保证可靠投递（Guaranteed Delivery），数据包丢了会自动重传，唯一的例外是Stream()系列，这类接口为了追求速度主动放弃了一部分可靠性，采用尽力而为（best-effort）模式，适合那些丢了也无伤大雅的实时画面类数据。

另一个很贴心的设计叫“迟到者支持”（Late-Joiner Support），战场网络里的组件并不是同时启动的，有的设备可能晚几秒甚至几分钟才上线，对于Report和Config这类操作，库会自动“记住”最后发送的值，新组件一连上就能立刻收到最新状态，而不是错过一切。与它配套的是IsRemoved标志，用来表示某条消息已经不再有效，服务关闭时系统会自动把它置为true，开发者也可以手动设置；在onboardapi里，所有以Key开头的参数都叫键控主题（keyed topics），每个唯一键被当作独立的数据处理，可以单独通过IsRemoved标志控制其生命周期，就好比每个士兵都有工牌号，谁离场了、谁还在岗，系统一清二楚。

数据模型会不断演进，这是任何长期项目的宿命，军事系统里不同版本的软件往往要在同一辆车上共存很多年，怎么保证版本升级不造成通信断裂，onboardapi给出的答案是DDS XTypes和XCDR2编码。XTypes是DDS规范里负责数据模型类型系统的部分，XCDR2则是新一代数据序列化编码格式，两者配合，让不同版本的软件可以平滑共存、无缝通信，即使数据模型一直在演化，向后兼容性也有保障，旧设备不会被新版本抛弃。

语言支持方面，onboardapi的核心库用C++编写，把性能敏感的部分做足优化，同时通过包装器（wrapper）提供Java、C#/.NET和Python等多语言集成，不同团队的开发者可以用自己熟悉的语言接入这套体系，不必都去啃C++。

作为一套面向车载系统的接口库，onboardapi的覆盖面相当惊人。官方文档把接口按领域划分成约五十个模块。

从M\_Alert（告警管理，负责报警和威胁告警的产生与生命周期管理）、M\_Camera（摄像头控制，对焦、变焦、增益、曝光、非均匀性校正NUC一应俱全）、M\_Sensor（通用传感器接口）到M\_CoordinateFrame（坐标系与位姿管理）、M\_Mount（转塔和云台控制）、M\_ObjectManager（目标管理）、M\_VideoTracker（视频跟踪）、M\_LaserRangeFinder（激光测距仪），再到M\_RecordingCtrl和M\_ReplayCtrl（记录与回放）、M\_ScanCtrl（扫描控制）、M\_Teleoperation（远程操控）、M\_MissionCtrl（任务控制），几乎覆盖了装甲平台信息化需要的大部分功能域。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoXDHM5foTtJp9L8ky72qjDAzMTtwE6sfNgTwaKnjcE3k8edolBM7kvzSSf7RxZibCfXQrVDSE51JwMzhlNT7oclU0avAYN6uKc/640?wx_fmt=png)

图 告警服务启动时序：按驾驶员、炮手、车长角色分别上报告警（来源：官方文档Interfaces页）

以告警服务为例，时序图展示了完整的启动流程，服务启动后先上报静态配置，再上报初始状态，随后从数据库读取历史告警，按乘员角色（驾驶员、炮手、车长）分别上报告警通知，最后更新活跃告警数，每一步都有对应的Report操作，IsRemoved标志则负责标记数据的生命周期。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDpy7WiaZ071gOkib1vHpsqnXriaPpgficsFbED8JXsDtYFSdcJWHXIicZmmZoNQR2mxrpANtJC8tSpPCddSLicgdMtLjdgRQ5SctgoVU/640?wx_fmt=png)

图 摄像头服务从启动、状态更新到关闭的完整交互（来源：官方文档Interfaces页）

摄像头服务的时序图展示了另一个典型场景，服务启动时上报静态设置和初始状态，客户端通过CmdSetZoomLevel调整变焦级别，服务随后把更新后的状态报告出来，关机时把IsRemoved置为true，表示这个服务已经不在线，下游应用据此判断“摄像头没了”，逻辑清晰得几乎像在讲故事。

看到这里，黑鸟看了一下实际写代码是什么体验：

官方示例用M\_CoordinateFrame模块演示了整个流程。开发者先实现IClient或IService接口，把关心的回调方法override掉，比如收到坐标变换报告时打印一行日志；然后调用Service::create和Client::create，传入domainId（域ID）、serviceName（服务名）和回调对象，库会自动创建对应的DDS读写器（readers和writers），从创建到收发数据只有几步。除了类继承式的回调，库还支持lambda回调，写起来更轻量；CMake集成也很标准，find\_package(onboardapi)之后target\_link\_libraries链接onboardapi::onboardapi即可。此外，ddkit还提...