---
title: 通过Nginx对API进行限速
url: https://www.anquanke.com/post/id/289933
source: 安全客-有思想的安全新媒体
date: 2023-07-28
fetch_date: 2025-10-04T11:52:47.870644
---

# 通过Nginx对API进行限速

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 通过Nginx对API进行限速

阅读量**307254**

发布时间 : 2023-07-27 16:11:31

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

**概述**

API 限速的主要目的是控制对 API 的访问频率和数据使用量，以保护 API 和后端服务的稳定性和可靠性。当接收到大量请求时，可能导致服务器过载或响应时间变慢，限制 API 的访问速率可以避免这种情况的发生。此外，API 限速还可以保护 API 免受恶意攻击，如 DDoS 攻击和暴力攻击。另一个原因是，API 提供者可能想要限制 API 的数据使用量，以确保他们的 API 不被滥用或过度使用。可以通过限制每个用户可以请求的数据量，达到该目的，以便 API 提供者可以控制服务的成本和资源使用率。综上所述，API 限速是一种有效的措施，可以确保 API 的稳定性和可靠性，防止 API 被恶意攻击和滥用。Nginx 是当前非常受欢迎的 Web 服务器和反向代理服务器。在高并发、高负载的 Web 场景中，Nginx 的高性能、稳定性和可扩展性优势得到了广泛认可，因此 Nginx 在这些场景下往往是最佳选择。Nginx 也支持 HTTP、HTTPS、SMTP、POP3 等多种协议，以及负载均衡、缓存、反向代理、安全控制等多种功能，使得它可以适用于各种不同的 Web 代理场景。

下文讲述如何通过 Nginx 实现 API 限速。

## ngx\_http\_map\_module 模块

ngx\_http\_map\_module 模块创建值依赖其它变量的值的变量。

### **示例配置**

map $http\_host $name {

hostnames;

default 0;

example.com 1;

\*.example.com 1;

example.org 2;

\*.example.org 2;

.example.net 3;

wap.\* 4;

}

map $http\_user\_agent $mobile {

default 0;

“~Opera Mini” 1;

}

### **指令**

### **map**

创建新变量，其值依赖在第一个参数中指定的一个或多个源变量的值。map 块内部的参数指定源值和结果值之间的映射。源值被指定为字符串或正则表达式。正则表达式应该以 “~” 符号（用于大小写敏感的匹配）或 “~\*” 符号（用于大小写不敏感的匹配）开头。正则表达式可以包含命名或位置捕获，可以在其它指令以及结果变量中使用。如果源值匹配下面描述的特殊参数的名称之一，那么它应该以 “\” 符号开头。结果值可以包含文本、变量，及其组合。也支持下面的特殊参数：

1. default <value>如果源值与指定的变种都不匹配，那么设置结果值。如果未指定 default，那么默认的结果值将为空字符串。
2. hostnames表示源值可以是带前缀或后缀掩码的主机名：

\*.example.com 1;

example.\* 1;

下面两条记录：

example.com 1;

\*.example.com 1;

可以合并为：

.example.com 1;

应该在值列表的前面指定该参数。

1. include <file>包含包含值的文件，可以有多个包含。
2. volatile表示该变量不可缓存。

如果源值与指定的多个变种匹配，比如与掩码和正则表达式都匹配，那么将按照如下优先级顺序，选择第一个匹配的变种：

1. 不带掩码的字符串值
2. 带前缀掩码的最长字符串值，比如 “\*.example.com”
3. 带后缀掩码的最长字符串值，比如 “mail.\*”
4. 第一个匹配的正则表达式（按照在配置文件中出现的顺序）
5. 默认值

## ngx\_http\_geo\_module 模块

ngx\_http\_geo\_module 模块创建值依赖客户端 IP 地址的变量。

### **示例配置**

geo $geo {

default 0;

127.0.0.1 2;

192.168.1.0/24 1;

10.1.0.0/16 1;

::1 2;

2001:0db8::/32 1;

}

### **指令**

### **geo**

描述指定变量的值与客户端 IP 地址的依赖关系。默认情况下，从 $remote\_addr 变量获取地址，但是也可以从其它变量获取，比如：

geo $arg\_remote\_addr $geo {

…;

}

如果变量的值不表示有效的 IP 地址，那么使用地址 “255.255.255.255”。可以使用 CIDR 表示法中的前缀（包括单独的地址）或范围来指定地址。也支持以下特殊参数：

1. delete

删除指定网络。

1. default

如果客户端地址不匹配任何指定的地址，那么给变量设置该值。当以 CIDR 表示法指定地址时，可以使用 “0.0.0.0/0” 和 “::/0” 代替 default。当未指定 default 时，默认值将为空字符串。

1. include

包含包含地址和值的文件。可以有多个包含。

