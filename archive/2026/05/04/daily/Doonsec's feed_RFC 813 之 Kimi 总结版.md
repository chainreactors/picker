---
title: RFC 813 之 Kimi 总结版
url: https://mp.weixin.qq.com/s/_l_OAz0WQf1wq5NRq-A5jA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:02:21.571735
---

# RFC 813 之 Kimi 总结版

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ib0JGGXPqNa8S4lQ4JuXzcu7Ik9qrFCXISsfYaxnOQUf3K9iazUWUibuALWZVKaLrrG65THXosWFBKVWX7wLwiaeyJeCibRmnlK1TwtK701pFqQA/0?wx_fmt=jpeg)

# RFC 813 之 Kimi 总结版

原创

7ACE
7ACE

Echo Reply

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**月之暗面**

# RFC 813 深度解析：TCP 窗口与确认策略

---

## 一、RFC 概览与定位

### 1.1 RFC 基本信息

| 项目 | 内容 |
| --- | --- |
| **RFC 编号** | [RFC 813] |
| **标题** | Window and Acknowledgement Strategy in TCP（TCP 中的窗口与确认策略） |
| **发布日期** | 1982-07 |
| **状态** | Historic（已被 RFC 7805 标记为历史文档） |
| **作者** | David D. Clark（MIT 计算机科学实验室） |
| **废弃/更新** | 被 RFC 7805 标记为 Historic；其内容已被后续 TCP 标准（RFC 1122、RFC 5681 等）吸收并规范化 |
| **关联 RFC** | RFC 793（TCP 核心规范）、RFC 896（拥塞控制）、RFC 1122（主机需求）、RFC 2581（TCP 拥塞控制）、RFC 5681（TCP 拥塞控制更新） |

### 1.2 文档定位与作用域

RFC 813 是 TCP 协议发展史上的**奠基性信息文档**，属于著名的"Dave Clark Five"系列（RFC 813-817）之一。它首次系统性地分析了 TCP 窗口机制与确认机制在实际实现中的性能陷阱，提出了"Silly Window Syndrome（SWS，愚蠢窗口综合征）"这一关键概念及其解决方案，并首次倡导了延迟确认（Delayed ACK）策略。

该文档的核心贡献在于：它揭示了仅符合 RFC 793 规范的字面要求，仍可能导致性能下降数个数量级的严重问题。它提出的发送端和接收端算法组合，为后续 TCP 性能优化奠定了实践基础。虽然其本身从未成为正式标准，但其中描述的算法已被 RFC 1122 等标准文档采纳，成为现代 TCP 实现的必备组件。

### 1.3 协议/规范架构图

```
RFC 813 TCP 窗口与确认策略核心架构
│
├── 问题域
│   ├── Silly Window Syndrome (SWS)
│   ├── 过度确认开销
│   └── 窗口策略选择
│
├── 发送端算法
│   ├── 可用窗口比例阈值检查
│   ├── 推送点（Push Point）例外
│   └── 与重传机制的协同
│
├── 接收端算法
│   ├── 窗口抑制（Window Shrinkage）
│   │   └── 50% 缓冲区阈值
│   ├── 延迟确认（Delayed ACK）
│   │   ├── PUSH 位检测
│   │   ├── 窗口变更触发
│   │   └── 定时器兜底
│   └── 动态延迟计算（附录 A）
│
└── 策略空间
    ├── 保守窗口（Conservative Window）
    ├── 乐观窗口（Optimistic Window）
    └── 极端延迟网络的复杂策略
```

---

## 二、核心机制与设计原理

### 2.1 核心问题

RFC 813 试图解决三个最根本的问题：

* **Silly Window Syndrome（SWS）**：当接收端应用程序缓慢消费数据时，每次释放少量缓冲区空间后向发送端通告小窗口，导致发送端发送极小的数据段（如 1-50 字节），网络被大量小报文充斥，吞吐量和 CPU 利用率急剧下降（可达数量级的恶化）。
* **过度确认开销**：接收端对每个数据段立即发送 ACK，导致发送端频繁处理 ACK 报文，调度开销远超实际协议处理开销，CPU 利用率恶化。
* **窗口策略的吞吐与鲁棒性权衡**：保守窗口在高延迟网络中吞吐受限，乐观窗口可能导致缓冲区溢出，需要策略指导。

