---
title: 苹果手机间谍软件Predator中未公开的反检测反蜜罐反取证技术
url: https://mp.weixin.qq.com/s/eV3VdxAkCE_wz6Ur1LVTog
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:25:53.373247
---

# 苹果手机间谍软件Predator中未公开的反检测反蜜罐反取证技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/V9abY6oHTkror8eCs1gxVy7wGyWPc4uibHU0xzMGiaeYHHu6QiauQjyXobWEFS7T8PZzNd0qp2QxbTMeakyufUHxA/0?wx_fmt=jpeg)

# 苹果手机间谍软件Predator中未公开的反检测反蜜罐反取证技术

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

> 黑鸟一直持续关注Predator间谍软件的最新技术点，近期相关文章可阅读Intellexa联盟与Predator间谍软件的故事，建议阅读后再阅读此篇
>
> 黑鸟，公众号：黑鸟[Intellexa联盟0day漏洞攻击不止：泄露分析揭全球监视黑幕](https://mp.weixin.qq.com/s/c9RTUQje6i1viPCAYUO1xA)

在数字战场的阴影中，Predator 间谍软件就像一位经验老道的猎手，由 Intellexa 开发，专为 iOS 系统设计。

它并非单纯的入侵工具，而是配备精密的诊断系统，能将每次失败转化为宝贵情报，帮助操作员优化策略，避免暴露踪迹。

这个故事从一次典型的感染尝试展开，逐步揭示 Predator 的逻辑流程：

从初始部署，到多层检测，再到自我保护和清理，每一步都如棋局中的精妙布局，旨在躲避研究人员和安全工具的追捕。

故事伊始，Predator 通过精心利用的漏洞悄然进入目标设备，驻扎在 /private/var/tmp/ 目录中。

这是它的临时基地，但它不会贸然行动。

首先，它激活核心类 CSWatcherSpawner::CSWatcherSpawner，通过 check\_perform() 函数启动一系列检查，确保环境安全。

如果任何一步失败，它会触发结构化的错误代码系统（范围 301–311），向指挥与控制（C2）服务器报告具体问题，然后自我清理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8eCs1gxVy7wGyWPc4uibLvXS8c9kLVmW1AibcialkiaIHvyXRwlB8vzibIKe5BpKp6HKiaCN0VSlzTw/640?wx_fmt=png&from=appmsg)

代码如 301、307、308 被保留作为占位符，而 302、303、305、306 则缺失——可能已弃用、特定于变体，或与其他 Intellexa 产品共享。

第一道关卡：多实例检测（错误代码 311）。

Predator 调用 getCountNames() 函数，使用 sysctl 系统调用枚举所有进程，再通过 proc\_pidpath() 获取每个进程的可执行路径。

它仔细计数位于 /private/var/tmp/ 中的实例。

如果发现两个或更多，它会有所察觉，这可能意味着设备已被多次尝试感染，或正处于监控状态。

于是，它报告 311 代码，告知操作员“多个实例运行中”，然后中止行动。这不仅仅是逃避，更是诊断：

操作员能据此判断是否需等待或更换策略。

紧接着，Predator 检查开发者模式。

通过 is\_developer() 函数，它查询 sysctlbyname("security.mac.amfi.developer\_mode\_status")。如果返回 true（特别是在 iOS 16+ 版本），表明开发者模式启用，这往往是研究人员的测试环境。

Predator 会立即停止，避免落入陷阱，帮助操作员识别出目标可能是安全专家。

接下来是越狱检测，使用 is\_not\_phone() 函数和 access() 系统调用扫描特定路径：

/bin/bash、/private/var/tmp/cydia.log、/Applications/Cydia.app、/private/var/lib/apt/、/private/var/lib/cydia、/etc/apt 和 /private/var/stash。它还检查 /bin/ 目录的条目数是否超过 2（标准 iOS 仅 ≤ 2）。

如果检测到越狱迹象，它会悄然退场，报告相应代码，让操作员知道设备已被修改，可能不适合感染。

