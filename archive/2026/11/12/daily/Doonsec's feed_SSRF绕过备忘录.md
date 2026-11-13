---
title: SSRF绕过备忘录
url: https://mp.weixin.qq.com/s/IDllrZZLef59D-OrqJgUiA
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:02:45.803355
---

# SSRF绕过备忘录

# SSRF绕过备忘录

原创

在稻香村养猪
在稻香村养猪

鉴帷安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# SSRF绕过协议备忘录

---

## 一、回环 / 本机地址

| 写法 | 示例 | SSRF 点 |
| --- | --- | --- |
| 整个`127.0.0.0/8` | `127.0.0.2`、`127.255.255.254` | 不只是 ，整段都可能落到本机`127.0.0.1` |
| 省略写法 | `127.1`、`127.0.1` | 解析器会补全为回环地址 |
| 十进制整数 | `2130706433` | `127.0.0.1`的 32 位整数形式 |
| 十六进制 | `0x7f000001`、、`0x7f.1``0x7f.0.0.1` | 每段可用十六进制表示 |
| 八进制 | `017700000001`、`0177.0.0.1` | 前导  被按八进制解析`0` |
| `0.0.0.0` / `0` | `0.0.0.0`、`0` | Linux 上常连到本机;平台相关 |
| 主机名变体 | `localhost`、、、任意`LOCALHOST``localhost.``.localhost` | 大小写、尾点、子域都可能解析到回环 |

**记忆点**：过滤逻辑若只匹配 ，会漏掉整个回环段和大量等价写法。`127.0.0.1`

---

## 二、IPv6 形式

| 形式 | 示例 | SSRF 点 |
| --- | --- | --- |
| 标准回环 | `[::1]`、`0:0:0:0:0:0:0:1` | IPv6 本机 |
| IPv4 映射 | `::ffff:127.0.0.1`、`[::ffff:7f00:1]` | IPv4 被嵌入 IPv6 |
| IPv4 兼容 | `::127.0.0.1` | 另一种 IPv4 嵌入形式 |
| NAT64 | `64:ff9b::7f00:1` | 后 32 位内嵌 ，经 NAT64 可翻译到 IPv4`127.0.0.1` |
| 6比4 | `2002:7f00:1::` | `2002:`后内嵌`127.0.0.1` |
| 带区域标识 | Linux：;Windows：`fe80::1%eth0``fe80::1%1` | `%`后是接口名或接口索引，可用于接口枚举和信息收集 |

**记忆点**：

* IPv6 过渡地址要看“里面藏了什么 IPv4”。
* `%ZoneID`不只是地址后缀，还是**接口信息收集点**：枚举接口名/索引、观察响应差异，可推断目标是否存在多网卡和活动链路。

---

## 三、内网与特殊网段

| 类别 | 地址段 | SSRF 点 |
| --- | --- | --- |
| 私有段 | `10/8`、、`172.16/12``192.168/16` | 常规内网服务 |
| 运营商 NAT | `100.64/10` | CGNAT 段，常被忽略 |
| IPv6 内网 | `fc00::/7`、`fec0::/10` | ULA 与旧站点本地地址 |
| 链路本地 | `169.254/16`、`fe80::/10` | 云元数据、邻居设备、本地链路服务 |
| 组播与保留 | `224.0.0.0` 以上 | 组播/保留段，可作为探测面 |

**记忆点**： 和  是链路本地重点； 容易被私有段列表遗漏。`169.254/16``fe80::/10``100.64/10`

---

## 四、云元数据地址

| 云/平台 | 地址 | 备注 |
| --- | --- | --- |
| AWS / GCP / Azure 通用 | `169.254.169.254` | 最经典的元数据端点 |
| AWS IPv6 | `fd00:ec2::254` | AWS IMDS 的 IPv6 端点 |
| 阿里云 | `100.100.100.200` | 阿里云元数据/内部服务地址 |
| Azure 平台地址 | `168.63.129.16` | Azure WireServer/平台通信地址 |
| Oracle Cloud | `192.0.0.192` | Oracle 元数据地址 |

**记忆点**：元数据地址是 SSRF 的高价值目标，优先于普通内网 IP 枚举；IPv6 元数据地址也需单独记录。

