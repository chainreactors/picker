---
title: DEX文件格式解析：深入Android字节码结构
url: https://mp.weixin.qq.com/s/dcfIULrX-rrN8U6fn1MBIg
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:21:35.678598
---

# DEX文件格式解析：深入Android字节码结构

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EhX3LXAfz6BiaBJjnTttFFF8L5oCzNHBM1ytIp9BH5KjGg3uiaV3Q4cYqnqkDTibPsrF3Pr98XtnnEA/0?wx_fmt=jpeg)

# DEX文件格式解析：深入Android字节码结构

A0tem

看雪学苑

![]()

在小说阅读器中沉浸阅读

**0****1**

**大体框架**

# Dex（Dalvik Executable）是Android系统中Java字节码的优化格式，相比传统的class文件，Dex具有更高的执行效率和更小的文件体积。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FL7MoKHMeXy5Rzia8UOlUYUV31rVHNXjIGeCcATaf8DKlcguHnR2WXQZyKQHWDLvKpJyW758TGRzQ/640?wx_fmt=png&from=appmsg)![]()

Dex文件整体架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FL7MoKHMeXy5Rzia8UOlUYUMJnCV4oJPUwJCic0wTUD7KnfozKPfbzia4khHibnuKWszTfSLqTer2tAQ/640?wx_fmt=png&from=appmsg)

Dex文件采用索引+数据的分离设计，所有索引区在前，实际数据在后。这种设计优化了内存访问和加载速度。

```
文件偏移    区域名称           作用
0x00       dex_header        文件头信息
0x70       string_ids        字符串索引表
...       type_ids          类型索引表
...       proto_ids         方法原型索引表
...       field_ids         字段索引表
...       method_ids        方法索引表
...       class_defs        类定义表
...       call_site_ids     调用点索引表(API 26+)
...       method_handles    方法句柄表(API 26+)
...       data              实际数据区
...       link_data         链接数据(可选)
```

#

**02**

**数据类型**

下面是解析Dex结构可能用到的数据类型。

Android源码  定义了dex文件用到的数据结构：

| 自定义类型 | 原类型 | 含义 |
| --- | --- | --- |
| s1 | int8\_t | 有符号单字节 |
| u1 | uint8\_t | 无符号单字节 |
| s2 | int16\_t |  |
| u2 | uint16\_t |  |
| s4 | int32\_t |  |
| u4 | uint32\_t |  |
| s8 | int64\_t |  |
| u8 | uint64\_t |  |
| sleb128 | 无 | 有符号LEB128,可变长度 |
| uleb128 | 无 | 无符号LEB128,可变长度 |
| uleb128p1 | 无 | 等于ULEB128加1,可变长度 |

## LEB128

sleb128、uleb128、uleb128p1是**Dex文件中特有的LEB128类型**.在下述Android源码位置可以找到LEB128的实现。

sleb128:有符号LEB128

uleb128:无符号LEB128

uleb128p1:uleb128+1

每个LEB128由1-5字节组成,所有字节组合在一起表示一个32位的数据, 每个字节只有**低7位为有效位**,**最高位标识是否需要使用额外字节。**

如果第1个字节的最高位为1,表示LEB128需要使用第2个字节,如果第2个字节的最高位为1,表示会使用第3个字节,依次类推,直到最后一个字节的最高位为0

uleb128读取代码如下：

值得注意的是参数为二级指针,也就是说,调用该函数时会移动一级指针,一级指针的偏移量即为读取到的uleb128的大小。

```
intreadUnsignedLeb128(const u1** pStream) {
const u1* ptr = *pStream;   //初始化
int result = *(ptr++);      //获取第一个字节

if (result > 0x7f) {        //如果第一个字节大于0x7f，那么就还有第二个字节
int cur = *(ptr++);     //第二个字节
        result = (result & 0x7f) | ((cur & 0x7f) << 7); //把两个字节合并
if (cur > 0x7f) {       //继续处理
            cur = *(ptr++);
            result |= (cur & 0x7f) << 14;
if (cur > 0x7f) {
                cur = *(ptr++);
                result |= (cur & 0x7f) << 21;
if (cur > 0x7f) {
/*
                     * Note: We don't check to see if cur is out of
                     * range here, meaning we tolerate garbage in the
                     * high four-order bits.
                     */
                    cur = *(ptr++);
                    result |= cur << 28;
                }
            }
        }
    }

    *pStream = ptr;
return result;
}
```

