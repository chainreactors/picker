---
title: SpecterAI V1.5 单兵作战系统正式发布
url: https://mp.weixin.qq.com/s/zE6rPde_ZHEMMB2W2CzD6w
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T05:00:57.770678
---

# SpecterAI V1.5 单兵作战系统正式发布

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bFTREXgyd3ln0eDhhFAbhmIlf9lbLEFCEsjAaF8Gt7Zen7V5hfYVWYSib7VDwH0JW097ytciaT6SHq0Xkrbm3LyWRsuRRzCXEqU4yX1YxXcts/0?wx_fmt=jpeg)

# SpecterAI V1.5 单兵作战系统正式发布

暗魂安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于暗魂攻防实验室
，作者暗魂攻防实验室

![](https://wx.qlogo.cn/mmhead/ps68icnpRvDVyT8kUQpG3Bo6ysUsspzN43YThicz37d8ETv46iaU0mQ9ezeiakqjZ2RIsKMdQDiazb5E/0)

**暗魂攻防实验室**
.

专注于网络空间安全、红蓝攻防对抗、渗透测试等技术研究

**点击蓝字**

![](https://mmbiz.qpic.cn/mmbiz_png/3XHJ1RF0NSYd27sBeQmXABLOsqiayvFsaHAAOUaaeqc9gNiazSc9n8ibSt2gdwPoulFeDR4ZXASzg57pJIARz0EnA/640?wx_fmt=png)

**关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/3XHJ1RF0NSYd27sBeQmXABLOsqiayvFsavTcCgm5F810vclCaGZbMgbDpU4rSNlTP51AkNUwicvu4OGGLVsud1Gw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3XHJ1RF0NSaWvWVF36nYELAlKM2WANEP5bwNmELpJuyWctlEwWGAZ0RcmXzlNEaqeLexVsDnRClqibHOkdqjibfg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/3XHJ1RF0NSYd27sBeQmXABLOsqiayvFsaWkNjEibIVG6YffQIdZo2JYSOWv442U1EGjMS5LTHLIJ8p0wpoVVuTWw/640?wx_fmt=png)

**微信搜一搜**

![](https://mmbiz.qpic.cn/mmbiz_png/3XHJ1RF0NSYd27sBeQmXABLOsqiayvFsablP5UibgCDRewJkbqAyjs9icIklxN2eGcE8Ve6RqOmOcV2uXtmL3whnA/640?wx_fmt=png)

暗魂攻防实验室

# **AI 赋能 · 开箱即用 · 重新定义红队渗透**

---

## **📌 导语**

各位网络安全爱好者、红队工程师、CTF 选手们，大家好！

还在为搭建渗透环境时无尽的依赖报错而抓狂？还在羡慕别人拥有"AI 副驾驶"却苦于不会配置？

今天，**暗魂攻防实验室** 带着诚意满满的升级之作 —— **SpecterAI V1.5 单兵作战系统**，来彻底解放你的生产力！

我们基于最新的 **Kali-Linux 2026.1** 深度定制，为你打造了一个 **开箱即用、AI 原生** 的顶级渗透攻防作战环境。无论你是 CTF 选手、渗透测试工程师，还是安全研究员，这套系统都将让你如虎添翼。

---

## **🧐 关于 SpecterAI**

**SpecterAI 单兵作战系统** 由暗魂攻防实验室精心打造，基于 Kali-Linux 2026.1 版本深度修改，围绕 **AI 安全** 为核心目标进行制作。旨在为广大网络安全爱好者提供一套 **零配置、开箱即用** 的渗透攻防作战环境。

| **项目** | **详情** |
| --- | --- |
| **操作系统** | Kali-Linux VMware (2026.1) |
| **内核版本** | Linux 6.19.14+kali-amd64 |
| **默认账户** | `root / root` |
| **分区大小** | 100G |
| **软件源** | Kali 官方源 + 阿里云国内源（可选） |
| **输入法** | fcitx5（左 Shift 切换中文） |

---

## **🚀 核心亮点**

### **一、AI 工具生态，武装到牙齿**

我们深知 AI 对网络安全的颠覆性意义。SpecterAI V1.5 集成了当前最硬核的 AI 武器库：

#### **1️⃣ HexStrike-AI**

* **路径**：`/root/hexstrike-ai/`
* **启动**：桌面一键启动器 / `hexstrike_server --debug`
* **端口**：`127.0.0.1:8888`
* 自带 Browser Agent，需要 Chrome/Chromium 环境支持
* 配合 Cherry Studio 使用，调用预创建的 AI 助手即可上手

#### **2️⃣ CyberStrike-AI**

* **路径**：`/root/CyberStrikeAI/`
* **启动**：桌面一键启动器 / `./run.sh`
* **访问**：`https://127.0.0.1:8080/#dashboard`
* 可结合 HexStrike 的 MCP 协议协同使用
* 支持连接各大厂商大模型（推荐小米 MiMo V2.5）

#### **3️⃣ Claude Code + CC Switch**

* Claude Code 已安装并配置完毕，CC Switch 开机自启
* 一键路由代理到国内大模型，告别网络烦恼
* 支持多种权限模式：

+ `acceptEdits`：自动批准文件编辑
+ `auto`：智能自动模式
+ `dangerously-skip-permissions`：危险模式（完全放开）

#### **4️⃣ Strix（V1.5 新增 🆕）**

全新安全扫描利器，支持多维分析：

```
# 本地代码分析
strix --target ./app-directory

# GitHub 仓库分析
strix --target https://github.com/org/repo

# 在线应用动态测试
strix --target https://your-app.com

# 多目标白盒测试
strix -t https://github.com/org/repo -t https://your-app.com

# 批量目标扫描
strix --target-list ./targets.txt
```

---

### **二、大师级 Skills，覆盖全场景**

SpecterAI V1.5 预装了 **6 大核心 Skills 模块**，让 AI 成为你最得力的安全助手：

#### **🔴 secskills — 自动化渗透测试**

```
/secskills
```

输入目标（IP / 域名 / URL + 端口），即可启动全自动渗透测试流程。覆盖信息收集、漏洞扫描、利用、后渗透的完整链条。

#### **🔵 code-audit — 智能代码审计**

```
/code-audit deep /path/to/project
```

全面覆盖 OWASP Top 10 十大维度：

| **维度** | **名称** | **覆盖内容** |
| --- | --- | --- |
| D1 | 注入 | SQL / Cmd / LDAP / SSTI / SpEL / JNDI |
| D2 | 认证 | Token / Session / JWT / Filter 链 |
| D3 | 授权 | CRUD 权限一致性、IDOR、水平越权 |
| D4 | 反序列化 | Java / Python / PHP Gadget 链 |
| D5 | 文件操作 | 上传 / 下载 / 路径遍历 |
| D6 | SSRF | URL 注入、协议限制绕过 |
| D7 | 加密 | 密钥管理、加密模式、KDF |
| D8 | 配置 | Actuator、CORS、错误信息暴露 |
| D9 | 业务逻辑 | 竞态条件、Mass Assignment、状态机 |
| D10 | 供应链 | 依赖 CVE、版本检查 |

#### **🟢 Reverse Engineering — 安卓逆向工程**

```
/decompile path/to/app.apk
```

支持 JavaScript、Android APK、iOS 应用等逆向分析。集成 Camoufox、IDA Pro 等工具，提供完整的逆向工作流与漏洞挖掘能力。

#### **🟡 ctf-skills — CTF 夺旗神器**

```
/solve-challenge /path/to/challenge.zip
```

支持 URL 或附件输入，自动识别题目类型并解题。WiFi 取证、Web 渗透、密码学……一句话让 AI 帮你拿 Flag。

#### **🟣 Claude-Red — 58 个红队专家技能**

由独立安全研究团队 **SnailSploit** 精心打造，覆盖 **13 大安全领域** 的 58 个结构化 SKILL.md 文件。当你提到 SQL 注入时，Claude 自动加载 SQLi 专家技能；当你讨论 AD 域渗透时，它瞬间切换到 Active Directory 攻击专家模式。

> GitHub：https://github.com/SnailSploit/Claude-Red

#### **⚫ Cybersecurity-Skills — 817 项结构化技能**

覆盖 **29 个安全领域**，每项技能均映射到六大行业框架：

* ✅ MITRE ATT&CK
* ✅ NIST CSF 2.0
* ✅ MITRE ATLAS
* ✅ MITRE D3FEND
* ✅ NIST AI RMF
* ✅ MITRE 反欺诈框架（F3）

> 这是目前唯一一个具有统一跨框架覆盖范围的开源技能库。

---

### **三、系统环境优化**

#### **🔧 基础工具链**

| **工具** | **版本** |
| --- | --- |
| Docker | 29.5.2 (build 79eb04c) |
| Docker Compose | v5.1.4 |
| Chrome | 148.0.7778.215 |
| ChromeDriver | 148.0.7778.178 |
| IDEA | 2026.1（已激活至 2099 年） |

> ⚠️ 注意：`docker compose` 不是 `docker-compose`，使用时请注意空格。

#### **🧹 系统清理**

内置 **BleachBit**，终端输入 `bleachbit` 即可启动图形化界面，一键清理缓存垃圾。

#### **🌐 网络代理**

桌面集成 **Clash Verge**，双击即可打开。终端使用梯子需开启虚拟网卡模式。

---

## **📅 版本迭代历程**

### **V1.5 正式版（2026年7月26日） 🆕**

* ✅ 系统环境优化：更新 Kali 源
* ✅ 软件更新：Claude → V2.1.220、CC Switch → 3.18.0、Hermes → 0.19.0
* ✅ 软件新增：**Strix**
* ✅ Skills 新增：**Claude-Red**、**Cybersecurity-Skills**

### **V1.4 正式版（2026年7月4日）**

* ✅ 优化 vmtools 功能
* ✅ Claude → V2.1.201（桌面图标 + 自动审批）
* ✅ CC Switch → 3.16.5、Hermes → 0.18.0、CyberStrike-AI → V1.6.50

### **V1.3 正式版（2026年6月18日）**

* ✅ Cherry Studio → V1.9.11、Claude → V2.1.181
* ✅ 新增 Hermes（附带安全 Skills）
* ✅ 新增 Skill：ctf-skills

### **V1.2 正式版（2026年6月12日）**

* ✅ 修复 CC GUI 在 root 模式下无法使用的问题
* ✅ 修复 Claude Code 报 `zsh: segmentation fault` 错误

### **V1.1 正式版（2026年6月5日）**

* ✅ 安装 Kali 完整版工具集
* ✅ 新增桌面快捷启动：HexStrike & CyberStrike
* ✅ 首次集成 Claude Code + CC Switch（含 3 个 Skills）

---

## **🎁 特别福利：小米 MiMo V2.5 大模型**

在 CyberStrike-AI 中，你可以使用 **小米 MiMo V2.5** —— 小米迄今最强模型，应对严肃复杂的专业安全任务。

> **粉丝专享邀请码：`ZUYUC7`**
>
> 仅 20 位名额，双方各得 ¥10 体验金，体验金 40 天有效。

注册后请在控制台左下方入口填写邀请码即可解锁全系模型。

---

## **📥 获取方式**

关注我们的官方渠道，获取 SpecterAI V1.5 系统镜像及完整使用文档！

| **渠道** | **信息** |
| --- | --- |
| 📱 微信公众号 | **暗魂攻防实验室**（anhunsec-red） |
| 🌐 官方网站 | https://www.anhunsec.cn |
| 💬 微信客服 | anhunsec\_kf |
| 📧 官方邮箱 | anhunsec@126.com |

---

## **📝 使用小贴士**

1. **首次登录**：账户 `root`，密码 `root`；普通用户 `kali / kali`（已锁定，可按需解锁）
2. **切换软件源**：编辑 `/etc/apt/sources.list`，切换为阿里云源可加速国内更新
3. **HexStrike 远程连接**：如需物理机连接虚拟机 MCP，修改 `API_HOST` 为 `0.0.0.0`
4. **Hermes WebUI**：从 CC Switch 右上角打开，终端不可关闭，浏览器访问 `127.0.0.1:9199`
5. **模型热切换**：修改 CC Switch 配置后需重启 Hermes 进程生效

---

## **🎯 适用人群**

* 🏅 **CTF 选手**：`/solve-challenge` 秒解赛题，`ctf-skills` 全方位辅助
* 🔴 **红队工程师**：Claude-Red 58 个专家技能，覆盖全攻击链
* 🔵 **安全研究员**：817 项结构化技能 + AI 代码审计，效率倍增
* 🟢 **逆向分析师**：APK 反编译 + IDA Pro 工作流，一键启动
* 🟡 **企业安全团队**：开箱即用的标准化渗透环境，降低搭建成本

---

## **🔚 结语**

暗魂攻防实验室，致力于为网络安全爱好者提供最硬核的技术支撑。

**SpecterAI V1.5** —— 让你的 Kali 拥有 AI 大脑，奔赴下一场攻防战斗吧！

> ⚠️ **免责声明**：本系统仅供授权范围内的网络安全测试、学习研究使用。使用者需遵守《网络安全法》等相关法律法规，严禁用于任何非法用途。由此产生的任何法律后果由使用者自行承担。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bFTREXgyd3mOcyC9Qu7eGQyy81gaePT1ZZIt1kzHjUibZkPFB8hAvHmvLl7WahetDJd2JCCzFsxlAvzPujjicQMb6agTQ4LKYZS0ryZS831qU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/3XHJ1RF0NSYUpNtNsWQe2XHahYNEwEOUdy9HXnc3zibSJTia1MMca7hlnVa6ngzfMVhnFPSUY8qvH2xHZuuZMDGg/640?wx_fmt=png)

**联系微信客服**

扫码联系

暗魂攻防实验室

![](https://mmbiz.qpic.cn/mmbiz_png/3XHJ1RF0NSaWvWVF36nYELAlKM2WANEPrJoC1peYbF3yta2sMuZSibL0wgonX2W3DEhNpvPN0mr392FTXB2PV7Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7IHABFmuMlWQkSSzOMicicfBLfsdIjkOnDvssu6Znx4TTPsH8yZZNZ17hSbD95ww43fs5OFEppRTWg/640?wx_fmt=gif)

●[【实战派推荐】提升渗透效率的2款工具](https://mp.weixin.qq.com/s?__biz=MzkyMjE1NzQ2MA==&mid=2247490758&idx=1&sn=a11ba2a7181ad1c42115bc305e8a24f2&scene=21#wechat_redirect)

●[anhunsec\_anfu\_V5.0红队单兵武器库介绍](https://mp.weixin.qq.com/s?__biz=MzkyMjE1NzQ2MA==&mid=2247490743&idx=1&sn=536f33008caf16fcf9b338fc8ac3fb1f&scene=21#wechat_redirect)

●[UDSCTF：UDS 协议安全挑战](https://mp.weixin.qq.com/s?__biz=MzkyMjE1NzQ2MA==&mid=2247490710&idx=1&sn=a9ca4a44693e1c288916338f9a537b72&scene=21#wechat_redirect)

●[CVE-2023-22527复现实录：沉浸式攻防体验尽在CyberStrikeLab靶场](https://mp.weixin.qq.com/s?__biz=MzkyMjE1NzQ2MA==&mid=2247490708&idx=1&sn=e4f6a9830fda07759f1e650700...