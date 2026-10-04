---
title: 不写一行 shellcode，怎么把 DLL 塞进别人的进程？
url: https://mp.weixin.qq.com/s/MVGqOM4jdqZ5h_qiaVgPGw
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:34:35.496934
---

# 不写一行 shellcode，怎么把 DLL 塞进别人的进程？

# 不写一行 shellcode，怎么把 DLL 塞进别人的进程？

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

## 一、老办法为什么越来越不好使

教科书式的 DLL 注入是四件套：

```
OpenProcess  →  VirtualAllocEx  →  WriteProcessMemory  →  CreateRemoteThread(LoadLibraryW, 路径)
```

在目标进程里申请一块内存，把 DLL 路径字符串写进去，再创建一个远程线程，线程入口直接指向 `LoadLibraryW`，参数就是那个路径。DLL 一被载入，`DllMain` 自动执行，代码就算落地了。

问题在于，这套动作里的每一个 API 都已经被安全产品"记住了"。SafeBreach Labs 在研究中把进程注入拆成**三个原语**——分配（allocation）、写入（writing）、执行（execution）——然后用实验得出一个关键结论：

> **EDR 的检测重心几乎全压在「执行原语」上，而最基础形态的分配与写入原语，基本不被检测。**

于是思路就变了：**能不能构造一种只依赖"分配 + 写入"的执行原语？** 更进一步——如果执行的触发来自一个**完全合法的系统行为**，而不是攻击者显式发起的调用，会怎样？

Windows 用户态线程池，恰好就是这个问题的答案。

---

## 二、线程池：一个被低估的执行原语工厂

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GqNM9RMzsIKZe3DhZ5zwX7qEKoXVBRU6E8C2Ficia93luqjxB5ZRjsicU7PUlVibiaYIBPfsnEg4aSETLynDvpWEQPrpDSbCDafIcw/640?wx_fmt=png&from=appmsg)

现代 Windows 用户态进程都能访问 ntdll 的线程池实现。多数 GUI / 服务 / shell 进程（notepad.exe、explorer.exe、各类 svchost）一旦有线程池 API 或依赖子系统触发初始化，进程内就会存在可用的默认线程池状态。池一旦活跃，就是**三层协作结构**：

| 层 · 关键对象 | 作用 |
| --- | --- |
| 用户态句柄层 · `PTP_POOL` | 池的句柄，由 `CreateThreadpoolWork` 等返回 |
| 用户态工作项层 · `_TP_WORK` 等 | 装着**回调指针 + 上下文 + 清理组链接**的结构体 |
| 内核态调度层 · Worker Factory | 真正取任务、跑回调的那些线程 |

> 补充：前两层都位于**调用方堆上**；第三层由 `NtCreateWorkerFactory` 建立，位于系统地址空间。工作项类型除 `_TP_WORK` 外，还有 `_TP_TIMER`、`_TP_WAIT`、`_TP_IO`、`_TP_DIRECT`、`_TP_ALPC`、`_TP_JOB`。

对注入者来说，这个组件堪称完美目标，原因有四：

1. **所有 Windows 进程默认都有线程池**

   —— 意味着技术适用性覆盖全进程；
2. 工作项和池**都由结构体表示** —— 天然适合用"分配 + 写入"原语去构造执行原语；
3. 支持**多种工作项类型** —— 队列类型多，机会就多；
4. 组件**横跨内核态与用户态**，复杂度高 —— 攻击面自然被放大。

> 需要注意：线程池对用户代码是**故意不透明**的。`_TP_WORK` 的字段偏移不属于任何你可以 `#include` 的头文件，只有函数指针的原型是公开的。SafeBreach 的贡献正是逆向出这些结构，并证明——**只要能在目标进程地址空间里放一个语法合法的 `_TP_*` 结构，并向该进程的 worker factory "宣告"它的存在，线程池就会替你在目标进程里执行你的回调，而不需要你创建任何线程。**

### 一次"正常"的提交长什么样

