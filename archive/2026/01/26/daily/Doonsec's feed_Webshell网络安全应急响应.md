---
title: Webshell网络安全应急响应
url: https://mp.weixin.qq.com/s/ReV9hl9Zik0UnWzwFjo2Gw
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:36:25.971642
---

# Webshell网络安全应急响应

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Mojwgx57LachDUOk3wN4roWicZxNIyHwLXLEZcb7dwgweIiaMspjHlQ7icSIn3guv2Yyhiasswj8vFoLxuowpbaJTA/0?wx_fmt=jpeg)

# Webshell网络安全应急响应

照夜清网络科技

![]()

在小说阅读器中沉浸阅读

#

### **1.1 webshell简介**

Webshell通常指以jsp、asp、php等网页脚本文件形式存在的一种服务器可执行文件，一般带有文件操作、命令执行功能，是一种网页后门。攻击者在入侵一个网站后，通常会将webshell后门文件与网站服务器web目录下正常的网页文件混在一起，使用浏览器或专用客户服务端进行连接，从而得到一个服务器操作环境来控制网站服务器。

### **1.2 webshell分类**

根据不同脚本名称划分，常见webshell服务器类型有jsp、asp、php等

1.JSP型webshell脚本

JSP是一种动态web资源的开发技术。Jsp是在传统的网页HTML文件中插入Java程序段和JSP标记形成的JSP文件（\*.jsp）

JSP型webshell脚本如下：

<%Runtime.getRuntime().exec(request.getParameter(“i”));%>

2.ASP型webshell脚本

是一种服务器开发专用脚本。可以与数据库和其他程序进行交互，是在IIS中运行的一种程序。

ASP型webshell脚本如下：

<%eval request(“cmd”)%>

3.PHP型webshell脚本

是一种通用开源脚本语言，主要适用于web开发领域。PHP可支持常见数据库及操作系统，可快速执行动态网页。

PHP型webshell脚本如下：

<?php

$a=exec($\_GET[“input”]);

Echo $a;

?>

### **1.3 webshell用途**

1.站长工具持续远程控制

一般用途是通过浏览器来对网站所在的服务器进行运维管理。现演变为在线编辑文件、上传和下载文件、数据库操作、执行命令等。

2.持续远程控制

网站通常会被攻击者单独、持续控制，同时webshell本身所拥有的密码验证可以确保其在未遭受暴力破解攻击时，只被其上传者利用。

3.权限提升

Webshell执行权限与web服务器运行权限相关。一般情况下，webshell为普通用户权限，此时攻击者为了进一步提升控制权限，会通过设置任务计划，内核漏洞等方法来获取root权限。

4.极强隐蔽性

部分恶意网页脚本可以嵌套在正常网页中运行，且不容易被查杀。一旦webshell上传成功，其功能也将被视为所在服务器的一部分，流量传输也将通过web服务器本身进行，拥有极强隐蔽性。

### **1.4 webshell检测方法**

1.基于流量的webshell检测

方便部署，可以通过流量镜像直接分析原始信息。基于payload的行为分析，我们不仅可以对已知webshell进行检测。还可以识别出未知的、伪装性强的webshell，对webshell访问特征、payload特征、path特征、时间特征等进行关联分析，以时间为索引，可还原攻击事件。

2.基于文件的webshell检测

通过检测文件是否加密，创建webshell样本hash库，可对比分析可疑文件。对文件的创建时间、修改时间、文件权限等进行检测，以确认是否为webhell。

3.基于日志的webshell检测

对常见队中日志进行分析，可有效识别webshell的上传行为。通过综合分析回溯整个攻击过程。

下图是Linux命令检索：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LachDUOk3wN4roWicZxNIyHwLn5O1sdl7dZyicm82a7O604ZGy4iaFz0ByCYjyjt9K47JU0H3FYm2BjSg/640?wx_fmt=png&from=appmsg)

### **1.5****初步判断**

1.了解事件表现

1)网页被篡改、存在非管理员设置内容。

2)出现攻击者恶意篡改网页或者网页被植入暗链的现象

3)安全设备报警，或被上级部门通报遭遇webshell。

2.判断事件发生时间

查看webshell的创建时间，结合异常现象发生的时间，定位大致的时间发生时间段

3.判断系统架构

查看系统本身是否存在漏洞，包括服务器、CMS、框架、数据库、脚本语言、业务架构等

4.临时处置

删除检测到的Webshell文件，对文件进行备份，方便后续取证溯源。对系统进行隔离，防止影响其他系统的。

### **1.6 webshell防御**

网页一旦被植入webshell，攻击者就能利用它获取服务器权限、控制发起DDos攻击、网页篡改、网页挂马、内部扫描、暗链/黑链植入等一系列攻击行为。下列是一些防御行为：

（1）配置必要防火墙，开启防火墙策略，防止暴露不必要的服务行为为攻击者提供利用条件。

（2）对服务器进行安全加固，关闭远程桌面功能、定期更换密码、禁止使用最高权限用户运行程序、使用HTTPS加密协议等。

（3）加强权限管理，对敏感目录进行权限设置，限制上传目录的脚本执行权限。

（4）安装webshell检测工具，隔离查杀，排查漏洞。

（5）排查程序存在漏洞并及时修补。

（6）时常备份。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LafVoHCH05Wd0EPtOu1AkoetmINp14nOcpFXqpaCLXGWAnBvCMXiaZrmmLk0dLjtJKmgAiczRUib03HgQ/0?wx_fmt=png)

照夜清网络科技

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Mojwgx57LafVoHCH05Wd0EPtOu1AkoetmINp14nOcpFXqpaCLXGWAnBvCMXiaZrmmLk0dLjtJKmgAiczRUib03HgQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过