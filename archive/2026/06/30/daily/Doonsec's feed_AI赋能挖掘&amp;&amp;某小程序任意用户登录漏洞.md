---
title: AI赋能挖掘&amp;&amp;某小程序任意用户登录漏洞
url: https://mp.weixin.qq.com/s/LUbinjXR0NLTUxkU8Tg_vw
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:44.167266
---

# AI赋能挖掘&amp;&amp;某小程序任意用户登录漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQrds04SxRLmOutGOcDjhuIEfL9tcQ5iczqN9y3kJ04fkIPiaibvp5icYAbPrUXpMcicAJASrE2qbATfWCoKM0Kgq0kvHticoOgl0Lm0/0?wx_fmt=jpeg)

# AI赋能挖掘&&某小程序任意用户登录漏洞

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于陌笙不太懂安全
，作者陌笙

![](http://wx.qlogo.cn/mmhead/00GYaClAoOo0M6vWibfxlTevuZgVm0LYDLUBfRh5aYicqq4IEibjicq8Ea4RCDIITyYCew89YflS348/0)

**陌笙不太懂安全**
.

web安全知识分享,渗透测试,SRC,CTF,等优质内容分享学习！

前言

圈友的点，拿来学习一手，挖掘过程遇到了很多问题，通过交流也学习到了，很多之前不太了解的内容，交流是个好东西。

信息收集

直接搜索学校的名字，会看到很多学校相关的小程序，我们来到红色箭头这个小程序这里，这个就是本次的挖掘目标

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTibh60gwvqqG65kic00sHvUIsRw8UvzFJQ56vhD5psomjmqmbZWgzkKeFP73GoJ6rpyn8LS6FwWU4lAVZ5WLnib0532sRqbKHWibw/640?wx_fmt=png&from=appmsg)

edusrc挖掘的话，小程序信息收集，直接丢学校名字在搜一搜里面，

搜到公众号打公众号，有小程序打小程序就行，非常适合，天天感觉

自己找不到边缘资产的师傅，直接跳过信息收集，挖就完了。

漏洞测试

点击小程序进行

查看，发现有很多功能，但是都是需要登录的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ29FS8SibgTkzSXIstwF21FFK7yH0icoZpdlMbxXzzia5oVu8aXwI9KxnNQxz4L55KvpR8WneWgPdKyM2WVHJJO7UeGCP19aFR3U/640?wx_fmt=png&from=appmsg)

我们点击登录

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTyrztJAtlccteRY3YGy9gSiaibuNmu8vQhYib2aZE1wxd9WMus8C0NO76WKSI2fh6HxfZicpcGNZypFLdnwoSmwrlYIicUtG6CAnYs/640?wx_fmt=png&from=appmsg)

在点击获取手机号登录，看到了这

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS8hPtozoBYPI9Za4sGjoAsOKyra7Ss9OXRzupM0YZf7aQPX7yUQMMC8DjznSTibicz0Qj6Hic3fVsDglkq7YyOlic3jWtnVPhsicFM/640?wx_fmt=png&from=appmsg)

一般看到这个，经常打小程序的师傅

点击允许拦截burp数据包，可以看到存在这三个参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRUuJkPjvxoVFuKyyM2mQHnTicr2SFTrgxIhrjGremzMgX9ZnPrBKFU8oQuuMYBV7qTwtyjaLCdniarfbI4s0JAVNMvVNMVfMNwo/640?wx_fmt=png&from=appmsg)

## 微信小程序 session\_key 泄露导致任意用户登录漏洞分析

### 1. 漏洞概述

该漏洞属于**身份认证绕过**类型。当微信小程序的 `session_key`、`encryptedData`、`iv` 三个参数同时被攻击者获取时，攻击者可通过解密、篡改、重加密的方式，伪造任意用户的授权数据，从而实现**无需密码的任意用户登录**。

1.1 漏洞标识

| 项目 | 内容 |
| --- | --- |
| 漏洞类型 | 身份认证绕过 / 会话劫持 |
| 威胁等级 | 高危 |
| 利用条件 | 三个参数同时泄露 |
| 影响范围 | 存在参数泄露的小程序及其用户 |

---

## 2. 核心概念解释

| 参数 | 含义 | 正常存储位置 |
| --- | --- | --- |
| `encryptedData` | 微信返回的用户信息密文（如手机号、昵称） | 客户端临时持有，提交后端解密 |
| `iv` | 加密算法所需的初始向量 | 随 `encryptedData` 一同提交 |
| `session_key` | 会话密钥，用于解密 `encryptedData` | **仅限后端存储，严禁返回客户端** |
| `openId` | 用户在特定小程序中的唯一标识 | 后端存储 |

---

## 3. 攻击原理

### 3.1 正常登录流程（标准设计）

