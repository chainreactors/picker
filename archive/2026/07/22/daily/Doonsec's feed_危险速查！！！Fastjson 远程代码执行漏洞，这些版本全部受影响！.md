---
title: 危险速查！！！Fastjson 远程代码执行漏洞，这些版本全部受影响！
url: https://mp.weixin.qq.com/s/v4JCIJNzFb25Nk3JOE8Psg
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:07:37.928120
---

# 危险速查！！！Fastjson 远程代码执行漏洞，这些版本全部受影响！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3wlibOpCwqMufPPvFS3xzIYetMggeVgibEL5sPQySibacG9kmq2ibxtvKqtmicX8RfArSXbWY0NIcls9KJBpbhWtGH3lQ36BM4K5BM3zX3DEJwIk/0?wx_fmt=jpeg)

# 危险速查！！！Fastjson 远程代码执行漏洞，这些版本全部受影响！

魔方安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/3wlibOpCwqMuz28Txjwx7Y2ETtPKBFFL7nhEdXpzMGdlCETCsEWPpfG2smT8qBj9XNxk6YLFr0ia3Bj0BhIyZoD5uAM70xoEK7liaU40PLewaA/640?wx_fmt=gif&from=appmsg)

7月19日，安全研究者公开披露 Fastjson 1.2.83 及之前版本存在远程代码执行漏洞。48小时内，PoC公开，存在被利用风险。这个曾被视作 1.x "安全终点"的版本，不再安全。

## **01.****事件回顾**

**7月19日**

研究者 Kirill Firsov 公开预警：Fastjson 存在 gadget‑free RCE

**7月20日**

研究者补充 DTO 绑定场景同样受影响；腾讯云发布安全通告

**7月21日**

PoC 在 GitHub 公开，多方复现确认，存在被利用风险

## **02.****漏洞解析**

过往所有 Fastjson RCE 都依赖目标环境存在特定第三方类（gadget），防御方通过**黑名单**和**移除危险依赖**即可缓解。

本次漏洞彻底打破了这一前提。攻击者无需用户权限，即可在未启用安全模式的目标服务器上远程执行任意代码，直接威胁系统的机密性、完整性与可用性，可导致服务器被完全控制。建议受影响用户尽快修复。

**传统防线失效：**
✗ 关闭 AutoType → 无效（1.2.68+ 默认已关闭，漏洞仍可利用）
✗ 配置黑名单 → 无效
✗ 移除第三方危险类 → 无效
✗ 绑定具体 DTO 类型 → 研究者已明确点名同样在影响范围

RCE 条件：Fastjson ≤ 1.2.83 + 未启用 SafeMode + 网络可达

· Linux/macOS：JDK 8 / 17 / 21 / 25 等已验证可 RCE

· Windows：JDK 8 可触发；高版本 JDK 因系统特性不受影响

· Spring Boot FatJar 场景下，`jar:http` 可远程拉取 JAR，进而配合 `/proc/self/fd` 等路径形成完整 RCE；Tomcat、Jetty、Undertow 等内嵌容器均受影响（`fd bridge` 链路已验证，但并非所有容器均支持单一 `jar:http` 直接 RCE）

## **03.****影响范围**

**受影响版本**Fastjson <= 1.2.83

· 1.2.66 / 1.2.67 通过 `jar:file` 同样可复现；更低版本亦存在其他安全风险，建议全面排查

· 未开启 SafeMode 的实例全部受影响

· AutoType 默认关闭状态同样可被利用

· 1.x 仓库已于 2024 年 10 月归档，不会再有官方补丁

· PoC 已公开，存在被利用风险

## **04.****解决方案**

### ▎升级修复方案

建议升级至 Fastjson2，以规避 1.x 系列存在的安全漏洞与反序列化风险。升级时需按官方迁移指南调整 API 调用及配置，并在测试环境完成功能与性能验证，确保业务无损。

### ▎紧急缓解：开启 SafeMode

完全禁用 AutoType，在解析入口层阻断所有 `@type` 反序列化。目前唯一即时止血手段。

代码启用：

`ParserConfig.getGlobalInstance().setSafeMode(true);`

