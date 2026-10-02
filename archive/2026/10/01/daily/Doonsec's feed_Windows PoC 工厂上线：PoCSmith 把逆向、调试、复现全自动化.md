---
title: Windows PoC 工厂上线：PoCSmith 把逆向、调试、复现全自动化
url: https://mp.weixin.qq.com/s/OZNzUiH_gqfVFxIZNgRQzA
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:48:01.199916
---

# Windows PoC 工厂上线：PoCSmith 把逆向、调试、复现全自动化

# Windows PoC 工厂上线：PoCSmith 把逆向、调试、复现全自动化

原创

Dr. Clay
Dr. Clay

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OMvvLokmNkxibia9wtWzTUD50YushlFxeQedxQvhFYUUBVEWTRMKk14Ucx6hd9fd4XicYlQGiaS1A2wl3hibw7PJ2NTDA25BEYtTdA/640?from=appmsg)
> **导语**：当补丁日（Patch Tuesday）一次性扔出上百个CVE，传统手工挖洞链路被无限拉长。originsec近日开源的PoCSmith给出了一个激进的解法——让LLM Agent读完补丁diff，自主完成Ghidra逆向、内核调试与虚拟机复现全流程，把PoC开发从"工匠手艺"变成"流水线作业"。

---

## 一、为什么要关心这个工具？

对一线漏洞研究员而言，从微软月度安全更新里挖出一个可利用的CVE，传统链路是这样的：拉取patchwatch diff报告 → 锁定受影响二进制 → Ghidra加载前后版本做ghidriff diff → 阅读反编译代码定位可疑点 → 写触发器 → 在Hyper-V里挂内核调试器 → 反复跑崩 → 抓dump分析 → 验证可利用性。这条链路里"读代码 + 反复调试"占据了80%的时间，且对操作员的耐心是极大消耗。

PoCSmith的出现并不是要替代研究员，而是把这条链里所有可形式化的部分外包给LLM Agent：研究员只需要在一个CVE上写出第一份"该走哪条路"的hint，剩下的代码生成、编译、部署、下断点、抓现场、再迭代，都由Agent循环完成。它的本质是**给漏洞研究配了一个能7×24小时不睡觉、严格按剧本执行的实习生**。

![PoCSmith自动化流水线](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6Oqj0zSibzseWibgH3iby7EZINTVEFIe3ff0u0cHKm80GK6Zx9fET68h9ia5jqWlEESJY50aBbKSiba9zPq02JBN2ibf3vIlicmCzV9TY/640?from=appmsg "PoCSmith自动化流水线")

## 二、PoCSmith的核心架构：六个MCP拼起来的"流水线工厂"

PoCSmith的代码结构并不复杂，它本身只是一层"胶水"——把六个MCP（Model Context Protocol）Server粘成一个闭环，让Claude Agent可以像调用函数一样调用每一个研究环节：

| MCP Server | 角色 | 来源 |
| --- | --- | --- |
| **patchwatch** | 产线入口，提供CVE diff报告与受影响二进制排名 | originsec/patchwatch |
| **pyghidra-mcp** | Ghidra逆向引擎，加载pre-patch二进制并应用PDB符号 | clearbluejar/pyghidra-mcp |
| **hyperv-mcp** | Hyper-V VM生命周期管理：快照、内核调试配置、PowerShell-Direct执行 | originsec/hyperv-mcp |
| **kd-mcp** | 远程内核调试器封装：断点、寄存器/内存读、!analyze -v | originsec/kd-mcp |
| **pocsmith-mcp** | 司机工具：编译、记录尝试、声明成功、结束phase | 本仓库自带 |
| **Anthropic API** | 思考者：默认claude-opus-4-7，可切换 | — |

这套架构的优雅之处在于**职责分离**：每个MCP只负责自己那一小块，Agent作为调度器在它们之间来回穿梭。当patchwatch报告说"CVE-2026-XXXXX影响win32k.sys的xxx函数"，Agent会先调pyghidra-mcp看反编译代码，再调hyperv-mcp启动一个pre-patch VM快照，接着调kd-mcp下断点，然后写PoC源码编译，最后让kd-mcp验证是否如预期崩在指定位置。下图展示了端到端的工作流：从PatchTuesday KB输入开始，经过五个阶段后走向成功或失败反馈环。

![PoCSmith 端到端工作流](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PqRLVQp4tOY5WsvVKMoJ7vqw4IAdu7xhfhQB3K46MdicqOp7ialXPg7HBxOSlGHDpl4HSSKtOKPdJZ85T7Za9AzH9pz2oOkpA8o/640?from=appmsg "PoCSmith 端到端工作流")

