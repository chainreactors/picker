---
title: CISA警告：思科统一配置管理（Cisco Unified CM）漏洞已被攻击者利用
url: https://mp.weixin.qq.com/s/3uepeUGGnQMGIHTggkhw6w
source: Doonsec's feed
date: 2026-06-26
fetch_date: 2026-06-27T05:46:17.746325
---

# CISA警告：思科统一配置管理（Cisco Unified CM）漏洞已被攻击者利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7OpwicYA4WRRFUN3T8NsAhnhcb1jDzdxGJMJRAYib1Zkia3MeUCOribKn4z3YicmvW0mno4b8NRwbrYs4b6XNqiaiaZK1LsF0uWibg5xfg/0?wx_fmt=jpeg)

# CISA警告：思科统一配置管理（Cisco Unified CM）漏洞已被攻击者利用

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

CISA 已将影响 Cisco Unified Communications Manager (Unified CM) 的一个严重服务器端请求伪造 (SSRF) 漏洞添加到其已知利用漏洞 (KEV) 目录中，敦促联邦机构和组织立即应用补丁，因为该漏洞已被积极利用。

该漏洞编号为 CVE-2026-20230，它允许未经身份验证的远程攻击者执行服务器端请求伪造 (SSRF) 攻击——这种威胁载体正日益被武器化，以在企业基础设施中站稳脚跟。

该漏洞使得未经身份验证的远程攻击者无需任何凭据即可对受影响的系统执行服务器端请求伪造攻击。

至关重要的是，成功利用该漏洞可能允许攻击者向底层操作系统写入任意文件，从而建立一个立足点，之后可以利用该立足点将权限提升到 root 级别，从而获得对受影响主机的完全控制权。

该漏洞于 2026 年 6 月 25 日被添加到 CISA 的关键漏洞事件 (KEV) 目录中，强制修复期限为 2026 年 6 月 28 日，这反映了积极利用该漏洞所带来的紧迫风险。

## **Cisco Unified CM 漏洞**

SSRF 漏洞在企业通信基础设施中尤其危险，因为它们允许攻击者滥用服务器端功能与内部系统交互、绕过网络控制并访问原本隔离的服务。

在这种情况下，文件写入功能将看似范围有限的缺陷转变为严重的身份验证前远程入侵途径。

攻击者可以构造恶意请求，强制 Unified CM 服务器将攻击者控制的内容写入敏感文件系统位置。

这些植入的文件随后可以在后续攻击阶段被触发或利用，以实现权限提升和持久的根级访问权限，这是企业安全漏洞场景中常见的经典多阶段利用链。

虽然 CISA 目前将勒索软件攻击活动关联性列为未知，但该漏洞的性质（未经身份验证的访问）以及文件写入和权限提升的可能性，使其成为勒索软件运营商和针对企业通信平台的高级持续性威胁 (APT) 组织的高价值目标。

## **受影响产品**

* Cisco Unified Communications Manager (Unified CM)
* Cisco Unified Communications Manager 会话管理版（Unified CM SME）

在互联网环境或混合环境中运行这两款产品的组织应将补救措施视为紧急优先事项。

CISA 已指示受影响的组织按照具有约束力的操作指令 (BOD) 26-04 采取以下步骤，该指令规定了基于风险的优先安全更新：

* 请立即根据思科官方安全公告cisco-sa-cucm-ssrf-cXPnHcW采取厂商提供的缓解措施。
* 根据CISA的取证分类要求进行取证分类，以识别先前入侵的潜在迹象。
* 评估所有受影响资产的互联网暴露情况，并确保遵守 BOD 26-04 的补丁时间表。
* 如果在规定的期限内无法采取缓解措施，则应停止使用该产品。
* 对于云服务部署，请遵循适用的 BOD 26-04 云指南。

强烈建议安全团队审核 Unified CM 日志，以发现异常的出站请求或意外的文件系统修改，作为检测后的立即措施。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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