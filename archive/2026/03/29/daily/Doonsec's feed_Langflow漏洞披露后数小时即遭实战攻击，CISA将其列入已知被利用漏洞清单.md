---
title: Langflow漏洞披露后数小时即遭实战攻击，CISA将其列入已知被利用漏洞清单
url: https://mp.weixin.qq.com/s/wZa2CmQ0JmDB1kaDYmuWpA
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:45:32.435031
---

# Langflow漏洞披露后数小时即遭实战攻击，CISA将其列入已知被利用漏洞清单

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKkibAhA4KpUhzHk6PhXwqEEGjYcnkxRbsuWHUmXJg8iclYvWEzfBt48NmBmpNpSGmttHnARmjRMo0icPpaJagIibSdLoG14iaJxWUGtk/0?wx_fmt=jpeg)

# Langflow漏洞披露后数小时即遭实战攻击，CISA将其列入已知被利用漏洞清单

数据安全研究组
数据安全研究组

数据安全合规交流部落

![]()

在小说阅读器中沉浸阅读

# CISA紧急警报升级：Langflow RCE被实战武器化，东南亚政府遭APT长期渗透曝光

**2026年03月29日**

---

CISA 拉响紧急警报——Langflow 关键 RCE 漏洞在数小时内遭到实战武器化，AI 应用框架的漏洞利用速度已远超任何人的预期。与此同时，一场针对东南亚多国政府机构的 APT 间谍攻击被完整曝光，攻击者综合使用 USB 蠕虫、远控木马与窃密工具，实现对政府网络的长期潜伏渗透。Anthropic 疑似泄露下一代模型 **Claude Mythos** 的存在，该模型据称专为安全漏洞检测设计，AI 安全攻防天平正加速倾斜。今天的每一条新闻，都指向同一个方向：防御窗口正在以小时为单位关闭。

---

## 🔴 重大事件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkic7JDKsOLibK0DloOnLkp0kvmnicgVDvALgXwcvHeCp7t3glI1zU4WNSvCR5HpR0x1SicQUUoNZkdMBD60Q4heuvAartdcu7Mbia5Y/640?wx_fmt=jpeg)

**CISA 紧急拉响警报：Langflow RCE 漏洞在数小时内被武器化，AI 基础设施大规模沦陷**

FreeBuf 报道，美国网络安全与基础设施安全局（CISA）就 Langflow 关键远程代码执行漏洞发出紧急警报，确认攻击者在漏洞披露后**数小时内**即完成武器化并发起实战攻击。Langflow 是被广泛用于构建 AI 工作流与 Agent 应用的开源框架，其漏洞直接暴露 AI 应用的执行引擎——攻击者不仅可以接管服务器，还可以劫持 AI Agent 的任务逻辑，访问其调用的所有外部 API 与数据库。CISA 将此漏洞列为已知被利用漏洞（KEV），**要求相关机构立即修复，不得拖延。** 所有部署 Langflow 的企业，今日内必须完成升级。
（来源：FreeBuf）

---

**东南亚政府机构遭 APT 组织长期渗透：USB 蠕虫 + RAT + 窃密工具三管齐下**

FreeBuf 披露一起针对东南亚多国政府机构的系统性 APT 间谍攻击活动，攻击者综合使用三类攻击工具：通过**USB 恶意软件**在物理隔离网络中传播，借助**远程访问木马（RAT）**建立持久化后门，再以**专用窃密工具**进行长期情报收集。攻击手法的多层组合揭示了攻击者深厚的定向攻击能力，能够同时应对网络隔离与物理安全防护。政府机构的长期潜伏特性使得此类攻击极难通过常规告警体系及时发现，USB 传播路径尤其难以在传统网络安全监控框架中被捕获。
（来源：FreeBuf）

---

**企业邮件威胁报告：正常邮件不足五成，AI 深度伪造攻击成新型钓鱼主力**

《2025 年中国企业邮箱安全性研究报告》揭示，国内企业邮箱用户全年收发邮件中**正常邮件占比不足五成**，国内注册企业邮箱独立域名达 550 万个，同比增长 3.8%，创近七年最大涨幅。AI 技术正在系统性重塑邮件攻击：AI 生成的高度个性化钓鱼邮件、AI 换声伪造的语音附件、AI 合成的"CEO 语音指令"正在成为商业邮件攻击（BEC）的主流手段，传统基于规则的邮件过滤效果正逐步失效。**邮件安全必须引入行为分析与内容语义理解能力，才能应对 AI 攻击升级的现实。**
（来源：嘶吼）

---

**影子 AI 泛滥：员工自发使用 ChatGPT、Claude 处理企业核心数据，成最难防的数据泄露路径**

