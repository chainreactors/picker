---
title: 【病毒分析】某银狐伪装Steam客户端启动器”Steam.exe“、”Telegram简体中文语言包“隐蔽投毒
url: https://mp.weixin.qq.com/s/HleWYqTko9ge-o-RFw6hxg
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:10:18.570283
---

# 【病毒分析】某银狐伪装Steam客户端启动器”Steam.exe“、”Telegram简体中文语言包“隐蔽投毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Pled5HYvsFFocrQ6Vz2AYb3wJiaZJYLjdn9G4npSEicCNCnRGFC10VRIcHOKTVYBfWXU8AHWm2Jr8fOO6pOntqV5MI4Cl6SR2cEa5SvSKKMSk/0?wx_fmt=jpeg)

# 【病毒分析】某银狐伪装Steam客户端启动器”Steam.exe“、”Telegram简体中文语言包“隐蔽投毒

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

我一哥们刚换的新电脑准备爽玩3A大作，然而在安装steam的时候不知道从哪里下载到一个看似人畜无害的steam，运行之后没反应，这才发现不对劲给我拿过来看一下。样本分析发现，是一份被极其隐蔽patch过的`9.69.92.62版本steam启动器`，其并未使用常见的方式在入口点或 TLS 回调处直接劫持控制流，而是将恶意代码插入到 steam 客户端自带的 protobuf 注册路径中。程序启动后，MSVC CRT会在 `WinMain` 前执行全局初始化函数表，通过 `clientmetrics.proto` 的 file-registration 初始化链触发恶意代码。之后动态解析API，下载bmp将文件写入内存，经自定义解密逻辑原地变换后，最终被作为 `gdi32!EnumObjects` 的回调函数执行，可以说手法非常的隐蔽。

vt和微步分析情况:

![2026-06-17-23-56-10-image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFGc1qEXLia3uH6UEreJ5AnFIicqEtxm4iaibPV2u80nYt5Ymibk6iak8ibKVjmRkDf7r8V2uAtT8HiafLlWvib89ibm1E6KvlHlib4w6SvNGc/640?wx_fmt=png&from=appmsg)

![2026-06-17-23-55-35-image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGQWMRhXVwSiak6Xq3kDSbyYLtbcAJetzIb07uSKiaYdic4ic1yqgPjBzYllleYpBmdKM3to9ibP0zhaTGYj9B5ZtFSBvUxe7E7ZG6I/640?wx_fmt=png&from=appmsg)

样本主要流程图如下：

![2026-06-18-22-31-48-image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEXiaTJWDT3O15dYTyklgx4GSiauzgpXIblib5MFqN093EjSoNLEIwo5H9ibxGE6bXB3vr5R7AwFv3YsuHlzTH56uTpPdVgUgdlSgw/640?wx_fmt=png&from=appmsg)一、样本分析

## 1.1 样本基本信息

| 项目 | 内容 |
| --- | --- |
| 文件名 | `Steam.exe` |
| 文件大小 | `4.46 MB` |
| 架构 | `32-bit PE` |
| ImageBase | `0x400000` |
| OEP | `0x58F9CD` |
| TLS Callback | `0x58F9E5` |
| SHA1 | `98fe8fca4e9d670acffa041de3cc8c5ed8a04d82` |
| MD5 | `D58F9D3409892188764DA6F311E915FD` |
| SHA256 | `E0F6227F02D8BF6263938088AF91D3F073DB4A43A529BA46665CB2E90F612799` |

![image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGcwpAiawje1mSgMo1PPIAZMzCMtBeVicmlZrn9ZE8ibkibjEicgMhrZNGLIq1lRev6zGBMj2jVhOOplVv15vjfiac3kAP8DtCnRNdxQ/640?wx_fmt=png&from=appmsg)

## 1.2 启动阶段

样本入口点 `0x58F9CD` 是标准 MSVC CRT 启动桩，功能为初始化安全 cookie 后进入 `__scrt_common_main_seh`：

```
char *__usercall start@<eax>(char *a1@<esi>){  __security_init_cookie();  return __scrt_common_main_seh(a1);}
```

在 `__scrt_common_main_seh` 中，程序会在调用 `WinMain` 前执行全局初始化函数表：

![2026-06-18-00-15-51-image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFEsW3NrSkj41ibv9U5MJJHNVYbtXkRicYnKodiag6cYLyibmZGkVIZic8mgMiaeG0icST0xyWZpO3YGibEkvquSQ4WNf6pIXibROPszfIk0/640?wx_fmt=png&from=appmsg)

