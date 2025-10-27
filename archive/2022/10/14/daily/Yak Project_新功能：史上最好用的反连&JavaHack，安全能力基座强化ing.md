---
title: 新功能：史上最好用的反连&JavaHack，安全能力基座强化ing
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247491180&idx=1&sn=5884aac8716de361a383c6e884bdca39&chksm=c2d262c8f5a5ebdecea937ebc8be5c322c21a1ffcda9b81d66e65d64dc84b64180ec937f122b&scene=58&subscene=0#rd
source: Yak Project
date: 2022-10-14
fetch_date: 2025-10-03T19:52:32.354263
---

# 新功能：史上最好用的反连&JavaHack，安全能力基座强化ing

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2XmtgR7yuBb6v5Bq7t03XRkcEC8nY1c2b1YJLFcYbAwUJDsNlydicrQw/0?wx_fmt=jpeg)

# 新功能：史上最好用的反连&JavaHack，安全能力基座强化ing

z3

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfSpFpvkIFZmQIErFibib1uiaOsLXZKbkicRsicXVN3QYGac0xrqKu7Pxo1UO0YLMiboTs0WCcBUO3qOhhw/640?wx_fmt=gif)

**反序列化**、**类加载**、**JNDI漏洞利用**是Java漏洞中特别常见的几种类型，但相对来说利用过程又是较为复杂的。**所以Yakit提供了两个特别好用的功能，无需Java环境，仅需一个Yakit。**

下面先介绍下使用方法再演示下实战利用。

![](https://mmbiz.qpic.cn/mmbiz_png/eSeibm514shJauEljFf7yUpymajaeXESLoqbrKateozk51DQssSmPS7zOIPPBSjBQZMpGusRK3qQC6712fLibUZg/640?&wx_fmt=png)

反连服务器

![](https://mmbiz.qpic.cn/mmbiz_png/aU7yG8jibIeqADHk9RNpPjf4cIdO08KhSCcUQRA04fq16196c6Nvic8k3CYoMfxZodiblF4IDAQB5FdicOdy5vaovg/640?&wx_fmt=png)

返连服务可用于手工渗透测试，既可用于漏洞检测，也可用于漏洞利用。

01

本地启动

初始页面如图(如果有配置公网反连，则会自动启用公网穿透，并自动填写Bridge信息)，反连地址默认是获取本机的第一块网卡IP。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2MxHoYBVBicOicvfiadd7vlN4KCE5EjaYDT6BA9DbYmoZWL6pQBIES7Dyw/640?wx_fmt=png)

启动成功后如图，根据需求填写蓝色提示框内的地址.

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2QswTKL2KHYCAYEq4T0UpGFSNEWKRc1MlxarNr80KcIicyGzZXJNSXcg/640?wx_fmt=png)

02

漏洞检测

写一段java代码测试下连接

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2LickfuSwoibDz1swX5liaR6iaEOjFPctNRanK1lYaUbaRxbrTtKdvEKExA/640?wx_fmt=png)

在Yakit上可以看见收到请求，token为aaa，返回内容为<empty>（代表响应内容为空）

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp22Bibia6wRibA5qQRLzMbGvMcUV2MteWCqYOibxicZypKETMyukKUNMkbdpw/640?wx_fmt=png)

03

漏洞利用

在返连页面右上角有个Payload配置，开启后可以看见左面出现类似 Yso-Java Hack 的页面，在这里可以配置payload。

命令填写

`open /System/Applications/Calculator.app`

然后点生成。可以看见返连地址自动添加了token。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2bOJshbicafDPj7SRAkWrrQe57I7XVjeKNPFSNDhIwKS1W6XwHACPgmA/640?wx_fmt=png)

复制新地址，再试一下连接ldap，发现弹出计算器。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2u8wu5wHy1VibspdyGGGQAbS8NzmIPQkJQp7gxzchZbQU22RK3S2UYeQ/640?wx_fmt=png)

在 Yakit 上可以看见利用流程: 受害端发出 ldap 请求，Yakit 返回一个 reference 类，指向一个 web 地址 -> 受害端访问 web 地址，Yakit 返回一个恶意类 -> 受害端加载恶意类导致命令执行。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2GwsZlAkzESbYtjwm19o6I3BibtwDiasTB1bObhh8xmWPJQvFfiaO9EAkQ/640?wx_fmt=png)

04

公网穿透

对于公网的目标，反连服务就需要在公网监听了，一是可以将Yak引擎公网部署，二是可以在公网搭建Bridge，这里主要讲下第二种方法。

