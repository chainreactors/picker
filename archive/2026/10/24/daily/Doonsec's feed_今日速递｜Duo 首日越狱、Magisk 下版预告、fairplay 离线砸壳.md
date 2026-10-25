---
title: 今日速递｜Duo 首日越狱、Magisk 下版预告、fairplay 离线砸壳
url: https://mp.weixin.qq.com/s/-KAyaYN9Cw_BIMRIFTTjfA
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:09:54.783742
---

# 今日速递｜Duo 首日越狱、Magisk 下版预告、fairplay 离线砸壳

# 今日速递｜Duo 首日越狱、Magisk 下版预告、fairplay 离线砸壳

小瑶在工地

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今日速递 · 2026-10-24

各位工友早。KeyMint / keybox 近窗仍热，今日不重复；Duo 首日越狱与 Magisk 下版预告压过其他钩子。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OoI9czGaCkRMiaGGZMCic4LCIKx9erFTvKmyEluTM5Gviagh9rQvwzPExM01qVEkYtjP3LrEamWlHrYIE9vhiaOy8JPDicXYIXN2vMuIicYJXBBGo/640?wx_fmt=png&from=appmsg)

PART 1

## 第一部分｜国内安全厂商 · 安全网站 · 安全论坛热点

本层以看雪近窗口新帖为主；Seebug Paper 收入 nokast-secureRAG 与 PHP 原理讲解；先知 musl 细节成条。KeyMint / keybox 主帖仍热，正文不重复；FreeBuf 405；嘶吼 Feed 陈旧。

## 1. 看雪｜ROP 游戏安全边界探索【2】：notepad 里弹 MessageBox

约 1 天前编程技术区：作者 **hawkeye\_Leo** 放出四篇系列第 2 篇《ROP · 游戏安全相关技术边界探索》。本期在 **notepad.exe** 上演示用 ROP 链弹出 MessageBox，并在用户确认后安全结束进程；对照常规 ShellCode「随便用栈」与 ROP「只能借现成 gadget」的差异。系列后

续预告游戏安全能力边界与反作弊检测思考。本条只记系列定位与演示目标，不复述 gadget 构造与注入步骤。

来源

```
https://bbs.kanxue.com/thread-293304.htm
```

**工地点评：**MessageBox 是教学向「能跑起来」的里程碑，不是外挂说明书。先搞清 ROP 与 ShellCode 谁在控栈，再谈后面游戏边界篇。

## 2. 看雪｜零依赖 tracefs uprobe：Flutter 加固流量怎么摸

约 1 天前逆向工程区：作者 **择势** 记录对某易盾级加固 Android App 的流量分析——代理抓包、Frida attach、静态补丁与 r0capture 一类方案在目标上纷纷失效。文中拆出两条独立网络通道：首页/登录走 OkHttp→系统 conscrypt；核心行情走 Dart `HttpClient`→libflutter 内嵌静态 **BoringSSL**（自带 CA、不理系统代理）。后续改走 **tracefs uprobe**、不依赖额外内核模块。本条只记「双通道 + 零依赖观测」新闻摘要，不提供绕过加固或抓包复现步骤。

来源

```
https://bbs.kanxue.com/thread-293295.htm
```

**工地点评：**Flutter 内嵌 BoringSSL 一出，系统代理和证书库就成摆设。合规检测先确认流量走哪条栈，再谈要不要动 uprobe。

## 3. 看雪｜打开 Mirai 源码：从 main.c 看公开结构

约 1 天前二进制漏洞区：作者 **git\_33582SilentSobs** 把公开仓库 **jgamblin/Mirai-Source-Code** 当新手读码练习，从 `main.c` 入口讲起，并按文件职责梳理 scanner / killer / attack / table 等模块分工。文中强调「自己 clone 打开看」，属于**公开恶意软件源码结构学习**。本条只保留模块划分与学习取向，不复述扫描、爆破或攻击逻辑，也不提供任何利用菜谱。

来源

```
https://bbs.kanxue.com/thread-293300.htm
```

**工地点评：**读公开 bot 源码是为了认结构、做防御对照，不是抄作业。近窗 PHP2Shell→Mirai 扫描浪再吵，也别把学习帖当成武器化手册。