嘶吼深度分析"影子 AI"现象的数据安全本质：企业员工出于提效目的，未经审批将代码、合同、客户数据输入第三方 AI 平台，已成为现阶段**最难被 DLP 等传统工具感知和管控的数据外流路径**。不同于恶意攻击，这种行为不产生异常告警，且往往被员工视为"正常工作方式"。一旦 AI 平台方发生数据泄露，企业敏感信息将毫无防护地暴露。企业必须将 AI 工具的数据流向纳入数据安全治理框架，而非仅依赖意识宣教。
（来源：嘶吼）

---

## 🟠 高危漏洞披露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKk8lfW1B1lGibsd9su7BhdQ4TNFpBQCibE8n0Ww7aEQj9qWjmBtxskxnjUPWJxt12VqP4VaT90Ov2s8BqgzAxtTUMUWC6aopCWANk/640?wx_fmt=jpeg)

**Anthropic 疑似泄露 Claude Mythos 模型：专项网络安全漏洞检测能力引发 AI 攻防格局震动**

FreeBuf 报道，Anthropic 疑似意外泄露了下一代 **Claude Mythos** 模型的存在，该模型据悉具备显著提升的网络安全漏洞检测专项能力。若 Claude Mythos 的安全检测能力属实，它将同时对攻防两端产生深远影响：防御方可用其自动化漏洞扫描，攻击方则可借其快速分析目标代码寻找突破口。AI 赋能下的漏洞发现速度竞赛，将进一步压缩安全团队的响应窗口期。
（来源：FreeBuf）

---

**Coruna 工具包升级 Triangulation iOS 攻击框架：数百万 iPhone 用户持续暴露**

FreeBuf 披露专门针对 iPhone 的 Triangulation 攻击框架完成新一轮演进，Coruna 漏洞工具包在此前串联六个 iOS 漏洞的基础上进一步强化了持久化与隐蔽性能力，数百万台运行旧版 iOS 的设备持续处于无声窃密风险之中。该框架此前曾被用于针对安全研究人员的 APT 定向攻击，工具演进意味着攻击门槛在持续降低，不再只有国家级攻击者才能利用。
（来源：FreeBuf）

---

**Claude 浏览器扩展零点击 XSS 提示注入漏洞：任意网站可无感劫持 AI 会话**

Claude 浏览器扩展高危漏洞持续有效，攻击者通过在任意网站嵌入特制内容，可对访问该页面的用户触发零点击 XSS 提示注入，在无任何用户交互的情况下劫持 Claude 会话，执行数据窃取与恶意操作。使用 Claude 扩展的企业员工每一次访问外部网站，都是一次潜在的攻击机会。**在官方补丁正式发布前，建议企业通过策略强制禁用该扩展。**
（来源：FreeBuf）

---

**Spring MVC Unicode 大小写绕过鉴权攻击链：ſ 转 S 的一个字符，打穿整个应用授权体系**

先知安全发布完整攻击链分析，揭示利用 Unicode 字符 **ſ**（长 s）转大写为 **S** 的特性，可绕过仅做小写匹配的 Spring MVC 鉴权拦截器，进而通过 Jackson 反序列化、文件描述符爆破等多步操作最终实现命令执行。这一攻击链展示了字符编码级别的安全漏洞如何被组合利用放大成完整 RCE，使用 Spring MVC 框架的开发团队应重点检查鉴权逻辑中的大小写处理是否存在类似缺陷。
（来源：先知安全）

---

**HPE Aruba OS 未授权密码重置漏洞：无凭据接管网络设备管理后台风险持续**

HPE Aruba OS 高危漏洞仍处于活跃利用窗口期，攻击者无需提供任何凭据即可重置管理员密码并完全接管网络设备管理后台。尚未完成补丁部署的机构应在本周内完成修复，临时措施包括将管理接口限制为仅限内网访问，并部署访问来源白名单。
（来源：安全客）

---

**WordPress Ally 插件高危 SQL 注入：约 40 万网站面临无授权数据库操控**

Ally WordPress 插件高危 SQL 注入漏洞仍处于活跃威胁状态，攻击者无需认证即可直接操控数据库，约 40 万使用该插件的网站面临批量数据拖取风险。自动化利用工具门槛极低，受影响站点应立即升级插件或临时停用。
（来源：安全客）

---

## 🟡 合规与监管动态

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk8LKH3IkWBsIQz3Vt40lI7vjX2An3PS9OwCia3QhtOiaLVByfp6oHlcLLTbhKfuhBylWe5PFJAo8ILZnwvJLgrPibPicE3L7CM1WKY/640?wx_fmt=jpeg)

**工信部 121 项 AI 安全治理标准落地在即：MCP 协议安全边界首次被纳入规范**

工信部发布 121 项行业标准征求意见计划，重点规范**模型上下文协议（MCP）安全**，对提示注入、越权操作等高频风险制定技术底线。结合 Langflow 漏洞遭 CISA 紧急通报的背景，AI 框架安全的合规化正在同步推进，企业应在规范正式落地前主动对齐，避免被动整改。
（来源：嘶吼）

---

