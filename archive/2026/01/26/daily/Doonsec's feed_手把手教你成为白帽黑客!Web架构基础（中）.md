---
title: 手把手教你成为白帽黑客!Web架构基础（中）
url: https://mp.weixin.qq.com/s/BIp8wVczLqHzYK80HjanmA
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:34:31.949539
---

# 手把手教你成为白帽黑客!Web架构基础（中）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21Hk1BPf3v1deAricOnNZqNcfXvicjevnk0WvKPCgGVtJpfJlR3GveXQAQ/0?wx_fmt=jpeg)

# 手把手教你成为白帽黑客!Web架构基础（中）

原创

南风
南风

南风安全站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Qf0Gh2FvlZA1kyGRIOibTuuficYLUsBtbWonLYzJCtZDHEOTHiaWk5yn5HZcV1djeoia8FYiaPfpGWH3A/640?wx_fmt=png&from=appmsg)

观看前还请动动小手点个关注，本号将逐步分享网安全栈知识，手把手教你成为白帽黑客！注意：文中出现的云主机公网IP信息及对于账号密码信息均已改动失效。文末扫码获取资料。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Qf0Gh2FvlZA1kyGRIOibTuumLKdsTcakVhPhTCXkqjPyW73scOQWibvhiamskrdRSCtrEfPME2hXppg/640?wx_fmt=png&from=appmsg)

PART 01

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0Qf0Gh2FvlZA1kyGRIOibTuufMOdvYMgcnibNa8jV83DicRVb28icsXe5smhjnzuBsibAXMTSduXjOhlSQ/640?wx_fmt=png&from=appmsg)

Web架构基础（中）

一、Nginx和PHP动态网站

```
前端：如HTML、CSS、JS等，用于创建用户界面和处理用户输入。后端：如PHP、Node.js、Python等，用于处理服务器端逻辑和数据存取。数据库：如MySQL、PostgreSQL等，用于存储和检索数据。
```

1.1 静态页面和动态页面

静态页面与动态页面的区别主要体现在页面内容的更新和用户交互方面。

0x01 静态页面

静态页面以纯 HTML文件为核心载体，其内容固定且不随用户访问行为动态变化，所有用户在任何时间、地点访问时，看到的页面内容完全一致，不存在动态数据展示，这类页面被称为纯静态页面。尽管静态页面可通过嵌入JS脚本实现动画效果、表单验证等交互增强，但只要页面核心内容不因用户操作或时间推移发生改变，仍属于静态页面。

```
内容一致性：  无论何时何地访问，页面内容都是相同的。无服务器处理：不需要服务器端程序来生成或修改内容。速度快：     无服务器端处理，通常加载速度更快。
```

0x02 动态页面

动态页面与静态页面的区别在于内容的实时性与个性化：动态页面内容由服务器端根据用户请求（登录状态、搜索关键词）、时间（实时数据更新）、环境（地理位置）等因素实时生成，非固定 HTML文件；每次访问可能呈现不同数据（电商商品库存变化、社交动态信息流），页面结构可复用但数据层动态更新。当前主流网站（如电商、社交、资讯平台）均采用动态页面架构，以实现交互性与个性化服务。

```
内容变化：    每次访问页面内容都可能不同，依赖于实时数据或用户交互。服务器端处理：服务器端语言如 PHP、Python等负责生成内容，并发送到浏览器。交互性：      动态页面能响应用户输入，如搜索、提交，且根据输入显示不同数据。
```

0x03 数据交互

动态网站的数据交互是用户与服务器间的双向通信：用户通过浏览器触发操作（如点击、提交、输入），前端将请求（含参数）发至服务器；服务器接收后，通过后端逻辑处理数据（如调用 API、执行数据库查询），并将结果（如JSON格式的数据、状态码）返回前端；前端最终将响应渲染为用户可见的动态内容。

0x04 Nginx的作用

Nginx常用于处理HTML、CSS、JS等静态文件请求；对动态内容Nginx通过反向代理间接支持：用户请求动态内容，Nginx将请求转发至后端应用服务器（Tomcat），后端服务器运行应用程序（如执行数据库查询）生成动态内容后返回Nginx，由Nginx最终响应给用户，例如用户在百度搜索关键词时，Nginx作为前端反向代理接收请求并转发至百度后端搜索服务器，后端查询数据库获取结果后通过Nginx返回给用户。

1.2 Nginx加PHP做动态页面

要在 Nginx中配置PHP以运行动态页面，您需要遵循以下步骤：

0x01 安装PHP插件

