---
title: 第45天-JavaEE安全探秘：动态代理与反序列化漏洞深度解析
url: https://mp.weixin.qq.com/s/SyENC7Y9eWi6UciQEwWNeA
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:17:17.101675
---

# 第45天-JavaEE安全探秘：动态代理与反序列化漏洞深度解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Byhdgj3e9qvd1hy9dq8I6Ex4g2Gx3DQ3dKicUaewGUESUFhkcSmUicI6RSb82ib6zjOp8O65BxmMynASSiaocpsLCphvKmk4DO590bEudTKUtgo/0?wx_fmt=jpeg)

# 第45天-JavaEE安全探秘：动态代理与反序列化漏洞深度解析

原创

萧瑶
萧瑶

AlphaNet

![]()

在小说阅读器中沉浸阅读

在JavaEE开发中，动态代理和反序列化是两个极为重要的技术点，它们不仅支撑着框架的灵活扩展，也常常成为安全攻击的突破口。本文将从基础概念到安全利用，为你梳理一份高质量的学习笔记，帮助你在开发中既会用，又能防。

📌 动态代理（Dynamic Proxy）

1. 什么是代理模式？

代理模式是Java中最常用的设计模式之一。它允许我们通过一个代理类来控制对原始对象（委托类）的访问。代理类和委托类实现相同的接口，代理类负责预处理消息、过滤消息、转发消息以及事后处理等。

2. 静态代理 vs 动态代理

· 静态代理：手动编写代理类，在编译期就确定代理关系。

· 动态代理：在运行时动态生成代理类，无需手动编写。Java原生提供了基于接口的JDK动态代理。

3. JDK动态代理的实现步骤

JDK动态代理主要涉及 java.lang.reflect.Proxy 和 java.lang.reflect.InvocationHandler 接口。实现分为四步：

① 创建接口及定义方法

```java

public interface UserService {

void login(String username, String password);

}

```

② 实现接口（委托类）

```java

public class UserServiceImpl implements UserService {

@Override

public void login(String username, String password) {

System.out.println("用户：" + username + " 登录成功");

}

}

```

③ 实现 InvocationHandler 接口，重写 invoke 方法

```java

import java.lang.reflect.InvocationHandler;

import java.lang.reflect.Method;

public class LogHandler implements InvocationHandler {

private Object target; // 委托类对象

public LogHandler(Object target) {

this.target = target;

}

@Override

public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {

System.out.println("调用前，记录日志...");

Object result = method.invoke(target, args); // 反射调用实际方法

System.out.println("调用后，清理资源...");

return result;

}

}

```

④ 创建代理对象并调用方法

```java

import java.lang.reflect.Proxy;

public class Main {

public static void main(String[] args) {

UserService userService = new UserServiceImpl();

LogHandler handler = new LogHandler(userService);

UserService proxy = (UserService) Proxy.newProxyInstance(

userService.getClass().getClassLoader(),

userService.getClass().getInterfaces(),

handler);

proxy.login("admin", "123456");

}

}

```

4. 🔐 安全总结：利用条件分析 & 执行 invoke

动态代理在安全领域常被用于构造利用链，因为 invoke 方法可以劫持所有接口方法的调用，在其中插入恶意逻辑。利用条件：

· 目标对象的方法调用被代理接管。

· invoke 方法中能够执行任意代码（如反射调用危险方法）。

· 结合反序列化，当反序列化对象触发指定方法时，可能进入 invoke 逻辑。

5. 安全案例：Ysoserial-CC1链 - LazyMap

在 Commons Collections 1 利用链中，LazyMap 的 get 方法会调用 transform，而 AnnotationInvocationHandler 的 invoke 方法可以触发 LazyMap.get，最终实现任意代码执行。这正是动态代理与反序列化结合产生的经典漏洞。

---

📦 反序列化（Deserialization）

1. 序列化与反序列化概念

· 序列化：将内存中的对象转换为字节流（二进制数据），方便存储或传输。

· 反序列化：将字节流还原为内存中的对象。

https://via.placeholder.com/400x200?text=对象+<->+字节流

2. 为什么需要序列化技术？

· 进程通信：网络传输对象（如RPC、RMI）。

