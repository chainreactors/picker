---
title: 2人团队，用Flocks全自动安全运营！
url: https://mp.weixin.qq.com/s/NDa7QKtdpLUtKpRo4ooUQQ
source: Doonsec's feed
date: 2026-08-27
fetch_date: 2026-08-28T13:34:37.104571
---

# 2人团队，用Flocks全自动安全运营！

# 2人团队，用Flocks全自动安全运营！

解放双手的
解放双手的

微步在线

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这是Flocks和一家科技制造企业的故事。这家企业的安全团队只有1-2名技术人员，但日常的安全运营重复性工作已全部被Flocks接管：

* 告警自动研判：工作流100%告警覆盖，15分钟一次，目标处置时效＜15分钟，效率提升80%
* DLP外发日志智能审计：499条→149条，噪声降低70.1%，2-3小时→4分钟，提效30-45倍；
* 零信任问题AI诊断：单次排查至少节省5分钟，SOP与案例沉淀为可复用Agent；
* IOC 自动同步封禁：每日自动抓取情报、查重入库，联动防火墙与零信任双通道批量拉黑；
* 安全态势报告每日自动生成，覆盖已接入数据源100%；
* 漏洞扫描录入处置整改自动化+全流程跟踪。

而这个安全团队的工作流、Agents、Tools和Skill，以及构建与安装的使用说明文档、提示词等被我们脱敏并整理成了压缩包，扫描下方二维码，即可有机会获取。

![](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K97WNv1yUtNfM1h12E4Ff1at2QMxgR0no1YmVOqyicQqchUeibVtLX15g2RBFB0djoWiceG1LKUDDvBYtV7TyWUic6bATjSicNn1CicBg/640?wx_fmt=png&from=appmsg)

扫码，马上让Flocks给你打工

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KJ5kFuz2K96jCw9TnHDVlXTdP2lXrtkyOL4X2DtiamINBebLOJ16qsBKqXweglBCYQfhkyvap3L4zTNXmmyicFBoibUhmX9kNVv1SYOc6MBXia0/640?wx_fmt=jpeg&from=appmsg)

**方案与架构**

### 当安全团队接触到Flocks以后，他们根据自身需求，对Flocks需要实现的能力进行了简单编排，具体架构如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K97pXbVCUx8k7k06V5v66ZlAw9FRN9JNibkh0RkYiaPnVEz0zDb88ibuFx8axXianYyjbMThFX9EIgtDC7GCbeiaknbmFfDAnWgnbRFQ/640?wx_fmt=png&from=appmsg)

在落地时，他们梳理了安全运营中最常用、也最耗时的六大场景，每一个运营场景对应一个工作流，工作流之间共享数据、相互触发。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K94PU88JdqoV2cmps9ZoVcODKI9lYHsqicZUaoEXdCpSxOlMsmqQibXhPIF5ic4mv4icIlHXRIK2YO9XeSCsUGUWQ0o7ialCZdEXBRWI/640?wx_fmt=png&from=appmsg)

**六大核心工作流**

工作流一：DLP员工外发日志智能审计

通过工作流自动完成员工和岗位解析、日志分页拉取、规则过滤、LLM批量研判、完整性校验和Excel报告导出。以往用云枢控制台逐条翻看日志的单次审计通常需要数小时；通过Flocks工作流自动跑完后，噪声被自动过滤，人工只需对可疑结果做最终确认。单次审计从"数小时"压缩到分钟级，噪声被自动过滤。

工作流二：SIP / EDR告警自动研判

传统模式无法覆盖所有事件人工排查；5分钟定时拉取EDR/SIP/NDR事件，自动查询CMDB、定位资产归属、补充情报信息，并由AI判断是否为误报。可确认的误报自动标记忽略，无法判断的事件转人工处置，并附带诊断信息，让1-2人也能覆盖数千条告警。

工作流三：员工零信任问题AI诊断

创建诊断子Agent，该智能体会获取关于CMDB、零信任、网络策略等API和排查SOP的知识。用户输入问题后，Agent自动收集上下文、执行检查步骤、输出原因判断和处理建议。员工无法访问内网资源、无法科学上网或零信任策略异常等高频问题，无需再占用安全/IT人员精力。

