---
title: Blinko plugins路径遍历漏洞存在任意文件读取漏洞 附POC
url: https://mp.weixin.qq.com/s/G3nX_Sk5SNhT-JM_uCrEJQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:32:28.425019
---

# Blinko plugins路径遍历漏洞存在任意文件读取漏洞 附POC

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6zr4tib1P8ZSBLhTNUbGZWKldAGl5YeToN7an4NLRqUkd0zv6DF6w672xAL85M5clibah70zeR7M3mWGXhXBfib2CbBzcFsZ8nQJM/0?wx_fmt=jpeg)

# Blinko plugins路径遍历漏洞存在任意文件读取漏洞 附POC

2026-5-11更新
2026-5-11更新

南风漏洞复现文库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

#

免责声明：请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息或者工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果与文章作者无关。该文章仅供学习用途使用。

## 1. Blinko简介

微信公众号搜索：南风漏洞复现文库
该文章 南风漏洞复现文库 公众号首发

本人只有 南风漏洞复现文库 和 南风网络安全 这两个公众号，其他公众号有意冒充，请注意甄别，避免上当受骗。

Blinko 是一个开源的 AI 驱动卡片笔记项目

## 2.漏洞描述

Blinko 是一个基于 AI 驱动的开源个人卡片笔记系统，支持知识管理与 AI 协作。其插件文件服务器端点在处理文件请求时，使用 join() 函数将用户提供的输入与插件目录路径进行拼接，但未对拼接后的最终路径进行边界校验。攻击者可以通过在请求路径中构造 ../ 等路径穿越序列，绕过目录限制并读取服务器上的任意文件（如系统配置、环境变量等），导致敏感信息泄露。

CVE编号:

CNNVD编号:

CNVD编号:

## 3.影响版本

Blinko <= 1.8.3
![Blinko plugins路径遍历漏洞存在任意文件读取漏洞](https://mmbiz.qpic.cn/sz_mmbiz_png/b9KQYsB8q6zEmzwSBDMas2ItOENyUcRs57b3aEdvM3Obpta7ovKdUlXduDbc5SI3neD8Op801b679hQjI0t4hgI0KV3aCpMLb4lOIj3I5yc/640?wx_fmt=png&from=appmsg "null")

Blinko plugins路径遍历漏洞存在任意文件读取漏洞

## 4.fofa查询语句

icon\_hash="-1446811182" || icon\_hash="-717082057"

## 5.漏洞复现

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6w9CJ50Ew4zlUokPF09e38egTicxIwgxFmkrEticx0boCiagpicyiav5dMyY8tHXvg9hySgFWn78ne5JBX6sj5JCGwC8oVMNV36GO60/640?wx_fmt=jpeg&from=appmsg "null")

## 6.POC&EXP

本期漏洞及往期漏洞的批量扫描POC及POC工具箱已经上传知识星球：南风网络安全

1: 更新poc批量扫描软件，承诺，一周更新8-14个插件吧，我会优先写使用量比较大程序漏洞。

2: 免登录，免费fofa查询。

3: 更新其他实用网络安全工具项目。

4: 免费指纹识别，持续更新指纹库。

5: Nuclei脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6wbuvviaicT9N80r8c8HX9SqMxYicXH77bEALZUBc8U792tqLM5OSj1js5kQCiaP9xnicee9HYF2nnicZM6DUPAFbtWLicmcTsiaDSicry0/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b9KQYsB8q6zJrBX0XEnib0BdDjr8mK0JqGxwz5u1j0eQNibmcA7LY9R2wdWZo9U4ib8fRc4Gvibic3hTXjaZHuMyldia6HF3DuMQL0ZrOTlfSCdUU/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xF6pKphqIcr6AXb2F6LRCJzD7IicXBK6N8NK9VkiaNFGtfu29vG9fQicI04zBaMnEF24YgiauCl3uHkEfkmLLDZNHqDbwqcbpgHRc/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6wpTTic8AMxo1JVtibMnvIZPZxkiapfWDquH55w4HNCGYbGhS5eeibcc0iaApia1PABN26aX2muhhPtTic5IYXLKQGYZFauNU22rre7zE/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xV9abicPdEic2ncBl7Mibd6N2eEf8GRLkoicPI7B6LHL2LbOOeIvnFGVnnXwI6UJmA2ou9vcnTpxXJVJI7PYlfriaEKaxIWqPtgOz4/640?wx_fmt=jpeg&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/b9KQYsB8q6xAiaa86PsZ1PRCkZyyQ1BUMF9pDyZNa52WCQ0voIo1DgicU9zEFMLZwghqeAmB5seLc7ltR710Ggibxs5eYB8tBiaynIR43WZ3r1Q/640?wx_fmt=jpeg&from=appmsg "null")

## 7.整改意见

建议您更新当前系统或软件至最新版，完成漏洞的修复。

## 8.往期回顾

[Blinko &lt; 1.8.4 路径遍历漏洞存在任意文件读取漏洞CVE-2026-23482 附POC](https://mp.weixin.qq.com/s?__biz=MzIxMjEzMDkyMA==&mid=2247490396&idx=1&sn=8014917ec87f3398e6f838482bedecb4&scene=21#wechat_redirect)

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