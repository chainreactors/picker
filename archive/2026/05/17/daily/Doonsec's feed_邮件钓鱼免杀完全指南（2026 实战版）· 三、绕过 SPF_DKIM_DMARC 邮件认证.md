---
title: 邮件钓鱼免杀完全指南（2026 实战版）· 三、绕过 SPF/DKIM/DMARC 邮件认证
url: https://mp.weixin.qq.com/s/UGfGCaWPSYEe4W1gQzMy8A
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:06:28.896456
---

# 邮件钓鱼免杀完全指南（2026 实战版）· 三、绕过 SPF/DKIM/DMARC 邮件认证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/P8tspoQj3Vrs45ea2EicgNQPoubyuhlCntVj0xbibrubNHEQUM874GOjMg2ej2ficef1vichAS8rtFnnVN27TT2JEE5KzgynCicakEz6Y1qhbEpw/0?wx_fmt=jpeg)

# 邮件钓鱼免杀完全指南（2026 实战版）· 三、绕过 SPF/DKIM/DMARC 邮件认证

原创

IceByte
IceByte

IceByte-Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P8tspoQj3Vo3eMYdRfC44y1t8stNUFd2DcRcK4sM4lzqzUZev2Op3VjCu5r8KH6eTcHTuX6wiaOwQVJ4cqQwLXNLyBDAiaLllfpE58tobtpkE/640?wx_fmt=png&from=appmsg)

> **系列说明**：本文是《邮件钓鱼免杀完全指南（2026 实战版）》系列的第三篇。上篇完成了 OSINT 信息收集，本篇深入邮件认证机制的核心，详解 SPF/DKIM/DMARC 的绕过手法，以及 2025-2026 年最危险的新型绕过技术。

---

## 前言：为什么邮件认证可以被绕过？

SPF、DKIM、DMARC 被称为邮件安全的"三驾马车"，理论上可以拦截**所有**伪造发件人的邮件。

但现实是：

* **71%** 的企业域名未正确配置 SPF（2026 年 APWG 报告）
* **68%** 的企业未部署 DKIM 签名
* 启用 DMARC `p=reject` 的企业比例仅为 **39%**
* 即使正确配置了三件套，**仍有 17 种已知手法**可以绕过验证

根本原因：**邮件认证机制依赖域名管理员的配置正确性与完整性**，而人类总会犯错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/P8tspoQj3VoIP61UibMAiaaCxq23rvKBcib6numricrOLbfEJ1Lo8AomU2Rx4ia5Bic5Mu7xxuG4po0ae8d0r8HKsa4TPGtyo69HJsuXysnXPOK9A/640?wx_fmt=png&from=appmsg)

---

## 一、SPF（Sender Policy Framework）机制与绕过

### 1.1 SPF 的工作原理

SPF 通过 **DNS TXT 记录** 声明"哪些 IP 地址被允许代表本域名发送邮件"。

**正常的 SPF 验证流程**：

```
发件人: attacker@victim.com
             ↓
接收方邮件服务器查询 victim.com 的 SPF 记录
             ↓
SPF 记录: v=spf1 ip4:203.0.113.0/24 include:spf.protection.outlook.com -all
             ↓
检查发件人 IP 是否在允许列表中
   ├── 在列表中 → SPF Pass
   └── 不在列表中 → SPF Fail → 按 DMARC 策略处理
```

**SPF 记录详解**：

```
v=spf1 [ qualifier] [ mechanism] ... [ qualifier] all

qualifier:
  +  → Pass（通过，默认）
  -  → Fail（拒绝）
  ~  → SoftFail（软失败，标记但不拒绝）
  ?  → Neutral（中立，不判断）

mechanism:
  ip4:<ip>/<mask>     → 允许指定 IP 或网段
  ip6:<ip>/<mask>     → 允许指定 IPv6 地址
  a:<domain>           → 允许指定域名的 A 记录 IP
  mx:<domain>          → 允许指定域名的 MX 记录 IP
  include:<domain>     → 引入其他域名的 SPF 记录（如第三方邮件服务）
  redirect=<domain>    → 重定向到另一个域名的 SPF 记录
  exists:<domain>      → DNS 存在性检查（高级用法）
```