### 2.2 核心设计原则

1. **双向保险原则**：发送端和接收端各自实现 SWS 防护算法，任何一端单独即可防止 SWS，两端配合可额外降低 CPU 开销（实测可达 4 倍提升）。
2. **比例阈值原则**：不依赖绝对值，而是使用可用窗口与提供窗口的比例作为决策依据，使算法自适应不同缓冲区大小。
3. **延迟确认原则**：在不影响协议正确性的前提下，通过合并 ACK 减少控制报文数量，但需保证"活性（liveness）"——不能因延迟而永久阻塞数据流。
4. **最小侵入原则**：发送端算法仅需在现有可用窗口计算逻辑后增加一行代码（比例检查），实现成本极低。
5. **定时器兜底原则**：所有延迟操作必须设置定时器，确保在无后续事件触发时仍能推进协议状态。

### 2.3 关键算法与状态机

#### 2.3.1 SWS 防护状态逻辑

```
发送端 SWS 防护算法 (Greenwald 算法)

State: 正常发送
    |
    v
Compute: usable_window = offered_window - unacknowledged_data
    |
    v
Check: usable_window / offered_window >= threshold (约 25%)
    |
    +-- YES --> 允许发送
    |
    +-- NO  --> 检查例外条件
                  |
                  +-- 数据量 >= MSS? --> 允许发送
                  |
                  +-- 到达 Push Point? --> 允许发送
                  |
                  +-- 否则 --> 设置 usable_window = 0，暂不发送
                                    |
                                    v
                              等待后续 ACK 更新窗口
```

#### 2.3.2 接收端窗口抑制算法

```
接收端窗口抑制算法

Initial:
    actual_buffer_space = 当前可用缓冲区大小
    offered_window = actual_buffer_space  (初始通告)

OnDataArrival:
    process_data()
    freed_space = 新释放的缓冲区空间

    if (actual_buffer_space - freed_space) > actual_buffer_space / 2:
        # 释放空间不足一半，抑制窗口
        offered_window = actual_buffer_space - freed_space
    else:
        # 释放空间达到或超过一半，完全开放窗口
        offered_window = actual_buffer_space

    # 注意：offered_window 仅在 ACK 中发送，需配合延迟确认策略
```

#### 2.3.3 延迟确认决策算法

```
延迟确认算法

OnSegmentArrival(segment):
    if PUSH bit is set in segment:
        MUST send ACK immediately
    else if window information has changed significantly:
        MUST send ACK with updated window
    else:
        # 满足延迟条件
        set timer (200-300ms for ARPANET)
        # 若在下个 segment 到达前 timer 未触发，则发送 ACK
        # 若下个 segment 到达，timer 重置，继续延迟
```

---

## 三、技术规范详解

### 3.1 章节技术要点

| 章节 | 技术要点 | MUST/SHOULD/MAY | 实现细节/约束条件 |
| --- | --- | --- | --- |
| §2 The Mechanisms | 区分 `offered_window`（通告窗口）与 `usable_window`（可用窗口） | MUST（概念区分） | `usable_window = offered_window - unacknowledged_bytes` |
| §3 SWS | SWS 成因：小 ACK 导致小 `usable_window`，进而产生小 segment 的恶性循环 | MUST（理解问题） | 初始大窗口被自然边界分割后无法自动重组 |
| §4 Improved Window | 接收端：窗口抑制至实际空间的 50% 以下时暂不开放 | RECOMMENDED | 阈值可调整，但开放增量应至少容纳一个 full-sized segment |
| §4 Improved Window | 发送端：可用窗口 < 25% 提供窗口时禁止发送 | RECOMMENDED | 例外：数据量 >= MSS 或到达 Push Point |
| §5 Improved ACK | 非 PUSH、非窗口变更条件下可延迟 ACK | RECOMMENDED | 必须设置定时器（200-300ms），保证活性 |
| §5 Improved ACK | 重传阈值应 > 2 倍平均 RTT（考虑延迟 ACK 的 holding time） | RECOMMENDED | 平滑算法样本数应约为 burst 中 segment 数的 2 倍 |
| §6 Conservative vs. Optimistic | 保守窗口：吞吐量上限 = buffer\_size / RTT | INFORMATIONAL | 乐观窗口需能检测丢包，否则不可行 |
| Appendix A | 动态 ACK 延迟：指数平滑测量 inter-segment 间隔，过滤异常值 | EXPERIMENTAL | 未经过广泛测试， fudge factor 可较宽松 |

