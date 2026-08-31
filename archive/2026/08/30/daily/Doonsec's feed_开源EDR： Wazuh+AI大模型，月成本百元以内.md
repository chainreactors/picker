---
title: 开源EDR： Wazuh+AI大模型，月成本百元以内
url: https://mp.weixin.qq.com/s/Xf0OGoSREYDQ-VaqIclCIA
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:51:05.797067
---

# 开源EDR： Wazuh+AI大模型，月成本百元以内

# 开源EDR： Wazuh+AI大模型，月成本百元以内

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

|  |  |
| --- | --- |
| 网络安全老宋 | 安全加固 · 开源EDR |

// Wazuh · AI研判 · 成本控制

# 甲方运维的开源EDR： Wazuh+AI大模型，月成本百元以内

商业 EDR 一年几万到十几万，开源 Wazuh + AI 分析月成本能压到一杯奶茶钱——前提是有人愿意维护。

目录 · Contents

00为什么开源 EDR 值得认真考虑

01Wazuh 是什么，怎么搭

02AI 集成怎么把成本压到百元以内

03开源栈的组合打法与两条提醒

04老宋说

🔑 一句话精华：商业 EDR 一年几万到十几万，开源 Wazuh + AI 分析月成本能压到一杯奶茶钱——前提是有人愿意维护。

前阵子有篇 Wazuh 部署实战在圈子里传得挺广：作者用一台普通 Windows 机器 + WSL2 + Docker 全本地搭了一套开源 EDR 架构，Wazuh 4.14.6 做端点检测，接了个 DeepSeek AI 分析器自动研判告警，四层过滤把 AI 调用量砍掉 80-95%，算下来月成本 百元以内。

这套方案的价值不在于「跑通了」，在于它把一件很多小团队想都不敢想的事变成了现实：没有专职安全分析师、预算有限，也能有一套能看的端点防护。今天把这条开源 EDR 路线拆开讲清楚。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flibvyBvibAIm4sqkwiaUhV6aa3mHOribPYOys3tCQREYKk2icibshG12ot1XRpFgD1JyPkIicKrxQAXiaiaGRF2zAaPbrm9cVAeQ6sWjJ2o/640?wx_fmt=png&from=appmsg)

## 00为什么开源 EDR 值得认真考虑

先算一笔商业账。CrowdStrike Falcon、Microsoft Defender for Endpoint 这类主流商业 EDR，价格普遍在 每端点每年 50-150 美元，一个 50 人的小团队一年就是大几千到上万美元——而且这个价格的前提是，你把每个端点的进程执行、文件访问、网络连接遥测全部发到厂商的云上。

// 老宋数据 · 开源 vs 商业 EDR

|  |  |  |
| --- | --- | --- |
| $50-150  商业 EDR 每端点每年 | 15,445  Wazuh GitHub Stars | ¥0-20  开源 + AI 月成本 |

开源路线把这些全变了：零许可费、遥测留在自己手里、架构透明。更关键的是，开源安全生态在 2026 年已经成熟到能打了——Wazuh 自 2025 年 10 月以来发了 5 个 point release，拿下两个 2026 Cybersecurity Stars 奖（云安全 + SIEM），GitHub 15,445 stars，被业界评价为「2026 年开源 SOC 最可辩护的起点」。

安全运营圈甚至给出了完整组合拳：Wazuh 做 SIEM/XDR 检测，Velociraptor 做深度取证，osquery 做资产盘点，Sigma/YARA 做检测规则，TheHive 做案件管理，MISP 做情报共享——这条链路两个工程师一个季度就能搭起来，成本是运维工时，不是许可费。

## 01Wazuh 是什么，怎么搭

Wazuh 是一个统一 XDR + SIEM 的开源平台，四大组件：Agent（端点上的轻量代理）、Manager（收集分析告警）、Indexer（基于 OpenSearch 的搜索存储）、Dashboard（可视化）。GPLv2 协议，基于 OSSEC 发展而来，支持 Linux/Windows/macOS 全平台。

|  |  |  |  |
| --- | --- | --- | --- |
| A  Agent  端点轻量代理 日志+FIM+SCA | M  Manager  收集分析告警 规则引擎+主动响应 | I  Indexer  OpenSearch 引擎 告警搜索与存储 | D  Dashboard  可视化界面 Agent 管理+报表 |

原文的部署路径很值得抄作业，几个关键点：