`__initterm` 会从 `First` 到 `Last` 顺序遍历函数指针，遇到非空表项即执行。经枚举，`0x728568-0x7289CC` 范围内共有 280 个非空初始化表项，其中最早可达恶意插入点的是：

```
0x7285A0 -> 0x446B80
```

因此，恶意代码的首次触发发生在 `WinMain` 前的 CRT 全局初始化阶段。

## 1.3 protobuf 注册阶段

`clientmetrics.proto` 是 Steam 正常代码里的 protobuf 描述文件。程序启动时 protobuf 会把这些 .proto 描述注册到内部表里。

初始化表项 `0x7285A0` 指向函数 `0x446B80`。该函数是一个小型全局注册包装器，用于注册 `clientmetrics.proto`：

```
.text:00446B80                 push    offset unk_812A50 ; _initterm 表项 0x7285A0 指向本函数；传入 clientmetrics.proto  0x812A50。.text:00446B85                 mov     ecx, offset unk_826318.text:00446B8A                 call    sub_5C5D20.text:00446B8F                 retn
```

![2026-06-18-00-20-05-image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/Pled5HYvsFH51XTRWlwf5CKMZQ3GsJePAB89lYaicdrSfia6guZA7oO86QdEDib4HyIIozAhsicdiabAhbjcUyAP2UQOfprrzYl1CyaTthNUBDTc/640?wx_fmt=png&from=appmsg)`unk_812A50` 的首字节初值为 `0`，说明该 proto 文件尚未注册。`unk_812A50 + 0x0C` 指向字符串 `clientmetrics.proto`，可确认该对象为 protobuf file-registration 数据。

调用链如下：

```
0x446B80  -> 0x5C5D20 Protobuf_FileRegistration_StaticCtor  -> 0x5C6220 Protobuf_RegisterFileRecursive_ThenInjectedCall  -> 0x5C2180 Protobuf_RegisterFile_InjectedPayloadCall
```

在 `0x5C2180` 的函数入口附近，样本先执行恶意主体，再继续正常 file registration 逻辑：

![2026-06-18-00-54-46-image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFFF7JNgKLuQb2RnMkw9uHmtJCa4EyIrTQ5LiaxBVHLeCjstB4kQNuNlVXzcNMB78F3xPE6VC4TsaABNlhJSInZkanr36y9fciaws/640?wx_fmt=png&from=appmsg)该插入点位于 protobuf `message.cc` 的 file-registration 路径，代码中可见调试路径字符串：

```
G:\Valve\steam\thirdpartycode\nonredist\protobuf\protobuf-3.15.3\src\google\protobuf\message.cc
```

同一初始化表中还有 4 个后续表项也可到达该 file-registration 插入点：

| 初始化表项 | 初始化函数 | proto 对象 | proto 名称 |
| --- | --- | --- | --- |
| `0x007285B0` | `0x00446C00` | `0x00812B74` | `uifontfile_format.proto` |
| `0x00728610` | `0x00447690` | `0x00813010` | `steammessages_base.proto` |
| `0x00728628` | `0x00447860` | `0x00813568` | `enums_clientserver.proto` |
| `0x007286C4` | `0x00447DF0` | `0x00816C58` | `google/protobuf/descriptor.proto` |

这些表项进一步说明，恶意逻辑被挂接在多个 protobuf 全局注册入口上。由于 `_initterm` 顺序遍历，首次触发点仍是 `0x7285A0 -> 0x446B80`。

## 1.4 其他挂钩点

除 file-registration 插入点外，样本还在 protobuf type-registration 路径`0x5C227C`开头插入恶意代码：

![2026-06-18-00-56-17-image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFGOJUQ5KN5iaTCgxOTUT7rgKuZWj7ZAy8VvXsceZiaXzOg2oeWSia1s0KJlZCYAQR6NjFp4dHk78zsibZXKCQgrOXaa29f5fibUvFTY/640?wx_fmt=png&from=appmsg)

另有一个恶意 thunk 位于 `0x5C34C0`：

```
.text:005C34C0 MaliciousPayloadThunk proc near         ; CODE XREF: sub_5C6C20:loc_5C6E6C↓p.text:005C34C0                                         ; sub_5C7C80+8↓p ....text:005C34C0                 jmp     Malicious_DownloadDecryptExecutePayload ; 由启动前全局初始化链通过 0x7285A0 -> 0x446B80 -> 0x5C5D20 -> 0x5C6220 -> 0x5C2180 -> 0x5C21AE 到达。.text:005C34C0 MaliciousPayload
```

