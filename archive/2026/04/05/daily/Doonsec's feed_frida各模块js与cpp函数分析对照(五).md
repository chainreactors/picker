---
title: frida各模块js与cpp函数分析对照(五)
url: https://mp.weixin.qq.com/s/N3lx5gzPlvMROmdSs2EDWg
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:42:11.372491
---

# frida各模块js与cpp函数分析对照(五)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBnsianOQU2vFMn0aN9d6vA3Fh3XSvHT0p7LNfMM1icWKniaM5FIY6YkYIMUGkFJtwibs7gtlicIpRbSw9AqpNC91rBY2fnDk7DpRibqVQ/0?wx_fmt=jpeg)

# frida各模块js与cpp函数分析对照(五)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

* # 官网：http://securitytech.cc

  ![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuSkNPRkjuaPf2NThmBooRdeZ52XpiazERTicv0JAic4CZiblUdhmSExjRiaWMny6SgstgHB2B2pibXcLCyH6ygjrnuQqzRrzuZyrtT0/640?wx_fmt=png&from=appmsg)

  # Instrumentation模块 JavaScript与底层C++函数映射关系分析

  ## 文档概述

  本文档详细分析Frida中Interceptor、Stalker等仪器模块的JavaScript API与其底层C/C++实现之间的映射关系，涵盖完整的五层架构模型分析。

  ## 五层架构模型分析

  ### 1. 接口定义层 (JavaScript API Layer)

  #### Interceptor主要接口：

  #### Stalker主要接口：

  #### 其他仪器相关接口：

  ### 2. 基础结构层 (GumJS Binding Layer)

  在 `subprojects/frida-gum/bindings/gumjs`目录中，Interceptor和Stalker模块的绑定实现在相关文件中。

  #### 关键数据结构

  ```

  ```

  ### 3. 具体实现层 (Platform-specific Implementation)

  #### Interceptor实现 ( `guminterceptor.c`)

  关键函数：

  #### Stalker实现 ( `gumstalker.c`)

  关键函数：

  ### 4. 工厂模式层 (Backend Factory)

  #### 指令重定位器工厂

  ```

  ```

  #### 拦截器工厂

  ```

  ```

  #### 跟踪器工厂

  ```

  ```

  ### 5. 应用集成层 (Integration with Frida Core)

  Interceptor和Stalker模块通过frida-core与上层应用集成，提供统一的API接口，并与事件系统和消息通道深度集成。

  ## 详细函数映射关系表

  ### Interceptor映射表

  | JavaScript Function | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `Interceptor.attach()` | `gum_interceptor_attach()` | `guminterceptor.c` | 附加拦截监听器 |
  | `Interceptor.detach()` | `gum_interceptor_detach()` | `guminterceptor.c` | 分离拦截监听器 |
  | `Interceptor.replace()` | `gum_interceptor_replace()` | `guminterceptor.c` | 替换目标函数 |
  | `Interceptor.revert()` | `gum_interceptor_revert()` | `guminterceptor.c` | 恢复被替换的函数 |

  ### Stalker映射表

  | JavaScript Function | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `Stalker.follow()` | `gum_stalker_follow()` | `gumstalker.c` | 开始跟踪线程执行 |
  | `Stalker.unfollow()` | `gum_stalker_unfollow()` | `gumstalker.c` | 停止跟踪线程 |
  | `Stalker.exclude()` | `gum_stalker_exclude()` | `gumstalker.c` | 排除内存范围不跟踪 |
  | `Stalker.flush()` | `gum_stalker_flush()` | `gumstalker.c` | 刷新跟踪缓冲区 |
  | `Stalker.garbageCollect()` | `gum_stalker_garbage_collect()` | `gumstalker.c` | 垃圾回收跟踪代码 |

  ## 内存布局与数据结构可视化

  ### GumInterceptor结构体内存布局

  ```

  ```

  ### GumStalker结构体内存布局

  ```

  ```

  ### GumInvocationListener结构体内存布局

  ```

  ```

  ## 系统调用级执行流程追踪

  ### Interceptor.attach()执行流程

  ### 函数调用拦截执行流程

  ### Stalker.follow()执行流程

  ### 动态二进制插桩执行流程

  ## 跨平台差异与抽象机制

  ### 指令集架构差异

  ### 内存保护机制差异

  ### 线程控制差异

  ### 抽象层设计

  ```

  ```

  ## 调试命令与安全实践

  ### GDB调试示例

  ```

  ```

  ### 性能优化建议

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

  ### 自定义Interceptor变换器

  ```

  ```

  ### 自定义Stalker事件处理器

  ```

  ```

  ### 底层扩展点

  ## 版本兼容性与演进

  ### API变更历史

  ### 向后兼容性保证

  ## 实战案例分析

  ### 案例1: SSL/TLS解密监控

  ```

  ```

  ### 案例2: 控制流完整性分析

  ```

  ```

  ### 案例3: 函数调用图生成

  ```

  ```

  ### 案例4: 性能剖析

  ```

  ```

  ## 总结与最佳实践

  Interceptor和Stalker模块是Frida最强大的动态分析工具，提供了从函数级别到指令级别的全面监控能力。理解其JS与C++的映射关系有助于：

  通过本文档的五层架构分析，开发者可以全面掌握Instrumentation模块的工作原理和使用技巧，为复杂的动态分析任务提供坚实的基础。

