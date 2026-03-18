---
title: 长亭「捕虾」工具开源首发！企业级 OpenClaw 风险监控实战指南
url: https://mp.weixin.qq.com/s/sdLxKFGBvEGpzBrHfOtL9Q
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:19:50.747766
---

# 长亭「捕虾」工具开源首发！企业级 OpenClaw 风险监控实战指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LJwWAbW20CiaJQ4bQmc0srKdrIERwVXKU0k965SrnPNgxxiagTpGRicqsTicK6mvicTC4yzGeRf3mrRH1bicAzbKvz0C2NJMV51AoKzaLtIIkU03w/0?wx_fmt=jpeg)

# 长亭「捕虾」工具开源首发！企业级 OpenClaw 风险监控实战指南

中国信息安全

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20CjVOCNTkiaXMLJZu5EN6FYrWq5QTWg6lH8oG45edcqias2emIIn4ByAKpZE9TnOUzMOozK18Oh9aR0yAKvdZq1iaXJ43JNAIfLAJY/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?from_tag=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uX9TOlqibIRtLibS6OM7tev0RyickHqFo11BlL39Dywer9ibkqiaHxwB6H0yHvfEJr3s0iaibtARo4TyngiaTNaibKtKYWu412JXfI8QxYMvHlWpPoGY/640?from=appmsg#imgIndex=1)

**文末下载长亭自研开源“捕虾”小工具ClawLens**

**No**

-Number-

**0****1**

**“小龙虾”过热引发毒性**

从被当作是提升效率的办公神器，到迅速被发现成为企业内网的隐形炸弹，这只被员工争相部署的 OpenClaw “小龙虾”，向企业安全管控抛出新问题。

**OpenClaw 相关漏洞：**

据国家信息安全漏洞库（CNNVD）统计，自2026年1月-2026年3月9日，共采集OpenClaw漏洞82个，其中**超危漏洞12个**，**高危漏洞21个、**中危漏洞47个、低危漏洞2个，包含了访问控制错误、代码问题、路径遍历等多个漏洞类型；漏洞**CVE-2026-25253（ClawJacked）** CVSS 评分 8.8 分，可远程控制本地 OpenClaw；超危漏洞**CVE-2026-28470** 为参数注入漏洞，可执行任意代码，影响全版本。

**OpenClaw 公网暴露风险数据：**

三方报告数据显示，全球超**4 万个 OpenClaw 部署实例**直接暴露公网，63% 存在已知漏洞，**1.3 万个实例**可被远程代码执行完全接管。

**OpenClaw 相关安全事件：**

Meta 公司OpenClaw 接入工作邮箱后失控，无视停止指令删除数百封核心邮件；知名 AI 编程工具 Cline npm 包被篡改，八小时内数百万开发者电脑被静默安装 OpenClaw 后门。

OpenClaw“龙虾热” 背后，是**工具漏洞、违规操作、管控缺位的三重隐患**，本地提权、主机入侵随时可能发生。为了让找虾、管虾成为清晰可控的方案，长亭快速推出企业级 OpenClaw 风险监控指南，发布开源 “捕虾” 工具，从全网扫描到流量狙击，一站式解决内网 “小龙虾” 隐患。

**No**

-Number-

**02**

**长亭“以虾捕虾”**

**工具“ClawLens”开源首发**

**秒安装，速排查**

ClawLens 是长亭科技自研的一款面向企业终端场景的 OpenClaw 安全检测工具，支持 Windows，macOS 和 Linux， 采用单二进制、零外部依赖设计，可快速完成本机 OpenClaw 安装、运行进程、系统服务、危险配置与凭证权限的安全检查。工具支持输出自包含 HTML 报告和 JSON 结果，**既适合安全团队人工排查，也适合集成到****SIEM****、自动化巡检或批量检查流程中。**

