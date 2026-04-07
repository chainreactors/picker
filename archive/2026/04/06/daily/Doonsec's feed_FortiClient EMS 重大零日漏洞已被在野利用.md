---
title: FortiClient EMS 重大零日漏洞已被在野利用
url: https://mp.weixin.qq.com/s/2_iivzfMZppd9n-9r8JyoQ
source: Doonsec's feed
date: 2026-04-06
fetch_date: 2026-04-07T04:27:15.096568
---

# FortiClient EMS 重大零日漏洞已被在野利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2TeFG7I0LSXz3ibKmb1GOlxpgEibUsebGd92Y1KM1nqINnY4icC2CzFsphKRvicarlbwxJIiaE4ZFORuBqCQz18Ul26kSsEZyhzZog/0?wx_fmt=jpeg)

# FortiClient EMS 重大零日漏洞已被在野利用

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3KTg0IOe9g5kPIe0ycxmqeqBfic3glRWJbU9atqGfsJJqEA0zf8qAzbbw737KrjNNpu6bFNoAahKZOfC1iaiavBqLiaLSwwDDZS9o/640?wx_fmt=png&from=appmsg)

Fortinet在安全研究人员披露其 FortiClient EMS 存在**重大零日漏洞**后紧急发布了热修复程序，该漏洞目前已遭到威胁行为者的主动利用。

该漏洞编号为 **CVE-2026-35616**，CVSSv3 评分为 **9.1 分（严重）**。攻击者可在**无需身份验证**的情况下，完全绕过 API 认证与授权控制机制，进而在存在漏洞的系统上执行任意代码或命令。

此漏洞归类为 **CWE-284（访问控制不当）**，存在于 FortiClient 终端管理服务器（EMS）的 API 模块中。

漏洞被成功利用**无需预先身份验证、无需用户交互，也无需提升权限**，这使得将 EMS 暴露在公网的机构面临极高风险。

未经过身份验证的远程攻击者可发送精心构造的 API 请求，绕过所有认证与授权校验，从而**完全接管终端管理操作权限**。

该漏洞利用方式基于网络，利用难度低，且对数据的机密性、完整性和可用性均造成严重影响，这也是其获得接近满分 CVSS 评分的直接原因。

**Part01**

## ****受影响版本与修复方案****

##

## 仅 **FortiClient EMS 7.4.5 和 7.4.6 版本**受该漏洞影响。

##

## **FortiClient EMS 7.2.x 系列不受影响**，无需采取任何操作。

##

## 即将发布的 **FortiClient EMS 7.4.7**将包含永久性修复方案；在该版本正式发布前，Fortinet已为上述两个受影响版本分支**立即推出了紧急热修复补丁**。

##

**Part02**

## ****漏洞发现与披露情况****

该漏洞由威胁情报公司 Defused 的研究员西莫・科霍宁（Simo Kohonen）与独立研究员阮德英（Nguyen Duc Anh）共同发现。

本周早些时候，Defused 监测到该漏洞已在野外被**主动利用**，随后按照**负责任漏洞披露流程**向Fortinet进行了上报。此次发现借助 Defused 即将于下周上线的 **Radar 功能**实现，该工具旨在实时发现新型漏洞利用活动。

Fortinet的安全公告（FG-IR-26-099）中指出，该漏洞的主要影响为**权限提升**，厂商已证实该漏洞在野外环境中已被**主动利用**。

![1775458396_69d3585c8149b2316695c.png!small?1775458397007](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2tkjSzP7keagWULIeGTFbjD3lUkRffVdFF32llDPFxQalAKKIYQc8A5ODsTJT8uPszicmFgxWyVZZiafrKeuhib3nnfjMdLCIF4U/640?wx_fmt=jpeg&from=appmsg)

收到报告后，Fortinet公司迅速响应，于**2026 年 4 月 4 日**发布了安全公告并推出紧急热修复程序，与该漏洞首次公开披露为同一天。

**Part03**

## ****官方修复建议与防护措施****

##

Fortinet强烈敦促所有使用受影响版本的客户**立即安装此紧急热修复程序**。各受影响版本的详细安装说明，可在官方 FortiClient EMS 版本发布说明中查阅：

* FortiClient EMS 7.4.5：请通过飞塔文档门户，参考 7.4.5 版 EMS 发布说明中的热修复安装指南
* **FortiClient EMS 7.4.6：请通过飞塔文档门户，参考 7.4.6 版 EMS 发布说明中的热修复安装指南**

各机构还应**监控 EMS 日志**，留意异常的 API 行为，尤其是未经过身份验证的请求，这类请求可能表明此前已存在漏洞利用尝试。

在完成补丁修复期间，如有可能，**在网络边界限制对 EMS 管理界面的外部访问**，可有效增加一层重要的安全防护。

**参考来源：**

Critical Fortinet FortiClient EMS 0-Day Vulnerability Actively Exploited in the Wild

https://cybersecuritynews.com/fortinet-forticlient-ems-0-day/

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