---
title: 把四款主流EDR的检测逻辑拆出来本地运行
url: https://mp.weixin.qq.com/s/GVg8XhF0S0taTMgkW9KV_g
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:04:43.488527
---

# 把四款主流EDR的检测逻辑拆出来本地运行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDrRSPIUfSiaTY02C5vbBljJ9NEqrB78FyQdjkzSkibqP9sAqKZx0FX4bhuFtEqkWKiaOiapY298UUYVak5oibvRwnicy70wibYsz9xwZg/0?wx_fmt=jpeg)

# 把四款主流EDR的检测逻辑拆出来本地运行

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

做端点安全测试的从业者大多遇到过一个两难的局面。想要验证自己的 payload 会不会被 EDR (端点检测与响应) 产品拦截，要么在测试环境装上真实的 EDR 代理，可一旦 payload 被标记，很可能还没等用到实战环境就已经失效。要么靠逆向分析去推导 EDR 的检测逻辑，再人工预判拦截点，可推导的结果和实际运行效果总会有偏差。

最近一位安全研究者公布了耗时六个月开发的项目 heavener，把第二种思路推到了极致。这是一套面向 Windows 的模块化 EDR 仿真引擎，能加载从商业端点安全产品中逆向提取的真实检测逻辑，针对实时或回放的 Windows 系统遥测运行判定，最终输出和生产环境 EDR 完全一致的检测结果。(blog.otterpwn[.]com/projects/heavener)

目前项目已经实现了四款主流厂商的模块，分别是 SentinelOne、Cortex XDR、CrowdStrike 与 Sophos。每个模块都加载厂商原生的检测资源运行，用户还能在引擎运行时通过 IPC 客户端热切换厂商模块，不需要重启整个引擎。

## 六层架构，完整复刻 EDR 检测流水线

##

heavener 的系统由六大核心层级串联起清晰的数据流。遥测首先从内核驱动与 ETW (Windows 事件追踪) 提供者采集上来，归一化为统一的事件格式，经过信息富集与行为关联后，送入当前激活的厂商检测模块，最终产生的告警会输出到类 SOC 风格的 Web 控制台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqYibZHas0Mv75jRyZeV99XXcVWCu9u4tTNoPH99FOdCQPmSPTNFvaDkqZrxia2mkCUL9VdJ9sk6f2CurjJJ5sBgQId4ibZXibV68o/640?wx_fmt=png&from=appmsg)

整个引擎定义了 25 种事件类型，覆盖进程生命周期、文件操作、注册表操作、网络与 DNS 查询、驱动加载、LDAP 查询、WMI 操作、计划任务、脚本执行、跨进程句柄访问等几乎所有端点安全检测会用到的行为维度。所有事件都以 BehavioralEvent 为载体，头部携带统一的类型与时间信息，主体则用可承载 19 种数据结构的变体类型存放不同事件的具体内容。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDp6iaYovGGwg65XNR5alcqaIEtckemvToze2gbVwW9cVibFbPXjc38KbR29ltopttKRoJfTlE5Yt3u49QKP6piaEPicok810dE724U/640?wx_fmt=png&from=appmsg)

事件处理管道运行在单条工作线程上，这是刻意设计的结果。检测逻辑对事件顺序高度敏感，进程创建之后写入文件再加载镜像，和这三个事件打乱顺序到来，代表的是完全不同的行为。单线程处理能保证厂商模块看到的事件顺序，和真实 EDR 代理采集到的顺序完全一致。事件通过无锁的提交接口送入队列，再成批取出处理，避免逐个事件加锁带来的性能损耗。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpiakMGwE3tg6ic6bgTCuNVcJNnmcRicBOfEUICMwX5yKwK0UicR4RCPKvaib8sroWgFRcZibGbdJPMFjHJMRFJQygrjjkA05lIjNdMg/640?wx_fmt=png&from=appmsg)

每个事件的处理都严格遵循三阶段流水线。首先更新进程模型，让所有下游组件都能拿到最新的进程状态。接着运行修饰引擎，为事件附加上聚合行为特征。最后才把事件送入当前激活的厂商模块。系统里的遥测关联器还会从原始遥测中合成更高层级的事件，这些合成事件同样会走完整的处理流水线。

## 内核驱动 + ETW，全维度采集系统遥测

##

为了拿到足够底层的系统行为数据，作者专门开发了名为 heavendrv 的 Windows 内核微筛选器驱动，这也是整个项目最早完成的组件。

