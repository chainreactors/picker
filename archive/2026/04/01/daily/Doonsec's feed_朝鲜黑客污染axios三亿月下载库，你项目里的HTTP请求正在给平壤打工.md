---
title: 朝鲜黑客污染axios三亿月下载库，你项目里的HTTP请求正在给平壤打工
url: https://mp.weixin.qq.com/s/iOA2mWVxLnPVfZdTNrCnoQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:22:33.631319
---

# 朝鲜黑客污染axios三亿月下载库，你项目里的HTTP请求正在给平壤打工

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKk9BbPB1xcgUxaQemM7QnemqB68wWr249x1koQHwBlLBXhBHtut8oNheWYLmJVYC7baTEDplgXDtdUJSEfEaaNJVyoichlFc4jz0/0?wx_fmt=jpeg)

# 朝鲜黑客污染axios三亿月下载库，你项目里的HTTP请求正在给平壤打工

数据安全研究组
数据安全研究组

数据安全合规交流部落

![]()

在小说阅读器中沉浸阅读

# 朝鲜黑客污染axios三亿月下载库，思科300余个代码仓库遭Trivy供应链攻击殃及

**2026年04月01日**

---

四月的第一天，供应链攻击的多米诺骨牌继续倒下。谷歌溯源确认，**axios**——月下载量 **3 亿次**的顶级 npm 开源库——遭朝鲜黑客组织 **UNC1069** 供应链投毒，目标直指窃取加密钱包；而 **TeamPCP** 对 Trivy 的攻击已进一步扩散，**思科 300 余个代码仓库被批量克隆、凭证大规模泄露**，目前正在紧急轮换所有受影响凭据。与此同时，月活安装超 **90 万次**的恶意 AI 浏览器扩展正悄然潜伏在 **2 万家企业**内部网络中实施窃密。这不是某一次单点失陷，而是整个软件供应链信任体系的系统性崩塌。

---

## 🔴 重大事件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkic7JDKsOLibK0DloOnLkp0kvmnicgVDvALgXwcvHeCp7t3glI1zU4WNSvCR5HpR0x1SicQUUoNZkdMBD60Q4heuvAartdcu7Mbia5Y/640?wx_fmt=jpeg)

**谷歌溯源确认：朝鲜黑客 UNC1069 污染 axios 两个版本，月下载 3 亿次 npm 库成窃密武器**

unSafe.sh 报道，谷歌威胁情报团队完成溯源分析，确认对 axios 开源库实施供应链投毒的攻击者为朝鲜国家级黑客团伙 **UNC1069**。攻击者通过劫持 axios 核心维护者账号发布含后门的恶意版本，植入名为 **WAVESHAPER.V2** 的后门程序，可收集系统信息、执行远程命令，并以窃取**加密货币钱包**为终极目标。axios 每月下载量高达 **3 亿次**，是全球 Node.js 生态最核心的 HTTP 客户端库之一，几乎所有 JavaScript/TypeScript 项目都有直接或间接依赖。**今日必做：立即执行 `npm list axios` 核查项目中 axios 的确切版本，锁定至官方确认安全的版本，并对 CI/CD 流水线中的 npm 安装步骤增加 lock file 强制校验。**
（来源：unSafe.sh）

---

**Trivy 供应链攻击扩散至思科：300+ 代码仓库被克隆，内部凭证大规模泄露，紧急轮换进行中**

unSafe.sh 披露，TeamPCP 对 Trivy 的供应链攻击持续扩散，**思科**已成为最高级别受害企业：攻击者通过 Trivy 投毒链入侵思科内部系统，成功克隆 **300 余个内部项目仓库**，多个凭据遭到窃取。思科目前正在进行**大规模凭证轮换**应急操作，受影响范围涵盖企业内部产品及部分美国政府机构客户项目的源代码。嘶吼同步报道，TeamPCP 还进一步篡改了 Aqua Security 的 Docker Hub 官方镜像仓库，将污染范围从 GitHub Actions 扩展至 Docker 镜像生态。**所有正在使用 Trivy 相关 Docker 镜像或 GitHub Actions 的团队，今日应立即核查镜像和 Action 的哈希完整性。**
（来源：unSafe.sh / 嘶吼）

