---
title: PKWCTF新生RE-“看看就好”
url: https://mp.weixin.qq.com/s/WgwWHAVmAVgSyzbNupXXZw
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:39:29.020949
---

# PKWCTF新生RE-“看看就好”

# PKWCTF新生RE-“看看就好”

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于玄网安全
，作者opis

![](https://wx.qlogo.cn/mmhead/Kwg1Hs1pPD0mGibcJsKaQBhSibOTFO3KdIhlo3BZ9icSv9MsJm3X0x62ts5A8gZmUcRothAx79K6Ck/0)

**玄网安全**
.

ctf竞赛交流，网络大臭虫一个

# RE1:糖衣炮弹

`拖到txt就有`![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5ficEr6ZcfxZXHM7Ffce3YdY0eJnwII5lNlWcam8UO8IOZYuevJ7RQoFAW3GaibwY9woD15ezsBY5wBgfXfvQjdh2RngGBLNw2OM/640?wx_fmt=webp&from=appmsg)

# RE2:gogogo！出发咯

`分析 mian函数`

```
if ( (unsigned __int64)v22 <= *(_QWORD *)(v2 + 16) )
    runtime_morestack_noctxt_abi0();
  v21 = &unk_140186C98;
  v22[0] = &off_1400DBB58;
  fmt_Println(v0, v1);
  v22[18] = &v21;
  v21 = &unk_140186C98;
  v22[0] = &off_1400DBB68;
  v22[19] = &v21;
  v22[20] = 1LL;
  v22[21] = 1LL;
  fmt_Print(v0, v1, (unsigned int)&off_1400DBB68, 1, v3, v4, v20);
  bufio_NewReader(v0, v1, v5, v6, v7, v8);
  v22[3] = bufio___Reader__ReadString(v0, v1, v9, v10, v11, v12);
  v22[4] = 10LL;
  v22[1] = v13;
  v22[2] = v0;
  strings_TrimSpace(v0, v0, v13, v13, v14, v15);
  if ( (unsigned __int8)main_xorCheckLookHere(v0, v0, v16, v17, v18, v19) )
  {
    v22[9] = &v21;
    v21 = &unk_140186C98;
    v22[0] = &off_1400DBB78;
    v22[10] = &v21;
    v22[11] = 1LL;
    v22[12] = 1LL;
  }
  else
  {
    v22[5] = &v21;
    v21 = &unk_140186C98;
    v22[0] = &off_1400DBB88;
    v22[6] = &v21;
    v22[7] = 1LL;
    v22[8] = 1LL;
  }
  fmt_Println(v0, v0);
}
```

`1：main_xorCheckLookHere 校验函数`

```
__int64 __fastcall main_xorCheckLookHere(__int64 a1)
{
  __int64 v1; // rax
  unsigned __int64 v2; // rbx
  unsigned __int64 i; // [rsp+2h] [rbp-18h]

  if ( v2 != qword_14019E438 )
    return 0LL;
  for ( i = 0LL; (__int64)i < (__int64)v2; ++i )
  {
    if ( i >= v2 )
      ((void (__noreturn *)(void))runtime_panicBounds)();
    if ( qword_14019E438 <= i )
      runtime_panicBounds(
        a1,
        main_encryptedFlag,
        i,
        (unsigned __int8)runtime_noptrdata ^ (unsigned int)*(unsigned __int8 *)(v1 + i));
    if ( *((_BYTE *)main_encryptedFlag + i) != ((unsigned __int8)runtime_noptrdata ^ *(_BYTE *)(v1 + i)) )
      return 0LL;
  }
  return 1LL;
}
```

`2：main.xorKey 与 main.encryptedFlag 存放密钥和密文`

```
.data:000000014019E430 main_encryptedFlag dq offset unk_1400D05FB
.data:000000014019E430                                         ; DATA XREF: main_xorCheckLookHere+8B↑r
.data:000000014019E438 qword_14019E438 dq 8                    ; DATA XREF: main_xorCheckLookHere+1C↑r
```

`3：main.beginnerHint 是提示字符串`

```
.data:000000014019E440 main_beginnerHint dq offset aNotSupportedFo+1621h
```

```
main 函数读入一行输入后，会走两条分支：

如果输入正好是 4 字节的 hint（代码里按小端比较 0x746e6968），程序会打印提示：hint: xor key = 0x12, cipher = BYEQFTio。
否则进入 xorCheckLookHere。这个函数要求输入长度必须为 8，然后把每个字节与 0x12 异或，再逐字节和密文 BYEQFTio 比较。全部通过则打印 Correct。

flag:PKWCTF{}
```

# RE3:澳门新葡京

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hiaeZ5goDm5ducz2z6NVwRpMhOjA0iaY5XZ6qrdMvU0nwEtD9cJ1DHSaTHDUAS2jMCfaTt0QLElkgFPCx6fKXbhwCJxlfOficZw8bHGQpC57j8/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cp93DIEib8iakic2YY5UHkTxQhwtRsPKNbhe9dVX7MvRianTbe4umVHROBEicuoOlSiaN4Gs7LT2FoH5cCMIEG7udmkribU5Ukk4c9gc/640?wx_fmt=webp&from=appmsg)`FLAG:PKWCTF{CQqQqQqQqQqQq_YOU}`

