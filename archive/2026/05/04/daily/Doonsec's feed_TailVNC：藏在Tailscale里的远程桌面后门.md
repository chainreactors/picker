---
title: TailVNC：藏在Tailscale里的远程桌面后门
url: https://mp.weixin.qq.com/s/qnvikKbi58ShreoHwnz_0A
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:30.960843
---

# TailVNC：藏在Tailscale里的远程桌面后门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibelkJBCoLG2ibBuiaSXUbwQttgdKQqicx2yOY6EbrQu98gcJoL6sl2ib1IgUZibX1lfsc1vrfMhL7ZVCCkBB78ibHfC3I3FJKXkibLbso/0?wx_fmt=png&from=appmsg)

# TailVNC：藏在Tailscale里的远程桌面后门

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> TailVNC 把 VNC 服务端和 Tailscale 节点打包成一个 exe，走 WireGuard 加密的网状网络，不暴露任何端口就能远程桌面。适合正经运维，也适合红队搞持久化。能绕过 Windows 会话隔离、跟踪登录屏和 UAC 桌面、注入 Ctrl+Alt+Del，甚至剪贴板同步。

## 01 这工具是干嘛的

Windows 远程桌面的老问题——端口暴露、网络配置麻烦、容易被扫。TailVNC 的思路很简单：走 Tailscale 的 mesh 网络，利用 WireGuard 加密，连端口都不用开。编译时把认证信息写死进二进制，扔到目标机上用 SYSTEM 权限跑起来，就能在任何地方用 VNC 客户端连过去。

灵感来自 SockTail（https://github.com/Yeeb1/SockTail），但 TailVNC 把功能做得更全。

## 02 核心功能拆解

TailVNC 有几个挺狠的设计：

* **Tailscale/Headscale 集成**

  ——直接用 `tsnet` 把 WireGuard 对等节点塞进二进制。既支持官方 Tailscale 坐标，也能用自建的 Headscale 控制平面。
* **绕过 Session 0 隔离**

  ——当以 SYSTEM 运行时，自动通过 `CreateProcessAsUser` 在活跃用户会话里拉起一个 agent 进程，通过 IPC 转发 VNC 流量，绕过 Vista 及之后系统的会话隔离。
* **动态桌面跟踪**

  ——不管你切到默认桌面、登录屏、UAC 安全桌面还是锁屏，它都能用 `OpenInputDesktop`/`SetThreadDesktop` 跟过去。
* **Ctrl+Alt+Del 注入**

  ——从 Session 0 通过 `sas.dll!SendSAS` 发送安全注意序列。
* **双向剪贴板同步**

  ——Latin-1 编码的剪贴板在 VNC 客户端和目标机之间互通。
* **编译时配置嵌入**

  ——认证密钥、VNC 密码、监听端口、控制 URL 全在编译时通过 `LDFLAGS` 注入，运行时不需要任何配置文件。
* **认证密钥混淆**

  ——Tailscale auth key 在构建时用 XOR 混淆，防止二进制里明文暴露。

## 03 架构一句话讲清楚

全局就两个进程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibelkJBCoLG2ibBuiaSXUbwQttgdKQqicx2yOY6EbrQu98gcJoL6sl2ib1IgUZibX1lfsc1vrfMhL7ZVCCkBB78ibHfC3I3FJKXkibLbso/640?wx_fmt=png&from=appmsg)

Session 0 里跑一个服务进程，管理 tsnet 网络、监听 VNC 端口（默认 5900 只绑 Tailscale 接口）、轮询当前控制台会话。检测到会话变化或 agent 崩溃，就自动重启 agent。agent 跑在用户会话里，负责 GDI+ 截图（约 30fps）、`SendInput` 模拟键盘鼠标、以及剪贴板监控。

通信走 TCP 双向代理，Agent 监听 `127.0.0.1:15900`。

## 04 技术栈一览

| 组件 | 技术 |
| --- | --- |
| 语言 | Go 1.25+ |
| 网络传输 | Tailscale tsnet（嵌入式 WireGuard 对等节点） |
| VNC 协议 | RFB 3.008（自实现，Raw 编码） |
| 屏幕捕获 | Windows GDI+（CreateDIBSection, BitBlt） |
| 输入注入 | Windows SendInput API |
| 会话管理 | WTSQueryUserToken + CreateProcessAsUser |
| 桌面切换 | OpenInputDesktop + SetThreadDesktop |
| SAS 注入 | sas.dll!SendSAS |
| VNC 认证 | DES challenge-response（RFB 标准） |
| 密钥混淆 | XOR + 十六进制编码 |
| 系统调用 | golang.org/x/sys（Windows syscall 封装） |
| 二进制压缩 | UPX（可选） |
| 构建系统 | GNU Make + Go LDFLAGS 注入 |

