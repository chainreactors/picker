---
title: 红队-java代码审计生命周期
url: https://www.secpulse.com/archives/193771.html
source: 安全脉搏
date: 2022-12-21
fetch_date: 2025-10-04T02:03:23.494367
---

# 红队-java代码审计生命周期

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

# 红队-java代码审计生命周期

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[KB-AT](https://www.secpulse.com/newpage/author?author_id=37336)

2022-12-20

40,989

# 红队-java代码审计生命周期

@深信服-华南天玄攻防战队-KBAT

## 前言

红队java代码审计生命周期中常见的一些漏洞学习总结以及一些审计思路。

## 红队-java代码审计生命周期过程

源码获取->审计环境配置->代码审计->poc&exp编写->后渗透利用->相关文档输出

![image-20221111160018658.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image-20221111160018658-1024x878.png "image-20221111160018658-1024x878.png")

## 源码获取

•          开源、二开（官网、github、码云）

•          相似站点批量扫备份文件

•          相似站点getshell打包

•          网盘搜索

•          咸鱼、淘宝、TG

•          云市场

•          ......

## 审计环境

•          idea

•          vscode

•          jdk8（按源码支持的）

•          tomcat

•          burp

•          jd-gui

•          .....

## 代码审计

### 快速代码审计

•          提取源码中的全部jsp，find /domain/ -name "\*.jsp",提取出来后用路径直接去用burp批量跑目录（可换请求的方法，GET、POST），把返回200(根据网站情况)的路径提取出来，表示可以直接未认证访问；然后在跟进这些jsp代码，通过查找相关的sink函数，在去定位source是否可控，如果可控那么就形成一条污染链，在看是否需要绕过sanitizer。

•          通过提取web.xml里面的servlet-name路径，然后拼接路径直接去用burp批量跑目录（可换请求的方法，GET、POST），把返回200(根据网站情况)的路径提取出来，表示可以直接未认证访问，然后根据对应的servlet-name的servlet-class根据相关联的class代码（用idea可直接将.class逆向出来，比较完整；有些是引用jar包形式，可通过jd-gui进行逆向或者idea逆向出来源码审计）。同样的通过查找相关的sink函数，在去定位source是否可控，如果可控那么就形成一条污染链，在看是否需要绕过sanitizer。

•          通过批量提取js或者html里面的url接口和path路径。同样方法类似如上。

•          关键的sink函数定位。

### SpringBoot项目结构

一个简单的springboot项目结构如下

![image-5558929.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image-5558929-655x1024.png "image-5558929-655x1024.png")

其中Java代码全部放在/src/main/java/目录下，资源文件在/src/main/resources/下

#### 代码结构

common/: 存放通用类，如工具类和通用返回结果
config/: 存放配置文件
controller/: 存放控制器，接收从前端传来的参数，对访问控制进行转发、各类基本参数校验或者不复用的业务简单处理等。
dao/: 数据访问层，与数据库进行交互，负责数据库操作，在Mybaits框架中存放自定义的Mapper接口
entity/: 存放实体类
interceptor/: 拦截器
service/: 存放服务类，负责业务模块逻辑处理。Service层中有两种类，一是Service，用来声明接口；二是ServiceImpl，作为实现类实现接口中的方法。
utils/: 存放工具类
NewBeeMallApplication.java: Spring Boot启动类
dto/: 存放数据传输对象（Data Transfer Object），如请求参数和返回结果
vo/: 视图对象（View Object）用于封装客户端请求的数据，防止部分数据泄漏，保证数据安全
constant/: 存放常量
filter/: 存放过滤器
component/: 存放组件

#### 资源目录结构

在src/main/resources下存放资源文件
mapper/: 存放Mybaits的mapper.xml文件
static/: 静态资源文件目录（Javascript、CSS、图片等），在这个目录中的所有文件可以被直接访问
templates/: 存放模版文件
application.properties: Spring Boot默认配置文件
META-INF/: 相当于一个信息包，目录中的文件和目录获得Java 2平台的认可与解释，用来配置应用程序、扩展程序、类加载器和服务
i18n/: 国际化文件的简称，来源是英文单词internationalization的首末字符i和n，18为中间的字符数

#### 其他结构

⚠️ Spring Boot无需配置 web.xml，但在其他Java项目中，web.xml是一个非常重要的文件，用来配置Servlet、Filter、Listener等。
pom.xml: maven的配置文件，记录项目信息、依赖信息、构建配置等
如果使用gradle进行自动化构建，则会存在build.gradle文件

### 请求传递流程

Java审计难上手的一大因素是Java一般都是大中型系统，架构相比于PHP开发的小系统会复杂很多，大型系统开发过程中难免出现不规范的编码习惯，再加上函数调用错综复杂，审计代码时光弄明白程序逻辑，理解程序员的编码习惯就要花费大量精力了。首先弄明白请求流程的处理，知道用户请求内容会经过哪些代码才能理解程序处理逻辑，可以对我们后续的审计提供非常大的帮助。用户的请求发送给服务器之后，中间件（案例项目使用的是Tomcat）会将请求解析发送给Spring的DispatcherServlet，DispatcherServlet的作用是分配请求，详细的过程我们暂时不深入。只需要知道中间件解析请求之后请求会经过Filter和Interceptor。Filter（过滤器）和Interceptor（拦截器）做的事很相似，但他们的触发时机不同，且Interceptor只在Spring中生效，它们可以用来对请求进行过滤字符、拦截、鉴权、日志记录等功能，简单说就是可以在参数进入应用前对其处理，做到全局的处理。请求经过Filter和Interceptor之后会被DispatcherServlet分配到对应路径的Controller（控制器），文件名为ExampleController，Controller负责简单的逻辑处理和参数校验功能，之后调用Service。Service主要负责业务模块逻辑处理。Service层中有两种类，一是接口类，文件名为ExampleService，用来声明接口；二是接口实现类，文件名为ExampleServiceImpl，作为实现类实现接口中的方法。实现的代码都在ExampleServiceImpl中。当Service涉及到数据库操作时就会调用Dao。Dao主要负责数据库的操作，由于使用Mybatis作为ORM框架，只做中间传递的作用，所有SQL语句都是写在配置文件中的，配置文件名为ExampleMapper.xml，存放在src/main/resources/mapper中。从用户请求到服务器处理的主要过程如下图所示（省略了DispatcherServlet）：

![image-2-5558974.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image-2-5558974-1024x867.png "image-2-5558974-1024x867.png")为了更好理解，以「保存订单」功能为例，主要的请求流程如下图，不了解Spring请求传递的同学可以在代码中跟一遍请求流程，会加深请求传递的印象。
![image-3.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image-3-1024x932.png "image-3-1024x932.png")

#### java项目分层

•          视图层(View 视图)

•          控制层（Controller、Action控制层)