### 3.2 关键术语定义

| 术语 | 定义 | 说明 |
| --- | --- | --- |
| `offered_window` | 接收端向发送端通告的窗口大小 | 可能被人为抑制，不一定等于实际缓冲区 |
| `usable_window` | 发送端计算的实际可发送数据量 | `offered_window - unacknowledged_data` |
| SWS | Silly Window Syndrome | 小窗口导致小 segment 的恶性循环 |
| Conservative Window | 通告窗口精确等于实际可用缓冲区 | 高延迟下吞吐受限 |
| Optimistic Window | 通告窗口大于实际可用缓冲区 | 依赖接收端处理速度 > 发送速度 |
| Push Point | 应用程序要求立即发送的数据边界 | 由 PUSH 位标识 |

---

## 四、实现与实践分析

### 4.1 实现复杂度评估

| 机制/功能 | 实现难度 | 常见陷阱 | 主流实现差异 |
| --- | --- | --- | --- |
| 发送端 SWS 防护 | 极低 | 阈值设置过低导致不必要的延迟；未处理 Push Point 例外 | Linux 使用 `tcp_min_snd_wscale` 等参数；BSD 类似实现 |
| 接收端窗口抑制 | 低 | 阈值设置过高导致吞吐下降；与零窗口探测交互复杂 | Linux `tcp_moderate_rcvbuf` 动态调整 |
| 延迟确认 | 低 | 定时器精度不足；与 Nagle 算法交互导致延迟叠加 | Linux 默认延迟 40ms（非 RFC 813 的 200ms）；Windows 类似 |
| 动态延迟计算 | 中 | 指数平滑参数调优困难；异常值过滤策略敏感 | 极少实现，多数使用固定延迟 |

### 4.2 与真实世界实现的差异

#### 4.2.1 主流实现特点

* **Linux**：实现了 RFC 813 的核心思想，但延迟确认定时器默认约为 40ms（远小于 RFC 813 建议的 200-300ms），以平衡延迟与吞吐。`tcp_delack_min` 等参数可调。发送端通过 `tcp_snd_wnd` 和 `tcp_packets_in_flight` 管理窗口。
* **BSD/macOS**：FreeBSD 的实现更接近 RFC 813 原始描述，延迟确认定时器通常为 100-200ms。Darwin（macOS）继承了 BSD 的实现风格。
* **Windows**：实现了延迟确认（默认 200ms），但发送端 SWS 防护的具体阈值与 Linux 存在差异。

#### 4.2.2 已知偏离规范的行为

* **延迟 ACK 与 Nagle 算法的交互延迟**：当发送端启用 Nagle 算法（RFC 896）且接收端启用延迟 ACK 时，小数据写操作可能产生约 200ms 的额外延迟（"Nagle-Delayed ACK 死锁"）。现代实现通过 `TCP_NODELAY` 或更精细的启发式规则缓解。
* **定时器值的大幅缩减**：现代网络 RTT 远低于 1982 年的 ARPANET，固定 200-300ms 的延迟确认在现代千兆网络中过于保守，因此主流实现将延迟 ACK 定时器缩减至 40-100ms 范围。
* **接收端窗口抑制阈值的变化**：RFC 813 建议 50% 阈值，现代实现常采用更激进的策略（如 MSS 对齐的窗口通告），配合自动缓冲区调整（`tcp_moderate_rcvbuf`）。

