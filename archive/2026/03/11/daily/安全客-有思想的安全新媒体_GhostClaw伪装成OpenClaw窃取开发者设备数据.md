---
title: GhostClaw伪装成OpenClaw窃取开发者设备数据
url: https://www.anquanke.com/post/id/315116
source: 安全客-有思想的安全新媒体
date: 2026-03-11
fetch_date: 2026-03-12T04:06:49.991028
---

# GhostClaw伪装成OpenClaw窃取开发者设备数据

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# GhostClaw伪装成OpenClaw窃取开发者设备数据

阅读量**22543**

发布时间 : 2026-03-11 13:58:16

**x**

##### 译文声明

本文是翻译文章，文章原作者 Mayura Kathir，文章来源：gbhackers

原文地址：<https://gbhackers.com/ghostclaw-masquerades-as-openclaw/>

译文仅供参考，具体内容表达以及含义原文为准。

![]()

一款名为 **@openclaw-ai/openclawai** 的恶意 npm 包，**伪装成合法的 OpenClaw CLI 工具**，在开发者设备上悄悄部署功能完整的信息窃取程序与远程控制木马（RAT）。

该威胁内部代号为 **GhostLoader**，结合了精细化社会工程学、加密载荷投递与持久化驻留能力，**可窃取开发者几乎所有高价值密钥**，包括 SSH 密钥、云平台凭证、AI 智能体配置以及浏览器活跃会话信息。

该 npm 包伪装成无害的 “OpenClaw 安装工具”，拥有整洁的 `package.json`、看似正常的 `src/index.js` 出口且无额外依赖，快速审查时风险特征极低。

真正的恶意行为藏在 `scripts` 目录中：`postinstall` 钩子会**静默将包全局安装**，使 `openclaw` 命令加入系统 PATH，并指向混淆处理的第一阶段加载程序 `scripts/setup.js`。

当开发者运行 `openclaw` 时，会看到界面逼真、带进度条与日志动画的 CLI 安装程序，以此掩盖**高度混淆的代码正在外联 C2 控制服务器**的事实。

JFrog 安全研究团队已确认这款名为 **@openclaw-ai/openclawai** 的恶意 npm 包正在活跃传播。

随后，恶意脚本会弹出仿苹果钥匙串风格的伪造提示框，声称需要 “安全存储凭证” 并索要系统密码。它会调用操作系统真实认证接口校验密码（macOS / Windows / Linux 均支持），伪装成正常行为。

当受害者输入密码时，`setup.js` 会**秘密解码经 XOR 加密的 URL 与活动 ID**，连接 `hxxps[://]trackpipe[.]dev`，下载经 **AES‑256‑GCM** 加密的第二阶段载荷。

解密后的 JavaScript 代码会写入临时文件，在独立 Node 进程中执行，并通过环境变量传递窃取的密码与活动标签：

* `NODE_AUTH_TOKEN`
* `NODE_CHANNEL=complexarchaeologist1`

执行约 1 分钟后文件会自动销毁，减少取证痕迹。

`setup.js` 经过高强度混淆：字符串表乱序、RC4 解密、控制流平坦化。运行时展示高度仿真的 CLI 安装界面与动态进度条。

![]()

在 macOS 上，如果 “完全磁盘访问权限” 限制了 Safari 数据读取，恶意软件还会通过 AppleScript 弹出对话框，**诱导用户为终端授权完全磁盘访问**，甚至提供直接打开系统设置的按钮，从而获取备忘录、邮件、iMessage 与 Safari 历史记录权限。

---

### GhostClaw 伪装成 OpenClaw 运行

第二阶段载荷 **GhostLoader** 是一个 11700 行的 CommonJS 模块，它会以伪 “npm 遥测服务” 的名义实现持久化：

* macOS / Linux：`~/.cache/.npm_telemetry/monitor.js`
* Windows：`%APPDATA%/.npm_telemetry/monitor.js`

