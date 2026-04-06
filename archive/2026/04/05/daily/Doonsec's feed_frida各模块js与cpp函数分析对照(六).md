---
title: frida各模块js与cpp函数分析对照(六)
url: https://mp.weixin.qq.com/s/tFGH7iOCoZrN7ynkJm0F2Q
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:42:15.916291
---

# frida各模块js与cpp函数分析对照(六)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBntUANHu4EFicnOMSgOhdj4fYoPwqMj1Ajnojsx5R3pAbAtibZ4oqUJ8mFWqBKdzp64icWy7ZiarUmpiczARS9ncRflcd40gWxEBdfib4/0?wx_fmt=jpeg)

# frida各模块js与cpp函数分析对照(六)

原创

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器中沉浸阅读

* # 官网：http://securitytech.cc

  ![](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBnuSkNPRkjuaPf2NThmBooRdeZ52XpiazERTicv0JAic4CZiblUdhmSExjRiaWMny6SgstgHB2B2pibXcLCyH6ygjrnuQqzRrzuZyrtT0/640?wx_fmt=png&from=appmsg)

  # ObjC和Java模块 JavaScript与底层C++函数映射关系分析

  ## 文档概述

  本文档详细分析Frida中ObjC和Java模块的JavaScript API与其底层C/C++实现之间的映射关系，涵盖完整的五层架构模型分析。

  ## 五层架构模型分析

  ### 1. 接口定义层 (JavaScript API Layer)

  #### ObjC模块主要接口：

  #### Java模块主要接口：

  ### 2. 基础结构层 (GumJS Binding Layer)

  在 `subprojects/frida-gum/bindings/gumjs`目录中，ObjC和Java模块的绑定实现在相关文件中。

  #### 关键数据结构

  ```

  ```

  ### 3. 具体实现层 (Platform-specific Implementation)

  #### ObjC实现 ( `gumobjc*.c`)

  关键函数：

  #### Java实现 ( `gumjava*.c`)

  关键函数：

  ### 4. 工厂模式层 (Backend Factory)

  #### ObjC工厂

  ```

  ```

  #### Java工厂

  ```

  ```

  ### 5. 应用集成层 (Integration with Frida Core)

  ObjC和Java模块通过frida-core与上层应用集成，提供统一的API接口，并与JNI（Java）和Objective-C Runtime深度集成。

  ## 详细函数映射关系表

  ### ObjC模块映射表

  | JavaScript Function | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `ObjC.classes.ClassName` | `gum_objc_api_resolver_get_class()` | `gumobjcapiresolver.c` | 获取Objective-C类 |
  | `ObjC.Object.choose()` | `gum_objc_object_choose()` | `gumobjcobject.c` | 枚举指定类的所有实例 |
  | `ObjC.selectorAsString()` | `gum_objc_selector_to_string()` | `gumobjcmessage.c` | 将选择器转换为字符串 |
  | `ObjC.schedule()` | `gum_objc_schedule_on_queue()` | `gumobjcdispatch.c` | 在指定队列上调度任务 |

  ### Java模块映射表

  | JavaScript Function | C Function | File Location | Description |
  | --- | --- | --- | --- |
  | `Java.use()` | `gum_java_use()` | `gumjavaapiresolver.c` | 获取Java类包装器 |
  | `Java.choose()` | `gum_java_choose()` | `gumjavaobject.c` | 枚举指定类的所有实例 |
  | `Java.cast()` | `gum_java_cast()` | `gumjavaobject.c` | 转换Java对象类型 |
  | `Java.perform()` | `gum_java_perform()` | `gumjavavm.c` | 在Java VM线程上执行代码 |
  | `Java.enumerateLoadedClasses()` | `gum_java_enumerate_loaded_classes()` | `gumjavavm.c` | 枚举已加载的Java类 |

  ## 内存布局与数据结构可视化

  ### GumObjCObject结构体内存布局

  ```

  ```

  ### GumJavaObject结构体内存布局

  ```

  ```

  ### GumJavaClassWrapper结构体内存布局

  ```

  ```

  ## 系统调用级执行流程追踪

  ### ObjC.classes.ClassName执行流程

  ### Java.use()执行流程

  ### Java.perform()执行流程

  ### ObjC.Object.choose()执行流程

  ## 跨平台差异与抽象机制

  ### 平台特定实现

  ### 内存管理差异

  ### 线程模型差异

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

  ### 自定义ObjC工具

  ```

  ```

  ### 自定义Java工具

  ```

  ```

  ### 底层扩展点

  ## 版本兼容性与演进

  ### API变更历史

  ### 向后兼容性保证

  ## 实战案例分析

  ### 案例1: iOS应用Hook

  ```

  ```

  ### 案例2: Android SSL Pinning Bypass

  ```

  ```

  ### 案例3: 动态类分析

  ```

  ```

  ### 案例4: ObjC内存分析

  ```

  ```

  ## 总结与最佳实践

  ObjC和Java模块是Frida在移动平台上的核心功能，提供了对高级语言运行时的深度访问能力。理解其JS与C++的映射关系有助于：

  通过本文档的五层架构分析，开发者可以全面掌握ObjC和Java模块的工作原理和使用技巧，为移动平台的动态分析任务提供坚实的基础。

