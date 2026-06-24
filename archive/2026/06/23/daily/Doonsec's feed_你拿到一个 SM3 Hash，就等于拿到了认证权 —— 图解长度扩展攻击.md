---
title: 你拿到一个 SM3 Hash，就等于拿到了认证权 —— 图解长度扩展攻击
url: https://mp.weixin.qq.com/s/pecxg19AMf6qqqZmneK7aA
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:04:30.348403
---

# 你拿到一个 SM3 Hash，就等于拿到了认证权 —— 图解长度扩展攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZaibroIiatwe1ugV8XibmnEIDsmKaCV0F6w0HBNryzrcsdvAEbNTx3CQpvVW5ugfhfK1cCyDMib5zQRsxGHvdZxjgnL0sgFcfmicicLYnNtfY1l4Q/0?wx_fmt=jpeg)

# 你拿到一个 SM3 Hash，就等于拿到了认证权 —— 图解长度扩展攻击

原创

利刃信安
利刃信安

利刃信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 你拿到一个 SM3 Hash，就等于拿到了认证权 —— 图解长度扩展攻击

**摘要：** SM3 是我国商用密码体系中的核心杂凑算法，广泛应用于数字认证、消息认证等场景。然而，许多人并不知道：当你用 `SM3(secret || message)` 做消息认证时，拿到 hash 值的人，即使不知道密钥，也能伪造任意消息的合法认证。

---

## 一、问题场景：一个看似安全的认证方案

某服务端使用 SM3 做消息认证，token 的计算方式为：

```
token = SM3(secret_key || message)
```

其中 `secret_key` 是 16 字节随机密钥，攻击者**不知道密钥内容**，但已知密钥长度为 16 字节。

攻击者截获了一条合法请求：

| 字段 | 值 |
| --- | --- |
| `message` | `"user=alice&role=user"` (20 字节) |
| `token` | `984c2580ecb81f4945a4fcc1be399115558627dab8062fd519c43cd3819fef33` |

攻击者想附加 `&admin=true` 来提升权限。他能在不知道密钥的情况下，伪造出一个合法的认证请求吗？

**答案是：能。** 这就是 SM3 长度扩展攻击。

---

## 二、原理：为什么拿到 Hash 就等于拿到认证权？

要理解这个漏洞，先看 SM3 的内部结构。

SM3 采用 **Merkle-Damgård 结构**——消息被分为 512-bit（64 字节）的分组，逐块压缩：

```
SM3(M) 的计算流程:
  IV(256bit) → [CF] → V₁ → [CF] → V₂ → ... → Vₙ = SM3(M)
                ↑M₁          ↑M₂              ↑Mₙ
```

压缩函数 CF 的输出（256-bit）直接作为下一块的 IV，最终输出的 hash 值就是最后一个 CF 的输出——换句话说，**hash 值就是压缩机的“内部状态”本身**。

这导致了一个致命后果：拿到 `H = SM3(secret || message)` 的人，可以把它当新的 IV，继续压缩自己构造的附加数据块：

```
攻击者伪造:
  H = SM3(M) → [CF] → V' = SM3(M || padding || evil_extension)
                   ↑evil_extension (含新填充)
```

**攻击者根本不需要知道 `secret` 的内容——只需要 `H` 和密钥的长度。** 这就是长度扩展攻击（Length Extension Attack）的核心。

---

## 三、答案：一步步计算

> 设 `secret_key = 0123456789ABCDEF0123456789ABCDEF`（实际攻击不需要密钥，仅用于验证）。

### 1. padding₁ 的计算

SM3 填充规则 (GB/T 32905-2016 §5.1)：

| 步骤 | 操作 | 结果 |
| --- | --- | --- |
| 原始长度 | `secret(16B) + message(20B)` | 36 字节 = 288 比特 |
| 追加 0x80 | `36 + 1` | 37 字节 |
| 补 0x00 | 补至 `56 mod 64`，即 `56 − 37 = 19` 个 | 56 字节 |
| 填长度 | 8 字节大端序，`288 = 0x0000000000000120` | 64 字节 |

