---
title: 桌面壁纸层监控HUD踩坑实录
url: https://yanghaoi.github.io/2026/10/04/zhuo-mian-bi-zhi-ceng-jian-kong-hud-cai-keng-shi-lu/
source: Yang Hao's blog
date: 2026-10-03
fetch_date: 2026-10-04T07:37:54.167602
---

# 桌面壁纸层监控HUD踩坑实录

[![LOGO](/medias/logo.webp)
Yang Hao's blog](/)

* [首页](/)
* 文章
  + [标签](/tags)
  + [分类](/categories)
  + [归档](/archives)
* [关于](/about)
* [留言板](/contact)

![](/medias/logo.webp)

Yang Hao's blog

Yang Hao's blog

* [首页](/)
* 文章
  + [标签](/tags%20)
  + [分类](/categories%20)
  + [归档](/archives%20)
* [关于](/about)
* [留言板](/contact)

# 桌面壁纸层监控HUD踩坑实录

[Windows](/tags/Windows/)
[Win32](/tags/Win32/)
[Direct2D](/tags/Direct2D/)
[C++](/tags/C/)

[杂记](/categories/%E6%9D%82%E8%AE%B0/)

发布日期:
2026-10-04

更新日期:
2026-10-04

文章字数:
12.5k

阅读时长:
47 分

阅读次数:

---

最近在做一个 Windows 桌面小工具：一块半透明的系统监控面板（CPU / 内存 / GPU / 显存 / 磁盘 / 网络），要“沉”到**桌面壁纸层之上、桌面图标之下**——按 `Win+D` 不消失，鼠标点击完全穿透，不进任务栏也不进 `Alt+Tab`。产物是一个纯原生、静态链接、约 2 MB 的单 exe，除系统 DLL 外零依赖，默认完全离线。源码已开源：**[yanghaoi/AuraUI](https://github.com/yanghaoi/AuraUI)**（MIT 许可）。

目标是它看起来的样子：

![半透明面板嵌在桌面壁纸层上](/2026/10/04/zhuo-mian-bi-zhi-ceng-jian-kong-hud-cai-keng-shi-lu/AURA-IMG-00.webp)

这个需求听起来像是“设几个窗口样式”的事。真正动手之后才发现，Windows 并没有任何公开 API 表达“把窗口放在壁纸和图标之间”这件事，于是整条路径只能靠未文档化的消息、跨进程 `SetParent`、以及对 shell 行为的实测推断来拼。拼出来的过程中踩到一串坑，共同点是——**API 全部返回成功，而结果都是错的**：

* `SendMessageTimeout(progman, 0x052C, 0, 0, …)` 返回成功，但 shell 什么都没做，窗口静默隐身；
* `UpdateLayeredWindow` 每秒返回成功，窗口属性读数全部健康，屏幕上却什么都没有；
* 解码“注册表里那个壁纸文件”得到的像素，和屏幕上真实显示的差了 ~15/255；
* 子窗口隐藏后，它的最后一帧永久僵死在桌面上；
* 托盘的左键、右键“全部无响应”，原因是把回调参数读反了。

下文先把可直接取用的结论列出来，再逐条展开现象、定位过程和最终方案，最后附上代码级问题清单与调试方法论。所有结论都在 Windows 10 19045（部分场景经 RDP 会话）上实测验证；第 13 节那五处修改另在 MinGW-w64 下**实际构建过**（零警告），其中 13.3 做了修改前后 `--dump` 逐像素对比，13.2 用独立测试程序验证了契约告警，并跑过端到端验证脚本。

## 1 结论

如果也在做类似的事，以下几条可以直接取用：

1. `0x052C` 的 **wParam 必须是 `0xD`**。写 `(0, 0)` 时 shell 静默无操作，壁纸层保持隐藏，挂上去的窗口属性全对但不可见——这是本项目最大的坑。
2. **不要挂 `Progman`**。`SHELLDLL_DefView` 会抓取父窗口的图像缓冲画自己的背景，它下面被盖住、上面盖住图标，没有可用位置。
3. 按类名找 `WorkerW` **不可靠**：窗口类按进程注册、类名可以重名。宿主必须同时满足「可见 + 属于 Explorer + 不含 `SHELLDLL_DefView`」。
4. **跨进程 `SetParent` 之后，分层子窗口在本机不可靠**，观察到三种互相独立的失效模式。挂载态只能用普通 GDI 重定向路径（非分层 + `WM_PAINT`/`BitBlt`）。
5. **半透明靠“壁纸垫底”实现**：解码壁纸、按摆放样式裁成面板尺寸的不透明裁片垫在面板下，再画半透明面板——表面不透明，`BitBlt` 安全，视觉等价透明。
6. **垫底必须解码 shell 实际显示的那一层缓存**（`Themes\CachedFiles\CachedImage_*`），不是注册表解析出的原图。用错层，圆角切除区会把“另一代编码”的裁片直接贴在真实桌面上。
7. 桌面层 WorkerW **从不重绘被腾出的区域**，子窗口移动/隐藏后会留下永久残影。修复首选“直接把正确的壁纸像素画到宿主表面”，SPI 重放只作兜底。
8. 托盘回调在 `NOTIFYICON_VERSION_4` 下 **`wParam` 是坐标、`lParam` 是事件**，且同一次点击会同时投递裸鼠标消息和抽象事件——只处理抽象事件，否则每个动作执行两遍。
9. ICO 的每个条目必须是**完整 DIB**（`BITMAPINFOHEADER` + XOR 像素 + AND 掩码）。缺头部时 `windres` 原样嵌入，`LoadImage` 静默失败并回退系统默认图标。
10. MinGW-w64（binutils ≥ 2.44）会自动链接一份 `RT_MANIFEST` **ID 1**，项目自带的 manifest 必须放 **ID 2**，再用 `CreateActCtxW` 显式激活。
11. **GPU 不要引入 SDK**：`nvml.dll` 运行时 `LoadLibraryExW` + `GetProcAddress`（符号带 `_v2` 回退），没卡就显示 `N/A`——产物才能保持零依赖。
12. **速率类指标的基线要带适配器标识**（网络用 LUID）：换网卡时重新起步，否则两块卡各自的累计计数相减会报出 TB/s 级假尖峰。

概括为一句话：**窗口属性读数、API 返回值、乃至“设置成功”的回读，都不能作为“屏幕上真的对了”的依据。**

## 2 目标与总体结构

### 2.1 桌面层的窗口拓扑

`desktop/desktop.cpp` 负责让 HUD 真正“沉”到桌面图标下面。壁纸层建好之后的拓扑是：

```
WorkerW  (图标宿主)   <- 内含 SHELLDLL_DefView -> SysListView32
WorkerW  (壁纸层)     <- HUD 挂这里
Progman
```

壁纸层 = **全屏、可见、属于 Explorer、且不含 `SHELLDLL_DefView`** 的 `WorkerW`。它的位置随 shell 版本变化：Windows 10 ~ 11 23H2 是顶层 `WorkerW`，而 Windows 11 24H2+（或 Win10 上发过一次 `0x052C` 之后）它会变成 `Progman` 的直接子窗口——所以两处都要找。

![桌面窗口拓扑与宿主筛选条件](/2026/10/04/zhuo-mian-bi-zhi-ceng-jian-kong-hud-cai-keng-shi-lu/AURA-IMG-01.svg)

图里右侧那三个条件，每一条都对应一次“窗口看不见”的实测：

* **可见**：父窗口隐藏时，子窗口自己的 `WS_VISIBLE` 仍是 `TRUE`，但屏幕上什么都没有。而壁纸层是**懒加载**的，系统刚启动时它可能根本不存在。
* **属于 Explorer**：窗口类按进程注册，类名可以重名，而 `FindWindowExW(..., L"WorkerW", ...)` 只比对类名字符串。实测本机 18 个 `WorkerW` 里有 3 个属于第三方：

  ```
  0x5108e0  WorkBuddyAI.exe     visible=False  Explorer的吗=NO
  0x2505ec  Everything.exe      visible=False  Explorer的吗=NO
  0x160170  RuntimeBroker.exe   visible=False  Explorer的吗=NO
  ```
* **不含 `SHELLDLL_DefView`**：含 DefView 的是图标宿主，不是壁纸层。

挂载本身还有个顺序要求（MSDN 明文）：**先把窗口样式从 `WS_POPUP` 改成 `WS_CHILD`，再 `SetParent`**。跳过这一步，窗口会停在“半挂载”状态，`GetParent()` 返回 `NULL`，z 序与坐标换算全乱。

### 2.2 线程模型

采集全部在后台采样线程完成，UI 线程只做一次 `Snapshot` 拷贝与绘制；壁纸解码另起一个 worker。

![线程模型与源码模块划分](/2026/10/04/zhuo-mian-bi-zhi-ceng-jian-kong-hud-cai-keng-shi-lu/AURA-IMG-09.svg)

跨线程只走消息，不共享可变状态：采样线程 `PostMessage(kMsgSnapshot)` 通知 UI 重绘，垫底 worker `PostMessage(kUnderlayReadyMsg)` 通知 UI 套用新裁片。健康检查每 2 秒跑一次，负责“重挂 / z 序自愈 / 显示器变化 / 托盘补挂”。

## 3 采集：把机器状态读出来

前两节讲的是「窗口怎么摆」。但 HUD 的正事其实是另一件事——**把当前环境的资源占用读出来**。这一节记录五个指标的取数方式、必须处理的边界，以及两块容易被略过的东西：**静态硬件身份**和**失联自愈**。

### 3.1 Snapshot 与节拍

所有指标打包进一个 `Snapshot`，由采样线程产出、UI 线程按值拷贝消费：

```
struct Snapshot {
    CpuInfo     cpu;      // usage + 型号 / 核心 / 线程
    MemoryInfo  memory;   // total / used / available / percent + "DDR4 2133MHz 32GB"
    GpuInfo     gpu;      // name / usage / vram / temp / power（各带 has* 有效位）
    DiskInfo    disk;     // valid + letter / total / free / used / percent
    NetworkInfo network;  // downBps / upBps + 适配器 / IPv4 / IPv6 / MAC / 网关
    unsigned long long sampleIndex;
    double             elapsedSec;   // 距上一拍的秒数，速率类指标要用它
};
```

每项都带自己的「有没有值」标志（`valid` / `hasUsage` / `hasVram` / `hasTemp`…），渲染端据此决定画进度条还是显示 `N/A`。**没有 NVIDIA 显卡、没有网卡、磁盘不存在时全部走 `N/A`，不崩**——这是「离线小工具」的基本体面。

采样线程的节拍是**绝对**的：

```
auto next = steady_clock::now() + milliseconds(intervalMs);   // 起点
while (!stopping_) {
    cv_.wait_until(lock, next, ...);
    ...
    next += milliseconds(intervalMs);                          // 下一拍 = 上一拍 + interval
    if (next <= steady_clock::now())                           // 落后就跳过，不补跑
        next = steady_clock::now() + milliseconds(intervalMs);
}
```

写成「采样结束 + interval」的话，**每一轮都会把采样耗时累积进去**（NVML 调用、网卡枚举都不便宜），跑久了节拍就漂。暂停时不采样，但仍响应唤醒（改间隔 / 恢复监控），并把节拍重新锚定，避免 `wait_until` 在一个已经过去的时间点上空转。

还有一个容易忽略的细节：`Start()` 里**先同步采一次**，再起线程。这样首帧——以及「启动时就处于暂停态、永远收不到 tick」这种情形——拿到的是真值而不是一排 0。差值类指标（CPU、网络速率）第一拍天然是 0%，从第二拍才动。

![采集节拍数据源与失联自愈](/2026/10/04/zhuo-mian-bi-zhi-ceng-jian-kong-hud-cai-keng-shi-lu/AURA-IMG-12.svg)

### 3.2 CPU：两次采样求差

`GetSystemTimes` 返回三个累计时间：`idle`、`kernel`、`user`。这里有个经典陷阱——**`kernel` 已经包含 idle 时间**，所以：

```
total = dKernel + dUser;                 // ✅ 不要再加 dIdle
busy  = total - dIdle;
pct   = 100.0 * busy / total;
```

按「idle + kernel + user」求和会把空闲时间算两遍，负载被系统性低估。另一个边界是 `total == 0`（两次采样之间系统时间没动，比如刚从休眠醒来），此时直接沿用上一拍的读数，而不是除零。

第一次调用只用来**建立基线**（记下三个累计值并返回上次读数），所以进程刚起来那一拍的 CPU 是 0%。

原始差值在 100 ms 这种短间隔下相当跳，所以做了一次轻量指数平滑：`last_ = last_ * 0.35 + pct * 0.65`。新值权重 0.65——既要压住抖动，又不能让数字看起来「慢半拍」。

### 3.3 内存与磁盘

内存直接取 `GlobalMemoryStatusEx`：`used = ullTotalPhys - ullAvailPhys`。注意用的是 `ullAvailPhys`（可用）而不是「空闲」，那才是用户视角的剩余内存。

磁盘用 `GetDiskFreeSpaceExW`，盘符**从 `GetWindowsDirectoryW` 取**而不是硬编码 `C`——系统装在别的盘上的机器不少。拿不到（卷消失、无权限）就把 `valid` 置 false，整行显示 `N/A`，不抛也不崩。

### 3.4 网络：速率与适配器

网络这项信息量最大，一次采样要同时产出**速率**和**适配器信息**。

速率来自 `GetIfTable2` 的 64 位计数器 `InOctets` / `OutOctets`，两次采样求差再除以 `elapsedSec`。这里有三条边界，每条都对应过一次真实故障：

* **基线必须携带适配器 LUID。** 切换网卡（拔插、VPN 出现、重新排名）后，新网卡的计数器是从开机起累计的另一条序列，拿它去减旧网卡的读数会得到一个 TB/s 级的假尖峰。检测到 LUID 变化就丢弃基线、重新起步。
* **`GetIfTable2` 失败也要重置基线。** 否则下一次成功的采样会把「两个间隔的流量」除以「一个间隔的时间」，速率虚高一倍。
* **计数器可能回绕。** 网卡重启后计数器归零，差值取 `in >= prev ? in - prev : 0`——宁可这一拍显示 0，也不报一个负数或天文数字。

适配器信息来自 `GetAdaptersAddresses`，需要一层过滤加一层排序：

```
if (a->IfType == IF_TYPE_SOFTWARE_LOOPBACK) continue;   // 回环
if (a->OperStatus != IfOperStatusUp) continue;          // 未启用
// 地址层面再剔掉 APIPA(169.254.x.x) 与链路本地(fe80::/10)
```

排序打分是「有网关 +4 / 有 IPv4 +2 / 有 IPv6 +1」，取最高分的那块——也就是「最像正在上网的那块」。但**选中的适配器不能每轮重选**：列表重新枚举时，一块短暂出现的 VPN 可能排到前面，监控对象就跳了。所以按 **LUID 优先、名字兜底**沿用上一轮的选择。

适配器列表本身有 5 秒刷新节流；只有在「本轮没找到该适配器」时才置脏、下一拍强制重枚举。

### 3.5 GPU：动态绑定 NVML

GPU 是唯一需要「额外能力」的指标。这里刻意**不把 CUDA / NVML SDK 作为构建依赖**——`nvml.dll` 在运行时用 `LoadLibraryExW` 加载，每个入口点用 `GetProcAddress` 解析，ABI 子集自己写在 `system/nvml_api.h` 里（9 个函数指针）。产物因此仍然是「除系统 DLL 外零依赖」的单个 exe。

几个工程细节：

* **只从绝对路径找 dll**（`%SystemRoot%\System32\nvml.dll`、`%ProgramW6432%\NVIDIA Corporation\NVSMI\nvml.dll`），避开工作目录的 DLL 劫持。
* **符号带 `_v2` 回退**：`nvmlInit_v2` 找不到就用 `nvmlInit`，`nvmlDeviceGetCount_v2` → `nvmlDeviceGetCount`，以此类推——老驱动只导出旧名。
* **必需符号用 `Api::Complete()` 一次性校验**，缺一个就 `FreeLibrary` 走人，不留下半个可用的句柄。
* **采集项彼此独立**：使用率（`getUtilizationRates`）、显存（`getMemoryInfo`）、温度、功耗（毫瓦 → 瓦）各判各的返回值。温度传感器在某些卡上不可用，不该连带把使用率也变成 `...