---
title: JerryScript引擎ecma_op_to_index漏洞分析与越界读写利用
url: https://mp.weixin.qq.com/s/J9IC6PzcIgmylIhUSGkbZg
source: Doonsec's feed
date: 2026-02-06
fetch_date: 2026-02-07T04:06:10.148978
---

# JerryScript引擎ecma_op_to_index漏洞分析与越界读写利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1Mlr6Ku5zUjIumqAk6ia6bF3WbJTW3jT3sKuCGEMCHenweYBVlc8aGxXDpuceJbglibruteNaLvH9wjBCUN6yKmwxeiaEQ0icGevE/0?wx_fmt=jpeg)

# JerryScript引擎ecma\_op\_to\_index漏洞分析与越界读写利用

flyyyy
flyyyy

看雪学苑

![]()

在小说阅读器中沉浸阅读

听说第八届“强网”拟态防御国际精英挑战赛一道 JerryScript 的 Pwn 题，抽空尝试做了一下。当时构造出 8 字节的越界读写后，一直尝试利用，但由于 GC 的原因一直没有成功，时间比较短，如果再多些时间应该也是可以利用成功的。

不过在调试过程中，了解了该引擎的一些机制，发现相比 v8 还是简单很多的。赛后与其他师傅交流，才发现原来可以通过 Patch 中的漏洞实现任意长度的越界读写。因此尝试复现了一下，诞生了这篇 writeup。

**题目信息**

题目给了几个程序运行的链接库，看了下版本是Ubuntu GLIBC 2.39-0ubuntu8.6，由于我本地位wsl2 ubuntu22版本，所以patch了一下。

查看jerryscript的版本信息

```
➜  jerry ./jerry --version
Version: 3.0.0 (b7069350)
```

接着本地编译一个，最后会看到build/bin目录下有一个jerry的可执行文件

```
git clone https://github.com/jerryscript-project/jerryscript.git
cd jerryscript
git checkout b7069350
patch -p1 < ../patch
python tools/build.py --debug --lto=off
```

**前置知识**

## 类型系统 类型的定义位于这个文件中 jerryscript/jerry-core/ecma/base/ecma-globals.h

ecma\_object\_t是类型header的开始部分，其中主要的字段有type、gc\_next\_cp、u1、u2。

其中的u1和u2分别代表properties和prototype相关，不是每一个对象都有这两个字段。

```
typedef struct
{
/** type : 4 bit : ecma_object_type_t or ecma_lexical_environment_type_t
                     depending on ECMA_OBJECT_FLAG_BUILT_IN_OR_LEXICAL_ENV
      flags : 2 bit : ECMA_OBJECT_FLAG_BUILT_IN_OR_LEXICAL_ENV,
                      ECMA_OBJECT_FLAG_EXTENSIBLE or ECMA_OBJECT_FLAG_BLOCK
      refs : 10 / 26 bit (max 1022 / 67108862) */
ecma_object_descriptor_t type_flags_refs;

/** next in the object chain maintained by the garbage collector */
jmem_cpointer_t gc_next_cp;

/** compressed pointer to property list or bound object */
union
  {
jmem_cpointer_t property_list_cp; /**< compressed pointer to object's
                                       *   or declerative lexical environments's property list */
jmem_cpointer_t bound_object_cp; /**< compressed pointer to lexical environments's the bound object */
jmem_cpointer_t home_object_cp; /**< compressed pointer to lexical environments's the home object */
  } u1;

/** object prototype or outer reference */
union
  {
jmem_cpointer_t prototype_cp; /**< compressed pointer to the object's prototype  */
jmem_cpointer_t outer_reference_cp; /**< compressed pointer to the lexical environments's outer reference  */
  } u2;
} ecma_object_t;
```

type\_flags\_refs中的Type就指的是类型，但是并不像v8那样细分为object arr、double arr……

其中的refs，这个对于利用的稳定性比较重要，如果产生了越界，可以通过修改这个字段不让改对象被gc回收，从而保持布局的稳定性。

> 然后笔者在实际利用过程中并没有这样，当时没有意识到，回头翻看源码的时候才发现。所以采用了人为构造函数进行ref，增加ref count

下面是一个简单的图示

```
|31 ......................... 6 |5 ......4 |3 ........ 0 |
|          Reference Count       |    Flags   |Type     |
|(26 bits)|(2 bits)|(4 bits)|
```

接着的gc\_next\_cp是用于gc回收时扫描对象而设立的字段，u1与properties相关，在受限的情况下，可以采用修改和这个字段的方式进行类型混淆，u2和原型链有关，暂时也没想到这个怎么用。

> 笔者尝试过，当时由于稳定性的原因，没有构造出很好用的原语，等待后续研究……

下面是 ecma\_extended\_object\_t 结构体

