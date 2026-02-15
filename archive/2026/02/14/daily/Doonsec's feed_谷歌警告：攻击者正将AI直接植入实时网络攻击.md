---
title: 谷歌警告：攻击者正将AI直接植入实时网络攻击
url: https://mp.weixin.qq.com/s/ElngW95AqaaxytQ4qoPlqg
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:17:16.856781
---

# 谷歌警告：攻击者正将AI直接植入实时网络攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2c5Mxe7d3akCNWsJApr9icD8oMCBmeKiauutI7iaXuMtAIQXcO61S16C03w9ibXTukzc93wYLsKqQXy2b0ciaQtgwiccnyRnl8JHnKI/0?wx_fmt=jpeg)

# 谷歌警告：攻击者正将AI直接植入实时网络攻击

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2kfVIqbktZRQcPez4PxdbeQvicqxxUuHCh7v5IugTJS5fXuH5qVHLtsl6ktwYKwIGy0RAicaKFQLYOqibbmgMb0oOvsmqXbkkBvw/640?wx_fmt=png&from=appmsg)

谷歌威胁情报小组今日发布的最新报告警示，威胁行为者已不再局限于对人工智能的简单试验，而是开始将AI直接整合到实际攻击工作流程中。

该报告部分聚焦于对谷歌自家Gemini模型的滥用与针对性攻击，凸显出生成式AI系统正日益成为恶意工具的测试、探测对象，甚至在某些案例中被直接纳入攻击体系。

**Part01**

## ****Gemini模型遭恶意代码直接调用****

研究人员发现部分恶意软件家族在执行过程中会直接向Gemini发起API调用。值得注意的是，这些变种会动态请求模型生成源代码来执行特定任务，而非将所有恶意功能硬编码在程序内部。

例如，被标识为HONESTCUE的恶意软件家族通过提示词获取C#代码，并将其作为攻击链环节执行。这种技术使攻击者能将逻辑转移到静态恶意二进制文件之外，可能使依赖特征码或预定义行为指标的传统检测方法失效。

**Part02**

## ****模型提取攻击持续涌现****

报告还记录了正在进行中的模型提取攻击（亦称蒸馏攻击）。威胁行为者通过向模型发送大量结构化查询，试图推断其行为模式、响应规律及内部逻辑。这种攻击的本质在于通过系统分析输出结果，攻击者可在不承担从头开发成本的情况下，近似复现专有模型能力并训练替代系统。谷歌表示已识别并阻断多起针对Gemini模型知识的高频提示词提取活动。

**Part03**

## ****AI渗透网络攻击全生命周期****

其他发现包括：国家背景组织和金融动机团体正在将AI工具整合进网络作战的既定阶段，涵盖侦察、漏洞研究、脚本开发和钓鱼内容生成。生成式AI模型被证实能协助制作高可信度诱饵、优化恶意代码片段，以及加速针对特定技术目标的研究。

报告同时指出，攻击者正在探索具备Agentic能力的AI系统——这类系统能以最少人工干预执行多步骤任务，预示未来恶意软件可能集成更自主的决策模块，但目前尚未发现Agentic AI被广泛部署的证据。谷歌评估当前绝大多数案例仍属于对人类操作者的能力增强而非替代。

**Part04**

## ****业界专家质疑报告动机****

ImmuniWeb SA首席执行官Ilia Kolochenko通过邮件向SiliconANGLE表示："这似乎是谷歌在投资者对生成式AI兴趣消退、失望情绪蔓延之际，精心策划的公关宣传。"

他提出两点反驳：首先，即便APT组织在攻击中使用生成式AI，也不意味着该技术已能独立创建复杂恶意软件或完成完整攻击链；其次，谷歌在明知国家级团体和网络恐怖分子滥用其AI技术的情况下，可能需为相关攻击造成的损失承担法律责任。

Kolochenko强调："构建防护栏和实施客户尽职调查成本并不高昂，本可预防报告中提到的滥用情况。核心问题在于责任归属——谷歌恐怕难以给出令人信服的答案。"

**参考来源：**

Google warns attackers are wiring AI directly into live cyberattacks

https://siliconangle.com/2026/02/12/google-warns-attackers-wiring-ai-directly-live-cyberattacks/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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