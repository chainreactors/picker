---
title: 2026ZeroG-CTF MISC 官方Write-up
url: https://mp.weixin.qq.com/s/oaScBRZEph_HTstQPjb2Hg
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:22.905139
---

# 2026ZeroG-CTF MISC 官方Write-up

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/w583TgvLJRYqtpjI6ibwjibiaIv6gNSM2xM4036BUCoHqvS9WRM08J3ic8yvdE1aMcoohpgkMfUKgVI2M1Rx9KibIXOWiakoWtyfibm7whBrmdsZ1U/0?wx_fmt=jpeg)

# 2026ZeroG-CTF MISC 官方Write-up

原创

平平无奇 n1
平平无奇 n1

Breaking-code

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# MISC-01

查看 README，可以看到提示

```
"轨迹会告诉你顺序，队伍会告诉你钥匙。"
```

说明日志中的轨迹编号大概率需要排序。

查看日志文件(ground\_control.log),可以发现以下可疑字段(对应 Hint 中的"轨迹告诉顺序")

```
trace=ZGST-03/12:eJyrVspLzE1VslJQ...
trace=ZGST-01/12:eJyrVkrLz1eyUkpK...
trace=ZGST-02/12:...
```

总结一下格式:

```
ZGST-当前序号/总片段数:数据片段
```

很明显后边的数据片段有点像 base64(范围:a-z,A-Z,+/=)

然后结合之前的 Hint,猜测需要排序,按照当前序号进行排序,然后拼接,ok 思路有了,写正则或者脚本先提取,然后排序,最后拼接解码

正则表达式

```
r'trace=ZGST-(\d+)/(\d+):([A-Za-z0-9+/=]+)'
```

提取并且拼接脚本

```
import re
with open("log.txt", "r", encoding="utf-8") as f:
    data = f.read()

pattern = r'trace=ZGST-(\d+)/(\d+):([A-Za-z0-9+/=]+)'

matches = re.findall(pattern, data)

matches.sort(key=lambda x: int(x[0]))

for index, total, content in matches:
    print(f"{index}/{total} -> {content}")

merged = ''.join(content for _, _, content in matches)

print("\n最终拼接结果：")
print(merged)
```

执行结果

```
01/11 -> eJw1jsFOwzAMhl8l8qWbaCvoWpB6
02/11 -> Q5M6Dghx4ATiEFJvzdY6k5MRJsS7
03/11 -> 49BxiKx8f+L/+4bJem8dQQuvyG5T
04/11 -> rF861Vn2QT3qE5kBchj1h8TPkXzQ
05/11 -> 7AUYxgjtGzzdyOVezsNp52RsSEcZ
06/11 -> HRK859C7Sdu0OMZYHi+/S0ejJZRX
07/11 -> 5MigpI2um6aqt/Vd1a+uV2mlsccB
08/11 -> WbIvJyKMeir8oKvmtjCBJT/0Wwln
09/11 -> tMj+xdo2U1cqK7Jy7ywtkuQygZnP
10/11 -> Nsu/4pB6xVJ5ffatCgOqwNqOamc/
11/11 -> 0SvHPXI+Y+m+0AOeS/j5BWxxXv8=
最终拼接结果：
eJw1jsFOwzAMhl8l8qWbaCvoWpB6Q5M6Dghx4ATiEFJvzdY6k5MRJsS749BxiKx8f+L/+4bJem8dQQuvyG5TrF861Vn2QT3qE5kBchj1h8TPkXzQ7AUYxgjtGzzdyOVezsNp52RsSEcZHRK859C7Sdu0OMZYHi+/S0ejJZRX5MigpI2um6aqt/Vd1a+uV2mlsccBWbIvJyKMeir8oKvmtjCBJT/0WwlntMj+xdo2U1cqK7Jy7ywtkuQygZnPNsu/4pB6xVJ5ffatCgOqwNqOamc/0SvHPXI+Y+m+0AOeS/j5BWxxXv8=
```

很明显是 base64,而且`eJw`也是经典的 zlib 压缩头,丢厨子看一看

