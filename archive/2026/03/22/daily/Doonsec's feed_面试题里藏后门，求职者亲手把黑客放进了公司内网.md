---
title: 面试题里藏后门，求职者亲手把黑客放进了公司内网
url: https://mp.weixin.qq.com/s/yTHVp6bfeCnelKlQGBdXfw
source: Doonsec's feed
date: 2026-03-22
fetch_date: 2026-03-23T04:23:15.720773
---

# 面试题里藏后门，求职者亲手把黑客放进了公司内网

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkibRne4PtDo0KpicVH3dMOEDuhz5Rx6kGmiaAeFGKKU561qX3YF3H9qlJKoud8T7ngX0GyhNa1uichEhicMfd7xfFdH2OdOLIN7BETM/0?wx_fmt=jpeg)

# 面试题里藏后门，求职者亲手把黑客放进了公司内网

原创

数据安全合规交流部落
数据安全合规交流部落

数据安全合规交流部落

![]()

在小说阅读器中沉浸阅读

# 假面试真入侵：Next.js招聘题暗藏后门，开发者设备成黑客跳板

**2026年03月22日**

---

攻击者把猎场搬到了招聘市场——伪造Next.js技术面试题，让求职者亲手在自己电脑上运行后门程序。与此同时，一个被红队秘密使用了14个月的Windows提权漏洞RegPwn终于在本月补丁日公开，存量未修复机器正面临被批量利用的风险。国内方面，AI系统漏洞数量持续攀升，CNNVD本周期共披露重要AI漏洞155个，Langflow与OpenClaw均在列。今天的威胁，比昨天更精准，也更难防。

---

## 🔴 重大事件

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKkicqlEicH7XMmic1ibPf65yGyUWfcPG3DPpLSyxWJnX8BMKIQZibeQu3jPep4eDTWKm7uqN3UNrPhiaGsibOBGPnJZiaLxDFF21DKSTicSI/640?wx_fmt=jpeg)

**假招聘真投毒：Next.js面试题内置后门，开发者设备遭RCE攻击**

攻击者伪造Next.js开发项目与技术测评题，以招聘面试为掩护发给开发者，诱导其在本地运行含有后门的代码仓库，实现远程代码执行（RCE）、敏感数据窃取并在沦陷设备上部署二级载荷。微软Defender安全团队已确认该攻击活动，目标群体集中于软件开发者——这一人群往往拥有代码仓库写权限和云平台密钥，是高价值渗透目标。**严禁在个人或企业设备上直接运行来路不明的面试题代码，务必在隔离沙箱环境中操作。**
（来源：嘶吼）

---

**酒店偷拍泛滥成灾：180余家酒店被发现安装摄像设备，视频遭倒卖与勒索**

据报道，国内多地酒店客房内被安装偷拍设备的事件持续曝光，目前已有超过180家酒店被证实存在此类问题。受害者在毫不知情的情况下遭到拍摄，相关视频被非法倒卖至网络平台，部分受害者还遭到以视频为把柄的勒索，涉案金额高达3万元。深圳多个区已相继发生此类案件，香港游客也受到波及。这一事件本质上是个人隐私数据的物理层面泄露，触犯了《个人信息保护法》关于图像采集与传播的核心条款。
（来源：嘶吼）

---

**虚假OpenClaw安装程序传播GhostSocks恶意软件，信息窃取链路完整曝光**

安全研究人员披露：攻击者通过伪造OpenClaw工具安装程序，在用户下载安装过程中植入 **GhostSocks** 信息窃取型恶意软件，可完整窃取浏览器凭据、会话Cookie与本地敏感文件。GhostSocks被用作更大规模攻击的初始访问途径，此前已有类似模式导致Snowflake客户数据库大规模泄露。**下载任何安全工具时务必验证官方渠道与哈希值，切勿通过搜索引擎广告或非官方链接获取安装包。**
（来源：Seebug Paper）

---

**伊朗背景黑客对医疗科技巨头Stryker实施Wiper攻击，爱尔兰中心被迫停工**

与伊朗情报机构有关联的黑客组织宣称对全球医疗技术企业Stryker发动数据清除攻击（Wiper Attack），致使Stryker最大的美国境外运营中心——爱尔兰工厂员工被迫提前离岗，相关系统遭到永久性破坏。Wiper攻击不以数据获利为目的，而是彻底摧毁系统可用性，恢复成本极高、周期极长，医疗行业已成国家级攻击者的核心打击目标。
（来源：Krebs on Security）

---

## 🟠 高危漏洞披露

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKkicVKOp0YtpRPx8NolCGaYWIn0gGziapiaiaUXFKXXXdX1XVwngFA0RLu9opc41tb0nDXEvHA8LYiacIfPKx2qUNNLTfVYGTiatT53oc/640?wx_fmt=jpeg)