PHP很多功能依赖特定插件（模块），安装好模块后PHP将具备额外特殊功能。

安装插件

```
指令： yum install php-fpm php-mbstring php-mysqlnd php-gd -y
```

该指令用于在 Red Hat系Linux系统（如CentOS、RHEL）中安装PHP的多个扩展。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21UqY87UzBYOE0KlpSWQPMI8maDdSJoaOGQFPia7pJQLg37vS822Ulkdg/640?wx_fmt=png&from=appmsg)![]()![]()![]()

php-fpm插件作用

是 PHP进程管理器，用于管理PHP FastCGI进程，常用于Web服务器Nginx与PHP应用程序间的通信。

php-mbstring插件作用

是 PHP的mbstring扩展，提供了对多字节字符串的函数支持，对于处理非ASCII字符集（如UTF-8）非常重要。

php-mysqlnd插件作用

是 PHP的mysqlnd扩展，提供与MySQL数据库服务器通信的接口。允许PHP脚本连接到MySQL数据库并进行数据操作。

php-gd插件作用

是 PHP的gd扩展，提供一系列的图形处理功能，包括创建图像、处理图像和输出图像到浏览器，常用于生成图表或修改图片。

-y参数

表示在安装过程中， yum将不会出现任何确认提示，直接执行安装。可以在自动化脚本中使用，因为它允许无交互安装。

调整配置

文件 www.conf第39和41行用户和用户组改为nginx，否则后续会因权限报错。

```
user = nginxgroup = nginx进入目录： cd /etc/php-fpm.d/调整配置： vim www.conf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21AS25BKwL5V0pzM9lUPGuDPgKFBEYmWrXJWyHcmUPbZNiaTPmPmSy66Q/640?wx_fmt=png&from=appmsg)![]()![]()![]()

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21KSCwLib1uBUTN7lx4zduJMNViasnaBVZuuRsSpvKU0BqXia5KHfliaHCoA/640?wx_fmt=png&from=appmsg)![]()![]()![]()

```
重启程序： systemctl start php-fpm.service开机自启： systemctl enable php-fpm.service
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21xFwiagniaxYem2BicVJcysmLeU2DyYicpicwudOjoQPanaZHDo9sYa157aQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()

查看运行状态：开启 php-fpm服务后，会默认开启9000端口。

```
查看状态： netstat -lntup
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21xe6SCFhjRrkT9jjHVUvlZRIkXggDGOZOeIu3ib9hbGpibVibrXPrzRUhw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

0x02 插件PHP-FPM的作用流程

PHP-FPM作为PHP进程管理器，通过FastCGI协议与Nginx协作，处理动态PHP请求。Nginx负责接收请求并转发给PHP-FPM，PHP-FPM执行PHP代码后将结果返回给Nginx，最终响应给用户。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21PArPN2tuKvbp9KhRbuwGAI5vKRYo1xSxjFFIGhS7w37kR2m00SkAMg/640?wx_fmt=png&from=appmsg)![]()![]()![]()

1、浏览器访问PHP文件

浏览器输入网址并请求某 PHP文件时（index.php），浏览器向服务器发送HTTP请求。请求通过DNS解析找到服务器IP地址，然后通过TCP/IP协议发送到Nginx。

优化建议：使用 CDN（内容分发网络）来缓存静态资源，减少对服务器的直接请求。确保服务器的网络连接稳定，带宽足够处理预期流量。

2、Nginx服务器转发请求

Nginx作为Web服务器，负责接收用户请求，当收到请求时，它会检查请求URL

来判断是否需要处理 PHP文件，若需要，则会自动转发给PHP-FPM处理。

优化建议：配置Nginx的location块，确保仅特定PHP文件或目录才被转发到PHP-FPM。使用Nginx的try*files指令，先检查文件是否存在，以减少不必要的PHP-FPM处理。优化Nginx的缓存设置，如proxy*cache，以减少对后端服务器的请求。

3、PHP-FPM处理PHP文件

PHP-FPM接收到Nginx转发的请求后，会执行PHP文件，将PHP代码转换为HTML代码。此过程涉及PHP解释器执行PHP脚本，并与数据库进行交互（如果有），然后生成HTML输出给Nginx服务器。

优化建议：优化 PHP-FPM配置，如pm.max*children和pm.start*servers，以适应服务器的CPU和内存。

使用 PHP-FPM的SSL/TLS，以减少加密和解密操作。优化PHP代码，减少执行时间，如使用缓存机制、优化数据库查询。用OpCode 缓存来避免重复编译PHP代码。

4、Nginx返回HTML代码

PHP-FPM处理完成后，生成的HTML代码会被发送回Nginx，Nginx再将HTML代码返回给用户的浏览器。

优化建议：启用GZIP压缩，减少传输的数据量。配置合理的HTTP头，如Content-Type和Cache-Control，以指导浏览器如何处理内容。如果使用了HTTP/2，确保Nginx和PHP-FPM都正确配置以支持HTTP/2。

5、总结

优化 PHP-FPM工作流程涉及到多个层面，包括网络配置、服务器硬件、Web 服务器和PHP-FPM的配置，及PHP代码质量。通过在每个步骤中实施上述优化建议，可以提高整个工作流程的效率和性能，从而为用户提供更快的服务。

0x03 配置Nginx

需给Nginx做配置，才能自动转发请求给php-fpm

创建站点

```
进入配置目录： cd /etc/nginx/conf.d/创建配置文件： vim panch.conf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21t8TOVNa8ibjfwSZEeE02Ap3rLj3SnxpSF4sHEsFsUywXmHEHXhqZHibw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