工作流四：威胁情报自动获取与封禁

通过silverfox\_ioc\_sync、silverfox\_hrti\_ioc\_sync、hrti\_vuln\_sync三个工作流，自动从情报网站、MCP工具和威胁情报源获取IOC，按Domain、IP、Hash分类提取，自动查重并写入飞书多维表格。对确认需要处置的IOC，联动防火墙、零信任等能力执行封禁。同时支持每日监控勒索情报，定时将飞书多维表格中当天的IOC批量拉黑。

工作流五：安全态势分析与报告生成

通过API或浏览器自动化获取安全设备数据，结合多维表格中的处置结果、告警分类和趋势数据，自动生成每日安全态势报告。全人员不再需要每周/月手工整理数据、撰写汇报材料。

工作流六：安全测试辅助与漏洞扫描闭环

创建渗透测试子Agent，该子Agent可应用Xray扫描器能力，辅助安全测试人员开展测试任务。子Agent根据目标资产、测试范围和历史案例生成测试思路，调用Xray执行漏洞扫描，对扫描结果进行初步分类、去重和风险描述标准化，最后自动录入飞书多维表格。

**复用组件能力**

不同安全场景沉淀为可复用Skill，不同专家能力沉淀为专用Agent。后续新增场景时可以复用现有的数据接入、研判Prompt、处置动作和报告模板，降低扩展成本。

核心Skill矩阵：

* yunshu\_dlp\_audit（DLP外发日志智能审计）
* sangfor\_sip\_disposition / yunshu\_edr\_disposition（NDR/SIP告警研判）
* yunshu-diagnosis（零信任问题智能诊断）
* hrti\_vuln\_sync（每日威胁情报获取）
* silverfox\_hrti\_ioc\_sync（银狐IOC每日获取）
* ransomware\_monitor（勒索情报每日获取）
* security\_daily\_report（每日安全态势日报）
* xray-scanner-use（长亭Xray漏扫）
* feishu-bitable（飞书多维表格）
* elk\_waf\_access\_log（ELK数据获取）

###

**落地效果**

### 这套架构在1-2人团队的真实运营中跑通后，团队观察到的几个关键变化：

单次审计从数小时压缩到分钟级。 DLP外发日志审计原本需要安全人员在云枢控制台逐条翻看、单次审计通常需要数小时；通过yunshu\_dlp\_audit工作流自动跑通后，LLM批量研判 + Excel报告导出，审计耗时显著缩短。

EDR+SIP告警疲劳显著缓解。 EDR每天约3000条事件、SIP每日约数十条失陷告警，传统模式1-2人无法覆盖所有事件人工排查；通过15分钟定时轮询拉取+AI自动去重与误报识别，大量重复性无效告警被自动忽略，每条事件自动提取 IOC信息沉淀至飞书多维表格归档，处置时效由数小时压缩至15分钟内，团队精力聚焦于极少数需人工判断的事件。

威胁情报消化形成闭环。 银狐IOC、勒索情报、漏洞情报三类情报源全部接入工作流，每日自动获取、分类查重、批量封禁，情报消化从"凭感觉"变成"靠系统"。

渗透测试和漏洞扫描不再漏录。 Xray扫描器能力 + 渗透测试子Agent形成"测试执行 → 漏洞发现 → 结果入库 → 整改跟踪"的闭环，解决了过去漏录、重复录入、漏洞描述不统一的问题。

报告生成自动化。 每日安全态势日报、周报、月报由security-report Agent自动生成，管理层汇报不再依赖安全人员手工整理数据。

在安全运营中，Flocks能让每一个重复场景变成"工作流一次配置，长期自动运行"，利用外部第三方在线多维表格沉淀数据结果，后续复盘、汇报、跨部门协作都有了统一的数据源。而可复用Skill，专家Agent的沉淀，能让小团队在新增安全场景时复用现有数据接入、研判Prompt、处置动作、报告模板，从而在不扩编的情况下，持续扩展安全运营的边界。

# ·END·

#

![](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K97E1sibCKJApUGN131ab4asy4Nibkt6Zsia2o7mrWxH6BEEQ1xYBx9glq5Wa3F6d6nEnbXSGqGTOIGT4fYQw08DEg7uhoddgOXEJQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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