---
title: WordPress插件严重漏洞使网站面临身份验证绕过攻击风险
url: https://mp.weixin.qq.com/s/7aiu0QKC8mg1wo89Vjjx9A
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:01:43.662476
---

# WordPress插件严重漏洞使网站面临身份验证绕过攻击风险

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibvcdjxgJnt64Ng1icGJdicGsjzNHMMaeaMCDU3bc6UIXlHicvrK8W40pTlTh0E5z8D8Yxk65pibIuAuzO29T9icDO8OdAq7LGYGEUD8aMZqaUJU/0?wx_fmt=jpeg)

# WordPress插件严重漏洞使网站面临身份验证绕过攻击风险

网安百色

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/WibvcdjxgJntuURMsQCvAxLtXMUdSjvIj8oemE7rKcKSuEu8iaqmKYN5cumiaVnC9lOr8QUQ1ibKgnaThwJhO1xvKB1icuHlC7pDBdH417HLxt7s/640?wx_fmt=png&from=appmsg)

一款广泛使用的WordPress插件中存在严重漏洞，导致超过200,000个网站面临完整账户接管风险，引发安全社区的紧急关注。

该漏洞由Wordfence的AI驱动PRISM威胁情报平台于2026年5月8日发现，影响注重隐私的分析工具Burst Statistics插件。

该漏洞被追踪为CVE-2026-8181，CVSS评分为9.8，允许未经认证的攻击者绕过身份验证并冒充管理员账户。

问题影响3.4.0至3.4.1.1版本，于2026年4月23日引入。

值得注意的是，该漏洞在15天内即被识别，并于19天后完成修复，凸显了AI驱动的漏洞发现如何缩短可利用窗口期。

WordPress插件认证绕过漏洞
漏洞源于插件MainWP集成中的不当验证，具体位于is\_mainwp\_authenticated()函数内。

该函数通过HTTP Authorization头处理认证请求，但未能验证凭证的有效性。

由于不安全的返回值处理机制，插件将WordPress的wp\_authenticate\_application\_password()函数返回的任何非错误响应均视为认证成功。

在某些情况下，认证失败时该函数会返回null而非错误，导致恶意请求未经检查即可通过。

攻击者可通过发送包含有效管理员用户名和任意密码（经Basic Authentication头编码）的伪造REST API请求来利用此漏洞。

插件随后将当前用户上下文设置为目标管理员，从而在请求期间授予全部权限。

成功利用后，攻击者可在无需预先认证的情况下执行高权限操作。

例如，单次对/wp-json/wp/v2/users端点的请求即可创建新管理员账户，实现持久化访问并完全控制网站。

由于该漏洞影响所有REST API端点，攻击者可滥用超出插件本身的WordPress核心功能，显著扩大攻击面。

补丁和缓解措施
Burst Statistics团队在披露后迅速响应。Wordfence于5月8日启动负责任披露流程，5月11日共享完整细节，供应商于2026年5月12日发布修复版本（3.4.2）。

强烈建议用户立即更新至3.4.2或更高版本以降低风险。

使用Premium、Care或Response服务层级的Wordfence客户已于5月8日获得防火墙防护，免费用户将于2026年6月7日获得同等防护。

安全专家警告称，该漏洞因利用简单且无需认证，对威胁行为者极具吸引力。

管理员应审计用户账户、监控日志并确保立即完成补丁部署，以防止系统遭入侵。

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