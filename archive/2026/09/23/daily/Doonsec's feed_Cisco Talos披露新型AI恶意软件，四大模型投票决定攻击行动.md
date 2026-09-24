---
title: Cisco Talos披露新型AI恶意软件，四大模型投票决定攻击行动
url: https://mp.weixin.qq.com/s/lV_XXsmwMeadk7Xw6GBsKw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T06:59:19.123938
---

# Cisco Talos披露新型AI恶意软件，四大模型投票决定攻击行动

# Cisco Talos披露新型AI恶意软件，四大模型投票决定攻击行动

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX33KcLZ0vicPJSUFibd7qIxGhPVia0Kqa4PCI5BqpBOuJmtBmSwaExHMnFJJlFfiaBDPP2n04X5ZvgibNqV6lCfBCCym1MwX3FzKnibs/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX05ksgvibaStmbsS7c4HibKvMbDdJ9C0L4VIOIlDibtwz2nB2eq52icVVBDib5z7tEEb4VV2XyULcGdSMKFia8HXFA9PIDXLYXibm7iaibE/640?wx_fmt=png&from=appmsg)

思科公司Talos威胁情报团队今日发布一款开源工具包，专门用于狩猎内置人工智能功能的恶意软件。

Part01

四模型投票决策战术行动

该团队详细披露的首个样本是一款Windows凭据窃取程序，完全不依赖命令与控制（C2）服务器接收指令。Talos将其命名为CLOSEDQUORUM，该恶意软件的所有战术决策都交由四个商用大语言模型投票决定。研究人员指出，目前公开记录中，还没有其他Windows恶意软件会将战术决策交由一组模型投票决定。

这四个模型分别是Google Gemini、DeepSeek、Qwen和Mistral，CLOSEDQUORUM每隔5到15分钟就会按顺序向四个模型发起查询。该恶意软件是一个大小为16.4MB的Go语言二进制文件，会向每个模型提交当前主机的状态信息，附带的系统提示词将模型定义为“高级恶意软件策略师”，要求模型仅返回可直接执行的决策。获得票数最高的决策将被执行，若出现平票，由DeepSeek投出决定票。最终选定的决策会被下发到四个功能模块之一执行，四个模块分别对应凭据窃取、代码注入、持久化驻留、横向移动四类功能。

Talos研究员Ryan Fetterman在博客中写道：“整个运行过程完全闭环，无需人工介入。程序会按顺序查询四个模型，统计各自独立给出的决策结果，再根据模型的判断执行对应操作。”

窃取模块会同时执行三类收集操作：从进程内存中提取Windows凭据，从Chrome、Edge、Firefox浏览器中读取保存的密码，从MetaMask、Exodus及以太坊密钥存储路径中获取钱包文件。窃得的数据会经过加密，通过Discord webhook向外传输。该恶意软件通过注册表运行键、计划任务、Windows管理规范（WMI）订阅实现持久化驻留，同时会屏蔽Windows事件跟踪功能，避免留下操作痕迹。

目前还没有证据显示攻击者已将CLOSEDQUORUM用于实际攻击。Talos共获取到6个样本，覆盖了开发者约一周的构建流程链，样本内的痕迹显示，该开发者与犯罪论坛上的账号有关联，相关账号从2025年开始发布信用卡盗刷相关内容。研究人员评估，这是一套凭据即服务的运作模式：开发者负责定制恶意软件二进制文件，买家负责投放传播。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2UnlibQDfXNVUQBtjV2RPUMmbYy6sR5FwxaqDMDZwvqL6ZkUZMg51lRMWodiaCa3LFufcibqLj7xWXxFpDYricAPibUAmpia6Mgib0ew/640?wx_fmt=png&from=appmsg)

Part02

CAIRN开源检测工具发布

Talos已将发现该恶意软件的工具包Cognitive Artifact Intelligence Research Network（简称CAIRN）上传至GitHub。CAIRN基于元数据开展检测，无需下载样本或在沙箱中运行。工具内置24个采集过滤器，专门识别恶意软件集成AI功能留下的痕迹，包括调用商用模型服务商的请求、Python框架导入记录、本地模型运行时特征，以及攻击者植入的、用于干扰自动化分析系统的自然语言文本。工具通过YARA规则将检测命中结果分为三个等级，最低等级仅识别到AI组件存在，最高等级可匹配到已命名的恶意软件家族；同时内置的嵌入模型还能对无任何共同字符串的样本进行聚类归组。

Part03

AI恶意软件演化速度加快

这些过滤器自2025年7月起就对收集到的样本持续运行检测。狩猎工作启动初期，大语言模型还只是攻击者附加在payload上的可选功能。仅一年时间，模型就已经开始主导payload的运行逻辑，CLOSEDQUORUM正是这一演化路径的最前沿产物。

这类规避技术的传播速度极快。Talos溯源发现，相关技术最早来自一名红队讲师，仅12个月内，独立攻击者的恶意样本就已经开始搭载该技术，过程中逐步从零散脚本演化为编译型恶意软件。

Fetterman将这种转变定义为攻击成本的转移：如今攻击链中越来越多的环节无需操作人员介入即可自动运行。他写道，人类攻击者受限于“注意力、工作时长和认知负荷”，而模型决策组可以每隔5到15分钟输出一次决策，无限期持续运行。他评估认为，在这类AI驱动的攻击模式普及之前，防御方仍有充足的窗口期研究这一转变趋势。

参考来源：

Cisco Talos finds malware that puts its next move to a four-model vote

https://siliconangle.com/2026/09/22/cisco-talos-finds-malware-that-puts-its-next-move-to-a-four-model-vote/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0XsTyO4SuMuGUvEh6HBoZLXPa9xnn1UsveAZRjUSfAKwT77dFfrwAPbRgSe6l66sYOBiaFSfWMn3DL4IfDrDmexoxCYLftaleo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651346509&idx=1&sn=71e02ef8b6a2ed67fdc94aa19b152171&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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