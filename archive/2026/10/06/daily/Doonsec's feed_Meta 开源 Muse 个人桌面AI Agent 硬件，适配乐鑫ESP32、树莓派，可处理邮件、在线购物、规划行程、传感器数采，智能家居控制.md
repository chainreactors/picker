---
title: Meta 开源 Muse 个人桌面AI Agent 硬件，适配乐鑫ESP32、树莓派，可处理邮件、在线购物、规划行程、传感器数采，智能家居控制
url: https://mp.weixin.qq.com/s/I7h6PCugIAsPT_PHI_FfNQ
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:51:43.480100
---

# Meta 开源 Muse 个人桌面AI Agent 硬件，适配乐鑫ESP32、树莓派，可处理邮件、在线购物、规划行程、传感器数采，智能家居控制

# Meta 开源 Muse 个人桌面AI Agent 硬件，适配乐鑫ESP32、树莓派，可处理邮件、在线购物、规划行程、传感器数采，智能家居控制

原创

~
~

IoT物联网技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUjAXvV9ltwLG0n2smxVa9dEumVYKwuaSoR2e8OGqEj7vAe3GiaHpKyrjIlPrXWd3h2c874kwU4r3DEFQTwhTYxZumYWIUyIVRfM/640?wx_fmt=png&from=appmsg)

> 处理邮件、在线购物、规划行程、智能家居联动

Muse是Meta公司于2026年9月推出的**个人桌面AI Agent智能体**，定位为能替用户执行日常任务的**多功能助手，**具备独立操作能力，可连接邮箱、日历、购物等第三方服务，完成处理邮件、在线购物、规划行程等任务，甚至在后台持续完成一些复杂操作。

Muse Gadgets 是Meta开源的**AI硬件开发套件**，包含乐鑫ESP32固件和Linux SDK，允许开发者用几十元的乐鑫ESP32开发板为AI助手 Muse 制作物理外设，支持连接显示屏、传感器等设备，可实现智能家居控制、日程提醒等功能。

Meta 还提供了官方设备 Muse Home Link，并开放了Discord社区供开发者交流。该项目降低了AI硬件门槛，用户可用闲置树莓派快速上手。

* 极致低功耗：乐鑫ESP32微控制器固件， ESP32是全球电子创客圈最廉价、最普及的微型芯片，单颗售价只要15到25元人民币。Meta官方开源的代码包直接接管了ESP32的I2S音频流传输与低功耗蓝牙配对。你只需将这块芯片连上一颗硅麦克风、一个几块钱的扬声器和一个轻触按键，接上家用Type-C电源或锂电池。按键按下，拾音上传；AI语音流式返回，芯片当场解码播放。
* 高阶交互：树莓派Linux Device SDK，如果你有一块吃灰的树莓派或微型工控板，SDK提供了完整的后台守护进程。你可以外挂一块几十元的电子墨水屏（E-ink Display）。清晨醒来，桌上的墨水屏已经静静显示着AI为你整理的每日日程、核心行业动态与天气；你路过书桌随口问一句，房间里的音箱当场温和回应。

设备刷入固件后，通过手机端进入开发者模式扫码即可完成Token配对绑定。设备端只负责传递传感器数据与音频包，绝不存储敏感凭据，彻底打消了用户对物理设备隐私泄露的顾虑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUgE5oVMwjbh6CvCsDVnIxdG3Vm4SJkbUAyTzUq8ad2bIwc3Iq1WWiapsLQ1RBFMhahOxLuYpgOGOJJ33BPdVBQDvouxPsjniauLc/640?wx_fmt=png&from=appmsg)

你可以使用乐鑫 ESP32 开发板运行 Muse 固件，或使用 Linux SDK 连接更复杂的设备，也就是说开发者不仅能够在低成本微控制器上部署 Muse 交互逻辑，还能直接在树莓派 5等更强大的边缘计算设备上运行 Muse 客户端。

* 彩色电子墨水屏：作为桌面的低功耗提醒器或智能看板，实时展示 Muse 同步的日程与待办事项。
* HDMI 显示棒 / 大屏扩展：将 Muse Agent 的界面或互动直接投射至电视或外部监视器上。
* 触控掌上挂件：自制类似于 Muse Charm 的随身交互终端，无需佩戴智能眼镜即可随时与 Agent 对话。

**Muse Gadgets 开发过程**

作为硬件极客，你可以基于开源 Muse Gadgets 项目打造专属于自己的 Muse 外设，步骤如下：

硬件开发板：采购免焊接的ESP32主板与墨水屏模块，单个硬件BOM成本在80元左右

3D外壳：用家用拓竹3D打印机制作一套复古打字机风、像素复古风或者极简包豪斯风的外壳，赋予它极致的工业美感；

获取凭证：访问 gadgets.muse.ai 注册并领取个人的 API Token；

连接开发工具：将 GitHub 官方代码库导入你常用的 AI 编程代理程序，如 Claude Code、Cursor、GitHub Copilot CLI 等，借助 Agentic Coding 能力快速理解协议并生成外设驱动代码；

固件刷写与调试：将代码刷入 ESP32 开发板或在 Linux / 树莓派设备上运行 SDK 客户端，即可完成硬件终端与 Muse 的实时双向连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0VE9kDxicLUh2ntJnSdY4icCLEI5U0JBu5c0ZHcaXeEriarMWACFvlgkoLjzKZv1osjYCrPpHw7TJ5s0vbFqT5l6cWRFib8j45Ey7e4DL8iamjIw/640?wx_fmt=png&from=appmsg)

Github开源项目地址: facebookincubator/muse-gadget-sdk

如果你也对开源AI录音卡感兴趣的话，可加 beacon0418

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