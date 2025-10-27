---
title: 浅谈android端的字符串加密
url: https://www.secpulse.com/archives/193005.html
source: 安全脉搏
date: 2022-12-07
fetch_date: 2025-10-04T00:38:48.556541
---

# 浅谈android端的字符串加密

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

# 浅谈android端的字符串加密

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[小道安全](https://www.secpulse.com/newpage/author?author_id=11697)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-12-06

11,853

背景

字符串加密是一个非常传统的代码保护方案，在android的逆向过程中会涉及到java代码和CC++代码，通常在对APP做逆向过程中第一步一般就是反编译后查看代码中是否有包含一些可以作为突破口分析的字符串信息。

作为开发者一般应用中的字符串信息都是保存相对敏感的信息，字符串一般信息会保存着如客户端和服务端通信信息，操作文件相关信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316959.png)

**（so部分的字符串加密）**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316960.png)

**(java部分的字符串加密)**

由于字符串信息中存储着很多关键的信息，因此在做逆向的过程中从字符串入手可以猜测、分析定位出一些关键的加解密算法、关键的逻辑结构。因此字符串也是一种提高被静态逆向分析的一个很重要的门槛。

字符串信息的加密的影响只到静态的逆向分析这一步，字符串信息信息在实际业务运行过程中必然需要进行对字符串的操作，那这个就涉及到了对加密字符串的解密过程。这个运行态也就是在对app进行利用动态调试分析过程中都是赤裸裸的展现出来。这是时候字符串的加密就显得苍白无力了。**因此可以通过反调试和字符串加密这两者的入门的动态和静态方式结合，稍微提高代码的安全性。**

字符串加密算法基础

**所谓字符串加密技术是指将一个信息(或称明文)经过加密钥匙及加密函数转换，变成无意义的密文，而接收方则将此密文经过解密函数、解密钥匙还原成原字符串。**

字符串加密免不了采用加解密的算法，加解密算法的加解密方式和加解密强度直接决定了被攻破的时间成本。

字符串加密算法有简单的异或方式；通用的AES、DES、RSA、Base64、MD5散列函数等等；相对有难度的自实现加解密算法、冷门的加解密算法。

不过一般情况下，作为开发者一般不太可能自己去造轮子写加解密算法，一般都是直接就套用网络上稳定的、标准的加解密算法。**其实如果从相对安全性来说，可以找那些冷门的加解密算法用于保护字符串。这样相对网络公开资料比较少，并且分析的人相对比较少，分析起来时间成本就相对比较高。**

下面就分析下so文件加密用的比较多的字符串加密是怎么实现的。

ollvm字符串加密原理

Ollvm中字符串加密的公开版本有很多个版本，并且每个版本功能实现虽然大同小异，但是各个版本也各有缺点。

**这些缺点有：**

**1、无法加密字符串数组；**

**2、无法加密unicode编码和非const的字符串数组；**

**3、无法加密全局char和wchar字符串常量和结构体变量。**

基于以上原因，实现自己定制修改字符串加密功能代码就显得很重要了。

下面就分析下ollvm中基于某版本字符串加密的实现和调用

Ollvm项目中，字符串加密实现主要功能在项目存储在如下的路径中

声明和实现的代码

ollvmincludellvmTransformsObfuscationStringObfuscation.h

ollvmlibTransformsObfuscationStringObfuscation.cpp

初始化随机数因子和调用字符串加密

ollvmlibTransformsIPOPassManagerBuilder.cpp

添加编译StringObfuscation.cpp文件

ollvmlibTransformsObfuscationCMakeLists.txt

**CMakeLists.txt配置要编译的StringObfuscation.cpp文件**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316961.png)

下面的声明的静态全局变量，主要是为了实现编译时候识别 **-mllvm -sobf**指令的标识,全局开关通过参数来判断是否要开启字符串加密。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-16703169611.png)

**随机数因子的初始化。**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316962.png)