地理限制是另一层防护（错误代码 309），Predator 通过 NSLocale 获取国家代码，如果匹配 "US"美国 或 "IL"以色列，它会中止执行，或许是为了规避高风险地区的法律审查。

这一步确保了行动的地域针对性，避免无谓的暴露。

更巧妙的，是控制台检测（错误代码 310），在 is\_console\_attached() 函数中，它比较 /private/var/preferences/Logging/com.apple.diagnosticd.filter.plist 文件的修改时间 (mtime) 与系统启动时间。

如果 mtime > 启动时间，表明日志记录是在引导后启用的，这暗示设备可能连接了调试控制台。

Predator 会触发 310 代码，报告给 C2，帮助操作员推断目标是否在被监控。

安全工具检测（错误代码 304）是 Predator 躲避研究人员的杀手锏，通过 is\_unsafe\_running() 函数，它扫描运行进程，寻找 tcpdump、frida-server、netstat、sshd、checkra1nd、loader、McAfee、AvastMobileSecurity、NortonMobileSecurity，甚至 Bash 和 checkrain。

如果检测到这些，它会中止，并报告 304 代码。这不仅仅针对专业工具如 Frida（用于逆向工程），还包括日常安全应用，让操作员知道失败源于目标的防护措施，而非兼容性问题。

同时，它检查自定义 HTTP 代理（/private/var/preferences/SystemConfiguration/preferences.plist）和根证书（/private/var/protected/trustd/private/TrustStore.sqlite3，使用 SQL 查询如 "select \* from tsettings WHERE length(sha256) > ?" 和 "select tset FROM tsettings WHERE INSTR(tset, ?)"），以检测潜在的 MITM 攻击或分析环境。

如果所有检测通过，Predator 进入潜伏阶段，但它仍保持警惕。

通过 monitoringCrashReporter() 函数，使用 kqueue 监视 /private/var/mobile/Library/Logs/CrashReporter/ 目录，一旦新崩溃日志生成，立刻删除。

同时，在 crash\_reporter\_block\_handler 中，如果日志文件名含 "SystemMemory"，它会定位并用 SIGKILL (信号 9) 杀死 mmaintenanced 守护进程，抑制内存转储，防止内存取证。

为进一步规避，它隐藏录音指示器。通过 TestHooker() 或 UMHooker 函数，利用 Mach 异常处理注入 SpringBoard 进程，钩住 SBRecordingIndicatorManager 方法。

当麦克风或摄像头激活时，抑制橙色/绿色指示灯，让受害者毫无察觉。

内核级技术是其核心，如 NSTaskROP::WithoutDeveloperMode 类，使用返回导向编程 (ROP) 链，即使无开发者模式也能实现持久注入和Hook。

它还预留了 is\_corellium() 函数（地址 0x100005bb8），虽在本样本中未调用，但暗示了对 Corellium 虚拟化平台的潜在检测。

如果行动失败，Predator 的逻辑闭环启动：注册Darwin通知观察者（Darwin Notification Observer），监听 com.apple.springboard.deviceWillShutDown 事件，在关机时移除磁盘痕迹。

然后，使用 \_remove() 删除暂存目录 /private/var/tmp/ 中的内容。

所有这些，都在 C2 回调后执行，确保失败也成为学习机会。

这个故事并非虚构，而是 Predator 真实的行为逻辑：

从诊断失败（如 304 代码揭示的安全工具），到压制日志（如崩溃报告），再到适应性规避（如网络监控检测）。

它让研究人员面临更大挑战：失败感染不再是死胡同，而是运营商的调试工具。

最终，在这个猫鼠游戏中，Predator 提醒我们：间谍软件的进化，正从简单入侵转向智能诊断与持久隐藏，剩下的，就是要想办法如何应对它们。