```
用户客户端微信服务器小程序后端1. wx.login() 获取 code2. 传递 code3. code + appid + secret4. 返回 session_key + openid5. 存储 session_key（不返回客户端）6. 用户授权（手机号/个人信息）7. 返回 encryptedData + iv8. 提交 encryptedData + iv9. 使用本地 session_key 解密10. 返回登录凭证 (token)用户客户端微信服务器小程序后端
```

这里我们直接使用工具加泄露的iv和key对进行encrypdata解密，发现不太行

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTZOEVOR3PE3P5FkGmhcNAmnqV0WZu7rwJ3CTTT4B9DamrQiaHUUrc8xrh0ggAvAs2ypOalCkYZB1ovsgkj7NYmK81Rl426NJibU/640?wx_fmt=png&from=appmsg)

对key和iv进行解url码

https://www.toolhelper.cn/EncodeDecode/Url

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTIiayxvc6IWOrh3djH14Z8TqyOcg4yMmWXicRyO5F7iaDna3YwY1HYFbiazOnTaUrq4BeovCWv40ggaZ2azOx3sheYa5qJI8xu23A/640?wx_fmt=png&from=appmsg)

发现再次解密显示这个，这里就到我的知识盲区了，这个时候

圈友告诉我这这两个值长度不对，是通过加密或者其他方式进行后期处理的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQOKmgxUkAibSVKTKQloBy0T5xljibiaia3qzXEL7xI2CIvpypPibq4RNCJz2M5Wic3nscicOJxAdNzI7mpyWh2e2xfmatrORhrofbtia8/640?wx_fmt=png&from=appmsg)

## 知识点

根据微信小程序官方文档及 AES-CBC 加密标准，`session_key` 与 `iv` 的长度规范如下：

| 参数 | 编码格式 | 编码后长度（Base64） | 解码后长度（二进制） | 算法要求 |
| --- | --- | --- | --- | --- |
| `session_key` | Base64 | 24 字符 | **16 字节（128位）** | AES-128-CBC 密钥 |
| `iv` | Base64 | 24 字符 | **16 字节（128位）** | AES-CBC 块大小 |

### 2. 技术说明

#### 2.1 session\_key

`session_key` 是微信服务器返回的会话密钥，用于解密 `encryptedData`。其技术规格如下：

* **算法**：AES-128-CBC
* **密钥长度**：128 位（16 字节）
* **传输编码**：Base64
* **编码后长度**：固定为 24 个字符

> **官方定义**：微信官方文档明确指出 `aeskey = Base64_Decode(session_key)` 的结果为 **16 字节** 的二进制数据。任何非此长度的实现均不符合规范，将导致解密失败。

#### 2.2 iv

`iv`（Initialization Vector，初始向量）是 AES-CBC 模式下的必需参数，用于增加密文的随机性。其技术规格如下：

* **算法**：AES-CBC
* **块大小**：128 位（16 字节）
* **传输编码**：Base64
* **编码后长度**：固定为 24 个字符

> **官方定义**：`iv` 的解码结果必须为 **16 字节**，否则解密接口将返回 `IV not 16 bytes long` 错误

这里显然不符合

我们直接对小程序进行反编译

这里我使用无影

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTV8AslFxImq0aZpg7Kiba6VedC93tsRyicbhXm2qibpeJ0BziaWb8DuFpPa7ib2J6wVlHCgJRSnmKpvsPA2LvDTDrO754W0gDhU1Rs/640?wx_fmt=png&from=appmsg)

反编译后，来到源码的文件夹，打开claude，让他来分析

（之前听过一节某大师傅挖掘银行众测的课有个漏洞就是这个，但是他是通过手写脚本手动分析逻辑进行加解密的，ai出来之后迅速拉进了我们和大佬打差距）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTiaFVFnWGPiaibRfT7JavSqwYqecialYutdjuwD0jCX1DZTXdxsgDKcq9XY1BiaLGibmQCFTBQ1ufq8qFCf5WD3LfSwsQp3NDtcflibs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTJ97aSnDND3CBWGYcfvPXbQBhkW96icarSEzoiaNyKeWNDw9LMVsdSogWVWLjWLo61ibDoeMGSFSUqlHUlg74e88UQ30gJtncaibc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSQtzDEHgIA7f01YTRmjkeG7boMhiarsKibpd7QcmFGGXYxImQZ2UK9rHdDkMABgIM6N32xeHUsGtUQDuqmonibLAPlwyQYmicg3As/640?wx_fmt=png&from=appmsg)

这里可以看到，这两个值确实是经过二次处理的，逻辑已经很清楚了

这个时候我们就已经可以给他手机号让他重新加密然后任意用户登录了

但是需要考虑考虑扩大危害

