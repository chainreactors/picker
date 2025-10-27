---
title: RSSHub规则化架构设计
url: https://blog.xlab.app/p/9c76cef/
source: 明天的乌云
date: 2023-03-31
fetch_date: 2025-10-04T11:15:05.007973
---

# RSSHub规则化架构设计

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

1. [1. RSSHub](#RSSHub)
2. [2. RSS-proxy](#RSS-proxy)
3. [3. 缝合](#%E7%BC%9D%E5%90%88)
4. 4. 相关文章

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

# RSSHub规则化架构设计

发表于
2023-03-30

分类于

[RSS](/categories/RSS/)

阅读次数：

本文字数：
1.3k

阅读时长 ≈
1 分钟

最近Feed43凉了，替代品似乎也不多，为什么不能把RSSHub变成Feed43呢

> 2023.8 更新
> 给RSSHub提了[PR](https://github.com/DIYgod/RSSHub/pull/12882)，实现了相关功能，成功将自己数十个Feed43迁移到RSSHub
> 文档参考 <https://docs.rsshub.app/other.html#zhuan-huan>

> 2023.5 更新
> 在RSSHub开了个讨论贴 <https://github.com/DIYgod/RSSHub/discussions/12204>

## RSSHub

<https://github.com/DIYgod/RSSHub>

曾经也给RSSHub贡献过一点代码，大部分的路由实现的套路都差不多

1. 从网页/API接口上抓取数据
2. 根据一定的规则，提取RSS需要的字段
3. 构建RSS

其中最核心部分有两个

1. 从哪里获取数据
2. 数据如何转换成需要的字段

核心部分都是通过js代码实现，想要支持一个新的RSS成本比较高

装环境，部署调试，提交pr，pr合并，更新自己的RSSHub，订阅新的RSS

有很多很多次，我想加一个RSS，都是因为这个功能Feed43也能实现，只要在网页上点几下就能制作好，而放弃RSSHub

这其实也不利于RSSHub的发展，扩充支持站点

## RSS-proxy

<https://github.com/damoeb/rss-proxy>

是一个比较理想的Feed43替代品

获取数据的地址和提取规则都是通过url传递，实时处理

增加新的RSS成本很低，但处理规则没有固化和分享

## 缝合

为什么不把RSSHub和RSS-proxy结合起来呢

将RSSHub处理路由和提取数据，参考RSS-proxy的模式，规则化

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` 1. 输入地址 2. 链接转换成对应的API接口 3. 发起网络请求 4. 根据规则提取数据 5. 输出RSS ``` |

举一个例子

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` 输入 https://a.com/users/ttttmr 转换成 https://a.com/api/users/news?user=ttttmr 发起网络请求，拿到json数据 提取数据   - .items得到数据列表     - .title得到标题     - .link得到链接 然后构建RSS ``` |

结构化描述步骤2和4，就是一条规则

RSSHub引擎负责执行这个规则就好

而且2中规则还可以复用给[Radar](https://github.com/DIYgod/RSSHub-Radar)，来告知哪些可以订阅

这样新支持一个RSS会非常简单，把规则随便扔给一个实例测一下，没问题就可以直接用了

用户的实例订阅官方规则库，自动同步更新

* 关于规则如何定义和实现

可以参考XPath，CSS选择器，正则表达式，JSONPath等，或者[cel](https://github.com/google/cel-spec)

RSSHub自己定义实现也不是不行

* 关于路由实现

比如在同一个url下，可能存在多个api，也就是多个规则

可以规则定义一个名字来区分，来实现区分订阅比如`用户投稿`和`用户点赞`，类似

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` https://rsshub/feed?url=https://a.com/users/ttttmr&type=post https://rsshub/feed?url=https://a.com/users/ttttmr&type=like ``` |

获取url参数，根据host过滤规则库，在规则库中遍历执行规则2，匹配出合适规则

根据type参数取出对应的规则，引擎执行，输出RSS

## 相关文章

* [Wechat2RSS: self-hosted版本发布](https://blog.xlab.app/p/fd57c4cf/)
* [用RSSHub替代Feed43](https://blog.xlab.app/p/1209a846/)
* [Wechat2RSS:更新频率策略设计](https://blog.xlab.app/p/d73537b/)
* [Wechat2RSS:架构演进](https://blog.xlab.app/p/a207c8e3/)
* [先知社区RSS](https://blog.xlab.app/p/6041ed53/)

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[RSS](/tags/RSS/)
 [Feed43](/tags/Feed43/)

[好用但难用的Excel](/p/98e8b0f5/ "好用但难用的Excel")

[前端沙箱挑战](/p/d4ad4aa/ "前端沙箱挑战")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2025

透明人

站点总字数：
343k

Theme NexT works best with JavaScript enabled