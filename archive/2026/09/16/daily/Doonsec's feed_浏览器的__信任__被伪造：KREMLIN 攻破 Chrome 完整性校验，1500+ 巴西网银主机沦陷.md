---
title: 浏览器的\"信任\"被伪造：KREMLIN 攻破 Chrome 完整性校验，1500+ 巴西网银主机沦陷
url: https://mp.weixin.qq.com/s/tBCeWn20eyNRRvHgN5ipHA
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:57:01.000051
---

# 浏览器的\"信任\"被伪造：KREMLIN 攻破 Chrome 完整性校验，1500+ 巴西网银主机沦陷

# 浏览器的"信任"被伪造：KREMLIN 攻破 Chrome 完整性校验，1500+ 巴西网银主机沦陷

原创

威胁情报中心
威胁情报中心

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

威胁研判 · 恶意软件分析

浏览器的"信任"被伪造

KREMLIN 攻破 Chrome 完整性校验，1500+ 巴西网银主机沦陷

不上架应用商店、无需用户授权——攻击者伪造 Chromium 自身的完整性校验值，让浏览器“自愿”加载恶意扩展；C2 配置写入以太坊智能合约充当“死信箱”，1,515 台受感染主机已被观测，98.75% 位于巴西。

· REF9334 / KREMLIN　· 巴西网银用户　· 2026 年 9 月

01 导读：一场持续 15 个月的“隐形扩展”行动

2026 年 9 月，Elastic Security Labs 披露了针对巴西银行用户的恶意软件行动 **REF9334** 的完整分析。该行动至少自 2025 年 5 月开始活跃，横跨七个攻击波次，核心武器是一套被作者自命名为 **KREMLIN**（署名 Kr3mlin4rt1st）的工具集——名字虽有“克里姆林宫”之意，但整条行动与俄罗斯没有任何关系：钓鱼诱饵仿冒十二家巴西银行，错误提示与代码注释均为葡萄牙语，链上交易时间集中在圣保罗工作时段。

这套工具集最值得警惕的能力是：**它能在 Chrome 和 Edge 中安装一个“用户从未批准过”的恶意扩展**。浏览器启动后会像加载正常扩展一样加载它，因为攻击者伪造了 Chromium 自己的完整性校验值（HMAC 与 App-Bound 加密哈希），让浏览器认为这次安装完全合法。

更值得注意的是其基础设施设计：C2 地址与载荷托管位置被写入**以太坊智能合约**，充当“死信箱”（Dead Drop Resolver），可动态更新、难以被拔除。而在分析师注册了其网络金丝雀（Network Canary）域名后，已观测到 **1,515 台受感染主机** 前来“报到”，其中 **98.75% 位于巴西**——且感染数量仍在加速增长。

02 感染链：从一封“银行回执”到浏览器沦陷

2.1 第一阶段：JavaScript 加载器

感染起点是一个伪装成银行回单、发票或企业文档的 .js 文件，由用户手动执行。载荷是一个轻度混淆的多阶段加载器（函数名替换为 itemXX 之类的通用标识符、字符串通过索引查表获取），混淆程度并不高，研究人员借助大语言模型即可完成还原。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqicLWPQiaQ2rs2JiaZqKVsJicy75ejITdicLrChtuYbrnYibfDicslllSsLJ0A1TH2wqbOBgibRqUCuxFoXGjws0qmiclQRYNaOWvfq2j84/640?wx_fmt=png&from=appmsg)

图1 | 第一阶段 JavaScript 加载器的 VirusTotal 检测情况：伪装为 Safra 银行回执文件，检出率极低（图源：Elastic Security Labs）

第一阶段执行以下动作：

* **弹出虚假报错**：生成一个 popup\_{date}\_{random}.js 文件调用 shell.Popup 提示“文档打开失败”，随后自删除，让受害者以为只是文件损坏；
* **沙箱检测**：统计桌面文件数量，并通过 WMI 查询统计运行进程数——桌面文件少于 5 个或进程少于 50 个即判定为沙箱并退出；
* **下载 Node.js 运行时**，用于执行下一阶段的 JavaScript；
* **向 C2 回传**，通过 /api/log\_loader?hash= 接口携带战役 ID 上报（样本中使用 hxxps://connection[.]upgradeonline[.]site）。

