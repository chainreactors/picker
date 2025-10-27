---
title: PWN入门：观音救混淆-类型混淆
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587736&idx=1&sn=f65b5a50cc7725e674815a3d36db16a0&chksm=b18c22d286fbabc4604fd2294bef49335a3265eb99da90fd6170ccf663ae6f29a77d1cc83841&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-24
fetch_date: 2025-10-06T19:40:32.039449
---

# PWN入门：观音救混淆-类型混淆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EficNsfyv6H2XuGwTPCuDQ5ib5bsOou4bibkwyYxN01YSCqXpn6vuhV4qhXUXa0taIhz7RujjqYlRxw/0?wx_fmt=jpeg)

# PWN入门：观音救混淆-类型混淆

福建炒饭乡会

看雪学苑

# 类型混淆为何物

在高级程序语言中，一个变量通常由三部分组成，它们分别是数据类型、类型名、数值，其中类型名是程序语言区分变量的标志（同一作用范围内不可重复，比如C语言中函数内局部变量名不能重复），数值就是变量存储的数据，变量所属的数据类型决定了数值如何被解释。

变量所属的数据类型并不是一成不变的，在不少程序语言当中，是允许对变量的数据类型进行强制转换的。

变量的数据类型发生混淆时威胁可大可小，其中最为严重的就是函数变量的混淆。

## 函数变量

在C语言中函数会被分配一个地址，因此函数也可以被看作是一个指针类型的变量。

```
数据类型 (*函数名)(形参列表)

示例：
typedef void (*test_func)(void);
```

### 啥是多态？

结构体是C语言中一个更广为人知的概念，在此不会过多进行介绍。作为多变量的集合，Linux内核当中的结构体中常常会定义函数变量。

函数在我们的眼中，一般都是只能完成特定行为的，而函数变量可以绑定到任意的函数上，从这个角度上看，函数变量有着极大的自由度，Linux内核可以通过函数变量表现处不同的行为。

函数变量可以看作是实现多态的一种途径，这个多态是个什么东西呢？

### 虚函数与多态

多态这一概念源自于面向对象，用于借助同一种接口表现不同的行为，类似于插电孔，一个接口供应各种电器，不同电器可以被用于实现不同的目的。

虚函数就是C++实现多态的关键，它可以分成虚函数和纯虚函数。虚函数要求基类完成实现，子类可以重写虚函数，纯虚函数允许基类不进行实现，但要求子类必须实现，而且拥有纯虚函数的基类不能再创建实例对象，也就是作为抽象类存在。

## C++中的虚函数

相比于C语言中的多态实现，C++中用于实现多态的虚函数会更加复杂一些，下面会用一个示例进行解析。

下方是示例程序的源代码，从源代码中我们可以看到，程序创建了名为`my_test`的基类，并定义了虚函数`vtest1`、纯虚函数`vtest2`以及函数`test`，子类`testA`中重写了虚函数`vtest1`，并且对纯虚函数进行了实现，主函数`main`会对它们进行调用。

除此之外，类还包含着构造函数和析构函数`~`，这两个函数都有一个特点，就是函数名前不带数据类型名，构造函数会类创建时调用，析构函数会在类销毁时调用，在基类`my_test`中，我们可以看到析构函数`~my_test`前带了`virtual`标识符，这是为了让子类销毁时可以正常运行析构函数。

```
#include <iostream>

using namespace std;

class my_test {
public:
    my_test() {
        cout << "enter my_test" << endl;
    }
    virtual ~my_test() {
        cout << "enter leave my_test" << endl;
    }
    virtual void vtest1() {
        cout << "is " << __func__ << endl;
    }

    virtual void vtest2() = 0;

    void test_func();
};

void my_test::test_func(void) {
    cout << "enter " << __func__ << endl;
}

class testA: public my_test {
public:
    testA() {
        cout << "enter testA" << endl;
    }
    ~testA() {
        cout << "enter leave testA" << endl;
    }

    void vtest1 () override {
        cout << "is [testA] " << __func__ << endl;
    }

    void vtest2(void) {
        cout << "is [testA] " << __func__ <<endl;
    }
};

int main(void)
{
    my_test *tmp;

    tmp = (my_test*)new testA();

    tmp->vtest1();
    tmp->vtest2();
    tmp->test_func();

    delete tmp;
}
```

程序的运行结果如下：

```
enter my_test
enter testA
is [testA] vtest1
is [testA] vtest2
enter test_func
leave testA
leave my_test
```

### 探究奇怪的符号名

从反汇编结果中，我们可以看到很多奇奇怪怪的名字，它们的名字怎么变成这样了呢？让我们先从最先被调用的`plt`节看起！

#### 奇怪的PLT名

`plt`节的内容在下方并没有详细列出，因为它的解析流程与C语言是一致的，这里我们重点关注`libstdc++.so`是如何知道这种奇葩名字的。

```
plt节：
<_Znwm@plt>
<_ZdlPvm@plt>

主函数main：
call   401050 <_Znwm@plt>
call   401060 <_ZdlPvm@plt>
```

