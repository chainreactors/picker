---
title: java代码审计
url: https://www.secpulse.com/archives/201268.html
source: 安全脉搏
date: 2023-06-03
fetch_date: 2025-10-04T11:45:04.236218
---

# java代码审计

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

# java代码审计

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-06-02

39,040

## 0x01代码审计的基本概念和流程

### 1、代码审计的定义和背景

Java代码审计是指对Java应用程序代码的分析，以确定是否存在安全漏洞和风险，并提出修复建议的过程。Java应用程序的开发在近年来已经成为了一种主流，随之而来的就是对Java代码安全性的关注。Java应用程序存在各种各样的安全问题，包括但不限于SQL注入、跨站点脚本（XSS）、跨站点请求伪造（CSRF）和文件包含漏洞等。因此，对Java代码进行审计，可以帮助开发者和安全团队及时发现和解决安全问题，确保应用程序的安全性。

Java应用程序代码审计也与Java语言及其框架的发展背景有关。Java语言的高度可移植性、跨平台性、安全性以及其生态系统的丰富性，使得Java应用程序成为了企业级和互联网应用程序的主要开发语言之一。与此同时，Java应用程序的快速开发和部署，也使得一些安全问题得以快速传播和扩散。在Java应用程序开发的过程中，开发者往往需要使用各种各样的框架和第三方库，这些框架和库的安全性也会直接影响到应用程序的安全性。因此，Java代码审计成为了保障Java应用程序安全的重要手段之一。

### 2、代码审计的流程和方法

1. 1. 收集信息：通过查看源代码、分析日志、使用工具等方式，收集目标应用程序的信息，包括但不限于：应用程序的文件目录结构、配置文件、程序源代码、请求参数、数据库结构等。
2. 2. 风险评估：根据收集到的信息，分析应用程序中可能存在的漏洞和安全隐患，并对其进行评估，确定哪些漏洞最为严重、哪些应该优先修复。
3. 3. 漏洞挖掘：通过手动测试和工具扫描等方式，对应用程序进行漏洞挖掘。测试应包括各种类型的漏洞，例如：SQL注入、跨站脚本、跨站请求伪造等。
4. 4. 漏洞验证：验证漏洞是否真实存在，并确定漏洞的影响程度、可能的攻击方式和风险级别。
5. 5. 报告编写：将漏洞及其影响、攻击方式、风险级别等信息整理成报告，供开发者和管理者参考。报告应该详细说明漏洞的位置、修复建议等内容，并提供漏洞的PoC（漏洞利用代码）。
6. 6. 漏洞修复：由开发人员修复漏洞，并通过测试验证修复效果。在修复漏洞之后，应再次进行代码审计，以确保没有新的漏洞产生。

Java代码审计的方法包括手动审计、自动化审计和混合审计。

