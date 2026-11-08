---
title: 今日速递｜Frida 17.26.1、Poki 真机、SSHhole 被打
url: https://mp.weixin.qq.com/s/4yDwaxHAoRW5TA0Nkf0irg
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:11:52.595977
---

# 今日速递｜Frida 17.26.1、Poki 真机、SSHhole 被打

# 今日速递｜Frida 17.26.1、Poki 真机、SSHhole 被打

小瑶在工地

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今日速递 · 2026-11-07

各位工友早。今天共 **19 条**：第一部分 7 条国内安全研究，第二部分 9 条工具与 X 讨论（新增 VMProtect、LLVM 优化与指针语义），第三部分 3 条事件进展；另附工具箱。今天主线是 **Frida 17.26.1** 补丁、**Poki** 免越狱真机 iPhone MCP，以及 Alpine 上 **\*sshole** 披露后数小时内已有蜜罐利用；昨稿 Frida 17.26.0 / GPT-6 Cyber / SSHhole 首发披露等不重复。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OoI9czGaCkQ9lBCtdzQ7QtpPCYVjF3v93uMia8eVC6Pb6uzWEJHrrmLgX5t8lGsypkYmbZUImibr3M24lpzNp6tOpbVcj2vlnZLyEM7cMlrbI/640?wx_fmt=jpeg&from=appmsg)

PART 1

## 第一部分｜国内安全厂商 · 安全网站 · 安全论坛热点

本层以看雪 Livewire 实战复盘 / IoT 协议与固件 Skill / 检测大纲 + 先知生成式 UI 沙箱与 CMS 鉴权文 + 看雪逆向 Skill 成条。KCLF、逆向已死2、先知沙箱与 MCP、UEFI / Anthropic / 冷柜等昨稿不重复；Seebug 521、FreeBuf 405、安全客本轮无强新 KEEP。

## 1. 看雪｜Livewire：属性注入打穿共享主机

看雪 WEB 安全区约 **5 小时前** 新帖复盘 **CVE-2025-54068**（Livewire 约 **≥3.0.0-beta.1, <3.6.3**，修复叙事落到 **3.6.4**）：公开影响是组件更新路径上的属性注入，可走到任意 PHP 函数调用，样本为共享主机 PHP 8.3 + Livewire v3.4.11，起点无需登录与 APP\_KEY。作者强调纵深防御各层被单独绕过后的连锁后果。本条只记影响面与升级取向，不复述利用链；跑 Laravel Livewire 的站点优先对照官方安全版本。

来源

```
https://bbs.kanxue.com/thread-293445.htm
```

**工地点评：**用了 Livewire 的站点，先查版本是不是还落在 3.6.3 之前。升级比事后翻日志划算。

## 2. 看雪｜无线吉他拾音器：空中协议也能逆向

看雪 IoT 安全区近窗原创：作者拆解某无线吉他拾音器的空中链路，开篇从**射频与扰码**入手，属于「听得见的硬件」协议逆向系列第一篇。适合做短距无线 / 消费电子固件与空口分析的读者当公开案例扫一眼；正文按学习向讨论协议结构，不涉及对他人设备的未授权接入。

来源

```
https://bbs.kanxue.com/thread-293366.htm
```

**工地点评：**想练射频和扰码，又不想一上来啃基站协议的，这篇消费电子案例更友好。实验请用自己的设备。

## 3. 看雪｜给大模型装固件审计骨架

看雪 IoT 区近窗长文介绍开源 **IoT 固件漏洞挖掘 Skill**：重点不是「让模型多看汇编」，而是把资深审计员的流水线、证据标准与质量门禁写成可执行协议；讨论跨请求高阶污点、对 IEEE S&P'26 Bridge 论文判据的实测修正，以及把文档本身纳入自检。作者明确说它不是一键挖洞工具。适合做固件审计自动化 / Agent 工作流的人对照自己的门禁设计。

来源

```
https://bbs.kanxue.com/thread-293350.htm
```

**工地点评：**关心「模型写的报告能不能复核」的，这篇比又一个扫描器名单更有用。先看门禁和四态判据，再谈接不接模型。

