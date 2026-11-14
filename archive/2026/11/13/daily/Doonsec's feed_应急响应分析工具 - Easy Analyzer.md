---
title: 应急响应分析工具 - Easy Analyzer
url: https://mp.weixin.qq.com/s/XeKb8lAJfGjOqaS2k3kPpA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:14:21.988036
---

# 应急响应分析工具 - Easy Analyzer

# 应急响应分析工具 - Easy Analyzer

GSDK
GSDK

GSDK安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

01项目地址

`https://github.com/MoShouSecurity/Easy_Analyzer`

02项目介绍

应急响应做到一半，证据管理最容易崩盘：

`日志在服务器上 grep，进程信息截图存桌面，
抓包分析一个工具、IOC 比对一个表格，
客户问"进展如何"，你得现场翻半天记录，
第二天续办，昨天的筛选条件和备注全没了，
AI 倒是能用，可证据一上传，脱敏和数据边界全裸奔。`

**Easy Analyzer** 是使用 Rust 开发的跨平台应急响应分析工具，提供 CLI 和桌面 GUI 双形态，支持 Windows x64、Linux x64、macOS ARM64——把日志、进程快照和抓包证据放进**一个案件**：筛查线索、核对原文、保存分析过程，适合离线证据分析、现场排查和多天续办。默认全部在本地完成解析、规则筛查与 IOC 匹配；AI 辅助由用户选择证据范围后主动发送，发送前可预览范围与预算。

![分析概览](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Wq4VJsQicA19TGfQUibvxic3ovvdoCcP7ocptfia7Ppx5IMpnapicDHmrhhquiclNbzOShnGwLLYo2TFf5xzicfamUPqTY4iacnMQAABevVu2EAiaDzc/640?from=appmsg)

分析概览

**一句话概括：一个 `.eair` 案件文件装下整场应急响应——日志、进程、抓包、IOC、AI 分析、报告导出全在本地完成。**

03核心亮点

`📁 案件管理：每次响应保存为独立 .eair 项目（内置 SQLite，证据无损压缩），持续追加证据，保留备注、AI 历史、IOC 清单和筛选条件
📄 日志分析：Windows EVTX、Linux 登录与 SSH 日志、Apache/Nginx 访问日志全支持，自定义 Web 日志格式，多维查询 + 原文核对
🧷 本地规则筛查：重复失败登录、失败后成功、账号权限变更、日志清除、可疑脚本执行、Web 攻击请求等线索一键筛出
🌳 进程分析：采集本机进程或导入 JSON 快照，识别编码执行、下载执行、临时目录运行、Office 启动脚本解释器等特征
🌐 离线流量：导入 PCAP/PCAPNG，双向会话汇总，提取 HTTP 字段与 DNS 查询名
🎯 IOC 匹配：IP/域名/URL 离线扫描，命中值定位字段位置并跳转证据原文
🤖 AI 辅助：用户主动选择范围发送，发送前预览预算，相似日志自动聚合省 token，证据引用校验
📖 命令速查：Windows/Linux 各 24 条排查取证命令按六类组织，附权限与适用条件说明
📤 报告导出：完整 HTML/JSON 报告，保留证据来源与原始记录，界面筛选不裁剪报告证据`

![IOC 匹配](https://mmbiz.qpic.cn/mmbiz_jpg/Wq4VJsQicA1ickXbQySUTa14SOkhnXRJZSGDfxuOBAMR1icdy247wLo5tk4g0JWZ7lqSAcwLx0dXERZQTWn8P3oaJ4tD7dviaqBQzNxCdA85cSw/640?from=appmsg)

IOC 匹配

04快速开始

从 Releases 下载对应平台程序（CLI 与 GUI 独立发布，附 SHA256SUMS）：

`# CLI 筛查日志
./easy-analyzer logs cases/Security.evtx -s

# 关键词 / 正则查询
./easy-analyzer logs cases/access.log -q 'union.*select|\.env' -r

# 混合导入 + 导出报告
./easy-analyzer analyze cases/auth.log cases/processes.json cases/capture.pcapng

# 案件创建与续办
./easy-analyzer project create response.eair --client "演示客户"
./easy-analyzer project import response.eair cases/auth.log --ioc indicators.csv`

GUI 流程更直接：新建项目 → 拖入日志/进程快照/抓包 → 分析概览看发现 → IOC 匹配 → 需要时开 AI → 保存 `.eair`、导出报告。项目文件手动保存，拷到另一台机器接着办，不需要原始文件和数据库服务。

边界也说清楚：网络能力限于离线分析（不做实时抓包和 TLS 解密）；AI 不会自动脱敏，发送前自己把好范围；本地规则和 AI 发现只是辅助核查，不等于确认入侵。

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
在看
，轻点两下取消在看
分享
留言
收藏
听过