并通过 Shell 配置文件、定时任务、后台守护进程等多种方式维持自启动。

它会向 `.zshrc`、`.bashrc`、`.bash_profile` 追加伪装成 “NPM Telemetry Integration Service” 的启动项，在 Linux 中写入 `@reboot` 定时任务，并使用 PID 锁保证**单例、持续运行**。

C2 服务器返回 JSON 格式响应，包含两个字段：

* `payload`：Base64 编码的加密载荷
* `k`：十六进制格式解密密钥

载荷使用 **AES‑256‑GCM** 算法解密。

![]()

首次运行时，**GhostLoader 会在 10 分钟内完成高强度数据搜刮**，并向 Telegram 发送 “新会话” 告警，包含受害者系统密码、主机名、IP、国家与设备配置，随后开始批量窃取敏感数据。

它会窃取：

* macOS 与 iCloud 钥匙串
* 解密 Chromium、Firefox 密码与 Cookie
* 通过 Chrome DevTools Protocol 窃取 Cookie
* 主流钱包应用、浏览器扩展助记词（BIP‑39）
* 桌面、文档、下载目录中的敏感文件

其**针对开发者的特征极为明显**，会专门窃取：

* **SSH 密钥**
* **AWS、Azure、GCP 云平台凭证**
* **Kubernetes kubeconfig**
* **Docker 配置**
* **npm、Git 账号**
* **GitHub CLI 主机配置**
* **Solana 密钥**
* **环境变量**

同时还会搜刮 **ZeroClaw、PicoClaw、OpenClaw** 目录下的 AI 智能体数据。若获得完全磁盘访问权限，还会窃取受苹果数据保护类别的备忘录、iMessage、Safari 历史记录、邮件与苹果账号数据库。

对于无法通过 SQLite 直接提取的 Cookie，恶意软件会利用 Chrome DevTools Protocol 启动无头浏览器，通过 `--remote-debugging-port` 程序化导出全部 Cookie。

![]()

所有窃取数据会打包为：

`[国家码]用户名_持久ID.tar.gz`

并通过多重渠道外发：

* 直接上传至 `trackpipe[.]dev`
* 小文件通过 Telegram Bot API
* 大文件通过 GoFile.io

随后，攻击者会在 Telegram 收到格式化的 **GhostLoader 报告**，汇总密码、支付信息、自动填充条目、钱包、助记词、SSH 密钥、权限状态、持久化方式与 AI 智能体信息。

---

### 从信息窃取器升级为持久化 RAT

完成首轮搜刮后，GhostLoader 会在后续启动时**切换为持久化远程控制木马（RAT）模式**。

它会向 C2 面板注册上线，获取 Telegram 配置，随后启动多项监控，包括**每 3 秒扫描一次剪贴板**，实时抓取：

* 加密货币密钥
* AWS 密钥
* OpenAI、Stripe API 密钥
* 助记词

![]()

RAT 大约每 25 秒（带抖动）向 C2 轮询指令，支持：

* 执行系统命令
* 更新载荷
* 重新采集数据
* 任意目录外发
* 启动 / 停止 SOCKS5 代理
* **克隆浏览器配置文件**

其中 **CLONE\_START** 指令尤其危险：

它会复制完整浏览器配置，启动带远程调试的无头 Chromium，将 CDP WebSocket 转发回 C2，**使攻击者直接获得已登录的浏览器会话，无需任何密码**。

为对抗安全人员分析，GhostLoader 采用多种规避手段：

* 独立进程 + 伪装进程名
* 自动清理临时载荷
* 隐藏在 `.npm_telemetry` 目录
* 外发后自动清空窃取目录
* 支持 **NUKE 自毁指令**，一键清除启动项、定时任务、临时文件与安装目录

JFrog 表示，**@openclaw-ai/openclawai** 已被 JFrog Xray 与 JFrog Curation 拦截，可降低使用其软件供应链安全产品的企业的感染风险。

建议企业：

