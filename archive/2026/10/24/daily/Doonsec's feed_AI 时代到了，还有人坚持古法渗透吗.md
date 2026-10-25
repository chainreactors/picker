---
title: AI 时代到了，还有人坚持古法渗透吗
url: https://mp.weixin.qq.com/s/jEyLhlIkl1DL-zs2vDoaSg
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:05:11.727915
---

# AI 时代到了，还有人坚持古法渗透吗

# AI 时代到了，还有人坚持古法渗透吗

原创

private null
private null

轩公子谈技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

没错，我还在坚持，因为 no money，no token

                                ![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsRSVBxld5mnyrrC89thTgf9xTQ6pqzUk5DAVy69gbHIRibS8gwlp3tZ6w6wNtGF5PrQ23Z0h6Shgve7Dg9pvKbMmjicBS6U3L2E/640?wx_fmt=png)

现在这个时代，发展的太快了，还记得那时候第一次用 cursor，快捷键打开输入框，根据注释生成代码，比如使用 socket 包 写一个端口扫描工具，回车，代码唰唰唰的出来了，可以直接运行

再到网页版 gpt 对话，某某某漏洞，如何绕 waf，

再到 ai agent 前台渗透，后台渗透，至内网渗透，貌似一眼望到了头。

回到主题了，本次开局仍是登陆框，古法渗透，ai 渗透，都未发现漏洞，但好在有指纹，可以找到开发商

系统是 net 开发的，分 mvc 和 form 版，这个项目是 form 架构

我们都知道，java 有 jar 包，.net 也有类似的打包机制

net 也是一样，cs 为源码，cs 直接运行不了，编译之后会变成 dll 文件，再去调用，将 dll 整个打包成 exe，跟把东西装进快递箱一个道理

使用dotnet publish -p:PublishSingleFile=true 后，所有 DLL 会被塞进一个 exe 文件里。这个 exe 叫做单文件 Bundle。

结构如下：

```
┌──────────────────────────────────┐│  PE 文件头 + Native 启动器        │  ← 标准 Windows 可执行文件│  (约 9 MB)                       │├──────────────────────────────────┤│                                  ││  内嵌的 DLL 1 (如 xx.WebApi.dll)│  内嵌的 DLL 2 (如 xx.Service.dll)│  ...                             ││  内嵌的 DLL 369                   │  ← 106 MB 的内嵌文件│                                  │├──────────────────────────────────┤│  Bundle Header                   │  ← 描述每个内嵌文件的位置│  (版本号 + 文件数 + 文件条目表)    │├──────────────────────────────────┤│  Header偏移量(8字节) + 签名(8字节)│  ← 指向 Bundle Header└──────────────────────────────────┘
```

官网只提供了 exe，并没有 cs 源码，所以目标就是把 exe 还原为 dll，再用ILSpy 反编译

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsJx13SJQ94AI0AGS4BXFzianFWUMXqeWubjfz5VO7ecsSPH57VuAa1Ux9T1FUdSIdgqUbXbPoS5osqqRLLogap6fJS3vd4DcXE/640?wx_fmt=png)

解析PE 头

详细的可以参考一下这个

https://learn.microsoft.com/en-us/windows/win32/debug/pe-format

```
第 0 字节:  "MZ"           ← 标记：我是一个 exe第 60 字节: 272            ← 提示：详细信息在 272 那里
第 272 字节: "PE"          ← 确认：这是 PE 格式第 276 字节: 0x8664        ← CPU: 64位第 278 字节: 10            ← 有 10 个节区第 292 字节: 240           ← Optional Header 长 240 字节
第 536 字节起: 节区清单    ← 每个节区 40 字节，记录名字+位置+大小
```

我们的目的只有一个：算出 PE 头占多大空间，剩下的就是 Bundle 数据。

```
PE 头结束 = 最后一个节区的位置 + 大小 = 9.2 MB文件总大小 = 116 MB→ 9.2 MB 之后全是 Bundle 内嵌的 DLL
```

大概上面这个意思， Python 脚本读取位置

