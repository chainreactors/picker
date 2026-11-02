---
title: 域名 / IP 被墙了怎么办？前端多入口容灾的完整落地方案
url: https://blog.upx8.com/IP
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-01
fetch_date: 2026-11-02T08:32:53.586202
---

# 域名 / IP 被墙了怎么办？前端多入口容灾的完整落地方案

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[开发](https://blog.upx8.com/code)
/
域名 / IP 被墙了怎么办？前端多入口容灾的完整落地方案

# 域名 / IP 被墙了怎么办？前端多入口容灾的完整落地方案

[开发](https://blog.upx8.com/code)
11-01
·
约 56 分钟
·
黑海洋
·

4,021

## 零、这篇和常见写法的差别在哪

网上讲「被墙了怎么办」的文章，绝大多数停在两个层面：

* 有的是**运营视角**：域名池、换域名、备案、CDN 分散。这类内容对「运营治理」很到位，但默认了一个前提——**前端能掌控的资源只有域名**。
* 有的是**协议视角**：ECH、IP 直连、TLS 指纹。这类内容技术密度高，但往往不谈资产流水线、重试预算、众包探测这些「跑起来之后才会痛」的事。

这篇想做的是把两层拼起来，并补上 2026 年才成立的两个新事实。所以全文按五个层来组织，每层只解决一件事：

![五层纵深：每层只解决一件事](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/a0435e884d1f3246e7d918ee1eb46761.webp)

上面一层挂了，下面一层还在；下面一层也挂了，还有触达层。这个结构决定了后面所有代码的归属——**写代码之前先想清楚这段逻辑属于哪一层，不属于任何一层的，就是过度设计。**

---

## 一、先搞清楚「被墙」到底是哪一种

「打不开」在用户眼里是一个现象，在网络层面至少有四种完全不同的形态。**手段要对症，否则全是白做。**

![四种「被墙」不是一种故障](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/e5c0e03e7f3d0357d59ca98d3b718402.webp)

| 形态 | 机制 | 前端能观察到的现象 | 有效手段 | 无效手段 |
| --- | --- | --- | --- | --- |
| **DNS 污染 / 劫持** | 解析返回错误 IP 或空应答 | 连到错误地址、证书报错、NXDOMAIN | 换域名；DoH 解析；IP 直连 | 同域名重试 |
| **IP 封锁（黑洞）** | 目标 IP 丢包 | 请求长时间挂起直到超时 | 换 IP；共享 IP 承载；对冲竞速 | 同 IP 下换域名 |
| **SNI / TCP RST** | 按域名识别后重置连接 | 握手阶段被重置，`ERR_CONNECTION_RESET` | ECH 加密 SNI；IP 直连；换域名 | 换 IP 不换域名 |
| **平台 / 浏览器拦截** | 微信、QQ、安全库把域名标红 | 出现拦截提示页，而非网络错误 | 换域名；域名提前预热养信誉 | 任何网络层手段 |

由此得到两条硬规则，后面所有设计都要服从它们：

1. **每个域名背后的 IP 必须相互独立。** 十个域名全指向同一个 IP，IP 一封全灭，域名池形同虚设。
2. **证书、注册商、权威 DNS 尽量分散。** 一张证书的 SAN 里塞一堆域名，一个被标记就整批关联。

> **合规说明**：面向中国大陆用户的加速域名需要完成 ICP 备案，域名池里每个域名都应当是合规、可备案的业务域名。本文讨论的是提升业务可用性与网络路径多样性。

---

## 二、2026 年两个新事实（这是本文和旧文最大的分歧点）

### 2.1 IP 地址证书已经 GA，「IP 直连兜底」这条路重新打开了

很多文章（包括很新的）会写：**浏览器无法直连 IP 并指定域名 SNI，所以「IP 直连兜底」走不通**。

前半句是对的，后半句在 **2026 年 1 月 15 日之后不成立了**。

[Let's Encrypt 官方公告](https://blog.upx8.com/go/aHR0cHM6Ly9sZXRzZW5jcnlwdC5vcmcvMjAyNi8wMS8xNS82ZGF5LWFuZC1pcC1nZW5lcmFsLWF2YWlsYWJpbGl0eQ)：IP 地址证书已 **General Availability**，支持 IPv4 和 IPv6，有效期 **160 小时（约 6.7 天）**，在 ACME 客户端里选 `shortlived` profile 即可签发。

这条改变了一个基础事实：

* **连接 IP 字面量时，ClientHello 里不携带 SNI**（RFC 6066 明确规定 HostName 里不允许出现 IP 字面量）。所以「按域名识别后 RST」这套阻断，对着 IP 连接**没有可匹配的字段**。
* **DNS 环节整个消失**。DNS 污染对你无效，因为压根没查 DNS。
* **证书校验能过**（IP SAN 匹配），所以 `fetch` 能正常发、能读 body、能走 CORS——不像自签名证书那样被浏览器直接拦掉。

注意区分两件事：

| 想做的事 | 能不能做 | 说明 |
| --- | --- | --- |
| 连 IP，但伪装成某个域名的 SNI | ✗ | 浏览器 JS 做不到，也确实不需要 |
| **连 IP，不带 SNI，用 IP-SAN 证书** | **✓** | 这才是「IP 直连兜底」的正确形态 |

### 2.2 ECH 落地了，但必须绑 DoH

[Cloudflare 文档](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXJzLmNsb3VkZmxhcmUuY29tL3NzbC9lZGdlLWNlcnRpZmljYXRlcy9lY2gv)写明：Free 套餐**默认开启 ECH**，外层 SNI 统一为 `cloudflare-ech.com`，中间人只看到「你在访问 Cloudflare 上的某个站」，看不到具体域名。Chrome 117+ / Firefox 118+ 支持，Android 17 已把它做进系统层并默认开启 ECH GREASE（连「这台机器开了 ECH」这个特征都被抹平）。

但有个前提必须记住，Cloudflare 文档自己写了：**ECH 的密钥来自 DNS 的 HTTPS 资源记录（HTTPS RR）**。所以：

> **ECH 必须配 DoH。** 否则明文 DNS 被污染或被丢弃，你连 ECH 配置都拉不到，ECH 等于没开。

也要认边界：阻断方可以直接封 `cloudflare-ech.com` 这个外层 SNI，或者封 Cloudflare 的 IP 段。所以 ECH 是「提高成本」，不是「免疫」。

---

## 三、传输层：五条互相补位的出口

![传输层：五条互相补位的出口](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/eb204ff3a8c2e3aeb59135ef3b00a293.webp)

| 出口 | 做法 | 覆盖的死角 | 边界 |
| --- | --- | --- | --- |
| **A 域名 + ECH** | Cloudflare 开 ECH，客户端配 DoH | 抗 SNI 阻断 | 外层 SNI 被整体封、CF IP 段被封时失效 |
| **B IP + IP-SAN 证书** | LE 短有效期证书 + nginx `default_server` | 抗 DNS 污染 + 抗 SNI | IP 本身被封时失效 |
| **C 泛域名随机子域** | `*.example.com` 通配证书，随机串轮换 | 抗「按精确域名封」 | 主域被整体封时失效 |
| **D 端口池** | 443 / 8443 / 2053 / 2083 / 2087 / 2096 | 抗端口阻断 | 单端口策略封禁时逐个试 |
| **E 共享 IP 承载** | 大 CDN 共享 IP、Serverless 默认域名 | 抗单 IP 封锁 | 封了会连坐大量正常业务，成本高 |

**为什么必须并列而不是主备**：ECH 挡不住「外层 SNI 被整体封」；IP 证书挡不住「IP 本身被封」。两者死角不重叠，所以是并列的两条腿，由竞速层决定这一轮走哪条。

### 3.1 IP-SAN 证书签发

```
# 首次
acme.sh --set-default-ca --server letsencrypt
acme.sh --issue --standalone -d 203.0.113.7 --profile shortlived

# 装到 nginx 并自动 reload
acme.sh --install-cert -d 203.0.113.7 \
  --key-file       /etc/le/ip.key \
  --fullchain-file /etc/le/ip.fullchain.pem \
  --reloadcmd      "nginx -s reload"
```

`--profile shortlived` 是硬要求：Let's Encrypt 规定 IP 证书必须是短有效期，不带这个参数请求会被拒。

### 3.2 nginx 侧要接受「没有 SNI 的连接」

关键在 `default_server`。少了它，无 SNI 的连接会被另一个 server 块抢走，然后证书不匹配。

```
map $http_origin $cors_origin {
  default "";
  "~^https://(app\.example\.com|shell\d+\.example\.net)$" $http_origin;
}

server {
  listen 443 ssl default_server;
  listen 8443 ssl default_server;
  server_name _;

  ssl_certificate     /etc/le/ip.fullchain.pem;
  ssl_certificate_key /etc/le/ip.key;
  ssl_protocols       TLSv1.2 TLSv1.3;
  ssl_early_data      on;

  add_header Access-Control-Allow-Origin  $cors_origin always;
  add_header Access-Control-Allow-Headers "authorization,content-type,x-idempotency-key" always;
  add_header Access-Control-Allow-Methods "GET,POST,PUT,PATCH,DELETE,OPTIONS" always;
  add_header Access-Control-Max-Age       86400 always;
  add_header Vary Origin always;

  if ($request_method = OPTIONS) { return 204; }

  location = /__health {
    return 204;
    add_header Access-Control-Allow-Origin * always;
    add_header Cache-Control no-store always;
  }
  location / { proxy_pass http://127.0.0.1:3000; }
}
```

---

## 四、寻址层：签名地址包 + 多通道并行拉取

![寻址层：并行拉、逐个验签、取最大版本号](https://i0.wp.com/cdn.skyimg.net/up/2026/11/1/72ff47bfd0a18ece74c4537819c867f5.webp)

### 4.1 为什么必须签名

地址包会被放在第三方公共存储（对象存储、jsDelivr、GitHub raw、IPFS 网关）上。这些地方的写入权限一旦出问题，攻击者就能往包里塞自己的服务器地址，全量用户被导向钓鱼站。所以包必须签名，公钥**硬编码在应用里**，并且内置两把（当前 + 下一把）以便轮换。

### 4.2 包结构

```
{
  "v": 7,
  "iat": "2026-11-01T00:00:00Z",
  "exp": "2026-11-08T00:00:00Z",
  "minShell": "1.4.0",
  "probe": "https://probe-a.example.net/__health",
  "exits": [
    {
      "id": "cf-ech",
      "kind": "domain",
      "host": "app.example.com",
      "ports": [443, 2053, 2083, 2087, 2096, 8443],
      "ech": true,
      "asn": "AS13335",
      "weight": 100,
      "note": "需 DoH，抗 SNI 阻断"
    },
    {
      "id": "ip-a",
      "kind": "ip",
      "host": "203.0.113.7",
      "ports": [443, 8443],
      "certType": "ip-san",
      "certNotAfter": "2026-11-06T12:00:00Z",
      "asn": "AS64500",
      "weight": 80,
      "note": "无 SNI，抗 DNS 污染"
    }
  ],
  "sig": "base64url(ECDSA-P256-SHA256 over canonical JSON without sig)"
}
```

`payload` / `sig` 分离还是整体签，两种都行，但**签名端和验签端必须用完全一致的序列化**。下文示例用「去掉 sig 字段后 JSON.stringify」。

### 4.3 服务端签名

```
// scripts/sign-pool.mjs
import { sign } from 'node:crypto'
import { writeFileSync } from 'node:fs'

// 一次性：generateKeyPairSync('ec', { namedCurve: 'P-256' })
// 私钥离线保管，公钥 JWK 写入前端包
const privateKey = /* 从离线介质读取 PEM */ null

const payload = JSON.stringify({
  v: 21,
  iat: Date.now(),
  exp: Date.now() + 7 * 24 * 3600 * 1000,
  probe: 'https://probe-a.example.net/__health',
  exits: [
    { id: 'cf-ech', kind: 'domain', host: 'app.example.com', ports: [443, 8443], ech: true, weight: 100, asn: 'AS13335' },
    { id: 'ip-a',   kind: 'ip',     host: '203.0.113.7',   ports: [443, 8443], certType: 'ip-san', weight: 80, asn: 'AS64500' },
  ],
})

// WebCrypto 验的是 IEEE P1363 格式(r||s)，这里必须指定，否则验签必失败
const sig = sign('sha256', Buffer.from(payload), {
  key: privateKey,
  dsaEncoding: 'ieee-p1363',
}).toString('base64url')

writeFileSync('pool.json', JSON.stringify({ payload, sig }))
```

`dsaEncoding: 'ieee-p1363'` 这一行是最容易踩的坑：Node 默认输出 DER 编码的签名，而 WebCrypto 的 `verify` 期望 r||s 的裸格式。两者不匹配的表现是「服务端签得好好的，前端每次都验签失败」，且报错信息毫无提示。

### 4.4 客户端验签

```
// src/lib/bootstrap.ts
const PUB_JWK = { kty: 'EC', crv: 'P-256', x: '…', y: '…' }   // 硬编码，随发版固定

export type Exit = {
  id: string
  kind: 'domain' | 'ip'
  host: string
  ports: number[]
  ech?: boolean
  cer...