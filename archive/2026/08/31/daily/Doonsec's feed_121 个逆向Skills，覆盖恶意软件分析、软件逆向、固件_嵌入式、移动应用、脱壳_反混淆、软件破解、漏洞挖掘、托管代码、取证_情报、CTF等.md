---
title: 121 个逆向Skills，覆盖恶意软件分析、软件逆向、固件/嵌入式、移动应用、脱壳/反混淆、软件破解、漏洞挖掘、托管代码、取证/情报、CTF等
url: https://mp.weixin.qq.com/s/JOROH30bMRhdNzPraHO_UA
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:59:18.159700
---

# 121 个逆向Skills，覆盖恶意软件分析、软件逆向、固件/嵌入式、移动应用、脱壳/反混淆、软件破解、漏洞挖掘、托管代码、取证/情报、CTF等

# 121 个逆向Skills，覆盖恶意软件分析、软件逆向、固件/嵌入式、移动应用、脱壳/反混淆、软件破解、漏洞挖掘、托管代码、取证/情报、CTF等

dslsdzc
dslsdzc

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## Rev-Skills介绍

121 个逆向工程技能，覆盖恶意软件分析、软件逆向、固件/嵌入式、协议逆向、移动应用、脱壳/反混淆、软件破解、漏洞挖掘、托管代码、取证/情报、CTF。**通用、可发布**：不假设用户已装任何工具，每个技能自带跨 OS 安装指引。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibL3bOeESMILx31hKFl0JP2oQn3Rroxwze4yoJajweI4Cef3tzibnwnuUu8OmsFfibV998zqMpHpGsGvDR0Wn0zTbbHkeciclMtHSkjcZs2ExI/640?wx_fmt=png&from=appmsg)

## 安装（三种方式）

### 方式一：npx（推荐，支持 7 种 AI 工具）

> 方式一自建安装器额外处理 Cursor / Copilot / Windsurf 的规则聚合（.mdc / 说明文件），这是标准 skills CLI 没有的能力；只装 Claude Code 系可用方式二。

```
npx rev-skills install                     # 交互式，默认 Claude Code
npx rev-skills install --target all        # 安装到全部 7 种工具
npx rev-skills install --target cursor     # 生成 Cursor 规则
npx rev-skills install --target gemini     # Gemini CLI 原生技能
npx rev-skills install --global            # 全局安装
npx rev-skills install --project           # 仅当前项目
npx rev-skills install --dry-run           # 只看计划不安装
npx rev-skills uninstall                   # 卸载
```

### 方式二：标准 skills CLI（agentskills.io 兼容）

本库遵循 Agent Skills 规范，可被任意兼容运行时（Claude Code / Codex / Cursor / Gemini CLI 等 50+ 工具）直接发现与安装：

```
npx skills add dslsdzc/rev-skills          # 项目作用域（.claude/skills/）
npx skills add dslsdzc/rev-skills -g       # 全局（~/.claude/skills/）
npx skills add dslsdzc/rev-skills -l       # 先列出技能，不安装
```

### 方式三：手动拷贝

把 `.claude/skills/` 下的技能目录复制到 `~/.claude/skills/`（Claude Code）或对应工具目录。

### 方式四：Claude Code 插件市场

本仓库自带 `.claude-plugin/marketplace.json`，可作为自托管插件市场直接添加：

```
/plugin marketplace add dslsdzc/rev-skills
/plugin install rev-skills
```

（若同名插件来自多个市场，用 `rev-skills@rev-skills` 消歧。）

## 多工具适配

| 工具 | 安装方式 | 体验 |
| --- | --- | --- |
| Claude Code | `--target claude` | 原生技能（按需加载） |
| Gemini CLI | `--target gemini` | 原生技能 |
| Cline | `--target cline` | 原生技能（兼容） |
| Codex CLI | `--target codex` | 原生技能 |
| Cursor | `--target cursor` → `.cursor/rules/*.mdc` | 规则聚合（知识+流程，无按需加载） |
| GitHub Copilot | `--target copilot` → `.github/copilot-instructions.md` | 规则聚合 |
| Windsurf | `--target windsurf` → `.windsurf/rules/*.md` | 规则聚合 |

## 技能导航（121）

入口 → 12 大类网关 → 108 原子技能，详见 `.claude/skills/` 与 `docs/skill-template.md`。快速索引：