· 数据持久化：将对象保存到文件、数据库。

· 深拷贝：通过序列化实现对象的完整副本。

· 缓存：将对象序列化后存入缓存（如Redis）。

常见应用场景：

· 将对象存入文件或数据库

· Socket 传输对象

· RMI（远程方法调用）传输参数和返回值

3. 常见的序列化/反序列化协议

协议/库 特点

Java 原生（ObjectInputStream / ObjectOutputStream） 内置，需实现 Serializable 接口

XMLDecoder / XMLEncoder Java 自带的 XML 序列化

XStream XML 和 JSON 转换

SnakeYaml YAML 格式

FastJson 阿里巴巴的高性能 JSON 库

Jackson 流行的 JSON 处理库

4. ⚠️ 为什么会出现反序列化安全问题？

根本原因：反序列化过程中会自动执行对象的某些方法，如果这些方法包含危险操作，攻击者就可以构造恶意数据触发。

以 Java 原生反序列化为例：

· writeObject()：将对象写入流。

· readObject()：从流中读取对象，还原时自动调用（如果重写了该方法）。

· FileInputStream / FileOutputStream：文件字节流。

· ObjectInputStream / ObjectOutputStream：对象序列化流。

危险代码分析：

· 重写的 readObject() 方法中直接调用了危险方法（如 Runtime.exec()）。

· 对象反序列化后，某些方法（如 toString()、hashCode()）在后续操作中被自动调用，从而触发恶意逻辑。

· 类在反序列化时，构造函数、静态代码块等也可能被执行。

5. 反序列化利用链的常见模式

攻击者通常需要构造一个“利用链”，使得反序列化过程中逐步调用到危险方法。常见模式有：

1. 入口类的 readObject 直接调用危险方法

· 例如：java.util.HashMap 的 readObject 中会计算键的 hashCode，若某个键对象的 hashCode 方法包含恶意代码，则触发。

2. 入口参数中包含可控类，该类有危险方法，readObject 时调用

· 例如：PriorityQueue 的 readObject 中会调用 comparator 的 compare 方法，若该 comparator 是恶意类，则触发。

3. 入口类参数包含可控类，该类又调用其他有危险方法类，形成链式调用

· 如 CC1 链：AnnotationInvocationHandler.readObject -> LazyMap.get -> ChainedTransformer.transform -> Runtime.exec。

4. 构造函数/静态代码块等类加载时隐式执行

· 某些类的静态代码块或构造函数中写有恶意代码，反序列化创建对象时触发。

6. 🔐 反序列化利用条件总结

· 输入可控：攻击者能够向反序列化接口提供恶意构造的字节流。

· 类实现 Serializable 或 Externalizable 接口：只有这样的类才能被序列化/反序列化。

· 存在可利用的调用链：在反序列化过程中能逐步触发危险方法（依赖第三方库如 Commons Collections 等）。

---

🛡️ 总结与安全建议

· 动态代理本身是安全的设计模式，但若与反序列化结合，可能被利用构造攻击链（如 CC1）。

· 反序列化漏洞的核心在于自动执行逻辑，开发者应避免在 readObject 等方法中执行危险操作。

· 使用反序列化时，建议：

· 对输入进行严格校验（如使用白名单）。

· 避免反序列化不可信数据。

· 升级存在漏洞的依赖库。

· 考虑使用更安全的序列化协议（如 JSON）代替 Java 原生。

希望这份笔记能帮助你更好地理解 JavaEE 中动态代理和反序列化的机制与安全风险。如果你在实际开发或安全研究中遇到相关问题，欢迎留言讨论！

---

📚 扩展阅读

· Ysoserial 工具与 Commons Collections 利用链分析

· Java 安全编码指南

· 《Java 安全攻防：反序列化篇》

本文由 Java安全学习笔记整理，仅供参考学习，请勿用于非法用途。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

AlphaNet

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Byhdgj3e9quk3H3M941l5byeiaCLHfZUhoIib5xPSPc8ddSdEOynSxIhaaiaIxwJImQia7wqHZPUerghtNSnbEj87A80CvEm0bGia8Is4qGerIvc/0?wx_fmt=png)

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