## 4. Seebug｜nokast-secureRAG：小模型做 RAG 提示注入检测

Seebug Paper **2026-10-23 16:33（北京时间）** 上架译文/导读：**nokast-secureRAG**（作者 Abhishek Rai；原文 arXiv:2610.28364）。面向本地 RAG 流水线，讨论用约 0.5B 参数小语言模型做上下文感知的提示注入检测，覆盖间接提示注入与检索投毒等风险。本号只记论文议题与出处，不评价检测效果，也不提供绕过思路。

来源

```
https://paper.seebug.org/3529 https://arxiv.org/abs/2610.28364
```

**工地点评：**本地 RAG 一火，投毒和间接注入就跟着来。小模型护栏能不能扛住，先看威胁模型再塞进产品。

## 5. Seebug｜PHP「核弹」原理讲解：补丁后再谈机制

Seebug Paper **2026-10-23 15:22（北京时间）** 转载 **Laruence** 原理文：在官方补丁落地后，梳理近窗 PHP 引擎级 RCE（社区称 PHP2Shell / CVE-2026-109618 等）的公开机制——请求触发异常退出路径时跳过正常清理，留下可被后续复用的异常状态。本条**只作原理新闻摘要**：强调「先升补丁」，不复述 PoC、不写利用步骤、不贴攻击脚本链接。

来源

```
https://paper.seebug.org/3528
```

**工地点评：**原理文有价值，前提是补丁已出。运维党对版本号；别把「讲解」当成可复现菜谱往生产机试。

## 6. 先知｜musl：一串合法数字把 0 写到 x[-1]

先知近窗文讨论 **musl** libc 浮点扫描路径里的越界写：在解析一串「看起来合法」的数字时，可将 0 写到 `x[-1]`；社区指向相关上游修复提交（如 `dd856098` 一带），撰文时尚未见独立 CVE 编号。本条只记**缺陷现象与修复动向**，不讨论触发串构造与利用链。

来源

```
https://xz.aliyun.com/news/92995
```

**工地点评：**「合法输入」照样能打穿边界，libc 级细节最适合当 fuzz / 代码审计教材。嵌入式与 Alpine 系先跟上游提交，别等 CVE 号才动手。

补查：KeyMint / keybox 主帖仍热榜靠前，近窗已多次覆盖，正文不重复；VMP / SecShell / 定制 ROM 等昨已发；FreeBuf mobile 405；嘶吼 Feed 停滞；先知详情偶遇阿里云 WAF，Feed/缓存摘要可用。

PART 2

## 第二部分｜X 上的二进制 / 安全 / OS 逆向热点 + 越狱工具

含 iPhone Duo 首日越狱、Magisk 下版预告、fairplay-decrypt 离线能力边界，以及 Anthropic/Claude×REA、Codex 封号与免越狱定位代理；工具箱版本块附后。Ghidra 12.2、Dopamine 3.0.12、CleanYourTV 等近窗已发，不重复正文。

## 1. iPhone Duo｜开售首日被越狱：Calif · iOS 27.1 · 无终端工具

MacRumors **2026-10-23** 报道：黑客团队 **Calif** 在 iPhone Duo 开售数小时内完成 **iOS 27.1** 越狱演示（桌面图标弹跳、叠 anime 角色等）。团队未公开发布面向终端用户的越狱工具；Stefan Esser 对德媒称多数漏洞已披露或计划向 Apple 披露，且「多数」将在即将到来的 **iOS 27.2** 修复；开发过程使用了 AI 辅助，但未细说用法。X 上 **@mattjay** 等同步热传，并点出 Calif 与近窗 PHP 漏洞同源团队交叉。本条只记公开事实与时间线，不提供越狱包或复现步骤。

来源

```
https://www.macrumors.com/2026/10/23/iphone-duo-jailbreak/ https://x.com/mattjay/status/2113658683024462240
```

**工地点评：**首日演示≠能装的工具。等 27.2 公告与官方披露清单比追「哪天出包」靠谱；主力机别赌未公开洞。

## 2. Magisk｜下一版预告：Hexacon 延误 + HSUM 细碎破坏

