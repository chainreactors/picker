---
title: 初探UE4引擎逆向
url: https://forum.butian.net/share/3687
source: 奇安信攻防社区
date: 2024-08-29
fetch_date: 2025-10-06T17:59:26.094715
---

# 初探UE4引擎逆向

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 初探UE4引擎逆向

* [漏洞分析](https://forum.butian.net/topic/48)
* [CTF](https://forum.butian.net/topic/52)

前言：在现代游戏开发中，尤其是在像虚幻引擎（Unreal Engine）这样复杂而强大的引擎中，名称管理是一个至关重要的部分。名称不仅用于标识游戏中的各种对象，还用于调试、日志记录和资源管理等多个方面。虚幻引擎中的FName系统是一种高效的名称管理机制，能够快速查找和处理名称字符串。

前言：在现代游戏开发中，尤其是在像虚幻引擎（Unreal Engine）这样复杂而强大的引擎中，名称管理是一个至关重要的部分。名称不仅用于标识游戏中的各种对象，还用于调试、日志记录和资源管理等多个方面。虚幻引擎中的FName系统是一种高效的名称管理机制，能够快速查找和处理名称字符串。
本项目的目标是基于UE4.27.2源码，独立实现一个GName加密算法。通过分析UE4源码中的FName和FNameEntry结构，我们将重构并实现一个简化版本的名称管理系统，同时添加名称的加密和解密功能。这不仅有助于理解虚幻引擎的内部工作机制，还能提供一个独立的、可用于学习和参考的名称管理和加密系统。
加密算法在游戏开发中的应用非常广泛，例如保护敏感数据、防止作弊和提高安全性。本项目将展示如何在名称管理系统中集成简单的加密和解密逻辑，并确保这些操作的高效性和可靠性。
通过这个项目，我们希望能够提供一个易于理解且实用的示例，帮助开发者更好地掌握名称管理和加密算法的实现细节。同时，这也为进一步探索和扩展虚幻引擎中的其他复杂机制提供了一个良好的起点。
一、GetName加密算法
-------------
为什么要进行加密算法的逆向分析呢？ 答案就是为了后面实现加密算法做铺垫包括dump sdk等等。。。
主要目的是通过ID 获取字符串
GName
ID: 110024 ====字符串
使用ue源码 把game dump下来
GetName()
ctrl+f 查找GetName() 默认位置在Source-》Runtime-》Engine 在UObjectBaseUtillty.h里
```c
FString GetFullGroupName( bool bStartWithOuter ) const;
/\*\*
\* Returns the name of this object (with no path information)
\*
\* @return Name of the object.
\*/
FORCEINLINE FString GetName() const
{
return GetFName().ToString();
}
/\*\* Optimized version of GetName that overwrites an existing string \*/
FORCEINLINE void GetName(FString &amp;ResultString) const
{
GetFName().ToString(ResultString);
}
```
FORCEINLINE 强制内联
FString 返回值 是个class CORE\\_API FString 类
DataType Data; //只有一个成员变量
Data 是TArray类型
```c
class CORE\_API FString
{
private:
friend struct TContainerTraits; //友元
/\*\* Array holding the character data \*/
typedef TArray DataType;
DataType Data; //只有一个成员变量
template //模板
using TRangeElementType = typename TRemoveCV()))&gt;::Type&gt;::Type;
template
struct TIsRangeOfCharType : TIsCharType&gt;
{
};
template
struct TIsRangeOfTCHAR : TIsSame&gt;
{
```
搜索模板
重点类型
```c
TArray{
wchar\_t\* data;
int num; //有多长
int maxnum ；//最大长度
}
```
所以说FString 返回的是TArray类
再看下GetFname
```c
FORCEINLINE FName GetFName() const
{
return NamePrivate;
}
```
我们看下NamePrivate的类型，发现就是FName
FName NamePrivate;
这个FName在class COREUOBJECT\\_API UObjectBase 里，这里学习下计算偏移获取FName的位置
计算偏移方法用类首地址+虚表 函数 函数指针在64位下占8个字节，成员属性变量占具体属性的长度
```c
class COREUOBJECT\_API UObjectBase
{
.............
virtual void DeferredRegister(UClass \*UClassStaticClass,const TCHAR\* PackageName,const TCHAR\* Name);
private:
/\*\* Flags used to track and report various object states. This needs to be 8 byte aligned on 32-bit
platforms to reduce memory waste \*/
EObjectFlags ObjectFlags;
/\*\* Index into GObjectArray...very private. \*/
int32 InternalIndex;
/\*\* Class the object belongs to. \*/
UClass\* ClassPrivate;
/\*\* Name of this object \*/
FName NamePrivate;
/\*\* Object this object resides in. \*/
UObject\* OuterPrivate;
friend class FBlueprintCompileReinstancer;
friend class FContextObjectManager;
}
```
virtual void DeferredRegister 是个虚表调用 +8
EObjectFlags enum遍历 +8(4)
int32 InternalIndex; 是个typedef FPlatformTypes::int32 +4字节
UClass\\* ClassPrivate; 是个class类的函数指针 +8
所以FName 在 类首地址+8+8+4+8 的位置处
接着分析GetFName().ToString(); 跟进去
```c
FString FName::ToString() const
{
if (GetNumber() == NAME\_NO\_NUMBER\_INTERNAL)
{
// Avoids some extra allocations in non-number case
return GetDisplayNameEntry()-&gt;GetPlainNameString();
}
FString Out;
ToString(Out);
return Out;
}
```
看下GetDisplayNameEntry（）
```c
const FNameEntry\* FName::GetDisplayNameEntry() const
{
return &amp;GetNamePool().Resolve(GetDisplayIndex());
}
```
从GetDisplayIndex() 看
```c
class CORE\_API FName
{
public:
FORCEINLINE FNameEntryId GetDisplayIndex() const
{
const FNameEntryId Index = GetDisplayIndexFast();
checkName(IsWithinBounds(Index));
return Index;
}
}
GetDisplayIndexFast：
FORCEINLINE FNameEntryId GetDisplayIndexFast() const
{
#if WITH\_CASE\_PRESERVING\_NAME
return DisplayIndex;
#else
return ComparisonIndex; //FNameEntryId ComparisonIndex;
#endif
}
struct FNameEntryId
{
FNameEntryId() : Value(0) {}
......
private:
uint32 Value; 直接返回的ID
}
```
通过GetDisplayIndex分析看，直接返回的ID给Index 然后return
接着分析&amp;GetNamePool()
```c
static bool bNamePoolInitialized;
alignas(FNamePool) static uint8 NamePoolData[sizeof(FNamePool)];
// Only call this once per public FName function called
//
// Not using magic statics to run as little code as possible
static FNamePool&amp; GetNamePool()
{
if (bNamePoolInitialized)
{
return \*(FNamePool\*)NamePoolData;
}
FNamePool\* Singleton = new (NamePoolData) FNamePool;
bNamePoolInitialized = true;
return \*Singleton;
}
```
发现，这里NamePoolData是个全局变量，这里在ue4.23之前的版本里是GName，这里是4.23之后了，所以是NamePoolData，要想实现整个加密算法，必须通过IDA去找，这里先不介绍挖个坑，放到后面去说，这个主要功能是new了FNamePool 给Singleton 然后返回个指针
看下FNamePool 发现是个类class FNamePool
```c
class FNamePool
{
public:
FNamePool();
void Reserve(uint32 NumBlocks, uint32 NumEntries);
FNameEntryId Store(FNameStringView View);
FNameEntryId Find(FNameStringView View) const;
FNameEntryId Find(EName Ename) const;
const EName\* FindEName(FNameEntryId Id) const;
/\*\* @pre !!Handle \*/
FNameEntry&amp; Resolve(FNameEntryHandle Handle) const { return Entries.Resolve(Handle); }
bool IsValid(FNameEntryHandle Handle) const;
FNameEntryId StoreValue(const FNameComparisonValue&amp; Value);
void StoreBatch(uint32 ShardIdx, TArrayView Batch) { ComparisonShards[ShardIdx].InsertBatch(Batch); }
#if WITH\_CASE\_PRESERVING\_NAME
FNameEntryId StoreValue(const FNameDisplayValue&amp; Value, bool bReuseComparisonId);
void StoreBatch(uint32 ShardIdx, TArrayView Batch) { DisplayShards[ShardIdx].InsertBatch(Batch); }
bool ReuseComparisonEntry(bool bAddedComparisonEntry, const FNameDisplayValue&amp; DisplayValue);
#endif
/// Stats and debug related functions ///
uint32 NumEntries() const;
uint32 NumAnsiEntries() const;
uint32 NumWideEntries() const;
uint32 NumBlocks() const { return Entries.NumBlocks(); }
uint32 NumSlots() const;
void LogStats(FOutputDevice&amp; Ar) const;
uint8\*\* GetBlocksForDebugVisualizer() { return Entries.GetBlocksForDebugVisualizer(); }
TArray DebugDump() const;
private:
enum { MaxENames = 512 };
FNameEntryAllocator Entries;
#if WITH\_CASE\_PRESERVING\_NAME
FNamePoolShard DisplayShards[FNamePoolShards];
#endif
FNamePoolShard ComparisonShards[FNamePoolShards];
// Put constant lookup on separate cache line to avoid it being constantly invalidated by insertion
alignas(PLATFORM\_CACHE\_LINE\_SIZE) FNameEntryId ENameToEntry[NAME\_MaxHardcodedNameIndex] = {};
uint32 LargestEnameUnstableId;
TMap&gt; EntryToEName;
};
```
从上面代码看到，类里集成很多方法 属性等，然后调用了里面的Resolve() 继续跟进
FNameEntry&amp; Resolve(FNameEntryHandle Handle) const { return Entries.Resolve(Handle);
是个FNameEntry 类型 ，我们先去 FNameEntryHandle 去看下
```c
struct FNameEntryHandle
{
uint32 Block = 0;
uint32 Offset = 0;
FNameEntryHandle(uint32 InBlock, uint32 InOffset)
: Block(InBlock)
, Offset(InOffset)
{}
FNameEntryHandle(FNameEntryId Id)
: Block(Id.ToUnstableInt() &gt;&gt; FNameBlockOffsetBits)
, Offset(Id.ToUnstableInt() &amp; (FNameBlockOffsets - 1))
{}
}
static constexpr uint32 FNameBlockOffsetBits = 16;
static constexpr uint32 FNameBlockOffsets = 1 &lt;&lt; FNameBlockOffsetBits; //1&lt;&lt;16
FNameEntryHandle(FNameEntryId Id)
: Block(Id.ToUnstableInt() &gt;&gt; FNameBlockOffsetBits)
, Offset(Id.ToUnstableInt() &amp; (FNameBlockOffsets - 1))
{}
```
找到了关键性的加密算法，Id.ToUnstableInt() 就是跟进ID返回的value 它的值，
uint32 ToUnstableInt() const { return Value; }，将它的值进行加密
这里先记下，到后面写解密算法的时候用得到，然...