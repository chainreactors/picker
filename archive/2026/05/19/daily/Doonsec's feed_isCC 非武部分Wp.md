---
title: isCC 非武部分Wp
url: https://mp.weixin.qq.com/s/AATBu3ijZJ6meWJasiGttg
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:00:56.998583
---

# isCC 非武部分Wp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5dTRhchoH8XcqksfXSzV1nibv1fAvQ4icqOZrNBWWSokSMjkOrESdV26Wb3mernI0lqtZ1Jly1RxIiaQe2xjCGsWnYU0jkdv0Ekhs/0?wx_fmt=jpeg)

# isCC 非武部分Wp

原创

玄网安全 oPis
玄网安全 oPis

玄网安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# isCC 非武部分Wp

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5c2eBSXE1HL7Xwj9EBIlcKm4VfNyH6m1TkBzKDY7DBvajT4ZiaAVkBDFLQcKuZcwEfoKm3LAUFrk2gwlH8r2HggtuhhE457CspQ/640?wx_fmt=jpeg&from=appmsg)

# MISC1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hiaeZ5goDm5e0685BKMsdSyzDcHW0OmUzQ4foQG5UMpWetc8qHxc8E3SnxWGiaK2rCohbj7WRDPKu1SRndbDUk1qx8gJmNnUxxcOZPDiaTEA5U/640?wx_fmt=png&from=appmsg)`大量垃圾流量，看到一条真正带数据的 HTTP`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hiaeZ5goDm5fvGOpNicHrtPJjx29SlBT7EENtbuwvorDopKOJYBDUWDx5giah6nyS3E3XvEHWFGX56IyFVQ1lLUbc8psQmkJ4F2aX7AloUricDM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hiaeZ5goDm5dSia9LN4FW01ia92jaCyTV64oDMmp6TVWtdbq1LBKpb32Tav9WsawibghUDoYIMiaDWkMvP8Oe0FX9aGAwUiaaic62LsK7pTktW0KJ4/640?wx_fmt=png&from=appmsg)`是个压缩包，是真压缩包，找密码`

`密码就在，那些垃圾流量数据里`

```
每条 UDP 载荷长度都一样，都是 28 字节 ASCII；
有一条内容重复出现了 4 次
```

