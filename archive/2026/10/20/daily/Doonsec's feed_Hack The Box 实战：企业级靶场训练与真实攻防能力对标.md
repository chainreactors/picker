---
title: Hack The Box 实战：企业级靶场训练与真实攻防能力对标
url: https://mp.weixin.qq.com/s/gkkSFxW1I9CxnT9tXnt4ZQ
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:47:31.106304
---

# Hack The Box 实战：企业级靶场训练与真实攻防能力对标

# Hack The Box 实战：企业级靶场训练与真实攻防能力对标

运维安全入门
运维安全入门

运维安全入门

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

上一章的 TryHackMe 和前几章的 Vulnhub 有一个共同点：它们都**刻意降低了初学者的门槛**——要么有引导，要么有路径，要么有提示。这是好事，但也有代价：你很难在上面遇到「真正困难」的问题。

**Hack The Box（HTB）** 是另一个极端。它没有学习路径，没有分级引导，只有一台机器、一个目标、以及**四种难度标签：Easy / Medium / Hard / Insane**——其中 Medium 以上的机器，基本上就是真实的渗透测试难度。

但 HTB 依然是最值得长期投入的靶场平台。原因有三：

1. **社区质量极高**

   ：全球渗透测试工程师的聚集地，高质量 writeup 数量远超 Vulnhub。
2. **机器贴近真实**

   ：大量机器取材于真实的攻防场景，包括企业内网、Active Directory 域环境。
3. **与职业直接相关**

   ：不少 HTB 机器被用作招聘时的技术考核题，通关 Pro Lab 则是圈内认可的能力证明。

**🛡️ 授权声明**　HTB 部分内容与机器需要订阅（VIP）。免费机器已足够入门，但 Medium 以上的深度训练通常需要订阅。

本文目录

1. Hack The Box 是什么，它的定位与差异
2. 账号体系：Free / VIP / Academy
3. 机器类型：Active、Retired、Pro Lab
4. 网络接入：Pwnbox 与 VPN 配置详解
5. 核心机制：难度、标签与徽章体系
6. 实战一：标准解题流程与 HTB 特色
7. 实战二：Retired 机器的实战复盘思路
8. 实战三：Pro Lab 与真实攻防对标
9. 实战四：Windows/AD 域机器专题
10. 常见问题与进阶技巧
11. 等保视角：把 HTB 能力引入企业
12. 总结

## 01Hack The Box 是什么，它的定位与差异

Hack The Box 成立于 2014 年，由两位英国渗透测试人员（多位资料提到其创始背景与 Rapid7 社区有渊源）创办，总部位于英国。它的定位非常明确：**面向已有基础、需要进阶挑战的渗透测试人员**。

### HTB 与其他平台的定位对比

| 维度 | TryHackMe | Vulnhub | Hack The Box |
| --- | --- | --- | --- |
| 定位 | 入门到初级 | 社区自制靶机 | 中高级进阶 |
| 引导 | 有学习路径 | 无 | 无 |
| 环境 | 云端为主 | 本地虚拟机 | 云端（需 VPN/Pwnbox） |
| 难度上限 | Medium | 看作者 | Insane |
| 内容来源 | 官方为主 | 社区投稿 | 官方 + 社区 + 合作方 |
| 社区 | 较活跃 | 以 writeup 为主 | 全球最大渗透社区 |
| 职业认可度 | 一般 | 一般 | 较高（招聘常用） |

**💡 提示**　从表中能看出一个清晰的递进关系：**TryHackMe 负责「入门」，Vulnhub 负责「实战经验」，HTB 负责「拔高」**。三者不是替代关系，而是针对不同阶段的不同工具。

#### HTB 的独特价值：机器的现实性

* **取材于真实事件**

  ：不少机器的漏洞和技术栈直接来自真实的攻防案例与 CVE。
* **技术栈现代**

  ：除了传统的 Linux 靶机，还有大量 Windows、Active Directory 域环境、以及云安全专题机器。
* **不只是「拿 flag」**

  ：很多机器需要横向移动、需要搭建跳板、需要处理真实的多机拓扑，*这与真实的红队行动高度相似*。

