---
title: 一个 AI  Agent + 蓝牙适配器,30 秒看穿你的蓝牙设备安全底裤
url: https://mp.weixin.qq.com/s/MS1TVRnTfcC1Nl8cZ1ORTQ
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:29:17.997743
---

# 一个 AI  Agent + 蓝牙适配器,30 秒看穿你的蓝牙设备安全底裤

# 一个 AI Agent + 蓝牙适配器,30 秒看穿你的蓝牙设备安全底裤

原创

信睿网络
信睿网络

信睿网络

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

智能灯泡、智能锁、手环、血压计、工业传感器……今天几乎每一个 IoT 设备都带着一颗 BLE(低功耗蓝牙) 芯片。

但很少有人知道:相当一部分蓝牙设备的控制指令,是在空气里"明文裸奔"的。

不加密、不配对、不校验 —— 这意味着:

* 被动嗅探:范围内任何人都能把你发给设备的指令原样录下来;
* 重放攻击:录下来的指令,换个设备原样发回去,设备照单全收;
* 指令注入:伪造、篡改指令,远程控制你的设备。

![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/ib6htUiaCMJ10BYPiaqZKoecfZRLrDPdMEChTsGSPqAX6MEbxsLvzMx1j3ea0nP5D4ZIQw8v3DTlQecWpfLJOEVuHxY1LVRRtfSrprTXBibhIVE/640?wx_fmt=jpeg&from=appmsg)

这不是理论。下面是我们近期一次授权测试的真实结果。

**一款市售智能灯泡,是怎么被"拿下"的**

我们用自研的 AI 驱动 BLE 安全测试 Agent,对一款常见的智能灯泡做了一次完整体检。全程自然语言驱动,从抓包到出结论,不到几分钟:

**第一步 · 被动抓包**

用 nRF52840 嗅探棒锁定目标设备,被动捕获它与 App 的完整蓝牙会话 —— 全程不主动连接、不干扰设备。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/ib6htUiaCMJ10vCLz2aiaSTYTibKBX4OP9N1wibJdRNV4USozySCh9ayNiaOibEyrSnE5dx57u2CqoiakibXbLFoGibssvtxtP9yia7auyLrGcRypu58z0/640?wx_fmt=png&from=appmsg)

**第二步 · 协议还原 + AI 分析**

Agent 自动还原出 GATT 服务结构、每一条读写指令、状态反馈通道,并给出结构化的安全判断:

🔴 链路全程未加密、未配对 —— 任何范围内的监听者都能读到控制指令
🔴 控制指令可被重放 —— 没有计数器 / nonce 防重放机制
🟠 接受任意陌生设备的写入 —— 不需要任何身份认证

![](https://mmecoa.qpic.cn/sz_mmecoa_png/ib6htUiaCMJ12OKsI6g6xXG1flhqR06maXVjatMkibqqEiaAYfRNsg7BwgziaRfcY8ZLzSSA9ucQR5SmqJ91omL09oVia7ue5ia1zkSORMS2pmkTOA/640?wx_fmt=png&from=appmsg)

**第三步 · 主动验证(授权范围内)**

我们用另一台全新的、从未配对过的蓝牙设备,把嗅探到的控制指令原样重放 —— 灯泡接受了。随后的协议级模糊测试(Fuzzing)灌入 17 组畸形指令,设备全盘接收了其中 11 组。

![](https://mmecoa.qpic.cn/mmecoa_png/ib6htUiaCMJ12xQWq4FfCeFibe5J50qbwqhS4GutdlO5Nqx8zheicJqr7zEaobOUyM2fDgvWWYrS61r5MrotExGk7WcoYB2zRibWPnK6heLN5FsM/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/sz_mmecoa_png/ib6htUiaCMJ13AjuDXWs6aqIsJw0JtO1W8iahPAQJWibz2ibNLiagD5WNBtBz6l0I5PXcp1O5ibJOIUaWn8PiaWHRZXDnvj5AKFmwXQauo1WRnR6XYQ/640?wx_fmt=png&from=appmsg)

这个灯泡抗崩溃,但完全不抗未授权控制 —— 范围内任何人都能控制它。

**为什么现在,这件事变得紧迫:因为CRA 来了**

欧盟《网络弹性法案》(Cyber Resilience Act, CRA)已经落地。它对带数字元素的产品(几乎涵盖所有联网 IoT 设备)提出了强制性网络安全要求:

* 出厂默认安全配置、无已知可利用漏洞;
* 对未授权访问的保护(认证、加密)、数据保密性与完整性;
* 漏洞处理流程与安全更新机制;
* 不满足要求的产品,将无法进入欧盟市场,违规面临高额罚款。

早发现,早修复,早拿证。 等到客户投诉、监管通报、召回下架,成本是今天的几十倍。

**我们能为你做什么？**

【信睿网络】专注 物联网安全测试 与 CRA 认证咨询,把"安全体检"和"合规拿证"打通成一条链:

①**IoT 安全测试(渗透级深度)**

* BLE / 蓝牙、Wi-Fi、Zigbee、固件、App、云端接口的全栈安全评估
* AI 驱动的自动化分析 + 资深工程师人工深挖,兼顾效率与深度
* 每一项发现都附可复现证据链与修复建议

② **CRA 合规咨询**

* CRA / EN      18031 等标准的差距分析(Gap Analysis)
* 安全需求梳理、架构评审、漏洞处理与 SBOM 流程搭建
* 陪跑式辅导,直到顺利拿证、顺利出海

③ **一份让研发看得懂、让管理层看得清的报告**

* 风险分级、攻击路径、证据、修复优先级,一份报告讲清楚

\* 所有测试均在客户授权范围内进行,严格遵守保密协议;测试数据与样机按约定处理。

【信睿网络】 · 让每一个联网产品,出厂即安全。

![](https://mmecoa.qpic.cn/mmecoa_png/ib6htUiaCMJ10c64W311MkxIqCz2Qz61u7MbAfzyBLb0hjHCXZYWNoicKHNialmUEGBfm7GIJ8ibVZMeQZfvWbliaricV61iaW2cG7NrXROrJrAhibNY/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmecoa.qpic.cn/mmecoa_png/RbvWEoCT2fQ3rgFwwI3v4uSxpI0pfAibEQRd2w5wrNMz20skmtk4EeVQFtuANBWSM55Q3XpfDYfDiaraKwQwVIOA/0?wx_fmt=png)

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