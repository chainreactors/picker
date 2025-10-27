---
title: V8 字节码反编译 还原bytenode保护的js代码
url: https://rce.moe/2025/01/07/v8-bytecode-decompiler/
source: 白帽酱の博客
date: 2025-01-08
fetch_date: 2025-10-06T20:10:29.214808
---

# V8 字节码反编译 还原bytenode保护的js代码

Toc

1. [前言](#%E5%89%8D%E8%A8%80)
2. [一个奇怪的electron应用](#%E4%B8%80%E4%B8%AA%E5%A5%87%E6%80%AA%E7%9A%84electron%E5%BA%94%E7%94%A8)
   1. [V8字节码](#V8%E5%AD%97%E8%8A%82%E7%A0%81)
      1. [V8字节码长什么样?](#V8%E5%AD%97%E8%8A%82%E7%A0%81%E9%95%BF%E4%BB%80%E4%B9%88%E6%A0%B7)
         1. [魔数](#%E9%AD%94%E6%95%B0)
         2. [版本哈希](#%E7%89%88%E6%9C%AC%E5%93%88%E5%B8%8C)
   2. [V8字节码”反编译”](#V8%E5%AD%97%E8%8A%82%E7%A0%81%E2%80%9D%E5%8F%8D%E7%BC%96%E8%AF%91%E2%80%9D)
      1. [V8字节码”反汇编”](#V8%E5%AD%97%E8%8A%82%E7%A0%81%E2%80%9D%E5%8F%8D%E6%B1%87%E7%BC%96%E2%80%9D)
         1. [拉取V8代码](#%E6%8B%89%E5%8F%96V8%E4%BB%A3%E7%A0%81)
         2. [魔改V8引擎](#%E9%AD%94%E6%94%B9V8%E5%BC%95%E6%93%8E)
         3. [编译V8引擎](#%E7%BC%96%E8%AF%91V8%E5%BC%95%E6%93%8E)
         4. [编译反汇编工具](#%E7%BC%96%E8%AF%91%E5%8F%8D%E6%B1%87%E7%BC%96%E5%B7%A5%E5%85%B7)
   3. [V8字节码反编译](#V8%E5%AD%97%E8%8A%82%E7%A0%81%E5%8F%8D%E7%BC%96%E8%AF%91)

Toc

**0** results found
![](/images/logo.jpeg)

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

白帽酱

白帽酱

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

V8 字节码反编译 还原bytenode保护的js代码

2025/01/07

[笔记](/categories/%E7%AC%94%E8%AE%B0)
[二进制](/categories/%E4%BA%8C%E8%BF%9B%E5%88%B6)

[v8](/tags/v8)
[反编译](/tags/%E5%8F%8D%E7%BC%96%E8%AF%91)
[逆向](/tags/%E9%80%86%E5%90%91)
[V8字节码](/tags/V8%E5%AD%97%E8%8A%82%E7%A0%81)
[bytecode](/tags/bytecode)

# 前言

某年某日的一天，我看到某IM应用发布了一个全新的桌面客户端开始了公测

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240283342-e54b138c-52fe-4f87-a233-9c6d006bf89d.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240283342-e54b138c-52fe-4f87-a233-9c6d006bf89d.png)

我马上就下载来试用了一番，发现它使用了`electron`重构了PC客户端。用`electron`重写？逆起来应该很容易吧

注意：新版本使用的V8 12.\*版本并没有反编译成功

# 一个奇怪的electron应用

分析`electron`引用第一步就是寻找资源文件。

所以，我就想在安装目录下寻找`app.asar`，来看看它的js代码是怎么写的。~~能不能整出点花活~~

进行一番寻找之后，我并没有在安装目录下找到任何的ASAR文件。

但是通过文件大小来看，安装目录下几个奇怪的`.node`文件看起来比较可疑。

`wrapper.node` `major.node` 两个数十M的文件是PE文件

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240289847-502493ba-ff09-4044-9146-69fd32ebc039.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240289847-502493ba-ff09-4044-9146-69fd32ebc039.png)
[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240297812-f8b33eb7-9cd0-4f26-b37d-7312fb495d4d.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240297812-f8b33eb7-9cd0-4f26-b37d-7312fb495d4d.png)

简单查看了一下字符串发现，这个PE文件内出现了少量明文的js代码，和有规律的js文件名储存结构，猜测js代码解密可能在这里?

通过JS文件名字符串，很容易定位一个函数体非常大的函数

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240309705-6c543cc8-dcfe-44ff-aa87-22ebf361b684.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240309705-6c543cc8-dcfe-44ff-aa87-22ebf361b684.png)

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240315372-1fda97b4-696b-42fe-94ee-124435615b85.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240315372-1fda97b4-696b-42fe-94ee-124435615b85.png)

这个函数内组装了数百个`ByteCodeInfo` 结构体，最终生成了生成一个结构体数组 `[]ByteCodeInfo`。

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240321006-6ed4a56f-1212-45d2-ae99-6bba98a11808.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240321006-6ed4a56f-1212-45d2-ae99-6bba98a11808.png)

通过结构体名可以猜测出，它可能储存的是V8字节码和js文件名与函数名的映射关系。

导出的字节码印证了这一点：熟悉nodejs分析的应该很容易看出来，他的头出现了 V8字节码的魔数部分`?? ?? DE C0`

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240330731-db14065e-4dd9-41fe-aefa-1948b61c0f59.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240330731-db14065e-4dd9-41fe-aefa-1948b61c0f59.png)

这个程序和开源的`bytenode`保护使用了相同的方法。都是把缓存的V8字节码保存下来，然后在运行时直接加载字节码缓存来避免源代码打包入代码，以达成源代码保护或是压缩代码提升性能的目的。

既然找到了字节码，我们就把它全部提取出来吧

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240337850-18424b23-af94-46a4-ab83-0391bb94948d.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1736240337850-18424b23-af94-46a4-ab83-0391bb94948d.png)

这里我写了一个IDA python脚本，把这个奇怪的`node`文件里面的所有储存的字节码和对应的文件信息全部提取了

## V8字节码

### V8字节码长什么样?

V8 字节码的生成是在`SerializedCodeData::SerializedCodeData` 中进行的

|  |
| --- |
| ``` SerializedCodeData::SerializedCodeData(const std::vector<uint8_t>* payload,                                        const CodeSerializer* cs) {   DisallowGarbageCollection no_gc;    // Calculate sizes.   uint32_t size = kHeaderSize + static_cast<uint32_t>(payload->size());   DCHECK(IsAligned(size, kPointerAlignment));    // Allocate backing store and create result data.   AllocateData(size);    // Zero out pre-payload data. Part of that is only used for padding.   memset(data_, 0, kHeaderSize);    // Set header values.   SetMagicNumber();   SetHeaderValue(kVersionHashOffset, Version::Hash());   SetHeaderValue(kSourceHashOffset, cs->source_hash());   SetHeaderValue(kFlagHashOffset, FlagList::Hash());   SetHeaderValue(kReadOnlySnapshotChecksumOffset,                  Snapshot::ExtractReadOnlySnapshotChecksum(                      cs->isolate()->snapshot_blob()));   SetHeaderValue(kPayloadLengthOffset, static_cast<uint32_t>(payload->size()));    // Zero out any padding in the header.   memset(data_ + kUnalignedHeaderSize, 0, kHeaderSize - kUnalignedHeaderSize);    // Copy serialized data.   CopyBytes(data_ + kHeaderSize, payload->data(),             static_cast<size_t>(payload->size()));   uint32_t checksum =       v8_flags.verify_snapshot_checksum ? Checksum(ChecksummedContent()) : 0;   SetHeaderValue(kChecksumOffset, checksum); } ``` |

V8 的字节码并没有固定的`C/C++`结构体定义，而是通过字节流的形式动态组织的。V8 中的某些类和辅助结构，像 `BytecodeArray`、`SerializedData` 或 `SnapshotData`，提供了一种逻辑上的结构化视图，使开发者能够以类和方法的形式操作字节码。

V8 字节码是一个字节流，类似于汇编语言中的指令序列，每条指令由 **操作码 (Opcode)** 和 **可选的操作数 (Operands)** 组成。每个操作码和操作数的组合可能具有不同的长度和参数布局。因此，字节码整体上并没有一个固定的内存对齐或结构体。

#### 魔数

首先，我们先看魔数(`MagicNumber`)部分。魔数在可以帮助我们快速在二进制文件中定位字节码可能出现的位置。

|  |
| --- |
| ``` static constexpr uint32_t kMagicNumberOffset = 0; static constexpr uint32_t kMagicNumber = 0xC0DE0000 ^ ExternalReferenceTable::kSize;  void SetMagicNumber() {      SetHeaderValue(kMagicNumberOffset, kMagicNumber);  } ``` |

魔数的值是通过固定值 `0xC0DE0000` 和 `ExternalReferenceTable::kSize` 的异或 (`^`) 操作得出的

|  |
| --- |
| ``` static constexpr int kSize =     kSizeIsolateIndependent + kExternalReferenceCountIsolateDependent +     kIsolateAddressReferenceCount + kStubCacheReferenceCount +     kStatsCountersReferenceCount; ``` |

魔数间接编码了与 `ExternalReferenceTable::kSize` 相关的信息

魔数位于序列化数据或快照数据的头部，作为识别该数据是否合法的标志。通过魔数，V8 可以快速判断数据是否符合特定版本和格式，如果加载了错误版本的字节码，V8引擎会直接抛出异常。

#### 版本哈希

版本哈希是 V8 代码中对当前版本的唯一标识。

|  |
| --- |
| ``` static uint32_t Hash() {     return static_cast<uint32_t>(         base::hash_combine(major_, minor_, build_, patch_)); } ``` |

它并没有直接明文记录当前版本的版本号，而是将版本号通过hash函数计算后写入头部.。

|  |
| --- |
| ``` V8_INLINE size_t hash_combine(Ts const&... vs) {   return Hasher{}.Combine(vs...); } ``` |

|  |
| --- |
| ``` // Combine two hash values together. This code was taken from MurmurHash. V8_INLINE size_t hash_combine(size_t seed, size_t hash) { #if V8_HOST_ARCH_32_BIT   const uint32_t c1 = 0xCC9E2D51;   const uint32_t c2 = 0x1B873593;    hash *= c1;   hash = bits::RotateRight32(hash, 15);   hash *= c2;    seed ^= hash;   seed = bits::RotateRight32(seed, 13);   seed = seed * 5 + 0xE6546B64; #else   const uint64_t m = uint64_t{0xC6A4A7935BD1E995};   const uint32_t r = 47;    hash *= m;   hash ^= hash >> r;   hash *= m;    seed ^= hash;   seed *= m; #endif  // V8_HOST_ARCH_32_BIT   return seed; } ``` |

HASH 算法使用的是`MururHash`

最终写了一个Go版本的 `V8` 字节码`版本Hash`的计算函数

|  |
| --- |
| ``` func hashValueUnsigned(v uint64) uint64 {     v = ((v << 15) - v - 1) & 0xFFFFFFFF     v = (v ^ (v >> 12)) & 0xFFFFFFFF     v = (v + (v << 2)) & 0xFFFFFFFF     v = (v ^ (v >> 4)) & 0xFFFFFFFF     v = (v * 2057) & 0xFFFFFFFF     v = (v ^ (v >> 16)) & 0xFFFFFFFF     return v }  func hashCombine(seed, value int64) int64 {     value = (value * 0xCC9E2D51) & 0xFFFFFFFF     value = ((value >> 15) | (value << (32 - 15))) & 0xFFFFFFFF     value = (value * 0x1b873593) & 0xFFFFFFFF     seed ^= value     seed = ((seed >> 13) | (seed << (32 - 13))) & 0xFFF...