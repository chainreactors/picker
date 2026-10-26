---
title: ConnectWise SkyKick凭证在Microsoft 365攻击中被滥用，备份服务已关闭
url: https://mp.weixin.qq.com/s/6-7OAUn-zWg5ctj9G6gVKA
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:18:17.366836
---

# ConnectWise SkyKick凭证在Microsoft 365攻击中被滥用，备份服务已关闭

# ConnectWise SkyKick凭证在Microsoft 365攻击中被滥用，备份服务已关闭

原创

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

攻击者利用从ConnectWise Cloud Backup （以前称为 SkyKick）泄露的凭据访问 Microsoft 365 客户环境。

截至 10 月 16 日 19:00 UTC，162 个租户出现了未经授权的登录，这引发了人们对特权供应商应用程序和持久访问的担忧。

ConnectWise在10月16日发布的公告中承认正在进行调查，并表示已采取遏制措施。该公司称，目前没有迹象表明合作伙伴的备份数据已被访问，但对事件范围的调查仍在进行中。Cloud Backup 应用程序于 10 月 15 日 06:13 至 08:34 UTC 期间从 144.172.64[.]128 获取 Microsoft Graph 访问令牌。托管提供商地址与该应用程序正常的 Azure 私有网络流量地址不同。

攻击者按照 GUID 排序顺序逐个租户进行攻击，每次攻击间隔数秒，这表明攻击者可能使用了脚本来攻击目标列表。身份验证使用的是供应商提供的凭据，而不是受影响客户环境中生成的凭据。

由于备份应用程序需要广泛的权限，攻击者可能因此获得对邮箱、OneDrive、SharePoint、Teams 和目录信息的访问权限。潜在影响取决于每个租户中授予的权限；仅凭令牌颁发并不能证明数据被盗。

ConnectWise Cloud Management – MS Teams 在向另外两个应用程序添加客户端密钥之前，给自己分配了全局管理员权限。

这些应用程序包括一款MSP管理工具和合作伙伴的单租户Huntress安全平台应用程序。新增的密钥被配置为在2028年过期，从而可能实现独立于原始ConnectWise凭证的持久性。

这些变更发生在观察到的公网IP认证大约两个半小时前。Huntress尚未证实这两个阶段是由同一操作员所为。

微软记录了第二个应用程序通过私有 IPv6 基础设施建立的连接，该基础设施也与合法流量相关联。Huntress 提醒说，仅凭此地址无法识别运营商。

Huntress 敦促各组织禁用 ConnectWise Cloud Backup（应用程序 ID 506e08f9-6e9a-4da4-942b-a099a03644ae）和 ConnectWise Cloud Management – MS Teams（应用程序 ID 24205314-2b89-4e07-a2a4-579e898a5640），而不是删除它们。

管理员应检查所有应用程序密钥和证书，查找自 10 月 13 日以来的意外添加项，调查未经授权的目录角色分配，并删除植入的凭据。禁用初始应用程序不会删除已添加到其他位置的密钥。

经核实， ConnectWise 的状态页面显示云备份功能运行正常。但这并不意味着安全调查已经结束。禁用该集成会暂停自动备份，但不会删除已存储的备份。

相关IOC

|  |  |
| --- | --- |
| `ConnectWise Cloud Backup` | 受信任的备份应用程序被滥用以访问 Microsoft 365 客户租户 |
| `SkyKick` | 与受影响应用程序关联的发布者名称 |
| `144.172.64[.]128` | 与可疑服务主体身份验证和相关活动关联的 IP 地址 |
| `Python-urllib/3.12` | 在可疑活动中观察到的 Python 用户代理 |
| `python-requests/2.31` | Python 请求与身份验证活动关联的用户代理 |
| `python-requests/2.34.2` | 微软报告的其他 Python Requests 用户代理 |

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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