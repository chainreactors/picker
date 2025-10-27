---
title: 1500个APP暴露Algolia API密钥，影响超300万用户
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247554118&idx=1&sn=7524c8b7cd571ef1c11e9b8cb8d34670&chksm=e915c47cde624d6a95861b00b7b22c979d89e3590633cf8d2395896bf6265231eeff92297f7d&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-11-24
fetch_date: 2025-10-03T23:39:42.593094
---

# 1500个APP暴露Algolia API密钥，影响超300万用户

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29VJwjUSAxKPXpfMiauSXATe44oKTPdnmvch7qI9XjWLB4pictHmXNaD66NqoAtc19cobPXG4hYLn3Q/0?wx_fmt=jpeg)

# 1500个APP暴露Algolia API密钥，影响超300万用户

ang010ela

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

1500个APP暴露Algolia API密钥，影响超300万用户。

Algolia 成立于2012年，是一个面向开发者的搜索功能API接口，为网站及APP的开发者提供搜索功能接口，可以为其提供发现和推荐功能，用户超过11万企业。新加坡网络安全公司CloudSEK研究人员发现有1550个移动APP会泄露Algolia API密钥，敏感内部服务和存储的用户信息有泄露的风险。

Algolia API系统有5类API key，分别对应Admin、Search、Monitoring、Usage和Analytics功能。这些API key中只有Search是可公开的，可以在前端代码中看到，帮助用户在APP中执行搜索查询。Monitoring key 为管理员提供集群状态信息。Usage和Analytics为用户提供使用统计数据。Admin key提供对其他4类API服务的访问，以及：

浏览、删除索引；

添加、删除记录；

列出索引；

获取、设置索引设置；

获得访问记录。

滥用以上服务可以宝库用户的敏感数据，比如用户设备、网络访问信息、使用统计数据、检索记录和其他相关信息的操作。

CloudSEK自动扫描工具发现有1550个APP泄露了Algolia API key和应用ID，攻击者利用这些泄露的信息可以实现对内部信息的非授权访问。这些暴露Algolia Admin API key的APP下载次数累计超过325万，其中有APP下载次数超过百万。其中32个APP会泄露admin secret，其中包括57个唯一的管理员密钥，攻击者利用泄露的管理员密钥可以访问敏感用户信息或修改APP索引记录和设置。

攻击者利用admin API key可以执行许多关键操作，并实现对敏感数据的访问，比如攻击者可以检索或者查看敏感数据。根据APP的版本，攻击者可以利用这些敏感访问更多的敏感数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATebYEbO84mkUAxlJIoY4YL73f0OwlMRlsedtibOcWVL38dzW6xiaLcw8QQ/640?wx_fmt=png)

图 API keys 暴露引发的攻击流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeSgvIoziacA89T95UufLjgK8POWPWG7g1Rl2ICicjhGU9J6G3tt7IgUag/640?wx_fmt=png)

图 暴露API的APP种类和下载次数

暴露密钥最多的APP种类为商城APP，下载次数超过230万次。此外，还有新闻APP、食品和饮料、教育、健身、医疗和商业APP，累计下载量超过95万次。

CloudSEK已联系了受影响的APP开发者，告知了密钥暴露情况和潜在的安全风险。

完整技术分析参见：https://cloudsek.com/whitepapers\_reports/hardcoded-algolia-api-keys-could-be-exploited-by-threat-actors-to-steal-millions-of-users-data/

参考及来源：https://www.bleepingcomputer.com/news/security/apps-with-over-3-million-installs-leak-admin-search-api-keys/

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29IPtCG50icBxktc5rzaIhdSc0JhHibksQzb1ibmicTa6v6FZwFfAeqmJzpTIuKqzbLGWPjtRn4rwUEXg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29VJwjUSAxKPXpfMiauSXATeYeIEa4OiaFXguSm9haklicCrTSLR9c0vZDHpvSzBib5K2juybJoK9Jl5w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icEjy5ZrpCcgr4BicXicPv08DSsrgibDcJQpvwkZoO4OqdIpJNhj6TO5xV0ic0AnVf7f2kcPnNevQlTtQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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