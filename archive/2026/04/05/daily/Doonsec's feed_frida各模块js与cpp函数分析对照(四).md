---
title: frida各模块js与cpp函数分析对照(四)
url: https://mp.weixin.qq.com/s/GAZE6upaghL4u4OlXfL5xA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:42:08.082652
---

# frida各模块js与cpp函数分析对照(四)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnu8mgBgqlQKn1lB3eJQFBWWDL2iap0PAhdC6OqKVJNlialeUFL6HcdjJsZINEq2NKoNRtVUH0JgTDXJ9Oick9bfJuhD1MENXXWVzs/0?wx_fmt=jpeg)

# frida各模块js与cpp函数分析对照(四)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

* # 官网：http://securitytech.cc

  ![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuSkNPRkjuaPf2NThmBooRdeZ52XpiazERTicv0JAic4CZiblUdhmSExjRiaWMny6SgstgHB2B2pibXcLCyH6ygjrnuQqzRrzuZyrtT0/640?wx_fmt=png&from=appmsg)

  # Native数据类型 JavaScript与底层C++函数映射关系分析

  ## 文档概述

  本文档详细分析Frida中NativePointer、NativeFunction、NativeCallback、Int64、UInt64等Native数据类型的JavaScript API与其底层C/C++实现之间的映射关系，涵盖完整的五层架构模型分析。

  ## 五层架构模型分析

  ### 1. 接口定义层 (JavaScript API Layer)

  #### NativePointer主要接口：

  #### NativeFunction主要接口：

  #### NativeCallback主要接口：

  #### Int64/UInt64主要接口：

  #### ArrayBuffer主要接口：

  ### 2. 基础结构层 (GumJS Binding Layer)

  在 `subprojects/frida-gum/bindings/gumjs`目录中，Native数据类型的绑定实现在相关文件中。

  #### 关键数据结构

  ```

  ```

  ### 3. 具体实现层 (Platform-specific Implementation)

  #### NativePointer实现 ( `gumjs-native-pointer.c`)

  #### NativeFunction实现 ( `gumjs-native-function.c`)

  #### NativeCallback实现 ( `gumjs-native-callback.c`)

  #### Int64/UInt64实现 ( `gumjs-int64.c`, `gumjs-uint64.c`)

  ### 4. 工厂模式层 (Backend Factory)

  #### 类型系统工厂

  ```

  ```

  #### 内存管理工厂

  ```

  ```

  ### 5. 应用集成层 (Integration with Frida Core)

  Native数据类型通过frida-core与上层应用集成，提供统一的API接口，并与QuickJS/V8引擎深度集成。

  ## 详细函数映射关系表

  ### NativePointer映射表

  | JavaScript Method | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `add()` | `gumjs_native_pointer_add()` | `gumjs-native-pointer.c` | 指针加法运算 |
  | `sub()` | `gumjs_native_pointer_sub()` | `gumjs-native-pointer.c` | 指针减法运算 |
  | `readU8()` | `gumjs_native_pointer_read_u8()` | `gumjs-native-pointer.c` | 读取8位无符号整数 |
  | `writeU8()` | `gumjs_native_pointer_write_u8()` | `gumjs-native-pointer.c` | 写入8位无符号整数 |
  | `readPointer()` | `gumjs_native_pointer_read_pointer()` | `gumjs-native-pointer.c` | 读取指针值 |
  | `writePointer()` | `gumjs_native_pointer_write_pointer()` | `gumjs-native-pointer.c` | 写入指针值 |

  ### NativeFunction映射表

  | JavaScript Constructor | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `newNativeFunction()` | `gumjs_native_function_construct()` | `gumjs-native-function.c` | 构造NativeFunction对象 |
  | Function call | `gumjs_native_function_invoke()` | `gumjs-native-function.c` | 调用原生函数 |

  ### NativeCallback映射表

  | JavaScript Constructor | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `newNativeCallback()` | `gumjs_native_callback_construct()` | `gumjs-native-callback.c` | 构造NativeCallback对象 |
  | Callback invocation | `gumjs_native_callback_on_invoke()` | `gumjs-native-callback.c` | 处理回调调用 |

  ### Int64/UInt64映射表

  | JavaScript Method | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `newInt64()` | `gumjs_int64_construct()` | `gumjs-int64.c` | 构造Int64对象 |
  | `add()` | `gumjs_int64_add()` | `gumjs-int64.c` | 64位整数加法 |
  | `toString()` | `gumjs_int64_to_string()` | `gumjs-int64.c` | 转换为字符串 |
  | `newUInt64()` | `gumjs_uint64_construct()` | `gumjs-uint64.c` | 构造UInt64对象 |

  ## 内存布局与数据结构可视化

  ### GumNativePointer结构体内存布局

  ```

  ```

  ### GumNativeFunction结构体内存布局

  ```

  ```

  ### GumNativeCallback结构体内存布局

  ```

  ```

  ### GumInt64/GumUInt64结构体内存布局

  ```

  ```

  ## 系统调用级执行流程追踪

  ### NativeFunction调用执行流程

  ### NativeCallback调用执行流程

  ### NativePointer内存读写流程

  ## 跨平台差异与抽象机制

  ### ABI差异处理

  ### 指针大小差异

  ### 字节序处理

  ### 抽象层设计

  ```

  ```

  ## 调试命令与安全实践

  ### GDB调试示例

  ```

  ```

  ### 安全考虑

  ## 错误处理与边界情况

  ### 常见错误场景

  ### 最佳实践

  ```

  ```

  ## 攻击检测场景映射

  ### 可用于检测的场景

  ### 防御绕过技术

  ## 性能分析与优化

  ### 时间复杂度分析

  ### 内存使用分析

  ## 扩展功能与自定义实现

  ### 自定义NativeFunction包装器

  ```

  ```

  ### 自定义内存访问工具

  ```

  ```

  ### 底层扩展点

  ## 版本兼容性与演进

  ### API变更历史

  ### 向后兼容性保证

  ## 实战案例分析

  ### 案例1: Windows API调用

  ```

  ```

  ### 案例2: 回调函数注册

  ```

  ```

  ### 案例3: 内存数据分析

  ```

  ```

  ### 案例4: 64位地址处理

  ```

  ```

  ## 总结与最佳实践

  Native数据类型是Frida连接JavaScript世界和原生代码世界的桥梁，提供了强大的底层操作能力。理解其JS与C++的映射关系有助于：

  通过本文档的五层架构分析，开发者可以全面掌握Native数据类型的工作原理和使用技巧，为复杂的动态分析任务提供坚实的基础。

