---
title: 国产开源 WorldClaw 一句话让 AI Agent 驱动 Blender 生成可自由探索、可持续编辑的多视角 3D 开放世界
url: https://mp.weixin.qq.com/s/tdXEBC0Z367zsuDxRvpONg
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:24:10.733245
---

# 国产开源 WorldClaw 一句话让 AI Agent 驱动 Blender 生成可自由探索、可持续编辑的多视角 3D 开放世界

# 国产开源 WorldClaw 一句话让 AI Agent 驱动 Blender 生成可自由探索、可持续编辑的多视角 3D 开放世界

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjvibqO1iacObaTSFZQUEB8LdeWAlVudHSA5s3jtrvvnic58APMAtwRIXPMoMg5iaOebIGYI1TDOakXl3xPonVYSJJbs8eAIU1jv4U/640?wx_fmt=png&from=appmsg)

> 多视角渲染、局部生成、视觉自检修复

WorldClaw采用由粗到细的Agentic 3D世界生成方式，多个Agent协作完成用户意图分析、场景规划和全局地形构建，再根据各区域的功能和地形条件，逐区生成建筑、车辆、植被等内容，并将其转换为可单独编辑、替换和复用的3D资产，并且全流程在 Blender 里闭环。初始场景完成后，Agent还会根据多视角渲染结果，持续检查并修正物体尺度、姿态、悬浮和穿模等问题。

* 模型聚合网关：通过 WorldRouter 统一接入 300+ AI 模型，一次配置可调用 Claude、GPT、Gemini、Qwen 等主流大模型，无需分别对接各厂商接口。
* 智能任务助手：自动抓取并整理用户待办事项，根据优先级提醒处理邮件回复、账单续费、生日预订等日常事务，支持一键确认或延后。
* 生活代理服务：基于自然语言理解完成订餐、购物、鲜花预订等操作，界面集成 Amazon、Uber Eats、DoorDash 等平台快捷入口，实现对话式本地生活闭环。
* 财务与成本监控：实时追踪账户余额及股票、加密货币行情，主动识别 AWS 等云服务费用异常并推送优化建议，帮助用户降低非必要开支。
* 硬件本地部署：提供专用迷你主机设备，支持本地 AI 运算与模型推理，满足对数据隐私和离线能力有要求的用户场景。

> 输入一段自然语言描述，直接产出一套可自由漫游的 3D 开放世界。例如「中世纪村落，雪山、平原、湖泊、沙漠，有动物」，可以生成多地貌混合的完整环境，官方给出了峡谷定居点、热带岛屿、北极前哨、四季村庄等11 套示例场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjZLbiamb3qoUetSnhic3rrH8X35pabmeGc9FicsV96dLP0QW9eaBW7Bv8GSmwJHLGblQVIcX25T9X8nRsUSMibPRRUia4htouo7AMw/640?wx_fmt=png&from=appmsg)

智能场景规划，精准拆解需求

内置规划 Agent，可深度分析用户输入的开放式自然语言提示词，将其转换为包含区域划分、地形类型、物体布局、材质属性及空间关系的结构化场景规格，为后续生成奠定清晰框架。

全局到局部生成，保障场景连贯性

采用“先全局后局部”的生成策略，先搭建完整的世界地形与空间框架，再逐步填充各区域的建筑、植被、物体等细节，从根源上避免道路断裂、尺度失衡等问题，保障场景整体连贯性。

独立资产生成，支持灵活编辑

生成的建筑、植被、车辆等各类对象均保持独立实例，而非单一烘焙模型，支持单独移动、替换、编辑，创作者可根据需求灵活调整场景内容，适配个性化创作需求。

视觉自检与修复，自动修正缺陷

搭载视觉 Agent，通过多视角渲染检查场景中物体的比例、姿势与接触问题，自动修复物体悬空、穿模等常见缺陷，无需人工手动修正，保障场景物理合理性。

Blender 深度整合，全流程高效操作

全流程运行于 Blender 5.1.1，深度整合地形生成、资产生成、场景摆放、缺陷检查与渲染全环节，支持 MCP 接口操作，创作者可在 Blender 内完成所有创作步骤，无需切换多个工具。

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUia1Zm4qsVfk3RlLUMHELT8fQlehxcv1ibu0JelSxZvNDIcnrq9ee4icfFPpcKlFMCtxn3bHkHg9icYG5La9A0MMnhefJAVsml66EQ/640?wx_fmt=png&from=appmsg)

> 一个中世纪风格开放世界村庄，有木屋、石塔、市集摊位，道路由石板铺成，连接各区域；有动物栖息，整体色调温暖，适合俯视角和第一人称探索的游戏场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUh8rRZliclQ4Up2ia2gopc4sm15RlNRVMsKf6cx22HlgKLDI7UibUiaticfpKfS5d52ibq21AOTopfQ0fkUkJ0rcWnOPywJlEicmpUkX8/640?wx_fmt=png&from=appmsg)

Github 项目地址: Tencent-Hunyuan/Hunyuan3D-WorldClaw

---

点个关注 **🌟，精彩不迷路 ❤️**

**往期推荐**

☞[小赚3万元！全靠这套开源AIoT 企业物联网平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946282&idx=1&sn=ad676c8d5c0785c5915e5c96ba318d82&scene=21#wechat_redirect)

☞[开箱即用！国产开源30+AI视觉算法IoT智能物联网云平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941969&idx=1&sn=bd91e2bdae181e82774c394c0e709f4b&scene=21#wechat_redirect)

☞[国产开源Web 工业IoT组态软件，支持Modbus、OPC，支持拖拉拽](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454941531&idx=1&sn=dce5163565601e80d153821745715745&scene=21#wechat_redirect)

☞[源码交付，7天完成国产信创部署智慧工地方案](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454940216&idx=1&sn=316b42125f746e16289fe04031496b10&scene=21#wechat_redirect)

☞[5万元斩杀线！ 一网统飞无人机AI巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454945550&idx=1&sn=403e8d5bad8c53ff1b7514a5e1146255&scene=21#wechat_redirect)

☞[上班摸鱼， 树莓派DIY智能 AI 视频算法监控老板行踪](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454932745&idx=1&sn=532fc401409718148a07b35002c40b98&scene=21#wechat_redirect)

☞[免费开源，千知AI知识图谱平台，支持DeepSeek、Qwen](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944463&idx=1&sn=879157ebcc69d371ad87aa3816db7bc7&scene=21#wechat_redirect)

☞[信创部署，源码交付！县域低空经济无人机 AI 巡检平台](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944340&idx=1&sn=0bd578639500191483b4c76cc9083052&scene=21#wechat_redirect)

☞[智慧农业大爆发：AI+物联网+区块链重构“天空地”一体化监测](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454944207&idx=1&sn=27aba015734707013b311674825c37cc&scene=21#wechat_redirect)

☞[一站式AIoT视频聚合平台，适配国标28181和国密35114协议](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946211&idx=1&sn=0072cf454ac83d98adb64c5767e58901&scene=21#wechat_redirect)

☞[“空中奇兵”无人机多光谱罂粟巡查平台，识别出苗期、花期、果期](https://mp.weixin.qq.com/s?__biz=MjM5OTA4MzA0MA==&mid=2454946024&idx=1&sn=6b7d30937351bcce27a0d930c5727726&scene=21#wechat_redirect)

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请及时告知，我们将尽快处理。

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