---
title: PHP2Shell 的「最终兵器」被解剖了：ChaCha20 加密配置的 Mirai 变种
url: https://mp.weixin.qq.com/s/R_rMD6wroCNC0TRDWaYyJw
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:44:05.831321
---

# PHP2Shell 的「最终兵器」被解剖了：ChaCha20 加密配置的 Mirai 变种

# PHP2Shell 的「最终兵器」被解剖了：ChaCha20 加密配置的 Mirai 变种

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0H2OUMr3j5J6AWq4kxor2zH8OGe3wS5QicgmiaOsAufRxqNjjeC0q5jLE5qoz54gZiaptz3ykgeOKzEBDXlplrv0ayUX4EkDeP10w/640?wx_fmt=jpeg)

过去一周，php2shell（CVE-2026-109618 / 109619）从预警、PoC 公开打到补丁后讨论，热度还没退。今天这篇是这个系列的**第四篇，也是离「实战」最近的一篇**：Joe Security 的人工深度逆向团队（Joe Reverser）把一个通过 PHP2Shell 链投递的**最终阶段载荷**完整拆开了一根函数一根函数地分析——判定 **Malicious 98/100（置信度 95）**。

这个样本本身是一个 **Mirai 衍生的 Linux 僵尸网络 bot**（多家厂商将其归为 **Potassium** 家族，Synthient 2026 年 3 月首次识别）。它的价值在于：把「PHP 漏洞被利用之后到底会发生什么」这个问题，从猜测变成了有代码、有地址、有 IoC 的实锤。

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GAx546JsXhFPqV4aEdqIPfFzaKFUkibttQbQ7r3Czee47nFlmsMofSYW1ByWDFHcIq7a0IibHNicsFiaDQcibFzao29Xn9GLoqX6PM/640?wx_fmt=png&from=appmsg)

## 一、样本基本信息

* **文件名**

  `0c5486f06620e26e316f4b33f318b0d646d5e1133789331aa2fed012360d1486.elf`
* **SHA-256**

  `0c5486f06620e26e316f4b33f318b0d646d5e1133789331aa2fed012360d1486`
* **MD5**

  `b61a098fc62a2c2696e196dca78da71a`
* **类型 / 大小**

  ELF64 x86-64 静态链接可执行文件，已剥离符号，**179,632 字节**
* **入口点**

  `0x400B7F`（主应用例程 `0x4001D0`）
* **分析时间**

  2026-10-22（Joe Reverser，25 分钟动态 + 全量静态）
* **判定**

  Malicious 98/100；家族未独立确定（Threatname: unknown）
* **关联背景**

  已确认的 **PHP2Shell 初始访问**活动

Joe 团队同时定位到同一哈希的既有 Joe Sandbox 自动化分析（编号 1990431，判定 Suspicious 24/100）——**自动化沙箱只给了 24 分，人工逆向给了 98 分**，这个反差本身就说明：对付这类样本，行为 superficially 「温和」但代码逻辑完整的 bot，自动化沙箱的视野远远不够。

## 二、这个样本在整条链的什么位置

先把坐标系立起来。综合 Sophos、Arctic Wolf 与 Joe Security 三方的观测：

* **攻击源**

  （Sophos / Arctic Wolf 记录）：`85.11.167[.]243`、`217.60.242[.]76`、`45.198.224[.]169` 三个 IP 发起 PHP2Shell 利用尝试；
* **Loader 主机**

  `92.118.112[.]100`，负责投递 Mirai 衍生载荷；
* **落地**

  本报告分析的 x86\_64 bot（另有 ARM 构建，215KB，面向路由器和摄像头类设备）；
* **最终目标**

  （Sophos 记录）：对乌克兰单一网络内两台相邻主机 `45.88.138[.]0` / `45.88.138[.]44` 发起持续 volumetric 洪水攻击。

**必须在开头说清楚的在野态势**：Sophos 在 10-22 晚间**更正**了早前「观测到一次成功利用」的判断——其客户遥测显示的是**海量扫描 + 少量失败尝试**，截至当时**没有任何成功失陷的证据**；Sophos 自己的对抗团队带着 AI 辅助也没能做出稳定可用的利用。翻译成大白话：**洞是真的、兵是实的，但弓弩目前还拉不满**。这不构成任何松懈的理由（工具链正在快速进化），但决定了当前的真实风险等级。

