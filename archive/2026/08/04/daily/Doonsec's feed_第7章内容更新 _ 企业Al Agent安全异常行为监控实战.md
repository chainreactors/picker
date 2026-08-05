---
title: 第7章内容更新 | 企业Al Agent安全异常行为监控实战
url: https://mp.weixin.qq.com/s/aW0eQX2iO_ODBR1XRn30Dw
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:55:29.869834
---

# 第7章内容更新 | 企业Al Agent安全异常行为监控实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3oqhn1BGnJo8GicRkY8MsjLWHPIvMwth1dx3c0etVRxd52iaocsugWZ9mYpuPFvVJCJdS4hZF4NfZeYBcluTVw8wIia6YF304VzU/0?wx_fmt=jpeg)

# 第7章内容更新 | 企业Al Agent安全异常行为监控实战

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

随着大语言模型在企业中的快速普及，AI 调用行为已成为安全管理的新盲区。

员工将 API密钥、数据库凭证、客户隐私数据直接粘贴至对话窗口，攻击者通过 Prompt 注入绕过 Agent 安全策略，Token费用缺乏有效追溯机制——这三类风险在绝大多数企业中仍处于**无监控状态。**

传统 WAF 防不住 Prompt 注入，普通 DLP 覆盖不了 AI 对话场景，采购商用方案动辄几十万起步，自研又摸不清完整链路。有没有一套能快速落地、拿来就能用的企业级 AI 安全运营方案？

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2XOy5524MczZLWpuyWHFicCxgxWcjudCc7UcXGouMhV8RTpLJT2WEcchhmnxhNtNe7v4rZu7ibyrqPVR0K9coZ6NDbrcJ8ZMsBA/640?wx_fmt=jpeg&from=appmsg)

¥199

从零手写检测引擎+可视化大屏+AI 智能分析

本课程围绕 LLM 安全运营中心（LLM SOC） 的完整建设展开，采用**"网关 → 检测引擎 → 可视化大屏 → 告警响应"四层架构：**

* 基于LiteLLM 构建 AI 统一网关
* 使用 Python FastAPI 开发 DLP 敏感信息检测与 Prompt 注入分析引擎
* 通过 ThinkPHP 8 +  ClickHouse + ECharts 搭建7模块可视化运营平台

最终交付一个集审计报告、用户风险画像、数据泄露追溯、LLM  行为日报、多平台实时告警于一体的企业级安全产品**。**

**学完这门课，带走 7 项硬核产出**

**1**

**一套可复用的 LLM 安全检测引擎**

Python FastAPI 实现，含 DLP 敏感信息正则、Prompt注入识别、异常行为分析三类检测器，独立部署，可直接接入现有 AI 网关。

**2**

**一个 ClickHouse 日志存储方案**

建表语句、查询封装、7 个常用统计方法开箱即用，列式存储下亿级日志也能毫秒响应。

**3**

**一个 Apple 风格可视化大屏模板**

深色科技风、毛玻璃侧边栏、ECharts 图表、hash 路由 SPA，可替换数据源直接复用。

**4**

**一份可直接打印签字的审计报告格式**

6 章证据链结构，Prompt 原文直出，用于合规审计或违规定责。

**5**

**集成 LLM 实现岗位感知分析**

调用大模型自动比对员工岗位与 Prompt内容，识别简历求职、私活外包、个人投资等非工作行为。

**6**

**三平台消息推送能力**

飞书交互式卡片、钉钉 Markdown + @全体、企业微信富文本，三种通道均已调通。

**7**

**一套完整的企业 AI 安全运营方法论**

从威胁模型、检测策略、风险定级到告警响应的全链路经验，可直接套用到团队实际业务中。

**谁适合学？**

课程难度定位初级；

前置要求：PHP 基础、会用 Docker、了解 HTTP 协议

* **后端开发工程师**— 通过实战项目切入 AI 应用层开发，掌握 LLM 网关集成、Prompt 安全机制、大模型调用链路等前沿技术点。
* **安全工程师** — 将传统安全能力延伸到 AI 场景，学习 DLP 敏感数据检测、Prompt 注入防御等新型安全技术。
* **AI 技术爱好者** — 不止于调用 API，深入理解从网关、检测到可视化的完整 LLM 应用链路，建立对 AI 系统工程的全局认知。
* **计算机相关专业学生** — 通过企业级实战项目，提前接触 Docker、ClickHouse、LLM等工业界主流技术栈，缩短从课堂到岗位的距离。

**课程目录：步步有产出，跟着做不迷路**

第一章 · 基础设施搭建

- 1-1 为什么要建 AI 统一网关

- 1-2 Docker Compose 启动四大服务

- 1-3 ClickHouse 日志表设计

第二章 · 后端项目初始化

- 2-1 技术选型：为什么是 ThinkPHP 8

- 2-2 Composer 创建项目骨架

- 2-3 ClickHouse 查询服务封装

第三章 · 安全威胁模型

- 3-1 数据泄露的三种场景

- 3-2 Prompt 注入的四种手法

- 3-3 异常行为与威胁矩阵

