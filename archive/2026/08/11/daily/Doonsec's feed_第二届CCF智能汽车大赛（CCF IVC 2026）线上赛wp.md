---
title: 第二届CCF智能汽车大赛（CCF IVC 2026）线上赛wp
url: https://mp.weixin.qq.com/s/HZRzFLioqX6ptS2rWX27Fw
source: Doonsec's feed
date: 2026-08-11
fetch_date: 2026-08-12T04:00:26.728020
---

# 第二届CCF智能汽车大赛（CCF IVC 2026）线上赛wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HYF1kyFLp05nfAHNOwqOrPYfHj3aibyN53n4Ddx6em90zib8rjQhLJYXMEa6eoIYV3G7VicEEHjszJtjFYNL2L5pK49JOECw2WXKZxFLTpGEAM/0?wx_fmt=jpeg)

# 第二届CCF智能汽车大赛（CCF IVC 2026）线上赛wp

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于secrets安全
，作者二狗26

![](https://wx.qlogo.cn/mmhead/5ZQ3V8nVdKpQhTdibbpU9ZF00YDKL3dlNMwPrd2pGs4LZ2Lo6gnlVm3WCwuOpLyPz9yZleibgAHWk/0)

**secrets安全**
.

凡事贵在坚持

# AURIX Shadow

题目描述：

```
车载ECU 固件逆向附件：aurix_shadow.zip
```

![](https://mmbiz.qpic.cn/mmbiz_png/HYF1kyFLp06lpF2tUCKl1CBWaA5Kia87YoK90my1FGL2RSYJ4nSZBT0B6ZwqaUKgRNPEHAhlC9eGEUG3vplWeAovzFZy38sVTPbTEVjzOuibI/640?wx_fmt=png&from=appmsg)

解题步骤：

这是一道 AURIX Shadow 题的详细分析。附件包含 ARM 网关固件对象（gateway\_fw.elf）、NCAL 标定区（nvm\_calibration.bin）、OTA capsule 和一段 UDS 记录。

udp\_diag.asc 里对 DID EF01 的读取返回 7F 22 33，说明这个 DID 被安全级别限制了。gateway\_fw.elf 是个 ELF32、ARM EABI5、小端、可重定位而且没剥离符号的对象。符号表里保留了 sub\_08001a10、sub\_08001c40 和 sub\_08002010 等函数。解码 sub\_08002010 用的 DID 表得到 ef01000702030000，其中 EF01 的 flags 为 7，需要的工程级别为 3，所以在线上直接读不到，得离线解。

nvm\_calibration.bin 以 NCAL 开头，记录数和表偏移都是大端。共 3 条记录，表偏移 0x18，每条 40 字节。第三条记录的 DID 是 EF01、flags 为 7、数据偏移为 0xd4、长度为 0x26，保护数据为：

```
7e743668b55d91c93de891e9a52efdef414125bb5bedac22959e2f9ed36dca5ae7d14d35d537
```

sub\_08001a10 是个 xorshift32 密钥流生成器。设 32 位初态为   ，每轮做三次移位异或：

每轮产生一个 32 位状态，按字节轮换取用：第 i 个流字节是   。

sub\_08001c40 是个滚动字节变换，初值   、计数器每步加 0x1d：

EF01 的处理链：先把密文 C 和密钥流    异或得到中间值 M，再对 M 做滚动变换，得到明文 F（即 flag）。

flag 格式固定，前缀是 flag{。把 flag{ 逆滚动回去，得到中间值前缀 3c7df1dff8，再和密文前五个字节异或，就拿到五个密钥流字节。

关键来了：xorshift32 的移位和异或在 GF(2) 上是线性运算。用 32 个单位向量（只有一个 bit 为 1）分别作为初态，生成前五个字节，就能列出 40 个二元线性方程。高斯消元后秩为 32，初态唯一确定：0x8572ed6d。

用这个初态生成 38 字节密钥流，异或后拿到中间值：

```
3c7df1dff8f991d3cc865930e166e1fcb5ecd8e34f7b6cface8c6c84f297c244a152f03bde46
```

再做一次滚动变换，flag 就出来了：flag{3d02c696a47d9e524d37241e33098bd0}。

为了验证没错，把 flag 逆滚动回去再和密钥流异或，重建出来的数据和 NCAL 里偏移 0xd4 的那 38 字节逐字节一致，说明整条链子跑对了。

解题过程

1. 先确认用的是原始附件。ZIP 的 SHA-256 应该是 279f503737c09195e83ae409f0dcc9e0e284bd7942c08a2a1a5235cd9b4181f0。

```
cd ”/root/Desktop/CTF/Re/AURIX Shadow”sha256sum aurix_shadow.zipunzip -o aurix_shadow.zip -d .
```

2. 确认固件的体系结构和保留的符号。应该看到 ELF32、ARM、little endian、REL、EABI5，还有 sub\_08001a10、sub\_08001c40、sub\_08002010。

```
file aurix_shadow/gateway_fw.elfreadelf -h aurix_shadow/gateway_fw.elfreadelf -sW aurix_shadow/gateway_fw.elf | grep 'sub_0800'
```

3. 按大端 40 字节一条读 NCAL 的第三条记录，然后读它的数据区。记录开头应该是 ef 01 00 07 00 00 00 d4 00 00 00 26，第二条命令能拿到完整的 38 字节保护数据。

```
xxd -g1 -s 0x68 -l 40 aurix_shadow/nvm_calibration.binxxd -p -s 0xd4 -l 38 aurix_shadow/nvm_calibration.bin
```

记录内容：

```
DID=0xef01flags=7data_offset=0xd4data_length=38ciphertext=7e743668b55d91c93de891e9a52efdef414125bb5bedac22959e2f9ed36dca5ae7d14d35d537
```

4. 把下面脚本存成题目目录里的 manual\_reproduce.py。脚本直接读原始 ZIP，逐条解析 EF01 记录；把 flag{ 逆滚动成 3c7df1dff8，用 32 个单位初态建二元方程组做高斯消元，然后打印初态、中间值、flag 和重建的密文。消元过程有 20 秒超时。

5. 跑一下分步脚本。矩阵秩应该是 32，初态唯一为 0x8572ed6d，中间值和 flag 如下：

```
python3 manual_reproduce.py
```

```
required_stream_prefix=3c7df1dff8matrix_rank=32initial_state=0x8572ed6dintermediate=3c7df1dff8f991d3cc865930e166e1fcb5ecd8e34f7b6cface8c6c84f297c244a152f03bde46flag=flag{3d02c696a47d9e524d37241e33098bd0}
```

6. 检查脚本输出的 rebuilt\_ciphertext，必须和步骤 3 从 NCAL 直接读的 38 字节一模一样。这个相等关系把已知前缀求出的初态、完整明文和原始 EF01 记录串到了一起，形成闭环验证。

```
rebuilt_ciphertext=7e743668b55d91c93de891e9a52efdef414125bb5bedac22959e2f9ed36dca5ae7d14d35d537
```

运行脚本

环境是 Python 3.10+，只用标准库。把 exp.py 和原始 aurix\_shadow.zip 放同一目录。

```
import structimport timeimport zipfilefrom pathlib import Path DEADLINE_SECONDS = 20.0MAX_RECORDS = 256 def step_state(value):    ”””xorshift32 的一步迭代。”””    value ^= (value << 13) & 0xFFFFFFFF    value ^= value >> 17    value ^= (value << 5) & 0xFFFFFFFF    return value & 0xFFFFFFFF def make_stream(state, length):    ”””从初态生成密钥流字节。每轮迭代出一个 32 位状态，按小端取字节。”””    result = bytearray()    for position in range(length):        state = step_state(state)        result.append((state >> (8 * (position % 4))) & 0xFF)    return bytes(result) def undo_rolling(data):    ”””逆滚动变换（密文 → 中间值）。”””    rolling = 0x5A    counter = 0    result = bytearray()    for transformed in data:        result.append(transformed ^ (rolling & 0xFF))        rolling = ((rolling & 0xFF) << 1) ^ counter ^ transformed ^ 0xC3        counter += 0x1D    return bytes(result) def apply_rolling(data):    ”””正向滚动变换（中间值 → 明文）。”””    rolling = 0x5A    counter = 0    result = bytearray()    for original in data:        transformed = original ^ (rolling & 0xFF)        result.append(transformed)        rolling = ((rolling & 0xFF) << 1) ^ counter ^ transformed ^ 0xC3        counter += 0x1D    return bytes(result) def locate_record(nvm, target_did):    ”””在 NCAL 标定区中查找指定 DID 的记录。”””    count, table = struct.unpack_from(”>II”, nvm, 8)    if count > MAX_RECORDS:        raise ValueError(”记录数超限”)    for record_index in range(count):        offset = table + 40 * record_index        did, flags, data_offset, length = struct.unpack_from(”>HHII”, nvm, offset)        if did == target_did:            return record_index, flags, data_offset, nvm[data_offset : data_offset + length]    raise ValueError(”目标 DID 不存在”) def solve(ciphertext, expected_prefix, deadline):    ”””用已知前缀求解 xorshift32 初态。     xorshift32 对初态是线性的（在 GF(2) 上），    用 32 个单位基向量生成样本，建立方程组并高斯消元。    ”””
逆滚动得到中间值前缀    stream_prefix = undo_rolling(expected_prefix)  ## 32 个单位向量做初态，生成基    columns = [make_stream(1 << bit, len(stream_prefix)) for bit in range(32)]  ## 建方程：每个字节的每个 bit 对应一个方程    equations = []    for byte_index, expected in enumerate(stream_prefix):        observed = ciphertext[byte_index] ^ expected        for bit_index in range(8):            coefficients = sum(                (((columns[column][byte_index] >> bit_index) & 1) << column)                for column in range(32)            )            equations.append([coefficients, (observed >> bit_index) & 1])  ## 高斯消元    pivots = []    row_index = 0    for column in range(32):        if time.monotonic() > deadline:            raise TimeoutError(”求解超时”)        selected = next(            (row for row in range(row_index, len(equations)) if equations[row][0] & (1 << column)),            None,        )        if selected is None:            continue        equations[row_index], equations[selected] = equations[selected], equations[row_index]        for row in range(len(equations)):            if row != row_index and equations[row][0] & (1 << column):                equations[row][0] ^= equations[row_index][0]                equations[row][1] ^= equations[row_index][1]        pivots.append(column)        row_index += 1    if len(pivots) != 32 or any(mask == 0 and value for mask, value in equations):        raise ValueError(”无法得到唯一初态”)    state = sum((equations[row][1] << column) for row, column in enumerate(pivots))    return state, len(pivots) def main():    deadline = time.monotonic() + DEADLINE_SECONDS    archive_path = Path(file).with_name(”aurix_shadow.zip”)    with zipfile.ZipFile(archive_path) as archive:        nvm_name = next(name for name in archive.namelist() if name.endswith(”nvm_calibration.bin”))        nvm = archive.read(nvm_name)    if nvm[:4] != b”NCAL”:        raise ValueError(”NCAL 魔数错误”)    record_index, flags, data_offset, ciphertext = locate_record(nvm, 0xEF01)  ## 用已知前缀 flag{ 求解 xorshift32 初态    state, rank = solve(ciphertext, b”flag{”, deadline)  ## 生成完整密钥流，异或 + 滚动变换拿到 flag    stream = make_stream(state, len(ciphertext))    intermediate = bytes(value ^ stream[index] for index, value in enumerate(ciphertext))    flag = apply_rolling(intermediate)  ## 验证：重建密文应该和原始一致    rebuilt = bytes(        value ^ stream[index] for index, value in enumerate(undo_rolling(flag))    )    if rebuilt != ciphertext:        raise ValueError(”重加密不匹配”)    print(f”record_index={record_index}”)    print(f”flags={flags}”)    print(f”data_offset=0x{data_offset:02x}”)    print(f”data_length={len(ciphertext)}”)    print(f”required_stream_prefix={undo_rolling(b'flag{').hex()}”)    print(f”matrix_rank={rank}”)  ...