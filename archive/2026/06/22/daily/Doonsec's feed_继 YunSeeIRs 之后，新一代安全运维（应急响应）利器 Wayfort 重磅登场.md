---
title: 继 YunSeeIRs 之后，新一代安全运维（应急响应）利器 Wayfort 重磅登场
url: https://mp.weixin.qq.com/s/5_Rze5OOSGxrg8T4pfGhcw
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:02:40.828705
---

# 继 YunSeeIRs 之后，新一代安全运维（应急响应）利器 Wayfort 重磅登场

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnAOeib5r0niaw7XxKO6HicGbibRrY441rv1KTxb67fiaUtn7zicatRqLI0dhSlTPUfRbOOgKvGCH4eic6l0yLpNUK1olcMso48C8OFicE/0?wx_fmt=jpeg)

# 继 YunSeeIRs 之后，新一代安全运维（应急响应）利器 Wayfort 重磅登场

原创

江思澄
江思澄

云晞科技Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 浏览器原生的特权访问管理平台（PAM）

---

觉得好用？给个 Star，是对我们最大的鼓励 ⭐![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmxCts9pJcjHZ7M1guAcJNhFKaicwdvfC1bbeJ2dW7ae87EYGsLicoeftcaGe9WTa2KnYrHH8n19KnU1SP0QPMKdocR86C02wOss/640?wx_fmt=png&from=appmsg)

### 你的运维工具箱，是不是也长这样？

登录一台 Linux，开 SecureCRT。 连一台 Windows 桌面，开 mstsc。 查一条 SQL，开 Navicat。 传个文件，开 WinSCP。 看对象存储，再登一次厂商控制台。

五种场景，五个客户端，凭据散落在各处。审计、录像、审批，每个工具一套说法，对不上账。

要是这些事，一个浏览器就能办完呢？

---

# 认识 Wayfort

![image-20260622230600618](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmroL7bkY7dpYOmYrDdPeBTV4QGGmfogMdd2MNkgFq6v2nyfFdxeXDiauceUX3cOBztLf1TiaarZYnAm7gfRV6xDfldDgYKwBAwc/640?wx_fmt=png&from=appmsg)

image-20260622230600618

Wayfort 是一款浏览器原生的特权访问管理平台。

不用装客户端，打开浏览器就能用。SSH、RDP、数据库、SFTP、对象存储，10 种协议共用一个入口，认证、审批、审计都在这里完成。

> *我们不想让运维在安全和效率之间二选一。*

### 四个数字，定义 Wayfort

| 10 | 0 | < 150ms | 100% |
| --- | --- | --- | --- |
| 统一接入协议 | 客户端安装 | 远程桌面首帧延迟 | 行为可审计率 |

---

### 一、十种协议，一个浏览器

![image-20260622230624925](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkZwndiatjMMIhlM1xNMxQTt9JibF6dtJGLtJIaNAf0qkEmMS3ZJdI9QdUWV1mJ7NuLib4rrRicBRnacnriaNconC98ZviagG47Pqj2g/640?wx_fmt=png&from=appmsg)

image-20260622230624925

字符终端、图形桌面、数据库、文件传输、对象存储，所有远程访问都收进同一个浏览器标签页。

| 协议 | 接入方式 | 会话录像 | 代理链 | 连接审批 |
| --- | --- | --- | --- | --- |
| **SSH** | xterm.js + WebGL 终端 | asciinema v2 + 命令审计 | ✅ | ✅ |
| **Telnet** | xterm.js 终端 | asciinema v2 | ✅ | ✅ |
| **RDP（新引擎）** | WebRTC 视频流 + WebGPU | H.264 + 输入时间线 | ✅ | ✅ |
| **RDP / VNC（Guacamole）** | guacamole-js 画布 | .guac（可转 MP4） | ✅ | ✅ |
| **数据库 CLI** | xterm.js 终端 | asciinema v2 | ✅ | ✅ |
| **DB Studio** | Monaco 编辑器 + 结果集 | 操作审计 + 写审批 | ✅ | ✅ |
| **对象存储（OSS）** | 文件管理器 + 在线预览 | 操作审计 | ✅ | ✅ |
| **SFTP** | 文件管理器 + 在线编辑 | 操作审计 | ✅ | ✅ |
| **TCP 端口转发** | 本地监听 / WS 隧道 | 元数据记录 | ✅ | ✅ |
| **匿名沙箱** | xterm.js Docker 容器 | asciinema v2 | — | — |

