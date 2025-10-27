---
title: FortiGate防火墙利用
url: https://buaq.net/go-143990.html
source: unSafe.sh - 不安全
date: 2023-01-04
fetch_date: 2025-10-04T02:58:42.167191
---

# FortiGate防火墙利用

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/6f688f05364b5adf9a4a75c09f9fe309.jpg)

FortiGate防火墙利用

FortiGate（飞塔）是为企业级用户提供的网络安全服务的设备。其具备即时监测病毒与蠕虫、过滤网络数据包内容的能力，并提供高效能的防火墙、VPN、和流量监控漏洞扫描等功能。我们最近在一次授权的渗透测
*2023-1-3 20:35:16
Author: [mp.weixin.qq.com(查看原文)](/jump-143990.htm)
阅读量:164
收藏*

---

FortiGate（飞塔）是为企业级用户提供的网络安全服务的设备。其具备即时监测病毒与蠕虫、过滤网络数据包内容的能力，并提供高效能的防火墙、VPN、和流量监控漏洞扫描等功能。

我们最近在一次授权的渗透测试任务中，遇到了飞塔防火墙设备。我们对该设备利用进行了研究。在本文中我们回顾了飞塔历史中较严重的两个漏洞。并且结合实际经验，分享一个利用的技巧。

CVE-2018-13379是SSLVPN中的一个目录遍历漏洞，该漏洞源于网络系统或产品未能正确地过滤资源或文件路径中的特殊元素，导致攻击者可利用该漏洞访问受限目录之外的文件，从而获取敏感信息，我们可以读SSLVPN的session文件来获取账号密码。

POC:

```
https://xxx.xxx.xxx.xxx:443/remote/fgt_lang?lang=/../../../..//////////dev/cmdb/sslvpn_websession
```

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCoeB7Go8Psufsdol4ZYgs7KA8px5JUzPNn2b8icyXucwI8saN4LB4TDNg/640?wx_fmt=png)

## CVE-2022-40684是一个身份验证绕过漏洞，这意味着未经身份验证的攻击者可以通过精心构造的 HTTP 或 HTTPS 请求执行某些管理任务。攻击者执行的最常见的管理任务是泄露 Fortinet 设备配置并在受感染设备上创建超级管理员账户，Fortigate 后端过于相信前端代理，攻击者可以在host和forward中设置内网 127.0.0.1:9980，从而绕过前端验证，直接访问后端api资源。

POC：

```
PUT /api/v2/cmdb/system/admin/admin HTTP/2
```

ForiGate是支持VPN功能的，所以我们可以通过配置vpn进行远程连接，对目标进行扫描

如何配置VPN我就不再详述了，有兴趣的同学可以参考这篇文章：https://blog.csdn.net/meigang2012/article/details/87903878

我们配置好VPN之后本地路由会同步过来，根据路由信息，我们可以对具有特殊性的网段进行探测

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCo9YJdiaGiaq7MQpn9WJUZia9QQ2doB4vRGlvCY0ibwB5hib5CzguBnLjjLPw/640?wx_fmt=png)

在ForiView Sessions 可以看到内网主机经过ForiGate的连接，我们可以通过分析，获取主机上的各种信息，以及目标的一些常用业务网站的地址等其他信息，帮助我们更好的进行横向。

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCotsy97x8mrNJmUllt62ht9M6NxnWZT75NFZrYRY6mO8N05ibDTvInsAQ/640?wx_fmt=png)

例如：可以通过Session信息看到目标主机上安装了卡巴斯基（Kaspersky）。

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCoVkbT37Hk1LHN4Pls80bApTvKTeLiafWjvja63OyjAmoGueCbZPCIcYg/640?wx_fmt=png)

什么是LDAP

* LDAP是一种目录服务协议，通常记录着用户的身份属性以及Computer，邮箱等信息，该协议定义了如何去访问目录服务器以及相关的API。
* AD是目录服务器中的一种，我们可以通过LDAP协议去访问AD目录服务器，同时对AD目录服务器的数据进行操作和查询操作。
* 域控制器默认会开启端口389，当我拿到一个LDAP用户的时候，也就相当于拿到了一个域账户

具体利用方式

通过阅读官方文档，我们不难看出，在配置LDAP的账号都是具有一定权限的，这就意味着我们只要拿到LDAP账号，就有很大可能能登录域控

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjColXgvNw71CZPmaHialgRh6IzIqnPH7jHqBt7tib9xBu65DxcakPwZeFAw/640?wx_fmt=png)

之前有位国外的大佬对  **CVE-2022-40684 进行了分析，并给出了获取LDAP配置的POC，可以看到，通过API是可以获取信息的**

**![](https://mmbiz.qpic.cn/mmbiz_jpg/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCotxAUPPYGsZticrnM4ju7LYweibD9QZR1VYHpdRN4Z7vxhX9fxmhNDu9w/640?wx_fmt=jpeg)**

  但是通过实际的测试，password字段是没有办法获取明文的

![](https://mmbiz.qpic.cn/mmbiz_jpg/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCoDzfduyg7rwIsDGn0UdcNTzA2iblmQiavdWmSpfU1xf57JfiaPWCwpQcvA/640?wx_fmt=jpeg)

但是，在编辑配置的过程中我发现server是受我们控制的，所以我们尝试通过把源配置的地址修改成我们恶意VPS的地址，进行测试连接

![](https://mmbiz.qpic.cn/mmbiz_jpg/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCoBytJkauPcW582icVT6S2RgN7iaFSA6Qk4VYkmusSSlhWFxrxfNWTfqyw/640?wx_fmt=jpeg)

VPS监听389端口，果然我们会发现防火墙会对我们的服务器进行账号密码验证，从而使我们抓到账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCoicfe7yt9qnhEDPS4Wjk7JicLjIwDG6twVicniaMicdb80ZxEG7KqGTUXbkg/640?wx_fmt=png)

通工具连接LDAP，我们可以轻松的获取的域内的信息

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCoFdhjVICjAXhAiclaEWcXpIm2EYCF6XvTgd2QQx2CicQAkibpnlGLN1gBA/640?wx_fmt=png)

通过3389远程连接域控

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCoyGwUibCQGs3O7FgdibjcW38W2PdFGkYWI1eMLiaOSnTU9NhTHAKHoicnlA/640?wx_fmt=png)

通过脚本进行自动化获取信息。

![](https://mmbiz.qpic.cn/mmbiz_png/2F3SX2ib8nCgpiakZiceRqeUw5R1pgJCjCotG6ORYGZicvD8YGan8sLXz2icepWzunYp42gibicLaCCrhqoJZMkJA8axQ/640?wx_fmt=png)

    其实利用的点还很多，这里只是我们总结的一个方面。在渗透测试过程中，很多时候，我们要懂得变通。耐得住寂寞，开拓思维，等待着柳暗花明又一村。

文章来源: http://mp.weixin.qq.com/s?\_\_biz=MzkwNjM5NTkwOA==&mid=2247483741&idx=1&sn=bb94c543b3a417ee236f2e41905412d4&chksm=c0e86936f79fe0208108580c99ff5467c2425469429105b6b400b3118b8dafcbd43e275c548b&mpshare=1&scene=1&srcid=0103hljT8scueLvoo2QKj9Bz&sharer\_sharetime=1672749310625&sharer\_shareid=205c037363a9188e37dfb6bb4436f95b#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)