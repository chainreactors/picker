---
title: 利用证书透明度日志构建隐蔽通信信道
url: https://mp.weixin.qq.com/s/FYFdWx3Jso7cdrA5iWJewg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:19:55.048539
---

# 利用证书透明度日志构建隐蔽通信信道

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h4gtbB74nShw5Buj2KwibVG2NDcoeT3JiaDawhyL2z5cGqxkzqb0N7aTNH6iag24tMgG5YF8AqGKR6kofjQUXOz46El6cxd22W2bqW67NibZT2g/0?wx_fmt=jpeg)

# 利用证书透明度日志构建隐蔽通信信道

latedeployment
latedeployment

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://latedeployment.github.io/posts/certificate-transparency-as-communication-channel/ | latedeployment |

*本文是 Certificate Transparency 系列的第三部分。*

# 引言

本文描述了一种利用证书验证基础设施，通过 Certificate Transparency 日志分发消息的方法。

读取者无需回连发送者的域名，并且数据也永远不会被 \_删除\_。

# TL;DR 快速概览

* 购买一个域名，例如 `example.com`
* 租用一台便宜的 VPS，将域名的 DNS 指向该服务器
* 生成包含隐藏数据的证书
* 使用 `Let's Encrypt`签署证书，数据将被存储到 Certificate Transparency 日志中
* 读取者查找已知域名的证书并读取消息
* 读取者只与 Certificate Transparency 日志 API 端点的域名通信

# 背景

参见第一部分 Certificate Transparency 101 了解更多关于 Certificate Transparency 的信息。

Certificate Transparency 日志是公开可访问的、仅追加的 Merkle 哈希树，记录着由证书颁发机构签发的证书。

它们的行为类似于区块链，因此数据永远无法从中删除。

这些日志可用于：

* **检测证书滥用**
* **提供可追溯性**

  (追踪谁签发了哪张证书)
* **允许浏览器验证**

  你所访问域名的证书在被信任之前已被记录

每个证书颁发机构都有自己的日志，像 `crt.sh`这样的工具允许搜索这些日志，但你也可以自行与 API 通信。日志的 API 在 *RFC 6962*中有定义，每个 CA 都有自己的 API 端点用于查询。

因此，我们拥有了一种可以追加数据的日志——前提是我们拥有一个域名并能为其创建证书。

如果读取者通过 API 读取证书，它完全不需要与我们的域名通信，而是通过 CA 的域名来读取数据。

更有趣的是，我们可以在证书本身中嵌入一些数据，方法包括利用 X.509 扩展或对主体备用名称 (SAN) 的某些用法，但这里我选择了公钥本身。

# 隐藏数据

参见 How to Hide Encrypted Data Inside RSA Public Keys 了解更多信息。

基本原理是，如果我们搜索素数足够 *长的时间\_，就能找到这样的素数——当它们相乘 (构成 RSA 模数) 时，特定值会出现在模数的某些比特位上。换言之，通过精心选择素数，我们可以将消息*嵌入\_ 到模数本身中。

在这个具体演示中，我使用了模数的低位比特，但实际上我们可以做得更巧妙，比如跳过某些比特位——例如每第 10 个比特是一个隐藏比特，诸如此类。这并不是最重要的。

这里的搜索速度相当快，比预期的还要快 (不到一分钟)，而且我相信更厉害的人能想出更好的方法来隐藏实际数据。在实践中，隐藏的数据本身可以被加密，因此看起来就像随机的 ("普通的") 比特位，读取者只需要知道在哪里寻找。

创建好素数后，我们就可以用它们生成证书并将其追加到 Certificate Transparency 日志中。

我使用了 Let's Encrypt 配合 OpenBSD 的 `acme-client`，但我相信也可以用其他方式完成。Let's Encrypt 通过一些 HTTP 请求验证了我的域名，最终批准了我的证书。

换句话说，我们通过向 Let's Encrypt 提供证书来将其"上传"到 Certificate Transparency 日志中，Let's Encrypt 批准后，包含我们嵌入数据的证书就被 *永久*存储在日志中了。