## 三、三档难度等级（A/B/C）与"工时天花板"

PoCSmith把PoC开发拆成三档可量化的目标，每档对应不同的工时、迭代次数、预算与phase数：

* **Level A — Crash Repro**：让目标程序崩在指定位置。预算60分钟、40次迭代、$10、8 phase。
* **Level B — Controlled Primitive**：拿到可控的读/写原语。预算240分钟、80次迭代、$50、16 phase。
* **Level C — Full Exploit**：完成完整利用链（提权/RCE）。预算240分钟、80次迭代、$50、16 phase。

这种"工时天花板 + 美元预算"的硬约束非常工程师文化——它承认LLM Agent是**会跑偏、会浪费token的**，所以必须给它画一个圈。研究员的角色从"亲自动手挖"变成"调参 + 写hint + 验收"。这种工作模式的转变，其实和软件工程从汇编走向高级语言的过程是同构的。

## 四、安全边界与免责设计

作者在README里反复强调一条铁律：**所有payload都只能在目标Hyper-V VM里跑，永远不会触及host**。这个保证来自hyperv-mcp的设计——Agent的系统提示里硬编码了执行边界，所有编译产物和执行动作都被限制在guest VM里。这是这类工具最容易翻车的地方（一旦Agent误把payload丢到host，整个研究员的笔记本就成肉鸡了），所以作者把它做成了**默认安全**而不是"调用方自觉"。

但免责归免责，研究员自己仍然要清楚：PoCSmith产出的一切POC源码、repro脚本都属于"已授权研究输出"，只能在你自己控制的VM里跑，任何对生产环境、他人系统的复用都需要重新走授权流程。

## 五、实战部署要点

整个工具链对宿主机有明确要求：Windows 11宿主 + Hyper-V、32GB内存起步、一份与CVE对应KB前的Windows ISO（如24H2）、Visual Studio 2022带C++桌面开发、Windows SDK含Debugging Tools（kd.exe）、Docker Desktop（推荐ghidra.mode=docker）或Java 21+Ghidra 11.x。

部署本身不复杂，仓库的`scripts\setup.ps1`会创建venv、装好所有依赖、拉pyghidra-mcp Docker镜像。研究员要做的核心配置只有三件：.env里填好ANTHROPIC\_API\_KEY和guest VM凭据，pocsmith.yaml里指定patchwatch路径与workspace根目录，最后用`patchwatch export-poc-context CVE-2026-XXXXX`导出报告，`pocsmith run --cve ...`开跑。

## 六、验证方法与未来趋势

如果想验证这套流程是否真正可用，最直接的checklist是：在你自己的Hyper-V里用一份已知公开CVE（如CVE-2026-XXXXX对应KB的pre-patch ISO）跑一遍Level A，看Agent能否在wall\_min=60分钟内拿到BSOD并产出notes.md与attempt history；如果连A都过不了，说明hint或配置有问题，可以`pocsmith resume --cve ...`接着跑。

从趋势上看，PoCSmith代表了一类新工具的雏形——\*\*"补丁驱动 + LLM闭环 + 沙箱执行"\*\*的三位一体。同样的模式可以平移到Linux内核、浏览器、macOS XNU，未来半年我们大概率会看到patchwatch+类似流水线在更多平台上铺开。对一线研究员而言，越早把这类工具纳入自己的工作流，就越能在补丁日的窗口期里把CVE变成可提交的PoC，而不是在Ghidra里一行一行啃反编译。

---

**下载地址**：https://github.com/originsec/pocsmith

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MvgHlLhIGicYz4JG4edwlXibCv1cK52Qcg0v69OXNBVJtyxwQHHicjynnd9a5mJseia8pqYY025diciakSubURFpVatDY9vhw0AM1R4/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NpOngTlSqReTiatzElI4wc8HXGQDxkYH96AjmcGiakBF5xRsVAlwyEbCV2liaAiaiano48kKqpSQRibDN526iabfaJYn70R7H7DqqfTg/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PNLBW35QdeEpuVXjndZJI9FB9uqib25MN04A6icNyvQXIQ7ZibdBfAJmSBfcFHHXeJwfVY1ZCAeQTJibwWN3E3v690KEYC808QzXM/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6M2uhwTVkHkQhSNC14snVofLANPdhLysrJdiavK0NRJJXzibsNukJy0tibFwBGHUrmaZE7Pa45wvDWWjgKa6sG3bjDLyDY8Io4UxU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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