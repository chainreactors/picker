---
title: 【渗透实战系列】|56-海康安防后渗透利用分析
url: https://mp.weixin.qq.com/s/FHoodSPyiCNJl1RssCYk4Q
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:31:58.364244
---

# 【渗透实战系列】|56-海康安防后渗透利用分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rf8EhNshONTpaEjqEVcwt75zQCblZEptbnS3pl2Dm0SxcpJHJCSKWTqhBy47Tibpn3JlSJvqselvYtoyrNvSWtg/0?wx_fmt=jpeg)

# 【渗透实战系列】|56-海康安防后渗透利用分析

路过一个人
路过一个人

Hacking黑白红

![]()

在小说阅读器中沉浸阅读

目录

```
前言Getshell海康威视综合安防后利用解密  PostgrepSQL 登录+管理员密码替换  minio  ActiveMq  Redis总结
```

## 前言

在近期的一场市政攻防演练中，海康威视综合安防系统作为高价值资产，成为了众人的重点关注对象。我有幸在实战中拿下了这样一个目标。这里总结了海康综合安防系统的得分点和攻击技巧，以备后用。

## Getshell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptyzTCoFjP3stGwm6yj1FEQz4uKYiazNicSreOzmkHicF2MzIpC2kvr6FbQ/640?wx_fmt=png&from=appmsg)

##

目标是通过外网扫描发现的综合安防系统

使用本地 nuclei快速扫描该站点，发现存在反序列化、文件上传等漏洞，选择一个任意文件上传漏洞直接获取了权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEpt0icrV29P8L0DW3qaFhjSEsKeicCzRUljYqcT8QoJa3cogMHoB8KibrKQA/640?wx_fmt=png&from=appmsg)

上传哥斯拉🐎

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEpt9ea88fa80uniaw6G6NsIcEdQFA8lW3UQKGQybqsgYEsibXROhRSQSR8g/640?wx_fmt=png&from=appmsg)

访问海康安防的网站目录如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptTCoBRibk52lntMIFicBuV7HAiadh63OxOqolbpn8SN2ibB35B6sYGmibSzQ/640?wx_fmt=png&from=appmsg)

## **海康威视综合安防后利用解密**

海康威视综合安防系统使用多种加密方式来保护敏感信息，例如配置文件和用户密码。通过解密这些信息，攻击者可以获取系统配置、数据库访问凭证等关键信息。

解密工具：

https://github.com/wafinfo/Hikvision

番外：工具只能在 windows 上用，本地 Macos 用不了，于是开了个虚拟机跑

```
java -jar Hikvision.jar <encryption>
```

### PostgrepSQL 登录+管理员密码替换

```
/hikvision/web/opsMgrCenter/conf/config.properties #海康数据库PostgreSQL配置文件
```

```

```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptc46L0q1ICfhpNnIr6oFQcTgJ5uibvE1bXWAuNEQYrN3ze6ayOdJlFHw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEpt33bsRsH9jYYyP86eszwzj1WPl15fvFZ3hG89j9Nmq0avWjgsoLr1Pg/640?wx_fmt=png&from=appmsg)

解密postgres数据库密码解密获取数据库凭证后，使用 Godzilla 数据库管理模块成功登录，但发现无法查看表内数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptribWWibGURNvJxhAQBK4lp3jcFfN1Zx43v1e9fDDrv5ia230A9behKC9w/640?wx_fmt=png&from=appmsg)

推测可能是哥斯拉自带的数据库管理模块存在兼容性问题。最后通过搭建隧道代理将流量转发至本地，利用哥斯拉内置的代理功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptujVhvwSibLcNAicwp8A1xFSIemddribCH5Xevv5RMBcGSzU0pWmpKqhpg/640?wx_fmt=png&from=appmsg)

`运行管理中心后台登陆用户: 数据库opsmgr_db 用户表:center_user`