+ 核心API保持稳定
+ 新功能通过扩展方式添加
+ 废弃的API会标记并提供迁移路径

+ **Frida早期版本**: 基本的Interceptor功能
+ **Frida 6.x**: 添加Stalker支持
+ **Frida 8.x**: 完善跨平台支持和性能优化
+ **Frida 10.x**: 添加更多的指令集架构支持
+ **Frida 12.x**: 优化内存使用和错误处理
+ **Frida 14.x**: 改进Stalker的可靠性和性能

+ 可以通过修改 `guminterceptor.c`添加新的拦截策略
+ 通过修改 `gumstalker.c`添加新的事件类型和处理逻辑
+ 扩展指令重定位器和写入器支持新的指令集特性

+ **Interceptor**: 每个拦截点需要分配跳板代码和上下文结构体
+ **Stalker**: 需要分配跟踪缓冲区、代码页和事件队列
+ **优化建议**:
+ 限制同时跟踪的线程数量
+ 及时清理不再需要的拦截器和跟踪器
+ 使用exclude排除大块不需要跟踪的内存

+ **Interceptor.attach()**: O(1)，但涉及内存分配和代码修改
+ **Interceptor回调**: O(n)，n为回调函数复杂度
+ **Stalker.follow()**: O(1)，但启动开销较大
+ **Stalker事件处理**: O(m)，m为每条指令的处理开销

+ **直接系统调用**: 绕过被拦截的API直接调用系统调用
+ **代码混淆**: 使用混淆技术干扰Stalker的分析
+ **反跟踪技术**: 检测和规避动态二进制插桩
+ **多线程规避**: 在未被跟踪的线程中执行敏感操作

+ **API监控**: 使用Interceptor监控敏感API调用
+ **控制流分析**: 使用Stalker分析程序执行路径
+ **反调试检测**: 检测Interceptor和Stalker的存在
+ **行为分析**: 基于函数调用序列进行行为分析

+ **Interceptor错误**:
+ 目标地址无效：无法创建跳板
+ 内存保护冲突：无法修改代码页
+ 多重拦截冲突：同一地址被多次拦截
+ **Stalker错误**:
+ 线程ID无效：无法跟踪不存在的线程
+ 内存不足：无法分配跟踪缓冲区
+ 性能问题：跟踪开销过大导致应用卡顿

+ **拦截器安全**: 避免拦截关键系统函数导致崩溃
+ **跟踪器安全**: 注意性能开销，避免影响目标应用正常运行
+ **内存安全**: 确保跳板代码和插桩代码的内存安全性

+ **Interceptor优化**:
+ 避免过度拦截，只拦截必要的函数
+ 使用高效的回调函数，避免复杂计算
+ 考虑使用replace而不是attach/leave组合
+ **Stalker优化**:
+ 排除不需要跟踪的内存范围
+ 调整队列容量和刷新间隔
+ 使用自定义变换器减少事件数量

+ **Darwin**: 使用Mach线程API (thread*suspend, thread*resume)
+ **Linux**: 使用ptrace()系统调用
+ **Windows**: 使用SuspendThread()/ResumeThread()

+ **Darwin**: 使用VM*PROTECT*WRITECOPY等Mach VM特性
+ **Linux**: 使用mprotect()和信号处理
+ **Windows**: 使用VirtualProtect()和异常处理

+ **x86/x86\_64**:
+ 变长指令，复杂寻址模式
+ 需要精确的指令重定位
+ 支持硬件性能计数器
+ **ARM/ARM64**:
+ 固定长度指令（ARM64: 32位，ARM: 16/32位混合）
+ 条件执行和分支预测
+ Thumb模式支持
+ **MIPS**:
+ 固定长度32位指令
+ 延迟槽(branch delay slot)处理
+ 流水线优化考虑