在 `crt.sh`上浏览并搜索我的域名，几分钟后就显示了该证书，但直接查询 API 则显示得更快。

最终我们的证书看起来是这样的：

```
Subject Public Key Info:
        Public Key Algorithm: rsaEncryption
            RSA Public-Key: (2048 bit)
            Modulus:
                ============================================
                ============== UNIMPORTANT DATA ============
                ============================================
                5b:48:65:6c:6c:6f:00:00:00:00:00:00:00:00:00:
                00:01
```

下面的数据中包含 ASCII 编码的 `Hello`，即 \_48:65:6c:6c:6f\_。

整个流程在下方附带的 Python 代码中有描述，具体请查看 `generate_rsa_key_with_hidden_data`函数。

# 通过 crt.sh 读取

为了简化这个示例，我直接使用 `crt.sh`。`crt.sh`网站解析所有相关的 Certificate Transparency 日志，并提供一个更简便的 "API" 来获取相关信息，尽管它既没有真正的 API，也并非总是可用 (有时需要刷新页面，因为它的数据库会宕机)。

```
domain="example.com"
cert_id=$(curl -s  "https://crt.sh/?q=${domain}&output=json" | jq -r '.[0].id')
cert=$(curl -s "https://crt.sh/?d=${cert_id}")
modulus=$(echo "$cert" | openssl x509 -noout -modulus | sed 's/Modulus=//')
message=$(echo "$modulus" | tr -d ':' | tail -c 33)
echo"$modulus"
echo"$message"
```

这样我们就能读取隐藏在证书中的消息了。

# 通过 Certificate Transparency API 读取

*RFC 6962 (Certificate Transparency)*提供了一套 API，允许我们高效地查询日志。如果想查找特定的证书，可以使用二分搜索按时间戳 (例如签发日期) 定位条目。这些日志可能非常庞大，有些包含超过 10 亿条记录，因此必须使用二分搜索。

这意味着，在最坏情况下，我们只需要大约 30 次 API 查询就能找到任意一张证书。

我们首先调用 `get-sth`API 获取树的大小 (即日志中有多少条目)，然后使用 `get-entries`配合合理大小的 `start`和 `end`来获取证书。假设我们知道某张证书是在特定日期创建的，就可以检查这些证书是否接近我们的目标，然后跳转到其他位置继续查找，直到找到正确的证书。

提供 Certificate Transparency 日志端点的公司包括 Sectigo、DigiCert、Let's Encrypt、Cloudflare、Google 等。3

从日志中读取数据后，我们需要解析它才能读取数据，以下是一个示例：

```
# Decode the leaf input (MerkleTreeLeaf structure from RFC 6962)
    leaf_input = base64.b64decode(entry["leaf_input"])

# MerkleTreeLeaf structure:
# - Byte 0: Version (0x00)
# - Byte 1: MerkleLeafType (0x00 for timestamped_entry)
# - Bytes 2-9: Timestamp (8 bytes, milliseconds since Unix epoch)
# - Bytes 10-11: LogEntryType (0x0000 for x509_entry,
#                               0x0001 for precert_entry)

    timestamp_ms =int.from_bytes(leaf_input[2:10], byteorder='big')
    timestamp = datetime.fromtimestamp(timestamp_ms /1000.0)

# Get entry type to determine how to parse
    entry_type =int.from_bytes(leaf_input[10:12], byteorder='big')

# Decode extra_data
    extra_data = base64.b64decode(entry["extra_data"])
    cert_data =None

if entry_type ==0:  # x509_entry
# For x509_entry: leaf_input has the certificate after header
# Bytes 12-14: certificate length (3 bytes)
# Bytes 15+: certificate DER
        cert_len =int.from_bytes(leaf_input[12:15], byteorder='big')
        cert_data = leaf_input[15:15+ cert_len]

elif entry_type ==1:  # precert_entry
# For precert_entry:
# - leaf_input: header + issuer_key_hash(32) + tbs_cert
# - extra_data: pre_certificate + chain
#
# extra_data format:
# - 3 bytes: length of pre_certificate
# - N bytes: pre_certificate (full DER cert with poison ext)
# - 3 bytes: length of chain
# - M bytes: chain
        cert_len =int.from_bytes(extra_data[0:3], byteorder='big')
        cert_data = extra_data[3:3+ cert_len]
else:
raiseValueError(f"Unknown entry type: {entry_type}")

# Parse the certificate
    cert = x509.load_der_x509_certificate(cert_data, default_backend())
```

