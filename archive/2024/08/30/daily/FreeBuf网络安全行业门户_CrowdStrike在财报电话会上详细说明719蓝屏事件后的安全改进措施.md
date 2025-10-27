---
title: CrowdStrike在财报电话会上详细说明719蓝屏事件后的安全改进措施
url: https://www.freebuf.com/news/409805.html
source: FreeBuf网络安全行业门户
date: 2024-08-30
fetch_date: 2025-10-06T18:04:54.605853
---

# CrowdStrike在财报电话会上详细说明719蓝屏事件后的安全改进措施

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

CrowdStrike在财报电话会上详细说明719蓝屏事件后的安全改进措施

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

CrowdStrike在财报电话会上详细说明719蓝屏事件后的安全改进措施

2024-08-29 18:27:08

所属地 上海

北京时间今天凌晨，在CrowdStrike2025财年第二季度的财报电话会上，董事长兼CEO，也是联合创始人的George Kurtz开场就用大量篇幅介绍了7月19日因监测规则升级事故而导致大量Windows主机蓝屏事件的情况。针对这一事件，CRWD采取了四项改进措施：

1. **增强规则更新的透明性和可控性**：此前用户只能控制版本更新，现在他们也可以配置规则更新了，用户通过新的细化控制功能可以选择何时何地部署新的规则内容。
2. **加强规则的质量控制**：8月初，CRWD正式推出了新的规则验证器和规则解释器。此前的安全事件与这两个组件未能正常工作有关。现在，这两个组件已经被重构，以防止错误内容的发布。
3. **外部审查和验证**：CRWD聘请了两家独立的第三方软件安全公司来审查Falcon终端传感器的代码和质量控制流程。该项工作将持续进行，旨在短期、中期和长期内提升安全性和弹性。
4. **调整规则发布流程**：与传感器版本的发布流程一致，新的规则发布流程包括样本测试、内部实验室测试等分阶段测试，最终部署将分批次进行，并遵循客户的策略设置。

其中，第一项和第四项改进措施在8月6日发布的事故审查初步报告中已有披露，这些措施有望大幅减少未来类似事故的影响范围和破坏程度。与之相反的是，7月19日的规则更新在短短78分钟内就被推送到了超过850万台Windows主机上，极大的扩大了此次事故的影响范围。

第二项和第三项改进措施旨在降低未来发生类似事故的可能性。第二项措施的重点是重构规则解释器，并引入更强的规则检测能力，以避免执行有问题的新规则。至于第三项措施，我感到有些意外，但它显示了CrowdStrike对提高透明度的承诺。

![1724927349_66d04d75eeb6cac9e264d.png!small](https://image.3001.net/images/20240829/1724927349_66d04d75eeb6cac9e264d.png!small)

尽管发生了719事件，CrowdStrike在2025财年第二季度的表现依然非常亮眼。季度末年经常性收入ARR同比增长32%，达到38.6亿美元，经营利润率为24%，"Rule of 40"指标高达60。

表面上看，CRWD似乎没有受到719事件的影响，但这主要是因为其第二财季结束于7月底，事件的影响尚未完全显现。在财报电话会上，CFO给出的下季度收入指引是9.79到9.85亿美元，仅比本季度的9.64亿美元略高。而第一季度CrowdStrike的收入为8.72亿美元。粗略估算，719事件对第三季度收入的影响可能接近1亿美元，拉低收入近10个百分点。

![1724927355_66d04d7bcb3e7dd571bf7.png!small](https://image.3001.net/images/20240829/1724927355_66d04d7bcb3e7dd571bf7.png!small)

在股价方面，719事件发生后，CRWD的股价从343.05美元下跌至8月2日的最低点217.89美元，下滑了36.5%，目前股价刚恢复到260美元左右。尽管George Kurtz表现出极大的信心，但显然CrowdStrike要完全走出此次事件的阴影仍需时日。

# CrowdStrike # 安全事故

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