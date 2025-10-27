---
title: 以AJ-Report为例从0开始学习Java代码审计
url: https://forum.butian.net/share/3854
source: 奇安信攻防社区
date: 2024-11-14
fetch_date: 2025-10-06T19:12:58.562185
---

# 以AJ-Report为例从0开始学习Java代码审计

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

### 以AJ-Report为例从0开始学习Java代码审计

* [漏洞分析](https://forum.butian.net/topic/48)

记录一下一个之前没有正经审计过项目，基本没接触过java的新手如何根据有限的漏洞信息，尝试用不同的思路进行复现审计

### 前言
记录一下一个之前没有正经审计过项目，基本没接触过java的新手如何根据有限的漏洞信息，尝试用不同的思路进行复现审计
### AJ-Report环境搭建
直接jar包启动？我不，我就要自己编译，装maven，测试执行`mvn help:system`的时候报了个error，意思大概就是下载失败，查了查大概是网络问题，换成阿里云的源还不行，自我怀疑了很久，后面发现是梯子的问题，关了就好了...
![image-20241002171321250](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-82225909bb38522b092b55a05e4c42ec8b7059c6.png)
#### maven是什么
好，第一个问题，maven是什么
Maven是一个Java项目管理和构建工具，它可以定义项目结构、项目依赖，并使用统一的方式进行自动化构建。
项目描述文件是`pom.xml`，存放Java源码的目录是`src/main/java`，存放资源文件的目录是`src/main/resources`，存放测试源码的目录是`src/test/java`，存放测试资源的目录是`src/test/resources`，所有编译、打包生成的文件都放在`target`目录里
![image-20241003110205629](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-4c0f47045f708250119ef3214305d58e14fe72d9.png)
pom.xml里，`groupId`类似于Java的包名，`artifactId`类似于Java的类名，使用``声明一个依赖后，Maven就会自动下载这个依赖包并把它放到classpath中。Maven使用`groupId`，`artifactId`和`version`唯一定位一个依赖，Maven从哪下载依赖呢，当然是镜像仓库。进入到`pom.xml`所在目录，执行`mvn clean package`即可在`target`目录下获得编译后自动打包的jar
![image-20241003110621302](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-740331715f4a446d0473c22b5b3efc5ae57f862c.png)
按照AJ-Report项目文档build的时候又报了个error，大概意思是要用JDK而不是JRE，所以改了改环境变量，顺便配置了一下多java环境，然后一切顺利
![image-20241002173923075](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-52cf3e4055c3e982b924fa60c6b5e83b7b9d927c.png)
一开始用IDEA导入项目源码发现很多import标红，比如`com.anji.plus.gaea`这些玩意，因为这个看着不像是公共依赖，我还以为是源码少，然后发现用maven编译完再jadx反编译的话就有`com.anji.plus.gaea`了，后面发现这其实就是公共依赖，maven自动索引从阿里云镜像库下载补齐，之后就好了
![image-20241002181920373](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-0d9147a2ff0d6442a84f3c9fa674a5b6d22e41c8.png)
如果是用IDEA导入jar包的话也可以，但是需要在项目结构里添加Libraries
![image-20241003223527318](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-2372ee4c8a9410a6e31d017dc1021459b6b931f8.png)
#### SpringBoot是什么
Spring Boot是一个基于Spring的套件，它帮我们预组装了Spring的一系列组件，以便以尽可能少的代码和配置来开发基于Spring的Java应用程序，其设计目的是用来简化Spring应用搭建和开发过程，提供一个开箱即用的应用程序架构，我们基于Spring Boot的预置结构继续开发。目前Java后端主流框架还有Struts 2、Hibernate、JavaServer Faces（JSF）、Vaadin、GWT、Play Framework和Vert.x等
具体看文档就好https://springdoc.cn/spring-boot/getting-started.html#getting-started
#### Tomcat是什么
SpringBoot默认的启动容器是Tomcat，大概就是spring-boot-starter-parent-&gt;spring-boot-dependencies-&gt;spring-boot-starter-web-&gt;spring-boot-starter-tomcat，Tomcat 的组成核心全部都通过 Maven 引入过来了，所以不需要额外安装Tomcat
<https://javabetter.cn/springboot/tomcat.html>
![image-20241003125008109](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-e2bcb32ad551f22b25722b4e55438bf6bc5b8acb.png)
Tomcat用来装载javaweb程序，可以称它为web容器，你的jsp/servlet程序需要运行在Web容器上，Web容器有很多种，JBoss、WebLogic等等，Tomcat是其中一种。web项目多数需要http协议，也就是基于请求和响应，那如何处理这个请求呢，他需要创建servlet来处理，servlet其实就是java程序，只是在服务器端的java程序servlet通过配置文件拦截你的请求，并进行相应处理，然后展示给你相应界面，那么servlet如何创建？tomcat就是帮助你创建servlet的东西。
### 一些IDEA使用技巧
#### 动态调试
改完配置文件之后，不管是jar项目还是源码项目，用idea直接调试都连不上数据库，报错，看起来就是完全没连上，看着依赖什么的也没问题，很神奇
`ERROR com.zaxxer.hikari.pool.HikariPool:593 - HikariPool-1 - Exception during pool initialization. com.mysql.cj.jdbc.exceptions.CommunicationsException: Communications link failure`
![image-20241003183838858](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-271f1c43087eb7941b1fe07a4be76680a87f0544.png)
编译好之后命令行运行jar是没问题的，感觉跟IDEA有关系但是没有证据
![image-20241003183920443](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-c287a82b0e4d129dabc2fb980a8e6fc63e382969.png)
那只能试试远程调试了
![image-20241003202614219](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-ef61589c6ec1a663c729c2b724cca349433fe7ec.png)
一开始断点没打上，忘了是因为啥了，反正最后好了，我把AJ-Report项目里启动jar包的bat脚本启动命令改成了：`"%JAVA\_HOME%"\bin\java -Xdebug -agentlib:jdwp=transport=dt\_socket,server=y,suspend=n,address=50055 -Xbootclasspath/a:%LIB\_JARS% -jar -Dspring.config.location=%CONF\_YML% %BIN\_DIR%\lib\%BOOT\_JAR%`，开始调试后socket会连上，之后访问web端进行相关请求来触发这个断点
![image-20241003202558934](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-0f844fcac32607250b795ea55f21329172a666d6.png)
步过：一行一行的往下走，不会进入到其他方法的内部。
步入：如果当前行有方法执行，可以进入方法的内部（不会进入官方定义的方法，仅能进入自定义的方法）。
强制步入：如果当前行有方法执行，可以进入方法的内部（可以进入官方定义的方法，这在查看底层源码时非常有用）。
智能步入：如果当前行有多个方法同时被执行，IDEA 将会询问你要进入哪个方法。
步出：从步入的方法内执行完该方法，然后退出到方法调用处。
#### 其他技巧
##### 全局搜索
Ctrl+shift+F全局搜索，跟搜狗输入法快捷键冲突了，要先关掉输入法的快捷键
发现搜一样的东西，匹配数量经常会变，后来发现跟settings里配置的最大匹配数有关系，因为最大匹配数小于真正的数量，标绿色的是因为在代码里是字符串
![image-20241002204907817](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-d2a6dbe357a16da7a1048c3aa87b0b892f4ffb35.png)
##### 调用和层次结构
Alt+F7，查看一个Java类、方法或变量的直接使用情况
![image-20241002212047094](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-a94e73ca85703706303e97a90331b1d0d82c4c50.png)
调用层次结构
看哪个地方调用了getLanguage，比如这里就是Calendar.createCalendar调用了getLanguage，下一级就是Calendar.getInstance调用了createCalendar
![image-20241002213039893](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-0c9f5545963177a87d0f16ad8be7589121e67119.png)
类型层次结构，每一个都是下一个的父类
![image-20241002213924219](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-73e25365dc741f00fb4f502d70c398f21b784517.png)
接下来开始正式审计
### swagger-ui截断绕过
URL中有一个保留字符分号`;`，主要为参数进行分割使用，有时候是请求中传递的参数太多了，所以使用分号`;`将参数对（key=value）连接起来作为一个请求参数进⾏传递。
Tomcat在解析请求路径时，会自行修正路径，并使用修正后的路径来匹配对应的Servlet，然而，在路径需要修正的情况下，Tomcat自行修正后得到的URI路径跟使用getRequestURI方法得到的URI路径不一致，因而在我们去对请求路径做权限访问控制时，容易导致绕过。具体Tomcat的源码就不跟了(
| payload | getRequestURL | getRequestURI | getServletPath |
|---|---|---|---|
| `/index` | `http://127.0.0.1:8081/index` | `/index` | `/index` |
| `/./index` | `http://127.0.0.1:8081/./index` | `/./index` | `/index` |
| `/.;/index` | `http://127.0.0.1:8081/.;/index` | `/.;/index` | `/index` |
| `/a/../index` | `http://127.0.0.1:8081/a/../index` | `/a/../index` | `/index` |
| `/a/..;/index` | `http://127.0.0.1:8081/a/..;/index` | `/a/..;/index` | `/index` |
| `/;/index` | `http://127.0.0.1:8081/;/index` | `/;/index` | `/index` |
| `/;a/index` | `http://127.0.0.1:8081/;a/index` | `/;a/index` | `/index` |
| `/%2e/index` | `http://127.0.0.1:8081/%2e/index` | `/%2e/index` | `/index` |
| `/inde%78` | `http://127.0.0.1:8081/inde%78` | `/inde%78` | `/index` |
前置知识了解到这里，可以开始看源码了
如果直接访问后台接口的话，会返回`{"code":"User.credentials.expired","message":"The Token has expired"}`全局搜一下，定位到error方法
![image-20241019203618306](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-7dba0e97c2cadf20a6ff445fb314664365dcf304.png)
验证Authorization和Share-Token，不通过的话调用error方法，都通过才能到filterChain.doFilter那里正常请求
![image-20241020180342614](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-658c025ed1b03e97065aeed5622cf8aa6f65cf6d.png)
这里是使用getRequestURI来获取uri，所以可以用分号来绕过，如果`uri`包含`swagger-ui`直接放行，就不需要验证token那些了，直接`/dataSetParam/verification;swagger-ui/`这样即可
![image-20241020171100386](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-bd5d94095f206d85704ca315e67dbea43343324b.png)
### validationRule参数任意命令执行
已知：`该平台可以通过post方式在validationRules参数对应值中进行命令执行，可以获得服务器权限，登陆管理后台接管大屏。`
所以我们要先找到validationRules参数在哪，通过全局搜索，来确定可疑的地方
![image-20241019165129356](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-b2ca998de93d21f64bea3aaa02fcacf337e94914.png)
全局搜索`validationRules`，发现在这有个`engine.eval(validationRules)`，eval大家都知道，就是一个命令执行的函数，虽然跟php里的eval不大一样，但是大概就是在`verificatio...