## 05 编译与配置

先准备好环境：Go >= 1.25.3、GNU Make、UPX（可选）。关键一步是去 Tailscale 管理后台生成一个 auth key，建议用可复用 + 临时密钥。

构建参数：

| 参数 | 是否必需 | 默认值 | 说明 |
| --- | --- | --- | --- |
| AUTH\_KEY | 是 | — | Tailscale 认证密钥，编译时自动 XOR 混淆嵌入 |
| LISTEN\_PORT | 否 | 5900 | VNC 监听端口（只绑 Tailscale 接口） |
| AUTH\_PASS | 否 | 空（无认证） | VNC 连接密码（DES challenge-response） |
| CONTROL\_URL | 否 | 空（官方 Tailscale） | Headscale 控制平面 URL |
| CONFIG\_DIR | 否 | C:\Windows\Temp\.cache | tsnet 状态目录（存放 WireGuard 密钥、节点身份） |

编译命令举个栗子：

# 最简构建——只提供 auth key
make build-vnc AUTH\_KEY=tskey-auth-kBEXAMPLEKEY

# 完整构建——所有参数都写上
# [CONTROL\_URL] 可选，用自建 Headscale 时才需要
# [CONFIG\_DIR] 可选，覆盖默认状态目录
make build-vnc \
  AUTH\_KEY=tskey-auth-kBEXAMPLEKEY \
  LISTEN\_PORT=5900 \
  AUTH\_PASS=VNCPassword \
  [CONTROL\_URL=https://headscale.example.com] \
  [CONFIG\_DIR='C:\Windows\Temp\.cache']

产物在 `dist/` 目录下，叫 `TailVNC-windows-amd64.exe`。

构建管道干这几件事：清除旧产物 → 下载 Go 依赖 → 用 `obfuscator/` 混淆 auth key → 通过 LDFLAGS 注入所有配置 → 剥掉符号表和 DWARF 调试信息（-s -w）→ 如果装了 UPX 就压缩（--best --lzma）。

其他 Make 目标：

make clean    # 清理构建产物
make deps     # 下载并整理 Go 模块
make help     # 打印使用帮助和参数说明

## 06 怎么用

TailVNC 必须用 SYSTEM 权限跑。如果在 Session 0 下运行（比如作为服务或 SYSTEM 上下文），它会自动检测当前控制台会话，在用户会话里拉起 agent 进程，然后代理所有 VNC 流量。如果直接在用户交互会话里启动，它会进入本地模式，不走 agent 代理层。

运行后目标机会加入配置的 Tailscale 网络，显示为一个新节点。打开任意标准 VNC 客户端，连接它的 Tailscale IP 加端口即可：

:5900

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfT16sibbQsMpehXu0IxY7v8ZWbUNmhs8f8PFbWTXNEzpEMDzF7Y9z0DTINVqIyBViaibCT7iaulHcTdGTiasn3qLZsspDw2PshJ16A/640?wx_fmt=png&from=appmsg)

▲ 连接后的 VNC 界面

## 07 优缺点和适用场景

**优点**：

* 零端口暴露，完全走 Tailscale 加密隧道，防火墙不用动。
* 编译时配置注入，无文件落地风险，适合红队持久化。
* 能跟到登录屏、UAC 安全桌面、锁屏，甚至注入 Ctrl+Alt+Del，比大多数 RAT 都强。
* 剪贴板同步，操作顺手。

**缺点**：

* 必须依赖 Tailscale/Headscale 网络，断网就没招。
* 需要 SYSTEM 权限才能发挥全部功能，普通用户跑不了会话跟踪。
* VNC 协议本身没加密（虽然走 Tailscale 隧道已经加密了），如果自己改端口要注意。
* 二进制编译时参数固定，一次编译只能针对一个目标。

适合场景：内网渗透时做持久化后门、远程运维被控主机、或者红蓝对抗中需要隐蔽的桌面控制。正经运维也可以拿来当紧急跳板，前提是你已经有 Tailscale 网络。

推荐指数：★★★★☆（扣一星因为依赖外部协调服务，而且编译流程略复杂）

**获取方式：私信回复"TailVNC"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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