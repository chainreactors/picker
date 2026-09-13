---
title: 暗网论坛 售卖“iOS 0-Day 利用套件 DarkSword &amp; Coruna”
url: https://mp.weixin.qq.com/s/HMvJ460QfGYYEb8jMdnLoQ
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:58:38.582904
---

# 暗网论坛 售卖“iOS 0-Day 利用套件 DarkSword &amp; Coruna”

# 暗网论坛 售卖“iOS 0-Day 利用套件 DarkSword & Coruna”

原创

NightTeam
NightTeam

夜组OSINT

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 事件概述

2026 年 9 月 11 日，黑客发布广告，声称出售两套“高端 iOS 完整利用链”：

| 商品名 | 自称覆盖版本 | 自称类型 | 标价 |
| --- | --- | --- | --- |
| **DarkSword** | iOS 18.4–18.7 | 零点击全链 | 7,500 美元（可议） |
| **Coruna** | iOS 13–17.2.1 | 全链（含钱包窃取、凭证收割、会话劫持） | 5,000 美元（可议） |

![](https://mmbiz.qpic.cn/mmbiz_jpg/es3jUghv8ribibIYfezib2eicFs5lALGkfqrINX1pyicjykOKCYjU8ME5LkXvWUknQL5kl8Srj7D8T530pEZEzYOWRUb6PANdrULST8AibMwa7dNk/640?wx_fmt=webp&from=appmsg)

卖家自称“已用于私有行动”“新鲜、未被检测、截至 2026 年 9 月仍可用”，同时明确拒绝测试与演示。

公开情报与上述营销文案存在关键矛盾：

![](https://mmbiz.qpic.cn/mmbiz_jpg/es3jUghv8ribr2Oof3Q6aD8tibr8IC9nrKemRRyV7PibiaDs5KicVpianbicsib4QrGfjuR1k47hA0ZkHR6P2sXuZDkuAiaMWcWLgsXN06t0VWF246CY/640?wx_fmt=webp&from=appmsg)

* **DarkSword** 与 **Coruna** 并非 2026 年 9 月新出现的未知 0-Day，而是 2026 年 3 月前后由 Google Threat Intelligence Group（GTIG）、iVerify、Lookout 等机构公开披露的 iOS 全链利用套件，并已被多家商业监控厂商与疑似国家背景集群（含 UNC6353）用于真实行动。相关漏洞已由 Apple 分批修复。
* 地下市场标价（合计约 1.25 万美元）远低于历史上国家级 0-Day 全链的采购成本，更符合 **披露后二次市场转售 / n-day 商品化 / 控制面板包装售卖**，而非“全新未披露 0-Day”。
* 卖家账号 **2026 年 9 月注册、发帖 5、主题 5、声望 0**，却挂“GOD User”标识，符合论坛付费等级或新号包装，**不具备独立研发高价值 iOS 全链的信誉画像**。

**判断：** 该帖是“国家级利用能力下沉到犯罪市场”这一趋势的最新销售样本。对防御方的意义主要在于：**未升级的存量 iPhone 仍可能被已公开套件或其变种命中**；对“仍是 0-Day”的宣称应视为营销话术，直至有独立样本验证。

![](https://mmbiz.qpic.cn/mmbiz_jpg/es3jUghv8r90yY9bhjW1g1X4k26IW8clEsGKl0SO2y49Le1YdhIW5ibksxTxotqwu2eYcicwjevCHtP28dqnPD06fbOQOjibdOh2qFpICvK05Q/640?wx_fmt=webp&from=appmsg)

## 商品声称与公开事实对照

### 帖内声称

**DarkSword**

* 目标：iOS 18.4–18.7
* 类型：零点击全链（无需用户交互）
* 能力：远程代码执行、沙箱逃逸、持久化、数据外带、完整设备接管
* 交付物：控制面板、部署脚本、私有部署协助、完整文档
* 状态：新鲜、未检测、2026 年 9 月仍可用
* 价格：7,500 美元

**Coruna**

* 目标：iOS 13–17.2.1
* 类型：完整攻击链，含钱包盗窃、凭证收割、会话劫持
* 能力：零点击、持久化、远程控制、外带
* 交付物：Web 控制面板、文档、私有部署支持
* 状态：已测可用；较旧但“极其可靠”
* 价格：5,000 美元

### 公开披露基线

**Coruna（约 2026 年 3 月初公开）**

* 面向 iOS **13.0–17.2.1** 的多链利用框架，公开报道称涉及约 **23 个漏洞、5 条完整链**。
* 入口多与 WebKit/Safari 访问相关；后续被用于监控场景，并出现面向加密货币/会话的犯罪化用法。
* 研究侧指出其与更早的高端间谍活动组件存在技术重叠，并已进入二次市场。

**DarkSword（约 2026 年 3 月 18–19 日公开）**

* 面向 iOS **18.4–18.7** 的 Web 驱动全链，公开描述为将多枚漏洞串联至内核级控制，最终投放植入。
* GTIG 等观察到自约 2025 年 11 月起，被多个商业监控厂商及疑似国家背景行为体用于针对沙特、土耳其、马来西亚、乌克兰等地目标。
* 后续植入家族公开命名包括 GHOSTBLADE、GHOSTKNIFE、GHOSTSABER 等。
* 同一集群 UNC6353 此前使用 Coruna，后又引入 DarkSword，说明两套工具已在同一运营商工具箱中并存。

公开报道中与 DarkSword 相关的漏洞编号包括（供补丁核对，非利用说明）：

* CVE-2025-31277、CVE-2025-43529（JavaScriptCore）
* CVE-2025-14174（ANGLE）
* CVE-2025-43510、CVE-2025-43520（内核相关）
* CVE-2026-20700（dyld PAC 相关）

Apple 已在 iOS 18.7.x / 26.x 系列更新中分批修复；部分旧机型另有回溯补丁。2026 年 8 月仍有厂商报告 Coruna/DarkSword **二代变种域名持续出现**，说明“披露 ≠ 消亡”，但也不等于卖家口中的“未被检测的 0-Day”。

### 关键矛盾

| 维度 | 卖家说法 | 公开情报 | 评估 |
| --- | --- | --- | --- |
| 是否 0-Day | 标题与 DarkSword 文案强调 0-Day、未检测 | 2026 年 3 月已大规模披露并补丁 | **营销夸大** |
| 版本范围 | 与公开范围几乎逐字相同 | 与 GTIG/iVerify 报告一致 | **像在抄公开报告，而非独立产品说明书** |
| Coruna 犯罪功能 | 明确写钱包/凭证/会话 | 公开报道确有犯罪化与钱包相关载荷 | **功能方向可信，来源不一定是该卖家原创** |
| 价格 | 5k–7.5k 美元 | 原始国家级套件研发成本被外媒估为数千万美元量级 | **二次市场/残包/控制面板授权价** |
| “9 月仍全新可用” | 明确声称 | 主链漏洞已补；未升级设备与变种仍可能中招 | **对已打补丁设备基本不成立；对存量旧系统部分成立** |

## 结论

该事件是 **2026 年 iOS 国家级利用套件犯罪零售化** 的典型橱窗：商品名、版本区间和能力列表几乎直接搬运已公开的 DarkSword 与 Coruna，但用“0-Day / 未被检测 / 9 月仍新鲜”包装成高价地下货。卖家画像更像转售或诈骗，而不是原开发团队。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8ricARaxBFDXarNyWBgNxEb2cSZlHVickr5nlIjLRH9Uf1MIzmSoZwJUIZADuzdgnuMs7JSMp7BRic9WH1SIThhA36JVH7v0L5A1gw/640?wx_fmt=webp&from=appmsg)

## 威胁情报全球监控系统

以上威胁事件由全球威胁情报系统（dark.libaisec.com）实时监测发现，订阅会员即可查看威胁情报详情及原文件。

![dark.libaisec.com](https://mmbiz.qpic.cn/sz_mmbiz_jpg/es3jUghv8r8n8klowCIY3wfPzUURXG5ZAuz5ibwdNNwxwVsIQw0PCyvpwqibhZ9Yxc2cK0z4KcbDoNjWT5j5AP9khPekxh60LM6iceInm0MFac/640?wx_fmt=webp&from=appmsg)

dark.libaisec.com

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/GLyX5CgG8A1AjQiarwFHPJibeWbc1nhED6yPPhcfplNAzMjXJx106p9J3HaRZUNyBAhECfklMPvyOsReia0qaVV8A/0?wx_fmt=png)

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