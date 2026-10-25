---
title: 龙信杯(服务器_AI版)
url: https://mp.weixin.qq.com/s/KV57pDuT6xaAOhU8c3lmMA
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:06:25.654568
---

# 龙信杯(服务器_AI版)

# 龙信杯(服务器\_AI版)

原创

QAQ
QAQ

QAQ的奇怪角落

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 2026 龙信杯 · 快递员 Server 取证 WP

**大肥鱼写的，不知道正误， 呃...最后一题没跑出来 手工复现等过两天的 ... 想摆几天... T∧T**

> 范围：本文整理已解出的 19 道题。第 20 题“1900\*\*\*\*647 收件人姓名”尚未解出，未计入本文。
>
> 检材：
>
> * `Server01.E01`：11,924,409,584 字节，MD5 `a186ab19bb13929dfd3e6f7641124dc5`，250 GiB
> * `Server02.E01`：4,420,211,245 字节，MD5 `e2029a3ff560a09db16053fca742acb2`，250 GiB
>
> 工具与环境：Sleuth Kit 4.15（`fls/icat/istat`）、libewf、Python 3.12、`sqlcipher3`、`cryptography`。 分区结构为 GPT + LVM2 + ext4，根逻辑卷起始扇区为 `4,200,448`。

---

## 答案速览

| 序号 | 题目 | 答案 |
| --- | --- | --- |
| 1 | 负责完整启动查询系统的 systemd 服务名称 | `dq-bootstrap.service` |
| 2 | 服务实际执行的宿主机程序完整路径 | `/opt/delivery-query/bin/crypto-agent` |
| 3 | 系统后期调整前使用的原始核心启动程序完整路径 | `/opt/delivery-query/bin/crypto-agent.core` |
| 4 | 开始清理时最先被停止的查询业务容器名称 | `dqmain-gate-1` |
| 5 | 完整业务源码运行时生成在宿主机的目录 | `/run/dq-runtime/app` |
| 6 | 打开、转换或验证加密业务数据库的工具镜像标签 | `dqmain/sqlcipher-tool:3.4.6` |
| 7 | 向网站服务器提供临时授权并封装运行密钥的核心服务镜像标签 | `dqcrypto/cryptod:3.4.4` |
| 8 | 授权响应签名验证使用的数字签名算法 | `ed25519` |
| 9 | 签名原文中第 6 个字段名称 | `server_nonce` |
| 10 | 请求时间与服务器时间允许相差的最大秒数 | `45` |
| 11 | 独立 .qenc 解密任务临时启动的 Docker 镜像标签 | `qc-runtime:1` |
| 12 | 独立解密功能测试所用加密文件的 SHA256 | `2bb1a4633b57963c8e555eb8b5fdddeb58c6c02f276029b64d5f65f660b9690c` |
| 13 | 查询平台支持的条件查询数量 | `4` |
| 14 | 当前正式使用的业务数据库名称（不带后缀） | `challenge` |
| 15 | 数据库中快递记录总数 | `5000` |
| 16 | 不同取件码数量 | `3642` |
| 17 | SF35\*\*\*\*4474 的完整运单号 | `SF356949764474` |
| 18 | 2026-09-01 入库、YTO、WAIT\_PICKUP 的快件数 | `82` |
| 19 | 面单尾号 1621 的到付件（2 件数码配件）总重量 | `2.7kg` |

---

# 一、启动链与反取证清理

## 第 1 题：负责完整启动查询系统的 systemd 服务

**答案：`dq-bootstrap.service`**

在 Server01 根文件系统中定位到 `/etc/systemd/system/dq-bootstrap.service`：

```
[Unit]
Description=DQ Main Bootstrap
After=docker.service network-online.target
Requires=docker.service
Wants=network-online.target

[Service]
Type=simple
ExecStart=/opt/delivery-query/bin/crypto-agent
ExecStopPost=/usr/local/libexec/dq-cleanup
Restart=no
StandardOutput=null
StandardError=null
TimeoutStopSec=20

[Install]
WantedBy=multi-user.target
```

注意区分：

* `dq-bootstrap.service`：真正启动查询业务的服务，`ExecStart` 指向宿主机上的 `crypto-agent`。
* `dq-bootstrap-guard.service`：失败关闭（fail-closed）守护服务，不是业务启动服务；它在 `dq-bootstrap.service` 不处于 active 时调用清理脚本。
* `/etc/systemd/system/dq-bootstrap.service.d/90-failclosed.conf`：把 `ExecStopPost` 覆盖为 `/opt/delivery-query/bin/dq-failclosed-cleanup systemd-execstoppost`，用于强制清理。