驱动通过四类内核机制注册回调，全方位捕获系统行为。第一类是进程与线程生命周期回调，能捕获进程创建退出和线程创建事件，同时带上内核层面抓取的调用栈。第二类是Windows 微筛选器 (minifilter)，在文件系统过滤链中的加载优先级对应数值 370000，负责捕获文件创建、写入、删除、重命名、命名管道创建、文件基础信息修改等操作，甚至能捕获重解析点设置来识别符号链接滥用行为。第三类是注册表回调，捕获注册表键创建、值设置、键与值删除等操作，最多能读取 4KB 的原始注册表值数据。第四类是对象回调，捕获跨进程句柄访问行为，记录访问权限掩码与调用栈，比如其他进程打开 lsass.exe 并申请读取虚拟内存权限的行为会被完整记录。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoho5V88NagTVrutvgJsIndt7T7PA4rKNV3BIZMLmsno7NhJQicTtykLdcOW3iamEOSlnbvg5z1NvwEsUVTdFIt8rh9OZBt6QQQM/640?wx_fmt=png&from=appmsg)

所有采集到的事件都会进入无锁队列，由用户态的驱动消费者通过 FilterSendMessage 拉取。通信协议带版本握手，用紧凑的 C 结构体传输，不同类型的事件复用字段承载不同数据，变长的字符串与调用栈数据则以长度前缀的二进制块紧跟在头部之后，单条记录最大限制为 64KB。当用户态消费速度跟不上内核采集速度时，驱动会统计丢弃的事件数而不会阻塞内核线程，避免影响系统稳定性。

驱动还有一个很实用的设计，它会记录每个新进程的真实创建者，而不仅仅是父进程 PID。现在很多攻击手段会使用进程父 PID 欺骗技术，修改系统上报的父进程 ID，但无法改变真正发起创建操作的进程。heavendrv 会同时上报这两个值，让引擎能够直接识别出这种伪装行为。

内核驱动承担了主要的采集工作，但仍有部分遥测只能通过 ETW 获取。引擎订阅了七类 ETW 提供者，其中 AMSI 提供者可以拿到完整的脚本内容，所有 PowerShell、VBScript、JScript 的执行内容都会被捕获，用来支撑基于命令行特征的检测规则。

WMI-Activity 提供者捕获 WMI 方法调用与事件订阅，支撑针对 WMI 横向移动、BitLocker 密钥提取等行为的检测。LDAP 提供者捕获查询过滤字符串，能发现针对 Active Directory 敏感属性的可疑查询。

DNS 提供者捕获域名解析事件。另外还有内核级的进程、文件、注册表、网络提供者，在内核驱动未加载时作为兜底采集方案。当内核驱动正常工作时，ETW 会切换为仅 DNS 模式，只启用补充性的提供者，避免重复采集精度更低的同类事件。

还有一类特殊的遥测来自 ETW 威胁情报提供者，微软将这个提供者的消费权限限制为仅受保护的轻量级进程也就是 PPL 才能使用，普通进程无法直接订阅。为此 heavener 单独实现了一个名为 heaventi-svc 的 PPL-AM 采集服务，通过命名管道转发原始事件。这个服务依靠 ELAM (早期启动反恶意软件) 驱动建立信任锚点，从而获得 PPL 运行权限。它能捕获跨进程内存操作，比如远程分配内存、远程修改内存保护这类行为，是发现远程进程注入的关键数据源。

要知道，原始的离散事件没有太大检测价值，只有结合进程上下文才能判断行为是否可疑。heavener 中的 ProcessModel 组件会在内存中维护一棵实时更新的进程树，每个进程节点都保存了检测规则可能用到的全部信息，包括进程唯一 ID、PID、父 PID、进程名、命令行、镜像路径、创建时间、完整性级别、会话 ID、用户 SID、文件版本信息、证书发布者、登录会话 ID，以及一系列行为标记，比如进程是否属于远程组、是否存在注入线程、是否被跨进程打开过、是否被申请过虚拟内存读写权限等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqiajC3WVyvLC7OKDOMvmk8CTiaTFgg90Mj3jzrY9I6jOaic9fr2Z4ZdfLy1v2KjjPRU3NqFrTxjYtWeI9ibfU2qFibn0QGdCPEPzus/640?wx_fmt=png&from=appmsg)

进程树同时维护两套索引，按 PID 可以快速查询当前运行的进程，按唯一 ID 可以查询历史进程信息。整棵树用读写锁保护，支持多读者单写者的并发访问。每个进程节点还带有一个扩展值字典，厂商规则可以在不同事件之间读写这个字典，用来累积跨事件的行为状态。