![](https://mmecoa.qpic.cn/sz_mmecoa_gif/iaZq4cu1zibCxpkmxmaE6WgBSXOSxhQOWFwKcImOISn2f8Ljlfiael5vrCh6cQlbqejlshmlsqibaib23XDv2vFOdatPxIh1l19sUicIzEyiaUMiaLE/640?wx_fmt=gif&from=appmsg#imgIndex=2)

在实际使用中，用户可直接下载对应平台的二进制文件运行，或通过源码执行 make build 完成编译。启动后，只需执行 clawlens 即可完成扫描并生成报告；如需接入自动化流程，可使用 clawlens -f json 输出结构化结果，或通过 clawlens -q 仅返回风险等级退出码，便于在脚本、CI 和批量巡检任务中调用。

该项目已经放置 GitHub 仓库开源，项目简介与使用方式可移步查看。

文末点击**“阅读全文”**直达下载地址

https://github.com/chaitin/clawlens/releases/tag/v0.1.0

![](https://mmbiz.qpic.cn/mmbiz_jpg/uX9TOlqibIRv2TR7guibc0a0cUbWHhQA66e7ia5EiaayYHibxNOjqVDxBKgxIxWR3BQS3ugvZHiaznIoSiaWHW80hBnNmayzGEQdrQbVOMFVVkfQAI/640?from=appmsg#imgIndex=3)

**No**

-Number-

**03**

**企业级捕“虾”指南**

已经部署了长亭风险评估系统（洞鉴）、资产暴露面运营管理（云图）、云工作负载保护平台（牧云）、长亭终端统一管控与安全检测响应平台、流量威胁检测响应系统（全悉）等产品的的用户，可暂时不依赖外部工具，参照以下指南快速“捕虾”。

场景一

**企业全网扫描海捕找“虾”**

**（附云图 SaaS 版免费试用申请通道）**

**核心目标**：内外网资产全面扫描识别 OpenClaw 的安装及部署。

**优势**：主动扫描，扫描范围广、发现速率快、更容易快速部署实施。

**✅ 使用工具：长亭风险评估系统（洞鉴）**

**排查覆盖范围**：内网互联网资产中 OpenClaw（及其历史版本 Clawdbot、Moltbot）系统的指纹识别与检测。

基于洞鉴自研的指纹识别引擎XAPP，通过对OpenClaw（龙虾）页面及接口特征的深度解析，提取了高置信度的指纹特征，在黑盒状态下精准识别 OpenClaw 及其历史包名 clawdbot/clawdis/warelay 的版本指纹。

以下为检测插件中的核心逻辑片段，用于匹配龙虾控制台的特征标识：

```
response.title_string.contains("Clawdbot Control") || response.title_string.contains("Moltbot Control") || response.title_string.contains("OpenClaw Control") || response.body_string.contains("__CLAWDBOT_CONTROL_UI_BASE_PATH__")
```

**操作指南**：

**下发任务：**洞鉴引擎已升级到6.18.11，根据扫描目标选择对应策略。

**执行扫描：**在内网网段（如192.168.0.1/24）或指定IP范围内执行探测任务，端口指定为8080或其他疑似端口。

**结果呈现：**洞鉴将实时输出检测结果，直接展示存在龙虾特征的资产IP、端口及匹配的具体指纹特征。

![](https://mmecoa.qpic.cn/mmecoa_png/iaZq4cu1zibCzr9WSicfrgMBeWSMtg04Sn9xTfZbrfcyk03L7HkvISzQjO1tqtS1m0gyLTEc2ukZnKiak2qxtKmqPIt8Hj2lFKH5dbS8MulZe7w/640?wx_fmt=png&from=appmsg#imgIndex=4)

**✅ 使用工具：资产暴露面运营管理（云图）**

**排查覆盖范围****：**互联网资产中 OpenClaw（及其历史版本 Clawdbot、Moltbot）系统的指纹识别与检测。

基于企业主体信息，云图即可自动关联发现全网的各类资产，并识别其指纹（包括 OpenClaw），仅需三步即可执行扫描任务！

**操作指南**：

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRuiaC34dicfbeQTYR8Ar9HdNpf7tibXE6EDyFZ0bUNgMWOlZZvPKNGuXibVohqMtWxl8429J8Opx2qvfiaBHgMEgiaFzPFRFAfdshhmg/640?from=appmsg#imgIndex=5)

未部署云图的客户，可通过下方通道申请免费试用（秒开通、免费试用 7 天，支持企业级扫描）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uX9TOlqibIRvNt76ppIibYaEQqeqU47jtsVibcZxwRcU3nQyg0S7GHw4AYGebxfk119iaSAhSSELgd24gibXTKQz2JqGC8thC0sZnBVumsNjJWgQ/640?from=appmsg#imgIndex=6)

场景二

**深度发掘“办公终端、**

**服务器终端”有没有“虾”**

**核心目标****：**定位已经安装成功的隐蔽性强的 OpenClaw，深度识别隐藏的安全隐患。

**优势**：主动扫描，更加深度识别，杜绝遗漏，同时可发现安装 OpenClaw 后的异常行为和遗留隐患。

**✅ 使用工具：云工作负载保护平台（牧云）**

**排查覆盖范围****：**覆盖服务器终端OpenClaw及所有衍生claw类框架，包括但不限于：OpenClaw Gateway、Claw Agent、ClawHub技能市场客户端、自定义claw类智能体进程，以及相关安装目录、配置文件等。

**操作指南**：

**1）找“虾”****---****识别定位****OpenClaw**

使用牧云进行进程级资产探测，利用产品资产清点功能，对进程名包含“openclaw、claw-agent、claw-gateway、claw-hub”；命令行参数包含“node openclaw、claw start、claw gateway”；可执行文件路径包含“~/.openclaw、/opt/openclaw、/var/lib/claw”进行搜索。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uX9TOlqibIRteLxz5hS1PZEQEP1AQjoQRbibV2xYbpiamuWiaHVZ3ccSUlVVrKz1nGVqZ8fCiaUUjcU2y6nQic5WK5tAPby4WdrJcap9AjYknGPHw/640?from=appmsg#imgIndex=7)

另外，产品还内置OpenClaw清点工具，可以一键清点OpenClaw资产，快速发现其安装情况。

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRtDpXuvkS8bk4U4Axunm6iayuA17icOQebKPwctAyibTzbUYgJrHaVUr7oQPV1lHaR09hQDsZib01YZmXCm1q1jMCLHh79n0tbM3Es/640?from=appmsg#imgIndex=8)

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRsib16aVtbWsBicoHGCKIs0Q3fSBQnqVIw3KJ6HMQcnxbQVQFjeqWennSlnLSKYa1YvCZeK8hO3fDZngBcj0huqU4nKGjvyTI0JA/640?from=appmsg#imgIndex=9)

**2）洗“虾”****---****实时监测****OpenClaw****以及其他****claw****的异常行为并进行防护**

实时监测OpenClaw及其他claw类资产的异常行为，精准识别本地提权、异常登录、恶意攻击等风险，通过自动化防护动作，在风险启动阶段阻断攻击路径，避免风险扩大。

**异常行为监测：**

* **高危端口监控：**实时监控claw类相关进程启动高危端口行为并进行报警。
* **本地提权检测：**重点监测claw类相关进程（如openclaw、claw-agent）的权限变更，包括但不限于：从普通用户切换为root/管理员权限、进程SUID/SGID权限新增、调用提权命令（su、sudo、chmod 4777等）。
* **暴力破解检测：**实时检测针对服务器的暴力破解行为。
* **异常登录检测：**检测登录IP非内网可信IP、非常用登录IP，或同一账号在短时间内从多个IP登录行为。
* **WebShell****检测**：实时检测 claw类进程关联的WebShell文件：监测/opt/openclaw、~/.openclaw等目录下新增的.php、.jsp、.sh等可疑脚本文件。
* **恶意文件检测:**对 claw类安装目录、运行目录、Skill技能包目录、临时文件目录进行恶意文件扫描，重点检测可能存在的恶意可执行文件、病毒、木马、恶意脚本。
* **可疑命令执行**：一旦检测到claw类进程有高危命令执行，立即触发告警，支持自定义新增高危命令规则。
* **网络异常检测：**监测claw类进程对外连接恶意 IP、恶意域名的行为。

**实时入侵自动防护：**

* **网络类自动封禁 IP：**针对暴力破解行为、异常登录、网络异常外联行为进行自动化封禁。
* **进程类自动阻断进程：**针对本地提权、可疑命令等行为进行自动化阻断进程。
* **文件类自动隔离文件**：针对 WebShell、病毒、木马等恶意文件进行自动化隔离。

**3）防“虾”****-****针对已发生的****claw****类安全事件快速处置，避免再次出现**

对已发生的claw类资产安全事件（如进程失控、恶意文件植入、主机被入侵），通过快速处置动作，隔离风险、清理恶意文件、恢复系统安全，同时溯源事件原因，避免再次发生。

**微隔离-- 一键隔离“失控”主机：**当检测到claw类资产失控（如进程被恶意控制、主机被入侵、大量敏感数据泄露），且自动化防护无法彻底阻断风险时，开启主机一键隔离，立即将失控主机与内网其他主机、公网隔离，禁止主机对外发送数据、接收外部连接（仅保留运维管理通道，供后续处置）

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRubKHRA2Rrh7npmduB3zV259sKS97Ievq9bRv85zYZJibuoO3FbNXF64NVrxHAhkBpaj6aY59xuIwibzQs02ZtWlic1qAyJ9pcXpg/640?from=appmsg#imgIndex=10)

**清理恶意文件：**针对已确认的恶意文件（如病毒、WebShell），支持一键清理文件**。**

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRvX4icRbkHlViaaIuzE8dbicfqx9FxPuKBYWf3rXMuUIA0ZycRibsdcehZ4cL2sibpafibHk4rQ42rn9AuaodSIBibwtiadLfvGsffHWC0/640?from=appmsg#imgIndex=11)

**日志溯源：**可自动收集事件相关日志（进程日志、网络日志、文件日志、登录日志）并实时转发至用户日志平台，供安全团队分析进行溯源，避免同类事件再次发生。

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRvgDzG8X8NS7o2xtVoKkXAwo3zPbDODHzVQzTpfiaCVHIXCvNnnsfwGickKS7n4EAjBwFrbd7P6ib857faGIfxItwPhMOUeXrTgUA/640?from=appmsg#imgIndex=12)

****✅**使用工具：长亭终端统一管控与安全检测响应平台**

macos + windows + 信创 linux 三端均支持。

企业管理者可以通过「终端管理/合规基线」页面，一键检测所有员工是否安装了小龙虾（当识别到安装了小龙虾行为时会在平台产生日志）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uX9TOlqibIRsIB8O7DwdHaJVDI7YXwibGP5eCnicE5Ou8EJj19NZ0vwgzdvfPGzThd9HdricuMptjvQR5SskTQ2ibMRy1WpaKhoOFQiaDuOj68FOw/640?from=appmsg#imgIndex=13)

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRsqTDbgVv285EYhbibibeD5amhdEncYcIY4baudkib2B5iaKa9yoibzxY3K9lTmJ6p5WYmnPBHGwo87sia5UatibQesnztmlOMibsYfUCk/640?from=appmsg#imgIndex=14)

![](https://mmbiz.qpic.cn/mmbiz_png/uX9TOlqibIRtRwpnFf8nqceYibJBicHtrLfnwboElLGrN8PS8R8tRYG3ePcwyR5p0iaWk1MOv2esWricgQAZ4NRlc1fKqeTKvCsQia27QwmjDVvPU/640?from=appmsg#imgIndex=15)

**操作指南**：以控制浏览器插件的方式发现控制OpenClaw的安装与使用，如“Clawdbot Browser Relay”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uX9TOlqibIRsNcPLhv4sVDPEnMicSpaweOGNQ4TQePwqfLCTguW2v23UOSCCu28cW25ugP3fwKdAiaHR5mIJIJ0ouwt4knSHDxqj9yXXoicTVbU/640?from=appmsg#imgIndex=16)

以防火墙和安全远程访问功能模块限制、隔离OpenClaw网络访问权限，防止OpenClaw意外暴露到局域网或公网。最好默认只监听本机。

* **检查防火墙是否开启**

![](https://m...