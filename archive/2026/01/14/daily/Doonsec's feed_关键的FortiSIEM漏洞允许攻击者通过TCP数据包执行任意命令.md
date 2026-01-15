---
title: 关键的FortiSIEM漏洞允许攻击者通过TCP数据包执行任意命令
url: https://mp.weixin.qq.com/s/QnyzSIVUuNWYE15IivvDkA
source: Doonsec's feed
date: 2026-01-14
fetch_date: 2026-01-15T03:29:28.756567
---

# 关键的FortiSIEM漏洞允许攻击者通过TCP数据包执行任意命令

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qzzQsdHFQcCtJibgf7DL61ftlyUjItF7oheapmIMpDNY6fiaW6Wuykw6lxu6M5nicnNsuibYks319dtBw/0?wx_fmt=jpeg)

# 关键的FortiSIEM漏洞允许攻击者通过TCP数据包执行任意命令

原创

O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzzQsdHFQcCtJibgf7DL61ft0eMpG1jeKx6wwujOiazj8mQYUdPbmflTNsaPSjYw5kwr1DicWby7Hdlg/640?wx_fmt=png&from=appmsg)

Fortinet 于 2026 年 1 月 13 日披露了 FortiSIEM 中的一个关键作系统命令注入漏洞，警告用户存在一个高风险漏洞，该漏洞允许未经认证的攻击者执行任意代码。

该问题被追踪为CVE-2025-64155，源于phMonitor组件7900端口中作系统命令（CWE-78）中特殊元素的不当中和。攻击者可以对超级节点和工人节点发放恶意 TCP 请求，可能导致整个系统被攻破。

该漏洞基于 CVSS v3.1 基础评分为 9.4（AV：N/AC：L/PR：N/UI：N/S：U/C：H/I：H/A：H），因其网络可访问性、低复杂性及缺乏必要权限，被评为“危急”。

无需用户交互，利用可能导致远程代码执行、数据盗窃或在依赖FortiSIEM进行安全信息和事件管理的环境中存在持久化。

## **受影响版本及修复**

该缺陷影响多个FortiSIEM分支，但收集器节点不受影响。Fortinet敦促立即升级或迁移，通过防火墙限制TCP 7900端口的访问作为变通方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qzzQsdHFQcCtJibgf7DL61ftUmzfiaI8FrlOPw1VOwwWWp2G5ePP2C1GMzYhAickAAzsIyoMOZKevrrw/640?wx_fmt=png&from=appmsg)

在生产环境中运行易受攻击版本的组织面临较高风险，尤其是在混合或本地部署SIEM时。

Horizon3.ai 的安全研究员Zach Hanley（@hacks\_zach）负责任地报告了Fortinet程序下的漏洞。该通告（FG-IR-25-772）已发布在Fortinet的PSIRT页面上，NVD细节尚待全面分析。目前尚无积极利用的证据浮现，但未经认证的特性要求紧迫性。

Fortinet 建议审计异常 TCP/7900 流量日志并及时安装补丁。此事件凸显了SIEM架构中最低权限网络分段的必要性。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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