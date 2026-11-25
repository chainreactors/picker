---
title: 渗透测试 Agent 平台 - 全链哨兵
url: https://mp.weixin.qq.com/s/C_iKRr1qi3OhomNNZM2LSA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:41.504412
---

# 渗透测试 Agent 平台 - 全链哨兵

# 渗透测试 Agent 平台 - 全链哨兵

GSDK
GSDK

GSDK安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

01项目地址

`https://github.com/zgsfsec/Full-Chain-Sentinel-System`

02项目介绍

全链哨兵（Full Chain Sentinel System）是知攻善防实验室出品的**授权渗透测试 Agent 平台**，通过中英文 Web 控制台，统一管理 Web、小程序与移动端测试、项目环境、审批和证据。

做过授权测试的人都清楚：

`目标资产散落在 N 个工具里，测试过程没有留痕，出口代理来回切，漏洞记录靠笔记，AI 辅助测试又怕它乱来没审批没审计。`

全链哨兵把整条链路装进一个控制台：对话式驱动测试，Agent 在**审批模式下行动**（人工审批 / 自动执行 / AI 审批三种模式可切），项目级隔离容器与会话，漏洞、资产、证据统一归档导出。

**一句话概括：对话里描述授权范围和目标，Agent 按审批边界干活，从流量抓包、POC 检索到移动端调试，一条链路全留痕、可审计。**

![全链哨兵项目概览](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA18q21wHZqSYwtYGKmDiaBRRABk7JLrDjIw1sNiaRjs48PfuSiaWUEia31TI99ktJeFmO4JvOg0Sic862mOicdGVLWVa8NnicLLktIbicEE/640?from=appmsg)

全链哨兵项目概览

03核心亮点

`🤖 对话式渗透 Agent：流式展示回复、思考与工具过程，支持会话分支、文件、终端和子代理，持续目标在自动模式下续跑
🛡️ 审批与审计：人工审批、自动执行、AI 审批三种模式，判定流水按项目、会话、来源、时间与关键词回溯
🕸️ 项目与代理：项目隔离工作目录、容器与会话，Kali 工作容器 + 常驻网关，SOCKS5/HTTP、WireGuard、OpenVPN 可切换出口
🔍 MITM 与 WebFuzz：HTTP 显式代理 + HTTPS 解密证书，流量实时筛选检查，选中数据包一键发送到 WebFuzz 发包工作台
📚 POC 库与订阅：检索引用 Nuclei 模板，官方或自建订阅源定时同步
📡 开源情报监控：批量监控 GitHub 仓库新提交，自动准备漏洞版与修复版源码并新建工程复现
📱 移动端接入：DroidBridge / SentinelBridge 接入安卓与 iOS 设备，按会话启用 shell、文件、抓包、动态调试
🧠 六角色模型分配：主模型、守门、漏洞评审、监督、指挥、监测分配给不同模型，执行监督可定位任务为何继续或停止
🧩 MCP 与插件中心：接入 HTTP / SSE / stdio MCP 服务器，安装官方插件或上传插件包，支持独立前端`

![对话工作台](https://mmbiz.qpic.cn/sz_mmbiz_png/Wq4VJsQicA1ibsjKvzWr1ibVWSIIturf0yTyANIfJPhg7rubfSeOnhKh4d827xzhqg3Aaxnh5wyicms1GoRuBLibHIgdlvib0FibJFdGQCy7riaxjoo/640?from=appmsg)

对话工作台

04部署与使用

安装并启动 Docker，从 Releases 下载对应系统与架构的压缩包（Linux / Windows x64 均支持），解压运行后打开日志中的完整入口地址，设置账号密码并确认授权声明即可。

在「设置 → 环境」准备工具镜像，「设置 → 模型」添加端点并分配主模型，然后创建项目——新项目自带工作容器与常驻网关，切换代理无需重建容器。默认审批模式，在对话中描述授权范围和目标就能开工。当前版本 v2.3.0。

**核心理念：让 Agent 干活的前提是让它带着"缰绳"干活——审批、审计、监督全程在线，效率和安全边界一个都不少。**

⚠️ 免责声明

注：工具仅供安全研究与学习之用，若将工具做其他用途，由使用者承担全部法律及连带责任，作者及发布者不承担任何法律及连带责任。信息及工具收集于互联网，真实性及安全性自测！！

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Xu1xJEZRrFjUe1HmsusbqLJiaQvscUlHp1kgYagMRTFy1TyiaryxmOjvkpS6UKic5ricVOjdicibiaLMTibKkUqiafYD8vw/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过