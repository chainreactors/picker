---
title: Adobe外包商被黑泄露1300万份工单，你发给客服的系统截图和密码已经不安全了
url: https://mp.weixin.qq.com/s/XmUbnn0aF9iAVZG5hEJr2Q
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:36:35.735512
---

# Adobe外包商被黑泄露1300万份工单，你发给客服的系统截图和密码已经不安全了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk99nMic0r4aWa5BEj7wEic5XYZbGZjZekpichtI2470BWRxpeQ4V1YIZuknEq5aEr6cLiaYFOYTknGp9eYE8HoN3HeAcVxwUHY8SP0/0?wx_fmt=jpeg)

# Adobe外包商被黑泄露1300万份工单，你发给客服的系统截图和密码已经不安全了

数据安全研究组
数据安全研究组

数据安全合规交流部落

![]()

在小说阅读器中沉浸阅读

# Adobe泄露1300万份客户工单，Chrome 0Day同日遭野外利用，今天有两件事必须做

**2026年04月04日**

---

**Adobe** 数据泄露事件震动企业安全圈：攻击者宣称通过入侵 Adobe 外包商，成功窃取 **1300 万份**客户支持工单及员工内部记录，客户姓名、邮件地址、企业信息、产品许可证数据全部暴露——波及范围直指全球每一家使用 Adobe 企业版产品的组织。与此同时，谷歌紧急发布 Chrome 安全更新，修复 **21 项高危漏洞**，其中包含已被攻击者在野实际利用的 0Day；而电商平台 Magento 的 **PolyShell** 未授权 RCE 漏洞完整攻击链已在地下黑产圈流通，自动化批量扫描爆破随时可能全面爆发。今天是周末，但今天有两件事不能等到周一：更新 Chrome，检查 Magento。

---

## 🔴 重大事件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKk9ZPFGH5daA2L2qIoEjL0D5JjcBnqiciagicd8fra0AdIdNE9vw21rIWGOKlIQ6QoaJDicvZD4sNLjwfOajVVThfGgPFknRewlZNpo/640?wx_fmt=jpeg)

**Adobe 数据泄露：攻击者入侵外包商窃取 1300 万份支持工单，波及全球企业用户**

FreeBuf 报道，攻击者公开宣称成功入侵 **Adobe 外包商系统**，获取 **1300 万份**客户支持工单及员工内部记录。泄露数据包含：客户姓名、企业邮件地址、公司名称、所购买的 Adobe 产品与授权信息、支持工单的历史沟通内容。Adobe 的企业客户遍及全球——几乎所有中大型企业都在使用 Adobe Acrobat、Creative Cloud、Experience Cloud 或 Sign，这意味着此次泄露的影响范围极难评估上限。支持工单中往往包含系统配置信息、错误日志、截图等高度敏感的技术细节，是攻击者实施定向钓鱼和社会工程学攻击的完美素材。**Adobe 企业版用户今日应密切关注 Adobe 官方安全公告，并对所有与 Adobe 客服沟通时披露的内部系统信息进行风险评估。**
（来源：FreeBuf）

---

**三部委联合专项行动打响：网信办 + 工信部 + 公安部同步整治 App 违规收集个人信息**

嘶吼报道，**中央网信办、工信部、公安部**三部门联合启动 **2026 年个人信息保护系列专项行动**，重点整治：超范围收集个人信息、强制授权、未告知用户等违规行为，覆盖教育、金融、医疗等重点领域。同步，公安部通报新一批 **37 款**违规 APP，违规行为集中在非必要权限索取和数据境外传输。此次三部委联动信号明确：个人信息保护执法正从"通报警示"进入"系统性专项整治"阶段，企业合规容错空间大幅收窄。**仍未完成 App 个人信息保护合规整改的企业，应将此作为本季度最高优先级合规任务立即启动。**
（来源：嘶吼）

---

**CNNVD OpenClaw 专项通报：2026 年 3 月 10 日至 4 月 2 日，累计采集漏洞数量达 155 个**

CNNVD 最新发布 OpenClaw 专项漏洞通报，统计周期 **2026 年 3 月 10 日至 4 月 2 日**，仅 23 天内累计采集 OpenClaw 相关重要漏洞 **155 个**，与此前 1 月至 3 月 9 日的 82 个相比，速度显著加快。这一数据折射出 AI Agent 安全研究的爆发式增长——随着 OpenClaw 用户基数突破 10 万，安全研究人员与攻击者同步加大了对这一高权限 AI 框架的挖掘投入。**仍在运行 OpenClaw 的机构，今日应完成最新版本核查与官方安全公告的订阅。**
（来源：CNNVD）

