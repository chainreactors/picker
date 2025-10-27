---
title: PWN入门：误入格式化字符串漏洞
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588749&idx=2&sn=6fc809be9ede10a46f7d204c536cd5bf&chksm=b18c26c786fbafd14e4e451e21e415e3d96e93feb517543db94006ba90a0f748c9b78f0cc838&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-19
fetch_date: 2025-10-06T20:08:54.787657
---

# PWN入门：误入格式化字符串漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq9XHo3twq6unibFrHomIibOWQ8VxoubiaKby2bKvLsRDs3uophQItG3ZCag/0?wx_fmt=jpeg)

# PWN入门：误入格式化字符串漏洞

福建炒饭乡会

看雪学苑

```
一

格式化字符串介绍
```

##

可变参数

在常规情况下，C语言中函数接收的形参数量都是固定的，但事实上，C语言中函数接受形参的数量并不是必须固定的，也支持动态变化的形参数量。

函数间传递可变参数时，基本的要求是函数至少指定一个参数。

C语言中可变形参的定义方式如下所示，除了首个参数指定类型和变量名外，后续的参数都通过`...`省略号代替。

```
(type arg1, ...)
```

除了`...`省略号代表动态变化的参数外，C语言还允许宏内通过`__VA_ARGS__`代替`...`。

```
__VA_ARGS__

示例：
#define test(...) orig(__VA_ARGS__)
```

###

### 可变参数的处理

首先先来看一下可变参数是如何传递的。下方给出了函数原型和函数调用。

```
void test(int num, ...)
test(10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0);
```

从反汇编上看，调用者保存寄存器处理了前6个参数，栈空间处理了后5个参数。此时可以知道，可变参数的传递也是遵循函数调用规范的。

```
push   $0x0
push   $0x9
push   $0x8
push   $0x7
push   $0x6
mov    $0x5,%r9d
mov    $0x4,%r8d
mov    $0x3,%ecx
mov    $0x2,%edx
mov    $0x1,%esi
mov    $0xa,%edi
call   test
```

对于可变参数的处理，GLibC提供了下方的4个接口函数。

```
void va_start(va_list ap, last);
type va_arg(va_list ap, type);
void va_end(va_list ap);
```

####

#### va\_list

这几个接口函数都会接收一个类型为`va_list`的变量，`va_list`的全称是可变参数列表`variable argument list`。

```
typedef __builtin_va_list __gnuc_va_list;
typedef __gnuc_va_list va_list;
```

追踪`va_list`的定义时一开始会查找`usr`目录下的`stdarg.h`，但是这个头文件到`__builtin_va_list`就结束了，头文件中没有又在编译过程中产生，难道是GCC内部定义的？

在GCC的文档中，有一个特殊的专栏`gccint`，这个专栏主要是介绍GCC编译器的内部结构，其中`18.10 Implementing the Varargs Macros`专门介绍了`vaargs`相关宏的实现。

```
https://gcc.gnu.org/onlinedocs/gccint/Varargs.html
```

通过浏览GCC源代码可以发现，`__builtin_va_list`并不是直接定义的，而是GCC内部生成的，并且`__builtin_va_list`的定义是区分体系结构的，下面展示了X86架构的情况。

```
ix86_build_builtin_va_list_64
    -> build_decl (BUILTINS_LOCATION, TYPE_DECL, get_identifier ("__va_list_tag"), record);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("gp_offset"), unsigned_type_node);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("fp_offset"), unsigned_type_node);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("overflow_arg_area"), ptr_type_node);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("reg_save_area"), ptr_type_node);
```

可以在GDB中打印`va_list`变量确认这一点。

```
p /x valist
$1 = {{gp_offset = 0x8, fp_offset = 0x30, overflow_arg_area = 0x7fffffffde90, reg_save_area = 0x7fffffffddd0}}
```

通过查看目前另外一种非常流行的体系结构ARM，可以看到`__builtin_va_list`的成员结构与X86几乎完全不同。

