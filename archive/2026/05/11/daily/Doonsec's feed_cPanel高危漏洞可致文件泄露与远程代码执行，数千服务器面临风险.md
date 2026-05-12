---
title: cPanel高危漏洞可致文件泄露与远程代码执行，数千服务器面临风险
url: https://mp.weixin.qq.com/s/XB8J58Eh--JnAVefQ7z1jQ
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:34:16.196261
---

# cPanel高危漏洞可致文件泄露与远程代码执行，数千服务器面临风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1EqzFufMW4CAk2c6TI1fNfBRB7l8Sx3a6YLl1dzA1nXicjQUDFtnwzon0ForAaB4iciaabwP7oRNC4Ay2vhjaFpeTC1syGQvZOys/0?wx_fmt=jpeg)

# cPanel高危漏洞可致文件泄露与远程代码执行，数千服务器面临风险

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3iaMdz6DEJkvyQF1k8JAtiaFjIlMH4HleW8Dtibjjo6laJvO5kpwVMuxHWeq3grUvfsKBUaBawWiaUe3iaAItK8ZcFnRBhaOFIzxmM/640?wx_fmt=png&from=appmsg)

##

cPanel已发布安全更新，修复了cPanel & WHM系统中三个可能允许攻击者读取文件、执行代码或提升权限的漏洞。

**Part01**

## ****漏洞详情****

CVE-2026-29201（CVSS评分4.3）：feature::LOADFEATUREFILE管理命令中的输入验证问题，攻击者可利用该漏洞读取服务器上的任意文件。

CVE-2026-29202（CVSS评分8.8）：create\_user API中因plugin参数验证不当导致的关键漏洞。经过身份验证的攻击者可利用此漏洞以受影响账户权限执行任意Perl代码。

CVE-2026-29203（CVSS评分8.8）：不安全的符号链接处理漏洞，用户可能通过chmod更改任意文件权限，导致拒绝服务或权限提升。

**Part02**

**修复版本与背景**

这些漏洞已在多个受支持的cPanel & WHM版本中修复，包括11.136.0.9、11.134.0.25、11.132.0.31及更新版本。WP Squared以及旧版CentOS 6/CloudLinux 6系统也获得了相应更新。

虽然目前尚未发现活跃攻击，但此次漏洞披露恰逢威胁分子将另一个cPanel关键漏洞（CVE-2026-41940）武器化，作为0Day漏洞部署Mirai僵尸网络变种之后。

**Part03**

## ****相关安全事件****

美国网络安全和基础设施安全局（CISA）近期已将Microsoft Defender的一个漏洞（CVE-2026-41940，CVSS评分9.3）列入其已知被利用漏洞（KEV）目录。

网络安全公司watchTowr本周早些时候首次披露该漏洞，并发布工具帮助防御者识别受影响主机。watchTowr在公告中表示："正如我们所述，根据KnownHost的报告，野外利用已经开始。因此我们发布检测工具生成器，帮助防御者识别受影响主机。"

（CVE-2026-41940）是一个影响cPanel和WHM 11.40之后版本的身份验证绕过漏洞。登录流程中的缺陷允许远程攻击者跳过或操纵身份验证检查，无需有效凭证即可访问控制面板。攻击者可能借此管理托管设置、访问敏感数据或控制服务器。

据Shadowserver基金会统计，可能有数千个实例暴露于风险中。cPanel和watchTowr已发布检测工具。相关漏洞利用可追溯至今年二月。域名注册商Namecheap已通知客户采取临时访问限制以降低风险。

**参考来源：**

New cPanel vulnerabilities could allow file access and remote code execution

https://securityaffairs.com/191931/security/new-cpanel-vulnerabilities-could-allow-file-access-and-remote-code-execution.html

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

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