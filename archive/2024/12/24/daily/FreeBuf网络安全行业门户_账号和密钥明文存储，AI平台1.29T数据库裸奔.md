---
title: 账号和密钥明文存储，AI平台1.29T数据库裸奔
url: https://www.freebuf.com/news/418279.html
source: FreeBuf网络安全行业门户
date: 2024-12-24
fetch_date: 2025-10-06T19:40:05.229190
---

# 账号和密钥明文存储，AI平台1.29T数据库裸奔

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

账号和密钥明文存储，AI平台1.29T数据库裸奔

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

账号和密钥明文存储，AI平台1.29T数据库裸奔

2024-12-23 10:49:05

所属地 上海

### 核心摘要

* 未加密数据库泄露：Builder.ai 一个未加密的数据库被公开访问，包含超过300万条记录，总计1.29TB，导致客户和内部数据泄露。
* 敏感信息外泄：泄露信息包括发票、保密协议、税务文件、电子邮件截图和云存储密钥，使客户个人信息和公司内部运作面临风险。
* 潜在攻击风险：泄露可能导致钓鱼攻击、伪造发票欺诈、未经授权访问云存储，并对Builder.ai的声誉造成损害。
* 响应迟缓：Builder.ai在接到通知后近一个月才采取措施保护数据库，引发对其应急响应能力的质疑。

近日，网络安全研究员Jeremiah Fowler透露，一家总部位于英国伦敦的人工智能开发平台Builder.ai，由于数据库配置错误，该平台遭遇了重大数据泄露事件，共计泄露数据超过300万条，1.29TB。

Builder.ai是Microsoft Power Platform的一部分，在全球多个地区设有分支机构，它允许企业通过自动执行流程和预测结果来提高业务绩效。Builder.ai可以与Microsoft Dataverse以及各种云数据源（如SharePoint、OneDrive或Azure）集成，方便用户访问和管理业务数据。Builder.ai提供了多种预生成的AI模型，用户可以直接使用这些模型，而无需从头开始构建，用户可以根据业务需求创建自定义的AI模型，用于分析文本、图像、结构化数据等。

根据Fowler在Website Planet的报告，泄露的敏感信息包括客户成本提案、保密协议、发票、税务文件、内部沟通记录、秘密访问密钥、客户个人信息以及电子邮件往来截图。数据库中约有337434个发票（18GB）和32,810个文件（4GB），标记为主服务协议。

![](https://image.3001.net/images/20241223/1734922058_6768cf4ada65c700cab21.png!small)![](https://image.3001.net/images/20241223/1734922068_6768cf54262b8e758b78e.jpg!small)![](https://image.3001.net/images/20241223/1734922079_6768cf5f3cd02536c0838.jpg!small)

“将文档和访问密钥以明文形式存储在同一数据库中，可能造成严重的安全漏洞。如果数据库意外曝光或被未经授权访问，恶意攻击者可能利用这些密钥访问链接系统、云存储或其他敏感资源，无需额外身份验证。”

数据库配置错误是常见问题，但最新报告显示，即使是ShinyHunters和Nemesis这样的黑客组织也在积极入侵暴露的数据库，这表明如果数据库落入恶意威胁攻击者手中，可能会危及公司声誉和用户隐私。

泄露的文档对黑客来说是宝贵的资源，可以用于社交工程攻击。例如制作含有恶意软件的虚假发票，以欺骗Builder.ai的客户。此外数据中的内部信息可能被用来对Builder.ai员工发起有针对性的钓鱼攻击，泄露的云存储访问密钥还可能允许未经授权访问其他位置存储的更敏感数据。

更糟糕的是，Builder.ai 应急响应流程十分迟缓。在研究人员通知后，Builder.ai花了整整一个月才保护数据库，并称“复杂的系统依赖”是延迟的原因。尽管解释不够明确，但这表明数据库曝光可能涉及第三方承包商。

研究人员强调，在构建系统时减少依赖性的重要性，以避免妨碍应急响应。为了最小化风险，Fowler建议组织应安全存储管理凭据和访问密钥，对其进行加密，存储在专用系统中，并与其他敏感数据隔离，以防止被利用。

参考来源：<https://hackread.com/builder-ai-database-misconfiguration-expose-tb-records/>

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