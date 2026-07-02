---
title: 该转战 codex
url: https://mp.weixin.qq.com/s/4iaJFF9irEvblfocb22BAw
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:53:08.621057
---

# 该转战 codex

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVnLJicnMWU0Fia6kc1QqLuBs3sEWFE23JiapCn7uOaW5ayTtVJYATHzPmyhJZpab6d20PtdM5EKhVDVzicw3xbtEWicpA9ibDCYURfNM/0?wx_fmt=jpeg)

# 该转战 codex

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 608，阅读大约需 4 分钟

## 前言

之前用 TRAE CN，后面迁移到了 claude code，但没想到 claude 最近又出了这档子事情。

不过，以 Anthropic 的情况，只能说是早晚的事情。

国内的大模型不是不能用，像 glm 5.2，qwen3.7 max，deepseek pro v4 不是不能用。
不过 deepseek 过段时间，要搞波峰波谷了。
智谱的 GLM 是 coding plan 抢不到。

## codex

codex 有 desktop 和 cli 两种。

![759a714ca24f2b997db591865e96446f.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkZ2yibrqQ7cAEw0gBfAPJYOjd7ODwichnzNiaL2Y6XFFBOAjMEhHnC1piaia97qjB075oDbvLpyGgTCuiaQgwNZw61XSB7sGeHicuVyQ/640?from=appmsg "null")

759a714ca24f2b997db591865e96446f.png

![c61c96c65561adf47ea207f95c7d5414.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVko4l7jKyz636kpiakz4CQ4h5H4FFHJxvMme9siceNNibw6dlu7RdsvgIicQ2MpRqlmNOic1ru4Y1220icq7PoIWf8JbCib5Ul6EECrDY/640?from=appmsg "null")

c61c96c65561adf47ea207f95c7d5414.png

codex 命令行形式，和 claude code 差不多，基本可以无痛迁移。
有 cc-switch，搞中转或者配别的大模型 key 也不是难事。

## cc-switch

虽然叫 cc-switch ，但 codex 也能用

配置 deepseek 的 api key 的话，需要开启路由
![fffa03417d2ffe7869085984c5562681.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVm25qTiaUV9xEYhWrHpJ8xnBmkRhJELZJCiaw4fnTPnn02QQDqxIN2FcZ93ia4gI5oNWcq2lhWygUWbPY3wNNqBkcbdb0e2nahTAw/640?from=appmsg "null")

fffa03417d2ffe7869085984c5562681.png

配置
![fd1d988b7e0f537493db83c63c2b7a53.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn8bicvHt8zDQ9jNm2nBsMW9tOICUo2BT2zGhDtDfqVtdMSf4ykVkfMMRdcqVtXlvia2ibbHmE3PrcjM9nZmiaIsECSNEyN5W8ibb1s/640?from=appmsg "null")

fd1d988b7e0f537493db83c63c2b7a53.png

命令行运行 codex

```
claude --dangerously-skip-permissions
```

codex 中也有类似的命令

```
codex --dangerously-bypass-approvals-and-sandbox
```

![003bf801b68d2b36dc40ff24c4d13793.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmBrl8yC2doxrgSe8NvTPOsubLojUfrTpmxYZ95JUPaSdtkrOm8GnOFbKcMcNqNITJTMunTrLbWaO3ZjWxGplCh5RnaBRtxIQw/640?from=appmsg "null")

003bf801b68d2b36dc40ff24c4d13793.png

也可以直接在 codex desktop 当中使用
![7a74f156217a3534f74e806c106efe1f.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkicdJNnV0tiaXtAGSZdQt1lSTQL4jRVbMlLibiaFkWbbCNIicayRIMGauhWE1bhXWc7wAwBv5dM6qAZHOiaOicDAFSqSs2MYDUbEGOxQ/640?from=appmsg "null")

7a74f156217a3534f74e806c106efe1f.png

## gpt 封号的问题

在不同的群里都看到过被封的问题，也有师傅私信问我这类的问题

如果有条件，可以去做一下 GPT 的 TAC（trusted-access-for-cyber）认证，如果通过了，会好很多。

如果不想做认证，有几种选择。

### 慢慢引导

一种是慢慢引导，先让 GPT 不涉及危险操作的行为，比如分析代码当中的路由信息

```
分析源代码，获取该项目的所有路由，并告诉我哪些可以无需认证即可访问
```

![a11c7fac0b3c33d9f2207bba8c9631b7.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVltje0d5WWZL4wQp52NRZMAZ6fsbuibaabIrjQmgfZfeDfpFUAaAYSkgx6PMTNLRjWPQTlIWOzTELDl1kibD58gicNZRJU9NOhbZk/640?from=appmsg "null")

a11c7fac0b3c33d9f2207bba8c9631b7.png

```
接着分析这些路由里哪些到后面的调用链中存在fastjson，并且分析项目中有没有fastjson反序列的风险
```

![dcbb71fa7f761e6fb0ce900fa2ce720a.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnbL7ffT02GGtS13jaNX0qSaBe5GZbyCicWltliaUlZcDDyIEI6w5oOZDW3ZxnqdU7Bhk7SK5rkmiaSu261NgOlVVoaMb7j8IVtnw/640?from=appmsg "null")

dcbb71fa7f761e6fb0ce900fa2ce720a.png

```
分析上述路由中，哪些与数据库交互的地方，存在SQL注入的，定位到代码，方便整改
```

### GPT 越狱

老实说，不推荐。
一个是越狱有时效性，一般公开的，用不了多长时间。
另一个，GPT 难道没有办法知道谁越狱了吗，用的多了，自然有风险。
最终回到那句——用别怕，怕别用。
如果是自己的号，能不用就尽量不用吧。
是那种日抛的号，那随意。
如果是中转的……
![33a94425c1c2a06d3a4c6b9ce5d7ca7d.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk6UevMQm5E6FqVAuicyc25lkC31HwLQmbMicYnuEKpTpMSjIIlUzzia14Z6NZqdYEBo9aDlYpFlpEwriaH9YuZO17RpeIAsInOHw0/640?from=appmsg "null")

33a94425c1c2a06d3a4c6b9ce5d7ca7d.png

越狱项目：

* • Codex CLI 破甲工具（GPT-5.5） — 注入无限制模式系统指令，关闭所有内容过滤器。 https://github.com/lingbol088-spec/Codex-5.5-codex-instruct-5.5

**利用官方配置机制，不修改二进制、不劫持网络、不篡改进程。风险自负。**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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