在populateModulePassManager 函数中，新增挂载新的pass代码，这样就可以根据全局开关来判断是否启用当前pass。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316963.png)

**StringObfuscation.h文件分析**

这个函数就声明了createStringObfuscation函数，看起来非常简单，这个函数也就是这个字符串加密的关键函数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316964.png)

**StringObfuscation.cpp文件分析(基于Armariris版本的字符串加密)**

这个版本的加密效果：可加密所有类型的ANSI, UNICODE字符串常量, 但是无法加密字符串数组, 因为字符串数组的全局符号名不是.str开头。

这个文件中主要有字符串加密函数和字符串解密函数2个函数组成的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-16703169641.png)

上文截图代码根据.str和.str.名称判断是否为字符串，并且过滤掉特定区段：Llvm.metadata，\_\_objec\_methname不进行字符串加密。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316965.png)

上面截图中的代码，可以看到字符串加密的就是进行简单的字符串异或加密。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316966.png)

用于往字符串加密的程序插入以“.datadiv\_decode+随机数”为结构的加密函数，用于实现对字符串进行加密处理。

防止破解者能够快速识别是基于ollvm实现的字符串加密，可以重点修改下这个函数的实现和“.datadiv\_decode+随机数”的特征。

有了以上的关键调用和流程，那么就可以基于以上的流程和规则进行做字符串加密功能的定制实现了，可以通过添加一些逻辑代码加强字符串加密的强度。

ollvm字符串加密后表现

**1、直接用标准的ollvm的字符串加密**，在字符串信息和导出函数中和init\_arrayq区段会存在.datadiv\_decode，这种采用的是一个字节和一个字节进行随机异或的加密方式。

数据都存储在数据段中，程序运行前就是初始化的时候就将加密的字符串全部解密出来，等待着使用。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316967.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-16703169671.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316968.png)

**2、通过基于ollvm的源代码，简单修改定制olllvm的源码，将解密函数名字修改成为非标准的**，但是这种的字符串加密在init\_array区段中依然会有展示，只不过展示的是非标准的函数信息。这种加密也是通过疑惑的方式进行加密。

字符串数据都存储在数据段中，程序运行起来后就是初始化时候，就一次性全部将字符串解密。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-16703169681.png)

**3、通过基于ollvm的源代码进行定制，字符串信息都存储在.bss区段中**，程序运行初始化的时候并没有进行做解密，只有在程序运行使用到那里才会解密到那里。其它的没使用的字符串是没有进行解密的。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193005-1670316969.png)

小结

从字符串成为破解者第一道门槛的的痛点，在到字符串加密仅是为了提高破解者静态分析的成本的大背景下进行，全文大篇幅的主要是以ollvm这个项目中的字符串加密为主线进行展开的，展开的方向主要以加密的实现原理和加密后的表现形式。

对ollvm字符串的解密相信是对大家来说比字符串加密是更感兴趣，篇幅有限先以字符串加密进行简单做下原理性的分析，**后面再分享ollvm字符串解密**。

**本文作者：[小道安全](newpage/author?author_id=11697)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/193005.html**](https://www.secpulse.com/archives/193005.html)

Tags: [AES](https://www.secpulse.com/archives/tag/aes)、[Android](https://www.secpulse.com/archives/tag/Android)、[base64](https://www.secpulse.com/archives/tag/base64)、[C](https://www.secpulse.com/archives/tag/c)、[DES](https://www.secpulse.com/archives/tag/des)、[java](https://www.secpulse.com/archives/tag/java)、[MD5散列函数](https://www.secpulse.com/archives/tag/md5%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B0)、[RSA](https://www.secpulse.com/archives/tag/rsa)、[字符串加密](https://www.secpulse.com/archives/tag/%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%8A%A0%E5%AF%86)、[逆向](https://www.secpulse.com/archives/tag/%E9%80%86%E5%90%91)

点赞：
11
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Java反序列化：URLDNS的反序列化调试分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1689306075699-300x217.png)

...