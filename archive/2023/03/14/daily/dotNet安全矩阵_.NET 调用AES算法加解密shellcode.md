---
title: .NET 调用AES算法加解密shellcode
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247487381&idx=1&sn=36155794410ae0998673457df46cfdb0&chksm=fa5aa178cd2d286e5378b9a9f5994c63af0ed42a33788decf8a4cb4d55a348d2791b413e1ca4&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2023-03-14
fetch_date: 2025-10-04T09:30:58.153189
---

# .NET 调用AES算法加解密shellcode

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9qFTicbhTwsqibM7XwXgWTdFUhS6ED5WLW76UkJibB0U24PntibuibYGpiaKSZvm8uJ6ra5JAsCicsa91KQ/0?wx_fmt=jpeg)

# .NET 调用AES算法加解密shellcode

专攻.NET安全的

dotNet安全矩阵

# 0x01 基本介绍

.NET使用AES（Advanced Encryption Standard）加密shellcode用于免杀，是一种提供了高级加密标准的算法，是一种对称密钥加密算法，加密和解密所使用的密钥是相同的，参数密钥Key：用于加密和解密数据的秘密密钥。初始化向量IV：用于初始化加密过程中的状态，例如下demo

```
byte[] aesKey = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10 };byte[] aesIV = { 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20 };
```

解密方法使用解密器对象decryptor.TransformFinalBlock方法解密

```
public static byte[] DecryptAES(byte[] key, byte[] iv, byte[] data)        {            using (Aes aes = Aes.Create())            {                aes.Key = key;                aes.IV = iv;
                using (var decryptor = aes.CreateDecryptor())                {                    return decryptor.TransformFinalBlock(data, 0, data.Length);                }            }        }
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9qFTicbhTwsqibM7XwXgWTdFGaUdcnBGjCic0p9jich9Kl5Cic7eehNDqE5CkichhFDFzLtTicqZF9ca7MA/640?wx_fmt=png)

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