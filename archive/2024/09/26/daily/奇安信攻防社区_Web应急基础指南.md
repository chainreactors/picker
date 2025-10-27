---
title: Web应急基础指南
url: https://forum.butian.net/share/3768
source: 奇安信攻防社区
date: 2024-09-26
fetch_date: 2025-10-06T18:20:00.851025
---

# Web应急基础指南

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

### Web应急基础指南

1 总述
web应急实际上是基于webshell和各类web漏洞如sql注入、RCE的应急响应。从抽象定义角度来说它独立于OS也就是windows或linux之外，但在实际操作中又常常与操作系统无法分开。
本篇中只涉及...

1 总述
====
web应急实际上是基于webshell和各类web漏洞如sql注入、RCE的应急响应。从抽象定义角度来说它独立于OS也就是windows或linux之外，但在实际操作中又常常与操作系统无法分开。
本篇中只涉及web部分，对于攻击队后续的维权手段（如CS马）等不做涉猎。
本文中不会出现安全设备日志分析相关知识（因为1厂商设备太多2笔者工作中接触不到多少安全设备3很多情况下客户那里是没有设备的），我们将从最原始的web日志，根据下面的应急响应四步骤开始分析。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723001427695-711e9d52-995c-43e2-9c25-2435957481a8.png)
2 信息搜集
======
基于web应急的信息搜集，如果抛开安全设备不谈肯定就是web日志了。通常用户的请求从客户端发出经过一系列设备最终到达web应用本身，这些设备中能够留下日志的有：web服务器（如apache、nginx）和应用服务器（如jboss、tomcat、uWSGI、IIS）。少数web应用自身也会留下记录，如thinkphp的日志或其他自定义的日志功能。
下图是一个经过抽象简化后的请求路径图，其中反向代理和应用服务器不一定存在。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723019415287-260a8052-15bf-4962-9a52-be25721029fb.png)
那么按照我们上文所述，则第一目标是：确定web服务器、应用服务器和web应用是否存在及其位置，然后找到它们的日志。
2.1 确定网站使用服务器类型
---------------
最好的状况是开发坐在你对面，有什么对面会直接说。而如果没有这么便利的条件，服务器上运行了啥就得你自己来找。
### 2.1.1 访问网站
我们可以先对网站进行一个基础的浏览，以确定它使用的服务器/应用语言。比如：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723023325419-09e1aac8-89f7-44b0-b0d4-bf1eafd9e64a.png)
这个请求就能看出使用了.NET。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723023361264-38e543b7-c61a-4c92-8628-8f9a11f1ba03.png)
而这个响应说明服务器是Nginx。
### 2.1.2 查看进程
在windows中我们可以使用tasklist+findstr来查找常用服务器进程。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723023029479-39c63c73-026c-444e-861f-e90d0525f9a3.png)
在linux中我们通常使用ps -aux+grep。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723024556733-742aa3d4-7ad9-4bfa-bd78-5fd75603a625.png)
- apache
- httpd
- apache2
- nginx
- nginx
- tomcat
- java/javaw
- IIS
- inetinfo
2.2 常见日志位置
----------
以下是windows和linux中一些服务器常见路径/配置文件路径（配置文件里会有日志路径）/日志文件路径。
### 2.2.1 Linux下
- Apache
- /usr/local/apache/logs/
- /var/log/apache2/
- httpd.conf
- access.log
- error.log
- Nginx
- /etc/nginx/logs/
- /var/log/nginx/
- nginx.conf
- access.log
- error.log
- Tomcat
- $CATALINA\\_HOME
- catalina.out
- localhost.yyyy-mm-dd.log
### 2.2.2 Windows下
- IIS
- %SystemRoot%\\System32\\LogFiles\\
- Apache
- 安装路径非固定
- httpd.conf
- access.log
- error.log
- Nginx
- 安装路径非固定
- nginx.conf
- access.log
- error.log
- Tomcat
- %CATALINA\\_HOME%
- catalina.out
- localhost.yyyy-mm-dd.log
在更多情况下，我们会直接对日志文件位置进行搜索。linux使用find命令，windows可以使用everything进行搜索。
2.3 Web应用中的日志
-------------
对于web应用本身，如果其使用了框架或自带日志功能，也会有日志文件。这种日志的路径不定，需要通过搜索web所属框架来寻找，或者通过查看应用的数据库来查询。
有些框架自带log功能，如大名鼎鼎的thinkphp，大多数小CMS也会自带一个简单的日志系统，一般存放在数据库中。有些系统后台也会自带登陆审核日志审计等功能。
所以我们查找web应用日志的最好方式是：
1. 在根目录下搜索log文件
2. 登陆网站数据库，查询是否有log表
这是大米CMS的日志位置，作为基于thinkphp的CMS它也保留了日志功能：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723086977987-3dae4a8c-32bf-4734-a765-4985ddd2e2ba.png)
这是yzmCMS的日志位置，php的CMS一般都会有一张admin\\_log表。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723087080068-362af8b1-8217-4c3e-971f-6ceeaa91cfc5.png)
2.4 Docker中的日志
--------------
Docker的web日志通过登陆Docker查看。
docker ps -a 列出所有容器
![](https://cdn.nlark.com/yuque/0/2023/png/32358243/1685497939519-541b8030-0fce-4345-b139-9da67456c5b7.png)
docker exec -it &lt;id&gt; /bin/bash 为此容器起一个shell
![](https://cdn.nlark.com/yuque/0/2023/png/32358243/1685498149044-a31006b0-663e-44d5-b850-ccb02710597d.png)
docker cp &lt;id&gt;:/etc/passwd /tmp/ 拷贝容器文件到本地
![](https://cdn.nlark.com/yuque/0/2023/png/32358243/1685498601927-065b8da5-6b31-4fe7-bb3f-d483989bc1dd.png)
3 分析研判
======
先问问各位读者：在获取到足够的日志后，我们如何展开分析？日志中能获取到的信息有哪些？
在能够获取到事件发生时间（通过询问客户）时，我们可以从事件发生前后开始寻找。如果不知道具体的事件发生时间，则需要将日志导入分析工具。
3.1 常见日志格式
----------
1. 确定事件发生的时间
2. 通过工具或手动分析，找到存在异常的请求包和可能的后门
3. 结合源代码对上述异常进行分析
由于web日志的生成方式比较多样，这里主要介绍一下针对大多数服务器日志的研判方法，我们以apache日志为例。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723098928786-b70c0136-08bc-409c-8e75-957e9895b80d.png)
可以看到，这些Apache日志的格式为：
访问IP - - \[访问时间（服务器时间）\] "请求方式 请求路由 HTTP协议版本" 响应码 -
而error.log这类的报错日志格式会有些许变化，但它需要具体情况具体分析。
3.2 使用工具对日志进行分析
---------------
如果在windows下分析，那么日志分析工具最为方便：因为它能够图形化展示日志详情。
这里使用360星图对日志进行审计。
打开星图的根目录/conf/config.ini，替换其中日志文件路径为我们需要分析的路径：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723105254606-c9694e11-4ba2-45d7-987f-aae06b7c1c28.png)
启动星图，待完毕后即可从result文件夹中获取报告：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723104944687-95ef4f3a-5d91-4cde-87f0-3919e74b0cdc.png)
同时还能获取到可疑攻击的统计，如下：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723105949362-48799286-b5bf-4da0-b608-717aefa14bce.png)
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723105986278-c576f001-7dc5-44ab-a689-5325ebaddcff.png)
3.3 使用命令对日志进行简单统计
-----------------
这是linux下常用的日志统计方式。一般我们会使用wc命令以统计行数，awk、cut命令进行文本处理，sort进行排序，使用uniq、cat、tail等命令读取文件，然后将它们组合进行审计。
以下是一些常用的审计命令组合，我会依次解释它们的作用：
1. `cut -d - -f 1 [file] | sort | uniq -c | sort -rn | head 20` 统计访问次数最多的IP
cut -d - -f 1使用-分割字符串，然后选取第一个分段
uniq -c 取唯一值，然后统计这些唯一值出现的次数
sort -rn 排序，按照数值逆向排序（-r为逆向reverse -n为数字number）
head 20 取头部20个
2. `awk '{print $1}' [file] | sort | uniq | wc -l`统计访问IP数量
awk '{print $1}' 取第一个子串（IP）
sort 排序
uniq 取唯一值
wc -l 统计行数
3. `grep "/index.php" [file] | wc -l` 统计页面index.php被访问次数
4. `awk '{++S[$1]} END {for (a in S) print a,S[a]}' [file]` 对于每一个IP，打印出它们访问的页面数量
有点抽象，可以理解为先用S存储每个$1出现的次数，然后对于每一个S中的值，打印出值和出现的次数
5. `grep ^[ip] [file] | awk '{print $1,$7}'` 查找IP访问的页面
这个就简单了，查找IP出现的行数然后使用AWK过滤出IP，页面。
6. `awk '{print $4,$1}' [file] | grep [time\_11/Jun/2020:14] | awk '{print $2}' |sort |uniq |wc- l` 判断对于某时间（可精确到小时），有多少IP访问了页面
3.4 黑页与黑链的研判
------------
黑页一般指的是入侵者对网站首页的改写。研判黑页与黑链，最先要解决的问题是：确定入侵者如何改写网站首页。
而入侵者使用的手段也是五花八门：如仅改写TITLE；如判断用户UA，在PC端不改写首页；如判断用户IP，在境外则展示被改写首页；如使用js脚本定时跳转首页，如仅改写META。
还有一些黑链通过修改服务器的拦截规则进行劫持，如匹配特定url转发到黑页：
```php
location /abc/ {
proxy\_pass http://www.baidu.com:80/;
}
```
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1724656747868-b836ad76-4cf9-4950-85e1-14d5a5f2a3d0.png)
一个简单的黑页判断通常仅会通过访问网站首页并抓包完成。在完成访问首页操作并确认黑页已跳转之后返回查看过程包，特别注意访问中加载的可疑外部js和跳转顺序等。
### 3.4.1 例1 META篡改
下图中的暗链仅篡改了META数据并实体编码篡改内容，使研判者难以使用肉眼判断网站是否被篡改：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723709095988-74b0b441-81fe-402b-a5b4-b18321498e73.png)
将其解码可发现网站META数据已被篡改为黑产导航：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723709309027-7a89ca1c-2fae-4520-86e7-9c8c7133962d.png)
3.5 特殊情况
--------
### 3.5.1 反向代理
有些情况下，服务器内部会做反向代理，也就是客户的访问会经过一个或多个反向代理服务器然后被转发到真正的服务器上。此时，对于真正的服务器而言访问它的是上一个反向代理服务器，则日志中记录的IP也会是上一个反向代理服务器的IP（也就是说，都是同一个IP）。
在此情形下，如果服务器开启了combined日志，我们可以通过筛选User-Agent头来简单区分访问者的身份。User-Agent头是由浏览器生成的标识，里面包含了浏览器版本、操作系统版本等信息：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723710950319-beea2072-7be4-4e51-9c27-1a274a3d5dde.png)
4 排查修复
======
排查修复这个名词由两个短语组成，排查与修复。
排查指的自然是排查攻击者留下的后门和系统本身存在的隐患——特别是导致此次应急事件中攻击者攻击成功的隐患；而修复则是指恢复遭到破坏网站的正常服务，并修补漏洞。
4.1 排查
------
对于web应急而言排查主要针对于webshell。
### 4.1.1 如何判断后门？
我们一般从创建时间、文件内容、访问日志三个方面来判断一个文件是否是后门。通俗来说，也就是：
创建时间：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723175408045-1c2e7995-5aa0-42dd-98af-763f7518d32d.png)
linux下使用这条命令来查找带时间的文件：
```php
find / -name \*.php -newermt "2023-03-01" -printf '%T+ %p\n' | sort -r
```
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723184332343-cd508750-8eef-4179-87a5-facc13fd3205.png)
文件内容：
主要是通过D盾等工具进行查杀。
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723175427792-192d3145-7425-41ff-b3a0-94937add116f.png)
找到疑似后门，可以通过访问日志来反推攻击时间：
![](https://cdn.nlark.com/yuque/0/2024/png/32358243/1723175438963-8dd65e15-2db8-445f-8124-14e0e8940e32.png)
### 4.1.2 内存马排查
我们以php和Java为例。内存马总而言之指的是“仅存在于内存中...