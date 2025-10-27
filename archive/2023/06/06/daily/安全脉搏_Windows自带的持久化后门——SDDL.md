---
title: Windows自带的持久化后门——SDDL
url: https://www.secpulse.com/archives/201392.html
source: 安全脉搏
date: 2023-06-06
fetch_date: 2025-10-04T11:46:09.228270
---

# Windows自带的持久化后门——SDDL

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

# Windows自带的持久化后门——SDDL

[工具](https://www.secpulse.com/archives/category/tools)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-06-05

19,093

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201392-1685958842.png)

## 0x01引言

前段时间在小蓝鸟上看到一个几乎不见的持久化后门--SDDL，然后就看着评论学习着，越看越迷茫就去查了查资料。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201392-1685958843.png "null")

## 0x02 Windows中的安全模型

当 Windows 中的用户或进程尝试访问系统中的资源时，系统会使用访问令牌来标识这些用户或进程。访问令牌包括一组安全标识符（SID）、用户特定的数据和访问权限。每个用户都有一个唯一的 SID，它用于标识该用户。

访问控制列表（ACL）是一组安全描述符，用于控制对对象的访问。ACL 中包含一条条 ACE（访问控制项），每个 ACE 都描述了一个安全主体（如用户、组或计算机）对对象的访问权限。

Windows 中的安全模型通过这些基本元素来实现对资源的保护。当访问令牌中包含的 SID 与 ACL 中的 ACE 相匹配时，访问将被允许。否则，访问将被拒绝。

访问控制是 Windows 安全模型中的一个关键方面，它允许管理员通过配置 ACL 控制对资源的访问。这种方法能够提供高度的安全性，但需要仔细规划和管理，以确保正确地保护系统和应用程序。

当一个线程尝试去访问一个对象时，系统会检查线程持有的令牌以及被访问对象的安全描述符中的DACL。先查询类型为DENY的ACE，若命中且权限符合则访问拒绝；未命中再在ALLOWED类型的ACE中查询，若命中且类型符合则可以访问。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201392-1685958844.png "null")

总之，ACL的组成结构包含了一系列访问控制项，每个访问控制项都包含了标识符、访问掩码、ACE类型和审计标志等信息。通过ACL，可以控制对象的访问权限，从而保护系统的安全性。

## 0x03DACL

#### 1、概念和作用

DACL指的是Discretionary Access Control List，也就是自主访问控制列表。它是Windows中的一种安全机制，用于控制对象（如文件、目录、注册表项等）的访问权限。是一组ACE（Access Control Entry，访问控制项）的集合，每个ACE对应一个用户或用户组，并定义了该用户或用户组在对象上所具有的访问权限。DACL中的ACE分为Allow和Deny两种类型，Allow表示允许访问，Deny表示拒绝访问。在Windows中，每个对象都有一个DACL，用于控制哪些用户可以访问该对象。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201392-1685958845.png "null")

#### 2、格式和语法

DACL的格式和语法基于SDDL（Security Descriptor Definition Language），SDDL是一种字符串表示形式，用于描述安全描述符和访问控制列表。以下是SDDL语法的基本格式：

cssCopy code

`D:(A;;[Access Type];[Security Identifier])`

其中，D:表示这是DACL的SDDL字符串，A表示ACE中的对象类型，Access Type表示访问权限的类型，Security Identifier表示允许或拒绝访问的安全标识符（SID）。

Access Type包括以下部分：

* • A：代表允许对对象的访问。
* • D：代表拒绝对对象的访问。
* • OA：代表允许对对象的所有者访问。
* • OD：代表拒绝对对象的所有者访问。
* • GA：代表允许对对象的组访问。
* • GD：代表拒绝对对象的组访问。因此，一个完整的DACL SDDL字符串可能如下所示：

cssCopy code

`D:(A;;GA;;;WD)(A;;GA;;;SY)(A;;0x1201bf;;;S-1-5-32-544)`

其中，这个DACL允许组Everyone和系统用户具有完全访问权限，并且允许本地管理员组具有包括删除和修改权限的特定访问权限。

## 0x04、SDDL

#### 1、概念和作用

SDDL（Security Descriptor Definition Language）是一种描述Windows安全描述符的语言，它用于描述Windows安全对象的安全描述符，包括访问控制列表（ACL）、安全标识符（SID）、安全描述符的所有者和主要组等。

SDDL的作用主要有以下几个方面：

1. 1. 显示安全描述符信息：使用SDDL可以将安全描述符转换为易读的字符串形式，从而方便用户查看和理解其中的信息。
2. 2. 编辑安全描述符：SDDL提供了一种统一的方式来编辑安全描述符的信息，用户可以使用SDDL语法修改安全描述符的内容，以实现对安全对象的访问控制。
3. 3. 传输安全描述符：SDDL可以将安全描述符的信息以字符串的形式传输，以方便在不同的系统之间共享安全描述符的信息。SDDL语言结构非常灵活，可以用于描述多种安全对象，包括文件、目录、注册表、命名管道等。

#### 2、语法和格式

SDDL（Security Descriptor Definition Language）是一种描述安全描述符（Security Descriptor）的语言，用于在Windows中定义和修改对象的安全描述符，包括访问控制列表（ACL）、SACL和安全描述符的所有者和主要组。

SDDL语法由多个段组成，每个段用分号分隔。下面是一个包含所有段的示例：

cssCopy code

```
O:SYG:SYD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SO)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;CR;;;AU)(A;;CCLCSWRPLOCRRC;;;PU)(A;;CCLCSWRPLOCRRC;;;SY)
```

每个段表示安全描述符的一个组件，以下是每个段的含义：