+ 核心API保持稳定
+ 新功能通过扩展方式添加
+ 废弃的API会标记并提供迁移路径

+ **Frida早期版本**: 基本的NativePointer和NativeFunction
+ **Frida 8.x**: 添加NativeCallback支持
+ **Frida 10.x**: 完善Int64/UInt64支持
+ **Frida 12.x**: 优化ABI处理和性能
+ **Frida 14.x**: 改进错误处理和跨平台兼容性

+ 可以通过修改 `gumjs-native-function.c`添加新的ABI支持
+ 通过修改 `gumjs-native-pointer.c`添加新的内存操作原语
+ 扩展类型系统支持更多数据类型

+ **NativeFunction**: 每个实例占用固定内存，参数转换需要临时缓冲区
+ **NativeCallback**: 需要分配回调桩内存和上下文结构体
+ **优化建议**: 重用NativeFunction实例，避免频繁创建

+ **NativePointer操作**: O(1)，直接内存访问
+ **NativeFunction调用**: O(n)，n为参数数量（参数转换开销）
+ **NativeCallback调用**: O(n)，n为参数数量（双向转换开销）
+ **Int64/UInt64操作**: O(1)，64位整数运算

+ **直接汇编**: 绕过NativeFunction直接执行机器码
+ **内存加密**: 隐藏NativePointer指向的数据
+ **动态代码生成**: 运行时生成和执行代码

+ **API调用监控**: 通过NativeFunction监控关键API调用
+ **回调函数分析**: 分析NativeCallback的使用模式
+ **内存访问模式**: 监控NativePointer的内存访问行为

+ **NativePointer错误**:
+ 无效地址访问：段错误或访问违规
+ 地址对齐错误：某些平台要求对齐访问
+ 权限不足：无法读写受保护内存
+ **NativeFunction错误**:
+ 函数地址无效：调用失败
+ 参数类型不匹配：未定义行为
+ ABI不匹配：栈损坏或参数错误
+ **NativeCallback错误**:
+ JavaScript异常：需要正确处理和传播
+ 线程安全问题：多线程环境下回调冲突
+ 内存泄漏：回调对象未正确释放

