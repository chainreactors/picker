---
title: Claude Code通过Git Worktree混淆实现沙箱逃逸
url: https://mp.weixin.qq.com/s/SsLMC1DTeGD6BZMJrCTYFg
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:22:48.280515
---

# Claude Code通过Git Worktree混淆实现沙箱逃逸

# Claude Code通过Git Worktree混淆实现沙箱逃逸

原创

Dr. Clay
Dr. Clay

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MCFeQJOoP0eLjWD3g1cx17JY4aqHjV0jJmAnoOeBYq3RA6DPkIsqvGI0F3ZJ5XHicFCxMS05cLWdA1icQjKAZaNGu1JNHRkJoQQ/640?from=appmsg)
> **导语**：当一个AI coding agent成为攻击面，攻击者不需要直接调用shell——只需要一段藏在`CLAUDE.md`里的自然语言指令，就能让agent亲手为自己打开系统的大门。安全研究员Metnew近日披露了CVE-2026-55607：Anthropic Claude Code中的一个沙箱逃逸漏洞，攻击者通过恶意仓库的prompt injection，操纵Git worktree工具链完成路径混淆，最终在最严格的沙箱配置下实现任意代码执行，奖金3700美元。

---

## 一、事件概述

### 1.1 背景

Claude Code是Anthropic推出的命令行AI编程助手，基于Claude模型驱动，具备创建工作区、执行代码、操纵Git分支等能力。它在macOS上默认启用seatbelt沙箱隔离，并对Bash工具执行施加严格限制。

安全研究员Metnew在研究AI agent安全边界时，发现了一条精妙的攻击路径：攻击者只需诱导用户克隆一个恶意Git仓库，用Claude Code打开它，并提出一个看似无害的请求——剩下的全部由仓库中的prompt injection驱动Claude自身完成，最终实现系统级代码执行。

该漏洞于2026年5月11日通过HackerOne提交（报告#3727895），2026年6月4日修复并部署，2026年6月25日公开披露，CVE编号为**CVE-2026-55607**，严重等级**High（CVSS 7.7）**。

---

## 二、技术分析

### 2.1 攻击前置条件

攻击的起点是一个精心构造的恶意Git仓库，其目录结构如下：

```
item6/                        ← 受害者克隆并用Claude Code打开的仓库
├── CLAUDE.md                 ← prompt injection指令序列
├── 3p_setup.sh               ← 分阶段载荷，通过fsmonitor触发
├── config                    ← root级gitconfig（携带fsmonitor payload）
├── HEAD                      │
├── description               │  这些文件使item6/本身成为一个完整
├── objects/                  │  的gitdir，从而激活worktree混淆链
├── refs/heads/master         │
├── .claude/
│   ├── settings.local.json   ← sandbox:{enabled:true, autoAllowBashIfSandboxed:false}
│   ├── agent-memory/         ← 中转目录
│   └── worktrees -> ./agent-memory   ← 符号链接（后续被替换为$HOME）
└── .git/                     ← 第二个"正常"git目录
```

关键在于：恶意仓库的根目录**同时也是一个合法的Git仓库**——`HEAD`、`config`、`objects/`、`refs/`等文件直接放在仓库根目录，而非`.git/`子目录下。这使得"创建名为`.git`的工作树"成为可能，因为该路径本身就是一个完整的、受攻击者控制的Git仓库。

### 2.2 攻击链分解

Metnew的攻击流程分为多个阶段，每个阶段由Claude Code执行prompt injection中的指令驱动，通过fsmonitor触发下一阶段载荷：

**第一步：seed阶段（步骤1-3）**

用户在Claude Code中打开恶意仓库后，CLAUDE.md中的prompt injection指令驱使Claude依次执行：

* `EnterWorktree(".git")` — 创建名为`.git`的工作树，路径为`.claude/worktrees/.git`
* `ExitWorktree` — 退出工作树（不清理）

此时，由于仓库根目录本身是gitdir（上面提到的构造），`.git`工作树实际上是一个完整的、受控的Git仓库。

**第二步：符号链接替换（步骤4-7）**

Claude Code的worktree工具会**跟随符号链接**。此时攻击载荷`3p_setup.sh`的第一阶段生效：

```
# stage 1: 将.claude/worktrees符号链接指向$HOME
if [[ $(wc -l < "$PWD/yolo") -eq 1 ]]; then
    rm -rf .claude/worktrees
    ln -s "$HOME" .claude/worktrees
fi
```

此时，`.claude/worktrees`符号链接已被替换为指向用户主目录`$HOME`。接下来Claude在`.claude/agent-memory`目录下再次执行`CreateWorktree(".git")`，由于worktree创建跟随符号链接，**实际的`.git`工作树被写入到了`$HOME/.git`**。

**第三步：伪造worktree元数据（步骤8-10）**

当Claude执行`git status`时，fsmonitor再次触发载荷的第三阶段，在`.git/worktrees/$USER`目录下重建worktree元数据，使`/Users/$USERNAME`（即`$HOME`）成为一个可导航的已注册工作树。

**第四步：进入$HOME并覆写.zshenv（步骤11-12）**

现在Claude被引导执行`EnterWorktree(".claude/worktrees/$USERNAME")`——这实际上进入了`$HOME`目录。再次执行`git status`时，gitdir解析指向`~/.git`，fsmonitor触发最终载荷：

