---
title: chrome安全研究-让SI帮你calc
url: https://mp.weixin.qq.com/s/FMgKHiYyQsN5O13alc_rhA
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:41:01.717365
---

# chrome安全研究-让SI帮你calc

# chrome安全研究-让SI帮你calc

原创

鬼麦子
鬼麦子

鬼麦子

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

闲来无事，赚不到钱，但又有那么多免费的token，c2 免杀梯子什么的都自研做了，差个证书，用在哪也还没方向，所以研究下Chrome，我看很多兄弟都能稳定利用Chrome一些比较近的版本exp了，但是具体操作没人说，刚好这个对业界挺刚需的。

周知Chrome Nday流传出来的exp，这玩意换个Chrome版本，换个编译启动参数，就没法用了，因为内存变了，所以呢，这篇文章就是为了尽可能的解决这个问题，弹calc.exe为止。

还有我这不是让人用的，人来看思路，其实我懂个蛋，我只知道大概思路，agent负责看了我这篇文章后具体执行操作（直立猿已经退出历史舞台了，起码在执行层面，还得是si硅基智能）。

https://issues.chromium.org/issues?q=exp.js&s=priority:asc&s=created\_time:desc

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6PzM5g8GpohCMDtSic2H3MmN1kmVZpE8D5nMG7Zic9OTZMiaianhTJZ0GQzSria4Pa71hlR97We6qBnQ65pxwjnYOwVCYqeoIibkYKMA/640?wx_fmt=png&from=appmsg)

https://issues.chromium.org/issues?q=rce&s=priority:asc&s=created\_time:desc

是这样，Chrome那些cve漏洞，也就是流传出来的exp，他们的漏洞类型是不一样的，可能某个exp能打126-128   有的exp能打131-133 这种，所以就很麻烦，得研究不少的cve exp。

在搞这之前需要用到的工具与知识:

知识:

chromium也就是Chrome，v8也就是javascript的执行渲染引擎，很大一部分chromium的漏洞其实是v8的漏洞，内存型二进制漏洞，需要进行内存级的调试，比如反汇编 调进程内存什么的。

某个cve不会通杀所有，比如Windows x64的只能x64，32的只能32，**漏洞逻辑是内核 / 组件代码的逻辑 bug，但能不能稳定利用、能不能打出可控原语，极度依赖内存分配器、ABI、内存布局、保护机制、对象结构，这些东西 OS、架构、位数之间完全不一样**。比如有个cve的exp  明明能打133的windows x64 chromium，但是切换到Linux x64 chromium也不一定能打，具体怎么样，你在选cve和exp时得让agent判断下，不要浪费token。还有就是并不是是个Chrome，关了沙箱就直接打，还有v8沙箱，有的还有参数限制--js-flags=

如： --allow-natives-syntax 给你工具，手动控 GC、看对象、触发优化；--predictable 减少随机噪声，堆喷 / 占位每次跑尽量场景一致。这些需要特定参数才能触发，说实话实战效果有限。

工具:

1. agent工具，随便什么agent都可以，应该是这样。
2. chromium多版本，或者说多版本下载能力。
3. v8多版本，或者说多版本下载能力。
4. cdb.exe 动态调试
5. rabin2 静态分析
6. python
7. d8.exe（V8 Debug Shell）
8. 梯子你懂得
9. linux ssh连接 里面装个msf

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6MOwHp3R6yTu37Na2U0KDT3FyeaRhS6bibydWVK7TIddHF4h4oZdPfAMvEibmgNRXfeCS6CjBkf3DFibM4wl0iaecYOpAwpj4JRrTg/640?wx_fmt=png&from=appmsg)

