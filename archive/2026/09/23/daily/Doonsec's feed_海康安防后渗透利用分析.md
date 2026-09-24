---
title: 海康安防后渗透利用分析
url: https://mp.weixin.qq.com/s/lYqLl0pRO8v-a5NVhGtjoQ
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:00:15.184208
---

# 海康安防后渗透利用分析

# 海康安防后渗透利用分析

路过的一个人
路过的一个人

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
原文作者:路过的一个人原文链接:https://xz.aliyun.com/news/91059
```

## 前言

在近期的一场市政攻防演练中，海康威视综合安防系统作为高价值资产，成为了众人的重点关注对象。我有幸在实战中拿下了这样一个目标。这里总结了海康综合安防系统的得分点和攻击技巧，以备后用。

## Getshell

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTy2daZIHTFMM5DvuiaDQgj59WPTcf6x45mdR7AZXp951hs3Bn2rMGbLvMxTMEnibF5abuFSPh0F2oGaN4ZDQg8bU42tRicYZHSew/640?wx_fmt=png&from=appmsg)

目标是通过外网扫描发现的综合安防系统

使用本地 nuclei快速扫描该站点，发现存在反序列化、文件上传等漏洞，选择一个任意文件上传漏洞直接获取了权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRCtduB5iclycx01tOEDYnMrS1WXlOAOXhO8pOkRcZQhDbVTzm8Jib2efktWYQX8aSz4oK2YCvpxGTn3V6b9ribiakuE3g37uTbbs/640?wx_fmt=png&from=appmsg)

上传哥斯拉🐎

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSEsmf8ErEmY6aFibm9otKrMgkF4nTz1z8ticS8gTRiaLFJLoQoct6oic4RCtvatFQ8xt32iaXjh6v6FnIV01eMTeXWtRKuOnu6ibGIE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTJOZI3FAgV7Ys8EtJ0eCxDvCQXmfk6jDl5uxkXZmmvSO3AlaufHrz2h0FdglDVD5dC8VxMSM8EpHUcOZyX6n8QGUfGbxtPw9A/640?wx_fmt=png&from=appmsg)

访问海康安防的网站目录如下：

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR19ibZkiaFr29rzcIVlSr4ibN6GNqMkxicsXp8KiclLqRugYLb303pRPoemlIN4HY3EToueqMZKP9NI3tDibGOZGcL3piaibcxparZVkg/640?wx_fmt=png&from=appmsg)

## **海康威视综合安防后利用解密**

海康威视综合安防系统使用多种加密方式来保护敏感信息，例如配置文件和用户密码。通过解密这些信息，攻击者可以获取系统配置、数据库访问凭证等关键信息。

解密工具：

https://github.com/wafinfo/Hikvision

番外：工具只能在 windows 上用，本地 Macos 用不了，于是开了个虚拟机跑

```
java -jar Hikvision.jar <encryption>
```

### PostgrepSQL 登录+管理员密码替换

###

```
/hikvision/web/opsMgrCenter/conf/config.properties #海康数据库PostgreSQL配置文件
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQlJBgYkibicGhH0Q5ZWAD9FafPONSZjuiclxGH3nxpic7NJOxtqicRlXr7XSoyrlXg9gDNMrhIoK2RpJ3ScmkaA4aUbCtTWblD42wk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT6yol80o5HNNiacmS3Ol54Wh9Qp1eyicNiabKAcTcxlPkUuB9icTuzENc1yX90Obu3XCLGyKekibKEzw4eYmXlU2NALfeX2MVVFsiag/640?wx_fmt=png&from=appmsg)

解密postgres数据库密码解密获取数据库凭证后，使用 Godzilla 数据库管理模块成功登录，但发现无法查看表内数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQiaML9AQNx4iatPVsQYePrGyntibiaGsOyIrYWa1BWGZcYbLQdBhouB2q1j7jP9PpNhclkpOX7Vc4WuypELrpYDonZCYMWYV1Vhia4/640?wx_fmt=png&from=appmsg)

推测可能是哥斯拉自带的数据库管理模块存在兼容性问题。最后通过搭建隧道代理将流量转发至本地，利用哥斯拉内置的代理功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS0lmSeUgITCmiayM3MMmXGvGH05O9bq6bxgHf0pR8ZMKqqGB3ab64tgCXZyoyBibibQcqqicmcFsdMFKswX42AOwe7cticMzFHSNZc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQfiaMwWiaxWzqrvC8SO5oHYiaHO6ds01vIF1hrziaaxFolM9HniblVSEia58sbOTHgvM9lRDFpzbSjY7H90XhibjJYWaMic6gEGmBsFrs/640?wx_fmt=png&from=appmsg)

`运行管理中心后台登陆用户: 数据库opsmgr_db 用户表:center_user`

本地数据库连接正常，找到 center\_user表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ1oK3r2bWQvfdiaZbUSXxXvvkibTZzcpnIjRquWKjK8y3JlveMto5Ij0QA6xJgV47liaR7mu3rTuVkbHs4JkSLHzPTGNAURlAK3c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSC0MrDcSicHDQ1agtmSX6Q0g6dZI9jibG73lVnibNA59aNy15mK3XImicibFJhcWnQuvPM4mkFOqMrskp5ybCYSibhl5NIMRjiaAHVGw/640?wx_fmt=png&from=appmsg)

利用之前的海康解密工具生成了新的密码和 Salt，先对原始密码进行备份。然后将 `center_user` 表中的密码和 Salt 替换为新生成的数据，过程如下：

[+] 生成密码成功：P@ssw0rd0.

[+] 生成salt成功：c4ca4238a0b923820dcc509a6f75849b

[+] 替换center\_user表 password salt：983605f69b7a3a91187eb301eda62bbde9513ea706821b3e93ccdadbfe055b88