# RE4:糖衣炮弹2

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5fGC2tJtbhEVdTKmGjKYbmox9QDHDcPnJJR7mPVemt16ibXVicNtOSzMUtz4ibia5qEeATBbbOMgRUBRaQDwbnydEuaNMU5QQVTEXM/640?wx_fmt=webp&from=appmsg)`16机制看到 不是upx，需要修改，在脱壳`

```
xxd -s 0x180 -l 8 tang2.exe
xxd -s 0x1b0 -l 8 tang2.exe
xxd -s 0x1d8 -l 8 tang2.exe
```

`脱壳：/mnt/d/CTF/CTF-RE/upx-5.0.1-win64/upx.exe -d tang2.exe`

![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5cxCh682E2Nsibe8AUntPNR8v2RuyQlqYG4aaBu1MfouaN8jSjCByzQAGBHs0mIdNeAAbggLQf8npTlvbhLUc4zLWia5icUUC2ntY/640?wx_fmt=webp&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_jpg/hiaeZ5goDm5e39Tvss0GItOWSOXYFqkcqJGZcZLZQZt1Gug0CY9vb9RojQ25YxjVNnrAHr2CKy2a4ibIrooRJUWzDsbl05Scp4SBqyeJHJEeM/640?wx_fmt=webp&from=appmsg)

```
uint8_t __fastcall enc_char(uint8_t ch_0, size_t index)
{
  uint8_t v2; // al
  char v3; // r8

  v2 = rol8(ch_0 ^ (13 * index + 90), (index & 3) + 1);
  return 9 * v3 + v2 + 23;
}
真实逻辑只有这些：

长度不是 25，直接返回 0。
i 从 0 到 24：计算 enc_char(input[i], i)，必须等于 target[i]。
有一个字节不相等就返回 0。
25 个字节全过，返回 1，main 里就会打印 Correct!。
```

```
x   = in[i] XOR ((0x0D * i + 0x5A) & 0xFF)
r   = ROL8(x, (i & 3) + 1)
out = (r + 9 * i + 0x17) & 0xFF

flag{easy_reverse_signin}
```

# RE5:S级任务！追击！呆呆鸟！

外层是 Dodo Extraction 壳，内嵌 Unity 游戏。`DecryptFlag` 把 `DODO-EXFIL-v2|` 和 8 个密钥碎片拼起来做 SHA-256，再作为 AES-CBC 的 key 解密 flag。提示里的自杀只是游戏内 `HP - 1`，不用打通关。

## 解题过程

### 第 1 步：从壳里取出脚本

exe 是 32 位 .NET，入口 `_CorExeMain`。`#US` 里有 `payload.zip`、`DodoExtraction.exe`。zip 附在文件末尾，可直接当 zip 打开。游戏脚本在：

```
DodoExtraction_Data/Managed/Assembly-CSharp.dll
```

用户字符串里能看到 `自杀协议执行：HP -1`、`DODO-EXFIL-v2|`、两段 Base64，以及 8 个 4 字符碎片：`K9Q2`、`7M4X`、`P8VA`、`2N6C`、`R5TJ`、`W3HL`、`F7ZD`、`B1YS`。

### 第 2 步：按 DecryptFlag 解密

`DecryptFlag` 的 IL 是：

1. `String.Join("|", recoveredKeyFragments)`
2. 再接上前缀 `DODO-EXFIL-v2|`
3. UTF-8 后 `SHA256`，结果作为 AES key
4. IV = Base64(`aW52LWRvZG8tMjAyNiEhIQ==`) = `inv-dodo-2026!!!`
5. 密文 = Base64(`fEoFX9UwUuJyvBmccIHNVj6K8he+O47LrLHbJF4WYFQ=`)
6. AES-CBC 解密，去掉 PKCS7