```
import struct
with open("xx.WebApi.exe", "rb") as f:    data = f.read()
# ① 读取 DOS Header 中的 "MZ" 签名mz = data[0:2]print(mz)  # b'MZ'
# ② 读取 e_lfanew（PE 签名的偏移量）# 在 DOS Header 的第 0x3C 位置，读取 4 字节e_lfanew = struct.unpack('<I', data[0x3C:0x40])[0]print(e_lfanew)  # 272 (0x110)
# ③ 读取 PE 签名（在 e_lfanew 指向的位置）pe_sig = data[e_lfanew:e_lfanew+4]print(pe_sig)  # b'PE\x00\x00'
# ④ 读取 COFF Header（PE 签名之后 20 字节）coff_start = e_lfanew + 4  # 0x114machine = struct.unpack('<H', data[coff_start:coff_start+2])[0]num_sections = struct.unpack('<H', data[coff_start+2:coff_start+4])[0]opt_size = struct.unpack('<H', data[coff_start+16:coff_start+18])[0]print(coff_start,machine,num_sections,opt_size)
# ⑤ 读取 Optional Headeropt_start = coff_start + 20  # 0x128magic = struct.unpack('<H', data[opt_start:opt_start+2])[0]print(opt_start,magic)# ⑥ 读取 Section Headers（Optional Header 之后）sec_start = opt_start + opt_size  # 0x218print(sec_start)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtwgziblnT7wJ9ricS912pVTSBlw9XTSvicgVicsVk7CUO4fpiaY4ShrCorYcnJ04c0sM9pKOIqHsar0icdU2pLZKicZdR7OLAmE4MTFg/640?wx_fmt=png)

① DOS Header — "MZ" 签名

```
偏移 0x00-0x01: 字节 4d 5a = "MZ"
```

"MZ" 是什么？ 是 Mark Zbikowski 的名字缩写，他是 MS-DOS 的架构师。所有 Windows 可执行文件都以 "MZ" 开头，这是 DOS 时代留下的传统。

② e\_lfanew — PE 签名的位置

```
偏移 0x3C-0x3F: 字节 10 01 00 00
```

怎么算出 272？ 这是 little-endian（小端序） int32：

```
字节序列: 10 01 00 00小端序计算: 0x10 + 0x01×256 + 0x00×65536 + 0x00×16777216         = 16 + 256 + 0 + 0         = 272 (十六进制 0x110)
```

什么是小端序？ 就是低位字节在前、高位字节在后。大多数 x86 计算机都用小端序。读取多字节数值时，第一个字节是最低位。

e\_lfanew 的含义？ 告诉我们 PE 签名在文件的第 272（0x110）个字节处。

③ PE Signature

```
偏移 0x110-0x113: 字节 50 45 00 00 = "PE\0\0"
```

"PE" 后面跟两个空字节，这是 PE 文件的签名。

④ COFF Header

在 PE 签名之后（偏移 0x114），读取 20 字节：

```
Machine: 字节 64 86 → 小端序 0x8664 → AMD64 (64位 x86)NumberOfSections: 字节 0a 00 → 10 个节区SizeOfOptionalHeader: 字节 f0 00 → 240 字节
```

⑤ Optional Header

在 COFF Header 之后（偏移 0x128）：

```
Magic: 字节 0b 02 → 小端序 0x020b → PE32+ (64位)
```

0x20b表示这是 64 位 PE 文件（PE32+），`0x10b` 则是 32 位（PE32）。

⑥ Section Headers

在 Optional Header 之后（偏移 0x218），每个节区 40 字节：

```
[0] .text      位置=0x00000400  大小=0x0060e600 (6,350,336 字节)[1] .CLR_UEF   位置=0x0060ea00  大小=0x00000200 (512 字节)[2] .rdata     位置=0x0060ec00  大小=0x0017ec00 (1,567,744 字节)[3] .data      位置=0x0078d800  大小=0x00009800 (38,912 字节)[4] .pdata     位置=0x00797000  大小=0x00036200 (221,696 字节)[5] .didat     位置=0x007cd200  大小=0x00000200 (512 字节)[6] Section    位置=0x007cd400  大小=0x00000200 (512 字节)[7] _RDATA     位置=0x007cd600  大小=0x00013400 (78,848 字节)[8] .rsrc      位置=0x007e0a00  大小=0x00149e00 (1,351,168 字节)[9] .reloc     位置=0x0092a800  大小=0x00008000 (32,768 字节)
```

关键计算：PE 头占多少空间？

最后一个节区 .reloc 的结束位置：

```
.reloc 结束 = 0x0092a800 + 0x00008000 = 0x00932800 = 9,644,032 字节 (约 9.2 MB)
```

文件总大小 116 MB，PE 头只占 9.2 MB，剩余 106.4 MB 都是 Bundle 内嵌的文件。

找签名，定位 Bundle Header

.NET 单文件 Bundle 在文件末尾附近放了一个固定签名（magic bytes），用来标识 "我是一个 .NET 单文件 Bundle"。

这个签名是 16 个固定字节：

8b 12 02 b9 6a 61 20 38 72 7b 93 02 14 d7 a0 32

这个签名在 .NET Core 源码中定义于 Microsoft.NET.HostModel.Bundle/Bundler.cs：

```
// .NET Core 源码中的签名定义private static readonly byte[] BundleSignature = new byte[]{    0x8b, 0x12, 0x02, 0xb9, 0x6a, 0x61, 0x20, 0x38,    0x72, 0x7b, 0x93, 0x02, 0x14, 0xd7, 0xa0, 0x32};
```

.NET Core 单文件 bundle 的末尾结构为：

... [Bundle Header] ... [Header偏移量(8字节)] [签名(16字节)]

最后 16 字节是签名，签名前 8 字节是 Bundle Header 的偏移量。

```
with open("xx.WebApi.exe", "rb") as f:    data = f.read()
bundle_magic = b'\x8b\x12\x02\xb9\x6a\x61\x20\x38'magic_pos = data.rfind(bundle_magic)
print(f"搜索的 8 字节: {bundle_magic.hex()}")print(f"找到位置: {magic_pos} (0x{magic_pos:x})")
```

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsSMRkE56Zt4ZnBWcPCTGnrupzE1UhxEwqtZNxjFZAFvpBmWMvFiaicYh7Xpdu76uwwHeyN3RaI9gYSdZrwLVBwSWlyYnLniaxUjU/640?wx_fmt=png)

验证偏移

```
import struct
with open("xx.WebApi.exe", "rb") as f:    data = f.read()
bundle_magic = b'\x8b\x12\x02\xb9\x6a\x61\x20\x38'magic_pos = data.rfind(bundle_magic)
full_sig = data[magic_pos : magic_pos + 16]expected = bytes([0x8b, 0x12, 0x02, 0xb9, 0x6a, 0x61, 0x20, 0x38,                  0x72, 0x7b, 0x93, 0x02, 0x14, 0xd7, 0xa0, 0x32])
print(f"实际读取: {full_sig.hex()}")print(f"期望签名: {expected.hex()}")print(f"匹配: {full_sig == expected}")
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduaiaicbxAiagLngCGhF8hCfJUhKkPdkeLKfITn6ps9jFOTjY5hiaJrtQs70EDic78ASibYEQKdibCw3PGXBia53pl43WqnCM5rF3y03BY/640?wx_fmt=png)