因此“负责完整启动查询系统”的服务名是 `dq-bootstrap.service`。

---

## 第 2 题：服务实际执行的宿主机程序完整路径

**答案：`/opt/delivery-query/bin/crypto-agent`**

证据直接来自 `dq-bootstrap.service` 的 `ExecStart`：

```
ExecStart=/opt/delivery-query/bin/crypto-agent
```

该文件是一个 Bash 包装脚本（V3.4.7 版本），核心逻辑是拉起同目录下的 ELF 核心程序：

```
BASE="${DQ_BASE:-/opt/delivery-query}"
CORE="${DQ_AGENT_CORE:-$BASE/bin/crypto-agent.core}"
...
"$CORE" "$@" &
child=$!
...
"$CLEANUP" "agent-exit-rc-${agent_rc}"
```

也就是说 systemd 实际执行的宿主机入口是 `/opt/delivery-query/bin/crypto-agent`。

---

## 第 3 题：系统后期调整前使用的原始核心启动程序

**答案：`/opt/delivery-query/bin/crypto-agent.core`**

时间线与文件对应关系：

1. 备份目录 `.v347-backup-20260902035004/crypto-agent.before` 保存了调整前的程序；
2. 该备份是 ELF 可执行文件，SHA256 为：

   ```
   49d9ebf18d63836da65147a70182963f9adcdff67829560ea06654019d4af2a2
   ```
3. 当前 `/opt/delivery-query/bin/crypto-agent.core` 的 SHA256 与之完全相同，说明 `core` 就是后期调整前的原始核心程序；
4. 当前 `/opt/delivery-query/bin/crypto-agent` 被替换成 V3.4.7 Bash 包装脚本，仅保留调度与失败清理逻辑。

`crypto-agent.core` 是未剥离符号的 Rust ELF（3,461,560 字节），可从中恢复出完整的租约请求、密钥派生和容器编排逻辑，是后续重建查询平台的关键。

---

## 第 4 题：开始清理时最先被停止的容器

**答案：`dqmain-gate-1`**

清理逻辑位于 `/opt/delivery-query/bin/dq-failclosed-cleanup`，脚本明确规定了停止顺序：

```
log "reason=$REASON; enforcing gate -> app -> port80 -> runtime"

# 1) Gate must stop first.
stop_service gate

# 2) Then app.
stop_service app

# 3) Verify port 80 is closed before runtime destruction. Retry because Docker stop is asynchronous.
...
# 4) Only after the stop/port-close phase, clear runtime plaintext.
if [[ -d "$RUNTIME" ]]; then
  find "$RUNTIME" -mindepth 1 -maxdepth 1 -exec rm -rf -- {} + 2>/dev/null || true
fi
```

`stop_service()` 的容器名规则为：

```
local cname="${PROJECT}-${svc}-1"
```

其中 `PROJECT` 默认为 `dqmain`，因此 `gate` 服务对应的容器名是 `dqmain-gate-1`。脚本执行时先停止 `dqmain-gate-1`，再停止 `dqmain-app-1`，随后确认 80 端口关闭，最后删除 `/run/dq-runtime` 下的运行时明文。

此外，`dq-bootstrap-guard` 会在 `dq-bootstrap.service` 不活跃时调用同一清理脚本，进一步确认了这条清理链。

---

# 二、运行时源码与镜像

## 第 5 题：源码运行时实际生成在宿主机的目录

**答案：`/run/dq-runtime/app`**

`/opt/delivery-query/docker-compose.yml` 中 app 容器只读挂载：

```
volumes:
  - /run/dq-runtime/app:/srv/app:ro
  - /run/dq-runtime/secret:/run/dq-runtime/secret
  - ./data:/data:ro
```

镜像 `dqmain/app-runtime:3.4.6-keyfix1` 本身不保存完整业务源码。运行时由 `crypto-agent.core` 完成以下步骤：

1. 取得租约，解密 `payload/app.bundle.enc`；
2. 校验 `manifest_hash` 绑定；
3. 把解密后的应用源码释放到宿主机 `/run/dq-runtime/app`；
4. 通过 FIFO `/run/dq-runtime/secret/runtime.keys.fifo` 把 `db_key_hex`、`index_key_hex`、`generation` 交给容器内的 `main.py`；
5. 启动 compose 的 `app` 与 `gate` 服务。

从 `payload/app.bundle.tar.gz` 中可恢复出运行时源码 `main.py` 与 `requirements.txt`。`main.py` 中的关键代码：