将LEB128编码的字节序列解码为32位无符号整数。

合并两个字节的操作十分巧妙:

```
步骤1：result & 0x7f
result = 0xAC = 1010 1100
0x7f   = 0x7F = 0111 1111
result & 0x7f = 0010 1100 = 0x2C = 44
作用：去掉第一个字节的继续标志，只保留数据位

步骤2：cur & 0x7f
cur = 0x02 = 0000 0010
0x7f = 0x7F = 0111 1111
cur & 0x7f = 0000 0010 = 0x02 = 2
作用：去掉第二个字节的继续标志（虽然本来就是0）

步骤3：(cur & 0x7f) << 7
(cur & 0x7f) = 2 = 0000 0010
左移7位后 = 0000 0010 0000 0000 = 256
作用：将第二个字节的数据放到正确的位置（bit 7-13）

步骤4：最终合并

(result & 0x7f) = 44  =        0000 0000 0010 1100
((cur & 0x7f) << 7) = 256 =    0000 0001 0000 0000
─────────────────────
最终result = 44 | 256 = 300 =  0000 0001 0010 1100
```

## encode\_value

encoded\_value是Dex文件中用于**存储常量值**的通用编码格式。它可以表示各种类型的常量数据，如数字、字符串、类型引用等。

1. 注解参数值：@MyAnnotation(name="test", value=42)
2. 静态字段初始值：public static final String TAG = "MyClass"
3. 数组常量：public static final int[] NUMBERS = {1,2,3}

```
// encoded_value不是固定结构体，而是变长的数据格式
// 由头字节 + 可变长度数据组成

struct encoded_value {
    u1 type_and_arg;        // 头字节：(value_arg << 5) | value_type
    u1 data[];              // 可变长度数据，根据类型和参数决定长度
};
```

### 编码结构解析

头字节解析(1字节)

```
// 格式：(value_arg << 5) | value_type
// 位布局：AAA TTTTT
// A = value_arg（高3位，0-7）
// T = value_type（低5位，0-31）

u1header = (value_arg << 5) | value_type;

// 解析方式
u1value_type = header & 0x1F;        // 提取低5位
u1value_arg = (header >> 5) & 0x07;  // 提取高3位
```

value\_type含义(低五位)

指定数据的类型格式：

```
#define VALUE_BYTE          0x00    // 字节值
#define VALUE_SHORT         0x02    // 短整型
#define VALUE_CHAR          0x03    // 字符
#define VALUE_INT           0x04    // 整型
#define VALUE_LONG          0x06    // 长整型
#define VALUE_FLOAT         0x10    // 浮点数
#define VALUE_DOUBLE        0x11    // 双精度浮点数
#define VALUE_METHOD_TYPE   0x15    // 方法类型
#define VALUE_METHOD_HANDLE 0x16    // 方法句柄
#define VALUE_STRING        0x17    // 字符串索引
#define VALUE_TYPE          0x18    // 类型索引
#define VALUE_FIELD         0x19    // 字段索引
#define VALUE_METHOD        0x1A    // 方法索引
#define VALUE_ENUM          0x1B    // 枚举值
#define VALUE_ARRAY         0x1C    // 数组
#define VALUE_ANNOTATION    0x1D    // 注解
#define VALUE_NULL          0x1E    // null值
#define VALUE_BOOLEAN       0x1F    // 布尔值
```

value\_arg函数(高3位)

根据类型不同，含义不同：

对于数值类型：value\_arg = 字节数 - 1

```
// 整数42只需1字节存储
value_arg = 1 - 1 = 0

// 整数65536需要3字节存储
value_arg = 3 - 1 = 2
```

对于布尔类型：value\_arg直接表示值

```
// true: value_arg = 1
// false: value_arg = 0
```

对于索引类型(STRING、TYPE、FIELD、METHOD)

value\_arg = 索引字节数 - 1

