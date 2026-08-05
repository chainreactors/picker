---
title: 工具推荐 | 已发现数十个真实漏洞！AIxVuln自动化漏洞挖掘系统，让安全研究事半功倍
url: https://mp.weixin.qq.com/s/IngUQCW2yEnQbb_uE_9asg
source: Doonsec's feed
date: 2026-08-04
fetch_date: 2026-08-05T04:58:10.659569
---

# 工具推荐 | 已发现数十个真实漏洞！AIxVuln自动化漏洞挖掘系统，让安全研究事半功倍

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g1pTgnczBiaGUAwgGzv6wXicYRMv2IXoxsx7HvCibjQNCgibETwaBicOokTpX5YqmT4jRicxuKf7EddpQG4n2vRou6eu4bicVH2ubBP9U2EPNiaZZXc/0?wx_fmt=jpeg)

# 工具推荐 | 已发现数十个真实漏洞！AIxVuln自动化漏洞挖掘系统，让安全研究事半功倍

m4xxxxx
m4xxxxx

星落安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_png/spc4mP9cfo75FXwfFhKxbGU93Z4H0tgt4O9libYH9mKfZdHgvke0CeibvXDtNcdaqamRk3dEEcRQiaWbGiacZ2waVw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

点击上方蓝字关注我们

![图片](https://mmbiz.qpic.cn/mmbiz_png/WN0ZdfFXY80dA2Z4y8cq7zy2dicHmWOIib5sIn8xAxRIzJibo2fwVZ3aicVBM8RnAqRPH5Libr4f02Zs5YnMLBcREnA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

现在只对常读和星标的公众号才展示大图推送，建议大家能把**星落安全团队**“**设为星标**”，否则可能就看不到了啦！

【声明】本文所涉及的技术、思路和工具仅用于安全测试和防御研究，切勿将其用于非法入侵或攻击他人系统以及盈利等目的，一切后果由操作者自行承担！！！

![图片](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaFmDuy7YwUnJotSNFicibwAFSkg0mOAjMhGMtkO4kFZ2o6EUDJHyXkzHZmTd5Iz7sRzjiafeyD6kfWibOGgN51uZNM0SbZCHDA2pmU/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&watermark=1&tp=webp#imgIndex=2)

***背景介绍***

AIxVuln 是一个基于大模型（LLM）+ 工具调用（Function Calling）+ Docker 沙箱的**自动化漏洞挖掘与验证系统**。

系统通过 Web UI / 桌面客户端管理"项目"，为每个项目自动组织多个**数字人**协作完成环境搭建、代码审计、漏洞验证与报告生成，并在隔离的 Docker 环境内完成依赖安装、服务启动、PoC 验证与证据采集，最终产出可下载的漏洞报告。

目前已通过该项目在真实开源项目中发现数十个漏洞。

## 工具特性

* **首次启动引导**

  — 首次运行自动进入初始化向导，引导创建管理员账户并一键构建所需 Docker 镜像，开箱即用
* 单二进制部署

  — Dockerfile、前端 UI 等资源全部嵌入可执行文件，无需额外文件即可运行
* 项目化管理

  — 支持从 Git 仓库、压缩包上传、压缩包 URL 三种方式创建项目，一键启动/取消，实时查看漏洞列表、容器、事件日志与报告
* 数字人协作

  — 每个数字人拥有独立人格（姓名、性别、年龄、性格、头像、自定义提示词），绑定特定 Agent 能力类型，以持久化实例运行，跨任务复用记忆
* 决策大脑（DecisionBrain）

  — 全局调度中枢，维护状态面板与记忆体，自动编排数字人、汇聚碎片化利用点（exploitIdea）并组装攻击链（exploitChain）
* 团队聊天（Team Chat）

  — 用户可通过 `@数字人名` 或 `@全体` 与任意数字人 / 决策大脑实时对话，数字人之间也可通过 TeamMessage 机制广播消息
* Docker 沙箱与多语言环境

  — 内置 `aisandbox` 攻击沙箱，支持 PHP / Java / Node.js / Python / Go 运行环境及 MySQL / Redis 等中间件
* 双 API 模式

  — 支持 OpenAI Chat Completions API 和 Responses API，可按 Agent 类型独立配置
* SQLite 配置管理

  — 配置存储于 `data/AIxVuln.db`，首次启动自动生成默认值，通过 Web UI 可视化编辑，支持按 Agent 类型独立覆盖
* 报告模板自定义

  — 报告模板存储在 `data/.reportTemplate/`，支持在 Web UI 中直接编辑
* 桌面客户端

  — 基于 Wails 构建跨平台桌面应用（`wailsapp/`），内嵌前端 UI

## 界面预览

### 首页 — 项目管理与创建

支持从 Git 仓库、压缩包上传、压缩包 URL 三种方式创建项目，一键启动漏洞挖掘任务。

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaGmk0xg3yz0vBk41xuCsqFxax34Mybns3nu5iawTIQJnobhLfOscmQxssib73trXKw0GGh48LRm4uGjtdEt23txNAgoR3iaiaiavib5c/640?wx_fmt=png&from=appmsg)

### 项目详情 — 实时状态总览

运行中的项目详情页，左侧展示数字人工作状态与容器列表，右侧展示环境信息（登录凭证、数据库信息、路由示例等），所有信息实时更新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHZdjqKcY9bC5jnUt50TAm1jEnP4C2bMbCy4wk2eHrQGUTnpoYLBXtrCLh0FDeicc26TNY0micRdhX2qmib9NeoAdkJzxZkVp4myU/640?wx_fmt=png&from=appmsg)

