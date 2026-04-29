---
title: FortiWeb 针对 Java 幽灵比特位（Ghost Bits）漏洞防护策略
url: https://mp.weixin.qq.com/s/ET6QSQgcWUhEdsUWQHjjrA
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:07:30.597736
---

# FortiWeb 针对 Java 幽灵比特位（Ghost Bits）漏洞防护策略

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Tqbm08xcZ3icxP0sENbGVckJFrY9zlYbvgCuRAY0d7jpZGldJgQDIv75fichIt65nb1SoLNVfLr7GAiboubQbsSQia9ysa8lG5viaj23X2ibp6tvU/0?wx_fmt=jpeg)

# FortiWeb 针对 Java 幽灵比特位（Ghost Bits）漏洞防护策略

原创

剑思庭
剑思庭

IRTeam工业安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026 年 4 月，在 Black Hat Asia 2026 大会上，揭示了 Java 生态中一个系统性、长期被忽视的底层编码缺陷——"Ghost Bits（幽灵比特位）"，并证明攻击者可利用该缺陷对 WAF/IDS 等安全设备实现全面绕过，进而触发 SQL 注入、反序列化 RCE、文件上传、SMTP 注入、请求走私等多种高危攻击链。漏洞影响范围覆盖 Java 主流框架与中间件，利用门槛低。

Java 的 char类型为 16 位（2 字节），而 byte类型仅为 8 位（1 字节）。当 Java 代码通过 (byte)ch、ch & 0xFF、baos.write(ch)、DataOutputStream#writeBytes()等方式将 char转换为 byte时，高 8 位会被静默丢弃，只保留低 8 位，这一丢失的高位数据即被称为"幽灵比特位（Ghost Bits）"。

以汉字「爻」（U+2F58）为例：

爻  →  U+2F58  →  二进制：00101111 | 00111010

(byte) 转换后：高 8 位 0x2F 丢弃，低 8 位 0x3A → 'X'

攻击者可利用这一特性，将攻击 Payload 中的关键 ASCII 字符替换为经过精心选取的 Unicode 字符（其低 8 位与原字符一致），使 WAF 看到的是无意义的 Unicode 字符序列，而后端 Java 服务解码时高位截断还原为原始攻击载荷，从而绕过基于字符串特征的安全检测。

PoC:

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0OicavkqgX2gZmdMdsH8ETT4JdibhW3ibzCnUqoh0pSKeCUZLfRppFexarQSAodrUegOM5LhswREV4TfSWfCA9KTb2XskxFJAASuk/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

防护建议：

采用Fortiweb作为WAF防护，需要增加如下修改：

一、基础配置

1. 启用深度解码与 Unicode 规范化

路径：System > Config > Advanced

开启 Recursive URL Decoding（递归 URL 解码）

开启 Unicode Normalization（NFC/NFKC），强制将变形字符归一化为标准 ASCII

开启 IIS-specific Unicode decoding 兼容全场景 Unicode 编码

开启 Base64 Arg Decoding，覆盖参数隐写场景

2. 强制字节级截断检测

启用 Byte-level inspection，对 URL、参数、Cookie、 multipart 文件名做低 8 位提取

匹配规则：提取低 8 位后与 SQLi/XSS/ 路径穿越 / RCE 特征库二次比对

对 %uXXXX、\uXXXX 格式做强制解析，阻断隐写载荷

二、专项防护规则

1. URL 路径与参数防护

拦截含高 8 位随机 Unicode + 低 8 位攻击字符组合，如 U+2F58 → 截断为 :

规则匹配：[\u0100-\uFFFF]{1,}([;'"()\/\*+-]|union|select|exec|jsp)

动作：Alert+Deny，记录完整请求日志

2. 文件上传防护（防 .jsp 绕过）

对 multipart 文件名做低 8 位还原，禁止伪装后缀

黑名单：还原后为 .jsp/.jspx/.war 直接阻断

白名单：仅允许业务合法后缀（.jpg/.png/.pdf 等）

3. 请求头与 CRLF 注入防护

检测 Header 中隐写 \r\n 的 Unicode 字符，阻断请求走私、SMTP 注入

限制 Header 中非 ASCII 字符比例，超过阈值直接拦截

4. JSON / 反序列化防护

对 Jackson/fastjson 相关参数做字节级归一化

拦截含 BCEL、ClassLoader、\u 拼接反序列化载荷

三、日志与应急响应

1. 关键日志开启

记录：URL 归一化前后、参数低 8 位还原结果、规则命中详情

告警阈值：单 IP 5 分钟≥3 次 此特征触发自动封禁

参考链接：

https://i.blackhat.com/Asia-26/Presentations/Asia-26-Bai-Cast-Attack-Ghost-Bits-4.23.pdf

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Rfoz3XfSibgibn8pmk0u7W9BYeJ5Ru29zm2waJqGsGZ7IpWoOkiaanMy3QAseGuZRGHExSjk9KeOwarvlEsMLl0xw/0?wx_fmt=png)

IRTeam工业安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Rfoz3XfSibgibn8pmk0u7W9BYeJ5Ru29zm2waJqGsGZ7IpWoOkiaanMy3QAseGuZRGHExSjk9KeOwarvlEsMLl0xw/0?wx_fmt=png)

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