**Windows权限提升漏洞RegPwn（CVE-2026-24291）复现分析：红队秘用14个月才上报**

由英国MDSecLabs研究员Filip Dragovic发现的Windows权限提升漏洞"RegPwn"已在本月补丁日完成修复。该漏洞设计极为精巧——攻击者在2025年1月即开始在红队评估中实战使用，**整整14个月后**才于2026年2月报告给微软。漏洞通过注册表操作实现本地权限提升，利用成本极低，目前已有完整复现分析公开，意味着大量攻击者将快速跟进。未部署3月补丁的Windows环境请今日内完成更新。
（来源：先知安全）

---

**PyTorch反序列化RCE漏洞曝光：torch.export.load存在隐藏代码执行风险**

流行深度学习框架PyTorch的 `torch.export.load` 接口被发现存在**反序列化远程代码执行漏洞**，攻击者可通过构造恶意模型文件，在目标加载时触发任意代码执行。AI模型文件（.pt/.pth）正被大量在研究机构和企业间流转分享，此漏洞使得"加载一个模型"等同于"执行一段任意代码"。建议所有使用PyTorch的团队立即审查模型来源，仅加载可信渠道的模型文件，并关注官方补丁动态。
（来源：先知安全）

---

**CNNVD披露Langflow安全漏洞（CVE-2026-27966），AI工作流平台认证缺失**

国家信息安全漏洞库（CNNVD）正式通报Langflow安全漏洞（CNNVD-202602-4530，CVE-2026-27966），漏洞成因为身份认证缺失，攻击者可未授权访问核心API接口。此前国际媒体已报告该漏洞在披露后**20小时内**即遭真实攻击利用。国内部署了Langflow的AI应用平台应立即核查版本并完成修复。
（来源：CNNVD安全动态）

---

**CNVD第10期周报：本周收录漏洞660个，高危漏洞占比近六成**

国家信息安全漏洞共享平台（CNVD）发布2026年第10期周报，本周共收录漏洞**660个**，其中高危漏洞**379个**（占比57.4%）、中危漏洞248个、低危漏洞33个。高危漏洞数量居高不下，企业安全团队需持续跟踪CNVD通报，及时评估资产暴露面。
（来源：CNVD漏洞平台）

---

**AI重要漏洞第三期通报：3月4日至19日共采集AI漏洞155个**

CNNVD发布2026年第三期人工智能重要漏洞通报，统计时间段为2026年3月4日至3月19日，共采集重要AI漏洞**155个**。AI系统漏洞数量持续高位，涉及大模型、推理框架、AI工具链等多个层面，显示AI基础设施的安全成熟度与其商业化速度之间存在显著差距。
（来源：CNNVD安全动态）

---

**仿冒谷歌账号钓鱼攻击：恶意PWA应用窃取验证码与加密货币钱包**

攻击者伪造谷歌账号安全页面，通过PWA（渐进式Web应用）技术分发恶意程序，可实时窃取一次性验证码（OTP）、采集加密货币钱包地址，并将受害者浏览器沦为攻击者的流量转发代理。PWA无需应用商店审核即可安装，且外观与原生App高度相似，极具欺骗性。使用域名 `google-prism[.]com` 实施伪装，用户须警惕任何要求授权"增强安全保护"的弹窗提示。
（来源：嘶吼）

---

**ClickFix攻击携MacSync恶意软件瞄准开发者，伪造Claude钓鱼页面广泛传播**

攻击活动利用"ClickFix"社会工程学技术，伪造Claude AI界面诱导用户执行剪贴板命令，最终投递**MacSync**恶意软件，针对macOS开发者环境实施数据窃取与持久化控制。Claude的品牌公信力被攻击者刻意利用，开发者和IT人员需对任何要求在终端粘贴运行命令的网页保持高度警惕。
（来源：安全牛）

---

**提示词注入绕过AI Webshell检测：安全防护与攻击技术同步升级**

研究人员披露：通过将恶意指令隐藏于代码注释或元数据中，可系统性绕过基于AI语义分析的Webshell检测工具，原因在于AI模型将代码逻辑与注释置于同一语义空间推理。这一研究揭示了AI安全工具自身存在的本质性弱点——防御AI被攻击的同时，AI防御工具本身也可以被攻击。
（来源：先知安全）

---

## 🟡 合规与处罚

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKkicSAaghWfRUFWx8EgCCvibk0FplaszMHHibxImqYicqIl1PWibyhaK8ibBhH0HXOpNGAgzGO2JovEzq4q6v4ic7SbRPmNhrnbDic4TrlM/640?wx_fmt=jpeg)

**工信部通报思科Catalyst SDWAN高危漏洞，已遭境外黑产实战利用**