### 数字人管理

管理 Agent 数字人角色，每个数字人拥有独立人格（姓名、性别、年龄、性格、头像）和自定义提示词，绑定特定 Agent 能力类型。支持增删改，修改后重启项目生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaE9L2PersPRyO00w2aXBUguqYTzxOkf5mN5tSSD3bxBWsEicH7d2pVRCYBgKBocN6rJ0ib2ArncqUkvwXtkHmBU6HXyibFJP8jPiaA/640?wx_fmt=png&from=appmsg)

### 严格审核机制 — 防止 AI 幻觉

ExploitIdea 经过"审核失败 → 正在整改"等多轮状态流转，决策大脑对每个候选漏洞进行严格审核，防止 AI 幻觉导致的误报。ExploitChain 组装后同样需要经过验证流程。

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaElKoWQKUznFcuQT65so6JGm5PA583crpZUWT9s5c6y0nf5afHTopIOsjrZumv4aOUQ6TZ62jOVZbYVz4xKaMSqZ9OHVaXfPfg/640?wx_fmt=png&from=appmsg)

### 高效的团队沟通机制

数字人之间、数字人与决策大脑之间通过 Team Chat 实时协作。以下展示了一次真实项目中的多轮沟通过程：

**环境搭建阶段** — Ops 数字人汇报编译问题，决策大脑给出修复指令，数字人自主执行修复：![团队沟通-环境搭建](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaFYW2bAdkLWgnStL3O3lgEUqIheWKgjfJgJhDHBUu6MnYjpdSV8BgbIa9btMaUNfbsiaOv4D2ol6JSsgLJRbeLPNYAHUsyK3p94/640?wx_fmt=png&from=appmsg)

**用户实时介入** — 用户通过 @数字人名 直接下达指令（绿色气泡），决策大脑同步协调其他数字人处理环境问题：

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaG0u6PurZbeSUtuqbM8vMafx7Yibc0FFQSIs76NicZXfKjicJwJGsaxXebzKzWzlNib6ULW1yibPsfqrHq3xLTyM3Hdbe5YNodFJAwU/640?wx_fmt=png&from=appmsg)

**决策大脑指导** — 决策大脑针对 MySQL 连接问题给出详细排查步骤和重建方案，数字人据此自主执行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaGbaCKcAUCbOHgrEDVetDjcRYkvbc0SO7aicZHh2mqn05RbcS91Qa3318RibeSuVX7tHn4oN9I4w00PhlZn2GFugg0uHamX69abk/640?wx_fmt=png&from=appmsg)

**多线并行** — Analyze 数字人广播发现的漏洞线索（@all），Ops 数字人同步处理 Maven 依赖问题，Verifier 数字人等待环境就绪后立即开始验证：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHQuLzX8N7WxWZZKRGBXficTXtqI0vXQwxBxOVQibwSSBMa6Ribn4k4stfVSIIsgUBVfwibibHUWKRMM87rkrvPwXvNIcmjn7ibF2HYU/640?wx_fmt=png&from=appmsg)

**自主协作** — 多个数字人同时汇报进展、分配剩余配额、用户可随时 @任意数字人 进行干预：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaHrx0qNM1dxXT9Aiat50MtDTYbibLuUiaseFHq76q8uIU9RKCL52ic4Sd8YcHKGV6kibLnllMic6HDl7jvOiasAvNCF6ohVPleHEicIJlM/640?wx_fmt=png&from=appmsg)

