---
title: 网络首发 | 北京航空航天大学关振宇教授团队：大语言模型驱动的网络协议逆向与安全测试方法
url: https://mp.weixin.qq.com/s/qvIFti3o7lKnvQLsOOmifA
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:49:56.835726
---

# 网络首发 | 北京航空航天大学关振宇教授团队：大语言模型驱动的网络协议逆向与安全测试方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3atRN4gmtIpwoicMtzvR6ErqlDoKEOoQFh6yTVN5to4QAib5yz6ynh0cA/0?wx_fmt=jpeg)

# 网络首发 | 北京航空航天大学关振宇教授团队：大语言模型驱动的网络协议逆向与安全测试方法

网络空间安全科学学报

![]()

在小说阅读器中沉浸阅读

**引用**

张东，詹一宸，白家驹，等.大语言模型驱动的网络协议逆向与安全测试方法[J/OL].网络空间安全科学学报,1-12[2026-01-24].

https://doi.org/10.20172/j.issn.2097-3136.251015.

ZHANG D，ZHAN Y C，BAI J J，et al. Large Language Model-Driven network protocol reverse engineering and securitytesting methodology[J/OL]. Journal of Cybersecurity，1-12[2026-01-24].

https://doi.org/10.20172/j.issn.2097-3136.251015.

**背  景**

在网络设备日益普及的今天，路由器、工业控制系统等终端的安全问题日益突出。2016年Mirai僵尸网络攻击事件导致美国域名服务商Dyn瘫痪，北美和欧洲大面积网络中断，充分暴露了网络设备协议漏洞的严重性。当前主流的协议安全测试方法通常面临以下问题：依赖固件代码分析、需要大量流量样本、无法应对缺乏文档的私有协议、自动化程度有限，难以覆盖未知或高度定制化的协议场景。针对上述挑战，北京航空航天大学网络空间安全学院关振宇教授团队提出了一种大语言模型驱动的网络协议逆向与安全测试方法，并据此设计了一套自动化测试框架——LRPT，并在实际网络设备测试中发现了10个未公开安全漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3GyJT4OsicJkPaUial7xiciaibGdNH8GabO4LDfthDRSImlgbZHF8DsHWU3g/640?wx_fmt=png&from=appmsg)

**01**

LRPT方法以DeepSeek大语言模型为核心构建智能代理系统，能够在仅有少量HTTP协议流量样本的情况下，实现协议结构的自动化推断、测试请求生成、交互反馈与漏洞检测。该系统通过智能化的迭代机制，使协议理解能力持续进化：大语言模型不仅能够从有限样本中推断出潜在的参数结构、字段约束和状态转移关系，还能基于服务器响应动态修正协议模型，识别新的接口路径和异常行为模式。整个过程形成了一个自适应的学习闭环——从初始流量采集到语义解析、测试生成、响应分析，再到协议模型迭代与安全漏洞标记，系统在交互中不断扩展对未知协议的认知边界，最终实现精准高效的漏洞挖掘，图1展示了本方法的完整工作流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3ibmy6JdsGFKDxTRJtTM9NeVwF3efy41lFYFFS1vWkzbPdic2JJqc9ggg/640?wx_fmt=png&from=appmsg)

图1  LRPT模型结构

Fig.1  The architecture of the LRP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3GyJT4OsicJkPaUial7xiciaibGdNH8GabO4LDfthDRSImlgbZHF8DsHWU3g/640?wx_fmt=png&from=appmsg)

**02**

LRPT的核心在于其智能代理系统的设计，该系统通过多个协同工作的模块实现了对未知协议的智能化探索。其中，协议结构与语义推断模块利用大语言模型对预处理后的流量样本进行深度语义解析，不仅能自动识别消息类型、参数结构及字段含义，构建初始协议知识库，还能基于有限观察进行逻辑推理。例如，当模型识别到"action": "get"操作时，能自动推断出可能存在"set""delete""update"等关联操作，并生成相应的验证测试用例，从而系统性地扩展协议功能字段空间。与现有方法相比，LRPT展现出三大显著优势：

* 一是摆脱了对固件或RFC文档的依赖，可直接从网络报文中推断协议结构，特别适用于私有协议场景；
* 二是具备强大的小样本适应能力，即使仅有少量流量样本，也能通过语义推理有效扩展协议探索空间；
* 三是实现了高度自动化，大幅降低了安全分析的技术门槛，使复杂的协议安全测试变得更加高效和普及。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3GyJT4OsicJkPaUial7xiciaibGdNH8GabO4LDfthDRSImlgbZHF8DsHWU3g/640?wx_fmt=png&from=appmsg)

