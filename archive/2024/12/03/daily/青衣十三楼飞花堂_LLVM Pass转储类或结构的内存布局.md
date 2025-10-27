---
title: LLVM Pass转储类或结构的内存布局
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487768&idx=1&sn=89d39255b09284433239ad822791febc&chksm=fab2d227cdc55b318317efd325f9f77b943a90e3c735e7aa75b7ca639f1cc411ea6b7137a2dd&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2024-12-03
fetch_date: 2025-10-06T19:39:40.790674
---

# LLVM Pass转储类或结构的内存布局

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPM7icT5ajR9UUibGNBqmyibpJBFH7sv1Nk2WqnTPWeKM059LbyY6icTL0ONDCLSnU5Yg72oTWngUquLmA/0?wx_fmt=jpeg)

# LLVM Pass转储类或结构的内存布局

原创

沈沉舟

青衣十三楼飞花堂

```
创建: 2024-12-01 19:55

目录:

    ☆ 背景介绍
    ☆ dumpclass.cpp
    ☆ dumptarget.cpp
    ☆ 用dumpclass.so处理dumptarget.cpp
    ☆ pahole
    ☆ clang -Xclang -fdump-record-layouts
    ☆ VC有隐藏选项
```

☆ 背景介绍

有次因故需要了解std::string类型内存布局，简单折腾一番，分享了一篇

```
《GDB查看结构或类的内存布局及分离终端》
https://scz.617.cn/unix/202411151604.txt
```

bluerust随即让我看下面这篇

```
STL容器逆向与实战 - [2023-02-07]
https://mp.weixin.qq.com/s/bfzeGbieYWaPS3_iB-gSeg
```

他的原话是，主要看"llvm pass dump data type"。看了这篇，与我而言，属于"每个字都认识"系列，大概明白其基本原理是啥，但完全不了解所涉及的"LLVM Pass"技术，看过之后，老虎吃天、无处下爪。我不会C++编程，基本未碰上过C++ STL容器逆向需求，不在意上文中那些具体容器的实现细节。我感兴趣的是，如何转储类或结构的内存布局，也就是上文第一部分的内容。原作者有句话，随便简单写个pass来dump，深深刺激了我，别人随便简单弄的东西，代码都给了，我还是不知如何实践。或许有些同道遭遇类似囧境，本文面向"LLVM Pass"小白提供完整可操作示例，聚焦"转储内存布局"，是上文降阶后的狗尾续貂、画蛇添足。

☆ dumpclass.cpp

参看

```
Writing an LLVM Pass (legacy PM version)
https://llvm.org/docs/WritingAnLLVMPass.html

Writing an LLVM Pass
https://llvm.org/docs/WritingAnLLVMNewPMPass.html
```

看雪那篇是Legacy格式的"LLVM Pass"，此处dumpclass.cpp改写成New格式。支持两个命令行参数，允许成员名中包含相对偏移或绝对偏移，允许过滤类或结构名。

