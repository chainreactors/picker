---
title: 漏洞分析 | 利用 CodeQL 分析 fastjson 1.2.80 利用链
url: https://www.anquanke.com/post/id/281733
source: 安全客-有思想的安全新媒体
date: 2022-10-18
fetch_date: 2025-10-03T20:03:20.064194
---

# 漏洞分析 | 利用 CodeQL 分析 fastjson 1.2.80 利用链

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 漏洞分析 | 利用 CodeQL 分析 fastjson 1.2.80 利用链

阅读量**371939**

发布时间 : 2022-10-17 10:30:22

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 前言

前阵子浅蓝师傅在Kcon2022上公开了fastjson 1.2.80漏洞的利用思路和Gadget，根据漏洞利用思路，本文分析下如何利用CodeQL去挖掘fastjson 1.2.80的这些利用链。

## 漏洞利用分析

fastjson 1.2.80 漏洞利用是将异常类 `Throwable` 作为期望类，利用期望类机制将异常类 `Throwable` 的子类加入到缓存中。对比下修复补丁，可以看到在最新版fastjson 1.2.83中额外增加了对异常类的判断，并且在添加类到缓存前新增了对autoTypeSupport的判断，只有开启了autoTypeSupport才将类加入到缓存中。

![]()

![]()

在旧版的 `com.alibaba.fastjson.parser.ParserConfig#checkAutoType` 方法中，如下代码判断expectClass（期望类）不为null，且类Class对象和期望类之间存在继承关系，就会调用 `TypeUtils.addMapping(typeName, clazz);`方法将类Class对象缓存

![]()

fastjson在反序列化类时，会根据类来调用对应的反序列化器进行处理，异常类会使用 `com.alibaba.fastjson.parser.deserializer.ThrowableDeserializer` 反序列化器进行处理，在 `deserialze` 方法中首先对异常类进行实例化，如果要解析异常类的字段，调用setter方法给字段赋值，就会执行如下代码

![]()

在代码中首先通过调用 `parser.getConfig().getDeserializer(exClass)` 方法获取异常类对应的反序列化器，接着会调用`exBeanDeser.getFieldDeserializer(key)` 方法根据key，也就是字段名获取在异常类反序列化器对象中存储的对应字段反序列化器，最后判断 `if (!fieldInfo.fieldClass.isInstance(value))`，当value不是字段对应类的实例时，就会调用 `TypeUtils.cast()` 进行类型转换，继续向下跟，一直到调用 `com.alibaba.fastjson.util.TypeUtils#castToJavaBean` 方法，在方法中存在如下代码片段

![]()

调用 `config.getDeserializer(clazz)` 方法根据传入的类Class对象获取对应的反序列化器，而这里的clazz就是字段对应的类Class对象，而在 `getDeserializer` 方法的最后有调用 `this.putDeserializer((Type)type, (ObjectDeserializer)deserializer);` 方法，`putDeserializer` 方法能够将传入的类Class对象缓存起来，利用这个特性我们可以将类字段对应的类加入到缓存中，后续对类反序列化时，将直接从缓存中获取，从而绕过对autotype的检测。

在fastjson 1.2.73版本中对 `com.alibaba.fastjson.parser.deserializer.JavaBeanDeserializer#createInstance` 方法的代码进行了修改，对比1.2.72版本可以看到，在1.2.73版本修改了判断逻辑，当value不是字段对应类的实例或类字段拥有注解就会调用字段反序列化器的 `parseField` 方法

![]()

在 `com.alibaba.fastjson.parser.deserializer.DefaultFieldDeserializer#parseField` 方法中会调用 `getFieldValueDeserilizer` 方法，跟进该方法

![]()

在 `getFieldValueDeserilizer` 方法的最后会调用 `config.getDeserializer()` 方法，前面说到可以利用该方法将传入的类加入到缓存中，这里传入的是字段对应的类，利用这个特性我们就可以在类实例化时将指定的类字段对应的类加入到缓存中，方便后续利用

