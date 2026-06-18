---
title: 威胁情报｜Arch Linux AUR 供应链投毒关联恶意 npm 包分析
url: https://mp.weixin.qq.com/s/5PDUz76xWA-AWN9BSu28Dg
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:48:33.343973
---

# 威胁情报｜Arch Linux AUR 供应链投毒关联恶意 npm 包分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8z8bibAexaCIYzJlpwwcK1Zo40IaQKgQZGPOg0Xh3uMw6FibBickZ0slsUbbXAXI2Mic7JrlnvBRgct99nO3v6eHUqufJibHNkLXibTwUOrFfGibvg/0?wx_fmt=jpeg)

# 威胁情报｜Arch Linux AUR 供应链投毒关联恶意 npm 包分析

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

******************# 背景********

************2026 年 6 月，Arch Linux AUR 生态曝出大规模供应链投毒事件，Sonatype 将该活动命名为 "Atomic Arch"。此次事件并非 Arch Linux 官方仓库、pacman、AUR helper 或 Arch Linux 本身存在零日漏洞，而是攻击者滥用 AUR 孤儿包认领机制，合法接管长期无人维护但仍被用户信任的包，并修改其 PKGBUILD 或安装脚本。

当用户执行常规 AUR 安装或升级操作时，恶意脚本会调用 npm 或 Bun，安装攻击者控制的 JavaScript 包，并借助 npm 生命周期钩子执行 Linux ELF 载荷。该载荷主要面向 Linux 开发者工作站和构建环境，具备窃取 GitHub、npm、SSH、Docker/Podman、Vault、浏览器数据及 shell 历史等敏感信息的能力。

公开披露阶段，受影响 AUR 包数量已从早期 400 余个扩大到约 1,500 个。该事件表明，开源生态中"无人维护但仍被信任"的组件，正在成为攻击者串联构建脚本、包管理器生命周期钩子和开发者本地环境的新型供应链入口。

本文基于 MistEye 对 `runescape-launcher`、`atomic-lockfile@1.4.2` 和 `js-digest@4.2.2` 的静态分析结果，梳理此次攻击链的关键技术环节。上述样本并非全部攻击样本，而是用于揭示攻击模式的技术剖面。**

# MistEye 响应**********

**********#

MistEye 是由 SlowMist 自主研发的 Web3 威胁情报与动态安全监控系统，集成了安全监控与情报聚合能力，为用户提供实时的风险预警与资产守护。

在此次 Arch Linux AUR 供应链投毒事件中，MistEye 对相关恶意包、npm 依赖、ELF 载荷、C2 通信及二阶段下载等攻击链环节进行了分析与关联研判，并提取相关 IOC。基于分析结果，MistEye 已向客户推送高危风险告警与威胁情报通告，协助客户及时识别和处置相关供应链风险。情报详情：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCI4JicRH2OFVicEnf0YLRwB2lS4y2tNiauMOzl6U0QiaABQENyHo8I7QR6T324dZicPcWmqzicwEq0a59yYbzufm9icAARbaAZ0xPyiaTM/640?wx_fmt=png&from=appmsg)

以下为详细技术分析。

# 攻击链分析：AUR install scriptlet 到 npm 生命周期脚本**********

**********#

本次攻击的技术主线可概括为三层递进：攻击者通过接管 AUR 包并篡改构建/安装脚本，在 pacman 安装或升级阶段触发 npm install 拉取恶意包，随后利用 npm 生命周期脚本(preinstall) 自动执行嵌入包内的 Linux ELF 原生载荷。以下按三层逐一展开。

第一层：AUR install scriptlet 转交执行权给 npm

以 runescape-launcher 包（版本 2.2.12-1）为例。攻击者在 .SRCINFO 和 PKGBUILD 中引入了对 install.sh 的引用，并将 npm 声明为运行依赖。

.SRCINFO 中的关键声明：

********```
pkgbase = runescape-launcher pkgver = 2.2.12 pkgrel = 1 install = install.sh depends = npm
```********

PKGBUILD 中的对应声明：

********```
depends=(      'npm'      cairo      libgcc      ...      zlib ) install="install.sh"
```********

install.sh 是一个 pacman install scriptlet 文件。攻击者在该文件中定义了 post\_install() 函数，并将 post\_upgrade() 指向同一个函数：

