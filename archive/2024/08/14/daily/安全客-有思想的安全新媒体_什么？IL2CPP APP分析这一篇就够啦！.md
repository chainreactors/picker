---
title: 什么？IL2CPP APP分析这一篇就够啦！
url: https://www.anquanke.com/post/id/299096
source: 安全客-有思想的安全新媒体
date: 2024-08-14
fetch_date: 2025-10-06T18:01:58.520730
---

# 什么？IL2CPP APP分析这一篇就够啦！

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 什么？IL2CPP APP分析这一篇就够啦！

阅读量**345060**

发布时间 : 2024-08-13 15:55:29

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

> 本文作者：SWDD@360SRC

## 前言

近年来，由U3D开发的游戏越来越多，诸如最近很火的手游版“永劫无间”等等，因此针对于U3D游戏安全的保护也越来越高级，目前大多数厂商都会选择IL2CPP来编译游戏。即便如此，只使用简单的IL2CPP虽然在反编译上极大的增加了难度，但是由于C#+.Net的特性，无法像传统的ELF，EXE文件等完全抹除符号，所以还是给破解者留下了很大的操作空间，破解者可以通过对内存的读写来绕过游戏内一些机制的判定，使得游戏运营防遭受损失，因此本篇文章将针对于IL2CPP这一技术探究一下逆向与破解的过程。

最近刷抖音又发现了一款小爆款游戏，叫做我们是战士，后续调查发现抖音上那一款估计是套壳游戏，而原本这个游戏的名字叫做《We Are Warriors!》，但是由于这个游戏某些恶心的设定，于是决定逆向这个游戏看看到底是怎么回事，解压APK发现了该程序妥妥的U3D结构，并且使用了IL2CPP,于是便诞生了这篇总结文章。注意本文中不会涉及到对该游戏的逆向，而是利用demo程序等做同等的操作替换。

## Unity3D项目结构

在开始分析il2cpp之前，首先我们了解一下一个unity app的项目结构：

AppName/

├── Assets/    # 包含所有游戏资源和脚本文件

├── Library/    # Unity的库文件和缓存，自动生成

├── ProjectSettings/ # Unity项目设置文件夹

├── Packages/   # Unity Package Manager (UPM) 的依赖包

├── obj/      # 中间对象文件夹，用于编译时

├── Temp/     # 临时文件夹，包括临时生成的资源

├── Build/     # 打包输出目录，包括生成的App文件和数据

├── Logs/     # 日志文件夹

├── Packages/   # Unity Package Manager (UPM) 的依赖包

└── ProjectSettings/ # Unity项目设置文件夹

在生成的时候\Temp\StagingArea目录下则会产生安卓编译时所需要的内容。

![]()

生成APK后的结构如下：

AppName/

├── AndroidManifest.xml  # Android应用清单文件

├── assets/        # 包含资源文件夹，如图像和声音

├── res/         # 包含资源文件夹，如布局和字符串

├── lib/         # 包含原生库文件夹，如armeabi-v7a和arm64-v8a

├── META-INF/       # 包含APK签名的META-INF文件夹

├── classes.dex      # Android应用的主要DEX文件

├── resources.arsc    # 包含资源表文件

├── AndroidManifest.xml  # Android清单文件

├── res/         # 包含资源文件夹，如布局和字符串

├── assets/        # 包含资源文件夹，如图像和声音

├── lib/         # 包含原生库文件夹，如armeabi-v7a和arm64-v8a

打包成APK的unity项目实际上和正常的unity项目是一致的，其中的Java代码主要用于实现unity和Android平台的交互，是由unity自己生成的代码，因此我们在对Unity项目分析时主要关注的还是在assets目录下储存的项目信息。

Assets目录结构：

│ bin\

│ │ Data\

│ │ │ ├── boot.config

│ │ │ ├── data.unity3d

│ │ │ ├── platform\_native\_link.xml

│ │ │ ├── resources.resource

│ │ │ ├── RuntimeInitializeOnLoads.json

│ │ │ ├── ScriptingAssemblies.json

│ │ │ └── unity default resources

│ │ │ Managed\

│ │ │ │ dll文件\

│ │ Managed\

│ │ │ dll文件\

│ Data\

│ │ ├── boot.config

│ │ ├── data.unity3d

│ │ ├── platform\_native\_link.xml

│ │ ├── resources.resource

│ │ ├── RuntimeInitializeOnLoads.json

