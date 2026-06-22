---
title: 任天堂美国员工数据遭泄露，第三方HR平台被勒索组织攻破
url: https://mp.weixin.qq.com/s/NQnCMaeFiBVCXQbJ7waKhQ
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:39.216753
---

# 任天堂美国员工数据遭泄露，第三方HR平台被勒索组织攻破

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0PJ2V4ZxQDlqDHAo5DQPWFK19zmticM8lj04ByGtzHBibuPqyVGibZxhRIefiaI7gQW7V5FGibOgBCC00TYXlGc3JiaIEzAMAzeQ0EI/0?wx_fmt=jpeg)

# 任天堂美国员工数据遭泄露，第三方HR平台被勒索组织攻破

FreeBuf
FreeBuf

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX3MtTjZy6riaMffabKttpqU2N0Vo3gz8RCkzLsB7uRQ44QS9kahAr5MVuQl5YHe27ntm0XkG4meclXOMUZdfjx0B5XGxAMFy6yI/640?wx_fmt=gif)

第三方人力资源平台TinyPulse遭遇供应链攻击，导致任天堂美国分公司员工记录遭窃。在臭名昭著的Shadowbyt3$勒索组织发布声明后，任天堂已确认此次数据泄露事件。

攻击者并未突破任天堂自身网络边界，而是入侵了TinyPulse的云环境。该平台由WebMD Health Services运营，主要提供员工调查、反馈及劳动力分析服务。由于TinyPulse汇总了大量客户企业的员工指标和人事信息，其基础设施存储着海量可识别身份的员工数据。

![TinyPulse攻击示意图](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3QkiaH5E3m5Zia2zUtGzHzibpovPMP9oOj57OC2NhmShd611DiaRev3kttqZh0HroucgMWvtpc1WiczD31acWjrfyl35vURicBDelib8/640?wx_fmt=jpeg)

Part01

攻击细节与责任归属

2025年10月出现的勒索即服务组织Shadowbyt3$于2026年6月12日宣称实施此次攻击，并向任天堂索要200万美元赎金以阻止数据公开。该组织给出48小时支付期限，但这家游戏巨头拒绝谈判。

在任天堂拒绝付款后，Shadowbyt3$转而向TinyPulse提出经济要求，设定6月16日为第二期限。期限届满未获支付，该组织开始在其暗网平台泄露数据样本。

Shadowbyt3$声称窃取了859MB数据集（涵盖2016至2026年初记录），而任天堂官方声明称泄露数据仅限于往年部分内部员工调查反馈。黑客仍坚称文件包含：

* 银行对账单PDF
* 员工姓名与企业邮箱
* 含员工识别号的W-9税务表格
* 员工间私信及内部聊天记录
* 人力资源分析报告与员工发展计划

安全专家已验证泄露样本中多名可识别人员确系任天堂美国现职员工。

![Shadowbyt3$暗网泄露站点](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3LNTaaWiaHX8DNTibzsIib7VFoic0Ak2V85s1nDyh301KaW3N6sibRxXanq904oTYuH9uY5zcvic2R8JtlMCTGUibVKJHn6ByxKGZj9A/640?wx_fmt=jpeg)

Part02

企业员工面临的持续安全风险

W-9税务文件与财务记录泄露将带来长期身份盗用风险，黑客常利用此类信息提交欺诈性纳税申报并截留退税款。同时，精准的银行信息可被用于制作针对性钓鱼邮件。

由于TinyPulse采用多租户软件架构服务数百家企业客户，使用该平台的其他企业可能面临类似数据泄露风险。

任天堂确认事件影响范围仅限于美国分公司员工，但仍建议所有使用TinyPulse平台的员工立即在Equifax、Experian和TransUnion等征信机构设置信用冻结，并密切监控纳税申报是否存在未授权变更。

参考来源：

Nintendo America Employee Data Exposed After Shadowbyt3$ Targets TinyPulse

https://hackread.com/nintendo-america-employee-data-shadowbyt3-tinypulse/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1X4enJ3Jg430Lq35ib6TKMfwMWPxpHxMTQkuB9iaHj8Dj755KsjMFZvicpFQEoIcZc5MiblY9MAMfKjrACxXChC1QibqxBjRdYoSAM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3X7WGI2rXPqAzCWXrGjRKsN5yjUV9BoibElELIHDAkotuemLyRebpuqevWQ5EkFXCsicicbVEnB6iaAgd8a7hBYX4m430XS37O4CQ/640?wx_fmt=png)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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