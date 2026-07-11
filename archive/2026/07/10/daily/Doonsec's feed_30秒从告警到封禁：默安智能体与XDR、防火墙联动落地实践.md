---
title: 30秒从告警到封禁：默安智能体与XDR、防火墙联动落地实践
url: https://mp.weixin.qq.com/s/UVIoB9uBal-9KdPzJx-orA
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:59:23.814285
---

# 30秒从告警到封禁：默安智能体与XDR、防火墙联动落地实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pYZtDTxxdaGl3yckaBwjdOIV4zVP6C9ciaSGhGJ7d0ojWcMicTk1qb7KeHAarZSYmUjD9cyRED0icKd0rPD1Wh8wrdCEGtqRrfE1YZhLMre7g/0?wx_fmt=jpeg)

# 30秒从告警到封禁：默安智能体与XDR、防火墙联动落地实践

Cismag
Cismag

信息安全与通信保密杂志社

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

日均**2000+**次攻击流，**30秒内**完成从发现到多防火墙联动封禁——这不是概念验证，是默安科技**安全运营智能体**在**能源行业**的真实落地结果。

## **行业现实：买得越多，防得越慢**

政企网络安全建设持续加码，防火墙、NDR、EDR等安全设备越堆越多，但运营效率并未同步提升。面对日均数千次的攻击流量，传统人工研判与处置模式的瓶颈愈发明显：

• **研判慢**：告警触发后，安全工程师需逐一分析攻击特征、评估影响范围、确认是否误报，单次研判耗时数十分钟至数小时

• **联动难**：异构防火墙品牌各异，策略下发需分别登录不同管理平台操作，跨设备协同靠人工逐条执行

• **响应滞后**：从告警产生到完成封禁，中间横跨多个环节与平台，实际响应时间远超"分钟级"要求

**安全团队深陷"看得见、拦不住"的困境。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ldFaBNSkvHiaicd0rtJna1sSaSwSZBLNQ3vtV02I9GF04Pt7zEMnSjaAOmuYiaFNhRJOnYdLkIG1cNciaiceicFJCYfQ/640?tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=1)

## **落地场景：**

## ****默安********智能体********与********XDR联动多防火墙自动化封禁****

针对上述痛点，默安科技以安全运营智能体为核心，联合XDR平台构建了从威胁感知到自动封禁的全流程智能化运营体系，已在能源单位的真实业务环境中完成落地验证。

**第一层：威胁感知——多源数据实时采集**

XDR平台实时采集攻击流数据、终端行为日志及全流量镜像等，构建全网威胁感知底座。多源数据统一汇聚，消除单点设备的感知盲区。

**第二层：智能检测——AI大模型立体纵深研判**

在XDR告警引擎完成初步特征分析与风险评分的基础上，默安智能体介入，进行立体纵深分析：

• **告警分析**：对告警内容进行深度语义理解，而非简单规则匹配

• **资产关联分析**：评估被攻击资产的业务重要性及漏洞暴露面，判断攻击实际威胁等级

• **攻击链还原**：基于ATT&CK框架映射，判断攻击当前所处阶段，预判后续可能动作

**综合研判后，****智能体输出高/中/低风险等级评定，****为后续处置决策提供依据。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ldFaBNSkvHiaicd0rtJna1sSaSwSZBLNQ3vtV02I9GF04Pt7zEMnSjaAOmuYiaFNhRJOnYdLkIG1cNciaiceicFJCYfQ/640?tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=2)

**第三层：决策分析——自然语言交互辅助决策**

安全运营人员可通过自然语言向默安智能体发起查询，例如："分析IP 192.168.x.x的攻击意图"、"评估封禁该IP对业务的影响"。

智能体基于全量上下文信息生成封禁策略建议，包含：

• 封禁范围：单IP/网段/地域

• 封禁时长：1小时/24小时/永久

• 影响评估：关联业务系统及误报风险

**处置策略遵循分级机制：高风险事件自动处置，中低风险事件需人工确认，在效率与安全之间取得平衡。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ldFaBNSkvHiaicd0rtJna1sSaSwSZBLNQ3vtV02I9GF04Pt7zEMnSjaAOmuYiaFNhRJOnYdLkIG1cNciaiceicFJCYfQ/640?tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

**第四层：自动化执行——跨品牌防火墙联动封禁**

发现威胁后，默安智能体通过MCP协议向XDR下发封禁指令，XDR作为统一编排中枢，通过API向异构防火墙同步下发策略：

• 防火墙A：阻断恶意IP南北向访问

• **防火墙B**：联动封锁攻击源IP，联动IPS策略

• **防火墙C**：ACL策略自动下发，阻断异常流量

• **防火墙D**：IP黑名单同步，边界防护加固

**四家不同品牌的异构防火墙，一套指令同步生效，无需人工逐一操作。**

![图片](https://mmbiz.qpic.cn/mmbiz_png/ldFaBNSkvHiaicd0rtJna1sSaSwSZBLNQ3vtV02I9GF04Pt7zEMnSjaAOmuYiaFNhRJOnYdLkIG1cNciaiceicFJCYfQ/640?tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=4)

## **落地效果显著**

经过此次实践检验，默安科技安全运营智能体在该能源单位的真实落地数据如下：

![图片](https://mmbiz.qpic.cn/mmbiz_png/Gianlj61NfoyBWjzYN8CF29OjneUOSMOM9uia6Zy5rcXN32DlFOph4MSboaw4nSSV4sLJglSo2HzZ1bWJdn6Crj0AmvF9t0na7U1ogvvwZeSs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=5)

## **结语**

30秒封禁、90%自动化处置、4家异构防火墙联动——这些数字不是演示环境跑出来的，是在能源单位真实业务网络里的落地结果。

默安安全运营智能体要做的，从来不是在控制台里多放一个对话框。它的定位从发布第一天就没变过：**是来干活的，不是来聊天的。**

**默安科技安全运营智能体：******已在********真实环境中完成落地验证****。

**来源：默安科技**

**★**

**★ ★ ★**

**★**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iclynibMMTgBwgCg9mGbuByfRqykUw7pNibhqs5FTfibiagTERwjA5aIr1nWU877gknbu4l0icwleVpLxzotXXbK3thA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iclynibMMTgBwhRphiasJXbLerI7qNNnpia0ibWnpkzdSTrWuZwf32kY8m9Qu17zSDTJSmvib7TNVWcIQu4M9QsFbBdA/0?wx_fmt=png)

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