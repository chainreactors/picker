---
title: OpenClaw 曝出四大漏洞，可导致数据窃取、权限提升与持久化攻击
url: https://mp.weixin.qq.com/s/Wxqixof2NyhiaNhlVHEa5g
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:07.547255
---

# OpenClaw 曝出四大漏洞，可导致数据窃取、权限提升与持久化攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1AFibxhnQaOFlqnwkYZEzlND4vQr58IPxlu2ibxcfZ3zN7wL4MPvSb8CaVWmlNMYF0cAFGdvor6Wznzm0xTE5A1noxuRMGt9Ueo/0?wx_fmt=jpeg)

# OpenClaw 曝出四大漏洞，可导致数据窃取、权限提升与持久化攻击

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1CGRtc83ibsTrS3tRL0VwRT1N1R5iaBwqYia3iap4ib0ibDFiczynqkJTiaLiczaOOPFlibctTm5wCtIWAuwfDXd5br36Ha5Hn9HYOAibXz4/640?wx_fmt=png&from=appmsg)

网络安全研究人员披露了 OpenClaw 中四个可被串联利用的安全漏洞，攻击者能够借此实现数据窃取、权限提升和持久化控制。Cyera 将这组漏洞统称为 Claw Chain，攻击者可利用其建立初始立足点、窃取敏感数据并植入后门。以下是漏洞详情：

* CVE-2026-44112（CVSS评分：9.6/6.3）- OpenShell 托管沙箱后端存在"检查时间/使用时间"（TOCTOU）竞争条件漏洞，允许攻击者绕过沙箱限制，将数据写入预设挂载根目录之外的位置。
* CVE-2026-44113（CVSS评分：7.7/6.3）- OpenShell 中的 TOCTOU 竞争条件漏洞，攻击者可借此绕过沙箱限制读取预设挂载根目录之外的文件。
* CVE-2026-44115（CVSS评分：8.8）- 输入验证允许列表不完整漏洞，攻击者通过在 heredoc 主体中嵌入 shell 扩展标记来绕过允许列表验证，从而在运行时执行未授权命令。
* CVE-2026-44118（CVSS评分：7.8）- 访问控制不当漏洞，非所有者环回客户端可冒充所有者提升权限，进而控制网关配置、cron 任务调度和执行环境管理。

**Part01**

## ****漏洞利用影响****

Cyera 指出，成功利用CVE-2026-44112可使攻击者篡改配置、植入后门并持久控制受感染主机，而CVE-2026-44113可被武器化用于读取系统文件、凭据和内部构件。

漏洞利用链包含四个阶段：

1. 通过恶意插件、提示注入或已入侵的外部输入在 OpenShell 沙箱内执行代码
2. 利用CVE-2026-44113和CVE-2026-44115窃取凭据、密钥和敏感文件
3. 利用CVE-2026-44118获取 Agent 运行时的所有者级控制权
4. 使用CVE-2026-44112植入后门或修改配置实现持久化

**Part02**

## ****漏洞根源与修复****

据网络安全公司分析，CVE-2026-44118的根本原因在于 OpenClaw 直接信任名为 senderIsOwner 的客户端控制所有权标志，该标志用于判断调用者是否有权使用所有者专属工具，但系统未将其与认证会话进行验证比对。

OpenClaw 在漏洞公告中详细说明修复方案："MCP 环回运行时现已分别颁发所有者与非所有者持有令牌，senderIsOwner 将完全根据请求认证所使用的令牌类型来判定。系统不再生成或信任可伪造的 sender-owner 标头。"

**Part03**

## ****安全建议****

经过负责任的披露流程，所有四个漏洞已在 OpenClaw 2026.4.22 版本中修复。安全研究员 Vladimir Tokarev 因发现并报告这些漏洞获得致谢。建议用户立即升级至最新版本以防范潜在威胁。

Cyera 强调："攻击者通过武器化 Agent 自身权限，逐步实现数据访问、权限提升和持久化控制——将 Agent 变成其在环境内的操作工具。每个步骤在传统控制措施看来都像是正常 Agent 行为，这扩大了爆炸半径，使检测难度大幅增加。"

**参考来源：**

Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence

https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html

---

**推荐阅读**

[![图片](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2WOichlYJst28QicxZVpXP1ibeVdB4iawibWIFgqV6Ry4LzdhyQbspxEr3NAqQviatF6AoAYMl0qboYWSzKwjM7zPSKtD3ncv5joxpM/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337950&idx=1&sn=12d64571335d50c1b93389447dfb8ef1&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0Ce65tvicePCnFcQKSQN7xK9UfrD3L8te45kRFiaSB63bHq71nRDRKpGfS3icCZhMXlfKaHoCOCAORVLngwoZ72fRHNAIBmYgevM/640?wx_fmt=png&from=appmsg)

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