---
title: Claude Desktop Connection Refused 故障排查以及本地 VM runtime 剖析
url: https://mp.weixin.qq.com/s/nV55I6Vh6Ea1qzogvJ9voA
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:01:11.462313
---

# Claude Desktop Connection Refused 故障排查以及本地 VM runtime 剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0UKPAuBeu7nq1BHv7S87C1D9TOJuAkpZudmjib7ltdggKAXW0LqoePCoxVbLyyyU3DKMUf3Xs5C7OE8WdtfiaY9QA6Ax6rPsmhVMdF2I5EDQg/0?wx_fmt=jpeg)

# Claude Desktop Connection Refused 故障排查以及本地 VM runtime 剖析

CSL
CSL

联想全球安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

Anonymous

事情起因很普通：在日常使用中，Claude Desktop（桌面端）在某次升级后发现 Cowork 模式下发消息突然失败，UI 界面弹出了一条极无信息量的报错：

API Error: Unable to connect to API (ConnectionRefused)

然而，奇怪的是，同一台机器上命令行版的 claude CLI 运行完全正常。既然 CLI 能连通，说明网络本身、账号与云端模型服务都没有问题。差别在于，Desktop 版本在后台多了一套极为复杂的本地执行层。

本文将沿着两条线索展开：先定位并修复这次连接失败的子进程链路，再深入解密 Claude Desktop 背后一整套由 macOS 虚拟化框架、gVisor 用户态网络及动态文件挂载组成的**本地虚拟机（VM）运行时。**

PART

**01**

**定位与修复ConnectionRefused****链路**

**进程链路诊断**

虽然同一台机器的 CLI 正常，但 Claude Desktop 在 Cowork 模式下并非直接调用 Node 脚本，而是通过一个包装程序启动 local Claude Code 进程。

其关键进程链路如下：

```
Claude Desktop (宿主机 UI)  └── Helpers/disclaimer (Mach-O 包装器)        └── local Claude Code (Node 进程) -> HTTPS/TLS 请求
```

通过阅读 Desktop 侧的日志，可以抓到 sdkOptions after patch 暴露的环境变量：

```
executable: '/Applications/Claude.app/Contents/Helpers/disclaimer'executableArgs: ['/Users/<user>/Library/Application Support/.../claude']envKeys: ['ANTHROPIC_BASE_URL', 'ANTHROPIC_CUSTOM_HEADERS', 'NODE_EXTRA_CA_CERTS']
```

disclaimer 作为一个 Mach-O 格式的 spawn wrapper，封装了 Desktop 和 local Claude Code 之间的调用。

**根证书信任链修复**

本次故障的原因与证书链有关：在需要自签名证书或中转网关的公司/测试网络环境下，由**disclaimer**启动的 local Claude Code 进程没有继承主机的 Node TLS 根证书，导致与 ANTHROPIC\_BASE\_URL 握手时因为证书无法信任而被拒绝。

由于 disclaimer 是个二进制包装程序，最直接的修复方式是将其重命名，并用一个同名的 Shell 脚本代理它，在 spawn 子进程前将 CA 证书注入环境变量：

```
#!/bin/shroot_ca="$HOME/.claude-root-ca.crt"if [ -r "$root_ca" ]; then  export NODE_EXTRA_CA_CERTS="$root_ca"fiexec "$@"
```

替换此入口后，Desktop 的网络请求恢复正常，日志中的 turn cycle 状态重回 healthy。

**服务端扣费但本地判失败的“误判点”**

调试中还遇到了一个有趣的现象：偏偏本地报 ConnectionRefused错误，但模型服务端已经扣除了 Token 费用。

这是因为 Desktop 触发对话时，发送的不是句简单的 hello，而是一个多路并发请求：

* **旁路请求（Side Request）**：使用较轻的模型（如 Sonnet 4），用于生成标题、能力测试或生成 ack。
* **主请求（Cowork Turn）**：使用主模型（如 Opus 4-8），向云端大模型发起的推理请求中附带了多达 50 多个本地工具声明 and 长上下文。