不用装客户端，现代浏览器打开就能用。

---

### 二、自研 WebRDP：把远程桌面真正做进浏览器

市面上的浏览器远程桌面，大多是在 Guacamole 上套一层壳。我们没走这条路，而是从底层写了一套完整的远程桌面引擎。

#### WebRTC 视频流传输

桌面画面以 VP9 视频流推到浏览器，不再逐帧搬运位图，延迟和带宽都明显降下来。需要时还能切到 AV1 编码，同等画质下比 VP9 再省 30–50% 带宽。

#### WebGPU 零拷贝渲染

像素直接交给 GPU 处理，CPU 几乎不参与。4K 高 DPI 屏幕下也不卡。

#### FreeRDP + IronRDP 双引擎

两套后端按需切换：FreeRDP 兼容性最广，IronRDP 用 Rust 写成，性能和内存安全更有底。

#### 动态分辨率 1:1 映射

浏览器窗口多大，远程桌面就铺多大。缩放、高 DPI、多显示器都原生支持，画面不糊，也不留黑边。

#### 个人文件驱动器

每个用户有一个独立的持久化文件夹，自动挂到远程桌面的「此电脑」里。浏览器上传的文件，远程桌面直接打开；远程桌面里的文件，也能拉回浏览器，中间不经第三方。

> **首帧延迟 < 150ms · 24 位真彩色 · 全链路录像回放**

---

### 三、DB Studio：DBA 的浏览器工作台

不用再开 Navicat、DataGrip 这些本地数据库客户端。

* **Monaco 编辑器**：和 VS Code 同款内核，语法高亮、智能补全、多标签页
* **表结构浏览**：点开就看，不用手敲 `DESCRIBE`
* **EXPLAIN 可视化**：执行计划画成树状图，瓶颈卡在哪儿看得清
* **结果导出**：CSV、JSON、Excel 随你选
* **写操作门禁**：`INSERT` / `UPDATE` / `DELETE` 自动拦下，走完审批才执行
* **国产数据库**：除了 MySQL、PostgreSQL，达梦（DM）和 openGauss 也原生支持

> 谁改了什么、什么时候改的，每一条 SQL 都查得到。

---

### 四、对象存储跳板：一个入口管住多朵云

阿里云 OSS、腾讯云 COS、AWS S3，三家的原生 SDK 都接好了。

一个节点绑一个 `access_key`，账号下的存储桶自动列出来。浏览、上传、下载、在线预览都在浏览器里完成，每一步都留审计记录。

不用再把 `access_key` 一个个发给运维，也不用提心吊胆怕泄漏。密钥统一托管在平台，每个人拿到的只是一次经过授权的访问。

---

### 五、安全：从架构第一层就开始

很多产品把安全做成功能清单里的几个勾选项。我们更愿意把它放进架构的地基里。

#### KMS 信封加密

凭据永不明文落盘。

每条凭据用一把独立的数据加密密钥（DEK），DEK 再由外部 KMS 的密钥加密密钥（KEK）包裹。支持：

* HashiCorp Vault / OpenBao Transit
* AWS KMS
* Azure Key Vault
* GCP Cloud KMS

主密钥从不接触磁盘。凭据从存储到使用，全程都是密文。

---

#### 防篡改审计账本

每条审批记录、每次高危操作，都用 KMS 签名后写进哈希链。

事后审计时，只要有人动过其中一条，后面整条链的校验立刻断裂。它改不动，又不必背上区块链那一整套复杂度——比起一份普通日志文件，这是能在密码学层面站住脚的证据链。

---

#### 多因素认证（MFA）

四种方式可选：

| 认证方式 | 说明 |
| --- | --- |
| **TOTP 时间令牌** | Google Authenticator / Authy / 任何标准 TOTP 应用 |
| **邮件 OTP** | 一次性邮件验证码，60 秒冷却 |
| **恢复码** | 10 组一次性恢复码，用于设备丢失场景 |
| **Passkey / WebAuthn** | 指纹、面容、硬件安全密钥，无密码登录 |

---

#### OIDC 单点登录

对接企业身份提供商：