* • O：安全描述符的所有者。
* • G：安全描述符的主要组。
* • D：DACL段，表示对象的访问控制列表。
* • S：SACL段，表示对象的安全审核策略。
* • A：ACE段，表示允许或拒绝特定用户或组访问对象，ACE段由多个字段组成，分别表示访问掩码、安全标识符、ACE类型和ACE标志等。

下面是一个示例，展示了包含一个DACL和一个SACL的SDDL格式的安全描述符：

```
D:(A;;GA;;;SY)(A;;GA;;;BA)(A;;GA;;;WD)(A;;GX;;;CO)S:(AU;SAFA;GA;;;WD)(AU;SAFA;GXGW;;;CO)
```

该SDDL描述符由两个段组成，第一个段（D）表示DACL，它允许系统管理员、内置管理员和所有用户以读取和写入的方式访问对象。第二个段（S）表示SACL，它允许系统管理员和内置管理员对对象进行安全审核，并将所有事件发送到安全日志中。

#### 3、SDDL编辑DACL以及SACL

使用SDDL来设置和修改DACL和SACL的步骤如下：

1. 1. 编写SDDL字符串

首先，需要编写SDDL字符串。SDDL字符串是一种描述安全描述符的文本格式，它由多个子项组成，每个子项对应于一个权限或一个安全标识符（SID）。

一个简单的SDDL字符串的示例为：D:(A;;GA;;;WD)(A;;GA;;;BA)

在这个示例中，D: 表示此SDDL字符串是用来描述DACL，即访问控制列表；A;;GA;;;WD 表示给Everyone用户组授予了读取和写入权限；(A;;GA;;;BA) 表示给Administrators用户组授予了读取和写入权限。2. 使用sc.exe命令行工具设置DACL和SACL

接下来，可以使用sc.exe命令行工具来设置DACL和SACL。sc.exe命令行工具是Windows操作系统自带的一个工具，可以用来管理服务。通过sc.exe工具，可以使用SDDL字符串来设置服务的DACL和SACL。

## 0x05 命令行工具sc.exe

#### 1、概念和作用

sc.exe是Windows操作系统中的命令行工具，用于管理和控制Windows服务。通过sc.exe，用户可以创建、修改、删除和查询Windows服务，以及控制服务的启动和停止等操作。sc.exe还可以用于修改服务的启动类型、设置服务的依赖关系和描述信息等功能。

具体来说，sc.exe提供了以下主要的功能：

1. 1. 创建Windows服务：用户可以使用sc.exe命令创建新的Windows服务。
2. 2. 修改Windows服务：用户可以使用sc.exe命令修改现有的Windows服务的配置信息。
3. 3. 删除Windows服务：用户可以使用sc.exe命令删除不需要的Windows服务。
4. 4. 查询Windows服务：用户可以使用sc.exe命令查看Windows服务的状态、配置信息和依赖关系等。
5. 5. 控制Windows服务：用户可以使用sc.exe命令启动、停止、暂停或恢复Windows服务的运行。
6. 6. 设置Windows服务的安全性：用户可以使用sc.exe命令设置Windows服务的安全性，包括修改服务的DACL和SACL等。

sc.exe是Windows系统中非常重要的命令行工具，可以方便地管理和控制Windows服务，保障系统的正常运行和安全性。

#### 2、基本用法和常用命令

sc.exe 是 Windows 操作系统自带的一个命令行工具，它可以用于管理 Windows 服务，包括创建、删除、启动、停止、修改服务的配置信息等操作。以下是 sc.exe 的一些常用命令和基本用法：

1. 1. 列出所有服务

   #### 2、格式和语法

   DACL的格式和语法基于SDDL（Security Descriptor Definition Language），SDDL是一种字符串表示形式，用于描述安全描述符和访问控制列表。以下是SDDL语法的基本格式：

cssCopy code

`D:(A;;[Access Type];[Security Identifier])`

其中，D:表示这是DACL的SDDL字符串，A表示ACE中的对象类型，Access Type表示访问权限的类型，Security Identifier表示允许或拒绝访问的安全标识符（SID）。

Access Type包括以下部分：

* • A：代表允许对对象的访问。
* • D：代表拒绝对对象的访问。
* • OA：代表允许对对象的所有者访问。
* • OD：代表拒绝对对象的所有者访问。
* • GA：代表允许对对象的组访问。
* • GD：代表拒绝对对象的组访问。因此，一个完整的DACL SDDL字符串可能如下所示：

cssCopy code

`D:(A;;GA;;;WD)(A;;GA;;;SY)(A;;0x1201bf;;;S-1-5-32-544)`

其中，这个DACL允许组Everyone和系统用户具有完全访问权限，并且允许本地管理员组具有包括删除和修改权限的特定访问权限。

## 0x04、SDDL

#### 1、概念和作用

SDDL（Security Descriptor Definition Language）是一种描述Windows安全描述符的语言，它用于描述Windows安全对象的安全描述符，包括访问控制列表（ACL）、安全标识符（SID）、安全描述符的所有者和主要组等。

SDDL的作用主要有以下几个方面：

1. 1. 显示安全描述符信息：使用SDDL可以将安全描述符转换为易读的字符串形式，从而方便用户查看和理解其中的信息。
2. 2. 编辑安全描述符：SDDL提供了一种统一的方式来编辑安全描述符的信息，用户可以使用SDDL语法修改安全描述符的内容，以实现对安全对象的访问控制。
3. 3. 传输安全描述符：SDDL可以将安全描述符的信息以字符串的形式传输，以方便在不同的系统之间共享安全描述符的信息。SDDL语言结构非常灵活，可以用于描述多种安全对象，包括文件、目录、注册表、命名管道等。

#### 2、语法和格式

SDDL（Security Descriptor Definition Language）是一种描述安全描述...