**03**

为验证LRPT方法的有效性，研究团队选取了来自ToToLink、NetCore、Linksys等品牌的6款常见家用路由器作为测试对象，并在其真实的最新版固件环境中开展实验。实验设定了严格的对比条件，确保输入一致、资源均等、判定标准统一。所选对比工具涵盖传统模糊测试框架Boofuzz与Snipuzz、协议逆向工具Netzob，以及LLM-Netzob（即基于大语言模型生成协议模板并应用于Netzob的混合方法）。实验取得了令人瞩目的成果：LRPT共发现了10个未公开安全漏洞，而Boofuzz、Snipuzz与Netzob均未发现任何漏洞，LLM-Netzob发现了3个漏洞。这些漏洞覆盖了信息泄露、未授权访问、拒绝服务、协议逻辑缺陷乃至远程代码执行等多种高危风险。具体漏洞对比结果详见表1。

表1  已发现的未公开漏洞

Table 1  Unreported Vulnerabilities Revealed

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3bjIKBl8Xnw2ETPAcgiahzAZ1TocT01fdxL38amoJhLfeBQurRJfxFYA/640?wx_fmt=png&from=appmsg)

所有漏洞均已报送至国家信息安全漏洞共享平台，其中6个已获得CNVD编号，CNVD编号获取情况见表2。

表2  CNVD编号信息

Table 2  CNVD Identification Number

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3tE5wBMORXSCBaMDPad5dudn8ffez87xqEj8LE369TAypRqTvEa097Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3GyJT4OsicJkPaUial7xiciaibGdNH8GabO4LDfthDRSImlgbZHF8DsHWU3g/640?wx_fmt=png&from=appmsg)

**总结**

本研究证实了大语言模型在网络协议安全测试领域，尤其是针对缺乏文档的私有协议场景下具有显著潜力。LRPT方法通过语义推理与动态反馈迭代机制，有效提升了协议逆向的自动化程度与漏洞挖掘深度。展望未来，可进一步开展跨模型能力对比研究，通过引入Gemini、Claude、GPT等不同架构大语言模型进行横向评估，以探究模型能力差异；同时可推进垂域安全模型微调，利用高质量安全语料进行针对性训练，从而增强模型在漏洞模式识别等专业任务中的表现。随着大语言模型技术的持续演进，其在网络安全领域的应用将不断深化，以LRPT为代表的研究方向正推动安全测试从依赖专家经验的传统模式，向智能化、自动化的新范式转变，为构建更稳固的网络空间安全防线提供了创新技术支撑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxAygTQdia2Hw7Xweq1hJOzI3GyJT4OsicJkPaUial7xiciaibGdNH8GabO4LDfthDRSImlgbZHF8DsHWU3g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxCkTcfcpQW10RBaTfPBnUVbp9Jk2IHuePBhxXQ3E40s5hUaQibnp2Qiav2IdYYTxria4cBoArYcWOspQ/640?wx_fmt=png)

《网络空间安全科学学报》由中国航天科技集团有限公司主管、 中国航天系统科学与工程研究院主办，双月刊，国内外公开发行（CN 10-1901/TP，ISSN 2097-3136），入选中国科学引文数据库（CSCD）核心库、《信息通信领域高质量科技期刊分级目录》T2级。办刊宗旨为“搭建网络空间安全领域学术研究交流平台，传播学术思想与理论，展示科学研究、创新技术与应用成果，助力网络空间安全学科建设，为网络强国建设提供坚实支撑与服务”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bpXMCVmmaxCkTcfcpQW10RBaTfPBnUVbpH7OESyiayAb2icdRqR7YHbCACAybEjpJD8NFTOxw06LzqbQNS7Uxmtw/640?wx_fmt=jpeg)

网站：www.journalofcybersec.com

电话：010-89061756/ 89061778

邮箱：wlkjaqkxxb@spacechina.com

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxA5UN8DNQAriaCeMRY5VHUlR4LtqP4uyVIiabYrqUNyHap5IW3ZQ41pv2Q9icgHjMoXO5IdiahpZmtibicQ/0?wx_fmt=png)

网络空间安全科学学报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/bpXMCVmmaxA5UN8DNQAriaCeMRY5VHUlR4LtqP4uyVIiabYrqUNyHap5IW3ZQ41pv2Q9icgHjMoXO5IdiahpZmtibicQ/0?wx_fmt=png)

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