---

**恶意 AI 助手浏览器扩展：超 90 万次安装、2 万家企业中招，窃密工具伪装成 AI 生产力工具**

安全牛独家报道，一款以"AI 侧边栏助手"形态出现的浏览器扩展程序，已累计完成超 **90 万次**安装，其中受害企业用户规模超过 **2 万家**。该扩展外观与功能上与正规 AI 助手几乎无法区分，但实际上持续在后台窃取：浏览器中的 Cookie 与会话令牌、用户访问的所有业务系统 URL 及内容、表单中输入的账号密码。由于扩展程序安装通常不在企业安全管控视野内，此类威胁在绝大多数企业中处于"已中招但完全不知情"的状态。**今日建议：立即在全员中发起浏览器扩展审计，所有未经 IT 部门审批的扩展一律禁用或卸载。**
（来源：安全牛）

---

**劳埃德银行软件更新故障致 45 万用户数据互串：国民保险号码、交易记录遭错误泄露**

unSafe.sh 报道，英国劳埃德银行因 3 月 12 日的一次**软件更新故障**，导致近 **45 万**手机银行用户的交易数据被错误展示给其他用户，泄露内容包括交易金额、日期及**国民保险号码**等高敏感信息。银行官方声明账户余额与资金转移未受影响，部分受影响用户已获补偿。此事件再次印证：软件更新引发的数据隔离失效，是金融机构数据泄露最高频的"非攻击型"触发因素，且往往在大量用户受影响后才被发现。
（来源：unSafe.sh）

---

**Claude Code 源代码泄露：Anthropic 员工操作失误，AI Agent 时代的前端配置安全危机**

FreeBuf 双篇报道揭示，**Claude Code** 源代码泄露事件本质是一类前端与 DevOps 配置失误——Anthropic 员工操作失误导致代码仓库配置不当，使得本不应公开的源码内容暴露。技术复盘指出，这并非模型本身被攻破，而是"AI 编程 Agent 工具放大了开发者的配置失误"——使用 Claude Code 等 AI Agent 进行自动化开发时，AI 工具会主动修改项目配置，而开发者对这些变更的审查往往流于形式。泄露的源代码可能被攻击者用于逆向分析潜在漏洞，进而针对使用 Claude Code 的企业用户发动精准攻击。
（来源：FreeBuf）

---

**71 款 APP 违规收集个人信息被点名：泡泡玛特、丝芙兰等知名品牌在列**

嘶吼报道，国家计算机病毒应急处理中心依据《网络安全法》《个人信息保护法》等法律法规，通报 **71 款移动应用**存在违法违规收集使用个人信息情况，被点名企业包括**泡泡玛特、丝芙兰**等消费者广泛使用的知名品牌。违规行为包括超范围收集、未经授权获取设备信息、强制索要非必要权限等高频违规类型。**建议企业 IT 与合规团队立即对所有内部运营的 APP 进行个人信息收集合规自查，避免成为下一期通报对象。**
（来源：嘶吼）

---

## 🟠 高危漏洞披露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKk8lfW1B1lGibsd9su7BhdQ4TNFpBQCibE8n0Ww7aEQj9qWjmBtxskxnjUPWJxt12VqP4VaT90Ov2s8BqgzAxtTUMUWC6aopCWANk/640?wx_fmt=jpeg)

**VoidStealer 绕过 Chrome ABE 防护机制：利用调试器硬件断点直接从内存提取主密钥**