[![1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1-1024x835.png "1-1024x835.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1.png)

1、手动审计是通过人工分析源代码、使用工具等方式进行的，可以发现较为复杂的漏洞；

2、自动化审计则是利用工具对源代码进行扫描和分析，可以快速发现大量的漏洞，但需要手动验证漏洞是否真实存在；

3、混合审计则是将手动审计和自动化审计相结合，既可以发现复杂漏洞，又可以快速发现大量的漏洞

## 0x02 JAVA基础理论

### 1、java语言的基本语法和结构

Java是一种面向对象的编程语言，基于C++语言而开发。它被广泛应用于网络编程、企业级应用、移动应用、游戏开发等领域。Java语言的基本语法和结构是学习Java编程的第一步，以下是Java语言的基本语法和结构：

1. 1. 注释：Java语言支持三种注释方式：单行注释、多行注释和文档注释。其中，单行注释以“//”开头，多行注释以“/”开头，“/”结尾，文档注释以“/\*”开头，“/”结尾。
2. 2. 数据类型：Java语言的基本数据类型包括byte、short、int、long、float、double、char和boolean。其中，byte、short、int和long为整数类型；float和double为浮点数类型；char为字符类型；boolean为布尔类型。
3. 3. 变量：Java语言的变量有两种类型：局部变量和成员变量。局部变量在方法中定义，只在方法内部有效；成员变量在类中定义，可以被类的所有方法访问。
4. 4. 运算符：Java语言支持算术运算符、赋值运算符、比较运算符、逻辑运算符等多种运算符。
5. 5. 控制语句：Java语言的控制语句包括if语句、switch语句、for循环、while循环、do-while循环等。
6. 6. 数组：Java语言的数组是一个存储相同数据类型元素的容器，可以动态创建和初始化。
7. 7. 类和对象：Java语言是面向对象的，所有的代码都必须定义在类中。一个Java类包括属性和方法两部分，对象是类的一个实例化，可以通过“new”关键字创建。
8. 8. 继承和多态：Java语言支持继承和多态两种特性。继承是指子类可以继承父类的属性和方法，多态是指同一个方法在不同的对象中有不同的实现。
9. 9. 异常处理：Java语言提供了异常处理机制，可以捕获和处理程序运行过程中的异常，避免程序崩溃。

### 2 、JavaEE类库和框架的介绍

#### 1、JavaWeb

(1)Servlet Servlet是Java语言的一个重要组件，用于创建动态Web应用程序，可以通过Java Servlet API进行开发和部署，运行在Java EE容器中，用于接收和处理HTTP请求并生成响应。Servlet运行在服务器端，主要用于创建动态Web内容，Servlet是java EE的核心。也是所有MVC框架实现的根本。(2)filter Filter（过滤器）是Java Web应用中的一个重要组件，主要用于过滤请求和响应，对其进行处理或修改。它可以在客户端向服务器发送请求之前或服务器响应客户端请求之前，对请求和响应进行拦截、过滤和处理，从而实现一些通用的功能，例如鉴权、日志记录、字符编码转换、性能监控、安全控制等。Filter基于Java Servlet规范，需要在web.xml文件中进行配置。当请求被发送到Web容器时，Filter可以对请求进行处理，也可以对响应进行处理，同时可以与其他Filter链式组合，形成一个Filter链，实现复杂的功能。

Filter有三个主要的回调方法：

1. 1. `init(FilterConfig config)`: 用于初始化Filter，该方法只会在第一次调用该Filter时被调用。
2. 2. `doFilter(ServletRequest request, ServletResponse response, FilterChain chain)`: 处理请求和响应，可以进行预处理、修改请求和响应，或者将请求和响应传递给下一个Filter。
3. 3. `destroy()`: 用于销毁Filter，在Filter生命周期结束时被调用。

Filter的处理过程可以通过FilterChain对象来实现，FilterChain对象可以将请求和响应传递给下一个Filter，也可以将请求和响应传递给Servlet容器处理，最终生成响应结果。FilterChain对象的调用顺序与在web.xml文件中配置的顺序相同。

总之，Filter是Java Web应用中非常重要的一个组件，可以实现很多通用的功能，减少代码重复，提高代码的可维护性和可扩展性。

#### 2、spring框架

Spring的英文翻译为春天，可以说是给Java程序员带来了春天，因为它极大的简化了开发，Spring是一个开放源代码的设计层面框架，它是于2003 年兴起的一个轻量级的Java 开发框架，框架的主要优势之一就是其分层架构，分层架构允许使用者选择使用哪一个组件，同时为 J2EE 应用程序开发提供集成的框架，Spring框架自从发布以来，就得到快速发展，经过时代的验证，现在已经是最受欢迎的企业级 Java 应用程序开发框架，数以百万的来自世界各地的开发人员使用 Spring 框架来创建性能好、易于测试、可重用的代码。从2004发布的第一个Spring版本，到现在已经更新到第五个Spring版本了。

[![640-20230601222954327.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/640-20230601222954327-1024x457.png "640-20230601222954327-1024x457.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/640-20230601222954327.png)

#### 3、Apache Shiro

Apache Shiro是一个Java的安全框架，提供身份验证、授权、加密、会话管理等安全功能。Shiro的设计目标是简单易用，同时提供灵活的扩展性和高度的安全性。Shiro是Apache软件基金会下的一个开源项目。Shiro提供了两个重要的安全概念，Subject和SecurityManager。Subject是Shiro的核心对象，代表当前用户。在Shiro中，开发人员可以通过Subject来完成身份认证、授权等操作。SecurityManager则是Shiro的安全管理器，用于管理Subject的登录、注销等操作。

Shiro支持多种身份认证方式，如基于表单的身份认证、基于HTTP的身份认证、基于CAS的身份认证等。在Shiro中，授权是通过角色和权限两个概念来实现的。角色是一组权限的集合，而权限则是操作某个资源的权限。Shiro提供了类似Spring Security的注解式授权方式，可以方便地对方法、类、URL等进行授权。

[![640-20230601222954387.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/640-20230601222954387.png "640-20230601222954387.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/640-20230601222954387.png)

#### 4、Struts2框架

Struts2是一个基于MVC（Model-View-Controller）架构的Web应用程序框架，它使用Java Servlet和JavaServer Pages（JSP）技术来创建Web应用程序。Struts2提供了许多功能和特性，包括：

1. 1. 拦截器（Interceptor）：Struts2的拦截器允许开发人员定义在Action调用前后执行的逻辑。这样可以方便地实现各种功能，例如身份验证、日志记录、性能监控等。
2. 2. 动态表单校验：Struts2提供了一种方便的方式来定义表单校验规则，这些规则可以动态地在客户端和服务器端进行校验。
3. 3. 适配器（Adapter）：Struts2的适配器允许开发人员在不修改应用程序代码的情况下，使用不同的视图技术（例如JSP、FreeMarker、Velocity等）。
4. 4. 国际化（I18n）支持：Struts2提供了内置的国际化支持，可以方便地实现多语言应用程序。
5. 5. AJAX支持：Struts2提供了方便的AJAX支持，可以轻松地实现AJAX应用程序。

总的来说，Struts2是一个功能强大、易于使用的Web应用程序框架，广泛应用于Java Web开发中。

[![640-20230601222954436.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/640-20230601222954436.png "640-20230601222954436.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/640-20230601222954436.png)

## 0x03代码审计工具

### 1、编辑器

#### 1、sublime

Sublime Text 是一个跨平台的文本编辑器，具有丰富的功能和插件生态系统。它支持多种编程语言，包括Java，并且具有许多强大的功能，例如语法高亮、自动补全、代码片段、多窗口编辑、跨文件查找和替换、拆分窗口等。Sublime Text 还有一个庞大的插件社区，提供了各种功能丰富的插件，如代码格式化、代码审计等。

[![640-20230601222954520.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/640-202306012229...