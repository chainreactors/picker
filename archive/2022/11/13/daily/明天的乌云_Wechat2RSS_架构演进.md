---
title: Wechat2RSS:架构演进
url: https://blog.xlab.app/p/a207c8e3/
source: 明天的乌云
date: 2022-11-13
fetch_date: 2025-10-03T22:38:06.824874
---

# Wechat2RSS:架构演进

[明天的乌云](/)

透明人博客

* [首页](/)
* [分类](/categories/)
* [归档](/archives/)
* [日报专栏](https://daily.xlab.app/)
* [我的推荐](/links/)
* [友情链接](/friends/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [1. 第一版](#%E7%AC%AC%E4%B8%80%E7%89%88)
2. [2. V2:远程管理](#V2-%E8%BF%9C%E7%A8%8B%E7%AE%A1%E7%90%86)
3. [3. V3:访问速度](#V3-%E8%AE%BF%E9%97%AE%E9%80%9F%E5%BA%A6)
4. [4. 服务迁移](#%E6%9C%8D%E5%8A%A1%E8%BF%81%E7%A7%BB)
5. [5. V4:Cloudflare](#V4-Cloudflare)
6. [6. 开源](#%E5%BC%80%E6%BA%90)
7. 7. 相关文章

![透明人](/images/logo.png)

透明人

Tmr Blog

[197
日志](/archives/)

[33
分类](/categories/)

[159
标签](/tags/)

0%

链接

* [透明日报](https://daily.xlab.app/ "https://daily.xlab.app")

# Wechat2RSS:架构演进

发表于
2022-11-12

分类于

[其他](/categories/%E5%85%B6%E4%BB%96/)

阅读次数：

本文字数：
859

阅读时长 ≈
1 分钟

[Wechat2RSS](https://wechat2rss.xlab.app/)作为公开免费服务运行[差不多一年了](/p/55546dec)，大概讲讲是怎么做的

目前RSS大概有两种模式

一种是比较常规的，放一个静态文件，更新内容的时候去更新这个文件

一种是类似[RSSHub](https://github.com/DIYgod/RSSHub)，通过传入参数，动态的去抓取资源，生成RSS的结果，通过控制缓存来控制刷新频率

## 第一版

第一版用Node.js写的，生成RSS的xml文件，用Nginx把静态文件放出去，然后用Telegram Bot把日志之类的传回来

![](/p/a207c8e3/v1.png)

主要考虑这样会安全一些，没有动态内容暴露出来，而且微信公众号的更新频率不需要太高，本身就只能一天一更，没必要做太复杂

最早这个服务是在境外VPS上跑的，随着RSS数量增加，微信开始有一些限频的操作，需要过验证码，不想费脑子去自动过验证码

后来发现可以手机上过，但是VPS网络和手机网络不在一个地方，经常过不了，然后代理到VPS出口网络就可以了

## V2:远程管理

这样用了挺长时间，但不时会有增改公众号的需求，总是上服务器改也挺麻烦的，后来给Bot加了些功能，可以通过Bot来增加公众号

顺便用Go重写了整个服务，部署起来更方便了

![](/p/a207c8e3/v2.png)

## V3:访问速度

RSS是通过Cloudflare暴露出来的，有些地方打不开，访问慢，后来了解到[Vercel](/p/66242742/)，在国内访问速度非常快，把xml文件推送到Vercel上，就不用Cloudflare了

![](/p/a207c8e3/v3.png)

## 服务迁移

其实到这里对VPS的要求就不高了，没有直接的对外服务，完全可以在内网运行

随着VPS到期，把这个服务转移到了我的旧笔记本上跑

## V4:Cloudflare

随着越来越多的人使用，Vercel的免费流量开始不太够用了，被迫又套上了Cloudflare加一层缓存

![](/p/a207c8e3/v4.png)

## 开源

这个世界还没有一个self-hosted的微信公众号转RSS的解决方案，我开源岂不是第一个

这个架构部署使用起来比较麻烦，对Telegram Bot有强依赖，用来登录和管理数据，做纯web管理我也想，但没动力/前端做hhh，开源或许有人可以来做

但是我对微信RSS有强需求，比较担心开源后爬微信的这个渠道会被封，这是对开源最大的顾虑了（垃圾代码是第二大）

## 相关文章

* [Wechat2RSS: self-hosted版本发布](https://blog.xlab.app/p/fd57c4cf/)
* [用RSSHub替代Feed43](https://blog.xlab.app/p/1209a846/)
* [RSSHub规则化架构设计](https://blog.xlab.app/p/9c76cef/)
* [Wechat2RSS:更新频率策略设计](https://blog.xlab.app/p/d73537b/)
* [先知社区RSS](https://blog.xlab.app/p/6041ed53/)

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[RSS](/tags/RSS/)
 [微信公众号](/tags/%E5%BE%AE%E4%BF%A1%E5%85%AC%E4%BC%97%E5%8F%B7/)
 [Wechat2RSS](/tags/Wechat2RSS/)

[浏览器版本识别](/p/d42eb783/ "浏览器版本识别")

[Wechat2RSS:更新频率策略设计](/p/d73537b/ "Wechat2RSS:更新频率策略设计")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2025

透明人

站点总字数：
343k

Theme NexT works best with JavaScript enabled