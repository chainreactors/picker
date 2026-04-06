---
title: frida各模块js与cpp函数分析对照(三)
url: https://mp.weixin.qq.com/s/QxNy7MyCT9jrqxeBXfuOyQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:42:03.478761
---

# frida各模块js与cpp函数分析对照(三)

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnsYwIJhDA7MicbYwicUlmhnwU1hFumv06tCib4OIdWGBnrUr2vl20VCOnHePiaEjibINFGH9pU9R9pF4BqhcibiaT1Bf2QpRue60CwHHo/0?wx_fmt=jpeg)

# frida各模块js与cpp函数分析对照(三)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

* # 官网：http://securitytech.cc

  ![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuSkNPRkjuaPf2NThmBooRdeZ52XpiazERTicv0JAic4CZiblUdhmSExjRiaWMny6SgstgHB2B2pibXcLCyH6ygjrnuQqzRrzuZyrtT0/640?wx_fmt=png&from=appmsg)

  # Module和Memory模块 JavaScript与底层C++函数映射关系分析

  ## 文档概述

  本文档详细分析Frida中Module和Memory模块的JavaScript API与其底层C/C++实现之间的映射关系，涵盖完整的五层架构模型分析。

  ## 五层架构模型分析

  ### 1. 接口定义层 (JavaScript API Layer)

  #### Module模块主要接口：

  #### Memory模块主要接口：

  ### 2. 基础结构层 (GumJS Binding Layer)

  在 `subprojects/frida-gum/bindings/gumjs`目录中，Module和Memory模块的绑定实现在相关文件中。

  #### 关键数据结构

  ```

  ```

  ### 3. 具体实现层 (Platform-specific Implementation)

  #### Module实现 ( `gummodule-*.c`)

  关键函数：

  #### Memory实现 ( `gummemory-*.c`)

  关键函数：

  ### 4. 工厂模式层 (Backend Factory)

  #### Module工厂

  ```

  ```

  #### Memory工厂

  ```

  ```

  ### 5. 应用集成层 (Integration with Frida Core)

  Module和Memory模块通过frida-core与上层应用集成，提供统一的API接口。

  ## 详细函数映射关系表

  ### Module模块映射表

  | JavaScript Function | C++ Function | File Location | Description |
  | --- | --- | --- | --- |
  | `Module.findBaseAddress()` | `gum_module_find_base_address()` | `gummodule-*.c` | 查找模块基地址 |
  | `Module.findExportByName()` | `gum_module_find_export_by_name()` | `gummodule-*.c` | 查找导出符号地址 |
  | `Module.enumerateExports()` | `gum_module_enumerate_exports()` | `gummodule-*.c` | 枚举模块导出符号 |
  | `Module.enumerateImports()` | `gum_module_enumerate_imports()` | `gummodule-*.c` | 枚举模块导入符号 |
  | `Module.enumerateSymbols()` | `gum_module_enumerate_symbols()` | `gummodule-*.c` | 枚举模块所有符号 |
  | `Module.getExports()` | `gum_module_enumerate_exports()` | `gummodule-*.c` | 获取导出符号列表（同步） |

  ### Memory模块映射表

  | JavaScript Function | C++ Function | File Location | Description |
  | --- | --- | --- | --- |
  | `Memory.alloc()` | `gum_memory_alloc()` | `gummemory-*.c` | 分配内存 |
  | `Memory.free()` | `gum_memory_free()` | `gummemory-*.c` | 释放内存 |
  | `Memory.copy()` | `gum_memory_copy()` | `gummemory.c` | 内存复制 |
  | `Memory.protect()` | `gum_memory_protect()` | `gummemory-*.c` | 修改内存保护属性 |
  | `Memory.scan()` | `gum_memory_scan()` | `gummemory.c` | 内存扫描（异步） |
  | `Memory.scanSync()` | `gum_memory_scan_sync()` | `gummemory.c` | 内存扫描（同步） |

  ## 内存布局与数据结构可视化

  ### ExportDetails结构体内存布局

  ```

  ```

  ### ImportDetails结构体内存布局

  ```

  ```

  ### MemoryRange结构体内存布局

  ```

  ```

  ## 系统调用级执行流程追踪

  ### Module.findExportByName()执行流程

  ### Memory.scan()执行流程

  ## 跨平台差异与抽象机制

  ### Module实现差异

  ### Memory实现差异

  ### 抽象层设计

  ```

  ```

  ## 调试命令与安全实践

  ### GDB调试示例

  ```

  ```

  ### 性能优化建议

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

  ### 自定义模块解析

  ```

  ```

  ### 自定义内存工具

  ```

  ```

  ### 底层扩展点

  ## 版本兼容性与演进

  ### API变更历史

  ### 向后兼容性保证

  ## 实战案例分析

  ### 案例1: 动态API解析

  ```

  ```

  ### 案例2: 内存特征码扫描

  ```

  ```

  ### 案例3: 模块依赖分析

  ```

  ```

  ## 总结与最佳实践

  Module和Memory模块是Frida中最核心的功能模块，提供了对目标进程二进制结构和内存空间的全面访问能力。理解其JS与C++的映射关系有助于：

  通过本文档的五层架构分析，开发者可以全面掌握Module和Memory模块的工作原理和使用技巧，为复杂的动态分析任务提供坚实的基础。

