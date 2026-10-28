---
title: 电子科技大学 | 计算机学院鲁力教授团队成果获MICRO 2026录用
url: https://mp.weixin.qq.com/s/nmALoDJJ3oIuiwYVHZ_1yQ
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:41:30.560805
---

# 电子科技大学 | 计算机学院鲁力教授团队成果获MICRO 2026录用

# 电子科技大学 | 计算机学院鲁力教授团队成果获MICRO 2026录用

信息网络安全杂志

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近日，第59届IEEE/ACM国际微体系结构研讨会（The 59th IEEE/ACM InternationalSymposium on Microarchitecture，MICRO 2026）公布论文录用结果。电子科技大学计算机学院鲁力教授团队的论文《Hades: A Hardware-Resident Substrate for Energy Admission inIntermittent Computing》被大会录用。该成果实现了电子科技大学首次以第一署名单位在MICRO发表论文，也填补了中国西部高校以第一署名单位在该会议发表论文的空白。

论文第一作者为计算机学院2024级博士生王晗，通讯作者为鲁力教授。团队已毕业博士（现西南石油大学副研究员）张翀为论文第二作者和核心合作成员。其他作者包括团队已毕业博士（现哈尔滨工业大学副研究员）孟千贺，以及团队博士生赵一泽、张睿喆。

在需要长期无人值守的物联网应用中，感知节点往往部署于难以频繁维护的环境，传统电池受使用寿命限制，更换成本高，在低轨卫星、深海和地下管廊等场景中难以实施。为摆脱对电池的依赖，无源感知系统通过采集光能、射频、温差和振动等环境能量维持运行。然而，这类能量通常微弱且间歇，传统系统需先唤醒微控制器（MCU），在软件运行时完成能量采样、状态解析、任务调度和检查点维护。在弱能量条件下，相关管理开销最高可占输入功率预算的约70%，成为制约任务吞吐和能量利用率的关键瓶颈。

![](https://mmbiz.qpic.cn/mmbiz_png/FNlvhjUaDTPIEwCBGOibYn0waYbqIXh8FL9E4TjibXoTTNXydtnPNvFyZbibyu88PZCZqgLGByiauFIV2GLqia27Plse7miby3xmeZll4HXcRNWpw/640?wx_fmt=png&from=appmsg)

图1 传统软件主导的间歇计算架构：MCU被唤醒后需先完成能量监测与运行时管理，才能执行应用任务

针对这一问题，论文提出硬件驻留型混合信号能量准入架构Hades，构建独立于MCU指令流的硬件控制路径。在MCU启动前即以近零开销完成能量准入判断，避免反复执行能量轮询和准入调度等软件运行时代码。实验结果表明，该方案仅增加0.29%的芯片面积，便能将能量准入开销降低98%以上，使每焦耳能量完成的任务数提升至基线系统的2.4倍，端到端任务吞吐量最高提升至2.5倍，为无源物联网设备在弱能量、难维护环境中的长期稳定运行提供了新的体系结构路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FNlvhjUaDTP7x7ibuRqbG2icqcUFKGofE05Ddia3LaDzHZA4zMEcrTd5ZUPj5hf9ZULb3ojia5yWGTer9JKKpPzLicIW4ia3ZXsfcCY060fbIvkF8/640?wx_fmt=jpeg&from=appmsg)

图2 Hades能量准入路径：在MCU启动前即以近零开销硬件完成全流程能量管理

**相关链接：**

智能计算系统团队长期围绕端侧智能、超低功耗无线系统、物联网计算与无线安全开展研究，致力于解决资源受限设备面临的感知、通信与计算难题。团队负责人鲁力教授主持国家自然科学基金重点项目、国家重点研发计划课题等科研项目10余项，在IEEE/ACM MICRO、ACM ASPLOS、USENIX NSDI、ACM MobiCom等国际顶级会议和期刊发表论文90余篇。王晗现为团队在读博士生，依托团队长期研究积累，在鲁力教授指导下持续开展超低功耗无线网络与端侧智能计算研究，已以第一作者在IEEE/ACM MICRO、ACM MobiCom、IEEE/ACM ToN等CCF-A类国际顶级会议和期刊发表论文3篇，相关成果曾获ACM SenSys最佳论文奖，并入选ACM SIGMOBILE Research Highlights。

自1968年创办以来，MICRO持续推动处理器微体系结构、编译优化、芯片系统设计与软硬件协同等方向的发展。会议由IEEE和ACM联合主办，与ISCA、HPCA和ASPLOS并列为计算机体系结构领域四大顶级会议。截至2025年，MICRO历届共录用论文2473篇，其中中国大陆高校、科研机构或企业参与的论文仅115篇。

来源：电子科技大学

![图片](https://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsN8yDJWicSECDq8dgel7DctAMAnNheJf2kkfQOiaFMdZaWNIDt9IxOkEhI5TJar4wnyAiba9twTOxeKZg/640?wx_fmt=png)

**信息网络安全**

《信息网络安全》创刊于2001年，是由公安部主管，公安部第三研究所、中国计算机学会主办，面向国内外公开发行的国内首批信息安全类期刊之一，于2015年成为中国科技核心期刊，2017年成为中国科学引文数据库来源期刊，2018年成为中文核心期刊，2022年入选CCF计算领域高质量科技期刊分级目录。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icL7Q0hLWsN9e1fkuM1ibgD3PcZiaqJrZia7KQWDwichD8lvo4RqfPcNkuyqje45IOXD0HocBDntaDdK4tibWoTIs5Ww/640?wx_fmt=jpeg)

中文核心期刊

中国科技核心期刊

中国科学引文数据库来源期刊

CCF计算领域高质量科技期刊

![图片](https://mmbiz.qpic.cn/mmbiz_png/v4vz52CcB12BRNZGqdRDIBsUQ6WickDoUNkuVicKXooNbRSzdGDGuJtxJodlbpr1B07yAReAz5V5jj47Yaq7ujRw/640?wx_fmt=png)

我们在不断努力和完善中，期待您的关注和支持！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icL7Q0hLWsNibBlGIDAuhv04Ap5j7X2I4Se7j2nvibDibXXmaA8WJqgXZ2Lh8sShG6jas26z3WlRcANNqZnr3nMTnQ/0?wx_fmt=png)

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