```
aarch64_build_builtin_va_list
    -> build_decl (BUILTINS_LOCATION, TYPE_DECL, get_identifier ("__va_list"), va_list_type);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("__stack"), ptr_type_node);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("__gr_top"), ptr_type_node);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("__vr_top"), ptr_type_node);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("__gr_offs"), integer_type_node);
    -> build_decl (BUILTINS_LOCATION, FIELD_DECL, get_identifier ("__vr_offs"), integer_type_node);

p /x valist
$3 = {__stack = 0x7ffffff1c0, __gr_top = 0x7ffffff1c0, __vr_top = 0x7ffffff180, __gr_offs = 0xffffffc8, __vr_offs = 0xffffff80}
```

GCC支持的目标体系结构有很多，为了统一管理不同体系结构的实现，GCC定义了`TARGET_`宏接口，不同体系结构的实现需要绑定到对应的接口上。

比方说针对`va_list`的实现都绑定到`TARGET_BUILD_BUILTIN_VA_LIST`宏上。

```
#define TARGET_BUILD_BUILTIN_VA_LIST aarch64_build_builtin_va_list
#define TARGET_BUILD_BUILTIN_VA_LIST ix86_build_builtin_va_list

ix86_build_builtin_va_list
    -> ix86_build_builtin_va_list_64
```

每种体系结构的实现文件中都必须指定`targetm`成员，且该成员必须绑定到`TARGET_INITIALIZER`宏上。

```
struct gcc_target targetm = TARGET_INITIALIZER;
```

该宏的作用是初始化目标端架构信息，在`target.def`文件中实现`gcc_target`。

但它定义`gcc_target`结构体比较特殊。

```
HOOK_VECTOR (TARGET_INITIALIZER, gcc_target)
......
HOOK_VECTOR_END (C90_EMPTY_HACK)
```

先来看一下`HOOK_VECTOR`宏，它其实就是定义`struct xxx {`。

```
#define HOOKSTRUCT(FRAGMENT) FRAGMENT
#define HOOK_VECTOR_1(NAME, FRAGMENT) HOOKSTRUCT (FRAGMENT)
HOOK_VECTOR(INIT_NAME, SNAME) HOOK_VECTOR_1 (INIT_NAME, struct SNAME {)
```

当我们看到单`{`的时候一定会感觉很奇怪，怎么缺了一半！为了实现结构体的定义，缺的部分就一定有东西补上，在这里补缺口的就是`HOOK_VECTOR_END`。

`HOOK_VECTOR_END`匹配`HOOK_VECTOR`一块定义了`struct {,} xxx;`。

```
#define HOOK_VECTOR_END(DECL_NAME) HOOK_VECTOR_1(,} DECL_NAME ;)
```

结构体中的成员定义会一般会通过`DEFHOOK`定义，该宏会定义根据返回值数据类型`TYPE`、函数名`NAME`、形参列表`PARAMS`定义出函数指针变量。

```
#define DEFHOOK(NAME, DOC, TYPE, PARAMS, INIT) TYPE (* NAME) PARAMS;
```

以下方的`DEFHOOK`为例，它定义了`tree build_builtin_va_list(void)`。

```
DEFHOOK (
    build_builtin_va_list,
    "...",
    tree, (void),
    std_build_builtin_va_list
)
```

除了`DEFHOOK`宏之外，也可以通过`DEFHOOKPOD`宏定义一个普通变量。

```
#define DEFHOOKPOD(NAME, DOC, TYPE, INIT) TYPE NAME;
```

从上面可以看到`HOOK_VECTOR`和`HOOK_VECTOR_END`打着`TARGET_INITIALIZER`的旗号于定义了`gcc_target`结构体。

至于`TARGET_INITIALIZER`宏的真身，则会在编译过程中展现。编译时会生成`target-hooks-def.h`，其中包含着`TARGET_INITIALIZER`宏的定义。

```
#define TARGET_INITIALIZER \
    { \
        ...... \
        TARGET_BUILD_BUILTIN_VA_LIST, \
        ...... \
    }
```

GCC会通过`targetm`接口针对不同的架构定制生成的信息。比如下面通过`targetm.build_builtin_va_list`接口生成`va_list`。

```
c_common_nodes_and_builtins
    -> build_common_tree_nodes
        -> tree t = targetm.build_builtin_va_list ()
        -> va_list_type_node = t
    -> lang_hooks.decls.pushdecl(build_decl (UNKNOWN_LOCATION, TYPE_DECL, get_identifier ("__builtin_va_list"), va_list_type_node))
```

