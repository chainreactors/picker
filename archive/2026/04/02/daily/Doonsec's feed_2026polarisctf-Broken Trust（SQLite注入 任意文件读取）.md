---
title: 2026polarisctf-Broken Trust（SQLite注入 任意文件读取）
url: https://mp.weixin.qq.com/s/APPE6GbW9FPGrI_GskThZQ
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:23:38.461859
---

# 2026polarisctf-Broken Trust（SQLite注入 任意文件读取）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rnM26TMJ5gm8hibo2A3Hic1Z8Mbupa8GcmsG6dc247O0cYNgPhxAMnXKWX1yME6U8WSh7YDOyzlLykS3N9HT0iaianpcw6MaVqJRSM/0?wx_fmt=jpeg)

# 2026polarisctf-Broken Trust（SQLite注入 任意文件读取）

原创

正在思考ing
正在思考ing

正在思考ing

![]()

在小说阅读器中沉浸阅读

# 鉴于上一次长城杯的惨痛教训，我们小队里包括本人在内的两位逆向手开始跟着web手学习

这是本人的首篇web，日后所有web方向的推文都会发在这个新的合集中，原来那个CTF的合集也更名为CTF-Reverse，只推送re相关内容

*题目描述：*

> 某FlaskWeb应用提供了一个仅管理员可访问的备份读取接口。
>
> 神通广大的CTFer是否能发现逻辑缺陷，拿到敏感文件呢

## 前端测试

进入容器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnWUIJDmibYB0ibewxlMl6JIkEm56IyoJ1Alk6icY4RjbH5WMlwyPYEsSG7zklYG0XN5NmJ5ahX4jynvPf9M7vuLRqUAxOC4NQLiao/640?wx_fmt=png&from=appmsg)

就是一个简单的登录页面，输入uid进行登录，我们先随便注册一个，用户名就设置为1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlvVYhNc4unldJgeIomZjTy1tJPv2n2PdRe8fRW7GSA0qkGCHazky6r8hNoUWychCDSGmEOjLAz3M7l6jRIHtKSXgQvLKCCVqM/640?wx_fmt=png&from=appmsg)

输入用户名系统会自动为我们分配一个uid（602007a638f8489ea8c8b0b367d12fee），猜测这个uid是根据我们的用户名生成的

这里尝试了一下设置用户名为admin看看能不能直接给我们生成admin的uid，但是系统提示这个名字已经被注册过了，只好作罢

拿着这个uid就可以回去登录了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlTUic9zbb3icgzdk96wqmhY25GkdWVQjUK6VFPfX1Ga6jfmaast1tTBYeE4qyakDRO5xCchmng5jwBDia0F5wvvJElA9npRyLiaxE/640?wx_fmt=png&from=appmsg)

登录上去后发现只有admin才可以使用backup interface（备份接口），那么我们的目标就很明确了：

想办法登录admin账号（大概率是获取admin的uid），通过backup interface读取敏感文件

我们身为Standard User可以刷新Session Data

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkCxBBuFganWtUkBRQnRsW49iakQBS0ibMAcXb2FWoSPTcwNGtibicS3zopanubOiaSuQqSQ2HOLicGErib8UNcibiamOOM7StpUsXoIpGU/640?wx_fmt=png&from=appmsg)

session中可能存储了uid，猜测系统可能通过session中的uid查询数据库来判断当前用户是否为admin，这里尝试sql注入

刷新Session Data，同时抓包看看

## 抓包&sql注入

## 关于sql注入的详细内容可以参考本人的这篇文章

## [SQL注入](https://mp.weixin.qq.com/s?__biz=MzE5MTc0NDAzNQ==&mid=2247483808&idx=1&sn=3fe8d352dad69a89bae316365b98bd82&scene=21#wechat_redirect)

用bp内置浏览器打开并登录我们刚刚注册的账号，刷新session的同时抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkObTicxcoW3v9byN645n5lw7fSLQnicj94fXDjvH7N7X4lItpiakFUy8uLtbBt7s6ctOYahzPQB3kiaLujBhT0mdXodWefpwOzJfw/640?wx_fmt=png&from=appmsg)

在请求包中我们看到了uid字段，在响应包中我们还能看到role和username字段

接下来就是进行sql注入了

