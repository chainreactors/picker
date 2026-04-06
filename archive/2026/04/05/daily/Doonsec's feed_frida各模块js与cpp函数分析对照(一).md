---
title: frida各模块js与cpp函数分析对照(一)
url: https://mp.weixin.qq.com/s/U01CpqpFfHuvZ6LWbe2KOA
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:41:56.939872
---

# frida各模块js与cpp函数分析对照(一)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnvEFLJVer61ZIuLlnoUko9tiayX00CmQqiaBLvEpMntdlReslVuMPMNibWN4Znbg52s0j2yiasMyFqhicnQIvG8tkSIibcj3Ij8Kt1hM/0?wx_fmt=jpeg)

# frida各模块js与cpp函数分析对照(一)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

# 官网：http://securitytech.cc

![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuSkNPRkjuaPf2NThmBooRdeZ52XpiazERTicv0JAic4CZiblUdhmSExjRiaWMny6SgstgHB2B2pibXcLCyH6ygjrnuQqzRrzuZyrtT0/640?wx_fmt=png&from=appmsg)

#

# Process模块 JavaScript与底层C++函数映射关系分析

## 文档概述

本文档详细分析Frida中Process模块的JavaScript API与其底层C/C++实现之间的映射关系，涵盖完整的五层架构模型分析。

## 五层架构模型分析

### 1. 接口定义层 (JavaScript API Layer)

Process模块提供的主要JavaScript接口包括：

* `Process.arch`
* `Process.platform`
* `Process.pageSize`
* `Process.pointerSize`
* `Process.setExceptionHandler(callback)`
* `Process.getCurrentThreadId()`
* `Process.enumerateModules()`
* `Process.enumerateRanges(protection)`
* `Process.enumerateMallocRanges()`
* `Process.findModuleByName(name)`
* `Process.getModuleByAddress(address)`
* `Process.queryMemory(address)`

### 2. 基础结构层 (GumJS Binding Layer)

在 `subprojects/frida-gum/bindings/gumjs`目录中，Process模块的绑定实现在相关文件中。

#### 关键数据结构

```
1. // GumScriptBackend中的Process相关结构
2. typedefstruct_GumProcessApi{
3. // 枚举模块的回调函数定义
4. gboolean (* enumerate_modules)(GumFoundModuleFunc func, gpointer user_data);
5. gboolean (* enumerate_ranges)(const gchar * protection,GumFoundRangeFunc func, gpointer user_data);
6. // ... 其他函数指针
7. }GumProcessApi;
```

### 3. 具体实现层 (Platform-specific Implementation)

不同平台的具体实现在 `subprojects/frida-gum/gum/backend-*`目录中。

#### Darwin平台实现 ( `gumprocess-darwin.c`)

* `gum_process_enumerate_modules()`
* `gum_process_enumerate_ranges()`
* `gum_process_find_module_by_name()`
* `gum_process_query_memory()`

#### Linux/Android平台实现 ( `gumprocess-linux.c`)

* 类似的函数实现，但使用不同的系统调用

### 4. 工厂模式层 (Backend Factory)

通过工厂模式创建不同平台的Process实现：

```
1. // gum_process_backend_create()
2. GumProcessBackend*
3. gum_process_backend_create (void)
4. {
5. #ifdef HAVE_DARWIN
6. return gum_darwin_process_backend_new ();
7. #elif defined(HAVE_LINUX)
8. return gum_linux_process_backend_new ();
9. // ... 其他平台
10. #endif
11. }
```

### 5. 应用集成层 (Integration with Frida Core)

Process模块通过frida-core与上层应用集成，提供统一的API接口。

## 详细函数映射关系表

| JavaScript Function | C++ Function | File Location | Description |
| --- | --- | --- | --- |
| `Process.enumerateModules()` | `gum_process_enumerate_modules()` | `gumprocess-*.c` | 枚举进程中加载的所有模块 |
| `Process.enumerateRanges()` | `gum_process_enumerate_ranges()` | `gumprocess-*.c` | 枚举指定保护属性的内存范围 |
| `Process.findModuleByName()` | `gum_process_find_module_by_name()` | `gumprocess-*.c` | 根据模块名查找模块信息 |
| `Process.getModuleByAddress()` | `gum_process_get_module_by_address()` | `gumprocess-*.c` | 根据地址查找所属模块 |
| `Process.queryMemory()` | `gum_process_query_memory()` | `gumprocess-*.c` | 查询指定地址的内存信息 |
| `Process.getCurrentThreadId()` | `gum_process_get_current_thread_id()` | `gumprocess-*.c` | 获取当前线程ID |

## 内存布局与数据结构可视化

### ModuleInfo结构体内存布局

```
1. +------------------+
2. | name (char*)|->模块名称字符串
3. +------------------+
4. |base(GumAddress)|->模块基地址
5. +------------------+
6. | size (gsize)|->模块大小
7. +------------------+
8. | path (char*)|->模块完整路径
9. +------------------+
```

### RangeInfo结构体内存布局

```
1. +------------------+
2. |base(GumAddress)|->内存范围起始地址
3. +------------------+
4. | size (gsize)|->内存范围大小
5. +------------------+
6. | protection (int)|->内存保护属性
7. +------------------+
```

## 系统调用级执行流程追踪

### Process.enumerateModules()执行流程

1. JavaScript调用 → GumJS绑定层
2. 调用 `gum_process_enumerate_modules()`
3. 平台特定实现（Darwin: `_dyld_image_count()`, `_dyld_get_image_name()`等）
4. 回调函数逐个处理每个模块
5. 结果转换为JavaScript对象返回

### 内存查询流程

