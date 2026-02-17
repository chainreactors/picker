---
title: Chroma DB存在swagger敏感信息泄露漏洞 附POC
url: https://mp.weixin.qq.com/s/d3qPOLz46w46Z82WomfYHQ
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:14:04.920126
---

# Chroma DB存在swagger敏感信息泄露漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xCRQVnCicqvmnVGXXlib79oS5BGmYWUl5ZrJfRgfNnG008ysoVJDicLG7nTQh3ia6oFRRef4jbXmSr0fTG2cuLwI6D5UqMfe0iavQY/0?wx_fmt=jpeg)

# Chroma DB存在swagger敏感信息泄露漏洞 附POC

2026-2-16更新
2026-2-16更新

南风漏洞复现文库

![]()

在小说阅读器中沉浸阅读

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. Chroma DB简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

Chroma DB

## 2.漏洞描述

Chroma DB存在swagger敏感信息泄露漏洞

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

Chroma DB
![Chroma DB存在swagger敏感信息泄露漏洞](https://mmbiz.qpic.cn/mmbiz_png/b9KQYsB8q6xeSBhtUzUib93iapQu8cP5GGY613b2uEr5ZWM7wSMJxywt3IXl3rqCPk6YUp0aHfshB3ZyGUIiarHakkOD2Qu0SaPxb9KN81uS38/640?wx_fmt=png&from=appmsg)

Chroma DB存在swagger敏感信息泄露漏洞

## 4.fofa查询语句

Chroma

## 5.漏洞复现

漏洞数据包：

api/v2/tenants/default\_tenant/databases/default\_database/collections

api/v1/collections?tenant=default\_tenant&database=default\_database

docs/

openapi.json

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xVibLRxumAD4Of4iagflOsql4zojdEqfWX0or3FbYgbhbDVjUd3W6YecOMGHBONBeiay1EfGT2OU2Az1tabdWicwNRuVNaAeuCsYM/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6zqAKdjhE1oYkjsaCQMRNjgicHzAujhzY0b6StGgUw3QW5nhH9RNgx08T2TWCSXrtAl8H4icKY54TomkYqhrQaZiciccZGTlSzDkl0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6z3crqhCxCvPvBS0aBAiaoz8tc0shy7edOKaHb9PBByFdVhNyZVdsJgcaicNiaIuJDGqo060LELH2OSEXBFwjd1l30dWMpZibDHXTs/640?wx_fmt=jpeg&from=appmsg)

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zBu0J3YRBPTib0jAftsv6R7sTic0jibbgicHW1ItBTd5OHI4JB5RJs8LOvFzn8Y6xThPM7AcT0Guzzzq0SUqnOjChTO3ibWoMmR57E/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wwGRFu6RDmxQibzG5Sq5UeqbBOg97BzBEygHxYdvxcG4DNaEzDLsEqQ2dgictia5NaHcpgba5oMlJicxzl6OkAq4FyX46Cnrk7icqA/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6yB5Xb7kBODVEfCrcRbibYygRSlLn2oh3HbDmg5Oib9VNt1Dic4dMh4E3eWhFAhZBo4NU27vUqq3BicTOreHoniaGp34Z66u96ad8hY/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6woZHd9iavOWic7u47H6iceiaqS2iaWoqmiaWbtUVasPibjRGJzGGKTj5XwicPqjeMqH8zhgLhOHmUtD3Pfjxy9ibFafSicVICQGUY7yDTns/640?wx_fmt=jpeg&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6xVax8TVxYHYvf6NLyQVK9JgIr6Ma1N5n2ypkazSEaXbcNdVKVPg1rE9S2DgXpg506rNQwOwc6rZ08M5j473KVJP2okBS8Wwq0/640?wx_fmt=jpeg&from=appmsg)

## 7.整改意见

打补丁

## 8.往期回顾

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