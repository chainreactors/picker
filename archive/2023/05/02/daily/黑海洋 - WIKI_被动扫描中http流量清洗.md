---
title: 被动扫描中http流量清洗
url: https://blog.upx8.com/3483
source: 黑海洋 - WIKI
date: 2023-05-02
fetch_date: 2025-10-04T11:40:18.221618
---

# 被动扫描中http流量清洗

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 被动扫描中http流量清洗

发布时间:
2023-05-01

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
12701

### 0x00 写在前面

几个月前写的被动扫描工具`rcefuzzer`的实际使用效果挺好的,除了被污染的流量贼它娘的多以外，需要清洗掉无意义的流量。

![](https://blog.thekingofduck.com/post-images/16360956681866/16363613590388.jpg)

### 0x01 核心问题

减少请求数量的核心问题是:

```
如何确定流量是否是重复的?
```

一个完整的标准链接包含了协议,凭证,目的地址,目标端口,路由,参数,描点这7部分,凭证和描点,其中凭据和描点都属于浏览器层面用户操作体验的问题,不用考虑。那么将其他五个部分加上不同的请求方法组成一个向量就是:

```
请求方法:协议:域名:端口:URL路径:参数名称排序合集
```

请求方法,协议,域名,端口这四个的变化比较小,基本上是固定的,也不用考虑怎么考虑。

### 0x02 路由处理

URL路径的花样会比较多,去除资源文件的不多说,这里主要考虑其他情况,比如

```
A:/path1/path2
B:///path1////path2
```

这里在处理的时候比较好奇中间件是怎么判断两个路由等效的,于是翻了以下代码,在`org.apache.catalina.connector.CoyoteAdapter#normalize`中可以看到代码对`\`,`//`,`/./`,`/../`等字符串进行了处理,路径标准化后再去做`servlet`调度。

![96827ED7-684C-4B18-A7EF-169E63A6B985](https://blog.thekingofduck.com/post-images/16360956681866/96827ED7-684C-4B18-A7EF-169E63A6B985.png)
![133DE564-841D-4463-AE59-8C18EE80FDFF](https://blog.thekingofduck.com/post-images/16360956681866/133DE564-841D-4463-AE59-8C18EE80FDFF.png)

对于做流量清洗来说，只需要关注：

![2EC0B35D-A87C-4BF0-8C82-69BDC1A60A09](https://blog.thekingofduck.com/post-images/16360956681866/2EC0B35D-A87C-4BF0-8C82-69BDC1A60A09.png)

这个实现读起来没那么友好,那么可以改写为：

![479F2B17-E5E9-4B15-A4F5-DC9B9F2E8F73](https://blog.thekingofduck.com/post-images/16360956681866/479F2B17-E5E9-4B15-A4F5-DC9B9F2E8F73.png)

再比如:

```
A:/news/1
B:/news/2
C:/news/1/read
D:/news/2/edit
```

很明显的是restfull风格或者伪静态的写法，AB属于同一个路由，BC不同，后端的写法可能是：

![4FAC106D-9AE0-4616-B244-95643D6D3C1E](https://blog.thekingofduck.com/post-images/16360956681866/4FAC106D-9AE0-4616-B244-95643D6D3C1E.png)

处理思路也比较清楚,路径标准化后再切割一下,尝试转换成不通的整数，相同的视作同一路由即可。

![78C9522E-188A-4D7B-B168-9283423A9920](https://blog.thekingofduck.com/post-images/16360956681866/78C9522E-188A-4D7B-B168-9283423A9920.png)

除了数字这种还经常遇到用hash或者uuid的,处理方式差不多，判断依据均已标准化后的路由为准。

![BF86F158-F069-433D-AD76-AA54D59D1084](https://blog.thekingofduck.com/post-images/16360956681866/BF86F158-F069-433D-AD76-AA54D59D1084.png)

### 0x03 参数处理

已经考虑到的后端写法如：

![493DFA24-BE9A-4C00-BAD7-AA44DFFDF057](https://blog.thekingofduck.com/post-images/16360956681866/493DFA24-BE9A-4C00-BAD7-AA44DFFDF057.png)

对应的URL如下：

```
A:/news?id=2
B:/news?action=edit&id=2
C:/news?action=del&id=2
D:/news?id=2&action=del
```

从相邻的来看,AB的参数不同,扫完A肯定得接着扫,但B扫完再扫C实际意义不大。CD的参数顺序不通,但本质上D和BC也是一样的。综合下来处理的思路是获取所有参数名排序后组成一个向量,作为判断流量是否重复的依据。也就是说,ABCD实际上只需要扫描AB即可。

### 0x04 写在最后

orz... 做的时候感觉蛮多东西可以玩的,写出来就感觉索然无味.

[取消回复](https://blog.upx8.com/3483#respond-post-3483)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")