本地数据库连接正常，找到 center\_user表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptQ3odlJj0dVErEtRoib4fo1rto6xMpVdefmd59Nib2xicNloWG8T0WWIxg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptNQBYwdGly9fQ19mCzzDZj8sJ1N0OloN2QBC3oFf2AkiaN0GujL7eEAA/640?wx_fmt=png&from=appmsg)

利用之前的海康解密工具生成了新的密码和 Salt，先对原始密码进行备份。然后将 `center_user` 表中的密码和 Salt 替换为新生成的数据，过程如下：

[+] 生成密码成功：P@ssw0rd0.

[+] 生成salt成功：c4ca4238a0b923820dcc509a6f75849b

[+] 替换center\_user表 password salt：983605f69b7a3a91187eb301eda62bbde9513ea706821b3e93ccdadbfe055b88

---

运营管理中心默认端口是8001，访问http://ip/center/login

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEpt31kBflvKokIf8Xmo8qbJJNUzhjUrVrNT56uE0DwgYania0SuUv6d7Sg/640?wx_fmt=png&from=appmsg)

使用修改后的密码登录：sysadmin/P@ssw0rd0. 登录成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptejSjb0qGcZMHF6SAicaj4IvItOBA5iacYcGo3cymyeEojISYlfoL2qPw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptRdyMODKBWb4R6z79KV5riaeLovKnFfibrkawaYwzg1SSTWwKhy53mARg/640?wx_fmt=png&from=appmsg)

可以看见运行管理中心下存在很多运行的服务，接下来要获取这些服务的权限进一步扩大得分,到这一步记得把原有的密码还原。

其余各种数据库配置文件包括redis等，密码都加密了需要进行解密，解密方法相同

```
/hikvision/web/components/ntp.1/conf/config.properties
/hikvision/web/components/activemq514linux64.1/conf/config.properties
/hikvision/web/components/cluster.1/conf/config.properties
/hikvision/web/components/lm.1/conf/config.properties
/hikvision/web/components/ls.1/conf/config.properties
/hikvision/web/components/lsm.1/conf/config.properties
/hikvision/web/components/mps.1/conf/config.properties
/hikvision/web/components/nodejslinux64.1/conf/config.properties
/hikvision/web/components/ntp.1/conf/config.properties
/hikvision/web/components/openjdk11linux64.1/conf/config.properties
/hikvision/web/components/postgresql11linux64.1/conf/config.properties
/hikvision/web/components/redislinux64.1/conf/config.properties
/hikvision/web/components/reportservice.1/conf/config.properties
/hikvision/web/components/svm.1/conf/config.properties
/hikvision/web/components/tomcat85linux64.1/conf/config.properties
```

### minio

默认目录 `/hikvision/web/components/minio.1/conf/` 下的配置文件通常包含了 MinIO 服务的访问凭证。通过解密该配置文件，可以获取到 `accessKey` 和 `secretKey`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptEGax0MYQeWhahzmou14mU42RQQadLyPVV5sa7Z7RZQahyk68gqzVyQ/640?wx_fmt=png&from=appmsg)

MinIO 服务默认监听在 9000 端口。由于 MinIO 前端页面涉及大量 JavaScript 的自动加载，若采用隧道代理，可能会导致资源加载异常，从而无法正常显示登录页面。

### ActiveMq

目录：/hikvision/web/components/activemq514win64.1/

刚开始的时候访问端口发现 404 未能跳转到登录页面，查看当前目录的 jetty.xml发现默认路径为 /activemqmamage

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptN6cVzFYvmws1HPzBotgFwicHFVoPCkD7Jpf3SibuVswg31uNIsIUZNQw/640?wx_fmt=png&from=appmsg)

最终访问http://ip/activemqmamage

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptDwbS7ukIZOXN1iaNADAegdq2OeSTdzdLBkccRlGO9AXPw9DNw5oF0wA/640?wx_fmt=png&from=appmsg)

### Redis

