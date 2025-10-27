---
title: 在 JSP 中优雅的注入 Spring 内存马
url: https://forum.butian.net/share/4053
source: 奇安信攻防社区
date: 2025-01-21
fetch_date: 2025-10-06T20:04:33.293363
---

# 在 JSP 中优雅的注入 Spring 内存马

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 在 JSP 中优雅的注入 Spring 内存马

* [渗透测试](https://forum.butian.net/topic/47)

JSP 下注入 Spring 内存马 & Spring Hack 无条件的一种方法

在 JSP 中优雅的注入 Spring 内存马
=======================
前言
--
随着内存马的检测工具不断完善, 内存马的排查也越来越严格, 目前市面上的主流内存马排查工具通常有两款:
4ra1n 师傅的: <https://github.com/4ra1n/shell-analyzer>, 其中核心思路为, 使用`JavaAgent`技术进行`Java 类`的重新加载, 筛选出可疑的类, 并反编译出其 class 字节码进行检测.
c0ny1 师傅的: <https://github.com/c0ny1/java-memshell-scanner>, 其中核心思路为, 内存马是注入到哪个变量的, 那么就通过反射遍历哪个变量, 筛选出可疑的类. 这些手法通过一个单独的`jsp`文件即可检测.
它们都囊括了`Servlet, Filter, Listener`内存马的检测, 但都没有专门的为`Spring`类型的内存马进行检测.
所以在这里我们可以通过一系列手段进行注入`Spring`内存马进行逃避检测, 当然本篇文章并不会介绍往常的`在 Controller 中注入 Controller (但会给出案例演示以示区别)`, 而是在 `Jsp (Servlet)`中进行注入`Controller (Spring)`.
基础环境搭建
------
在这里本篇的文章都会基于该环境进行演示, 以更好的描述文章中所提到的点以及问题. 这里以`SpringMVC + Tomcat 8.5.0`进行创建项目, 环境大致如下.
### 依赖信息 pom.xml
`pom.xml`文件内容:
```xml
<properties>
<spring.version>5.3.39</spring.version>
<tomcat.version>8.5.0</tomcat.version>
</properties>
<dependencies>
<!-- c3p0 -->
<dependency>
<groupId>com.mchange</groupId>
<artifactId>c3p0</artifactId>
<version>0.9.5.2</version>
</dependency>
<!-- mysql 驱动 -->
<dependency>
<groupId>mysql</groupId>
<artifactId>mysql-connector-java</artifactId>
<version>8.0.28</version>
</dependency>
<!--Tomcat核心库-->
<dependency>
<groupId>org.apache.tomcat</groupId>
<artifactId>tomcat-catalina</artifactId>
<version>${tomcat.version}</version>
</dependency>
<!--Tomcat工具库-->
<dependency>
<groupId>org.apache.tomcat</groupId>
<artifactId>tomcat-util</artifactId>
<version>${tomcat.version}</version>
</dependency>
<!--JSPAPI-->
<dependency>
<groupId>javax.servlet.jsp</groupId>
<artifactId>jsp-api</artifactId>
<version>2.2</version>
</dependency>
<!--JSTL标签库-->
<dependency>
<groupId>javax.servlet.jsp.jstl</groupId>
<artifactId>jstl-api</artifactId>
<version>1.2</version>
<scope>provided</scope>
</dependency>
<!--ServletAPI-->
<dependency>
<groupId>javax.servlet</groupId>
<artifactId>javax.servlet-api</artifactId>
<version>4.0.1</version>
<scope>provided</scope>
</dependency>
<!--Spring AOP-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-aop</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Aspects-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-aspects</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Beans-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-beans</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Context-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-context</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Core-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-core</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Expression Language (SpEL)-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-expression</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring JDBC-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-jdbc</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring ORM-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-orm</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Transaction Management-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-tx</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Web-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-web</artifactId>
<version>${spring.version}</version>
</dependency>
<!--Spring Web MVC-->
<dependency>
<groupId>org.springframework</groupId>
<artifactId>spring-webmvc</artifactId>
<version>${spring.version}</version>
</dependency>
</dependencies>
```
其中引入`Tomcat 8.5.0 & SpringMVC 5.3.39`进行调试.
### 组件信息 web.xml
随后定义`/webapp/WEB-INF/web.xml`文件内容如下:
```xml
<context-param>
<param-name>contextConfigLocation</param-name>
<param-value>classpath:spring-parent.xml</param-value>
</context-param>
<listener>
<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>
<servlet>
<servlet-name>dispatcherServlet</servlet-name>
<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value>classpath:spring-child.xml</param-value>
</init-param>
<load-on-startup>1</load-on-startup>
</servlet>
<servlet-mapping>
<servlet-name>dispatcherServlet</servlet-name>
<url-pattern>/</url-pattern>
</servlet-mapping>
```
特别注意这里定义的`ContextLoaderListener`中读取的`contextConfigLocation`为`spring-parent.xml`.
而`DispatcherServlet`中读取的`contextConfigLocation`为`spring-child.xml`, 这里笔者这样定义也是有含义的, 它会涉及到`Spring`的父子容器问题.
### Spring IOC 定义
定义`/resources/spring-child.xml`文件内容如下:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:context="http://www.springframework.org/schema/context"
xmlns:mvc="http://www.springframework.org/schema/mvc"
xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd">
<context:component-scan base-package="com.heihu577.controller"/> <!-- 扫描包 -->
<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
<property name="prefix" value="/WEB-INF/pages/"/>
<property name="suffix" value=".jsp"/>
</bean> <!-- 定义视图解析器 -->
<bean class="com.mchange.v2.c3p0.ComboPooledDataSource">
<property name="driverClass" value="com.mysql.cj.jdbc.Driver"/>
<property name="jdbcUrl"
value="jdbc:mysql://localhost:3306/mysql?useSSL=true&amp;useUnicode=true&amp;characterEncoding=utf-8"/>
<property name="user" value="root"/>
<property name="password" value=""/>
</bean> <!-- 定义数据源配置 -->
<mvc:annotation-driven/> <!-- 能支持 Spring MVC 高级功能, JSR 303 校验, 映射动态请求 -->
<mvc:default-servlet-handler/> <!-- 将 Spring MVC 不能处理的请求, 交给 Tomcat 处理, 例如 css js -->
</beans>
```
其中`/resources/spring-parent.xml`定义为如下内容:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:utils="http://www.springframework.org/schema/util"
xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/util https://www.springframework.org/schema/util/spring-util.xsd">
<utils:properties id="myConfig"> <!-- 定义一个 Properties 类型的 Bean, 假装数据源配置. -->
<prop key="username">root</prop>
<prop key="password">toor</prop>
</utils:properties>
</beans>
```
其中为什么这样定义, 在后续部分进行说明.
### SpringMVC Controller 定义
定义在`com.heihu577.controller`中, 如下:
```java
@Controller
public class HeihuController {
@RequestMapping("/hello")
@ResponseBody
public String hello() {
return "hello";
}
}
```
一个特别简单的接受请求的 Controller, 后续会在该 Controller 上进行添加代码进行讲解.
传统 Controller 注入方式
------------------
在介绍这种方法之前, 我们先来回顾一下传统的 Controller 注入方式, 创建如下 Controlle...