### 4.3 安全性考量

| 安全问题 | RFC 描述 | 现代缓解措施 |
| --- | --- | --- |
| SWS 导致的 DoS | 未直接讨论 | 发送端/接收端 SWS 防护已成为所有现代 TCP 栈的标配 |
| 延迟 ACK 导致的重传误判 | §5 讨论了重传阈值需考虑 holding time | Jacobson/Karels RTT 估计算法（RFC 6298）；最小 RTT 下限保护 |
| 乐观窗口的缓冲区溢出 | §6 指出需能检测丢包 | 现代实现极少使用纯乐观窗口；依赖 SACK（RFC 2018）精确检测丢包 |
| 定时器依赖的活性保证 | §7 形式化论证了活性 | 所有延迟 ACK 实现必须配备定时器，这是硬性要求 |

---

## 五、协议演进与互操作性

### 5.1 版本演进历史

```
1981  RFC 793   TCP 核心规范发布，定义窗口和 ACK 机制但缺乏性能指导
1982  RFC 813   首次提出 SWS 概念、延迟 ACK 策略、窗口/ACK 优化算法
1984  RFC 896   Nagle 算法（与 RFC 813 发送端策略互补）
1989  RFC 1122  主机需求文档，将 RFC 813 的算法纳入正式要求
1997  RFC 2001  TCP 慢启动、拥塞避免、快重传、快恢复（与窗口策略协同）
1999  RFC 2581  更新拥塞控制，明确与 SWS 防护的交互
2009  RFC 5681  进一步更新 TCP 拥塞控制，SWS 防护成为隐含前提
2016  RFC 7805  将 RFC 813 标记为 Historic，承认其历史贡献
```

### 5.2 向后兼容性分析

RFC 813 的算法设计具有**极佳的向后兼容性**：

* **发送端算法**：仅增加一个本地判断条件（`usable_window / offered_window >= 25%`），不修改任何协议报文格式或交互语义。即使对端未实现任何优化，发送端算法仍能防止本地产生 SWS。
* **接收端算法**：窗口抑制和延迟 ACK 均不违反 RFC 793 的规范字面。RFC 793 仅要求"promptly acknowledge"，未定义具体时间；窗口值只要不超过实际缓冲区即可（抑制窗口是保守的）。
* **协商机制**：无需任何协商，纯单边行为。

### 5.3 扩展机制评估

| 扩展机制 | 设计优劣 | 实际采用情况 |
| --- | --- | --- |
| 固定比例阈值（25%/50%） | 简单、自适应不同缓冲区大小；但在极端缓冲区大小下可能不够精细 | 核心思想被广泛采用，具体阈值由实现自行调整 |
| 动态 ACK 延迟（附录 A） | 理论上可自适应网络条件；但实现复杂，指数平滑参数敏感 | **未被主流实现采纳** ，多数使用固定延迟 |
| 乐观窗口 | 可显著提升小缓冲区系统的吞吐；但需丢包检测能力，风险高 | 极少直接使用，现代通过自动缓冲区调整和窗口缩放（RFC 1323）间接实现类似效果 |
| 分阶段乐观窗口（§6 末尾） | 理论上可解决极端延迟网络的吞吐问题；但稳定性差，易"聚束" | 从未实现 |

---

## 六、批判性分析与局限性

### 6.1 设计取舍与权衡

| 设计决策 | 当时的考量 | 今天的挑战 |
| --- | --- | --- |
| 固定比例阈值（25%/50%） | 简单、无需配置、自适应 | 现代网络缓冲区动态变化（`auto-tuning`），固定比例可能不是最优；需要与 BDP（带宽时延积）感知结合 |
| 延迟 ACK 200-300ms | 基于 ARPANET 的 inter-segment 延迟测量 | 现代网络 RTT 通常为 1-50ms，200ms 过于保守；但过度缩减会增加 ACK 频率 |
| 未涉及拥塞控制 | RFC 813 聚焦流控制而非拥塞控制 | 现代 TCP 中拥塞窗口（`cwnd`）与接收窗口（`...