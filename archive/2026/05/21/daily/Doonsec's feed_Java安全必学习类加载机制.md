---
title: Java安全必学习类加载机制
url: https://mp.weixin.qq.com/s/YPZhj8Y_X653PUahJFK5rg
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:05:14.195303
---

# Java安全必学习类加载机制

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ULOszTo2RiaAiaqB19vibCnE4Hv9PLf8fSjSgaAqKb1Z5PzscaQdKA8vhcgdk5PNrx8cSRZngUaJxCB2SvBg5ic6H833ILD0H352yVr3gvjZcvk/0?wx_fmt=jpeg)

# Java安全必学习类加载机制

me7eorite
me7eorite

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 类加载类型

## 静态加载

**编译时:** 加载相关的类，类不存在直接报错，无法运行。

* • 依赖性强，缺少类就无法编译通过

```
// 编译时就必须存在 Dog 类，否则报错
Dog dog = new Dog();
```

## 动态加载

**运行时:** 加载需要的类，不使用该类就不会报错。

* • 灵活性高，降低依赖性
* • 延迟加载，用到时才触发

```
// 运行时才去找 Dog 类，编译阶段不检查
Class c = Class.forName("Dog");
```

## 类加载时机

| 触发方式 | 加载类型 | 说明 |
| --- | --- | --- |
| `new` 创建对象 | 静态 | 编译时确定 |
| 子类被加载时 | 静态 | 父类同步加载 |
| 调用类的静态成员 | 静态 | 编译时确定 |
| 使用反射 | 动态 | 运行时触发 |
| `Class.forName()` | 动态 | 运行时显式加载 |

# 类加载过程(生命周期)

类从被加载到 JVM 内存到卸载，需经历 7 个阶段，分别为 加载、验证、准备、解析、初始化、使用、卸载。其中,验证、准备、解析三个阶段统称为**连接**。为什么？执行顺序？
类加载的过程只包括: **加载、验证、准备、解析、初始化**。一般这 5 个阶段都是顺序发生的，但有**动态绑定**的情况下，解析阶段会晚于初始化阶段发生。
![[类加载过程.png]]

## 加载(Loading)【从哪里来？--> 怎么处理? -->到哪里去？】

在该阶段 JVM 将字节码从不同的数据源(Class文件、Jar文件、网络)转为二进制字节流加载到内存中，**并生成为一个代表类的 `java.lang.Class` 对象**。

## 验证(Verification)【主要有什么规范？】

该阶段 JVM 对二进制字节流进行校验，只有**符合 JVM 字节码规范**的才能被 JVM 执行，主要包含以下几个部分：

1. 1. 确保二进制字节流格式符合规范。s
2. 2. 所有方法需遵守访问控制关键字限定。
3. 3. 方法调用的参数个数和类型是否正确
4. 4. 确保变量在使用之前被正确初始化
5. 5. 检查变量是否被赋予恰当类型的值
6. 6. ...
   该阶段是保证 JVM 安全的屏障。

## 准备(Preparation)

该阶段 JVM 对类变量/静态变量(`static`)分配内存并初始化(给定对应数据类型的默认初始值: 0、0L、null...)
例如：

```
public String var1 = "test";
public static String var2 = "test2";
public static final String var3 = "test3";
```

上述代码在准备阶段：

1. 1. `var1` 不会分配内存
2. 2. `var2` 会被分配内存初始值为`null`
3. 3. `var3`是(`static final`)常量会被初始化为`test3`。

## 解析(Resolution)【处理哪里的数据？完整怎样的转化？】

该阶段将常量池中的**符号引用**解析为**直接引用**,简单来说，将"名字"转换为"真实位置"。
例如，代码中编写 `com.example.vuln`,在编译时只是一个字符串(**'名字'**)，JVM 并不知道它来自于哪里。等程序运行时,JVM会根据该**名字**找到类在内存的位置，该结果即为直接引用。

* • 举例：`Class.forName(userInput)` 当 `userInput` 可控，其作为符号引用，JVM在该阶段会解析并寻找加载对应的类。

+ • 没加载 → 触发类加载（Load → Link → Init）
+ • 已加载 → 直接拿已有的Class对象

