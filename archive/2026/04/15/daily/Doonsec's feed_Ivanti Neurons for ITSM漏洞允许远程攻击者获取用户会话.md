---
title: Ivanti Neurons for ITSM漏洞允许远程攻击者获取用户会话
url: https://mp.weixin.qq.com/s/QbPE4MYPikfr0cUfVg0oZA
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:48:02.271984
---

# Ivanti Neurons for ITSM漏洞允许远程攻击者获取用户会话

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnt3T7lWv5b9LNIxdlic6ndAZ0Cg49VFIXQg7DGNQS0c9gx96KwibhqI78ByYIWEZa9neIeUEISETRzfCZQnGzUWnFyCHQtF9hTwo/0?wx_fmt=jpeg)

# Ivanti Neurons for ITSM漏洞允许远程攻击者获取用户会话

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnuY3uCIFkGzhF8T5F60gPb1D7ZND4MjP6KiaBuYGIHOpurhSerNVLH2HHvicg6S7qAfcYhnJz77Uyo48UlvLicFbShakeGk0XWGZA/640?wx_fmt=png&from=appmsg)

Ivanti发布了安全更新，修复了其内部部署IT服务管理平台Ivanti Neurons for ITSM (N-ITSM)中的两个中等严重性漏洞。

如果被利用，这些漏洞可能允许远程认证攻击者保留未授权访问权限或从其他用户那里窃取会话数据。

该公司确认，在公开披露时，尚未发现任何针对这两个漏洞的活跃利用行为。这两个问题都是通过Ivanti的负责任披露计划报告的，并已在新发布的2025.4版本中得到修复。

**CVE-2026-4913：路径保护不当漏洞**

第一个漏洞CVE-2026-4913的CVSS评分为5.7（中等），归类于CWE-424（保护机制失效）。该漏洞源于Ivanti N-ITSM 2025.4版本之前对备选路径的保护不当。

远程认证攻击者可能利用此漏洞，即使其账户已被管理员禁用，仍能保留对系统的访问权限。

这种类型的绕过在企业环境中尤为危险，因为在内部威胁事件或员工离职期间，及时撤销访问权限是一项关键的安全控制措施。

该漏洞可通过网络访问，需要低权限，并且需要用户交互才能触发，这些因素共同构成了其中等严重性评级。

**CVE-2026-4914：存储型XSS导致跨会话数据窃取**

第二个漏洞CVE-2026-4914是一个存储型跨站脚本（XSS）漏洞，CVSS评分为5.4（中等），归类于CWE-79。在Ivanti N-ITSM 2025.4版本之前，该漏洞允许远程认证攻击者注入恶意脚本，这些脚本会在其他用户会话的上下文中执行。

通过利用此漏洞，攻击者可能获取来自其他用户会话的有限信息，可能捕获会话令牌、凭证或敏感的ITSM数据。

该攻击需要用户交互，意味着受害者必须访问恶意制作的内容才能使攻击成功。该漏洞的跨范围影响（CVSS向量中的S:C）表明其影响可能超出即时会话范围。

这两个漏洞影响Ivanti Neurons for ITSM 2025.3版本及所有先前版本，涵盖内部部署和云部署环境。

* 内部部署客户必须通过Ivanti许可系统（ILS）手动升级到2025.4版本
* 云客户无需采取任何行动，因为Ivanti已于2025年12月12日对所有云环境应用了修复

Ivanti敦促所有内部部署客户立即应用2025.4更新。由于尚未观察到公开利用行为，目前没有可用的入侵指标。

运行旧版本的组织应优先处理此次升级，特别是考虑到CVE-2026-4913在具有严格访问控制策略的环境中所带来的访问保留风险。

本公众号所载文章为本公众号原创或根据网络搜索下载编辑整理，文章版权归原作者所有，仅供读者学习、参考，禁止用于商业用途。因转载众多，无法找到真正来源，如标错来源，或对于文中所使用的图片、文字、链接中所包含的软件/资料等，如有侵权，请跟我们联系删除，谢谢！

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo5lNbibXUkeIxDGJmD2Md5vKicbNtIkdNvibicL87FjAOqGicuxcgBuRjjolLcGDOnfhMdykXibWuH6DV1g/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&randomid=p6hk1x4r&tp=webp#imgIndex=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

网安百色

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1QIbxKfhZo6T5IuE1hib7qvAtbaaUZ8tt2fviaDoictibySdn9ibPOF34VZoLwMDYQWCnQGouyMttnhZib6G8fddDqNw/0?wx_fmt=png)

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