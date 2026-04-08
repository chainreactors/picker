---
title: 红队攻防实战秘籍：从外网突破到内网的格局全览
url: https://mp.weixin.qq.com/s/fCGn9P6evoWXMhVYqlo7nw
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:34:47.883057
---

# 红队攻防实战秘籍：从外网突破到内网的格局全览

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/J7CSmJcRR8lErjxUsts383icFib6R3PbTaic26LTPAN7uRnVC8uiao1VbkBUVVnlDkYT9IH0dtHR5cJ9Y5icz2dqAFZYIPmhuUzdtkLE3W14MuMg/0?wx_fmt=jpeg)

# 红队攻防实战秘籍：从外网突破到内网的格局全览

TtTeam

![]()

在小说阅读器中沉浸阅读

以下文章来源于Khan安全团队
，作者忍者

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6HvHSDXDlBxY0qXVHLH06BWXdlPIkic8a73R4oJ3j8MoQ/0)

**Khan安全团队**
.

安全不是一个人，我们来自五湖四海。研究方向Web内网渗透，免杀技术，红蓝攻防对抗，CTF。

![](https://mmbiz.qpic.cn/mmbiz_png/J7CSmJcRR8lyzI33hiarHM0Qic4Eblwo4hjvwibdk4gq5K9lOvWkgbevCRI8Ax8Z7Eh1fBtwBXvbY97PpCZOXzJia2t9ypibazczSJSyuuibtVCVs/640?wx_fmt=png&from=appmsg)

## 一、侦察与初始打点（Reconnaissance & Initial Access）

##

寻找防线的薄弱环节往往比挖掘0-day漏洞更有效。外网打点不仅依赖技术，更依赖对目标业务和人员的了解。

* **资产与信息收集（OSINT）：**

+ **DNS探测：**针对`intranet`、`sharepoint`、`wiki`、`cyberark`等关键字进行DNS查询，快速定位高价值目标（技巧#5）。
+ **自动化监控：**结合`Spiderfoot`进行长期开源情报监控，使用`theHarvester`收集子域和邮箱，或者利用`DomainHunter`寻找可信的过渡域名来绕过拦截。
+ **元数据提取：**利用`PowerMeta`或`FOCA`公开文档的元数据，这通常可以泄露内部用户名和软件版本。

* **钓鱼与社会工程学（网络钓鱼）：**

+ **多维度投递：**如果经常Payload被拦截，尝试发送包含Python或PowerShell单行命令的邮件，诱导目标（甚至Mac用户）手动执行。
+ **绕过双角色认证（2FA）：**随着O365、AWS等云服务的普及，2FA成为标配。利用`Evilginx`记录Cookie进行会话劫持，或通过钓鱼获取VPN/Citrix等可能未开启2FA的边界入口权限。
+ **邮件格式：** SPF 记录如果没有配合 DMARC 策略，依然可以被格式。如果目标 DMARC 策略薄弱，直接伪造其内部邮箱发送邮件，成功率极高。

## 二、防御规避与武器化（Defense Evasion & Weaponization）

##

与杀毒软件、EDR（端点检测与响应）和沙箱的对抗是红队的日常。

* **绕过监控与沙箱：**

+ **混乱行为：** EDR 常监控`whoami`或`net users /domain`等敏感命令。可以使用`echo %userprofile%`替代，或将命令变体为`net use /dom`和`powershell -ec`。
+ **辅助父子进程检测：**使用`SelectMyParent`工具父子进程（例如避免出现`powershell.exe`生成`cmd.exe`的可疑行为）。
+ **反沙箱技术：**遇到FireEye等沙箱拦截时，使用`GenHTA`等工具生成拥有反沙箱逻辑的HTA文件，或将恶意代码直接加载到内存中。

* **执行车站：**

+ **备用执行手段：**当`runas`被拦截时，使用未托管的PowerShell（Unmanaged PowerShell）；当`regsvr32`被拦截拦截时，利用工具（如SCT-obfuscator）进行干扰。
+ **利用系统特性：**尝试利用ADS（备用数据流）落盘文件，或者利用卷影拷贝（VSC）执行恶意程序以躲避蓝队查杀。

## 三、凭据获取与权限提升（Credential Access & Privilege Escalation）

##

获取可疑是内网渗透的重中之重。除了传统的Mimikatz，还有更多低噪的获取方式。

* **域环境密码提取：**

+ **Kerberoasting：**这是一条通往域管的快速通道。使用 PowerView 等工具导出服务取消并离线破解。
+ **与历史默认凭据：**不要忘记SYSVOL中残留的GPP密码。如果破解陷入僵尸局，尝试整合用户历史密码生成字典，或使用公司名、季节、年份组合盲猜。
+ **哈希窃取与中东：**在低权限下，可通过在共享文件夹放置UNC图标LNK文件，或使用WordSteal嵌入图片，配合`Inveigh`抓取NetNTLM哈希。

* **目标软件的特定窃取：**

+ 内存中运行着 KeePass？利用`KeeThief`提取密码。
+ 遇到密码保护的文档，使用`office2john`哈希进行破解。

## 四、内网探索与横向移动（Discovery & Lateral Movement）

##

在成熟的网络环境中，盲目扫描会迅速暴露。

* **精准定位与资产发现：**

+ 导出完整的 DNS 区域数据（DNS Zone Dump），或者利用较差的`BloodHound`攻击路径。注意：除了域管理员，还要关注服务器运营商等默认映射的高权组。
+ 攻陷机器后，利用`tasklist`、`netstat`查看`query user`当前进程和在线用户，判断是否适合跳板。

* **舌头的横向技术：**

+ **本地管理员共享：**相同系统构建的机器通常拥有相同的本地管理员哈希，实现批量横向。
+ **劫持与间谍活动：**发现所有的 RDP 会话？使用`tscon`劫持会话。在 VDI 环境下，可以利用 Citrix Shadow Taskbar 监控用户的虚拟桌面。
+ **传统非路径：**利用默认打印机密码、WSUS更新机制，甚至是利用RDPInception攻击反向突破隔离网络。

## 五、行动安全与C2基础设施（OPSEC & Infrastructure）

##

OPSEC（Operational Security）决定了红队能够在目标内网潜伏多久。

* **流量与通信认知：**

+ **C2架构：**按照最佳实践建立红队基础设施。利用域前置（Domain Fronting）技术，让恶意流量干扰在合法的CDN节点中；或利用SSH隧道（配合GatewayPorts）建立轻量级流量器。
+ **混乱视听（Decoys）：**将攻击活动分开。可以利用Nessus从外网进行高噪音扫描，或发送大量垃圾邮件，消耗蓝队的分析精力，掩盖真实的攻击通道攻击。

* **痕迹清理与防溯源：**

+ 在 Linux 下操作时，使用`kill -9 $$`避免 bash 历史记录落盘，修改 DHCP 删除主机名和 VPN 配置接入时暴露自身信息。
+ 移动端同样通知，一旦红队基础设施遭到蓝队反制或扫描，立即采取应对措施。

## 六、总结：红队的心智模式

##

* **目标导向：**红队演练不是为了“刷洞”或纯粹的漏洞利用测试（渗透测试），而是为了“潜入”并完成业务目标（例如：“ATM机吐钱”或“窃取核心配方”）。
* **团队协作：**渗透是一门艺术，也是工程。团队协作能够激发出更好的想法，保持更多的元素。
* **持续学习：**蓝队的防御技术在不断升级。关注顶尖的安全会议，紧跟安全研究人员的最新成果，才能保持对抗优势。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

TtTeam

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

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