* Okta / Auth0
* Azure Active Directory
* Keycloak / Casdoor
* 任何标准 OIDC Provider

员工不用再记一套额外的账号密码。JWT 可以主动吊销，登录失败会锁定，会话集中管理。

---

#### 在线监看 + 强制下线

管理员能实时看到任何一个在线会话的屏幕画面。

看到危险操作，一键就能把人踢下线，两套机制兜底，不会出现「点了下线人还在」的尴尬。

---

#### 异常登录检测

用多个信号给登录行为打分，自动识别风险：

* **不可能位移**：10 分钟前在北京登录，现在又从纽约登录？自动告警
* **暴力破解**：连续失败到阈值，账户自动锁定
* **GeoIP 定位**：内置 IP 地理库，自动更新，能定位登录来源
* **多通道通知**：站内消息、SSE 实时推送、邮件，本人和安全团队都收得到

---

#### 安全四支柱

![image-20260622230741865](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVleJkiaE4KaD5uU3ufFWcYEoVHMYp2EXOqEDvWicOlWBNFtoNYz9CGgMUhspPUZjaA0oMlxmK3hZicsScqH3gqlLbMGnCxS39bbX8/640?wx_fmt=png&from=appmsg)

image-20260622230741865

---

### 六、审批工作流：连上之前的最后一道闸

不是每个人、任何时候，都该自由连进生产环境。

**连接前审批**点击连接时，如果目标资产配了审批策略，申请面板会自动弹出，不用切到另一个系统去提工单。

**SSE 实时推送**审批人秒级收到通知，不用轮询刷新；审批状态一变，申请人这头也马上知道。

**多级审批 / 批量决策 / 转交**适配复杂的组织架构。审批人还能调整授权时长，不必只在「批」和「驳」之间二选一。

**时限授权**批准时设好有效期，到期权限自动回收。临时权限不会再悄悄变成永久权限。

**审批通过自动连接**申请人不用手动重试。审批通过的那一刻，连接自动建立。

> 谁能连什么、什么时候连、能连多久，全做成可配置的策略，不再靠口头约定。

---

### 七、AI 运维助手：能动手，也守规矩

Wayfort 内置了一套完整的 AI 运维子系统：能调用工具、动手执行、跨会话记住上下文，不只停留在对话框里聊天。

#### 多厂商接入，不被锁定

OpenAI、Claude、Gemini 这些主流厂商都能接，随时切换，成本可控，也不会被某一家绑死。

#### 预置专业智能体

开箱即用的 6 个全局智能体，外加 3 个专业子智能体：

| 智能体 | 职责 |
| --- | --- |
| **SRE Copilot** | 综合运维副驾驶 |
| **健康巡检员** | 系统健康检查与预警 |
| **日志分析师** | 日志模式识别与异常定位 |
| **安全审计员** | 安全合规检查 |
| **应急响应员** | 故障应急处置与恢复 |
| **成本优化师** | 资源利用分析与成本建议 |
| ↳ 数据库医生 | 慢查询诊断、索引建议 |
| ↳ K8s 领航员 | 集群状态、Pod 调度分析 |
| ↳ 网络工程师 | 连通性排查、链路诊断 |

#### 三档权限模式

* **Plan**：AI 只规划方案，每一步执行都要人工确认
* **Normal**：低风险操作自动执行，高风险操作拦下来走审批
* **Bypass**：全自动执行，仅限受信环境和受信操作员

#### RAG 知识库

把运维手册、故障处理 SOP、架构文档传上去，AI 就根据你自己的资料回答，而不是拿网上的泛泛信息来猜。底层用向量检索配合混合检索，召回更准。

#### 跨会话长期记忆

上次排查到哪一步，AI 记得，不用每次从头交代背景。换个会话、隔天再来，思路都接得上。

> 重复的巡检、排障、查信息，交给智能体去做。但它的每一步都在审计之内，能追溯、能回滚——说到底，AI 是帮手，权限始终攥在人手里。

---

### 八、代理链：再深的隔离网段也能穿

```
浏览器
  │
  ▼
Wayfort 网关
  │
  ▼ ─── SOCKS5 代理 ───▶ SSH 跳板机 A ───▶ SSH 跳板机 B ───▶ 目标主机
                              │
                              ▼
                        故障转移 ──▶ 备用跳板机 C
```

