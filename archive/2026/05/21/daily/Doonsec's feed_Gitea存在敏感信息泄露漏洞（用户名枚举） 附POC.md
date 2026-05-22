---
title: Gitea存在敏感信息泄露漏洞（用户名枚举） 附POC
url: https://mp.weixin.qq.com/s/rdsK-2f8_bZiY2Kqcs2JUA
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T05:57:47.683718
---

# Gitea存在敏感信息泄露漏洞（用户名枚举） 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6w7PUtOoyepnnEyJcdEhZ16IOFY7FCp05j5xJvNibQ5MVR594VtWyLkFHTicmLBQxxNgzlYAh7S9GA88yH7kB4xtfPVFDOye7tAM/0?wx_fmt=jpeg)

# Gitea存在敏感信息泄露漏洞（用户名枚举） 附POC

2026-5-21更新
2026-5-21更新

南风漏洞复现文库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. Gitea简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

Gitea 是一个轻量级的 DevOps 平台软件。

## 2.漏洞描述

Gitea 是一个轻量级的 DevOps 平台软件。从开发计划到产品成型的整个软件生命周期，他都能够高效而轻松的帮助团队和开发者。包括 Git 托管、代码审查、团队协作、软件包注册和 CI/CD。它与 GitHub、Bitbucket 和 GitLab 等比较类似。Gitea存在敏感信息泄露漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

Gitea 是一个轻量级的 DevOps 平台软件。
![Gitea存在敏感信息泄露漏洞（用户名枚举）](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6yNFUCYgwHSVicCib6IicLKNJBia5Kx61yhic4icLhia5d5IvPAJwViahFMMYyMzCxatFPnLsl4rLmj51cgicNJnYZ17Bnzjvwu3oFUbt7I/640?wx_fmt=png&from=appmsg "null")

Gitea存在敏感信息泄露漏洞（用户名枚举）

## 4.fofa查询语句

title="Gitea"

## 5.漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yGHib8oIJTE6f7X4knd6lNlKZFv8PmLyJiajjnONicek2SkIQCcKSBKlgic1xibmdBD1MEa6fcABhuq0ibiculk79Zcttz4h4xcwCkb8/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

5: Nuclei脚本。

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6x5ib7CgGox8XB0icSMIc0N2wUNImxpUVPHrtLTPNiaJNDZKYEY2U6Ja0Zy00ptia9Zv6M8QgZ49UDnsyiaMSxK9zicz6BuZKIrXdQLw/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wW7jb118vf6rHGiaqLXW0qtDkIxnF1G8MOPp6CEcj39Bzp0qViczPBbeWyGWnLEhicIuIuv7EOicVthJibjd6WZ3icTwrtJichrcHfok/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zO17qQCbicykM84zI5gA6Pllz4uT7zDrQB3KHNhDpgwCkh4xgPjAribocXAtyXHOuibbz2INDjaib63gN3iaWkPmG9HibA51eLaAjP0/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wA9a2CVDHZ27uZqiamdFZWQQOib3do8uiclQhFUPU1Ot0t09hiajT8bTwpA6tgs6zL5Vicm4Ly26EWp74MvicbkbqUqO9grSywR5MGg/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wv5Q7FFbSey7NSwPWLow4PX6lkV7rylZ4UwexhrOu9rhqdI3JznYzMicncFRfhJTvIjydI8v1yHSypHdvTSjsAkpC6XOYu3gOA/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wFwXo8LPegTCHr3NImd3gpffau3ia8qlL47nkwzIMQcXdpDgOHTd5xVeIA6vnhu69GvxZZdCY17KSDTbfJvwiaIZYWiaJkmdic4WM/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

打补丁

## 8.往期回顾

[友数聚科技CPAS审计管理系统V4 doDownLoadPicFile接口存在文件读取漏洞 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490481&idx=1&sn=a8a3dd298765d8146cbe53476ee81659&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HsJDm7fvc3a95GFchUA48sGQuaFpFPPmL593YvcFo4IPeV2QPL2L72h5t4ibNq9IyXI9GmRWmvV2eh8zo3ldtmg/0?wx_fmt=png)

南风漏洞复现文库

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HsJDm7fvc3a95GFchUA48sGQuaFpFPPmL593YvcFo4IPeV2QPL2L72h5t4ibNq9IyXI9GmRWmvV2eh8zo3ldtmg/0?wx_fmt=png)

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