1. proxy

定义受信任的地址。当请求来自受信任地址时，将使用 “X-Forwarded-For” 请求头字段中的地址。与常规地址不同，受信任地址是顺序检查的。

1. proxy\_recursive

启用递归地址搜索。如果禁用递归搜索，那么将使用 “X-Forwarded-For” 中发送的最后一个地址，代替匹配受信任地址的原始客户端地址。如果启用递归搜索，那么将使用 “X-Forwarded-For” 中发送的最后一个非受信任地址，代替匹配受信任地址的原始客户端地址。

1. ranges

表示地址被指定为范围。该参数应该是第一个。为加速基于 geo 的加载，地址应按升序排列。比如：

geo $country {

default ZZ;

include conf/geo.conf;

delete 127.0.0.0/16;

proxy 192.168.100.0/24;

proxy 2001:0db8::/32;

127.0.0.0/24 US;

127.0.0.1/32 RU;

10.1.0.0/16 RU;

192.168.1.0/24 UK;

}

conf/geo.conf 文件可能包含如下行：

10.2.0.0/16 RU;

192.168.2.0/24 RU;

最具体匹配的值被使用。比如，对于地址 127.0.0.1，将选择值 “RU”，而非 “US”。带范围的示例：

geo $country {

ranges;

default ZZ;

127.0.0.0-127.0.0.0 US;

127.0.0.1-127.0.0.1 RU;

127.0.0.1-127.0.0.255 US;

10.1.0.0-10.1.255.255 RU;

192.168.1.0-192.168.1.255 UK;

}

## ngx\_http\_limit\_conn\_module 模块

ngx\_http\_limit\_conn\_module 模块用于按照定义的键，限制连接数量，特别是来自单个 IP 地址的连接数量。

并非所有连接都被计数。只有拥有正在被服务端处理的请求，并且全部请求头已被读取的连接才被计数。

### **示例配置**