**@topjohnwu** 于 **2026-10-24 01:00 UTC**（北京时间 09:00）发帖：下一版 Magisk 比预期久——原计划尽快跟上 Googlebook 支持，巴黎 **Hexacon** 行程拖慢进度；**Headless System User Mode（HSUM）** 又以大量细碎方式打断 Magisk，修复并不 trivial。作者称「事情终于进入不错的状态」，但**尚未挂正式 tag**。当前公开正式仍为 **v31.0**。

来源

```
https://x.com/topjohnwu/status/2113797829961666921 https://github.com/topjohnwu/Magisk/releases/tag/v31.0
```

**工地点评：**作者亲口预告 ≠ 今晚就能刷。HSUM 环境先别硬上 canary；等正式 Release 说明再动生产机。

## 3. fairplay-decrypt｜Mac/Linux 离线 FairPlay IPA 解密（公开能力边界）

仓库 **EthanArbuckle/fairplay-decrypt** 近窗持续推送：宣称可在 **Mac / Linux** 上对 App Store IPA 做**离线** FairPlay 解密，密钥推导相对独立；社区（如 **@qwerty\_\_cs**）热传其「旧机提取账号凭据 + 电脑侧解密高版本 App」的能力边界描述。本条**仅作公开能力与研究边界新闻**：用于理解 FairPlay 保护面与合规逆向研究场景，**不是盗版/破解安装指南**，不复述凭据提取或砸壳操作步骤。

来源

```
https://github.com/EthanArbuckle/fairplay-decrypt https://x.com/qwerty__cs/status/2113630688759132361
```

**工地点评：**研究 FairPlay 边界可以；拿去搬商店付费 App 就过线了。本号只记「能做什么」的公开说法，不写「怎么做」。

## 4. 社区称｜Anthropic / Claude × REA：安全拦截 ≠ 官方封杀

X 账号 **@xbquan** 等近窗转述 Reddit 讨论：有人让 Claude 搜集开源逆向项目 **REA** 资料并写入门指南，资料搜完、指南写到一半触发安全审查拒绝继续。社区叙事出现「Anthropic 悄悄掐断 REA」等阴谋论；转述帖强调**拒绝生成 ≠ 官方针对项目封杀**，更可能是逆向关键词触发护栏误杀。本条明确标注**社区称 / 报道口径**，非 Anthropic 官方公告。

来源

```
https://x.com/xbquan/status/2113774975375024491
```

**工地点评：**护栏误杀和「官方针对性削弱」不是一回事。真要稳定用 AI 做 RE，本地可控流水线比赌云端关键词名单靠谱。

## 5. OpenAI Codex｜因「做逆向」封号争议

**2026-10-23**，Codex 用户 **@log4j** 连发自述：OpenAI 以从事逆向工程为由封号；当事人称仅本地做逆向、未挖洞、未做渗透。社区转述（如 **@chenYijl**）指出：OpenAI 自家安全向产品 Daybreak 条款允许「授权逆向」，封号前还有过安全提示——官方回应口径里「安全提示不算违规结论」，但账号仍未解封。本条记**政策张力与社区争议**，不作站队结论。

来源

```
https://x.com/chenYijl/status/2113773491396976775
```

**工地点评：**条款写「授权可做」和实际风控怎么判，中间还有一道灰。白帽/研究者用云端 agent 前，先看清自己账号的使用边界。

## 6. iOS Location Spoofer｜免越狱：代理改写 Wi-Fi/基站定位

开源仓库 **xweiba/location-spoofer** 定位为 iOS 定位服务行为研究与开发测试工具：支持地图选点、本地/第三方代理、WGS-84 / GCJ-02，以及环境检测与问题诊断。公开讨论口径强调**免越狱**、通过代理改写 Apple 网络定位（Wi-Fi / 蜂窝）响应，而非改 GPS 硬件；对部分系统版本与证书策略有已知限制。本条只记公开能力边界，不作安装或滥用教程。看雪近窗 xenoid 云手机方案（thread-293175）备选未上正文。

来源

```
https://github.com/xweiba/location-spoofer https://x.com/tantanyuli/status/2113785290926227781
```

