---
title: Bypass WAF （小白食用）
url: https://forum.butian.net/share/3709
source: 奇安信攻防社区
date: 2024-09-12
fetch_date: 2025-10-06T18:23:29.378614
---

# Bypass WAF （小白食用）

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

### Bypass WAF （小白食用）

* [渗透测试](https://forum.butian.net/topic/47)

前言：现在绕过waf手法在网上层出不穷，但是大家好像忘记一个事情就是，思路比方法更有价值，大家对着网上一些手法直接生搬硬套，不在意是不是适合的场景，网上的文章，好像着急的把所有的绕过方法都给你罗列出来。没有传授给你相应的技巧。到最后，小白拿着一堆绕waf的方法却被waf拦在外面。

Bypass WAF （小白食用）
-----------------
\*\*前言：现在绕过waf手法在网上层出不穷，但是大家好像忘记一个事情就是，思路比方法更有价值，大家对着网上一些手法直接生搬硬套，不在意是不是适合的场景，网上的文章，好像着急的把所有的绕过方法都给你罗列出来。没有传授给你相应的技巧。到最后，小白拿着一堆绕waf的方法却被waf拦在外面。\*\*
### 什么是waf
Web应用程序防火墙（Web Application Firewall，WAF）是一种用于保护Web应用程序的安全设备。Web应用程序是指通过Web浏览器或其他Web客户端访问的应用程序。WAF的目的是保护Web应用程序免受黑客、网络攻击和数据泄漏等安全威胁的攻击。
#### 软件waf
软件waf，安装在需要防护的服务器上，实现方式通常是Waf监听端口或以Web容器扩展方式进行请求检测和阻断。
常见如：D盾
![image-20240806170759757](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4e9ee47ee739ab7c10c675d1f6ad3e0c5399aa3b.png)
#### 硬件waf
是一种基于硬件实现的Web应用防火墙（‌WAF）‌解决方案。‌它通常是在硬件服务器上定制硬件，‌然后将Linux系统和软件系统嵌入其中，‌以提供安全防护。‌这种解决方案的好处是Linux相对于Windows Server更加安全，‌因此硬件WAF能够提供较高的安全性。‌与软件WAF和云WAF相比，‌硬件WAF的部署和运行更加依赖于物理硬件，‌其安全性能和稳定性通常较高，‌适合对安全性要求极高的应用场景
\*\*缺点\*\*：成本高、配置复杂、扩展性有限
#### 系统内置waf
就是类似于过滤器，列举一个经典例子打过AWD的朋友都知道一个waf叫watchbird。
他就是系统内置的典型
![image-20240806172614739](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-1fc1e81e7e9689d90a211f3668711387c281378e.png)
![image-20240806172709918](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-4044a58d9b8b636ddb5c473e84c5c4a7b971c941.png)
这个waf，就是通过关键词防御，比如我要cat /flag。他监测到flag这个字段，就会抢险提前反弹一个假的flag。这个配置是不需要联网只需要有个PHP环境。
### 云上waf
云WAF是一种部署在云端的网络安全解决方案，能够有效地防护网站和网络应用程序免受各种网络攻击，如SQL注入、跨站脚本攻击（XSS）以及其他各种Web应用程序漏洞。通过在云端部署WAF，企业可以无需大规模投资硬件和维护，即可获得强大的网络安全保障。
![image-20240806171312113](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-646b3300001393448cf48e2a7f54ae51460b8a0c.png)
### 一些常见的负载均衡的办法
![image-20240806170149257](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-b2ce0f809f9437bc7ec78d311fdee3d104dfacc3.png)
- 轮询：依次分配
- 动态轮询：类似于加权法（根据设置的权重值，进行连接分配）
- 随机：随机分配
- \*\*加权：根据设置的权重值，进行连接分配\*\*
- 最快算法：基于响应时间去分配的
- 最少连接：连接最少的分配
- 观察法：利用最小的连接量和最少的响应打分，然后去进行分配
- 预测法：计算分数趋势，根据分数去分配
### \*\*那为什么我们要去了解负载均衡呢\*\*
我来模拟一个例子，咱们一个正常时候请求访问时这样的
![image-20240806171706524](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-065aa79a640433122babc2e8488202229bdda2ff.png)
但是如果，我突然发送多条请求，超过了waf的负载，那难道业务就不能进行正常访问了吗？
不是这样的，如果我们超过了waf的负载，我们会走下面这个通道访问服务器。
![image-20240806171922822](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0173e9de9d93afc5e9c856125b1040ee9cc65b75.png)
这里面我假设waf的权重是98，另一个是2。大家应该就懂为什么，我们讲负载均衡了。
如果说出现这种情况，那我们直接一个并发打过去，连绕过都不需要。
WAF工作原理
-------
WAF可以通过对Web应用程序的流量进行过滤和监控，识别并阻止潜在的安全威胁。WAF可以检测Web应用程序中的各种攻击，例如SQL注入、跨站点脚本攻击（XSS）、跨站请求伪造（CSRF）等，并采取相应的措施，例如拦截请求、阻止访问、记录事件等。
WAF的工作原理通常包括以下几个步骤：
流量识别：WAF识别来自客户端的请求，并对请求进行分析。WAF可以检查请求头、请求体、Cookie、URL参数等信息，并识别其中的攻击。
​
攻击检测：WAF对识别的请求进行攻击检测。WAF可以使用多种技术来检测攻击，例如正则表达式、特征匹配、行为分析等。WAF可以检测多种攻击，包括SQL注入、XSS、CSRF、命令注入等。
​
攻击响应：WAF根据检测结果采取相应的措施，例如拦截请求、阻止访问、记录事件等。WAF可以使用多种技术来响应攻击，例如重定向、报错、拦截等。
​
日志记录：WAF记录所有请求和响应的详细信息，包括请求头、请求体、响应头、响应体等。WAF可以将日志发送给中央日志管理系统，以便进行分析和审计。
### 常见的WAF厂商
- 国内:宝塔、安恒,绿盟,启明星辰,360磐云、长亭、安全狗、阿里云、腾讯云、华为云、百度云
- 国外:飞塔,梭子鱼,Imperva
如何探测WAF
-------
#### WAFw00f
介绍：WAFw00f是一个用于探测网站是否存在Web应用程序防火墙的工具，它通过发送正常和异常的HTTP请求，结合特征分析和算法推理，来识别不同类型的WAF
​
用法：wafw00f <https://www.xxxx.com>
#### namp
介绍:网络扫描工具，它包含了一些WAF指纹识别的脚本，可以用来探测WAF的存在
​
用法：nmap www.xxx.com --script=http-waf-detect.nse
#### SQLMap
介绍：主要用于检测和利用SQL注入漏洞，但它也包含了一些WAF指纹识别的功能。
​
用法：sqlmap -u "xxx.com?id=1" --identify-waf
#### go-test-waf
这是一个使用Go语言编写的WAF测试工具，可以自动测试WAF的拦截能力和规则配置。
​
用法：通过DockerHub库直接获取，拉取项目库docker pull wallarm/gotestwaf
### 针对CDN类型的WAF绕过思路
#### 1.通过子域名查找
很多时候，一些重要的站点会做CDN，而一些子域名站点并没有加入CDN，而且跟主站在同一个C段内，这时候，就可以通过查找子域名来查找网站的真实IP。
\*\*用空间测绘去查询（FOFA、Hunter、360Quake、Shodan、Zoomeye或者谷歌等搜索引擎）\*\*
\*\*一些在线查询工具\*\*，如：
<http://tool.chinaz.com/subdomain/>
<http://i.links.cn/subdomain/>
<http://subdomain.chaxun.la/>
<http://searchdns.netcraft.com/>
<https://www.virustotal.com/>
#### \*\*Layer子域名挖掘机\*\*
wydomain：<https://github.com/ring04h/wydomain>
subDomainsBrute:<https://github.com/lijiejie/>
Sublist3r:<https://github.com/aboul3la/Sublist3r>
#### 2.在线ping工具
- ping.chinaz.com
- 17ce.com
- tools.ipip.net/newping.php
#### 3.DNS历史解析记录
查询域名的历史解析记录，可能会找到网站使用CDN前的解析记录，从而获取真实ip，相关查询的网站有：
iphistory：<https://viewdns.info/iphistory/>
DNS查询：<https://dnsdb.io/zh-cn/>
微步在线：<https://x.threatbook.cn/>
域名查询：<https://site.ip138.com/>
DNS历史查询：<https://securitytrails.com/>
Netcraft：<https://sitereport.netcraft.com/?url=github.com>
#### 4.\*\*SSL证书寻找真实IP\*\*
通过浏览器查看网站的SSL/TLS证书信息，有些CDN提供商会在证书中标明自己的信息。
可以通过浏览器或命令行工具获取SSL证书的详细信息。
\*\*使用浏览器\*\*打开目标网站（例如，<https://example.com>）。
点击地址栏中的锁图标。
查看证书详细信息，记下证书中的“颁发给（Issued To）”和“颁发者（Issuer）”信息。
\*\*使用命令行工具（openssl）\*\*
你可以使用openssl命令行工具来获取证书信息。以下是获取证书详细信息的命令：
openssl s\\_client -connect example.com:443 -showcerts
#### 5.国外ping
为什么我单独把他拉出来呢？\*\*大部分 CDN 厂商因为各种原因只做了国内的线路\*\*，而针对国外的线路可能几乎没有，此时我们使用国外的DNS查询，通过一些冷门地区进行ping，很可能获取到真实IP。
国外多PING测试工具：
[https://asm.ca.com/zh\\\\_cn/ping.php](https://asm.ca.com/zh%5C\_cn/ping.php)
<http://host-tracker.com/>
<http://www.webpagetest.org/>
<https://dnscheck.pingdom.com/>
#### \*\*6.扫描全网\*\*
通过Zmap、masscan等工具对整个互联网发起扫描，针对扫描结果进行关键字查找，获取网站真实IP。
1、ZMap号称是最快的互联网扫描工具，能够在45分钟扫遍全网。
<https://github.com/zmap/zmap>
2、Masscan号称是最快的互联网端口扫描器，最快可以在六分钟内扫遍互联网。
<https://github.com/robertdavidgraham/masscan>
#### \*\*7.通过域名备案信息广域探测\*\*
网站需要服务器，但是再有钱的公司，也不可能一个域名一台服务器，大多数情况下，都是多个域名业务，共享一台服务器。那么如果目标网站存在备案，可以查询其备案信息，收集该单位或者个人备案的其他网站域名以及其他子域，然后再进行一轮广域的探测，很有可能其中的某个边缘子域，没有做 CDN，就直接暴露了真实服务器的 IP 地址，然后再进一步验证该 IP 是否也是目标网站的真实 IP 。
### 实战：快速定位精准真实IP
我们很多时候做渗透的时候,总会遇到CDN,这样
这里我们借助fofa
思路如下
我们想确定一个网站的真实IP地址，通常现在网站都会使用https协议，用到SSL证书是必不可少的，绝大多数企业证书都是通配符证书，因此我们可以把证书的序列号拿下来然后搜索这个证书用在了哪些业务里，然后如果部分业务中没有使用CDN或者没有覆盖到CDN,真实ip就出现了
这里我用的是火狐浏览器
首先查看证书
![image-20240424144902142](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-0b79f48795ba1e300173c40eb69a73f76c5e3950.png)
找到序列号
![image-20240424145015457](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-e0fa0ea443c542480f086a25c4307cd0a4c75307.png)
55:E6:AC:AE:D1:F8:A4:30:F9:A9:38:C5
55E6ACAED1F8A430F9A938C5
将其转成10进制
![image-20240424145225637](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-33549a18bde4ead1e0f06a83e35d381cf1f8bd70.png)
26585094245224241434632730821
我们可以通过下面的语句来进行调查
cert="26585094245224241434632730821"
![image-20240424145410182](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-10f7e9e122975ff373484bb40bc7438ce99dd80b.png)
绕过waf的思路
--------
### 1、基于HTTP协议绕过思路
#### 1.1协议未覆盖
POST请求常用有4种参数提交方式：
- Content-Type:application/x-www-form-urlencoded;
- Content-Type:multipart/form-data;
- Content-Type:application/json;
- Content-Type:application/xml;
Waf未能覆盖Content-Type:multipart/form-data从而导致被绕过。
或者waf会认为他是文件上传请求，从而只检测文件上传，导致被绕过，就是\*\*前后解析不一致\*\*。
举一个例子
假设你渗透一个网站，然后你输入payload在后面，然后被waf拦截了，你无法正常上传
![image-20240809140841067](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-02b81b9c016d8943aa173e40684d97882b9f09e8.png)
这个时候你可以将包该为上传类型，用bp自带的
![image-20240809141012978](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-70e35f68bcfb12f338a101134cdd3ee6950aa792.png)
![image-20240809141242087](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/08/attach-ffead11b8f152ebc3c2ec187eb2878639af7d5b1.png)
你会发现是能够被解析的。但是waf会和后端解析不一致，\*\*waf认为是上传，后端却认为是查询\*\*，所以绕过。
### 2.1HTTP/1.x和HTTP/2差异绕过WAF：
HTTP/2是HTTP协议的下一个代版本，相比于之前2提供了更...