**判断闭合方式：**

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rnMib3vkXPWpaVOE3siaEvn2GTqOuHGyM2saX02I6hxiaNnTibW6zxxRosiavjYqbsjXT5Ab32q6WDXS3PhZTNc6elicC0o2SuepzicrY/640?wx_fmt=png&from=appmsg)

发现用单引号返回"User not found"，双引号返回"Invalid JSON"，由此可判断是单引号闭合

同时还发现#不能进行注释，必须要用--，因此猜测这个数据库不是mysql而是sqlite

**判断表列数：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rliaoZ2gVkGR1FyMlmunDONiapnbYtuJoFB0SciaogUP7EQyomSaPRjQEGx8GjCBLXN0FnoMz3YvDpfUKlxUUSeIic2z3xPku73O4k/640?wx_fmt=png&from=appmsg)

一直order by到4才报错，说明这个表有3列

**联合查询：**

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkGzlbJr5xpPBibicNjGFvMRSAUg7MwibH4w7RlX88l8GKbTPe8JBuFjZwVGyd0Bru4iayqm6uMibpQR8ibcMtdicJ6RUGzIGXUO6Qdiao/640?wx_fmt=png&from=appmsg)

用sqlite\_version()函数确定了就是sqlite数据库，因此我们需要查询sqllite内置的sqlite\_master表，看看这个数据库有哪些表

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rm35pVPzjB7ibibeB7zYZHHNqVZqdTcX1XnGsTPJjia81LibCbhGfujyPgO6SkIDyCnxcmF27cvpY334YZPegolALgLrZSZ13lmcyE/640?wx_fmt=png&from=appmsg)

我们需要重点查询的是sql字段，这样不光可以看到有哪些表，还可以看见各个表的创建语句，从而获得表的结构

用group\_concat()函数将各行拼接在一起输出

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkaorbiadhicuTNHhvOZAiafQzr3KM1w2AgPfXTNowhRacmZJm8ybKbcicq1icicVWu07mmbDxptQXuPIcfPFdbLaAic7eU2eJTS3NVDk/640?wx_fmt=png&from=appmsg)

可以看到只有一张users表，有uid、username和role三个字段，直接查users表role为admin的记录的uid

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmxvqHAZSiauke9tTNDyDRzeqMWubQS0l5Nhx6EzVRbRcbibNRM6MntE7ibeDPbk0SiaxgIYTLc3nAecQOwJUuzoroWhTwicIOBoF9Q/640?wx_fmt=png&from=appmsg)

成功获得admin的uid：247504cc113440479ec92ad1b53f57ed

上面的过程是我参考队里web手的题解，自己做的时候发现使用or 1=1的注入方式绕过查询可以直接获得admin的uid

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmiaB1VFib575vPz4YQDic6ROxdxcajpp7azae44JgFCAIZlWl8rI55z5503k62NjtupO0LVD53FZiajCN94sxEY2ds22AIia1axItA/640?wx_fmt=png&from=appmsg)

拿着admin的uid登录

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmItibOjvM6pAw5WtolHHxarDrUMl8MzeYKX7IVB02NCUiaOslusAaXKn1pg2SX0EibBcV4kT2DEKAZWHtvYHal1N3d3Ug78hH1Y0/640?wx_fmt=png&from=appmsg)

登录成功

## 任意文件读取

点击Access Backup Server

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rknicxuykCKqUL91TCJTIvWyQ9Q1lwJXX16sIagzCcRr1427S04WxmCAIE3Beav3RqhqkMibDK6EqVEia2QX41Psk29mOv27g4QsQ/640?wx_fmt=png&from=appmsg)

发现没有文件，但是上方的url出现了file=config.json，可以确定是GET传参方式，并且想到了任意文件读取漏洞

猜测flag在根目录下，因此构造参数file=../../../flag，发现还是提示File not found，猜测服务器对../进行了过滤，这里尝试双写绕过，构造参数file=....//....//....//flag，访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkfBnwYIkXia9L0JHM9p3sHEDEOlHNbB8ib0Wtb7lR6VwnuR3rA8m8DmibM7gQlqzeIT6bGWiaxVA3ibQTib1ZribeHCa1lqcrwKx4KRg/640?wx_fmt=png&from=appmsg)

成功获得flag：

XMCTF{63fd8758-9382-4011-876f-650de7a3cbcb}

有没有哪位师傅知道为什么直接采用or 1=1的注入方式绕过查询可以直接得到admin的uid呢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_33@2x.png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

正在思考ing

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

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