在进程树之上，ModifierEngine 负责计算跨事件的聚合行为特征。它会监控所有文件创建事件，为每个进程维护最近 32 个创建文件的滑动窗口，用来解锁和文件操作相关的检测逻辑，比如勒索软件会在短时间内在不同目录下生成大量同名勒索信文件，这类特征就依赖滑动窗口统计才能识别。

TelemetryCorrelator 遥测关联器负责从原始底层事件中合成更高层级的事件。比如在系统任务目录下创建文件，就会被合成为计划任务创建事件。在 SAM 注册表的用户路径下创建符合 RID 模式的键，就会被合成为用户账户创建事件。这些合成事件的抽象层级和真实 EDR 代理输出的事件一致，让厂商原生规则可以直接运行，不需要额外适配。

另外还有 LogonSessionMap 组件，通过 Windows API 将登录会话 LUID 解析为登录类型，能判断进程运行在交互式会话还是 RDP 会话中，为横向移动检测提供关键上下文。

所有厂商检测模块都实现了统一的 C++ 接口，包含初始化、关闭、文件扫描、事件接收、告警拉取等标准方法。引擎只负责调用接口，完全不关心模块内部的实现细节。每个模块接收统一的配置结构，包含厂商数据目录、规则文件、模型文件的路径，以及模块特有的配置项。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqxEKVC42tzhgrrkianNHoAexnibccLXfXfQoibepyzle2SaawmRbD3fI5nop6DbN3IuUO0LgR2Iwd6t50JxldqpyVS4ltBAkdC9E/640?wx_fmt=png&from=appmsg)

模块支持运行时热切换，用户通过 IPC 客户端发出切换命令后，引擎会销毁当前模块并初始化新模块，切换过程中事件会先暂存在队列中，新模块就绪后再批量送入，全程不需要停止遥测采集。

不同厂商的模块覆盖的检测能力各有不同，完全取决于从真实代理中逆向提取到的资源。

### SentinelOne

SentinelOne 模块包含两层检测能力。静态扫描层运行厂商原生的 ML 分类流水线，包含八个 XGBoost 模型，搭配 YARA 规则对文件进行检测，返回从良性到可疑再到恶意的完整判定等级。

行为引擎层嵌入了 LuaJIT 运行时，加载从真实代理中提取的 203 个 Lua 行为脚本。这些脚本通过两套并行的分发机制运行。第一套是事件类系统，每个脚本会针对 S1 内部的事件类层级注册处理函数。事件到来时，引擎会把内部的 BehavioralEvent 转换为 S1 的 Lua 事件格式，分发给所有注册过的处理器。比如一次镜像加载事件，会分发给三个不同的类处理器。第二套是 registerOSEventFilter 管道，厂商的 Lua 脚本库中定义了 137 个 OS 过滤回调，每个都是独立的检测例程，只关注特定类型的事件。引擎维护了静态路由表，将每个检测逻辑映射到对应的事件类型，还附带可选的守卫函数。守卫函数在引擎侧执行前置判断，比如检查特定修饰标记、匹配注册表路径、验证文件名模式等，只有满足前置条件的事件才会进入 Lua 虚拟机执行，避免不必要的性能开销。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDoeciaYDlic2u0K3VmxA7icPsfr3Jt6CAeQVTicqch3ts5aibawr6o2QhL00ibn1zIEdSAmLUW5szib2aegOEdhOTFgPdE1WSLOFB0fIA/640?wx_fmt=png&from=appmsg)

Lua 脚本可以通过注册的原生函数回调到 C++ 层，查询进程模型、获取文件富集信息、读取代理配置、读写进程扩展字典。每个事件在分发前都会被转换为完全匹配 S1 内部事件结构的 Lua 表，让脚本运行的环境和真实代理中完全一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqshozOV1M1tDg7VMt84mX3UqUJvge8SqWQokLXSzUuTibsh9R0pcKm1lJ9bK0ibL3acBbeiacIlnpzb75j0aqz0a7go8FuOXN1jY/640?wx_fmt=png&from=appmsg)

### Cortex XDR

