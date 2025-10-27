---
title: [2024]基于C++的混淆壳(二) IAT隐藏
url: https://key08.com/index.php/2024/03/08/1836.html
source: 白帽Wiki - 一个简单的wiki
date: 2024-03-09
fetch_date: 2025-10-04T12:11:41.745441
---

# [2024]基于C++的混淆壳(二) IAT隐藏

[![](https://key08.com/avatar_pack.gif)](https://key08.com/)

# 白帽Wiki

从2012年开始专注高级网络安全技术研究

查你所想

![](https://key08.com/avatar_pack.gif)

### 一只鸭子

* [首页](https://key08.com/)
* [板块活动记录](https://key08.com/index.php/1596.html "板块活动记录")
* [IDA Internal](https://key08.com/index.php/2365.html "IDA Internal")
* [EDR开发相关](https://key08.com/index.php/project_ayy_waf.html "EDR开发相关")
* [威胁追踪](https://key08.com/index.php/cve_detect.html "威胁追踪")
* [Hypervisor](https://key08.com/index.php/hypervisor_code.html "Hypervisor")
* [机器学习&神经网络](https://key08.com/index.php/keras.html "机器学习&神经网络")
* [EFI驱动编写](https://key08.com/index.php/EFI_Driver_Code.html "EFI驱动编写")
* [关于&联系方式](https://key08.com/index.php/215273185.html "关于&联系方式")

×

# [白帽Wiki - 一个简单的wiki](https://key08.com/)

## [[2024]基于C++的混淆壳(二) IAT隐藏](https://key08.com/index.php/2024/03/08/1836.html)

[huoji](https://key08.com/index.php/author/1/)
 [混淆](https://key08.com/index.php/tag/%E6%B7%B7%E6%B7%86/),[壳](https://key08.com/index.php/tag/%E5%A3%B3/),[IAT](https://key08.com/index.php/tag/IAT/)
 2024-03-08
 1569 次浏览
 0 次点赞

### 做壳步骤
创建区段
遍历所有指令
识别指令类型
加花/混淆/处理跳转表 <-先说到这里
处理原来老的区段
处理PE入口点
处理PE头
### IAT隐藏
我们希望我们的被加壳的程序IAT被隐藏掉,所以先遍历老的,保存为一个数组
```cpp
const auto peBase = peFile->get\_buffer()->data();
const auto sectionBase = peBase + newSection->VirtualAddress;
PIMAGE\_DATA\_DIRECTORY importDirectory =
&((PIMAGE\_NT\_HEADERS64)(peBase + ((PIMAGE\_DOS\_HEADER)peBase)->e\_lfanew))
->OptionalHeader.DataDirectory[IMAGE\_DIRECTORY\_ENTRY\_IMPORT];
if (importDirectory->Size > 0) {
// 获取第一个导入描述符
PIMAGE\_IMPORT\_DESCRIPTOR importDescriptor =
(PIMAGE\_IMPORT\_DESCRIPTOR)(peBase +
importDirectory->VirtualAddress);
while (importDescriptor->Name != 0) {
// 获取IAT
PIMAGE\_THUNK\_DATA64 thunk =
(PIMAGE\_THUNK\_DATA64)(peBase + importDescriptor->FirstThunk);
while (thunk->u1.AddressOfData != 0) {
LPCSTR function\_name;
bool isOrdinal = (thunk->u1.Ordinal & IMAGE\_ORDINAL\_FLAG);
if (isOrdinal) {
//function\_name = (LPCSTR)(thunk->u1.Ordinal & 0xFFFF);
function\_name = NULL;
}
else {
PIMAGE\_IMPORT\_BY\_NAME functionName = (PIMAGE\_IMPORT\_BY\_NAME)(peBase + thunk->u1.AddressOfData);
function\_name = (LPCSTR)functionName->Name;
}
if (function\_name) {
char\* dllName = (char\*)(peBase + importDescriptor->Name);
// 将信息添加到IatTable
\_BuildIAT entry;
entry.functionName = std::string(function\_name);
entry.dllName = std::string(dllName);
entry.inCodeSectionAddress = (uint64\_t)thunk->u1.Function;
IatTable.push\_back(entry);
}
// 移动到下一个thunk
thunk++;
}
// 移动到下一个导入描述符
importDescriptor++;
}
}
```
这边省略了Ordinal,因为我实在是懒得处理了,想处理找blackbone的代码
### 建表,复制
弄完后,建立一个表,存一些基本结构
```cpp
struct \_iatTable {
uint64\_t functionAddress;
char dllName[64];
char functionName[64];
};
struct \_initTable {
size\_t iatTableSize; //保持第一个
uint32\_t fnGetProcAddressOffset;
uint32\_t fnGetKernel32BaseOffset;
uint32\_t entryPoint;
\_iatTable iatTable[1];
};
```
把老的一坨IAT复制过来
```cpp
// 复制初始化信息到壳段头部
const auto copyiedSize =
sizeof(\_initTable) + (sizeof(\_iatTable) \* IatTable.size());
\_initTable\* initTable = (\_initTable\*)malloc(copyiedSize);
if (initTable == nullptr) {
// 这不是 驱动,没有低资源模式.
\_\_debugbreak();
}
memset(initTable, 0x0, copyiedSize);
auto startBase = (uint64\_t)sectionBase;
/\*
initTable
shellcode\_init
\*/
\_initTable\* insertTable = (\_initTable\*)(sectionBase);
for (size\_t i = 0; i < IatTable.size(); i++) {
const auto entry = &IatTable[i];
// 不可能大于64字节
if (entry->dllName.size() > sizeof(initTable->iatTable[i].dllName)) {
\_\_debugbreak();
}
memcpy(initTable->iatTable[i].dllName, entry->dllName.c\_str(),
entry->dllName.size());
memcpy(initTable->iatTable[i].functionName, entry->functionName.c\_str(),
entry->functionName.size());
entry->buildAddress =
(uint64\_t) & (&insertTable->iatTable[i])->functionAddress;
//printf("build address :%p \n", entry->buildAddress);
}
```
这样我们就把IAT的信息存到区段的头部了
区段开始 ->
->->init table结构
->->IAT结构
->->->->dll名字
->->->->函数名字
->->->->call的地址
至于怎么修复,下一章会说,还有一个重要的是,在修复重定位的时候 检查是不是来自iat的call,如果是 改为到指定的iattable1的call地址
```cpp
// 3. 在保护区域里面,就修正相对跳转地址为保护区域地址
// 如果当前正在拷贝一个call 0x123456
if (item.callType == \_callType::kIMM) {
// 看看是不是在保护区里面
for (auto& buildIns : sourceFunctionInsn.build\_ins) {
// 如果call的地址是被移动到保护区的地址
if (buildIns.codeSectionAddress == item.calladdress) {
// 修正他;
const auto nextAddress =
item.inNewSectoinAddress + item.insSize;
const auto newOffset =
buildIns.newSectionAddress - nextAddress;
memcpy((void\*)(item.inNewSectoinAddress + getInsCopyLength(item.cs\_ins)), &newOffset, 4);
item.isFixed = true;
break;
}
}
// 不在重新计算位置
if (item.isFixed == false) {
const auto nextAddress =
item.inNewSectoinAddress + item.insSize;
const auto newOffset = item.calladdress - nextAddress;
memcpy((void\*)(item.inNewSectoinAddress + getInsCopyLength(item.cs\_ins)), &newOffset, 4);
item.isFixed = true;
// \_\_debugbreak();
}
continue;
}
```
其他的mov lea 也一样处理.不再叙述

![](https://key08.com/usr/themes/GreenGrapes/img/creativecommons-cc.png)

本文由 [huoji](https://key08.com/index.php/author/1/) 创作，采用 [知识共享署名 3.0](http://creativecommons.org/licenses/by/3.0/cn)，可自由转载、引用，但需署名作者且注明文章出处。

 点赞 0

* 上一篇: [[2024]基于C++的混淆壳(一)](https://key08.com/index.php/2024/03/05/1834.html "[2024]基于C++的混淆壳(一)")
* 下一篇: [[2024]基于C++的混淆壳(三) shellcode与oep编写](https://key08.com/index.php/2024/03/13/1838.html "[2024]基于C++的混淆壳(三) shellcode与oep编写")

还不快抢沙发

[取消回复](https://key08.com/index.php/2024/03/08/1836.html#respond-post-1836)

添加新评论

提交评论

![icon_mrgreen.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mrgreen.png)![icon_neutral.png](https://key08.com/usr/plugins/Smilies/tieba/icon_neutral.png)![icon_twisted.png](https://key08.com/usr/plugins/Smilies/tieba/icon_twisted.png)![icon_arrow.png](https://key08.com/usr/plugins/Smilies/tieba/icon_arrow.png)![icon_eek.png](https://key08.com/usr/plugins/Smilies/tieba/icon_eek.png)![icon_smile.png](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)![icon_confused.png](https://key08.com/usr/plugins/Smilies/tieba/icon_confused.png)![icon_cool.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cool.png)![icon_evil.png](https://key08.com/usr/plugins/Smilies/tieba/icon_evil.png)![icon_biggrin.png](https://key08.com/usr/plugins/Smilies/tieba/icon_biggrin.png)![icon_idea.png](https://key08.com/usr/plugins/Smilies/tieba/icon_idea.png)![icon_redface.png](https://key08.com/usr/plugins/Smilies/tieba/icon_redface.png)![icon_razz.png](https://key08.com/usr/plugins/Smilies/tieba/icon_razz.png)![icon_rolleyes.png](https://key08.com/usr/plugins/Smilies/tieba/icon_rolleyes.png)![icon_wink.png](https://key08.com/usr/plugins/Smilies/tieba/icon_wink.png)![icon_cry.png](https://key08.com/usr/plugins/Smilies/tieba/icon_cry.png)![icon_surprised.png](https://key08.com/usr/plugins/Smilies/tieba/icon_surprised.png)![icon_lol.png](https://key08.com/usr/plugins/Smilies/tieba/icon_lol.png)![icon_mad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_mad.png)![icon_sad.png](https://key08.com/usr/plugins/Smilies/tieba/icon_sad.png)![icon_exclaim.png](https://key08.com/usr/plugins/Smilies/tieba/icon_exclaim.png)![icon_question.png](https://key08.com/usr/plugins/Smilies/tieba/icon_question.png)

![选择表情](https://key08.com/usr/plugins/Smilies/tieba/icon_smile.png)

[![](https://img.buymeacoffee.com/button-api/?text=Trust Feature For Human Duck&emoji=&slug=huoji&button_colour=16a085&font_colour=ffffff&font_family=Cookie&outline_colour=ffffff&coffee_colour=FFDD00)](https://www.buymeacoffee.com/huoji)

* [最新Wiki](#sidebar-new)
* [最新评论](#sidebar-comment)
* [随机Wiki](#sidebar-rand)

* [[2025]"ucpd.sys后门事件"详细分析技术报告-他是后门.....吗?](https://key08.com/index.php/2025/09/18/2815.html)
* [[2025]阻止漏洞驱动利用(byovd)技术致盲安全软件](https://key08.com/index.php/2025/09/15/2785.html)
* [[2025]深入研究R3通过网络(WFP架构)致盲EDR的技术原理与解决方案](https://key08.com/index.php/2025/08/31/2761.html)
* [[2025]从0制作IDA的F5代码还原功能(hex-rays插件) 上](https://key08.com/index.php/2025/08/12/2731.html)
* [[2025]VMP源码学习——变异分析](https://key08.com/index.php/2025/07/31/2729.html)
* [[2025]SleepDuck-通用堆栈欺骗检测POC,检测SleepMask](htt...