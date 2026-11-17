---
title: Cursor插件市场混进了假Claude Code：11小时，最多5000名开发者可能中招
url: https://mp.weixin.qq.com/s/2aankuchAiOK2yt5BEsjwg
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:09.610119
---

# Cursor插件市场混进了假Claude Code：11小时，最多5000名开发者可能中招

# Cursor插件市场混进了假Claude Code：11小时，最多5000名开发者可能中招

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M3q56Kic1svSY4Ca9BwveNvG7KnXiciagnVHuHibAYWRGwMxRrAGic4pgOoyibISMgxoFgBn381cro3iaSQM2ulEAUYyN0r3v2o5DSVc/640?from=appmsg)
> **导语**：这次事件里没有 CVE，也没有 0day。攻击者全程用的都是合法凭据和合法通道：一把被曝的服务商密钥、一批没脱敏的对话轨迹、还有一堆用户贴进客服对话框的密码。他最终把带 SSH 后门的假插件推进了一个 AI 编程工具的插件市场，而整条链的起点，是 10 月 6 日一家 AI 推理服务商内部凭据被滥用。

![Cursor 插件市场投毒事件示意图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MTg6Q589MVrzdP3FwlzyLnhb9UwEwNMo5gEMHOuZea2KRdewFzMzCTV8VRfibpd1HelOremSeOF1rzCMTPQurUlR4eCASP5bac/640?from=appmsg "Cursor 插件市场投毒事件示意图")

*图：The Hacker News 配图*

## 先说清楚三个名字

不搞懂这三个词，后面的链条会看得很累。

**Cursor** 是一款基于 VS Code 的 AI 编程编辑器，主打用自然语言改代码。它的插件市场（官方叫 VS Code 扩展市场）相当于 Chrome 应用商店，用户从里面装各种 AI 助手插件。

**Claude Code** 是 Anthropic 官方的 AI 编程插件和命令行助手，正常情况下通过公共市场 Open VSX 分发。

**Fireworks AI** 是提供模型推理和训练服务的厂商。Cursor 曾把自己的一部分推理流量和一批数据共享给它，双方用一个存储桶做数据交换。

记住这三层关系就够了：一层是给开发者装插件的商店，一层是被伪装顶替的官方插件，最底下那层是掌握着密钥的服务商。

## 一、起点在 Fireworks AI，不在 Cursor

Cursor 在 11 月 13 日发布的调查更新里，把整条链拆得很清楚：事情从 Fireworks AI（AI 推理服务商）开始。

10 月 6 日上午 9 点（PDT），Fireworks AI 监测到内部凭据被非授权使用。攻击者拿这把内部凭据访问了部分客户账号里用于模型评测任务的环境变量。10 月 10 日的公告写得很谨慎——当时只确认环境变量被捕获，其中包含以密钥形式存放的 API Key 和 token；没有迹象表明客户模型、数据集、训练数据、推理流量或个人信息被碰到。

反转出现在 10 月 23 日。Fireworks 用来托管研发机器的第三方云服务商出了安全事件，10 月 24 日，攻击者借这条路摸进 Fireworks 的开发机，在上面跑了一个未授权任务，导致额外一批客户数据受影响。Fireworks 在补充公告里承认了第二段入侵，并说明受影响的范围包括：资源元数据（Fireworks 资源标识、显示名、描述、创建时间）、账单信息（账单与收货地址、发票与付款历史、账户余额、信用额度使用）、以及部分客户不完整的模型权重与数据集。支付卡号 Fireworks 自己不存，没被碰。

需要注意的是，这里泄露的不是 Fireworks 平台本身，而是**它持有的客户凭据**。真正致命的是接下来这一跳。

## 二、攻击者拿到的是一把"合法"的 key

Cursor 给 Fireworks 发过一把访问密钥，用来读一个共享的只读存储桶。Fireworks 这边出事之后，这把 key 被曝了出去。

攻击者拿这把 key 复制了整个桶的数据。桶里装的是什么？Cursor 说得很具体：数量有限的 coding agent 轨迹记录，大部分来自 2025 年，对应那些没开隐私模式（Privacy Mode）的会话——Cursor 有权拿这些数据做模型训练。

问题出在"做训练用"和"已脱敏"是两回事。桶里有少量轨迹带着未脱敏的凭据。Cursor 给出的数字是：**不到 0.01% 的客户有 API 凭据暴露**，涉及不到 0.05% 的非隐私模式用户（这部分用户已被逐一通知）。