---

## 五、WebSocket（ / ）`ws://``wss://`

WebSocket 的特殊性：握手阶段是 HTTP 升级请求，但许多防护只覆盖普通 HTTP 请求，不覆盖  路径；握手之后的数据帧则脱离 HTTP 语义。`Upgrade: websocket`

### 5.1 升级请求被滥用为 SSRF 载体

服务器处理 HTTP → WebSocket 协议升级时，如果对升级请求的目标地址缺少与普通 HTTP 请求同等强度的校验，攻击者可构造特制升级请求，让服务器将其代理/转发到任意内部地址。

**代表性漏洞：Next.js `CVE-2026-44578`**

自托管 Next.js 内置 Node.js 服务器对 WebSocket 升级请求的处理逻辑缺少普通 HTTP 请求上的安全检查，未经认证的远程攻击者可迫使服务器将流量代理到任意内部或外部目标，包括云元数据端点和内网服务。Vercel 托管部署不受影响，仅自托管场景暴露。

**SSRF 点**：任何暴露  或  端点、且反向代理/网关未对 WebSocket 升级请求实施与 HTTP 同等目标地址管控的场景。`ws://``wss://`

### 5.2 WebSocket 消息触发内部 HTTP 请求

应用收到 WebSocket 消息后，若根据消息内容（查询参数、路径参数、消息体中的 URL）发起服务端出站请求且未校验，就形成 SSRF。

**代表性漏洞：Apache Camel `CVE-2026-46726`**

`camel-vertx-websocket` 消费者将入站 WebSocket 的查询参数和路径参数未经  过滤直接映射到 Camel Exchange 消息头。攻击者连接 WebSocket 时提供  之类的参数，下游 HTTP 生产者就会将请求重定向到攻击者指定的目的地。注入 URI 中的属性占位符（环境变量、应用配置、Vault 引用）会被解析为真实值并发送给攻击者，造成凭据泄露。未认证可利用的条件是 WebSocket 端点本身未开启认证。`HeaderFilterStrategy``?CamelHttpUri=http://169.254.169.254/...`

**SSRF 点**：任何“WebSocket 入站 → 根据消息内容发起 HTTP 出站”的桥接逻辑，尤其是入站参数被直接注入内部控制头或目标 URL 时。

### 5.3 绕过基于 HTTP 的安全工具与策略

WebSocket 握手在协议层与 HTTP 不同，导致许多围绕 HTTP 请求设计的安全工具和策略在 WebSocket 路径上失效。

**代表性漏洞：OpenClaw `CVE-2026-62197`**

OpenClaw 的 CDP（Chrome DevTools Protocol）发现机制错误地接受了本应被策略阻止的 WebSocket URL。拥有较低信任访问权限的攻击者可借此绕过网络封锁策略，将 OpenClaw 实例变成 SSRF 代理，访问原本不可达的内部目标。相关漏洞  进一步表明，CDP 的  端点返回的  字段如果未经校验，攻击者可将其指向任意主机，实现第二跳重定向到内部地址。`CVE-2026-43576``/json/version``webSocketDebuggerUrl`

此外，CDP 的  域不会暂停 WebSocket 握手。依赖 CDP  进行请求拦截的防护或测试工具，在 WebSocket 场景下存在结构性盲区。`Fetch``Fetch`

### 5.4 DNS pinning 在 WebSocket 传输中的失效

即使防护方在验证阶段对 CDP 主机名做了 DNS pinning（将解析结果固定为公网 IP），原始 WebSocket 传输和 Playwright 传输可能在之后执行独立的 DNS 解析，丢弃验证时固定的结果。攻击者如果控制了一个“已批准”的 CDP 主机名或其 DNS 应答，就可以让验证时解析到公网、连接时解析到内网，实现 rebinding 式绕过。

**SSRF 点**：任何在“检查”与“WebSocket 实际建连”之间存在独立 DNS 解析的环节。

---

## 六、WebTransport（HTTP/3 + QUIC）