![](https://mmbiz.qpic.cn/mmbiz_png/V9abY6oHTkqicLTpZgaSicHytbgFjmcM3EX3ruNNnWUQ6I3OibZCibVeRLNCIVAzSh8IQ2RicabS3XSqibREpdttO08Q/640?wx_fmt=png)

详细报告&翻译：

https://www.jamf.com/blog/predator-spyware-anti-analysis-techniques-ios-error-codes-detection/

2024年12月，谷歌威胁情报小组（GTIG）发布了关于Intellexa Predator间谍软件的详尽研究报告，记录了其零日漏洞利用链和PREYHUNTER阶段性组件。他们的研究发现，“监视”模块能够检测开发者模式、越狱工具、安全应用程序和网络拦截配置。

然而，Jamf Threat Labs 在对 Predator 样本进行独立逆向工程时，发现了一些未公开的机制，揭示了这款间谍软件反分析能力的真正复杂程度。本文将介绍以下原创发现：

一套完整的错误代码分类体系（301-311），使操作人员能够准确诊断植入物失效的原因。

每种检测方法的实现细节，而不仅仅是高层次的描述

一个未公开的用于反取证的崩溃报告监控系统

SpringBoard 钩子用于向受害者隐藏录制指示器

内核利用类名揭示了其内部架构

这些发现表明，Predator 操作员可以详细了解部署失败的情况——这种能力对试图分析这些样本的研究人员具有重大意义。

CSWatcherSpawner架构

该植入程序包含一个名为 `transforming\_analysis` 的 C++ 类CSWatcherSpawner::CSWatcherSpawner，用于协调所有反分析检查。该类实现了一套全面的检测方法，并配备了完善的报告机制。

该架构的显著特点不仅在于检查范围广，还在于其报告机制，该机制可在部署失败时为操作员提供精确的诊断信息。

check\_perform() 入口点显示了 getCountNames() 检查和错误代码 311，用于检测多个实例

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8eCs1gxVy7wGyWPc4uib6M5cWibNpViaZBHZ0GMaC98U3ZHrcBnLibUETznmrUguq3VKOB6NAAycg/640?wx_fmt=png&from=appmsg)

图 1：check\_perform() 入口点，显示 getCountNames() 检查和多实例检测的错误代码 311 分发

错误代码分类

最重要的未记录发现是Predator的错误代码系统。当任何反分析检查触发时，恶意软件并不会直接终止，而是在清理并退出之前，向其命令与控制基础设施报告一个特定的错误代码。

该check\_perform()函数揭示了完整的分类体系：

错误代码列表（301 至 311），缺少 302、303、305 和 306，并显示了触发条件和检测方法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8eCs1gxVy7wGyWPc4uibLvXS8c9kLVmW1AibcialkiaIHvyXRwlB8vzibIKe5BpKp6HKiaCN0VSlzTw/640?wx_fmt=png&from=appmsg)

表 1：错误代码及其条件

缺失的错误代码：302、303、305、306

仔细检查二进制文件的字符串部分，可以发现错误代码分类中存在一个有趣的漏洞。该\_\_cstring部分存储的错误代码按顺序出现，但存在明显的间隔：

分析截图显示了 \_\_cstring 部分中的错误代码字符串。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8eCs1gxVy7wGyWPc4uibFAGERdJm7qHXEmsFbn4pWY3QHZ1vEzyz71lAEpkqk86EdI9284liaMw/640?wx_fmt=png&from=appmsg)

图 2：\_\_cstring 部分中的错误代码字符串——注意地址是连续的，但代码却不是连续的（301、304、307、308），这表明缺少 302、303、305 和 306。

值得注意的是，错误代码 302、303、305 和 306 在此样本中完全缺失。编号方案中的这些缺失暗示了以下几种可能性：

保留代码：用于尚未实现的未来功能或检查的占位符代码

特定版本：这些代码可能用于其他 Predator 变体或针对不同平台的版本

已弃用的检查：已移除但其错误代码仍保留在分类法中的检测方法

共享分类法： Intellexa 多个产品共享的错误代码系统，不同产品实现不同的子集。