2.2 第二阶段：持久化 + 以太坊“死信箱”

第二阶段完成四件事：

1. **建立持久化**：从内嵌 CAB 包中解压出一个计划任务，注册名为 MicrosoftNodeRuntimeUpdater，描述文本伪装成 Node.js V8 运行时更新程序，在用户登录一分钟后以 conhost.exe --headless node.exe 方式启动恶意脚本；
2. **查询以太坊智能合约** 0xCD7360A83E5cdbBbbbcEB0e78748babA6740d07b，读取三个参数：

* main-v2：主模块（恶意扩展安装器）下载地址；
* sub-module：一个 JPEG 载体，内含 .NET 进程注入套件（RunPE），本次分析中未被实际使用；
* sentinel：一个 JPEG 载体，内含 CAB 包，装的是**合法的 SentinelOne 程序** SentinelMemoryScanner.exe，用于 DLL 侧加载；

3. **从合约返回的地址下载载荷**——托管位置混合了攻击者自有域名与对 Archive.org 公共服务的滥用（JPEG 隐写载体，Base64 编码、以文件首尾标记定界；主载荷则是倒置后再 Base64 编码：base64.b64decode(payload[::-1])）；
4. **执行第三阶段**：CAB 中的 items.json 指定安装目录并充当更新机制，随后启动 SentinelMemoryScanner.exe。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqib6icjjbqDE9I8Xfy6d4t9J2lpEADBjuM96ajZ8WuFlgjGPqQruf8vY4khsmRHRG9FVzMGVbEm97LaFQ7ttLhE9ib95FdoBlicwKE/640?wx_fmt=png&from=appmsg)

图2 | 从 CAB 包中提取的计划任务 XML 模板：注册名 MicrosoftNodeRuntimeUpdater，描述文本伪装成 Node.js V8 运行时（图源：Elastic Security Labs）

把 C2 配置写进智能合约的好处显而易见：**域名被封可以随时在链上改写**，执法机构和安全厂商无法“查封”一条公链。

2.3 第三阶段：C++ 安装器

主载荷是一个 2.10 MB 的 x64 C++ 程序，处于活跃开发状态，未做混淆，因静态链接了大量开源库而体积臃肿。它只加密了部分字符串（解密算法为逐字节异或 (0x34 + i) & 0xFF），还残留调试信息——整体工程水平与其基础设施的成熟度并不相称，呈现明显的“仓促开发”特征。

几个值得关注的对抗设计：

* **间接系统调用（Indirect Syscall）**：启动时构建“API 名哈希 → 系统服务号（SSN）”映射。它不逐个解析 Nt\*/Zw\* 桩函数，而是利用 ntdll.dll 中 syscall 桩按 SSN 顺序排列的特性，对照异常目录（.pdata）中按地址排序的 RUNTIME\_FUNCTION 条目，通过数算目标调用之前的 Zw\* 导出数量推导 SSN，然后借助 ntdll 中现成的 syscall; ret 序列发起调用（找不到则回退到内置的硬编码桩）。研究人员通过 GetSyscallNumber 函数中的特征字符串将其关联到开源库 **PigSyscall**；
* **DLL 侧加载与加载器锁绕过**：滥用合法签名程序 SentinelMemoryScanner.exe 侧加载伪装成 SentinelAgentCore.dll 的恶意载荷（该手法最早由 Symantec 在 Seedworm 相关行动中披露）。当宿主进程为 SentinelMemoryScanner.exe 时，恶意代码会定位 ntdll 内部的 LdrpLoaderLock 临界区与 LdrpWorkInProgress 全局变量，释放加载器锁，使工作线程在 DllMain 返回前就能运行，避免死锁（完整实现可参考开源项目 LdrLockLiberator）；
* **反沙箱/反虚拟机**：检查宿主进程名、运行进程黑名单（涵盖 Joe Sandbox、ProcMon、Wireshark、x64dbg、IDA、dnSpy、Frida 等数十种分析工具）、用户名黑名单（CurrentUser、Sandbox、maltest、JohnDoe 等）、CPU 数量（>2）与内存（>3 GB）等硬件条件。多数检测命中后会故意调用非法地址 0x1337 触发访问违例、让程序崩溃以中断分析；
* **网络金丝雀检查**：尝试访问一个**本不该存在的未注册域名** hxxp://www[.]creamp1eonlyfans[.]net——正常互联网环境下该域名无法解析，若能取回内容，说明身处模拟联网的沙箱，恶意软件随即主动崩溃。这个设计后来被研究人员反向利用，成为整场行动的“杀伤开关”（详见第六节）；

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9tkC6SrtibzIgY5j2SD5KINXSrm439IO3ukujWAbkqgE1GjBicoAuLVvGaCdTv24luHlOWoAS02cecO7XRDHn2UmIPib4IsqWSQQ/640?wx_fmt=png&from=appmsg)

