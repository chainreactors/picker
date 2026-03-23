---
title: 第102天-Java反序列化漏洞：从入门到精通，一篇带你彻底搞懂！
url: https://mp.weixin.qq.com/s/-FS6jJn89xraKydRh4G7Kw
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:22:24.706116
---

# 第102天-Java反序列化漏洞：从入门到精通，一篇带你彻底搞懂！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Byhdgj3e9qtaGsoibVTRaOvasSicfDJcWwpbKdn0g9aGvVHCXJLsIzvibc0kqcHNwQe3jOv9ZC3QaLyQFKdeR0iaxKlQUZXfVxrk6W8OJdhDSM0/0?wx_fmt=jpeg)

# 第102天-Java反序列化漏洞：从入门到精通，一篇带你彻底搞懂！

原创

Сяо Яо
Сяо Яо

AlphaNet

![]()

在小说阅读器中沉浸阅读

嘿，未来的安全大神们！👋 你是否曾在代码审计时对 Java 的反序列化漏洞感到困惑？或者听说过 Log4j、Fastjson 的大名，却不清楚它们背后的攻击原理？

别担心！今天，让我们一起踏上探索 Java 反序列化漏洞的旅程。本文将采用 **“是什么-为什么-怎么做”** 的经典结构，从零开始，带你一步步揭开 Java 反序列化的神秘面纱，让你不仅知其然，更知其所以然。准备好了吗？Let's Go! 🚀

### 🧐 是什么：揭开反序列化的神秘面纱

首先，我们得搞清楚什么是序列化和反序列化。

* **序列化 (Serialization)**：简单来说，就是把程序中的 Java 对象（比如一个用户信息对象）转换成一串字节流。这些字节流可以轻松地存储在文件里，或者通过网络发送到另一台计算机。

* **反序列化 (Deserialization)**：顾名思义，就是序列化的逆过程。它把字节流重新转换回原来的 Java 对象，让程序可以继续使用它。

你可以把它想象成“打包”和“拆包”的过程。

```
// 这是一个可以被序列化的用户类
public class User implements java.io.Serializable {
    private String name;
    private int age;
    // ... 构造函数、getter/setter等 ...
}

// 序列化：将User对象“打包”成字节流
FileOutputStream fos = new FileOutputStream("user.dat");
ObjectOutputStream oos = new ObjectOutputStream(fos);
oos.writeObject(new User("Manus", 2));
oos.close();

// 反序列化：从文件“拆包”，还原成User对象
FileInputStream fis = new FileInputStream("user.dat");
ObjectInputStream ois = new ObjectInputStream(fis);
User user = (User) ois.readObject();
ois.close();
```

**如何快速识别？**

* **魔法数字**：Java 原生序列化后的数据，其字节流通常以 `ac ed 00 05` 这几个十六进制数开头。

* **Base64 编码特征**：如果对这串字节流进行 Base64 编码，你经常会看到以 `rO0AB` 开头的字符串。

### 💥 为什么：危险的反序列化

既然反序列化是 Java 的正常功能，为什么会变得危险呢？

**核心问题在于：程序过于信任接收到的数据。**

如果一个攻击者精心构造了一个恶意的字节流，并在其中“塞入”了能够执行恶意操作的代码（我们称之为“Gadget Chain”或“利用链”）。当服务器程序毫无防备地对这个字节流进行反序列化时，恶意代码就会在服务器上被触发执行，可能导致：

* **远程代码执行 (RCE)**：攻击者可以像操作自己的电脑一样控制你的服务器。

* **服务器权限被窃取**：网站被篡改，数据库被拖走。

* **内部信息泄露**：敏感数据和商业机密荡然无存。

这就像你收到一个快递，以为里面是本书，结果拆开包裹的瞬间，里面弹出一个会搞破坏的机器人！

### 🛠️ 怎么做：漏洞分类与攻防实践

Java 的反序列化漏洞主要可以分为两大类：**原生类反序列化** 和 **第三方组件反序列化**。

#### 1. 原生类反序列化漏洞

这类漏洞主要源于 Java Development Kit (JDK) 自带的类和接口。

* `ObjectInputStream.readObject()`: 这是最核心、最基础的反序列化方法。任何想要被序列化的类都必须实现 `java.io.Serializable` 接口。这也是绝大多数反序列化漏洞的入口点。

* `XMLDecoder`: 用于处理 XML 格式的序列化数据。如果程序使用它来解析不受信任的 XML 输入，也可能触发漏洞。

* `SnakeYaml`: 一个强大的 YAML 解析库，同样支持 Java 对象的序列化和反序列化。`Yaml.load()` 方法在处理恶意 YAML 文件时可能存在风险。