http {

limit\_conn\_zone $binary\_remote\_addr zone=addr:10m;

…

server {

…

location /download/ {

limit\_conn addr 1;

}

### **指令**

### **limit\_conn <zone> <number>**

设置共享内存区域，以及对于给定的键值，允许的最大连接数量。当超过该限制时，服务端回复请求时，将返回错误。比如，指令：

limit\_conn\_zone $binary\_remote\_addr zone=addr:10m;

server {

location /download/ {

limit\_conn addr 1;

}

每个 IP 地址同一时间仅允许一个连接。可以有多个 limit\_conn 指令。比如，以下配置将限制每个客户端 IP 到服务端的连接数，同时限制到虚拟主机的总连接数：

limit\_conn\_zone $binary\_remote\_addr zone=perip:10m;

limit\_conn\_zone $server\_name zone=perserver:10m;

server {

…

limit\_conn perip 10;

limit\_conn perserver 100;

}

当且仅当当前层级未定义 limit\_conn 指令时，从前面的配置层级继承这些指令。

### **limit\_conn\_zone <key> zone=<name>:<size>**

设置共享内存区域的参数，它将为多个键保存状态。特别是包含当前连接数的状态。key 可以包含文本、变量，及其组合。不计算具有空键值的请求。使用示例：

limit\_conn\_zone $binary\_remote\_addr zone=addr:10m;

在这里，客户端 IP 地址用作键。注意，这里使用 $binary\_remote\_addr 变量代替 $remote\_addr。$remote\_addr 变量的大小可以从 7 到 15 个字节不等。存储的状态在 32 位平台上，占用 32 或 64 字节的内存，在 64 位平台上，始终占用 64 字节的内存。$binary\_remote\_addr 变量的大小对于 IPv4 地址始终是 4 字节，对于 IPv6 地址始终是 16 字节。存储的状态在 32 位平台上，使用占用 32 或 64 字节，在 64 位平台上，占用 64 字节。1M 区域可以保存大约 3.2 万 32 字节状态，或大约 1.6 万 64 字节状态。如果区域存储被耗尽，那么服务端将对后续所有请求返回错误。

### **内嵌变量**

$limit\_conn\_status

保存限制连接数的结果：PASSED、REJECTED 或 REJECTED\_DRY\_RUN。

**ngx\_http\_limit\_req\_module 模块**

ngx\_http\_limit\_req\_module 模块用于按照定义的键，限制请求处理速率，特别是来自单个 IP 地址的请求处理速率。该模块使用“漏桶”方法进行限制。

### **配置示例**

http {

limit\_req\_zone $binary\_remote\_addr zone=one:10m rate=1r/s;

…

server {

…

location /search/ {

limit\_req zone=one burst=5;

}

### **指令**

### **limit\_req zone=<name> [burst=<number>] [nodelay | delay=<number>]**

设置共享内存区域，以及请求的最大突发大小。如果请求速率超过为区域配置的速率，那么延迟处理它们，以便以定义的速率处理请求。过多的请求将被延迟，直到它们的数量超过最大突发大小，此时将以错误终止请求。默认情况下，最大突发大小等于零。比如，指令：

limit\_req\_zone $binary\_remote\_addr zone=one:10m rate=1r/s;

server {

location /search/ {

limit\_req zone=one burst=5;

}

平均情况下每秒钟最多允许 1 个请求，突发请求不超过 5 个。

当请求正被限制时，如果不希望延迟处理，那么应该使用参数 nodelay：

limit\_req zone=one burst=5 nodelay;

delay 参数指定超过限制的请求被延迟的阈值。默认是 0，即所有超限请求都被延迟。

可以有多个 limit\_req 指令。比如，以下配置将限制来自于单个 IP 地址的请求处理速率，同时按虚拟主机限制请求处理速率：

limit\_req\_zone $binary\_remote\_addr zone=perip:10m rate=1r/s;

limit\_req\_zone $server\_name zone=perserver:10m rate=10r/s;

server {

…

limit\_req zone=perip burst=5 nodelay;

limit\_req zone=perserver burst=10;

}

当且仅当当前层级中未定义 limit\_req 指令时，从前面的配置层级继承这些指令。

### **limit\_req\_zone <key> zone=<name>:<size> rate=<rate> [sync]**

为共享内存区域设置参数，它将为多个键保存状态。特别是存储超限请求的当前数量的状态。key 可以包含文本、变量，及其组合。不计算具有空键值的请求。使用示例：

limit\_req\_zone $binary\_remote\_addr zone=one:10m rate=1r/s;

在这里，状态被保存在 10M 的区域 “one” 中，该区域的平均请求处理速率不能超过每秒 1 个请求。

客户端 IP 地址用作键。注意，这里使用 $binary\_remote\_addr 代替 $remote\_addr。$binary\_remote\_addr 变量的大小对于 IPv4 地址始终是 4 字节，对于 IPv6 地址是 16 字节。存储的状态在 32 位平台上始终占用 64 字节，在 64 位平台上占用 128 字节。1M 的区域可以存储大约 1.6 万 64 字节状态，或大约 8 千 128 字节状态。

如果区域存储被耗尽，那么将删除最近最少使用的状态。在无法创建新状态后，将以错误终止请求。

用每秒请求数（r/s）指定速率。如果希望使用每秒少于 1 个请求的速率，那么用每分钟请求数（r/m）指定速率。比如，每秒半个请求上 30r/m。

### **内嵌变量**

$limit\_req\_status

保存限制请求处理速率的结果：PASSED、DELAYED、REJECTED、DELAYED\_DRY\_RUN 或 REJECTED\_DRY\_RUN。

**ngx\_http\_core\_module 模块**

### **指令**

### **limit\_rate <rate>**

限制向客户端传输响应的速率。用每秒字节数指定 rate。0 值禁用速率限制。针对每个请求设置该限制，因此如果客户端并发地打开两个连接，那么总速率将为指定的限制的两倍。参数值可以包含变量。在根据特定条件限制速率的场景下，这可能很有用：

map $slow $rate {

1 4k;

2 8k;

}

limit\_rate $rate;

也可以在 $limit\_rate 变量中设置速率限制。但不建议使用该方法：

server {

if ($slow) {

set $limit\_rate 4k;

}

…

}

也可以在代理服务响应的 “X-Accel-Limit-Rate” 头字段中设置速率限制。可以使用 proxy\_ignore\_headers、fastcgi\_ignore\_headers、uwsgi\_ignore\_headers 和 scgi\_ignore\_headers 指令禁用该功能。

### **limit\_rate\_after <size>**

设置初始数量，之后向客户端继续传输响应将被限速速率。参数值可以包含变量。

示例：

location /flv/ {

flv;

limit\_rate\_after 500k;

limit\_rate 50k;

}

## 示例

**目标：**如果客户端 IP 不地址在白名单中，那么按照客户端 IP 所在的网段限制连接数，以及每个连接的请求速率。**示例配置：**

geo $limit\_key {

default “limit\_group\_default”;

# 白名单

127.0.0.0/24 “”;

# 限制组 limit\_group\_a

10.0.2.0/24 “limit\_group\_a”;

10.0.3.0/24 “limit\_group\_a”;

}

limit\_conn\_zone $limit\_key zone=conn\_limit\_zone:10m;

limit\_conn conn\_limit\_zone 1;

limit\_req\_zone $limit\_key zone=req\_limit\_zone:10m rate=1r/s;

limit\_req zone=req\_limit\_zone burst=5;

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**星阑科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/289933](/post/id/289933)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.s...