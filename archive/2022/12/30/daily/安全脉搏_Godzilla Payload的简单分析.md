---
title: Godzilla Payload的简单分析
url: https://www.secpulse.com/archives/194369.html
source: 安全脉搏
date: 2022-12-30
fetch_date: 2025-10-04T02:43:51.514095
---

# Godzilla Payload的简单分析

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

# Godzilla Payload的简单分析

[资讯](https://www.secpulse.com/archives/category/news)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-29

11,180

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297522.png)

# 前言

对Godzilla Payload的一点简单分析～

# Java服务端

Java服务端即Webshell，负责对客户端传输数据的解析、执行和结果返回。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297523.png "null")

# Godzilla Payload

哥斯拉的全功能Java马位于godzilla\_4.0.1/shells/payloads/java/assets下，实现了命令执行、文件上传/下载、基本信息获取等全部功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297525.png "null")

哥斯拉和冰蝎在原理层的区别在于哥斯拉在初次链接时会将全功能的Java马打入session对象中后续只传具体的方法名到服务端即可执行相应的Java代码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297526.png "null")

而冰蝎则是每次都加载不同的恶意类实现执行任意java代码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297531.png "null")

payload.class全部方法如下：

```
/* 属性 */
PageContext pageContext;
HashMap praameterMap = new HashMap<Object, Object>();
 /* 方法 */
Class g(byte[] b) ：类加载
String get(String key)：获取prameterMap某个键的值
byte[] getByteArray(String key)：获取praameterMap某个键的值

// Shell相关
byte[] run() ：核心方法，根据parameterMap中获取的evalClassName和methodName调用方法
void formatParameter()：{"ILikeYou":"bWV0b28="} prameterMap，又将praameterMap放入request的parameters属性
boolean equals(Object obj)：判断对象是否为PageContext类型
String toString()：调用run方法，并清空request的parameters属性
byte[] test()：返回"ok"的字节码，shell初次链接时确认key和密码使用
void noLog(PageContext pc)：清空日志
handle():

// 文件管理
getFile()、listFileRoot()、readFile()、uploadFile()、newFile()、newDir()、deleteFile() 、moveFile() 、copyFile() 、deleteFiles(File f)

// 命令执行
byte[] execCommand()

// 基础信息
byte[] getBasicsInfo()
byte[] include()
Map<String, String> getEnv()
String getDocBase()
String getRealPath()

// 数据库管理
byte[] execSql()

// 反射
Object invoke(Object obj, String methodName, Object... parameters)
Method getMethodByClass(Class cs, String methodName, Class... parameters)
static Object getFieldValue(Object obj, String fieldName)

// Base64操作
String base64Encode(String data)
String base64Encode(byte[] src)
byte[] base64Decode(String base64Str)
```

## 结果输出

```
f.equals(arrOut);
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297535.png "null")

实例化的payload对象重写的equals方法传入的参数为ByteArrayOutputStream类型，进入handle方法，在handle方法中将传入的arrOut赋值给this.outputStream用于结果输出。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297536.png "null")

## 参数获取

```
f.equals(pageContext);
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297539.png "null")

判断传入类型分别赋值

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297541.png "null")

对应如下

```
ByteArrayOutputStream -> this.outputStream
HttpServletRequest | ServletRequest -> this.servletRequest
[B (byte[].class) -> this.requestData
HttpSession -> this.httpSession
```

参数识别赋值后进入handlePayloadContext，在handlePayloadContext中，通过反射获取request、response、session对象。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297544.png "null")

完成handlePayloadContext后，进行this.requestData的获取。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297547.png "null")

## 代码执行

```
f.toString();
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297552.png "null")

当this.outputStream为空时，初始化SessionMap，使用GZIPOutputStream修饰this.outputStream.

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297557.png "null")

```
formatParameter();//获取服务端接受的参数（方法名）
```

从this.requestData中解压缩数据并存入this.parameterMap。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297562.png "null")

完成 formatParameter后，执行run方法，执行代码输入后清空所有请求相关对象。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297564.png "null")

传入类名为空时执行payload类中对应方法，不为空时从sessionMap中获取类并实例化执行其中对应方法。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194369-1672297567.png "null")

## 流程总结

```
f.equals(arrOut):获取输入对象待用
f.equals(pageContext):获取所有参数
f.toString():执行代码
```

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/194369.html**](https://www.secpulse.com/archives/194369.html)

Tags: [Godzilla](https://www.secpulse.com/archives/tag/godzilla)、[java](https://www.secpulse.com/archives/tag/java)、[命令执行](https://www.secpulse.com/archives/tag/%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Java反序列化：URLDNS的反序列化调试分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1689306075699-300x217.png)

  Java反序列化：URLDNS的反序列化…](https://www.secpulse.com/archives/202757.html "详细阅读 Java反序列化：URLDNS的反序列化调试分析")
* [![界面劫持之拖放劫持](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1688004080281-300x168.png)

  界面劫持之拖放劫持](https://www.secpulse.com/archives/202412.html "详细阅读 界面劫持之拖放劫持")
* [![Java 反序列化之 XStream 反序列化](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1687854074464-300x280.png)

  Java 反序列化之 XStream 反…](https://www.secpulse.com/archives/202377.html "详细阅读 Java 反序列化之 XStr...