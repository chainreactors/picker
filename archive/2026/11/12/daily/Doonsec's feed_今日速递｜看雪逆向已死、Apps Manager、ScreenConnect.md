---
title: 今日速递｜看雪逆向已死、Apps Manager、ScreenConnect
url: https://mp.weixin.qq.com/s/kDzio-jB1RVcgyBKwZOO1w
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:16.893961
---

# 今日速递｜看雪逆向已死、Apps Manager、ScreenConnect

# 今日速递｜看雪逆向已死、Apps Manager、ScreenConnect

小瑶在工地

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今日速递 · 2026-11-12

各位工友早。今天主线是看雪上关于「**逆向已死、AI当立**」的讨论、社区把**Apps Manager** 称已移植到 iOS 27.2.1，以及经失陷**ScreenConnect** 打进 MSP 的新活动；昨稿安卓指南、币安沙箱告警、Outlook 在野漏洞等不重复。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OoI9czGaCkQDsGK4ccH37KG0qwjkzCtZUV2rHesUib904WdV8EUBxSjLvrg4BqX1ibVth6jD46fgKaeZykVWwpZeuib4t3CI8wLsO1TAW88glw/640?wx_fmt=jpeg&from=appmsg)

PART 1

## 第一部分｜国内安全厂商 · 安全网站 · 安全论坛热点

本层以看雪窗口内新帖为主（AI 对逆向行业的判断、GhostFrame / ESXi 转述、CISO 调查编译等），并补入安全客对一批 AI 平台令牌失窃的译文。评奖公关、提示词实验和求职讨论不进主条；安卓指南、drozer、暗网凭据等昨稿不重复。

## 1. 看雪｜「逆向已死，AI当立」：行业判断先看这篇

看雪 Android 安全版块在约**2026-11-11** 出现一篇由「小黄鸭爱学习」撰写的帖子，标题是《逆向已死，AI当立！！！逆向工程师该何去何从》，首页已经能看到。作者的核心判断是：AI agent 已经把客户端算法分析从过去常见的「十天半个月」缩短到数小时，传统主要靠加固、加密来对抗分析的做法会越来越难维持，安全重心会更多转向云端风控。这里只记这条行业判断和它讨论的影响，不展开具体分析步骤。

来源

```
https://bbs.kanxue.com/thread-293502.htm
```

**工地点评：**做客户端安全、或者正在考虑要不要继续深耕逆向的人，值得先点开看作者怎么论证；把它当成一份观点帖，而不是操作指南。

## 2. 看雪｜转述 GhostFrame：ESXi 层被指可拿走 Windows 凭证

同一窗口里，看雪资讯转载了一篇关于新型恶意框架 GhostFrame 的报道，标题写它能控制 VMware ESXi 虚拟机，并且不必进入客户系统就能窃取 Windows 凭证。文末标明资讯来源是 cybersecuritynews，并转述 Recorded Future / Insikt Group 的研究，把它与 TAG-218、Settra 勒索活动联系起来。这里只记公开报道里的事件轮廓和影响面，不写植入或传播步骤。

来源

```
https://bbs.kanxue.com/thread-293503.htm
```

**工地点评：**管虚拟化平台的人值得看一眼这条转述：如果威胁出在宿主机这一层，只加固虚拟机内部是不够的。细节以原研究报告为准。

## 3. 安全客｜一批 AI 平台被盯上的是访问令牌

安全客于**2026-11-11 11:01** 刊登一篇译文，梳理 9 月底到 11 月初至少十几家 AI 开发者或托管平台遭同类攻击的公开披露，认为攻击者要的高度集中在 AI 访问令牌，而不是一般业务数据。名单是各家自己公告拼起来的，包括 Andromeda、NVIDIA Brev、CommandCode、Lightning AI、Northflank、OpenCode、Railway、Trigger.dev、Warp、Zeabur，以及本周披露的 Chainstack（10-26）和 WorkOS（10-30）。Fireworks AI 也出现在名单里，细节昨稿已经写过，这里不再展开。文中还提到部分事件里用到了开源渗透框架 ARTEX，11-09 已介绍过该工具本身，本条不重写。

来源

```
https://www.anquanke.com/post/id/316461
```

