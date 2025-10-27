---
title: SRC之若依系统弱口令恰分攻略
url: https://www.freebuf.com/articles/web/421543.html
source: FreeBuf网络安全行业门户
date: 2025-02-13
fetch_date: 2025-10-06T20:35:03.943161
---

# SRC之若依系统弱口令恰分攻略

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

SRC之若依系统弱口令恰分攻略

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

SRC之若依系统弱口令恰分攻略

2025-02-12 11:44:29

所属地 台湾省

**本文作者：Track-杳若**

# 前言

```
若依系统存在较多魔改版本，具有前后端分离的情况，内置了druid
```

通过这个拿下了交大证书

![img](https://image.3001.net/images/20250212/1739332110_67ac1a0ee23faec8e75af.png!small)

# Druid弱口令上分攻略

## 信息收集

首先，我们要做的是收集基于若依CMS的系统

### 图标收集方法

最简单的就是利用图标的方法进行收集(以下只是举例)

```
(icon_hash="-1231872293" || icon_hash="706913071")
```

![img](https://image.3001.net/images/20250212/1739332111_67ac1a0fb9bed3a2646ec.png!small)

### 内容收集

另外可以收集的就是内容 ![img](https://image.3001.net/images/20250212/1739332113_67ac1a111b4ea8262778c.png!small)

下面是以主体中的关键字进行匹配(大部分存在二改的情况)

![img](https://image.3001.net/images/20250212/1739332114_67ac1a12b7539aef949d9.png!small)

### 标题收集

![img](https://image.3001.net/images/20250212/1739332115_67ac1a13bfd7b5498635e.png!small)

收集类似的标题

![img](https://image.3001.net/images/20250212/1739332116_67ac1a14a7d1a92ec9192.png!small)

### 前后端分离之后端收集1

发现下述内容，是ruoyi后端，也需要进行收集

![img](https://image.3001.net/images/20250212/1739332117_67ac1a15d139dee0a46e8.png!small)

由于存在很多魔改版本,大致会修改ruoyi那一段

![img](https://image.3001.net/images/20250212/1739332118_67ac1a169af6934ef9227.png!small)

收集的思路大致为内容匹配(以下是思路之一)

![img](https://image.3001.net/images/20250212/1739332119_67ac1a17487f470dc7674.png!small)

### 前后端分离之后端收集2

除了存在后台欢迎的情况，也可能做了弱权限校验，会出现以下情况

![img](https://image.3001.net/images/20250212/1739332120_67ac1a180b29e7f340836.png!small)

因此此类也需要收集

![img](https://image.3001.net/images/20250212/1739332120_67ac1a18a553a83f95891.png!small)

### 权限校验回显500

![img](https://image.3001.net/images/20250212/1739332121_67ac1a197810a2d6fbde7.png!small)

该回显不是严格意义上服务器回显500，与之前遇到的回显401弱校验类似

拼接了/druid/login.html

![img](https://image.3001.net/images/20250212/1739332122_67ac1a1a59013fa503e8e.png!small)

一看图标，尝试若依弱口令 123456 直接进去了

![img](https://image.3001.net/images/20250212/1739332123_67ac1a1b5e1dde47a67a0.png!small)

### 最重要

如果是为了教育上分的话，需要加上一点小小的黑魔法 加上下面这句话就会筛选出来的内容为教育网段内容

```
org="China Education and Research Network Center"
```

![img](https://image.3001.net/images/20250212/1739332124_67ac1a1c7d0fdaaa18408.png!small)

## druid目录探测

### 默认路径探测0-未授权

如果配置不当可能不需要druid密码即可直接访问druid

```
/druid/index.html
```

### 默认路径探测1-druid

若依默认的druid路径是

```
/druid/login.html
```

收集的网址直接拼接，如果成功，就说明存在druid后台

![img](https://image.3001.net/images/20250212/1739332125_67ac1a1d6595b13532917.png!small)

### 默认路径探测2-默认api

若依存在默认的api，druid的路径可能在api下

```
/prod-api/druid/login.html
/dev-api/druid/login.html
```

收集的网址直接拼接，如果成功，就说明存在druid后台

![img](https://image.3001.net/images/20250212/1739332126_67ac1a1e2f3c5821defd3.png!small)

### 默认路径探测3-开发自定义

在这个情况下，直接扫描是没有任何用处的，通常的思路是首先浅浅登录错误一次，查看数据包的目录

#### 示例如下

发现存在一个地址

![img](https://image.3001.net/images/20250212/1739332128_67ac1a20a9e5c6313cecb.png!small)

抓包查看地址后发现如下目录

![img](https://image.3001.net/images/20250212/1739332132_67ac1a24aa292d2d395f2.png!small)

那么拼接地址为

```
/{发现的api}/druid/login.html
```

![img](https://image.3001.net/images/20250212/1739332133_67ac1a2577df928ec5dab.png!small)

### 默认路径探测总结

常见路径地址如下

```
/druid/index.html
/druid/login.html
/prod-api/druid/login.html
/prod-api/druid/index.html
/dev-api/druid/login.html
/dev-api/druid/index.html
/api/druid/login.html
/api/druid/index.html
/admin/druid/login.html
/admin-api/druid/login.html
```

甚于内容请在实战中进行尝试

## druid弱口令爆破

通常druid不需要验证码就可以进行爆破（请自行收集字典)

### 常见用户名

```
admin
druid
ruoyi
...
```

### 常见密码

```
123456
admin
druid
...
```

## 任意用户注册(较少见)

通常我们遇到的ruoyi系统如下

![img](https://image.3001.net/images/20250212/1739332136_67ac1a28c0905e8fcddbd.png!small)

注意URL为

```
https://xxxxx.edu.cn/login?redirect=%2Findex
```

也可能遇到其他二改系统的路径为

```
https://xxxxx.edu.cn/{任意内容}/login?redirect=%2Findex
```

![img](https://image.3001.net/images/20250212/1739332148_67ac1a34cbcf5aed3c429.png!small)

大部分使用ruoyi框架的人都会忽略掉前端的注册界面(后端可能删了) 因此我们拼接/register

![img](https://image.3001.net/images/20250212/1739332151_67ac1a375423f54b1e0a7.png!small)

这个时候我们注册账户，如果后端未关闭的话，可以注册成功

注册失败大致如下

![img](https://image.3001.net/images/20250212/1739332155_67ac1a3ba1e839f185579.png!small)

下面是某交的成功案例

![img](https://image.3001.net/images/20250212/1739332159_67ac1a3f7cbe1994723a0.png!small)

## Druid登录后利用

在我们无法登录若依的时候，如果我们获取到了druid连接池，我们可以尝试扩大危害

首先如何发现druid请看前文

<https://bbs.zkaq.cn/t/31119.html>

进入druid后我们重点关注的是`/druid/weburi.html`与`/druid/websession.html`

### Druid到获取未授权路由

在这我们可以获得创建了连接池的URI ![img](https://image.3001.net/images/20250212/1739332161_67ac1a41b76aa4f8e5bcc.png!small)

在这里面如果开发在开发的时候没做权限校验，我们可以获得未授权的API接口

在这里就放个案例，进去之后发现了一个接口

![img](https://image.3001.net/images/20250212/1739332163_67ac1a43ea835db364902.png!small)

通过拼接发现了未授权接口

![img](https://image.3001.net/images/20250212/1739332165_67ac1a45a26d5e5d9c2d6.png!small)

### Druid到敏感信息泄露

有时候可能会在路径中翻到上传的文件(如PDF后缀)

![img](https://image.3001.net/images/20250212/1739332166_67ac1a46d095aef4e941f.png!small)

访问的话，会发现泄露了大量的敏感信息

![img](https://image.3001.net/images/20250212/1739332169_67ac1a49064fbc0d86d4d.png!small)

### Druid到登录系统

在`/druid/websession.html`路径下，我们有时候可以看到已经连接的`SESSIONID`

![img](https://image.3001.net/images/20250212/1739332170_67ac1a4a70a222a6f56bf.png!small)

我们切到登录处在登录的同时替换掉`SESSIONID`有可能可以登录系统

这里不进行赘述

## Swagger-ui泄露

除了Druid之外，其实和Swagger组件是一起的

同理也存在自定义路径的可能性需要收集，如果Swagger组件没修改的话，查看的效果和druid泄露的效果类似

这边提供部分路径(建议确定是否是自定义路径之后进行dirsearche扫描)

```
/swagger-ui/index.html
/prod-api/swagger-ui/index.html
/api/swagger-ui/index.html
```

## 进系统捡漏硬恰

有时候/druid/login.html界面是无法直接访问到的，进行了权限校验，要登录系统才可以

那我们需要获取权限，最好的方法是先登录若依

![img](https://image.3001.net/images/20250212/1739332171_67ac1a4b8e3a9e70ac7d1.png!small)

往往大部分能直接登录若依的弱口令被恰的差不多了，我们可以进系统恰druid，这是大部分人忽略的地方

![img](https://image.3001.net/images/20250212/1739332172_67ac1a4caa6bee35db7d6.png!small)

往往内嵌在系统数据监控中，这是一种捡漏的方法

![img](https://image.3001.net/images/20250212/1739332173_67ac1a4dd858399b358d9.png!small)

## 总结

相对来说爆破还是需要一本好的字典的，重点在于收集面

以下是在edu-src中使用druid弱口令上分的部分

![img](https://image.3001.net/images/20250212/1739332175_67ac1a4f272b79fe49e74.png!small)

# 渗透测试 # 黑客 # 网络安全 # web安全 # CTF

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

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

信息收集

* 图标收集方法
* 内容收集
* 标题收集
* 前后端分离之后端收集1
* 前后端分离之后端收集2
* 权限校验回显500
* 最重要

druid目录探测

* 默认路径探测0-未授权
* 默认路径探测1-druid
* 默认路径探测2-默认api
* 默认路径探测3-开发自定义
* 默认路径探测总结

druid弱口令爆破

* 常见用户名
* 常见密码

任意用户注册(较少见)

Druid登录后利用

* Druid到获取未授权路由
* Druid到敏感信息泄露
* Druid到登录系统

Swagger-ui泄露

进系统捡漏硬恰

总结

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

* [...