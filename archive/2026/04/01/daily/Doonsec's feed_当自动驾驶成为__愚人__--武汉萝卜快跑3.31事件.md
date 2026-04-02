---
title: 当自动驾驶成为\"愚人\"--武汉萝卜快跑3.31事件
url: https://mp.weixin.qq.com/s/vh2qQJQpDegGFWg026Bx9Q
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:23:34.986030
---

# 当自动驾驶成为\"愚人\"--武汉萝卜快跑3.31事件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Njo9XALrRFRYeVxFdRfUJicxqUMtGMHQImxhA0P96YlL0k4vdcyw9mbudBYIVcR4baZ99KSqChjF0bmjm9HAluC1SEiaw3YxurtiaeHTWFIhnc/0?wx_fmt=jpeg)

# 当自动驾驶成为"愚人"--武汉萝卜快跑3.31事件

原创

zh1chu
zh1chu

安全脉脉

![]()

在小说阅读器中沉浸阅读

**免责声明：本文基于公开信息从技术角度分析，具体故障原因以官方最终调查结论为准。**

**昨天晚上，如果你行驶在武汉二环线、三环线或白沙洲大桥上，你可能会遇到这样一幕：数十台萝卜快跑自动驾驶车辆突然如被按下"暂停键"，齐刷刷停在主干道甚至高架快车道上**

**![](https://mmbiz.qpic.cn/mmbiz_jpg/dAYfDaj0k4LUxI1U0J6ZicfKv1ox1JAaQMuCCTjQJ5tqAhUdp9d3iaORYcibI9T1bhrlSYSBnIfPTyqtktQORC5YhVVfsRibdnNVBtevXygyhqI/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=0)据武汉交警官方通报，3月31日晚从20:57开始，122报警中心密集接到报警，约80-100台萝卜快跑车辆同时失去动力，造成"猪肝红"级别拥堵，部分车辆甚至引发追尾事故。有乘客被困高架近两小时，车内SOS紧急按钮一度失效**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Njo9XALrRFQLzU4yQNpX5g6vx2NCOlKqFuGA5AGfAw45aoDETtNSicHZrQSiaDRc8NUPliaPXdKzh69MfN9nqbG8zib6iaAfzFHM3lKzbdZDK4S0/640?wx_fmt=png&from=appmsg)

根据官方通报和乘客反馈，故障呈现出典型的**集中式系统故障**特征：

* **时间同步性**：近百台车在同一时段（20:57后）集体瘫痪
* **症状一致性**：屏幕均显示"驾驶系统异常，工作人员预计5分钟赶来"
* **客服响应**：官方客服称系"网络故障"
* **恢复方式**：需企业工作人员到场处置，交警只能疏导，无法恢复车辆

具体故障原因很多种可能，以官方最终调查结论为准。谈一谈此次武汉萝卜快跑3.31给行业的三点警示：

### 架构脆弱性：当自动驾驶系统采用"重云端、轻车端"架构时，云端服务器、OTA平台或核心网络服务成为致命的单点故障源

### 失效模式设计缺陷：自动驾驶系统被设计为"安全第一"，但这次故障却是"危险地停止"。在2025年12月，谷歌Waymo在旧金山也因停电触发"最小风险策略"原地停滞，但区别在于Waymo车辆能够安全停靠路侧，而非直接锁死在行车道。

### 紧急通信链路的可靠性：有被困用户反映，车顶SOS按钮"根本打不通"，400客服电话多次被自动挂断，被困近两小时后才在交警协助下脱困

###

### 萝卜快跑在武汉的这次故障，不是自动驾驶技术的"死刑宣判"，而是真实场景下问题的暴漏。真正的无人驾驶安全，不是"不撞车"那么简单，而是**在任何极端情况下，都能保护车内和车外人员的生命安全**。

###

##

## 作为车辆网络安全从业者，我们乐见且拥抱技术进步，但更要坚守安全底线。此次事件揭示了一个被行业长期忽视的真相：**我们过去十年的车辆网络安全，主要关注"静态网络安全"，而自动驾驶时代，我们必须转向"动态网络安全"**。

## 范式转移：从"静态网络安全"到"动态网络安全"

### 什么是"静态网络安全"？

传统车辆网络安全（2015-2023）主要关注：

* **固件分析**：逆向T-Box、IVI系统的二进制漏洞
* **通信测试**：实验室环境下CAN总线重放攻击、UDS诊断会话绕过

**特点**：车辆在车库/实验室中，攻击目标是**信息泄露**或**非授权启动**/控制。

### 什么是"动态网络安全"？

自动驾驶时代（2024-），安全场景变为：

* **动态传感器欺骗**：车辆在行驶中，攻击者伪造传感器数据诱导错误决策
* **动态通信中断**：车辆在变道/超车时，V2X信号被干扰导致决策真空
* **动态系统降级**：车辆在高速巡航时，云端失联触发"失效模式"

**特点**：车辆以60-120km/h运动，攻击目标是**行为操控**或**功能降级**，后果是**物理伤害**。

### 典型案例：TPMS伪造攻击的静态vs动态差异

**传统车辆**：

* 仪表盘显示"胎压异常"警告灯
* **后果**：信息误导，但**决策权在人类**，风险可控

**自动驾驶车辆（动态安全时代）**：

* 干扰自动驾驶决策链，安全机制触发

* **后果**：车辆直接停摆，可能造成追尾或多车拥堵（如萝卜快跑事件）

同一个TPMS漏洞，在传统车只是**信息层欺骗**，在自动驾驶车却成为**控制层攻击**，触发**系统层失效**。当车辆成为"移动的智能体"，网络安全不再是关于"数据泄露"或"车辆被盗"的静态问题，而是关于**"行驶中的100辆车如何瞬间变成路障"**的动态危机。

![](https://mmbiz.qpic.cn/mmbiz_png/DqSCFmLSbr6RuAGyRSnhm0oM5XX7USzxLMicaWxXTRNiaDkM56mAsvmGtVrGPezib6THEHbLCOYGmE91Gq31DhZHA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DqSCFmLSbr6BNJLhxKxx8tFdhG7aOicY7psSXrh79te4WoicUFNMfbDD8FzbBwvD0vPAf8GtyAEWUzzfAViaBn3Sw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DqSCFmLSbr6BNJLhxKxx8tFdhG7aOicY7z5mGSibUdypiaVCtUoib9UFgJsyQKj0P6EBqKCDe3WiaXo8ng8e1iaWkvZw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/DqSCFmLSbr5iatNMIL2icB5KhjCFcxmUqzMJK1SHV0Sxe2IlwsTgAEpgUncQeQGOs96pibJMA77H2xmbNELphUaibg/0?wx_fmt=png)

安全脉脉

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/DqSCFmLSbr5iatNMIL2icB5KhjCFcxmUqzMJK1SHV0Sxe2IlwsTgAEpgUncQeQGOs96pibJMA77H2xmbNELphUaibg/0?wx_fmt=png)

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