签名找到了，接下来找Header偏移量

... [Bundle Header] ... [偏移量(8字节)] [签名(16字节)]
                          ↑
                    magic\_pos - 8

```
import struct
with open("xx.WebApi.exe", "rb") as f:    data = f.read()
bundle_magic = b'\x8b\x12\x02\xb9\x6a\x61\x20\x38'magic_pos = data.rfind(bundle_magic)
# 读取签名前 8 字节raw_bytes = data[magic_pos - 8 : magic_pos]
# 解析为 int64（小端序）header_offset = struct.unpack('<q', raw_bytes)[0]print(raw_bytes)print(header_offset)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRds6BiazvLytstq8FnQZhtf4miaF48VRtOicodibBOn9I7xLrbs2sLKEwSZMt5osRqefo6WfcpcChREPR81I8kjOAzUFIbAuJqm4AwE/640?wx_fmt=png)

小端序 int64 计算：

```
字节: 38 54 39 07 00 00 00 00位置: [0] [1] [2] [3] [4] [5] [6] [7]
值 = 0x38 × 256⁰ + 0x54 × 256¹ + 0x39 × 256² + 0x07 × 256³   = 56 × 1 + 84 × 256 + 57 × 65536 + 7 × 16777216   = 56 + 21504 + 3735552 + 117440512   = 121,197,624
十六进制: 0x7395438
```

更简单的一招是 xxd 直接从指定偏移读取：

xxd-s 0x7395438 -l 48 xx.WebApi.exe

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdsObpNaulo6UC8uFycfMEKCCX72KB0TYzATSB3iauTojmahWxoicBfibv0S0Atq0oSF4c7Nw2kW2qGexskKhdEc2RanZZ02CvJZjE/640?wx_fmt=png)

121197624就是Bundle Header 在文件的第 121,197,624 个字节处。

解析 Bundle Header

Bundle Header 描述了这个 Bundle 的基本信息：版本号、文件数量、Bundle ID。

还是用grep过滤16进制数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduOTk5njOGia6a4yWGetH2x9uxerkZl2IpdgUzbC16qOA23QJibYEXYyz1R7K9sJq3icEZjcbaGIKPP7LnTZQujxUtiarDRuUsTd6g/640?wx_fmt=png)

字段 1：MajorVersio...