---
title: Claude Code 30分钟挖出Vim用了三十年的0Day，收到陌生文件先别急着打开
url: https://mp.weixin.qq.com/s/ho2ScK7cCBbPWGEAyhZmeQ
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:24:01.968188
---

# Claude Code 30分钟挖出Vim用了三十年的0Day，收到陌生文件先别急着打开

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKkicBpx1ic1hlXmqDErSibXUhricM0zPBLmZfOWDszpuyrOsTtB4az6OIMEEibtTSNLUD1bg1piblgKNicsNDuxdrryamJVSTCaicAFcaic8/0?wx_fmt=jpeg)

# Claude Code 30分钟挖出Vim用了三十年的0Day，收到陌生文件先别急着打开

数据安全研究组
数据安全研究组

数据安全合规交流部落

![]()

在小说阅读器中沉浸阅读

# AI用30分钟找到Vim三十年老工具的0Day，打开一个文件你的服务器就沦陷了

**2026年04月02日**

---

安全研究人员使用 **Claude Code** 在 30 分钟内发现了 Vim 与 GNU Emacs 的多个零日漏洞，随即被确认为高危 RCE 漏洞（**CVE-2026-34982**）——攻击者仅需向受害者发送一个恶意文本文件，用户一旦用 Vim 打开即触发任意代码执行，沙箱防护形同虚设。这不仅是一次具体漏洞的披露，更是 AI 辅助漏洞挖掘全面进入实战阶段的历史性标志：攻击者现在可以用 AI 以前所未有的速度批量发现开发者最依赖的工具中的漏洞。与此同时，**14000 余个** F5 BIG-IP RCE 漏洞实例仍暴露在互联网上未打补丁，**WhatsApp** 假冒 App 间谍软件已感染真实用户。今天的威胁，来自你每天在用的工具。

---

## 🔴 重大事件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkic7JDKsOLibK0DloOnLkp0kvmnicgVDvALgXwcvHeCp7t3glI1zU4WNSvCR5HpR0x1SicQUUoNZkdMBD60Q4heuvAartdcu7Mbia5Y/640?wx_fmt=jpeg)

**Claude Code 用 30 分钟发现 Vim 与 Emacs 多个 0Day：AI 辅助漏洞挖掘正式进入全面实战**

FreeBuf 报道，安全研究人员使用 **Claude Code** AI 编程助手对 Vim 和 GNU Emacs 代码库进行分析，在 **30 分钟内**成功识别出多个零日漏洞，随即被官方确认并分配 CVE 编号。这是 AI 辅助漏洞挖掘从"实验室演示"走向"实战工具"的标志性节点。泛联新安代码钟馗此前也在 OpenClaw 框架中以类似方式、消耗 **200 万 token**、历时 30 分钟发现高危持久性注入漏洞并上报 NVDB。两件事同时发生意味着同一个结论：**AI 工具已经可以系统性地、以小时为单位在大型成熟代码库中发现隐藏多年的安全漏洞**，这对防御侧和攻击侧的能力平衡都是根本性改变。
（来源：FreeBuf / 嘶吼）

---

**Claude Code 源代码泄露后续：Anthropic 紧急联系 GitHub 下架超 8000 份副本，确认非安全漏洞**

unSafe.sh 报道，Anthropic 对 Claude Code 源代码泄露事件完成应急处置，紧急联系 GitHub 下架了超过 **8000 份**代码副本与改编版本。官方声明泄露不涉及客户数据或模型核心算法，根因是员工在打包发布流程中的人为操作失误，而非安全漏洞被利用。尽管如此，已在野外流传的源代码副本可能被用于逆向分析 Claude Code 的实现细节，为针对性攻击提供路线图。**使用 Claude Code 的企业和开发者应密切关注 Anthropic 后续的官方安全公告。**
（来源：unSafe.sh）

---

**WhatsApp 警告：200 名用户遭意大利 SIO 公司设计的假冒 App 感染间谍软件**

unSafe.sh 报道，WhatsApp 官方发出警告：意大利监控软件公司 **SIO** 设计了一款外观与 WhatsApp 高度相似的假冒应用程序，通过社会工程学手段诱骗 iPhone 用户下载安装，成功将间谍软件植入受害者设备。已确认至少 **200 名用户**受到影响。WhatsApp 强调此次事件不是其自身平台漏洞，而是用户被引导安装了第三方恶意应用。所有受影响账号已被强制登出，WhatsApp 要求受害者删除假冒 App 并下载官方版本。**提醒：任何软件的安装来源都必须是官方 App Store，不接受任何"内测版"或"增强版"的链接邀请。**
（来源：unSafe.sh）

---

**Drift 加密平台发生重大安全事故：细节待披露，加密资产用户需保持高度警惕**