|  |  |
| --- | --- |
| R1 | **版本选稳定版**作者踩的第一个坑就是默认分支克隆到 5.1.0-alpha0 不稳定版——一定 git checkout 到最新稳定 tag（当前 4.14.x）。 |
| R2 | **WSL2 两个必调参数**.wslconfig 给 WSL2 分配 12GB+ 内存；Indexer（OpenSearch）要求 vm.max\_map\_count=262144，每次重启重置，写进 ~/.bashrc 自动执行。 |
| R3 | **日志控制从第一天就做**Manager 配置 logall no（不开全量日志）、log\_alert\_level 3；建 ISM 索引保留策略 30 天自动删；FIM 别盯 C:\Windows 大目录，先从小目录测。 |
| R4 | **密码要分清**v4.14 有三套凭据：Dashboard 登录（admin）、REST API（wazuh-wui）、内部用户（kibanaserver），混了就是认证失败。 |

## 02AI 集成怎么把成本压到 20 元

这是整套方案的灵魂：小团队没有专职分析师，让 AI 当「值班研判」。

架构很朴素：Wazuh Manager 把 level 5+ 告警通过 integration 转发到本地 FastAPI 服务，FastAPI 调用 DeepSeek API 分析后返回结构化结论（严重级别、分析、建议）。每条告警消耗约 700-1000 token。

关键在四层过滤——直接全量转发，告警风暴能把你一个月预算几分钟烧光：

|  |  |  |
| --- | --- | --- |
| 过滤层 | 规则 | 效果 |
| Level 过滤 | 只分析 level 7+（Critical/High） | 过滤 60-70% |
| 规则黑白名单 | 只分析关心的规则 ID | 过滤 10-20% |
| 频率限制 | 同规则+同端点 5 分钟最多 3 次 | 过滤 10-15% |
| 内容去重 | 相同告警 10 分钟不重复分析 | 过滤 5-10% |

实测效果：Wazuh 每天产生 1000 条告警，真正调 AI 的只有 50-200 条，月成本 百元以内；告警量大到离谱（每天 1 万+）也差不多。

但我要补一句清醒的话：AI 分析是「加速研判」，不是「替代判断」——它帮你把 1000 条告警筛成 20 条值得看的，最后拍板还得靠人。接 AI 之前，先把 level 分级和规则过滤调准，否则喂给 AI 的全是噪音。

## 03开源栈的组合打法与两条提醒

Wazuh 只是起点，原文作者也列了后续：Velociraptor 做深度取证、osquery 做资产发现、飞书/钉钉告警推送。按成熟度分步加，别一口气全上。

两条提醒值得刻在桌上：

|  |  |
| --- | --- |
| 01  免费 ≠ 省力  省的是许可费，不省运维工时——规则调优、告警降噪、版本升级都是活。没人维护的开源工具，就是「更便宜吃灰的摆设」。 | 02  选型前先想清楚  不是所有团队都需要 EDR——先想清楚业务线真正的问题、你 hold 不 hold 得住，不要赔了夫人又折兵。 |

## 04老宋说

// 老宋说：开源 EDR 这条路的本质，是把「端点安全」从「买得起的人的奢侈品」变成了「愿意动手的人的日用品」——商业 EDR 每年几万到十几万、遥测还要上云，开源栈零许可费、数据留在本地，2026 年生态已经成熟到 Wazuh 连拿两个行业奖、被当成开源 SOC 的默认起点，这说明端点防护的入门门槛正在被系统性拉低。行业观察是，开源 EDR + AI 研判的组合正在填补「请不起分析师的小团队」这个真空，但它的天花板同样清晰：规则调优、告警治理、事件响应这些活，工具替代不了人力投入，免费软件的运维成本只是换了一种货币在支付。给你一句实在的建议：如果你团队确实没有专职安全人员，别一上来就全量铺开——先挑 10 台核心终端装 Wazuh，把 level 分级和过滤规则调两周，确认有人能接住告警，再谈扩大范围；工具是给你省力气的，不是给你添包袱的。

```
https://mp.weixin.qq.com/s/7LjHk3HcfCbumG9wjDLn8Q      https://github.com/wazuh/wazuh
```

防御，不是在演练期间发现攻击，而是在演练开始前就把攻击面收敛到最小。

end

不想错过文章内容？读完请点一下**“在看**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g5u115ni&tp=webp#imgIndex=1)******”**，加个**“****关注”**，您的支持是我创作的动力

期待您的一键三连支持（点赞、在看、分享~）

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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