在发生证书错误时，旁路轻量请求可能勉强握手成功并产生了 Token 消耗；但最关键的主 turn 请求在接收 SSE（服务器发送事件）数据流时，因为 local Claude Code 自身的 Node TLS 校验不完整而单方面中断了连接（error\_status = null，即连接层错误），导致 UI 报错与服务端计费同时成立。

PART

**02**

**解密后台的虚拟机（VM）****运行时**

一旦解决了网络请求的信任链，我们再把目光投向 Cowork 模式最核心的魔鬼细节：**在 macOS 桌面端下，运行模型下达的 shell 命令的那个沙箱，到底长什么样？**

**![](https://mmbiz.qpic.cn/mmbiz_png/0UKPAuBeu7mab1ZJsX36icglI5Z0C7djhxyaQTr0uUjp1UJwXmGiaIq3te8ZLbdYvnByWa0ntx1xBtcmgC7jKEx9SzY51DmnsjbYYEGibp662Q/640?wx_fmt=png&from=appmsg)**

**VM捆绑包与底层虚拟化**

在 macOS 路径下，可以找到 Claude Desktop 的虚拟机包：

~/Library/Application Support/Claude-3p/vm\_bundles/claudevm.bundle

该目录下包含如下关键文件：

* rootfs.img（一个约10GB的GPT格式磁盘镜像，包含 EFI 分区与标准的Linux ext4根文件系统
* vmIP（静态分配的虚拟机 IP：172.16.10.3）
* gvisorMacAddress(02:00:00:00:00:01)

通过运行时进程 and 插件分析，Claude 桌面端加载了 Swift 插件 swift\_addon.node，该插件动态链接了 macOS 系统的 Virtualization.framework 与 vmnet.framework。

也就是说，Claude Desktop 确实是在 macOS 后台启动了一个真正完整的轻量化 Linux 虚拟机，用作隔离的本地工具执行沙箱。

**降权的用户执行环境**

当模型在对话里调用**Bash** 跑脚本时，如果直接用 root 权限运行，一旦指令存在恶意越权行为，后果严重。

阅读 coworkd.log 日志可以看到，系统在启动 VM 时，会通过 useradd 动态创建一个临时用户：
useradd -m -d /sessions/<session-user> -s /bin/bash <session-user>

* 虚拟机内部由高权限 of coworkd 守护进程管理环境
* 大模型下达并被本地拉起的 mcp\_\_workspace\_\_bash 工具，实际上是在虚拟机里通过 oneshot-bash 降权运行在 UID/GID 为 1004/1004的 <session-user> 普通用户下，且该用户不在 sudo 组中，实现了安全的特权隔离。

PART

**03**

**VM目录共享与网络托管机制**

既然命令行工具是在 Linux 虚拟机里执行，那么 VM 是如何读写我们 macOS 本地项目里的代码的？并且它是如何连网的？

**动态目录共享与主客机路径映射**

本地目录进虚拟机采用的是 Apple Virtualization 的目录共享技术（类似 virtiofs）。

在虚拟机内部，只读挂载了主机的根共享点 /mnt/.virtiofs-root 。为了防止模型随意读取不该读的文件，Desktop 实施了**基于单次命令的动态子目录挂载与主客机路径映射（Path Mapping）：**

* 当用户向对话授权某个目录（如 ~/Downloads）时，HostLoop 记录该授权；
* 当模型触发 mcp\_\_workspace\_\_bash 时，coworkd 临时将主机的 Downloads 目录以读写形式挂载到虚拟机内的 /sessions/<session-user>/mnt/Downloads 下；
* 命令执行完毕后，挂载点被立即卸载。

由于主机与虚拟机路径不同，Desktop 内部包含了一个 pre-tool hook 路径混用拦截机制。在解包 Desktop 的 app.asar（对应构建后的 index.js ）后可以发现，代码中包含了一个针对模型工具调用的 pre-tool hook 拦截器。当模型尝试将虚拟机路径（ /sessions/... ）传给宿主机侧的工具（如 `Read` / `Edit` / `Write`）时，该机制会在工具执行前直接拦截，并返回明确的警告提示，迫使模型区分环境并自行修正路径，从而避免跨系统文件操作失败：

**Host 工具**必须且只能使用宿主机路径（ /Users/<user>/Downloads ）。

**VM Bash** 必须且只能使用挂载路径（ /sessions/<session-user>/mnt/Downloads ）

**精确的虚拟机沙箱安全边界**

在启动 local Claude Code 时，桌面端会向其传递受管的安全沙箱设置（sandbox 配置）

* **命令执行边界（**`allowUnsandboxedCommands: false`**）：**

系统强行禁止在宿主机（macOS）直接执行非沙箱命令。这确保了模型下达的所有 shell 操作必须被路由进物理隔离的 Linux 虚拟机中执行，保护了物理机的安全。

* **网络出网边界（**`network.allowedDomains` & `allowManagedDomainsOnly: true`**）：**

这套沙箱网络限制作用于虚拟机内部。gVisor 配合 Desktop 宿主程序在网络出口层级，将虚拟机内所有命令（如 curl、git、npm 等）的连接去向严格锁定在 allowedDomains（如 api.anthropic.com 或指定的内部托管网关）之内。这正是作者总结的“这不是一个 VM 随便出网的模型，由 Desktop 控制 allowed domains”。如果在沙箱内部执行命令连往未授权的外网服务器，其网络流量会被在出口处拦截阻断。

PART

**04**

**总结与技术边界的代价**

Claude Desktop Cowork 的这套架构展示了极其严密的安全设计边界：

* **Shell 隔离：**使用隔离 of Linux 虚拟机限制系统命令对物理机（macOS）的直接危害。
* **目录隔离：**通过单次命令动态挂载与 ro/rw 细粒度控制防本地文件被过度读取。
* **API 与网络隔离：**宿主机控制网络出口，通过 gVisor 强行拦截并限制 allowed domains 白名单，把数据外泄的风险降到最低。

这种将“本地执行”和“虚拟机容器”深度融合的思路非常激进，但也带来了显著的**排查与维护代价。**

在命令行 CLI 时代，遇到连接报错我们只需要排查环境变量 and 本机的代理。而在 Desktop 时代，一旦出现类似 ConnectionRefused 或是 Something went wrong 的错误，开发人员和安全研究者必须依次排查：Electron 进程链 -> Disclaimer 包装器 -> HostLoop 调度 -> Workspace MCP -> 虚拟机运行状态 -> gVisor 网络栈。这也标志着 AI 助理在本地的落地，已经从单纯的“应用开发”演变成了“本地微型分布式沙箱系统”的运维与调试。

<<<  END >>>

**往期精彩合集**

● [从几类典型案例看攻击溯源与钓鱼风险防范](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493950&idx=1&sn=0a5ea7e33288b90816dc11189a46236e&scene=21#wechat_redirect)

● [Cloudflare Dynamic Workers 与 Workflows： 边缘计算正在从“部署代码”走向“运行时代码”](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493916&idx=1&sn=c869da94452f053c6bf3f6b4e8de6784&scene=21#wechat_redirect)

● [AI时代下的DevSecOps：安全开发如何跑出“机器速度”？](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493855&idx=1&sn=6e17d9005a51b94b139dc72a7a728295&scene=21#wechat_redirect)

● [调研完10+开源AI渗透工具：离真正自动化还差得很远](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493831&idx=1&sn=748effeaf8a858478d50e3bc78487b2c&scene=21#wechat_redirect)

● [后端安全不是玄学：从编码到上线的8条安全底线](https://mp.weixin.qq.com/s?__biz=MzU1ODk1MzI1NQ==&mid=2247493803&idx=1&sn=8b7f3f8f07fea587a8e158a0f8d67962&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/0UKPAuBeu7nVx0rtdjntQiaQNzTPlkZvWLUjPUTgmQJryZH5w8pM11sIDpmGk6utnAveGKNEJYSgSaZ1gwLcbYEQeC1rlqO7OMzsYGiaYXnsA/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

联想全球安全实验室

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PicDhHpwdziaibPZd0FJCTel2o5j0mRe7AsGTibmwUbRoonkSFQBNETSL4jqgjKSCE7z3B8KeR9q94miagM69SFsB3A/0?wx_fmt=png)

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