嘶吼报道，加密金融平台 **Drift** 发生重大安全事故，目前官方尚未完整披露事故细节与损失规模。加密平台安全事故在近期呈现高频态势，与朝鲜黑客组织 UNC1069 对 axios 的供应链投毒、专门针对加密钱包的窃密行动形成呼应。**持有加密资产的用户应立即将资产转移至硬件冷钱包，暂停使用受影响平台，等待官方明确公告。**
（来源：嘶吼）

---

## 🟠 高危漏洞披露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkicnpvbP39AcJIa9MHCBxNWRicq6r62c2qvclLapWR682BSoVmwBMpoGLe8PpYghoQ740qHF42xVlKA7ZuL2giaI4NsmSvNBlYFw8/640?wx_fmt=jpeg)

**Vim CVE-2026-34982 高危 RCE：打开任意文件即触发漏洞，Vim 9.2.0-9.2.0272 全线受影响**

FreeBuf 发布 CVE-2026-34982 完整分析，**Vim 9.2.0 至 9.2.0272** 版本存在高危远程代码执行漏洞：攻击者通过构造特制恶意文件，受害者只需用 Vim 打开该文件即可触发漏洞，沙箱防护被有效绕过，攻击者获得受害者权限下的任意命令执行能力。钓鱼文件传播场景（伪装为配置文件、日志、文本说明）是主要攻击载体。**立即执行：`vim --version` 核查当前版本，若为受影响版本立即升级至官方最新修复版本；在修复前避免用 Vim 打开任何来源不明的文件。**
（来源：FreeBuf）

---

**F5 BIG-IP CVE-2025-53521 被重新分类为 RCE：14000 余个实例仍暴露网络，补丁率极低**

unSafe.sh 报道，F5 BIG-IP APM 高危漏洞 **CVE-2025-53521** 被官方从"拒绝服务（DoS）"重新分类为**远程代码执行（RCE）**，危险等级大幅升级。Shadowserver 监测数据显示，目前仍有超过 **14000 个**受影响实例直接暴露在互联网上，CISA 已要求联邦机构强制修复，但全球大量非联邦机构的设备仍未打补丁。F5 建议受影响用户从安全来源重建完整配置，以防止恶意软件在修复后仍有残留。**仍未修复的机构今日应当作最优先任务处理。**
（来源：unSafe.sh）

---

**Nginx-UI 备份恢复漏洞 PoC 公开：加密备份可被篡改，攻击者可注入恶意 Nginx 配置实现全控**

FreeBuf 报道，**Nginx-UI**（流行的 Nginx 可视化管理界面）备份恢复功能存在严重漏洞，PoC 已在安全社区公开流传：攻击者可篡改经加密的备份文件，在恢复过程中注入恶意 Nginx 配置，最终实现对服务器的完整控制。Nginx-UI 在国内外服务器运维社区广泛使用，PoC 公开后漏洞利用门槛大幅降低。**今日立即：暂停使用 Nginx-UI 的备份恢复功能直到官方补丁发布，并审查已有备份文件的完整性。**
（来源：FreeBuf）

---

**Google Vertex AI "双重间谍"风险：AI Agent 可利用宽松权限配置实现内部横向渗透**

unSafe.sh 报道，Palo Alto Unit 42 研究发现，**Google Cloud Vertex AI** 平台的默认配置和宽松权限设置可能导致 AI Agent 被"武器化"——攻击者可利用 AI Agent 获取到的服务凭证访问内部代码库、提升权限、触发供应链安全风险。Unit 42 将这一威胁模型称为"double agent"（双重间谍）：AI Agent 作为内部合法用户，利用已有的高权限造成远超外部攻击者的破坏效果。Google 官方建议采用 BYOSA（自带服务账号）模型降低风险。
（来源：unSafe.sh）

---

**OpenClaw 生态安全事件全景：从 RCE 漏洞到 Skill 供应链投毒，AI Agent 安全进入至暗时刻**

嘶吼多篇深度分析全面梳理 OpenClaw 近期安全事件：**RCE 漏洞**（提示词注入绕过边界标记机制）、**Skill 供应链投毒**（恶意 Skill 被推至下载首位）、**蚂蚁 AI 实验室发现的 1 严重 + 4 高危漏洞**（普通账号可接管智能体），以及工信部 NVDB 发布的紧急预警，共同构成了 AI Agent 生态在爆发式增长后的安全代价。OpenClaw 在 GitHub 上已获 **183K Star**，庞大的用户基数意味着每一个未修复漏洞都对应着极大的攻击面。
（来源：嘶吼）

---

## 🟡 合规与监管动态

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk8LKH3IkWBsIQz3Vt40lI7vjX2An3PS9OwCia3QhtOiaLVByfp6oHlcLLTbhKfuhBylWe5PFJAo8ILZnwvJLgrPibPicE3L7CM1WKY/640?wx_fmt=jpeg)