图3 | 网络金丝雀检查代码（图源：Elastic Security Labs）

* **战役追踪标记**：通过全部检查后，加载一个“客户 ID”（Customer ID，如 98d8049e-804f-11f1-b79f-ae3a8bb85d01）和一个葡萄牙语互斥体名（如 ClarinhoQueSim-XEDA2O）。“客户”概念暗示**运营者与开发者可能不是同一批人**，这套工具或存在对外分发。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9c8L5s22kgXBErM4fAHjibC4RTrpoiapWMkDuUtlQic5WeGuhorErTX3NmcFIiaEXqXHuHvHxpCjiaT95ZfNOiaMwLAsNiccSAa7Wa9c/640?wx_fmt=png&from=appmsg)

图4 | 安装器中硬编码的客户 ID 与互斥体名（ClarinhoQueSim-XEDA2O）日志输出（图源：Elastic Security Labs）

03 核心手法：如何让浏览器“自愿”加载恶意扩展

这是整份报告技术含量最高的部分。KREMLIN 采用了一种有公开研究背书、但在野恶意软件中罕见的安装路径：**不依赖 Chrome 应用商店，也不依赖命令行参数，而是直接把扩展文件拷入浏览器配置文件目录，并在 Secure Preferences 中“手工注册”**。

3.1 背景：Chromium 的完整性防线

Chromium 系浏览器通过 Secure Preferences 文件记录已安装扩展。为防止外部进程篡改，关键配置项受 HMAC 完整性校验保护：HMAC 的种子（seed）硬编码在浏览器安装目录下的 resources.pak 中；而在较新版本（Chromium ≥ 144）上，Chrome 还引入了与 App-Bound Encryption（ABE，Chrome 127 起引入的凭据保护机制）配套的新式 \*\_encrypted\_hash 校验值，需要 OSCrypt 密钥才能生成。

也就是说，想“偷渡”一个扩展，攻击者必须同时拿到三样东西：**旧版 OSCrypt 密钥、新版 App-Bound OSCrypt 密钥、以及 resources.pak 中的种子**。KREMLIN 一样不落地全做到了。

3.2 安装流程拆解

1**等待时机** —— 轮询 GetLastInputInfo，等浏览器关闭或用户至少 2 分钟无操作；若浏览器仍在运行，则直接 TerminateProcess 强杀——既避免配置文件并发写冲突，也让“闪退”看起来像一次普通的浏览器崩溃

2**窃取旧版密钥** —— 从 %LOCALAPPDATA%\Google\Chrome\User Data\Local State 读取 Base64 编码的 os\_crypt.encrypted\_key，剥离 5 字节 DPAPI 前缀后调用 CryptUnprotectData 解密

3**窃取 App-Bound 密钥（调试器法）** —— 以 --no-startup-window 在调试器下拉起一个新的浏览器进程，监听调试事件直到捕获 LOAD\_DLL\_DEBUG\_EVENT 且加载模块为 chrome.dll 或 msedge.dll；随后扫描其 .rdata 段定位特征字符串 OSCrypt.AppBoundProvider.Decrypt.ResultCode，再在 .text 段中搜索引用该字符串的 RIP 相对 LEA 指令，配合字节模式匹配定位密钥缓冲区指针，最后用 ReadProcessMemory 从浏览器进程内存中读出密钥。整个过程不注入代码、不修改目标进程内存，只扮演“外部调试器”

4**提取 HMAC 种子** —— 从 %PROGRAMFILES%\Google\Chrome\Application\<版本号>\resources.pak 中提取种子值