•          服务层(Service)

•          业务逻辑层BO(business object)

•          实体层(entity 实体对象、VO(value)object)值对象、模型层(bean)

#### Servlet

•          Servlet是在Java Web容器上运行的小程序

•          Servlet3.0之前的版本都需要在web.xml中配置

•          Spring MVC框架就是基于Servlet技术实现的

### sql注入漏洞

#### 成因

本质是将用户的输入当做代码执行，程序将用户的输入拼接到了sql语句中，改变原来sql语句的语义造成攻击。

#### **常见的一些例子**

DAO: 存在拼接的SQL语句

```
String sql="select * from user where id="+id
```

Hibernate框架

```
session.createQuery("from Book where title like '%" + userInput + "%' and published = true")
```

Mybatis框架

```
Select * from news where title like ‘%${title}%’
Select * from news where id in (${id})，
Select * from news where title =‘java’ order by ${time} asc
```

#### 审计方法

对于sql注入来讲，只要是与数据库存在交互的地方，应用程序对用户的输入没有进行有效的过滤，都有可能存在SQL注入漏洞。
在实际环境中**，中间件漏洞的****sql****注入漏洞可能更多：**

•          Mybatis框架中的like、in和order by语句。

•          Hibernate框架中的createQuery()函数

快速定位相关sql语句上下文，查看是否有显式过滤机制。

#### 修复

•          参数化查询，使用java.sql.PreparedStatement来对数据库发起参数化查询。

```
stmt=conncetion.prepareStatement(sqlString);
stmt.setString(1,userName);
stmt.setString(2,itemName);
rs=stmt.executeQuery();
```

•          使用预编译能够预防绝大多数SQL注入，**java.sql.PreparedStatement****代替java.sql.Statement**,但对于order by后的不能用预编译进行处理，只能手动过滤。

```
String sqlString = "select * from db_user where username=? and password=?";
        PreparedStatement stmt = connection.prepareStatement(sqlString);
        stmt.setString(1, username);
        stmt.setString(2, pwd);
        ResultSet rs = stmt.executeQuery();
```

•          Mybatis的SQL配置中，采用#变量名称

### XSS漏洞

#### 成因

网站与后端交互的输入输出没有做好过滤，导致攻击者可以插入恶意js语句进行攻击。根据后端代码不同 ，大致可以分为反射型、存储型、DOM型
举例:

```
@RequestMapping("/xss")
public ModelAndView xss(HttpServletRequest request,HttpServletResponse
response) throws ServletException,IOException{
 Str...