```
#include "llvm/Passes/PassBuilder.h"
#include "llvm/Passes/PassPlugin.h"
#include "llvm/Support/raw_ostream.h"

#define DEFAULTSUBSTR   "<default>"

using namespace llvm;

namespace {

static cl::opt<int> passmode
(
"passmode",
cl::desc("absolute offset or not"),
cl::value_desc("int"),
cl::init(0)
);

static cl::opt<std::string> substr
(
"substr",
cl::desc("part of struct name"),
cl::value_desc("std::string"),
cl::init(DEFAULTSUBSTR)
);

struct DumpClass : PassInfoMixin<DumpClass>
{

    std::string getTypeName ( Type *type, const DataLayout &data )
    {
        if ( type->isIntegerTy() )
        {
            IntegerType    *i   = cast<IntegerType>( type );

            return "uint" + std::to_string( i->getBitWidth() ) + "_t";
        }
        else if ( type->isPointerTy() )
        {
            PointerType    *ptr = cast<PointerType>( type );

            return getTypeName( ptr->getPointerElementType(), data ) + "*";
        }
        else if ( type->isArrayTy() )
        {
            ArrayType      *arr = cast<ArrayType>( type );

            return getTypeName( arr->getArrayElementType(), data ) + "[" + std::to_string( arr->getArrayNumElements() ) + "]";
        }
        else if ( type->isFloatTy() )
        {
            return "float";
        }
        else if ( type->isStructTy() )
        {
            StructType     *stc = cast<StructType>( type );

            return std::string( stc->getStructName() );
        }
        else
        {
            return "unknown_" + std::to_string( data.getTypeAllocSizeInBits( type ) );
        }
    }

    void dumpType ( int depth, Type *type, const std::string &suffix, const DataLayout *data, unsigned base, int mode )
    {
        std::string blank( depth * 4, ' ' );

        if ( type->isStructTy() )
        {
            StructType         *stc = cast<StructType>( type );
            const StructLayout *sl  = data->getStructLayout( stc );

            errs() << blank + stc->getStructName() + "\n" + blank + "{\n";
            for ( size_t i = 0; i < stc->getStructNumElements(); i++ )
            {
                Type       *subType = stc->getStructElementType( i );
                unsigned    offset  = sl->getElementOffset( i );
                unsigned    size    = data->getTypeAllocSize( subType );

                if ( mode > 0 )
                {
                    offset += base;
                    dumpType( depth+1, subType, std::to_string(offset)+"_"+std::to_string(size), data, offset, mode );
                }
                else
                {
                    dumpType( depth+1, subType, std::to_string(offset)+"_"+std::to_string(size), data, 0, mode );
                }
            }
            errs() << blank + "} field_" + suffix + ";\n";
        }
        else
        {
            errs() << blank + getTypeName( type, *data ) + " field_" + suffix + ";\n";
        }
    }

    void visitor ( Function &F )
    {
        if ( F.getName() != "main" )
        {
            return;
        }

        std::set<StructType*>   types;
        const DataLayout       &data    = F.getParent()->getDataLayout();

        for ( auto &B : F )
        {
            for ( auto &I : B )
            {
                if ( auto *A = dyn_cast<AllocaInst>( &I ) )
                {
                    Type   *type    = A->getAllocatedType();
                    if ( type->isStructTy() )
                    {
                        StructType *stc = cast<StructType>( type );

                        if ( stc->isOpaque() )
                        {
                            continue;
                        }
                        std::string struct_name
                                        = std::string( stc->getStructName() );
                        if ( substr != DEFAULTSUBSTR && struct_name.find( substr ) == std::string::npos )
                        {
                            continue;
                        }
                        types.insert( stc );
                    }
                }
            }
        }

        int                     index = 0;

        for ( StructType *type : types )
        {
            dumpType( 0, type, std::to_string( index++ ), &data, 0, passmode );
        }
    }

    PreservedAnalyses run ( Function &F, FunctionAnalysisManager &FAM )
    {
        visitor( F );
        return PreservedAnalyses::all();
    }

};

}

PassPluginLibraryInfo getDumpClassPluginInfo ()
{
    const auto  callback = []( PassBuilder &PB )
    {
        PB.registerPipelineParsingCallback
        (
            [](
                StringRef               Name,
                FunctionPassManager    &FPM,
                ArrayRef<PassBuilder::PipelineElement>
            )
            {
                if ( Name == "DumpClass" )
                {
                    FPM.addPass( DumpClass() );
                    return true;
                }
                return false;
            }
        );
        PB.registerPipelineStartEPCallback
        (
            [&]( ModulePassManager &MPM, auto )
            {
                FunctionPassManager FPM;

                FPM.addPass( DumpClass() );
                MPM.addPass( createModuleToFunctionPassAdaptor( std::move( FPM ) ) );
                return true;
            }
        );
    };

    return { LLVM_PLUGIN_API_VERSION, "DumpClass", LLVM_VERSION_STRING, callback };
}

extern "C" LLVM_ATTRIBUTE_WEAK ::llvm::PassPluginLibraryInfo llvmGetPassPluginInfo ()
{
    return getDumpClassPluginInfo();
}
```

从dumpclass.cpp生成dumpclass.so

```
clang-14 \
-I"/usr/include/llvm-14" \
-I"/usr/include/llvm-c-14" \
-Wall -pipe \
-fPIC -shared -Wl,-soname,dumpclass.so \
-O3 -s \
-o dumpclass.so dumpclass.cpp
```

后面会演示如何将dumpclass.so用作"LLVM Pass"来转储类或结构的内存布局。

☆ dumptarget.cpp

dumptarget.cpp是假想的目标程序，将来根据dumptarget.cpp转储其中的类或结构。

```
#include <deque>
#include <map>
#include <unordered_map>
#include <string>
#include <iostream>

class TargetClass
{
private:
    std::string                                                     unused;
public:
    std::deque<std::map<int, std::unordered_map<std::string, int>>> myDeque;
    std::map<int, std::unordered_map<std::string, int>>             myMap;
};

int main ( int argc, char * argv[] )
{
    TargetClass obj;

    obj.myMap[1]["one"] = 1;
    obj.myMap[2]["two"] = 2;

    obj.myDeque.push_back( obj.myMap );

    for ( const auto &d : obj.myDeque )
    {
        for ( const auto &pair : d )
        {
            std::cout << "Key : " << pair.first << " -> Value : ";
            for ( const auto &innerpair : pair.second )
            {
                std::cout << innerpair.first << " -> " << innerpair.second;
            }
            std::cout << std::endl;
        }
    }

    return 0;
}
``...