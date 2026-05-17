---
title: VMware Fusion漏洞可致攻击者获取root权限
url: https://mp.weixin.qq.com/s/Mej9s5_vLeu62bG2Fq4dQQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:44:03.946956
---

# VMware Fusion漏洞可致攻击者获取root权限

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnsv7M3hZhaEiaNYeXIhCSGDsc8KiaDCicibTNnaIWtvoZL9F5MpgtZcmYXvmLj4yWRAZgkeCTGHtzugYPq9Fd859KCE5fvKCibrL2gM/0?wx_fmt=jpeg)

# VMware Fusion漏洞可致攻击者获取root权限

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/WibvcdjxgJnuwGLkEx1xTTv6BXlZnApvGf4QgIWODjc7Y0RMFt7gsmG8FfjD2LRqR9QFWWc6Ytgan51vCicicYQN8iaUMQTicmTxJq57XXSDJBhA/640?wx_fmt=png&from=appmsg)

VMware Fusion曝出新漏洞，攻击者可借此提权至root控制Linux系统

研究人员证实，VMware Fusion中 newly disclosed（新披露）的安全漏洞可能使攻击者获得受影响系统的root权限，引发严重安全担忧。

该漏洞编号为CVE-2026-41702，严重程度评级为"高危"，CVSS评分为7.8，表明其在实际环境中具有显著危害性。

**VMware Fusion漏洞详情**
目前负责VMware产品的Broadcom公司于2026年5月14日发布安全公告（VMSA-2026-0003），指出问题根源在于SETUID二进制文件中存在的检查时间与使用时间竞争条件（TOCTOU）。此类漏洞的特征是系统完成条件检查后，在实际使用结果前未验证状态是否已被篡改，从而留下可利用的窗口。

Broadcom确认，拥有普通用户权限的本地攻击者可利用此漏洞获取root级系统控制权。攻击者将能执行任意命令、篡改敏感文件或部署持久化恶意软件，完全掌控目标系统。

安全研究员Mathieu Farrell（@coiffeur0x90）因负责任地提交该漏洞获得致谢。尽管披露时未发现公开的在野利用案例，但因其仅需本地访问权限且无需用户交互的简单攻击向量，在共享计算环境或企业网络中存在极高风险。

**影响范围与修复方案**
漏洞影响所有平台上的VMware Fusion 25H2版本。依赖Fusion进行开发测试、环境沙箱等虚拟化操作的企业及个人用户，若未及时更新系统将面临直接威胁。

Broadcom已在VMware Fusion 26H1版本中修复该问题。值得注意的是，目前无临时解决方案，更新补丁是唯一有效缓解措施。该漏洞因攻击复杂度低、无需用户交互，且对机密性、完整性及可用性均构成高危影响，极易被入侵者用于初始访问后的权限提升。在企业环境中，此类漏洞常与其他漏洞组合利用，最终实现系统完全沦陷。

**安全建议**
安全专家建议立即升级至VMware Fusion最新版本。同时，组织应实施严格的访问控制策略、限制本地用户权限，并监控系统异常活动迹象。此次事件再次凸显本地提权漏洞的持续威胁，尤其在广泛使用的虚拟化平台中。随着攻击者 increasingly target（日益聚焦）开发工具与虚拟化环境，及时修补与主动监测仍是关键防御手段。

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