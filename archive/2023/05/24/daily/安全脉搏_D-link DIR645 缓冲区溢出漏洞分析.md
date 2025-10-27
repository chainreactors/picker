---
title: D-link DIR645 缓冲区溢出漏洞分析
url: https://www.secpulse.com/archives/200897.html
source: 安全脉搏
date: 2023-05-24
fetch_date: 2025-10-04T11:37:49.278269
---

# D-link DIR645 缓冲区溢出漏洞分析

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

# D-link DIR645 缓冲区溢出漏洞分析

[漏洞](https://www.secpulse.com/archives/category/vul)

[第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738)

2023-05-23

11,731

**前言**

D-Link DIR-645在实现上存在命令注入及栈缓冲区溢出漏洞，攻击者可利用这些漏洞任意更改内存，以root权限执行任意shell命令或代码。该漏洞是CGI脚本在处理authentication.cgi请求，将请求头的CONTENT\_LENGTH值作为read函数读取文件的内容大小，由于该值可控，因此造成read函数的缓冲区溢出。

**固件模拟**

首先通过attifyos虚拟机进行环境搭建，attifyos虚拟机中集成了常用的固件环境模拟工具。

attifyos虚拟机下载地址：https://pan.baidu.com/s/1Vracsnlt5uNbdmfYK4dp8Q

密码:tvoh

DIR645固件下载地址：https://pan.baidu.com/s/1B7fDB4NETjdGWtlkiPULpw

提取码：5iaz

下载完成后，进入虚拟机目录/home/oit/tools/firmadyne，执行python fat.py

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824658.png)

此时会要求输入所需要模拟的固件地址，这里我将固件放置在桌面，因此目录为/home/oit/Desktop/firewalks/DIR645A1\_FW103RUB08.bin

接下来会要求填写固件的品牌名，可任意填写

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824659.png)

然后便是根据要求不断填写firmadyne的用户密码，在attifyos1.3中，密码为firmadyne。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824662.png)

过程中可能需要填写oit用户的密码，密码为attify123。最后当出现如下页面时，则表示固件模拟成功。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824663.png)

此时访问http://192.168.0.1，可看到路由器登录页面

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824667.png)

**漏洞复现**

向路由器管理系统发现如下请求

```
POST /authentication.cgi HTTP/1.1Host: 192.168.0.1User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept-Language: en-US,en;q=0.5Content-Type: application/x-www-form-urlencodedReferer: http://192.168.0.1/Content-Length: 7044Cookie: uid=TjnCBrkNZjConnection: close
uid=A21G&password=AAAAAA1024*A
```

返回结果如下图所示，造成相关服务500，无法访问

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824668.png)

而正常的请求结果如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824672.png)

请求体的内容超长导致了dir645出现了缓冲区溢出，从而拒绝服务。

**漏洞分析**

首先通过binwalk解压固件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824673.png)

进入到路由器系统目录下，发现请求的authentication.cgi路径，实际处理文件为cgibin

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824678.png)

接下来对cgibin进行反编译，将该程序导入到ida中，默认进入初始函数的main函数中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824680.png)

F5查看伪代码，可以看到main函数主要是判断请求uri，根据不同的uri选择不同的函数进行处理

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824682.png)

如果为authentication.cgi，则进入authenticationcgi\_main函数处理，并将请求的数据作为参数值传入该函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824685.png)

进一步进入authenticationcgi\_main函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824690.png)

在这个函数里，根据请求方式的不同，进入不同的程序逻辑处理。我们的漏洞利用poc为post方法，查看post相关逻辑

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824692.png)

可以看到，当为post请求时，读取CONTENT\_LENGTH和CONTENT\_TYPE的值，若不为空，则将相关参数值传入到read函数里进行读取。函数为read(v21,v70,v20)

根据c语言的函数用法如下所示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824694.png)

我们可以看到，该函数用于读取打开文件的内容。其中第一个参数为要读取的文件内容，第二个参数为读取到的内容保存的缓冲区，第三个参数指定所要读取文件的长度。这个函数如果使用不规范的话，当第三个参数指定的读取文件长度超过第二个参数所定义的缓冲区大小时，就造成了缓冲区溢出漏洞。

那么在这里漏洞案例中，我们来看下read（v21,v70,v20) 函数所对应的这三个参数值分别是什么。

v21=fileno(stdin) 为用户输入的值，即post请求体的中的body数据

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824697.png)

v70为函数定义的数据结构，大小为1024比特

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824699.png)

v20 = atoi(v18)= atoi(getenv(“CONTENT\_LENGTH”），为CONTENT\_LENGTH的值

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200897-1684824704.png)

由于这里v20所代表的读取内容的长度是用户可控的，因此当设置CONTENT\_LENGTH大于1024，请求体内容超长时，就造成了read函数出现缓冲区溢出漏洞

**本文作者：[第59号实验室](newpage/author?author_id=49738)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200897.html**](https://www.secpulse.com/archives/200897.html)

Tags: [attifyos虚拟机](https://www.secpulse.com/archives/tag/attifyos%E8%99%9A%E6%8B%9F%E6%9C%BA)、[D-Link DIR-645](https://www.secpulse.com/archives/tag/d-link-dir-645)、[缓冲区溢出](https://www.secpulse.com/archives/tag/%E7%BC%93%E5%86%B2%E5%8C%BA%E6%BA%A2%E5%87%BA)、[缓冲区溢出漏洞](https://www.secpulse.com/archives/tag/%E7%BC%93%E5%86%B2%E5%8C%BA%E6%BA%A2%E5%87%BA%E6%BC%8F%E6%B4%9E)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![安全攻防 | 浅谈ms17-010多种利用方式](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1671787149061-300x233.png)

  安全攻防 | 浅谈ms17-010多种利…](https://www.secpulse.com/archives/194017.html "详细阅读 安全攻防 | 浅谈ms17-010多种利用方式")
* [![浅谈软件安全开发](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189560-1666337028-300x213.png)

  浅谈软件安全开发](https://www.secpulse.com/archives/189560.html "详细阅读 浅谈软件安全开发")
* [![CVE-2021-3156：Sudo 堆缓冲区溢出漏洞 POC](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/08/16299630801-300x201.png)

  CVE-2021-3156：Sudo 堆…](https://www.secpulse.com/archives/163895.html "详细阅读 CVE-2021-3156：Sudo 堆缓冲区溢出漏洞 POC")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱
...