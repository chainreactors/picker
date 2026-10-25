---
title: 暗网博弈：APT情报技术体系 - 连载三
url: https://mp.weixin.qq.com/s/4Sz4W3CDOkAym_3PoWatjg
source: Doonsec's feed
date: 2026-10-24
fetch_date: 2026-10-25T07:09:48.752235
---

# 暗网博弈：APT情报技术体系 - 连载三

# 暗网博弈：APT情报技术体系 - 连载三

原创

AI紫队安全研究
AI紫队安全研究

AI紫队安全研究

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**大家好，我是AI紫队安全研究。建议大家把公众号“AI紫队安全研究”设为星标，否则可能就无法及时看到啦！因为公众号只对常读和星标的公众号才能大图推送。操作方法：先点击上面的“AI**紫队安全研究**”，然后点击右上角的【...】,然后点击【设为星标】即可。**

**关注视频号 “**AI紫队安全研究**” 不定期周五晚上10点直播。**

# **第二部分全域感知——国家级情报摄取与数据底座**

# **第2章 UPSTREAM与PRISM：两条摄取路径的工程化分野**

## **2.1 全量摄取的双轨架构**

NSA的信号情报摄取体系在工程上分为两条逻辑路径：**UPSTREAM（上游截获）**与**DOWNSTREAM（下游获取）**。两者的本质区别不在于数据内容，而在于**采集位置**和**法律授权框架**——UPSTREAM在通信链路层完成流量镜像，依据FISA Section 702的”境外通信”条款运行；DOWNSTREAM则在应用层通过服务商接口直接拉取结构化数据，即公众熟知的PRISM计划。

graph TB
    subgraph 双轨摄取架构
        subgraph UPSTREAM["UPSTREAM — 链路层截获"]
            CABLE["海底光缆<br/>分光器 / 光学分路"] --> SPLICE["流量镜像节点<br/>DCGS-N / TURMOIL前端"]
            SPLICE --> FILTER["选择器过滤<br/>BANYAN / TURMOIL分类器"]
            FILTER --> NSA\_UP["NSA数据管道<br/>→ XKEYSCORE索引"]
        end

        subgraph DOWNSTREAM["DOWNSTREAM — 应用层获取"]
            PROVIDER["服务提供商<br/>Google/MS/Apple/Facebook..."] --> PRISM\_IFACE["PRISM接口<br/>FISA 702合规通道"]
            PRISM\_IFACE --> STRUCT["结构化数据<br/>邮件/聊天/文件/视频日志"]
            STRUCT --> NSA\_DOWN["NSA数据管道<br/>→ XKEYSCORE索引"]
        end

        NSA\_UP --> FUSION["统一数据湖<br/>PINWALE / TURBULENCE"]
        NSA\_DOWN --> FUSION
    end

    style UPSTREAM fill:#0d1117,stroke:#e94560,color:#fff
    style DOWNSTREAM fill:#0d1117,stroke:#0f3460,color:#fff

这两条路径并非冗余备份，而是**互补设计**。UPSTREAM能捕获传输层元数据（源/目的IP、TCP时间戳、路由跳变）和未加密有效载荷，但对TLS加密内容无能为力；PRISM则在应用层获取已解密的结构化数据，但依赖服务商配合且存在请求延迟。两条管道的数据最终汇入同一数据湖，由XKEYSCORE完成统一索引与关联检索。

感兴趣的读者，建议加入知识星球后留言，感谢！

![](https://mmbiz.qpic.cn/mmbiz_png/E3ZvvAXyiaibm0l6wIBoUfic1Rxr77k9bUlBJeO2gkADWstEJ1u2JGkNGd6Td2RFTWbUh4PWaibl2jEpIAZnNsBUjCX8D6Xrlmuw44kpnsx1H34/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sUKKZDdVP8SDmJE3icia7GnaJnVTPhzvKxNj1UhibY8xmZLVfpF4v54OD9Jia6UhwdOcd8YMMw0ZbHnN3UodTaib7tw/0?wx_fmt=png)

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