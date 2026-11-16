---
title: FBI曝光AI自动化攻击，ARTEX仅用3小时即可攻陷企业系统
url: https://mp.weixin.qq.com/s/yIIUxZjzHaItGKqd7y1SAw
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:44:13.768203
---

# FBI曝光AI自动化攻击，ARTEX仅用3小时即可攻陷企业系统

# FBI曝光AI自动化攻击，ARTEX仅用3小时即可攻陷企业系统

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX1WSpJnicZMXFkaaoUM47FjcvQibzZQetYtHYRsLZdaVZftRHZuXagbSFM8Tv8Qpv0tEgubypXPI8whicrZpKcHWw69RAC3W7JrhQ/640?wx_fmt=gif)

![FBI预警ARTEX攻击](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3bmrDClYPpibJdUjicw8N7dtpRic7BjaP8BejGcgJf0eECEPPZ0lPR7GQ60JrkkJ3mc1eeGrZxaj57uKESdcMgicBhMwUqFFEHyYw/640?wx_fmt=png)

FBI发出警告，称攻击者正利用ARTEX AI Agents自动化实施网络攻击，部分入侵行动不到三小时就能获取特权访问。

FBI在2026年11月13日发布的FLASH预警中，详细说明了攻击者如何组合窃取的凭证、暴露的应用和云权限，缩短从资产发现到入侵得手的时间。

ARTEX是一款开源安全测试框架，并非恶意软件家族。它采用Go语言编写，可将外部大语言模型与Agent连接，把指令转化为可执行命令。

操作人员设定攻击目标后，Agent会自动扫描目标、运行工具、分析结果、调整失败步骤，整个攻击过程仅需极少人工介入。

Part01

ARTEX加速企业攻击流程

据Cybersecuritynews.com此前的ARTEX企业攻击分析，该框架并非依赖单一新型漏洞，而是串联各类已知常见弱点实施攻击。Agent可排查云权限、测绘Active Directory、测试访问路径。Google观测到，单次自动化攻击突发仅持续2至25秒，防御者几乎没有时间关联分析相关事件。

FBI记录的攻击手段包括SQL注入、API缺失认证、密码暴露、滥用可信云连接。攻击者获取初始访问权限后，Agent会向现有应用添加凭证、部署Web shell、尝试窃取凭证。其他活动还包括排查未安装端点防护的Windows系统，测绘超过11万个Active Directory对象。

Microsoft此前已将ARTEX与Storm-0940关联，该组织具有中国国家背景，主要通过失陷的ConnectWise应用凭证攻击Microsoft 365环境。

攻击者利用客户已授权的权限，尝试访问超过2250个租户。该数字仅为攻击目标规模，并非确认遭入侵的租户数量，且仅凭成功登录无法证明攻击者已窃取客户数据。

FBI的预警汇总了上述发现，同时警告ARTEX还会攻击易被忽视的供应商门户、销售工具和移动端后端。"不到三小时"是部分观测到的入侵案例的耗时，并非该工具的固定能力。截至11月初，公网暴露的ARTEX控制台已超过1600个，但暴露的安装实例并不必然意味着其操作者将其用于恶意用途。

WorkOS单独披露的一起入侵事件，凸显了内部业务应用面临的风险。WorkOS检测到，一款存储客户联系方式、对话记录（包括Slack消息摘录）的销售应用遭未授权访问。WorkOS首席执行官确认攻击中使用了ARTEX，同时公司称没有证据表明生产服务或WorkOS应用数据受到影响。

Microsoft的另一项调查记录显示，ARTEX Agent会在GitHub上搜索暴露的密钥。在某起案例中，Agent从搜索代码仓库到窃取Azure Key Vault数据仅用时五分钟。这一活动表明，泄露的应用凭证可被用于获取云资源访问权限，尤其是当这些凭证对应的身份在关联服务中拥有宽泛权限时。

研究人员还排查了一名与韩国金融攻击相关的攻击者暴露的服务器，在文件中发现了AI路由工具、可复用攻击指令、代理服务和存储的凭证。这些攻击共影响约6.7万人。不过，仅因各方都使用ARTEX，无法证明该攻击者、Storm-0940与WorkOS攻击者之间存在关联。