**padding₁ (28 字节, hex)：**

```
80000000000000000000000000000000000000000000000000000120
```

验证：`36 + 28 = 64` 字节，恰好一个 512-bit 分组。

### 2. 伪造 token 的计算

攻击者以 `H = 984c2580...819fef33` 作为新的 IV，对 `"&admin=true"` 进行 SM3 压缩：

| 步骤 | 操作 |
| --- | --- |
| ① 拆分 H | `V₀ = 0x984C2580, V₁ = 0xECB81F49, V₂ = 0x45A4FCC1, V₃ = 0xBE399115, V₄ = 0x558627DA, V₅ = 0xB8062FD5, V₆ = 0x19C43CD3, V₇ = 0x819FEF33` |
| ② 新总长 | `36 + 28 + 11 = 75` 字节 = 600 比特 |
| ③ padding₂ | `0x80 + 44×0x00 + 0x0000000000000258` (53 字节) |
| ④ 扩展块 | `"&admin=true"(11B) |
| ⑤ CF 压缩 | 以 H 为 IV 执行 64 轮 CF 压缩 |

**伪造 token：**

```
ef5bd5887e59cb85a6e870ee0d4a2ea5e73150a9b1a5108c5e58b970a6bc411f
```

### 3. 构造合法认证请求

攻击者发送：

```
message = "user=alice&role=user"  ← 原消息
        + padding₁_bytes          ← 28 字节原始二进制填充
        + "&admin=true"           ← 扩展消息

token   = ef5bd5887e59cb85a6e870ee0d4a2ea5e73150a9b1a5108c5e58b970a6bc411f
```

服务端计算 `SM3(secret || message')` 时，完整数据为：

```
secret(16B) || message(20B) || padding₁(28B) || "&admin=true"(11B)  → 75 字节
```

第一块 64B → CF 输出 H（等于攻击者截获的 token），第二块以 H 为 IV 压缩扩展块 → 输出刚好等于攻击者伪造的 token，**验证通过**。

---

## 四、详解：为什么攻击可行？

**直观类比：** 把 SM3 看作一台消息搅拌机——每次投入 64 字节原料，搅拌 64 轮后输出 32 字节浓缩液。最终浓缩液就是搅拌机的内部状态。攻击者拿到浓缩液后，直接倒入自己的原料继续搅拌，产出新浓缩液——**无需知道之前投入了什么原料。**

### 攻击者需要什么？

| 需要 | 不需要 |
| --- | --- |
| `token` （截获的 hash 值） | 密钥内容 |
| 密钥长度（如 16 字节） | 原始消息内容（仅长度） |
| SM3 算法实现 | 破解密钥 |

### 正常场景 vs 攻击场景

|  | 正常场景 | 攻击场景 |
| --- | --- | --- |
| 输入 | `secret || "user=alice&role=user"` | `secret || "user=alice&role=user" || padding₁ || "&admin=true"` |
| 权限 | 普通用户 | **管理员** |
| token | 合法截获 | **伪造** |

---

## 五、防御方案

| 方案 | 原理 | 推荐度 |
| --- | --- | --- |
| **HMAC-SM3** | `HMAC(K, M) = SM3(K⊕opad || SM3(K⊕ipad || M))` ，外层 hash 阻断了从输出恢复内部状态的路径 | ★★★★★ |
| **密钥放末尾** | `token = SM3(message || secret)` ，攻击者无法构造末尾未知的扩展 | ★★★ |
| **截断输出** | 只取 SM3 前 128 bit，攻击者无法获得完整 256-bit 内部状态 | ★★★ |
| **KMAC** | NIST SP 800-185 标准，天然免疫长度扩展攻击 | ★★★★ |

**结论：不要用裸 hash 做消息认证，使用 HMAC。**

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZaibroIiatwe1Ijz7jib5Bwjy65Kzg7q6JU6BGvgr2NLDZOvGs639QJHWib6ibMWNN4nGGlAgbfBtiaRWccAfh4KGpoibDzDwLQW9Nbb5QtE0yibdww/0?wx_fmt=png)

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