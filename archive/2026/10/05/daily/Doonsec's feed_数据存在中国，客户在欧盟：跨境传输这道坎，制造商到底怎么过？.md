---
title: 数据存在中国，客户在欧盟：跨境传输这道坎，制造商到底怎么过？
url: https://mp.weixin.qq.com/s/n87N9uuRm6C07GDe40h1fQ
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:23:10.594652
---

# 数据存在中国，客户在欧盟：跨境传输这道坎，制造商到底怎么过？

# 数据存在中国，客户在欧盟：跨境传输这道坎，制造商到底怎么过？

原创

GTG-Hardy
GTG-Hardy

GTG网络安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzoKx62zMSJZm2xWz5PsicP41O6niay9JRnWdkuxia0UhEfYyzmvmXcickPPxEk2CUqSgHP6wf3PtbVEzltorIAjUKjdia0ZTG0SyIb4/640?wx_fmt=png&from=appmsg)

德国客户的订单、法国用户的 APP 账号、荷兰子公司的员工资料，实际上都躺在深圳的服务器里。

这不是配置错误，是默认架构：云平台架在国内、运维团队在国内、推送和统计 SDK 在境外、售后靠远程桌面连回客户的设备——**数据在欧盟产生，处理却发生在中国。**

很多厂家以为签一份 SCC 就合规了，结果客户来审计时要 TIA 拿不出来、要路径图也画不出来。

这篇想讲清楚三件事：**你的数据到底有没有出境、合规只有哪三条路、落地要走哪六步。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzpXD01C8b64fJiby7CGhTWP4oTa2SjlsqJdRicB6mHRhNOARgN8XiaVV9Pia0m9fniaIjNUf2cXvRINNxib35680Fz4U4PY7LIgFEr2s/640?wx_fmt=png&from=appmsg)

**0****1**

**认定前提：你的数据到底有没有出境**

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzp8wPxiadtVJQpuRoFHpjb6sFSY7LenhZpXzWsfefUvChnwT62LTMESSotibdBYQbNjVcKkCeia9YhsSr0aVRbg5sUDBUXHR1piagE/640?wx_fmt=png&from=appmsg)

**什么算传输（transfer）。**

 第 44 条原文是这么写的：

> Any transfer of personal data ... to a third country or to an international organisation shall take place only if ... the conditions laid down in this Chapter are complied with.

有两个最容易误判的点。

**第一，传输不等于复制。**判断标准是第三国的主体能不能接触到数据，不是数据有没有落盘。

**第二，远程访问也算。** 深圳工程师远程连上法兰克福的服务器看一眼日志，全程没下载文件，这依然构成传输。EDPB 在 Guidelines 05/2021 里说得很明确：只要能访问、查看，就属于第五章意义上的传输。

对着这张表自查，中一条就存在出境场景：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzqxeLBgePgKRHpvmjTkkZxSTEDmb9FQ2NrUNN7j1SW9LuDKxnznrAthy5LrymOLnz0ibnTIZTOjUcxP0HUBVAuNH6HcNmuw6vKE/640?wx_fmt=png&from=appmsg)

**02**

**路径选择：三条合规通道，中国制造商能走哪条**

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzqOR2FiacHjtIiaXqKsIDBMKFiaic3iaOcaZiaW7NhdnM43Edwrlpfic1icGSJsY3TgoTqwia6Ud7bV0tyVFqPz4pyick4N4uRmoNWnUkHzw/640?wx_fmt=png&from=appmsg)**

**第 46(1) 条那个附加条件，才是真正卡人的地方。**

原文是：

> ... only if the controller or processor has provided appropriate safeguards, and on condition that enforceable data subject rights and effective legal remedies for data subjects are available.

后半句的意思是：不只是签一份文件，还要保证数据主体有可执行的权利和有效的法律救济。

**03**

**关键缺口：签了 SCC 之后还差什么**

**SCC不是免责证明。**

2020 年欧盟法院在 Schrems II 案（案号 C-311/18）里明确：数据出口方（exporter）还要评估目的地国的法律会不会影响保护效果。

放到中国企业身上很具体——《国家情报法》第 7 条的协助义务、《数据安全法》第 35 条的依法调取，都会让评估结论偏向“存在风险”。

