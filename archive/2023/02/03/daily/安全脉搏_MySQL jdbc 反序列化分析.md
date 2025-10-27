---
title: MySQL jdbc 反序列化分析
url: https://www.secpulse.com/archives/195290.html
source: 安全脉搏
date: 2023-02-03
fetch_date: 2025-10-04T05:33:12.736822
---

# MySQL jdbc 反序列化分析

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

# MySQL jdbc 反序列化分析

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-02

12,250

## 0x01 前言

听师傅们说这条链子用的比较广泛，所以最近学一学，本来是想配合着 tabby 或是 codeql 一起看的，但是 tabby 的环境搭建一直有问题，耽误了很久时间，所以就直接看了

## 0x02 JDBC 的基础

* • 本来不太想写这点基础的，但想了想觉得还是要补一点

JDBC 对数据库的操作一般有以下步骤

* • 导入包：要求您包含包含数据库编程所需的 JDBC 类的软件包。通常，使用 `import java.sql.*` 就足够了。
* • 注册 JDBC 驱动程序：要求您初始化驱动程序，以便您可以打开与数据库的通信通道。
* • 建立连接：需要使用 `* DriverManager.getConnection ()*` 方法来创建一个 Connection 对象，该对象表示与数据库服务器的物理连接。要创建新的数据库，在准备数据库 URL 时，无需提供任何数据库名称，如下面的示例所述。
* • 执行查询：需要使用 Statement 类型的对象来构建 SQL 语句并将其提交到数据库。
* • 清理：需要显式关闭所有数据库资源，而不是依赖 JVM 的垃圾回收。

例如创建一个数据库

```
// 步骤 1. 导入所需的软件包
import java.sql.*;

public class JDBCExample {
   // JDBC 驱动程序名称和数据库 URL
   static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
   static final String DB_URL = "jdbc:mysql://localhost/";

   //  数据库凭证
   static final String USER = "username";
   static final String PASS = "password";

   public static void main(String[] args) {
   Connection conn = null;
   Statement stmt = null;
   try{
      // 步骤 2：注册 JDBC 驱动程序
      Class.forName("com.mysql.jdbc.Driver");

      // 步骤 3：建立连接
      System.out.println("Connecting to database...");
      conn = DriverManager.getConnection(DB_URL, USER, PASS);

      // 步骤 4：执行查询
      System.out.println("Creating database...");
      stmt = conn.createStatement();

      String sql = "CREATE DATABASE STUDENTS";
      stmt.executeUpdate(sql);
      System.out.println("Database created successfully...");
   }catch(SQLException se){
      // 处理 JDBC 错误
      se.printStackTrace();
   }catch(Exception e){
      // 处理 Class.forName 的错误
      e.printStackTrace();
   }finally{
      // 用于关闭资源
      try{
         if(stmt!=null)
            stmt.close();
      }catch(SQLException se2){

      }
      try{
         if(conn!=null)
            conn.close();
      }catch(SQLException se){
         se.printStackTrace();
      }
   }// 结束 try
   System.out.println("Goodbye!");
}// 结束 main
}// 结束 JDBCExample
```

这一个 MySQL-JDBC 的漏洞简单来说就是 MySQL 对服务器的请求过程利用

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307076.png "null")

正常的命令执行得到结果后就结束了，但是如果响应的结果是一个恶意的 poc 并且在后续过程中进行了反序列化，那么就可以用来执行任意命令了

## 0x03 漏洞分析

### 漏洞原理

如果攻击者能够控制 JDBC 连接设置项，那么就可以通过设置其指向恶意 MySQL 服务器进行 `ObjectInputStream.readObject()` 的反序列化攻击从而 RCE。

具体点说，就是通过 JDBC 连接 MySQL 服务端时，会有几个内置的 SQL 查询语句要执行，其中两个查询的结果集在 MySQL 客户端被处理时会调用 `ObjectInputStream.readObject()` 进行反序列化操作。如果攻击者搭建恶意 MySQL 服务器来控制这两个查询的结果集，并且攻击者可以控制 JDBC 连接设置项，那么就能触发 MySQL JDBC 客户端反序列化漏洞。

