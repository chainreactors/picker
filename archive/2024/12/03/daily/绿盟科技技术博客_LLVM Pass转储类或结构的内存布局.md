---
title: LLVM Pass转储类或结构的内存布局
url: https://blog.nsfocus.net/llvm-pass/
source: 绿盟科技技术博客
date: 2024-12-03
fetch_date: 2025-10-06T19:39:15.396948
---

# LLVM Pass转储类或结构的内存布局

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# LLVM Pass转储类或结构的内存布局

### LLVM Pass转储类或结构的内存布局

[2024-12-02](https://blog.nsfocus.net/llvm-pass/ "LLVM Pass转储类或结构的内存布局")[绿盟科技](https://blog.nsfocus.net/author/nsfocuser/ "View all posts by 绿盟科技")

阅读： 984

## 一、背景介绍

有次因故需要了解std::string类型内存布局，简单折腾一番，分享了一篇

《GDB查看结构或类的内存布局及分离终端》
https://scz.617.cn/unix/202411151604.txt

bluerust随即让我看下面这篇

STL容器逆向与实战 – [2023-02-07]
https://mp.weixin.qq.com/s/bfzeGbieYWaPS3\_iB-gSeg

他的原话是，主要看”llvm pass dump data type”。看了这篇，于我而言，属于”每个字都认识”系列，大概明白其基本原理是啥，但完全不了解所涉及的”LLVM Pass”技术。我不会C++编程，基本未碰上过C++ STL容器逆向需求，不在意上文中那些具体容器的实现细节。我感兴趣的是，如何转储类或结构的内存布局，也就是上文第一部分的内容。本文面向”LLVM Pass”小白提供完整可操作示例，聚焦”转储内存布局”。

## 二、dumpclass.cpp

参看

————————————————————————–
Writing an LLVM Pass (legacy PM version)
https://llvm.org/docs/WritingAnLLVMPass.html

Writing an LLVM Pass
https://llvm.org/docs/WritingAnLLVMNewPMPass.html
————————————————————————–

看雪那篇是Legacy格式的”LLVM Pass”，此处dumpclass.cpp改写成New格式。支持两个命令行参数，允许成员名中包含相对偏移或绝对偏移，允许过滤类或结构名。

————————————————————————–
#include “llvm/Passes/PassBuilder.h”
#include “llvm/Passes/PassPlugin.h”
#include “llvm/Support/raw\_ostream.h”

#define DEFAULTSUBSTR “<default>”

using namespace llvm;

namespace {

static cl::opt<int> passmode
(
“passmode”,
cl::desc(“absolute offset or not”),
cl::value\_desc(“int”),
cl::init(0)
);

static cl::opt<std::string> substr
(
“substr”,
cl::desc(“part of struct name”),
cl::value\_desc(“std::string”),
cl::init(DEFAULTSUBSTR)
);

struct DumpClass : PassInfoMixin<DumpClass>
{

std::string getTypeName ( Type \*type, const DataLayout &data )
{
if ( type->isIntegerTy() )
{
IntegerType \*i = cast<IntegerType>( type );

return “uint” + std::to\_string( i->getBitWidth() ) + “\_t”;
}
else if ( type->isPointerTy() )
{
PointerType \*ptr = cast<PointerType>( type );

return getTypeName( ptr->getPointerElementType(), data ) + “\*”;
}
else if ( type->isArrayTy() )
{
ArrayType \*arr = cast<ArrayType>( type );

return getTypeName( arr->getArrayElementType(), data ) + “[” + std::to\_string( arr->getArrayNumElements() ) + “]”;
}
else if ( type->isFloatTy() )
{
return “float”;
}
else if ( type->isStructTy() )
{
StructType \*stc = cast<StructType>( type );

return std::string( stc->getStructName() );
}
else
{
return “unknown\_” + std::to\_string( data.getTypeAllocSizeInBits( type ) );
}
}

void dumpType ( int depth, Type \*type, const std::string &suffix, const DataLayout \*data, unsigned base, int mode )
{
std::string blank( depth \* 4, ‘ ‘ );

if ( type->isStructTy() )
{
StructType \*stc = cast<StructType>( type );
const StructLayout \*sl = data->getStructLayout( stc );

errs() << blank + stc->getStructName() + “\n” + blank + “{\n”;
for ( size\_t i = 0; i < stc->getStructNumElements(); i++ )
{
Type \*subType = stc->getStructElementType( i );
unsigned offset = sl->getElementOffset( i );
unsigned size = data->getTypeAllocSize( subType );

if ( mode > 0 )
{
offset += base;
dumpType( depth+1, subType, std::to\_string(offset)+”\_”+std::to\_string(size), data, offset, mode );
}
else
{
dumpType( depth+1, subType, std::to\_string(offset)+”\_”+std::to\_string(size), data, 0, mode );
}
}
errs() << blank + “} field\_” + suffix + “;\n”;
}
else
{
errs() << blank + getTypeName( type, \*data ) + ” field\_” + suffix + “;\n”;
}
}

void visitor ( Function &F )
{
if ( F.getName() != “main” )
{
return;
}

std::set<StructType\*> types;
const DataLayout &data = F.getParent()->getDataLayout();

for ( auto &B : F )
{
for ( auto &I : B )
{
if ( auto \*A = dyn\_cast<AllocaInst>( &I ) )
{
Type \*type = A->getAllocatedType();
if ( type->isStructTy() )
{
StructType \*stc = cast<StructType>( type );

if ( stc->isOpaque() )
{
continue;
}
std::string struct\_name
= std::string( stc->getStructName() );
if ( substr != DEFAULTSUBSTR && struct\_name.find( substr ) == std::string::npos )
{
continue;
}
types.insert( stc );
}
}
}
}

int index = 0;

for ( StructType \*type : types )
{
dumpType( 0, type, std::to\_string( index++ ), &data, 0, passmode );
}
}

PreservedAnalyses run ( Function &F, FunctionAnalysisManager &FAM )
{
visitor( F );
return PreservedAnalyses::all();
}

};

}

PassPluginLibraryInfo getDumpClassPluginInfo ()
{
const auto callback = []( PassBuilder &PB )
{
PB.registerPipelineParsingCallback
(
[](
StringRef Name,
FunctionPassManager &FPM,
ArrayRef<PassBuilder::PipelineElement>
)
{
if ( Name == “DumpClass” )
{
FPM.addPass( DumpClass() );
return true;
}
return false;
}
);
PB.registerPipelineStartEPCallback
(
[&]( ModulePassManager &MPM, auto )
{
FunctionPassManager FPM;

FPM.addPass( DumpClass() );
MPM.addPass( createModuleToFunctionPassAdaptor( std::move( FPM ) ) );
return true;
}
);
};

return { LLVM\_PLUGIN\_API\_VERSION, “DumpClass”, LLVM\_VERSION\_STRING, callback };
}

extern “C” LLVM\_ATTRIBUTE\_WEAK ::llvm::PassPluginLibraryInfo llvmGetPassPluginInfo ()
{
return getDumpClassPluginInfo();
}
————————————————————————–

从dumpclass.cpp生成dumpclass.so

clang-14 \
-I”/usr/include/llvm-14″ \
-I”/usr/include/llvm-c-14″ \
-Wall -pipe \
-fPIC -shared -Wl,-soname,dumpclass.so \
-O3 -s \
-o dumpclass.so dumpclass.cpp

后面会演示如何将dumpclass.so用作”LLVM Pass”来转储类或结构的内存布局。

## 三、dumptarget.cpp

dumptarget.cpp是假想的目标程序，将来根据dumptarget.cpp转储其中的类或结构。

————————————————————————–
#include <deque>
#include <map>
#include <unordered\_map>
#include <string>
#include <iostream>

class TargetClass
{
private:
std::string unused;
public:
std::deque<std::map<int, std::unordered\_map<std::string, int>>> myDeque;
std::map<int, std::unordered\_map<std::string, int>> myMap;
};

int main ( int argc, char \* argv[] )
{
TargetClass obj;

obj.myMap[1][“one”] = 1;
obj.myMap[2][“two”] = 2;

obj.myDeque.push\_back( obj.myMap );

for ( const auto &d : obj.myDeque )
{
for ( const auto &pair : d )
{
std::cout << “Key : ” << pair.first << ” -> Value : “;
for ( const auto &innerpair : pair.second )
{
std::cout << innerpair.first << ” -> ” << innerpair.second;
}
std::cout << std::endl;
}
}

return 0;
}
————————————————————————–

## 四、用dumpclass.so处理dumptarget.cpp

有多种办法加载dumpclass.so，此处演示其中之一，依次执行这两条命令

clang-14 \
-Wall -pipe -S -emit-llvm \
-Xclang -disable-O0-optnone \
-o dumptarget.ll dumptarget.cpp

opt-14 \
-disable-output \
-load ./dumpclass.so -load-pass-plugin ./dumpclass.so \
-passes=DumpClass -passmode=1 -substr=”::basic\_string” \
dumptarget.ll 2>&1 | less

先从dumptarget.cpp生成dumptarget.ll，再用dumpclass.so处理dumptarget.ll。正常情况下会得到

————————————————————————–
class.std::\_\_cxx11::basic\_string
{
struct.std::\_\_cxx11::basic\_string<char>::\_Alloc\_hider
{
uint8\_t\* field\_0\_8;
} field\_0\_8;
uint64\_t field\_8\_8;
union.anon
{
uint64\_t field\_16\_8;
uint8\_t[8] field\_24\_8;
} field\_16\_16;
} field\_0;
————————————————————————–

尝试不给opt指定passmode、substr参数，观察输出，加强理解。

## 五、pahole

pahole也能转储类或结构的内存布局，不如dumpclass.cpp，出于完备性写在此处。

g++ -Wall -pipe -std=c++11 -O0 -g -o dumptarget\_dbg dumptarget.cpp
...