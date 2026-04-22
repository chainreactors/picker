---
title: 无须编程，聊天造物！乐鑫龙虾 ESP-Claw 物联网 AI 智能体，支持标准 MCP 设备与传统 IoT 设备接入
url: https://mp.weixin.qq.com/s/Mfe90qF0qz-LgqusPOqliQ
source: Doonsec's feed
date: 2026-04-21
fetch_date: 2026-04-22T04:40:51.531351
---

# 无须编程，聊天造物！乐鑫龙虾 ESP-Claw 物联网 AI 智能体，支持标准 MCP 设备与传统 IoT 设备接入

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUg9GhzhxibIib7ianib2BGyJ1oxjo3defmcJZTqX3QYzm7sU9rgA2PVyzuukVbvqr2v8aU1PUwr6cM4jibsRTXx9alBl5IhQk96ryCI/0?wx_fmt=jpeg)

# 无须编程，聊天造物！乐鑫龙虾 ESP-Claw 物联网 AI 智能体，支持标准 MCP 设备与传统 IoT 设备接入

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjiblibTSymO0W8g7enCE44QApytLWev9etFSMhU1OiaVibaBLAMxHDOkDeTrTOn98FjqUExDfoFwsRBE58GHWvRibXkNR0ekKSeJ38/640?wx_fmt=png&from=appmsg)

> 文末联系小编，获取项目源码

众所周知，传统物联网设备至今仍处于被动执行阶段：能联网，却不能思考；能执行，却不能决策；能记录，却不能学习。IoT物联网设备高度依赖云端，且难以实现自然的实时交互。

ESP-Claw 打破了“AI 必须依赖高算力服务器”的局限，推出面向物联网设备的 Chat Coding 式 AI 智能体框架，将 Agent Runtime 下沉至边缘芯片，使设备在本地实现感知、推理与决策的完整闭环，推动物联网设备迈向“自主智能决策”。

在 OpenClaw 理念的基础上，ESP-Claw 增加了如下特性：

* 对话定义设备行为： 通过 IM 聊天 + Lua 动态加载，普通用户即可定义设备行为，无需编程
* 设备端智能闭环：在设备本地完成感知、推理、决策与执行
* 事件驱动： 可由任意事件触发 Agent Loop 和其他动作，而不只是用户消息
* 结构化记忆管理： 在设备端实现结构化记忆与持续学习，隐私内容不上云
* MCP 通讯： 支持标准 MCP 设备与传统 IoT 设备接入，设备具备 Server/Client 双重身份
* 开箱即用： 基于 Board Manager 快速配置，并提供一键烧录
* 灵活与稳定兼顾： LLM 结合本地规则动态决策，所有功能支持模块化按需裁剪

## 🤖 四大核心能力

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgXcZX9GmV7ibGkJ0xvHsaFPq5piaiaeGlbyLbR6srm1NicNDmmoAvav4RklvHXibTO0PHeUibt1B0CbPoh6RJsKUhNVCpwmradyyzXk/640?wx_fmt=png&from=appmsg)

聊天即造物：LLM 动态决策 + Lua 确定性规则

无需编程，AI 生成驱动代码，用户通过飞书、微信或 Telegram 发送一句话，ESP-Claw 即可生成并运行对应的 Lua 脚本——驱动灯带、屏幕、摄像头等外设，或实现自定义游戏、控制算法。测试满意后，生成的逻辑可一键固化为本地 Lua 规则，确保在 LLM 服务中断或更换模型时仍能稳定运行。

![图片](https://mmecoa.qpic.cn/sz_mmecoa_gif/BXztdls6Z78ViaC8JjiboeV9MjxPHjDvuDIdC9ZicKFCAdMCATdlmqZLxZFRoibVNec6Yvd60eIW8blouAuuhYMdB6auV8xGaicKrYicegJjR6nwM/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=6)

毫秒级响应：事件驱动，主动感知

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUjudHVAXk3EOicqJklibkZCGPoMbic0hEAxC6rsicxtILIqeEvqJ5IWhUf9ib0iaMYYrQ3NSVEkcbibCmpu6O9YBiczO5KyAMo2IAperuw/640?wx_fmt=png&from=appmsg)

ESP-Claw 采用事件驱动架构：设备主动上报事件，由本地事件总线触发处理逻辑。对于高实时性需求，通过本地规则直接执行，实现毫秒级响应，断网亦可独立运行。当本地无匹配规则时，Agent 自动调用 LLM 进行分析；对超出本地算力的任务，如图像识别，自动上传云端处理后返回结果，实现云边协同。