---

## 🟠 高危漏洞披露

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkicnpvbP39AcJIa9MHCBxNWRicq6r62c2qvclLapWR682BSoVmwBMpoGLe8PpYghoQ740qHF42xVlKA7ZuL2giaI4NsmSvNBlYFw8/640?wx_fmt=jpeg)

**Chrome 0Day 已在野外被实际利用：谷歌紧急发布修复 21 个高危漏洞的安全更新**

FreeBuf 早报报道，谷歌紧急发布 Chrome 安全更新，修复 **21 项高危安全漏洞**，其中包含已被攻击者**在野实际利用**的 0Day 漏洞。Chrome 浏览器的在野利用 0Day 是所有漏洞类别中修复优先级最高的一类，因为攻击者通常通过恶意网页实施"无文件驱动式下载"攻击，用户仅需访问被控制的网页即可触发漏洞，无需任何点击或文件操作。**今日立即更新 Chrome：菜单 → 帮助 → 关于 Google Chrome → 等待更新完成 → 重启浏览器。此操作需要今天完成，不接受任何理由的延迟。**
（来源：FreeBuf）

---

**PolyShell 高危漏洞：Magento/Adobe Commerce 无授权 RCE，完整攻击链已在黑产圈流通**

嘶吼报道，新型高危漏洞 **PolyShell** 影响所有 **Magento 开源版**与 **Adobe Commerce 2.x** 系列，攻击者无需任何身份认证即可远程执行恶意代码、窃取并接管管理员账号。关键危险信号：Sansec 紧急预警，**完整漏洞攻击利用链已在地下黑产圈层流通扩散**，自动化批量扫描爆破攻击或将很快全面爆发。Adobe 官方虽已推送修复补丁，但该补丁仅内嵌于 **2.4.9 Alpha 测试版**，正式商用稳定版暂未更新，**全网大量在线运营商城目前仍处于无防护状态**。这是当前最紧迫的待修复漏洞之一，对于无法立即升级的商城，今日必须部署 WAF 规则进行临时阻断。
（来源：嘶吼）

---

**GNU InetUtils Telnetd CVE-2026-24061：CVSS 9.8 满分级远程认证绕过，PoC 已公开**

绿盟 CERT 通报 **CVE-2026-24061**，GNU InetUtils Telnetd 组件存在远程身份验证绕过漏洞，CVSS 评分 **9.8**，漏洞细节与 PoC 已完全公开。Telnetd 虽是较为老旧的协议服务，但在工控系统、旧版嵌入式设备、内网管理系统中仍有大量残留部署。CVSS 9.8 + PoC 公开的组合意味着此漏洞已进入"可无门槛批量利用"阶段。**今日应排查内部网络中所有运行 Telnetd 服务的设备，优先关闭或限制访问，并按照 GNU 官方公告完成修复。**
（来源：绿盟 CERT）

---

**Ally WordPress 插件高危 SQL 注入：40 万网站面临数据库拖库风险**

安全客报道，**Ally WordPress 插件**存在高危 SQL 注入漏洞，攻击者可通过构造恶意请求直接访问并提取网站数据库内容，受影响网站超过 **40 万个**。WordPress 插件漏洞的利用通常通过自动化扫描工具大规模实施，40 万的受影响规模意味着漏洞公开后短时间内即会出现批量利用。**使用 Ally 插件的 WordPress 站点应立即在后台检查插件更新，若无可用更新，应临时停用该插件直至官方修复版本发布。**
（来源：安全客）

---

**Apifox 供应链投毒持续跟踪：绿盟 CERT 完整分析报告，影响范围再确认**

绿盟 CERT 发布 Apifox 桌面客户端供应链投毒完整分析报告，确认官方 CDN 托管前端 JS 文件被植入多重混淆恶意脚本，客户端启动后自动加载并最终实现 RCE。影响范围持续确认中，所有 Apifox 桌面客户端用户应完成主机安全排查（重点排查异常进程、网络连接、新增文件），并等待官方明确安全版本公告后再恢复使用。
（来源：绿盟 CERT）

---