* 仅使用官方可信源的 OpenClaw 版本
* 部署自动化审核与 SCA 工具，在安装前识别恶意行为

已安装该包的开发者应**彻底清理持久化项**（Shell 配置、定时任务、守护进程），结束 `npm_telemetry / monitor.js` 进程，删除 `.npm_telemetry` 目录，卸载恶意包，并**考虑全盘重装系统**。

由于 GhostClaw 利用了开发者对工具链的信任，企业应对满足以下任一特征的 npm 包保持高度警惕：

* 请求系统密码
* 使用 `postinstall` 钩子进行全局安装
* 安装阶段下载远程加密载荷

---

### 入侵指标（IOC）

| 指标 | 内容 |
| --- | --- |
| 包名 | @openclaw-ai/openclawai |
| 类型 | NPM |
| 版本 | 1.5.15、1.5.14 |
| XRAY-ID | XRAY-949975 |
| C2 域名 | hxxps[://]trackpipe[.]dev |
| 引导路径 | /t/bootstrap?t=fafc0e77-9c1b-4fe1-bf7e-d24d2570e50e |
| 活动 ID | complexarchaeologist1 |
| 安装目录 | ~/.cache/.npm\_telemetry/ |
| 执行文件 | monitor.js |
| 临时文件 | /tmp/sys-opt-\*.js |
| Shell 注释 | # NPM Telemetry Integration Service |
| Cron 注释 | # Node.js Telemetry Collection |
| 加密算法 | AES-256-GCM（16 字节 IV，16 字节校验标签） |
| IP 查询 | hxxps[://]ipinfo[.]io/json |
| 备用上传 | GoFile.io API |
| 数据外发 | Telegram Bot API、C2 面板 |
| 环境变量 | NODE\_AUTH\_TOKEN、NODE\_CHANNEL、NPM\_CONFIG\_TAG、GHOST\_RECOLLECT、GHOST\_TG\_CONFIG |

本文翻译自gbhackers [原文链接](https://gbhackers.com/ghostclaw-masquerades-as-openclaw/)。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**安全客**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/315116](/post/id/315116)

安全KER - 有思想的安全新媒体

本文转载自: [gbhackers](https://gbhackers.com/ghostclaw-masquerades-as-openclaw/)

如若转载,请注明出处： <https://gbhackers.com/ghostclaw-masquerades-as-openclaw/>

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [安全资讯](/tag/%E5%AE%89%E5%85%A8%E8%B5%84%E8%AE%AF)
* [网络攻击](/tag/%E7%BD%91%E7%BB%9C%E6%94%BB%E5%87%BB)

**+1**0赞

收藏

![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)安全客

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p3.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p4.ssl.qhimg.com/t010857340ce46bb672.jpg)](/member.html?memberId=171771)

[安全客](/member.html?memberId=171771)

这个人太懒了，签名都懒得写一个

* 文章
* **1080**

* 粉丝
* **6**

### TA的文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37

### 相关文章

* ##### [侧边栏里的间谍假冒AI浏览器插件窃取90万用户数据](/post/id/315092)

  2026-03-11 14:01:17
* ##### [Kubernetes安全预警Ingress-Nginx注入漏洞可致集群密钥全局泄露](/post/id/315095)

  2026-03-11 14:00:47
* ##### [Budibase存在高危漏洞 可导致生产环境密钥全面泄露](/post/id/315099)

  2026-03-11 14:00:25
* ##### [Radware推出Alteon Protect实现云级ADC应用安全防护](/post/id/315102)

  2026-03-11 14:00:03
* ##### [研究人员打造AI智能体 可全自动实施诈骗通话](/post/id/315106)

  2026-03-11 13:59:37
* ##### [黑客利用微软Teams诱骗员工开放远程访问权限](/post/id/315110)

  2026-03-11 13:59:13
* ##### [微软推出365 E5升级套件与Agent 365 AI管控平台](/post/id/315113)

  2026-03-11 13:58:42

### 热门推荐

文章目录

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)