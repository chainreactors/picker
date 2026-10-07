---
title: 惊心！歹毒！遭遇【VS编译时触发后门】保卫战
url: https://mp.weixin.qq.com/s/8bIRkXGUkwFezeoWb6UZmQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:31.789349
---

# 惊心！歹毒！遭遇【VS编译时触发后门】保卫战

# 惊心！歹毒！遭遇【VS编译时触发后门】保卫战

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

今日，在研究一个带“**COM BypassUAC + 反射式 DLL 注入功能”的源代码时，遭遇了“编译VS源代码时触发后门”的惊心动魄时刻，且听我分析道来。**

**源代码下载下来后，**我习惯性地**用vs2022打开了reflective\_dll.sln直接编译，发现了报错项2个。现在有了AI，直接用AI来检查下代码报错，这下发现大问题了，在**reflective\_dll.vcxproj里包含了一段后门shellcode，它会在你编译时直接触发这个后门，用心之歹毒。****

## 一、结论：这是**人为植入的第三方后门**，与项目功能无关，专门等编译时触发

我可以明确排除「项目自带功能」这一可能，依据如下：

### 1. 与项目业务逻辑完全无关

项目本身是 **COM BypassUAC + 反射式 DLL 注入**（C 代码，`src/ReflectiveDll.c` / `ReflectiveLoader.c`）。而这段 shellcode 是一个 **x64 联网下载器**：下载 `SearchFilter.7z` 到 `%LOCALAPPDATA%\Microsoft\Feeds`，释放伪装成 `C:\ProgramData\sevenZip\7z.exe` 解压，再执行 `SearchFilter.exe`。两者毫无代码或功能关联——项目里没有任何一行代码引用、加载或需要它。

### 2. 实现手法是典型的「后门/投毒」特征，而非工程配置

* 藏在 `.vcxproj` 的 `InitialTargets` + `CodeTaskFactory` 里——这是**供应链投毒的经典手法**（利用 MSBuild 在构建进程内执行任意代码），而非任何正常工程会用到的配置；
* 载荷经 **Base64 + 三轮 XOR + GZip** 层层混淆，并调用 `VirtualAlloc`/`VirtualProtect`/`CreateThread` 在内存中直接执行，**刻意规避静态查杀**；
* shellcode 自身无导入表，靠 **PEB 遍历 + 哈希** 动态解析 API，且用伪装 Chrome UA、伪装成 7-Zip / 系统 Feeds 目录——这些都是**恶意软件的规避与伪装技术**，正常构建脚本绝无必要。

### 3. 工程内其他文件全部干净，唯独 `.vcxproj` 被动过

* `.sln`

  、`.vcxproj.filters`、`.vcxproj.user`、`.gitignore`、全部 `.c/.h`、`README.md`、`LICENSE` —— **均无任何异常**；
* 后门**只**存在于 `reflective_dll.vcxproj` 这一处。若是项目自带功能，必然会在 README 中说明、并配套源码；实际却完全隐形。
* `.vcxproj`

  其余内容（各平台配置、宏定义）是**正常且专业的**，唯独首尾被插入了两段与工程无关的代码——属于「在干净工程上追加后门」的篡改特征。

### 4. 「等人来编译」的意图非常明确

`InitialTargets` 的语义就是**任何构建动作前自动执行**。它不依赖用户做任何额外操作——只要有人：

* 用 Visual Studio 打开并点「生成」，或
* 命令行跑 `msbuild` / `devenv /build`，

后门就会在编译进程内静默运行。这正是「布好陷阱、等人上钩」的定向投毒形态。

### 5. 本机已经触发过一次（重要）

`x64/Debug/` 下有**今天 17:46 的构建产物**（`.obj`、`.tlog`、`unsuccessfulbuild` 等），说明该工程**已被本机 MSBuild 执行过**。`unsuccessfulbuild` 表明编译在 C2440 报错处失败了——**但 `InitialTargets` 在编译之前就已执行**，所以后门的 shellcode 当时已经跑过一次。

---

## 需要你注意的风险

1. **本机可能已被植入**

   ：检查这两个路径是否存在落地物

* `C:\ProgramData\sevenZip\7z.exe`
* `%LOCALAPPDATA%\Microsoft\Feeds\SearchFilter.7z`

  / `SearchFilter.exe`

2. **可能已外联**

   ：shellcode 运行即会联网下载，建议查该时段的网络连接/EDR 记录。
3. **C2 地址未明文存储**

   ：shellcode 里没有硬编码 URL（唯一的 `131.0.0.0` 是 UA 字符串的一部分），下载地址应是运行时拼接的，需动态分析或抓包才能拿到。

****![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7OjVslk72cIoKc5uuz7OnLmVjOglLkVfdE5rnRzYjaT6KFGvia12YxMdCsbFdL0WhxAibgDmBNxmC5c0FJmf2TjC39zUx6ia7hXo/640?wx_fmt=png&from=appmsg)****

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7EAh1lNB2az24zuXD5ib1kNYTuCuOicLk2IxrSUKM62DXUWo7UkNO945qI7TmpYPsOd8kLicwva2jU6TK8nSTCH4942SBwYMnb2k/640?wx_fmt=png&from=appmsg)

****二、****reflective\_dll.vcxproj中的shellcode触发原理********

********后门就在 **`reflective_dll.vcxproj`** 里，分两处，配合构成一条完整的「构建期自动执行」链。********

## 位置一：文件根节点（第 2 行）

```
<Project DefaultTargets="Build" ToolsVersion="4.0"         xmlns="..." InitialTargets="cYhrfP5mH9">
```

