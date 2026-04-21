---
title: NIST放弃全面分析CVE，转向优先处理高危漏洞
url: https://mp.weixin.qq.com/s/-rhWYG9xG6N_6e7XbmyeCA
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:47:08.738268
---

# NIST放弃全面分析CVE，转向优先处理高危漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1xdpmqF6G6Q4OMaORwJpUjV3Tj79BFdliaq1Jy27z84jiaFtHicRTNA2g5IWkRibz7xtTysZy2zbQNzEmNLKDC1t7j6icaNxeQrrF8/0?wx_fmt=jpeg)

# NIST放弃全面分析CVE，转向优先处理高危漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0XPku0rIdg0Z7qhcBI6PP5FVJxLy833lD8zWwCpAvy4T685qrMUdWichol2CoTnLySgnK7Bfumate6EoWmbzTO22s81pHbkYibY/640?wx_fmt=jpeg&from=appmsg)

##

美国国家标准与技术研究院（NIST）宣布对其国家漏洞数据库（NVD）的网络安全漏洞处理机制进行全面改革，放弃对每个提交的通用漏洞披露（CVE）进行全面分析的长期目标，转而采用基于风险的分级评估模型，优先处理最危险的漏洞。

此项改革自今日起生效，主要源于NIST接收的CVE提交量激增。2020至2025年间，CVE提交量增长263%，今年第一季度提交量同比增幅近三分之一。2025年NIST共处理约42,000个CVE，同比增长45%，但处理速度仍无法跟上提交量的增长。新模式下，NIST将仅对符合以下三项标准之一的CVE进行完整分析：

* 被列入美国网络安全和基础设施安全局（CISA）已知已利用漏洞（KEV）目录的漏洞
* 影响联邦政府使用软件的CVE
* 根据14028号行政命令被归类为关键软件的CVE

在新机制下，NIST目标是在收到KEV目录条目后一个工作日内完成分析。其他已报告的CVE仍会保留在NVD中，但将被标记为"未计划分析"状态，意味着NIST不会自动添加安全团队用于补丁优先级判定的严重性评分和产品数据。

NIST同时着手清理自2024年初积压的漏洞。所有在2026年3月1日前发布且未完成分析的CVE将被移入"未计划分析"类别，仅在有资源时才会考虑处理（KEV目录中的CVE除外）。

新模型还包含两项流程变更：当CVE编号机构（CNA）已提供严重性评分时，NIST不再重复评估；对于修改后的CVE，仅当变更实质影响分析数据时才会重新评估，而非每次更新都自动重新分析。

身份威胁检测与响应提供商SlashID公司CEO兼联合创始人Vincenzo Iozzo指出，人工智能是推动CVE提交量激增的关键因素之一："AI报告的有效漏洞数量急剧上升，仅去年报告量就翻倍有余。NIST的新政策具有合理性，其保留分析的类别正是最关键的漏洞类型。"

网络安全解决方案公司RunSafe Security首席技术官Shane Fry认为："该公告向行业释放信号——等待CVE评分再采取行动的时代已经终结。漏洞可见性本不完美，采用多元化漏洞数据源的企业将获得更可靠的漏洞洞察。更重要的是，企业应假设软件中已存在未知漏洞，并部署能在补丁或CVE评分发布前阻断攻击的防护措施。"

**参考来源：**

NIST shifts National Vulnerability Database to risk-based triage as CVE submissions hit record levels

https://siliconangle.com/2026/04/15/nist-shifts-national-vulnerability-database-risk-based-triage-cve-submissions-hit-record-levels/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1O8uucFibpl8PczsdFCl05VYJ6SAC0hbGnY2ORo3zp7cw9tGtthViaRCO0qTggMtiampGyl7T4RbMmFXECrOhAnNwzV3vBWEBFN0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337048&idx=1&sn=7238361cc36d8446dbd7c8ed85cb2f42&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3spxg6eNGaglroiaTIHUKMic8uvvkEeAsNmnn8AeHsjRKujlaUPiavLo83wZqicrvkLP3s98KWBBVmvIbicPOpAwgU4qInObvQnvwo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

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