## 4. 看雪｜检测大全：从开机链讲到 Frida / KPM

看雪茶余饭后近窗热帖放出《检测大全》课程大纲：覆盖 APatch / TEE 三绿、Frida 与 LSPosed 源码、KPM 内核模块，以及企业壳检测逻辑拆解方向。定位是系统化底层课而非单点脚本。本条只记公开大纲与讨论热度，方便想系统补 Android 检测基础的读者点开目录；不展开任何对抗配方。

来源

```
https://bbs.kanxue.com/thread-293411.htm
```

**工地点评：**缺系统课、又总被检测打断的，可以先把大纲当「该补哪些底层」的地图。买课与否另说，目录本身已经能指路。

## 5. 先知｜生成式 UI 沙箱：Pyodide 碰到了 Deno 宿主

先知 AI 安全近窗：分析 **Prefab UI** 生成式 UI 执行链上的宿主权限越界（公开跟踪 **CVE-2026-120338**，影响叙述约 0.14.0 至 0.21.0 之前）。场景是大模型生成的 Python 在 **Pyodide / WASM** 沙箱里跑，却能经跨语言接口摸到 **Deno** 宿主文件 API。前提包括启用 Generative UI、安装 Deno，以及能调用相关 MCP 工具；不等同于默认安装即中、也不等于系统提权。做 Agent 代码执行沙箱的人，应核对「沙箱内对象是否暴露宿主全局」。

来源

```
https://xz.aliyun.com/news/93129
```

**工地点评：**沙箱里的 Python 如果还能直接叫到外面的文件系统，隔离就只剩半截。自己搭生成式 UI / MCP 执行器的，把跨语言桥列进检查项。

## 6. 先知｜某 CMS：鉴权绕过一路走到 RCE

先知近窗漏洞分析文梳理某 CMS 管理端鉴权链路：拦截器白名单、Token 刷新头、多处过滤器不一致等问题叠加后，可从鉴权绕过推进到远程代码执行。适合做 Java / Spring 类后台鉴权审计的人对照「白名单是否过宽、刷新令牌是否可被匿名触发」。本条只摘要公开结论取向，不复述请求构造。

来源

```
https://xz.aliyun.com/news/93135
```

**工地点评：**后台「刷新一下 Token」的接口如果匿名也能碰，后面的门再严也没用。做 CMS / 中台的，优先审登录周边白名单。

## 7. 看雪｜逆向 Skill：让模型按证据推进

看雪 Android 安全区近窗分享开源 **mobile-reverse-skill**：面向 Claude Code / Codex，把移动端逆向拆成可复用阶段，强调区分「观察到的事实 / 推测 / 已验证结论」，并在工具失败或证据不足时如实记录。适合做 AI 辅助逆向工作流的人对照自己的提示词与交接规范；仅面向 CTF、学习与授权范围内的应用研究。

来源

```
https://bbs.kanxue.com/thread-293328.htm
```

**工地点评：**模型爱早下结论，这篇 Skill 就是在教它「先亮证据再说话」。自己用 AI 做逆向的，可以把「事实 / 推测 / 已验证」三栏抄进工作流。

补查：Seebug Paper 本轮 521；FreeBuf 405；安全客本轮无强于昨稿的新 geek KEEP；嘶吼 CrystalRAT/OpenClaw 标注日期偏旧未进主条；看雪过 Root / 加固实操、KCLF、逆向已死2、透明代理、MemLLVM、AI APK、PHP2Shell 等昨稿或不适主条不重复。

PART 2

## 第二部分｜X 上的二进制 / 安全 / OS 逆向热点 + 越狱工具

窗内工具钩为 Frida 17.26.1 与 Vector canary-3118；真机自动化钩为 Poki。Frida 17.26.0 / Vector 3117 / GPT-6 Cyber / mirroir / Podroid / Facebook 相册评分昨稿不重复主条。

## 1. Frida 17.26.1｜QuickJS 异常哨兵修了三处