## 初始化(Initialization)【做了什么？什么会触发？】

该阶段为类加载的最后一步，类变量将被赋予代码定义的值。换句话说,初始化阶段是执行类构造器方法，**执行类里的 static 代码**（也就是 `<clinit>()`）。
比如：

```
class A {
    static int x = 10;
    static {
        System.out.println("init A");
    }
}
```

初始化时做的就是：

```
x = 10
执行 static 代码块
```

* • **初始化的触发需要满足以下某项：**

1. 1. 创建类的实例(`new xxx()`)
2. 2. 访问 static 变量/方法(非 `final`)
3. 3. 反射(`Class.forName()`)
4. 4. 初始化子类(会先初始化父类)
5. 5. 程序的入口(`Main`方法对应类)
   那么，初始化是会执行类里的 static 代码，而这一步可能导致RCE。

# 类加载器【 加载器类型，对于不同标准怎么统一处理？加载地址 】

`JVM` 判断类是否相同，不仅看类名，还看是"谁加载的"。
![[类加载器.png]]
类加载器决定从哪里加载类,通过 "双亲委派" 机制
例如：`new Test()`
JVM 视角: 1.使用`ClassLoader` --> 找到 `Test.class` --> 加载 --> 运行
主要的类加载器为以下三种:

1. 1. `Bootstrap`

* • 加载: Java核心类(`Java.lang.*`)
* • 特点: 通过 C++ 实现,不是 Java 对象。`String.class.getClassLoader()`返回`null`。

2. 2. `Extension`

* • 加载: `jre/lib/ext` 中的拓展库

3. 3. `Application`

* • 加载: 用户编写的代码(`classpath`中)
* • 特点：平常接触的多。
  自定义类加载器属于第四种，类的加载问题可被控制。
  由于 类加载默认是"从上往下找" 双亲委派: 加载 Test 类 --> 想问 `Bootstrap` ...
  **避免核心类被覆盖的问题并且不同加载器可加载 "同名不同类"。**

---

在漏洞分析过程中，需要关注类从哪里来，是否是自定义的类加载器，关键在于触发类加载的方式。

# 双亲委派【加载规则】

类加载先交给父加载器，只有父加载器加载不了才自己加载，从而保证类的唯一性和核心类的安全性。

```
Bootstrap ClassLoader
        ↑
        │
Extension ClassLoader
        ↑
        │
System/Application ClassLoader
        ↑
        │
Custom ClassLoader
```

这种层次关系被称作为双亲委派模型：
加载一个类 → 先给父加载器 → 一直往上问（直到 Bootstrap） → 都加载不了 → 才自己加载。
这种设计存在两个核心作用：

1. 1. 防止核心类被覆盖

* • 例如: `java.lang.String`

2. 2. 避免重复加载

# 总结

加载阶段是从不同来源（文件、网络、jar包等）找到二进制字节流，将其转换为方法区中的运行时数据结构，并在堆中生成对应的 Class 对象作为访问入口。
在此过程中 JVM 提供了三种内置类加载器：Bootstrap ClassLoader（负责加载核心类库）、Extension ClassLoader（负责加载扩展类）、Application ClassLoader（负责加载用户 classpath 下的类），此外还支持自定义类加载器。为保证加载的安全性，设计了双亲委派机制，防止核心类被覆盖和重复加载。
验证阶段，验证 Class 对象是否符合 JVM 规范。
准备阶段，将定义的 static 变量进行内存分配并赋默认值（如 int 默认为 0，引用类型默认为 null）。
解析阶段，将常量池中的符号引用替换为直接引用（即内存中的实际地址），使 JVM 能够真正找到对应的类、方法和字段。
初始化阶段，执行类的初始化逻辑，触发条件包括：使用 new 创建对象、调用静态方法或访问静态字段、使用 Class.forName() 加载类、子类初始化时父类尚未初始化、以及 JVM 启动时的主类（含 main 方法的类）。

# 参考文章

一文彻底搞懂 Java 类加载机制
类加载过程详解
Java 类加载篇（一）ClassLoader 类加载机制总结

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

Gh0xE9

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
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过