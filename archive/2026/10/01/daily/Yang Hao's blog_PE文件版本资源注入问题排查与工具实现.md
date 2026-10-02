---
title: PE文件版本资源注入问题排查与工具实现
url: https://yanghaoi.github.io/2026/10/01/pe-wen-jian-ban-ben-zi-yuan-zhu-ru-wen-ti-pai-cha-yu-gong-ju-shi-xian/
source: Yang Hao's blog
date: 2026-10-01
fetch_date: 2026-10-02T07:49:08.903141
---

# PE文件版本资源注入问题排查与工具实现

[![LOGO](/medias/logo.png)
Yang Hao's blog](/)

* [首页](/)
* 文章
  + [标签](/tags)
  + [分类](/categories)
  + [归档](/archives)
* [关于](/about)
* [留言板](/contact)

![](/medias/logo.png)

Yang Hao's blog

Yang Hao's blog

* [首页](/)
* 文章
  + [标签](/tags%20)
  + [分类](/categories%20)
  + [归档](/archives%20)
* [关于](/about)
* [留言板](/contact)

# PE文件版本资源注入问题排查与工具实现

[Windows](/tags/Windows/)
[PE文件](/tags/PE%E6%96%87%E4%BB%B6/)
[C语言](/tags/C%E8%AF%AD%E8%A8%80/)

[杂记](/categories/%E6%9D%82%E8%AE%B0/)

发布日期:
2026-10-01

更新日期:
2026-10-01

文章字数:
9.7k

阅读时长:
38 分

阅读次数:

---

最近在做一个构建辅助工具：给 PE 文件批量写入版本信息（`RT_VERSION`），必要时追加图标与随机数据块，并修改 PE 头的时间戳与校验和。按 Windows 文档的描述，这应当是调用 `BeginUpdateResource` / `UpdateResource` / `EndUpdateResource` 三件套的问题。实测下来，其间遇到四个行为问题，共同点是——**API 全部返回成功，而结果都是错的**。

这个工具经历了四轮草稿迭代才达到可用状态：第一版只写数字版本号的骨架，第二版补齐了字符串结构但语义有误，第三版以固定长度数组实现、字段长度写死导致中文与长值溢出，第四版改用柔性数组加手工 4 字节对齐后达到可用，最后整理为正式工具 `pe_resource_injector`（源码已开源：[GitHub 仓库](https://github.com/yanghaoi/pe_resource_injector)）——产出两个程序：`peres.exe`（资源注入器）与 `peview.exe`（PE 查看器，由 6 个 Python 测试脚本集成为 C 原生程序）。下文先交代这四版各自的问题，再逐个展开实测中遇到的四个 API 行为问题，最后附上 peview 的双路资源视图设计与多模块工程结构。

![PE 资源注入工具主界面](/2026/10/01/pe-wen-jian-ban-ben-zi-yuan-zhu-ru-wen-ti-pai-cha-yu-gong-ju-shi-xian/PE-IMG-01.svg)

## 1 结论

如果也在做类似的工作，以下四条结论可以直接取用：

1. `UpdateResource` 不能给**完全没有资源目录**的 PE 添加资源，会返回 `ERROR 1359`。
2. **不要自建资源目录**。字节布局完全合规也没有意义，Windows 可能只识别其中一部分。补一个空目录头，让 `UpdateResource` 自行构建。
3. 同一个 `UpdateResource` 会话里，**先写「字符串类型名」资源、再写「字符串名」资源会失败**（`ERROR_NOT_SUPPORTED`）。且两种提交顺序各自只对一半样本有效，必须写完后回读校验，不符合则换顺序重试。
4. 资源较多时，`EndUpdateResource` **可能不提交删除请求**——输出文件 md5 与输入完全一致。

概括为一句话：**正确性必须以 `FindResource` 回读校验为准，API 返回值不能作为依据。**

## 2 背景知识：版本信息的实际形态

### 2.1 版本信息存在哪

PE 文件的版本信息不是一个字段，而是 `.rsrc` 资源节里的一棵 **二进制资源树**：

```
资源类型 RT_VERSION (16)
  └─ 资源名 VS_VERSION_INFO (1)
       └─ 语言 ID (如 0x0409)
            └─ 二进制块：VS_VERSIONINFO
```

因此「改版本信息」本质上是「改资源」，必须使用资源更新 API，**不能**按字节直接修补 `.rsrc`。

### 2.2 VS\_VERSIONINFO 的内存布局

MS 官方文档对这一点有明确说明：

> *“This structure is not a true C-language structure because it contains variable-length members.”*
> —— [VS\_VERSIONINFO structure (Microsoft Learn)](https://learn.microsoft.com/en-us/windows/win32/menurc/vs-versioninfo)

也就是说，`typedef struct` 加 `sizeof` 无法得到正确长度：它是变长的、带 padding 的。实际布局如下（单位：字节）：

| Block | 偏移 | 内容 |
| --- | --- | --- |
| **VS\_VERSIONINFO** | 0–1 | `wLength`（整个块的总长，**含尾部 padding**） |
|  | 2–3 | `wValueLength` = 52（`sizeof(VS_FIXEDFILEINFO)`） |
|  | 4–5 | `wType` = **0**（Value 是二进制） |
|  | 6–37 | `szKey` = `L"VS_VERSION_INFO\0"`（16 WCHAR = 32 字节） |
|  | 38–39 | `Padding1`（6+32=38，补 2 字节把后面顶到 4 对齐） |
|  | 40–91 | `VS_FIXEDFILEINFO`（52 字节） |
|  | 92… | `Children` = StringFileInfo + VarFileInfo（92 已经 4 对齐，`Padding2` 可省） |
| **StringFileInfo** | 0–5 | 6 字节头（`wLength` / 0 / **1**） |
|  | 6–35 | `L"StringFileInfo\0"`（15 WCHAR = 30 字节）→ 36 已 4 对齐，无 padding |
| **StringTable** | 0–5 | 6 字节头 |
|  | 6–23 | `L"040904B0\0"`（9 WCHAR = 18 字节）→ 24 已 4 对齐 |
| **String** | 0–5 | 6 字节头（`wLength` / `wValueLength`(字节数) / **1**) |
|  | 6… | Key（含 NUL） |
|  | … | **padding**（0 或 2 字节，使 Value 落在 4 的倍数的偏移上） |
|  | … | Value（含 NUL） |
|  | … | **尾部 padding**（让下一个兄弟 4 对齐，计入本块 `wLength`） |
| **VarFileInfo** | 0–5 | 6 字节头 |
|  | 6–29 | `L"VarFileInfo\0"`（12 WCHAR = 24 字节）= 30 |
|  | 30–31 | **padding 2 字节**（此处必然存在） |
| **Var “Translation”** | 0–5 | 6 字节头（`wLength` / `4` / **0**） |
|  | 6–29 | `L"Translation\0"` = 30 |
|  | 30–31 | padding 2 字节 |
|  | 32–35 | **一个 DWORD** = lang(WORD) + codepage(WORD)，不是字符串 |

String 块 padding 的计算规律如下（动态版代码里的 `align2` 就是在做这件事）：

设 key 长度 K、value 长度 V，`A = align2(V+1)`（一定是偶数），则

```
oldsize = 6 + 2*(K+1) + 2*A     →  2*A ≡ 0 (mod 4)
oldsize ≡ 2K + 8 ≡ 2K (mod 4)
padding = 0  (K 为偶数)
padding = 2  (K 为奇数)
```

**结论：padding 只取决于 key 长度的奇偶，与 value 长度无关**，因为 `A` 已被 `align2` 强制为偶数。这一处写错后，资源管理器将不显示任何版本信息。

### 2.3 三件套 API

```
HANDLE h = BeginUpdateResource(path, /*bDeleteExistingResources=*/FALSE);
UpdateResource(h, RT_VERSION, MAKEINTRESOURCE(VS_VERSION_INFO), wLang, pData, cbData);
EndUpdateResource(h, FALSE);   /* TRUE = 丢弃全部改动（回滚） */
```

要点（来自 [UpdateResource](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-updateresourcew) / [BeginUpdateResource](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-beginupdateresourcew)）：

* `UpdateResource` 只是把改动排入内部队列，**只有 `EndUpdateResource` 才真正落盘**；
* `bDeleteExistingResources = TRUE` 会**清空所有资源**（图标、对话框、manifest 全部丢失），通常不应使用；
* `lpData=NULL && cb=0` 表示删除该资源（Win7 之前若 `cb != 0` 会抛异常）；
* 目标文件必须可写、且**不能正在运行**；
* 含 RC Config 数据的 LN 文件 / `.mui` 文件有额外限制（只能修改 Version / RC Config / Manifest 三类）。

## 3 初始实现的四个缺陷

### 3.1 第一版：只有版本号骨架

```
VS_VERSIONINFO versionResource;                 /* 未初始化！ */
versionResource.TotalSize = sizeof(VS_VERSIONINFO);
versionResource.DataSize  = sizeof(VS_FIXEDFILEINFO);
versionResource.Type      = 1;                  /* 应为 0 */
wcscpy(versionResource.Name, L"VS_VERSION_INFO");
versionResource.FixedFileInfo = versionInfo;    /* Padding1 / Padding2 / Children 全未清零 */
```

问题：

1. `Padding1` 是未初始化的值——它正好位于 `szKey` 与 `VS_FIXEDFILEINFO` 之间，会导致解析错位；
2. `wType=1` 表示「文本数据」，但此处 Value 是二进制的 `VS_FIXEDFILEINFO`，应为 `0`；
3. `Children` 完全未填——写入后「详细信息」页里公司名/产品名均为空，只有数字版本号生效；
4. `wLength = sizeof(VS_VERSIONINFO)` 把声明中 `Padding2 + WORD Children[2]`（8 字节）也计入，且这些空间是垃圾数据。

### 3.2 第二版：结构补齐但语义有误

```
#pragma pack(push,2)      /* 用 2 字节 packing 消除隐式对齐 */
...
wcscpy_s(...)             /* MSVC 安全 CRT，MinGW 默认不可编译 */
```

问题：

1. \*\*`Translation` 被写成了字符串 `L"040904B0"`\*\*，而规范要求是 `DWORD`（`lang<<16 | codepage`）。
   后果：`VerQueryValue(L"\\VarFileInfo\\Translation")` 取到的是乱码 → 资源管理器无法把语言 ID 映射到 StringTable → 版本信息整体不显示。
2. `Var.wValueLength = wcslen(Value)*sizeof(WCHAR)`——混淆了「字节数」与「字符数」。
3. `wcscpy_s` 是 MSVC 的 secure CRT，MinGW 下要么编译不过，要么需要 `_CRT_SECURE_NO_WARNINGS` / `MINGW_HAS_SECURE_API`。
4. `#pragma pack(push,2)` 本身是个偏方：它能消除隐式 padding，但与其他非 pack 结构体混用时偏移会算错，且 `sizeof` 的结果依赖编译器实现，不推荐。

### 3.3 第三版：长度写死

```
typedef struct {
    WORD  wLength; WORD wValueLength; WORD wType;
    WCHAR szKey[12];      /* key 最多 11 字符 */
    WORD  Padding;
    WCHAR Value[12];      /* value 最多 11 字符 */
} String;

String companyName = { sizeof(String), sizeof(companyName.Value), 1,
                       L"CompanyName", 0, L"Protect.EXE" };
```

问题：

1. \*\*`OriginalFilename`（16 字符）、`LegalCopyright`（14 字符）放不进 `szKey[12]`\*\*——直接截断甚至越界；
2. \*\*中文与长值放不进 `Value[12]`\*\*——`"Copyright (C) 2024 XXXXXXX"` 明显超长；
3. `wValueLength = sizeof(companyName.Value)` 恒等于 24 字节，与实际字符串长度脱钩。填 `"Protect.EXE"`（11 字符 = 24 字节含 NUL）时恰好正确，换成 `"公司名称"`（4 字符 = 10 字节）即错，Windows 会多读 7 个 WCHAR 的垃圾；
4. `VS_Children Children[1]` 只声明了一个元素，却用 `{ stringFileInfo, varFileInfo }` 两个元素初始化 → 编译期即”excess elements”，且 `sizeof(VS_VERSIONINFO)` 不含 `VarFileInfo`，写入的 `wLength` 偏小；
5. `versionInfo = { ... };` 这种「给已声明变量赋花括号列表」的写法在标准 C 里不合法（MSVC 也会报），应使用复合字面量 `(VS_VERSIONINFO){...}` 或直接初始化。

### 3.4 第四版：可用版本

核心思路：

1. **柔性数组**（`WCHAR KeyPaddingValue[]` / `WCHAR Children[]`）描述变长结构；
2. 每个块先算 `sizeMems = align4(header + key + align2(value))`，用 `calloc` 清零（padding 天然为 0）；
3. 逐层 `memcpy` 拼接，用 `wLength / sizeof(WCHAR)` 手工计算偏移；
4. 最后 `UpdateResource(..., versionInfo, versionInfo->wLength)` 提交。

```
int CalculateSizeMems(const WCHAR* k, const WCHAR* v) {
    DWORD bytes = ((lstrlenW(k)+1) + align2((lstrlenW(v)+1))) * sizeof(WCHAR);
    return align4(sizeof(String) + bytes);
}
```

对 padding 的处理是这一版的关键：

```
int padBytes = sizeMems - oldsizeMems;                  /* 0 或 2 */
memcpy(pString->KeyPaddingValue, wstrKey, (lstrlenW(k)+1)*2);
memcpy(pString->KeyPaddingValue + (lstrlenW(k)+1) + padBytes/2,
       wstrValue, pString->wValueLength);
```

这一版仍然遗留四个工程问题（后在正式工具中逐条解决）：

* 所有 `calloc` 出来的块\*\*均未 `free`\*\*（一次性 CLI 无影响，做成库或批量调用即为泄漏）；
* `stringTable->Children` 用 `WCHAR[]` 手工偏移拼接，8 段 `memcpy` 的偏移量是手算的，增加一个字段就要修改一串数字，容易出错；
* 语言键写成小写 `L"040904b0"`（惯例是大写 `040904B0`），个别解析器对大小写敏感；
* 未删除已存在的 `RT_VERSION`，若原文件是其他语言的版本资源，会出现两份共存。

## 4 无资源目录的 PE

目标**完全没有资源目录**时，`UpdateResource` 会直接失败。这个问题在实现初期即暴露——用一个不含 `.rsrc` ...