添加配置

在创建的站点配置文件添加 Nginx连接 php-fpm 的配置。

```
添加配置： vim panch.conf查看配置： cat -n panch.conf
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21fLC73NwtGGTEbwYB025icvp13VSic2pbzbKibjEGdgok3UPibrA4gEOjug/640?wx_fmt=png&from=appmsg)![]()![]()![]()

确保所有路径和端口都与服务器实际匹配

为 /usr/share/nginx/html/panch；

创建站点目录

```
进入根目录： cd /usr/share/nginx/html/创建站点目录： mkdir panch
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21ibgEKWwEFWlCFr6FhdoEzwEpZjxiciaCQPT6rWma5Bxgic0qXvInARjNrw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

```
检查语法：nginx -t重启服务：systemctl restart nginx
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21tymUndGIQdGwrdFG8Pvr6iab6c9J1CEJOnLpjdaibxcYuB7s9vIEohEw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

站点目录放入源码

```
下载可道云的源代码作为站点： http://kodcloud.com/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21EQFsENMIAOLWxF3Gy2q8Yn83TKBtjuicrf0eAKOdUzib7TQeZ1DScIicw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

上传代码到站点根目录并解压

```
进入目录： cd panch上传源码： rz -E解压文件： unzip kodexplorer4.51.zip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21EtNjmlhVnQm2sYhxR7Oia2Ocq7MqOicCicyQOyyPknbWOlRIwbHUiakFXA/640?wx_fmt=png&from=appmsg)![]()![]()![]()

```
删除原压缩包： rm -rf kodexplorer4.51.zip查看解压内容： ls
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21j5ibWWWMY05OBMWBIniaPhSicWVkq96jxSur01fbhiaJdtIv3dcmmpE0BQ/640?wx_fmt=png&from=appmsg)![]()![]()![]()

查看Nginx和PHP-FPM的启动用户

都是 nginx用户，但是panch目录的代码文件是root用户。

```
指令： ps -ef|grep nginx
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21zbNYUib5p1aowbbPloZkQaqI1epOML0iaf7YUtdZ1LhYrsTIJUWfCVfA/640?wx_fmt=png&from=appmsg)![]()![]()![]()

此时 Nginx用户没有权限对此目录进行上传文件等操作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21TsX90hccTSC7CLL5YoJrY8Joufu9oQAibYXicwVniccKAXelWmnh6tEAA/640?wx_fmt=png&from=appmsg)![]()![]()![]()

修改目录权限

将当前目录所有文件、文件夹及其子目录和子文件的用户和用户组都改为 Nginx。

```
参数 -R：意为所有的意思。修改指令： chown -R nginx:nginx .
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21LPPvWW3JmibYyVJyviaTYAP0qiaialOQl0gVREF049gydeHamnic9YvslVw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

在 hosts文件里添加网站域名panch.com

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21e6N1PXnJKEVj9F5N8MKYfT5XeEIAbYBEdDia3uztCNicDyWXcEmdgaWw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI21NoOxcmkmgH7oSQYiaaS9HtAVbQflYtOkJ86XR8Qy6b7RDEqE1qxugyw/640?wx_fmt=png&from=appmsg)![]()![]()![]()

默认管理员是 admin

设置密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/jDyiaHT64L0SS8tZE8rtpOqgjdhLyTI211DqBTjJ0nFtGSWpQM7CKOgHpfv7l3G...