#### 2. 第三方组件反序列化漏洞

随着开发的复杂化，我们大量使用开源的第三方库（组件），这些库为了方便也提供了序列化功能，从而成为了漏洞的重灾区。

| 组件名称 | 简介 | 历史漏洞查询 | 常见触发函数 |
| --- | --- | --- | --- |
| **Log4j** | Apache 的日志记录框架 | 阿里云漏洞库-Log4j | `logger.error()`, `logger.info()` |
| **Shiro** | 流行的 Java 安全框架 | 阿里云漏洞库-Shiro | `CookieRememberMeManager` |
| **Jackson** | 顶级的 JSON 解析器 | 阿里云漏洞库-Jackson | `readValue()` |
| **XStream** | XML 序列化/反序列化库 | 阿里云漏洞库-XStream | `fromXML()` |
| **Fastjson** | 阿里巴巴开源的 JSON 解析库 | 阿里云漏洞库-Fastjson | `parseObject()`, `parse()` |

#### 深入剖析：JNDI 注入攻击

在许多高级的反序列化攻击中，**JNDI 注入** 是终极武器。

* **JNDI (Java Naming and Directory Interface)**：Java 命名和目录接口。你可以把它理解成一个“中介”，程序通过它来查找和访问各种资源，比如远程对象。

* **攻击原理**：攻击者通过反序列化漏洞，让服务器去访问一个恶意的 JNDI 服务（如 RMI 或 LDAP）。这个恶意服务会返回一个包含恶意代码的工厂类，服务器下载并执行后，攻击就完成了。

**JDK 的防御与绕过史：一场持续的攻防战**

Java 官方一直在努力修复 JNDI 注入的风险，但攻击者总能找到新的方法。

* **JDK 6u45 / 7u21 后**：默认禁止 RMI 远程加载类文件，提高了安全性。

* **JDK 6u141 / 7u131 / 8u121 后**：进一步限制 RMI 和 CORBA 协议，让这类攻击失效。但攻击者转向了 LDAP 协议。

* **JDK 6u211 / 7u201 / 8u191 后**：最终也限制了 LDAP 协议的远程加载，似乎堵住了所有路。

然而，道高一尺，魔高一丈。安全研究员们又发现了在特定条件下绕过这些版本限制的方法，这场攻防战仍在继续（绕过方法我们下期再讲 😉）。

### 🔍 总结：审计要点与实战工具

学习了这么多理论，我们来总结一下在实际工作中如何发现和利用这些漏洞。

#### 代码审计关键点 (Sink Points)

当你在审计 Java 代码时，如果看到以下这些函数在处理来自用户的、不受信任的输入，一定要提高警惕！它们就是反序列化漏洞的“引爆点”。

```
// 1. JDK 原生反序列化
ObjectInputStream.readObject()

// 2. XMLDecoder 反序列化
XMLDecoder.readObject()

// 3. Yaml 反序列化
Yaml.load()

// 4. XStream 反序列化
XStream.fromXML()

// 5. Jackson 反序列化
ObjectMapper.readValue()

// 6. Fastjson 反序列化
JSON.parse()
JSON.parseObject()

// 7. Shiro 反序列化 (通常在 rememberMe Cookie 中)
CookieRememberMeManager

// 8. Log4j (JNDI注入)
logger.error()
logger.info()
```

#### 必备实战工具

工欲善其事，必先利其器。以下是安全研究员在研究反序列化漏洞时常用的开源项目：

* **Yakit**: 一款强大的、一体化的网络安全单兵作战平台。

* **ysoserial**: 生成各种 Java 反序列化利用链（Gadget Chains）的“瑞士军刀”。

* **JNDI-Injection-Exploit**: 用于快速搭建恶意 JNDI 服务，配合 ysoserial 进行漏洞利用。

* **JYso**: 一款功能强大的反序列化利用工具。

* **java-chains**: 收集了各种 Java 反序列化利用链的研究项目。

---

### 🧠 结尾思考

恭喜你，坚持看到了这里！🎉 你已经对 Java 反序列化漏洞有了一个全面而深入的理解。

**核心要点总结：**

1. **本质**：反序列化是将字节流恢复为对象的过程，其危险在于信任了不可信的数据。

2. **分类**：分为 JDK 原生漏洞和第三方组件漏洞，后者在现代开发中更为常见。

3. **关键**：JNDI 注入是实现远程代码执行的终极手段。

4. **审计**：盯住 `readObject`, `parseObject`, `fromXML` 等关键函数是发现漏洞的核心。

现在，留给你一个思考题：**既然反序列化风险这么大，为什么我们不直接禁用它呢？在哪些业务场景下，序列化和反序列化又是不可或缺的呢？**

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