```
RUNTIME_FIFO=os.getenv("DQ_RUNTIME_FIFO","/run/dq-runtime/secret/runtime.keys.fifo")
DB_PATH=os.getenv("DQ_DB_PATH","/data/challenge.db")
with open(RUNTIME_FIFO,"r",encoding="utf-8") as f:
    RUNTIME=json.loads(f.read())
DB_KEY=bytes.fromhex(RUNTIME["db_key_hex"])
INDEX_KEY=bytes.fromhex(RUNTIME["index_key_hex"])
GENERATION=int(RUNTIME["generation"])
```

清理脚本会删除 `/run/dq-runtime` 下的全部内容，这是本案的反取证核心动作；但源码 bundle、容器 overlay 层和镜像构建层仍保留了可恢复副本。

---

## 第 6 题：打开、转换或验证加密业务数据库的工具镜像

**答案：`dqmain/sqlcipher-tool:3.4.6`**

在 `crypto-agent.core` 的 `materialize_sqlcipher` 函数中可以还原出 materialize 命令。其参数表包含：

```
/usr/bin/docker
run
-i
--network
none
-v
/run/dq-runtime/tmp:/work:rw
-v
/opt/delivery-query/data:/data:rw
dqmain/sqlcipher-tool:3.4.6
```

对应的字符串区域还包含：

```
data/challenge.db
data/bootstrap.db.enc
challenge.db absent and bootstrap stage absent
tmp/challenge_plain.db
```

这说明该镜像负责在无网络环境下打开、转换或验证 SQLCipher 业务库，镜像标签即 `dqmain/sqlcipher-tool:3.4.6`。Server02 的 containerd `meta.db` 中也能检索到同一镜像引用：

```
docker.io/dqmain/sqlcipher-tool:3.4.6
```

---

## 第 7 题：负责临时授权并封装运行密钥的核心服务镜像

**答案：`dqcrypto/cryptod:3.4.4`**

Server02 的 `/opt/query-crypto/docker-compose.yml`：

```
services:
  cryptod:
    image: dqcrypto/cryptod:3.4.4
    restart: "no"
    environment:
      DQ_CRYPTO_BASE: /opt/query-crypto
    volumes:
      - ./:/opt/query-crypto:ro
    networks: [dqcrypto]
```

`cryptod` 由 mTLS 网关 `mtls-gate` 暴露 `9443` 端口，实际服务是 `crypto_service.py`。它在启动时加载：

* `runtime-store/service-root.key`
* `runtime-store/runtime-store.json`
* `identity/lease-sign.key`
* `config/challenge.json`

对外提供 `/v1/lease/acquire` 与 `/v1/lease/renew`，生成临时租约并把 `APP_DEK`、`RUNTIME_SEED` 封装进租约响应。其镜像标签为 `dqcrypto/cryptod:3.4.4`。

---

# 三、服务端签名与时间校验

## 第 8 题：授权响应签名使用的数字签名算法

**答案：`ed25519`**

`crypto_service.py` 的导入与签名代码：

```
from cryptography.hazmat.primitives.asymmetric import ed25519, x25519
...
lease_sign=ed25519.Ed25519PrivateKey.from_private_bytes(
    b64d((BASE/'identity/lease-sign.key').read_text().strip())
)
...
out['server_signature']=b64(lease_sign.sign(acquire_sig_text(out)))
```

客户端 `crypto-agent` 使用 `/opt/delivery-query/identity/lease-sign.pub` 验证签名。因此算法为 Ed25519（题目格式要求小写，填 `ed25519`）。

---

## 第 9 题：签名原文的第 6 个字段

**答案：`server_nonce`**

`crypto_service.py` 中 acquire 响应的签名原文构造如下：

```
def acquire_sig_text(r:dict)->bytes:
    fields=['lease_id','audience','expires_at','server_ephemeral_pub',
            'seal_nonce','server_nonce','sealed_key_bundle']
    return '\n'.join(str(r[k]) for k in fields).encode()
```

按顺序为：

| 序号 | 字段 |
| --- | --- |
| 1 | `lease_id` |
| 2 | `audience` |
| 3 | `expires_at` |
| 4 | `server_ephemeral_pub` |
| 5 | `seal_nonce` |
| 6 | `server_nonce` |
| 7 | `sealed_key_bundle` |

第 6 个字段是 `server_nonce`。

---

## 第 10 题：请求时间允许相差的最大秒数

**答案：`45`**

`guard_common()` 中：

```
def guard_common(challenge_id,node_id,manifest_hash,runtime_epoch,nonce,timestamp):
    now=int(time.time())
    if abs(now-int(timestam...