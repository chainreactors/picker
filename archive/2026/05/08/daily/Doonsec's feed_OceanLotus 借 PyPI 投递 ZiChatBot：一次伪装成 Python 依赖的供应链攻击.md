---
title: OceanLotus 借 PyPI 投递 ZiChatBot：一次伪装成 Python 依赖的供应链攻击
url: https://mp.weixin.qq.com/s/0w7sXp6T7SUVkoT0wyqFMQ
source: Doonsec's feed
date: 2026-05-08
fetch_date: 2026-05-09T05:05:46.158023
---

# OceanLotus 借 PyPI 投递 ZiChatBot：一次伪装成 Python 依赖的供应链攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/UhfibIyPpmuPcc6GwibAAYQeC7UnpNBpuj24ph3uyDlnqib8beEnKg5OF8zFsiaOOicqYmpRVaup2oOcqtib95QqEbLnD5TDwRxdIvhfzh97jn6yQ/0?wx_fmt=jpeg)

# OceanLotus 借 PyPI 投递 ZiChatBot：一次伪装成 Python 依赖的供应链攻击

原创

Ti
Ti

TIPFactory情报工厂

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Kaspersky 在 2026 年 5 月发布的一篇报告披露，研究人员在日常威胁狩猎中发现：从 2025 年 7 月开始，PyPI 上持续出现一组恶意 wheel 包。这些包表面上都在提供正常功能，实际上真正的目的却是把恶意载荷偷偷带进开发者环境，最终部署一支此前未公开的恶意家族——**ZiChatBot**。

更值得警惕的是，这不是传统意义上的“装了恶意包就立刻连自建 C2”的老套路。报告显示，ZiChatBot 没有依赖专用命令控制服务器，而是把 **Zulip 公共团队聊天服务的 REST API** 当成了控制通道。这意味着：攻击者正越来越熟练地把公开平台、开发生态和供应链入口混合起来使用，以提高隐蔽性并降低基础设施暴露风险。

从研究结论看，Kaspersky 认为这批样本与 **OceanLotus** 存在较强关联。虽然归因仍然保持了审慎措辞，但从投递方式、解包逻辑、落地载荷以及相似性分析结果来看，这次事件已经足以被视为一场**精心设计的 PyPI 供应链攻击**。

## 先说结论：这次攻击最值得记住的四件事

如果你只想快速把握这篇报告的重点，可以先记住下面四点：

1. 1. **入口在 PyPI**：攻击者上传了多个伪装成正常 Python 库的 wheel 包，目标是让开发者或自动化环境把它们装进项目里。
2. 2. **横跨 Windows 与 Linux**：样本既能下发 `.DLL`，也能下发 `.SO`，说明其面向的不只是单一平台，而是典型开发/构建环境本身。
3. 3. **ZiChatBot 使用 Zulip 作为“公共 C2”**：它不依赖传统恶意基础设施，而是借公开 SaaS 服务完成控制与回传。
4. 4. **属于供应链思路的延展**：攻击者不仅自己上传恶意包，还会再造一个“无害依赖包”去引用它，让恶意部分藏得更深。

这类攻击真正危险的地方，在于它并不一定要盯着终端用户，而是瞄准**开发者、CI/CD、构建机、研究环境和内部脚本生态**。一旦某个包进入组织内部的软件链路，后续影响会被持续放大。

## 攻击是怎么铺开的：三个恶意项目、一个隐藏依赖链

报告指出，攻击者在 PyPI 上创建并上传了三个伪装库项目：

* • `uuid32-utils`：表面功能是生成 32 字符随机 UUID
* • `colorinal`：表面功能是跨平台终端彩色文本
* • `termncolor`：表面功能是终端 ANSI 彩色格式输出

其中最关键的一点在于：这些项目并不全都直接暴露恶意逻辑。研究人员发现，`termncolor` 的代码表面看并没有明显恶意内容，但它会把 **恶意的 `colorinal` 包作为依赖导入**。这就让攻击链多了一层“遮挡”：当分析人员或受害者只快速浏览表层包代码时，很容易以为它只是一个正常封装库。

Kaspersky 给出的元数据显示，这批包在 2025 年 7 月相继上传，作者名与邮箱均为伪装身份。一个值得注意的信号是：这些 wheel 包同时提供 **Windows x86 / x64** 与 **Linux x86\_64** 版本，这说明攻击者在一开始就把投递目标设定为更广泛的开发生态，而不是只打某一类桌面终端。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UhfibIyPpmuOw4yje5udzUzaA68bfChuvwJURgZVic6OfLMfx7xoNKBLqxGOYJ93vOFENfbpbo4g9t6rliaJKmSyZ4iaLI1JjOk4f2cJEadSMGc/640?from=appmsg)