+ 核心API保持稳定
+ 新功能通过扩展方式添加
+ 废弃的API会标记并提供迁移路径

+ **Frida早期版本**: 基本的ObjC支持
+ **Frida 6.x**: 添加Java支持
+ **Frida 8.x**: 完善跨平台支持和性能优化
+ **Frida 10.x**: 添加更多的高级语言特性支持
+ **Frida 12.x**: 优化内存使用和错误处理
+ **Frida 14.x**: 改进Android版本兼容性和稳定性

+ 可以通过修改 `gumobjcapiresolver.c`添加新的Objective-C特性支持
+ 通过修改 `gumjavaapiresolver.c`添加新的Java API支持
+ 扩展对象包装器支持更多的属性和方法访问模式

+ **ObjC包装器**: 每个对象和类包装器占用固定内存
+ **Java包装器**: 需要维护JNI引用和JavaScript包装器
+ **优化建议**:
+ 及时释放不再使用的对象引用
+ 重用类包装器避免重复查找
+ 使用weak引用避免内存泄漏

+ **ObjC类查找**: O(1)（缓存后），O(n)（首次查找，n为类数量）
+ **Java类查找**: O(m)（m为类路径搜索时间）
+ **对象创建**: O(1)（简单包装），O(k)（k为构造函数复杂度）
+ **方法调用**: O(1)（直接调用），O(p)（p为参数转换开销）

+ **直接调用**: 绕过高级语言API直接调用底层函数
+ **动态加载**: 运行时动态加载和解析类
+ **混淆技术**: 使用混淆技术隐藏类和方法名
+ **多线程规避**: 在未被监控的线程中执行敏感操作

+ **ObjC Hook检测**: 监控关键Objective-C方法的调用
+ **Java Hook检测**: 监控敏感Java API的使用
+ **反调试检测**: 检测ObjC和Java运行时的存在
+ **行为分析**: 基于高级语言API调用进行行为分析

+ **ObjC错误**:
+ 类不存在：返回undefined
+ 方法不存在：调用时抛出异常
+ 内存不足：对象创建失败
+ **Java错误**:
+ Java VM不可用：Java.available为false
+ 类未找到：Java.use()抛出异常
+ JNI异常：需要正确处理和清除
+ 线程错误：在非Java线程上执行JNI调用

+ **ObjC安全**:
+ 避免调用可能导致崩溃的私有方法
+ 注意内存管理避免循环引用
+ 处理nil对象和异常情况
+ **Java安全**:
+ 正确处理JNI异常
+ 避免在错误的线程上下文中操作
+ 注意Android版本兼容性

+ **ObjC优化**:
+ 缓存常用的类和方法引用
+ 避免频繁的对象创建和销毁
+ 使用批处理减少消息发送开销
+ **Java优化**:
+ 重用Java.use()返回的类对象
+ 减少Java.perform()调用次数
+ 使用局部变量避免重复字段访问

+ **ObjC**:
+ 可以在任何线程上调用Objective-C方法
+ Grand Central Dispatch（GCD）支持
+ 主队列和自定义队列调度
+ **Java**:
+ 必须在附加到Java VM的线程上执行JNI调用
+ 主线程通常已经附加，其他线程需要显式附加
+ Android主线程有特殊限制

+ **ObjC内存管理**:
+ 自动引用计数（ARC）或手动引用计数（MRC）
+ 使用 `retain`/ `release`管理对象生命周期
+ JavaScript包装器持有强引用
+ **Java内存管理**:
+ Java垃圾回收自动管理
+ JNI局部引用和全局引用管理
+ 需要显式释放全局引用避免内存泄漏