```
import base64
import hashlib
import io
import re
import zipfile
from pathlib import Path

import dnfile
from Crypto.Cipher import AES

exe = next(
    p
    for p in Path(r"C:\Users\34645\Downloads\S级任务！追击！呆呆鸟！！").iterdir()
    if p.suffix.lower() == ".exe"
)

raw = exe.read_bytes()
dll = zipfile.ZipFile(io.BytesIO(raw)).read(
    "DodoExtraction_Data/Managed/Assembly-CSharp.dll"
)
dll_path = Path(r"C:\Users\34645\AppData\Local\Temp\opencode\dodo\Assembly-CSharp.dll")
dll_path.parent.mkdir(parents=True, exist_ok=True)
dll_path.write_bytes(dll)

pe = dnfile.dnPE(str(dll_path))
us = pe.net.user_strings
blob = dll[us.file_offset : us.file_offset + us.sizeof()]

strings = []
i = 1
while i < len(blob):
    b = blob[i]
    if b == 0:
        i += 1
        continue
    if b & 0x80 == 0:
        ln, i = b, i + 1
    elif b & 0xC0 == 0x80:
        ln, i = ((b & 0x3F) << 8) | blob[i + 1], i + 2
    else:
        ln = ((b & 0x1F) << 24) | (blob[i + 1] << 16) | (blob[i + 2] << 8) | blob[i + 3]
        i += 4
    raw_s = blob[i : i + ln]
    i += ln
    if raw_s:
        strings.append(raw_s[:-1].decode("utf-16le"))

prefix = next(s for s in strings if s.startswith("DODO-EXFIL-v2"))
blobs = []
for s in strings:
    try:
        dec = base64.b64decode(s, validate=True)
    except Exception:
        continue
    if dec and re.fullmatch(r"[A-Za-z0-9+/=]+", s):
        blobs.append(dec)
iv = next(b for b in blobs if len(b) == 16)
ct = next(b for b in blobs if len(b) > 16)
fragments = [s for s in strings if re.fullmatch(r"(?=.*\d)[A-Z0-9]{4}", s)]

material = prefix + "|".join(fragments)
key = hashlib.sha256(material.encode()).digest()
pt = AES.new(key, AES.MODE_CBC, iv).decrypt(ct)
print(pt[: -pt[-1]].decode())
```

运行输出：

```
PKWCTF{D0_y0U_LiK3_G@M3?}
```

# RE6:空城计

```
1. 文件里有什么
目录里只有两样东西：

source.c：注释说「实际施工后剩下一个 main」，函数体就是 return 0。
空城计.exe：7680 字节，32 位 PE，镜像基址 0x400000。
节表：

节 RVA 文件偏移 内容
.text 0x1000 0x400 7 字节，就是 main
.rdata 0x2000 0x600 导入表、TLS 目录
.data 0x3000 0xA00 真正的代码和密文
.reloc 0x5000 0x1C00 重定位
main（0x401000）只有：

push ebp
mov  ebp, esp
xor  eax, eax
pop  ebp
ret
导入的 API 却是 CreateFileW、ReadFile、CloseHandle、ExitProcess、AddVectoredExceptionHandler、MessageBoxW。空的 main 用不到这些，说明逻辑在别处。

2. 入口不在 main，而在 TLS
PE 的 TLS 目录在 RVA 0x2048。IMAGE_TLS_DIRECTORY32.AddressOfCallBacks = 0x402024，回调表第一项是 0x403000，第二项是 0。

进程加载时，系统会在 main 之前调用 0x403000。这段代码在 .data 里，不是 .text。

3. TLS 回调 0x403000：只处理进程附加
cmp  dword ptr [ebp+0xC], 1     ; DLL_PROCESS_ATTACH
jne  0x403080                   ; 不是附加就直接返回
call $+5
pop  esi                        ; esi = 0x40300E
lea  edx, [esi+0xF2]            ; edx = 0x403100，VEH 处理函数
mov  eax, [esi+0x1006]          ; IAT：AddVectoredExceptionHandler
push edx
push 1                          ; First = TRUE，插到处理链最前
call dword ptr [eax]
Reason != 1 时直接 ret 0xC。注册失败则调用 ExitProc...