+ **内存访问安全**: NativePointer读写需要验证地址有效性
+ **类型安全**: NativeFunction参数类型必须严格匹配
+ **回调安全**: NativeCallback需要处理异常和线程安全

+ **小端序平台** (x86, x86\_64, ARM): 直接内存访问
+ **大端序平台** (某些PowerPC, MIPS): 需要字节序转换

+ **64位平台**: GumAddress = uint64\_t
+ **32位平台**: GumAddress = uint32\_t
+ **统一接口**: 通过GumAddress类型抽象

+ **x86\_64**: System V ABI (Unix) vs Microsoft x64 ABI (Windows)
+ **ARM64**: AAPCS64调用约定
+ **ARM**: AAPCS调用约定
+ **MIPS**: O32/N32/N64 ABI

+ 64位整数运算
+ 与32位系统的兼容性处理
+ 字符串转换和格式化

+ 回调函数桩生成
+ JavaScript到C的参数转换
+ C到JavaScript的返回值转换
+ 线程安全处理

+ 函数调用约定处理
+ 参数类型转换
+ 返回值处理
+ ABI特定实现（不同平台的调用约定）

+ 指针算术运算实现
+ 内存读写操作实现
+ 与不同数据类型的转换

+ 标准JavaScript ArrayBuffer API
+ Frida扩展的内存读写功能

+ `newInt64(value)`
+ `newUInt64(value)`
+ 各种算术和位操作方法
+ 与NativePointer的相互转换

+ `newNativeCallback(func,returnType,argTypes[,abi])`
+ 返回可被原生代码调用的回调函数指针

+ `newNativeFunction(address,returnType,argTypes[,options])`
+ 调用函数实例执行原生函数

+ `newNativePointer(value)`
+ `NativePointer.prototype.add(rhs)`
+ `NativePointer.prototype.sub(rhs)`
+ `NativePointer.prototype.and(mask)`
+ `NativePointer.prototype.or(mask)`
+ `NativePointer.prototype.xor(mask)`
+ `NativePointer.prototype.shl(shift)`
+ `NativePointer.prototype.shr(shift)`
+ `NativePointer.prototype.equals(rhs)`
+ `NativePointer.prototype.compare(rhs)`
+ `NativePointer.prototype.toInt32()`
+ `NativePointer.prototype.toString([radix])`
+ `NativePointer.prototype.readU8()`, `readS8()`, `readU16()`, etc.

1. **精确控制**: 对原生函数和内存进行精确的控制和操作
2. **性能优化**: 避免不必要的类型转换和内存分配
3. **安全分析**: 利用Native数据类型进行深度的安全检测
4. **跨平台开发**: 理解不同平台的ABI差异和处理方式

1. `// 处理64位地址（在32位JS环境中）`
2. `const largeAddress =newUInt64('0x123456789abcdef0');`
3. `const ptr =newNativePointer(largeAddress);`
5. `// 执行指针运算`
6. `const offsetPtr = ptr.add(newUInt64('0x1000'));`
7. `console.log('Offset pointer:', offsetPtr.toString(16));`
9. `// 读取内存`
10. `const value = offsetPtr.readU64();`
11. `console.log('Memory value:', value.toString(16));`

1. `// 分析结构体数据`
2. `const structPtr =newNativePointer(0x12345678);`
4. `// 读取结构体字段（假设结构体包含int32、指针、int64）`
5. `const field1 = structPtr.readS32();// 第一个字段：32位整数`
6. `const field2 = structPtr.add(4).readPointer();// 第二个字段：指针`
7. `const field3 = structPtr.add(12).readS64();// 第三个字段：64位整数`
9. `console.log('Struct fields:', field1, field2, field3.toString());`

1. `// 注册信号处理回调`
2. `const libc =Module.findBaseAddress('libc.so');`
3. `const signalAddr =Module.findExportByName('libc.so','signal');`
5. `if(signalAddr){`
6. `const signalFunc =newNativeFunction(signalAddr,'pointer',['int','pointer']);`
8. `// 创建信号处理回调`
9. `const sigHandler =newNativeCallback(function(sig){`
10. `console.log('Received signal:', sig);`
11. `return0;`
12. `},'i...