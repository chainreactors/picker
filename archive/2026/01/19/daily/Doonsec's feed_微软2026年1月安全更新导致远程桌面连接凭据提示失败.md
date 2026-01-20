---
title: 微软2026年1月安全更新导致远程桌面连接凭据提示失败
url: https://mp.weixin.qq.com/s/E6m5Nbt4W6mm1HOgfk-J_A
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:33:30.815379
---

# 微软2026年1月安全更新导致远程桌面连接凭据提示失败

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo57Gxvokg2S3zs9fwPRPyzsDibpUZrp2ulPdv6MsibUBXWJp1gCkNXJaicAxNiavmawUetEx1EvPlBp6Q/0?wx_fmt=jpeg)

# 微软2026年1月安全更新导致远程桌面连接凭据提示失败

网安百色

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/1QIbxKfhZo57Gxvokg2S3zs9fwPRPyzsbn1BxtVEtsMK3MbL01C8195j8SRqclDMTo4JibhEJqbbnEt0n31TGibw/640?wx_fmt=jpeg&from=appmsg)

微软已发布一个带外紧急更新，以解决影响Windows客户端设备上远程桌面连接的关键问题。

该问题在安装2026年1月安全更新（KB5074109）后立即出现。管理员和用户报告称，通过Windows应用尝试登录时，凭据提示功能普遍失效，严重影响了对Azure虚拟桌面和Windows 365环境的访问。

该原始更新于2026年1月13日发布，旨在解决运行特定Windows构建版本的系统的常规安全漏洞和错误。

然而，在部署后不久，用户发现他们在启动远程会话时无法再成功进行身份验证。这影响了依赖虚拟化桌面基础设施的组织，因为员工无法访问其基于云的工作站。

## 远程桌面连接失败

技术根本原因被追溯到Windows应用在特定操作系统构建版本（构建版本26200.7623和26100.7623）上处理凭据提示的方式出现了回归问题。
当用户尝试连接时，身份验证界面无法正确处理凭据，导致反复出现登录错误。这实际上将用户拒之于远程环境之外，即使他们输入了有效的用户名和密码。

对于使用Azure虚拟桌面和Windows 365的企业环境，影响尤为严重，因为Windows应用是这些环境的主要连接网关。
该故障被隔离在客户端对连接的处理上，这意味着服务器基础设施仍然正常运行，但客户端设备无法完成建立会话所需的手握。

## 缓解措施

微软迅速承认了该问题并加快了解决方案的推出。该公司现已发布了一个独立的"带外"更新KB5077744，专门用于修复先前更新引入的回归问题。
此修复程序恢复了Windows应用的正常功能，并确保在远程桌面会话期间凭据提示按预期工作。
建议管理受影响终端的系统管理员立即部署KB5077744以恢复服务可用性。此更新将操作系统构建版本号增加到26200.7627和26100.7627。

## 补丁详情

| 更新类型 | KB编号 | 发布日期 | 受影响的构建版本 | 修复内容 |
| --- | --- | --- | --- | --- |
| 问题更新 | KB5074109 | 2026年1月13日 | 26200.7623, 26100.7623 | 安全修复（导致RDP失败） |
| 解决方案更新 | KB5077744 | 2026年1月17日 | 26200.7627, 26100.7627 | 修复凭据提示失败 |

## 受影响平台

| 平台 | 组件 | 症状 |
| --- | --- | --- |
| Azure虚拟桌面 | Windows应用 | 凭据提示失败/登录错误 |
| Windows 365 | Windows应用 | 凭据提示失败/登录错误 |
| Windows客户端 | 远程桌面 | 无法连接到远程主机 |

管理员可以直接从微软更新目录或通过其标准更新管理渠道（如Windows Server Update Services（WSUS）和Microsoft Intune）下载修复补丁。
应用此更新无需移除先前的安全补丁，确保设备在恢复远程连接的同时，仍能免受1月13日所解决的漏洞的影响。

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