可被利用的两条查询语句：

* • SHOW SESSION STATUS
* • SHOW COLLATION

### 链子

**pom.xml**

```
<dependency>
  <groupId>commons-collections</groupId>
  <artifactId>commons-collections</artifactId>
  <version>3.2.1</version>
</dependency>
<dependency>
  <groupId>mysql</groupId>
  <artifactId>mysql-connector-java</artifactId>
  <version>8.0.13</version>
</dependency>
```

CC 链作为命令执行的部分，也就是说需要我们找一个 JDBC 合理的入口类，并且这个入口类需要在 JDBC 连接过程中被自动执行，最终是找到了这样一个类 `com.mysql.cj.jdbc.result.ResultSetImpl`，它的 `getObject()` 方法调用了 `readObject()` 方法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307079.png "null")

JDBC 通过 MySQL 数据库查询数据会返回一个结果集，将查询到的结果返回给程序，并将结果封装在 `ResultSetImpl` 这个类中。

所以这个类不满足**用户可控输入**这一点，所以我们应该要去找谁调用了 `ResultSetImpl#getObject()`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307085.png "null")

根据网上的链子是 `ResultSetUtil` 类调用了 `ResultSetImpl#getObject()`，并且能够继续向上调用（如果 tabby 或者其他工具搞好了应该会用那些工具分析）

`ResultSetUtil` 这个类是用来处理一些测试实例的结果，或者是 profiler 的结果。简而言之还是用来做数据处理的类，继续往上看谁调用了它。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307091.png "null")

最终是 `com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor#populateMapWithSessionStatusValues` 方法调用了 `ResultSetUtil#resultSetToMap`

`ServerStatusDiffInterceptor` 是一个拦截器，在 JDBC URL 中设定属性 `queryInterceptors` 为 `ServerStatusDiffInterceptor` 时，执行查询语句会调用拦截器的 preProcess 和 postProcess 方法，这是一个自动执行的过程，我们可以把它作为利用链头。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307095.png "null")

看一下 `populateMapWithSessionStatusValues` 方法的代码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307097.png "null")

先建立了 JDBC 的连接，并创建查询，查询语句是 `SHOW SESSION STATUS`，接着调用 `ResultSetUtil.resultSetToMap`，完成查询并封装查询结果。

### 漏洞复现

* • 之前看 Y4tacker 师傅的文章时，发现有提到是直接用 python 脚本打，里面有很多数据，但是这个 ”打“ 肯定不是空穴来风的，所以需要再明确一下攻击思路。

环境搭建可能会踩坑，若有师傅踩坑了可以滴我一下

我们需要先伪造数据包，并用 wireshark 抓包，观测一下流量，编写 Test 类内容如下

```
import java.sql.*;

public class Test {
    public static void main(String[] args) throws Exception {
        Class.forName("com.mysql.jdbc.Driver");
        String jdbc_url = "jdbc:mysql://192.168.116.129:3306/test?characterEncoding=UTF-8&serverTimezone=Asia/Shanghai" +
                "&autoDeserialize=true" +
                "&queryInterceptors=com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor";
        Connection con = DriverManager.getConnection(jdbc_url, "root", "123123");
    }
}
```

通过 `tcp.port == 3306 && mysql` 来过滤协议

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307100.png "null")

我们需要用 python 脚本伪造的 MySQL 服务端需要伪造的是 `Greeting` 数据包 `Response OK` 、`Response Response OK` 以及 JDBC 执行查询语句 `SHOW SESSION STATUS` 的返回包等，我们逐个来分析。

首先是 `greeting` 数据包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195290-1675307104.png "null")

这里发送 `greeting` 数据包之后需要发送 `Login` 请求，`Login` 请求里面...