---
title: 手把手教你成为白帽黑客!Web架构基础（上）
url: https://mp.weixin.qq.com/s/G8JBVIp__ef_5jmzK38GQg
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:31:52.963586
---

# 手把手教你成为白帽黑客!Web架构基础（上）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21YD652wtnGcPB30lfMonnuY0y1P0PdGYGTzIV0Y7icmaXjdTOf9vRwlA/0?wx_fmt=jpeg)

# 手把手教你成为白帽黑客!Web架构基础（上）

原创

南风
南风

南风安全站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI215GJubhpqniamgeiagjbru3mMjbMmxgJS4AXH0HhJ083vu8KnriaJhL6MQ/640?wx_fmt=png&from=appmsg)

观看前还请动动小手点个关注，下章将详解MySQL数据库基础!本号将逐步分享网安全栈知识，手把手教你成为白帽黑客!注意：文中出现的云主机公网IP信息及对于账号密码信息均已改动失效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI219Oews67ic3mMDtCiaWWU0V62vcwK6RMpS6u9ibLWLib4hvqOyS03UFO6uA/640?wx_fmt=png&from=appmsg)

PART 01

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI2191RXVEdzueAPnbJOVSClPsgdC4I7gAGODjEibQ5kaAGibxbUuWdywQLQ/640?wx_fmt=png&from=appmsg)

Web架构基础（上）

一、Web与HTTP协议和HTML简介

全球广域网（World Wide Web），即万维网。

1.1 Web架构

0x01 C/S架构

即客户端/服务端（Client/Server）架构，其中客户端（如微信）负责用户交互和数据展示，服务器端处理核心业务逻辑和数据存储，确保职责分离和安全高效；例如：服务端管理共享数据如商品信息或用户账户，客户端则存储本地数据如聊天记录以提升响应速度或支持离线使用，这种架构优势在于集中维护和安全性高，但需注意网络依赖和客户端兼容性等挑战。

0x02 B/S架构

即浏览器/服务端（Browser/Server）架构，是基于浏览器的访问模式，用户通过浏览器直接访问服务端（如淘宝网站），无需安装额外软件。服务端集中处理所有业务逻辑和数据存储，浏览器仅负责界面展示和指令传递，这种架构显著降低了开发和维护成本，并支持跨平台访问，用户只需一个浏览器即可使用不同网站的服务。

1.2 Web发展

0x01 Web 1.0阶段

纯静态页面，无交互功能，仅展示内容。客户端页面使用 HTML语言开发。

0x02 Web 2.0阶段

支持用户上传信息、交互和购物。服务端后台开发语言包括 PHP、Java、Ruby、Python等，后台开发语言主要用于生成动态页面。

0x03 Web 3.0阶段

移动互联网时代，实现衣食住行等各种需求，仅需使用手机。服务端后台开发语言包括 PHP、Java、Ruby、Python等。

1.3 HTTP协议简介

HTTP（Hyper Text Transfer Protocol超文本传输协议）是由蒂姆·伯纳斯-李于1990年发明，作为万维网数据通信基础标准。它采用请求-响应模型实现客户端（如浏览器）与服务端高效交互，通过无状态特性简化系统设计。当前HTTP/1.1至HTTP/3版本持续演进，支持文本、图像、视频等传输，成为现代Web应用核心通信机制。

1.4 HTTP数据传输过程

0x01 用户发起请求

用户在浏览器输入URL，触发HTTP请求。

0x02 浏览器生成请求报文

浏览器将操作转化为HTTP请求报文（含请求头、方法等），发送至服务端。

0x03 数据网络传输

请求通过互联网（经路由器、DNS解析等）传输至目标服务器。

0x04 服务端处理并响应

服务器解析请求，执行逻辑（读取数据库），生成HTML文档作为HTTP响应返回。

0x05 数据传输至客户端

响应数据包通过互联网传回用户设备，由浏览器接收。

0x06 渲染展示页面

浏览器解析HTML内容，加载关联资源（CSS/JS），最终渲染可视化页面给用户。

1.5 HTTP数据传输演示

找到部署网站的某图片文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0QI3nH3lkWMyR4BoHTMKrwHolqiaDvXSmjpJJYSUewyqEmnjCw1pQLqFDmOI7jAcibhfM0Xic66xKpYQ/640?wx_fmt=png&from=appmsg)

访问此图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0QI3nH3lkWMyR4BoHTMKrwHzAOFXzypL7UufMU2aoKX2XJ6EteYyzogyUNFUfa7B4e0ZDica6QT9CA/640?wx_fmt=png&from=appmsg)

Wireshark抓包

虚拟机 NAT模式，抓Vmnet8网卡数据包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0QI3nH3lkWMyR4BoHTMKrwHhLcuMcgXo4g6p1qvZuXzVCfaujWeFYmbuCqvJOF8g5PsibP1dLbdibicQ/640?wx_fmt=png&from=appmsg)

