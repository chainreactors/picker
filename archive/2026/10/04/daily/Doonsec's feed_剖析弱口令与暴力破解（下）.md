---
title: 剖析弱口令与暴力破解（下）
url: https://mp.weixin.qq.com/s/B6Q2CtAlcOp7ksLL7iZmMA
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:54:17.890747
---

# 剖析弱口令与暴力破解（下）

# 剖析弱口令与暴力破解（下）

原创

晨星安全团队
晨星安全团队

晨星安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 剖析弱口令与暴力破解（下）

上一篇拆解了DVWA暴力破解模块Low、Medium、High三个级别的完整PHP源码，看到输入过滤、失败延时、表单Token都只能起到辅助防护作用，无法独立抵御口令暴力枚举。

本篇我们结合CTF实操案例，梳理各类业务系统、硬件设备常见默认口令。

## CTF Web 实战

### 网站被黑（BugKu CTF）

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9Qjhoic18MJWHjS4vBiaOtugAlTw1cqPIsIt8x46dW36fHn5gJmTT6Ataq2icJKYurhn2aVv4krsZX1HKwJDVcFYLOCMJySfKgiaCFLA/640?wx_fmt=webp&from=appmsg)

打开是一个静态网页

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9QjiaFKA4ialia2JHxgNjBnicM7Uia2lkRmlr9hstqpR1Ucof7A78ELHL2iclSXmrDOONfj4QbVPibfLmBScPmC6LdXiaUZVRicEd8icUficzcU/640?wx_fmt=webp&from=appmsg)

扫描后台目录找到登录页面

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9Qjjn4ia9IQYibxzwawZjWLqMNtOuux5rJ0reCmOY5JIVXEWFibGPczl2ibBFQw0gGqPSlUoicQupapoFDibMiaOmv0R8ugCI9BZZ5hJo60/640?wx_fmt=webp&from=appmsg)

访问发现只需要密码

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9QjiaSb69fAE6frR9uauXVmuqWOeXtBGdklrqXCGXsS0ic8jhUkoWsK4LLcCoz0wMD0iblraLL3Vtbyn2b6fDDwU2gcQqujhfibmCVc4/640?wx_fmt=webp&from=appmsg)

因为没有给其他线索，所以使用 BurpSuite 爆破，先开启代理拦截，输入 1234 后抓包发送到攻击模块

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9Qjia3SvIQup88gcOqobuicuY2ib5QbIgOU0ialYG8g0eBKH3GIgicuE55cVZscrIAzNC7O1boxcOH14C0z90pfdy261W0HwhVl5Nh0OI/640?wx_fmt=webp&from=appmsg)

给要爆破的密码参数添加 $，类型选择狙击手

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9QjgSSb1ib7Yxicrg4ic83Ivry8YZIBby2XGE67o3Irh2ZHTPDGsst6At40ZaiczyeQCXA4NhV2OiblFEnHAGWoiaweGic9OgcUrEXJ4hno/640?wx_fmt=webp&from=appmsg)

在有效载荷中配置字典

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9QjgOO9BibNiczUuX9qicxYNJ9RFwia4hjTv73Ajmrs6ia50x4E897V7wQU3Ay9vO9lgicn1IIdDoKKO2cLhgQBXSYGzMUbmWkdn9CXwgU/640?wx_fmt=webp&from=appmsg)

点击右边的开始攻击，然后会弹出这个攻击框

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9QjhMaWmok0CstLsXicgvEbIGR33iat66odecDUy0iaqbZCB02qYKCKbcSkmVVEBVWsswv4RK1XWptHrjlRgbrLJzn1QFibeTGYK0fdE/640?wx_fmt=webp&from=appmsg)

选择长度排列找出不一样的数据包，看到有个 hack 与其他的不一样

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9QjjxGJoXS3oicZ3Lj284VGP2xenAJmYI2ZIu5TgqWPMQcfKQER9WIogtb5nzrMSYYTnpZjiccT2Y42pFBqx2r4D9ricqJGxjszYLI0/640?wx_fmt=webp&from=appmsg)

输入 hack 拿到 flag

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9Qjia4wHpy4xnP6Vbzur9foibJAH67r9SQicdHnHG5mBdy1pKVLUzlGYRTtgic8LLOyduX1kiaPx3qGibR8QicZWb71s02eRMuc7Qv55DZI/640?wx_fmt=webp&from=appmsg)

## 刷洞技巧

### 若依框架等

FOFA 语法：`(icon_hash="-1231872293" || icon_hash="706913071")`

默认弱口令：admin/admin123

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZCjMVth9Qjiat9wklupQzy8XSiaviaRELKQwk2ybeuArePt6sfCBbljM57RtdDJibYZcDpYWtfib0ESzVQtvdlv4qpdiat3KJ2NwXwgXiawEkuibbtE/640?wx_fmt=webp&from=appmsg)

### 系统设备等

#### 致远OA

1. `system` / `system`：A8系统系统管理员、A6的单位管理员
2. `group‑admin` / `123456`：集团版集团管理员
3. `admin1` / `123456`：企业版单位管理员
4. `audit‑admin` / `123456`：审计管理员

#### 泛微OA

1. `sysadmin` / `1`

### 安全设备

#### 常见安全设备

| 设备产品 | 用户名 | 默认密码 |
| --- | --- | --- |
| 天融信防火墙 | superman | talent |
| 联想网御防火墙 | admin | leadsec@7766、administrator、bane@7766 |
| 深信服防火墙 | admin | admin |
| H3C | admin | adminer |
| 山石防火墙 | hillstone | hillstone |
| 绿盟IPS | weboper | weboper |
| 深信服VPN | 51111端口 | delanrecover |
| 迪普防火墙 | admin | admin\_default |
| 明御WAF | admin | admin |
| 华为防火墙 | admin | Admin@123 |
| Zabbix | admin | zabbix |
| RabbitMQ | guest | guest |

#### 绿盟安全产品

IPS入侵防御系统、SAS运维安全管理系统、SAS安全审计系统、DAS数据库审计系统、RSAS远程安全评估系统、WAF WEB应用防护系统、UTS威胁检测系统

#### MapZone Server Login

MAPZONE Server 是公司自主开发的一套服务型GIS 平台产品,产品基于面向服务架构,提供数据服务发布、功能服务发布、外部服务聚合、定制化服务等功能。

MapZone / MapZone

### GitHub开源项目

在 GitHub 上找带后端的项目，翻配置文件找初始默认的用户名密码

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZCjMVth9Qjia9n2HCEyPM7rJIuYhvwLzKEwQsrcJhM8tvfywyEXvxN7m0T4xNTH5Y6fawLjJpcTjdcOejtsmMVgqW3kwdu2mImHic2Wv7vkhc/640?wx_fmt=webp&from=appmsg)

**-END-**

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Tw9nMcspHZk3JUC8heWAKneleRCqkKZy03kddtZa7UiaJoe7m4ZhNlGbliaRm8qMJ17YMCHhG1RemyRjOgYn9YOw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过