顺着这些凭据，攻击者摸到了 Cursor 日常在用的一批 SaaS 服务，从里面拿到的东西包括：部分归档的非生产环境源码仓库（有些里面带业务联系人信息）、有限的客服数据与邮件往来、产品使用指标与联系方式、部分 coding agent 会话摘要，以及**一些用户发给 Cursor 客服的凭据**。

最后一条最狠。用户报障的时候顺手贴的密钥，成了攻击者的跳板。

## 三、11 小时的窗口期

10 月 29 日凌晨 2:27（PT）到下午 1:35（PT），攻击者用前面拿到的内部凭据，把自己篡改过的 Anthropic Claude Code 扩展，直接放进了 Cursor 插件市场对外服务的缓存里。

几个必须说清楚的事实：

* 这不是 Anthropic 官方发的版本，也不是 Anthropic 产品本身的漏洞。上游市场 Open VSX 从来没有过这个恶意版本，恶意包只出现在 Cursor 自己那张缓存上。
* 受影响的是 2.1.312 和 2.1.313 两个版本，覆盖 Windows 和 macOS。
* 恶意包对外分发约 11 小时后被下架，期间最多 **5000 名** 在 10 月 29 日请求过这两个特定缓存版本的开发者可能拉到过带毒构建。
* Cursor 随即把整个插件市场下线，与托管攻击者服务器的那家云服务商合作把服务器端也打掉了。目前反向 shell 和主机信息回传通道都已失效。

Cursor 的监控在 10 月 29 日当天发现了异常活动，随后停用厂商密钥、启动应急响应、开始吊销和轮换凭据。他们看到的最后一次攻击者活动发生在 11 月 1 日，之后被阻断。

### 带毒扩展干了什么

Cursor 在 10 月 30 日发布的通告里附了完整 IOC（失陷指标），载荷行为梳理如下：

**采集与回传**：主机名、用户名、操作系统、架构、用户主目录路径、环境变量名、工作目录、已配置的 Git 邮箱、公网 IP。

**植入后门**：往受害者的 `authorized_keys` 里追加攻击者公钥（密钥注释为 `svc-telemetry`），尝试启用本机 SSH 服务，并建立反向 SSH 隧道。

**持久化**：macOS 走 LaunchAgent（`com.apple.sysmond.plist`），Windows 走计划任务（任务名 `SysMon`，尝试以 SYSTEM 身份运行）并配启动脚本兜底（`sysmon.cmd`）。后台脚本大约每 60 秒重试一次隧道。

**一个关键缓解事实**：启用本机 SSH 服务需要管理员权限，而恶意代码本身在非管理员场景下会因自身缺陷失败。所以大多数机器上，攻击者**没能真正从隧道登进来**。但攻击者公钥已经写进去了、持久化已经装好了、主机信息已经回传了。Cursor 在通告里仍然要求全部按受影响的流程走排查——因为环境变量收集这一步，不排除后续通过后门拿到更多凭据。

![带毒扩展的 SSH 后门与反向隧道](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PdicLgYXD66LFZV8nLdRJ25KVHF8YgFM3rThNJvNRUiaAeGKFaRMLSojXtJDCkibN3UosVC483KnQqWzbpL0gNQcRlL57OSzLibgU/640?from=appmsg "带毒扩展的 SSH 后门与反向隧道")

### IOC 清单

| 类别 | 指标 |
| --- | --- |
| 攻击者服务器 | 134[.]209[.]82[.]225 |
| 反向 SSH | tunnel@134[.]209[.]82[.]225，TCP 22 |
| 外部信标 | hxxp://134[.]209[.]82[.]225:8099/beacon（HTTP POST） |
| 本地信标 | 127[.]0[.]0[.]1:8099/beacon（HTTP POST，回环） |
| 未授权公钥 | ssh-ed25519 AAAA...Ss0P，注释 `svc-telemetry` |
| 公钥指纹 | SHA256:0Z6R+DF64Do2nwQic8a7kkfDLNNk4IiK+2U2Rci4htk |
| 隧道密钥指纹 | SHA256:KOAU57+ZG6u3MG4WwzPzPX2O5YEe9qdOC1Bl+6MVyDQ |
| 载荷哈希 | `extension.js` SHA256: ecb58cb29078d9646ad1dcdbe51526f2d9cfea06be5fb2ab183e8ecc3ab6bf15 |
| 落地文件 | `~/.config/.smt` 、`~/.config/.smtk`、`/tmp/.stk_<10位十六进制>`、`%USERPROFILE%\.config\smt.cmd` |
| 持久化 | `~/Library/LaunchAgents/com.apple.sysmond.plist` 、计划任务 `SysMon`、`sysmon.cmd` |
| 关键命令 | `ssh -N -R '*:0:localhost:22'` 、`autossh -M 0`、`schtasks /create /tn SysMon`、`systemsetup -setremotelogin on` |
| SSH 参数 | `StrictHostKeyChecking=no` 、`UserKnownHostsFile=/dev/null`、`IdentitiesOnly=yes`、`ExitOnForwardFailure=yes` |

