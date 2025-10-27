---
title: 鞋类品牌Ecco在500天内泄露超60GB敏感数据
url: https://www.freebuf.com/articles/database/353229.html
source: FreeBuf网络安全行业门户
date: 2022-12-23
fetch_date: 2025-10-04T02:20:16.997138
---

# 鞋类品牌Ecco在500天内泄露超60GB敏感数据

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

鞋类品牌Ecco在500天内泄露超60GB敏感数据

* ![]()
* 关注

* [数据安全](https://www.freebuf.com/articles/database)
* [企业安全](https://www.freebuf.com/articles/es)

鞋类品牌Ecco在500天内泄露超60GB敏感数据

2022-12-22 13:15:52

所属地 上海

12月22日消息，**Cybernews研究人员发现全球鞋类制造商和零售商Ecco，在500天内暴露了数百万份敏感文件，共计60GB**。

Ecco是一家丹麦鞋类制造商和零售商，在全球拥有数千家店铺和销售点。研究人员表示，不仅任何人都可能修改数据，而且**服务器的配置错误很可能会使公司遭受攻击，从而波及世界各地的客户**。

据了解，Ecco从销售数据到系统信息的数百万份敏感文档都处于可在线访问状态，任何有权限的人都可以查看、编辑、复制、窃取或删除数据。

![](https://image.3001.net/images/20221222/1671686149_63a3e80570d44c5565def.jpg!small)Cybernews研究员就此联系了Ecco但未收到回复。但截至发稿，**Ecco似乎已经解决了这个问题**。

研究员称发现一个公开实例，它为Ecco托管了Kibana，Kibana是一个ElasticSearch可视化仪表板。Kibana允许处理ElasticSearch上的信息，ElasticSearch是企业处理大量数据时使用的存储设施。

尽管托管仪表板受超文本传输协议（HTTP）认证保护，但服务器配置错误导致所有应用程序接口（API）请求被允许通过。

研究员通过错误配置的认证在Ecco的ElasticSearch上查找索引名称，查找出50个暴露的索引，有超过60GB的数据。

![](https://image.3001.net/images/20221222/1671686129_63a3e7f1502095c260ab7.jpg!small)研究员称，历史数据表明，自2021年6月4日以来，被暴露的数据库至少有506天是可以访问的。威胁行为者可能通过修改代码、命名和url进行网络钓鱼，或者让受害者在浏览器和设备上安装勒索软件加载程序或远程访问工具，进行远程攻击。

Cybernews研究人员指出，企业应该提高审查安全策略和访问的频率，确保没有不一致的地方，特别是在每次代码推送到实时环境之后。

参考链接：

> https://cybernews.com/security/ecco-leaks-sensitive-data-for-months/

# 数据泄露

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)