非连续编号（从 301 跳到 304，再从 304 跳到 307）表明此错误分类随着时间的推移而演变，或者旨在适应可能根据目标配置有条件编译的检查。

为什么这很重要

这套错误代码系统将部署失败的情况从“黑盒”转化为诊断事件。当操作员针对目标部署 Predator 并收到错误代码 304 时，他们就知道目标正在运行安全工具——并非漏洞利用失败，也并非设备不兼容，而是明确表明正在进行主动分析。

这对目标个人有直接影响：如果 Frida 等安全分析工具正在运行，Predator 将中止部署并向操作员报告错误代码 304，然后操作员可以排查部署失败的原因。

检测实施细节

虽然谷歌的研究提到Predator可以检测“自定义HTTP代理”和“自定义根CA”，但具体的实现细节并未公开。以下是二进制文件揭示的内容：

多实例检测（错误 311）

首先，调用check\_perform()会getCountNames()检查是否存在多个 Predator 实例正在运行。这可以防止研究人员同时运行多个分析实例：

getCountNames() 伪代码的屏幕截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8eCs1gxVy7wGyWPc4uibxcvG6YTfh237LDDA8C2thSglF80m5UBkbERibYQFqwVoj0w5J7ScZNg/640?wx_fmt=png&from=appmsg)

图 3：getCountNames() 伪代码 — 通过 sysctl 枚举所有进程，使用 proc\_pidpath 获取可执行文件路径，统计从 /private/var/tmp/ 目录运行的进程数

该函数遍历所有正在运行的进程sysctl，通过检索每个进程的可执行文件路径proc\_pidpath()，并统计有多少进程正在从/private/var/tmp/（Predator 的暂存目录）运行。如果计数为 2 或更高，则报告错误代码 311。

开发者模式检测：针对研究人员

基于谷歌发现 Predator 可以检测开发者模式，我们反向工程分析了这种检查的工作原理。

该is\_developer()函数专门针对使用 API 的 iOS 开发者模式sysctlbyname：

分析屏幕截图显示对 sysctlbyname 的调用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8eCs1gxVy7wGyWPc4uibU0M7c0bhDEIjarzPicUShq44Q5NccjiaE4EibPs3rVKQiaJ0Qff4UCrnBQ/640?wx_fmt=png&from=appmsg)

图 4：开发者模式检测实现，显示了 sysctlbyname("security.mac.amfi.developer\_mode\_status") 调用

这一点意义重大，因为 iOS 16 中专门为安全研究人员和开发者引入了开发者模式。通过检测到这一点，Predator 实际上表明：“如果你启用了开发者功能，你可能不是普通的攻击目标。”

越狱检测：is\_not\_phone()

该is\_not\_phone()函数检查是否存在与越狱相关的文件和目录：

流程图显示了越狱指标的检查

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8eCs1gxVy7wGyWPc4uibFmgk3W2WtanKictUia0Eb7icrPBfqMibspww7tOFwQNiaI1xs6xhSAtQSFg/640?wx_fmt=png&from=appmsg)

图 5：is\_not\_phone() 图形视图 — 越狱指示器的级联文件存在性检查

该函数使用系统调用检查以下路径access()：

/bin/bash— Shell 二进制文件（原生 iOS 系统中不存在）

/private/var/tmp/cydia.log— Cydia 软件包管理器日志

/Applications/Cydia.app— Cydia应用程序

/private/var/lib/apt/— APT 软件包管理器目录

/private/var/lib/cydia— Cydia 数据目录

/etc/apt— APT 配置

/private/var/stash— 越狱藏匿处目录

此外，它还会检查是否/bin/包含两个以上的条目（原生 iOS 在 /bin 中只有最少的二进制文件）。

地理限制：避开美国和以色列的管辖权

谷歌的研究发现，Predator 会检查设备所在地区是否为美国或以色列。我们的分析记录了这一地理位置检查的具体实现方式（错误代码 309），值得进一步关注。Predator 无法在地区设置为美国或以色列的设备上运行。

分析截图显示了地理限制检查

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkror8e...