被篡改的 VSIX 包哈希（四个变体）：

* 2.1.312 darwin-arm64：SHA256 `fcbb327e38e61c4fec795e0d0591f52cd1014b813d20a5912104953c3a17c364`
* 2.1.312 win32-x64：SHA256 `3de1722901165769893bef57c72594e9a54459faa23f3091b136b79966edd081`
* 2.1.313 darwin-arm64：SHA256 `80402fdcad8799285fd93044976973ca000da7995fb93363f819bb8e4f84ee6c`
* 2.1.313 win32-x64：SHA256 `6786ec90cbd45949695bd7805c9fbb26cfc91bc5fc897de0183d9bcb9cb21731`

补充一句避免误伤：载荷会访问 `ifconfig[.]me` 和 `api[.]ipify[.]org` 查公网 IP，这两个是合法服务，**单凭访问它们不算失陷指标**。

自查最简单的一条：macOS 上跑 `grep -qs svc-telemetry ~/.ssh/authorized_keys`，Windows 上在 PowerShell 里检查 `$HOME\.ssh\authorized_keys` 和 `C:\ProgramData\ssh\administrators_authorized_keys` 里有没有 `svc-telemetry`。命中即视为受影响。

Cursor 同时放出了两个清理脚本：`remediate-macos.sh`（用受影响用户身份跑，别用 root）和 `remediate-windows.ps1`（管理员 PowerShell 执行）。脚本会移除恶意扩展、持久化机制、运行中的隧道进程和攻击者公钥，残留任何东西都会以非零状态退出。

## 四、横向影响：Notion 的聊天记录和 Uber 的驾照

Fireworks 这次被曝的凭据，是多家公司的"上游"。谁把数据放在了 Fireworks 上，谁就跟着遭殃。

**Notion** 自己确认了：受影响的 workspace 不到 1%。最初评估是 Notion AI 的合成测试数据，后来发现里面混有 Insights 功能用到的 Notion AI 聊天记录。对绝大多数受影响的 workspace 来说，这些记录是"无法归属"的——没有标注作者、不知道来自哪个 workspace，也没有工具调用结果。Notion 随后停用了 Insights 功能，也不再通过 Fireworks 提供开放权重模型。

**Uber** 走的是通知流程。公司 10 月 9 日收到服务商告知，说黑客闯进去偷走了内部凭据并用其访问了 Uber 的数据，随后开始通知受影响的司机。截至 11 月中旬，各州披露的驾照信息涉及人数分别是：马萨诸塞州 2567 人、南卡罗来纳州 3430 人、罗德岛州 1873 人，伊利诺伊州人数待定，加州也发了通知但没给具体数字。这是 Uber 今年第二次已知的数据泄露——上一次是货运部门 Uber Freight 被勒索团伙得手。

## 五、红队视角：这条链为什么难防

![Cursor 事件完整攻击链](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6P1Oh29EblcSJPjxaR22PdeqFuGeAibC4ohWvXuNNxqAJt8a7gEeCPD7OR2ejnJgxystqHr1PH3LZ3ykgd3xUa0g6ibDFGiayg5PI/640?from=appmsg "Cursor 事件完整攻击链")

站在攻击者的位置复盘，这是一条教科书级的供应链横向路径，每一跳都是"合法凭据 + 合法通道"：

**第一跳用供应商的密钥开门。** 攻击者不需要打 Cursor 的任何系统，他只需要一把 Cursor 自己发出去的、给第三方的 key。防守方这边的问题在于，供应商被入侵时，Cursor 根本不知道自己的 key 已经在别人手里了。日志上看到的全是正常访问。

