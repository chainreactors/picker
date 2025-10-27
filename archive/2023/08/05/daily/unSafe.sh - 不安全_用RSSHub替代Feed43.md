---
title: 用RSSHub替代Feed43
url: https://buaq.net/go-173724.html
source: unSafe.sh - 不安全
date: 2023-08-05
fetch_date: 2025-10-04T12:00:09.672332
---

# 用RSSHub替代Feed43

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/bd8ddd28acbd9b5f921d221d6baadf0a.jpg)

用RSSHub替代Feed43

早些时候提出RSSHub规则化架构设计，最近抽空简单实现了这块功能，目前也已经合并到RSSHub主线，本人几十个Feed43也已经成功迁移到RSSHub，非常舒适考虑到使用上可能有一些门槛，写一篇使
*2023-8-4 22:40:14
Author: [blog.xlab.app(查看原文)](/jump-173724.htm)
阅读量:46
收藏*

---

早些时候提出[RSSHub规则化架构设计](https://blog.xlab.app/p/9c76cef)，最近抽空简单实现了这块功能，目前也已经合并到RSSHub主线，本人几十个Feed43也已经成功迁移到RSSHub，非常舒适

考虑到使用上可能有一些门槛，写一篇使用教程

* RSSHub transform路由怎么用
* 如何利用RSSHub将任意网页做成RSS

官方文档：<https://docs.rsshub.app/other.html#zhuan-huan>

由于这个功能支持任意页面，当请求恶意页面时可能会有SSRF的风险

所以仅支持自建，并将`ALLOW_USER_SUPPLY_UNSAFE_DOMAIN`环境变量设置为`true`

部署文档 <https://docs.rsshub.app/install/>

> 推荐自建是配置访问控制，避免自建服务被滥用/攻击

## 制作方法

目前是支持将任意的HTML和JSON转换为RSS，下面通过几个例子介绍制作过程

对于有前端基础/了解`CSS选择器`的可以直接看[官方文档](https://docs.rsshub.app/other.html#zhuan-huan)，结合文档例子应该很容易举一反三

对于了解或使用过Feed43，可以理解为将Feed43的用于匹配的`正则Pattern`转化为更加语法话的`CSS选择器`和`JSON Path`

CSS选择器可以参考 <https://developer.mozilla.org/zh-CN/docs/Web/CSS/CSS_selectors>

### HTML

路由格式为`/rsshub/transform/html/:url/:routeParams`

`url`就是需要爬的地址，其中`routeParams`可用参数有很多，大多数情况下填2-3个参数就可以用了

| 键 | 含义 | 接受的值 | 默认值 |
| --- | --- | --- | --- |
| `title` | 指定 RSS 的标题 | `string` | 从当前网页中取 `<title>` |
| `item` | 通过 CSS 选择器查找 HTML 元素作为 `item` 元素 | `string` | html |
| `itemTitle` | 在 `item` 中通过 CSS 选择器查找 HTML 元素作为 `title` 元素 | `string` | `item` 元素 |
| `itemTitleAttr` | 获取 `title` 元素属性作为标题 | `string` | 元素 text |
| `itemLink` | 在 `item` 中通过 CSS 选择器查找 HTML 元素作为 `link` 元素 | `string` | `item` 元素 |
| `itemLinkAttr` | 获取 `link` 元素属性作为链接 | `string` | `href` |
| `itemDesc` | 在 `item` 中通过 CSS 选择器查找 HTML 元素作为 `descrption` 元素 | `string` | `item` 元素 |
| `itemDescAttr` | 获取 `descrption` 元素属性作为描述 | `string` | 元素 html |

以本站`https://blog.xlab.app/`为例，写一个标题

| key | value |
| --- | --- |
| title | 明天的乌云 |

打开浏览器的开发工具，找到想要定位的文章

![](https://blog.xlab.app/p/1209a846/html_item.png)

可以看到文章在`article`标签中，那么构造`item`参数

| key | value |
| --- | --- |
| title | 明天的乌云 |
| item | article |

对于文章标题，可以看到在`a`标签中，属性是`class="post-title-link"`

![](https://blog.xlab.app/p/1209a846/html_title.png)

构造`itemTitle`参数

| key | value |
| --- | --- |
| title | 明天的乌云 |
| item | article |
| itemTitle | `a[class="post-title-link"]` |

`itemTitleAttr`不填的话会自动取元素中的文本，这里例子就不用填

对于文章连接，可以看到也是在这个元素中，其中需要的链接在`href`属性中

![](https://blog.xlab.app/p/1209a846/html_link.png)

构造`itemLink`和`itemLinkAttr`参数

| key | value |
| --- | --- |
| title | 明天的乌云 |
| item | article |
| itemTitle | `a[class="post-title-link"]` |
| itemLink | `a[class="post-title-link"]` |
| itemLinkAttr | href |

现在提取文章内容，在`div`元素中，有`itemprop="articleBody"`属性，其中的`p`标签是内容

![](https://blog.xlab.app/p/1209a846/html_desc.png)

构造`itemDesc`

| key | value |
| --- | --- |
| title | 明天的乌云 |
| item | article |
| itemTitle | `a[class="post-title-link"]` |
| itemLink | `a[class="post-title-link"]` |
| itemLinkAttr | href |
| itemDesc | `div[itemprop="articleBody"] p` |

`itemDescAttr`也不用填，默认取其中的`html`

将表格经过URL编码转换，得到`routeParams`

|  |  |
| --- | --- |
| ``` 1 ``` | ``` title%3D%25E6%2598%258E%25E5%25A4%25A9%25E7%259A%2584%25E4%25B9%258C%25E4%25BA%2591%26item%3Darticle%26itemTitle%3Da%255Bclass%253D%2522post-title-link%2522%255D%26itemLink%3Da%255Bclass%253D%2522post-title-link%2522%255D%26itemLinkAttr%3Dhref%26itemDesc%3Ddiv%255Bitemprop%253D%2522articleBody%2522%255D%2Bp ``` |

> 别急，下面有[编码工具](#%E5%B0%8F%E5%B7%A5%E5%85%B7)

最后，拼接URL编码的链接得到完整路由

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /rsshub/transform/html/https%3A%2F%2Fblog.xlab.app%2F/title%3D%25E6%2598%258E%25E5%25A4%25A9%25E7%259A%2584%25E4%25B9%258C%25E4%25BA%2591%26item%3Darticle%26itemTitle%3Da%255Bclass%253D%2522post-title-link%2522%255D%26itemLink%3Da%255Bclass%253D%2522post-title-link%2522%255D%26itemLinkAttr%3Dhref%26itemDesc%3Ddiv%255Bitemprop%253D%2522articleBody%2522%255D%2Bp ``` |

RSS就做好了

![](https://blog.xlab.app/p/1209a846/html_rss_p.png)

### 简化

虽然看起来表里这么多参数，其实有些是可以不填的，有些可以写的更加简单一些

| key | value |
| --- | --- |
| title | 明天的乌云 |
| item | article |
| itemTitle | `a[class="post-title-link"]` |
| itemLink | `a[class="post-title-link"]` |
| itemLinkAttr | href |
| itemDesc | `div[itemprop="articleBody"] p` |

`title`可以不填，会自动处理

`itemTitle`不用定位这么精细，可以取更上一层的元素，比如`h2`

`itemLink`和`itemLinkAttr`可以不填，会自动取第一个`a`链接

`itemDesc`也可以不填，自动取整个html

最终`routeParams`参数可以简化为

| key | value |
| --- | --- |
| item | article |
| itemTitle | h2 |

得到简单能用的路由

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /rsshub/transform/html/https%3A%2F%2Fblog.xlab.app%2F/item%3Darticle%26itemTitle%3Dh2 ``` |

简单，不好看，但能用

![](https://blog.xlab.app/p/1209a846/html_rss2_p.png)

由于这个规则足够简单，可以适应于更多的网站，比如使用相同框架的站点Hexo/Hugo/WordPress等，规则是可以通用的

可以期待未来RSSHub可以不用手动编写参数，仅提供链接就能制作RSS

### JSON

JSON的其实和HTML差不多，相信看完HTML的例子，再去看官方文档和例子，应该也能看懂了

## 小工具

填写下面的表单，构建RSSHub订阅地址

RSSHub地址:
目标地址:
访问密钥:

编码结果：

url：

routeParams：

最终路由：

订阅地址

## 相关文章

* [Wechat2RSS: self-hosted版本发布](https://blog.xlab.app/p/fd57c4cf/)
* [RSSHub规则化架构设计](https://blog.xlab.app/p/9c76cef/)
* [Wechat2RSS:更新频率策略设计](https://blog.xlab.app/p/d73537b/)
* [Wechat2RSS:架构演进](https://blog.xlab.app/p/a207c8e3/)
* [先知社区RSS](https://blog.xlab.app/p/6041ed53/)

文章来源: https://blog.xlab.app/p/1209a846/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)