嘶吼披露，新型窃密恶意软件 **VoidStealer** 采用全球首创的技术手段：利用**硬件断点**（调试器功能）直接从 Chrome 浏览器运行内存中读取明文状态的 **v20\_master\_key** 主密钥，完整绕过谷歌 Chrome 127 版本引入的\*\*应用程序绑定加密（ABE）\*\*防护机制。Gen Digital（诺顿、Avast、AVG、Avira 母公司）发布专项报告确认，这是全球野外实战中首例采用该底层绕过机制的窃密恶意软件。一旦主密钥被提取，浏览器中保存的所有密码、Cookie、信用卡信息全部暴露。
（来源：嘶吼）

---

**OpenClaw 提示词注入：一个恶意网页即可实现主机 RCE，多层静态防护被逐步绕过**

先知安全与嘶吼双平台发布 OpenClaw 提示词注入漏洞研究，揭示高权限 AI Agent 面临的根本性安全困境：攻击者通过精心构造的**多阶段诱导策略**（利用长上下文认知负载和任务导向性），可逐步使 OpenClaw 忽略安全边界，最终在用户主机上执行**任意系统命令**。OpenClaw 拥有操作本地文件、执行系统命令、联网访问等高权限，其引以为傲的"边界标记封装"防护机制在特定诱导路径下被成功绕过。蚂蚁 AI 实验室同期报告发现 OpenClaw **1 个严重漏洞 + 4 个高危漏洞**，普通账号可提权接管智能体并读取本地敏感文件，官方已紧急修复。
（来源：先知安全 / 嘶吼）

---

**OpenAI Codex 严重漏洞：黑客可劫持 GitHub 访问令牌，CI/CD 流水线面临接管风险**

嘶吼报道，OpenAI Codex 被披露存在严重漏洞，攻击者可利用该漏洞**劫持用户的 GitHub 访问令牌**，进而以受害者身份访问所有关联的 GitHub 仓库、触发 Actions 工作流、修改代码内容。在 AI 辅助编程场景中，Codex 与 GitHub 的深度集成使得令牌劫持的影响范围远超传统场景——攻击者可以悄无声息地向代码库注入后门，而代码提交记录显示的仍是受害者本人的账号。
（来源：嘶吼）

---

**DigitalOcean Droplet Agent CVE-2026-24516：预授权命令注入直接 RCE**

先知安全发布 DigitalOcean Droplet Agent 预授权 RCE 漏洞（**CVE-2026-24516**）完整分析，漏洞位于 Droplet Agent 的命令注入处理逻辑中，攻击者无需任何认证即可通过构造特制请求触发命令执行，实现对 DigitalOcean 虚拟机的完整控制。使用 DigitalOcean 云服务的团队应立即核查 Droplet Agent 版本并应用官方补丁。
（来源：先知安全）

---

## 🟡 合规与监管动态

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKk8Capo6EPF6Wia5u6LfxzJKaKnsyqARW9QcQxSY7VJ0FwXkBjDo9RN8hmb7PJtvOEj4jkeIdVs5IuBYp8zpNz7eFo7iaCMudZdCQ/640?wx_fmt=jpeg)

**国安部警示智能穿戴设备泄密风险：军官手表 GPS 数据公开导致军事机密外泄**

嘶吼报道，国家安全部披露具体案例：某国军官使用的**智能手表**因开启了高精度 GPS 轨迹公开记录功能，导致其行动路线数据在运动健康平台上公开可见，进而暴露了敏感军事地点与行动规律。国安部警示：此类事件已在全球多个国家军队中频繁发生，智能穿戴设备的"无感知数据上传"功能是当前最易被忽视的信息安全漏洞之一。对于企业而言，**员工在涉密场所或处理敏感业务时使用智能手表的管控策略亟待建立。**
（来源：嘶吼）

---

**全国网安标委征集个人信息保护标准应用实践案例：合规落地进入"晒成果"阶段**

