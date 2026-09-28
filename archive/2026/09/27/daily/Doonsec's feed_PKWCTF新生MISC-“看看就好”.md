---
title: PKWCTF新生MISC-“看看就好”
url: https://mp.weixin.qq.com/s/b65GE-i1Tq34_2Q-45tzNA
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:53:59.383128
---

# PKWCTF新生MISC-“看看就好”

# PKWCTF新生MISC-“看看就好”

原创

玄网安全 opis
玄网安全 opis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# MISC1:你瞅啥

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5dswWLfhcefg3XibjHFRKDsCX6tFt0vbMzicQxjJ2RPQZqUqcQmicJWIadMibbARsDufbGBc8s0Zkb0bbiakbA592W4rmUMHcticfZvc/640?wx_fmt=webp&from=appmsg)

# MISC2:De-Fusion

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fL0Gb7aU6c5y50a3YsQnht2OGA3HVHosOKynf80AesZg8ZZvvbAKMibuNxiaBn6TPJquqiapvsFQbCm0ZsGDlLOpra9icJiaMTXGkc/640?wx_fmt=webp&from=appmsg)`有一个压缩包，解压得到flag2.png`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5dY6xU2q5lgbu7KbmR2p2Y3icCr74fJf9XsnBrzy4AB0TEdz9AGQ1bkAF0IaGiabIk6F0bSsWq2AftgC5a2wyNiclNqFk4gxelBfg/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5d5HLdiciaKrFcLIdoQXHJEribSjsVYicv11SocxsA4uYUiaycMIbeWpYBMEThmxNNljREhlIqBZYXaDOte0bvG7qssHjqkNHQ0yKvg/640?wx_fmt=webp&from=appmsg)`核心foremost分离`

```
PKWCTF{T34rl4m3nts_K4l31d0_H34rt}
```

# MISC3:pyjail-沉鱼

```
eval(expr, {"__name__": "__main__"}) 只传了自定义 globals，没把 __builtins__ 设成空。Python 会自动把完整 builtins 塞进去，所以 __import__('os')、open() 都能用。Flag 在环境变量里，读 os.environ['FLAG'] 即可。
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5eSiaOFtIKt8IfZ4s44qdNRlGUW5X72cNGoIpHPdBqjvickbCq4YRe1yZ3CtiaDLLrExl9eWBVVo5bCAoc19gr0eTZHLppia6OJxG0/640?wx_fmt=webp&from=appmsg)

# MISC4:pyjail-落雁

服务器不是用空 globals + 严格 AST 限制，而是直接把提交的字符串转小写后做 in 匹配，匹配到 import、os、open、eval、exec、system、flag 等关键词就直接 ValueError: No xxx allowed! 抛出。

这就是典型的 CTF 沙箱 jail（Blacklist Jail / Source Filter Jail），和 Level 1 完全不一样。`__builtins__['__imp'+'ort__']('o'+'s').environ['FL'+'AG']`![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cDvxT8SXiaDcPBthyWErydsGD1yMXLI040cQSlWBHJXMKVpwpq95c0R1ib7klGYLjUZ1mRNspX8nic2AAZJ7asOZUeibc5YXs0OXE/640?wx_fmt=webp&from=appmsg)

# MISC5:EchoesInCache

## 摘要

题目给出浏览器缓存、流量包和后台截图。从 `cache.db` 定位 `/api/echo` 日志，在 pcap 中拼出 LSB 提取指令，再对 `喵喵喵.png` 红通道 LSB 做 XOR，得到 flag。

## 解题过程

附件结构：

* `browser_cache/cache.db`：SQLite 缓存库
* `network/traffic.pcapng`：本机回环 HTTP 流量
* `screenshots/`：后台截图，其中 `喵喵喵.png` 为隐写载体

`cache_meta` 中有提示 `same path, same time, different echo`。`request_log` 记录了 `/api/echo?id=101` 到 `id=160`，`response_hash` 为 `hidden_in_pcap`。

pcap 中同一接口返回 JSON：`{"echo":"<base64>","id":"...","msg":"hello user"}`。解码后噪声为 `noise:<id>`，有效记录为 `log_NN:<hex>`。按序号拼出：

```
key=echo_key_2026;target=喵喵喵.png;method=red_lsb
```

对 `喵喵喵.png` 取红色通道 LSB（像素行优先、字节 MSB first），截到 `cipher=...::END::`，再用重复密钥 `echo_key_2026` XOR 密文。

```
#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import re
from pathlib import Path

