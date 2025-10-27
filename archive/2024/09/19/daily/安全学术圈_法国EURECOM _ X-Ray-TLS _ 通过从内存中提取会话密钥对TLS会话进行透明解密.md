---
title: 法国EURECOM | X-Ray-TLS : 通过从内存中提取会话密钥对TLS会话进行透明解密
url: https://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247491208&idx=1&sn=7753f7851d4196b1f4e72398a7c4cffb&chksm=fe2ee103c9596815034973eb5a644b9b5b83c038dacd1f3219e4e1513e3470f419034c3dffbd&scene=58&subscene=0#rd
source: 安全学术圈
date: 2024-09-19
fetch_date: 2025-10-06T18:26:03.325140
---

# 法国EURECOM | X-Ray-TLS : 通过从内存中提取会话密钥对TLS会话进行透明解密

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6Dibw6L070WFbrThnh5ib03ZKm7aYMhFW5YEK7MUunAZABFxPRLWy6ia2O57QLOHyGIlZviacLZ2vHrC4OBhXicyFtA/0?wx_fmt=jpeg)

# 法国EURECOM | X-Ray-TLS : 通过从内存中提取会话密钥对TLS会话进行透明解密

原创

Ledraw

安全学术圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFbrThnh5ib03ZKm7aYMhFW5ibmLFsBns9alBagSFb9YkXDYJFH8bYALfhiawKtYtjv7AJ3pSGHYFXyg/640?wx_fmt=png&from=appmsg)

> *原文标题：X-Ray-TLS: transparent decryption of TLS sessions by extracting session keys from memory*
> *原文作者：Florent Moriconi, Olivier Levillain, Aurélien Francillon, Raphael Troncy*
> *发表期刊：ACM ASIA Conference on Computer and Communications Security (ACM ASIACCS)*
> *原文链接：https://dl.acm.org/doi/10.1145/3634737.3637654**PDF地址：https://www.eurecom.fr/publication/7588/download/data-publi-7588.pdf* *主题类型：流量解密*
> *笔记作者：Ledraw*

# 研究背景

传统的TLS拦截方法（如中间人攻击和HTTPS代理）通常复杂且具有侵入性。需要一种更简单且不侵入的方式来解密TLS会话，以便在不影响安全性的情况下进行流量分析。

# 方法与实现

* X-Ray-TLS方法

+ 通过比较两次内存快照之间的差异，提取会话密钥来透明地解密TLS会话。
+ 利用现有的内核功能和eBPF来从进程内存中提取TLS会话密钥。
+ 支持TLS 1.2、TLS 1.3和QUIC协议。
+ 适用于多种TLS库和应用程序，特别是在CI/CD管道中检测软件供应链攻击。
+ 不需要修改目标程序或使用虚拟机监控程序。

* 整体架构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFbrThnh5ib03ZKm7aYMhFW5FYibBRA8D7qYspRbg0iaSUN1UGXEZMwicUQ9hyM2rB1ReicCULWhonJsBQ/640?wx_fmt=png&from=appmsg)

* X-Ray-TSL与其他方法对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFbrThnh5ib03ZKm7aYMhFW5RN7AGjhp3Czc07o3zD0C0u7vvkYAnH70o2ia3ewMu7OU3vwtVjvSbjQ/640?wx_fmt=png&from=appmsg)

# 技术细节

* 内存快照策略:

+ 使用软脏位（soft-dirty bit）来跟踪内存页面的变化。
+ 提供五种内存快照策略，从完整转储到部分转储，优化性能和减少冻结时间 。

* 五种快照策略的冻结时间对比

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6Dibw6L070WFbrThnh5ib03ZKm7aYMhFW50LevjksicG5sr4XJ1KGcQwsOV4HbRSINPH3jtxFQsw9fz3Z4J0n5ITg/640?wx_fmt=png&from=appmsg)其中full-partial-rst方法的冻结时间最少

# 应用场景

* CI环境（Continuous Integration）:

+ 适用于企业网络和CI环境，帮助检测信息泄露、确保工件可追溯性，并支持构建失败的根本原因分析 。

* 通用性:

+ 与其他TLS检查方法（如MITM和HTTPS代理）相比，X-Ray-TLS不需要目标程序的配合，并且在不同的TLS库中具有通用性

# 展望

计划使用数据驱动技术来改进密钥提取和模式检测。这将有助于自动发现密钥存储模式，从而将密钥搜索集中在特定的内存区域

# 结论

X-Ray-TLS提供了一种高效且不侵入的TLS流量解密方法，适用于多种实际应用场景，特别是在CI/CD管道中。其实现已在GitHub上发布，并得到了法国国家研究机构的支持。展示了X-Ray-TLS在TLS流量解密中的创新性和实用性。

> [安全学术圈招募队友-ing](http://mp.weixin.qq.com/s?__biz=MzU5MTM5MTQ2MA==&mid=2247484475&idx=1&sn=2c91c6a161d1c5bc3b424de3bccaaee0&chksm=fe2efbb0c95972a67513c3340c98e20c752ca06d8575838c1af65fc2d6ddebd7f486aa75f6c3&scene=21#wechat_redirect)
> 有兴趣加入学术圈的请联系 **secdr#qq.com**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

安全学术圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6Dibw6L070WFvZRQiafv3iccicic1dIYUEQ1ZzLh1a10l7tfw7zkWkRbY9kEPBwX2NiadOrwFl9a48as9qiayp3eOgDUQ/0?wx_fmt=png)

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