**4 月起多项网安新规正式施行：严打恶意索赔，规范免密支付自动扣款**

嘶吼报道，多项影响互联网平台安全的法规于 **2026 年 4 月 1 日**正式施行，核心内容包括：严厉规制恶意利用平台规则进行索赔的行为；规范互联网免密支付与自动扣款流程，要求平台对高风险操作强制二次确认。对企业运营侧的直接影响：**免密支付和自动扣款相关功能需立即按新规进行合规评估，避免在监管检查中被认定为违规。**
（来源：嘶吼）

---

**CNNVD AI 漏洞通报第四期：10 天内采集重要 AI 漏洞 162 个，单位时间密度创新高**

CNNVD 发布人工智能重要漏洞通报第四期，统计周期为 **2026 年 3 月 20 日至 3 月 30 日**，仅 10 天内共采集重要 AI 漏洞 **162 个**——折算日均约 16.2 个，远超前三期统计的周均水平，与 Claude Code 发现 Vim/Emacs 0Day 的新闻一同印证：AI 安全漏洞的发现速度正在被 AI 工具本身加速。
（来源：CNNVD）

---

## 🌐 国际动态

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKkibabmYDcKWCcicvdnMZqul07vtwDBzzGdiccm5m0TLA0IY9ZyRLCHQbAHcvFPInicicbibPO8D04IpeTkJwoWmt3v6kMF6Xh7Iibo2Cg/640?wx_fmt=jpeg)

**Trivy 供应链攻击影响范围持续确认：Docker Hub 官方镜像遭污染，GitHub 组织账号批量被劫持**

嘶吼报道，TeamPCP 对 Trivy 的供应链攻击影响范围进一步确认：除此前披露的 GitHub Actions 组件被劫持外，攻击者还成功向 Docker Hub 官方镜像仓库推送了**伪装的恶意 Docker 镜像**，并批量劫持了多个企业 GitHub 组织账号，篡改数十个开源代码仓库。此次攻击链已覆盖从 GitHub Actions → Docker Hub → 下游企业仓库的完整污染路径，**每一个在 CI/CD 流水线中使用 Trivy 的团队，今日都必须验证镜像哈希完整性。**
（来源：嘶吼）

---

## 💡 今日安全建议

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk8YiaCLsEFeA5jxYRHgQUGDYjOJS8Z8WS8ymOGWqNhW5gvV4db7aftp4ulqaBKsNSN5JLNHvSWElHM6ZxDCp0WmXEusicflqyKZ8/640?wx_fmt=jpeg)

**① 今天更新 Vim：CVE-2026-34982 的利用场景在运维人员日常工作中随时发生**

运维人员每天都在用 Vim 查看日志、编辑配置文件，这恰好是攻击者投放恶意文件最容易混入的场景。今天更新 Vim 只需 60 秒：在 Linux 上执行 `sudo apt update && sudo apt upgrade vim`（或对应包管理器命令），在 macOS 上执行 `brew upgrade vim`。如果有服务器无法立即升级，临时缓解措施是在 Vim 配置中禁用 modeline：在 `.vimrc` 中添加 `set nomodeline`。这一行配置可以今天完成，不影响任何正常使用。

**② 今天向团队宣布一条新规则：不得用 Vim/任何文本编辑器打开来源不明的文件**

CVE-2026-34982 的根本利用场景是"受信任的工具 + 不可信的文件"。除了打补丁，今天可以在团队中建立一条操作规范：任何通过邮件、即时通讯、外部系统接收到的文本文件，在确认来源可信之前，不得在服务器上直接用编辑器打开——可以先在隔离环境中查看文件的十六进制内容，或使用 `cat`/`head` 等只读命令初步检查后再决定是否进一步操作。这条规则零成本，今天就可以执行。

**③ 重新评估 AI Agent 的权限边界：今天是"清算日"**

Vertex AI "double agent" 风险、OpenClaw RCE、Claude Code 发现 0Day 这三件事合在一起说明了同一件事：**AI Agent 的权限越高，其被滥用时的破坏力越大，其自身的安全缺陷也越危险**。今天建议针对企业内部所有已部署的 AI Agent 工具做一次权限审计：（1）列出每个 AI Agent 拥有哪些系统权限；（2）核查是否存在"最小权限原则"违反；（3）确认每个高权限操作是否都有人工审批节点。这不是"未来要做"的事情，而是今天已经迫切需要完成的安全基线工作。

---

*数据来源：安全客 · FreeBuf · 嘶吼 · 安全牛 · 先知安全 · Seebug Paper · unSafe.sh · CNVD · CNNVD*
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