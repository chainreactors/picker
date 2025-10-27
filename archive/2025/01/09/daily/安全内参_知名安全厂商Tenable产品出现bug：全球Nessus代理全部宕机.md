---
title: 知名安全厂商Tenable产品出现bug：全球Nessus代理全部宕机
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513446&idx=2&sn=63f3ef7038fb130316964b9c6ae3ef5d&chksm=ebfaf246dc8d7b50abb8f1f3f6013ae35bec54dae84deb7169a14a625c5eaf0a5e52a80c4f29&scene=58&subscene=0#rd
source: 安全内参
date: 2025-01-09
fetch_date: 2025-10-06T20:11:37.301781
---

# 知名安全厂商Tenable产品出现bug：全球Nessus代理全部宕机

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7u0J4bwCgCrFHDvUlyUotUm0Zlxz0SmgL4ZxOabGk7WftdnIRQlp6rMjicCUzgTw6WV4l6k1VIMcrg/0?wx_fmt=jpeg)

# 知名安全厂商Tenable产品出现bug：全球Nessus代理全部宕机

安全内参

**关注我们**

**带你读懂网络安全**

**客户必须手动升级软件，重新启动因插件增量更新问题导致宕机的Nessus 漏洞扫描器代理。**

编译：代码卫士

网络安全公司 Tenable 表示，客户必须手动升级软件，重新启动因插件增量更新问题导致宕机的Nessus 漏洞扫描器代理。

Tenable 公司停止该插件更新以阻止其影响更多的系统，并在一份事件报告中指出，对 “在所有站点上的某些用户”而言，这些代理全部宕机。这一事件影响位于美洲、欧洲和亚洲的更新至 Nessus Agent 10.8.0及10.8.1的客户。该公司已经拉取这些有问题的版本并发布了 Nessus Agent 10.8.2修复了导致代理宕机的问题。

Tenable 公司在最新发布的动态中提到，计划在今天前恢复插件下载内容。该公司在Nessus Agent 10.8.2的发布备注中提到，“一个已知问题可导致 Tenable Nessus Agent 10.8.0和10.8.1在触发一个增量插件更新时宕机。为阻止这一问题，Tenable已披露为这两个代理版本准备的插件更新。另外，Tenable 已禁用 10.8.0和10.8.1版本阻止更多问题的发生。”

**手动升级**

受影响客户必须升级至10.8.2版本或降级至10.7.3版本让 Nessus 代理重新恢复正常，如果代理配置用于升级或降级，则还另需重置插件。

然而，修复该问题需要手动升级使用 Tenable Nessus Agent 10.8.2安装包的代理，在必要时，首先应该使用脚本（已在发布备注中分享）或nessuscli 重置命令重置代理插件。

2024年7月曾发生一起影响更严重的类似事件。CrowdStrike 公司 Falcon 更新问题导致大面积宕机事件发生，影响全球很多组织机构而后服务，包括银行、航空公司、机场、电视台以及医院等。该事件导致全球 Windows 系统出现蓝屏死机事件，导致数十万企业宕机。

原文链接

https://www.bleepingcomputer.com/news/security/bad-tenable-plugin-updates-take-down-nessus-agents-worldwide/

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：代码卫士

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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