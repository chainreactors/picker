---
title: llvm中ll文件解读
url: https://forum.butian.net/share/3885
source: 奇安信攻防社区
date: 2024-11-19
fetch_date: 2025-10-06T19:16:27.589785
---

# llvm中ll文件解读

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

### llvm中ll文件解读

对于常见的llvm pass，网上已有很多文章，但是最近的CTF赛题也会出现在原本的llvm pass的基础上考察对ll文件的理解，需要对ll文件进行修改才能过了交互，本文将以几个例题阐述笔者对ll文件一些相关概念的理解，希望对你学习llvm pass有所帮助

ll文件中常见变量的理解
============
```text
@ - 全局变量
% - 局部变量
alloca - 在当前执行的函数的堆栈帧中分配内存，当该函数返回到其调用者时，将自动释放内存
i32 - 32位4字节的整数
align - 对齐
load - 读出，store写入
icmp - 两个整数值比较，返回布尔值
br - 选择分支，根据条件来转向label，不根据条件跳转的话类型goto
label - 代码标签
call - 调用函数
```
例题WMCTF-2024 babysigin
======================
\*\*很重要的一些理解\*\*
------------
```text
CallInst：函数类型的变量
LoadInst：ll中应对应load指令
StoreInst：ll中应对应store指令
llvm::dyn\_cast：这种就是判断其是否是GlobalVariable/LoadInst/StoreInst类型
```
有关LoadInst
----------
发现想要满足LoadInst类型，那么传入的不应该是个直接的值，而是先int cmd=1234,func(cmd)用这种方式传参即可
再详细解释一下LoadInst，比如我的exp.c中是这样的
```c
WMCTF\_WRITE(0x8888);
```
那么ll文件就会是这样,显然不满足load
```ll
call void @WMCTF\_WRITE(i32 noundef 34952)
```
但如果先定义一个变量再传参
```c
int cmd = 0x8888;
WMCTF\_WRITE(cmd);
```
那么ll文件就长这样
```ll
@cmd = dso\_local global i32 34952, align 4
%1 = load i32, i32\* @cmd, align 4
call void @WMCTF\_WRITE(i32 noundef %1)
```
\*\*显然这样就满足load类型了！！！\*\*
有关StoreInst
-----------
- 这部分和LoadInst类似，可以在WMCTF\\_OPEN分析中的最后一关这部分看到如何解决
这里先看简单的 WMCTF\\_OPEN 和 WMCTF\\_READ
---------------------------------
```c
v77 = llvm::ilist\_iterator,false,false&gt;::operator\*(&amp;v79);
//v76变成CallInst类型
v76 = (llvm::CallBase \*)llvm::dyn\_cast(v77);
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*WMCTF\_READ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
v19 = (llvm::Value \*)llvm::CallBase::getCalledFunction(v76);
//得到函数名称
v55 = llvm::Value::getName(v19);
v56 = v20;
llvm::StringRef::StringRef((llvm::StringRef \*)v54, "WMCTF\_READ");
if ( (llvm::operator==(v55, v56, v54[0], v54[1]) &amp; 1) != 0 )
{
//得到函数的第0个参数
v21 = llvm::CallBase::getOperand(v76, 0);
//将这个参数转换为ConstantInt类型
v53 = (llvm::ConstantInt \*)llvm::dyn\_cast(v21);
if ( v53 &amp;&amp; llvm::ConstantInt::getSExtValue(v53) == 0x6666 )
{
v22 = (llvm \*)fd;
if ( read(fd, (void \*)mmap\_addr, 0x40uLL) &lt; 0 )
{
v23 = llvm::errs(v22);
llvm::raw\_ostream::operator&lt;&lt;(v23, "WMCTF\_READ error\n");
v86 = 0;
return v86 &amp; 1;
}
v24 = llvm::errs(v22);
llvm::raw\_ostream::operator&lt;&lt;(v24, "WMCTF\_READ success\n");
}
}
//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*WMCTF\_MMAP\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
//与WMCTF\_READ类似不再做分析
v25 = (llvm::Value \*)llvm::CallBase::getCalledFunction(v76);
v51 = llvm::Value::getName(v25);
v52 = v26;
llvm::StringRef::StringRef((llvm::StringRef \*)v50, "WMCTF\_MMAP");
if ( (llvm::operator==(v51, v52, v50[0], v50[1]) &amp; 1) != 0 )
{
v27 = llvm::CallBase::getOperand(v76, 0);
v49 = (llvm::ConstantInt \*)llvm::dyn\_cast(v27);
if ( v49 &amp;&amp; llvm::ConstantInt::getSExtValue(v49) == 0x7890 )
{
mmap\_addr = mmap(0LL, 0x1000uLL, 3, 33, 0, 0LL);
if ( mmap\_addr == (const void \*)-1LL )
{
v28 = llvm::errs(0LL);
llvm::raw\_ostream::operator&lt;&lt;(v28, "WMCTF\_MMAP failed\n");
}
else
{
v29 = llvm::errs(0LL);
llvm::raw\_ostream::operator&lt;&lt;(v29, "WMCTF\_MMAP success\n");
}
}
}
```
- \*\*分析完后发现WMCTF\\_OPEN 和 WMCTF\\_READ只要正常传参就行\*\*
再看WMCTF\\_WRITE
--------------
```c
v30 = (llvm::Value \*)llvm::CallBase::getCalledFunction(v76);
v47 = llvm::Value::getName(v30);
v48 = v31;
llvm::StringRef::StringRef((llvm::StringRef \*)v46, "WMCTF\_WRITE");
if ( (llvm::operator==(v47, v48, v46[0], v46[1]) &amp; 1) != 0 )
{
//获取函数的第0个参数
v32 = llvm::CallBase::getOperand(v76, 0);
//判断这个参数是否是LoadInst类型
v45 = (llvm::UnaryInstruction \*)llvm::dyn\_cast(v32);
if ( !v45 )
{
v86 = 0;
return v86 &amp; 1;
}
//从LoadInst中获取第一个参数，判断其是否是全局变量
v33 = llvm::UnaryInstruction::getOperand(v45, 0);
v44 = (llvm::GlobalVariable \*)llvm::dyn\_cast(v33);
if ( !v44 )
{
v86 = 0;
return v86 &amp; 1;
}
//是全局变量再从GlobalVariable获的第一个参数
v34 = llvm::GlobalVariable::getOperand(v44, 0);
//将获得的参数值转换为ConstantInt类型
v43 = (llvm::ConstantInt \*)llvm::dyn\_cast(v34);
if ( v43 )
{
if ( (unsigned int)llvm::ConstantInt::getSExtValue(v43) != 0x8888 )
{
v86 = 0;
return v86 &amp; 1;
}
if ( write((int)&amp;dword\_0 + 1, mmap\_addr, 0x40uLL) &lt; 0 )
{
v35 = llvm::errs((llvm \*)((char \*)&amp;dword\_0 + 1));
llvm::raw\_ostream::operator&lt;&lt;(v35, "WMCTF\_WRITE error\n");
v86 = 0;
return v86 &amp; 1;
}
}
}
```
- \*\*分析完后发现WMCTF\\_WRITE传入的参数在ll中应当是load指令的结果，同时这个参数得是个全局变量\*\*
- ll文件中应当长这样
```ll
@cmd = dso\_local global i32 34952, align 4
%1 = load i32, i32\* @cmd, align 4
call void @WMCTF\_WRITE(i32 noundef %1)
```
最后看WMCTF\\_OPEN
--------------
- 先过第一关
```c
CalledFunction = (llvm::Value \*)llvm::CallBase::getCalledFunction(v76);
Name = llvm::Value::getName(CalledFunction);
v75 = v3;
llvm::StringRef::StringRef((llvm::StringRef \*)v73, "WMCTF\_OPEN");
if ( (llvm::operator==(Name, v75, v73[0], v73[1]) &amp; 1) != 0 )
{
//获取函数的0个参数，判断是否是LoadInst类型
Operand = llvm::CallBase::getOperand(v76, 0);
if ( (llvm::isa(&amp;Operand) &amp; 1) == 0 )
{
v4 = llvm::errs((llvm \*)&amp;Operand);
llvm::raw\_ostream::operator&lt;&lt;(v4, "parameter error: first operand is not a LoadInst\n");
v86 = 0;
return v86 &amp; 1;
}
//也是获取函数的第0个参数，但是和上面类似有点不同，笔者这里不懂，但是只要保证WMCTF\_OPEN的参数是load类型就行
v5 = (llvm \*)llvm::CallBase::getOperand(v76, 0);
v71 = (llvm::UnaryInstruction \*)llvm::dyn\_cast(v5);
if ( !v71 )
{
v6 = llvm::errs(v5);
llvm::raw\_ostream::operator&lt;&lt;(v6, "parameter error: filename is not a LoadInst\n");
v86 = 0;
return v86 &amp; 1;
}
//获取LoadInst的第0个参数
v70 = (llvm::Value \*)llvm::UnaryInstruction::getOperand(v71, 0);
//获取参数的名字
/\*
这里打个比方
%3 = load i8\*, i8\*\* @filename, align 8
v70 = (llvm::Value \*)llvm::UnaryInstruction::getOperand(v71, 0);就相当于获取和@filename有关的东西
那么llvm::Value::getName(v70);就是或者上述内容的名字，也就是filename
在exp.c中这就是char \*filename = "./flag";但是我们知道变量的命名不能带. 所以这里我们只能自己手动改ll文件
\*/
v69[0] = llvm::Value::getName(v70);
v69[1] = v7;
llvm::StringRef::StringRef((llvm::StringRef \*)v68, ".addr");
if ( (llvm::StringRef::contains(v69, v68[0], v68[1]) &amp; 1) == 0 )
{
v8 = llvm::errs((llvm \*)v69);
llvm::raw\_ostream::operator&lt;&lt;(v8, "parameter error: filepath does not contain .addr\n");
v86 = 0;
return v86 &amp; 1;
}
}
```
- 再过第二关,可以看到这个open实际上就是根据v66这个字符串的值来open，因此这个WMCTF::getFunctionCallValue\[abi:cxx11\]将是我们分析的重点
```c
anonymous namespace::WMCTF::getFunctionCallValue[abi:cxx11]((llvm \*)v66, (\_\_int64)this, Parent, v84, 0);
if ( (std::string::empty(v66) &amp; 1) != 0 )
{
v9 = llvm::errs((llvm \*)v66);
llvm::raw\_ostream::operator&lt;&lt;(v9, "function error: could not retrieve function call value\n");
v86 = 0;
v65 = 1;
}
else
{
Context = llvm::Module::getContext(Parent);
llvm::StringRef::StringRef(v63, v66);
v10 = v63[0];
String = (llvm::Value \*)llvm::ConstantDataArray::getString(Context, v63[0], v63[1], 0LL);
v41 = llvm::GlobalVariable::operator new((llvm::GlobalVariable \*)&amp;qword\_58, v10);
v38 = Parent;
Type = llvm::Value::getType(String);
v40 = String;
v11 = rand();
std::to\_string((std::\_\_cxx11 \*)v59, v11);
std::operator+(v60, "string\_constant", v59);
llvm::Twine::Twine(v61, v60);
llvm::Optional::Optional(&amp;v58, 1LL);
llvm::GlobalVariable::GlobalVariable(v41, v38, Type, 1LL, 8LL, v40, v61, 0LL, 0, v58, 0);
std::string::~string(v60);
std::string::~string(v59);
v62 = v41;
v12 = llvm::Mo...