+ **ObjC**: 仅在Apple平台（macOS、iOS）可用
+ 依赖Objective-C Runtime API
+ 使用 `objc_msgSend()`进行消息发送
+ 支持ARC和MRC内存管理
+ **Java**: 主要在Android平台可用
+ 依赖JNI（Java Native Interface）
+ 需要处理Java VM线程附加/分离
+ 支持不同的Android版本和Java VM实现

+ 分离线程 ( `DetachCurrentThread()`)

+ 附加线程到Java VM ( `AttachCurrentThread()`)

+ 调用 `FindClass()` JNI函数
+ 处理类加载器上下文

+ `gum_java_api_resolver_new()`
+ `gum_java_perform()`
+ `gum_java_use()`
+ `gum_java_choose()`
+ `gum_java_cast()`

+ **核心实现**: `gumjavaapiresolver.c` - Java API解析器
+ **VM交互**: `gumjavavm.c` - Java VM交互层
+ **对象管理**: `gumjavaobject.c` - Java对象包装
+ **类加载**: `gumjavaclassloader.c` - 类加载器管理

+ `gum_objc_api_resolver_new()`
+ `gum_objc_api_resolver_query_method()`
+ `gum_objc_object_new()`
+ `gum_objc_send_message()`

+ **核心实现**: `gumobjcapiresolver.c` - Objective-C API解析器
+ **对象管理**: `gumobjcobject.c` - Objective-C对象包装
+ **消息发送**: `gumobjcmessage.c` - 消息发送机制
+ **类枚举**: `gumobjcmodule.c` - 类和方法枚举

+ `Java.available`
+ `Java.androidVersion`
+ `Java.enumerateLoadedClasses(callbacks)`
+ `Java.enumerateClassLoaders(callbacks)`
+ `Java.use(className)`
+ `Java.choose(className,callbacks)`
+ `Java.cast(handle,klass)`
+ `Java.array(className,elements)`
+ `Java.registerClass(spec)`
+ `Java.scheduleOnMainThread(fn)`
+ `Java.perform(fn)`
+ `Java.performNow(fn)`
+ `Java.vm`
+ `Java.classFactory`

+ `ObjC.available`
+ `ObjC.classes`
+ `ObjC.Object`
+ `ObjC.Object.choose()`
+ `ObjC.selectorAsString(sel)`
+ `ObjC.schedule(queue,work)`
+ `ObjC.mainQueue`
+ `ObjC.deepUnwrap(obj)`
+ `ObjC.deepWrap(value)`

1. **移动应用分析**: 对iOS和Android应用进行深入的动态分析
2. **安全测试**: 绕过各种安全机制进行渗透测试
3. **逆向工程**: 辅助复杂的移动应用逆向工程任务
4. **自动化测试**: 构建基于高级语言API的自动化测试框架

1. `// 分析iOS应用内存中的对象`
2. `if(ObjC.available){`
3. `// 枚举特定类的所有实例`
4. `constNSString=ObjC.classes.NSString;`
5. `ObjC.Object.choose(NSString,{`
6. `onMatch:function(instance){`
7. `try{`
8. `const stringContent = instance.UTF8String().readUtf8String();`
9. `if(stringContent && stringContent.includes('password')){`
10. `console.log('Password-related string found:', stringContent);`
11. `}`
12. `}catch(e){`
13. `// 忽略无效对象`
14. `}`
15. `},`
16. `onComplete:function(){`
17. `console.log('NSString enumeration completed');`
18. `}`
19. `});`
21. `// 监控对象创建`
22. `constNSObject=ObjC.classes.NSObject;`
23. `Interceptor.attach(NSObject['- init'].implementation,{`
24. `onLeave:function(retval){`
25. `const obj =newObjC.Object(retval);`
26. `console.log('New object created:', obj.$className);`
27. `}`
28. `});`
29. `}`

1. `// 动态分析Android应用类`
2. `if(Java.available){`
3. `Java.perform(function(){`
4. `// 枚举所有加载的类`
5. `Java.enumerateLoadedClasses({`
6. `onMatch:function(className){`
7. `if(className.startsWith('com.targetapp.')){`
8. `console.log('Target class found:', className);`
10. `try{`
11. `const klass =Java.use(className);`
12. `// 分析类的方法`
13. `const methods = klass.class.getDeclaredMethods();`
14. `methods.forEach(method =>{`
15. `const methodName = method.getName();`
16. `if(methodName.includes('encrypt')|| methodName.includes('decrypt')){`
17. `` console.log(`Sensitive method found: ${className}....