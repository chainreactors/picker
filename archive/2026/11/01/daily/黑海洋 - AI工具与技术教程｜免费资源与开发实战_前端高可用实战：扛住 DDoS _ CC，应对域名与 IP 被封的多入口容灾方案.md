---
title: 前端高可用实战：扛住 DDoS / CC，应对域名与 IP 被封的多入口容灾方案
url: https://blog.upx8.com/DDoS-CC-IP
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-01
fetch_date: 2026-11-02T08:32:54.752412
---

# 前端高可用实战：扛住 DDoS / CC，应对域名与 IP 被封的多入口容灾方案

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
前端高可用实战：扛住 DDoS / CC，应对域名与 IP 被封的多…

# 前端高可用实战：扛住 DDoS / CC，应对域名与 IP 被封的多入口容灾方案

[开发](https://blog.upx8.com/code)
11-01
·
约 52 分钟
·
黑海洋
·

3,864

> **一句话结论**：前端"打不开"的根因通常不在前端代码，而在**入口不可达**。要把防线拆成四层：**边缘抗攻击 → 多入口（域名池）→ 浏览器侧兜底（Service Worker）→ 数据降级**。只做 Service Worker 缓存，只能保护"访问过的老用户"，保护不了首次访问的新用户。

---

## 一、先搞清楚：这套方案防什么，不防什么

很多"前端容灾"文章讲的是弱网、接口抖动、发版事故。这些很重要，但如果你的实际风险是下面这些，就需要另一套思路：

| 编号 | 威胁 | 用户看到的现象 | 本质 |
| --- | --- | --- | --- |
| T1 | 大流量 DDoS（L3/L4） | 全站打不开 | 带宽/连接被打满 |
| T2 | CC 攻击（L7，刷接口/动态页） | 页面慢、接口 502/503 | 源站资源被耗尽 |
| T3 | 域名被封 / DNS 污染 | 部分地区或运营商打不开 | 域名层不可达 |
| T4 | IP 被封 / 黑洞 | 连接超时 | IP 层不可达 |
| T5 | 单个 CDN 故障 | 静态资源 404/超时，白屏 | 单点依赖 |
| T6 | 配置中心与业务同域 | 主域出事时切换能力一起失效 | 控制面与数据面耦合 |
| T7 | 发版缓存错配 | 老用户白屏 | 缓存版本管理 |

**需要先接受的现实**：

* 大流量 DDoS 的上限取决于**高防带宽**，不取决于前端代码。前端能做的是"让攻击期间尽量少出事"和"让用户能自己找到可用入口"。
* 首次访问的用户没有 Service Worker、没有本地缓存。能救他们的只有**入口层多活**和**多渠道分发的可用域名**。
* 容灾代码本身可能放大故障。攻击期间所有客户端同时重试，等于给还活着的节点再来一轮 DDoS。所以重试要有"预算"。

> 合规提示：面向中国大陆用户的加速域名需要完成 ICP 备案；域名池里的每个域名都应当是合规可用的域名。本文方案用于提升业务可用性，不涉及规避监管。

---

## 二、总体架构：四道防线

```
用户
 │
 ├─ 第一道：边缘层     高防 / WAF / 多 CDN / 智能 DNS / 源站隐藏
 ├─ 第二道：入口层     域名池 + 签名下发 + 独立导航页 + 客户端竞速
 ├─ 第三道：浏览器层   Service Worker 预缓存 + 多 CDN 资源加载 + 兜底页自动迁移
 └─ 第四道：数据层     多域名 API + 重试预算 + 熔断 + 快照读
```

降级等级（比"L0–L3 全套状态机"更贴近攻击场景）：

| 等级 | 触发 | 表现 |
| --- | --- | --- |
| L0 正常 | 主域名健康 | 实时数据 |
| L1 域名切换 | 主域名失败或超时 | 自动切到池内其他域名，用户无感 |
| L2 只读快照 | 所有 API 域名失败 | 展示本地快照 + "数据较旧"提示条 |
| L3 兜底迁移 | 当前入口域名整体不可达 | SW 返回兜底页，自动探测并跳转到可用入口域名 |

**为什么这么分**：每一级都能指回一类具体故障，指不回去的手段就是过度设计。

---

## 三、第一道防线：边缘层（不写前端代码也能做的 P0）

### 3.1 抗 DDoS

* 使用云厂商**高防 CDN / 高防 IP**，业务入口全部走高防，不直接暴露源站。
* 至少**两家**入口服务（例如"高防 + 普通 CDN"或"两家 CDN"），用 DNS 权重切换。
* 如果业务部署在多个区域，入口使用 Anycast，分散单点被打的风险。

### 3.2 隐藏源站，只认回源

攻击者一旦拿到源站真实 IP，就会绕过高防直接打源站。三条硬规矩：

1. 安全组/防火墙**只放行 CDN/高防的回源网段**，其余一律丢弃。
2. 回源时由 CDN 注入一个固定密钥头，源站校验，不通过直接断开。
3. 清理历史 DNS 解析记录、邮件头、证书透明度日志里可能泄露的源站 IP；泄露过就换 IP。

```
# 示例：只信任回源网段，并校验回源密钥头
set_real_ip_from 203.0.113.0/24;          # 替换为厂商提供的回源网段
real_ip_header   X-Forwarded-For;
real_ip_recursive on;

map $http_x_origin_auth $origin_ok {
  default 0;
  "replace-with-a-long-random-string" 1;
}

server {
  listen 443 ssl;
  if ($origin_ok = 0) { return 444; }     # 非 CDN 回源，直接断开
  # ...
}
```

### 3.3 抗 CC：把"贵"的请求挡在源站之前

CC 攻击打的是**昂贵的动态请求**。思路是分层消耗攻击者的成本：

1. **能静态化就静态化**：首页、列表页、配置文件走 CDN 缓存，回源率越低越抗打。
2. **接口分级限流**：按 IP、账号、接口三个维度，昂贵接口（搜索、导出、登录）单独收紧。
3. **挑战只对可疑流量**：WAF 上对异常 IP/指纹启用 JS Challenge 或验证码，正常用户不打扰。
4. **全局保护水位**：整体 QPS 超阈值时，主动对低优先级接口返回 `429`/`503` + `Retry-After`，保住核心链路。
5. **缓存穿透防护**：对"查不到"的结果也做短时间负缓存，避免攻击者用随机参数打穿到数据库。

```
# 示例：分级限流（http 块内）
limit_req_zone $binary_remote_addr zone=per_ip:10m rate=10r/s;
limit_req_zone $server_name        zone=global:1m  rate=2000r/s;

server {
  location /api/ {
    limit_req zone=per_ip burst=20 nodelay;
    limit_req zone=global burst=500;
    limit_req_status 429;
    proxy_pass http://app;
  }
  location /api/search {                  # 昂贵接口更严
    limit_req zone=per_ip burst=3;
    limit_req_status 429;
    proxy_pass http://app;
  }
}
```

### 3.4 DNS 与域名策略

* 权威 DNS 使用**两家服务商**，TTL 设为 60–300s，开启健康检查和故障自动摘除。
* 域名池里的域名尽量**分散**：不同注册商、不同后缀、不同权威 DNS、不同 CDN。
* **不要把所有域名放进同一张证书的 SAN**，否则一个域名被标记，整批会被关联。
* 备用域名要**提前备案、提前解析、提前小流量使用**，别等主域名出事再临时启用。
* 做**多地区、多运营商拨测**，持续监控每个域名的可达率，异常自动摘除并告警。

---

## 四、第二道防线：域名池 + 签名下发（让新用户也有救）

### 4.1 设计要点

1. **包内内置**一组入口域名、API 域名、CDN 域名。这是最后的底线，不依赖任何远端。
2. 域名列表通过**多个独立渠道**下发：不同云的对象存储、业务域名上的静态文件、独立导航域名等。客户端**并行拉取，取最快且验签通过的**。
3. 下发内容必须**签名**，并带 `version`（防回滚）和 `expiresAt`（防过期）。否则谁劫持了一个渠道，就能把你的用户导向恶意域名。
4. 私钥离线保管，客户端**内置两把公钥**，便于密钥轮换。
5. 另外准备一个**独立导航页**：托管在与主站完全不同的服务商和域名上，只做一件事——展示当前可用地址并自动跳转。这个地址可以放在 App 内、官方社群、邮件/短信模板里。

### 4.2 服务端：生成并签名域名池

```
// scripts/sign-pool.mjs
import { generateKeyPairSync, sign } from 'node:crypto';
import { writeFileSync } from 'node:fs';

// 一次性：生成密钥对，私钥离线保存，公钥（JWK）写进前端包
// const { publicKey, privateKey } = generateKeyPairSync('ec', { namedCurve: 'P-256' });
// console.log(JSON.stringify(publicKey.export({ format: 'jwk' })));

const privateKey = /* 从离线介质读取 */ null;

const payload = JSON.stringify({
  version: 13,                                       // 每次发布递增
  issuedAt: Date.now(),
  expiresAt: Date.now() + 7 * 24 * 3600 * 1000,
  entryDomains: ['https://www.example.com', 'https://www.example.net', 'https://www.example.org'],
  apiDomains:   ['https://api.example.com', 'https://api.example.net', 'https://api.example.org'],
  cdnDomains:   ['https://cdn-a.example.com', 'https://cdn-b.example.net'],
  swRolloutPercent: 30
});

// WebCrypto 使用 IEEE P1363 格式（r||s），必须指定 dsaEncoding
const sig = sign('sha256', Buffer.from(payload), { key: privateKey, dsaEncoding: 'ieee-p1363' }).toString('base64');
writeFileSync('pool.json', JSON.stringify({ payload, sig }));
// 把 pool.json 同时发布到多个渠道（至少两家不同云）
```

### 4.3 客户端：并行拉取 + 验签 + 防回滚

```
// pool/pool.js
const BUILTIN = {
  version: 0,
  entryDomains: ['https://www.example.com', 'https://www.example.net', 'https://www.example.org'],
  apiDomains:   ['https://api.example.com', 'https://api.example.net', 'https://api.example.org'],
  cdnDomains:   ['https://cdn-a.example.com', 'https://cdn-b.example.net'],
  swRolloutPercent: 0
};

// 内置两把公钥：当前 + 下一把（用于轮换）
const PUBLIC_KEYS = [ /* JWK_CURRENT */, /* JWK_NEXT */ ];

// 独立于业务域名的多个下发渠道
const CHANNELS = [
  'https://cfg-a.example-static.com/pool.json',   // 云 A 对象存储 + CDN
  'https://cfg-b.example-oss.net/pool.json',      // 云 B 对象存储
  'https://api.example.com/pool.json'             // 业务域名上的副本
];

const LS_KEY = 'dr:pool';

function readCached() {
  try { return JSON.parse(localStorage.getItem(LS_KEY)); } catch { return null; }
}

async function verifyEnvelope(env) {
  const data = new TextEncoder().encode(env.payload);
  const sig = Uint8Array.from(atob(env.sig), (c) => c.charCodeAt(0));
  for (const jwk of PUBLIC_KEYS) {
    const key = await crypto.subtle.importKey(
      'jwk', jwk, { name: 'ECDSA', namedCurve: 'P-256' }, false, ['verify']
    );
    if (await crypto.subtle.verify({ name: 'ECDSA', hash: 'SHA-256' }, key, sig, data)) return true;
  }
  return false;
}

async function pullFrom(url, cached) {
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), 3000);
  try {
    const res = await fetch(url, { signal: ctrl.signal, cache: 'no-store' });
    if (!res.ok) throw new Error('status-' + res.status);
    const env = await res.json();
    if (!(await verifyEnvelope(env))) throw new Error('bad-signature');
    const pool = JSON.parse(env.payload);
    if (pool.expiresAt < Date.now()) throw new Error('expired');
    if (cached && pool.version < cached.version) throw new Error('rollback');
    return pool;
  } finally {
    clearTimeout(timer);
  }
}

let current = readCached() || BUILTIN;
let lastRefresh = 0;

export async function refreshPool(force = false) {
  if (!force && Date.now() - lastRefresh < 30000) return current;   // 节流，避免攻击期间自我 DDoS
  lastRefresh = Date.now();
  const cached = readCached();
  try {
    const pool = await Promise.any(CHANNELS.map((u) => pullFrom(u, cached)));   // 取最快且验签通过的
    current = pool;
    try { localStorage.setItem(LS_KEY, JSON.stringify(pool)); } catch {}
  } catch {
    // 全部渠道失败：继续使用缓存或内置，不抛错
  }
  return current;
}

export const getPool = () => current;

// 启动时刷新一次，之后每 10 分钟刷新；全部 API 域名失败时由 api.js 主动触发
refreshPool();
setInterval(()...