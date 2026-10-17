---
title: Unreal Engine 4引擎基础及其2024第九届游戏安全竞赛-初赛-安卓客户端安全为例
url: https://mp.weixin.qq.com/s/XXn9ZrV4ZTEosOqtfCkjQA
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:27:28.923349
---

# Unreal Engine 4引擎基础及其2024第九届游戏安全竞赛-初赛-安卓客户端安全为例

# Unreal Engine 4引擎基础及其2024第九届游戏安全竞赛-初赛-安卓客户端安全为例

dayDReam\_10
dayDReam\_10

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 本文以 2024 第九届腾讯游戏安全竞赛安卓初赛题目（com.tencent.ace.match2024）为例，完整记录一次 UE4 手游的逆向过程。内容从 GUObjectArray、GWorld、GName 三大核心结构体的源码分析讲起，便于对 UE 引擎对象系统不熟悉的逆向入门者学习

使用工具：IDA 9.4Pro、Frida 17、ue4dumper

环境：Android 64 位，UE4.27

## 0.关键结构体基本认识

### GUObjectArray(FUObjectArray)

`UE`中所有东西都继承自`UObject`,引擎会维护一个全局对象数组`GUObjectArray`，里面存储了所有`UObject`对象的指针，通过这个数组可以遍历引擎中的每一个类，可以读取类的属性以及在内存中的偏移。

#### 我们从理解源代码开始