+ 核心API保持稳定
+ 新功能通过扩展方式添加
+ 废弃的API会标记并提供迁移路径

+ **Frida早期版本**: 基本的模块和内存操作
+ **Frida 10.x**: 添加完整的符号枚举功能
+ **Frida 12.x**: 优化内存扫描性能，添加异步API
+ **Frida 14.x**: 改进跨平台兼容性和错误处理

+ 可以通过修改 `gummodule-*.c`添加新的模块解析功能
+ 通过修改 `gummemory-*.c`添加新的内存操作原语
+ 扩展GumModule和GumMemory结构体添加新方法

+ **Module操作**: 符号枚举会为每个符号分配ExportDetails结构体
+ **Memory操作**: 扫描会分配临时缓冲区和结果数组
+ **优化建议**: 使用流式API避免一次性加载大量数据

+ **Module操作**:
+ `findExportByName()`: O(n)，n为导出符号数量
+ `enumerateExports()`: O(n)，需要遍历所有导出符号
+ `getExports()`: O(n)，同上但返回完整列表
+ **Memory操作**:
+ `alloc()/free()`: O(1)，系统调用开销
+ `scan()`: O(size/pattern\_length)，线性扫描
+ `protect()`: O(1)，系统调用开销

+ **直接系统调用**: 绕过Module API直接解析二进制
+ **内存加密**: 隐藏恶意代码和数据
+ **动态加载**: 运行时加载和解析模块

+ **API Hook检测**: 监控关键导出函数的地址变化
+ **内存扫描检测**: 检测可疑的内存扫描行为
+ **模块完整性验证**: 验证关键模块的导出表完整性

+ **Module错误**:
+ 模块不存在：返回null
+ 符号不存在：返回null
+ 权限不足：无法读取模块信息
+ **Memory错误**:
+ 无效地址：访问违规
+ 内存不足：分配失败
+ 保护冲突：无法修改保护属性

+ **Module缓存**: 缓存常用的模块和符号查找结果
+ **Memory批量操作**: 避免频繁的小内存分配
+ **扫描优化**: 使用更精确的模式减少扫描范围

+ **Darwin**: 使用 `mach_vm_allocate()`、 `mach_vm_deallocate()`、 `mach_vm_protect()`
+ **Linux**: 使用 `mmap()`、 `munmap()`、 `mprotect()`
+ **Windows**: 使用 `VirtualAlloc()`、 `VirtualFree()`、 `VirtualProtect()`

+ **Darwin (Mach-O)**:
+ 使用 `_dyld_get_image_header()`获取镜像头
+ 解析LC*SYMTAB、LC*DYSYMTAB等加载命令
+ 支持懒绑定和非懒绑定符号
+ **Linux (ELF)**:
+ 解析程序头表(PT\_DYNAMIC)
+ 处理.dynsym、.dynstr段
+ 支持PLT/GOT机制
+ **Windows (PE)**:
+ 解析IMAGE*NT*HEADERS
+ 处理导出目录表
+ 支持转发器(forwarder)功能

+ **Darwin**: 解析Mach-O的LC\_SYMTAB加载命令
+ **Linux**: 解析ELF的.dynamic段和符号表
+ **Windows**: 解析PE的导出表