### 漏洞报告示例

系统自动生成结构化漏洞报告，包含完整利用链分析、攻击流程图和验证证据：

**完整利用链分析** — 自动绘制从攻击入口到最终危害的完整调用链路图：

![](https://mmbiz.qpic.cn/mmbiz_png/g1pTgnczBiaG0OzGb6VFS5o6WnKkbwRn3sDP7J13OGmdBVGWGbkv8Tn0WSbLgiccV4gSrEgdQKkwF25SGRE6DyDe2P8Y0padQrrawS35Khco4/640?wx_fmt=png&from=appmsg)

**验证证据与 PoC** — 包含时间盲注验证、UNION SELECT 探测等详细测试过程和关键证据（HTTP 请求/响应）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaFJbgCDlymKHouawJCaMPXdE173zl1mial6FFJC9rZSmiaFR3XzvKfTjgt99GqUF0UAwUg6nWXcuoG5AdC9MicyArcPDyRyqfX4F4/640?wx_fmt=png&from=appmsg)

***相关地址***

****关注微信公众号后台回复“****入群****”，即可进入星落安全交流群！****

关注微信公众号后台回复“20260804**”，即可获取项目下载地址！**

***圈子介绍***

博主介绍：

目前工作在某安全公司攻防实验室，一线攻击队选手。自2022-2024年总计参加过30+次省/市级攻防演练，擅长工具开发、免杀、代码审计、信息收集、内网渗透等安全技术。

目前已经更新的免杀内容：

* 部分免杀项目源代码
* 星落安全内部免杀工具箱1.5
* GoCobaltStrike星落专版2.5.1

* 一键击溃windows defender
* 一键击溃火绒进程
* CobaltStrike免杀加载器
* 数据库直连工具免杀版
* aspx文件自动上线cobaltbrike
* jsp文件自动上线cobaltbrike
* 哥斯拉免杀工具 XlByPassGodzilla
* 冰蝎免杀工具 XlByPassBehinder
* 冰蝎星落专版 xlbehinder
* 正向代理工具 xleoreg
* 反向代理工具xlfrc
* 内网扫描工具 xlscan

* Todesk/向日葵密码读取工具
* 导出lsass内存工具 xlrls
* 绕过WAF免杀工具 ByPassWAF
* 等等...

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=9)

目前星球已满1100人，价格由208元调整为218元(交个朋友啦)，1200名以后涨价至268元。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/g1pTgnczBiaFyWGU2KhdjNRwshvTpgy30xDOHbEI9bSu8D79rJVX77PWuBLnEKBB4RMyMQIYy2wbVV40G82RiaJ7wibnibiaG6IV4ZJmoclHiburQ/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=13)

![图片](https://mmbiz.qpic.cn/mmbiz_png/MuoJjD4x9x3siaaGcOb598S56dSGAkNBwpF7IKjfj1vFmfagbF6iaiceKY4RGibdwBzJyeLS59NlowRF39EPwSCbeQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

往期推荐

1.[加量不加价 | 星落免杀第二期，助你打造专属免杀武器库](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247495969&idx=1&sn=d3379e8f69c2cefb6d0564299e13d579&scene=21#wechat_redirect)

2.[【干货】你不得不学习的内网渗透手法](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489483&idx=1&sn=0cbeb449e56db1ae48abfb924ffd0b43&scene=21#wechat_redirect)

3.[新增全新Web UI版本，操作与管理全面升级 | GoCobalt Strike 2.0正式发布！](https://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247497899&idx=1&sn=018f02ef4064930cbcb40d6b0495e136&scene=21#wechat_redirect)

4.[【免杀】原来SQL注入也可以绕过杀软执行shellcode上线CoblatStrike](http://mp.weixin.qq.com/s?__biz=MzkwNjczOTQwOA==&mid=2247489950&idx=1&sn=a54e05e31a2970950ad47800606c80ff&chksm=c0e2b221f7953b37b5d7b1a8e259a440c1ee7127d535b2c24a5c6c2f2e773ac2a4df43a55696&scene=21&token=458856676&lang=zh_CN#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/DWntM1sE7icZvkNdicBYEs6uicWp0yXACpt25KZIiciaY7ceKVwuzibYLSoup8ib3Aghm4KviaLyknWsYwTHv3euItxyCQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/rlSBJ0fllllT7yxybzslhp8mC8ibaTia9STZtOXaUjfJbHfLJzPAAs44YKKbWvBj9YPicLA34xgAFpXMfB3SaUnUQ/0?wx_fmt=png)

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