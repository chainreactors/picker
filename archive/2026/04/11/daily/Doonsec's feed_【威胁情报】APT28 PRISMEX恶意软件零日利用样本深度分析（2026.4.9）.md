---
title: 【威胁情报】APT28 PRISMEX恶意软件零日利用样本深度分析（2026.4.9）
url: https://mp.weixin.qq.com/s/IJiNyl83RFLD0dHLLTs4wQ
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:04.043171
---

# 【威胁情报】APT28 PRISMEX恶意软件零日利用样本深度分析（2026.4.9）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FZdgbEn3GibtFz0aFIoAYLwtqhJFgbc2QzXmwfpheHBn1XnaZIfpbHTRdnodn113js0v0HrxQqZnCw0ibY49XZBSHYiciaKRr8xvM/0?wx_fmt=jpeg)

# 【威胁情报】APT28 PRISMEX恶意软件零日利用样本深度分析（2026.4.9）

Ots安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0GBs0PZpFdw0lI3lEpOFLlEkxzZ8ctfcWEca2CzjPw0IQLaIznbhtZnURtUkiaZM2C3rxE83pdl9iaoxd70BwXk5xhGxody8kLew/640?wx_fmt=jpeg&from=appmsg)

某境外APT组织近期通过矛 phishing 方式部署全新恶意软件套件PRISMEX，对乌克兰及北约盟国关键机构实施定向攻击。该活动于2026年4月9日被公开披露，涉及零日漏洞利用、隐写术隐藏载荷及COM劫持持久化技术，已影响国防、应急服务、物流及铁路等领域。本文基于公开情报，对PRISMEX样本行为进行技术拆解，提供IOC与防御建议，帮助企业快速识别潜在入侵。

事件背景与时间线

PRISMEX恶意软件套件最早可追溯至2025年9月活跃，2026年1月12日已准备相关零日利用基础设施。1月30日观察到LNK文件利用样本上传，2月10日相关补丁发布。此次4月9日披露的分析显示，攻击者正加速针对乌克兰中央执行机构、水文气象部门、国防及应急服务，以及波兰铁路、罗马尼亚/斯洛文尼亚/土耳其海事运输、斯洛伐克和捷克后勤支持伙伴实施行动。攻击目标明确指向运营规划与供应链中断。

CISA同期要求联邦机构在2026年4月11日前完成Ivanti Endpoint Manager Mobile（EPMM）相关高危补丁（CVE-2026-1340），进一步凸显近期APT活动对企业远程管理系统的威胁叠加。

攻击手法与TTPs分析

PRISMEX采用典型两阶段攻击链，核心TTPs包括：

* 初始访问： spear-phishing 投递恶意Excel文件（PrismexSheet），利用VBA宏触发。
* 隐写术载荷提取：PrismexLoader（又称PixyNetLoader）为代理DLL，从PNG图像文件（SplashScreen.png）中采用自定义“Bit Plane Round Robin”算法提取.NET载荷，实现内存加载，避免磁盘落地。
* 持久化机制：PrismexDrop原生dropper通过计划任务+COM DLL劫持实现开机自启；PrismexSheet同样修改COM注册表项。
* C2通信：最终载荷为修改版COVENANT Grunt（PrismexStager），滥用合法云服务Filen.io作为C2通道，支持信息采集与破坏性擦除。
* 零日利用：关联CVE-2026-21509与CVE-2026-21513，攻击者快速武器化，结合Microsoft Shortcut（LNK）文件形成无交互执行链。部分样本还部署MiniDoor（Outlook邮件窃取器）。

样本行为高度隐蔽：显示诱饵文档（如无人机库存清单）迷惑用户，同时后台完成环境探测、持久化与载荷执行。

影响范围与受害者画像

受害者主要为：

* 乌克兰政府及国防相关机构
* 北约盟国物流、铁路、海事运输企业
* 供应链支持伙伴

攻击兼具间谍与破坏双重属性，既窃取敏感运营数据，又具备%USERPROFILE%下文件擦除能力，可能导致供应链中断与关键基础设施可用性下降。

IOC汇总

| 类型 | 具体IOC | 说明 |
| --- | --- | --- |
| 域名 | wellnesscaremed[.]com | 关联零日利用与两阶段攻击链 |
| 文件特征 | SplashScreen.png（隐写PNG） | 存放.NET载荷 |
| User-Agent | Adobe Synchronizer | 部分C2流量特征 |
| 持久化 | COM注册表修改 + 计划任务 | PrismexSheet/PrismexDrop核心 |

（注：当前公开情报暂无具体文件哈希，建议结合行为检测。）

防御建议

1. 优先级最高：立即检查并修补Ivanti EPMM（CVE-2026-1340）及关联零日，截止日期2026年4月11日。
2. 端点检测：监控COM注册表异常修改、计划任务新增，以及PNG图像中异常大文件或可疑VBA宏执行。
3. 网络层：封锁可疑Filen.io相关流量，过滤含“Adobe Synchronizer” User-Agent的HTTP/HTTPS请求。
4. 用户侧：禁止打开来源不明Excel/PDF，启用宏禁用策略；部署行为基检测工具识别内存加载与隐写术。
5. 威胁狩猎：在EDR日志中搜索Prismex相关DLL加载与COVENANT Grunt特征。

总结

APT28最新PRISMEX恶意软件样本展示了现代APT在零日利用、隐写术与合法云C2方面的成熟组合，对关键基础设施威胁显著。企业需结合本次情报提升检测能力，及时响应类似定向攻击。

本文基于公开情报分析，仅供学习与研究交流。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0HNI3hLMtqHo5icicicBahFv4W0ibP1bAVT9voRjO5SUIpEej9iaGnwomicn0PHtum6ZLKRGJGPGbKRCAt7WnHPaSkh9cN54TNo2j4hI/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

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