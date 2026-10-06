---
title: 戴尔CSM曝两处高危漏洞，未授权攻击者可直接获取管理员权限
url: https://mp.weixin.qq.com/s/poCuL2gEOisWNpAX-gOPdw
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:35.986864
---

# 戴尔CSM曝两处高危漏洞，未授权攻击者可直接获取管理员权限

# 戴尔CSM曝两处高危漏洞，未授权攻击者可直接获取管理员权限

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1ffMgvt0AibFSBD1ibv4oEKz80NBWjB7eCYA3RC59SDAQlJTI2UqhGQ5P00tTcF4xFkTpfoI2JGiaYe323Uz4TmR1icMy2QB4ca1E/640?wx_fmt=gif)

![戴尔修复容器存储模块高危漏洞，未授权攻击者可获完整管理权限](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2nsTsiaPv9GI32Wa8XRMbqXsiaibPkwBx0cic6g2EPQ212vP2aQxWleTPjSv1St3MPLica6vXVAQUticicU7J80jYkLHM44sPqMwyUs0/640?wx_fmt=jpeg)

戴尔已发布安全更新DSA-2026-448，修复容器存储模块（CSM）中的多个高危漏洞。未授权远程攻击者可利用这类漏洞，完全掌控受影响存储环境的最高管理权限。

使用存在漏洞的戴尔CSM部署的企业需立即升级。戴尔明确表示，目前没有针对这些漏洞的临时规避方案或缓解措施。

本次公告影响1.17.0之前的所有CSM版本，官方在1.18.0及后续版本中提供了完整修复。修复范围覆盖CSM Authorization、CSM Operator、CSI组件以及第三方Go库。

Part01

两个漏洞CVSS满分

本次披露的漏洞中，CVE-2026-63688和CVE-2026-63692危害最严重，CVSS评分均为满分10.0。CVE-2026-63688是身份验证缺失漏洞，存在于2.4.0版本CSM Authorization的csm-authorization-storage gRPC服务端中。

未授权攻击者可利用该漏洞获取所有已注册存储阵列的管理员凭证，进而控制戴尔支持的五大存储产品系列。

拿到后端管理员凭证后，攻击者可篡改存储配置，访问阵列中存储的敏感数据。

攻击者还能中断正常运行的业务负载，影响业务连续性。

此外，攻击者可在环境中创建持久化访问路径，长期维持控制权限。

CVE-2026-63692同样影响2.4.0版本的CSM Authorization。该漏洞存在于授权代理与租户服务中，核心功能接口未设置有效的身份验证机制。

网络攻击者可利用该漏洞绕过身份验证控制，将权限提升至管理员级别。获得管理员权限后，攻击者可访问并篡改所有租户的存储资源。

Part02

多类高危漏洞叠加

可致权限提升与集群失陷

另一个高危漏洞CVE-2026-54472为CSM Authorization中的硬编码凭证漏洞，CVSS评分为9.8。未授权远程攻击者可利用该漏洞伪造符合密码学校验规则的管理员JWT，获取CSM Authorization代理的管理员访问权限。

戴尔提醒用户，完成版本更新后需轮换JWT签名密钥。本次更新还修复了已归档的karavi-authorization组件中的CVE-2026-61421。

旧版文档中曾将JWT签名密钥示例写为“supersecret”，并附带了真实令牌示例。如果企业部署karavi-authorization时使用了该文档中的默认值，且从未修改签名密钥，攻击者仍可通过伪造令牌接管其管理员权限。

CVE-2026-67269存在于1.12.0版本的CSM Operator中，CVSS评分为9.9。低权限远程用户可通过构造恶意ContainerStorageModule资源获取Kubernetes节点root权限，最终造成整个集群失陷。

CVE-2026-67273的CVSS评分为9.6。低权限攻击者可通过模板引擎注入访问Kubernetes Secrets，创建集群范围的RBAC资源。

这类访问可直接绕过Kubernetes原有的权限控制，让攻击者获得集群资源的广泛控制权。

本次修复的漏洞还包括证书验证不当、戴尔PowerMax CSI驱动授权缺失、日志敏感信息泄露，以及影响PowerFlex、PowerMax、PowerStore CSI驱动的多个安全问题。

本次更新还修复了多个第三方Go组件的漏洞，涉及golang.org/x/crypto、golang.org/x/net、golang-jwt/jwt以及protobuf。

Part03

官方建议尽快升级

戴尔建议所有受影响的CSM部署方，尽快将实例升级至1.18.0或更高版本。

升级完成后，安全团队需及时轮换JWT签名密钥，审查CSM Authorization的访问日志。

同时，安全团队要审计管理员令牌的使用记录，排查异常访问行为。

企业还应全面核查Kubernetes RBAC策略与自定义资源，确认是否存在未授权的配置变更。

参考来源：

Critical Dell Container Storage Flaws Let Unauthenticated Attackers Gain Full Administrative Control

https://cybersecuritynews.com/critical-dell-container-storage-flaws/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bRSnFgE3WPnpU3s0eVp7QdRn9fI63ymmlhTHpsMBL2VnRMPZQy9DhvZasynJV1ia534sF84uxxKKulzDlBibjrQ7ylDiaickrCIY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651347479&idx=1&sn=1cf9c858a30d0b7af06d196002bd2913&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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