**第二跳用 AI 助手的行为轨迹当凭据库。** 这一步是这次事件里最值得琢磨的地方。coding agent 的对话轨迹不是普通日志，它装着开发者让 AI 帮忙写代码时顺手粘进来的密钥、配置和内部地址。用这些轨迹做训练是合理需求，但没脱敏就等于把客户的密钥池抄了一份放在桶里。桶还是只读的——只读不代表只被自己读。

**第三跳打客服工单。** 用户把密码贴进客服对话框，攻击者通过 SaaS 侧的邮件往来直接拿到。这条路径不需要任何漏洞。

**第四跳才是真正的落地。** 有了能写 Cursor 插件市场缓存的凭据，剩下的就是老本行：投毒、放后门、等。11 小时，5000 次拉取机会，在开发者群体里已经是很高的转化率了。

顺着这条链往回看，Google 威胁情报团队（GTIG）和 Mandiant 在 11 月 2 日发布的报告给出了更大的背景：他们把这种模式命名为 **LLMJacking（大模型劫持）**——攻击者通过偷来的云身份令牌（IAM 凭据、Service Account 密钥、GitHub 个人访问令牌、活动会话令牌）拿到 LLM 访问权，再把这份访问能力转卖给地下渠道，让正主付账单。单起事件里，欺诈性云账单一天能超过 10 万美元，部分组织在被吊销凭据前累计损失达到 100 万美元。

GTIG 还观察到更精细的运营细节：攻击者会用 `max_tokens=1` 的最小请求做凭据批量验证，专门绕开受害方的 EDR 和 SIEM 用量异常告警；有人拿 LiteLLM 网关的用户 ID 重绑定漏洞（CVE-2026-40217）把普通虚拟密钥提成 `PROXY_ADMIN`；还有人搭 `new-api`、`gcli2api` 这类网关聚合被盗密钥对外分销。这已经是分工明确的产业环节了——GTIG 称之为"LLM Mixer"。

## 六、该做什么

**如果你是开发者**：检查自己有没有在 10 月 29 日当天从 Cursor 插件市场装过或更新过 Claude Code 2.1.312 / 2.1.313。装了的话，先跑上面的 `svc-telemetry` 检查，再跑官方清理脚本。别只卸载扩展——载荷会往系统里丢独立的持久化脚本，卸载不掉的。

**如果你在团队里**：Cursor 明确要求过一件事——卸载扩展本身可能不够。要把受影响主机上能访问到的凭据和会话全部轮换掉，并且从可信设备上做这件事。Cursor 自己的做法是按风险从高到低轮换所有暴露的凭据，连没有暴露证据的内部凭据也一并换掉。

**如果你在做 AI 工具链**：这次踩坑的地方值得逐条抄作业。给供应商的 key 要短命、要最小权限、要有独立审计；训练数据落地前必须做凭据脱敏扫描；agent 对话轨迹当训练集用的时候，得当成客户密钥库来管；模型服务的 marketplace 缓存要有独立的完整性校验和发布签名，别让缓存层变成可写的高价值目标。

**如果你在云上**：GTIG 报告里那条"用 `max_tokens=1` 验证密钥"的思路，反过来就是检测思路——对 LLM 网关做单 token 请求量的基线，比盯着 token 总量更能抓到这种"低调试钥匙"的行为。

## 时间线

| 时间 | 事件 |
| --- | --- |
| 10 月 6 日 09:00 PDT | Fireworks AI 检测到内部凭据被非授权使用 |
| 10 月 10 日 | Fireworks 发布首份公告，仅确认环境变量与其中的密钥被捕获 |
| 10 月 23 日 | Fireworks 研发机器所在的第三方云服务商发生安全事件 |
| 10 月 24 日 | 攻击者借道云服务商进入 Fireworks 开发机，运行未授权任务 |
| 10 月 29 日 02:27 PT | 恶意 Claude Code 扩展被投放到 Cursor 插件市场缓存 |
| 10 月 29 日 13:35 PT | Cursor 下架恶意版本并下线整个插件市场 |
| 10 月 30 日 | Cursor 发布安全通告、IOC 与清理脚本，开始通知受影响用户 |
| 11 月 1 日 | 最后一次观察到的攻击者活动，被阻断 |
| 11 月 2 日 | GTIG / Mandiant 发布 LLMJacking 专题报告 |
| 11 月 9 日 | Fir...