首先需要在 VPS 上安装 Yak 引擎。

（执行`bash <(curl -sS -L` `http://oss.yaklang.io/install-latest-yak.sh``)`进行安装），执行`yak grpc --secret yourpassword`启动Bridge。

更多介绍可以看这篇文章[《想拥有自己的 Yak Bridge？DNSLog、ICMPLog、TCPLog 全部免费》。](http://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247488877&idx=1&sn=901321bb720ca8ba2024f702ccfffd47&chksm=c2d269c9f5a5e0df5605995845dafc2278bd90ded27f15e4c9e45b37ac15d62a2d3350519f75&scene=21#wechat_redirect)

如图输入 Bridge 地址和密码，启动（如果报错 connection refused 则表示连接 Bridge 失败，检查下密码是否正确、端口是否成功开启、vps 上是否有防火墙限制、云服务控制台上是否设置了安全策略）

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2mPmFY2ibic5ZRTMbStvwoSJelBicubUBQ2bICiax0FooYuwtK20hjk7I1Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2w3icP9ZgibfxnmQ5O91TGicrvqcXS4seC7JPXwxOwuRIKJvj7uPFMZFsA/640?wx_fmt=png)

连接成功后可以看到反连地址的 IP 已经变为 Bridge 服务器的 IP 了，接下来的操作和本地启动相同。

![](https://mmbiz.qpic.cn/mmbiz_png/eSeibm514shJauEljFf7yUpymajaeXESLoqbrKateozk51DQssSmPS7zOIPPBSjBQZMpGusRK3qQC6712fLibUZg/640?&wx_fmt=png)

Yso-Java Hack

![](https://mmbiz.qpic.cn/mmbiz_png/aU7yG8jibIeqADHk9RNpPjf4cIdO08KhSCcUQRA04fq16196c6Nvic8k3CYoMfxZodiblF4IDAQB5FdicOdy5vaovg/640?&wx_fmt=png)

页面初始状态如图，左侧配置 payload 参数，右侧用来展示生成的 payload。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp27C72oTicicSWwLvfm6mic5hdg94G7bXpZkQWTEib27dxCnnac7phrfYEQw/640?wx_fmt=png)

01

生成序列号payload

默认开启 “使用利用链”，即生成序列化 payload ，一级选项是利用链，二级选项是恶意类。鼠标放到小问号上可以看到介绍。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp25vTibwlZSxKZMo1sJ4fZM9DRFKrZfaRSlMD93041c245t83JWOERoDQ/640?wx_fmt=png)

选择利用链和恶意类后，会出现配置表单，类名默认是随机生成的，填写所有表单信息，点击生成，就可以在右侧看到生成的 payload ，点击上方可以切换展示方式。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2diaXdOUPWygemoHMWU6VKn8qM6JW69gz9CR9hTebryVBPmVIZpQ6u2w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2p39Unl6xslKfYnF0sJwS6KicLiapQOWKzL3niatwUaIWnhnKQYHyjN30Q/640?wx_fmt=png)

还可以展示生成payload的代码，还可以将代码发送到Yak Runner，师傅们写插件时如果懒得写，就可以直接在这里直接生成代码。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2FHV5FIcSxicCWejn2adsMm9f3yddUBSLoTd79vypzqPCjgLKuXYAlww/640?wx_fmt=png)

最新版本 payload 展示类型增加了一个 DUMP ，可以看到 payload 的数据结构，像下面这样。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2e4eqGcQMU2e9bnOpWZlYrjJicNwiaLgh0QdehjyR4O32DGdPZc4jribzg/640?wx_fmt=png)

02

生成恶意类

如图，关闭 “使用利用链” 就可以生成恶意类，具体操作和生成利用链类似

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2iasRjricRayfjoicouJlmtCiaG6vNoSbkrhZ6MDbZSlnx9YJe90nYV8mmQ/640?wx_fmt=png)

可以看见关闭 “使用利用链” 时多了一个启动反连服务按钮，下面再看一下反连服务。

0303

配合反连使用

在配置好恶意类后，点击启动反连，就可以使用当前恶意类直接启动反连了（如果配置了公网反连则使用此配置启动，否则使用本地启动，如果启动失败，请自行在高级配置里配置反连地址），如图

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp25PT1X7ictfSw02qr4GPDThOLcaMFmWNtK1ibryKyePHsdwVqcVt7Iq6g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/eSeibm514shJauEljFf7yUpymajaeXESLoqbrKateozk51DQssSmPS7zOIPPBSjBQZMpGusRK3qQC6712fLibUZg/640?&wx_fmt=png)

实战测试