**界面说明** Hack The Box 首页按 Active / Retired / Starting / Free 分类展示机器。每张卡片包含机器名、难度星级、标签（web/rev/pwn/crypto/misc）、作者头像，以及已通关人数。筛选器可按标签与难度组合过滤。Retired 机器已下线但 writeup 仍可参考，适合作为免打靶的复盘素材；Free 档位无需订阅即可开机。

## 02账号体系：Free / VIP / Academy

HTB 的账号体系比 TryHackMe 复杂一些，理解清楚能避免很多误解。

| 类型 | 可访问内容 | 价格 | 适用人群 |
| --- | --- | --- | --- |
| Free | Free Machines、Starting Point、论坛 | 免费 | 入门与基础训练 |
| VIP | Active Machines、Retired、Writeups | 订阅制 | 进阶与职业准备 |
| Academy | 付费课程 + 靶场 + 认证路径 | 较高 | 系统化培养 |

### Retired 机器与 Writeup 的特殊价值

这是 HTB 最有学习价值的设计之一。**Retired（已下架）**意味着该机器已经从活跃列表中移除，但其**官方 writeup 依然可以查看**（VIP 权限）。

**💡 提示**　为什么 Retired 机器对学习特别重要？*因为它消除了「剧透」的顾虑*——机器已下架，不会有新玩家正在打通它，你可以毫无心理负担地对照 writeup 逐步学习，把每一步都真正理解清楚。**对初学者，我强烈建议从 Retired 机器入手，而不是从活跃机器硬啃。**

### Starting Point：容易被忽略的免费区

HTB 的 Starting Point 是一个**完全免费的入门专区**，提供了难度递增的机器和配套的基础课程，内容质量与付费区相当。

* **Starting Point Easy**

  ：三台基础机器，适合完全新手。
* **Starting Point Medium**

  ：进阶机器，含 Web 与提权。
* **配套课程**

  ：每个模块都有关于工具与概念的简短课程，*是快速建立知识框架的好方式*。

**💡 提示**　很多 HTB 用户会跳过 Starting Point 直接打付费机器，结果在基础概念上反复碰壁。**建议即使有经验，也花一两个小时过一遍 Starting Point 的课程部分**，它对理解 HTB 特有的工作流很有帮助。

## 03机器类型：Active、Retired、Pro Lab

HTB 的机器按生命周期与用途分为几类，每类的使用方式不同。

| 类型 | 状态 | 特点 | 使用建议 |
| --- | --- | --- | --- |
| Active | 活跃中 | 可攻略的新机器 | 练手，保持手感 |
| Retired | 已下架 | 固定不变，有 writeup | 系统学习首选 |
| Starting Point | 入门区 | 免费，有配套课程 | 新手必做 |
| Pro Lab | 实验环境 | 多机域环境，有网络拓扑 | 高级实战 |
| Enterprise | 企业版 | 大型 AD 域环境 | 团队培训 |

### Pro Lab：HTB 最有野心的产品

Pro Lab 不是单台机器，而是**一个完整的企业内网模拟环境**：多台机器、多台域控、真实的网络拓扑、以及需要在多台机器之间横向移动才能完成的挑战。

Pro Lab 模拟的是真实红队行动：从一个突破口开始，逐步拿下整个域

```
# Pro Lab 的典型拓扑（示例） Internet    ↓ Public-Facing  ──→  Bastion (跳板机)                         ↓    Internal Network:  DC01, DC02, Web01, App01, SQL01                         ↓    目标：域管理员权限
```

**💡 提示**　Pro Lab 的训练价值无法被单机靶机替代。真实攻防的核心难点从来不是「拿下第一台机器」，而是**「在多台机器之间判断哪条路径最短、风险最低」**。Pro Lab 逼着你做这些判断——*而这正是红蓝对抗中最考验经验的部分*。

## 04网络接入：Pwnbox 与 VPN 配置详解

这是 HTB 新手最容易卡住的技术环节。与 TryHackMe 不同，**HTB 要求你必须用 VPN 或 Pwnbox接入它的内网靶机网络**。

### 方式一：Pwnbox（官方提供的云端 Kali）

Pwnbox 是 HTB 提供的云端 Kali 实例，预装了大量工具，并且**已经内置了 HTB 的 VPN 配置**——开箱即用，无需手动配置。

