---
title: .NET 调用 ShellExec_RunDLL 执行命令
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487390&idx=1&sn=f5caf13f12ca326bf8ce009433c82c7d&chksm=fa5aa173cd2d2865c18ade2da764070c526f34e08c801582d184616a0183db1519217e2bd9a5&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2023-03-15
fetch_date: 2025-10-04T09:36:04.835227
---

# .NET 调用 ShellExec_RunDLL 执行命令

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8k47aOMo838CGZrvp6AiaB57yeX0jcx4nkx8p3IibdIQflcQj55UPH8iaDcicFJXdb0ibZkVYp1A7pAIA/0?wx_fmt=jpeg)

# .NET 调用 ShellExec\_RunDLL 执行命令

专攻.NET安全的

dotNet安全矩阵

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8k47aOMo838CGZrvp6AiaB5Jw7yBGJ8iawrHrgZ20eqg9lu7EMbKryeAwmzHusEPfkMYykszEXMAWA/640?wx_fmt=jpeg)

# 星球优惠活动

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。经过运营团队成员商议一致同意给到师傅们最大优惠力度，**只需99元就可以加入我们。**

星球汇聚了行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布**很多高质量的.NET**安全资源，可以说市面上很少见，都是干货。其中主题包括**.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库**等等，后续还会倾力打造**专刊、视频**等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibHErRN3IhgSaicia7Rl5SF0plpcuicd0KG8Cn7vGczlBRtvSJvicWejH7TOro6AGLQ627SvVzxzBnphg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58UeoxTMuRezdHEJu6Hp08Xgm2F49cyBI1zlcj5XqLJK8zedWlUjibYmia3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=wxpic)

dotNet安全矩阵知识星球 — 聚焦于微软.NET安全技术，关注基于.NET衍生出的各种红蓝攻防对抗技术、分享内容不限于 .NET代码审计、 最新的.NET漏洞分析、反序列化漏洞研究、有趣的.NET安全Trick、.NET开源软件分享、. NET生态等热点话题、还可以获得阿里、蚂蚁、字节等大厂内推的机会

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