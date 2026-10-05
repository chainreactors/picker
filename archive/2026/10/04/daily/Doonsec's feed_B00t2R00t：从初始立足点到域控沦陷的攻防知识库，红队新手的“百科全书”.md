---
title: B00t2R00t：从初始立足点到域控沦陷的攻防知识库，红队新手的“百科全书”
url: https://mp.weixin.qq.com/s/mOuJnPG4MgtZg_B_ykznUw
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:57:07.796453
---

# B00t2R00t：从初始立足点到域控沦陷的攻防知识库，红队新手的“百科全书”

# B00t2R00t：从初始立足点到域控沦陷的攻防知识库，红队新手的“百科全书”

原创

KLSEC
KLSEC

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

你拿到一个授权目标，扫完端口发现开放了445和88，知道这是AD环境。然后呢？

大多数人的下一步是打开浏览器，搜“AD渗透流程”，翻到一篇2022年的博客，里面的工具链接已经404了。再搜一篇，命令参数不全。再搜一篇，写得跟天书一样。

B00t2R00t就是来解决这个问题的。2026年9月25日，H3llKa1ser在GitHub上放出了这个项目。它的自我介绍只有一句话：**“一个全面的攻防知识库——从初始立足点到完整域沦陷。”**

GitHub仓库的README里写得很清楚，这不是一个“工具集”，是一个**按真实攻击杀伤链组织的百科全书**：Enumerate → Exploit → Escalate → Persist。覆盖Active Directory、云、Web、网络、无线和红队操作六大领域。

**一、它怎么组织的：方法论、技术、工具，三层分离**

B00t2R00t的目录结构是它最值得说的设计。

第一层是`Methodology/`，这是“ playbook 层”。当你面对一个不熟悉的目标类型时，先看这里。它告诉你在什么阶段该做什么、按什么顺序做。README里原话是：“New to a target type? Start in Methodology — it's the high-level playbook for what to do and in what order.”

第二层是`Techniques/`，按领域划分：Active Directory、Cloud、Web Applications、Network Services、Wireless、Red Teaming、Privilege Escalation、Pivoting、CVEs、AI Pentesting。每个领域下面是具体的技术页面。

第三层是`Tools/`，工具用法文档和攻击技术**刻意分开**。README里解释了为什么：“Looking for a tool's syntax? Head to Tools — usage docs are separated from techniques on purpose.”

这个三层分离解决了一个真实痛点：你不需要在“理解攻击逻辑”和“查工具参数”之间来回跳。技术页面讲的是“为什么要这么做”，工具页面讲的是“这个命令的每个参数是什么意思”。

**二、AD渗透：从枚举到域控的完整链路**

AD部分是B00t2R00t最厚的一块。覆盖的内容从基础枚举到Kerberos攻击、ADCS、信任关系和持久化。

**枚举阶段**，它给了具体的命令和判断逻辑。比如`pth-smbclient`的用法：`pth-smbclient -U "AD/ADMINISTRATOR%<NT_HASH>" //IP_ADDRESS/SHARE/`，然后`ls`列文件、`cd`进目录、`get`下载、`put`替换文件。这个命令解决的是“拿到NTLM哈希但不知道怎么用”的场景。

**Metasploit的AD模块**被拆成了六个独立页面：Credential Extraction、AD Enumeration、AD Exploitation、Kerberos Tickets、Lateral Movement、Meterpreter Session、AD Persistence。每个页面讲清楚模块的适用场景和参数。

**C2框架**覆盖了Covenant和Villain。Covenant的Post-Exploitation页面给了具体的命令：`SamDump`、`keylogger /time:"120"`、`shellcmd ipconfig/all`、`PortScan /computernames:"IP" /ports:"80,443-445,3389"`。

**Pivoting**部分覆盖了Villain C2的sibling server配置，步骤很具体：`ifconfig`拿网络信息 → 启动第二个Villain实例 → `connect SIBLING_TEAM_SERVER PORT_NUM` → `siblings`验证关系。

**三、云和AI：没有落下新战场**

B00t2R00t没有只写AD。云安全部分覆盖了AWS、Azure、GCP和Kubernetes。

Azure部分包含了**Azure Research Toolkit (ART)** 的用法，以及AzureAD PowerShell模块的链接。Credential Extraction页面专门讲了**Pass-the-PRT**（Primary Refresh Token）的利用方式，这是Azure AD环境中拿到初始立足点后的关键一步。

AI安全部分单独成节，覆盖**提示词注入、越狱逃逸、模型攻击**。Training页面链接了RedAiRange——一个AI红队靶场。Tools页面包含了**CyberStrike AI**的链接，这是2026年开源的一个AI自主渗透测试平台。

**四、后渗透和提权：Linux、Windows、Docker**

提权部分按操作系统分开。Linux提权页面里有一个具体案例：**Tmux会话劫持**。前提条件是“Session is run as root and our user has access to it”，利用命令是`tmux -S /SOCKET-PATH attach -t SESSION_NAME`。这是一个容易被忽略的提权路径——很多运维人员用root跑tmux会话，但忘了限制会话的访问权限。

Windows提权、Docker逃逸、文件传输、Shell生成、字典资源，都在Miscellaneous和Privilege Escalation两个目录下。Red Teaming部分还覆盖了**Evasion、C2、Payloads、Phishing、Exfiltration**，以及**EvilGinx的Phishlets**用法，链接了o365-mfa.yaml的GitHub仓库。

**五、怎么用：三种场景**

README里给了三种使用场景：

**新手面对不熟悉的目标类型**：先读`Methodology/`，理解整体流程。**需要某个具体技术**：直接跳到对应的领域文件夹。**在客户现场需要查命令**：用`Tools/`目录，按工具名查找用法。

GitBook镜像站点（h3ll-ka1ser.gitbook.io/boot2root）提供了更好的阅读体验，每个页面都有“For the complete documentation index, see llms.txt”的链接——这意味着你甚至可以把文档索引喂给AI Agent，让它按需检索。

**写在最后**

B00t2R00t的价值不在于“有多少个工具”。它的价值在于**组织方式**。它把AD渗透、云安全、提权、C2、钓鱼这些分散的知识点，用一条“Enumerate → Exploit → Escalate → Persist”的杀伤链串起来。新手跟着这条链走，知道每一步的输入输出是什么。老手把它当检查清单用，确保没有漏掉某个攻击面。

README的免责声明写得很直接：“This material is provided strictly for authorized security testing, research, and education. Only use these techniques on systems you own or have explicit written permission to test.”

**严正声明**

B00t2R00t是一个攻防知识库，不包含自动化利用工具。所有技术内容仅供**已获得明确书面授权**的安全测试、研究和教育场景使用。未授权访问计算机系统属于违法行为，与本文作者无关。请遵守法律法规，在授权范围内进行安全评估。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zL8x37G6prKFHZF4gTaajT0RYoRj81C6Rod7btfah6ZiaFaxIibKsVXNU7SMqnZia2FOtCYLFFgMor803P3ysbiba9ruW8LoMzjQw/0?wx_fmt=png)

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