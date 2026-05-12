---
title: [MCP]自动化逆向/黑客技能-硬件与步骤—终极指南
url: https://mp.weixin.qq.com/s/Ops8j9EL7VDdLN8HMUC3Cw
source: Doonsec's feed
date: 2026-05-11
fetch_date: 2026-05-12T05:33:36.291113
---

# [MCP]自动化逆向/黑客技能-硬件与步骤—终极指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icfnkibn16VegQOlIRehVlUk8svDkS0MOUkziar3SdUt1WBdMv47BcrmNkDOj41muL8Ohty9v9dfOSDiccZPgtDSD53CmrqV5FoUNOSP5Gib5tnI/0?wx_fmt=jpeg)

# [MCP]自动化逆向/黑客技能-硬件与步骤—终极指南

原创

bl0ckdev
bl0ckdev

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

强制硬件要求;你的显卡必须是可以运行8b最小模型,这里的定义8不是最小的,所以务必遵循硬件要求的逻辑。原因在于：我用4Gb显存和16G内存跑适合4gb模型，室温23°,显卡温度保持在90°,持续72高频训练后显卡报废！

> 如硬件要求不够,那就只能选择在线模型Api。但是研究深度的封号特别严重,我们需要通过各种手段对在线的适配角色。让Ai毫无保留地回答我们的问题。

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16Vej5IOGQorNSp8iboFuEziavQ2AGsibxUwEay7KZiaXoO7BpDSTdjogWUDwHicUiaWjoroyMMfrsk8c3Tps2LWyRhHQw5Ij0Ert2TLReY/640?wx_fmt=png&from=appmsg)

Mac book

* Apple M系列最低16G以上  （除非你使用最低的模型,自己微调。）

Windows/Linux：

* GeForce RTX 3060
* GeForce RTX 5060

Windows/Linux：AMD系列  (AMD我没有进行测试,选择前问清楚是否支持8b)

```
https://docs.ollama.ac.cn/gpu#gpu-selection
```

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VejRWfic4pxic2ticibDjPiaa838zloyxIicyBqq51pV4lgtXtokBia3q3IJSnHHwrfI2oibfibEibRazdFosPPyRoFTL2XxRRricxEeAefZZM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VehnNNvxpcO1AhNezMC52cEZUcuHPiaAgibT9B1icEOOVm3jl0yqFQlvHLszYg3evzpufmiaCwCeJzKyYgYGAXXIyXMrb6y1o3bJJZo/640?wx_fmt=png&from=appmsg)

自动化逆向的基础逻辑（一次深度配置/后边就是修改）

* 选择适配自己显卡的本地模型!
* MCP、Ollama 和 OpenWebUI !
* 根据你的硬件和系统进行逻辑诊断并且安装Pyhton!
* 安装Ollama并运行本地模型\*-\*( 这个简单,难度在于选择模型)!
* 配置OpenWebUI 以管理提示符\*-\* （在容器中完成启动并且基础了解）!
* 将 第一个MCP 与 python及本地大型语言模型集成！
* 完整的运行一次“打通”安装软件的流程！

---

特别提醒：

{darkesn-并不是让你“学”,而是直接用。}

* 熟悉Ghidra/IDA
* 基础漏洞研究知识（利用逻辑/漏洞类型/分析流程）
* Pyhotn的基础认知（安装/调试/执行脚本）的熟悉度
* 在工作流程中使用最新LLM功能，或至少利用AI改进日常任务的经验

目的在于学习如何将传统技能与私有大型语言模型堆栈和自定义模型上下文协议服务器结合。我们将拥有由人工智能驱动的工作流程，加速理解，发现弱点，简化分析。并构建出可重复的代理AI工作流程，能够分析软件、发现潜在漏洞。

点击阅读原文：扩展笔记星球（从0到9的全细节文图处理）！

零零散散的需要你接触的是：

* Git
* linux
* open claw
* Hermes Agent
* LLM
* Claude
* Antigravity

目前就整理了这些模糊的,对我而言MCP就像一个新游戏,在MCP和vim之间做选择,我宁愿深度学习mcp,因为我对mcp感兴趣！

  大家可以在各种可以搜索到的地方进行搜索免费资料和视频进行学习。我个人会把我的笔记储存在新的“星球笔记”中。添加的会直接 授权 H6000\*标签！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VeiaUnEACXX5ZrvbAmoDvwWDPQSBJoY8n1G6mwLlyzbeX8PdYeK4NO03meiaNfNcLJYnhHuKUgtxvoZxkfWJ5Z3s5gGhPNDFpeNuo/640?wx_fmt=png&from=appmsg)

前一个月推荐 邀请添加！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Veh2W9WymHGlD1vWESe9maZHk9fmzJFg05InEc28wIS4FwibbjsjlibtKgUictqn3DU6xXqSDomFK0vpLEE1s3l2v0aaCOSMEaaU3s/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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