---
title: LinIR-Linux下的应急响应采集工具
url: https://mp.weixin.qq.com/s/KhlXC1Oxu37xr_3fjAncWg
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:21:15.057668
---

# LinIR-Linux下的应急响应采集工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TAFC5BLa6G1S9jzVDbYP3icvh3kNh6c0njNckib4IkCKHT0MgUO2OK6z0mN5uuWpW9tQgtRQw2InxLia1Qaor7X3ialCBVf3VmD0NuuN7636BLk/0?wx_fmt=jpeg)

# LinIR-Linux下的应急响应采集工具

原创

黑屋运维
黑屋运维

漕河泾小黑屋

![]()

在小说阅读器中沉浸阅读

> 当你登上一台可能已被入侵的服务器，你敢相信上面的 `ps`、`netstat`、`ss` 吗？

---

## 一、问题：你以为在取证，其实在被骗

应急响应的第一步通常是"看看机器上在跑什么"。大多数人的第一反应是：

```
ps auxnetstat -tnlpss -tnpcrontab -lsystemctl list-units
```

这些命令在 99% 的日常运维场景里完全够用。但在**应急响应**场景下——你面对的可能是一台已经被 rootkit 接管的主机。

问题来了：

* `ps` 可以被替换成一个过滤掉恶意进程的二进制
* `netstat`/`ss` 可以通过 `LD_PRELOAD` 劫持 libc 来隐藏连接
* `crontab -l` 如果被 hook，可能根本不显示攻击者写入的定时任务
* `systemctl` 通过 D-Bus 通信，中间环节太多，任何一层都可能被污染
* 就连你的 `PATH` 本身都可能指向一个 `/tmp/.hidden/bin/` 目录

传统的应急响应工具——无论是手工命令行还是自动化脚本——几乎都默认信任了目标系统的用户态工具链。

**这就是 LinIR 要解决的核心问题。**

---

## 二、LinIR 是什么

LinIR（Linux Incident Response）是一个面向 Linux 和 macOS 的单二进制取证分诊工具。它的设计出发点只有一个：

> **不信任目标主机上的任何命令。**

它不调用 `ps`，而是直接读 `/proc/<pid>/stat`、`/proc/<pid>/exe`、`/proc/<pid>/cmdline`。

它不调用 `netstat`/`ss`，而是直接解析 `/proc/net/tcp`、`/proc/net/tcp6`，再通过遍历 `/proc/<pid>/fd/` 的 socket inode 来关联 PID。

它不调用 `systemctl`，而是直接解析 systemd unit 文件的 `ExecStart`、`Environment`、`WantedBy` 字段。

它不调用 `crontab`，而是直接扫描 `/etc/crontab`、`/etc/cron.d/`、`/var/spool/cron/` 下的原始文件。

它不调用 `lsof`，而是自己构建 inode → PID 映射表。

在 macOS 上也一样：不调用 `launchctl`、`lsof`、`nettop`，而是使用 `sysctl`、`proc_pidinfo`、`proc_pidfdinfo` 等 syscall 级接口。

**整个工具从采集到分析到评分，零外部命令依赖。** `CGO_ENABLED=0` 静态编译，单文件拖到目标机就能跑。

---

## 三、与传统工具/方案的对比

### 和手工命令行对比

| 维度 | 手工命令行 | LinIR |
| --- | --- | --- |
| 信任模型 | 完全信任系统命令 | 零信任，直接读内核接口 |
| rootkit 对抗 | 无 | 多源交叉验证（进程/网络/文件/模块视图对比） |
| 环境检测 | 无 | 自检 LD\_PRELOAD/PATH/DYLD 污染 |
| 结果格式 | 文本，需人工整理 | JSON/CSV/文本/tar.gz 分诊包 |
| 可重复性 | 低（依赖操作者经验） | 高（同一二进制，同一输出结构） |
| 评分 | 无 | 加权证据评分 0-100 |

### 和自动化脚本（GScan、LinPEAS 等）对比

