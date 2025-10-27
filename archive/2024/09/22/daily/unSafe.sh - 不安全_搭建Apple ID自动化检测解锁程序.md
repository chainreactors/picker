---
title: 搭建Apple ID自动化检测解锁程序
url: https://buaq.net/go-263257.html
source: unSafe.sh - 不安全
date: 2024-09-22
fetch_date: 2025-10-06T18:20:38.599955
---

# 搭建Apple ID自动化检测解锁程序

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/bf8ed35b36423ae1ff671d6eac26ed2a.jpg)

搭建Apple ID自动化检测解锁程序

介绍appleid\_auto，一款基于密保问题的自动化 Apple ID 检测&解锁程序。发卡网站引流必备。前端用于管理账号，支持添加多个账号，并提供展
*2024-9-21 17:48:34
Author: [www.upx8.com(查看原文)](/jump-263257.htm)
阅读量:37
收藏*

---

## 介绍

appleid\_auto，一款基于密保问题的自动化 Apple ID 检测&解锁程序。发卡网站引流必备。

前端用于管理账号，支持添加多个账号，并提供展示账号页面。

支持创建包含多个账号的分享页面，并可以为分享页面设置密码。

后端定时检测账号是否被锁定，若被锁定或开启二步验证则自动解锁，修改密码并向API回报密码。

登录Apple ID并自动删除Apple ID中的设备。

启用代理池和Selenium集群，提高解锁成功率，防止风控。

发卡网站可以使用它来搭建账户分享界面进行引流。

## 特点

* 多用户使用，权限控制
* 多账号管理
* 账号分享页，支持设置密码、有效期、自定义HTML内容
* 自动解锁与关闭二步验证
* 自动/定时修改密码
* 自动删除Apple ID中的设备
* 代理池与Selenium集群，提高解锁成功率
* 允许手动触发解锁

## 部署方法：

### 第一步：更新源并安装依赖

**Ubuntu/Debian：**

**Centos：**

### 第二步：安装 PHP 7.4 和必要的 PHP 扩展

**Ubuntu/Debian：**

**Centos：**

部分系统仓库中没有 PHP 7.4 的包，需要添加外部 PPA 来安装 PHP 7.4

### 第三步：配置PHP 7.4

1. 删除对 `putenv` 函数的禁用
   找到 PHP 的 CLI 和 FPM 的配置文件：

在这两个文件中，查找以下行：

确保 `putenv` 没有在这行中列出。如果列出了，删除它，然后保存文件。

重新启动 PHP-FPM ：

2. 安装 `fileinfo` 扩展

一般情况下，`fileinfo` 扩展应该在安装 PHP 7.4 时已经包含了，可以通过以下命令检查它是否已经启用：

如果它已经启用，应该会看到 `fileinfo` 作为输出。

如果没有启用，可以通过以下命令来进行启用：

### 第四步：安装 MySQL 8.0 并配置

1. 安装 MySQL 服务器。
   **Ubuntu/Debian：**

**Centos：**

2. 启动 MySQL 并设置安全选项。

### 第五步：创建数据库

这是在如下配置过程中填入的数据，可以自行修改

* DATABASE = appleid\_auto
* USERNAME = appleid\_user
* PASSWORD = password

### 第六步：下载项目源码并解压

### 第七步：配置项目

主要对以下内容进行修改：

1. 是否开启注册功能
   ENABLE\_REGISTER = true
2. API Key，用于调用前端的API
   API\_KEY = 123456
3. 是否启用任务后台运行，即不显示浏览器窗口
   TASK\_HEADLESS = true
4. 是否启用代理池
   ENABLE\_PROXY\_POOL = false
5. 当后端报告代理不可用时，是否自动禁用该代理
   PROXY\_AUTO\_DISABLE = false
6. 当任务执行失败时，是否5分钟后重试，否则直接等待下一次执行任务
   FAIL\_RETRY = true
7. 是否开启后端API，来实现在前端控制解锁任务，做到实时更新，并允许用户触发解锁
   ENABLE\_API = true
8. 数据库连接信息
9. DATABASE = appleid\_auto
10. USERNAME = appleid\_user
11. PASSWORD = password

    ### 第八步：安装 Composer 依赖

### 第九步：配置反向代理和伪静态

1. 移动项目到 `/var/www` 目录
2. 确保 `www-data` 用户具有访问权限
3. 安装 Nginx

**Ubuntu/Debian：**

**Centos：**

4. 创建新的 Nginx 配置文件

3. 粘贴以下配置（注意对域名进行修改，我这里以`test.adonis142857.ir`作为示例）：

启用新的站点配置：

### 第十步：导入数据库

### 第十一步：创建管理员账户

### 第十二步：配置后端

安装时按照提示输入参数即可，默认会以appleauto为容器名部署一个Docker容器。

### 第十三步：登录网站配置Apple ID

1. 在浏览器中打开网址

   例如：
2. 在账号管理中添加账号
   ![](https://pic.imgdb.cn/item/64d5c52e1ddac507ccf7d1e8.jpg)
3. 在分享页管理中添加分享页面
   ![](https://pic.imgdb.cn/item/64d5c5b71ddac507ccf91ad2.jpg)
4. 在代理池代理中添加代理（可选）
   ![](https://pic.imgdb.cn/item/64d5c6131ddac507ccf9f0e9.jpg)
5. 在个人信息界面中添加推送（可选）
   ![](https://pic.imgdb.cn/item/64d5c66c1ddac507ccfac0c3.jpg)

   ## 相关地址：

   GitHub地址：<https://github.com/pplulee/appleid_auto>
   官方使用教程：<https://appleid-auto.gitbook.io/doc_zhcn/>

文章来源: https://www.upx8.com/4343
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)