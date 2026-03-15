---
title: 今日（2026年3月14日）OpenClaw 最新安全动态总结
url: https://mp.weixin.qq.com/s/2Nq-FXpNp94mMToy_ePoDg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:28:15.036128
---

# 今日（2026年3月14日）OpenClaw 最新安全动态总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RwAbCjh555uw7iaHo0rN3puTuZJECGwrRa4vmB5bDpcstajIJsYjUfLtxEjddTeZYibjEbBXrcAGopueuE3OM5DjoLWAwCUmap9Y4yEfuABas/0?wx_fmt=jpeg)

# 今日（2026年3月14日）OpenClaw 最新安全动态总结

奇安信 CERT

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_svg/uHwLXtyH4IXTars0DEAdy9nZcUtFcGrTy3nibexVh7BkBPMPp5nLfNgt67b5GWcgVibZsbUSHhKbtb6Eibh4vBoiaLfySz3fSygp/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_svg/dx4Y70y9Xcs692v9TjnicxJEZft7mP8uWicBRPuXXzZg069MvuoD4NP9L3WJiaoqponicCib5DMjypusYpLvEsR5g11bPZsUtwfjB/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

3月14日资讯导视

* 昨日发布的 v2026.3.12 仍是全网最热话题——这是一个重度安全加固版本，一次性修复了10+ 个 GHSA（涉及设备令牌、插件执行、WebSocket、Unicode欺骗等）。
* NanoClaw（专为解决OpenClaw安全缺陷而生的开源替代品）今天宣布与Docker深度合作，热度爆表。
* 中国国家互联网应急中心风险提示持续发酵，暴露实例超4万+（中国约2.3万）。

![图片](https://mmbiz.qpic.cn/mmbiz_svg/GPyw0pGicibl6FlfJiaNBkMPMFyFOibLIWIcnofJD9HFIEkZM5SEbOlmbksIpNdHnJna42D5LSLYtEA7cbicE6qBeJv0fJ8eeZjfM/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

![图片](https://mmbiz.qpic.cn/mmbiz_svg/ZqDaDiccbgkhBmJZvPXtaUAefuaoJCVTKXplxCtc9ibiav0toECE9GgicrEgxdtJOMFHDgLu3CN01gofEcWnI72wNtR2AicveephI/640?wx_fmt=svg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4)

**01**

**今日核心事件**

v2026.3.12 安全发布（3月13日上线，仍是今日讨论焦点），

GitHub Releases：

https://github.com/openclaw/openclaw/releases/tag/v2026.3.12

安全改进亮点（官方明确列出 GHSA 修复）：

1. 设备配对令牌改为：短生命周期临时令牌（防止QR/聊天中嵌入永久凭证）。
2. 插件默认：禁用隐式工作区自动加载，防止克隆仓库恶意代码执行（GHSA-99qw-6mr3-36qr）。
3. 执行审批提示转义零宽Unicode字符，防伪造提示（GHSA-pcqg-f7rg-xfvv）。
4. WebSocket预认证帧大小限制 + 缩短未认证握手时间。
5. 浏览器持久化配置文件创建/删除路由阻断。
6. Feishu/LINE/Zalo webhook签名强制验证。
7. 其他：命令授权收紧、子Agent沙箱隔离、Git\_EXEC\_PATH阻断等（共10+ GHSA）。

影响：所有 < v2026.3.12 版本强烈建议立即升级，并旋转所有暴露令牌。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

**02**

**今日热度最高新动态**

###

NanoClaw + Docker 安全隔离方案。NanoClaw（开源安全替代品）今天宣布与Docker官方合作，使用微VM容器沙箱运行Agent，实现完全隔离（解决OpenClaw历史RCE、令牌窃取问题）。

X平台刷屏：22K+项目，仅用周末开发，已成“别信任OpenClaw”的首选方案。

![图片](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

**03**

****我国官方风险提示持续发酵****

国家互联网应急中心提醒：OpenClaw默认高权限 + 插件投毒风险，已出现“提示词注入”“误删除核心数据”“恶意skill后门”等真实案例。

部分地区出现“OpenClaw卸载服务”副业，政府/国企正逐步限制使用。

###

![图片](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

**04**

****近期高危CVE回顾（仍在活跃讨论，无当日新增）****

本次分析的 OpenClaw 核心漏洞如下表所示：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| GHSA/CVE | 严重性 | 类型 | 影响 | 修复版本 | 技术要点 |
| GHSA系列（v2026.3.12批量修复） | 7.8-9.x | 执行/认证绕过 | Unicode伪造、插件劫持、WebSocket预认证 | 2026.3.12 | 短生命周期token + 沙箱边界 |
| CVE-2026-25253 | 8.8 | 令牌窃取→RCE | 恶意链接一键劫持本地网关 | 2026.1.29 | gatewayUrl未校验 + WebSocket自动连接 |
| CVE-2026-28466/28474 | 9.3-9.4 | RCE（Nextcloud插件） | 参数未过滤导致远程执行 | 2026.2.6 | Nextcloud Talk插件转发缺陷 |

###

![图片](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=11)

**05**

****今日技术分析要点（社区最关注）****

****☞GHSA vs CVE跟踪差距**：OpenClaw短短几周发布了200+ GHSA，但仅部分有CVE，导致企业工具检测盲区（VulnCheck已申请170+ CVE）。**

****☞根因总结**：**高权限本地Agent + 默认信任输入（gatewayUrl、插件、prompt）+ WebSocket弱认证，形成供应链 + 一键攻击链。

****☞新趋势**：**社区转向：容器化/零信任（NanoClaw Docker微VM），AI Agent必须“沙箱优先”。

###

![图片](https://mmbiz.qpic.cn/mmbiz_png/Q5psicuZhSKO8Kjic7UiauSE5ialRQwCEeiaPHXzDxpHEib7ZNRdMlbVBGO7Ow54XxdrzIPMo9l6wahTTqotibRamh8jw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=12)

**06**

****立即行动建议（Mac用户尤其注意）****

* 升级：`git pull` 或直接下载 v2026.3.12，运行 `openclaw security audit --deep --fix`。
* 加固：开启Sandbox、禁用隐式插件、启用短生命周期令牌、切换NanoClaw Docker版。
* 扫描：用OpenClaw Security Monitor 或 ClawSec Suite 检查暴露端口/恶意skill。
* 监控：GitHub Security Advisories + 中国国家网络安全通报中心。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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