```
//EpicGames/UnrealEngine/blob/4.27/Engine/Source/Runtime/CoreUObject/Public/UObject/UObjectArray.h#L1056
class FUObjectArray
{
//后文提到extern COREUOBJECT_API FUObjectArray GUObjectArray所以直接找这里了
//FUObjectArray的内存布局
private:
typedef FChunkedFixedUObjectArray TUObjectArray;

    int32 ObjFirstGCIndex;//4Bytes
    int32 ObjLastNonGCIndex;//4Bytes
    int32 MaxObjectsNotConsideredByGC;//4Bytes
bool OpenForDisregardForGC;//1Byte
//此处有padding 3Bytes
    TUObjectArray ObjObjects;//offset=0x10
//...
};
// 关键显然是TUObjectArray ObjObjects 利用typedef 追FChunkedFixedUObjectArray

//EpicGames/UnrealEngine/blob/4.27/Engine/Source/Runtime/CoreUObject/Public/UObject/UObjectArray.h#L359
class FChunkedFixedUObjectArray
{
enum
 {
  NumElementsPerChunk = 64 * 1024,
 };//此处不属于布局

/** Master table to chunks of pointers **/
 FUObjectItem** Objects;//Chunk 指针表，通过它找到具体 Chunk
//可以理解为一个指向“指针数组”的指针
// Objects (FUObjectItem**)
//     │
//     └──→ 指向一个数组（因为数组也就是一个指针指向的）（块指针表）
//             │
//             ├─ [0] 是 FUObjectItem*，指向 Chunk 0
//             ├─ [1] 是 FUObjectItem*，指向 Chunk 1
//             ├─ [2] 是 FUObjectItem*，指向 Chunk 2
//             └─ ...
//而1 个 Chunk = 65536(0x10000) 个 FUObjectItem
//Chunk[i]
// ├── FUObjectItem[0]
// ├── FUObjectItem[1]
// ├── FUObjectItem[2]
// ├── ...
// └── FUObjectItem[65535]
//因为 UObject 数量可能很多，UE4 不能把所有 FUObjectItem 强行放在一个连续数组里，而是分成一块一块的
/** If requested, a contiguous memory where all objects are allocated **/
 FUObjectItem* PreAllocatedObjects;//连续预分配的 FUObjectItem 内存
/** Maximum number of elements **/
 int32 MaxElements;
/** Number of elements we currently have **/
 int32 NumElements;
/** Maximum number of chunks **/
 int32 MaxChunks;
/** Number of chunks we currently have **/
 int32 NumChunks;
}

//EpicGames/UnrealEngine/blob/4.27/Engine/Source/Runtime/CoreUObject/Public/UObject/UObjectArray.h#L26
struct FUObjectItem
//注意64位下 sizeof(FUObjectItem) = 0x18，尾部有一个4的padding
//32位下 sizeof(FUObjectItem) = 0x10 可以自己动手算算？
{
    UObjectBase* Object;   // +0x00
    int32 Flags;           // +0x08
    int32 ClusterRootIndex;// +0x0C
    int32 SerialNumber;    // +0x10
};

//Engine/Source/Runtime/CoreUObject/Public/UObject/UObjectBase.h line210
class COREUOBJECT_API UObjectBase
{
private:
//virtual ~UObjectBase()此类有虚析构函数
// 64 位下，指针 = 8 字节，vptr = 8 字节
// 8 + 4 + 4 + 8 + 8 + 8 = 40 = 0x28
// 32 位下，指针 = 4 字节，vptr = 4 字节
// 4 (vptr) + 4 (ObjectFlags) + 4 (InternalIndex) + 4 (ClassPrivate) + 8 (NamePrivate) + 4 (OuterPrivate) = 28 = 0x1C
/** Flags used to track and report various object states. This needs to be 8 byte aligned on 32-bit
     platforms to reduce memory waste */
 EObjectFlags     ObjectFlags;//0x08 //大小4字节
/** Index into GObjectArray...very private. */
 int32       InternalIndex;//0x0C
/** Class the object belongs to. */
 UClass*       ClassPrivate;//0x10
/** Name of this object */
 FName       NamePrivate;//64位下8 + 4 + 4 + 8 32位下 4 + 4 + 4 + 4
/** Object this object resides in. */
//...
virtual ~UObjectBase();
};

class CORE_API FName//Engine/Source/Runtime/Core/Public/UObject/NameTypes.h line906
{
private:

/** Index into the Names array (used to find String portion of the string/number pair used for comparison) */
 FNameEntryId ComparisonIndex;//用于忽略大小写的比较
#if WITH_CASE_PRESERVING_NAME
/** Index into the Names array (used to find String portion of the string/number pair used for display) */
 FNameEntryId DisplayIndex;//用于输出和展示
#endif // WITH_CASE_PRESERVING_NAME
/** Number portion of the string/number pair (stored internally as 1 more than actual, so zero'd memory will be the default, no-instance case) */
 uint32   Number;// 数字后缀
}

//Engine/Source/Runtime/Core/Public/UObject/NameTypes.h line78
struct FNameEntryId
{
private:
 uint32 Value;
//uint32 block  = Value >> 16;
//uint32 offset = Value & 0xFFFF;

CORE_API static FNameEntryId FromValidEName(EName Ename);
};

//Engine/Source/Runtime/Core/Public/UObject/NameTypes.h line180
class FNameEntry
//FNameEntry 是 FNamePool(Gname) 中存储一个名字（Name）的基本/最小条目
{
private:
#if WITH_CASE_PRESERVING_NAME//这个宏可能会影响后续反查
 FNameEntryId ComparisonId;//用于大小写机制:4 Byte
#endif
 FNameEntryHeader Header;//记录长度等信息//2 Byte
//  位布局（UE4.27，关闭 WITH_CASE_PRESERVING_NAME 时）：

//   15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0
//  ┌─────────────────────────────────────┬────┬──┐
//  │              Len (10位)             │ xx │W │
//  └─────────────────────────────────────┴────┴──┘
//                                           ↑    ↑
//                                          保留  IsWide (最低位)
//这一条用于确认下面的字符串是哪种类型
union
 {//真正存储字符串的地方
  ANSICHAR AnsiName[NAME_SIZE];//两种方法
  WIDECHAR WideName[NAME_SIZE];
 };
}
```

### GWorld(UWorld)

`UE`引擎中有一个全局变量`GWorld`，代表当前游戏的世界状态，通过`GWorld`可以访问到当前游戏中的所有关卡、角色、物品等信息，获取运行时数据实例，并且是一个指针变量，指向`Uworld。`

