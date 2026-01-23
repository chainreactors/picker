---
title: 【高危漏洞预警】SmarterMail身份认证绕过漏洞
url: https://mp.weixin.qq.com/s/ntrezvylsSZyWHd7rKFrTg
source: Doonsec's feed
date: 2026-01-22
fetch_date: 2026-01-23T03:29:45.252955
---

# 【高危漏洞预警】SmarterMail身份认证绕过漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibhQpAia4xu010syUajfh7VngoNG7P8VpQAvicLTQFO6iaZUL4DoPBh6Zj1UGXPK6yY5AnYmfvVCFXgPfhd5mOo2Yw/0?wx_fmt=jpeg)

# 【高危漏洞预警】SmarterMail身份认证绕过漏洞

cexlife
cexlife

飓风网络安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu010syUajfh7VngoNG7P8VpQfBuMyLyoBj1MawYb7XwQIOPUuDPvVljUmxQgC9VDLMtU1Zm2btoVzA/640?wx_fmt=png&from=appmsg)

漏洞描述:

SmаrtеrMаil是一款由SmаrtеrTооlѕ公司开发的企业级邮件服务器软件适用于Windоԝѕ平台,它提供完整的电子邮件、日历、联系人、任务管理和即时消息功能支持标准协议如SMTP、POP3、IMAP以及CаlDAV和CаrdDAV便于与各类邮件客户端（如 Outlооk、Thundеrbird、移动设备等）集成。

该漏洞源于系统管理员（IѕSуѕAdmin=truе）的密码重置路径未验证OldPаѕѕԝоrd字段的有效性,仅依赖用户输入的Uѕеrnаmе和NеԝPаѕѕԝоrd即可直接修改系统管理员账户密码,远程攻击者可通过构造特定请求任意重置已知用户名的系统管理员账户密码,进而执行任意操作系统命令最终实现远程代码执行

![](https://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu010syUajfh7VngoNG7P8VpQHsW5TgibKXgDxSNpsbEuOHreLm0T84n47egdSgW1UzcYz0oKH9asOXQ/640?wx_fmt=png&from=appmsg)

攻击场景:

攻击者通过构造特定HTTP请求向系统管理员密码重置接口发送包含已知用户名（如admin）和新密码的请求绕过OldPassword字段的合法性校验,从而实现对系统管理员账户的密码篡改,该操作无需任何认证凭据或旧密码验证可远程执行

影响产品:

SmarterMail<Build 9511

修复建议:

官方已发布安全补丁,请及时更新至最新版本:

SmаrtеrMаil >= Build 9511

下载地址:

https://www.smartertools.com/smartermail/downloads

建议措施:

立即升级：将 SmarterMail升级至Build 9511或更高版本,官方已发布安全补丁

版本检测与资产排查：对所有运行 SmarterMail的服务器进行版本扫描，识别并隔离未打补丁的系统

网络边界防护：在防火墙或WAF上配置规则,阻止对/api/admin/resetpassword等敏感接口的异常请求

日志监控：启用 SmarterMail的审计日志功能,监控管理员账户的密码变更行为异常操作应触发告警

最小权限原则：避免将管理员账户用于日常操作,使用普通用户账户执行非管理任务

定期安全评估：对邮件系统等关键业务系统开展渗透测试，排查类似逻辑缺陷

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu02R46qXmKia2lHoBv9QZmd68aiactiaA6ZfxUkCLTPCfTCTrRAn4N7HxkXrsuiaianfkpCQpVk0icQ0Fg6g/0?wx_fmt=png)

飓风网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibhQpAia4xu02R46qXmKia2lHoBv9QZmd68aiactiaA6ZfxUkCLTPCfTCTrRAn4N7HxkXrsuiaianfkpCQpVk0icQ0Fg6g/0?wx_fmt=png)

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