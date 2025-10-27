---
title: asm项目v0.0.3版本总结
url: https://mp.weixin.qq.com/s?__biz=MzkyMDIxMjE5MA==&mid=2247485349&idx=1&sn=2cba596c66582dd3def6cba328486030&chksm=c1970014f6e089021292dcbe9b500cd1067131302186454d6cb76608840b2d38094941d738de&scene=58&subscene=0#rd
source: leveryd
date: 2023-03-15
fetch_date: 2025-10-04T09:36:16.183258
---

# asm项目v0.0.3版本总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJbm1WYtvCv76CknMhNsw1XpvLHS88aw1VTHMiaLkYs7QNyZjmibW4OWgUA/0?wx_fmt=jpeg)

# asm项目v0.0.3版本总结

原创

leveryd

leveryd

# 背景

![](https://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJb2qy1o1D8ZyZicAwBlXe96ZKmq5h1SVxrYZLGV3pV3ghR8STAvnbGE8A/640?wx_fmt=png)
> 文字版见 https://github.com/leveryd-asm/asm/releases/tag/v0.0.3

目前asm项目[1]可以回答以下问题

* 公司有哪些favicon？favicon信息包括通用和公司图标
* 公司有哪些证书？
* 公司有哪些asn号码？
* 公司有哪些ip？
* 公司有哪些web服务、首页信息？
* 公司有哪些端口信息？

根据当前的数据，尝试基于kibana做了X公司资产的dashboard![](https://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJb8efaBMSY5vwLR0kW36V76mlSqoZzRBoICklD9xXP8Bjz4ShyaAfjHw/640?wx_fmt=png)

下面向你介绍一下本次更新中最重要的两类功能的设计和实现。

# 组织和资产的映射关系

为什么需要这个呢？如果我们知道有哪些组织，并且知道哪些资产属于组织，就可以从企业角度管理资产，比如绘制上面的企业资产dashboard

网络测绘厂商或者攻击面管理厂商是怎么做这个事情的呢？

zoomeye的org字段能够搜索指定组织的资产![](https://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJbo66nzoceq9CznV28OKUTT6QdukV00WFfc9H3aG7syZERV1gbqAlf0w/640?wx_fmt=png)

https://0.zone/ 不支持 "组织:xxx" 这种查询语法，但也支持关键字搜索![](https://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJbNBcrGibPAbCnEos4BKxLSbe2kCS2LHSeYj9HsMPvO929ZLRp0G9anuQ/640?wx_fmt=png)

zoomeye支持组织名搜索的功能我感觉挺神奇的，就比如程序怎么能知道一个c段有哪些组织名呢。根据证书、网页title、响应csp、重定向的地址等等信息，我们肉眼可以知道是哪个组织的，但是程序怎么根据这些信息得到一个组织名呢，而且程序还能准确的知道这个组织叫做谷歌而不是谷歌XXX、叫做twitter而不是推特 (打个比方)？

再说组织和资产的映射关系也不是个简单的事情，比如A公司服务部署在谷歌云的虚拟机上，那虚拟机ip所属的组织是应该被标记成A公司还是谷歌呢？

于是，我又测试了一下zoomeye搜索其他厂商，数据如下，看起来zoomeye的组织名并不是很"万能"。

```
org:"谷歌"  798,974条记录
org:"推特" 0条记录
org:"twitter" 642,676条记录
org:"小红书" 0条记录
org:"知乎" 0条记录
org:"拼多多" 0条记录
```

asm项目中目前是怎么做资产和组织映射的、怎么识别资产是属于哪个组织？

elasticsearch中每类资产都有org和org\_num两个字段，org是字符串数组类型，存放组织标签信息，所以一个资产可以标记成多个组织拥有。

目前是让用户手动配置去给资产打上对应组织的标签，比如证书组织中如果有baidu或者百度关键字，就给对应证书资产打上相应标签。有一个cronjob会每两小时根据用户的配置去更新一次映射关系。

```
{ "org": "百度", "query": "subject_org:baidu OR subject_org:百度", "index": "tls" }
{ "org": "百度", "query": "title:baidu OR title:百度", "index": "web-service" }
{ "org": "百度", "query": "response-body:baidu OR response-body:百度", "index": "web-service" }
{ "org": "百度", "query": "parsed-domain.registered_domain:baidu.com", "index": "web-service" }
{ "org": "百度", "query": "asn.as-name:baidu OR asn.as-name:百度", "index": "web-service" }
```

背后是怎么实现的呢？

通过 update\_by\_query 和 painless script 实现批量更新组织信息。

读取配置、请求elasticsearch接口等功能是通过logstash实现而不是编程语言。

这个过程中遇到"批量更新时，文档版本冲突"的问题。通过调整pipeline.worker=1、logstash filter sleep插件等办法临时解决。

> logstash配置见 https://github.com/leveryd-asm/asm/commit/bb353d5cb15eb441bb2b16a0c17d6f20a3a8b5ef

# "web首页、asn、端口、子域名、证书、favicon"等资产信息探测并入库

pd组织的工具和elk结合起来很容易实现资产探测和入库：httpx、naabu、tls、subfinder等工具都支持json输出，logstash将json数据导入到elasticsearch中。

![](https://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJbIFlDARWRthO2icRpq1qDxNvygreUXxWnic6KwTLqldWX6FL3eenjlj7g/640?wx_fmt=png)

每个索引都会有一个first\_create\_time和last\_update\_time字段，分别表示文档第一次创建的时间和最近一次被更新的时间。这个时间字段可以用来发现新增的资产、过期的数据。

索引的其他字段你可以通过elasticsearch查看，或者`httpx -json`、`naabu -json`等方式查看，这里我就不对字段做过多说明。

每个索引也通过文档id做了去重，比如证书资产以`domain_ip_port`去重

![](https://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJbgqqibXr9ejVL57vRhSwDrdvfDFGSfyTbNuCR3PIE7rvBMxnqyIK20gA/640?wx_fmt=png)
> 实现资产导入的logstash配置见 https://github.com/leveryd-asm/asm/blob/master/templates/argo-workflow-template-asset/level1/logstash/config.yaml

# v0.0.4版本

计划暂定如下，欢迎在 https://github.com/leveryd-asm/asm/issues/33 issue中讨论

![](https://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYxbyszzZrqicShknWtGR8MJbyyqViaKAanQDXPniar6fGGuTZlibMaic7NpOapc2UxEibypbc4ubU0qU3QA/640?wx_fmt=png)

# 总结

此次更新，用户能够在argo ui创建多种类型资产的探测任务。结合elasticsearch功能丰富的查询api可以更加灵活地过滤出资产，对资产做更一步的处理。

欢迎加我微信 happy\_leveryd 或者 邮箱 leveryd@gmail.com 与我交流。

### 参考资料

[1]

asm项目: *https://github.com/leveryd-asm/asm*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYzLqic1QRTmPcgwxruJG9yRD0jsKyhb8rL8oHWWCMyAIibge74Wy4jF0epz8iblImDLmxGibwcf9wVPibg/0?wx_fmt=png)

leveryd

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FwyeCXsWiaYzLqic1QRTmPcgwxruJG9yRD0jsKyhb8rL8oHWWCMyAIibge74Wy4jF0epz8iblImDLmxGibwcf9wVPibg/0?wx_fmt=png)

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