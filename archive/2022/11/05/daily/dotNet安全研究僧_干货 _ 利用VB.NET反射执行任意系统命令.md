---
title: 干货 | 利用VB.NET反射执行任意系统命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487017&idx=1&sn=7757c8b0e31035754427d74cf5be0c58&chksm=fa5aa0c4cd2d29d2c06c0880dd94c35710fecfa86210eab2c8a984309c0a418e13e9e2057d72&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2022-11-05
fetch_date: 2025-10-03T21:46:00.819441
---

# 干货 | 利用VB.NET反射执行任意系统命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9qHn4vl9dSASnJlYpuzuNsDMeuV6VOibS7qe9kOPxeF43wcnrELich1xehxgialFduJvUoGyZaE6ib6w/0?wx_fmt=jpeg)

# 干货 | 利用VB.NET反射执行任意系统命令

专攻.NET安全的

dotNet安全矩阵

# 0x01 介绍

VB.NET反射机制和C#大同小异，只在语法上稍微有些不同，利用Type.GetType类可以获得对象的类型，此包含对象的所有要素方法、构造器、属性等等，此类有6个重载方法，第一个参数指定程序集名typeName，后面两个布尔型参数分别为throwOnError, ignoreCase，表示是否抛出异常，忽略大小写，如下代码

```
System.Type.GetType("System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089", True, True)
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9qHn4vl9dSASnJlYpuzuNsXWK6xSMJ2Zt0j2XslQAI4b2gexUVX8TrUXuVTnhqpGcadA2zZcdiajQ/640?wx_fmt=png)

笔者关注到另外一个ReflectionOnlyGetType类，它与GetType类不同之处在于只是显示反射上下文内容，不能够执行代码

```
public static Type ReflectionOnlyGetType(string typeName, bool throwIfNotFound, bool ignoreCase)        {            StackCrawlMark stackMark = StackCrawlMark.LookForMyCaller;            return RuntimeType.GetType(typeName, throwIfNotFound, ignoreCase, reflectionOnly: true, ref stackMark);        }
```

最后用Activator.CreateInstance创建实例化对象执行反射，具体使用方法请跟随笔者一探究竟

## 1.1 使用方法

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9qHn4vl9dSASnJlYpuzuNsNV27F5MrWgEDDzwDPotJYQdsLA6yiar2hOV4dk6mEvUD5Hoxyeic41JQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9qHn4vl9dSASnJlYpuzuNsG47sc6pKqDD5gvd2EtRfTX7Gadd4WWbwIdjAgViawlJL34nFiay3zNQA/640?wx_fmt=png)

## 1.2 工具化

后续工具发布会发布在星球里，请关注dotNet安全矩阵星球

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9qHn4vl9dSASnJlYpuzuNsxsKOVjCwmkBtjN5gbnvp1aBJ8jdCgHic1RWTZlbR2H389HuMXKyV62w/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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