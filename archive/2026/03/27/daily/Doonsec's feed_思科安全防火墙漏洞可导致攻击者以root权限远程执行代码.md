---
title: 思科安全防火墙漏洞可导致攻击者以root权限远程执行代码
url: https://mp.weixin.qq.com/s/iINM32Qqy-AX0CDdTouFIw
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:13.812912
---

# 思科安全防火墙漏洞可导致攻击者以root权限远程执行代码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3BaqP450soBtzGAB0GCibNmxwbxQUcXDpXksNnzsvLGecqzMZ5aSsoxBODmhx5olNW5zibfyXF89gNYM3Yc6Soy07Gpl0bysxnE/0?wx_fmt=jpeg)

# 思科安全防火墙漏洞可导致攻击者以root权限远程执行代码

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX112QMIomGFETibtIicfgoAPwwY10zoBNaRGJaic9g339ZUsE6iaZMBV0X9xF9CXibCDw8MSwSCCas4Q3AydLMVqxy1yqVqiaLnxEc8I/640?wx_fmt=jpeg&from=appmsg)

##

思科发布紧急安全公告，披露其安全防火墙管理中心（Secure Firewall Management Center，FMC）软件存在一个高危漏洞。该严重漏洞允许未经身份验证的远程攻击者以完整 root 权限执行任意代码。

##

**Part01**

## ****漏洞详情****

编号为 CVE-2026-20131 的漏洞源于不安全的反序列化问题（CWE-502），CVSS 评分为 10.0 分。攻击者无需任何权限即可远程利用此漏洞。该安全缺陷存在于思科安全 FMC 的基于 Web 的管理界面中，直接由用户提供的 Java 字节流的不安全反序列化导致。

攻击者只需向存在漏洞的 Web 界面发送特制的序列化 Java 对象，即可利用此弱点。若利用成功，攻击者可直接在目标设备上执行任意 Java 代码，从而将系统权限提升至完整 root 访问权限。

**Part02**

## ****潜在危害****

获取核心管理系统的 root 访问权限极其危险，攻击者可借此修改安全控制措施、禁用防御机制，并为后续更深层次的网络攻击建立持久立足点。

**Part03**

## ****漏洞发现与利用情况****

该高危漏洞最初由思科高级安全计划小组的 Keane O'Kelley 在内部安全测试中发现。但近期情况升级，思科更新官方公告确认，其产品安全事件响应团队（PSIRT）在 2026 年 3 月已发现该漏洞在野被利用的尝试。

**Part04**

## ****风险提示****

由于此攻击无需用户交互且无需事先认证，具有面向公众管理界面的系统面临极高风险。思科强烈建议限制 FMC 管理界面的公共互联网访问，这将显著减少暴露的攻击面。但该措施不能替代立即打补丁的必要性。

**Part05**

## ****缓解措施****

该漏洞影响思科安全 FMC 软件和思科安全云控制（SCC）防火墙管理平台，与设备配置无关。需注意的是，思科已确认安全防火墙自适应安全设备（ASA）和安全防火墙威胁防御（FTD）软件系列不受此特定问题影响。

对于 SaaS 交付的 SCC 防火墙管理环境，思科已在例行维护期间部署了必要的安全修复，这意味着云客户无需采取额外措施。但对于本地部署，目前没有任何临时缓解措施可用，企业必须立即应用思科提供的官方安全更新。

管理员应使用思科软件检查工具验证其确切软件版本，并立即升级存在漏洞的系统。

**参考来源：**

Cisco Secure Firewall Vulnerability Allows Remote Code Execution as Root User

https://cybersecuritynews.com/critical-cisco-secure-firewall-vulnerability/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

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