### 1.2 常见 SPF 配置错误

**错误 1：`~all` 而非 `-all`**

```
# 错误配置（SoftFail —— 邮件仍可能被投递）
v=spf1 include:spf.protection.outlook.com ~all

# 正确配置（HardFail —— 邮件应被拒绝）
v=spf1 include:spf.protection.outlook.com -all
```

`~all` 的含义是："不在列表中的 IP 发邮件，可能是误会，**标个软失败就行，别拒绝**"。大多数邮件网关对 `~all` 的处理是**仅标记，不拦截**，攻击者可以轻易伪造发件人。

**错误 2：SPF 记录超过 10 次 DNS 查询限制**

SPF 标准（RFC 7208）规定，验证过程中 DNS 查询次数**不得超过 10 次**，否则结果为 `PermError`（永久错误），大多数服务器会**跳过 SPF 验证**。

```
# 存在问题的 SPF 记录（嵌套 include 过多）
v=spf1 include:spf1.example.com include:spf2.example.com include:spf3.example.com ... -all
# 如果 spf1.example.com 本身又 include 了 3 层，很容易超过 10 次限制
```

攻击者可以故意触发 `PermError`，使 SPF 验证失效。

**错误 3：`redirect=` 与 `include:` 混淆**

```
# redirect= 会替换整个 SPF 记录（只在最后生效）
v=spf1 redirect=spf.example.com

# include: 是"引入"而不是"替换"
v=spf1 include:spf.example.com -all
```

如果管理员错误使用 `redirect=` 且 `spf.example.com` 配置不当，整个 SPF 验证会被绕过。

### 1.3 SPF 绕过手法

| 手法 | 原理 | 成功率 |
| --- | --- | --- |
| 冒充子域名（无 SPF 记录） | 大多数管理员只为 `@company.com` 配置 SPF，忽略 `hr.company.com`、`mail.company.com` 等子域名 | ~73% |
| **0 日：SPF 记录解析漏洞（2026.4 披露）** | 某些邮件服务器（Exim < 4.96）在解析 SPF 的 `exists:` 机制时存在整数溢出，可绕过验证 | ~95% |
| 利用被入侵的合法域名代发 | 攻击者入侵一个 SPF 配置正确的域名，利用其邮件服务器发送钓鱼邮件 | 100%（完全绕过） |
| DNS 劫持 / DNS 缓存投毒 | 篡改目标域名的 SPF DNS 记录（需要控制 DNS 服务器） | 取决于 DNS 安全性 |

> **2026 年 4 月新披露的 0day（CVE-2026-3187）**：Exim 邮件服务器在解析 SPF 记录中的 `exists:` 机制时存在整数溢出漏洞，攻击者可以构造特殊 SPF 记录使验证结果恒为 `Pass`。该漏洞目前已有在野利用，官方已发布补丁。

---

## 二、DKIM（DomainKeys Identified Mail）机制与绕过

### 2.1 DKIM 的工作原理

DKIM 使用**非对称加密**（RSA 或 ED25519）对邮件进行数字签名，接收方通过 DNS 发布的**公钥**验证签名是否有效。

**完整的 DKIM 验证流程**：

```
发送方:
  1. 使用私钥对邮件的某些头字段 + 正文进行签名
  2. 将签名结果放入 DKIM-Signature 头字段
  3. 发送邮件

接收方:
  1. 从邮件头提取 DKIM-Signature 字段
  2. 根据 s= 和 d= 标签查询 DNS 获取公钥（selector._domainkey.domain.com）
  3. 使用公钥验证签名
  4. 检查签名覆盖的头字段是否包含关键字段（From、Subject、Message-ID）
```

**DKIM-Signature 头字段详解**：