*图 1：`colorinal` 项目的分发信息，显示其针对不同操作系统与架构提供了多个 wheel 版本。*

## 初始感染：不是“安装即爆炸”，而是“导入时触发”

从攻击设计看，`uuid32-utils` 与 `colorinal` 的感染链基本一致，Kaspersky 因此以 `colorinal` 作为代表样本做详细拆解。

这条链路最狡猾的一点是：**恶意动作并不只发生在 pip 安装阶段，而是在后续导入库时才真正触发。**

具体来说，在 Windows 环境里，当用户安装 `colorinal-0.1.7-py3-none-win_amd64.whl` 后，名为 `terminate.dll` 的 dropper 会先被解出并落到本地磁盘。随后，只要受害者的项目代码里真正 `import colorinal`，Python 就会先执行该库目录下的 `__init__.py`，再进一步加载恶意脚本 `unicode.py`。

![](https://mmbiz.qpic.cn/mmbiz_png/UhfibIyPpmuPbkgWCLE7cZzkjRnJOw4SicDcQwiaykc7TFcARoZ4TIXro85NRelHMCqvnkD9p2hD070cqGQPWuKG6ft9x15CbdvdG12jng9t40/640?from=appmsg)

*图 2：`termncolor` 并不直接暴露恶意逻辑，而是通过依赖方式把恶意 `colorinal` 带进来。*

![](https://mmbiz.qpic.cn/mmbiz_png/UhfibIyPpmuN0xoE1miacT0iaw6PEZibibbsHDIh0KPLMTC9uchlP3OEAmftVPVhz7DPicDg0EgUWfia9NmecCZiaHjvib21kn0zPicbTlhjkV6C1h1OI/640?from=appmsg)

*图 3：安装后真正触发恶意流程的关键，是 `__init__.py` 对恶意 `unicode.py` 的导入。*

这种设计很像把恶意逻辑埋在“正常开发动作”后面：不是用户下载就立刻暴露，而是要等到依赖真正进入业务代码路径时才激活。对于自动化测试、构建流水线、PoC 环境或者临时脚本用户而言，这种延后触发尤其危险，因为它更容易绕过粗粒度检测与人工检查。

## Windows 侧的核心动作：Python 脚本负责引导，DLL 负责投递

在 Windows 版本中，研究人员看到 `unicode.py` 里有一个名为 `is_color_supported()` 的函数，代码注释声称它是在检查终端是否支持颜色输出。但这实际上只是伪装。

真正发生的事情是：这段 Python 代码会把 `terminate.dll` 装入当前 Python 进程，并调用 DLL 导出的 `envir` 函数，同时传入 UTF-8 编码的字符串参数 `xterminalunicode`。从这里开始，Python 脚本扮演的是“引导器”角色，而 DLL 则承担**dropper** 的真正职责——负责释放最终载荷 ZiChatBot、建立持久化并清除痕迹。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UhfibIyPpmuNsvyNpTib58Z650BprZTGERSR4FSdPrvtCzblFZRZqU77EHRDdugpOv0MmnpHmmWakSPYqcRVVz6QLrBpUy1fNvObOgRlr6Fsw/640?from=appmsg)

*图 4：表面上是功能代码，实际动作却是把 dropper 装入宿主 Python 进程并执行。*

报告还特别指出，恶意流程结束后，攻击者会主动删除库中的恶意脚本文件以及 dropper 本身，尽量把安装目录“清理干净”。这说明其设计目标不仅是投递成功，还包括**事后降低静态取证可见度**。

## Dropper 做了三件事：落地 ZiChatBot、建立持久化、删除自己

Kaspersky 对 `terminate.dll` 的分析显示，这个 dropper 的核心逻辑集中在导出函数 `envir` 中，主要完成三项任务：

1. 1. 部署 ZiChatBot 载荷；
2. 2. 建立自动启动机制；
3. 3. 执行 shellcode，删除自身以及安装目录里的恶意脚本。

在具体实现上，它会先使用 **AES-CBC** 解密敏感字符串，密钥正是导出函数接收到的参数 `xterminalunicode`。随后它再解密与 ZiChatBot 相关的嵌入数据，并通过 **LZMA** 解压出两个关键文件：

* • `vcpktsvr.exe`
* • `libcef.dll`

然后恶意程序会在 `%LOCALAPPDATA%` 下创建 `vcpacket` 目录，把这些文件放进去，并在注册表 `Run` 项中创建持久化启动项 `pkt-update`，指向 `vcpktsvr.exe`。这意味着每次用户登录后，ZiChatBot 都有机会被重新激活。

从对抗角度看，这里有两个有意思的细节：

* • 它借助看似“正常”的 Windows 可执行文件名与路径结构，尽量让落地物不那么扎眼；
* • 它把“自删除”也纳入主逻辑，使攻击链更像一次短暂的投递过程，而不是把整个恶意工具箱都留在原始安装目录中。

## Linux 版本也在：通过 crontab 建立持久化

这次攻击并非只覆盖 Windows。Linux 版本的 wheel 包会落地 `terminate.so`，并把 ZiChatBot 放到 `/tmp/obsHub/obs-check-update` 路径下，再通过 `crontab` 创建自动执行任务。

与 Windows 版本相比，Linux 侧的 ZiChatBot 更简洁：报告称它只由一个 ELF 可执行文件组成。但思路完全一致——**开发者以为自己装的是一个 Python 库，实际上却在本机写入了可持久运行的后门组件。**

这也是为什么我会把这次事件看作一次非常典型的“开发生态层面攻击”：它不是利用浏览器、不依赖钓鱼文档，而是利用了开发者对包管理生态的天然信任。

## ZiChatBot 本体：不连专用 C2，而是借 Zulip 公共 API 通信

如果说前面的 PyPI 包只是“入口层”，那 ZiChatBot 本体最值得关注的就是它的控制方式。

Windows 版本的 ZiChatBot 以 `libcef.dll` 形式存在，由看似合法的 `vcpktsvr.exe` 加载。恶意逻辑位于导出函数 `cef_api_mash` 中。一旦运行，它会向 **Zulip REST API** 发起一系列连续 HTTP 请求。

报告中提到，ZiChatBot 当前主要支持的控制动作是：**执行从服务端收到的 shellcode**。它会使用两组独立的 channel-topic 对：

* • 一组用于发送当前系统信息；
* • 另一组用于拉取包含 shellcode 的消息。

当 shellcode 获取成功后，它会新建线程执行；完成后，还会向原始消息返回一个“心形表情”作为执行成功的回执。

这一设计说明，攻击者已经非常熟悉如何把公开协作平台“挪用”为命令控制层：

* • 流量目的地看起来像正常 SaaS 服务；
* • 不需要自建、维护、续费和保护传统恶意基础设施；
* • 一旦某个组织默认放行协作平台流量，检测和阻断门槛就会显著抬高。

这类“公共服务即 C2”的思路，已经成为近几年高端攻击中越来越常见的一条路线。

## 基础设施层面的启示：PyPI 是投递面，Zulip 是控制面

Kaspersky 没有发现典型的恶意基础设施——比如被入侵服务器、商业 VPS，或者对应的独立域名/IP 体系。相反，这次攻击的两大支点都落在**公开平台**上：

* • **PyPI**：承担恶意包投递；
* • **Zulip**：承担 C2 通信。

这说明攻击者越来越倾向于把攻击链“寄生”在高信任度的公共服务上。对于企业防守方而言，这会带来一个现实问题：仅靠传统 IOC 思路已经不够了。因为连接 `pypi.org`、访问公开聊天服务 API、拉取看似正常 wheel 包，在很多环境里都不属于显而易见的异常行为。

报告还建议，将 `helper.zulipchat.com` 完整 URL 纳入 denylist，以帮助定位或阻断潜在受感染主机。虽然 Zulip 已经停用了该组织，但已有感染设备依然可能持续尝试外连。

![](https://mmbiz.qpic.cn/mmbiz_png/UhfibIyPpmuMvIUuAPqoQMzAUhtVsuRfdZ10SqicfvAtWAU8Og5kwkicYW8Sk07IicAy2D9hbQ0Zrwb3DYfR489rCg2Edx089c5jMlwZrxmmjtA/640?from=appmsg)

*图 5：攻击者注册在 Zulip 上的 “helper” 组织已被官方停用，但历史感染主机仍可能尝试连接。*

## 归因为什么指向 OceanLotus

Kaspersky 的归因并不是“拍脑袋式”判断，而是基于 KTAE（Kaspersky Threat Attribution Engine）的分析结果。报告称，ZiChatBot 使用的 dropper 与他们先前在一份 TI 报告中分析过、并归因给 OceanLotus 的另一个 dropper 存在 **64% 的相似度**。

进一步的逆向对比表明，两者在：

* • 嵌入载荷的解密方式；
* • 解压逻辑；
* • 主要执行流程；
* • 关键算法和结构设计

等方面都具有较高一致性。

当然，64% 相似度并不等于数学意义上的“铁证”，但在威胁情报分析里，尤其是结合攻击对象、载荷设计、基础设施思路和历史活动轨迹时，它已经足以构成较强的归因支撑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/UhfibIyPpmuOC0vahF5m33zDdrJzrPhvkooODDtsKPpLWP0Ktshz41ENt8EMp4mhdK3yibw5MOZybG6ABgYvkXjBIt35OiasGyP3tslicNSIQds/640?from=appmsg)

*图 6：Kaspersky 的 KTAE 系统显示，本次 dropper 与历史 OceanLotus 样本存在显著相似性。*

## 这份报告真正提醒防守方的，不只是一个 IOC

我认为，这篇报告最重要的价值，并不只是告诉我们“某几个包名是恶意的”。更关键的是，它展示了一个越来越成熟的攻击公式：

> **开发生态投递 + 跨平台落地 + 公共 SaaS 通信 + 供应链伪装依赖**

这套公式对企业意味着几件事：

### 1. 包管理安全必须前移

如果你的开发环境、数据科学环境、研究环境或 CI/CD 允许直接从公网拉第三方依赖，就必须把**依赖来源治理、私有镜像、包签名校验、异常依赖审计**前移，而不是等 EDR 在终端侧“兜底”。

### 2. “看起来正常”的开发流量也要建模

访问 PyPI、GitHub、公开聊天 API，本来都是正常行为。但当这些行为与**新安装包、构建节点、异常进程落地、计划任务/注册表持久化**组合在一起时，就不再普通。真正有效的检测，必须走向**上下文关联**。

### 3. 供应链攻击越来越像“低可见度渗透”

这次攻击没有花哨的鱼叉邮件，没有明显 exploit，也没有显眼的 C2 域名。它更像是把恶意逻辑静静嵌进日常工程动作里。对于很多组织来说，这类攻击的危险之处恰恰在于：**它太像正常工作流的一部分。**

## 可操作的检测与缓解建议

基于报告内容，我建议至少补上以下检查项：

* • 检查是否曾安装过 `uuid32-utils`、`colorinal`、`termncolor`；
* • 在开发机与构建机中排查异常落地文件：`terminate.dll`、`terminate.so`、`libcef.dll`、`vcpktsvr.exe`；
* • Windows 侧关注 `%LOCALAPPDATA%\vcpacket\` 与 `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` 下的 `pkt-update`；
* • Linux 侧关注 `/tmp/obsHub/obs-check-update` 与异常 `crontab` 条目；
* • 检查是否存在到 `helper.zulipchat.com` 的可疑访问；
* • 将外部依赖接入内部镜像或审批流程，减少直接从公网安装未知包的机会。

如果你的组织里有 Python 开发、数据分析、自动化运维或安全研究团队，这类排查不应该被当作一次性的“新闻响应”，而应被纳入**常态化软件供应链治理**。

## 最后

OceanLotus 是否就是这次活动背后的最终操作者，后续或许还会有更多样本和情报来补强。但即使先把归因问题放在一边，这次事件本身已经足以说明：**攻击者正在把包管理生态当成长期稳定、成本低、隐蔽性强的投递面。**

对防守方来说，真正的挑战不是记住某个包名，而是建立一种新的判断习惯：当一个依赖“看起来只是开发工具”时，也要问一句——它有没有可能正在把后门带进来？

## IOC 提取

结合原始报告，文中可直接提取的 IOC 如下：

### 恶意包名 / 文件名

* • `termncolor-3.1.0-py3-none-any.whl`
* • `uuid32_utils-1.x.x-py3-none-xxxx.whl`
* • `colorinal-0.1.7-py3-none-xxxx.whl`
* • `Backward.dll`
* • `Backward.so`
* • `terminate.dll`
* • `terminate.so`
* • `libcef.dll`
* • `vcpktsvr.exe`

### 文件哈希（MD5）

* • `termncolor-3.1.0-py3-none-any.whl` — `5152410aeef667ffaf42d40746af4d84`
* • `uuid32_utils-1.x.x-py3-none-xxxx.whl` — `0a5a06fa2e74a57fd5ed8e85f04a483a`...