该 thunk 被多个代码位置调用，包括：

```
0x5C6E6C0x5C7C880x5CDCC10x5CDCD60x62E3D9
```

当前闭环分析中，最早执行恶意主体的路径来自 `0x5C21AE`，即 protobuf file-registration 链。

## 1.5 恶意代码分析

恶意代码的主体位于：`0x005C34D0`

![2026-06-18-01-02-54-image.png](https://mmbiz.qpic.cn/mmbiz_png/Pled5HYvsFEzPfn6zhZVcO9xgjGLmW5HEGBsSN6ceicBLe70vak7TXiaBFu4eueyR3FnRkT0xbPpz8Cr50C9wtFyZQKXbTKjwppqrZDxLDvN8/640?wx_fmt=png&from=appmsg)

函数开头在栈上构造多个模块名：

```
User32Gdi32wininetmsvcrtntdllShell32
```

随后通过 PEB 获取 kernel32 基址，并使用自定义 API 哈希逻辑解析函数地址的经典操作。

## 1.6 恶意代码下载逻辑

恶意代码会申请一段小缓冲区，调用 `GetModuleFileNameA` 获取当前模块路径，并检查路径中是否包含`“语言”`字符串：

```
.text:005C3707                 mov     [ebp+var_34], 0D3h ; D3 EF D1 D4 decode to "语言".text:005C370B                 mov     [ebp+var_33], 0EFh.text:005C370F.text:005C370F loc_5C370F:                             ; DATA XREF: sub_5C4A20+A0↓o.text:005C370F                 mov     [ebp+var_32], 0D1h.text:005C3713                 mov     [ebp+var_31], 0D4h
```

如果命中该字符串，样本会解码字符串 `stir` 为 `open`，再解码 Telegram URI：

```
.text:005C37CE                 mov     [ebp+var_B8], 77h ; 'w' ; Obfuscated URI; subtract 3 per byte => tg://setlanguage?lang=classic-zh-cnn..text:005C37D5                 mov     [ebp+var_B8+1], 6Ah ; 'j'.text:005C37DC                 mov     [ebp+var_B8+2], 3Dh ; '='.text:005C37E3                 mov     [ebp+var_B8+3], 32h ; '2'.text:005C37EA                 mov     [ebp+var_B8+4], 32h ; '2'.text:005C37F1                 mov     [ebp+var_B8+5], 76h ; 'v'.text:005C37F8                 mov     [ebp+var_B8+6], 68h ; 'h'.text:005C37FF                 mov     [ebp+var_B8+7], 77h ; 'w'.text:005C3806                 mov     [ebp+var_B8+8], 6Fh ; 'o'.text:005C380D                 mov     [ebp+var_B8+9], 64h ; 'd'.text:005C3814                 mov     [ebp+var_B8+0Ah], 71h ; 'q'.text:005C381B                 mov     [ebp+var_B8+0Bh], 6Ah ; 'j'.text:005C3822                 mov     [ebp+var_B8+0Ch], 78h ; 'x'.text:005C3829                 mov     [ebp+var_B8+0Dh], 64h ; 'd'.text:005C3830                 mov     [ebp+var_B8+0Eh], 6Ah ; 'j'.text:005C3837                 mov     [ebp+var_B8+0Fh], 68h ; 'h'.text:005C383E                 mov     [ebp+var_B8+10h], 42h ; 'B'.text:005C3845                 mov     [ebp+var_B8+11h], 6Fh ; 'o'.text:005C384C                 mov     [ebp+var_B8+12h], 64h ; 'd'.text:005C3853                 mov     [ebp+var_B8+13h], 71h ; 'q'.text:005C385A                 mov     [ebp+var_B8+14h], 6Ah ; 'j'.text:005C3861                 mov     [ebp+var_B8+15h], 40h ; '@'.text:005C3868                 mov     [ebp+var_B8+16h], 66h ; 'f'.text:005C386F                 mov     [ebp+var_B8+17h], 6Fh ; 'o'.text:005C3876                 mov     [ebp+var_B8+18h], 64h ; 'd'.text:005C387D                 mov     [ebp+var_B8+19h], 76h ; 'v'.text:005C3884         ...