![]()

fastjson在创建类对应的反序列化器对象时，会获取类的字段，将从类的public field、类的public setter方法的参数、构造方法的参数这3个地方获取，利用这些特性我们就能直接或间接扩展出更多可利用的类，下面分析下编写codeql规则挖掘fastjson 1.2.80利用链。

## 编写ql规则

可以用来作为fastjson gadget的类

1. java.lang.Throwable 的子类
2. 类或子类的public field类型、setter方法的参数类型、构造方法的参数类型

我们根据上述条件编写查询规则，首先定义一个 `ThrowableClass` 类，用来表示直接或间接继承自`java.lang.Throwable`的类

```
class ThrowableClass extends Class {
    ThrowableClass() {
        this.getASupertype*().hasQualifiedName("java.lang", "Throwable")
    }
}
```

要获取类的 public 修饰的字段，这里采用定义谓词的方式，谓词相当于一个函数

```
Field getPublicFieldFromClass(Class cl) {
    exists(Field field|
        field.getDeclaringType() = cl
        and field.getAModifier().getName() = "public"
        and result = field
    )
}
```

这里 `getPublicFieldFromClass` 谓词表示接收一个Class类型的参数，匹配这个类的所有public修饰的字段，通过codeql内置变量result返回类的字段。

`field.getAModifier()` 用来获取字段的访问修饰符，可以编写如下测试查询语句，查询所有异常类的字段属性，以及字段的访问修饰符

```
from ThrowableClass tclass, Field field
# 匹配属于异常类的属性字段
where field.getDeclaringType() = tclass
select tclass, field, field.getAModifier()
```

![]()

要获取类的setter方法的参数，可以直接使用codeql内置的 `SetterMethod` 类，这个类用来表示setter方法，该类定义在 Member.qll 文件中。

setter方法会满足几个条件：

1. 方法只接收一个参数
2. 方法的主体正好包含一个语句
3. 将方法参数的值赋给与方法声明的类型相同的字段

![]()

在 `SetterMethod` 类中还提供了一个用来获取setter方法对应的字段的谓词 `getField`，我们使用这个谓词即可

要获取构造方法的参数，同样采用定义谓词的方式，接收一个Class类型参数，返回这个类的构造方法的参数，注意因为fastjson会优先选择参数最多的构造方法，所以这里使用 `max( | | )` 聚合函数来判断获取参数最多的构造方法

```
Parameter getParameterFromConstructor(Class cl) {
    exists(Constructor constructor, Parameter p |
        constructor = cl.getAConstructor()
        and constructor.getNumberOfParameters() = max(int i | cl.getAConstructor().getNumberOfParameters() = i | i)
        and p = constructor.getAParameter()
        and result = p
    )
}
```

下面以查询Groovy利用链为例，在Groovy利用链的最后是调用 `newInstance` 方法实例化恶意类触发命令执行，我们以 `newInstance` 方法作为sink点，编写一个类 `NewInstaceMethod` 来表示 `newInstance` 方法

```
class NewInstaceMethod extends Method {
    NewInstaceMethod() {
        exists(GenericClass gclass |
            this.getName() = "newInstance"
            and gclass.getQualifiedName() = "java.lang.reflect.Constructor"
            and this.getDeclaringType().getSourceDeclaration() = gclass
        )
    }
}
```

编写查询语句，查询从source到sink之间的函数调用关系，这里是先获取异常类的字段对应的类，然后是将类或类的子类的构造方法作为source，`getASubtype()` 谓词用于获取类的所有子类，加上 `*` 表示获取直接子类或间接子类

```
from ThrowableClass tclass, Class sourceClass, SetterMethod setter, NewInstaceMethod method, Constructor constructor
where (
    sourceClass = getPublicFieldFromClass(tclass).getType().(Class)
    or (
        setter.getDeclaringType() = tclass
        and sourceClass = setter.getField().getType().(Class)
    )
    or sourceClass = getParameterFromConstructor(tclass).getType().(Class)
) and isExcludeClass(sourceClass)
and isExcludeClass(sourceClass.getASubtype*())
and constructor = sourceClass.getASubtype*().getAConstructor()
and edges+(constructor, method)
select constructor, constructor, method, "Fastjson Gadget"
```

