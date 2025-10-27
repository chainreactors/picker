---
title: LLVM Pass-PWN：从理论到实践，从入门到精通
url: https://forum.butian.net/share/3848
source: 奇安信攻防社区
date: 2024-11-09
fetch_date: 2025-10-06T19:12:08.339085
---

# LLVM Pass-PWN：从理论到实践，从入门到精通

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

### LLVM Pass-PWN：从理论到实践，从入门到精通

内容包含LLVM Pass类PWN详细解读

环境搭建
====
我用kali本机只能下载有15和以上的，其他的缺少依赖项，懒得弄了，直接用docker搭建ubuntu20.04的可以下载
```bash
sudo apt install clang-8
sudo apt install llvm-8
sudo apt install clang-10
sudo apt install llvm-10
sudo apt install clang-12
sudo apt install llvm-12
```
基础知识
====
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-a7b9a9c2cb6089033c8906c0d4055f7134caefa6.png)
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-a1de9b8974add786b946771c0351906a082f06f7.png)
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-59e6dcf670dbe9f9113dfb536e12e04e6648cec3.png)
LLVM IR
-------
LLVM IR即代码的中间表示，有三种形式：
LLVM IR（Intermediate Representation，中间表示）是LLVM编译器框架中的一种中间代码表示形式。LLVM IR有三种主要的表示形式：
1. \*\*.ll 格式\*\*：人类可读的文本格式。
2. \*\*.bc 格式\*\*：适合机器存储和处理的二进制格式。
3. \*\*内存表示\*\*：LLVM编译器在运行时使用的内存中的数据结构。
### 实例
假设我们有一个简单的C语言代码：
```c
int add(int a, int b) {
return a + b;
}
```
编译这个代码时，LLVM会将其转换为LLVM IR。我们可以通过不同的方式查看和存储这个LLVM IR。
#### 1. \*\*.ll 格式（人类可读的文本格式）\*\*
这是LLVM IR的文本表示形式，适合人类阅读和编辑。你可以通过命令行工具`clang`或`llvm-dis`生成这个格式。
```llvm
; ModuleID = 'example.c'
source\_filename = "example.c"
define i32 @add(i32 %a, i32 %b) {
entry:
%0 = add i32 %a, %b
ret i32 %0
}
```
在这个例子中：
- `define i32 @add(i32 %a, i32 %b)` 定义了一个返回类型为`i32`（32位整数）的函数`add`，它有两个参数`a`和`b`，类型都是`i32`。
- `entry:` 是函数的入口基本块。
- `%0 = add i32 %a, %b` 表示将`a`和`b`相加，并将结果存储在临时变量`%0`中。
- `ret i32 %0` 返回结果`%0`。
#### 2. \*\*.bc 格式（二进制格式）\*\*
这是LLVM IR的二进制表示形式，适合机器存储和处理。它通常比文本格式更紧凑，适合在编译器内部传递或存储在磁盘上。
你可以通过`clang`或`llvm-as`工具生成这个格式：
```bash
clang -emit-llvm -c example.c -o example.bc
```
生成的`example.bc`文件是二进制格式，无法直接阅读，但可以通过`llvm-dis`工具将其转换回人类可读的`.ll`格式：
```bash
llvm-dis example.bc -o example.ll
```
#### 3. \*\*内存表示\*\*
当LLVM编译器在运行时处理代码时，LLVM IR会以内存中的数据结构形式存在。这种表示形式是LLVM编译器内部使用的，通常是通过C++对象和数据结构来表示的。
例如，函数`add`在内存中可能表示为一个`llvm::Function`对象，基本块`entry`表示为一个`llvm::BasicBlock`对象，指令`%0 = add i32 %a, %b`表示为一个`llvm::Instruction`对象。
这些内存中的对象和数据结构允许LLVM进行各种优化和代码生成操作。开发者可以通过LLVM的C++ API来操作这些内存表示，例如添加、删除或修改指令，或者进行各种优化。
```python
.c -&gt; .ll：clang -emit-llvm -S a.c -o a.ll
.c -&gt; .bc: clang -emit-llvm -c a.c -o a.bc
.ll -&gt; .bc: llvm-as a.ll -o a.bc
.bc -&gt; .ll: llvm-dis a.bc -o a.ll
.bc -&gt; .s: llc a.bc -o a.s
```
LLVM IR的处理
==========
LVM Pass可用于对代码进行优化或者对代码插桩（插入新代码），LLVM的核心库中提供了一些Pass类可以继承，通过实现它的一些方法，可以对传入的LLVM IR进行遍历并操作。
LLVM对IR中的函数、基本块（basic block）以及基本块内的指令的处理
### 示例函数
假设我们有一个简单的 C 语言函数：
```c
void example\_function(int x, int y) {
int result;
if (x &gt; y) {
result = x + y;
} else {
result = x \* y;
}
printf("The result is %d\n", result);
}
```
### 编译为 LLVM IR
将上述函数编译为 LLVM IR 可能会产生类似以下的中间表示：
```llvm
define void @example\_function(i32 %x, i32 %y) {
entry:
%result = alloca i32
%x\_gt\_y = icmp sgt i32 %x, %y
br i1 %x\_gt\_y, label %iftrue, label %iffalse
iftrue:
%add\_result = add i32 %x, %y
br label %after\_if
iffalse:
%mul\_result = mul i32 %x, %y
br label %after\_if
after\_if:
%phi\_result = phi i32 [ %add\_result, %iftrue ], [ %mul\_result, %iffalse ]
store i32 %phi\_result, i32\* %result
%print\_result = call void @printf(i8\* getelementptr inbounds ([17 x i8], [17 x i8]\* @.str, i32 0, i32 0), i32 %phi\_result)
ret void
@.str = private unnamed\_addr constant [17 x i8] c"The result is %d\n\00"
```
### 解释
- \*\*函数（Function）\*\*: `@example\_function` 是一个函数，它接受两个整数参数 `x` 和 `y` 并打印它们的运算结果。
- \*\*基本块（Basic Block）\*\*: 一个基本块是一段连续的指令序列，控制流不能从中中断。在这个示例中，我们有三个基本块：
- `entry`: 函数的入口点，分配局部变量空间并进行条件跳转。
- `iftrue`: 当 `x &gt; y` 时执行的代码块。
- `iffalse`: 当 `x &lt;= y` 时执行的代码块。
- `after\_if`: 无论哪个条件分支被执行之后的合并点。
- \*\*基本块内的指令（Instructions）\*\*: 每个基本块包含了一系列的指令。例如，在 `entry` 基本块中，我们有：
- `%result = alloca i32`：分配一个整数类型的局部变量 `result`。
- `%x\_gt\_y = icmp sgt i32 %x, %y`：比较 `x` 是否大于 `y`。
- `br i1 %x\_gt\_y, label %iftrue, label %iffalse`：根据条件跳转到 `iftrue` 或者 `iffalse` 基本块。
在 `iftrue` 基本块中，我们有：
- `%add\_result = add i32 %x, %y`：如果 `x &gt; y`，则计算 `x + y`。
- `br label %after\_if`：无条件跳转到 `after\_if` 基本块。
在 `iffalse` 基本块中，我们有：
- `%mul\_result = mul i32 %x, %y`：如果 `x &lt;= y`，则计算 `x \* y`。
- `br label %after\_if`：无条件跳转到 `after\_if` 基本块。
在 `after\_if` 基本块中，我们有：
- `%phi\_result = phi i32 [ %add\_result, %iftrue ], [ %mul\_result, %iffalse ]`：选择 `iftrue` 或 `iffalse` 中的结果作为最终结果。
- `store i32 %phi\_result, i32\* %result`：将结果存储到局部变量 `result` 中。
- `%print\_result = call void @printf(...)`：调用 `printf` 函数打印结果。
- `ret void`：返回空值，结束函数。
流程
==
- LLVM PASS就是去处理IR文件，通过opt利用写好的so库优化已有的IR，形成新的IR。
- LLVM PASS类PWN就是opt加载pass.so文件，对IR代码进行转换和优化这个过程中存在的漏洞加以利用。这里需要注意的是.so文件是不会被pwn的，我们pwn的是加载.so文件的程序——opt。所以我们需要对opt进行常规的检查。
CTF题目一般会给出所需版本的opt文件（可用./opt --version查看版本）或者在README文档中告知opt版本。安装好llvm后，可在/usr/lib/llvm-xx/bin/opt路径下找到对应llvm版本的opt文件（一般不开PIE保护）。
搜索vtable定位到虚表，最下面的函数就是重写的虚函数runOnFunction
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-b434003bcfd1ee8af84fc2d3a1ac274aeb990224.png)
调试
==
```bash
clang-8 -emit-llvm -S exp.c -o exp.bc或者
clang-8 -emit-llvm -S exp.c -o exp.ll
```
```bash
opt-8 -load ./VMPass.so -VMPass ./exp.bc
```
调试opt然后跟进到so文件
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-73dc061def395fd03526f4a678df6ae99ecc951b.png)
opt并不会一开始就将so模块加载进来，会执行一些初始化函数才会加载so模块。
调试的时候可以把断点下载llvm::Pass::preparePassManager，程序执行到这里的时候就已经加载了LLVMHello.so文件（或者到main+11507），我们就可以根据偏移进一步将断点下在LLVMHello.so文件里面
查看vmmap，发现已经加载进来，然后可以更加偏移断在runOnFunction上
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-e2a93af7d3a4ea717bf9a9f0d060dc729cf55796.png)
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-3b749b1c8afdc5ae70caae68934ef5d007ebf3ea.png)
成功
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-450f5a96d2608b87968ae1def11676a377ed1f80.png)
使用脚本
```python
from pwn import \*
import sys
import os
os.system("clang-8 -emit-llvm -S exp.c -o exp.bc")
p = gdb.debug(["./opt-8",'-load','./VMPass.so','-VMPass','./exp.bc'],"b llvm::Pass::preparePassManager\nc")
p.interactive()
```
IR结构
====
[LLVM IR数据结构分析](https://akaieurus.github.io/2023/10/02/LLVM-IR%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%88%86%E6%9E%90/)
LLVMContext
-----------
- 一个全局数据
- 只能通过`llvm::getGlobalContext();`创建赋值给一个`LLVMContext`变量
- 删除了拷贝构造函数和拷贝赋值函数
moudle
------
- 主要是包含函数和全局变量的两个链表
- 创建一个Module，需要一个名字和一个LLVMContext
- Module操作函数链表的成员函数 `begin() end () size() empty() functions()`，直接拿到函数链表的函数`getFunctionList()`，查找模块内函数链表中函数的函数`getFunction`
```c
iterator\_range functions() {
return make\_range(begin(), end());
}
FunctionListType &amp;getFunctionList() { return FunctionList; }
Function \*getFunction(StringRef Name) const;
```
- -Module操作全局变量的成员函数 `global\_begin() global\_end () global\_size() global\_empty() globals()`直接拿到全局变量链表的函数`getGlobalList()`
```c
iterator\_range globals() {
return make\_range(global\_begin(), global\_end());
}
GlobalListType &amp;getGlobalList() { return GlobalList; }
```
- 插入或查找函数 `StringRef Name：函数名 Type \*RetTy：返回值类型 ArgsTy… Args：每个参数的类型 FunctionType \*T：函数类型（其实就是参数类型和返回值类型的集合），可以通过get方法构造 isVarArg：是是否支持可变参数`
```c
FunctionCallee getOrInsertFunction(StringRef Name, FunctionType \*T);
template
FunctionCallee getOrInsertFunction(StringRef Name, Type \*RetTy,
ArgsTy... Args);
返回值类型是FunctionCallee，成员为一个Value指针（就是具体的函数Function 指针）和一个FunctionType指针
class FunctionCallee {
private:
FunctionType \*FnTy = nullptr;
Value \*Callee = n...