工信部正式通报思科企业SD-WAN管理软件存在权限提升、文件覆盖等多项高危漏洞，并明确指出该漏洞**已遭境外黑产实战利用**，要求政企单位紧急加固。CNNVD同步发布关于Cisco Catalyst SD-WAN Manager和Controller授权问题漏洞（CVE-2026-20127）的详细通报，建议受影响机构优先部署官方补丁并临时限制管理接口暴露。
（来源：嘶吼 / CNNVD安全动态）

---

**CNNVD通报OpenClaw多个安全漏洞：2026年1月至3月共采集82个**

国家信息安全漏洞库（CNNVD）通报，自2026年1月至3月9日，共采集**OpenClaw安全漏洞82个**，涉及AI助手框架的多个组件，类型包括认证缺陷、权限控制不当及输入验证不足等。AI工具平台的安全基线建设亟待提速。
（来源：CNNVD安全动态）

---

**国家安全部提示：无线设备暗藏泄密风险，勿让蓝牙Wi-Fi"出卖"你**

国家安全部发布安全提示，警示无线设备（蓝牙、Wi-Fi）在特定场景下存在被境外情报机构利用的泄密隐患，呼吁涉密场合关闭无线功能，并通过12339举报线索。企业安全管理规范应纳入涉密区域无线设备管控要求。
（来源：安全牛）

---

**中央网信办召开会议传达学习2026年全国两会精神，数字安全被重点强调**

中央网信办组织召开专题会议，传达学习2026年全国两会精神，将数字安全、数据安全与网络强国战略作为重点工作方向，预计后续将有更多配套监管政策落地。
（来源：安全牛）

---

## 🌐 国际动态

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XfaKEJuIKk8FAFDAl0FDicNueaTddH5USFep5MxsAKibxjHTbA0M6l4wiaUZLLnGFhLHhbDhrhI2WVu01P5y0fvjm4Q05tSkBJPFZaC1eeLfZw/640?wx_fmt=jpeg)

**AI赋能下的勒索软件威胁演进：低技能团伙正实施高水准攻击**

安全牛发布《2025年勒索软件态势复盘与2026年防御展望》，核心判断是：生成式AI虽未实现攻击全面自动化，但已从根本上重塑攻击成本结构——低技能攻击团伙借助AI工具可实施高水准精准攻击，而高端组织则实现了攻击效率、强度与精准度的全面提升。2026年勒索软件将更难被传统特征检测识别。
（来源：安全牛）

---

**Kimwolf僵尸网络主脑"Dort"身份被完整还原，三国联合瓦解C2基础设施**

Krebs on Security详细披露Kimwolf僵尸网络核心操控者"Dort"的身份画像，此人长期控制超过300万台IoT设备发动大规模DDoS攻击并以此勒索企业。目前美德加三国联合行动已摧毁其C2基础设施，但残余节点仍需持续监控。
（来源：Krebs on Security）

---

**以色列官方安全App"红警"被仿冒，战争焦虑成社会工程学武器**

攻击者伪装成官方机构，以"紧急战时更新"为名通过短信钓鱼（Smishing）诱导以色列用户下载假冒Red Alert APK，实际为间谍软件。战争焦虑与紧迫感被刻意利用于降低用户的安全判断能力——这一模式可复制到任何存在社会情绪的场景，包括自然灾害、疫情等突发事件期间。
（来源：安全牛）

---

## 💡 今日安全建议

![](https://mmbiz.qpic.cn/mmbiz_jpg/XfaKEJuIKk8QETiaETTLUzQNbIKsHgZNn9ibUALAZCRkKRYRLOV7OTltNz3VhNUq4a8BjDlv0HzxnWzwnx5icEpeFUoAXobrh7YAicmF1parEyI/640?wx_fmt=jpeg)

**① 严格隔离运行外部代码，尤其是招聘/测评场景**
针对开发者的面试题投毒攻击正在规模化，任何外部来源的代码项目（包括面试题、开源代码示例）都应在**独立虚拟机或容器沙箱**中运行，切勿在个人工作机或公司内网设备上直接执行。

**② 今日内完成Windows 3月补丁更新，重点覆盖RegPwn漏洞**
CVE-2026-24291（RegPwn）已有完整复现分析公开，被大规模利用只是时间问题。内网Windows设备尤其是特权主机（域控、跳板机、开发服务器）应优先完成本月补丁部署，并检查是否存在异常注册表操作记录。

**③ 全面审查AI工具链的供应来源与安全配置**
PyTorch模型文件RCE、Langflow认证缺失、OpenClaw多漏洞——AI基础设施的安全债务正在集中爆发。建议安全团队对照CNNVD最新AI漏洞通报，逐项评估企业内部AI工具的版本状态、访问控制与模型来源可信度，避免成为AI供应链攻击的突破口。

---

*数据来源：安全客 · FreeBuf · 嘶吼 · 安全牛 · 先知安全 · Seebug Paper · CNVD · CNNVD · Krebs on Security*
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