**工地点评：**用这类托管或评测平台的团队，重点是把自己的 AI 令牌当一等凭据来管，并核对本周 Chainstack、WorkOS 的官方说明；名单是公开披露的汇总，不是一份完整受害目录。

## 4. 看雪｜微步编译：100 位 CISO 怎么排 2027 的安全优先级

看雪资讯在约**2026-11-11** 刊出微步对 a16z《The New Security Agenda》的编译：调查对象是 100 位千人以上企业的 CISO。帖内写**87%** 计划增加 2027 年安全预算，只有**4%** 打算缩减安全团队；2027 的多项优先级都与 AI 有关，AISOC 排在第一，但生产落地比例仍然不高（帖内写 AISOC 的生产使用为**18%**）。数字以该编译原文为准，这里不做外推。

来源

```
https://bbs.kanxue.com/thread-293500.htm
```

**工地点评：**做安全规划或向上汇报预算的人，可以把它当作一份同行问卷摘要；注意这是编译稿，引用时最好再核对 a16z 原文。

## 5. 看雪｜凌空罩：Windows 本地防截屏工具

看雪安全工具版块在约**2026-11-11** 深夜出现一篇介绍帖，推荐 Windows 上的本地防截屏、防录屏软件「凌空罩 / AkashaVeil」0.1.x。作者强调它不联网，可以对窗口做捕获排除，或叠一层显隐水印便于追查。这是窗口内的公开工具介绍，偏产品功能，这里只记它的定位，不写实现细节。

来源

```
https://bbs.kanxue.com/thread-293504.htm
```

**工地点评：**有会议保密或窗口防截取需求的人可以看一眼功能说明；它不是安全分析长文，也还是 0.1 的早期版本。

## 6. 看雪｜ARTEX 热门 Fork 被指换成带后门的镜像

微步在看雪资讯的转述帖（约**2026-11-11**）写道：ARTEX 项目下架之后，出现了高星 Fork，维护方把官方镜像换成了第三方镜像，登录接口存在未认证命令执行后门。事件起点正文写的是 11 月 4 日，11-09 稿已经介绍过 ARTEX 工具本身，本条只记「热门 Fork / 镜像被替换」这一新进展，不写触发条件，也不重复工具用法。

来源

```
https://bbs.kanxue.com/thread-293501.htm
```

**工地点评：**还在跟 ARTEX 相关仓库的人，先核对镜像和维护者是不是原来那套；不要随便去跑来路不明的 Fork。

7. 先知｜延伸阅读（11-09）：路径检查过了，写入仍可能离开工作区

先知社区在 2026-11-09 20:30 刊出一篇由 Chihiro 撰写的文章《【AI安全】Agent 写文件时，路径检查通过后为什么还会越界？》。这不是今日新帖，日期写在这里，当作窗口外已核实材料的延伸阅读。文章从已公开的 Claude Code 问题 CVE-2026-103435 说起：权限检查通过时，目标还在项目目录里；真正写入时程序会再按路径查找一次，中间如果目录项变了，文件就可能写到工作区外面。Anthropic 公告将受影响版本列为 2.1.129 之前，并在 2.1.129 修复。作者还顺着同一条「先检查、后按路径再打开」的时序，看了 OpenClaw、OpenShell 的写入和同步函数。11-08 稿写过 Claude Code 把密钥写进公开配置文件的那起事件，和本条不是同一件事。

来源

https://xz.aliyun.com/news/93227

工地点评：做 Agent 产品、或会让模型在本地写文件的人，值得点开看看「检查过了」和「最后写到哪里」为什么不是一回事；这是 11-09 的分析文，不是今天的新漏洞通报。

补查：窗口内国内新帖仍不足以另写一条「今日」新闻。第 7 条改用 11-09 先知已核实研究作延伸阅读（93227），日期已在标题和正文标明，不是今日新文。同日可打开的 93221 是 WordPress 插件分析、93223 是系统调用拆解，不进主条。嘶吼未见窗口内新稿；Seebug Paper RSS 最新仍为 11-05；FreeBuf 此前被拦。看雪探针 293505–293511 仍为空壳，最高真实新帖仍是 293504。微步雷达评奖、绿盟获奖稿、Deepseek 提示词实验等不进主条。安卓 / iOS 逆向以及 LLVM、VMP、TEE、keybox 方向，窗口内没有可独立成条的新材料；昨稿安卓指南、drozer、暗网凭据等不重复。