![](https://mmbiz.qpic.cn/mmbiz_png/w583TgvLJRZlNWiaXdROHcVrgG2dkDRx7Ofb4c14b3tWZYf0t25yT1ibV2bzs5rfwPN90ia9W7SU5rM2aaSqwcQDZsz1UNricg2aq345wPjApfg/640?wx_fmt=png&from=appmsg)

和推测的一致,得到了一段 json,但是很丑,可以丢随便找个 json 在线美化网站(https://www.toolhelper.cn/JSON/JSONFormat)

```
{
  "mission": "ZeroG-CTF First Launch",
  "lab": "Pwnstars",
  "crew": [
    "N1",
    "A",
    "Hugo",
    "Gnaw",
    "Fen"
  ],
  "domain": "www.pwnstars.online",
  "nonce": "5a45524f472d3031",
  "cipher": "xorstream-sha256-ctr",
  "kdf": "sha256('Pwnstars::' + '-'.join(crew) + '::' + domain)",
  "note": "Fen says: the trail gives order, the team gives key."
}
```

采用伪随机流 XOR 加密(`CTR-like stream cipher`)  ,然后同时给了 KDF密钥派生函数`sha256('Pwnstars::' + '-'.join(crew) + '::' + domain)`

所以字符串为

```
Pwnstars::N1-A-Hugo-Gnaw-Fen::www.pwnstars.online
```

SHA256 生成密钥

```
import hashlib

key_material = "Pwnstars::N1-A-Hugo-Gnaw-Fen::www.pwnstars.online"
key = hashlib.sha256(key_material.encode()).digest()
```

会得到 32 字节 key

再来看 cipher 部分,伪随机流 XOR 加密, 拼接成 keystream 再与密文异或

```
SHA256(key + nonce + counter)
```

```
keystream = b''
counter = 0

while len(keystream) < len(cipher):
    ctr = counter.to_bytes(4, 'big')
    block = hashlib.sha256(
        key + nonce + ctr
    ).digest()
    keystream += block
    counter += 1

keystream = keystream[:len(cipher)]
```

想到还给了个随机值,先转成字符串

```
nonce = bytes.fromhex("5a45524f472d3031")
```

得到`ZEROG-01`

最后直接异或解密就行

```
plain = bytes([
    c ^ k for c, k in zip(cipher, keystream)
])
print(plain)
```

解密后的明文(终端输出可能排版会有点问题,让 AI 给你 整理一下就行)

```
================ ZeroG Telemetry Frame ================

Mission       : ZeroG-CTF First Launch
Operator Lab  : Pwnstars
Crew          : N1 / A / Hugo / Gnaw / Fen
Home          : www.pwnstars.online

Status        : nominal
Gravity       : near-zero
Orbit         : stable
Noise         : acceptable

The encrypted channel was designed for training purposes.
Do not look for the flag in plain sight.

FINAL=c3ludHtNcmViVF9mZ25lZ2Vudnlfc2Viel9jamFmZ25lZn0=

=======================================================
```

看这里

```
FINAL=c3ludHtNcmViVF9mZ25lZ2Vudnlfc2Viel9jamFmZ25lZn0=
```

依旧丢给厨子`synt{MrebT_fgnegenvy_sebz_cjafgnef}`

很明显是移位密码,再仔细看发现是 `rot13`

```
import codecs
s = "synt{MrebT_zbbayvtug_enqvb_qgzs}"
print(codecs.decode(s, 'rot_13'))
```

或者用厨子

![](https://mmbiz.qpic.cn/mmbiz_png/w583TgvLJRYXZ8x5ialK7U066zMZdDvA9V7muqibY3nnwakkn2pChGC9UBwiapTxk1EicEriadibicg01ngjT9aM2Ma6PEucXI7cDLiawsKeTOUDNjA/640?wx_fmt=png&from=appmsg)

```
flag{ZeroG_moonlight_radio_dtmf}
```

完整的解题代码

```
import re
import hashlib
import base64
import codecs

with open("ground_control.log", "r", encoding="utf-8") as f:
    data = f.read()
with open("telemetry.bin", "rb") as f:
    cipher = f.read()

pattern = r'trace=ZGST-(\d+)/(\d+):([A-Za-z0-9+/=]+)'

matches = re.findall(pattern, data)

matches.sort(key=lambda x: int(x[0]))

for index, total, content in matches:
    print(f"{index}/{total} -> {content}")

merged = ''.join(content for _, _, content in matches)

print("\n最终拼接结果：")
print(merged)
#这里太麻烦我手动处理了
key_material = "Pwnstars::N1-A-Hugo-Gnaw-Fen::www.pwnstars.online"
key = hashlib.sha256(key_material.encode()).digest()
print("key是",key)

nonce = bytes.fromhex("5a45524f472d3031")

keystream = b''
counter = 0

while len(keystream) < len(cipher):
    ctr = counter.to_bytes(4, 'big')
    block = hashlib.sha256(
        key + nonce + ctr
    ).digest()
    keystream += block
    counter += 1

keystream = keystream[:len(cipher)]

plain = bytes([
    c ^ k for c, k in zip(cipher, keystream)
])

print("\n这是解密后的明文")
print(plain)

if isinstance(plain, bytes):
    plain_text = plain.decode(errors="ignore")
else:
    plain_text = plain

match = re.search(r'FINAL=([A-Za-z0-9+/=]+)', plain_text)

if not match:
    print("未找到 FINAL=")
    exit()

final_encoded = match.group(1)

print("\n提取到的 FINAL：")
print(final_encoded)

try:
    decoded_base64 = base64.b64decode(final_encoded)
except Exception as e:
    print("Base64 解码失败：", e)
    exit()

decoded_text = decoded_base64.decode(errors="ignore")

print("\nBase64 解码后：")
print(decoded_text)

result = codecs.decode(decoded_text, "rot_13")

print("\n最终 FLAG：")
print(result)
```

```
01/11 -> eJw1jsFOwzAMhl8l8qWbaCvoWpB6
02/11 -> Q5M6Dghx4ATiEFJvzdY6k5MRJsS7
03/11 -> 49BxiKx8f+L/+4bJem8dQQuvyG5T
04/11 -> rF861Vn2QT3qE5kBchj1h8TPkXzQ
05/11 -> 7AUYxgjtGzzdyOVezsNp52RsSEcZ
06/11 -> HRK859C7Sdu0OMZYHi+/S0ejJZRX
07/11 -> 5MigpI2um6aqt/Vd1a+uV2mlsccB
08/11 -> WbIvJyKMeir8oKvmtjCBJT/0Wwln
09/11 -> tMj+xdo2U1cqK7Jy7ywtkuQygZnP
10/11 -> Nsu/4pB6xVJ5ffatCgOqwNqOamc/
11/11 -> 0SvHPXI+Y+m+0AOeS/j5BWxxXv8=

最终拼接结果：
eJw1jsFOwzAMhl8l8qWbaCvoWpB6Q5M6Dghx4ATiEFJvzdY6k5MRJsS749BxiKx8f+L/+4bJem8dQQuvyG5TrF861Vn2QT3qE5kBchj1h8TPkXzQ7AUYxgjtGzzdyOVezsNp52RsSEcZHRK859C7Sdu0OMZYHi+/S0ejJZRX5MigpI2um6aqt/Vd1a+uV2mlsccBWbIvJyKMeir8oKvmtjCBJT/0WwlntMj+xdo2U1cqK7Jy7ywtkuQygZnPNsu/4pB6xVJ5ffatCgOqwNqOamc/0SvHPXI+Y+m+0AOeS/j5BWxxXv8=
key是 b'\xc0\xff\xb0:\xed\xaf\xa1\xca\x8d\xe3>\xd8 \xf5\xf2-\x1b\x02\xe8\x8a\xc3\xbf{\x06\x03N>\xe0F\xe33\x94'

这是解密后的明文
b'================ ZeroG Telemetry Frame ================\n\nMission       : ZeroG-CTF First Launch\nOperator Lab  : Pwnstars\nCrew          : N1 / A / Hugo / Gnaw / Fen\nHome          : www.pwnstars.online\n\nStatus        : nominal\nGravity       : near-zero\nOrbit         : stable\nNoise         : acceptable\n\nThe encrypted channel was designed for training purposes.\nDo not look for the flag in plain sight.\n\nFINAL=c3ludHtNcmViVF9mZ25lZ2Vudnlfc2Viel9jamFmZ25lZn0=\n\n======================================================='

提取到的 FINAL：
c3ludHtNcmViVF9mZ25lZ2Vudnlfc2Viel9jamFmZ25lZn0=

Base64 解码后：
synt{MrebT_fgnegenvy_sebz_cjafgnef}

最终 FLAG：
flag{ZeroG_startrail_from_pwnstars}
```

# MISC-02

查看 README，可以看到提示

```
The moon does not speak Morse tonight.
key = sha256("ZeroG::" + radio_password + "::www.pwnstars.online")
Numbers may become characters again.
```

不是摩斯码，那就是电话按键音了（题目描述中也有 Hint）

这类电话按键声通常都是DTMF双音多频，每个按键由两个频率组成

标准频率表：

```
        1209  1336  1477  1633
697       1     2  ...