WebTransport 是基于 QUIC（UDP）的浏览器 API，与 WebSocket 的根本区别：WebSocket 升级自 HTTP/1.1（TCP），WebTransport 直接在 UDP 上建立 QUIC 会话，绕过 HTTP/1.1 和 HTTP/2 传输层——大多数网络管控和安全工具恰恰部署在这一层。

### 6.1 连接目标未校验 → 直接 SSRF

WebTransport 从浏览器或服务端 JavaScript 中调用  建立 QUIC 连接。如果应用（如 MCP server 的工具输出）允许调用方提供目标 URL 且未对主机做校验，攻击者可让连接指向任意内部地址。`new WebTransport(url)`

**SSRF 点**：任何接受用户可控 URL 并直接传给  的代码路径，等价于一个 UDP 层的 SSRF 原语。`new WebTransport()`

### 6.2 CORS 不适用于 WebTransport 数据报/流

WebTransport 握手阶段（HTTP/3  请求）会携带  头，但是否接受完全由服务器决定。一旦 QUIC 会话建立，数据报和流不受 CORS 预检约束。攻击者控制的 WebTransport 服务器可以无条件接受所有 Origin，浏览器端不会像 Fetch 那样基于  进行阻断。`CONNECT``Origin``Access-Control-Allow-Origin`

这意味着，在 XSS 或同源脚本注入场景下，WebTransport 可以作为一个不受 CORS 限制的双向通道，在仅允许 HTTP 出站的管控环境中建立 C2 或数据外带通道。

### 6.3 绕过 HTTP 代理与流量检测

因为 WebTransport 走 UDP/QUIC，标准 HTTP 代理和基于 HTTP 的流量检测工具无法直接检查或阻断，除非部署了专门的 QUIC 过滤能力。这是 WebTransport 相对于 WebSocket 和 Fetch 在“绕过既有管控”维度上的结构性优势。

**SSRF 点**：在“允许 UDP 出站但只审计 HTTP/TCP”的网络策略下，WebTransport 是一条不被审计的出站通道。

---

## 七、协议扩展速查

| 协议 | 传输 | SSRF 相关点 |
| --- | --- | --- |
| `ws://` / `wss://` | TCP（HTTP/1.1 Upgrade） | 升级请求可能缺少目标校验；消息可能触发内部请求；CDP Fetch 不暂停握手；DNS pinning 可能在传输层失效 |
| WebTransport | UDP（HTTP/3 + QUIC） | 连接目标未校验即 SSRF；CORS 不覆盖数据报/流；绕过 HTTP 代理和传统流量检测 |

**记忆点**：

* WebSocket 的“门”在 HTTP Upgrade，但许多防护只守普通 HTTP 门，不守这扇侧门。
* WebTransport 的“门”在 UDP/QUIC，多数 HTTP 层的waf根本不经过它。

---

## 八、一页速查

```
本机：
127.0.0.1 / 127.0.0.2 / 127.1 / 2130706433
0x7f000001 / 0x7f.1 / 0x7f.0.0.1
017700000001 / 0177.0.0.1
0.0.0.0 / 0 / localhost / localhost. / *.localhost

IPv6：
[::1] / 0:0:0:0:0:0:0:1
::ffff:127.0.0.1 / [::ffff:7f00:1]
::127.0.0.1
64:ff9b::7f00:1
2002:7f00:1::
fe80::1%eth0   （Linux）
fe80::1%1      （Windows，接口索引，信息收集点）

内网/特殊：
10/8、172.16/12、192.168/16
100.64/10
fc00::/7、fec0::/10
169.254/16、fe80::/10
224.0.0.0 以上

云元数据：
169.254.169.254
fd00:ec2::254
100.100.100.200
168.63.129.16
192.0.0.192

协议旁路：
ws:// / wss://        → HTTP Upgrade 侧门；消息触发内部请求；CDP Fetch 不暂停握手
WebTransport           → UDP/QUIC；目标未校验即 SSRF；CORS 不覆盖数据报/流；绕HTTP 代理
```

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/CrThU6KH4h6tIKtBf8x6N1HvaC1XDCTkHIYksgCSwL69XUH7mcVDaQKt0INibHBPrSXF1gqS7deibChQHtibUyOxmqYrWuy2scrNuhsBnrZrdc/0?wx_fmt=png)

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