```
// 字符串索引15，需要1字节
value_type = VALUE_STRING (0x17)
value_arg = 1 - 1 = 0
header = (0 << 5) | 0x17 = 0x17

// 字符串索引300，需要2字节
value_type = VALUE_STRING (0x17)
value_arg = 2 - 1 = 1
header = (1 << 5) | 0x17 = 0x37
```

对于特殊类型(NULL,ARRAY等)

value\_arg通常为0或有特殊含义

```
// NULL值
value_type = VALUE_NULL (0x1E)
value_arg = 0  // 固定为0
header = (0 << 5) | 0x1E = 0x1E

// 数组
value_type = VALUE_ARRAY (0x1C)
value_arg = 0  // 固定为0，大小用uleb128单独编码
header = (0 << 5) | 0x1C = 0x1C
```

## encoded\_array

encoded\_array是Dex文件中用于存储数组常量的数据结构，主要用于：

1. 静态字段初始值数组
2. 注解参数中的数组值
3. 枚举值列表

数据结构定义:

```
encoded_array {
uleb128size;              // 数组元素个数
encoded_valuevalues[];    // 数组元素，每个都是encoded_value
}
```

| 名称 | 格式 | 说明 |
| --- | --- | --- |
| size | uleb128 | 数组中的元素数量 |
| values | encoded\_value[size] | 采用本部分所指定格式的一系列`size`<br/>`encoded_value`<br/> 字节序列；依序串联。 |

由于encoded\_array.values数组元素为encoded\_value,所以每个元素的大小不固定,不能当作一般的数组解析。

## encoded\_annotation

encoded\_annotation是Dex文件中用于**存储注解实例**的数据结构，它表示一个具体的注解及其参数值。

```
encoded_annotation {
uleb128type_idx;                    // 注解类型的type_ids索引
uleb128size;                        // 注解元素个数
annotation_elementelements[];       // 注解元素数组
}

annotation_element {
uleb128name_idx;                    // 元素名称的string_ids索引
encoded_valuevalue;                 // 元素值
}
```

该类型主要在DexClassDef的Annotations部分使用,此处仅做介绍。

| 名称 | 格式 | 说明 |
| --- | --- | --- |
| type\_idx | uleb128 | 注释的类型。这种类型必须是“类”（而非“数组”或“基元”）。 |
| size | uleb128 | 此注解中 name-value 映射的数量 |
| elements | annotation\_element[size] | 注解的元素，直接以内嵌形式（不作为偏移量）表示。元素必须按`string_id`<br/> 索引以升序进行排序。 |

注解是什么?

```
@Override// 这是注解
public String toString() {
return "MyClass";
}

@MyAnnotation(value = "test", count = 42)  // 带参数的注解
public class MyClass {

@Nullable// 标记可能为null
private String name;

@Inject// 依赖注入标记
private UserService userService;
}
```

特点：

* 编译后保留在字节码中
* 程序运行时可以读取和处理
* 影响程序的实际行为
* 可以携带参数和数据

#

**03**

**文件头**

官方好像不支持头文件，所以我们需要手搓或者偷一个，这里直接去安卓源码copy一下

https://android.googlesource.com/platform/dalvik/+/refs/heads/master/libdex/DexFile.h

https://android.googlesource.com/platform/art/+/refs/heads/master/libdexfile/dex/dex\_file.h

copy之后还需要修改，让ai来即可。

```
struct dex_header {
// 文件标识部分
uint8_t  magic[8];           // "dex\n035\0" 魔数标识
uint32_t checksum;           // 文件完整性校验
uint8_t  signature[20];      // SHA-1数字签名

// 文件基本信息
uint32_t file_size;          // 整个dex文件大小
uint32_t header_size;        // 头部大小(固定0x70)
uint32_t endian_tag;         // 字节序标记

// 链接信息
uint32_t link_size;          // 链接段大小
uint32_t link_off;           // 链接段偏移
uint32_t map_off;            // 映射表偏移

// 各索引区的大小和位置
uint32_t string_ids_size;    // 字符串数量
uint32_t string_ids_off;     // 字符串索引偏移
uint32_t type_ids_size;      // 类型数量
uint32_t type_ids_off;       // 类型索引偏移...