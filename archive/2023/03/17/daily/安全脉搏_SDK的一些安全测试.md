---
title: SDK的一些安全测试
url: https://www.secpulse.com/archives/197686.html
source: 安全脉搏
date: 2023-03-17
fetch_date: 2025-10-04T09:50:27.001842
---

# SDK的一些安全测试

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# SDK的一些安全测试

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[编码安全](https://www.secpulse.com/newpage/author?author_id=48435)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-03-16

12,445

**SDK安全要求**

在android应用开过过程中，SDK是android应用中不可缺少的一部分，通过集成各种第三方的SDK可以减少APP应用开发的工作量。但是在APP应用中集成各种第三方SDK可能存在各种安全的风险，除了一些基础的安全问题还有一些致命的异常崩溃的安全问题，通过验证测试分析sdk的安全风险尽可能规避安全风险。

下面来源：<<移动互联网应用程序SDK安全技术要求及测试方法>> 文档中，它罗列出来sdk中的安全基本要求：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955889.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-16789558891.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955894.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955895.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955897.png)

**SDK安全测评**

SDK可能存在的安全风险包括：

1. 这些安全风险不仅包括会出现sdk中可能存在代码漏洞，这会促使APP应用容易受到攻击；
2. 第三方SDK没有在维护更新或无法使用；
3. 使用第三方免费SDK可能存在知识产权的问题。

所以在sdk集成之前很有必要对sdk进行测试验证分析，验证测试方式：

1. 可以检测第三方依赖性中的漏洞的插件(例如：dependency-check-gradle)在应用接入SDK前进行验证测试sdk是否存在安全漏洞；
2. 也可以通过jeb或者jadx将sdk的代码反编译分析是否存在可能的漏洞；
3. 对sdk的隐私数据保护、访问权限的控制进行测试；
4. 对sdk的行为LOG和调用栈LOG进行测试。

**SDK的基本安全测评：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955898.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955900.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955904.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955905.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955906.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955907.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955909.png)

**SDK数据存储风险测评**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955911.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955912.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955913.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955914.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955915.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955917.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-16789559171.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955918.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955925.png)

**SDK数据交互风险测评**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955929.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955932.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955933.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955934.png)

**SDK重要组件测评**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955935.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-16789559351.png)

**SDK代码及资源文件安全测评**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955937.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-16789559371.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955939.png)

**SDK的异常处理**

当SDK代码进入异常或者错误状态时，就会发生异常。java和C++代码都可能引发异常。通过验证测试异常是为了确保应用将处理异常并转换为安全状态，而不是通过UI界面或日志记录机制公开敏感信息。

1、确保SDK使用精心设计和统一的方案进行管控代码；

2、通过创建适当的空检查、绑定检查等来规划标准 RuntimeException（例如 NullPointerException、IndexOutOfBoundsException、ActivityNotFoundException、CancelException、SQLException）。应有意抛出 RuntimeException 的子项，并且应由调用方法处理意向。

3、确保对于每个非运行时 Throwable，都有一个适当的 catch 处理程序，最终正确处理实际异常。

4、引发异常时，确保SDK程序具有用于导致类似行为的异常的集中处理程序。这可以是静态类。对于特定于方法的异常，请提供特定的 catch 块。

5、确保sdk在其 UI 或日志语句中处理异常时不会公开敏感信息。确保异常仍然足够详细，可以向用户解释问题。

6、确保在执行 finally 块期间，始终擦除高风险应用程序处理的所有机密信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197686-1678955940.png)

下面几种方式可以对SDK中异常进行动态分析：

1、使用Xposed或者frida工具进行hook方式，并使用意外值调用它们，或使用意外值（例如空值）覆盖现有变量；

2、在Android应用程序的UI界面字段中键入意外值。

3、使用应用程序的意图、公共提供程序和意外值与应用程序交互。

4、篡改网络通信或应用程序存储的文件。

**0结束1**

参考材料：<<移动互联网应用程序SDK安全技术要求及测试方法>> 文档

**本文作者：[编码安全](newpage/author?author_id=48435)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197686.html**](https://www.secpulse.com/archives/197686.html)

Tags: [android应用](https://www.secpulse.com/archives/tag/android%E5%BA%94%E7%94%A8)、[SDK](https://www.secpulse.com/archives/tag/sdk)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![APP隐私合规自查关键点](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686723...