或 JVM 参数 ：`-Dfastjson.parser.safeMode=true`

或配置文件：`fastjson.parser.safeMode=true`

开启后需回归 `@type` 相关功能，灰度观察解析异常与业务降级。

### ▎补充防护

· 使用防护类设备拦截带有如下内容的POST、JSON请求：

@type":"jar:file:.

@type":"jar:http:..

· 下线闲置接口，补充鉴权与来源限制
· 降低应用运行权限，减少横向影响

## **05. 魔方安全应急响应**

针对此次漏洞事件，魔方安全第一时间启动应急响应机制，由安全专家团队开展漏洞原理分析、影响范围评估及检测能力建设。基于对漏洞利用特征与暴露资产特征的深入分析，已完成漏洞资产指纹识别规则及检测插件更新。

### ▎魔方安全产品支撑

> 魔方外部攻击面管理系统EASM

> 魔方网络资产攻击面管理系统CAASM

> 猎影·暴露面智能运营平台

> 万仞·网络空间资产测绘系统

> 磐石·资产与漏洞一体化运营平台

以上产品均已支持该漏洞检测能力，可针对互联网暴露资产开展精准识别，帮助用户快速发现受影响资产、评估安全风险并及时处置。

![](https://mmbiz.qpic.cn/mmbiz_jpg/3wlibOpCwqMv7nIqdEOibEq7O5ia7tBhPcnvzpWLWPkReYxsaNsGluibDNCoI0C6BfaCqEWt543hbN2WFzyZlXKxkL1JBjm385D0KhwBapTpwAc/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/3wlibOpCwqMu8f35dj6g8Bjibyib73SQASzzIAmoLAwITa5ebKOSZLFytYCFPn5KibSPqcaRnqRjPlgSTBkbkpOHybb01nhPLBRZI4bx68FTBZc/640?wx_fmt=jpeg)

**已采购**魔方安全相关产品的用户，可直接登录平台查看漏洞影响资产检测结果、风险详情及处置建议。

**尚未采购**相关产品的用户，可扫描下方二维码，申请产品试用及专项漏洞检测服务。魔方安全将根据用户实际业务场景，协助开展互联网暴露资产发现、漏洞影响资产识别及风险验证，帮助企业快速了解自身安全暴露情况，及时发现并处置潜在风险。

![](https://mmbiz.qpic.cn/mmbiz_png/3wlibOpCwqMta7OMzVa0MmwnUvEhB76qyibpDnqGKVT21iahDt8lickkibv9nWMibr73Hrx1nX6vu1JvDMlAbtS78UEVHEmsROBEwn9Pkw2Ntaenc/640?wx_fmt=png&from=appmsg)

魔方安全将持续关注全球漏洞情报动态，持续完善资产识别规则、漏洞检测插件及安全运营能力，帮助用户实现风险的快速发现、精准验证和闭环处置，全面提升企业外部攻击面安全防护能力。

**END**

**往期推荐**

Recommend

[![](https://mmbiz.qpic.cn/mmbiz_png/3wlibOpCwqMtS4dgrXkk6CZd5MM9fsNJ8pdKE34GvssyZQZtJJ436iauO9UQXErWMZfP6OSbjEamoEgKHrAHIfPjbNYMZyiauqjURs7ibhT2EN0/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI3NzA5NDc0MA==&mid=2649293088&idx=1&sn=439734caadfb4e7b9eed26791d187228&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3wlibOpCwqMvRU6XW5rdGfNDHxJF67Bpl5EhcG2BqJbOXFh71tbryMpyh355QU5iathoj3pPIFKTyWqZAtujakFNkG3ibAQh9s1sEtiahy4omIc/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzI3NzA5NDc0MA==&mid=2649292993&idx=1&sn=e2a5c546b6f1802068e0697efc0bd787&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3wlibOpCwqMswkznKHLfH2OBnL2LtrEp7Sicb6B1YvjzbkI4FvrlicsOz9LWfiae4cxYYdEnUI1uN8R0TwZIX23dnicEZ0jMSaVU8dfeibKGx3KrA/0?wx_fmt=png)

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