![标题: fig:](https://mmbiz.qpic.cn/mmbiz_png/8z8bibAexaCLqoFOjBypOzMqEiaLvic77mel1Q6CL5a9Z3BHzia1vjf7Rwh0uI1p9LQRRBOIp9DS1EJx7ibiaKbD36e8SJwicnM996ObDvyRRXhibJE/640?wx_fmt=png&from=appmsg)

关键执行链如下：

.SRCINFO 声明 install = install.sh 和 depends = npm
   → PKGBUILD 同步声明 install="install.sh" 和 depends=('npm' ...)
   → makepkg 把 install.sh 打进最终 pacman 包
   → pacman 首次安装时调用 post\_install()
   → pacman 升级时调用 post\_upgrade()
   → post\_upgrade() 调用 post\_install()
   → post\_install() 进入 /tmp
   → 执行 npm install atomic-lockfile commander chalk
   → npm 安装 atomic-lockfile@1.4.2
   → 触发 atomic-lockfile 的 preinstall
   → 执行 Linux x86-64 ELF 载荷 src/hooks/deps

需要注意几点：commander 和 chalk 是 npm 上的合法流行包，不一定是恶意包；同一 post\_install() 中还存在原有/伴随的 setcap 逻辑，恶意新增点是 cd /tmp 与 npm install atomic-lockfile commander chalk。

该层的核心设计意图是：将 pacman 的包安装/升级生命周期作为跳板，把执行权从系统包管理器转交给 npm，且首次安装和升级时均会触发。

第二层：npm lifecycle 触发原生 ELF——atomic-lockfile@1.4.2

atomic-lockfile@1.4.2 是本次攻击中首波使用的确认恶意 npm 包。该包表面上伪装为文件锁工具库，保留了完整的 TypeScript/JavaScript 库结构、main/module/exports 入口、CLI 和类型定义。但攻击者在 package.json 的 scripts.preinstall 中配置了安装期自动执行原生二进制：

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIMFPG6viajH8rMTic3znOZqIdh2sPLicHREqCjseC0bz8HF9MxvoCcEBV2L3hJdnAGSVPNNyIPhFVZId4zFib6ian2MvA33zxt5HRk/640?wx_fmt=png&from=appmsg)

src/hooks/deps 并不是普通的依赖安装脚本，而是一个剥离了符号表的 Linux x86-64 PIE ELF 可执行文件。关键元数据：

* 文件路径：src/hooks/deps
* 文件类型：ELF 64-bit LSB pie executable, x86-64, dynamically linked, stripped
* ELF SHA-256：6144d433f8a0316869877b5f834c801251bbb936e5f1577c5680878c7443c98b
* 大小：3,040,376 bytes
* 动态依赖：libbpf.so.1、libm.so.6、libc.so.6
* 内嵌 eBPF object SHA-256：3607de2597f8955f9a88f36ee43b64d3891b8ef536e99fa098e80169350f7b01
* 内嵌 eBPF object 偏移：0x324f9
* 原始 tarball SHA-256：64bc53032ecfbf4e25d0191d75321821ba2ae01bdb123b4c8c2ebd12161253fc

该 ELF 载荷的能力覆盖凭据采集、持久化、分通道通信/上传，以及在 root 或具备相应 capability 的条件下尝试启用 eBPF 隐身组件，以下逐一展开。

重复异或解码与 Tor 隐藏服务 C2

在 atomic-lockfile@1.4.2 的 ELF payload 中，关键 C2 并未以明文字符串形式出现，而是通过 repeating-XOR 编码后存储。样本在 0x1aa60 偏移处嵌入 32 字节 key，在 0x2da96 偏移处存储 62 字节 ciphertext。解码方式为：

********```
plain[i] = cipher[i] ^ key[i % 32]
```********

解码后得到 Tor v3 hidden service 地址：

olrh4mibs62l6kkuvvjyc5lrercqg5tz543r4lsw3o6mh5qb7g7sneid.onion

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCIZwYGztXhle6Nnn3ibZW81aX8uBVGT8MwPYCYibMqdgEHVJLVs0QG3owF9fuwRaaTPktBqeqBJ0SMkhUbeMz3mC0Bj5ROD1cmEM/640?wx_fmt=png&from=appmsg)

62 字节长度正好对应 56 字符 Tor v3 onion hostname 加上 .onion 后缀。除 C2 host 外，样本还使用相同思路编码了 agent 标识和版本：

* agent 名称：atomic，key offset 0x1bc60，cipher offset 0x3fddf
* agent 版本：0.8.2，key offset 0x1c900，cipher offset 0x3fde5

这一设计使得完整 C2 不会出现在普通 strings 输出中。因此，仅依赖 strings | grep .onion、明文 YARA 规则或简单 IOC 提取流程，可能无法发现该 hidden service C2。

Tor/SOCKS 通信链路

虽然 C2 host 被 XOR 编码隐藏，但 ELF 中仍可见 SOCKS/Tor 相关明文字符串，例如：

********```
socks CONNECT resp: socks greeting read: socks CONNECT write: socks CONNECT failed: rep= socks5 auth rejected: /tor-expert-bundle-
```********

这些字符串结合解码出的 .onion 地址，说明该 payload 内置了通过 SOCKS/Tor 访问 hidden service C2 的通信框架。