```
ntdll!TpAllocWork  → RtlAllocateHeap                                  // 在本地堆上分配一个 TP_WORK  → TP_WORK.CleanupGroupMember.Pool = 进程默认池  → TP_WORK.Task.Callback          = 回调  → TP_WORK.Task.Context           = 上下文
ntdll!TpPostWork（或 SubmitThreadpoolWork）  → 把 TP_WORK 插入 Pool->WorkQueue（无锁链表）  → 置 WorkState.Exchange = 2                        // 标记为"可取"  → NtSetIoCompletion(Pool->IoCompletion, 1)         // 唤醒一个 worker 线程
[worker 线程在 NtRemoveIoCompletion 上醒来]  → 取 WorkQueue 队首  → 调用 TP_WORK.Task.Callback(TP_WORK.Task.Context)
```

两点值得留意：

* 回调**在操作系统已经拥有的 worker 线程里执行**，用户代码没有创建任何新线程；
* 整条"插入 + 派发"路径都经过一个**进程内的 I/O 完成端口**（`Pool->IoCompletion`），靠 `NtSetIoCompletion` 发信号唤醒。这个句柄，正是各个变体最终以不同方式去攻击的东西。

---

## 三、PoolParty 的三步原语

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GS8sibSxZg9SictjDF9I5pYloWZ6lXeToM61dia2PYGP7iaGgxiasT93MLGcs6cIY33txVEicqCPictib6zSXEdibNzia4GOGf01ic9qqdCY/640?wx_fmt=png&from=appmsg)

所有 PoolParty 变体都收敛为同一个三步形状，**差别只在第三步**：

```
1. OPEN    —— OpenProcess(目标, PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_DUP_HANDLE)2. WRITE   —— VirtualAllocEx(目标, RW) + WriteProcessMemory(伪造的 _TP_* 结构)              · 其 Task.Callback 指向要执行的代码              · 其 CleanupGroupMember.Pool 指向目标的默认池                （通过 NtQueryInformationProcess + ReadProcessMemory 读出来）3. ANNOUNCE—— 怎么告诉目标的 worker factory："醒醒，你队列里有新活了，地址在这儿"
```

SafeBreach 在 Black Hat Europe 2023 上给出了 **8 个变体**，可归为两类战术：

**七种"任务单投递"战术**（利用系统原生事件作触发器，把恶意回调塞进任务队列）：
`TP_WORK` 伪造高优先级任务单、`TP_WAIT` 绑定事件信号、`TP_IO` 伪装文件 I/O 完成包、`TP_ALPC` 冒充可信组件间通信、`TP_JOB` 利用进程加入作业对象事件、`TP_TIMER` 设置延迟/周期回调、以及直接向 IoCompletion 投递回调指针的裸完成包形态。

**一种"工人改造"战术**：绕过任务队列，直接篡改 Worker Factory 的 `StartRoutine`，让新生的工人线程一开始就跑攻击者的逻辑。

在当年的测试中，这套技术对五家主流 EDR（Palo Alto Cortex、SentinelOne、CrowdStrike Falcon、Microsoft Defender for Endpoint、Cybereason）达成了完全绕过。

> **重要澄清（本文增补）**：这类"100% 绕过"的结论是**2023 年时间点的测试快照**，不等于今天仍然成立。Trustwave 后续的 C# 实现 SharpParty 就观察到：微软在 2025 年 3 月收到报告并实现检测后，相关检出明显上升。**把这类结论当成永恒真相，是运维侧最容易踩的坑。**

---

## 四、"无 shellcode"到底难在哪：回调签名与参数位错位

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0F46PBNS5zE6auov7zy7dJI6JHjjic6icQiaSoqdMJJT2V9Np46jvMsIYZd6F5eeMLuOEFjLqpv4EOzh9QZcrvv8eEicetsAQIMzhk/640?wx_fmt=png&from=appmsg)

这是整件事**真正的技术内核**，也是最容易被含糊带过的地方。

