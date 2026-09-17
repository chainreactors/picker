---
title: Fortinet FortiWeb 8.0–8.0.1  未授权 RCE 利用链地下售卖事件
url: https://mp.weixin.qq.com/s/Dys5lUgDo39zIv4wEOaOSQ
source: Doonsec's feed
date: 2026-09-16
fetch_date: 2026-09-17T06:57:34.995672
---

# Fortinet FortiWeb 8.0–8.0.1  未授权 RCE 利用链地下售卖事件

# Fortinet FortiWeb 8.0–8.0.1 未授权 RCE 利用链地下售卖事件

原创

李白
李白

李白你好

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## Fortinet漏洞情报

2026年9月16日 00:50黑客在地下论坛发布标题为 *“Selling - Fortinet 1-day Exploit RCE”* 的售卖帖，声称出售针对 **Fortinet FortiWeb 8.0–8.0.1** 的“1-day”利用，通过串联两个 CVE 实现**未授权远程代码执行（Unauthenticated RCE）**，并提供完整利用链软件。

![](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNWwyFr2k1A3h7B8Diay2mnuGbwyurrfGiaYCPEndaCFllPibU4y02yWZz7LOS5Ogbk8FJEby7bdC93HgDPtkbwICBHibJzibhqiaOz8o/640?wx_fmt=png&from=appmsg)

售卖条件：

* 仅接受论坛托管（Forum Escrow）或指定中间人 `@paw`
* 仅接受门罗币（XMR）
* 标价 760 美元，可议
* 要求先通过论坛私信联系

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNWmwBSLAPjff6nlaoKiackVQqhzOX6rEnzwFLHDcHtjRLX9EZ0VoR5diaOQy8ESd6SiaKOMR3pBwU6GjdraWu5XMyxF8sicxw2kgKc/640?wx_fmt=webp&from=appmsg)

所谓“1-day”与版本范围（仅 8.0–8.0.1）高度指向 **2025 年 11 月已公开披露并被大规模利用** 的已知漏洞链，而非全新 0-day。公开 Metasploit 模块早已存在，地下售卖更可能是**封装后的现成利用包**或面向不愿使用公开工具的买家。

**动机：** 地下市场持续对边缘安全设备（WAF/防火墙）未打补丁实例有需求。FortiWeb 作为面向互联网的 WAF，一旦被控可改策略、植入后门、作为跳板进入内网。

## 技术研判：与已知公开利用链高度匹配

公开情报显示，FortiWeb 8.0.0–8.0.1 存在可直接链式利用的两个漏洞，修复版本为 **8.0.2 及以上**：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNUibFICOQORxS17RFALWwg7zdlDSIDqYdjqNoicEZrrJheSgE0y5VUOrsLU7GIoBhdanr2ZxianuvNia63icwYeWU3usD2cGw5TR4mQ/640?wx_fmt=webp&from=appmsg)

| CVE | 类型 | 权限要求 | 作用 | 修复版本（8.0 分支） |
| --- | --- | --- | --- | --- |
| CVE-2025-64446 | 相对路径遍历 + 认证绕过（CWE-23） | 未认证 | 访问内部 CGI（如 `fwbcgi`），伪造管理员身份，可创建本地管理员账号 | 8.0.2 |
| CVE-2025-58034 | 操作系统命令注入（CWE-78） | 需认证（常与上一漏洞串联） | 通过管理 CLI（7.x/8.x 常见 `/ws/cli/open`）执行任意命令，获取 root 级代码执行 | 8.0.2 |

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNWpUTEAkrGc4iczSTbHJ48D2XJeHiaSf1H4NR48icH5I1GutcIQlLmaoo3hZvOz3nBSql9iaib6yxSmyYHwiccyERk0ByiaBRGbulFghU/640?wx_fmt=webp&from=appmsg)

该链已被 CISA 列入已知被利用漏洞（KEV）目录，存在公开 PoC、检测工件生成器和 Metasploit 模块 `exploit/linux/http/fortinet_fortiweb_rce`。利用流程通常为：路径混淆到达 CGI → 伪造管理员身份创建账号 → 登录后通过 CLI 注入命令。

卖方声称“串联两个 CVE 实现任意 FortiWeb 8.0–8.0.1 未授权 RCE”，与上述公开链在**版本范围、利用结果、链式结构**上一致。2026 年 8 月另有 CVE-2026-26035（RADIUS 通配认证配置不当，影响至 8.0.2），但该漏洞本身不直接构成通用未认证 RCE，且卖方明确限定 8.0.1，因此**主匹配对象仍是 2025 年那条链**。

**结论：** 该商品大概率不是全新 0-day，而是对已公开、已大规模利用漏洞的商品化包装。对仍运行 8.0.0/8.0.1 且管理面暴露的设备，风险与 2025 年底野生利用浪潮相同。

## 影响面与风险