| 维度 | 典型脚本工具 | LinIR |
| --- | --- | --- |
| 实现方式 | Shell/Python，调用系统命令 | 纯 Go，直接读 /proc 和 syscall |
| rootkit 场景 | 输出可被篡改 | 不经过用户态工具链 |
| 跨平台 | 通常仅 Linux | Linux + macOS 统一 |
| 依赖 | 需要 bash/python/perl | 零依赖，静态二进制 |
| 维护成本 | 脚本碎片化 | 单一代码库，类型安全 |

### 和 EDR/商业方案对比

| 维度 | EDR | LinIR |
| --- | --- | --- |
| 部署 | 需安装 agent，持续运行 | 单次执行，用完即走 |
| 权限 | 需要持久化 root 权限 | 按需 sudo，不驻留 |
| 适用场景 | 持续监控 | 事后分诊、IOC 排查 |
| 联网要求 | 通常需要云端通信 | 完全离线可用 |
| 费用 | 商业授权 | MIT 开源 |

**LinIR 不是 EDR 的替代品。** 它更像是应急响应人员的"一次性手术刀"——拖上去、扎一刀、取证据、撤走。不需要安装，不需要配置，不需要联网。

---

## 四、核心功能

### 一次性采集

一条命令完成全套采集：

```
sudo ./linir collect --yara-rules /opt/rules/ --bundle
```

自动执行：自检 → 环境预检 → 进程枚举 → 网络采集 → 持久化扫描 → 完整性检查 → 跨域关联 → YARA 扫描 → 证据评分 → 输出（JSON + 文本 + CSV + tar.gz）。

### IOC 在线监控

```
sudo ./linir watch --iocs ./iocs.txt
```

持续监控主机网络连接，与 IOC 列表实时比对。三层监控架构：

* **层 1**：Linux conntrack netlink / macOS BPF 事件驱动（零遗漏）
* **层 2**：/proc/net/nf\_conntrack 轮询（RST 连接保留 ~10s）
* **层 3**：/proc/net/tcp 轮询（通用回退）

命中后自动补采进程上下文、二进制哈希、持久化关联、YARA 扫描，形成结构化、带评分的命中事件。

### Web 仪表盘

```
sudo ./linir gui
```

暗色主题的交互式仪表盘，支持一键采集、风险评分可视化、进程/网络/持久化表格搜索过滤、IOC 实时监控（SSE 事件流）、YARA 扫描。全部通过 `go:embed` 打包到二进制中，无额外文件。

### 评分体系

不是简单的"有就报"，而是**单点低分 + 组合高分 + confidence 分离**：

* `/tmp` 下有个可执行文件？仅 +10 分（可能是安装器解包）
* 但如果它还在联网、还关联了持久化、还命中了 YARA？那就是 +10 +10 +10 +20 +10（combo）= 60 分，severity: high
* 父进程是 `apt-get`？分值自动减半（suppress 机制）
* 主机可信度 low？不直接堆分，而是降低 confidence 并记录到 `integrity_flags`

这样干净系统趋近 0 分，真实威胁才会拉高分数。

---

## 五、诚实说不足

### IOC 监控的 PID 归属问题

这是目前最大的已知限制，也是花了最多时间解决的问题。

Linux 的 `/proc` 文件系统有一个根本性特点：**进程退出后，它在 /proc 下的所有信息立即消失。** 这意味着如果一个进程（比如 `curl`）发起了一个 HTTP 请求然后退出，从网络层看到连接的时候，进程可能已经不存在了——你知道有个连接去了恶意 IP，但你不知道是谁发起的。

LinIR 的应对策略是多层的：

1. **conntrack 事件驱动**：在 SYN 阶段就捕获事件（此时进程还在）
2. **快速定向查找**：不做全量 /proc 扫描，而是针对性地找 inode → PID（~10-50ms）
3. **多次重试**：在 socket FD 消失前抢时间
4. **pending 队列**：抓不到就等下一次轮询补全
5. **进程名回退**：即使进程退出了，之前从 `/proc/<pid>/comm` 采到的名字还在

但对于极短命进程（< 100ms），PID 归属成功率确实不是 100%。这不是代码 bug，而是 Linux /proc 的设计使然——`ss -tnp` 也有同样的问题。完美解决需要 eBPF，但那会引入内核版本依赖，与 LinIR 的"零依赖"原则冲突。