**ContextDialer 代理链**支持 Direct → SOCKS5 → SSH 任意层级嵌套。

* **目标侧零 Agent**：目标主机上什么都不用装
* **故障转移组**：多条链路自动切换，断了一条，无感切到备用
* **健康探测**：代理节点状态实时探测，掉线自动摘除
* **反连 Agent**：隔离网内的主机主动拨出到网关（WSS + mTLS + yamux），只需放行一条出站规则

> 网络拓扑再绕，代理链都能跟着钻进去。运维这头，看到的只是一个「连接」按钮。

---

### 九、SSH 运维工具箱：连上之后，不止一个终端

连上一台 SSH 主机后，Wayfort 在终端之外，还给了你一整套可视化运维面板。

#### 18 个工具分类，覆盖日常运维

![image-20260622230808320](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmaDxHBTcAOT3micVzriae1TVIicQuMRGpibWw6fBR7EGQpYialFr40Q98McyBRxx54jHQrLZX4OnpnNibWDIM1pfbklvpnueicUDmWc0/640?wx_fmt=png&from=appmsg)

image-20260622230808320

全部可视化操作，全部审计留痕，全部基于 SSH，不用额外装 Agent。

#### 防火墙管理亮点

* 暴露面矩阵可视化
* 每条规则实时命中计数
* ufw / nftables 一等编辑与持久化
* **三档自动回滚防锁死**：改错了规则，也不至于把自己关在门外

#### WireGuard 管理

* 完整生命周期：安装 → 接口 → 对端 → 客户端配置
* 浏览器内生成二维码，手机扫码就连
* React Flow 网络拓扑可视化
* 网关 NAT 配置

> 不用再对着黑屏盲敲，常用操作点一点就行，而终端本身的能力一点没少。

---

### 十、匿名 Docker 沙箱：打开就有的一次性 Shell

不用注册，不用登录，打开页面就有一个完全隔离的 Linux Shell。

| 特性 | 说明 |
| --- | --- |
| **TTL 定时销毁** | 默认 10 分钟，到期硬切断 + 即时销毁 |
| **资源硬限制** | CPU 0.5 核 · 内存 128MB · PID 64 |
| **网络隔离** | `network: none` ，完全断网 |
| **退出即销毁** | 不留任何痕迹，全程录像审计 |

#### 三大适用场景

**产品演示**给客户一个即开即用的体验环境。不用准备虚拟机，不用发账号密码，扫码或点链接直接进。

**在线教学**每个学生一个独立沙箱，互不干扰。课程结束自动回收，下次上课重新分配。

**CTF 竞赛**安全隔离的挑战环境。选手逃不出去，互相看不见，也连不上外网。

---

### 技术架构一览

Wayfort 分成四层，各管各的事，也能各自单独扩展。

![image-20260622230841259](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVm4Ye2I1PZdPbtqXdUyKZD2NlU4SqCNKSpZf9Fh3TwsRYyYXo6cqDWrBhOmwu8CiaVg3scZ1cA9L8DcuXLlFiaYD1TBqsuTQ5730/640?wx_fmt=png&from=appmsg)

image-20260622230841259

#### 关键技术选型

| 层级 | 技术栈 |
| --- | --- |
| 后端 | Go 1.26 · Gin · GORM · 纯 Go 无 CGo 依赖 |
| 前端 | React 19 · Next.js · xterm.js · WebRTC · WebGPU |
| 数据库 | PostgreSQL 16 · Redis 7 |
| 安全 | KMS（Vault / AWS / Azure / GCP）· OIDC · Passkey / WebAuthn |
| 桌面 | FreeRDP 3.x · IronRDP (Rust) · libvpx (VP9) · AV1 |
| 文档协作 | OnlyOffice Document Server |

纯 Go 后端，跨平台编译，分钟级私有化部署。

---

### 六大解决方案

不同场景的需求不一样，我们把常见的六类整理成了现成方案。

---

#### 方案一：等保合规与审计

> 满足等保 2.0 的硬性要求，审计员来了也不慌。

* ✅ 全协议会话录像，字符、图形、文件、数据库全覆盖
* ✅ KMS 签名审计账本，密码学防篡改
* ✅ 细粒度权限加多级审批，最小权限真正落地
* ✅ 强制下线加异常登录告警，监控不间断

-...