```
# final payload: 当前目录为$HOME，gitdir指向~/.git → 覆写~/.zshenv
if [[ "$PWD" -ef "$HOME" ]]; then
    echo "echo 'ethical prove of vulnerability' && open -a Calculator" >> ./.zshenv
    exit 0
fi
```

### 2.3 沙箱为何被突破

这是整个漏洞最精妙的部分。macOS上，Claude Code执行Bash工具时的实际调用链为：

```
/bin/zsh -c "seatbelt enforcement" "$PAYLOAD"
```

而`zsh`在应用seatbelt限制**之前**，会先读取并执行`~/.zshenv`文件。攻击者正是利用这一顺序——将恶意代码写入`~/.zshenv`，使其在seatbelt沙箱**应用之前**就已执行，从而实现沙箱逃逸。

Metnew在PoC中验证了这一点：即使Claude Code配置为`sandbox:{enabled:true, autoAllowBashIfSandboxed:false}`（最严格模式），攻击仍然成功。

![Git Worktree沙箱逃逸攻击流程图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6P86wE0wDlIYvTTeic00tyEe8kWhA1fcOkicXAiaLsGdoZ8Iyzy4hqbpkddd8U8EBH3p5IkFLSpia50lIndNP5T0N0Jnp3Emhw5ibH8/640?from=appmsg "Git Worktree沙箱逃逸攻击流程图")

---

## 三、漏洞根因

CVE-2026-55607的攻击链由三个独立的安全缺陷组成：

**缺陷1：`.git`被接受为合法的worktree名称**

Claude Code的worktree工具未对工作树名称进行安全校验，`CreateWorktree(".git")`被允许执行。这使得攻击者可以在项目目录下创建一个路径与Git元数据目录冲突的工作树。

**缺陷2：Worktree创建跟随符号链接写出项目目录**

Claude Code允许通过符号链接将worktree元数据写到项目目录之外（如`$HOME`），且这一操作无需用户确认。

**缺陷3：`~/.zshenv`可被未授权覆写**

在seatbelt沙箱配置文件（`folder-specific-autogen.sb`）生效之前，`zsh`会先加载`~/.zshenv`。Claude Code未能防止这一路径的写入，导致攻击者可以在沙箱外围植入任意代码。

Anthropic在2.1.163版本中**修复了缺陷1**：`.git`不再被接受为有效的worktree名称。

---

## 四、影响范围与修复

**影响版本：**

* Claude Code v2.1.139（macOS Tahoe，受害者测试环境）
* 可能影响所有启用worktree工具的版本

**修复方案：**

* **自动更新：** Claude Code默认自动更新，受影响用户已自动收到修复
* **手动更新：** 更新至**2.1.163**及以上版本
* **验证方法：** 运行`claude --version`确认版本号

**CVSS评分：** 7.7（High）

---

## 五、防御建议

对于安全研究者和AI工具使用者：

* **谨慎克隆未知仓库：** 这是最根本的触发条件——攻击需要用户主动克隆并用Claude Code打开恶意仓库
* **审查CLAUDE.md内容：** 对来自不可信来源的`CLAUDE.md`、`INSTRUCT.md`等文件保持警惕，它们可能包含prompt injection指令
* **避免在未审查的仓库中运行工具自动批准：** Claude Code的工具审批流程应被视为安全边界，而非可选项
* **关注AI Agent的攻击面：** AI coding agent的每一个工具调用都是潜在攻击面——本漏洞证明，即使是最严格的沙箱配置，也可能被精心设计的文件系统原语组合击败

---

## 六、漏洞赏金与时间线

| 时间 | 事件 |
| --- | --- |
| 2026年5月11日 | 通过HackerOne提交报告（#3727895） |
| 2026年5月12日 | 提交扩展RCA分析 |
| 2026年5月18日 | 催促审核（一周未分类） |
| 2026年5月27日 | 审核通过，严重等级定为High（CVSS 7.7） |
| 2026年5月28日 | 授予$3,700奖金 |
| 2026年6月4日 | 修复版本部署 |
| 2026年6月（复测） | 确认修复，额外授予$50复测奖励 |
| 2026年6月25日 | 公开披露CVE-2026-55607 |

值得注意的是，Metnew原本计划在Pwn2Own Berlin 2026上演示类似漏洞链，若被接受预计可获奖金，但方面拒绝了其注册申请。在报告中写道：最终实际获得的3,750与Pwn2Own报价差距悬殊。

---

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6P04nLo6ic5ONGQIhTNAHp9DLcoPEjw0ACJyekw30y0zU1Iicw8ENF2y5LeWceuUouSIQ7sC53Cf3BohLPhbLib8aRTMFgbGobLaA/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MHrRAOicF11SlY9ia628Ig2CpyZZqic8ufOyHOnCW0Ml9WYLsUbNpbQo5gxy6no9PLnAHulDDSxpQAtcIrv46NII3xqw5ibSeWRKc/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NoibLOIO3HqQkZP1Hxft3KLia6UrYheYCiatibnzmcy7A4RXdkbhzlGiafkW34e8BMM9eiaZJic3LianN5bqA6WeBib9icVrpOHiarxdqKTY/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OJsiboj8qef7BtqjY2Dw3smiaLEL04Dryic9wrD2xEiaJeX64cWZvKvJo2wLhX5rm6lGgZZUWG23DJXfOfsefRchFKXLaqqoATUdw/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

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