from PIL import Image

ROOT = Path(r"E:\opendata\challenge\浮生-challenge")
PCAP = ROOT / "network" / "traffic.pcapng"
IMG_DIR = ROOT / "screenshots"

def bits_to_bytes(bits: list[int]) -> bytes:
    out = bytearray()
    for i in range(0, len(bits) - 7, 8):
        b = 0
        for j in range(8):
            b = (b << 1) | bits[i + j]
        out.append(b)
    return bytes(out)

def repeating_xor(data: bytes, key: bytes) -> bytes:
    return bytes(d ^ key[i % len(key)] for i, d in enumerate(data))

def main() -> None:
    raw = PCAP.read_bytes()
    bodies = re.findall(rb'\{"echo":"[^"]+","id":"[^"]+","msg":"[^"]+"\}', raw)

    logs: dict[int, str] = {}
    for body in bodies:
        obj = json.loads(body)
        echo = base64.b64decode(obj["echo"]).decode("utf-8")
        m = re.fullmatch(r"log_(\d+):([0-9a-fA-F]{2})", echo)
        if m:
            logs[int(m.group(1))] = m.group(2)

    instruction = bytes(int(logs[i], 16) for i in sorted(logs)).decode("utf-8")
    fields = dict(part.split("=", 1) for part in instruction.split(";"))
    key = fields["key"].encode("utf-8")
    target = IMG_DIR / fields["target"]

    pixels = list(Image.open(target).convert("RGB").getdata())
    payload = bits_to_bytes([p[0] & 1 for p in pixels])
    cipher_hex = re.search(rb"cipher=([0-9a-fA-F]+)::END::", payload).group(1)
    flag = repeating_xor(bytes.fromhex(cipher_hex.decode()), key).decode("utf-8")
    print(flag)

if __name__ == "__main__":
    main()
```

输出：

```
PKWCTF{cache_never_lies_but_logs_do}
```

`dashboard.png` / `error.png` 以及噪声 echo 是干扰项，可忽略。

# MISC5:奥马哈

## 摘要

动态 nc 服务连续给出 5 局 Pot-Limit Omaha 翻牌圈后局面，要求在 15 秒内计算 k1ne 在河牌上能**严格击败**三名对手的 outs 数量。核心是枚举剩余 32 张未知牌，并按“手牌恰好 2 张 + 公共牌恰好 3 张”评估成牌。

## 解题过程

服务地址：`nc nc1.ctfplus.cn 15185`。每局公开：

* k1ne 的 4 张手牌
* 3 名对手（cq / F1iAz / ddn）各 4 张手牌
* 4 张公共牌（Turn）
* 剩余未知牌：`52 - 4 - 12 - 4 = 32`

Outs 定义：河牌发出后，k1ne 的最终牌型必须**严格大于**所有对手；平局不计入。

### 第 1 步：实现奥马哈成牌比较

标准 5 张牌型从强到弱：同花顺 > 四条 > 葫芦 > 同花 > 顺子 > 三条 > 两对 > 一对 > 高牌。A 可作为 1 组成 A-2-3-4-5。

奥马哈强制组合：从 4 张手牌中选恰好 2 张，从 5 张公共牌中选恰好 3 张，取所有 `C(4,2)*C(5,3)=60` 种组合中的最大牌型。比较时用可排序元组（牌型等级 + 主牌 + kickers）。

### 第 2 步：枚举河牌计数 outs 并连打 5 轮

对每张剩余河牌，分别计算四人的最佳奥马哈牌型，统计 `hero > max(villains)` 的张数，在 15 秒超时前提交整数。五轮全部正确后给出 flag。

```
#!/usr/bin/env python3
import re
from itertools import combinations
from collections import Counter
from pwn import *