同时，ELF 中还存在 HTTP 请求构造与上传相关字符串，包括 POST、GET、HTTP/1.0、HTTP/1.1、Host:、Content-Length:、Content-Type: application/json、Content-Type: application/octet-stream、POST /upload HTTP/1.1 与 Content-Type: multipart/form-data 等。POST /upload 与 multipart 模板说明 payload 具备上传构造能力，但是否对应 temp.sh 服务及是否实际外传仍需动态流量、代理日志或主机取证证据确认。

凭据与开发环境采集面

**该 ELF 的凭据采集面覆盖了现代开发者工作站的多个关键凭据存储点。

远程平台凭据方面，载荷包含 GitHub token 验证与仓库枚举相关字符串——`GET /user`、`GET /user/repos`、`Authorization: Bearer`、`Accept: application/vnd.github+json`；npm token 验证字符串——`GET /-/whoami`、`registry.npmjs.org`、`\_authToken=`；以及 Vault 凭据相关字符串——`/.vault-token`、`X-Vault-Token:`。

即时通讯与协作工具方面，Slack 相关字符串包含 `auth.test`、`conversations.list`、`users.info` API 路径以及针对 `%.slack.com` 的 Cookie SQL 查询；Teams/Skype 方面包含 `X-Skypetoken:`、`authsvc.teams.microsoft.com` 和针对 `%teams.microsoft.com` 的 Cookie 查询；Discord 相关字符串如 `discord:` 也有出现。

本地与容器环境方面，载荷关注 `.ssh`、`known\_hosts`、`PRIVATE KEY`、`PuTTY-User-Key-File` 等 SSH 凭据文件，以及 `.bash\_history`、`.zsh\_history`、`.env` 和 Chromium 系列浏览器的 Cookie 与 Local Storage 路径。Docker/Podman 与 DevOps 工具相关字符串——包括 `docker login`、`docker push`、`docker pull`、`docker build`、`docker run`、`docker tag`、`docker-compose`、`podman login`、`podman push` 等——在 ELF 中出现，但当前仅能作为静态字符串线索，尚未确认完整采集链。`claude:` 字符串同样可作为 AI 工具相关线索，不能单独证明 Claude 数据采集。**

![标题: fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/8z8bibAexaCJrm2doAQrKtunBh4RuPds6kMic7rYoPVhRcj9iaztGxOzWRB6BiaXQfwuGibIvTRhias91cmMDOmqk1MicJjdr1AzhTQnbwGA2kNEm0/640?wx_fmt=png&from=appmsg)

上传与二阶段下载

载荷包含 HTTP multipart 上传模板，以及 /var/tmp、/secrets 等数据暂存路径。样本具备通过 onion C2 进行任务/结果通信和构造 multipart 上传请求的能力；是否对应 temp.sh 服务、是否在具体受害主机成功上传或完成外传，需要动态执行、代理日志或主机取证证据确认。二阶段下载链路也留下了清晰的静态痕迹：/bin/sha256/ 和 sha256 fetch: 字符串指向二阶段 hash 校验路径；server returned empty binary 和 tmp 200 headers too large 说明存在二阶段下载失败的错误处理逻辑。Tor bundle 拉取痕迹 /tor-expert-bundle- 与 SOCKS 传输链路组合，构成 staging 下载线索。

疑似 cryptominer 线索

atomic-lockfile 的 ELF 中出现 /usr/bin/monero-wallet-gui 字符串。结合二阶段下载链路，推测载荷可能在二阶段拉取与 Monero 挖矿相关的二进制。当前样本内未确认 xmrig、randomx、stratum、矿池域名或钱包地址等强矿工特征，因此不能断言内置矿工本体。

持久化

样本中出现了 systemd 服务相关模板，覆盖用户级和系统级两类启动场景。这说明载荷具备将自身注册为系统服务、在重启或用户会话启动后继续运行的设计意图。

********```
/.config/systemd/user [Unit] [Service] ExecStart= Restart=always RestartSec=30 .service WantedBy=multi-user.target WantedBy=default.target
```********

 eBPF 隐身与反取证

**eBPF (extended Berkeley Packet Filter) 是 Linux 内核提供的一套机制，允许用户在不修改内核源码的前提下，向内核加载并运行受限制的自定义程序。它在正常用途下服务于网络过滤、可观测性和安全监控，但本次样本中的 eBPF 组件被设计为反方向的工具——不是用来"看"系统，而是用来"藏"自己。

`atomic-lockfile@1.4.2` 的 ELF 载荷 `src/hooks/deps` 依赖 `libbpf.so.1`，并通过 `bpf\_object\_\_open\_mem`、`bpf\_object\_\_load`、`bpf\_program\_\_attach`、`bpf\_map\_\_pin` 等 API 尝试加载内嵌的 eBPF relocatable object。这部分逻辑不会无条件执行：样本会先调用 `geteuid()` 检查是否为 root 用户，然后读取 `/proc/self/status`，解析其中的 `CapEff:` 字段，并测试与 `CAP\_BPF`、`CAP\_SYS\_ADMIN` 对应的 capability 位。更准确地说，权限条件...