运营管理中心默认端口是8001，访问http://ip/center/login

使用修改后的密码登录：sysadmin/P@ssw0rd0. 登录成功

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTSibGlac2PFicPRbyL2Srha1q7JFqzpfUtgtqKYkh8rjGGcS9uicsaTrGx0N29enfI2n2JUAJyUgiawoGUX1SnZFZgMCZJHFuxahg/640?wx_fmt=png&from=appmsg)

可以看见运行管理中心下存在很多运行的服务，接下来要获取这些服务的权限进一步扩大得分,到这一步记得把原有的密码还原。

其余各种数据库配置文件包括redis等，密码都加密了需要进行解密，解密方法相同

```
/hikvision/web/components/ntp.1/conf/config.properties/hikvision/web/components/activemq514linux64.1/conf/config.properties/hikvision/web/components/cluster.1/conf/config.properties/hikvision/web/components/lm.1/conf/config.properties/hikvision/web/components/ls.1/conf/config.properties/hikvision/web/components/lsm.1/conf/config.properties/hikvision/web/components/mps.1/conf/config.properties/hikvision/web/components/nodejslinux64.1/conf/config.properties/hikvision/web/components/ntp.1/conf/config.properties/hikvision/web/components/openjdk11linux64.1/conf/config.properties/hikvision/web/components/postgresql11linux64.1/conf/config.properties/hikvision/web/components/redislinux64.1/conf/config.properties/hikvision/web/components/reportservice.1/conf/config.properties/hikvision/web/components/svm.1/conf/config.properties/hikvision/web/components/tomcat85linux64.1/conf/config.properties
```

### minio

默认目录 `/hikvision/web/components/minio.1/conf/` 下的配置文件通常包含了 MinIO 服务的访问凭证。通过解密该配置文件，可以获取到 `accessKey` 和 `secretKey`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRFwtZbuM3jr9L93x1vNCAmxzFAU0v5DibMlbABcG9qmpM0xssl8riaibJdp27XjZSmuFC9gLiaM01xK2PVf4Iz8M5cgia2F8BO4bfQ/640?wx_fmt=png&from=appmsg)

MinIO 服务默认监听在 9000 端口。由于 MinIO 前端页面涉及大量 JavaScript 的自动加载，若采用隧道代理，可能会导致资源加载异常，从而无法正常显示登录页面。

### ActiveMq

目录：/hikvision/web/components/activemq514win64.1/

刚开始的时候访问端口发现 404 未能跳转到登录页面，查看当前目录的 jetty.xml发现默认路径为 /activemqmamage

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQHN7x911XzX0tGvyfwMibLAJ8icSbviaOGtu84Us7wpIiaQOkvgJZudfmGnKoPFJUJyLKefJ89wQamcmhmdK5XNxGG0HTDFTK78Ck/640?wx_fmt=png&from=appmsg)

最终访问http://ip/activemqmamage

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboS3bictNgK9bV01TibNavgcbibNuDnY4RdjxTuYdH0Bflp9ySPNU4j36pb6uqcqtx2RMD6WbqfNqVgZqJ01CBAAPGa8aeKczPVV2k/640?wx_fmt=png&from=appmsg)

### Redis

###

同样获取 redis 密码解密登录成功如下：/hikvision/web/components/rediswin64.1/conf/config.properties

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR6hwT1uKbWZgjibmpsBBb4YmY7xs91UoLhES4QOVYxwU5wSVll3pgwYskwCnOzcTTTNeZc5YJVEt1StEibLib0fndsSHP57VMzuM/640?wx_fmt=png&from=appmsg)

## 总结

海康威视综合安防系统通常包含三个以上服务实例（如 PostgreSQL、Redis、minio 等）。在实际渗透过程中，这些文件中往往隐藏着数据库连接凭证、API密钥或系统敏感信息，深入分析往往能带来意外的收获。

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**skill+grok辅助挖掘某企业sr****c****实战效果，能出但是重复多，agent独立挖掘也可以，见仁见智，看个人习惯，好的模型是最重要的。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQwyn779TTwY7vZkePQCL8k3K8dYxNdyzfgADL4dJcNUvpmodLeDVCZ6xDC4RJXEBmO2tcWqgUNdTVicKTW0jpdsg7X6xwP5gIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQnIqagDL2A4BUIXrib9YVmATWuaIDqETqYd9ToHib52mDyoMyqc6Wzh733FRnbsDsGgey7B8s8jr72UtkPY6ich58niaPJqoItKcE/640?wx_fmt=png&from=appmsg)

**企业src边缘&核心资产实战效果&&有重复但是证明好模型+AI确实够用**

**（图片仅供参考，我出不等于你出，见识**到**ai神力即可，多去用AI!!!）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1YNI9U6r6NMO4UMUBROoWeC4XQC4Dge94ODZ7tXY6tbxqb3IJoghve0u1SfkygE5UJ5HTdUBvLZKrn5ps13F71piax5dlHnOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGjdxKy4nllaLXIznTvRqicichITccuB8psYFRYakw6ViauCk6iccziahfPw4fnrqhyCp7Zkq7lRI0DOicyrZlNyicYibTVibfGFZVaG0c/640?wx_fmt=png&from=appmsg)

**不是P图,单洞1.2w记录**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQQpQdR2Ttwqxibyr75Is0kBG2N2tLYQIaau7SS278oyQ4RDpNScviaMt4wtlfgDCibE05WgoMhE5kZUrP8ciaYIdnxA594wsmoAAs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRn2EsfFkA5mG6dcn7JLQMroc2dy3EQb3ueY2Cspd0WYgicXEnSF68UD43nNd4plkxmkTpEOh2kkQMEWZZIjE0ibA8r1q4IfiaxI/640?wx_fmt=png&from...