在`ix86_build_builtin_va_list`函数中我们会看到这样一种现象，就是获取`va_list`时会拿两次，分别对应`sysv`和`ms`，返回时会先判断，再选择其中的一种作为返回值。

这是因为GCC支持两种应用程序二进制接口`ABI Application Binary Interface`类型，一是`System V`，对应Unix/Linux平台，二是`MicroSoft`，对应微软的Windows平台，GCC会根据当前使用的平台进行选项。

Unix/Linux平台使用的ABI被称作是`ELF Executable and Linkable Format`，而Windows平台使用的ABI则被称作是`PE Portable Executable`，两种格式的ABI其实是非常接近的，因为它们都源自于`COFF Common File Format`。

```
ix86_build_builtin_va_list
    -> sysv_va_list_type_node
    -> ms_va_list_type_node
    -> return ((ix86_abi == MS_ABI) ? ms_va_list_type_node : sysv_va_list_type_node);
```

在X86架构中，`va_list`中存在`gp_offset`、`fp_offset`、`overflow_arg_area`、`reg_save_area`四个成员，其中`overflow_arg_area`指向非寄存器存储的数据地址（一般放在栈上），`reg_save_area`指向寄存器存储的数据地址（一般会从寄存器挪到栈上），`gp_offset`是指通用寄存器保存的数据在`reg_save_area`中的偏移值，`fp_offset`是指浮点寄存器保持的数据在`reg_save_area`中的偏移值。

```
----------------------------------------------
caller   | ...                               |
stack    | arg7, arg8, ..., argX             | <----|
----------------------------------------------      |
         | callee return                     |      |
         | caller rbp                        |      |
----------------------------------------------      |
         | ......                            |      |
         | xmm0 - xmm7                       | <--| |
callee   | rdi, rsi, rdx, rcx, r8, r9        | <--| |
stack    | ......                            |    | |
         | fp_offset         | gp_offset     |    | |
         | overflow_arg_area | reg_save_area |    | |
------------------^------------------^--------    | |
                  |                  |            | |
                  |                  |------------| |
                  |---------------------------------|
```

这里还需针对浮点数据特殊说明一下，下面展示了一个带有浮点类型数据的调用。

```
void test(int num, ...)
test(20,
    1.1, 2.1, 3.1, 4, 5, 6, 7, 8.2, 9.11, 0.11,
    1.1, 2.1, 3.1, 4, 5, 6, 7, 8.2, 9.11, 0.11);
```

从上方可以看到，`test`函数接受了许多的浮点数据。

在当前CPU中浮点寄存器一共有8个，如果可变参数列表中的浮点数据未超出8个，那么就会将当前传递的浮点数据数量放入`rax`寄存器中，如果超出了就将上限8压入`rax`寄存器中。

```
存入10个浮点数据：
mov    $0x8,%eax
call   test

存入3个浮点数据：
mov    $0x3,%eax
call   test
```

对于超出浮点寄存器存储上限的部分，当然也是放到栈上。

针对浮点数的处理可以分成四个阶段，第一个阶段是给1到7号浮点寄存器赋值，并将0号浮点寄存器的数值先放到`rax`内（因为0号浮点寄存器后面会用）。

第二个阶段是处理超出存储容量的浮点数，它有着非常统一的格式`movsd val,%xmm0 ; lea -0x8(%rsp),%rsp ; movsd %xmm0,(%rsp)`，第一步做的保存浮点数到寄存器`xmm0`，第二步是将`rsp`减去0x8再更新`rsp`，这相当于对栈进行扩容，第三步是将`xmm0`中保持的浮点数存放到刚扩大的栈上。

阶段三是还原`xmm0`寄存器中本应存放的数值。

阶段四是处理浮点寄存器保持的浮点数数量，然后调用函数。

```
阶段一：
movsd  0xdc1(%rip),%xmm7
movsd  0xdc1(%rip),%xmm6
movsd  0xdc1(%rip),%xmm5
movsd  0xdc1(%rip),%xmm4
movsd  0xdc1(%rip),%xmm3
movsd  0xdc1(%rip),%xmm2
movsd  0xd91(%rip),%xmm1
mov    0xd92(%rip),%rax

阶段二：
sub    $0x8,%rsp
movsd  0xd8e(%rip),%xmm0
lea    -0x8(%rs...