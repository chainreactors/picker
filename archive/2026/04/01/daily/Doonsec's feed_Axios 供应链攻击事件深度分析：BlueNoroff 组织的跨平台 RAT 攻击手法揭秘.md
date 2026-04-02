---
title: Axios 供应链攻击事件深度分析：BlueNoroff 组织的跨平台 RAT 攻击手法揭秘
url: https://mp.weixin.qq.com/s/ENHWeInvFdHR4ge9BKtiCw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:28:44.939195
---

# Axios 供应链攻击事件深度分析：BlueNoroff 组织的跨平台 RAT 攻击手法揭秘

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GsI0VdBbyRoYuXUGz5DgdAY6BDnoL3viawYer779MdmJQUwJHOYyYp9LptZzgC9DQzaY7Byg4xSZjAyTg8dke552AJlkH7awdo/0?wx_fmt=jpeg)

# Axios 供应链攻击事件深度分析：BlueNoroff 组织的跨平台 RAT 攻击手法揭秘

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0Eg9fYtyuCxZEV7WhgsfPbWnybWhPkhJL1TbGxAVbbT4kibqogEbYIPMleH5pYUUAvf6ALUGmPskjVbHOvvWBylemls7p5qas9A/640?wx_fmt=other&from=appmsg)

一、事件背景

2026年3月30日至31日，npm 生态圈顶级依赖库 Axios（周下载量超 8300 万次）遭受供应链攻击。攻击者通过劫持维护者账户，在 axios@1.14.1 和 axios@0.30.4 两个版本中注入恶意代码。

经 VT 验证和逆向分析，此次攻击归因于 朝鲜 Lazarus Group 旗下的 BlueNoroff 子组织，置信度为 高。

二、攻击链分析

投递阶段：

恶意版本引入 plain-crypto-js@4.2.1 作为 dropper，该库经过混淆处理，执行时根据目标平台环境解密并部署相应的 RAT（远控木马）。

多平台载荷：

| 平台 | 载荷形式 | 归因关联 |
| --- | --- | --- |
| Windows | PowerShell RAT | 定制化脚本 |
| macOS | Mach-O C++ (NukeSped) | 与 RustBucket webT 模块代码相似 |
| Linux | Python RAT | `peinject` 模块含源码 BUG |

三、关键技战术分析（TTP）

1.项目命名关联

* macOS 木马内部项目名 macWebT 关联至 BlueNoroff 2023 年 RustBucket 家族的 webT 模块

2.新型注入技术

* 发现 .NET 进程注入 DLL Extension.SubRoutine.Run2()，零公开引用记录

3.C2 基础设施

* 主控域名关联攻击者 npm 账户 nrwise（域名 callnrwise.com）
* IP 段与 Hostwinds AS54290 有重叠，9 个 Lazarus IP 共享同一 ASN

4.杀软规避

* 初始检测率极低（Linux 样本初始 0/76），为攻击者提供约 6 小时的隐形窗口期

四、检测与响应

已发布的检测规则：

* 8 条 YARA 规则（100% 检出率）
* 8 条 Sigma 规则（覆盖 Windows/macOS/Linux）
* 11 条 Suricata/Snort 规则（含 Base64 信标匹配）

IOC 摘要：

* 18 个 SHA256 哈希
* 2 个确认的 C2 域名
* MITRE ATT&CK 映射完整

五、处置建议

1. 立即核查 package.json 及 package-lock.json 中是否存在受影响版本
2. 执行降级：回滚至 1.14.0 或升级至官方修复版本
3. 审计日志：检查近期安装依赖的 CI/CD 流水线日志
4. 网络侧检测：部署上述 Suricata 规则，监控出站异常信标

六、总结

这是近年来罕见的影响范围如此广泛的 npm 供应链攻击事件。攻击者不仅具备多平台 RAT 开发能力，还使用了创新的代码注入技术和成熟的隐匿策略。建议各开发团队立即响应，并将此攻击手法纳入供应链安全审计清单。

------ >推荐阅读：

* Axios npm 供应链妥协——完整分析包

https://gist.github.com/N3mes1s/0c0fc7a0c23cdb5e1c8f66b208053ed6

![](https://mmbiz.qpic.cn/mmbiz_png/zNsFJyIuL0GMwWOZwJezg3jXG9vicS41H41YxCbicq8tf2CUr6jKKJRUdrabv6cmUsqEKffDnZ7jdibNvMicfEP2Ke4iaUibicQC2gxzbLWn5gBaYc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zNsFJyIuL0EwaGQlqg1tBFmKE6zvr1TkOMAZD9rrC8o0ZcGCM5wM6ASGNtfsX4Ttgse2v2KR4xeGMUS53CWw35QsDA0GOibtZicowfJEdB7Po/640?wx_fmt=png&from=appmsg)

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FgPjBe7Jue5e6icu3HQDxibKibslcHuVZj2qsCOChVT3YCTpvbo9g6JLibbzZNbogS8bNiasEr2EHchtFobqJI9fPspo4NI4NCYiclY/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

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