| 方案 | 成本 | 配置难度 | 性能 |
| --- | --- | --- | --- |
| Pwnbox（免费时长） | 含在订阅内，有时限 | 零配置 | 受云端性能影响 |
| Pwnbox + 自有服务器 | 需自备 VPS | 零配置 | 性能优秀 |
| 本地 Kali + VPN | 本地资源 | 需配置 .ovpn | 性能最好 |

**💡 提示**　Pwnbox 有**使用时长限制**（受订阅等级影响），超时后需要付费延长。如果你是长期学习，*建议租用一台海外 VPS（如 DigitalOcean、Contabo）自行搭建 Pwnbox 或 Pwnbox-NG 镜像*，成本可控且完全自主。

### 方式二：本地 Kali + VPN

VPN 连接后需要手动确认接口与路由是否正常

```
# 1) 在机器页面下载 .ovpn / .ovpn.zip 文件 #    VIP 用户通常下载的是 academy 之外的 lab 配置文件  # 2) 连接 VPN sudo openvpn --config lab_user.ovpn  # 3) 确认连接成功（会出现 tun0 等接口） ip a | grep tun sudo ifconfig tun0 up 2>/dev/null  # 4) 确认能访问靶机网段 ping 10.10.10.x  # 5) 解析 HTB 域名（可选） echo '10.10.10.x  academy.htb' | sudo tee -a /etc/hosts
```

**💡 提示****关于 HTB 的域名解析：**很多机器的题目说明里会给出一个域名（如 `academy.htb`）而不是 IP。这是因为机器 IP 会随重置变化，*而域名能通过 DNS 稳定解析*。连接 VPN 后你可以正常解析，如果解析失败就在 `/etc/hosts` 里写死 IP。

#### VPN 常见问题排查

| 症状 | 原因 | 解决 |
| --- | --- | --- |
| 连接超时 | UDP 端口被网络阻断 | 尝试配置 TCP 模式或换网络 |
| 连接成功但访问不了靶机 | 路由未生效 | 检查 tun 接口 IP 与掩码 |
| 多个 VPN 冲突 | 同时开了其他 VPN | 断开其他 VPN 客户端 |
| 频繁掉线 | 网络不稳定 | 改用 Pwnbox 避免本地网络影响 |
| DNS 解析失败 | 未配置 DNS | 手动写 /etc/hosts 或指定 DNS |

## 05核心机制：难度、标签与徽章体系

HTB 的难度标注分为四档，这个分级标准比 Vulnhub 规范得多，也更有参考价值。

| 难度 | 特征 | 典型所需技能 | 预计耗时 |
| --- | --- | --- | --- |
| Easy | 直接的 Web 漏洞或弱凭据 | 基础工具、常见漏洞 | 1-4 小时 |
| Medium | 需要信息收集串联、逻辑漏洞 | 枚举能力、初步提权 | 6-20 小时 |
| Hard | 复杂利用链、绕过、源码级分析 | 源码审计、深度提权 | 1-4 天 |
| Insane | 二进制/内核/复杂密码学 | 二进制安全、内核安全 | 3 天以上 |

#### 技术标签系统

每台机器都带有技术标签，**这是 HTB 最有特色的学习辅助功能**：你可以按标签筛选，集中练习某类技术。

* **Web**

  ：注入、XSS、文件上传、反序列化等。
* **Windows**

  ：Windows 主机、提权、SMB/RDP 等。
* **Active Directory**

  ：域渗透、Kerberos、GPO 攻击。
* **Linux**

  ：Linux 主机、sudo/SUID 提权。
* **Cloud**

  ：AWS/Azure/GCP 相关。
* **Hardening / CIS**

  ：安全配置检查方向。
* **Forensics / OSINT**

  ：取证与开源情报收集。

**💡 提示****标签系统对学习的价值怎么强调都不为过。**很多人学渗透是随机刷机器，东一榔头西一棒子，结果每类技术都停留在浅层。*按标签集中训练*，比如连续打 10 台 AD 标签的机器，你对域渗透的理解会发生质变——因为你会反复遇到同类问题，形成稳定的分析模式。

#### 徽章体系：把学习成果可视化

HTB 为用户设置了系列徽章（Badge），按「首个血旗（First Blood）」「机器通关」「Pro Lab 进度」等维度划分。虽然主要是游戏化激励，但它**客观上记录了你的能力成长轨迹**——对求职和团队评估都有参考价值。