* **re-analyze**：入口（探测 → 偏好 → 识别 → 编排）
* **re-binary-core**：re-address-space（地址换算）、re-triage、re-format-pe/elf/macho、re-imports、re-ghidra、re-ida、re-radare2、re-gdb、re-x64dbg、re-lldb、re-tracing、re-memdump、re-windbg、re-binaryninja、re-emulation、re-shellcode、re-kernel、re-ebpf、re-game、re-console、re-go、re-rust、re-plugin-dev、re-hypervisor、re-anti-cheat、re-cpp-abi、re-swift、re-zig、re-nim、re-fp-runtime、re-variant、re-mips、re-arm、re-riscv
* **re-malware**：re-sandbox、re-behavior、re-ioc、re-ransomware、re-loader、re-fileless、re-doc-malware
* **re-firmware**：re-fw-extract、re-fw-rootfs、re-fw-emulate、re-hardware-io、re-automotive、re-uefi、re-rtos、re-tee
* **re-protocol**：re-netcap、re-proto-rev、re-crypto-id、re-crypto-keys、re-crypto-decrypt、re-ics、re-iot-proto、re-whitebox、re-tls
* **re-mobile**：re-apk、re-ios、re-frida、re-frida-script-author、re-mobile-pack、re-hybrid-app、re-android-native、re-android-crypto（加密审计）、re-ios-jb、re-flutter、re-harmonyos
* **re-anti-analysis**：re-packer-id、re-unpack-simple、re-unpack-advanced、re-deobfuscate、re-evasion
* **re-cracking**：re-license、re-patching、re-keygen、re-drm
* **re-vuln**：re-fuzzing、re-crash-triage、re-exploit
* **re-ctf**：re-angr、re-z3、re-pwn、re-stego
* **re-managed**：re-dotnet、re-java、re-script-deob、re-wasm、re-ai-triage（AI 分流）→ re-ai-model、re-ai-attack、re-blockchain、re-python、re-browser-ext、re-electron、re-javacard
* **re-forensics**：re-mem-forensics、re-disk-forensics、re-ti、re-attribution、re-hunting、re-mobile-forensics
* **re-macos**：macOS 应用逆向（签名/entitlements/Secure Enclave）
* **re-hw-chip**：芯片/PCB 物理层（decap/裸片/木马检测）
* **re-ai-attack**：模型安全评估（行为层：提取/指纹/成员推断/对抗）
* **re-sdr**：射频逆向（采集/解调/帧恢复）
* **re-feedback**：经验反馈元网关——三源收集（会话复盘/文章扫描/手动输入）→ 蒸馏脱敏 → 归域 → 三档处理（发表 issue / 本地入库 / 不入库），re-analyze 第四步挂钩

## 工具获取

点击关注下方名片进入公众号

回复关键字【260831】获取下载链接

## 往期精彩

[一款开源的私有化企业级代码审计Bot平台，基于OpenCodeReview+CodeGraph+Gitlab

2026-08-25

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKibNxuJazfxUtia6ASBFFYpAc2cQVPL9zQ5aCBdavQXj9BQOYx8eUoYpj9Pbx97zUON7IvAXTYNKibibfNwsibrCa0dSUIsaic5EkHI/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497475&idx=1&sn=f658a2a6088b8505347f8017bbc0880c&scene=21#wechat_redirect)[Nuclei 漏洞扫描图形化工具 更新v2.6.0！支持 POC 管理、资产搜索、AI 辅助分析

2026-08-24

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLZm2zrKv3QA4LZQ8jNUsItdAkIb9k1uTnVenZRcstd2nKhZcA6zob1iaXyuwMbvSRlzc2dKD9JpmWX4icehBUqMwKqCYhF1b2Mo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497466&idx=1&sn=0c43688812f678e04799fa4e352201ec&scene=21#wechat_redirect)[协奏于攻守之间 | AI 原生渗透测试 IDE，让人与智能体共用浏览器、终端、流量、资产图、任务、证据和控制权

2026-08-21

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMICI0tzj7WJNdO3kicbK9F7flZCNtZx0OticoKVJB4EnyS8ZZTZfvDG3uG4qDIUkwCqgDVUlMQbbPRAZgviaB3gQiayDs43TcRPQzo/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497457&idx=1&sn=e82263bf6b59ab846bddbfeb26dcd952&scene=21#wechat_redirect)[DeepSeek Harness（dsh）渗透测试模式

2026-08-20

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMKW3YnCRicSI4YRFbUHODRxIs0w2TVnkH6rjvley3rZgPW31u5xPlkibYltTZKfgOQEy3W8Oz5iap6ickcS5oEteUibRgzozibJRKswE/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497439&idx=1&sn=f676e33d8cbcfce919ab0456dc62525f&scene=21#wechat_redirect)[Forgex 是一款面向 Windows 平台的集成式AI渗透测试工具箱

2026-08-19

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMLh10vHv22CYhicZR2BI5vEicd0l9BwxUR9ePnAavybniaXEzh9TY9dtSh2rFujS01rfDcQBT7XeV1EbnT8ssqNfvVcr3bSoN6DqM/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497416&idx=1&sn=8cdab12f4c63821bcd715246da32624a&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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