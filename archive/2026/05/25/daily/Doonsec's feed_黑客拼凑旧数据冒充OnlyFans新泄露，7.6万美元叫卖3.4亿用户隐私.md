---
title: 黑客拼凑旧数据冒充OnlyFans新泄露，7.6万美元叫卖3.4亿用户隐私
url: https://mp.weixin.qq.com/s/jmCNRmYmz09giEoPsJgqZA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T05:59:15.181827
---

# 黑客拼凑旧数据冒充OnlyFans新泄露，7.6万美元叫卖3.4亿用户隐私

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1yviaGicBzDw9rNgQeaL1hqJfRuL53Smq8Jk23CRzVlPCVANnXjujUqoI6HicRFEtwEyEjWbxpISD4qKia66V4d5RImogt2p3iaeCE/0?wx_fmt=jpeg)

# 黑客拼凑旧数据冒充OnlyFans新泄露，7.6万美元叫卖3.4亿用户隐私

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX26eTlxFZcFS4H6MF15kTszDdX7xQaFUiaI3NzkIhEY3nkmBgicrNyfVAA5yo8uzQ44sWV9hib6GyNAICfRcqLQ3rSx3FiavpicyYSY/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3ODt1SZcXkdtkNMoby2xdpgopjGb1Zia6zlk0EaE20xNNnib8jwh0AeIPnKffFxQepGOwzYvcglF08CcUXeAwspa3DMFsQSX8DQ/640?wx_fmt=png&from=appmsg)

一名威胁行为者正在兜售其宣称包含数亿OnlyFans用户（包括内容创作者和订阅者）关联信息的庞大数据库。但通过与卖家的对话及样本数据审查发现，这些数据并非来自OnlyFans系统的直接入侵或爬取。

本周早些时候，该数据在某知名网络犯罪论坛上架。用户“Euphoric\_Reply\_5727”声称提供“3.4亿条OnlyFans用户记录”，标价0.313比特币（约合7.6万美元）。卖家宣称这些数据来自“OnlyFans内部数据库”，包含个人信息、账户活动指标、关联社交资料及支付相关细节。

Part01

卖家否认入侵OnlyFans系统

该数据库广告显示其包含用户名、真实姓名、电子邮箱、电话号码、粉丝数、点赞数、上传内容统计、账户类型及关联社交媒体资料。这些描述最初令人联想到平台遭直接入侵或数据爬取事件。

但通过Telegram直接联系卖家后，对方澄清并未入侵OnlyFans系统。卖家声称该数据库是通过整合Twitter、Instagram和Spotify等平台的历史泄露数据与公开信息构建而成。卖家表示：“我们并未入侵OnlyFans，只是利用现有泄露数据库匹配了平台用户。”

![hacker-selling-onlyfans-user-records-old-breaches-2](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3xndsfIpPrzZrA0F2mogibLa0qA05NbXZQFICHSfDKLQXr7063hmiayB46SMricpp0RhGBQuAA5bsurgqN0DjCLYglxTE3ib73ZjM/640?wx_fmt=jpeg)

威胁行为者分享的截图显示35GB数据，图片来源：Hackread.com

Part02

样本数据揭示真实来源

审查的样本数据显示，该数据集为纯文本格式，包含用户名、邮箱、电话号码、注册日期、粉丝数、点赞数、上传内容统计、关联社交资料和账户类型等字段。部分条目还包含标记为“card”的字段，卖家称这是关联账户支付卡号的后四位。

深入分析发现，样本中存在不完整记录、“None”等占位值，以及本应公开可见的账户指标。其数据格式也与现代消费级平台的内部数据库存储方式存在差异。

![hacker-selling-onlyfans-user-records-old-breaches-3-1536x1233](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX17iadNkqaoAGEicfMjBYuD8ralWRYTXQUhMp6LOTnRxic5hRU8GMj2oZEwa9MB7GS0muvdCwNlBXPMRIlC0vKcL9EsPCpMkxg1x0/640?wx_fmt=jpeg)

威胁行为者发布的帖子，图片来源：Hackread.com

Part03

支付卡信息真实性存疑

验证发现，样本中部分用户名确实对应真实的OnlyFans账户（例如10个UID匹配公开资料），但关联邮箱验证未触发“已注册”提示。关于支付卡后四位数据的真实性，目前既无法证实其来自新泄露，也无法排除是旧数据重复利用。

尽管存在疑问，该数据集仍构成隐私安全威胁。用户名、邮箱、电话号码和社交资料的关联，可能使创作者和订阅者面临钓鱼攻击、勒索、骚扰和身份冒用等风险。此事件反映了威胁行为者通过整合历史泄露数据与公开信息，构建可检索身份数据库的地下产业趋势——其价值往往不在于窃取密码，而在于将网络身份与现实身份相关联。

截至媒体发稿时，该数据仍在售。

参考来源：

Hacker Selling 340 Million OnlyFans User Records Built From Old Breaches

https://hackread.com/hacker-selling-onlyfans-user-records-old-breaches/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1SRP5DY7WibSicW4eWTtYzFWDTfVGMqCQ4UicdvaeHbSfA0ReLjXu6why8RH43kXBsNQ39qgiaxrmAsN9kbEnVENaHKmtQZib2otm8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651338613&idx=1&sn=d0ae0c38319293b058cc4ff73b9319ae&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2SyOCpMWiaRGCVOcBia89UPEschd9VicMFd7SM1rhpC18v24yZmRTYBC8tEqUDDS3qdYSfbjKdJickyhKGibU8gBkvBNA4wk6YmXR4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX10qTyJA57Sdxs0Fr7cHS55CX7gSQjs1wMImiaY3U1oCiaGqo4iawbngLJoKm4SevxGIGDNfAmiaQibqwoF5GUllU6EUicGjXnhv2No8/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1QdwtcGCOOIKBNhvicy3Ybp7zV9077e0Jqlump0dNo07QTSYcDTsb6Dw3kL42v37rbo5dfD9QWIIGUCj0HB03jQTOQqBicVOH4Y/640?wx_fmt=png)

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