#### 一样的看源代码

```
//Engine/Source/Runtime/Engine/Classes/Engine/World.h line894
class UWorld : public UObject, public FNetworkNotify
//当 UWorld 继承 UObject 时，UWorld 对象在内存里的顺序:
// [ UObject 基类的所有成员 ]      ← 先放
// [ FNetworkNotify 部分，FNetworkNotify 是多态次基类，它的虚函数集合与 UObject 的虚表无法合并，因此它携带自己的 vptr，额外贡献 8 字节（64 位）或 4 字节（32 位）]
// [ UWorld 自己的成员 ]           ← 后放
//     PersistentLevel
//     NetDriver
//即：
// [ UObject 子对象 ]                   ← 主基类，偏移 0 开始
//     +0x00 vptr
//     +0x08 ObjectFlags
//     +0x0C InternalIndex
//     +0x10 ClassPrivate
//     +0x18 NamePrivate
//     +0x20 OuterPrivate
//     → 到 0x28 结束

// [ FNetworkNotify 子对象 ]            ← 多态次基类
//     +0x28 它自己的 vptr（8 字节，64 位下）
//     （没有数据成员）
//     → 到 0x30 结束

// [ UWorld 自己的成员 ]                 ← 从这里开始
//     +0x30 PersistentLevel
//     +0x38 NetDriver
//     ...
{
//     64位与32位差别：
//     64 位:
// +0x00  UObject vptr            8
// +0x08  ObjectFlags             4
// +0x0C  InternalIndex           4
// +0x10  ClassPrivate            8
// +0x18  NamePrivate             8
// +0x20  OuterPrivate            8
// +0x28  FNetworkNotify vptr     8
// +0x30  PersistentLevel         ←
//     32位：
// +0x00  UObject vptr             4
// +0x04  ObjectFlags              4
// +0x08  InternalIndex            4
// +0x0C  ClassPrivate             4
// +0x10  NamePrivate              8
// +0x18  OuterPrivate             4
// --------------------------------
//       sizeof(UObject) = 0x1C
// +0x1C  FNetworkNotify vptr      4
// +0x20  PersistentLevel          ←
ULevel*PersistentLevel;
// 64位: +0x30
// 32位: +0x20
// World 主 Level

AGameModeBase*AuthorityGameMode;
// 64位: +0x118
// 32位: +0x98
// GameMode

AGameStateBase*GameState;
// 64位: +0x120
// 32位: +0x9C
// GameState

TArray<ULevel*> Levels;
// 64位: +0x138
// 32位: +0xB0
// 当前 World 中的 Level 集合

FSceneInterface*Scene;
// 64位: +0x188
// 32位: +0xE0
// 渲染 Scene

TArray<TWeakObjectPtr<AController>> ControllerList;
// 64位: +0x198
// 32位: +0xE4
// Controller

TArray<TWeakObjectPtr<APlayerController>> PlayerControllerList;
// 64位: +0x1A8
// 32位: +0xF0
// PlayerController
};
//要点是Ulevel
//4.27/Engine/Source/Runtime/Engine/Classes/Engine/Level.h#L412
UCLASS(MinimalAPI)
class ULevel : public UObject, public IInterface_AssetUserData
{
GENERATED_BODY()

public:
FURLURL;//要找Actors就得先找FURL
//这里FURL无重要元素，直接给出布局
//     64位下ULevel
// │
// ├─ +0x00 UObject
// │
// ├─ +0x28 IInterface_AssetUserData
// │
// ├─ +0x30 FURL URL
// │      ├─ +0x00 Protocol
// │      ├─ +0x10 Host
// │      ├─ +0x20 Port
// │      ├─ +0x24 Valid
// │      ├─ +0x28 Map
// │      ├─ +0x38 RedirectURL
// │      ├─ +0x48 Op
// │      └─ +0x58 Portal 十字节
// │
// ├─ +0x98 Actors

// 32位下 ULevel
//
// ├─ +0x00  UObjectBase     ...