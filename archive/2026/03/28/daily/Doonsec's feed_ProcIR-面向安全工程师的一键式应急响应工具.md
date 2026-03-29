---
title: ProcIR-面向安全工程师的一键式应急响应工具
url: https://mp.weixin.qq.com/s/cnqN8cvHK5O1CckTp4UsEg
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:31:39.489591
---

# ProcIR-面向安全工程师的一键式应急响应工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TAFC5BLa6G1PrcCCC2gnrwfFic0UAZSauSFVxtvXeQVrneCpPC5H1LAtzXdUlK28OhWI4cpLFy7gmZPCxy5tx8dfZl8eGgrbbwg0AHusF3NM/0?wx_fmt=jpeg)

# ProcIR-面向安全工程师的一键式应急响应工具

原创

黑屋安服仔
黑屋安服仔

漕河泾小黑屋

![]()

在小说阅读器中沉浸阅读

## 前言

做应急响应的师傅们应该都有过这种体验：

接到电话，上机排查，然后开始一套组合拳——tasklist、netstat、autoruns、schtasks、wmic、reg query……一个个命令敲完，再逐条比对，光是把"当前系统到底跑了啥"搞清楚，可能半小时就过去了。

更难受的是，很多攻击不是"正在运行"的，它可能是一个定时任务、一个 WMI 订阅、一个白加黑——你用 tasklist 根本看不到，但它就在那等着被触发。

所以我写了 **ProcIR**。

一个面向安全工程师的 Windows 应急响应排查工具，一次扫描，把进程、持久化、历史痕迹、事件日志、DLL 加载、内存布局全看了，按风险评分排好序，直接告诉你该看哪个。

---

## 这个工具解决什么问题

一句话：**在应急响应中，用最短时间发现最可疑的东西。**

不是杀软，不做查杀。不联网，不上传。不常驻，不监控。

扫一次，看结果，辅助研判。

---

## 设计思路：不是单点检测，是多维融合

市面上大部分排查工具的思路是"逐项检查"——看进程列表、看自启动、看网络连接，各看各的，然后人工脑内关联。

ProcIR 的核心设计思路不一样：**把所有维度采集到的数据，归一到同一个对象上，做融合评分。**

### 统一对象模型

举个例子，假设 `C:\Users\Public\evil.exe` 这个文件：

* 在「活跃进程」里，它 PID 是 1234，在跑
* 在「注册表 Run」里，它被写了自启动
* 在「计划任务」里，有个任务指向它
* 在「Prefetch」里，它执行过 3 次
* 在「事件日志」里，4688 记录了它的创建
* 在「DLL 模块」里，它加载了一个同目录的未签名 version.dll

传统工具你得在 6 个不同的地方分别发现这些信息，然后自己拼起来。

ProcIR 的做法是：这 6 条线索全部关联到同一个 `ExecutionObject`，统一打分：

```
ExecutionScore (进程评分)     = 47
TriggerScore   (触发器评分)   = 35
ForensicScore  (历史痕迹评分) = 20
EventScore     (事件评分)     = 25
DLLHijackScore (模块评分)     = 65
SynergyBonus   (组合加权)     = 40
─────────────────────────────
FinalScore                    = 232 → Critical
```

一眼就知道该先看谁。

---

## 八个分析维度

### 1. 运行态：当前谁在跑

枚举所有活跃进程，提取：

* PID / PPID / 进程名 / 完整路径 / 命令行 / 用户 / 启动时间
* 文件 SHA256 / MD5
* 数字签名验证（WinVerifyTrust）
* 父子进程关系分析
* 40+ LOLBin 识别
* 系统文件名伪装检测（svchost.exe 是不是真的在 System32？）

### 2. 触发态：谁在等着被触发

不只看"正在运行"，还看"未来会运行"：

* 注册表 Run / RunOnce（6 个位置）
* Startup 文件夹
* 计划任务（深度解析：作者、触发方式、是否隐藏、运行账户、执行间隔）
* 系统服务（启动类型、ServiceDLL）
* WMI 事件订阅（EventFilter + Consumer + Binding 完整链路）
* IFEO 调试器劫持
* Winlogon Shell/Userinit 劫持

### 3. 历史态：谁曾经来过

即使样本已删除、进程已退出：

* **Prefetch**：Windows 预取文件，记录了曾经执行过什么
* **最近文件修改**：72 小时内用户目录/Temp 下新建的 exe/dll/脚本
* **事件日志**：4688 进程创建、4104 PowerShell 脚本块、7045 服务安装、4698 任务创建
* **DLL 模块枚举**：所有进程加载的 DLL

### 4. 事件态：系统记录了什么

从 8 个日志源提取高价值事件：

* Security（4688/4697/4698/4702/4624/4625/4648/4672）
* System（7045）
* PowerShell Operational（4104）
* TaskScheduler Operational
* WMI Activity
* Sysmon（如果有，自动检测）

### 5. 模块态：白加黑检测

这是实战中最高频的攻击手法之一。

核心检测逻辑：

* **签名进程 + 用户目录未签名 DLL = 白加黑**（+40 分）
* **EXE 同目录未签名 DLL = 经典侧加载**（+35 分）
* **系统进程加载用户目录 DLL = 极高危**（+50 分，直接 Critical）
* **系统 DLL 名 + 非系统路径 = 伪装**（+30 分）

