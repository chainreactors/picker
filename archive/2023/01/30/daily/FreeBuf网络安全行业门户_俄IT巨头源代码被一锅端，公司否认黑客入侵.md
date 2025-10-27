---
title: 俄IT巨头源代码被一锅端，公司否认黑客入侵
url: https://www.freebuf.com/news/355880.html
source: FreeBuf网络安全行业门户
date: 2023-01-30
fetch_date: 2025-10-04T05:10:39.688198
---

# 俄IT巨头源代码被一锅端，公司否认黑客入侵

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

俄IT巨头源代码被一锅端，公司否认黑客入侵

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

俄IT巨头源代码被一锅端，公司否认黑客入侵

2023-01-29 11:17:05

所属地 上海

![](https://image.3001.net/images/20230129/1674959925_63d5dc358d3fe2ebd4b72.png!small)

俄罗斯最大的IT科技公司之一Yandex的源代码仓库据传遭到前员工窃取，相关数据已在某个流行黑客论坛上以BT种子形式泄露。

1月25日，泄密者发布了一个磁力链接，他们声称这是“Yandex git 源”，其中包含 2022 年 7 月从公司窃取的 44.7 GB 文件。据称，这些代码存储库包含公司除反垃圾邮件规则之外的所有源代码。

![](https://image.3001.net/images/20230129/1674959959_63d5dc577d521749ecf54.png!small)

软件工程师 Arseniy Shestakov 分析了泄露的 Yandex Git 存储库 ，并表示其中包含有关以下产品的技术数据和代码：

* Yandex 搜索引擎和索引机器人
* Yandex 地图
* 爱丽丝（人工智能助理）
* Yandex 出租车
* Yandex Direct（广告服务）
* Yandex 邮件
* Yandex Disk（云存储服务）
* Yandex 市场
* Yandex Travel（旅游预订平台）
* Yandex360（工作区服务）
* Yandex 云
* Yandex Pay（支付处理服务）
* Yandex Metrika（互联网分析）

Shestakov 还在 GitHub 上分享了 泄露文件的目录列表， 供那些想查看哪些源代码被盗的人使用。

“至少有一些 API 密钥，但它们可能仅用于测试部署，”Shestakov 谈到泄露的数据时说。

在一份给媒体的声明中，Yandex 表示他们的系统没有被黑客入侵，一名前雇员泄露了源代码存储库。

> “Yandex 没有被黑。我们的安全服务从公共领域的内部存储库中发现了代码片段，但内容与 Yandex 服务中使用的存储库的当前版本不同。
>
> 存储库是用于存储和使用代码的工具。大多数公司在内部以这种方式使用代码。
>
> 需要存储库来处理代码，而不是用于存储个人用户数据。我们正在对向公众发布源代码片段的原因进行内部调查，但我们没有发现任何对用户数据或平台性能的威胁。”- Yandex。

## 数据泄露的动机是政治性的

记者 还与 Yandex前高级系统管理员、开发副主管兼传播技术总监Grigory Bakunov讨论了此次泄密事件 。他对泄露的代码非常熟悉，曾在 2002 年至 2019 年期间在这家科技巨头工作。

巴库诺夫解释说，数据泄露的动机是政治性的，负责数据泄露的 Yandex 员工并未试图将代码出售给竞争对手。

这位前高管补充说，泄漏不包含任何客户数据，因此不会对 Yandex 用户的隐私或安全构成直接风险，也不会直接威胁泄漏专有技术。

> Yandex 使用名为“Arcadia”的单一存储结构，但并非公司的所有服务都使用它。此外，即使只是构建服务，您也需要大量内部工具和专业知识，因为标准构建程序并不适用。
>
> 泄漏的存储库仅包含代码；另一个重要部分是数据。神经网络的模型权重等关键部分都没有，所以几乎没有用。
>
> 尽管如此，仍有许多有趣的文件，其名称如“blacklist.txt”可能会暴露正在运行的服务。

然而，Bakunov 告诉记者，泄露的代码使黑客有可能识别安全漏洞并创建有针对性的漏洞利用。巴库诺夫认为，现在这只是时间问题。

这位前高管还评论了 Yandex 的回应，称泄露的代码可能与公司工作服务中使用的当前代码不相同，但相似度可能高达 90%。

因此，对泄露代码开展全面检查之后，恶意黑客很可能会从Yandex系统中发现可供利用的缺口。

> 参考来源：https://www.bleepingcomputer.com/news/security/yandex-denies-hack-blames-source-code-leak-on-former-employee/

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

文章目录

数据泄露的动机是政治性的

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