第四章 · DLP 敏感信息检测

- 4-1 9 条正则规则设计

- 4-2 FastAPI 检测引擎实现

- 4-3 四级风险评分体系

第五章 · 注入检测与网关集成

- 5-1 注入规则与行为检测规则

- 5-2 注入 + 行为检测器实现

- 5-3 LiteLLM Callback 全链路打通

第六章 · 首页可视化大屏

- 6-1 大屏设计思路与视觉风格

- 6-2 页面模板与数据 API

- 6-3 ECharts 图表与前端交互

第七章 · 告警中心与审计报告

- 7-1 告警体系设计

- 7-2 告警列表与筛选

- 7-3 审计报告证据链抽屉

第八章 · 用户画像与规则配置

- 8-1 六维度用户风险画像

- 8-2 规则可视化编辑面板

第九章 · 数据泄露追溯

- 9-1 事件维度 vs 资产维度

- 9-2 三层手风琴追溯布局

- 9-3 敏感内容自动高亮

第十章 · LLM 行为分析日报

- 10-1 为什么岗位信息是关键变量

- 10-2 DeepSeek 岗位感知研判

- 10-3 缓存策略与日报列表

第十一章 · 告警推送与系统配置

- 11-1 飞书/钉钉/企微三平台推送

- 11-2 系统设置与 API Key 管理

第十二章 · 一键部署与课程总结

- 12-1 setup.sh 全自动部署

- 12-2 生产环境注意事项

- 12-3 12 章知识体系回顾

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3AwNhoFwgIlOuwXAwPBTCD8whOF9ibGtmDRlodHFibbibKGAiaVTE8YROxnZzZzia1qPGAasHKnAxmvB61fVT3Oic4Z2KxhbHr9zoYc/640?wx_fmt=png&from=appmsg)

**阶段一・地基（第 1-2 章）**

Docker 环境 + LiteLLM 网关 + ClickHouse 建表 + ThinkPHP 项目骨架，跑通第一条数据通路

**阶段二・检测（第 3-5 章）**

安全威胁模型梳理 + DLP 检测引擎 + Prompt 注入检测 + Callback 全链路集成

**阶段三・可视化（第 6-8 章）**

首页大屏 + 告警中心 + 审计报告 + 用户画像 + 规则配置面板

**阶段四・智能（第 9-10 章）**

资产维度数据泄露追溯 + LLM 岗位感知行为日报

**阶段五・生产化（第 11-12 章）**

三平台告警推送 + 系统配置 + 一键部署脚本 + 完整知识体系复盘

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K3ULXgF4Ro1pic8fOOgexU7hcDTbzG4S4jGx6m5Sia0gotbkSKFYW2OOYTqkiaxtw7rUU0Soey20eY5eF7eVqtHt65PS4LEB0gfqI/640?wx_fmt=png&from=appmsg)

**实战派讲师坐镇**

**陈婷：**Web 安全专家，GitHub项目QingScan 作者，代码审计、漏洞挖掘、安全编程领域近年以上实战经验。

**报名入口**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K2n1FxKAATNT0H24Yg7oZ15dP3ZmurnZ56ULM2ib5QicLeIWLv5n4f3rwxStgoabozZBCricTj1aCL5B7b6r1Fuu5ja6kqp3uULWs/640?wx_fmt=png&from=appmsg)

¥199

一次购买永久回看，学完即可交付完整产品

**课程咨询**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K3ia7wcoBPYRpDCNXpuoVuSYbsQ8PP8lza4bN4fZGzZciaMic7xDtibRRzjbpsRzfaxnnQPf9PMgqNRQdH0JicSOM0woGOnicrJLqia4w/640?wx_fmt=png&from=appmsg)

**添加企微，一对一咨询**

大模型早已不是尝鲜工具，而是企业的日常生产力。

AI 用得越广，安全的底线就越不能松。等到数据泄露了、账单爆了、被合规通报了再补，代价只会更高。

与其到处找零散资料踩坑，不如跟着这套完整方案，亲手搭出一套能落地的企业级 AI 安全运营平台。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2lHSJaprmcfaXzge6hKO4gEIvlQy97knjibJT37KHz2VaUu6nve0X6PGuNDGSYQB2DWb9bIwkEjRVt4KNr3nmoryG5hwkq0fHI/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K3w5aXMbRuCXADAcdnNySdlIu6SaF9BB8WPPTul3UfYWxFBPYiaxcyibicFzq9UmuqLKN7OawfOHNH2ic3D9Y1x1e9fNtvZ9xWBHzE/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K2fRUFjrqvficxw3SqqaxpTiabcib4cicvRB9kiaw1xJ2OQSia6QORbD0GublvicuI0IXZFum4aISYzeIP2ice4op5IicW5Ww2PCG8ickGqU/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K1DbA3pubcqEdJU8bJFsMGtmdyia2LrQp92gHdhOiamYf767JiaMD1YCU1Z1s5fX0kjxGZzCx63cNehvfulVf2cUDEcVlyt7QOB5M/640?wx_fmt=gif&from=appmsg)

**球在看**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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