**再做一份TIA。**

TIA（Transfer Impact Assessment，传输影响评估）要回答三件事：**目的地国法律**（政府能不能拿到数据、有没有救济途径）、**数据本身**（是否涉及第 9 条特殊类别数据、规模多大）、**已有措施**（签了什么、技术上做了什么）。

顺带校正一个常见写法：TIA 不是 GDPR 哪一条明文规定的义务，它来自 Schrems II 判决和 EDPB 的建议文件。

**补充措施按 EDPB 三分法做。**

EDPB 在 Recommendations 01/2020 里把补充措施分成三类：

* **技术****（最有效）：**传输与端到端加密、假名化，密钥放在欧盟侧；
* **合同：**政府访问抗辩条款、透明度报告承诺；
* **组织：**最小权限、访问审批、远程会话留痕、禁止下载截图。

做完要有一句明确结论：措施是否有效、要不要调整、甚至要不要停止传输。

**04**

**执行路径：六步从场景盘点走到台账复审**

| 步骤 | 做什么 | 产出物 |
| --- | --- | --- |
| 1 | 画出境路径图（存储地、访问地、接收方），含远程访问 | 出境场景清单 + 路径图 |
| 2 | 每条路径匹配合法工具（第 45 / 46 / 49 条） | 路径—工具对照表 + 已签 SCC |
| 3 | 完成 TIA 并出书面结论 | TIA 报告 |
| 4 | 保障不足时补技术、合同、组织措施 | 补充措施清单 + 有效性结论 |
| 5 | 收集接收方合规证明，补齐 DPA 附件 | 文件清单 |
| 6 | 建传输文件台账，每年复审 | 台账 + 复审记录 |

第六步最容易掉：SCC 升级或到期没续签，传输依据就没了，而通常没人提醒你。

![](https://mmbiz.qpic.cn/mmbiz_png/U5ROicHxZUzpeMe8n9QnZU847mk2rAibuosI6ZDVkHWR5eoksKicFia1KiapJVLwNnibmeBVH1DfqQ6ZNfaJb3F5YTpcpFeBgSICBDSdwIKXvNgvo/640?wx_fmt=png&from=appmsg)

**05**

**常见误区：中国制造商最常踩的三个坑**

* **SCC 签了，TIA 没做：**文件在，结论拿不出来，客户审计时就是纸面合规。
* **远程访问没人管：**售后、IT、客服、研发都可能从国内连进来，很多厂家一个都没登记。
* **文件不做台账****：**人换了、云商换了，签的文件早就对不上现在的业务。

跨境传输不神秘，落到动作上就两步：承认数据在出境，然后给每条出境路径配一个说得过去的依据。

真要自查，先问一句：**我们所有从欧盟到中国的数据链路，能不能在一张图上画完？**

**广测电磁：全球数字安全合规优选伙伴**

**别让合规只停留在“拿证”。**

面对欧盟 CRA网络弹性法案、AI法案及 GDPR/CCPA/数据法案等严苛监管，凭借CNAS(L18872)+A2LA(6947.01)双资质及前360/深信服核心网络安全专家团队，为您提供真正的“实战级”防护。

**🏆 为什么GTG能为您降本避险？**

* 拒绝模板：不只给报告，我们提供定制化漏洞修复方案，确保产品真安全。
* 极致省心：代写核心文档，免除繁琐填表，让合规效率提升70%。
* 全域覆盖：从消费电子到汽车、工控、医疗，一站式解决全球隐私与数据安全难题。

您的全球合规通行证，从这里开始。

**[👉 立即咨询 CRA / AI法案 / 隐私合规]**

更多相关内容

欢迎关注视频号**“GTG网络安全实验室”**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U5ROicHxZUzouApxJNxTRuQwdawgsOzch47hiaktjGFWam1HvFN1RKwHBcdEVPB2nBEU0MDqG18wjVvEDsnGGSl0aIBRfTpicViaK5tJibmgicqG4/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/nU5v4aGBAyTCxIBHVZGhicPLY9XcpAMrBicsiaXF1ERvicoRgK6vx53LwYgdT5XnNziah1Mdmib8RsvVic7hrVm5fEI7Q/0?wx_fmt=png)

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