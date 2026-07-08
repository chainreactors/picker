---
title: 意大利国家民航局数据泄露：近9000条用户记录及后台数据库曝光
url: https://mp.weixin.qq.com/s/tagUj9Noq-B72pxjhEkFRA
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:02:05.814114
---

# 意大利国家民航局数据泄露：近9000条用户记录及后台数据库曝光

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iaNqLNrWSicIrBUHzvibAuuTQPa8SCmhIDG9uvcrXztTAvakOqXaBPjnSHKib591cegNwFYc6QmZmVLIg91icKa7GiaJxISJtepVY4wESISemjG6E/0?wx_fmt=jpeg)

# 意大利国家民航局数据泄露：近9000条用户记录及后台数据库曝光

原创

暗网哨兵
暗网哨兵

暗网哨兵

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年07月06日，暗网中出现一则针对意大利国家民航局（ENAC，Ente Nazionale per l'Aviazione Civile）的数据泄露帖子。发帖者声称获取并公开了ENAC数据库中的部分内容，共包含6个SQL文件，其中核心数据库文件为enac.sql。根据帖子描述，泄露数据涉及约8,890条用户记录，主要来自用户信息表，包含身份信息、账号信息及认证相关字段。发帖者还宣称已删除目标数据库。

![](https://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIrlYmXH9CP8mQMiaTIQoAiaMcmpBNjBrjg4LHXmHJq8UiamPicRXyBUhz8ibxh2RFyE3yIkibAou7DOaT1hVoGVvzdSx0taucBLg6hN0/640?wx_fmt=png&from=appmsg)

泄露的数据详情

根据帖子介绍，泄露内容主要来自`users`用户表，涉及字段包括：

* 用户ID（ID）
* 姓名、姓氏
* 第二姓氏（Second Surname）
* 用户类型
* 用户名
* 出生日期
* 电子邮箱
* 邮箱验证状态
* 密码哈希（Password Hash）
* 存储密码字段（Stored Password）
* Remember Token（认证令牌）
* 公司ID
* 用户组ID
* 创建时间、更新时间
* 税务识别码（Tax Code）
* 所在城市
* 使用语言
* 性别

此外，泄露包中还包含多个与phpMyAdmin及数据库配置相关的SQL文件。帖子附带了部分数据库记录样本，展示了用户账号、认证信息及相关字段结构。

泄露主体简介

ENAC（Ente Nazionale per l'Aviazione Civile）是意大利国家民航局，负责全国民用航空领域的监管工作，包括航空安全、机场管理、航空运营审批及行业监督等职能，其职责类似于美国联邦航空管理局（FAA）。根据帖子描述，此次泄露涉及的是ENAC系统中的用户数据库及相关数据库文件。

历史文章

[近期暗网重大泄露事件概览【20260706】](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485809&idx=1&sn=f838f5ffee79570ddd5b70aebb38254a&scene=21#wechat_redirect)

[苹果iPhone 18 Pro 被“扒光”，630GB 数据暗网曝光！](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485760&idx=1&sn=05672ad9750392031b74656e60a78fff&scene=21#wechat_redirect)

[DarkForums近10万用户档案与42万条IP关联数据遭整合发布：用户画像、历史IP及论坛资料被汇总](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485664&idx=1&sn=16eba98c80ccd85197b7b31ab3085258&scene=21#wechat_redirect)

[近期暗网重大泄露事件概览【20260701】](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485709&idx=1&sn=b8ea623f288f7fd704b2b87cd3319831&scene=21#wechat_redirect)

[1932份内部文件外泄：俄罗斯顶尖工科大学竟成军事与情报人才“输送工厂”](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485652&idx=1&sn=2f9f67ab8663ee258d6926a5d9e11efb&scene=21#wechat_redirect)

[超11.46亿条叙利亚公民与Facebook账户关联数据曝光：手机号、个人资料及社交账号信息遭汇总泄露](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247485636&idx=1&sn=922229c51a9f9e504ac2e1462506232e&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIoKCZpzLFy6Lv0ZLtm3yVKpcu7MUQ1jGIPUYwK0HIP9moPpP2Wpcddib6TnCZFIUbTX2zUlG2pOY9tVHEaAqChbz6SqeMFxmk4Q/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=15)

我们的服务

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIozRSJllZibFoNoFmkxpYb9fgAk2zBn6ic7WkSvNL2RC7aib8FJKBLMqdc4ZRjvh1wk1cJ4qia3VodLicicrfwgp5FdJdFdcaicC57HuE/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=16)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBOjLcRoq5z6HJGh2YFWNrGpT2OCnicLfK2icJCTPNlutcb2gVia57NfRqrhN8KcI7NI4A16MZyY7zHrIiawZJ032vs7yqLKiapr5fbQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

***01 **暗网监控与风险预警*****

7×24小时持续监控全球暗网论坛、数据交易市场、黑客社区、泄露平台及地下渠道，及时发现与客户相关的数据泄露、账号泄露、敏感信息曝光、勒索软件活动等风险事件，并提供预警通报与分析服务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBMXUKEibMPGptpmTfDG2hHvFy9t5aziaf6ics8ffhLv9uPHWnUKINx7HBD0fFdsMFS4fXb9FEOjWEqyicGEFZQggbnwOa8Pc43ZrPg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22)

***02 **定向数据采集服务*****

根据客户业务需求，提供定制化数据收集与整理服务。支持：指定网站数据采集，指定行业数据采集，指定国家地区数据采集，以及其他相关数据采集服务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBOOhYOtiaZoc57SOOribQLoLehLt5UDV9fct4m2zg4SFVmicYCCuJ2Cw99UTFEwBsWHuvWvBxkic7MjOIiavlvUfXXDh9maNib3M6T5o/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

***03 定制化情报服务***

针对客户个性化需求提供专项支撑。例如：舆情监测、目标画像分析，行业情报研究。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIqlYFDUQZ21c13E7A02tJQOBxiaemq4Xe7icD9VQ6dt2YQKaT2keyNSLu9icGR1TKwUcEtwGZ0M5lFNiaJHrjTvocXGQuPBZfD4YOg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=31)

**内部社区交流群**

**加入方式**

![图片](https://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIq8UKNtdicNibk0aO8k25UAedlB0QtCSMDBPTOwzaDFQ8GgEqgKQxnbRFkHiaGia9grNCFF3EBaJBdnfC1o4vD0JaOYfRdsRhE1Vog/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/HaJr68L1tTTyCC8O1Oa7QCNiaQwscfJqPCZib6GkcFrg9UiazicTe9PZdDEwZ111UTxdTXXrgeUzibuo6AQiaMuKTpNg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

点点关注不迷路

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIrrWGp3fibB8Ya39P5JtKp5ADwdziakKyGLkbVsT6BUht87anj0zvgkFtYt7XPJ7tFsQsQ0AdQnRdqDngo8RAfmTuqTjNicwawvjM/0?wx_fmt=png)

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