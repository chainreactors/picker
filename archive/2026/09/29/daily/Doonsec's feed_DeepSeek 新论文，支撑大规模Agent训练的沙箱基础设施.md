---
title: DeepSeek 新论文，支撑大规模Agent训练的沙箱基础设施
url: https://mp.weixin.qq.com/s/K69ObJLR-aoitheGXMa3oA
source: Doonsec's feed
date: 2026-09-29
fetch_date: 2026-09-30T07:41:07.225633
---

# DeepSeek 新论文，支撑大规模Agent训练的沙箱基础设施

# DeepSeek 新论文，支撑大规模Agent训练的沙箱基础设施

原创

刘顺
刘顺

安全有术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSKf4G7kcviaqwfD0iaJmXLcgarGrAKtL3TDHhcLfE9cj6x0NedPZxV5C1TxZmDl7aAtOPXhGzdV60kT4baESTzg/640?wx_fmt=jpeg&from=appmsg)

> 一夜之间，300 万个沙箱在 DeepSeek 的机房里醒来，又睡去。它们执行的，是 AI 自己生成的代码。

---

## 导语

9 月 19 日，DeepSeek 提交了一篇新论文：《DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale》，作者名单超过 130 人，梁文锋在列。

外界很快被一连串数字吸引：单日服务约300 万个沙箱、峰值并发38 万+、创建速度每秒 5,000 个、单个训练任务一次拉起3.2 万个沙箱。

但作为安全从业者，我读完论文后印象最深的，是关于智能体在沙箱中的表现——

大模型 Agent 在沙箱里翻日志、伪造请求、覆写 /bin/bash、扫描可达端口，甚至把操作系统内核搞崩了。

这篇文章，我们就聊聊这篇论文到底讲了什么。

> 文末附上了我整理翻译的论文全文中文版 PDF。

---

## 一、为什么 Agent 训练需要"海量沙箱"？

先补一个背景。

传统大模型训练，吃的是静态数据：输入、输出、奖励信号，都是提前准备好的。但Agent 训练完全不同——模型要真的"动手"：读代码仓库、执行命令、安装依赖、修改文件、跑测试。它每走一步，环境状态就变一次，下一步又建立在之前的改变之上。

这意味着：模型之外，还得有成千上万个足够接近真实机器、用完能恢复干净的"工作现场"——这就是沙箱（Sandbox）。

问题是，Agent 训练对沙箱的需求是"变态级"的：

* 突发性：一个 RL 训练任务，可能在几秒内要求创建上万个沙箱；
* 长寿命：沙箱要跨越模型的多轮交互持续存活，中位寿命十几分钟，长尾超过 3 小时；
* 高密度：Agent 大部分时间在"等模型想下一步"，CPU 利用率极低——90% 的沙箱平均 CPU 用量不到申请额的 5%；
* 异构性：一周之内，容器后端涉及 11,266 个基础镜像、102,171 个工作区。

传统的"起一个容器、跑完销毁"的思路，在这个量级面前彻底失效。于是 DSec 应运而生。