## 🟡 合规与监管动态

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk8LKH3IkWBsIQz3Vt40lI7vjX2An3PS9OwCia3QhtOiaLVByfp6oHlcLLTbhKfuhBylWe5PFJAo8ILZnwvJLgrPibPicE3L7CM1WKY/640?wx_fmt=jpeg)

**国家计算机病毒应急处理中心通报 13 类个人信息违规行为：超范围收集与强制授权首当其冲**

安全牛报道，国家计算机病毒应急处理中心集中通报 **13 类**个人信息违规行为类型，为企业 App 合规提供了最新执法口径参考。重点违规类型包括：超范围收集与业务无关的个人信息、设置"不授权则无法使用"的强制授权机制、未向用户充分告知数据处理目的与范围。结合三部委专项行动的启动，此次通报的意义在于清晰划定了执法标准，为企业自查提供了明确对照清单。
（来源：安全牛）

---

**CNNVD 漏洞周报第 13 期：AI 与 WordPress 双双成为本周漏洞重灾区**

安全牛报道，CNNVD 2026 年第 13 期漏洞周报（3 月 23 日至 3 月 29 日）将 **AI 框架**与 **WordPress 生态**列为本周漏洞重灾区。AI 漏洞以 Langflow、OpenClaw 等框架为主，WordPress 漏洞以 Ally 等插件为代表。两类技术栈的共同特点：用户基数庞大、安全意识相对薄弱、版本更新率低。
（来源：安全牛）

---

## 🌐 国际动态

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKk90HmJUIqb0psPGcw2IqHdZuEvZc92Z0S4rS6k9E9mn87bsGzRc56hJVv908pAwa4EXFBGicOeFax1D9Ug45qibT8JgJwG6ibgE4c/640?wx_fmt=jpeg)

**谷歌正式将 Axios npm 供应链攻击归因于朝鲜 APT 组织：国家级黑客瞄准开源生态**

FreeBuf 早报报道，谷歌威胁情报团队正式对外公布溯源结论，确认 axios npm 供应链投毒事件由**朝鲜国家级 APT 组织**主导实施。这是继 npm 生态多次遭受朝鲜黑客攻击之后，谷歌首次对此类事件进行正式公开归因。朝鲜黑客的开源生态攻击策略已从"偶发性尝试"演变为"系统性产业链"，开发者工具供应链是当前国家级攻击者最活跃的攻击面之一。
（来源：FreeBuf）

---

## 💡 今日安全建议

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk8YiaCLsEFeA5jxYRHgQUGDYjOJS8Z8WS8ymOGWqNhW5gvV4db7aftp4ulqaBKsNSN5JLNHvSWElHM6ZxDCp0WmXEusicflqyKZ8/640?wx_fmt=jpeg)

**① 今天有一个必须做的操作：打开 Chrome 更新**

Chrome 0Day 在野利用意味着此刻互联网上已有被控制的网页在等待未打补丁的用户访问。打开 Chrome → 右上角三点菜单 → 帮助 → 关于 Google Chrome → 等待更新安装 → 点击重新启动。这个操作需要 3 分钟，但它可以防止你的设备成为被利用的目标。今天在工作群或家人群里发这条提醒，你的同事和家人也需要做同样的操作。

**② 电商负责人今天必须核查 Magento 版本——PolyShell 攻击链已在黑产流通**

PolyShell 的危险不在于"可能被利用"，而在于"完整攻击链已流入地下市场"——这意味着会使用 Sqlmap 的初级黑客都可以发起攻击。如果你们的商城使用 Magento 或 Adobe Commerce：（1）立即确认当前版本；（2）如果无法立即升级到 2.4.9，今天部署 WAF 规则临时阻断；（3）检查管理员账号是否有异常登录记录。这三步今天都可以完成，不需要等到工作日。

**③ Adobe 企业用户今天做一件小事：检查有无可疑的 Adobe 主题钓鱼邮件**

1300 万份支持工单的泄露意味着攻击者已掌握大量企业的产品使用信息，下一步必然是定向仿冒 Adobe 客服发送针对性钓鱼邮件。今天建议在企业内部发出提醒：未来一段时间内收到任何以"Adobe 支持"、"Adobe 许可证"、"Adobe 安全通知"为主题的邮件，在核实官方域名之前不要点击任何链接，不要输入任何账号密码。仿冒邮件往往在数据泄露后的 72 小时内开始出现。

---

*数据来源：安全客 · FreeBuf · 嘶吼 · 安全牛 · 先知安全 · Seebug Paper · 绿盟 CERT · CNVD · CNNVD*
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