![](https://mmbiz.qpic.cn/mmbiz_png/hiaeZ5goDm5cQmHnxXVrvQS1ceJZoel967P6k9eibtKD5lLFInaswo8BpzAKHHxWUwvR0L5KIOA24PiacqCMITr5CIYkTsiblkYentmFcY6Zsz0/640?wx_fmt=png&from=appmsg)`ShengDongJiXi@36-1-6`

`LSB隐写`![](https://mmbiz.qpic.cn/sz_mmbiz_png/hiaeZ5goDm5cmT8mz3txicoB51Ec6nu9Loia1EiaftOVjwwMF3TXQLXyibvp7GLOS1PibvwNQCvVuibkC35uhgVJKC4BR58qfCDp3roniapysR0bUXo/640?wx_fmt=png&from=appmsg)`ISCC{1d3f1c4t10gn_1s_Eth3_k3yl_t0_ivT1ct0ry}`

# MISC2

## 1. 题目结构

外层附件解压后得到：

* `barcode_00.png` ~ `barcode_20.png`（共 21 张）
* `score.rar`

核心是从 21 张图里恢复 21 行二进制，重建一个 21×21 二维码。

## 2. 三路取数（通用）

每张 PNG 都尝试 3 路信息源：

1. PNG Comment
2. 第 0 行红通道 LSB 解码文本（row0\_lsb）
3. Code128 条码正文

行格式统一匹配正则：`[A-U][0-9a-fA-F]{6}[A-U]`

即每行形如：`字母 + 6位hex + 相同字母`。

## 3. 按 A..U 排列并还原位图

拿到 A..U 后：

1. 按字母顺序排序
2. 取中间 6 hex，转成 24bit
3. 按系列规则取后 21bit（low 21 bits）
4. 21 行拼成 21×21 矩阵

本题样本中，二维码需要做一次黑白反相才能正常识别（这一点 PoC 里已自动穷举）。

![](https://mmbiz.qpic.cn/mmbiz_png/hiaeZ5goDm5cFH0aCsOd1kCbZ90DNmHL61X7tMr7BZpDGgxMUZeSwiaj5wCmvjhcXocB6dRqDDcMpJf8aXLXThDNgn91yYDwlfTGib6xRvicB84/640?wx_fmt=png&from=appmsg)

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
import zxing

ROW_RE = re.compile(r"([A-U][0-9a-fA-F]{6}[A-U])")
LETTERS = "ABCDEFGHIJKLMNOPQRSTU"

def extract_comment(im: Image.Image) -> str:
    info = im.info or {}
    c = info.get("Comment") or info.get("comment") or ""
    if isinstance(c, bytes):
        c = c.decode("utf-8", "ignore")
    return str(c)

def extract_row0_lsb_ascii(im: Image.Image) -> str:
    row = im.convert("RGB").crop((0, 0, im.width, 1))
    bits = "".join("1"if (r & 1) else"0"for (r, g, b) in row.getdata())
    out = []
    for i in range(0, len(bits), 8):
        b = bits[i : i + 8]
        if len(b) < 8:
            break
        v = int(b, 2)
        if v == 0:
            break
        out.append(chr(v) if 32 <= v < 127 else"?")
    return"".join(out)

def extract_code128(path: Path, reader: zxing.BarCodeReader) -> str:
    try:
        b = reader.decode(str(path), try_harder=True)
    except Exception:
        return""
    if b is None:
        return""
    return (getattr(b, "raw", "") or "").strip()

def collect_rows(root: Path) -> dict:
    reader = zxing.BarCodeReader()
    rows = {}

    imgs = sorted(root.glob("barcode_*.png"))
    if len(imgs) != 21:
        raise RuntimeError(f"expect 21 pngs, got {len(imgs)}")

    for p in imgs:
        im = Image.open(p)
        comment = extract_comment(im)
        lsb = extract_row0_lsb_ascii(im)
        code128 = extract_code128(p, reader)

        for src_name, txt in (("comment", comment), ("row0_lsb", lsb), ("code128", code128)):
            for m in ROW_RE.findall(txt):
                if m[0] == m[-1] and m[0] not in rows:
                    rows[m[0]] = {
                        "row": m,
                        "src": src_name,
                        "file": p.name,
                    }

    missing = [ch for ch in LETTERS if ch not in rows]
    if missing:
        raise RuntimeError(f"missing rows: {missing}")
    return rows

def build_matrix(rows: dict, mode: str, reverse_bits: bool) -> np.ndarray:
    # mode: tail -> use lower 21 bits from 24-bit, head -> use upper 21 bits
    mat = []
    for ch in LETTERS:
        hex6 = rows[ch]["row"][1:7]
        b24 = f"{int(hex6, 16):024b}"
        b21 = b24[-21:] if mode == "tail"else b24[:21]
        if reverse_bits:
            b21 = b21[::-1]
        mat.append([1 if c == "1"else 0 for c in b21])
    return np.array(mat, dtype=np.uint8)

def try_decode_qr_from_matrix(mat: np.ndarray) -> tuple[str, dict]:
    # brute-force common transform variants for this challenge family
    reader = zxing.BarCodeReader()
    out_dir = Path("E:/MCP/att18/variants")
    out_dir.mkdir(parents=True, exist_ok=True)
    idx = 0

    base_variants = [("base", mat), ("transpose", mat.T)]
    for base_name, m0 in base_variants:
        for rot in (0, 1, 2, 3):
            m1 = np.rot90(m0, rot)
            for invert in (False, True):
                m2 = (1 - m1) if invert else m1
                for border in (2, 4, 8):
                    canvas = np.pad(m2 * 255, border, mode="constant", constant_values=255)
                    img = np.kron(canvas, np.ones((8, 8), dtype=np.uint8))
                    f = out_dir / f"variant_{idx:04d}.png"
                    idx += 1
                    cv2.imwrite(str(f), img)

                    # 1) OpenCV
                    det = cv2.QRCodeDetector()
                    text, _, _ = det.detectAndDecode(img)
                    if text:
                        return text, {
                            "base": base_name,
                            "rot": rot,
                            "invert": invert,
                            "border": border,
                            "decoder": "opencv",
                            "image": str(f),
                        }

                    # 2) ZXing
                    try:
                        b = reader.decode(str(f), try_harder=True)
                    except Exception:
                        b = None
                    if b and getattr(b, "raw", ""):
                        return b.raw, {
                            "base": base_name,
                            "rot": rot,
                            "invert": invert,
                            "border": border,
                            "decoder": "zxing",
                            "image": str(f),
                        }

    return"", {}

def solve(root: Path, line3_digits: str) -> str:
    rows = collect_rows(root)

    print("[+] collected A..U rows")
    for ch in LETTERS:
        item = rows[ch]
        print(f"    {ch}: {item['row']}  ({item['src']} from {item['file']})")

    for mode in ("tail", "head"):
        for reverse_bits in (False, True):
            mat = build_matrix(rows, mode=mode, reverse_bits=reverse_bits)
            pwd, meta = try_decode_qr_from_matrix(mat)
            ifpwd:
                print("[+] QR decoded")
                print(f"    password: {pwd}")
                print(f"    variant : mode={mode}, reverse_bits={reverse_bits}, {meta}")
                flag = f"ISCC{{{pwd}{line3_digits}}}"
                print(f"[+] FLAG: {flag}")
                return flag

    raise RuntimeError("QR decode failed in all tested variants")

def main():
    ap = argparse.ArgumentParser(description="Black/White Strings generic solver PoC")
    ap.add_argument("--root", required=True, help="folder containing barcode_00..20.png and score.rar")
    ap.add_argument("--line3-digits", default="4151515", help="digits above line 3")
    args = ap.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"root not found: {root}")

    solve(root, args.line3_digits)

i...