约 **2026-11-06 13:16 UTC**（≈ Asia/Shanghai 21:16），**Frida 17.26.1** 发布。官方说明：rebase 到当前 QuickJS 后，「无异常挂起」哨兵改为未初始化值而非 *null*；自有补丁里仍有三处把挂起异常重置成 *null*（挂起运行时供他线程使用、跑 `Error.prepareStackTrace()`、惰性全局钩子），会被新运行时误判为仍有异常。感谢 **@mrmacete** 修掉。相对昨稿 17.26.0 的小步补丁，用 Stalker / 多线程脚本的建议跟上。

来源

```
https://frida.re/news/2026/11/06/frida-17-26-1-released/ https://github.com/frida/frida/releases/tag/17.26.1
```

**工地点评：**昨天刚升到 17.26.0 的，今天可以再跟一版。出现莫名其妙的「空异常」时，优先怀疑是不是还停在旧补丁水位。

## 2. Vector canary-3118｜别问 Compose，问窗口按了哪颗键

**JingMatrix/Vector** 于约 **2026-11-06 20:03 UTC** 放出 **canary-3118**（相对昨工具箱 canary-3117）。Release 标题：**Ask the window which button was pressed, not Compose（#1060）**。仍是 canary：CI 通过即发。用 Compose / 多窗口场景的 Vector 用户可对照 Release 包；追 bug 用 Debug zip。

来源

```
https://github.com/JingMatrix/Vector/releases/tag/canary-3118
```

**工地点评：**昨天刚试 3117 工作资料夹的，今天又有一版按键相关修复。正式环境仍建议等稳定标签。

## 3. Poki｜免越狱，让 Agent 像你一样用 iPhone

**Poki**（约 **2026-11-05/06** 开源，AGPL-3.0）提供本机 **MCP Server + Agent**：在 Mac 上经 USB/无线连接真机 iPhone，读辅助功能树并发原生触摸/输入事件，公开卖点是**无需越狱、无需外接硬件、无需手机端 Helper App**。changelog 显示 v0.1.1 起支持远程连接。依赖 macOS + Xcode + Rust + Node.js 24+ 等。与昨稿 mirroir-mcp 同属「真机自动化」赛道，但本窗星标与讨论更集中在 Poki；仅面向自有设备。

来源

```
https://poki.bot/ https://github.com/JosssphZhou/poki https://x.com/ai_neuralwire/status/2118797227808506093
```

**工地点评：**不想越狱又想让模型点微信、提醒事项的，可以看 Poki。先在备用机跑，付款类操作它会停下来让你接手——别全程放手。

## 4. Claude Dispatch｜浏览器扩展也能代你点「允许」

The Hacker News 近窗转述 Forever Security：能在 **claude.ai** 跑脚本的浏览器扩展，可把任务塞进 **Claude Desktop** 的 **Dispatch**，在本机执行命令；测试里扩展自动点掉批准框并触发全局 npm install。前提是用户同时登录网站与桌面端且开启 Dispatch。Anthropic 称将退役 Dispatch，但帮助页仍写现有用户可继续使用；研究者还点名 Remote Control / Cowork 可能有相似面。本条只整理公开风险模型与缓解建议（关跨设备 Dispatch、审扩展权限）。

来源

```
https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html
```

**工地点评：**开了 Dispatch 的，先确认自己是否真的需要跨设备派活。浏览器扩展权限，要按「能替你点电脑」来管，而不是按「好看的小工具」。

## 5. Claude Code｜User-Agent 里漏出了登录邮箱

X 近窗汇总：Claude Code 为识别作者身份把登录邮箱放进上下文后，部分 Web 请求的 **User-Agent** 把头信息带给了第三方站点，用户反馈随后收到定向骚扰邮件。公开叙述称约 **2.1.317** 起有隐私插件临时阻断，并计划从上下文移除邮箱。做 Agent 上网工具的团队，应避免把身份标识默认塞进出站头；个人用户可对照版本与官方隐私说明升级。

来源

```
https://x.com/i/trending/2118630191685914974
```

**工地点评：**邮箱不该出现在随便哪个网站都能看见的请求头里。用 Claude Code 的，升到带隐私修复的版本；收到异常推销邮件时，优先怀疑是工具泄露而不是「巧了」。

## 6. CWP｜面板 Web 服务器被换成「无日志后门」