![](https://mmbiz.qpic.cn/mmbiz_png/aU7yG8jibIeqADHk9RNpPjf4cIdO08KhSCcUQRA04fq16196c6Nvic8k3CYoMfxZodiblF4IDAQB5FdicOdy5vaovg/640?&wx_fmt=png)

新功能介绍完了，下面看下实战场景吧，以 Fastjson 和 shiro 利用为例。

01

Fastjson测试

这里使用 vulfocus 启动一个 CNVD-2017-02833 实例，攻击流程如下

1. 在 vps 启动一个 yak 引擎`yak grpc --host 0.0.0.0`，Yakit 端输入服务器地址和端口（默认8087），连接
2. 打开Yakit的端口监听器，监听一个端口，以 8086 为例

   ![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2Unib0wiaW3yA50mzJNLIpkkhtIXB357UPs4X2Z5GC1bibIyyCpphaYlHQ/640?wx_fmt=png)
3. 启动反连服务器并配置恶意类为 TCPReverseShell ，主机填 vps 的 ip ，端口填上面监听的 8086 ，点击应用

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2fLBgQlgyadJHO9oJPcVRlc5vbteQqloXuWgopY3ic3Ss52CbHoDRS8A/640?wx_fmt=png)

4. 打开 webfuzzer，发送 Payload

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2AHN0qKVMq7lpwuuYt3JHXnnxHsib3TyrG7iaYgF1ZvF0xiaeicee0DsONQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp27udJRkx01cesXfGjUu0F2Nnmp1rmicdTUAfzvv9Hq0EFDsNQVSGyXEw/640?wx_fmt=png)

如图，反连列表中可以看见成功收到 LDAP 和 HTTP 请求，说明目标成功加载了恶意类（如果只收到 LDAP 请求，没有 HTTP 请求，可能是目标未开启

com.sun.jndi.ldap.object.trustURLCodebase ）

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2WhQJOd8rmZBmD1jgj1MBDF1ibuPnMtjUdcmfOvl2MYCDLhcaIVE6E3Q/640?wx_fmt=png)

端口监听器收到了目标机器的连接

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp24fF3uODAQRdCrv1uAqRauMQiac77YVtp3gUgHqAHEW8LTYQkOmSQoeg/640?wx_fmt=png)

02

Shiro测试

使用vulfocus/shiro-CVE-2016-4437镜像搭建环境，启动Yakit

打开Yso-Java Hack

利用链选择CommonsBeanutils1

恶意类选择RuntimeExec，填写命令，生成Yak代码

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2t2WoSoGI5Dda0xZ4rMWtsUNrYvBZ3qGIXuorsH1Qxx3FUP7I6C9NeA/640?wx_fmt=png)

编写Yak脚本

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZfEAI2RNg9aJeKCtbLvrMp2oUpRaLicr65hiajEu62PSP2ARBGX6nAnkIugoImDRFnnXs29ZDWqaLyw/640?wx_fmt=png)

执行后进入容器看见/tmp目录下多了111文件，利用成功

![](https://mmbiz.qpic.cn/mmbiz_png/eSeibm514shJauEljFf7yUpymajaeXESLoqbrKateozk51DQssSmPS7zOIPPBSjBQZMpGusRK3qQC6712fLibUZg/640?&wx_fmt=png)

总结

![](https://mmbiz.qpic.cn/mmbiz_png/aU7yG8jibIeqADHk9RNpPjf4cIdO08KhSCcUQRA04fq16196c6Nvic8k3CYoMfxZodiblF4IDAQB5FdicOdy5vaovg/640?&wx_fmt=png)

有些Java漏洞的利用太繁琐了，需要java环境、多种工具配合使用、还要在 VPS 上看回显、记各种命令…

**对比之下 Yakit 真的太好用了！**本次更新的两个功能基本上可以解决大部分Java漏洞利用的场景，希望师傅们多多使用，欢迎提出意见。

![](https://mmbiz.qpic.cn/mmbiz_png/eSeibm514shJauEljFf7yUpymajaeXESLoqbrKateozk51DQssSmPS7zOIPPBSjBQZMpGusRK3qQC6712fLibUZg/640?&wx_fmt=png)

插件新功能速递

![](https://mmbiz.qpic.cn/mmbiz_png/aU7yG8jibIeqADHk9RNpPjf4cIdO08KhSCcUQRA04fq16196c6Nvic8k3CYoMfxZodiblF4IDAQB5FdicOdy5vaovg/640?&wx_fmt=png)

插件可以申请修改他人的插件啦！作者同意修改...