```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=company.com;
  s=default; t=1715000000; bh=abc123...; h=from:to:subject;
  b=base64_encoded_signature...
```

| 标签 | 含义 | 安全影响 |
| --- | --- | --- |
| `v=` | DKIM 版本（应为 `v=1`） | — |
| `a=` | 签名算法（推荐 `rsa-sha256`） | `rsa-sha1` 已被证明不安全 |
| `d=` | 签名域名 | 攻击者可以伪造 d=，但需要对应私钥 |
| `s=` | 选择器（selector） | 用于构造 DNS 查询：`s`.\_domainkey.`d` |
| `c=` | 规范化算法（header/body） | `simple` 比 `relaxed` 更严格 |
| `h=` | 被签名的头字段列表 | **如果 From 不在 h= 中，攻击者可以伪造发件人！** |
| `bh=` | 邮件正文的哈希值 | — |
| `b=` | 签名数据（Base64） | — |

### 2.2 DKIM 绕过手法

**手法 1：弱密钥长度（< 1024 bit）**

DKIM 密钥长度低于 **1024 bit** 时，RSA 私钥可以被暴力破解。攻击者破解私钥后，可以对任意邮件进行签名。

```
# 检查目标域名的 DKIM 密钥长度
$ dig TXT default._domainkey.target-company.com +short
"v=DKIM1; k=rsa; p=MI...（公钥）"

# 将公钥保存为 pem 文件，检查密钥长度
$ echo"MI..." | base64 -d > pubkey.der
$ openssl rsa -pubin-in pubkey.der -text-noout
# 如果显示 512 bit 或 768 bit → 可被暴力破解
```

**手法 2：`h=` 字段篡改（Header Canonicalization Attack）**

如果 DKIM 签名没有覆盖 `From` 头（即 `h=` 中不包含 `from`），攻击者可以**在传输过程中篡改 From 字段**，而签名仍然有效。

```
原始邮件（DKIM 签名的 h= 中不包含 from）:
  From: legitimate@company.com
  DKIM-Signature: h=to:subject:date; ...

攻击者篡改后:
  From: attacker@company.com   ← 改了，但签名仍然有效！
  DKIM-Signature: h=to:subject:date; ...（不变）
```

> ⚠️ **注意**：大多数现代邮件服务器（Microsoft / Google）在签名时**默认包含 From 字段**，但某些自建邮件系统（如老版本 Postfix + OpenDKIM）可能存在配置错误。

**手法 3：DKIM Replay 攻击**

攻击者不需要破解任何密钥，只需要：

1. 注册一个域名（如 `legitimate-sounding.com`）
2. 正确配置 SPF/DKIM/DMARC
3. 向自己发送**大量合法邮件**（如订阅新闻稿、注册网站）
4. 这些邮件会通过 DKIM 签名，**签名有效**
5. 攻击者提取这些邮件的 DKIM 签名部分
6. **将签名"重放"到钓鱼邮件上**（修改收件人、正文，但保留原始 DKIM 签名）

```
原始合法邮件:
  From: newsletter@legitimate-sounding.com
  To: attacker@evil.com
  DKIM-Signature: d=legitimate-sounding.com; s=default; b=VALID_SIGNATURE
  Subject: Your weekly newsletter

攻击者重放:
  From: newsletter@legitimate-sounding.com  （不变，DKIM 验证通过）
  To: victim@target.com                  （改了收件人）
  DKIM-Signature: d=legitimate-sounding.com; s=default; b=VALID_SIGNATURE（原样复用）
  Subject: 紧急：请立即验证您的邮箱
  Body: 钓鱼内容...
```

**为什么 DKIM Replay 有效？**

DKIM 签名默认**只签名邮件头字段和正文**，不签名 `To` 字段（某些配置下）。因此，攻击者可以保留原始签名，只修改收件人和正文。

**防御方法**：在 DKIM 签名中包含 `i=`（身份标识）字段，或使用 DMARC 的 `pct` 字段逐步部署验证。

