---
title: GitLab修复多个可导致拒绝服务和代码注入攻击的漏洞
url: https://mp.weixin.qq.com/s/xn4X0DDUW5MSILPyu94W5g
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:03.527704
---

# GitLab修复多个可导致拒绝服务和代码注入攻击的漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WibvcdjxgJnsPiaIvKoC9GEoptvvNoibKHuzwqyByx8oucJEPB08ZbWicgTWZ0nZdclmul38Q2ociad0hudL7QFg8ib0prc3CkibMXqflbgHlnv2Cg/0?wx_fmt=jpeg)

# GitLab修复多个可导致拒绝服务和代码注入攻击的漏洞

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJnvMlaYQeriaAX0uB2RP5VYKnl79u8OVCyh6kwnFqkrk3fkNTDojn62FlVxpZJjZnf9acZQgGm1hJO24AWPPBVibvJPrlgLkmibne0/640?wx_fmt=png&from=appmsg)

GitLab为其社区版（CE）和企业版（EE）发布了紧急安全更新（版本18.10.3、18.9.5和18.8.9），以修复可能导致拒绝服务（DoS）攻击和代码注入攻击的高危漏洞。

GitLab强烈建议所有自托管系统的管理员立即升级，以保护其实例安全。

**高危漏洞**

此次安全更新修复了三个对GitLab环境构成重大风险的高危漏洞：

**CVE-2026-5173（CVSS 8.5分）**：由于访问控制不当，经过身份验证的攻击者可通过WebSocket连接执行非预期的服务器端命令。

**CVE-2026-1092（CVSS 7.5分）**：未经身份验证的用户可通过向Terraform状态锁API提交未经正确验证的JSON数据，触发拒绝服务攻击。

**CVE-2025-12664（CVSS 7.5分）**：无账户的攻击者可通过重复发送GraphQL查询使服务器过载，从而造成拒绝服务状态。

**中等严重性漏洞**

除上述严重问题外，GitLab还修复了多个可能影响用户安全和系统稳定性的中等严重性漏洞：

**CVE-2026-1516（CVSS 5.7分）**：经过身份验证的用户可在代码质量报告中注入恶意代码，秘密泄露查看该报告的其他用户的IP地址。

**CVE-2026-1403（CVSS 6.5分）**：CSV文件验证机制薄弱，可能导致经过身份验证的用户在文件导入过程中使后台Sidekiq工作进程崩溃。

**CVE-2026-4332（CVSS 5.4分）**：分析仪表板中的输入过滤不足，可能使攻击者在其他用户的浏览器中执行恶意JavaScript代码。

**CVE-2026-1101（CVSS 6.5分）**：GraphQL查询中的输入验证不当，可能使经过身份验证的用户导致整个GitLab实例拒绝服务。

**其他安全补丁**

此次更新还包括多个较低严重性的补丁，用于解决数据泄露和访问控制失效问题：

**CVE-2026-2619（CVSS 4.3分）**：授权机制错误，允许具有审计员权限的经过身份验证的用户修改私有项目中的漏洞标记数据。

**CVE-2025-9484（CVSS 4.3分）**：信息泄露漏洞，允许经过身份验证的用户通过特定GraphQL查询查看其他用户的电子邮件地址。

**CVE-2026-1752（CVSS 4.3分）**：访问控制不当，允许开发人员修改受保护的环境设置。

**CVE-2026-2104（CVSS 4.3分）**：CSV导出中的授权检查不足，允许用户访问分配给他人的机密问题。

**CVE-2026-4916（CVSS 2.7分）**：授权检查缺失，允许具有自定义角色的用户降级或移除具有更高权限的组成员。

GitLab强调，所有自托管安装必须尽快升级至18.10.3、18.9.5或18.8.9版本。

由于这些更新无需复杂的数据库变更，多节点部署可在无系统停机的情况下完成升级。

托管在GitLab.com上或使用GitLab专用版的用户已处于安全状态，因为该公司已将补丁应用于其云服务器。

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