**当前策略：事件不丢，PID 尽量补。** 补不到的标记为 `pid_resolve_state: unresolved`，不影响事件本身的存在性。

### macOS 的能力边界

macOS 没有 `/proc`，没有 conntrack，SIP 会限制某些 `proc_pidfdinfo` 调用。当前通过 `/dev/bpf` 抓包 + `proc_pidfdinfo` 快照来工作，但：

* BPF 只能看到经过网卡的包，回环接口需要额外处理
* UDP IOC 监控刚加入（之前只有 TCP SYN）
* sysctl pcblist\_n 的 PID 提取依赖结构体偏移，Apple 换版本可能失效

### 评分的局限

评分是"基于规则的加权模型"，不是机器学习。它能覆盖已知的攻击模式和异常模式，但：

* 无法识别全新的、不匹配任何规则的攻击
* 组合规则需要人工设计，不能自动发现新的关联模式
* suppress 机制基于进程名白名单，攻击者如果伪装成 `apt-get` 就能绕过

### 不是 EDR，不做持续监控

LinIR 定位是**一次性分诊工具**。`watch` 模式虽然可以持续运行，但它不会：

* 自动修复或隔离威胁
* 向云端报告
* 与 SIEM 实时联动
* 自动更新规则

它的定位是给应急响应人员一个快速、可信、结构化的起点。

---

## 六、一些设计选择的解释

### 为什么不用 eBPF？

eBPF 确实是 Linux 上最强大的内核观测工具。但：

* 需要内核版本 >= 4.x（某些功能需要 5.x）
* 需要特定内核配置（`CONFIG_BPF`、`CONFIG_BPF_SYSCALL`）
* 需要 BTF 或手动适配不同内核版本
* 违反"单二进制零依赖"的原则

LinIR 选择基于 `/proc` + netlink + BPF（macOS）的方案，能在几乎所有 Linux 2.6+ 和 macOS 10.15+ 上运行。未来可能作为可选增强引入 eBPF，但不会作为主路径。

### 为什么用 Go？

* `CGO_ENABLED=0` 可以完全静态编译
* 交叉编译到 8 个 Linux 架构 + 2 个 macOS 架构只需要 `GOOS=xxx GOARCH=xxx go build`
* 没有运行时依赖（不需要 libc、不需要 Python、不需要 JVM）
* 并发模型适合同时采集多个数据源
* 二进制大小 ~11MB，可以 scp 到任何目标机

### 为什么证据优先于结论？

LinIR 不会告诉你"这台机器被黑了"。它会告诉你：

* PID 1234 的 exe 在 /tmp 下（+10）
* 它有到 1.2.3.4:443 的 ESTABLISHED 连接（+10）
* 它关联到一个 crontab 持久化项（+10）
* YARA 规则 "webshell\_php" 命中了它的 exe（+20）
* 组合：临时目录+YARA（+10）

总分 60，severity: high，confidence: high。

剩下的判断交给分析人员。工具给证据，人做决策。

---

## 七、最后

LinIR 是一个还在持续迭代的项目。目前 v1.0.0 覆盖了应急响应中最核心的几个环节：进程、网络、持久化、完整性、YARA、IOC 监控。

它不完美——PID 归属有竞速问题、macOS 支持有平台限制、评分模型需要持续调优。但它提供了一个**在不可信环境下尽量可信的取证起点**。

如果你是安全从业者、应急响应人员、或者对 Linux/macOS 内核取证感兴趣的开发者，欢迎试用和反馈。

**GitHub：** https://github.com/dogadmin/LinIR

MIT License，欢迎 Star、Issue、PR。

---

*本文基于 LinIR v1.0.0，工具仅用于授权的安全评估和应急响应。*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

漕河泾小黑屋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz/5r3L9YiaerKevqpmP3HJsIqs9ianF9A6r7GzqvlqSGQZheERk1PrZwHbhhcungUyYccRDRU3FJugqUWjicsXw7EWw/0)

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