+ 保存原始指令
+ 生成跳转到拦截处理程序的代码
+ 处理指令重定位（跨平台差异）

+ `gum_stalker_follow()`
+ `gum_stalker_unfollow()`
+ `gum_stalker_exclude()`
+ `gum_stalker_flush()`

+ **通用跟踪器**: `gumstalker.c` - 动态二进制插桩引擎
+ **平台特定实现**:
+ **x86/x86\_64**: 使用Intel PT或软件跟踪
+ **ARM/ARM64**: 使用分支跟踪或软件跟踪
+ **MIPS**: 软件跟踪实现

+ `gum_interceptor_attach()`
+ `gum_interceptor_detach()`
+ `gum_interceptor_replace()`
+ `gum_interceptor_revert()`

+ **通用拦截器**: `gum_interceptor.c` - 跨平台函数拦截框架
+ **平台特定后端**:
+ **x86/x86\_64**: `gumx86relocator.c`, `gumx86writer.c`
+ **ARM/ARM64**: `gumarmrelocator.c`, `gumarmwriter.c`, `gumarm64relocator.c`, `gumarm64writer.c`
+ **MIPS**: `gummipsrelocator.c`, `gummipswriter.c`

+ `Script.bindWeak(callback,target)`
+ `Script.nextTick(callback)`
+ `setTimeout(callback,delay)`
+ `clearTimeout(timerId)`

+ `Stalker.follow([threadId],options)`
+ `Stalker.unfollow([threadId])`
+ `Stalker.garbageCollect()`
+ `Stalker.exclude(range)`
+ `Stalker.flush()`
+ `Stalker.trustThreshold`
+ `Stalker.queueCapacity`
+ `Stalker.queueDrainInterval`

+ `Interceptor.attach(target,callbacks)`
+ `Interceptor.detach(listener)`
+ `Interceptor.replace(target,replacement)`
+ `Interceptor.revert(target)`
+ `InvocationContext`对象（包含 `context`, `returnAddress`, `depth`, `register`, `errno`, `lastError`等属性）

1. **深度监控**: 对应用程序进行全方位的行为监控和分析
2. **性能优化**: 合理使用仪器功能避免过度开销
3. **安全分析**: 利用动态插桩技术进行高级安全检测
4. **逆向工程**: 辅助复杂的逆向工程任务

1. `// 函数级别性能剖析`
2. `const profileData =newMap();`
4. `Interceptor.attach(Module.findExportByName(null,'some_function'),{`
5. `onEnter:function(args){`
6. `this.startTime =Date.now();`
7. `this.startCpuTime =Process.getCpuTime();`
8. `},`
9. `onLeave:function(retval){`
10. `const duration =Date.now()-this.startTime;`
11. `const cpuTime =Process.getCpuTime()-this.startCpuTime;`
13. `const funcName ='some_function';`
14. `if(!profileData.has(funcName)){`
15. `profileData.set(funcName,{ calls:0, totalTime:0, totalCpuTime:0});`
16. `}`
18. `const data = profileData.get(funcName);`
19. `data.calls++;`
20. `data.totalTime += duration;`
21. `data.totalCpuTime += cpuTime;`
22. `}`
23. `});`
25. `// 定期输出剖析结果`
26. `setInterval(()=>{`
27. `profileData.forEach((data, funcName)=>{`
28. `` console.log(`${funcName}: ${data.calls} calls, ${data.totalTime}ms total, ${data.totalCpuTime}ms CPU`); ``
29. `});`
30. `},5000);`

1. `// 生成函数调用图`
2. `const callGraph =newMap();`
3. `let currentDepth =0;`
5. `function trackFunctionCalls(moduleName){`
6. `Module.enumerateExports(moduleName,{`
7. `onMatch:function(exportDetails){`
8. `if(exportDetails.type ==='function'){`
9. `Interceptor.attach(exportDetails.address,{`
10. `onEnter:function(args){`
11. `const caller =this.returnAddress;`
12. `const callee = exportDetails.address;`
14. `if(!callGraph.has(caller)){`
15. `callGraph.set(caller,newSet());`
16. `}`
17. `callGraph.get(caller).add(callee);`
19. `currentDepth++;`
20. `},`
21. `onLeave:function(retval){`
22. `currentDepth--;`
23. `}`
24. `});`...