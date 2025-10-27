---
title: Docker搭建企业邮箱，poste.io教程
url: https://buaq.net/go-164988.html
source: unSafe.sh - 不安全
date: 2023-05-22
fetch_date: 2025-10-04T11:36:56.197852
---

# Docker搭建企业邮箱，poste.io教程

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

![](https://8aqnet.cdn.bcebos.com/9185adab7e14934f07fd086a8fd87994.jpg)

Docker搭建企业邮箱，poste.io教程

首先要知道，搭建企业邮箱即可拥有自己的域名后缀邮箱，自定义邮件地址，什么admin，root，info都是随便用的。Poste.io官网：https:/
*2023-5-21 22:2:50
Author: [blog.upx8.com(查看原文)](/jump-164988.htm)
阅读量:72
收藏*

---

首先要知道，搭建企业邮箱即可拥有自己的域名后缀邮箱，自定义邮件地址，什么admin，root，info都是随便用的。Poste.io官网：https://poste.io/ 文档：https://poste.io/doc/

Poste.io 是一个电子邮件服务器解决方案，旨在提供简单且安全的电子邮件系统。它提供了一个完整的邮件服务器堆栈，包括邮件传输代理（MTA）、邮件传输代理（IMAP/POP3）和邮件过滤器。Poste.io 的设计目标是易于部署和管理，并且适用于个人用户、小型企业和中小型组织。

Poste.io 提供了一个直观的 Web 界面，使用户可以轻松设置和管理他们的邮件服务器。它支持多个域名和用户帐户，并提供了用户管理、电子邮件过滤、垃圾邮件和病毒检测等功能。此外，Poste.io 还集成了基于网页的电子邮件客户端，使用户能够通过 Web 浏览器访问和发送电子邮件。

1、域名一个，如果没有，点击 Gname 购买一个com、net或者org，不推荐用icu等不受信任的域名后缀。

2、vps，推荐使用 莱卡云 ，中文页面，购买的主机全部开通25，推荐购买2G内存或以上（视频演示中我使用的是 美国CN2 GIA（弹性）2核1G ），但是不能滥用。企业或者个人正常使用可以发工单申请rDNS。
大家知道，市场上开通了25的vps并不好找，我以前介绍过的CC，也是直接支持rDND的，自己可以在后台绑定，注册地址：https://app.cloudcone.com.cn/?ref=7462 优惠的vps可以参考页面：<https://bbs.csdn.net/topics/610404063>

本次教程，我使用的vps系统为Ubuntu 20.04！

不过，我们当然还是先进行域名解析如下：

| 主机记录 | 记录类型 | 记录值 |
| --- | --- | --- |
| mail | A | 你的IP地址 |
| smtp | CNAME | mail.\*\*.com |
| pop | CNAME | mail.\*\*.com |
| imap | CNAME | mail.\*\*.com |
| @ | MX | mail.\*\*.com |
| @ | TXT | v=spf1 mx ~all |

1、更新系统，安装docker和screen；

```
apt  update && apt install screen docker.io -y
```

2、拉取镜像；

```
docker pull analogic/poste.io
```

3、新建邮件目录

```
mkdir /home/mail
```

4、在screen中启动容器，注意这里的：mail.\*.com要改成你的邮箱域名！

```
screen
docker run \
    --net=host \
    -e TZ=Europe/Prague \
    -v /home/mail:/data \
    --name "mailserver" \
    -h "mail.*.com" \
    -t analogic/poste.io
```

5、访问地址 mail.你的域名/admin/install/server（这里显示不安全，继续访问，下一步设置证书），设置域名，管理员邮箱和密码。

6、在系统设置中，找到标签`TLS Certificate`，自动申请个证书。申请完证书，就可以https访问了。然后在域名详情中，点击生成`redirect`，生成后添加域名DKIM 解析，例如：

```
s20230520790._domainkey.proxies.icu. IN TXT "k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxdSK7/g146G3kTo9KrjXBmHJr6PQA80RbL/f6iAQ1zRgGi3n9sbxmXXsBFrgXhMqOdE5BTVts2Z1z2TsWyBHxhHYJcy2uDJN6xnTMOxiLWgjLkzcl49BM//53n75VLlQIJcmmRzHrHfbowWk8g7wAKH6ClC/GRoJ7VVs8/ESZYQPd1oQdcQ1XiDCt4XI7u+CzupfOKQ+9XnEsCKFQTye4Qtjbbp/SXI8CCl0Bdv8bdRAtwHxPGf2f8fee1KnmUCHWT5Cfdw9oB3Dwd77eTPKVFRtFYz7IT5yrk2HWmQT3oBVIepWpapxMIpviOX8zJ522HTlPuhBJhoi9Ep4qmzPnQIDAQAB"
```

![截屏2023-05-20 19.35.18.png](https://iweec.com/usr/uploads/2023/05/3468958996.png "截屏2023-05-20 19.35.18.png")

7、在邮件账户中，可以添加删除用户；服务器状态中，查看诊断，能清楚的看到服务器端口状态；
顺便给大家检测25端口的命令：telnet smtp.qq.com 25

8、邮箱用户登陆地址为 mail.你的域名/webmail/，可以测试发信了；检测邮箱健康 <https://www.mail-tester.com/>

得分超过5就能使用，但是要想更高一些分数，可以提交工单申请rDNS，前提是你不能发送垃圾邮件。

收件服务器【IMAP】

| 设置 | 内容 |
| --- | --- |
| EMAIL | 你的邮箱 |
| 密码 | 你的邮箱密码 |
| 服务器【Host Name】 | mail.\*.com |
| 端口【Port Number】 | 993 |
| Security | SSL |

寄件服务器【IMAP】

| 设置 | 内容 |
| --- | --- |
| EMAIL | 你的邮箱 |
| 密码 | 你的邮箱密码 |
| 服务器【Host Name】 | mail.\*.com |
| 端口【Port Number】 | 587 |
| Security | SSL |

忘了说，最好是再设置一下hostname，参考<https://blog.upx8.com/3567> 或者直接

```
sudo hostnamectl set-hostname mail.* .com
```

B站：https://www.bilibili.com/video/BV1eT41147kY/
YouTube：https://www.youtube.com/watch?v=d8ySEJSb2GQ

文章来源: https://blog.upx8.com/3568
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)