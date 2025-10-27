---
title: 推荐 | 基于Roslyn实现C#脚本代码执行
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247486693&idx=1&sn=fa9c3e02922c098748e9f5aeef4b7b36&chksm=fa5aa208cd2d2b1e8fde199fe6520edef65d69731b7b2f62350d9045d2a26f12446984495746&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2022-10-19
fetch_date: 2025-10-03T20:16:33.567454
---

# 推荐 | 基于Roslyn实现C#脚本代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicFnzoBLCC3n5u7eicEFtOa30WcmmlsEVLK3wBzhibgkQjn6cKWlFlmYSwwRlcBSK0YKPPWDyQRDrGw/0?wx_fmt=jpeg)

# 推荐 | 基于Roslyn实现C#脚本代码执行

专攻.NET安全的

dotNet安全矩阵

# 0x01 背景

有些情况下需要在程序运行期间动态执行C#代码，从C# 6 开始利用Roslyn编译器可以方便地在我们的程序中动态编译代码，具体的版本信息是.NET 4.6及.NET Core均支持，假定在渗透过程中目标站点已经具备了Roslyn环境时，可以尝试使用CSharpScript.EvaluateAsync方法执行需要编译的代码内容，编译时需引入ScriptOptions.Default.WithReferences提供必备的程序集文件，执行后效果如图

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Yicc7ldqBSFNuDCwTUqTiaUoSEuVibFuXtiakHOGBUGfibbH3QAxfffWYCwnNb26DaCw91Ue4iayGEAVLxw/640?wx_fmt=png)

## 1.1 原理分析

查看站点是否安装了Roslyn环境，一般只需关注是否存在Microsoft.CodeAnalysis.CSharp.dll，通常在代码里会引入以下命名空间，

```
using Microsoft.CodeAnalysis.CSharp.Scripting;using Microsoft.CodeAnalysis.Scripting;
```

EvaluateAsync以异步线程任务的方式返回脚本执行后的结果，第二个参数项ScriptOptions.Default.WithReferences 表示引入的程序集

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicFnzoBLCC3n5u7eicEFtOa3LnTm6Dl8rW09WcmqGicibmuQvqwjTA93WiawHW4AykYEg7JwmxfWd8f5g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicFnzoBLCC3n5u7eicEFtOa3Cvvd5iaMdZzrbhGxooMGjLPbd0dYWwv8L71HzfwMOiaMdPqqPhqDLnMg/640?wx_fmt=png)

## 1.2 使用场景

以弹出计算器作为demo，但这样在实战中看不到命令返回的结果，所以笔者改造后如下图

```
await CSharpScript.EvaluateAsync("System.Diagnostics.Process.Start(\"calc\")", ScriptOptions.Default.WithReferences(typeof(System.Diagnostics.Process).Assembly));
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicFnzoBLCC3n5u7eicEFtOa3krJ8qoNjLLoaw75ia3nrtKbwD7wd3cib5LibfdZxHGj7Uz7xcQ4O2EVYA/640?wx_fmt=png)

**脚本工具已打包在星球，感兴趣的师傅可以自行研究测试。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicFnzoBLCC3n5u7eicEFtOa3riazPtLepc46hyTyMUPJlAoicIozSSliaOkR5m7SUVU6wiafC9ib38aCdEw/640?wx_fmt=jpeg)

# 0x02 星球优惠活动

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。**星球提供50元代金劵，师傅们先到先得噢！扫描星球亮点里的二维码即可加入我们。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibuxMvdKPXjjMPhQjaCh2vwvLYKIWu5xbbR52F3JahJNvjfDw1jd3gy5Kgwh92quxrtlluFs0sIdQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布**很多高质量的.NET**安全资源，可以说市面上很少见，都是干货。其中主题包括**.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库**等等，后续还会倾力打造**专刊、视频**等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibHErRN3IhgSaicia7Rl5SF0plpcuicd0KG8Cn7vGczlBRtvSJvicWejH7TOro6AGLQ627SvVzxzBnphg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58UeoxTMuRezdHEJu6Hp08Xgm2F49cyBI1zlcj5XqLJK8zedWlUjibYmia3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

dotNet安全矩阵知识星球 — 聚焦于微软.NET安全技术，关注基于.NET衍生出的各种红蓝攻防对抗技术、分享内容不限于 .NET代码审计、 最新的.NET漏洞分析、反序列化漏洞研究、有趣的.NET安全Trick、.NET开源软件分享、. NET生态等热点话题、还可以获得阿里、蚂蚁、字节等大厂内推的机会.

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