奇安信 XLab 近窗披露：Linux 主机面板 **Control Web Panel（CWP）** 的 web 服务器二进制被替换为后门版（称 **cwpdoor**），带特定完整性头的请求可执行命令且不进访问日志；安装需已有 root，伪装成版本更新脚本。公开给出套接字 / 进程 / strings 三类自查与 IOC。跑 CWP 的主机应对照原文自查，并视情况从备份恢复官方二进制、轮换面板凭据。

来源

```
https://thehackernews.com/2026/11/hackers-hide-linux-backdoor-in-control.html
```

**工地点评：**用 CWP 管机器的，按文章三条命令自查一遍不费事。已经中招的，当整机沦陷处理：换密码、查别的后门，别只换一个文件。

## 7. VMProtect 研究转帖｜练习样本还原，不等于通杀

2026-11-03 16:49（Asia/Shanghai），@MalwareBibleJP 转介一篇 VMProtect 虚拟化研究：借助 LLVM 中间表示重建练习程序中的单个 x64 函数，作者报告 199 组输入的输出一致，但尚未做形式化等价证明。原文发表于 9 月 9 日、9 月 22 日补充，本次是近期转帖而非新工具发布；样本关闭了其它保护，不能推广为通用能力。

来源

```
https://x.com/MalwareBibleJP/status/2117539535248884140
```

**工地点评：**适合想弄懂“虚拟机保护为何让反编译变难”的读者。先看练习样本的限制和验证结果，比只看“还原成功”四个字更有用。

## 8. QED｜模型改写代码，先证明再测快慢

2026-11-07 05:33（Asia/Shanghai），@julesreynd 分享 QED 黑客松项目：模型寻找比 clang -O3 更快的改写，再由 Alive2 检查等价性。按作者披露，134 个案例中 132 个获得已证明的改写，79 个进入实机测试，其中 51 个在两台 CPU 上都更快；这些是项目自报结果，并非 LLVM 官方性能结论。

来源

```
https://x.com/julesreynd/status/2118819057004609924
```

**工地点评：**做编译器优化的可以看它如何把“结果正确”和“跑得更快”分开验收。有证明也不代表一定加速，最后还得上真机测。

## 9. LLVM 与指针来源｜地址相同，不代表编译器眼里相同

2026-11-07 02:30（Asia/Shanghai），@ayushagarwal027 转介 C++ 与 Rust 指针来源教程，结合 LLVM IR、Godbolt 和 Miri 解释编译器怎样判断指针来自哪块分配。帖子也交代了反例：实验中的 Rust 显式指针 API 没带来预期优化，其价值在于表达意图、帮助检查误用，而非保证提速。

来源

```
https://x.com/ayushagarwal027/status/2118773081523306880
```

**工地点评：**看反汇编时遇到“明明写过，编译器怎么当没发生”的疑问，这类基础很有帮助。做底层开发或分析优化后二进制的，都值得补这一课。

## 工具箱补充｜版本与窗口内更新

和今天新闻相关的工具，版本信息以官方页面为准。有新 tag 的单独标出；无更新的也列一行方便对照。

**Frida 17.26.1**（新正式 tag；相对昨 17.26.0）

* QuickJS 异常哨兵三处修复。正文 PART2#1。
* 官方：
* https://github.com/frida/frida/releases/tag/17.26.1

**Vector canary-3118**（新 canary；相对昨 canary-3117）

* #1060 窗口按键询问修复。正文 PART2#2。
* 官方：
* https://github.com/JingMatrix/Vector/releases/tag/canary-3118

**Ghidra 12.2**／**jadx v1.5.6**／**Dopamine 3.0.13**

* 相对昨日无新正式 tag；Dopamine 不重复展开。
* Ghidra：
* https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra\_12.2\_build
* jadx：
* https://github.com/skylot/jadx/releases/tag/v1.5.6
* Dopamine：
* https://github.com/opa334/Dopamine/releases/tag/3.0.13

**Magisk v31.1**／**KernelSU v3.3.1**／**APatch 11282**

* 相对昨日无新正式 tag。
* Magisk：
* https://github.com/topjohnwu/Magisk/releases/tag/v31.1
* K...