│ │ ├── ScriptingAssemblies.json

│ │ └── unity default resources

│ │ Managed\

│ │ │ dll文件\

│ Managed\

│ │ dll文件\

bin\

│ Data\

│ │ ├── boot.config

│ │ ├── data.unity3d

│ │ ├── platform\_native\_link.xml

│ │ ├── resources.resource

│ │ ├── RuntimeInitializeOnLoads.json

│ │ ├── ScriptingAssemblies.json

│ │ └── unity default resources

│ │ Managed\

│ │ │ dll文件\

│ Managed\

│ │ dll文件\

Data\

│ ├── boot.config

│ ├── data.unity3d

│ ├── platform\_native\_link.xml

│ ├── resources.resource

│ ├── RuntimeInitializeOnLoads.json

│ ├── ScriptingAssemblies.json

│ └── unity default resources

│ Managed\

│ │ dll文件\

Managed\

│ dll文件\

游戏的主要脚本逻辑就在assets\bin\Data\Managed\Assembly-CSharp.dll中，因此针对于使用Mono打包的Unity 3D项目直接使用ILSPY或者使用DNSPY就可以实现反编译，并且阅读性与源码基本无异。因为如此，导致了Mono打包的Unity App存在着极高的被破解风险，由此现在大多数的Unity 游戏都不使用Mono打包了，都开始使用iL2cpp，那么iL2cpp是如何提升逆向破解难度的呢？请继续往下看。

## IL2CPP分析

IL2CPP是Unity引入的一种新的脚本后处理方式，用于加强对编译后代码的保护。在Unity开发中，人物操作、攻击、伤害和死亡判断通常通过C#脚本实现。IL2CPP通过将C#脚本编译为C++代码，然后再编译为本地代码，提供了额外的安全层。这种方式使得反编译和逆向工程变得更加困难，有助于保护知识产权和游戏内容的安全性。

### **IL2CPP生成分析**

IL2CPP的代码位于\Editor\Data\il2cpp\libil2cpp\codegen，通过分析可以发现，IL2CPP采用了一种类似于虚拟机的机制。它通过将C#代码编译成中间语言（IL），然后再将IL代码转换成C++代码，最终编译为本地机器码。在这个过程中，IL2CPP对代码进行了多层次的优化和处理。

IL2CPP在将C#代码编译成IL代码时，会对代码进行一定程度的优化，例如移除不必要的代码和进行常量折叠。接着，IL代码会被转化为C++代码。在这个阶段，IL2CPP生成的C++代码不仅包含了原始C#代码的逻辑，还加入了一些辅助的代码，用于实现运行时环境和垃圾回收等功能。生成的C++代码会被编译为本地机器码。这一步通常会使用平台相关的编译器，以确保生成的代码在目标平台上具有最佳的性能和兼容性。由于C++代码在编译后变成了本地机器码，反编译的难度大大增加，从而增强了代码的安全性。IL2CPP还通过各种手段来优化代码执行的效率。它会对频繁执行的代码路径进行优化，以减少运行时的开销；它还会使用高效的数据结构和算法，以提高整体性能。

iL2cpp编译过程首先是将C#的脚本，还有Unity引擎的代码，Boo 代码通过各自的编译器编译为IL指令代码，然后还有一些其他的IL代码一起通过iL2cpp转化成C++代码，然后通过C++编译成libIL2cpp.so，再由Il2cpp提供的虚拟机对代码进行解释和运行。在其源码的结构中，也可以发现其两个部分的代码。

![]()

将流程转换成线性图则如下图所示：

![]()

### **IL2CPP加载分析**

根据IL2CPP的生成过程，我们会发现游戏的逻辑都到了Native运行，那么C#的语言特性需要如何继续实现呢，我们可以看vm中的代码。

在\Unity Edit\2021.3.22f1c1\Editor\Data\il2cpp\libil2cpp\vm\GlobalMetadata.cpp中我们可以发现如下代码

boolil2cpp::vm::GlobalMetadata::Initialize(int32\_t\*imagesCount, int32\_t\*assembliesCount)

