---
title: Cisco SD-WAN vManage 漏洞遭零日攻击利用
url: https://mp.weixin.qq.com/s/whSHR1tk7HAiRhYDLK7zbg
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:02:08.985505
---

# Cisco SD-WAN vManage 漏洞遭零日攻击利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PI3deFbLkAWSK9Esztde5icPEH7Wm3niacOOPStWXnnqFe6iaB0Tet53fiaHotDMzcsN4Ykic6a6GbsChbKl5Ic6LOFkWX6XbEL6jE/0?wx_fmt=jpeg)

# Cisco SD-WAN vManage 漏洞遭零日攻击利用

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

思科披露了其 Catalyst SD-WAN Manager（以前称为 vManage）中的一个严重安全问题，该问题目前正被积极用于零日攻击，引发了全球企业网络环境的担忧。

该漏洞编号为 CVE-2026-20262，是基于 Web 的管理界面中的一个任意文件写入漏洞。其 CVSS 评分为 6.5，源于文件上传操作期间对用户输入内容的验证不当。

思科表示，拥有有效凭证和写入权限的攻击者可以利用此漏洞将精心构造的文件上传到目标系统。一旦被利用，该漏洞允许攻击者在底层操作系统上的任何位置创建或覆盖文件。

## **Cisco SD-WAN vManage 漏洞**

可以利用此功能部署恶意载荷，包括 Web Shell，并有可能将权限提升到 root 级别，从而显著增加攻击的严重性。

思科产品安全事件响应团队 (PSIRT) 确认，截至 2026 年 6 月，该漏洞已在有限的实际应用中被观察到。

这使得该缺陷属于零日漏洞的范畴，攻击者可以在大规模修补之前利用它。

该问题影响 Cisco Catalyst SD-WAN Manager 的所有部署模型，包括本地系统、Cisco SD-WAN 云、Cloud-Pro 和 FedRAMP 环境。

值得注意的是，目前没有其他可行的替代方案，因此立即打补丁是唯一有效的缓解措施。安全研究人员强调，暴露在互联网上的SD-WAN管理接口风险最高。

攻击者可以利用暴露的 API 端点，通过构造 HTTP 请求上传恶意文件。例如，攻击者可以使用目录遍历技术将 WAR 文件上传到敏感目录。思科提供了特定的入侵指标 (IOC)，以帮助企业检测潜在的攻击。

可疑活动可能会出现在日志文件中，例如：

* vmanage-server.log 显示未经授权的文件上传，包括类似“../../../../var/lib/wildfly/standalone/deployments/suspicious.war”的路径。
* vmanage-appserver.log 指示部署了意外的 WAR 文件。
* serviceproxy-access.log 捕获对恶意端点（例如“/suspicious/index.jsp”）的 HTTP POST 请求。

这些日志表明存在后渗透活动，攻击者在系统中部署恶意应用程序并与之交互。

思科澄清说，此漏洞不会直接影响 SD-WAN 流量处理或连接。

然而，管理平面一旦遭到破坏，攻击者就可能篡改配置或保持持续访问权限。为了解决这个问题，思科已在多个软件分支上发布了补丁版本。

强烈建议受影响的用户根据其部署情况升级到修复版本，例如 20.9.9.2、20.12.7.2、20.15.4.5、20.15.5.3、20.18.3.1 和 26.1.1.2。

还鼓励组织审核日志，限制对管理界面的外部访问，并在联系 Cisco TAC 寻求事件响应支持之前使用“request admin-tech”命令收集诊断数据。

该漏洞是在内部安全测试中发现的。然而，它迅速被利用，凸显了暴露的管理接口和不足的输入验证机制所带来的持续风险。

由于没有其他解决办法，而且攻击仍在进行，及时修补漏洞和持续监控对于降低风险仍然至关重要。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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