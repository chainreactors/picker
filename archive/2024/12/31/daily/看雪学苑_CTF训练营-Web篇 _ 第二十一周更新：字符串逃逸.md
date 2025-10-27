---
title: CTF训练营-Web篇 | 第二十一周更新：字符串逃逸
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587900&idx=3&sn=9eda07f313d525b1598297a32ee31ea2&chksm=b18c227686fbab60f9ad036f444f16462d54e3f2a0d8af82e9eaa7346c3eea32914fc5b51045&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-31
fetch_date: 2025-10-06T19:41:05.308447
---

# CTF训练营-Web篇 | 第二十一周更新：字符串逃逸

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ESzLNmAcDTHtzjK0qFJLr6mmswvCm0KoZKbUQc9zAdbTOm3Ar1my3edyOsAstVPciazG3LCEAFd7A/0?wx_fmt=jpeg)

# CTF训练营-Web篇 | 第二十一周更新：字符串逃逸

看雪课程

看雪学苑

本周我们将在上一周的基础上对序列化的知识点进行深入的学习，我们将细致的学习Phar反序列化及其原理；此外我们将看一个非常经典的反序列化利用方式，字符串逃逸。经过本周学习，相信同学们将对反序列化有了更为深入的理解。

第二十一周（12月25日更新）  反序列化漏洞（二）Phar反序列化和字符串逃逸

第二章 字符串逃逸

视频2-1 什么是逃逸

视频2-2 变长逃逸和变短逃逸

视频2-3 实战场景和规律总结

欢迎来到《CTF训练营-Web篇》！随着互联网的普及与发展，网络安全也越发成为人们关注的焦点。而在网络安全中，Web安全无疑是其中的一个重点领域。

该课程以CTF比赛中的Web安全为核心，包含了丰富的Web安全攻击和防御知识，帮助学员了解常见的网络攻击方式并掌握一些基本的渗透测试和漏洞利用技术。

通过学习该课程，您将了解常见于CTF比赛中的Web安全攻击手段，例如SQL注入、XSS攻击等。同时，您还将学习如何使用各种工具和技术支持漏洞挖掘、渗透测试、攻防演练等行业实际应用。

学习本课程，你将获得全面的Web安全知识体系，提高实际操作能力，为你今后从事网络安全相关工作打下坚实的基础。

快来开启《CTF训练营-Web篇》的学习之旅吧！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HphDmwaicmoJsxhtILouhU0mS7wPYKnA0KSD33gsMAXicIJRVLHUiauwHZIqNo0ubbN4QnBSqB2lsYA/640?wx_fmt=jpeg)

**课程简介**

本课程面向希望在Web方向发展的学员，旨在通过由浅入深的课程帮助学员掌握系统化的Web安全知识和良好的解题能力。

由于是体系课，我们将系统化的来学习，因此讲师将本课程分为4大阶段！

**第一阶段（入门篇）：**学习CTF中Web安全需要掌握的最基本的知识、对PHP应用的一类漏洞进行讲解、完成对PHP语言的基础学习。

**第二阶段（基础篇）：**完成对Web安全中一个十分经典，在CTF竞赛中出镜率也极高的Web漏洞的学习——SQL注入。

**第三阶段（进阶篇）：**对一些常见的Web漏洞学习，包括命令/代码执行、文件上传和文件包含。

**第四阶段（强化篇）：**对那些喜欢在难题中出现的考点进行系统化的学习，包括PHP反序列化、SSRF、XXE等，

课程会将理论和实践相结合，帮助学员最大化地完成课程目标。

**知识体系/目录**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GMjqO82AGRWSJrIX9UmhlnVazYxiaOFLobSlvfhQhXcchenGwM5icVLQCAQsC8OlOubJUvEYrcreEg/640?wx_fmt=png)

\*下滑导航栏查看具体目录![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaajvl7fD4ZCicMcjhXMp1v6UibM134tIsO1j5yqHyNhh9arj090oAL7zGhRJRq6cFqFOlDZMleLl4pw/640?wx_fmt=png)

**阶段一：入门 — 初入Web安全世界**

**第1周：Web安全概览、环境配置与工具介绍**

第1章  Web安全概览（试看）

* 视频1-1  什么是WEB
* 视频1-2  什么是WEB安全
* 视频1-3  如何开始学习WEB安全

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HzjnnQrCEbgmosjEoX1d6rs56nl4ZJXsVArol2Phnq4NmJc7jynm45ib7UQO5NBCibfJxhj0RoEEEg/640?wx_fmt=png)

第2章 工具介绍与环境搭建

* 视频2-1 PHP环境搭建与PHPStudy
* 视频2-2 Java环境搭建、Burpsuite抓包与HTTP
* 视频2-3 Python环境搭建、Dirsearch与SQLMap

**第2周：Web渗透测试的灵魂：信息搜集**

第1章  渗透测试与信息收集

* 视频1-1  什么是渗透测试
* 视频1-2  信息搜索要做些什么
* 视频1-3  信息搜集工具与技巧一览

第2章  CTF中的信息搜集

* 视频1-1  信息搜集在CTF中的体现
* 视频1-2  CTF中做题的CheckList
* 视频1-3  信息搜集相关习题精解

**第3周：让开发者如履薄冰的一些“PHP黑魔法”**