{

s\_GlobalMetadata=vm::MetadataLoader::LoadMetadataFile(“global-metadata.dat”);

if (!s\_GlobalMetadata)

returnfalse;

​

s\_GlobalMetadataHeader= (constIl2CppGlobalMetadataHeader\*)s\_GlobalMetadata;

IL2CPP\_ASSERT(s\_GlobalMetadataHeader->sanity==0xFAB11BAF);

IL2CPP\_ASSERT(s\_GlobalMetadataHeader->version==29);

IL2CPP\_ASSERT(s\_GlobalMetadataHeader->stringLiteralOffset==sizeof(Il2CppGlobalMetadataHeader));

​

s\_MetadataImagesCount=\*imagesCount=s\_GlobalMetadataHeader->imagesSize/sizeof(Il2CppImageDefinition);

\*assembliesCount=s\_GlobalMetadataHeader->assembliesSize/sizeof(Il2CppAssemblyDefinition);

​

// Pre-allocate these arrays so we don’t need to lock when reading later.

// These arrays hold the runtime metadata representation for metadata explicitly

// referenced during conversion. There is a corresponding table of same size

// in the converted metadata, giving a description of runtime metadata to construct.

s\_MetadataImagesTable= (Il2CppImageGlobalMetadata\*)IL2CPP\_CALLOC(s\_MetadataImagesCount, sizeof(Il2CppImageGlobalMetadata));

s\_TypeInfoTable= (Il2CppClass\*\*)IL2CPP\_CALLOC(s\_Il2CppMetadataRegistration->typesCount, sizeof(Il2CppClass\*));

s\_TypeInfoDefinitionTable= (Il2CppClass\*\*)IL2CPP\_CALLOC(s\_GlobalMetadataHeader->typeDefinitionsSize/sizeof(Il2CppTypeDefinition), sizeof(Il2CppClass\*));

s\_MethodInfoDefinitionTable= (constMethodInfo\*\*)IL2CPP\_CALLOC(s\_GlobalMetadataHeader->methodsSize/sizeof(Il2CppMethodDefinition), sizeof(MethodInfo\*));

s\_GenericMethodTable= (constIl2CppGenericMethod\*\*)IL2CPP\_CALLOC(s\_Il2CppMetadataRegistration->methodSpecsCount, sizeof(Il2CppGenericMethod\*));

​

ProcessIl2CppTypeDefinitions(InitializeTypeHandle, InitializeGenericParameterHandle);

​

returntrue;

}

这个代码在加载global-metadata.dat，并且对其做了合法性判断。继续阅读后我们还会发现其使用了GetStringLiteralFromIndex(StringLiteralIndex index)等函数加载了字符信息，函数指针信息等一系列内容。

为了更好的分析，我们可以通过010导入UnityMetadata.bt的模板文件，使得文件的结构更加清晰。

//————————————————

//— 010 Editor v13.0.1 Binary Template

//

//  File: UnityMetadata.bt

// Authors: xia0

// Version: 0.2

// Purpose: Parse unity3d metadata file

// Category: Game

// File Mask: \*.dat

// ID Bytes: FA B1 1B AF

// History:

// 0.2 2023-03-24 avan: Automatically generate the string content of all StringLiterals based on the offset value of the StringLiteral in GlobalMetadataHeader.

// 0.1 2019-10-31 xia0: init basic unity3d metadata info version

//————————————————

// Blog: https://4ch12dy.site

// Github: https://github.com/4ch12dy

// https://www.sweetscape.com/010editor/manual/DataTypes.htm

// http://www.sweetscape.com/010editor/repository/templates/

​

typedefint32TypeIndex;

typedefint32TypeDefinitionIndex;

typedefint32FieldIndex;

typedefint32DefaultValueIndex;

typedefint32DefaultValueDataIndex;

typedefint32CustomAttributeIndex;

typedefint32ParameterIndex;

typedefint32MethodIndex;

typedefint32GenericMethodIndex;

typedefint32PropertyIndex;

typedefint32EventIndex;

typedefint32GenericContainerIndex;

typedefint32GenericParameterIndex;

typedefint16GenericParameterConstraintIndex;

typedefint32NestedTypeIndex;

typedefint32InterfacesIndex;

typedefint32VTableIndex;

typedefint32InterfaceOffsetIndex;

typedefint32RGCTXIndex;

typedefint32StringIndex;

typedefint32StringLiteralIndex;

typedefint32GenericInstIndex;

typedefint32ImageIndex;

typedefint32AssemblyIndex;

typedefint32InteropDataIndex;

​

​

typedefstructIl2CppGlobalMetadataHeader

{

int32sanity<format=hex>;

int32vers...