通过查看`libstdc++.so`中的符号信息可以知道，这些奇葩名字就是这个动态链接库定义的，通过比对运行期地址-运行期基地址得到的偏移值，可以确认这一现象。

```
ELF文件中的偏移值：
readelf -s /lib/x86_64-linux-gnu/libstdc++.so.6 | grep nwm
  4817: 00000000000a9570    53 FUNC    GLOBAL DEFAULT   13 _Znwm@@GLIBCXX_3.4
readelf -s /lib/x86_64-linux-gnu/libstdc++.so.6 | grep _ZdlPvm
  1473: 00000000000a78e0     9 FUNC    GLOBAL DEFAULT   13 _ZdlPvm@@CXXABI_1.3.9

运行期地址：
(gdb) info  symbol 0x00007ffff7ca9570
operator new(unsigned long) in section .text of /lib/x86_64-linux-gnu/libstdc++.so.6
(gdb) info symbol 0x00007ffff7ca78e0
operator delete(void*, unsigned long) in section .text of /lib/x86_64-linux-gnu/libstdc++.so.6

动态链接库基地址：
0x7ffff7c00000     0x7ffff7c99000    0x99000        0x0  r--p   /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.30
```

### 奇怪的new - 上

首先我们可以看到，调用`<_Znwm@plt>`处理`new`之前，会先将`0x8`压入`rdi`寄存器中作为第一个参数，这个`0x8`是什么东西呢？

```
mov    $0x8,%edi
call   401050 <_Znwm@plt>
mov    %rax,%rbx
mov    %rbx,%rdi
call   4013ea <_ZN5testAC1Ev>
```

通过追踪程序可以看到，`0x8`会在`new`函数实际运行时使用，通过GDB的符号解析支持或者解析符号信息都可以确认这一点。

```
GDB显示：
operator new(unsigned long)

DWARF显示：
<1><24b3>: Abbrev Number: 13 (DW_TAG_subprogram)
    <24b4>   DW_AT_name        : (indirect string, offset: 0xa4a): operator new
    <24bb>   DW_AT_linkage_name: (indirect string, offset: 0x5f4): _Znwm
<2><24c7>: Abbrev Number: 1 (DW_TAG_formal_parameter)
    <24c8>   DW_AT_type        : <0x537>
<2><24cc>: Abbrev Number: 0

ELF显示：
6: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND _Znwm@GLIBCXX_3.4 (2)
```

`new`这里接收0x8作为参数是为了分配占用8字节的指针。

### 初识调试符号

这里针对调试符号进行一下特别的说明，首先我们知道二进制文件是十分晦涩且难懂的，为了提高二进制文件的可读性，所以计算机提供调试符号将二进制信息转化为人类可读的语义信息（调试符号既可以像ELF文件一样打包进自身，也可以学习PE文件的做法，单独形成名为`.pdb`的文件）。

在Linux当中存在ELF符号和DWARF符号两种，首先我们先看下DWARF符号。

#### DWARF符号

在ELF文件中`.debug_xxx`节都是DWARF信息，在生成汇编文件`.s`时就可以看到它们的身影（通过GCC的`-save-temps`选项可以保留临时文件进行查看），Linux下查看二进制格式文件的DWARF信息，可以通过`readelf --debug-dump`将全部的DWARF信息转储出来。

ELF中有许多的`.debug_xxx`节，`.debug_info`节是需要我们重点关注的。

`.debug_info`节是DWARF的核心信息，它以树状图的形式存储DWARF信息，根节点是编译单元`Compile Unit`，每个`.o`文件都对应一个编译单元，编译单元下面的节点记录着所有需要使用的符号信息。

`<1>`可以看作是顶级符号，通过`<xx>`表明的符号级别可以将下属符号全部遍历出来。下面给出了一个示例，`<1>`中表明了`DW_TAG_subprogram`，这代表符号是函数，在属性名`DW_AT_name`中可以知道函数名是`shell_get`，函数节点包含一个名为`DW_TAG_formal_parameter`的子节点，它代表函数接收的形参，从`DW_AT_name`属性中可以看到形参名是`msg`，`DW_AT_type`属性标明了变量的数据类型，通过索引值`0x74`会先发现该变量是占8字节的指针，再根据`0x6f`可以知道变量被`const`关键字修饰，最后通过`0x68`找到数据类型`DW_TAG_base_type`。此时我们可以推导出完整的数据类型`signed char*`。

