---
title: 刚升到 Gitea 1.27.0 以为安全了？两个 0day 直接 RCE
url: https://mp.weixin.qq.com/s/PONVOe9ehMxbB86HiVKSQw
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:56:22.095607
---

# 刚升到 Gitea 1.27.0 以为安全了？两个 0day 直接 RCE

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LAQpgdWQScuaeYhoVrCynXr0wBA4GcCL5A4z1odzMO8as9qQtmLAV3djV6TN6jFwKoYjJiaiaRUrZnDiaFNVpwohXKmIuibotcwgoc9x0Eiarb8k/0?wx_fmt=jpeg)

# 刚升到 Gitea 1.27.0 以为安全了？两个 0day 直接 RCE

night安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctVS8Ps0NsFTqMiasz8uDibcvoib0spt17ORFYGT7Lk8y0JElHpWukiczXboIicO8mrOUut0DwfE4PvMwpuReeibS0yQHqN8Tictdm4Z4/640?wx_fmt=png&from=appmsg)

前两天刚写完 Gitea CVE-2026-58443 的分析，告诉大家升到 v1.27.0 就安全了。结果今天外网直接甩出来两个新的 0day，一个远程代码执行（RCE），一个任意文件读取（Path Traversal / LFI）。PoC 目标版本明明白白写着 v1.27.0，也就是上一轮的「修复版」。不需要管理员权限，只要能建仓库或者能提交代码的普通用户就能打。自托管的 Gitea 和 Gitea.com SaaS 都中招。补丁还没出，CVE 也还没分配。

一、危害

这次不是一个小洞，是两个高危 0day 组合拳。研究者在外网公开披露的信息很明确：Remote Code Execution + File Inclusion，无需管理员权限，任何能创建仓库或向已有仓库提交代码的用户都能触发。

