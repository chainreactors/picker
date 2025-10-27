---
title: 推荐 | 基于C#实现数据库连接字符解密工具
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247486642&idx=4&sn=55055fba621991a2d04a576927e2ea00&chksm=fa5aa25fcd2d2b49eb949bba480bf041a68a1fcbc9456185601a981c3a33c5116642a0d40047&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2022-10-15
fetch_date: 2025-10-03T19:57:37.818474
---

# 推荐 | 基于C#实现数据库连接字符解密工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicK9iaOeDHJDic7lHJ1ggZGu1LoQqpNGQI8W3kvMPlm9dLuh0zLTYENoLPvibzLnNIRxJ28Q5y4NGkhg/0?wx_fmt=jpeg)

# 推荐 | 基于C#实现数据库连接字符解密工具

专攻.NET安全的

dotNet安全矩阵

# 0x01 背景

.NET安全矩阵群有位师傅问起web.config里数据库连接字符串被编码加密，如何解密得到原始字符串

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK9iaOeDHJDic7lHJ1ggZGu1BWc8G8UwGVaZS9gjf4V5otp35KwL9IhWQDrfZeRV4N8NiaPy6OIXJWA/640?wx_fmt=png)

之前星球和群里也分享过一些关于webconfig加解密的方法，但还有一类通过DESCryptoServiceProvider类实现对称加解密方式，今天我们就来聊一聊此类场景下的解密

## 1.1 基本原理

通过DESCryptoServiceProvider实现对称加密，常见的私钥数据加密时需提供8位长度的key，当解密时需反编译或配置文件里找到key，即可还原文本内容。如果还原失败可能的原因在于使用IV偏移了初始化向量，工具代码实现如下

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK9iaOeDHJDic7lHJ1ggZGu1MnlWRLS4VDX2TI6x8dMD54u7bCURMOomyshR138vxkaSxwxIRB7iaLg/640?wx_fmt=png)

## 1.2 使用方法

解密命令如下：SharpofDecryptWebconfig.exe -Dec 加密的连接字符串 自定义8位长度的密钥

```
SharpofDecryptWebconfig.exe -Dec B6P3WI+PnYVgqe14RevoL7iZ+ULeDITsH2BzmvCsjwYo6RerAShpTSDRyVN9HrAc1FXlj+fPqio= 12345678
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK9iaOeDHJDic7lHJ1ggZGu1HTaxjia5ZibxFmZQltMRRHnRe9W4qYQvgU8oobSbK97icewicwZtcZOoibA/640?wx_fmt=png)

加密命令改成：SharpofDecryptWebconfig.exe -Enc

```
SharpofDecryptWebconfig.exe -Enc server=.;Database=MSSQL;User ID=sa;Password=123456 12345678
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK9iaOeDHJDic7lHJ1ggZGu17fuUicUaGhDSzSGVVasMowtmqmD5KWkHzoRV9bJBhCM9jRCm273brsg/640?wx_fmt=png)

**工具已打包感兴趣的师傅可以自行研究测试。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9ibUfNLafYZnhX1rv67zXhOq9aB2aibISpgBe5yfIlmzHjx8iakhrbialgyAlyib0qx6ZibfiaOUOichD3Mw/640?wx_fmt=jpeg)

**免责声明** 由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号dotnet安全矩阵及作者不为**此**承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

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