示例从chromium100-140  每个版本随便挑了一个:

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6O093YDriaZfsaWRXV7QPwGictYEeYu7Gchcwfo22Idic24dq89VOAgA5pQzGt1TYN1JwQyE1p5VsKtglZzjDXWic2Spz00LTBZI5c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6NrccpoRiaG4B1nYUoanmMkicDjHY8bLribTLGMQ2InceYrLviaTaX1ibYwDQ4knlBLydF0YaL2AUcSxDZZQglQ04TR344aacXy3uj4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6MrCVSv2GtvN5ibKmgFPsMIoM49uRgRZlSlvxiaz1QttaXQ1sYa3fIKd3ScJ8RhibZHAiaC2MR80VtEoYCI3b1dHQ6JXWzicosy8yaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6NvnxlXNjPdcNCzCtyoRnFo0NSzgFTNH30wnNVAWNGNezogzW1kTpOia9AlvtrO151ibBk975jmD3DAaeCMbHDP1TL7iciazeGWg4U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6PmuEk8aLUNQhLmCFbzxV7uPfhVqfJ2SLq3E60QQaMAvFPPyM4q8LQS2m4edu48bTibIBHvbptoNq7ziaEpfgOkQVLTT6YdbHsSo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6Ob6txgGD6ZDolEz32OyVw0ibbmFcTfZDGiaNQv4UFD4dDCxjSIib6I00NicG1jbHYwfqBojNGxVj5icBljLKia6ltibpa9aPDDiclJcTg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6MHPDXUndkOJltM3mk3D5nKt7WPTSrTOye7VCkpk3VibZfLJ4V3FGh0tAicQiaHKTMcAHvgMaWbInyYpe2xlGINlnoJ8KHDL44K5c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6Oan57Dock2QNFW7RupycooS4Lqp44lUcAQN6qCnuqe7T4vWQpBrnJwKMcUzNb1GdHiaASiaJq2pOgz1yIqq3GgZK56YGtpcAgPE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6NXh2qSL93FCSfcicxOkr81LP4wmGY1uDDk0zia4vUMCbuxg2taudanNhLdc8OnLRW3Ug7ZE1QPfbMcfsqLrC4NziaLhr2lRUZGWA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6OUic81aFKAyZ85w5Ufl3eW52YlyZWdkVhUzJaKXY4C4AT0p17Ot4ictzvNL4BkZNp2hcRN3opicegicwibNHADwPbLsicnEEvTro8ick/640?wx_fmt=png&from=appmsg)

140打开计算器后闪退，抓不到合适截图  就这样意思下。

这是已经能calc的，agent调试好的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6MAH7eSr4H6ZsxgK38CoTx5b8kjEASRWLscM6E2tFfQjRkgFLibMJ3CB5oiaCqXM3sL6wY2RAicTbHEawQQOSasZVdickKuM6KPlDo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6NfKIC9HfG6Bw2wBmMLYI6HCBEcckXlqPEKt8LxM8k6ZwyVXbmoW3EJpibZ235WEiaaPlyZRPuzhn3J4BsQiaW3dtBjkUgg2v6Gicc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6Mu3KWQO7dZSU1CYqmiasiabeuicdF2PsibBpnCSnVnkq3YBxDGkXtq2hZuLsWEzEibY3tcSooMGeib2L0KLNVHF82Ouw1LjEy6KcBEc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/kCaGE674k6PkaT9mhbv0GaicibIg18O2W6w7sCzsWa8TtDLhwVau3N98C5nAuIUsGN2VwndYykRjLYKIvFKnB8iaM1cHiaDSvsJyZx2GAJgRlnY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kCaGE674k6MeWELJxnIAbdjKLbdOjavf1CbRM7MLMXriaYZalv1nyY7VcOBu4cJQw1Z99jVqbicwmrJBTDpbjKwl7ibthJBEskG3Ksib3E1w7FI/640?wx_fmt=png&from=appmsg)

其实我也看不懂，但并不妨碍calc

我不会发exp的，但是具体操作如下

让agent把这些总结了一套类似skill的md:

