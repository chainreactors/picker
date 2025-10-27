---
title: Java Struts2系列的XSS漏洞（S2-002）
url: https://www.secpulse.com/archives/197010.html
source: 安全脉搏
date: 2023-03-07
fetch_date: 2025-10-04T08:47:51.582615
---

# Java Struts2系列的XSS漏洞（S2-002）

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

# Java Struts2系列的XSS漏洞（S2-002）

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-06

9,017

## 0x01 前言

复现一下 S2-002 的洞

## 0x02 S2-002

### 漏洞简介

`Struts2-002` 是一个 `XSS` 漏洞，该漏洞发生在 `s:url` 和 `s:a` 标签中，当标签的属性 `includeParams=all` 时，即可触发该漏洞。

### 漏洞影响版本

`Struts 2.0.0 - Struts 2.1.8.1`

## 0x03 环境搭建

* • 如果不想手动搭建的话，环境我已经配好了 https://github.com/Drun1baby/JavaSecurityLearning/tree/main/JavaSecurity/Struts2/S2-002AndS2-006

因为 s2-002 的洞是一个 XSS，与处理的 Action 没有任何关系，所以这里我们只需要配置 `.jsp` 文件，以及 `.xml` 文件

* • resources 文件夹下

**struts.xml**

```
<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE struts PUBLIC
        "-//Apache Software Foundation//DTD Struts Configuration 2.0//EN"
        "http://struts.apache.org/dtds/struts-2.0.dtd">

<struts>
    <package name="S2-002" extends="struts-default">
        <action name="login" class="com.drunkbaby.action.LoginAction" method="execute">
            <result name="success">welcome.jsp</result>
            <result name="error">index.jsp</result>
        </action>
    </package>
</struts>
```

* • webapp 文件夹下

**index.jsp**

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%@ taglib prefix="s" uri="/struts-tags" %>

<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>S2-002</title>
</head>
<body>
<h2>S2-002 Demo</h2>
<s:url action="login" includeParams="all"></s:url>
<s:a href="%{url}">click</s:a>
</body>
</html>
```

**welcome.jsp**

```
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%@ taglib prefix="s" uri="/struts-tags" %>

<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>S2-002</title>
</head>
<body>
<p>Hello <s:property value="username"></s:property></p>
</body>
</html>
```

接着在 WEB-INF 下，**web.xml**

```
<!DOCTYPE web-app PUBLIC
 "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"
 "http://java.sun.com/dtd/web-app_2_3.dtd" >

<web-app>
  <display-name>S2-002 Example</display-name>
  <filter>
    <filter-name>struts2</filter-name>
    <filter-class>org.apache.struts2.dispatcher.FilterDispatcher</filter-class>
  </filter>
  <filter-mapping>
    <filter-name>struts2</filter-name>
    <url-pattern>/*</url-pattern>
  </filter-mapping>
  <welcome-file-list>
    <welcome-file>index.jsp</welcome-file>
  </welcome-file-list>
</web-app>
```

项目结构如图，至此环境搭建完毕

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082111.png "null")

## 0x04 漏洞复现与分析

```
http://localhost:8080/?%22%3E%3Cscript%3Ealert(1)%3C/script%3E%3C%22
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082112.png "null")

### 漏洞分析

> 之前自己也没有分析过 XSS 相关的漏洞，在最后我会做一个小结来思考一下如何自己挖掘出这个漏洞

我们先下一个断点在 `org.apache.struts2.views.jsp.ComponentTagSupport#doStartTag()` 方法处，开始调试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082113.png "null")

当在 JSP 文件中遇到 `Struts2` 标签 `<s:` 时，程序会先调用 `doStartTag()` 方法 ，并将标签中的属性设置到对应标签对象相应属性中。最后，在遇到 `/>` 结束标签的时候调用 `doEndTag()` 方法。

进入到了 `index.jsp`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082115.png "null")

跟进 `this.component.start()`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082118.png "null")

在 `index.jsp` 中 `includeParams=all`，往下看代码知道 88 行，跟进 `mergeRequestParameters()` 方法

在 `includeParams=all` 的情况下会调用 `mergeRequestParameters()` 将 Tomcat 处取来的参数，这里取到了我们输入的 payload，并且保存在 `this.parameters` 中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082120.png "null")

`mergeRequestParameters()` 方法运行完毕，往下是 `includeGetParameters()` 方法，也跟进去看一下；发现也是调用了 `mergeRequestParameters()`，同样是保存在了 `this.parameters` 中，不过这一次保存的是经过 url 编码的数据

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082123.png "null")

继续往下，程序还调用了 `includeExtraParameters()` 方法，跟进；这里的意思是如果有额外的参数，会被保存进这里，然后再保存到 `this.paramters`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082126.png "null")

**其实到这里漏洞出发点就来了，第一次调用 `mergeRequestParameters()` 方法的时候那一段参数是未经过 URL 编码的，从而产生了 XSS**

在执行完毕 `doStartTag()` 方法之后，会去到 `doEndTag()` 方法，我们跟进 `this.component.end()`，`this.component` 是 URL 类，所以也就是调用了 `URL.end()`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082129.png "null")

往下走，第 146 行，判断目前调度器（Dispatcher）的实例是否支持这一 Struts2 组件的行为，并且判断这一个请求是否需要 Struts2 组件调用某 Action 来处理；如果不需要调用 Action 处理，则直接进入 `buildUrl()` 的代码逻辑，如果需要 Action 来处理，会先去选择/调用 Action，再进行后续操作。

其实也就是 Struts2 运行的基本逻辑

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082131.png "null")

此处因为我们定义了 `action=login`，所以进入到了 else 的代码逻辑，跟进 `this.determineActionURL()` 方法

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082137.png "null")

`determineActionURL()` 方法先定位到了对应的 `action`，再进行 `buildUrl()` 的操作，跟进 `buildUrl()`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082141.png "null")

再跟进

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082143.png "null")

此时的 params 即将会被拿去拼接，造成触发 XSS 漏洞

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197010-1678082146.png "null")

具体拼接是在...