经典 PoolParty 是把 shellcode 写进目标（往往是一块 RWX 内存），然后让 `Task.Callback` 指向它。所谓 **shellcodeless**，就是**不往目标里写任何自定义代码**，而是让回调直接指向一个目标进程里**已经存在的合法函数**——最自然的选择就是 `LoadLibraryW`。

听起来很直接，但一动手就会撞墙。公开资料里的实证把这个问题讲得很清楚：

`PTP_WORK_CALLBACK` 的类型展开是——

```
VOID CALLBACK WorkCallback(    PTP_CALLBACK_INSTANCE Instance,   // 参数一    PVOID                 Context,    // 第二个参数    PTP_WORK              Work        // 第三个参数);
```

而 `TpAllocWork` 的 `PVOID OptionalArg` 会被当作 **Context（参数二）** 传递给回调。可 `LoadLibraryA/W`**只接受一个参数**：

```
HMODULE LoadLibraryW(LPCWSTR lpFileName);
```

在 x64 调用约定下，回调被调用时是 `RCX = Instance`、`RDX = Context`、`R8 = Work`。而 `LoadLibraryW` 只读 `RCX`。于是：

> 朴素地把 `LoadLibraryA` 塞给 `TpAllocWork` 当回调，DLL 路径（wininet.dll）会落到 **RDX**，而 **RCX 拿到的是 ntdll 内部 `TppWorkPost` 动态生成的 `TP_CALLBACK_INSTANCE` 结构指针**——并不是路径字符串。结果要么加载失败，要么加载到错误内容。

实证者还试过一个折中：写一个桩回调，里面调 `LoadLibraryA(Context)`。这确实能跑通，但桩函数本身落在**私有 RX 内存**里，调用栈变成 `LoadLibraryA → RX 区内的桩 → RtlUserThreadStart`，又回到了"被执行栈回溯盯上"的老问题——绕了一圈，等于没绕。

**所以"shellcodeless"的成立条件，本质就是一件事**：让回调拿到的**首参**所指向的内存，直接就是 DLL 路径字符串。一旦这件事成立，`LoadLibraryW` 就成了"天然可用"的回调，目标进程里只多出**一个路径串 + 一个伪造结构**，没有任何自定义代码、没有 RX/RWX 区段、没有新建线程。

> **⚠️ 未核实标注**：具体到 DLLParty 采用哪一种手段来达成首参指向路径（例如如何安排伪造工作项中"回调实例 / 上下文"区域的内存布局、或是否借助其他工作项类型绕过签名差异），**因原文未能抓取，本文不作断言**。上述"参数位错位"问题及其后果，来自可核实的公开实证；而 DLLParty 的具体解法，请以原文为准。

---

## 五、完整流程（逻辑骨架）

需要强调的是，下面只是**逻辑骨架**，不包含可用于直接攻击的完整实现。

```
① 打开目标OpenProcess(PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_DUP_HANDLE | PROCESS_QUERY_INFORMATION)
② 定位目标的线程池   · 经 Worker Factory 句柄 → NtQueryInformationWorkerFactory 取 StartParameter     （该参数实质上就是指向 TP_POOL 结构的指针）   · 或走 NtQueryInformationProcess + ReadProcessMemory 读出默认池 ③ 写入负载数据VirtualAllocEx(目标, RW) + WriteProcessMemory：     · DLL 路径字符串（宽字符）     · 伪造的 _TP_WORK（或 _TP_TIMER / _TP_WAIT / _TP_IO …）       ├ Task.Callback  = LoadLibraryW 在目标进程中的地址       ├ Task.Context   = 路径串地址       └ CleanupGroupMember.Pool = 目标的默认池 ④ 宣告并触发（变体差异点）   · 常规工作项：把伪造结构挂进目标任务队列链表   · 异步工作项：投递到 I/O 完成队列，靠后续 I/O 事件触发   · 定时器工作项：挂进 timer queue，到期触发   · 或直接 NtSetIoCompletion 唤醒 worker
⑤ 落地   目标进程自己的 worker 线程（起始于 ntdll!TppWorkerThread）取出任务，   调用 LoadLibraryW(路径) → DLL 载入 → DllMain 以目标进程身份执行
```