---

## 三、DMARC（Domain-based Message Authentication）机制与绕过

### 3.1 DMARC 的工作原理

DMARC 建立在 SPF 和 DKIM 之上，告诉接收方：**如果 SPF 和 DKIM 都失败了，应该如何处理这封邮件？**

**DMARC DNS 记录格式**：

```
_dmarc.company.com. IN TXT "v=DMARC1; p=reject; sp=reject; adkim=s; aspf=s; pct=100; rua=mailto:dmarc@company.com"
```

| 标签 | 含义 | 推荐值 |
| --- | --- | --- |
| `v=` | DMARC 版本 | `v=DMARC1`（固定值） |
| `p=` | 主策略（对 `company.com` 的处理） | `reject`（拒绝） |
| `sp=` | 子域名策略 | `reject` |
| `adkim=` | DKIM 对齐模式 | `s`（严格）或 `r`（宽松） |
| `aspf=` | SPF 对齐模式 | `s`（严格）或 `r`（宽松） |
| `pct=` | 应用策略的邮件百分比 | `100`（全部应用） |
| `rua=` | 汇总报告接收地址 | `mailto:dmarc@company.com` |
| `ruf=` | 详细报告接收地址（可选） | `mailto:forensics@company.com` |

**对齐模式（Alignment Mode）详解**：

DMARC 要求 SPF 或 DKIM 的"对齐"检查通过才算有效：

```
严格模式（adkim=s / aspf=s）:
  DKIM 签名的 d= 必须与 From 域名**完全一致**
  From: user@company.com
  DKIM d=: company.com   → ✅ 对齐通过
  DKIM d=: mail.company.com → ❌ 对齐失败

宽松模式（adkim=r / aspf=r）:
  DKIM 签名的 d= 只需与 From 域名**同属一个组织**（子域名也可）
  From: user@company.com
  DKIM d=: mail.company.com → ✅ 对齐通过（宽松模式）
```

### 3.2 DMARC 策略的实际执行差异

**`p=none`（仅监控）**：

```
v=DMARC1; p=none; rua=mailto:dmarc@company.com
```

邮件仍然会被投递，**不会拦截**。只是向 `rua=` 指定的地址发送汇总报告。

> **现状**：约 60% 配置了 DMARC 的企业使用 `p=none`，原因是不敢贸然开启 `reject` 怕误拦合法邮件。

**`p=quarantine`（隔离）**：

邮件会被放入**垃圾邮件文件夹**，用户可以手动找回。

**`p=reject`（拒绝）**：

邮件在 SMTP 层面被拒绝（返回 `550 5.7.1` 错误），**不会进入收件箱**。

### 3.3 DMARC 绕过手法

**手法 1：利用 `p=none` 域名**

如果目标域名的 DMARC 策略为 `p=none`，攻击者可以**任意伪造该域名的发件人**，邮件不会被拒收。

```
# 检查目标域名的 DMARC 策略
$ dig TXT _dmarc.target-company.com +short
"v=DMARC1; p=none; ..."   ← 可被绕过！
```

**手法 2：子域名遗漏**

许多企业只为**主域名**配置了 DMARC，但忽略了子域名（如 `mail.company.com`、`internal.company.com`）。

根据 DMARC 标准，如果 `company.com` 设置了 `sp=reject`，子域名会继承策略。但某些旧版邮件服务器**不执行子域名策略继承**，攻击者可以伪造 `user@mail.company.com`。

**手法 3：`pct < 100` 的利用**

```
v=DMARC1; p=reject; pct=50; ...
```

`pct=50` 表示"只对 50% 的邮件执行 reject 策略"，剩下 50% 执行 `none`。攻击者可以**重复发送多封钓鱼邮件**，总有部分能绕过。

**手法 4：DNS 污染 / DNS 劫持**

如果攻击者能够污染目标域名的 DNS（如通过中间人攻击、DNS 服务器漏洞），可...