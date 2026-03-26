---
title: 第107天-Shiro 550 漏洞深度解析：无 CC 依赖？CB 链一招制敌！
url: https://mp.weixin.qq.com/s/2MjqRDp3BHZEn4x5Hpzhjw
source: Doonsec's feed
date: 2026-03-25
fetch_date: 2026-03-26T04:26:40.490234
---

# 第107天-Shiro 550 漏洞深度解析：无 CC 依赖？CB 链一招制敌！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Byhdgj3e9qsynia0gQwUHfc9Hf5ibvWrVMkwprLOqfqYh6J6lNluLSdsgIzyicQWQHPy1CEcGpLP6kK9bRh2ny1RDiaprJa8sqibS9iazIKWzFic2s/0?wx_fmt=jpeg)

# 第107天-Shiro 550 漏洞深度解析：无 CC 依赖？CB 链一招制敌！

原创

Сяо Яо
Сяо Яо

AlphaNet

![]()

在小说阅读器中沉浸阅读

🤔 引言：Shiro 的“新”弱点？

嗨，各位未来的白帽黑客和安全开发者！👋

当我们谈论 Java 反序列化漏洞时，`Apache Shiro` 和 `Commons Collections（CC）` 几乎是绑定的经典组合。但问题来了：

👉 **如果目标环境没有 CC 依赖怎么办？**

很多人会下意识认为“无解”。但真正的答案是：

> ❗ **依然可以打，而且更隐蔽。**

今天我们要讲的，就是一条实战价值极高的利用链：

> 🚀 **Commons Beanutils（CB）链**

它不依赖 CC，却依然可以实现 **RCE（远程代码执行）**，是进阶 Java 安全必须掌握的一条链。

---

## 1️⃣ 是什么：反序列化利用链三要素

在深入 CB 链之前，先建立一个核心模型👇

任何反序列化利用链，本质都由三部分组成：

---

### ➡️ 1. Source（入口点）

* 触发点

* 一般是 `readObject()` 方法

* 反序列化时自动执行

👉 本链入口：

```
PriorityQueue
```

---

### 🔗 2. Gadget（调用链）

* 一系列“合法类”的组合

* 利用方法调用串联执行路径

👉 本链核心：

```
BeanComparator
```

---

### 🎯 3. Sink（执行点）

* 最终危险操作发生的位置

* 通常是：

  + 反射

  + 类加载

  + 命令执行

👉 本链终点：

```
TemplatesImpl
```

---

### 📌 一句话总结：

```
PriorityQueue → BeanComparator → TemplatesImpl → RCE
```

---

## 2️⃣ 为什么：CB 链的核心原理

这条链之所以成立，依赖两个关键机制👇

---

### 🧠 关键点 ①：PropertyUtils 的“隐式调用”

`Commons Beanutils` 提供：

```
PropertyUtils.getProperty(obj, "name")
```

本质做的事情是：

```
自动调用 → obj.getName()
```

---

👉 攻击思路：

我们控制：

* obj = TemplatesImpl

* property = "outputProperties"

那么就变成：

```
TemplatesImpl.getOutputProperties()
```

✔️ 成功进入危险类

---

### 💣 关键点 ②：TemplatesImpl = 内置 RCE 引擎

这是整条链的“核弹级组件”。

调用路径：

```
getOutputProperties()
→ newTransformer()
→ getTransletInstance()
→ defineTransletClasses()
→ defineClass()
```

最终结果：

> ✅ 加载我们注入的恶意字节码
>
> ✅ 执行任意代码

---

## 💻 恶意 TemplatesImpl 构造（可滚动代码）

```
// 获取恶意类字节码
ClassPool pool = ClassPool.getDefault();
CtClass evilClass = pool.get("com.govuln.shiroattack.Evil");

// 创建 TemplatesImpl
TemplatesImpl obj = new TemplatesImpl();

// 写入恶意字节码
setFieldValue(obj, "_bytecodes", new byte[][]{
    evilClass.toBytecode()
});

// 必须字段（否则不会触发）
setFieldValue(obj, "_name", "pwn");
setFieldValue(obj, "_tfactory", new TransformerFactoryImpl());
```

---

📱 **说明：**

* 在公众号中，该代码块会自动支持左右滑动

* 不会换行，不会溢出页面

---

## 3️⃣ 怎么做：完整利用链执行流程

现在把链路拼起来👇

---

### 🔥 Step 1：入口触发

```
PriorityQueue.readObject()
```

反序列化触发

---

### 🔗 Step 2：堆重建触发 compare

```
heapify()
→ siftDown()
→ siftDownUsingComparator()
→ comparator.compare()
```

---

### ⚙️ Step 3：BeanComparator 执行

```
PropertyUtils.getProperty(o1, property)
```

👉 实际效果：

```
TemplatesImpl.getOutputProperties()
```

---

### 💥 Step 4：触发 RCE

```
getOutputProperties()
→ newTransformer()
→ defineClass()
→ 执行恶意字节码
```

---

## 🚀 完整调用链

```
PriorityQueue.readObject()
→ heapify()
→ siftDown()
→ siftDownUsingComparator()
→ BeanComparator.compare()
→ PropertyUtils.getProperty()
→ TemplatesImpl.getOutputProperties()
→ newTransformer()
→ defineClass()
→ 💥 RCE
```

---

## ✨ 核心总结

---

### ✅ 1. 利用链本质

| 组件 | 作用 |
| --- | --- |
| PriorityQueue | 入口 |
| BeanComparator | 调用桥 |
| TemplatesImpl | 执行 |

---

### ✅ 2. CB 链核心优势

* ❌ 不依赖 Commons Collections

* ✅ 更隐蔽

* ✅ 绕过部分防御

---

### ✅ 3. 攻击本质

> 利用“合法 API + 反射机制”构造非法执行路径

---

## 🧠 进阶思考

给你一个真正拉开差距的问题：

> ❓ 除了 PriorityQueue，还有哪些类可以作为 Source？

思考方向：

* 是否实现 `Serializable`

* 是否存在 `readObject`

* 是否能触发方法调用链

---

## 🎯 结尾

如果你能真正理解这条链，你已经进入了：

> 🧩 **Java 反序列化利用的中级阶段**

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