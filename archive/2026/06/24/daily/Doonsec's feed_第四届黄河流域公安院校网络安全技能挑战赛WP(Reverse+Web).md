---
title: 第四届黄河流域公安院校网络安全技能挑战赛WP(Reverse+Web)
url: https://mp.weixin.qq.com/s/v2wxeX2IHRg65vXx7pK7Uw
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:04:17.315206
---

# 第四届黄河流域公安院校网络安全技能挑战赛WP(Reverse+Web)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tNS6iaKdc2uvnd7cALXmUBa5Jn3p1A63VKq5eGuSPDx16jn0QwEibicBmrQWGpYBEFU6qpjibg6GU6hfL0D7ibvX4ibnIVKF7rHYib3XlHX6GA3AwQ/0?wx_fmt=jpeg)

# 第四届黄河流域公安院校网络安全技能挑战赛WP(Reverse+Web)

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于沉思安全
，作者x3x\_bot

![](http://wx.qlogo.cn/mmhead/LTpwfH82ricmd0KHzGqehNEEwzZt6BXzI73pSJOp00riaWMEU7odeicdaJ5KDBltzq2VkUPbibZyxCw/0)

**沉思安全**

## 目录

* Reverse

+ Flow
+ Rose
+ Salome
+ TIME
+ Yield
+ 遥遥领先

* Web

+ Note
+ ez3pring
+ ezlog
+ real\_Grafana
+ 喵喵宠物医院
+ 川味小厨

## Reverse

### Flow

#### 题目概述

`attachments/Flow` 是包含`Flow_rev.exe` 的 ZIP 存档。可执行文件是用 UPX 打包的 64 位 Windows PE，但加壳标识符已从`UPX0/UPX1/UPX2/UPX!`重命名为`VMP0/VMP1/VMP2/VMP!`。

#### 关键发现

* 恢复 UPX 部分名称和副本上的魔法允许`upx -d`解压二进制文件。
* 可见支票接受`flag{why_you_think_it_is_flag}`，但平台提交拒绝了它。
* 二进制文件为 `lstrcmpA` 安装了一个 IAT hook；该 hook 忽略 `lstrcmpA` 参数，并在 24 字节 flag 中间部分执行真正检查。
* 真正的钩子检查使用生成的 16 字节密钥和类似 XXTEA 的 6 字转换。

#### 解题过程

1. 将打包的 PE 标识符的副本从`VMP*`修补到`UPX*`。
2. 使用 UPX 解包。
3. 逆转可见的类RC4检查，并在平台拒绝后将其识别为诱饵。
4. 分析安装到 `lstrcmpA` 上的 IAT hook，重点看 `0x140001830`。
5. 移植 hook key 生成器和类似 XXTEA 的逆变换。
6. 解密隐藏目标，恢复真正的 flag 中间部分。

#### 最终结果

`flag{Y0u@regrEatreveRser_1145}`

#### 求解脚本

```
from pathlib import Path
import hashlib
import math
import re
import struct
import zipfile

ROOT = Path(__file__).resolve().parent
ZIP_PATH = ROOT / "attachments" / "Flow"
EXE_PATH = ROOT / "attachments" / "Flow_rev.exe"
IMAGE_BASE = 0x140000000
VMP0_RVA = 0x1000
VMP1_RVA = 0xE000
VMP1_RAW = 0x200
VMP1_SIZE = 0x5600
COMP_RVA = 0xE025
OEP_RVA = 0x13F0
KEY = b"wowyoufindit?"
TARGET = bytes.fromhex("b1 f1 76 13 91 62 fb 72 56 3b a4 8d 45 27 e6 d3 b1 e1 c6 02 09 1d d6 f3")
REAL_TARGET = bytes.fromhex(
    "46 d4 14 39 26 50 da f1 87 5c b2 7d 36 2d 6e a3"
    "34 23 36 cc 74 1f 84 5c"
)
T_C0 = bytes.fromhex("c7 ea 45 6f 83 52 c5 f3 3a ee b0 97 b5 95 86 77")
T_D0 = bytes.fromhex("05 06 04 07 01 06 07 02 05 05 02 03 05 01 06 04")
T_E0 = bytes.fromhex("02 03 04 05 02 06 02 05 04 03 05 03 05 07 01 01")
T_F0 = bytes.fromhex("07 03 0e 0f 0c 09 00 02 0d 04 0b 05 0a 08 01 06")
T_100 = bytes.fromhex("08 03 01 0b 04 05 0d 02 07 0c 00 0f 0a 06 09 0e")
T_110 = bytes.fromhex("04 0b 01 0a 08 03 0e 07 0d 0f 06 02 0c 00 09 05")
T_120 = bytes.fromhex("74 b7 1c 41 15 b8 ff b5 24 4d 25 57 23 7c 21 05")
T_130 = bytes.fromhex("53 9c 0a c1 16 d7 71 47 76 57 68 32 d8 ad af a7")
T_140 = bytes.fromhex("b9 fa b9 a0 cd 01 d8 22 f3 50 cf 3d c2 6d 79 4d")
MASK32 = 0xFFFFFFFF

def load_exe() -> bytes:
    if EXE_PATH.exists():
        return EXE_PATH.read_bytes()
    with zipfile.ZipFile(ZIP_PATH) as zf:
        return zf.read("Flow_rev.exe")

def u32(buf: bytes, off: int) -> int:
    return struct.unpack_from("<I", buf, off)[0]

def p32(buf: bytearray, off: int, val: int) -> None:
    struct.pack_into("<I", buf, off, val & 0xFFFFFFFF)

def p64(buf: bytearray, off: int, val: int) -> None:
    struct.pack_into("<Q", buf, off, val & 0xFFFFFFFFFFFFFFFF)

def sign32(x: int) -> int:
    x &= 0xFFFFFFFF
    return x - 0x100000000if x & 0x80000000else x

class StubBits:
    def __init__(self, data: bytes, src: int):
        self.data = data
        self.src = src
        self.ebx = 0
        self.dl = data[src]

    def bit(self) -> int:
        val = self.ebx << 1
        carry = 1if val > 0xFFFFFFFFelse0
        self.ebx = val & 0xFFFFFFFF
        if self.ebx == 0:
            word = u32(self.data, self.src)
            self.src += 4
            val = (word << 1) + carry
            carry = 1if val > 0xFFFFFFFFelse0
            self.ebx = val & 0xFFFFFFFF
            self.dl = self.data[self.src]
        return carry

def initial_memory(data: bytes) -> bytearray:
    mem = bytearray(0x15000)
    headers = min(0x200, len(data))
    mem[:headers] = data[:headers]
    sections = parse_sections(data)
    for _name, va, _sz, rp, rs in sections:
        if rs:
            mem[va : va + rs] = data[rp : rp + rs]
    return mem

def unpack_vmp0(data: bytes) -> tuple[bytearray, int]:
    src = VMP1_RAW + (COMP_RVA - VMP1_RVA)
    bits = StubBits(data, src)
    mem = initial_memory(data)
    dst = VMP0_RVA
    ecx = 0
    rbp = -1

    whileTrue:
        bits.dl = data[bits.src]
        if bits.bit():
            bits.src += 1
            mem[dst] = bits.dl
            dst += 1
            continue

        eax = ecx + 1
        whileTrue:
            eax = ((eax << 1) + bits.bit()) & 0xFFFFFFFF
            if bits.bit():
                break

        old_eax = eax
        eax = (eax - 3) & 0xFFFFFFFF
        if old_eax >= 3:
            eax = (((eax << 8) & 0xFFFFFFFF) | bits.dl) & 0xFFFFFFFF
            bits.src += 1
            eax ^= 0xFFFFFFFF
            if eax == 0:
                break
            rbp = sign32(eax)

        eax = ecx + 1
        ecx = ((ecx << 1) + bits.bit()) & 0xFFFFFFFF
        ecx = ((ecx << 1) + bits.bit()) & 0xFFFFFFFF

        if ecx == 0:
            ecx = eax
            eax += 2
            whileTrue:
                ecx = ((ecx << 1) + bits.bit()) & 0xFFFFFFFF
                if bits.bit():
                    break

        rbp_u = rbp & 0xFFFFFFFFFFFFFFFF
        carry = 1if rbp_u < 0xFFFFFFFFFFFFF300else0
        ecx = (ecx + eax + carry) & 0xFFFFFFFF

        start = dst + rbp
        if start < 0:
            raise ValueError(f"bad backref start={start} dst={dst} rbp={rbp}")
        for _ in range(ecx):
            mem[dst] = mem[start]
            dst += 1
            start += 1
        ecx = 0

    return mem[VMP0_RVA:dst], bits.src

def apply_call_fixups(buf: bytearray) -> int:
    # Apply the branch-target transform at 0x1400133c6..0x14001341a.
    size = 0x7600
    end = size - 3
    pos = 0
    fixed = 0
    dl = 7
    while pos < end:
        al = buf[pos]
        pos += 1
        candidate = False
        if0x80 <= al <= 0x8Fand pos >= 2and buf[pos - 2] == 0x0F:
            candidate = True
        elif ((al - 0xE8) & 0xFF) <= 1:
            candidate = True
        ifnot candidate or pos >= end:
            continue

        saved = pos
        val = u32(buf, pos)
        pos += 4
        if ((val & 0xFF) - dl) & 0xFF:
            pos = saved
            continue

        eax = int.from_bytes(val.to_bytes(4, "little")[::-1], "little")
        eax = (eax - saved + 0x1000) & 0xFFFFFFFF
        p32(buf, saved, eax)
        fixed += 1
    return fixed

def parse_sections(data: bytes):
    e_lfanew = u32(data, 0x3C)
    nsec = struct.unpack_from("<H", data, e_lfanew + 6)[0]
    opt_size = struct.unpack_from("<H", data, e_lfanew + 20)[0]
    sec_off = e_lfanew + 24 + opt_size
    sections = []
    for i in range(nsec):
        off = sec_off + 40 * i
        name = data[off : off + 8].rstrip(b"\0").decode("latin1")
        vs, va, rs, rp = struct.unpack_from("<IIII", data, off + 8)
        sections.append((name, va, max(vs, rs), rp, rs))
    return sections

def rva_to_off(sections, rva: int) -> int | None:
    for _name, va, sz, rp, rs in sections:
        if va <= rva < va + sz and rs:
            return rp + (rva - va)
    returnNone

def build_memory(data: bytes, unpacked: bytearray) -> bytearray:
    mem = initial_memory(data)
    mem[VMP0_RVA : VMP0_RVA + len(unpacked)] = unpacked
    return mem

def apply_reloc_fixups(mem: bytearray) -> int:
    # Apply 0x14001347b..0x1400134b1. The relocation stream starts
    # immediately after the import-table stream used by the loader stub.
    pos = 0x12000
    while u32(mem, pos) != 0:
        _dll_name_rva = u32(mem, pos)
        pos += 8
        while mem[pos] != 0:
            pos += 1
            while mem[pos] != 0:
                pos += 1
            pos += 1
        pos += 1
    pos += 4

    rbx = VMP0_RVA - 4
    count = 0
    whileTrue:
        al = mem[pos]
        pos += 1
        if al == 0:
            break
        if al > 0xEF:
            al = (al & 0x0F) << 16
            al |= struct.unpack_from("<H", mem, pos)[0]
            pos += 2
        rbx += al
        raw = struct.unpack_from("<Q", mem, rbx)[0]
  ...