**界面说明** 机器详情页给出难度星级、标签、发行者、累计完成人数、当前状态（Active / Retired / Offline），以及用户提交的 writeup 列表入口。页面还标注了 Awarded 与提示释放记录。退役机器虽然无法开机，但社区 writeup 依然可读，适合在不方便实操时用来梳理完整攻击链。

## 06实战一：标准解题流程与 HTB 特色

HTB 的解题流程与 Vulnhub 大体一致，但在实战中有几个明显的特色需要强调。

### 完整流程（含 HTB 特色）

1. **读题**

   ：HTB 的题目描述信息量通常比 Vulnhub 大，包含场景背景、目标说明。*务必先读完再动手*。
2. **快速全端口扫描**

   ：HTB 机器的入口服务经常在非标准端口。
3. **枚举优先于利用**

   ：HTB Medium 以上的机器，通常不存在「一眼看出漏洞」的情况，枚举质量决定成败。
4. **建立假设并逐一验证**

   ：这是核心能力。
5. **提权**

   ：拿到初始权限后，`sudo -l` 与凭据搜索是标准动作。
6. **写笔记**

   ：从第一步就开始记录，不要事后回忆。
7. **复盘**

   ：对照 writeup 分析自己的思路差距。

### HTB 特色一：枚举质量决定成败

这是 HTB 与入门靶场最大的区别。在 Medium 及以上难度中，**80% 的时间应该花在信息收集上**。

子域名与虚拟主机枚举是 HTB 机器的常见突破口

```
# 1) 全端口 + 版本（必须扫全） nmap -p- -sV -sC --min-rate 5000 10.10.10.x -oN full.txt  # 2) UDP（常被跳过但很重要） nmap -sU --top-ports 100 --min-rate 5000 10.10.10.x -oN udp.txt  # 3) Web 深度枚举 nikto -h http://10.10.10.x -C all gobuster dir -u http://10.10.10.x -w big.txt -x php,txt,bak,html,js \   -t 50 --no-error -k -o gobuster.txt  # 4) 源码/备份文件专项 #    .git  .svn  .bak  .old  .swp  ~  .zip  .tar.gz #    .DS_Store  web.config.bak  database.sql  # 5) 子域名与虚拟主机（HTB 上很常见） ffuf -u http://10.10.10.x -H 'Host: FUZZ.domain.htb' \   -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \   -fc 302 -t 50
```

**💡 提示****虚拟主机枚举值得单独强调。**很多 HTB 机器的服务端根据 `Host` 头返回不同内容，只有用正确的主机名才能访问到。线索通常藏在：证书的 SAN 字段、响应头、robots.txt、以及 DNS 记录的枚举结果中。*用 `curl -k -H 'Host: xxx.htb' https://10.10.10.x` 逐一试探*，这是每个 HTB 机器都该做的标准动作。

### HTB 特色二：多机拓扑与横向思维

Pro Lab 与 Enterprise 机器中，横向路径规划是核心能力

```
# 在多机环境中，需要持续判断「下一步做什么」 Web 入口机器  --获得凭据-->  内网机器 A 内网机器 A    --发现路由-->  内网网段 10.10.x.x/24 内网机器 A    --横向移动-->  域控 DC 域控          --权限提升-->  域管理员  # 关键技能：画出拓扑图，随时更新已知信息 # 建议用 draw.io 维护一张靶场拓扑图
```

![HTB 多机拓扑示意：入口机 → 凭据 → 内网 → 域控的横向路径规划](https://mmbiz.qpic.cn/mmbiz_png/0l1UjZtX9txibtibvxiawgkvEibOLuafVHqibpNQJajSyGibSyq1UQoseN0E8o2yyCicolKo85t3U0sY4v90BrmEQrkLXI5MqmbwiaJjqVKt3Qf1xwc/640?from=appmsg)

图：HTB 多机拓扑示意：入口机 → 凭据 → 内网 → 域控的横向路径规划

## 07实战二：Retired 机器的实战复盘思路

为避免剧透具体机器的完整解法，这一节用**分析框架**的方式复盘 HTB 机器的常见解题模式。这些框架在多台机器上反复适用。

### 模式一：从 Web 到 Shell 的四种典型路径

| 路径 | 典型手法 | 触发条件 | 后续动作 |
| --- | --- | --- | --- |
| 文件上传 | 绕过扩展名/内容校验 | 有上...