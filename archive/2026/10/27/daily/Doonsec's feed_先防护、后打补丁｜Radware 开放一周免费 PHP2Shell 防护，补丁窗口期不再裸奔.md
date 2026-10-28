---
title: 先防护、后打补丁｜Radware 开放一周免费 PHP2Shell 防护，补丁窗口期不再裸奔
url: https://mp.weixin.qq.com/s/4jieVA4Uvukt7Tt4asgsOg
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:46:11.677853
---

# 先防护、后打补丁｜Radware 开放一周免费 PHP2Shell 防护，补丁窗口期不再裸奔

# 先防护、后打补丁｜Radware 开放一周免费 PHP2Shell 防护，补丁窗口期不再裸奔

Radware

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R9d3Gh1qCIxfFJ2fItnuOYbjdrlSJIicncWwZXzrOEfn2WZxAkECcZxj6ae1kK2ZpDODjwwdvBiaPPuu5mqA0SNoBD9RTsdIlxzEzfhtG3TX8/640?wx_fmt=jpeg&from=appmsg)

**核心提示**

PHP 核心两个 CVSS 9.2 的远程代码执行漏洞（CVE-2026-109618 / CVE-2026- 109619，合称 PHP2Shell）细节已泄露、在野利用已被公开披露。

企业完成补丁验证、测试、上线通常需要数天到数周——这段暴露窗口怎么办？Radware 现已开放"一周免费 PHP2Shell 防护"，通过其云安全平台为受影响组织提供紧急接入，让你在安全打补丁的同时，先把攻击挡在门外。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d3Gh1qCIxmkZK89zC8N9zZXj1DHibBAWLutVft051l6YCeVxYoaB4xvpKke4o8LRA9yZiaSDfNHNuOCNtclQI3KN395Hk5Ll486FyCV5peA/640?wx_fmt=png&from=appmsg)

**威胁态势：**

**漏洞影响的是 PHP 引擎本身**

两个漏洞（CVE-2026-109618 / CVE-2026-109619）位于 PHP 引擎本身，可能允许未经身份验证的攻击者在受影响服务器上执行恶意代码或访问敏感信息。它们不局限于某个特定应用、内容管理系统或插件——只要运行受影响版本的 PHP 对外提供 Web 服务，就在风险范围之内。

PHP 官方已于 10 月 21 日 14:00 UTC 发布修复版本：PHP 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35。但现实问题是：验证、测试、部署修复需要时间——在修复推进期间，企业存在一段难以避免的暴露窗口。多国政府机构已临时下线服务，国家网络安全通报中心、CNVD 也已收录该漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/R9d3Gh1qCIyaEG1icv0VK0MqJjjmdAJFjaKvF9KE3dxsbAibXGKTnsGyLbOAZVkicMkI4icFJx5xMm6pSOGnfeQLNjJOWI7pC5AF71UyyjxNAAo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/R9d3Gh1qCIwRapQevFarQvU4WwnPoErYjYTG3fDmH7LQNhq3icW16AuW9MwN5ics8hKVtHKAhDJ2ZnBicIs84b3uxqvapl0yFcS3iccvKia0LBNg/640?wx_fmt=png&from=appmsg)

**Radware 的主张：先防护，后打补丁**

这是 Radware 官方公告的标题，也是它给出的答案：Protect first. Patch safely.——防护先行，补丁从容。升级 PHP 运行时是治本之策，但补丁不能瞬间完成；在补丁落地之前，边界防护与虚拟补丁是压缩暴露窗口的关键手段。

**01**

**签名防护**

Radware Cloud Application Protection 客户启用 2026 年 10 月签名包（版本 8.0.0.638），规则 ID 12330 即可拦截 PHP2Shell 的已知利用载荷，签名已随 Security Update Service（SUS）自动推送。

**02**

**AI 虚拟补丁**

AI Xploit Shield 同步更新签名与策略，基于每个组织的应用、API、暴露面与环境自动生成定制化运行时防护，在补丁部署前阻断 AI 武器化的漏洞利用。

**03**

**持续监测**

通过 Radware 应用防护平台实时日志与告警，监控针对 PHP2Shell 载荷的探测与利用行为，为安全团队提供攻击态势可见性。