```
<0><c>: Abbrev Number: 55 (DW_TAG_compile_unit)
    ......
......
<1><1fa>: Abbrev Number: 23 (DW_TAG_subprogram)
    <1fb>   DW_AT_name        : (indirect string, offset: 0): shell_get
    ......
<2><214>: Abbrev Number: 6 (DW_TAG_formal_parameter)
    <215>   DW_AT_name        : msg
    <219>   DW_AT_decl_file   : 1
    <219>   DW_AT_decl_line   : 27
    <21a>   DW_AT_decl_column : 35
    <21b>   DW_AT_type        : <0x74>
    <21f>   DW_AT_location    : 2 byte block: 91 68 	(DW_OP_fbreg: -24)
<2><222>: Abbrev Number: 0
......
<1><68>: Abbrev Number: 1 (DW_TAG_base_type)
    <69>   DW_AT_byte_size   : 1
    <6a>   DW_AT_encoding    : 6	(signed char)
    <6b>   DW_AT_name        : (indirect string, offset: 0x5d): char
<1><6f>: Abbrev Number: 14 (DW_TAG_const_type)
    <70>   DW_AT_type        : <0x68>
<1><74>: Abbrev Number: 2 (DW_TAG_pointer_type)
    <75>   DW_AT_byte_size   : 8
    <75>   DW_AT_type        : <0x6f>
......
```

#### ELF符号

ELF符号指的就是`.symtab`节中的内容，ELF符号信息并不如DWARF符合全面。

如果没有GDB这样的调试器，或者ELF文件内也没有DWARF信息，还想要分析函数的形参、局部变量等信息，就只能从函数的反汇编结果抓起了！

### 奇怪的new - 下

调用`<_Znwm@plt>`完成`new`操作之后，我们会发现`new`会给`tmp`分配一个可用的地址，然后就会拿这个地址作为形参，然后调用`<_ZN5testAC1Ev>`函数。

```
mov    %rax,%rbx
movq   $0x0,(%rbx)
mov    %rbx,%rdi
call   4013b6 <_ZN5testAC1Ev>
```

阅读`_ZN5testAC1Ev`函数的反汇编代码可以知道，`_ZN5testAC1Ev`函数是`testA`类的构造函数，它会先调用基类的`my_test`构造函数，在执行自身构造函数中的逻辑。

从这里我们可以看出来，构造函数的调用是编译过程中安排好的。

```
_ZN5testAC1Ev
    -> mov %rdi,-0x18(%rbp)
    -> _ZN7my_testC1Ev
        -> mov %rdi,-0x8(%rbp)
        -> lea 0x2a9f(%rip),%rdx # 0x403d90
        -> mov -0x8(%rbp),%rax
        -> mov %rdx,(%rax)
    -> lea 0x2956(%rip),%rdx # 0x403d60
    -> mov -0x18(%rbp),%rax
    -> mov %rdx,(%rax)
```

上方给出了一些汇编代码，之所以将它们特别列出，是因为这些汇编代码做的事情并不是构造函数中指定的行为。

`_ZN5testAC1Ev`最先接受`tmp`的指针作为形参，然后将它放入`rbp-0x18`处，这是为了保存数据，避免`_ZN7my_testC1Ev`运行过程中破坏`rdi`。处理完形参后，我们可以发现`my_test`和`testA`的构造函数中存在着三条极其相似的汇编指令`lea ; mov ; mov`，它们做的事情也是相似的。第一步通过`lea`指令某数据在ELF文件内存镜像中的地址交给`rdx`，第二步通过`rax`防止`tmp`地址的数值，第三步将步骤一中的内存镜像地址存放到`tmp`上。

```
[22] .data.rel.ro      PROGBITS         0000000000403d50  00002d50
        0000000000000088  0000000000000000  WA       0     0     8
```

根据地址查看ELF文件可以知道数据对应的是`.data.rel.ro`节，该节中的这段数据是做什么用的呢？

### 原来你是虚函数表！

调用`testA`的构造函数前，程序会将`tmp`的指针先交给`rbx`再给`rdi`，从这里看来，单独复制一份地址给`rbx`好像是个很多余的操作啊！

```
mov    %rax,%rbx
mov    %rbx,%rdi
call   4013ea <_ZN5testAC1Ev>
```

编译器是非常聪明的，当我们继续往下看时，就会发现程序会将`tmp`的地址放到`rbp-0x18`的位置上，之后就会通过`mov (%rax),%rax`将前面构造函数放置的地址A存到`rax`中，然后偏移0x10 / 0x18得到地址B，再将地址B上保存的地址放入`rdx`中，最后调用`rdx`。`rbp-0x18`起到索引数据和作为形参传递的作用。

```
mov    %rbx,-0x18(%rbp)

vtest1:
mov    -0x18(%rbp),%rax
mov    (%rax),%rax
add    $0x10,%rax
mov    (%rax),%rdx
mov    -0x18(%rbp),%rax
mov    %rax,%rdi
call   *%rdx

vtest2:
mov    -0x18(%rbp),%rax
mov    (%rax),%rax
add    $0x18,%rax
mov    (%rax),%rdx
mov    -0x18(%rbp),%rax
mov    %rax,%rdi
call   *%rdx
```

函数1的地址等价于`0x403d60 + 0x10`，对应`.data.rel.ro`节上的`0x4014de`，函数2的地址等价于`0x403d60 + 0x18`，对应`.data.rel.ro`节上的`0x40152e`。

```
Contents of secti...