抓包期间访问图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0QI3nH3lkWMyR4BoHTMKrwHmt5Ll1TnNOpJia1IWV6RVJDbKfcHFLCZHKWQZ0FTrRicaibaO0C6APiabQ/640?wx_fmt=png&from=appmsg)

右键-追踪流-HTTP或TCP流

回应 304，拿到缓存页面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0QI3nH3lkWMyR4BoHTMKrwHWVkWXS9GEx4Lmkqia7YURsvspqtOf9fP1WibraFnHtEpQJ2zC6bFCyyg/640?wx_fmt=png&from=appmsg)

重新抓包 map.jpg图片

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21bAwBJflibm3Mic2JlVCLAArUv37WgNeXj33wvHhcnIBQO40abVz4TpZw/640?wx_fmt=png&from=appmsg)

右键——追踪流——HTTP或TCP流

红色部分是发送的网络数据请求

蓝色部分就是服务端响应的数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0QI3nH3lkWMyR4BoHTMKrwHGpd7OCFTqv3ZM0TzE0rf1ChcymPdEn2R6agicBHTRkmD4wzV8E7zR9g/640?wx_fmt=png&from=appmsg)

```
HTTP协议分两部分：请求协议与响应协议请求协议包含：请求行、请求头、请求体（请求数据）响应协议包含：响应行、响应头、响应体（响应数据）
```

1.6 请求数据

浏览器检查里也可看到HTTP 协议数据

0x01 请求行

```
GET /yiliao/images/map.jpg HTTP/1.1
```

```
GET    是请求方法之一，获取指定资源。POST    用于提交数据给服务器进行处理。/yiliao/images/map.jpg    请求资源路径，服务器图片路径，也是统一资源标识符URI。HTTP/1.1    是HTTP协议版本。http://192.168.159.160:80/yiliao/images/map.jpg    是统一资源定位符URL。
```

0x02 请求头

```
Host: 192.168.159.160      指定服务器主机名或IP地址。Connection: keep-alive      指示客户端和服务器间连接是否保持活跃，以便在同一连接上发送多个请求。Upgrade-Insecure-Requests: 1      表示客户端愿意升级到HTTPS安全连接。User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML,like Gecko)Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0    用户代理标识，告诉服务器客户端操作系统和浏览器信息。Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7：      指示客户端可接受的响应内容类型。Accept-Encoding: gzip, deflate：    指示客户端支持的响应内容的压缩编码方式。Accept-Language: zh-CN,zh;q=0.9
```

0x03 请求空行

用于隔断请求协议与响应协议

0x04 请求体

提交的信息，如密码验证码等

0x05 请求方法

```
GET    获取指定资源（如网页、图片），仅用于数据读取，无副作用。POST    提交数据到服务器（如提交表单），常用于创建新资源或触发操作。HEAD    与GET类似，但只返回响应头（不含数据体），用于检查资源状态。PUT    更新指定资源（需提供完整数据），常用于覆盖式修改。TRACE    回显客户端请求，用于测试或诊断路径（实际开发较少使用）。OPTIONS    获取服务器支持的HTTP方法列表（如检测CORS配置）。DELETE    删除指定资源（如移除服务器文件或数据库条目）。CONNECT    主要用于通过代理服务器建立安全隧道（如用于 HTTPS 连接）。
```

1.7 响应数据

0x01 响应行

```
HTTP/1.1 200 OK
```

```
HTTP/1.1      是HTTP版本200 OK        状态码常用状态码https://www.cnblogs.com/gitnull/p/9532129.html
```

0x02 响应头

显示服务端的信息

```
Date: Wed, 04 Aug 2021 02:22:11 GMT Server: Apache/2.4.6 (CentOS) PHP/5.4.16 Last-Modified: Fri, 04 May 2018 08:13:44 GMT ETag: "a49-56b5ce607fe00" Accept-Ranges: bytes Content-Length: 2633 Content-Type: text/html; charset=UTF-8
```

0x03 响应空行

分隔作用，响应头结束和响应体开始

0x04 响应主体

包含服务器返回的实际数据内容

0x05 HTTP状态码

```
200 OK301 永久跳转 被浏览器记住302 临时跳转 被浏览器记住403 权限拒绝404 文件找不到500 服务器内部错误502 错误的网关504 网关超时
```

0x06 HTTP版本

```
HTTP/0.9    仅GET方法，无头部功能极简，无法扩展HTTP/1.0    新增POST/HEAD、头部字段、状态码仅支持短连接、无Host头HTTP/1.1    长连接、Host头、扩展方法、分块传输HTTP/2.0    二进制帧、多路复用、头部压缩，需HTTPS部署
```

1.8 HTML简单了解