同样获取 redis 密码解密登录成功如下：/hikvision/web/components/rediswin64.1/conf/config.properties

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTpaEjqEVcwt75zQCblZEptbIBjs71BiblWH9QrlfXp4HOyQQLBWQmMYjVGHehmoic0ruKE7Q8oUR9A/640?wx_fmt=png&from=appmsg)

## 总结

海康威视综合安防系统通常包含三个以上服务实例（如 PostgreSQL、Redis、minio 等）。在实际渗透过程中，这些文件中往往隐藏着数据库连接凭证、API密钥或系统敏感信息，深入分析往往能带来意外的收获。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rf8EhNshONSgp1TKd5oeaGb76g5eMFibnANHNp30ic7NtpVnU12TNkBynw2ju7RDHbYtVZibm5rjDh7VKbAEyO8ZQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp#imgIndex=63)

**网络靶场思维导图**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONSxos09ofR8rMosX8OyFTib6sCaMFtHB8ZqfGiaKKgfgEXCRJj6HYxLLABMHb2xELR2Uib4CUPIZlLTw/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=64)

```
资料获取

回复“电子书”获取web渗透、CTF电子书:

回复“视频教程”获取渗透测试视频教程;

回复“内网书籍”获取内网学习书籍;

回复“CTF工具”获取渗透、CTF全套工具;

回复“内网渗透”；获取内网渗透资料;

回复“护网”；获取护网学习资料 ;

回复“python”,获取python视频教程；

回复“java”，获取Java视频教程;

回复“go”，获取go视频教程

知识星球
```

【Hacking藏经阁】知识星球致力于分享**技术**和**认知**。

**1、技术方面。**主攻渗透测试（web和内网）、CTF比赛、逆向、护网行动等；

400G渗透教学视频、80多本安全类电子书、50个渗透靶场（资料主要来自本人总结、以及学习过程中购买的课程）

**2、认知方面。**副业经营、人设IP打造，具体点公众号运营、抖\*yin等自媒体运营（目前主要在运营两个平台4个号）。

如果你也想像我一样，不想35岁以后被动的去面试，那么加入星球我们一起成长。

欢迎加入99米/年，平均每天2毛7分钱，学习网络安全一整年。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONShDSbaaStARPj9t8BRl2VXu6r8XjAfoyWVLNtuibD8Dk6Wb0icpNFoUt3EKa27qXXpk5mJPkrkbXAw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&retryload=1&tp=webp#imgIndex=65)

*渗透实战系列*

[▶](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247525667&idx=1&sn=5f79f7dedb2b96197cedf34b90136e0a&chksm=ce64cfbaf91346ac008d096dfc97eecf8cec0fa2e7d2f9f11783bc889fa99f4dc07ec581e323&token=1146059525&lang=zh_CN&scene=21#wechat_redirect)[【渗透实战系列】|55-某大型集团渗透测试（全域权限）](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247548256&idx=1&sn=09cacadbcb7fe7a7c38c3b3a9dcc5208&scene=21#wechat_redirect)

[▶](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247525667&idx=1&sn=5f79f7dedb2b96197cedf34b90136e0a&chksm=ce64cfbaf91346ac008d096dfc97eecf8cec0fa2e7d2f9f11783bc889fa99f4dc07ec581e323&token=1146059525&lang=zh_CN&scene=21#wechat_redirect)[【渗透实战系列】|54-小程序渗透记录 通过细节挖掘漏洞的艺术](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247544884&idx=1&sn=82fe2afa774e253e020af6d28ecf0d9e&scene=21#wechat_redirect)

[▶](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247525667&idx=1&sn=5f79f7dedb2b96197cedf34b90136e0a&chksm=ce64cfbaf91346ac008d096dfc97eecf8cec0fa2e7d2f9f11783bc889fa99f4dc07ec581e323&token=1146059525&lang=zh_CN&scene=21#wechat_redirect)[【渗透实战系列】|53-记一次3万多赏金的XSS漏洞挖掘经历](https://mp.weixin.qq.com/s?__biz=Mzg2NDYwMDA1NA==&mid=2247544816&i...