内置 50+ 个常见被侧加载的系统 DLL 名。

### 6. YARA：内容级检测

内置了一个纯 Go 实现的 YARA 引擎（不需要 GCC/CGO），支持：

* 文本字符串（nocase / wide / fullword）
* 十六进制模式（含通配符）
* 正则表达式
* 条件语法

在 YARA 页面上传规则文件，一键全量扫描，只扫可疑对象，自动跳过已签名系统文件。

### 7. 内存态：无文件攻击检测

对指定 PID 执行 `VirtualQueryEx`，枚举全部内存区域：

* **RWX 内存** → 可能的 Shellcode 注入
* **私有可执行内存** → 无文件映射的代码执行
* **非映像可执行区域** → Reflective DLL / 内存加载

自动排除浏览器/JIT 引擎的正常 RWX。

### 8. IOC 监控：动态命中

输入威胁情报 IP/域名列表，实时监控 TCP 连接表，命中时精准归因到进程。

纯内核表读取，零网络影响。域名在加载时一次性解析为 IP，监控期间不做任何 DNS 操作。

---

## 评分模型：为什么不是简单规则匹配

单一维度的检测太容易误报。`cmd.exe` 本身合法，`rundll32.exe` 本身合法，甚至"用户目录有个 exe"也不一定恶意。

ProcIR 的评分是**多层叠加**的：

### 基础规则层

每个维度独立打分。单一维度很难超过 Medium。

### 强规则层（Override）

某些组合直接判定高危，不依赖基础分：

* Office 派生 PowerShell + 编码执行 → 直接 Critical
* regsvr32 远程 Scriptlet 加载 → 直接 Critical
* 系统进程加载用户目录 DLL → 直接 Critical

### 组合加权层（Synergy）

多个维度同时命中时额外加分：

* 命令行异常 + 外联 = +15
* 外联 + 持久化 = +20
* 事件证据 + YARA 命中 = +20
* DLL 劫持 + 外联 = +20

### 白特征抵消层（Anti-FP）

降低正常软件误报：

* 微软签名 + System32 路径 → 减分
* 已知厂商签名（Google/Adobe/腾讯/阿里等 20+）→ 减分
* 浏览器 Native Messaging → 减分

### 上下文权重

命令行命中规则的进程，总分 ×1.5。 父子链异常的进程，总分 ×1.2。

**设计原则：单一维度不过高，多维度叠加才真正危险。**

---

## 行为链识别：从"点"到"链"

除了单点评分，ProcIR 还能自动识别完整的攻击链：

| 攻击链 | 检测模式 |
| --- | --- |
| 宏攻击链 | Word → PowerShell → 外联 |
| 浏览器利用链 | Chrome → cmd → powershell |
| 持久化执行链 | 文件落地 → 注册表写入 → Prefetch 执行记录 |
| WMI 后门链 | WMI Consumer → 脚本引擎 → URL |
| DLL 侧加载链 | 签名进程 → 用户目录 DLL |
| 下载执行链 | cmd /c → certutil/curl → 执行 |

命中行为链的分数会直接叠加到关联的执行对象上。

---

## 技术实现

纯 Go，外部依赖只有 `golang.org/x/sys`（Windows API 绑定）。

* 进程枚举：`CreateToolhelp32Snapshot` + `NtQueryInformationProcess`（读 PEB 拿命令行）
* 数字签名：`WinVerifyTrust` + `GetFileVersionInfo`
* 网络连接：`GetExtendedTcpTable` / `GetExtendedUdpTable`
* 持久化：注册表 API + SCM API + 计划任务 XML 解析 + WMI 查询
* 事件日志：`wevtutil`（支持在线和离线 .evtx）
* DLL 模块：`CreateToolhelp32Snapshot(TH32CS_SNAPMODULE)`
* 内存分析：`VirtualQueryEx`
* YARA：纯 Go 实现的规则解析器 + 模式匹配引擎
* GUI：内嵌 HTTP 服务器 + HTML/JS 单页应用（不需要 Node.js / Electron）

52 个 Go 源文件，11,700+ 行代码，编译产物 11MB。

---

## 使用场景

**场景 1：常规应急**

上机 → 运行 procir.exe → 点"开始扫描" → 看"执行对象"视图 → Critical 和 High 的先查 → 右键复制 SHA256 去 VT 确认

**场景 2：白加黑排查**

扫描 → 看"模块分析"视图 → 有没有签名进程加载了用户目录的未签名 DLL → 双击看详情

**场景 3：持久化排查**

扫描 → 看"触发器"视图 → 排序看高分的 → 是不是有可疑的计划任务/WMI/服务

**场景 4：威胁情报碰撞**

扫描 → 切到"IOC 监控" → 粘贴情报 IP 列表 → 开始监控 → 看有没有进程在连这些 IP

**场景 5：可疑进程深挖**

进程视图发现一个高分进程 → 切到"内存分析"输入 PID → 看有没有 RWX 内存 → 切到 YARA 上传规则扫一下

---

## 最后

工具地址：**https://github.com/dogadmin/ProcIR**

单文件，11MB，管理员运行，扫完即走。

不是杀软，不做查杀，只帮你更快找到该看的东西。

如果对你有帮助，给个 Star。有问题欢迎提 Issue。

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