Cortex XDR 是架构最复杂的模块，包含三层独立的检测体系。第一层是 YARA 静态扫描，包含 36 套按文件类型分类的规则集，覆盖 PE 文件、脚本、宏、文档等多种文件类型。静态扫描时引擎会先识别文件类型，再运行对应的规则集。第二层是 ML 检测，运行 Cortex 的本地分析 XGBoost 模型。YARA 和 ML 的结果可以通过可配置的融合策略合并，支持取最高严重等级、YARA 优先、ML 优先、加权组合四种模式。第三层也是核心层，是 CLIPS 行为引擎。CLIPS 是一款前向链规则引擎，最早由 NASA 约翰逊航天中心在上世纪 80 年代开发。heavener 中运行的是完整的 CLIPS 专家系统，加载了从最新版 Cortex XDR 代理中提取的约 7967 条生产规则。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrYnONd384y1rKzr5ufCRs9EVCHl3LnjOVtzImMZkl4I0Q1Mricw4VGCBqS9wia2n504NB6Qkicu6umB66Liahhe1JAV31YibNpVGhA/640?wx_fmt=png&from=appmsg)

引擎会把每个 BehavioralEvent 转换为对应的 CLIPS 事实字符串，断言到工作内存中。不同事件类型有对应的构建逻辑，每个事实都会带上从进程模型和文件富集中获取的全部相关字段。单是进程启动这一类事实就包含 27 个字段，覆盖镜像路径、命令行、父进程信息、SID、完整性级别、代码签名、哈希、PE 版本信息、熵值等，每个字段都至少有一条规则会引用。

其中 ETW-TI 路径的处理最为特殊。当远程内存操作事件到来时，引擎会先通过栈富集器处理调用栈，然后对目标分配内存、调用站点内存、页基址、分配基址四块独立的内存区域执行 YARA 扫描，再通过地址解析器将基地址解析为对应的镜像路径。所有这些信息会和操作本身的事实一起打包送入 CLIPS 工作内存，让规则既能知道发生了什么操作，也能知道操作发生时内存里的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDqHBbpRHMQicz186UwhjBQ2X7ibcGFnwvEt2ibRick1garGXSP55QWSGTiaZXEU3FzYicRkwe1oUjWy7DIYs41yMNJvD6devqGlO8smM/640?wx_fmt=png&from=appmsg)

栈富集器本身能输出非常丰富的分析结果。它会对每个栈帧进行分类，如果内存属性是镜像映射就属于合法模块承载，如果没有镜像后备就标记为无后备帧，通常对应 shellcode 或者反射加载器。系统调用溯源分类器会遍历解析后的调用栈，判断系统调用起源于 ntdll 的正常路径，还是没有经过 KERNELBASE 的间接系统调用，或是完全来自 ntdll 之外的直接系统调用。调用栈伪造检测则会检查每个返回地址之前的字节，验证其是否符合合法 CALL 指令的编码格式，如果不符合就标记为伪造帧。

另外还有专门的字节补丁检测路径。当引擎检测到进程将自身敏感 DLL 的.text 段修改为可写可执行状态时，会启动字节补丁扫描器，读取内存中的.text 段内容和磁盘上的原始文件逐字节对比，找出所有被修改的区域，记录偏移和修改前后的字节序列，能够在字节级别检测到 EDR unhooking 行为。

为了让这套 CLIPS 规则正常运行，项目还从零重写了 66 个规则会调用的外部函数，其中包括一套完整的 ECMAScript 兼容正则引擎，因为规则中使用的正则语法是 C++ 标准正则库不支持的。CLIPS 引擎还支持可选的进程外隔离模式，引擎会启动子进程运行 CLIPS 逻辑，通过命名管道通信，子进程崩溃时会自动重启，反复崩溃的事件会被跳过以保证整体流程能继续推进。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoDdNntibd8sX6HuQH40BUibapCibswvWKsf5N6u9xCibiaINhl937E4sSTfPCuHHukCAXKqcemeS31wMlFbuIGL3jWxF7FGmzciaZuU/640?wx_fmt=png&from=appmsg)

### CrowdStrike

目前 CrowdStrike 模块仅支持静态 ML 检测。它的行为检测逻辑封装在 channel 文件中，作者正在逆向分析这类文件的解析与导入逻辑，后续会逐步扩展行为检测能力。当前的静态扫描器运行 CrowdStrike 的 XGBoost ML 模型，返回恶意概率，判定阈值完全取自真实组件的逻辑。

### Sophos

Sophos 模块包含两套 ML 模型，分别针对 PE 文件和 PDF、Office 等文档类型，在此之上还有传统的特征码扫描引擎。根据逆向结果，三类检测结果会取最严重的一项作为最终判定...