反编译之后这里泄露了两个手机号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQwHFN1ojAdeQAjib27VFic5aWicoFa0R69jkAnSMwFw5x0icHbBFZfhSzkSHTWkACGeLCTVLqBTwmNfOP35VN1OicztYpDfn2v4MAc/640?wx_fmt=png&from=appmsg)

对这两个手机号进行登录尝试，结果真有一个是有管理权限的

让ai对这个手机号逆向加密回去

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ5uEE105lkfgRrtBIaia5ZyNqnL8QaeWPgXmVFib6uRb9CMiciaBQhDvbHENQhy8kWgrtYiadWAknlQ3Eibg9Enzia4GGwFc5KanCC40/640?wx_fmt=png&from=appmsg)

我们直接复制加密后的内容来到登录处进行替换

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQJPGDBGSpZHfrMejyicCXBLibI2VYRiakwbibHhBCh5f3pib8dRjVIMHGhEtRuIdnWicU5JsIeJfOyLvvpTytMPB6T834icdZtAcpxicY/640?wx_fmt=png&from=appmsg)

然后放包，直接进入小管理员的后台

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR9PvicCCM8Dm5iby5HovMRTmyq8ot6pyLW8WEawRMKdMgJlJKgfuajBTc85lzUh50fk3UDI3gica0FN1WTZwKDz8XMc7b6fY5SwM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT3Cr9kwgI4gjwLfbgXmiahzM7DUFfGReibClAVvP4yznUnIa6wr8F4uAIiaBek7RywibtUYXrzbUDPspB6BxfX0nXJDp9Z8xJNL4Q/640?wx_fmt=png&from=appmsg)

这里继续扩大危害

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTXia9zQ321wo0HA6zSRx4sH5LaHqXUUk5FNZzPhNBQGnCudXjUIg48qiaCWJ8FnQhlD6yicPB97FwT6T8oNVibqXbA1x8QTyKgvzo/640?wx_fmt=png&from=appmsg)

点击公寓管理

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRgKjZOchfuka5I3vKgOIAw4kPBuiaIxvfLNicWpMpqV2ZibIEzAnVkmicSJ9WtHAw9q3GpE8MrERcaeTeVMIIWFDnQhrWXABDVciaI/640?wx_fmt=png&from=appmsg)

点击学生搜索抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTsuJHEJQI0lFOQQMYvE5Vt65xkIs28eqk3O9JQGlQOEBl8eUOzyN7rF8f4sARVHdyZUH1vuCqllq8wmWRS26zxp8YFYC5uEmY/640?wx_fmt=png&from=appmsg)

可以看到手机号

这里我们可以通过控制这两个参数

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSmkZwMeu4UyxfcvibCbEEtrIVA23qBKL0eyWEAUhmD0d2qYLR6h3KNzZHpiciccRibgHDU9NI3gBBYdbJxhDbDdENMlYeeULXW550/640?wx_fmt=png&from=appmsg)

对学校3w条学生的手机号进行查看，从而造成3w用户的账号接管

继续查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRePhicArfu9VmpR6vwbs5rhQtsZ2966hq3BN3qPgswDGic4ZDmLSyq2zCyNmOlP5ialhH6rKTPlJ4LatPt8AVmSTeOH0pP4hibzY4/640?wx_fmt=png&from=appmsg)

点击，具体信息进行抓包，可以看到更详细的信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRA9Keax6mhWcWOGJUS6b7x5SOJpsIowWzVIm8rAbSX6YgCvaQicYicnkiaCIzuZSgTrVE9x1NwbqiaicaUee1XTdVpOgJI04TGuSOs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ742S7H2m1ibdKREb2kKPjEL9NTZOqJDqYfVJuZJjlSnXRQK4dtds7RgP2VTqFF5ia2O76txpf9liaeYnYGicr4quer7icwmjiat3Ac/640?wx_fmt=png&from=appmsg)

这里依然看不到敏感信息，但是这是一种很常见的情况，后端返回很多信息，但是前端渲染一部分

我们抓包查看

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTB6Qg7gayveDjWkOUnZHubAyUTNeJSEU3bdrqVZV6ZaIwm5JcLYPSCRic5gYlZ4Kzfc74zrryK4pq3aBOfouDkq8Z6mQZbJjZU/640?wx_fmt=png&from=appmsg)

直接泄露了sfz，也就是说，通过这个能获取，全校3w多条sfz信息，危害加一。

**下面是一则内部学习圈广告😜**

**别着急退，看完的师傅们有福了/doge**

欢迎师傅们加入内部网络安全学习圈子。圈子提供三大板块的内容：

**1**

**网络安全0→1学习路径**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

1. 完整的「30+周安全学习任务路线图」公开，每周任务明确，清晰的学习重点和目标，从入门到进阶，由浅入深，循序渐进；
2. 学习内容涵盖：

* 常见的Web漏洞原理与利用
* 业务逻辑漏洞挖掘
* SRC实战技巧
* W...