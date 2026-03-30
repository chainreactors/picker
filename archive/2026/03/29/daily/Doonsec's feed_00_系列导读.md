---
title: 00_系列导读
url: https://mp.weixin.qq.com/s/AN72Xa7jP-qlZ_1YoVYWQw
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:43:48.388280
---

# 00_系列导读

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L7VicJKsiaibFCvQpfAjTBwficqxIc2q0SM6ibMJksib5OXcz8osrFgDmmoiawU1kB5rtlj8dVtC93BnCiabqMFEgQb17ZMGh3bB8JMO7H7Epj8Dgww/0?wx_fmt=jpeg)

# 00\_系列导读

原创

丘驰
丘驰

极客零零七

![]()

在小说阅读器中沉浸阅读

> 极客零零七 · AD攻击系列 · 导读

---

学AD攻防，最怕的不是单个技术点难——Kerberoasting的命令谁都能背下来。**最怕的是学完一堆散点知识，遇到真实环境时串不成链。**

这个系列用11篇文章，按照**实战攻击链的顺序**，从"手里什么都没有"一步步走到"拿下整个域"，最后站到蓝队视角看怎么防。每篇都有完整的命令、真实场景案例和攻防双视角分析。

---

### 系列目录

#### 第一阶段：突破边界

**第1篇｜第一个域凭据怎么来？AD渗透的初始立足点获取指南**

渗透的真正起点。Responder毒化、密码喷洒、AS-REP Roasting、共享文件搜索——系统梳理所有从零获取第一个域凭据的方法，按成功率排出优先级。

> 核心技术：LLMNR/NBNS毒化、密码喷洒、AS-REP Roasting、GPP密码、SMB共享搜索

####

#### 第二阶段：提权与横向

**第2篇｜Kerberos不是你的朋友：从协议原理到全攻击链**

有了凭据之后的第一课。不翻译RFC，而是从攻击者视角拆解Kerberos每一步认证中的可利用弱点。理解这篇，后面所有票据类攻击都是顺理成章的事。

> 核心技术：Kerberoasting、AS-REP Roasting、Golden Ticket、Silver Ticket、Pass-the-Ticket、DCSync

**第3篇｜你看不见的攻击路径：AD权限滥用完全指南**

比密码破解更隐蔽的提权方式。BloodHound画出来的那些"最短路径"，走的就是ACL链。本篇讲透GenericAll、WriteDACL、WriteOwner等危险权限的利用方法，以及如何用Cypher查询发现隐藏的5跳攻击路径。

> 核心技术：GenericAll、WriteDACL、WriteOwner、ForceChangePassword、BloodHound Cypher查询

**第4篇｜拿到一台机器之后：AD横向移动技术实战手册**

6种横向移动技术的对比——什么场景用什么技术、为什么、怎么避免踩坑。重点拆解Pass-the-Hash的底层原理和NTLM Relay的实战链路（PetitPotam + ADCS组合拳）。

> 核心技术：PTH、PTT、PsExec、WMI、WinRM、DCOM、NTLM Relay、PetitPotam

**第5篇｜AD委派攻击三部曲：一条被低估的域控攻击路径**

概念门槛最高但实战频率极高的攻击类型。把非约束委派、约束委派、RBCD三种机制讲透，配完整的攻击链案例——4条命令从普通域用户到SYSTEM。

> 核心技术：非约束委派+PrinterBug、约束委派+S4U+altservice、RBCD

####

#### 第三阶段：扩大战果

**第6篇｜被遗忘的攻击面：AD CS证书服务攻击完全指南**

几乎无人看守的攻击面。ESC1到ESC11逐一拆解，重点讲ESC1（3条命令域管）和ESC8（PetitPotam+证书=域控）。证书持久化比Golden Ticket更难清除——重置密码不影响已颁发的证书。

> 核心技术：ESC1-ESC11、PKINIT、证书持久化、CA私钥伪造

**第7篇｜打穿隔壁：AD域信任攻击**

拿下一个域不够，要拿整个林。ExtraSIDs攻击从子域直达林根域控，跨林Kerberoasting突破林信任边界。一句话总结：**林是安全边界，域不是。**

> 核心技术：ExtraSIDs Golden Ticket、跨林信任密钥、SID Filtering绕过、跨林Kerberoasting

####

#### 第四阶段：持久驻留

**第8篇｜赶不走的幽灵：AD域持久化技术与检测对抗**

拿到域控不是终点。Golden Ticket、AdminSDHolder劫持、SID History注入、Skeleton Key——每种持久化技术都讲清楚三件事：怎么种、怎么查、怎么清。附蓝队完整清理检查表（12项）。

> 核心技术：Golden/Silver Ticket持久化、Skeleton Key、AdminSDHolder、SID History注入、GPO后门

####

#### 参考与防御

**第9篇｜AD攻击武器库：每个阶段该用什么工具**

不是工具安装教程，而是选择指南。按攻击阶段分类，讲清每个工具的核心能力、适用场景和工具间的配合关系。附工具决策树和攻击技术-工具对应表。

> 覆盖工具：BloodHound、Mimikatz、Rubeus、impacket、CrackMapExec/NetExec、Certipy、Responder、PowerView、Kerbrute等

**第10篇｜蓝队反击战：AD域防御加固完整指南**

换到防御者视角。20项加固措施按投入产出比排序，分3个阶段（立即/30天/90天）落地。前6项措施能阻断80%的AD攻击路径——不需要额外预算，只需要执行力。

> 核心内容：Tier模型、Protected Users、LAPS、Credential Guard、SMB签名、NTLM限制、蜜罐账户、监控告警规则

####

#### 完结篇

**第11篇｜从网线到域控：一次完整AD渗透的全流程复盘**

把前10篇的所有技术串成一条完整的攻击链。模拟从"手里什么都没有"到"拿下整个AD域"的全过程，2.5小时完成。附攻防双视角复盘：每一步攻击对应什么防御措施能阻断它。

> 攻击链：Responder → AS-REP Roast → Kerberoast → 约束委派 → DCSync → 域控

---

### 这个系列适合谁

* **渗透测试工程师**：系统补全AD攻击知识，从散点命令到完整攻击链
* **红队成员**：实战案例和工具选择参考，每篇都有可直接复用的命令
* **蓝队/安全运营**：第8篇（检测）和第10篇（加固）是为你写的，知道攻击者怎么打才能防得住
* **安全研究员/学生**：从协议原理到实战利用的完整学习路径

---

> 关注公众号「极客零零七」，回复「AD攻击」获取最新版AD域攻击速查表
>
> **声明**：本系列仅供授权渗透测试和安全研究学习使用，禁止用于非法活动。

###

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

极客零零七

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

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