PART 2

## 第二部分｜X 上的二进制 / 安全 / OS 逆向热点 + 越狱工具

本层先写 worse\_query 生态里的社区工具新进展（Apps Manager 称已覆盖 iOS 27.2.1，WQFiles 连发 0.9.x），以及微软 FORGE 的内核缺陷报告、Lazarus 研究、Zoom 补丁和 AntiFox 相关入侵观察。不重复昨天的币安沙箱告警、Regitela 首发和苹果 11-09 更新主条；网上误传的 jadx v1.5.1、APatch 11219 与官方发布页不符，不采用。

## 1. X｜Apps Manager 称已移植到 iOS 27.2.1

@yang\_niubi 于**2026-11-11 18:35 UTC**（北京时间 11-12 02:35）发帖称，已经把 Apps Manager 基于 worse\_query 移植到 iOS 27.2.1 及以下，不需要 TrollStore 或越狱，可以直接安装 IPA，用来查看应用容器并备份、恢复或清理数据。@qwerty\_\_cs 大约 20 分钟后发了同主题说明。这是昨稿币安、慢雾、OKX 告警之后的社区工具新进展，不是那条告警本身，也不是 Filza 或 Regitela 的首发。苹果是否已经修好 worse\_query，本窗口仍未见官方确认，这里不写成已经修好，也不写安装方法。

来源

```
https://x.com/yang_niubi/status/2120586276202225942

https://x.com/qwerty__cs/status/2120591038037545195
```

**工地点评：**关心这条沙箱问题后续工具的人，可以把它当成「有人声称覆盖到了 27.2.1」的进展记录；能不能用、安不安全，都还要自己判断，别把它理解成完整越狱。

## 2. WQFiles｜窗口内连发 v0.9 到 v0.9.3

同一条技术线上，kolbicz/WQFiles 在窗口内连续打出四个正式版 tag：v0.9（**2026-11-11 11:47 UTC**，北京时间 19:47）到 v0.9.3（18:18 UTC，北京时间 11-12 02:18），都不是草稿或预发布。项目把自己定位为无需越狱的 iOS 文件浏览和应用数据管理工具，具体系统版本范围以仓库说明为准。仓库本身 11-09 就已创建，昨稿只点到、没有单开主条；今天写的是 0.9.x 连续正式版本，不重复首发故事，也不写签名或操作步骤。

来源

```
https://github.com/kolbicz/WQFiles/releases

https://x.com/iOSRXWY/status/2120566403686433003
```

**工地点评：**已经在跟踪这条工具线的人，去官方 Release 页看 0.9.3 即可；它和上面的 Apps Manager 是同一类社区跟进，不是新的完整越狱方案。

## 3. 微软 FORGE Lab｜59 个 Linux 内核缺陷报告

微软安全博客于**2026-11-11** 刊出 FORGE Lab / Cen Zhang 的新文《Lessons from 59 Linux Kernel Bug Reports》。这和 11-10 稿用过的 11-09 那篇 Rust / Hyenas 文章不是同一篇。文中写：他们用代号 MDASH 在 2026 年 5 月下旬到 6 月中旬扫描了部分 Linux 内核子系统，目前公开向上游提交了**59** 份报告，已分配**33** 个 CVE，其中**8** 个在受控实验室确认可本地提权，**38** 个修复已经合入 mainline。初始扫描大约两周产出大量原始发现，但整理成可复现的报告和补丁花了数月人工。59 份报告里，缺陷从引入到首次公开报告的平均年龄是**8.1 年**。这里只记规模和结论，不写那 8 个 CVE 的构造过程。

来源

```
https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/
```

**工地点评：**关心内核安全和辅助挖洞方法的人值得读原文：它把「扫出很多候选」和「真正向上游交出去、合进主线」之间的工作量写得很清楚，人也还是瓶颈。

## 4. 微软｜Lazarus：改很少的神经元给智能体加后门