# 使用场景

由于读取数据的连接目标是"正常"的域名 (如 Cloudflare 或 Sectigo)，这使得阻止数据读取过程变得更加困难。我们存储的数据也永远不会被删除。

虽然 Let's Encrypt 对证书签发有速率限制，但我相信人们会找到方法来克服这一点。

要构建一条大消息，只需创建多张证书，将它们堆叠起来记录到日志中，从而突破公钥模数的大小限制。另一种方法是创建子域名，为额外的证书提供"存储空间"。

# 代码

## 证书生成

```
#!/usr/bin/env python3
import secrets

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric.rsa import (
    RSAPrivateNumbers, RSAPublicNumbers
)

defmiller_rabin(n, k=10):
"""Miller-Rabin primality test."""
if n <2:
returnFalse
if n ==2or n ==3:
returnTrue
if n %2==0:
returnFalse

    r, d =0, n -1
while d %2==0:
        r +=1
        d //=2

for_inrange(k):
        a = secrets.randbelow(n -3) +2
        x =pow(a, d, n)
if x ==1or x == n -1:
continue
for_inrange(r -1):
            x =pow(x, 2, n)
if x == n -1:
break
else:
returnFalse
returnTrue

defgenerate_prime(bit_size):
"""Generate a random prime of given bit size."""
whileTrue:
        candidate = secrets.randbits(bit_size -1)
        candidate |= (1<< (bit_size -1)) |1# Set MSB and LSB
if miller_rabin(candidate, 20):
return candidate

defgenerate_rsa_key_with_hidden_data(message, key_size=2048,
data_bits=128):
"""
    Generate RSA key with hidden data in the modulus.

    The trick: we want (p * q) mod 2^data_bits = target
    So we pick q, then find p where:
        p mod 2^data_bits = target * q^(-1) mod 2^data_bits
    """
    prime_bits = key_size //2
    data_bytes = (data_bits +7) //8

# Pad message and convert to int
    msg_padded = message.ljust(data_bytes, b'\x00')
    target =int.from_bytes(msg_padded, 'big') |1# Must be odd

    mask = (1<< data_bits) -1

# Generate fixed prime q
    q = generate_prime(prime_bits)

# Calculate required lower bits for p
    q_inv_mod =pow(q, -1, 1<< data_bits)
    p_lower = (target * q_inv_mod) & mask

# Find prime p with those lower bits
    upper_bits = prime_bits - data_bits
for_inrange(100000):
        upper = secrets.randbits(upper_bits -1)
        upper |= (1<< (upper_bits -1))
        p_candidate = (upper << data_bits) | p_lower

if p_candidate.bit_length() != prime_bits:
continue
if miller_rabin(p_candidate, 20):
            p = p_candidate
break
else:
raiseValueError("Could not find suitable prime")

if p < q:
        p, q = q, p

    n = p * q
    e =65537
    phi_n = (p -1) * (q -1)
    d =pow(e, -1, phi_n)
    dp = d % (p -1)
    dq = d % (q -1)
    qinv =pow(q, -1, p)

    pub = RSAPublicNumbers(e, n)
    priv = RSAPrivateNumbers(p, q, d, dp, dq, qinv, pub)
return priv.private_key(default_backend())

defextract_from_modulus(n, data_bits=128):
"""Extract hidden data from modulus. No private key needed"""
    mask = (1<< data_bits) -1
    data_int = n & mask
ret...