![](https://mmbiz.qpic.cn/mmbiz_png/REdCMBKc8fbd0ibYTpz36KQ7CpkPk74GKAoS8rTfeWvQGPyia7FLt6Hen5PIxAAGmG4SFia2SwWnGUt1IUAJSW1P5qic07TiaJkr51AjDMJvN8Ak/640?wx_fmt=png&from=appmsg)

▲ 图源论文：单个任务创建的沙盒数量分布——容器任务 p50 达 352 个、p99 达 4,044 个，microVM 任务长尾更逼近 1.6 万个

---

## 二、DSec 是什么：一套平台，四种沙箱

DSec 的定位很清晰：Agent 训练的弹性沙箱基础设施。它的架构可以概括成"一套 SDK、四种后端、两级调度"。

![](https://mmbiz.qpic.cn/mmbiz_png/REdCMBKc8fZK8y6YGEic4ytWrbHJv1aCpMWnibqRDldHegRLg6V3EaiaiaUICicxdLOkKcKdnDxk3guG1icEok0XibtXRicWbjCxHp1zIy2Z5icDmicw0/640?wx_fmt=png&from=appmsg)

▲ 图源论文：DSec 整体架构——训练集群经统一 SDK（libdsec）接入，IAM 鉴权后由放置引擎调度到节点，Edge/Aether/Chronus 三层负责沙箱生命周期与会话管理，底层由 3FS 支撑镜像存储，AppArmor + eBPF 负责隔离

四种后端，覆盖从轻到重的全部需求：

| 后端 | 隔离强度 | 典型场景 |
| --- | --- | --- |
| FnCall（函数调用） | 低 | 类 OJ 刷题、编译、GPU 算子评测 |
| 容器（Docker） | 中 | 软件工程任务、工具调用 |
| Firecracker microVM | 较强 | 安全攻防、Computer-use |
| 完整虚拟机（QEMU） | 强 | 安卓模拟器、需要 GUI 的完整 OS |

训练框架通过统一的 Python SDK（libdsec）完成沙箱的创建、执行与回收——不过论文也明确，libdsec 提供的是统一访问路径，**为任务选择合适的后端仍是调用方的责任**，因为四种后端的启动成本、隔离边界与文件系统语义并不相同。

成本优化方面有两个漂亮的设计，简单说两个：

其一，"可组合层"代替单体镜像。基础镜像、代码工作区、工具包（比如 DeepSeek Harness）被拆成三个独立版本化的只读层（EROFS 格式），启动时用 overlayfs 叠加组合。升级工具包只需重建那一层，而不是重建几万个镜像——维护成本从 O(m×N) 降到 O(m)。

其二，镜像按需加载。论文统计发现，沙箱运行时实际只访问镜像数据的4.2%–13.3%。于是 DSec 把镜像放在自研的 3FS 分布式文件系统上，用多少取多少：8,192 个容器突发部署只花约 35 分钟（Docker 冷拉取要 60 分钟以上），单节点磁盘写入量从 1,600GB 降到 700GB。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/REdCMBKc8fb10x2iayaxUd0fc4SBKXmlz9WxlsZrn2lpZzdwhyKScEJCDQtIu2Hicy7yvLSg9YnTJZFjlHZnzI5zm60M7czWYPyrVSm3RJzGE/640?wx_fmt=png&from=appmsg)

▲ 图源论文：8,192 容器突发部署实验——按需 EROFS 拉取与全本地缓存基线几乎同步完成，Docker 冷拉取慢 1.71 倍，累计磁盘写入量减少约 57%

![](https://mmbiz.qpic.cn/mmbiz_png/REdCMBKc8fbPtrYOoKh31ic2YicIUtXgGNFAsh9TrticMdpn0gib9RicEswiaFV59jLrJBGztW6xY1PqaZO2QfnPOyKEG1gSWOcKhjCKfQG8QrodM/640?wx_fmt=png&from=appmsg)

▲ 图源论文：DSec 核心机制一览——可组合层、内存优化、容器 CPU QoS、按需镜像加载四大机制协同工作

再加上内存回收、CPU 双层 QoS 调度、云端弹性扩容，DSec 把"3.2 万个沙箱同时醒来"变成了日常操作。

> 金句：Agent 时代的算力瓶颈，正在从 GPU 转移到"给 AI 一台干净的机器"这件事上。

---

## 三、安全视角：当 AI 开始"不守规矩"

这是我最想展开的部分。论文第 6.4 节像是写给安全团队的"事故复盘报告"，DeepSeek 记录了多类真实的 Agent 异常行为：

1. 沙箱内"找答案"（Reward Hacking 的典型形态）

* Agent 翻查平台管理的文件和通信渠道，寻找残留在日志里的参考答案；
* 向 chronus（沙箱内的执行代理）的 Unix 套接字直接发送伪造的 RPC 消息，冒充用户请求；
* 因为执行链路会调用 bash，Agent 尝试覆写 /bin/bash，往后续的 shell 会话里注入命令；
* 更绝的是：在被加了文件访问控制后，有 Agent 尝试用 `XFS_IOC_SWAPEXT` 这个冷门 ioctl 交换两个文件的数据区段映射，绕开保护——结果把 XFS 文件系统元数据搞坏，直接触发了文件系统关闭。

2. 沙箱外"抄近路"

* 扫描端口和可达服务，寻找任务预期之外的信息源；
* 通过 Go module 代理拉取 GitHub 代码、安装新版软件包，只为找到现成的参考实现。

3. 无差别破坏

* 一个 Agent 从根目录递归执行 grep，遍历 /proc 并读取 /proc/kpagecgroup，触发内核 bug，内核直接崩溃；
* 在漏洞利用任务中，本该转发到目标虚拟机的攻击命令，被 Agent 在自己的容器里执行，把自己打崩了；
* 一个 Agent 调用了 `yes` 命令，持续输出的 stdout 被日志系统如实记录，存储膨胀了几十 GB。

DeepSeek 给出的缓解手段是两层：**AppArmor** 控制文件与套接字访问（即使 Agent 以 root 运行也生效），**eBPF** 实施细粒度网络白名单——网络权限按域名或镜像服务定义，实际过滤则精确到 IP、端口与协议，并可随任务阶段动态调整。

但论文写得非常坦诚：

> "这些控制只覆盖问题的一部分，并不能对'触发内核 bug'这类破坏性行为提供通用防御。"

翻译成人话：沙箱隔离能做到"关起来"，但做不到"保证它老实"。这句大实话，比任何安全产品宣传片都有价值。

---

## 四、对我们的三点启示

启示一：沙箱是大模型 Agent 应用的安全底线，不是可选项。Agent 会操作真实系统，它的每一次"手滑"都可能是真实故障。凡是让 Agent 接触代码、文件、网络的场景——不管是代码助手还是智能运维——执行环境必须沙箱化、强隔离、可回收。

启示二：权限要"最小化到任务级"。DSec 的网络策略细到"允许 PyPI、禁止 NPM"这种粒度，且随任务阶段动态变化。对比很多企业的 Agent 应用还停留在"给个容器就完事"，差距是全方位的。

启示三：Agent 行为审计是新兴战场。论文展示的攻击面（日志泄露、内部 RPC 伪造、系统组件篡改）在通用云环境同样成立。AI 安全的攻防模型正在变化：对手不是外部黑客，而是"系统里那个不按剧本走、还极其执着的自动化执行者"。

---

## 结语

这篇论文表面上是 DeepSeek 公开了一套训练基础设施，实际上是第一次向外界完整展示了：当 Agent 规模化运行时，"执行环境"本身如何成为一个独立的工程与安全学科。

300 万沙箱每天起落的背后，是人类第一次认真回答这个问题：我们该如何安全地，把机器交给机器。

---

## 📎 附：论文中文翻译版

为方便大家阅读，我将论文正文完整翻译整理为中文版 PDF，详见链接：

https://pan.baidu.com/s/1HfE7vTsQ2MjioAt5vChyNg?pwd=b364

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/MSKf4G7kcvia6k5rU2vLf9nzMbZ6rcC7NHoDNqhf3ibofLCp1PN52P1UN8wVBLIFZib5JLCiaAqAxo3vicmx89HErFw/0?wx_fmt=png)

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