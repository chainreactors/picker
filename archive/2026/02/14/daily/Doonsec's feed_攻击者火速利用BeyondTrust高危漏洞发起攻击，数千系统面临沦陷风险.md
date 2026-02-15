---
title: 攻击者火速利用BeyondTrust高危漏洞发起攻击，数千系统面临沦陷风险
url: https://mp.weixin.qq.com/s/GqQco2Ku7kBKFvXmUvsInA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:17:19.627792
---

# 攻击者火速利用BeyondTrust高危漏洞发起攻击，数千系统面临沦陷风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1VwYDe0eGAicY1byHiaKOdzia9lKTbHKYJklsd4nfv4f4KNy2lzbWXghAzlloUpRh2cRe4ib4icBPx1rzllhEm1B6pHpUicpEduiaSbs/0?wx_fmt=jpeg)

# 攻击者火速利用BeyondTrust高危漏洞发起攻击，数千系统面临沦陷风险

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3AkIOjC2Y4URfXgsuQYelRxCVlFBmCmjrYoYJB4Fg4MxWTIUdtJtfZur0tD4iatZOXv2qZTIro0urZSYYfBdkkNd7QNLQWU81E/640?wx_fmt=jpeg&from=appmsg)

**Part01**

## ****漏洞概括****

在PoC漏洞利用代码公开后，攻击者迅速针对BeyondTrust的关键漏洞（CVE-2026-1731）发起攻击，该漏洞可实现未经认证的远程代码执行。威胁行为体在概念验证（PoC）利用代码公开后，立即开始利用这个新修复的高危漏洞（CVSS评分9.9）。

本周BeyondTrust发布了安全更新，修复其远程支持（Remote Support）和旧版特权远程访问（Privileged Remote Access）产品中的关键缺陷。该漏洞允许未经认证的攻击者发送特制请求，无需登录即可远程执行操作系统命令。这个于2026年2月6日披露的漏洞若被利用，可能导致完全远程代码执行，因此更新补丁对防止滥用至关重要。

**Part02**

## ****技术细节****

BeyondTrust在安全公告中警告："BeyondTrust远程支持（RS）和某些旧版特权远程访问（PRA）存在关键的身份认证前远程代码执行漏洞。未经认证的远程攻击者通过发送特制请求，可能以站点用户身份执行操作系统命令。"

成功利用该漏洞可使远程攻击者无需认证或用户交互即可运行系统命令，可能导致系统完全沦陷、数据窃取和服务中断。公告进一步指出："成功利用无需任何认证或用户交互，可能导致系统被入侵，包括未授权访问、数据外泄和服务中断。"

**Part03**

## ****影响范围****

BeyondTrust于2月6日发布CVE-2026-1731补丁，此前Hacktron研究人员警告称有数千个实例暴露在互联网上。Hacktron AI团队报告显示，约11,000个BeyondTrust远程支持实例暴露在云端和本地环境中，其中约8,500个为本地系统，若未打补丁将保持脆弱状态。受影响部署主要集中于医疗保健、金融服务、政府和酒店行业的大型企业。

**Part04**

## ****攻击态势****

2月10日PoC利用代码公开后，GreyNoise在24小时内检测到攻击尝试，其中单个IP地址承担了大部分侦察活动。GreyNoise报告称："2月10日，针对BeyondTrust远程支持和特权远程访问中关键身份认证前远程代码执行漏洞（CVE-2026-1731）的PoC利用代码被发布到GitHub。截至2月11日，GreyNoise全球观测网格已记录到针对脆弱BeyondTrust实例的侦察探测。"

GreyNoise观察到针对CVE-2026-1731的快速侦察活动，其中单个IP承担了86%的扫描量。该活动源自长期运行的扫描操作，使用商业VPN和基于Linux的工具。威胁行为体主要探测非标准端口，表明其知晓企业会将BeyondTrust服务从443端口迁移。JA4+指纹显示存在共享的漏洞利用工具和VPN隧道。

**Part05**

## ****威胁关联****

同一批IP还针对SonicWall、MOVEit、Log4j、Sophos、SSH和IoT设备，表现出多重漏洞利用行为。BeyondTrust工具是高价值目标，即使新变种快速出现，过往的0Day攻击链仍保持活跃。报告总结道："执行CVE-2026-1731侦察的IP并非单一用途。虽然其BeyondTrust活动属于检查（枚举）行为，但GreyNoise档案显示它们同时针对其他产品进行主动利用尝试：SonicWall、MOVEit Transfer、Log4j、Sophos防火墙、SSH暴力破解和IoT默认凭证测试。部分IP甚至使用带外回调域（OAST）这种更复杂的技术，在投递有效载荷前确认漏洞存在。"

**参考来源：**

Attackers exploit BeyondTrust CVE-2026-1731 within hours of PoC release

https://securityaffairs.com/187962/uncategorized/attackers-exploit-beyondtrust-cve-2026-1731-within-hours-of-poc-release.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

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