---
title: 干货分享 | 利用.NET回调函数执行任意命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487008&idx=3&sn=66fd2cced2a681ddfede9950706ff760&chksm=fa5aa0cdcd2d29db75c12019dc92cacc9579bc948d648c5cbbb47b336e2de0c46f0c0976128b&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2022-10-29
fetch_date: 2025-10-03T21:14:43.907480
---

# 干货分享 | 利用.NET回调函数执行任意命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicoCq4nLPC5FAcw9iaiaWHZHTSyujL1STyuQJU66SVnrRYY8FGY4nPpzf44SP6mePcq5PKLFulshMnw/0?wx_fmt=jpeg)

# 干货分享 | 利用.NET回调函数执行任意命令

专攻.NET安全的

dotNet安全矩阵

# 0x01 背景

说起回调函数大家一定首先想到php语言提供的call\_user\_func、call\_user\_func\_array等函数，但再.NET里也存在一个冷门的回调函数，它就是CallByName，位于：Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a，此DLL里包含了多个 方法可用于创建新进程。具体使用方法请跟随笔者一探究竟

## 1.1 使用方法

CallByName是个很灵活的函数。帮助说明：执行一个对象的方法，或者设置或返回一个对象的属性。通过名称来调用操作对象的属性和调用对象的方法。函数定义 CallByName(object ObjectRef, string ProcName, CallType UseCallType, params object[] Args)，如下图

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicoCq4nLPC5FAcw9iaiaWHZHT977JVy8DIhYpTz7MdYNJ5e192ITaAgMPobPwBmGookZm8wORlBu8Sw/640?wx_fmt=png)

```
ProcName 包含对象的属性名或方法名的字符串表达式。CallType 枚举类型的枚举成员，表示所调用过程的类型。CallType 的值可以是 Method、Get 或 Set。Args 包含要传递给所调用的属性和方法的参数。
```

其中CallType.Get返回对象的属性的值，CallType.Method可以调用对象的方法执行，反编译后的代码如下

```
switch (UseCallType)            {                case CallType.Method:                    return LateBinding.InternalLateCall(ObjectRef, null, ProcName, Args, null, null, IgnoreReturn: false);                case CallType.Get:                    return LateBinding.LateGet(ObjectRef, null, ProcName, Args, null, null);                case CallType.Let:                case CallType.Set:                    {                        Type objType = null;                        LateBinding.InternalLateSet(ObjectRef, ref objType, ProcName, Args, null, OptimisticSet: false, UseCallType);                        return null;                    }                default:                    throw new ArgumentException(Utils.GetResourceString("Argument_InvalidValue1", "CallType"));            }
```

实际可用的demo如下回调Process类的Start启动计算器：CallByName(Obj, "Start", CallType.Get, "calc")，图2

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicoCq4nLPC5FAcw9iaiaWHZHT1GoRHtlLmxdcqzztkZWDemc39ZOX0Qs9iclcq7Wibb9LgzeZWmKqEYBg/640?wx_fmt=png)

工具已打包感兴趣的师傅可以自行在星球里查看

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicoCq4nLPC5FAcw9iaiaWHZHT90Zsn9eTPXjk0VaqHYkwSrf55k4WoFSSQz6CsZssicxlzD5VI8QwBQg/640?wx_fmt=jpeg)

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