5**落地扩展并伪造校验** —— 将扩展 ZIP 解压进每个可读取的浏览器 Profile 目录，然后改写 Secure Preferences——开启开发者模式（extensions.ui.developer\_mode 与 account\_values.extensions.ui.developer\_mode），在 extensions.settings.<extension\_id> 下注册扩展，并在 protection.macs 中为上述每一项重新计算旧版 HMAC 与新式 OSCrypt 加密 SHA-256 哈希（\*\_encrypted\_hash），最后更新聚合校验值 super\_mac 与 super\_encrypted\_hash

至此，浏览器下次启动时会认为这个扩展是**“用户亲手安装并批准的”**，没有任何提示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOq9xvoMTrN5nZFvJKYVzPZpXIUxanFniaW6zV1KqzOcP4GUkgWnXSUk9hKnWN64q8YfF2MpnLBB0y4ICPLngUM0GicyL8jDSQicREA/640?wx_fmt=png&from=appmsg)

图5 | 激活恶意扩展所需的 Secure Preferences 修改示例：开启开发者模式、注册扩展，并重算 protection.macs 中的 HMAC 与加密哈希（图源：Elastic Security Labs）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/odcL3w4qOqic8yHxib9EJlSQlaZuwDJdydEClje0UFrp3uFCsOwkh88OvZVmVZ6CXZVoGn0EVLIKqkIfdMWib8zzqqTg4fnJTdiaK5iaqQquAPuw/640?wx_fmt=png&from=appmsg)

图6 | 恶意扩展安装与 Chromium 完整性校验伪造全流程（图源：笔者依据原文技术分析绘制）

3.3 顺手牵羊：浏览器数据打包外泄

安装完成后，安装器还会把每个 Profile 下的 Login Data、Login Data For Account、Web Data、Network/Cookies 及 Extensions/\*\* 打包成 ZIP，并附上一个 keys.json（内含 v10/v20 两个 OSCrypt 密钥，用于事后解密数据库中的加密字段）。ZIP 通过未公开文档的 SystemFunction032 API 以 RC4 加密（密钥为明文 ZIP 的 SHA-256 摘要），连同客户 ID 一起 POST 至 hxxps://volmira[.]site//api/savecreds 和 hxxps://zaviro[.]online//api/v1/fingerprint。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqib220ZDhtq3mJXQMa46eMZmPD95jxaQD3Yl5shdk9MtFnaiaUuErqf7lYaF14Wofe1fUIcSxnhMs1ZSUicP1R1IRTw2tBicf25WNA/640?wx_fmt=png&from=appmsg)

图7 | 浏览器数据窃取与加密回传流程（图源：笔者依据原文技术分析绘制）

04 恶意扩展本体：架在浏览器里的间谍平台

分析的扩展样本（SHA-256：223be3f8…c3f7ca）伪装成名为 **AVSync** 的合法软件，申请 tabs、cookies、storage、webRequest 等权限，由后台 Service Worker 与两个注入到所有页面的 content script 组成。代码未混淆、变量命名规范，配置中一个拼写错误的字段名 ENDPOINT\_DINAMIC 可作为狩猎同类样本的枢轴特征。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqibq1gm7rWYOQDSOWy5uLEKGytqnqj58leb8vOQvWD4ziaZJJSqojU77zib0Ce9EZsjoP38sFToz5AC1I40gROicDoGHcvU2IicGovA/640?wx_fmt=png&from=appmsg)

图8 | 恶意扩展以 AVSync System Inc 之名出现在浏览器扩展列表中，ID 为 ndpbidppejfanjbhfgjlohfanbfbklff（图源：Elastic Security Labs）

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOqib7pwibd9IYyd12waNEFdic7bElojhlwU3l4d5NMJU1A24WaJYX9ibrPP2Vcj29xKv3qAGE1HgNtLiaWv6sFhlMogo4zCR8L33Ejw0/640?wx_fmt=png&from=appmsg)

图9 | 扩展配置文件：注意拼写错误的 ENDPOINT\_DINAMIC 字段与内嵌的客户 ID（图源：Elastic Security Labs）

4.1 C2 寻址

扩展先通过 E...