## 三、样本能力剖析：六个模块 + 一套进程控制

这个 175KB 的静态 ELF 没有引入任何外部依赖，所有能力自包含。Joe 拆出了六个功能模块：

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0HFohVRM9DUBibCjfHAKzGrmUJI1h6kTE9Jt0iaIKfE7Sjj1NVw9JCQaGnapiaRcTfjiaaXfaHvDUEWAUyUeQQdqboHXr5ZYfNuqks/640?wx_fmt=png&from=appmsg)

**① 进程名伪装：给排查者看的门面。** 例程覆写参数存储后调用 `prctl(PR_SET_NAME, ...)`，把自己伪装成系统服务名：`telnetd`、`udhcpc`、upnpd`、`watchdog`、`syslogd`、`klogd`、`uhttpd`、`uchttpd`。运维在`top` 里一眼扫过去，很容易当成正常服务放过。

**② 守护进程化。** fork + `setsid` + 关闭标准描述符，启动额外 worker——经典 bot 化操作，脱离终端控制。

**③ 反调试。** 解析 `/proc` 进程状态文件里的 `TracerPid:` 字段，握手前检查，发现被 trace 就转向连接重置处理——**跟踪它会导致连接异常，而不是直接断**，给分析者制造噪音。

**④ ChaCha20 加密配置。** 全部 **473 条配置条目**用 ChaCha20 加密，连 `expand 32-byte k` 这个常量都额外过了层 `XOR 0xA5` 混淆。Joe 恢复出完整 key/nonce 后逐条解密，并与三个进程的内存dump逐一比对吻合。据 Nokia Deepfield，**把 ChaCha20 用于 Mirai 的静态配置表，是这个家族此前的变种里没见过的用法**。

**⑤ C2 寻址（本文第四节详说）。** DNS + 八位组置换 + 地址池轮换。

**⑥ 载荷更新。** 按架构选择路径（本构建选 `x86_64`）→ TCP 80 明文 HTTP 下载 → 用 `.upd_w` 测试可写位置 → `chmod 0755` 后 `execve`，还保留 bot 标识。

**进程控制**是另一条贯穿线：枚举 `/proc` 下进程的 `status`/`cmdline`，内部维护 PID 排除列表，对 **5270 / 790 / 880** 三个 PID 成功执行了 `SIGKILL`——典型的「杀掉竞品 bot 和清理脚本」。另在 `127.0.0.1:1234` 开了本地控制套接字（与远程 C2 是两回事，做本地实例控制）。

**能力与行为的分界（Joe 的严谨之处）**：运行时可观测的是 DNS 查询、连接尝试、`/proc` 读取、SIGKILL、配置解密；而**加密会话建立、DDoS 执行、交互 shell 会话、替换下载完成都只是静态确立的能力，在受检运行中并未实际演示**。读这类报告要特别盯这个分界——混为一谈就会高估当前利用成熟度。

## 四、C2 怎么找、怎么藏、怎么通信（全文最精彩的部分）

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GHNP0GmEogF0BugRXiangGBhd6z2Uc9E1KjRvzeVrsIicdaJA4RJvfFHZalIMWlPu7xxEBdiadlKHE4dwbrZUNVThX00TmeRV0ZY/640?wx_fmt=png&from=appmsg)

**寻址：域名是真的，答案是假的。**

1. 配置内存里 8 个主发现槽都写着 `thunder.godofthunder[.]st`；
2. bot 发起 DNS 查询，兜底用 18 个硬编码公共解析器（8.8.8.8 / 1.1.1.1 / 1.0.0.1 等）——**这意味着企业内部的 DNS 封锁、RPZ、sinkhole 根本看不到它的查询**；
3. Joe 实测 DNS 应答为 `134.154.64.199`；
4. 但 bot 连接前会做**八位组置换**：`A.B.C.D → A.D.B.C`，即 `134.154.64.199 → 134.199.154.64`；
5. 真实 C2 是 `134.199.154.64`，端口从 14 个配置端口里轮换（Joe 记录到 `50488`，Sophos 记录到 `50792`——**两个都在同一张端口表里，这反而交叉印证了端口轮换行为**）。

**防御含义极其直接：封锁 DNS 应答地址（134.154.64.199）毫无用处，那是诱饵；必须按 `134.199.154.64` 这个真实 IP 堵。** ELLIO 的独立分析给了同向建议：限制出站 53 端口到自有解析器，把 bot 的查询拉回你能看见的地方。

**通道：主用现代加密，兜底一个字节。**

* 主路径是 **X25519 密钥协商 + ChaCha20-Poly1305 认证加密**，记录带序列号；另有一套 ChaCha20 + 16 字节截断 HMAC-SHA-256 的备用记录格式；
* 最陈旧的兜底是**全网流量单字节 `XOR 0xED`**（常量 `0x0DEAFFED` 的低字节）——Nokia Deepfield 把它列为这个家族的命名级特征；
* 交互式 shell 走独立成帧通道，帧头魔数 `c4 71 29 b8`，三种帧类型（开/写/关会话），经 `/dev/ptmx` 分配 PTY，失败则回退 socket-pair；
* **一个对防守方有利的细节**

  ELLIO 实测发现 bot **不校验服务端身份**——对握手回复的全部检查就是「长度超过 32 字节且 tag 字节正确」。这意味着**防御性 sinkhole 在理论上是可行的**：任何按这个格式应答的设备都能「冒充」C2 把 bot 圈起来。

Joe 还从样本里挖出一块**预留但未启用**的能力：ENS（以太坊域名服务）配置——两个 `.eth` 名字、`ip` 到 `ip32` 三十二个文本记录键、七个公共以太坊 RPC 端点。Arctic Wolf 确认两个构建里 ENS 解析均**处于关闭状态**。ELLIO 的追踪显示这些名字注册于 10-13，其中一个的文本记录在 10-14 两小时内被改写过四次，还有个记录内容是「woah woah, there is nothing to see here!」——攻击者的小品级幽默，但也提醒我们：**这条路一旦启用，封禁难度会明显上升**。

## 五、DDoS 与 MITRE 映射

派发表 24 个槽位（含 1 个空桩），覆盖 UDP 洪泛、per-target UDP socket、raw TCP、TCP 连接洪泛、raw ICMP、`IPPROTO_RAW`、随机化载荷 UDP、带 ChaCha20 载荷变换的 UDP、socket 选项操纵、复合 TCP/UDP/raw 路径、HTTP 处理器等。静态包生成特性包括 raw socket、`IP_HDRINCL`、校验和、随机化头部/载荷。应用层材料有 GET/POST/HEAD 模板、可变 User-Agent、CitizenFX/FiveM 字符串。特殊命令：`0xFF` 停 worker、`0xFE` 触发更新。

MITRE ATT&CK 映射（Joe 版，精选）：

* **初始访问**

  T1190（利用面向公网的应用）——PHP2Shell；
* **防御规避**

  T1027（混淆）/ T1140（解码）/ T1036.004（伪装服务名）/ T1622（调试器规避）；
* **C2**

  T1095（非应用层协议）/ T1573.001（对称加密通道）/ T1105（工具传输——自更新）；
* **执行**

  T1059.004（Unix shell）；
* **发现**

  T1057（进程发现）/ T1082（系统信息发现）；
* **影响**

  T1498.001（网络 DoS）/ T1499（端点 DoS）。

## 六、IoC（防御向）

| 类型 | 值 |
| --- | --- |
| SHA-256 | 0c5486f06620e26e316f4b33f318b0d646d5e1133789331aa2fed012360d1486 |
| MD5 | b61a098fc62a2c2696e196dca78da71a |
| C2 域名 | thunder.godofthunder[.]st |
| C2 IP | 134.199.154.64（14 个端口轮换，含 50488 / 50792） |
| 诱饵 IP（勿只封它） | 134.154.64.199 |
| 更新服务器 | hackattackkaboom[.]botlesscucks[.]st（117.55.202[.]115，路径 /x86\_64） |
| 附属域名 | hik.gettingheadfromduckysmom[.]st |
| Loader 主机 | 92.118.112[.]100 |
| ENS 标识 | 2sexy4u.eth / sushiconsumer.eth（当前未启用） |
| 本地监听 | 127.0.0.1:1234 |
| Shell 帧魔数 | c4 71 29 b8 |
| ChaCha20 配置密钥 | 5a3f2e7b8c9d0a6e3b4f7c8a1d5c2b0d6f1a0c3e2d8e4a091c7e5a4d3c2b6a08（nonce 4a1b00ff2d7c3a1200010305，用于失陷样本配置解密） |

完整配置解密结果 Joe 有公开链接（decrypted\_config.txt / .json），应急响应时可直接比对。

## 七、检测与防御

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0ESLgcWg2FOyFUQeNYTDZwuIQyBGgQgDNRGe8G8xAib4zwiapPyaokuGO7uwGXNb3BhZg2sctP65rDAwA8aYsJHmQk08P6B3cHjg/640?wx_fmt=png&from=appmsg)

**网络侧：**

* **按 IP 阻断**

  C2（134.199.154.64）、更新主机（117.55.202.115）、loader（92.118.112.100）——不要只做 DNS 层面的封锁，18 个硬编码公共解析器会让你的 RPZ 变成摆设；
* 出站 53 端口收敛到自有解析器；
* 到 C2 的 14 个配置端口出现出站流量，本身就是**高置信失陷信号**；
* 通道特征可做检测：96 字节握手、约每 90 秒 39 字节的固定长度保活；
* 有条件可以上**防御性 sinkhole**（利用 bot 不校验服务端身份这一点）。

**主机 / 服务侧：**

* 哈希 IoC 入库全盘扫描；
* `prctl`

  伪装的进程名（watchdog/telnetd/syslogd 等）出现在非常见位置；
* `/dev/ptmx`

  + fork 会话、异常 SIGKILL 循环、出站 80 明文 HTTP 拉 ELF；
* 商用规则：Sophos 已发布 IPS 特征（防火墙侧 67359 / 67360 / 67375 / 2313184–2313188，端点侧另有 2313189）。

**治本仍在服务端**：PHP 升级到 8.2.35 / 8.3.36 / 8.4.27 / 8.5.12；过渡期关闭 `session.upload_progress.enabled`（针对 109619）+ WAF 拦截可疑 multipart 请求。

## 八、这个样本告诉我们的事

**1. 「扫描海量、成功寥寥」的窗口不会一直开着。** Sophos 的更正说明攻击者目前卡在利用可靠性上；但 ELLIO 记录到工具链的进化速度——**从探测到可用 exploit 用了 48 分钟，再到落地 foothold 只多花了 81 分钟**；SOCRadar 还在攻击者服务器上发现了「一键式」PHP2Shell 利用工具（aslr\_exploit.py，针对 8.4.26 + mod\_php）和三件套筛查脚本，已扫过约 20 个分布在七国的站点。窗口是在收窄的，只是还没关上。

**2. 攻击者已经把「隐匿」当系统工程做。** DNS 掉包、14 端口轮换、X25519 + ChaCha20-Poly1305、进程名伪装、反调试、ENS 预留——单看每招都不新，组合在一起就是一份完整的「抗 takedown」设计。对应的防守也必须是组合拳：按 IP 堵 + 收敛出站 DNS + 主机行为监测 + sinkhole，缺一环就漏。

**3. 自更新通道是双刃剑，也是机会。** 替换载荷走明文 HTTP、无签名、无完整性校验——**谁控制更新主机，谁就控制整个 botnet**。对防守方而言，这意味着出站到更新域名的 HTTP 流量是优先级很靠前的监测项；对研究者而言，这也是 botnet 运营者极为要害的单点风险。

**4. 自动化沙箱的天花板。** Joe Sandbox 给 24 分，Joe Reverser 给 98 分。面对「行为温和、逻辑完整」的静态编译 bot，别只依赖自动化判定——人工逆向和配置解密才是看清威胁的路径。这个教训对所有「疑似但不确定」的样本都适用。

**参考来源**

* Joe Security《PHP2Shell 关联载荷深度逆向报告》（2026-10-22）https://www.joesecurity.org/reports/report-b61a098fc62a...