1. JavaScript调用 `Process.queryMemory(address)`
2. 调用 `gum_process_query_memory(address)`
3. Darwin平台：使用 `vm_region_64()`系统调用
4. Linux平台：解析 `/proc/self/maps`
5. 返回内存区域信息

## 跨平台差异与抽象机制

### Darwin vs Linux实现差异

* **Darwin**: 使用Mach-O相关的API和 `vm_region`系列函数
* **Linux**: 解析 `/proc`文件系统和ELF相关API
* **Windows**: 使用PEB和VirtualQuery系列函数

### 抽象层设计

通过统一的函数指针表和工厂模式，隐藏平台差异：

```
1. struct_GumProcessBackend
2. {
3. GObject parent;

5. /* Platform-specific methods */
6. gboolean (* enumerate_modules)(GumProcessBackend* self,GumFoundModuleFunc func, gpointer user_data);
7. gboolean (* enumerate_ranges)(GumProcessBackend* self,const gchar * protection,GumFoundRangeFunc func, gpointer user_data);
8. // ... 其他方法
9. };
```

## 调试命令与安全实践

### GDB调试示例

```
1. # 在gum_process_enumerate_modules处设置断点
2. (gdb)break gum_process_enumerate_modules
3. # 查看模块枚举过程
4. (gdb) info registers
5. (gdb) x/10s $rdi  # 查看模块名称
```

### 性能优化建议

* 避免频繁调用 `enumerateModules()`，可缓存结果
* 使用适当的过滤条件减少 `enumerateRanges()`的开销
* 注意内存泄漏，及时释放大对象

## 错误处理与边界情况

### 常见错误场景

* 无效地址查询：返回null或抛出异常
* 权限不足：某些内存区域无法访问
* 并发修改：模块列表在枚举过程中可能变化

### 最佳实践

```
1. // 安全的模块枚举
2. try{
3. const modules =Process.enumerateModules();
4. modules.forEach(module =>{
5. console.log(`${module.name}: ${module.base}- ${module.base.add(module.size)}`);
6. });
7. }catch(e){
8. console.error('Failed to enumerate modules:', e);
9. }
```

## 攻击检测场景映射

### 可用于检测的场景

* **模块注入检测**: 监控异常模块加载
* **内存扫描**: 检测可疑的内存区域
* **完整性验证**: 验证关键模块的基地址和大小

### 防御绕过技术

* **直接系统调用**: 绕过Frida的hook
* **内存加密**: 隐藏恶意代码
* **反调试技术**: 检测调试器存在

## 性能分析与优化

### 时间复杂度分析

* `enumerateModules()`: O(n)，n为模块数量
* `enumerateRanges()`: O(m)，m为内存段数量
* `findModuleByName()`: O(n)，需要遍历所有模块

### 内存使用分析

* 每次调用都会分配临时结构体
* 大量模块时内存占用显著
* 建议分批处理或使用流式API

## 扩展功能与自定义实现

### 自定义模块枚举

```
1. // 扩展Process模块功能
2. Process.myCustomEnumerateModules =function(filter){
3. returnProcess.enumerateModules().filter(module =>{
4. return module.name.includes(filter);
5. });
6. };
```

### 底层扩展点

* 可以通过修改 `gumprocess-*.c`添加新的平台特定功能
* 通过扩展GumProcessBackend结构体添加新方法

## 版本兼容性与演进

### API变更历史

* Frida 10.x: 引入统一的Process API
* Frida 12.x: 添加内存查询功能
* Frida 14.x: 优化性能和错误处理

### 向后兼容性保证

* 核心API保持稳定
* 新功能通过扩展方式添加
* 废弃的API会标记并提供迁移路径

## 实战案例分析

### 案例1: 动态库依赖分析

```
1. // 分析应用的动态库依赖
2. const mainModule =Process.findModuleByName(null);
3. console.log('Main module:', mainModule);

5. // 查找所有包含"ssl"的模块
6. const sslModules =Process.enumerateModules()
7. .filter(mod => mod.name.toLowerCase().includes('ssl'));
8. console.log('SSL modules:', sslModules);
```

### 案例2: 内存保护分析

```
1. // 分析可执行内存区域
2. const executableRanges =Process.enumerateRanges('---x');
3. executableRanges.forEach(range =>{
4. console.log(`Executable range: ${range.base}- ${range.base.add(range.size)}`);
5. });
```

## 总结与最佳实践

Process模块是Frida中最基础也是最重要的模块之一，提供了对目标进程的全面控制能力。理解其JS与C++的映射关系有助于：

1. **深入理解Frida架构**: 掌握从JS到原生代码的完整调用链
2. **性能优化**: 避免不必要的开销，合理使用API
3. **安全分析**: 利用Process模块进行深入的安全检测
4. **自定义扩展**: 基于现有架构开发新的功能

通过本文档的五层架构分析，开发者可以全面掌握Process模块的工作原理和使用技巧。

* 公众号:安全狗的自我修养
* vx:2207344074
* http://gitee.com/haidragon
* http://github.com/haidragon
* bilibili:haidragonx
* ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnskRnS8U6adRicNHKTOlLGF5GbKN4iaVmdBgAxJic5L2XI3XUjicZ4arBqh2Hz08qbibKaO5YDxiaRaZCgtOdH0Oia04cnTtqZlpC6EL0/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

##

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuq2npT2aXicLLTeYJSxb3maL7cWeo2Orfy4y56Vqyq66lv5hNa9jsrpxLpchvYxOQxd4oUU5QkgGNtX2q4tdTzDKNz8icRlq9gw/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

+ ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPMJPjIWnCTP3EjrhOXhJsryIkR34mCwqetPF7aRmbhnxBbiaicS0rwu6w/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=omk5zkfc&tp=webp#imgIndex=5)

#

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许...