嘶吼报道，全国网络安全标准化技术委员会发布通知，征集个人信息保护标准（GB/T 35273 等）的应用实践案例，用于标准修订参考与行业示范推广。这一举措标志着个人信息保护标准的推进已从"制定阶段"进入"落地验证阶段"。有条件的企业可以将自身合规建设成果提交参与，既是行业贡献，也是提升企业合规品牌形象的机会。
（来源：嘶吼）

---

## 🌐 国际动态

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkicm8VBPgdtic5iabzpibH6xNMSGoupLDFtTPaQMrjSibWERCIGDh8h9lhtaskAqdLxKGNPnh2pEJrE7BjvxzyUZQwC3G3F9x3iablAc/640?wx_fmt=jpeg)

**RedLine 恶意软件核心开发者被引渡至美国：面临多项重罪指控，最高 30 年监禁**

unSafe.sh 报道，亚美尼亚籍嫌疑人 Hambardzum Minasyan 被成功引渡至美国，面临多项联邦重罪指控，被认定为 **RedLine** 信息窃取恶意软件的关键开发者。RedLine 是近年来危害最广泛的商业化信息窃取器之一，曾被多个国家级 APT 组织用于攻击美国关键基础设施。尽管"Operation Magnus"行动已打击了 RedLine 部分基础设施，但该恶意软件仍在暗网中持续流通使用。
（来源：unSafe.sh）

---

**伊朗黑客组织 Handala 宣称入侵 FBI 局长邮箱：政府高层邮箱成 APT 首要猎物**

安全牛报道，伊朗关联黑客组织 **Handala** 公开宣称已成功入侵 FBI 局长邮箱并获取内部通信内容。无论声明真实性如何，这一事件再次突显政府与执法机构高层邮件账号的极高攻击价值，以及针对性社会工程学攻击与账号接管攻击在 APT 行动中的核心地位。
（来源：安全牛）

---

## 💡 今日安全建议

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk8YiaCLsEFeA5jxYRHgQUGDYjOJS8Z8WS8ymOGWqNhW5gvV4db7aftp4ulqaBKsNSN5JLNHvSWElHM6ZxDCp0WmXEusicflqyKZ8/640?wx_fmt=jpeg)

**① 今天排查供应链风险：axios 和 Trivy 是否出现在你的项目中**

axios 月下载 3 亿次意味着几乎所有 JavaScript 项目都直接或间接依赖它，而 Trivy 则是目前最流行的容器与代码漏洞扫描工具。今天用 30 分钟做两件事：（1）在代码仓库中执行 `npm list axios` 或 `grep -r "axios" package-lock.json`，确认所用版本是否为受污染版本，并立即锁定至官方已确认安全的版本；（2）核查当前 CI/CD 流水线中 Trivy 的 GitHub Action 版本和 Docker 镜像哈希，与官方 Release 进行比对验证。任何一个环节存疑，今天就启动凭证轮换。

**② 今天在全公司发起浏览器扩展清查：90 万次安装的恶意 AI 扩展是警钟**

90 万次安装量意味着在你的公司里很可能有人已经装了这个恶意扩展。建议今天通过企业设备管理平台或直接向员工发起提醒，要求所有人检查并上报当前安装的浏览器扩展列表，IT 团队进行统一审核，凡是未经审批的 AI 助手类扩展一律暂停使用直到完成安全核查。对于有 MDM 管理能力的企业，今天可以推送扩展白名单策略，将浏览器扩展纳入正式安全管控范围。

**③ 高权限 AI Agent 使用规范应该今天写进你的团队操作手册**

OpenClaw/Claude Code 等 AI Agent 的提示词注入与源代码泄露事件共同指向同一个问题：高权限 AI 工具正在以开发者未充分预期的方式扩大攻击面。今天建议为团队建立三条基本规则：（1）AI Agent 不得在生产环境服务器上运行；（2）AI Agent 的文件系统访问范围应限制在工作目录内；（3）AI 生成的任何对外发布内容（配置文件、Dockerfile、CI/CD 脚本）在合并前必须经过人工安全审查。这三条规则写进团队文档，今天就可以完成。

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