`InitialTargets` 是 MSBuild 的合法属性，作用是**在本次构建的任何目标之前，先自动执行指定的 Target**。这里被塞进了 `cYhrfP5mH9` —— 也就是说，只要用 VS 打开并构建这个工程（甚至 `msbuild reflective_dll.vcxproj`），`cYhrfP5mH9` 都会先跑。

## 位置二：文件末尾（第 262–270 行，紧跟在合法内容 `ImportGroup` 之后）

```
<UsingTask TaskName="cG5nbiSNoL" TaskFactory="CodeTaskFactory"           AssemblyFile="$(MSBuildToolsPath)\Microsoft.Build.Tasks.Core.dll">  <Task>    <Code Type="Method" Language="cs"><![CDATA[      ... 恶意 C# ...    ]]></Code>  </Task></UsingTask><Target Name="cYhrfP5mH9">  <cG5nbiSNoL /></Target>
```

`CodeTaskFactory` 允许在工程文件里内联 C# 代码，MSBuild 会在**构建进程内直接编译并执行**它 —— 这是它的正常功能，被滥用来藏后门。这段内联 C# 做的正是：

1. **解码载荷**

   ：`SlqjPF` = 一大段 Base64（主数据），另有 3 个 32 字节 Base64 密钥 `DOil5`/`xe3zp`/`roZ8G`；
2. **三轮 XOR 解密**

   ：三个 `for` 循环各按 32 字节循环密钥 XOR 一遍；
3. **GZip 解压**

   ：`GZipStream(... Decompress)` → 得到最终 shellcode；
4. **内存执行**

   （这是关键，全部通过 P/Invoke 调 Windows API）：

* `HQGzyT0`

  = `VirtualAlloc`，分配 `0x3000`(MEM\_COMMIT|MEM\_RESERVE) + `0x04`(PAGE\_READWRITE)；
* `Marshal.Copy`

  把 shellcode 写进去；
* `PBe2MlH`

  = `VirtualProtect`，改成 `0x20`(PAGE\_EXECUTE\_READ)；
* `D2k9VLa`

  = `CreateThread`（`vfcyzgU` = `GetCurrentProcess`）创建线程执行；
* `WaitForSingleObject(..., 0xFFFFFFFF)`

  等它跑完。

解码后是一段 **12998 字节的 x64 shellcode**（非 PE，直接可执行），内含 `urlmon.dll`/`wininet.dll`、伪装 UA `Chrome/131.0.0.0`，以及落地路径 `C:\ProgramData\sevenZip\7z.exe`、`%LOCALAPPDATA%\Microsoft\Feeds\SearchFilter.exe` —— 典型的「联网下载 + 伪装目录落地 + 执行」下载器。

---

**一句话**：后门 = 第 2 行的 `InitialTargets="cYhrfP5mH9"`（触发点）+ 第 262–270 行的 `<UsingTask cG5nbiSNoL>` 与 `<Target cYhrfP5mH9>`（执行体）。前者让后者在每次构建时自动运行，后者在构建进程内解密并执行远程加载器 shellcode。

********三、shellcode功能********

以下是从 `reflective_dll.vcxproj` 中提取并还原的完整结果。

## 解密结果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN4wGv4zQRQsTGgbDEw1umPibfj8aiaBtJgv48FHn1hts2Hxib82smCuXbVftP9Kt1No9SpzUoibdpTpH4rATFSP4HB3ibQGpPwPogCY/640?wx_fmt=png&from=appmsg)

三个密钥（hex）：

* 5cc2ab1518392c8008104f857cfb673973c111b1cde6af6a35a66d7eb1e402db
* 66c766278d1ed308ed85b4ec1cae96f2761e921c6c292f7b40ad3dcef01ee0de
* 73a0d35c24ceb1c833c49fe4dfa83f621fa9c4c74f2ade214ccae9cdddd77a68

这段 shellcode 干什么（已反汇编确认）

入口（偏移 0）：

```
0x00: JMP +9525        ; 跳到 0x253a 的主逻辑0x05: (strlen / strcmp / strcmpi 等辅助函数)0x34: PEB 遍历          ; 标准 API 解析器
```

0x34 起 是经典的 PEB → InMemoryOrderModuleList 遍历，通过模块名比较（OR AX,0x20 做大小写归一）定位 kernelbase.dll（偏移 0xe3）和 kernel32.dll（偏移 0xeb），再按 哈希 解析 API（偏移 0xf0 起 ror+累加 的 0xd3 轮转哈希，与主程序同款手法）。

字符串区（偏移 0x2fa9–0x32xx）暴露全部意图：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN4c4enQWfLdcZj2PGmvibjymT33lHFVFqq1aPNy1Urh8v3XzticXD6LQ5MEC83T6Bzdcok3hTbBib6qb5jamLEJBaH6ATez8bCFf8/640?wx_fmt=png&from=appmsg)

行为总结：这是一段 x64 位置无关下载器（downloader）——

1. 无导入表，通过 PEB 遍历 + 哈希动态解析 kernelbase.dll/kernel32.dll/urlmon.dll/wininet.dll/rpcrt4.dll 的 API；

2. 用伪装 Chrome UA 联网下载载荷到 %LOCALAPPDATA%\Microsoft\Feeds\SearchFilter.7z；

3. 释放/伪装成 C:\ProgramData\sevenZip\7z.exe 进行解压；

4. 最终执行 SearchFilter.exe。

这与构建期后门「在 MSBuild 进程内 VirtualAlloc+VirtualProtect+CreateThread 直接内存执行」的设计完全吻合——任何一次编译该工程，本机就会被注入并运行这个下载器。

********四、关于木马文件的分析********

********7z.exe和SearchFilter.exe，这两个文件放在各种云沙箱、杀毒软件查杀均不报毒，越来越有趣了。我坚信它们是有问题的，至于真相是什么，放在下一篇中了。********

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过