**国家安全部深度伪造警告：AI 换脸换声已致多起企业重大经济损失**

国安部发出官方警示，明确指出深度伪造技术已被攻击者用于伪造企业高层的视频与音频指令，实施精准定向欺诈，国内已发生多起重大损失案例。企业应立即评估现有审批流程是否存在"仅凭视频/语音即可触发高风险操作"的环节，并为涉及资金转移和数据授权的指令建立独立二次核实机制。
（来源：嘶吼）

---

**Google 停止接受 AI 生成漏洞报告，强调人工验证不可替代**

安全牛报道，Google 正式宣布不再接受 AI 自动生成的漏洞报告，理由是此类报告质量普遍低劣、占用大量人工审核资源且有效率极低。Google 同期宣布投资数千万美元强化开源软件供应链安全。这与引入 LLM 代码审查导致供应链攻击成功率高达 88% 的研究形成呼应——AI 工具在安全审查领域的价值被系统性高估，人工判断仍是不可替代的核心环节。
（来源：安全牛）

---

## 🌐 国际动态

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKkibabmYDcKWCcicvdnMZqul07vtwDBzzGdiccm5m0TLA0IY9ZyRLCHQbAHcvFPInicicbibPO8D04IpeTkJwoWmt3v6kMF6Xh7Iibo2Cg/640?wx_fmt=jpeg)

**东南亚 APT 攻击深度解析：物理隔离 + 网络防护并存场景下的渗透路径**

此次东南亚政府机构遭受的 APT 攻击之所以值得特别关注，在于其攻击路径的系统性——USB 蠕虫解决物理隔离问题，RAT 提供持久化远控能力，窃密工具负责长期情报收集，三者协作完成传统安全防护体系难以覆盖的完整攻击链。这一模式对国内同类目标具有极强的参考价值：物联网终端、USB 打印机、移动存储介质等"最后一公里"设备，往往是最难纳入安全监控的盲区。
（来源：FreeBuf）

---

**Google 将抗量子加密迁移提前至 2029 年：密码基础设施升级窗口急剧收窄**

Google 已将全面部署后量子密码（PQC）的时间表从 2031 年提前至 **2029 年**，给整个行业留下的准备时间不足三年。TLS 证书体系、代码签名、数字身份认证等依赖现有非对称加密的基础设施均需完成迁移。金融、政务等高安全等级机构应今年启动 PQC 迁移规划，而非等待监管强制要求才行动。
（来源：安全牛）

---

## 💡 今日安全建议

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk9Z2WdYfVaJ6qxZozcDoJ2gt2OV0xVzmcu8wZ3lq0vCGKU4ia9Y2ba6l3icblwxa9ib13h6gFIFPIn8Ic3hDVA5p1WK4N54aianTQs/640?wx_fmt=jpeg)

**① Langflow 漏洞今日必须处理：CISA 已发出最高级别警报，无任何等待理由**
CISA 将 Langflow RCE 列入 KEV 意味着该漏洞已被确认在真实攻击中使用，任何运行 Langflow 的企业都面临即时风险。立即确认所有部署环境的 Langflow 版本，强制升级至官方修复版本，同时排查近期服务器日志是否已有异常 API 调用记录——感染可能已经发生。

**② 将 USB 设备管控纳入安全策略，定期扫描移动存储介质**
东南亚 APT 攻击案例中，USB 蠕虫是突破物理隔离的核心手段。企业应评估现有 USB 设备管控策略是否涵盖：只读 USB 配置、设备接入白名单、移动存储自动扫描等基础控制。对于涉密系统，应考虑在操作系统层面禁用 USB 存储设备写权限，仅保留鼠标键盘等 HID 设备的使用权限。

**③ 建立 AI 工具数据流向的主动监控，今天开始记录 AI 平台访问日志**
影子 AI 的数据外泄在没有主动监控的情况下几乎不可见。建议安全团队今天开始在出站流量日志中搜索员工设备对主要 AI 平台的访问记录，评估数据传输频率与体量，识别高风险的数据上传行为，并以此为依据制定 AI 工具使用管理规范——先了解现状，再制定政策。

---

*数据来源：安全客 · FreeBuf · 嘶吼 · 安全牛 · 先知安全 · Seebug Paper · 绿盟科技博客 · CNVD · CNNVD*
*本文仅供安全防御研究参考，请在合法授权范围内使用相关技术信息*
*转载请注明来源*

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YknTYfPDxUQX5JIwYiax7NPB4hzEuttRqaZgcAphmU5ick6pUaUNxjy5u8nONc1Rbrqu0nlYJpnibNicKlpDVcbrsQ/0?wx_fmt=png)

数据安全合规交流部落

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YknTYfPDxUQX5JIwYiax7NPB4hzEuttRqaZgcAphmU5ick6pUaUNxjy5u8nONc1Rbrqu0nlYJpnibNicKlpDVcbrsQ/0?wx_fmt=png)

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