**与传统的对比**：

**① 是否新建线程**

* 传统：是，`CreateRemoteThread` 属高危强信号
* 线程池：否，复用系统已有的 worker

**② 是否需要 shellcode**

* 传统：不需要，但必须建远程线程
* 线程池：不需要，也不需要桩代码

**③ 目标内新增内存属性**

* 传统：通常是 RWX，强信号
* 线程池：仅 RW 数据，只有路径串与伪造结构

**④ 执行触发者**

* 传统：攻击者显式调用
* 线程池：线程池的合法调度

**⑤ 检测抓手**

* 传统：`CreateRemoteThread`、RWX 区段、远程线程起始地址
* 线程池：线程池结构被跨进程改写、模块加载调用栈异常

---

## 六、范围、限制与脆弱性（本文增补）

这类技术并非"放之四海皆准"，实际约束不少：

1. **目标线程池必须已初始化**

   。若进程尚未建立可用线程池状态，工作项无处可挂。
2. **需要相当高的进程句柄权限**

   。`PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_DUP_HANDLE` 本身就该是监控重点。
3. **结构偏移随系统版本漂移**

   。`_TP_WORK` 等结构不属于公开 ABI，字段布局靠逆向获得；Windows 更新可能导致失效甚至把目标进程搞崩。这是该族技术**最本质的脆弱性**。
4. **依赖目标进程内 `LoadLibraryW` 的地址**

   。需要解析目标进程的模块导出表，并考虑 ASLR 与架构（x86/x64）差异。
5. **依赖"参数位"这一层约定**

   。签名与调用约定的任何变化都会让"直接拿 LoadLibrary 当回调"失效。
6. **DllMain 内的 loader lock 限制**

   。在 DLL 加载锁内可调用的 API 受限；若在 `DllMain` 里再去做复杂初始化（如 C2 拉起、再加载其他 DLL），容易死锁或卡住——实践中更稳妥的做法是只在 `DllMain` 做最小动作。
7. **检测态势是动态的**

   。如前所述，2023 年的"完全绕过"结论在 2025 年后已被部分厂商追上。

---

## 七、检测与防御

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0E1yFJuPqd0oGlHvhGqjMlvpdHnus6HrdvxHIpDnfmU6OueunaO3l0rUGiaYgZgiaKal1lznoB8ucLEw9FwdQXZuFK20I4IibeekM/640?wx_fmt=png&from=appmsg)

防御侧的好消息是：**线程池内部结构虽然不透明，但也正因为"正常形态"高度固定，异常反而显眼。**

* **线程起始地址基线**

  ：正常 worker 线程的起始地址恒为 `ntdll!TppWorkerThread`。一个自称 worker、却起始于**私有 / 无映像支持内存**的线程，值得二次审视。
* **结构完整性**

  ：校验 `TP_POOL` 任务队列链表与工作项字段的一致性；识别那些**不属于本进程分配器**的伪造工作项。
* **句柄监控**

  ：监视对 `TpWorkerFactory` 对象的跨进程句柄获取，以及 `NtSetIoCompletion` / `NtQueryInformationWorkerFactory` 等调用的异常组合。
* **行为遥测（最关键）**

  ：紧盯**模块加载事件**——进程加载了非常规来源的 DLL，且 `LoadLibrary` 的调用栈中，返回地址落在线程池调度路径内（而非正常的业务调用链）。这是"shellcodeless"绕不开的落脚点：**DLL 终究要被加载，加载就会留下遥测。**
* **权限收敛**

  ：减少可被跨进程写入的进程句柄暴露面；对敏感进程启用受保护进程（PPL）等机制。
* **检测理念调整**

  ：不要把 `CreateRemoteThread` 当成进程注入的同义词。应把\*\*"线程池结构被跨进程改写"\*\*本身当作一等...