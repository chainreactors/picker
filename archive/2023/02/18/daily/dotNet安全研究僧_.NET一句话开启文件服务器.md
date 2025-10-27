---
title: .NET一句话开启文件服务器
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487239&idx=1&sn=e35dc58cdec0192cb9a9a3729e76c7f1&chksm=fa5aa1eacd2d28fcaad0b776f8cbcb9bf7579539ed1432a6268601f055f3af302bcb83f19303&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2023-02-18
fetch_date: 2025-10-04T07:23:18.723095
---

# .NET一句话开启文件服务器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8xUtGf3nJUQuIDnnwJ9Bia0nXI1Q0gOU8icONI7FdNGYWMF49KXKrgK0iaBiatAj8QpAwKmZCYicDb2Mg/0?wx_fmt=jpeg)

# .NET一句话开启文件服务器

专攻.NET安全的

dotNet安全矩阵

# 0x01 .NET一句话开启文件服务器

```
dotnet tool install --global dotnet-serve；
```

安装完成之后通过 cmd 控制台进入到需要发布共享的文件夹里面，进入到 D:\WebForm\ 文件夹，开启命令如下

```
dotnet serve -p 8088
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8xUtGf3nJUQuIDnnwJ9Bia0xzMlEPicq5lj8XpjQ6yVUzdicH8QV0Y8n2JSdq1MHrztxiaf6G3TWQ6zw/640?wx_fmt=png)

默认会使用 8080 端口，上面代码的 -p 就是指定端口为 8088如果接受默认端口，那么可以使用 dotnet serve 开启服务器，此时用浏览器访问 http://127.0.0.1:8088就可以看到文件了

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8xUtGf3nJUQuIDnnwJ9Bia0MNCRkQE6zDwQSZBFsia2D0GkKCp1eHibsicqjXnhuZoggKrRSJYicwqicGA/640?wx_fmt=png)

下载地址：https://github.com/natemcmaster/dotnet-serve

# 星球优惠活动

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。经过运营团队成员商议一致同意给到师傅们最大优惠力度，**只需99元就可以加入我们。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibDrGhv0rKz4CRLm152SnCkETPR6LWmyhiccY1ufjKmWB9qia1vPukNHnh2Rg5sHFGobrzX0FS1Zd0Q/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布**很多高质量的.NET**安全资源，可以说市面上很少见，都是干货。其中主题包括**.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库**等等，后续还会倾力打造**专刊、视频**等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibHErRN3IhgSaicia7Rl5SF0plpcuicd0KG8Cn7vGczlBRtvSJvicWejH7TOro6AGLQ627SvVzxzBnphg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58UeoxTMuRezdHEJu6Hp08Xgm2F49cyBI1zlcj5XqLJK8zedWlUjibYmia3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

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