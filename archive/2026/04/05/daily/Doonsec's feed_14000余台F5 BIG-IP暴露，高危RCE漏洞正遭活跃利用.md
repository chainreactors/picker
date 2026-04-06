---
title: 14000余台F5 BIG-IP暴露，高危RCE漏洞正遭活跃利用
url: https://mp.weixin.qq.com/s/GMm9Kggk-68BhwVkT0XLqQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:39:55.491062
---

# 14000余台F5 BIG-IP暴露，高危RCE漏洞正遭活跃利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2zibt2GP3YicgmiaJjdaJJqzqP9lk2RmjzmGo7cV9wz0RvRARlNTsGicUlJicdGtxrmuVxKG2rUbBCvXDnr2PMd7FEdFXUaicUMdZMA/0?wx_fmt=jpeg)

# 14000余台F5 BIG-IP暴露，高危RCE漏洞正遭活跃利用

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX28rvMrcIwjqnuFUgZI6RNKpyx6kXtychL9QbX8dxOYwK8fv7WpnByjvhbXX4Cyd2gZ2vE0LMA52wyTTajtRdVujqm9QBpO5cA/640?wx_fmt=png&from=appmsg)

##

F5 BIG-IP访问策略管理器（APM）的关键安全漏洞正遭活跃利用，致使数以千计的企业网络面临风险。该漏洞被官方标记为（CVE-2025-53521），当其影响从标准拒绝服务（DoS）升级为严重远程代码执行（RCE）漏洞后，立即引发网络安全界的紧急警报。

美国网络安全与基础设施安全局（CISA）已将该漏洞列入其已知 exploited漏洞目录，要求立即采取行动。Shadowserver基金会提供的遥测数据显示，2026年3月31日研究人员在全球范围内识别出超过17,100个暴露的F5 BIG-IP APM实例。尽管部分组织已开始部署修复措施，仍有超过14,000套系统完全暴露在公共互联网中。根据设备地理分布图谱，美国和日本的受影响实例最为集中。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3qc5aV85JmgjS5rhibMqwzWFUPew95wSasP4pr1jVbhOoyibyRDselN3zoEfGialJL9NZU95ldhTyrzjicYfkCTJgtxMDiaE9OeCT8/640?wx_fmt=jpeg&from=appmsg)

由于BIG-IP APM作为企业应用访问的安全网关，成功利用该漏洞的攻击者可绕过企业边界防护，直接渗透内部网络。

##

**Part01**

## ****补丁延迟的严重后果****

漏洞最初被归类为DoS问题是造成大规模暴露的主因。F5首次披露（CVE-2025-53521）时仅将其评定为DoS漏洞，在企业环境中，此类漏洞的修补优先级通常低于直接入侵威胁。VulnTracker安全研究人员指出，许多IT团队可能为处理更紧急的警报而暂缓部署该补丁。

当威胁行为体发现可将该漏洞武器化以实现任意远程代码执行后，滞后的补丁部署演变为重大安全隐患。攻击者通过此RCE漏洞可完全控制F5设备，进而实施数据窃取、勒索软件投放或深度网络驻留。

**Part02**

## ****紧急应对措施****

运行F5 BIG-IP APM服务的组织必须将此视为"立即修补"级事件，安全团队应采取以下措施：

* 应用厂商更新：立即查阅F5更新的安全公告（K000156741），将所有BIG-IP APM实例升级至最新修补版本
* 假定失陷并排查：鉴于漏洞正遭活跃利用，仅打补丁已不足够，管理员需彻底审查系统日志并主动搜寻入侵指标（IoCs）
* 审计外部资产：使用网络监控工具确保识别所有面向互联网的APM接口，并实施安全配置

（CVE-2025-53521）从可控DoS漏洞迅速升级为活跃利用的RCE漏洞，这一演变过程深刻警示着现代威胁态势的急速变化。

**参考来源：**

14,000+ F5 BIG-IP APM Devices Exposed Online Amid Active RCE Vulnerability Exploits

https://cybersecuritynews.com/14000-f5-big-ip-apm-exposed-online/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1df9O3S7TcqYQ5TtfibKYusLhstH06qHkXsM712er2kqnjI8bykhu6xWMFStgejUxm8xOIKU6ibAmY2cojOAEcd3IawxVWR9UcM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651336627&idx=1&sn=980bb90fbcbc3a4df630ccd700eefbcf&scene=21#wechat_redirect)

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