**受影响产品：** FortiWeb 8.0.0、8.0.1（卖方声明范围）。公开资料中同链还影响 7.6/7.4/7.2/7.0 及部分已停更的 6.x，但本次商品明确只卖 8.0–8.0.1。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ft6csZH0gNVGB8d5G8eqa4eLspGAhW0SLkqvnAic9hUy6B7ibsYbRBia2PVnKNCCgK7VCgbrgHD7OEy8eMRV8nUnEO8MNH9fUA2X03H655IAqQ/640?wx_fmt=webp&from=appmsg)

**攻击前提：** 管理 HTTP/HTTPS 接口可从攻击者网络到达（常见于管理口误暴露公网）。

**成功利用后可能后果：**

* 创建持久管理员账号
* 以高权限在设备上执行命令（root）
* 篡改 WAF 策略、关闭防护
* 窃取配置、证书、会话
* 作为跳板横向移动或投放后续载荷

2025 年 10–11 月已观察到野生利用，特征包括创建特定管理员账号、对 `fwbcgi` 的路径遍历请求等。时隔近一年仍有地下售卖，说明**未升级设备存量仍然可观**。

## 检测与狩猎建议

1. **版本核查：** 立即确认所有 FortiWeb 是否已升级至 **8.0.2 或更高**（8.0 分支）；其他分支按厂商公告升级。
2. **暴露面：** 管理口不得对公网开放；无法立即升级时，按厂商建议关闭互联网方向的 HTTP/HTTPS 管理。
3. **日志与配置审计：**

* 排查异常新增的本地管理员账号
* 检查对 `/cgi-bin/fwbcgi`、带 `../` 或 `%3f/../../` 的 `/api/v2.0/` 请求
* 关注 WebSocket CLI（`/ws/cli/open`）异常会话

4. **网络侧：** 对已知公开利用特征做 IDS/WAF 规则（注意卖方可能对公开 PoC 做了轻微变形）。
5. **事后：** 升级后复查配置与日志，必要时轮换凭证并检查是否有持久化后门。

公开检测资源包括 watchTowr 等发布的工件生成器及厂商/社区规则，可直接用于狩猎。

## 缓解与处置优先级

| 优先级 | 动作 |
| --- | --- |
| 紧急 | 将 FortiWeb 8.0.0/8.0.1 升级至 8.0.2+；无法升级则切断公网管理访问 |
| 高 | 全量审计管理员账号与近期配置变更；检查是否已有异常账号 |
| 中 | 限制管理面来源 IP；启用可信主机；监控后续类似地下售卖 |
| 持续 | 将 Fortinet 边缘设备纳入常规补丁 SLA，避免“管理口暴露 + 滞后补丁”组合 |

厂商官方缓解与升级路径以 FortiGuard PSIRT（如 FG-IR-25-910 及相关后续公告）为准。

## 情报评估与后续跟踪

* **技术真实性：** 高。描述与 CVE-2025-64446 + CVE-2025-58034 公开链一致，版本卡点精确。
* **是否为全新 1-day：** 低。更可能是对已公开链的商品化。不排除卖方对利用稳定性、封装或对抗做了小改动。
* **交易真实性：** 中。新号 + 托管模式常见，存在收钱不交货或捆绑恶意软件风险。
* **建议跟踪项：** 该帖后续回复与成交情况；是否出现针对 8.0.2+ 的新链售卖；Shodan/Censys 上仍暴露的 8.0.1 管理面规模。

## 总结

该地下帖并非全新零日爆料，而是**已知高危 FortiWeb 未认证 RCE 链在地下市场的持续变现**。对已打补丁（≥8.0.2）且管理面隔离的环境，直接风险有限；对仍运行 8.0.0/8.0.1 且管理接口可达的资产，应视为**可被低成本、可复制利用的紧急风险**，按 2025 年野生利用同等优先级处置。

防御核心仍是：**尽快升级、关闭公网管理、审计异常管理员与路径遍历痕迹。** 地下售卖只会缩短从“公开利用”到“批量滥用”的时间窗口。

参考：https://www.cisa.gov/news-events/alerts/2025/11/14/fortinet-releases-security-advisory-relative-path-traversal-vulnerability-affecting-fortiweb

https://hacktricks.wiki/en/network-services-pentesting/pentesting-web/fortinet-fortiweb.html https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2026-105/

## 网络安全情报攻防站

**www.libaisec.com**

综合性的技术交流与资源共享社区

专注于红蓝对抗、攻防渗透、威胁情报、数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNXJ2smpxYaKDrW7XZWolPkXWJV2225QCicwtjsicqACHfHu91yicGkuQUszQKXOBiak2lhLlRFaMs4ArRzn5QXscJpCIaiaRtFJPaKk/640?wx_fmt=webp&from=appmsg)
> 👇 点击阅读原文，访问**网络安全情报攻防站**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XoIcX2HtlUAuS65pf9u98YWJSdI6kWZ64ziasaVXOFXiabEV2AuCY8yGygtKHicEFVvHnw3bzhsDXBB3DQIiaNhOiaQ/0?wx_fmt=png)

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