```
typedef struct
{
ecma_object_t object; /**< object header */

/**
   * Description of extra fields. These extra fields depend on the object type.
   */
union
  {
ecma_built_in_props_t built_in; /**< built-in object part */

/**
     * Description of objects with class.
     *
     * Note:
     *     class is a reserved word in c++, so cls is used instead
     */
struct
    {
uint8_t type; /**< class type of the object */
/**
       * Description of 8 bit extra fields. These extra fields depend on the type.
       */
union
      {
uint8_t arguments_flags; /**< arguments object flags */
uint8_t error_type; /**< jerry_error_t type of native error objects */
#if JERRY_BUILTIN_DATE
uint8_t date_flags; /**< flags for date objects */
#endif /* JERRY_BUILTIN_DATE */
#if JERRY_MODULE_SYSTEM
uint8_t module_state; /**< Module state */
#endif /* JERRY_MODULE_SYSTEM */
uint8_t iterator_kind; /**< type of iterator */
uint8_t regexp_string_iterator_flags; /**< flags for RegExp string iterator */
uint8_t promise_flags; /**< Promise object flags */
#if JERRY_BUILTIN_CONTAINER
uint8_t container_flags; /**< container object flags */
#endif /* JERRY_BUILTIN_CONTAINER */
#if JERRY_BUILTIN_TYPEDARRAY
uint8_t array_buffer_flags; /**< ArrayBuffer flags */
uint8_t typedarray_type; /**< type of typed array */
#endif /* JERRY_BUILTIN_TYPEDARRAY */
      } u1;
/**
       * Description of 16 bit extra fields. These extra fields depend on the type.
       */
union
      {
uint16_t formal_params_number; /**< for arguments: formal parameters number */
#if JERRY_MODULE_SYSTEM
uint16_t module_flags; /**< Module flags */
#endif /* JERRY_MODULE_SYSTEM */
uint16_t iterator_index; /**< for %Iterator%: [[%Iterator%NextIndex]] property */
uint16_t executable_obj_flags; /**< executable object flags */
#if JERRY_BUILTIN_CONTAINER
uint16_t container_id; /**< magic string id of a container */
#endif /* JERRY_BUILTIN_CONTAINER */
#if JERRY_BUILTIN_TYPEDARRAY
uint16_t typedarray_flags; /**< typed array object flags */
#endif /* JERRY_BUILTIN_TYPEDARRAY */
      } u2;
/**
       * Description of 32 bit / value. These extra fields depend on the type.
       */
union
      {
ecma_value_t value; /**< value of the object (e.g. boolean, number, string, etc.) */
ecma_value_t target; /**< [[ProxyTarget]] or [[WeakRefTarget]] internal property */
#if JERRY_BUILTIN_TYPEDARRAY
ecma_value_t arraybuffer; /**< for typedarray: ArrayBuffer reference */
#endif /* JERRY_BUILTIN_TYPEDARRAY */
ecma_value_t head; /**< points to the async generator task queue head item */
ecma_value_t iterated_value; /**< for %Iterator%: [[IteratedObject]] property */
ecma_value_t promise; /**< PromiseCapability[[Promise]] internal slot */
ecma_value_t sync_iterator; /**< IteratorRecord [[Iterator]] internal slot for AsyncFromSyncIterator */
ecma_value_t spread_value; /**< for spread object: spreaded element */
int32_t tza; /**< TimeZone adjustment for date objects */
uint32_t length; /**< length related property (e.g. length of ArrayBuffer) */
uint32_t arguments_number; /**< for arguments: arguments number */
#if JERRY_MODULE_SYSTEM
uint32_t dfs_ancestor_index; /**< module dfs ancestor index (ES2020 15.2.1.16) */
#endif /* JERRY_MODULE_SYSTEM */
      } u3;
    } cls;

/**
     * Description of function objects.
     */
struct
    {
jmem_cpointer_tag_t scope_cp; /**< function scope */
ecma_value_t bytecode_cp; /**< function byte code */
    } function;

/**
     * Description of array objects.
     */
struct
    {
uint32_t length; /**< length property value */
uint32_t length_prop_and_hole_count; /**< length property attributes and number of array holes in
                                            *   a fast access mode array multiplied ECMA_FAST_ACCESS_HOLE_ONE */
    } array;

/**
     * Description of bound function object.
     */
struct
    {
jmem_cpointer_tag_t target_function; /**< target function */
ecma_value_t args_len_or_this; /**< length of arguments or this value */
    } bound_function;

/**
     * Description of implicit class constructor function.
     */
struct
    {
ecma_value_t script_value; /**< script value */
uint8_t flags; /**< constructor flags */
    } constructor_function;
  } u;
} ecma_extended_object_t;
```

简化完毕其实是这样。ecma\_object\_t object和一个union u

其中的object就是上方的通用类型的header，对于复杂类型会使用到ecma\_extended\_object\_t，其中的union u会根据不同的类型选择不同的字段，以此定义不同对象的属性字段。

```
typedef struct
{
ecma_object_t object;

union
  {
struct
    {
uint8_t type;

union {
uint8_t array_buffer_flags;
uint8_t typedarray_type;
      } u1;

union {
uint16_t typedarray_flags;
      } u2;

union {
uint32_t length;
ecma_value_t arraybuffer;
ecma_value_t value;
      } u3;
    } cls;

struct
    {
uint32_t length;
uint32_t length_prop_and_hole_count;
    } array;

struct
    {
jmem_cpointer_tag_t scope_cp;
ecma_value_t bytecode_cp;
    } function;

struct
    {
jmem_cpointer_tag_t target_function;
ecma_value_t args_len_or_this;
    } bound_function;

  } u;
} ecma_extended_object_t;
```

## 类型调试实例

> 下面笔者迁移了部分v8 exploit的知识，通过ai写出了一个针对于jerryscript调试的gdb插件，提升了调试的效率

这里以dataview为例子

```
let ab = new ArrayBuffer(0x100);
let dv = new DataView(...