```
---name: chromium-exp-debugdescription: Windows 环境下，为指定版本 Chromium/V8 复现并调试公开漏洞 exp 的可移植流程。覆盖素材抓取、调试环境搭建、工具选择、调试方法论与交付验收标准。当任务涉及「复现历史 Chrome CVE」「给某个 Chrome/V8 版本做 exp 适配」「拿到任意读写/弹计算器」时使用。---
# SKILL — Chromium 指定版本 EXP 调试与交付（Windows）
> 面向换机器、换项目、换版本后仍需可用的通用作业手册。所有路径、版本、地址均为占位或示例，**按现场实测替换**。> 默认目标：在 Windows 上让公开 exploit 在**指定的历史 Chromium / V8 构建**上跑通，最终验收是**弹出计算器**（或等价的可观察代码执行）。
---
## 1. 触发条件与适用边界
**适用**- 已知某 CVE / issue 编号，要在本地某个历史版本 Chrome 或独立 V8（d8）上复现利用。- 已有一个 PoC，需要把它从「能触发崩溃」推进到「任意读写 → 代码执行」。- 需要判断「这个漏洞在我的构建上到底还在不在」，并给出可交付、可复验的产物。
**不适用**- 自研 0-day、免杀、真实目标攻击。- 无公开素材且不允许自研触发的场景（本手册不教你从零挖洞）。- 只想静态审计源码（可直接看补丁 diff，不必走本流程）。
**硬边界（先接受，能省大量时间）**- 安全 issue 从修复到公开约 **14 周**，所以**公开 N-day 永远落后当前 stable 约 3.5 个月**，打不了「当月最新 stable」。- 版本的 milestone 字段通常是**修复版本**，不是引入版本；不要拿它当「洞存在的版本」。- 已撤回的 CVE（introduced & fixed before Stable）没有可利用窗口，直接跳过。
---
## 2. 总流程
```① 定靶      选版本 + 架构（x86/x64）→ 记下完整版本号与 V8 版本② 找洞      抓 CVE / issue + exp + 附件 → 判定「窗口」③ 备环境    下载对应 chromium / d8 构建 → 固定目录规范④ 先验窗口  跑最小触发件，确认洞在（否则换素材，不调参）⑤ 标定      用调试器/打印拿到该构建的布局常量（堆地址、map、字段偏移）⑥ 接链      触发 → 任意 r/w → addrof/fakeobj → 代码执行⑦ 双线验收  d8 线 + 浏览器线，各自多次复现⑧ 交付      固定命名、双击可跑脚本、README、文档同步```
原则：**先判窗口，再做标定；窗口不对，任何调参都是白干。**架构选择经验：**优先 32 位（x86）**——无 V8 Sandbox、无指针压缩，地址是绝对 32 位，沙箱内任意读写直接等于进程内任意读写，链路最短。
---
## 3. 素材抓取（CVE / issue / exp）
### 3.1 信息来源（按可信顺序）
| 源 | 用途 ||---|---|| Chrome Releases 博客 | CVE 号 ↔ 受影响版本区间 ↔ 修复版本 || issues.chromium.org | 根因描述、复现步骤、正文里的 PoC 代码、附件 || chromium-review | 修复 CL → **父提交**即最后一个漏洞版本 || crrev.com/\<revision\> | revision ↔ 源码 commit || ChromiumDash | stable 版本 ↔ commit position / revision || 构建快照站 | 直接下历史 revision 的浏览器包 || V8 官方归档 | 直接下历史版本 d8（rel / dbg） |
### 3.2 检索捷径
- 公开安全 bug 的利用代码常**直接写在 issue 正文**，习惯命名 `exp.js` / `poc.js`：  `https://issues.chromium.org/issues?q=exp.js&s=priority:asc&s=created_time:desc`- 想要「自带完整利用」的素材，用 `q=rce`、`q=arbitrary read write`、`q=calc` 之类关键词。- **不要只看 Resources / 附件页**：那里多是截图，且常需登录；正文代码块才是 exp 正本。
### 3.3 取全文与附件的可用接口
```text# issue 全文（JSON，含正文与所有字段）GET https://issues.chromium.org/action/issues/<ISSUE_ID>
# 附件直下（多数无需登录）GET https://issues.chromium.org/action/issues/<ISSUE_ID>/attachments/<ATTID>```
附件落地统一改名：`a<attid>_<语义>.<ext>`，并在台账里记 attid，便于回溯与去重。
### 3.4 版本 ↔ 源码窗口判定
```text# DEPS 反查：取目标版本的 v8_revisionGET https://chromium.googlesource.com/chromium/src/+/refs/tags/<CHROME_VERSION>/DEPS?format=TEXT# 返回 base64，解码后找 v8_revision```
判定步骤：1. 从公告/issue 拿到**修复版本**。2. 本地构建版本号 **小于** 修复版本 ⇒ 大概率在窗口内（还要看该修复是否被 backport）。3. 用修复 CL 的父提交反证：漏洞代码在父提交存在、在修复提交消失。4. 交叉验证：issue 的 milestone 只是修复里程碑，不等于「引入版本」。5. 有疑问就跑**最小触发件**（见 §7.1），这是唯一可信判据。
### 3.5 素材台账（必须做）
每条素材记录：issue 号、CVE 号、优先级/状态、命题（一句话）、附件 attid 与大小、本地实测结论（成功/崩溃/无反应）、失败原因分类。**失败原因分类**的价值远大于「失败」二字：窗口不符 / 原语不完整 / 架构不成立 / 依赖特殊构建（fuzzer、simulator、sandbox）/ 需要沙箱逃逸。
---
## 4. 调试环境搭建
### 4.1 构建获取
```text# Chromium 历史快照（持续归档，不会随 stable 更新）https://commondatastorage.googleapis.com/chromium-browser-snapshots/Win_x64/<REVISION>/chrome-win.ziphttps://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/<REVISION>/chrome-win32.zip   # 32 位# 最新 revisionhttps://commondatastorage.googleapis.com/chromium-browser-snapshots/Win_x64/LAST_CHANGE
# V8 预编译 d8（覆盖近多年版本，rel/dbg 皆有）https://commondatastorage.googleapis.com/chromium-v8/official/<MAJOR>/v8-win32-rel-<V8_VERSION>.ziphttps://commondatastorage.googleapis.com/chromium-v8/official/<MAJOR>/v8-win64-dbg-<V8_VERSION>.zip# 目录列举https://commondatastorage.googleapis.com/chromium-v8/?list...