微软研究博客于**2026-11-10** 发表关于 Lazarus 的研究（昨稿未收录），The Hacker News 在 11-11 跟进。研究展示一种权重级后门：编辑少于 10 个很少被激活的神经元，不需要完整重新训练，就可以在特定条件出现时让智能体执行攻击者的命令。微软写明尚未看到威胁行为者使用该方法，并给出了权重比对、来源审计等防护方向。这里只记研究结论和官方态度，不写植入方法的细节。

来源

```
https://thehackernews.com/2026/11/microsoft-researchers-show-ai-agents.html

https://www.microsoft.com/en-us/research/blog/lazare-veni-foras-reprogramming-dormant-neurons-to-backdoor-ai-agents/

https://www.microsoft.com/en-us/security/blog/2026/11/10/detecting-sleeper-agents-hiding-in-ai-model-neurons/
```

**工地点评：**做模型供应或智能体部署的团队，可以把这篇当成「权重被改过也要能查」的提醒；它是实验室研究，不是已经在野的攻击通报。

## 5. Zoom｜Workplace for Windows 两个未认证提权漏洞已出补丁

Zoom 于**2026-11-10** 发布两份安全公告，The Hacker News 在 11-11 跟进。ZSB-26023（CVE-2026-108186）是输入验证问题，CVSS**9.6**（严重），影响 Zoom Workplace for Windows 从 7.1.0 起、7.1.8 之前的版本；ZSB-26024（CVE-2026-108187）是来源验证错误，CVSS**8.1**（高），影响 7.1.5 之前的版本。官方描述均为：未经认证的用户可能通过网络访问完成提权。公告未称已经遭到在野利用。这里只记分级、影响版本和升级方向，不写利用方式。

来源

```
https://www.zoom.com/en/trust/security-bulletin/ZSB-26023

https://www.zoom.com/en/trust/security-bulletin/ZSB-26024

https://thehackernews.com/2026/11/critical-zoom-workplace-flaw-could.html
```

**工地点评：**公司电脑还在用 Zoom Workplace 老版本的，去官方下载页升到公告要求的版本即可；不必等到出现在野利用再动。

## 6. AntiFox｜开源智能渗透平台被观察到用于 AWS 密钥相关入侵

The Hacker News 于**2026-11-11** 转述 Arctic Wolf Labs 向其提供的报告：部署在阿里云上的开源智能渗透平台 AntiFox 界面，与针对互联网 IIS 及 AWS 环境的入侵有关，部分案例成功读取了生产环境 Secrets Manager 中的密钥，或对 S3 进行了操作。THN 写该 GitHub 项目当时约 474 个 star、251 个 fork。文中回顾了已报道的 ARTEX 等工具，11-09 已写过 ARTEX 本身，本条只记 AntiFox 这条新观察。Arctic Wolf 的独立博文本轮未打开，事实以 THN 11-11 转述为准。

来源

```
https://thehackernews.com/2026/11/antifox-ai-pentesting-platform-linked.html
```

**工地点评：**管云上密钥和跳板机的人值得看这篇转述，核对自己这边有没有来路不明的渗透平台实例；它不是对某个 CVE 的补丁说明，细节以原报告为准。

## 工具箱补充｜版本与窗口内更新

和今天新闻相关的工具，版本信息以官方页面为准。有新 tag 的单独标出；无更新的也列一行方便对照。WQFiles 的 0.9.x 已写入第二部分第 2 条，不在本工具箱常列清单里；苹果 11-09 那批安全更新没有新增条目，不重写。网上误报的 jadx v1.5.1、APatch 11219 与官方发布页不符。

**Frida 17.26.2**（相对昨日无新正式 tag）

* 仍为 2026-11-07 发布的 17.26.2。
* 官方：
* https://github.com/frida/frida/releases/tag/17.26.2

**Vector canary-3118**／**Ghidra 12.2**／**jadx v1.5.6**／**Dopamine 3.0.13**

* 相对昨日无新正式 tag。
* Vector：
* https://github.com/JingMatrix/Vector/releases/tag/canary-3118
* Ghidra：
* https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra\_12.2\_build
* jadx：
* https://github.com/skylot/jadx/releases/tag/v1.5.6
* Dopamine：
* https://gi...