edges是定义的查询谓词，用来查询函数调用，`a.polyCalls(b)`表示a调用了b，`edges+` 表示一次到多次调用

```
query predicate edges(Callable a, Callable b) {
    a.polyCalls(b)
}
```

`isExcludeClass` 谓词是定义用来排除某些类，减少误报

```
predicate isExcludeClass(RefType type) {
    not (
        type.getQualifiedName() in [
            "java.lang.Object",
            "java.lang.String",
            "java.lang.Number",
            "java.lang.Integer",
            "java.lang.Class"
        ]
    )
}
```

最后看下查询结果，可以看到查询到了groovy利用链的函数调用关系

![]()

```
org.codehaus.groovy.tools.javac.JavaStubCompilationUnit#JavaStubCompilationUnit(org.codehaus.groovy.control.CompilerConfiguration, groovy.lang.GroovyClassLoader, java.io.File)
org.codehaus.groovy.control.CompilationUnit#CompilationUnit(org.codehaus.groovy.control.CompilerConfiguration, java.security.CodeSource, groovy.lang.GroovyClassLoader)
org.codehaus.groovy.control.CompilationUnit#CompilationUnit(org.codehaus.groovy.control.CompilerConfiguration, java.security.CodeSource, groovy.lang.GroovyClassLoader, groovy.lang.GroovyClassLoader)
org.codehaus.groovy.control.CompilationUnit#addPhaseOperations
org.codehaus.groovy.transform.ASTTransformationVisitor#addPhaseOperations
org.codehaus.groovy.transform.ASTTransformationVisitor#addGlobalTransforms
org.codehaus.groovy.transform.ASTTransformationVisitor#doAddGlobalTransforms
org.codehaus.groovy.transform.ASTTransformationVisitor#addPhaseOperationsForGlobalTransforms
```

因为codeql不支持同时查询两个数据库，所以针对其它链的查找不使用查询函数调用的方式，而是直接查找可利用的类。将前面获取类字段的操作封装成一个谓词，方便多次调用

```
RefType findClass(RefType type) {
    exists(SetterMethod setter,RefType source |
        (
            source = getPublicFieldFromClass(type).getType().(RefType)
            or (
              setter.getDeclaringType() = type
              and source = setter.getField().getType().(RefType)
            )
            or source = getParameterFromConstructor(type).getType().(RefType)
        )
          and isExcludeClass(source)
        and result = source
    )
}
```

再编写一个谓词 `isSinkClass`，用来判断获取的类是不是可以被利用的类

```
predicate isSinkClass(RefType type) {
    type.getQualifiedName() in [
        "java.io.InputStream",
        "java.sql.Connection"
    ]
}
```

以查询Jython利用链为例，直接在LGTM平台上查询，这里首先调用我们封装好的谓词 `findClass` 获取异常类的字段，然后再根据字段对应的类或子类再次调用 `findClass` 获取类的字段，最后判断获取到的类字段对应的类是不是可利用的类

![]()

可以看到查询到了Jython利用链的可利用的类，`ParseException` 异常类中存在 `org.python.core.PyObject` 类型的字段，`com.ziclix.python.sql.PyConnection` 是 `org.python.core.PyObject` 类的子类，而在`com.ziclix.python.sql.PyConnection` 类中存在 `java.sql.Connection` 类型的字段。

下面是查询OGNL利用链，这里需要调用4次 `findClass` 谓词，最终查询到了OGNL利用链的可利用类。

![]()

![]()

## 参考链接

Hacking JSON【KCon2022】：<https://github.com/knownsec/KCon/blob/master/2022/Hacking%20JSON%E3%80%90KCon20...