**工地点评：**网络定位能骗、硬件 GPS 不一定跟——测 App 风控可以，别指望「全系统伪定位一键通杀」。合规测试机专用。

## 工具箱补充｜版本与窗口内更新

和今天新闻相关的工具，版本信息以官方页面为准。无新正式 tag 的也列一行，方便对照；Magisk 下版仅预告、未挂 tag。

**Magisk v31.0**（正式仍此 tag；下一版作者预告中）

* 正式 tag 相对昨日无新版本；@topjohnwu 今日预告下版（HSUM / Googlebook），尚未发版。
* 官方：
* https://github.com/topjohnwu/Magisk/releases/tag/v31.0

**Frida 17.24.3**（动态插桩，2026-10-19）

* 相对昨日无新版本。
* 官方：
* https://frida.re/news/2026/10/19/frida-17-24-3-released/

**Dopamine 3.0.12**（iOS rootless 越狱，2026-10-20）

* 相对昨日无新版本。
* 官方：
* https://github.com/opa334/Dopamine/releases/tag/3.0.12

**palera1n v3.0.0-beta.3**（checkm8 系越狱工具，prerelease，2026-10-18）

* 相对昨日无新版本。
* 官方：
* https://github.com/palera1n/palera1n/releases/tag/v3.0.0-beta.3

**KernelSU v3.3.1**（Release 2026-10-12）

* 正式 tag 相对昨日无新版本。
* 官方：
* https://github.com/tiann/KernelSU/releases/tag/v3.3.1

**APatch 11282**（2026-10-15）

* 相对昨日无新版本。
* 官方：
* https://github.com/bmax121/APatch/releases/tag/11282

**Ghidra 12.2**（NSA 逆向框架，2026-10-22；昨已正文）

* 相对昨日无新版本；昨已主条，今日仅工具箱对照。
* 官方：
* https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra\_12.2\_build

**LSPosed**：稳定版仍为 v1.9.2；相对昨日无新版本。JingMatrix/Vector 仍 canary-3112。jadx 仍 v1.5.6。TrollStore 仍 2.1.1：窗口内无相对昨文的可单独成条新版本。

PART 3

## 第三部分｜事件热点

优先供应链与运行时根因补丁；LiteLLM / Node Brotli / Ghidra 12.2 昨已主条，今日不重复。GitLab CVSS 10 近窗已写，今日从 Ruby Onigmo 根因侧补新角度。

## 1. OVHcloud CLI｜GitHub Release 被劫持：五版归档短窗投毒

OVHcloud 官方顾问 **GHSA-862f-55f5-vmvw** 与多家媒体确认：**2026-10-19** 约 94 分钟窗口内，遭窃的贡献者 GitHub 账号替换了 **ovhcloud-cli** 既有 Release（v0.11.0–v0.15.0）上的多架构归档，植入窃密构建；源码、tag 与构建流水线未改，根因是未开启 GitHub Release 不可变。官方当晚推出干净 **v0.16.0**（不可变 + 签名 tag），并建议窗口内安装/升级者轮换本机可读密钥。本条不讨论恶意样本细节与复现。

来源

```
https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw https://thehackernews.com/2026/10/hackers-hijack-five-ovhcloud-cli.html
```

**工地点评：**Release 能被事后换文件，就等于供应链后门。公共仓库赶紧开 immutability；装 CLI 务必 pin 哈希，别裸 curl | sh。

## 2. Ruby｜Onigmo 三洞紧急补丁：撑起近窗 GitLab CVSS 10

Ruby 放出 **4.0.9 / 3.4.12 / 3.3.13**，修复内置正则引擎 **Onigmo** 三处缺陷。媒体与官方说明：这些缺陷正是近月 GitLab 连续高危/满分 RCE（含 CVSS 10）的根因侧——在编译攻击者可控正则时可能破坏内存。影响面不限 GitLab：任何把不可信字符串交给 `Regexp.new` / 插值进模式的应用都在范围内；仅使用开发者写死正则的应用不受影响。Ruby 暂未自请 CVE，建议跟踪 GitLab 相关 CVE 号并升级解释器。本条不讨论触发模式与 PoC。

来源

```
https://thehackernews.com/20...