Part02

安全团队需强化监测防护

FBI建议限制公网暴露的管理工具，缩减应用权限，扫描代码仓库中存储的密钥。防御方应将异常应用登录行为，与凭证新增、角色变更、高频API调用活动进行关联分析。

按攻击阶段梳理观测到的战术与技术：

* 侦察与云发现：扫描Web目录、测绘暴露系统、测试窃取的云凭证，通过快速请求与验证测试排查Azure、AWS权限；对应T1595主动扫描、T1580云基础设施发现、T1087.004云账户发现、T1526云服务发现。
* 初始访问：利用SQL注入、API缺失认证、不安全文件上传及其他Web应用漏洞，使用泄露的密码、窃取的VPN信息、失陷的供应商凭证；对应T1190利用面向公众的应用、T1078有效账户、T1133外部远程服务、T1199可信关系。
* 供应链攻击：滥用第三方应用访问权限与可信云连接，通过失陷的服务商进入客户环境；对应T1195供应链攻击、T1199可信关系。
* 执行与持久化：部署JSP、PHP Web shell，通过Kudu管理API执行命令，安装远程访问工具，向现有OAuth应用添加凭证；对应T1505.003 Web shell、T1059命令与脚本解释器、T1105入口工具传输、T1098.001新增云凭证。
* 权限提升：启动拥有高权限角色的云实例，创建管理员账户，访问云元数据，使用未修改的认证密钥伪造管理员令牌；对应T1098.003新增云角色、T1552.005云实例元数据API、T1606伪造Web凭证。
* 内部发现：针对域控制器运行PowerShell查询，测绘超过11万个Active Directory对象，识别未部署端点安全防护的Windows系统；对应T1059.001 PowerShell、T1087.002域账户发现、T1518.001安全软件发现。
* 横向移动：利用窃取的认证材料、哈希传递、票据传递、Windows远程管理尝试访问域控制器，部分尝试被端点防护拦截；对应T1550.002哈希传递、T1550.003票据传递、T1021.006 Windows远程管理。
* 数据收集与暂存：查询后端数据库，读取云存储与邮箱内容，访问云密钥，创建存储卷为窃取数据的传输做准备；对应T1530云存储数据、T1114.002远程邮件收集、T1555.006云密钥管理存储、T1074.002远程数据暂存。
* 命令与控制：通过住宅代理、Tor、SOCKS代理、失陷中继路由流量，使用Chisel、SoftEther搭建隧道连接；对应T1090代理、T1090.003多跳代理、T1572协议隧道、T1071.001 Web协议。

在遏制攻击过程中要做好证据留存，排查所有次要访问路径，在阻断共享云基础设施之前，需对照当前日志验证历史攻击指标的有效性。

本次预警公布的指标包括：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2fKAyvJict55HrLU9CnpniafyxFBZjPy5sQTaCpJ8En4EkqPhrrmAUOraLrzgOSlSHPqtibLib7mg1st0RRY5m6PeppqicGWgnErkA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yH6Yf02iae1jtIpCGCFpLibu6AYhM1ecIlWS8hlkdVO9NT7YMkdCicgHLtoIXA3MztX40sjmlQLDP1CcGuiagbwaqYD8aKENI0js/640?wx_fmt=png&from=appmsg)

参考来源：

FBI Reveals How Hackers Use ARTEX AI Agents to Gain Privileged Access in Under Three Hours

https://cybersecuritynews.com/fbi-reveals-hackers-artex-ai-usage/

### **推荐阅读** [![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Wh05Z0rN9nVQTjUXnyXs6uYnM9oo6THt2FhXmXzcuMkHbceiatCbhz8mR2zDd0yicfXLAnN2mwPzVRz1C0ibPQ0ocMnNt16QAkg/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651349303&idx=1&sn=86458815b0d0b880c32e19864a449a98&scene=21#wechat_redirect) **电报讨论** ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2cCEVtIlLczLq1S4rms9uYa8x5Xedy0Il667ib20FMyHawNapLuHBl3peZxWoStYkAJdBcMicfmy9icChQA8uKfBib5EPaMicU5ykw/640?wx_fmt=png&from=appmsg) ![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png) ![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过