![](https://mmbiz.qpic.cn/mmbiz_png/LAQpgdWQScsXaLose7RcSicUuibibBv7bkK5pPUgiblZtqyMFfO21IIveRKPzUOMICBSGIz83DLCC3eoO3qWHJQ8mFuetFROQzIgpZ2uyVIKJ3I/640?wx_fmt=png&from=appmsg)

**0day-A · 远程代码执行（RCE）**

PoC 脚本 `gitea_rce_poc.py` 以普通用户身份登录目标实例后自动完成全套利用：创建仓库、投递两段 payload commit、触发服务端执行命令。截图里跑的是 `id; uname -a`，成功拿到 `uid=1000(git)` 的 shell。这意味着攻击者可以在 Gitea 服务端以 git 用户身份执行任意系统命令。

**0day-B · 任意文件读取（File Inclusion / Path Traversal）**

PoC 脚本 `gitea-file-inclusion-poc.py` 同样用普通用户身份，指定 `--path /etc/passwd` 参数后，成功读出服务端完整 passwd 文件内容。这意味着攻击者可以遍历读取服务端文件系统上的敏感文件（配置文件、密钥、数据库凭证等）。

**影响范围** 研究者明确指出两个漏洞同时影响：

· 自托管 Gitea 部署（所有已知版本，含最新发布版 v1.27.0）

· Gitea.com 官方 SaaS 托管服务

**CVE 状态** 尚未分配 CVE 编号，补丁尚未发布。研究者表示将在补丁发布后公开技术细节和完整 write-up。

**CVSS 预估** 10.0 Critical（网络可达 + 无需认证/低权限 + 无交互 + 作用域变更 + 全影响面）。最终分值以官方分配为准。

|  |  |
| --- | --- |
| 版本区间 | 状态 |
| ≤ v1.26.4 | 受影响（含旧 CVE-2026-58443） |
| v1.27.0（当前最新版） | 受影响（新 0day 已验证） |
| 暂无安全版本 | ⚠️ 补丁待发布 |

⚠️ 风险定性，这是目前 Gitea 最严重的安全事件之一。上一轮 CVE-2026-58443 还只是授权绕过写私有仓，这次直接是 RCE + 读任意文件，而且打的正是大家刚升上去的「安全版」v1.27.0。不需要管理员权限意味着任何有正常代码提交权限的账号都可能成为攻击入口。如果你在运维 Gitea，不管什么版本，现在就应该按下方临时缓解措施行动起来。

二、原理分析

**背景：上一轮 CVE-2026-58443（已修，但修了个寂寞）**

先快速回顾一下上周那个洞。Gitea 的 PR 更新接口 `POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update` 在做 public-only 令牌校验时只检查了路由里的公开基础仓库，没在服务端合并变基到私有头分支时再把令牌限制套一遍，导致 public-only 令牌越权写私有分支。CVSS 9.6，v1.27.0 修了它（补丁 #38406）。当时我们说「升到 1.27.0 就安全了」。

**新 0day：完全不同的攻击面**

这次的两个 0day 走的不是 PR 更新那条路。从 PoC 截图的利用流程来看，攻击者只需要三步

· 用普通用户账号登录（不需要管理员）

· 创建一个新的仓库（或向已有仓库推送 commit）

· 通过仓库操作中的某个环节投递恶意 payload

RCE 的 PoC 分两阶段投递 payload（payload 1/2 accepted），说明利用链涉及两次 commit 操作来组装完整的攻击载荷。文件包含的 PoC 则通过推送特定格式的 payload 后直接请求读取服务端路径。两者都绕过了 Gitea 对仓库操作的正常安全检查，在服务端实现了代码执行或文件系统访问。

**为什么连 v1.27.0 都防不住**

v1.27.0 修的是令牌授权边界的问题（public-only bypass），但这两个新 0day 利用的可能是 Git 仓库操作层面的另一类缺陷，比如 LFS 对象处理、仓库钩子注入、Git SSH 包装层、或者 Actions 工作流中的路径校验缺失等。具体技术细节要等研究者发完整 write-up 才能确认，但从 PoC 行为来看，攻击入口就在「能创建/贡献仓库」这个最基本的操作上，跟是不是管理员毫无关系。

三、完整攻击链

以下攻击链根据两张 PoC 终端截图还原，展示两个 0day 的实际利用流程。

1探测目标

PoC 脚本首先连接目标 Gitea 实例（如 `http://localhost:3000`），确认可达并识别版本为 1.27.0。

2普通用户认证

使用普通用户名密码登录（截图中为用户 `shai`），日志显示 `logged in as Shai (1.27.0)`。全程不需要管理员或任何特殊权限。

3创建仓库

脚本自动创建一个新仓库（RCE PoC 中为 `Shai/test-repo-0325669374`，LFI PoC 中为 `shai/rd-1784979808`），作为投递 payload 的载体。

4投递 Payload 并触发漏洞 ⚡

**RCE 路线**：分两阶段投递 payload（`delivering payload 1/2... payload accepted` → `delivering payload 2/2... payload accepted`），每个 payload 以独立 commit 形式写入仓库。两段 payload 组合后在服务端拼接成可执行的攻击链。

**LFI 路线**：推送恶意 payload（`pushing payload... payload pushed`）后，通过仓库接口请求读取服务端指定路径。

5获取结果（漏洞确认）⚡

**RCE 结果**：`retrieving output... operation complete`，输出 `id=1000(git) gid=1000(git)` + 完整 uname 信息。攻击者在服务端拿到了 git 用户的 shell。

**LFI 结果**：`retrieving file...`，输出 `/etc/passwd` 完整内容（root 到 nobody 全部用户条目）。服务端文件系统被穿透。

📌 关键认知，这两条攻击链最可怕的地方在于门槛极低且无法靠「升级」规避。上一轮的 CVE-2026-58443 你还能升到 1.27.0 来修，但这两个 0day 打的就是 1.27.0 本身。任何有正常仓库操作权限的用户都是潜在攻击者，而任何允许用户自注册或自由创建仓库的 Gitea 实例都暴露在攻击面上。Gitea.com 的 SaaS 用户同样不能幸免。

四、自主排查

由于补丁尚未发布，目前没有「升级即修复」的办法。下面给的是确认自身暴露面和临时缓解用的排查动作，全部只读或管理操作。

排查项 1 · 核对实例版本（只读）

```
curl -s https://<你的Gitea域名>/api/v1/version# 当前所有已知版本均受影响# 返回示例：{"version":"1.27.0","url":".../api/swagger","current_version":"1.27.0"}# ← 即使是 1.27.0 也已被 0day 验证可利用
```

排查项 2 · 审计用户注册与仓库创建策略（需管理员）

```
# 1. 检查是否开放了自助注册（这是最大的攻击面入口）# 登录管理后台 → 认证设置 → 查看「启用注册」是否开启# 如果开启 → 任何人都可以注册账号并发起攻击# 2. 检查谁有权限创建仓库# 管理后台 → 用户列表 → 筛选有仓库创建权限的非管理员用户# 攻击面 = 有仓库操作权限的用户数# 3. 检查外部协作（Fork / PR / Push 权限）# 重点看公开仓库是否允许匿名/低权限用户 Push 或创建 PR
```

✅ 排查判定

· 开放自助注册 + 允许普通用户创建仓库 → 攻击面完全敞开，立即执行下方临时缓解措施。

· 使用 Gitea.com SaaS → 同样受影响，关注官方公告，暂时限制不必要的外部协作者权限。

· 关闭自助注册 + 严格限制仓库创建权限 → 攻击面缩小但未消除，仍需等待官方补丁。

五、临时缓解方案（补丁发布前）

⚠️ 目前尚无正式补丁可用。以下是研究者建议的临时缓解措施，能显著缩小攻击面但不能彻底消除风险。

① 立即关闭自助注册

这是最关键的一步。自助注册开启意味着任何人都可以注册账号并获得仓库操作权限，从而成为潜在攻击者。管理后台 → 认证设置 → 关闭「启用注册」。对已有用户做一次审计，清理不再需要的账号。

② 收紧仓库创建权限

审查并限制谁可以创建新仓库。将仓库创建权限收归可信用户/管理员，禁止普通用户自行创建仓库。因为攻击链的第一步就是「创建仓库」，掐掉这一步就能阻断自动化 PoC。

③ 限制仓库协作（Push / PR / Fork）范围

仔细审查每个仓库的协作设置。最小化允许 Push 和创建 PR 的用户范围，特别是公开仓库。如果业务允许，暂时关闭来自外部用户的 Fork 和 PR 功能。

④ 关注官方公告，补丁一出立刻升

研究者明确表示将在补丁发布后公开完整技术细节和 write-up。届时大概率会分配 CVE 编号。一旦 Gitea 官方发布安全更新，立即升级。同时关注 GitHub Advisory 和 Gitea 官方博客的安全通告频道。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctTWicwicwovsVtMLAjYPfEB9lMRmJJiaIozWIuicwrbneXZ3pGly4lRNAd1WrP6AKYA925Iz4c1EbnMLCOqWzkCmdCLXDQibsG4VQw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SaibaRNhOjqiaCicRfSc5cJ3oiaCRqb97SmncCWWvuTyytibyIDxB9ZXWOuNaiaGAX2t0DYAAbdJ7aicS6WeCz4wfMoUg/0?wx_fmt=png)

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