HTML ( HyperText Markup Language ) 超文本标记语言 ，由 SGML (标准标记语言)发展而来，也叫 Web 页面。扩展名是 .html 或 .htm 。

HTML 是一种用来制作网页的标准标记语言。超文本是指超出普通文本范畴的文档，可以包含文本、图片、视频、音频、链接等元素。

HTML 不是一种编程语言，而是一种写给网页浏览器、具有描述性的标记语言。

0x01 HTML结构和标签格式

```
<!DOCTYPE html><html lang = "en">  <head>    <meta charset = "UTF-8">    <title>ida小站</title>  </head>  <body>    <h1>Hello World<h1>  </body></html>
```

0x02 结构释义

```
<!DOCTYPE html>    告诉浏览器使用什么样的html或xhtml来解析html文档。<html></html>    文档开始标记和结束标记，告诉浏览器是HTML文档，之间是文档头部<head> 和主体<body>。元素出现在文档开头部分，与之间的内容不会在浏览器的文档窗口显示，但是其间的元素有特殊重要的意义。<meta charset="UTF-8">    声明编码方式用UTF-8字符集。<title></title>     定义网页标题，在浏览器标题栏显示。<body></body>    主体之间的文本是可见的网页主体内容。
```

0x03 标签语法

```
<标签名 属性1=“属性值1” 属性2=“属性值2”……>内容部分</标签名> <标签名 属性1=“属性值1” 属性2=“属性值2”…… />
```

```
1、HTML标签由尖括号包围的特定关键词2、标签分为闭合和自闭合两种标签3、HTML不区分大小写4、标签可以有若干个属性,也可以不带属性,比如就不带任何属性5、标签可以嵌套,但是不可以交叉嵌套6、XHTML是实现HTML到XML的过渡。
```

1.9 演示编写网页

编写html代码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Q2RicrMPuBPozOuD8FamvRibBYESlOLuLohaBRIjqttibcQeBYm2u90sC0YVsuMnMIJzx9Mic6ibEIKtQ/640?wx_fmt=png&from=appmsg)

保存并用IP地址文件名访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Q2RicrMPuBPozOuD8FamvRibiaFKZibzd0Z99FAH5Al6Zme8vsNB96KUSTjOHXpK9Va37yBibLicAOdCZw/640?wx_fmt=png&from=appmsg)

跳转至百度

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Q2RicrMPuBPozOuD8FamvRibcoK3TJhDicsnSu7sibvBicKYHYiaibm8jBu6p0uiaWlGWNwZPibFRSJv774pw/640?wx_fmt=png&from=appmsg)

解压准备好的网站源代码

删除css文件夹，访问纯HTML效果

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Q2RicrMPuBPozOuD8FamvRibhPqkZdibx5GhJiabibERf93GPO5F7PSIC1XqI9eg0rHJ5bNMzFrgHia8sw/640?wx_fmt=png&from=appmsg)

二、Nginx安装和配置

2.1 Web服务器应用软件

```
清华大学开源镜像站：https://mirrors.tuna.tsinghua.edu.cn/
```

Apache和Nginx等属于Web服务器应用软件（也称为Web Server），是部署在服务端的核心程序，用于处理HTTP请求和响应。

Apache是开源Web服务器软件，后发展为Apache软件基金会。原始Apache服务器软件现已更名为HTTPD（HTTP守护进程），成为该基金会下的核心子项目。

0x01 Apache

Apache是早期主流的Web服务器软件，曾占据较大市场份额。随着技术演进，新兴的Nginx凭借其卓越性能快速崛起，如今已成为全球最常用的Web服务器，广泛应用于高流量场景。

0x02 Nginx

高性能与高并发：采用事件驱动架构，高效处理海量并发请求，减少资源消耗（如内存占用低）。

可靠性与适用性：适用于大型网站（如电商、社交媒体），全球大量知名站点依赖其稳定运行。

2.2 安装Nginx和Apache

0x01 安装Nginx

查看当前系统yum库软件包

```
指令：yum repolist
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI217L0fKTB7UVDFsVmg0qYkUliayav8s6N1POcppxShVInlB8sibODqdGzQ/640?wx_fmt=png&from=appmsg)![]()

```
安装yum扩展包：yum install epel-release -y
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Q2RicrMPuBPozOuD8FamvRibvu8MazROoXuZ8Sdpd4QS6oeoJOicuUZZ4bnVVSPtUWM0Zsm1IC7kxFw/640?wx_fmt=png&from=appmsg)

```
安装Nginx软件：yum install nginx -y
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Q2RicrMPuBPozOuD8FamvRibZofQ897HbSYibYMxBjMnRQUSibcsK9hhY6KAghl8HRicoQiaWFQMGxbF0Q/640?wx_fmt=png&from=appmsg)

开启 nginx服务

```
...