![](https://mmbiz.qpic.cn/mmbiz_png/R9d3Gh1qCIzPMyXN1CSYIBqiclyeAGjviaTC1T340GpojuGwibBlC7ukOJEzW8klaicKQV2C4E8yibDlDJo0cKGpU2DpGsI78gXG0YOfu5KUsZ6g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/R9d3Gh1qCIyS6Nw8E3M4Jp7Dt99qg9px7GabjmfxQa4PFdL7XJR9a5n9A7xrKxsiaScVfZJRQuMEibbkS3uBeorYvn4YxjEzYwkGJDYfdTYaI/640?wx_fmt=png&from=appmsg)

**一周免费 PHP2Shell 防护计划来了**

针对尚未使用 Radware 服务的组织，Radware 正式推出限时免费方案——通过其云安全平台提供为期一周的免费 PHP2Shell 防护，帮助企业在打补丁期间降低暴露风险。该防护旨在：

![](https://mmbiz.qpic.cn/mmbiz_png/R9d3Gh1qCIwW18GDjrZqiaicZ5qN6kib11GkjcWrQUwMGuascp4SVYNTADsMClhxFyhiavJtby0lWbdGDSq8l5RRjOjicwBibrTIblNAqaYnq8QUM/640?wx_fmt=png&from=appmsg)

**如何申请一周免费 PHP2Shell 防护？**

联系 Radware 申请紧急接入，说明需要"一周免费 PHP2Shell 防护"即可开始。

**几点须知：**

· 该方案限定期限、面向符合条件的组织，需完成接入流程并遵守 Radware 适用服务条款；

· 防护按"现状"免费提供，Radware 可随时修改、暂停或撤回该方案；

· 防护是打补丁的补充，不是替代——组织仍应尽快更新受影响的 PHP 环境，并自行评估自身暴露面、应用厂商发布的补丁。

![](https://mmbiz.qpic.cn/mmbiz_png/R9d3Gh1qCIw3jM5ocbicmdh0msdb6usTYbLr7sDQFjs1YjS96tJ8WYZmpXa4Sia9XoVMwP2XBXs6zqB9Snvos0BRU1MI4HkxnZUIiaZlHVOgGo/640?wx_fmt=png&from=appmsg)

**影响范围速览**

**！！受影响版本**：PHP 8.5.x < 8.5.12 ｜ PHP 8.4.x < 8.4.27 ｜ PHP 8.3.x < 8.3.36 ｜PHP 8.2.x < 8.2.35 ｜ PHP 8.1 及更早（已停止维护，无官方补丁）

该漏洞位于 **PHP 核心层**而非某个应用，因此无论上层跑的是 WordPress、Drupal、Joomla、Magento、Laravel、Symfony，还是 phpMyAdmin、Nextcloud、Roundcube——只要底层PHP 在受影响范围内，全都中招。共享主机商、cPanel / Plesk 等托管面板、内嵌 PHP 的厂商设备，即使你从不直接管理 PHP，也可能因为依赖链而被动暴露。

另需注意：坊间流传"关闭 Session Upload Progress 就能防住 CVE-2026-109619"的缓解方案已被主动撤回，PHP 官方开发者明确表示——**打补丁或升级 PHP 是唯一真正的缓解手段，任何ini 配置都无法替代官方修复。**这也进一步凸显了在补丁周期内依赖防护层拦截的必要性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/R9d3Gh1qCIwFvrV5WAYTrRBaavtUfibJjic2o808NClr4O1c8zKvhonNvnG9IcnOrmDJB541hYWNoxrLwj2iaBd7yU42xUg4SuQlYA2YPeTfbs/640?wx_fmt=png&from=appmsg)

**行动建议**

![](https://mmbiz.qpic.cn/mmbiz_png/R9d3Gh1qCIxibCnGIVf3NfRNBBRHzoib2TCKe1RILSQz1BL3vhTlHgpSLlviccQQ3zDcT2QIgoYObdFDjIw4ficJYMibiaYWbxcDbvd7f47mCU7ws/640?wx_fmt=png&from=appmsg)

✅ **具体做什么**

1.**确认 Radware 防护已生效** —— Cloud Application Protection 客户确认签名包版本为8.0.0.638（或更高），规则 ID 12330 处于启用状态；AI Xploit Shield 客户确认策略已自动更新。未打补丁的资产立即进入防护覆盖。

2. **尽快升级 PHP 运行时** —— 按所在分支升级至 8.5.12 / 8.4.27 / 8.3.36 / 8.2.35。注意：升级的是 PHP 运行时本身，不是上层应用；不要只盯着 CMS 版本号。8.1 及更早分支用户请尽快迁移到受支持版本——**8.2 也将于 2026 年 12 月 31 日 EOL**，建议提前规划。

3. **全量盘点 + 持续狩猎**—— 不要遗漏厂商设备、托管面板内嵌的 PHP；优先修复面向互联网、面向客户的系统。结合 Radware 平台日志持续监测 PHP Worker 进程异常派生 shell、非预期外联等可疑行为。

本次修复工程浩大——近 200 个文件被修正，新增代码超过 1 万行。技术细节提前泄露意味着防御窗口比想象中更短，"明天再打补丁"在今天可能意味着已经中招。好消息是：通过 Radware 签名防护 + AI 虚拟补丁 + 威胁情报的组合拳，补丁周期内的暴露风险可以被有效压缩——而且现在，还有一周免费防护可以先接上。

*参考阅读：*

*· Radware 威胁通告：**https://www.radware.com/security/threat-advisories-attack-reports/php2shell/*

*· Dan Schnour 博客《PHP2Shell: Guidance for Protecting Your Environment》*

*· Radware《One Week of Free PHP2Shell Protection》官方公告*

![](https://mmbiz.qpic.cn/mmbiz_jpg/R9d3Gh1qCIzMcFuSb9vW2KVXzttf97SkebC4PUiaEqZv02xu6N9VuwM0y8ibrZkia7miaxibUUTQCwyasEqsj4xBbFpiaXjBVB0gu2vOcj5Aj4f8A/640?wx_fmt=jpeg&from=appmsg)

点击下方" **阅读原文**"

**留下您的信息，申请紧急接入**

**关于Radware**

Radware®（NASDAQ: RDWR）是多云环境应用安全和交付解决方案的全球领导者。该公司的云应用程序、基础设施和API安全解决方案使用人工智能驱动的算法，可提供精确、无操作、即时的防护，免受复杂的网络、应用程序、DDoS攻击、API滥用和恶意机器人的攻击。全球的企业和运营商依靠Radware解决方案来应对不断变化的网络安全挑战，并在降低成本的同时保护品牌和业务运营。

欲知详情，请访问：*https://cn.radware.com/*

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R9d3Gh1qCIysk05MsUS4iae6JIoeodCrrWvkbOjoZvhFjXzzcFdCXO6LLl7Aib8TQoiccDIUiciaWyiajydXLk3iby9ib2DQwhbbw1LMjZoME12Leys/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UicD0GtT0eekic18Nh4SL4rS595HS4YERgCaQUJa8Sk46oBUoRFyg6Zmw0KCtJglpf8YFAiaaVP2ULH7yaSlbpeGA/0?wx_fmt=png)

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