RANK_MAP = {c: i + 2 for i, c in enumerate("23456789TJQKA")}
SUIT_MAP = {"♠": 0, "♥": 1, "♣": 2, "♦": 3}
ALL_CARDS = [(r, s) for r in range(2, 15) for s in range(4)]

def parse_card(tok):
    tok = tok.strip().strip("[],")
    return (RANK_MAP[tok[0]], SUIT_MAP[tok[1]])

def parse_card_list(inner):
    return [parse_card(p) for p in inner.split(",") if p.strip()]

def eval_5(cards):
    ranks = sorted((c[0] for c in cards), reverse=True)
    suits = [c[1] for c in cards]
    is_flush = len(set(suits)) == 1
    cnt = Counter(ranks)
    counts = sorted(cnt.values(), reverse=True)
    by_freq = sorted(cnt.keys(), key=lambda r: (cnt[r], r), reverse=True)
    unique = sorted(set(ranks), reverse=True)
    is_straight, straight_high = False, 0
    if len(unique) == 5:
        if unique[0] - unique[4] == 4:
            is_straight, straight_high = True, unique[0]
        elif unique == [14, 5, 4, 3, 2]:
            is_straight, straight_high = True, 5
    if is_straight and is_flush:
        return (8, straight_high)
    if counts == [4, 1]:
        return (7, by_freq[0], by_freq[1])
    if counts == [3, 2]:
        return (6, by_freq[0], by_freq[1])
    if is_flush:
        return (5, *ranks)
    if is_straight:
        return (4, straight_high)
    if counts == [3, 1, 1]:
        kickers = sorted((r for r in ranks if r != by_freq[0]), reverse=True)
        return (3, by_freq[0], *kickers)
    if counts == [2, 2, 1]:
        pairs = sorted((r for r, c in cnt.items() if c == 2), reverse=True)
        kicker = next(r for r, c in cnt.items() if c == 1)
        return (2, pairs[0], pairs[1], kicker)
    if counts == [2, 1, 1, 1]:
        kickers = sorted((r for r in ranks if r != by_freq[0]), reverse=True)
        return (1, by_freq[0], *kickers)
    return (0, *ranks)

def omaha_best(hole, board):
    best = None
    for h in combinations(hole, 2):
        for b in combinations(board, 3):
            score = eval_5(h + b)
            if best is None or score > best:
                best = score
    return best

def count_outs(hero, villains, board):
    known = set(hero) | set(board)
    for v in villains:
        known.update(v)
    outs = 0
    for river in (c for c in ALL_CARDS if c not in known):
        full = board + [river]
        hs = omaha_best(hero, full)
        if all(hs > omaha_best(v, full) for v in villains):
            outs += 1
    return outs

def parse_round(text):
    def grab(pat):
        return parse_card_list(re.search(pat, text).group(1))
    return (
        grab(r"k1ne[^\n]*\[([^\]]+)\]"),
        [
            grab(r"cq[^\n]*\[([^\]]+)\]"),
            grab(r"F1iAz[^\n]*\[([^\]]+)\]"),
            grab(r"ddn[^\n]*\[([^\]]+)\]"),
        ],
        grab(r"Board[^\n]*\[([^\]]+)\]"),
    )

def main():
    r = remote("nc1.ctfplus.cn", 15185, timeout=20)
    for _ in range(5):
        data = r.recvuntil(b"(15s) > ", timeout=18)
        hero, villains, board = parse_round(data.decode("utf-8", errors="replace"))
        r.sendline(str(count_outs(hero, villains, board)).encode())
    prin...