+ `gum_memory_alloc()`
+ `gum_memory_free()`
+ `gum_memory_copy()`
+ `gum_memory_protect()`
+ `gum_memory_scan()`

+ **通用实现**: `gummemory.c` - 跨平台内存操作
+ **Darwin特定**: `gummemory-darwin.c` - 使用Mach VM API
+ **Linux特定**: `gummemory-linux.c` - 使用mmap/mprotect

+ `gum_module_find_base_address()`
+ `gum_module_find_export_by_name()`
+ `gum_module_enumerate_exports()`
+ `gum_module_enumerate_imports()`
+ `gum_module_enumerate_symbols()`

+ **Darwin**: `gummodule-darwin.c` - 使用Mach-O解析
+ **Linux**: `gummodule-linux.c` - 使用ELF解析
+ **Windows**: `gummodule-windows.c` - 使用PE解析

+ `Memory.alloc(size)`
+ `Memory.copy(dst,src,n)`
+ `Memory.dup(address,size)`
+ `Memory.protect(address,size,protection)`
+ `Memory.scan(address,size,pattern,callbacks)`
+ `Memory.scanSync(address,size,pattern)`
+ `Memory.allocUtf8String(str)`
+ `Memory.allocAnsiString(str)`
+ `Memory.allocUtf16String(str)`

+ `Module.load(name)`
+ `Module.ensureInitialized(name)`
+ `Module.findBaseAddress(name)`
+ `Module.findExportByName(module,symbol)`
+ `Module.getExports()`
+ `Module.getImports()`
+ `Module.getSymbolByName(module,symbol)`
+ `Module.enumerateExports(module)`
+ `Module.enumerateImports(module)`
+ `Module.enumerateSymbols(module)`
+ `Module.enumerateRanges(module,protection)`

1. **二进制分析**: 深入理解目标应用的模块结构和依赖关系
2. **内存操作**: 精确控制和监控目标进程的内存使用
3. **API Hook**: 基于符号信息实现精准的函数Hook
4. **安全检测**: 利用模块和内存信息进行深度安全分析

1. `// 分析模块的导入依赖`
2. `function analyzeModuleImports(moduleName){`
3. `` console.log(`Analyzing imports for ${moduleName}:`); ``
4. `Module.enumerateImports(moduleName,{`
5. `onMatch:function(importDetails){`
6. `` console.log(`  ${importDetails.name} from ${importDetails.module}`); ``
7. `},`
8. `onComplete:function(){`
9. `console.log('Import analysis completed');`
10. `}`
11. `});`
12. `}`
14. `analyzeModuleImports('libcrypto.so');`

1. `// 扫描内存中的特定字节序列`
2. `const pattern ='48 89 ?? ?? ?? 48 8b ?? ?? ?? ?? ??';`
3. `const base =Module.findBaseAddress('libtarget.so');`
4. `const size =0x100000;// 1MB扫描范围`
6. `Memory.scan(base, size, pattern,{`
7. `onMatch:function(address, size){`
8. `console.log('Found pattern at:', address);`
9. `// 进一步分析找到的地址`
10. `},`
11. `onError:function(reason){`
12. `console.error('Scan error:', reason);`
13. `},`
14. `onComplete:function(){`
15. `console.log('Scan completed');`
16. `}`
17. `});`

1. `// 动态解析和调用Windows API`
2. `const kernel32 =Module.findBaseAddress('kernel32.dll');`
3. `const loadLibraryAddr =Module.findExportByName('kernel32.dll','LoadLibraryA');`
5. `if(loadLibraryAddr){`
6. `constLoadLibrary=newNativeFunction(loadLibraryAddr,'pointer',['pointer']);`
7. `const libName =Memory.allocUtf8String('user32.dll');`
8. `const user32Handle =LoadLibrary(libName);`
9. `console.log('Loaded user32.dll:', user32Handle);`
10. `}`

1. `// 内存区域保护监控`
2. `Memory.monitorProtectionChanges =function(address, size, callback){`
3. `const originalProtection =Memory.queryProtection(address);`
4. `// 定期检查保护属性变化`
5. `const interval = setInterval(()=>{`
6. `const currentProtection =Memory.queryProtection(address);`
7. `if(curr...