---
title: 65元，打造私人 AI 助理！国产开源 PicoClaw 把 Claude/DeepSeek/豆包 塞进树莓派，管控 IoT 智能家居设备
url: https://mp.weixin.qq.com/s/3JAVZDW_zXCO-tBs4l8B4Q
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:22.531219
---

# 65元，打造私人 AI 助理！国产开源 PicoClaw 把 Claude/DeepSeek/豆包 塞进树莓派，管控 IoT 智能家居设备

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0VE9kDxicLUiaDkW2mzOFIQ82k5icKAMFA7EAG6ACMDACDGGUB4Us8Om0W7bRUPnQCyibffkYEZSz3Wf3KpoRMfNJTGtpogC8dRm1BRKsb2hous/0?wx_fmt=jpeg)

# 65元，打造私人 AI 助理！国产开源 PicoClaw 把 Claude/DeepSeek/豆包 塞进树莓派，管控 IoT 智能家居设备

原创

.
.

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiaicd3FjhpcORkXzp07XpBQHsgph50uiaDHJuKJQqh2ho1fk4YrItdTbdKia649Jt6nmz3al5KayH1dVrCTTg5Aq0spDAmfx4JKfU/640?wx_fmt=png&from=appmsg)

> 文末**获取项目源码**

PicoClaw 是一款国产开源的轻量级私人 AI Agent 助手，采用 Go 语言编写，可部署在乐鑫ESP32、树莓派Zero/3B/4B/5 等系列硬件上，内存占用不到 10MB，启动时间不到 1 秒，仅需USB 供电，连上家中 Wi-Fi，即可实现7×24小时在线工作，通过钉钉、飞书和企业微信提供Claude、DeepSeek、Qwen、豆包等智能体服务。

PicoClaw 底层基于 OpenClaw 打造，面向物联网低功耗设备，抽象了模型、工具、记忆和执行层，比同类方案资源占用小 99%，响应速度快 400 倍，可以一次构建、随处运行。

* Go 原生实现，二进制部署，可在乐鑫ESP32、树莓派zero、 RISC-V、ARM64 、安卓等众多 10 美元硬件上运行。

* 多 LLM 支持：修改配置文件，即可切换 OpenAI、Claude、DeepSeek、豆包等大模型。
* 本地安全优先：自托管，数据留在你的设备上，你可以完全控制你的 AI 助手。
* 多聊天渠道支持： 通过钉钉、飞书、企业微信、LINE、QQ、Discord、Slack 将 AI 连接到任何设备。

* 本地记忆：Markdown文件形式持久化存储AI人格、用户信息和长期记忆，断电重启不丢失。
* 工具调用：支持网络搜索、获取时间、GPIO硬件控制等工具，实现ReAct模式的Agent循环。

## 🦀 为什么选择 PicoClaw ？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaLoxXINGmPvR8mNq36XGDHYqHWnhHWhx6EMmK8NKTWX5IfF0jBRodDWV9Jg12Eiccczia0b94IGutIY0USB2mOrkjbcia66Xj0Es/640?wx_fmt=png&from=appmsg)

PicoClaw 本质是一个运行在乐鑫ESP32、树莓派等物联网设备上的AI Agent 客户端框架，它可以：

🌐 通过WiFi 连接互联网

🤖 调用大模型 API（OpenAI / Anthropic / DeepSeek 等）

⚡ 本地执行逻辑，控制智能家居设备

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiaN3wDW5SRS9QHXeiaAeHMvaz6lYaYWC8uxsVfHUa4iag5PnZrDuJSWoK1t66FMENNkiaLaryqK3loZKVR4K2yUicZDHoiaPa5YTibQQ/640?wx_fmt=png&from=appmsg)

## 💎 性能优势

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgTq70SDMtH3lzCkibm8OHBy9XRq18Ad7dr6pm588oC8uc1bPV8OMDtNEJHmLflW6K6CY8TgqdiclcE1mYoflibdq6YXY4l4gIHhw/640?wx_fmt=png&from=appmsg)

| 指标 | OpenClaw | NanoBot | PicoClaw |
| --- | --- | --- | --- |
| 编程语言 | TypeScript | Python | Go |
| 内存占用 | >100MB | >100MB | <10MB |
| 启动时间 | >30s | >30s | <1s |
| 最低硬件成本 | ~$50 | ~$50 | ~$10 |

## 🤖 技术架构

## ![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUgT6XfSvf1w1w4bia9iba2WuV4wgqGlqNBBfkXrFric4S4AxOoGL9qle5R5iamyO5vh2UxJV4icfQn0CSatk3yHhgyWPjvyyTXXCl9g/640?wx_fmt=png&from=appmsg)

PicoClaw 是一个受 nanobot 启发的超轻量级个人 AI 助手。它采用 Go 语言 从零重构，95% 核心代码由 AI Agent 生成，经历了一个"自举"过程——即由 AI Agent 自身驱动了整个架构迁移和代码优化。

🎯 应用场景

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUiag8tAofEia8icMIBqW6VYyft8cBy0e1Mqqhw0wl44HZ5aiazkrFRe6ia8cB9OOicqpGXxWY237eNSHTpic2vVGPzqB9q9yR3BBiaaIFE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/0VE9kDxicLUiauZ3Wic7nGPrpib8g26hV3JsaKj83Fic8kGwqONAjriaup1KcwQhH56lO3catv6rN8uuEHickUs1gCWIeQYopCGuFicibDE1iatTRGFCc/640?wx_fmt=png&from=appmsg)

* 💻 代码助手：本地代码补全、调试和文档生成。保护代码隐私的同时获得 AI 助力。
* ✍️ 内容创作：用 AI 撰写博客、邮件和文档。所有草稿和想法都保留在你的设备上。
* 📊 数据分析：在本地分析敏感业务数据。数据不离开你的基础设施，确保完全保密。
* 📅 个人助手：通过定时命令、cron 自动化和多平台机器人集成管理日常任务
* 📚 研究与学习：总结论文、回答问题、组织知识库。内置网络搜索和长期记忆，保持上下文连续性。
* 🔌 API 与集成：网关模式将 PicoClaw 变成 AI 后端。通过 MCP 协议和 REST API 连接任何聊天平台。

🌳 写在最后

PicoClaw 的愿景是打造终极轻量、安全、完全自主的 AI Agent 基础设施。让平凡的事情自动化，释放你的创造力。

PicoClaw 项目源码：https://github.com/sipeed/picoclaw

---

点个关注 🌟，精彩不迷路 ❤️

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

**免责声明：**本公众号所发布的内容来源于互联网，我们会尊重并维护原作者的权益。由于信息来源众多，若文章内容出现版权问题，或文中使用的图片、资料、下载链接等，如涉及侵权，请告知我们，我们将尽快处理。

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