![图片](https://mmecoa.qpic.cn/mmecoa_gif/BXztdls6Z7icTE1ribt0hq4LCmd2Yx3ZXAZhK3pTlOiaBrPicA03mJficP1BxsNtrXupKdibrsIicPqjcAibnichhyictSyErrITt0tJ3aCY9LSibOr3F8/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=11)

本地记忆系统：越用越懂你

ESP-Claw 在设备本地实现了完整的 结构化长期记忆系统：

* 五类记忆： 用户资料（profile）· 用户偏好（preference）· 事实知识（fact）· 设备事件（event）· 行为规则（rule）
* 轻量级检索： 不依赖向量数据库，而采用 摘要标签 机制。每条记忆附带 1–3 个关键词标签，请求时系统注入标签池，供 LLM 按需召回正文，从而在 MCU 有限资源下实现高效检索。
* 自动进化： 系统通过对话抽取、事件归档、行为规则沉淀三条链路持续积累记忆。更关键的是，LLM 能从中发现规律，并 主动建议自动化。

![图片](https://mmecoa.qpic.cn/mmecoa_gif/BXztdls6Z7ibCAibeZzsaDQZiaEtNNtwzw9AhBa6RkIXhNiceiaoI0qzpeESlZoy3LnYxl7C74McBrmhUXoZO7mRcSz7MVyia9Xot5UjXK0hEEnX4/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=16)

同时支持对 Agent 核心角色（如 soul、identity 等）的可编辑与持久化，使设备具备可定制的人格与行为风格。

MCP 统一协议：让设备成为 AI 原生对象

ESP-Claw 设备同时具备 MCP Server 和 MCP Client 双重身份：

* 作为 MCP Server： 将传感器读取、执行器控制等硬件能力封装为标准 MCP Tool，任何支持 MCP 的 Agent（如 OpenClaw、Claude、Codex）均可直接调用

  ![图片](https://mmecoa.qpic.cn/mmecoa_gif/BXztdls6Z797lM3BSticM8mjAo7FKhgPED6runoh4tmc1K1J5oMWqyQpwhLwexPXZU84XSaXPAjZqXmprwgkEHaMvZq1EVhaUyYHNP1wDV4w/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=14)
* 作为 MCP Client： 主动调用网络上任何 MCP Server 暴露的服务，包括其他 IoT 设备、PC 端及云端软件能力（如高德地图查询路况、调用飞书发送提醒）

  ![图片](https://mmecoa.qpic.cn/sz_mmecoa_gif/BXztdls6Z78ZfZyOjica5CrbZS9kN2Bcm6oISM1OV7UhFoaFAHWV0AvicKZSsiaPicK9wokicqWovTicwDotjzAmLd8t0gQvaOjtq5bCtoiaA3BWUI/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=10005&wx_lazy=1#imgIndex=15)

采用AI 原生语义接口， 工具命名采用动词-名词结构（turn\_on、get\_temperature），返回值携带单位与新鲜度元信息，AI 无需外部文档即可理解和调用。

## 🔥 项目源码

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiadFwVWzxYW3hVhRzC3BD7Vd23iaMBjlc00KYt7Jibdfp9jf6la8YGF3N3ibzzRfvY3Juv4wDtlI1d3LlvsgKqUjBcyl9dceOic4Wc/640?wx_fmt=png&from=appmsg)

乐鑫ESP-Claw 现已100%开源！目前该框架已支持 ESP32-S3、ESP32-C5、ESP32-P4 等芯片，只需一块 DevKitC 入门级开发板即可开始体验，根据场景需要自由拓展外部传感器和执行器。

乐鑫ESP-Claw代码分为四层：

* **应用装配层：application/basic\_demo/main，负责启动入口、网络连接、参数配置、HTTP 配网页面以及 Demo 级模块注册**
* **能力层：components/claw\_capabilities，包括 IM 通讯、MCP Client/Server、Lua 运行时、调度、文件、时间、Web 搜索等能力**
* **运行时核心层： `components/claw_modules`，包括核心上下文、能力注册、事件路由、记忆管理与技能管理等**
* **设备与脚本扩展层：components/lua\_modules，把显示屏、摄像头、音频、按键、GPIO、存储等外设能力暴露给 Lua 和上层 Agent**

ESP-Claw开源项目地址：

https://github.com/espressif/esp-claw

---

如有IoT 源码采购和项目交付需求，请扫码联系小编，微信号: beacon0418

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiammPZaNSh2HzseQoJ9bNzUSCR9jaK8eBlwD7hS4Qc7LH5ZWOb8IrvxwhaqLcic14VbJIiaWQk4ffEylWbhyeMiaM2q1SaV1EmX40/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgskq8VzxckmN9998ALu5rS2oztQH1K25Dg9soia2ia0gkd7x2AYelfa9HLv70n6ppiaoLbq1n0qSQ6TNoAjof2ibkVoryffJO0gibk/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454939032&idx=1&sn=5679fa0132dd03f96b7854e02250f5bb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/tnMEWNbfO5cnUxs4P033DlMMqqOLqmN4nJPPZIh6azfSNld68R6DUJneWzEdAm0vHbaGxD8KIQe6hsIV3gRK9Q/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454938828&idx=1&sn=c23447c25873fe4f344373b3b2f5303e&scene=21#wechat_redirect)

**往期推荐**

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[4万元，国产信创私有化部署，破解县域无人机AI巡检平台落地难题](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941157&idx=1&sn=b63f67eb0f573b247f47059347b9e407&scene=21#wechat_redirect)

☞[上班摸鱼， 智能 AI 监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请告知我们，我们将尽快处理。主理人微信: beacon0418

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

IoT物联网技术

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tnMEWNbfO5dAnL0wnu7VicnmWCziaZr42icK2RbNCTV6KezOBgYPIZc7hiaZiaTaUnPZzwShBn7FXicr96iamdc0kKPYw/0?wx_fmt=png)

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