第1章  PHP与黑魔法（一）

* 视频1-1  入门PHP
* 视频1-2  弱类型概念与strcmp问题
* 视频1-3  哈希弱比较问题
* 视频1-4  is\_numeric弱比较问题
* 视频1-5  json\_decode弱比较问题
* 视频1-6  intval函数问题
* 视频1-7  preg\_match函数问题

第2章  PHP与黑魔法（二）

* 视频2-1  函数与get\_defined\_vars函数
* 视频2-2  课时6-2extract函数变量覆盖
* 视频2-3  3parse\_str变量覆盖
* 视频2-4  $变量覆盖
* 视频2-5  内置类简单介绍
* 视频2-6  请求参数解析问题

**阶段二：基础 — 带你16小时玩转SQL注入**

**第4周：SQL注入基础(一)原理与回显注入方式**

第1章  SQL基础与SQLi原理

* 视频1-1  MySQL简介
* 视频1-2  MySQL基础\_语法\_函数\_数据库
* 视频1-3  使用PHP代码与MySQL联动
* 视频1-4  使用PHP操作数据库
* 视频1-5  SQLi原理

第2章  SQLi基础、联合注入和报错注入

* 视频2-1  SQLi相关函数补充

  视频2-2  SQLi全局变量补充与information\_schema库操作
* 视频2-3  字符-数字型注入
* 视频2-4  联合注入
* 视频2-5  大整数报错和Xpath报错注入

       视频2-6  主键重复报错注入

**第5周：SQL注入基础(二)非回显注入方式**

**第1章节 布尔盲注**

视频1-1回显注入与盲注的区别

视频1-2 学习盲注前的基本tricks复习

视频1-3 对于非回显注入的insight

视频1-4 布尔盲注的攻击流程

**第2章 时间盲注**

视频2-1 时间盲注和布尔盲注

视频2-2 五种时间盲注的方式

视频3-3 例题精解和自动化脚本编写

本章靶场实例

**第3章 习题讲解**

习题课1 SQLi测试步骤和万能密码

习题课2 两道Union&报错注入

习题课3 如何编写更为高效的SQLi脚本

**第6周：SQL注入基础(三)一些其他的注入方式**

**第7周：SQL注入基础（四）使用工具进行注入**

**第8周：SQL注入进阶（一）二次注入、堆叠注入和绕过技巧**

**第9周：SQL注入进阶（二）SQLi到GetShell和MSQQL注入**

**第10周：SQL注入进阶（三）PostgreSQL和MongoDB注入**

**第11周：SQL注入进阶（四）注入技巧与思路拓展**

**阶段三：进阶 — 深入探讨CTF中常见的“简单”漏洞**

**第12周：命令/代码执行（一）原理和基础知识**

**第13周：命令/代码执行（二）Bypass技巧**

**第14周：命令/代码执行（三）disable\_function和openbase\_dir的突破**

**第15周：命令/代码执行（四）ThinkPHP RCE漏洞详解**

**第16周：文件上传（一）原理、常见检测绕过和解析漏洞**

**第17周：文件上传（二）补充与真题演练**

**第18周：文件包含（一）原理与前置知识**

**第19周：文件包含（二）一览包含技巧**

**阶段四：强化 — 迈向主力Web选手之路**

**第20周：反序列化漏洞（一）原理、基础知识和POP链**

**第21周：反序列化漏洞（二）Phar反序列化和字符串逃逸**

**第22周：反序列化漏洞（三）ThinkPHP反序列链分析**

**第23周：反序列化漏洞（四）Laravel反序列化链分析**

**第24周：SSRF（一）原理与基础利用**

**第25周：SSRF（二）Soap类SSRF、Gopher在SSRF中的妙用**

**第26周：XXE（一）原理和前置知识**

**第27周：XXE（二）Blind XXE和例题讲解**

**第28周：SSTI——原理、绕过与例题讲解**

**第29周：前端安全（一）同源策略攻防**

**第30周：前端安全（二）XSS原理、绕过与例题讲解**

**第31周：前端安全（三）CSRF与JSONP安全问题**

**第32周：Node.js与原型链污染**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GMjqO82AGRWSJrIX9UmhlnOiabMZLF73Tuv93kgic12jDzINmh9yv1DGMbvk7nRt8bkednbxHbEpyw/640?wx_fmt=png)**

**课程收获**

1、掌握Web安全学习方法

2、具备参与各大线上或线下比赛的能力

3、体系化的Web安全知识

**立即学习**

*![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HzjnnQrCEbgmosjEoX1d6rWDibFibjbAtlNpbVjDMwqElh5mVvmocwMN61cibKicURQaZ92WibUSibeOcQ/640?wx_fmt=png)*

**《CTF训练营-Web篇》**

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GMjqO82AGRWSJrIX9Umhlnc7OXwHtBqXEOBenoJ780G1rHHfuO1O8HlKKsR3me8gF357g4E7Wiabw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GMjqO82AGRWSJrIX9Umhlnc7OXwHtBqXEOBenoJ780G1rHHfuO1O8HlKKsR3me8gF357g4E7Wiabw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GMjqO82AGRWSJrIX9Umhlnc7OXwHtBqXEOBenoJ780G1rHHfuO1O8HlKKsR3me8gF357g4E7Wiabw/640?wx_fmt=gif)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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