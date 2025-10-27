---
title: Nacos未授权访问漏洞复现
url: https://forum.90sec.com/t/topic/2230
source: 90Sec - 最新话题
date: 2023-03-30
fetch_date: 2025-10-04T11:05:04.174009
---

# Nacos未授权访问漏洞复现

[90Sec](/)

# [Nacos未授权访问漏洞复现](/t/topic/2230)

[账号审核](/c/account/11)

[xunfeng](https://forum.90sec.com/u/xunfeng)

2023 年3 月 29 日 02:14

1

\*\*漏洞简单描述：
Nacos是一套帮助发现、配置和管理微服务的程序。提供一组简单易用的特性集，能够快速的实现动态服务发现、服务配置、服务元数据以及流量管理。

2020年12月29日，Nacos官方在github发布的issue中披露Alibaba Nacos 存在一个由于不当处理User-Agent导致的未授权访问漏洞 。通过该漏洞，攻击者可以进行任意操作，包括创建新用户并进行登录后操作。

`https://github.com/alibaba/nacos/issues/1105`

在Nacos 2.0版本存在未授权访问漏洞，程序未有效对于用户权限进行判断，导致能够添加任意用户、修改任意用户密码等等问题。

危害等级：高危

影响范围 : Nacos <= 2.0.0-ALPHA.1

\*1. 漏洞环境查找：

```
直接使用fofa、hunter、zoomeye等公网环境，虽然公网环境的nacos 不是很多。但是存在漏洞的环境还不少。
我这里用的是hunter，title="nacos" 就可以直接使用。
```

[![image](https://forum.90sec.com/uploads/default/optimized/2X/b/b50e8b350ada5ddc9f5edc8a589be1516efa00ea_2_690x491.png)

image1575×1122 79 KB](https://forum.90sec.com/uploads/default/original/2X/b/b50e8b350ada5ddc9f5edc8a589be1516efa00ea.png "image")

\*2.然后使用google hackbar发送数据包：
POC：
`http://IP:端口/nacos/v1/auth/users?pageNo=1&pageSize=9`

[![image](https://forum.90sec.com/uploads/default/optimized/2X/5/59d1bceb0c2e3a463c6824286a72e119287c6076_2_690x405.png)

image1820×1069 106 KB](https://forum.90sec.com/uploads/default/original/2X/5/59d1bceb0c2e3a463c6824286a72e119287c6076.png "image")

密码很慢解密，后期利用方法可以使用添加账号、修改账号poc。此类poc公网环境测试风险比较大。

[SR\_sec](https://forum.90sec.com/u/SR_sec)

2023 年6 月 12 日 03:57

2

太水了！

[Rabbit](https://forum.90sec.com/u/Rabbit)

2023 年7 月 20 日 04:31

3

太水了

[boy](https://forum.90sec.com/u/boy)

2023 年7 月 21 日 02:09

4

![:hot_face:](https://forum.90sec.com/images/emoji/twitter/hot_face.png?v=12 ":hot_face:")太水了

* [首页](/)
* [类别](/categories)
* [准则](/guidelines)
* [服务条款](/tos)
* [隐私政策](/privacy)

由 [Discourse](https://www.discourse.org) 提供技术支持，启用 JavaScript 以获得最佳体验