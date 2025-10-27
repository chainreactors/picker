---
title: 微软CEO眼中AI Agent商业模式和安全
url: https://mp.weixin.qq.com/s?__biz=MzI1MjQwMTAyOQ==&mid=2247483886&idx=1&sn=4babd4b0b9d2cbbb3073bf7a9fbb80c8&chksm=e9e50504de928c12a34fb6f0317d3cdfe17291a570374e8553890f5bfeebdf12624f8e5f0d59&scene=58&subscene=0#rd
source: 落水轩
date: 2024-12-21
fetch_date: 2025-10-06T19:39:11.884694
---

# 微软CEO眼中AI Agent商业模式和安全

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ZrnQ9cTzz1WMXia4ZYkyg1TCjsDxY3eiaJPuorYL1FVMaEQ82Hh5b2SWAmqrlZapT5YTCWOmNOttoRyicbwWCXrjw/0?wx_fmt=jpeg)

# 微软CEO眼中AI Agent商业模式和安全

原创

高渐离

落水轩

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZrnQ9cTzz1WMXia4ZYkyg1TCjsDxY3eiaJnWG8OL9JlCsTlbqV8XDq9wibHJwPT0ZgxY7u4zSRL12icib3rssBy2oPQ/640?wx_fmt=png&from=appmsg)

在大模型领域，底座大模型的网络效应不明显。但网络效应会始终存在于应用层。既包括消费者端（to C场景），也包括企业端（to B场景）。

在AI Agent的系统里，涉及至少两方。一方是AI Agent自身，另一方是被AI Agent调用的应用。

## To C场景的AI Agent

###

### 商业逻辑

###

AI Agent本身来说，以AI搜索为例，传统搜索引擎是无状态的，但现在，AI搜索会立即获得答案，更加直观，持续和有记忆。当然分发渠道仍然非常重要。所以，Google这样的传统搜索引擎仍然具有优势。因为在Android和苹果手机上，它都是默认搜索引擎。但是习惯一旦形成就很难改变。大家越来越多会使用AI搜索，直接获取答案。这是一种长期的结构性变化。传统搜索引擎的商业模式会面临巨大威胁。

传统的To C场景的商业模式往往通过广告和流量方式变现的。但AI Agent世界中，这些方式可能会发生变化。当前C端的商业模式仍然不明晰。（商业变现目前仍然是以订阅制为主）

### 安全问题

很多C端的AI Agent，像某某助手之类的，它可以在没有电商网站运营方许可的情况下直接在电商网站上交易么？

在这种情况下，C端的AI Agent其实是在以用户身份访问电商网站上的数据。按传统的理解，这部分数据同时归属于电商网站运营方和用户。

这里有两个原则：

1. 必须获得授权。C端应用中，像购买记录之类的数据是属于客户的。客户必须同意授权才可以。
2. 必须具备一个信任边界。C端的AI Agent不能无限制的访问C端应用上的数据。因为里面部分的数据其实是C端应用自己生产的，例如电商网站里面的商户数据。

## To B场景的AI Agent

##

### 商业逻辑

在to B场景下，用户需要购买B端应用的Connector服务。to B场景下，未来B端应用会暴露一个智能体接口，供其他智能体调用和合作。B端的AI Agent可以让用户更容易访问B端的应用。而B端应用通过Connector实现了货币化。

B端的AI Agent本身的售卖，通过提升人效，从而实现了商业化。

### 安全问题

B端场景则不存在以上数据访问的权限问题。因为B端应用的数据都是归属于B端的客户的。

## AI Agent的权限管理

Agent除了记忆，工具调用这两大组成部分之外，还需要一个权限管理模块。

Agent拥有哪些权限，可以安全访问哪些数据，谁来进行管理和治理。这些结合起来，Agent的行为会变得更加可管理。执行操作时，它是可验证的，并且具有记忆功能。那么你就进入了一个完全不同的阶段，可以处理更多自主任务。

即使在处理自主任务过程中，也会面临例外情况，可能需要请求许可，或者需要调用其他操作。因此，仍然需要一个UI层来组织这些工作。因此，Copilot被视为工作文档和工作流程的组织层。

## 总结

AI Agent在跟后端应用的交互过程中会存在权限问题。

这里，一方面AI Agent自身要具备权限管理模块。并通过UI层来显式的请求许可和调用其他操作。另一方面，被AI Agent调用的应用，需要提供相应的接口和设置访问边界，避免数据访问过界。

整个AI Agent的商业模式在B端已经比较清晰，但C端还存在着变现问题。（目前还主要是通过订阅制）

文章参考：

《**深度｜微软 CEO 纳德拉最新两万字洞察：C 端 Agent 商业模式仍需摸索，广告流量模式或面临转变，B 端关键在生态集成**》[https://mp.weixin.qq.com/s/It3xs5joaxYIHw6V2DKHRA](https://mp.weixin.qq.com/s?__biz=Mzg3NDkyMTQ5Mw==&mid=2247496996&idx=1&sn=c71497dfa81594187ad32f5e3a23ed91&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1WOsZoFuzvcqld7856xdZUXcXVmW7W3IPYG61GL78m6ILibka5ibzU3jtSBwNcKWUibiboYRfGwuTTOSA/0?wx_fmt=png)

落水轩

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZrnQ9cTzz1WOsZoFuzvcqld7856xdZUXcXVmW7W3IPYG61GL78m6ILibka5ibzU3jtSBwNcKWUibiboYRfGwuTTOSA/0?wx_fmt=png)

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