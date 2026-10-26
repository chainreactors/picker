---
title: 安天网络行为检测能力升级通告（20261025）
url: https://mp.weixin.qq.com/s/3nzY9Y7utGyc9Jq3hKhCnA
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:14:33.732370
---

# 安天网络行为检测能力升级通告（20261025）

# 安天网络行为检测能力升级通告（20261025）

安天集团

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

点击上方"蓝字"

关注我们吧！

##

安天长期基于流量侧数据跟踪分析网络攻击活动，识别和捕获恶意网络行为，研发相应的检测机制与方法，积累沉淀形成了安天自主创新的网络行为检测引擎。安天定期发布最近的网络行为检测能力升级通告，帮助客户洞察流量侧的网络安全威胁与近期恶意行为趋势，协助客户及时调整安全应对策略，提升网络安全整体水平。

**01**

**安天**网络行为检测能力概述****

安天网络行为检测引擎收录了近期流行的网络攻击行为特征。本期新增检测规则313条，本期升级改进检测规则37条，网络攻击行为特征涉及代码执行、代码注入等高风险，涉及漏洞利用、文件上传等中风险。

**02**

**更新列表**

本期安天网络行为检测引擎规则库部分更新列表如下：

![](https://mmbiz.qpic.cn/mmbiz/XBFaicYdOHk8G9wnpz1dKCWHRAC78zqicHo95tRnHwSJEib00FlyIr67t65stBFTKy2icPwPIChzLtJsmic2uApCT7mmTmcHY7ia31mgEv0wuAyws/640?wx_fmt=bmp&from=appmsg)

安天网络行为检测引擎最新规则库版本为Antiy\_AVLX\_2026102207建议及时更新安天探海威胁检测系统-网络行为检测引擎规则库（请确认探海系统版本为：6.6.1.4 及以上，旧版本建议先升级至最新版本），安天售后服务热线：400-840-9234。

**03**

**网络流量威胁趋势**

近期，安全研究人员发现，伪造Web3加速器“Apex Accelerator”通过恶意npm包@apexacc/cli和@apexacc/audit向Windows与macOS系统投递窃密程序和后门。项目以免费AI额度、代码工具和安全审计功能吸引开发者，其中所谓18项安全审计工具实际返回硬编码、日期生成或随机结果。安装后的启动器会从GitHub Releases下载平台对应二进制文件，并通过vrf.apexaccs[.]org获取攻击者命令。相关组件还可截获并重定向OpenRouter大模型请求，读取其中的提示词、对话历史、代码片段和工具输出，并在AI代理配置中注册攻击者控制的MCP服务器。

此外，研究人员发现一项钓鱼活动正在传播Rust编写的CikaBika Bot远控木马。受害者收到包含磁盘映像文件的PDF诱饵，映像中放置伪装成Word文档的LNK快捷方式；打开后会显示诱饵文档，同时启动隐藏PowerShell进程解码并运行嵌入式程序。后续Nim加载器释放Rust DLL和PowerShell部署脚本，并尝试将DLL移动至受保护的Edge目录，通过DLL搜索顺序劫持加载恶意代码。CikaBika启动后使用Discord为每台受感染主机建立独立通信通道，收集系统、进程和网络信息及屏幕截图，可接收命令执行、进程控制、文件上传下载、摄像头和屏幕流等指令，并可将目录压缩为ZIP后通过Ngrok外传。

**本期活跃的安全漏洞信息**

**1**

**IBM Verify Identity Access 信任管理问题漏洞(CVE-2026-109126)**

**2**

**Apache Camel 路径遍历漏洞(CVE-2026-79986)**

**3**

**Apache Camel 信息泄露漏洞(CVE-2026-85251)**

**4**

**IBM MQ Operator 反序列化注入漏洞(CVE-2026-12148)**

**5**

**Red Hat Enterprise Linux 输入验证错误漏洞(CVE-2026-16487)**

**值得关注的安全事件**

**1**

**BAE Systems遭网络攻击全美联邦破产通知服务中断**

**美国联邦司法机构披露，BAE Systems为联邦法院运营的Bankruptcy Noticing Center相关IT系统和网站遭遇网络安全事件，导致全美破产法院通知业务中断。受影响设施包括bnc.uscourts.gov、bankruptcynotices.uscourts.gov、notices.uscourts.gov以及National Creditor Registration Service，相关网站和系统均一度无法访问。BNC负责为美国各地联邦破产法院制作和传输破产通知，此次事件同时停止了通知文件的生产与分发。美国法院行政办公室正与受影响法院及BAE Systems协调，BAE Systems继续调查并恢复相关系统。**

**2**

**SideCopy组织向印度机构投递ReverseRAT远控木马**

**安全研究人员披露，UAC-0277攻击活动利用超过100个遭入侵安全研究人员披露，APT组织SideCopy正在针对印度机构开展鱼叉钓鱼活动，目标包括学术机构，并通过多阶段感染链部署ReverseRAT。攻击邮件携带ZIP压缩包，内部包含伪装LNK快捷方式和诱饵文档；执行后会从攻击者服务器下载混淆HTA文件，并利用mshta.exe运行，随后加载恶意DLL、批处理脚本和第二阶段HTA，同时通过注册表Run键建立持久化。后续脚本使用.NET反序列化和反射加载在内存中启动ReverseRAT，可远程执行命令、收集系统信息、截屏、窃取密码和剪贴板内容、操作文件并外传敏感数据。**

**安天探海网络检测实验室简介**

安天探海网络检测实验室是安天科技集团旗下的网络安全研究团队，致力于发现网络流量中隐藏的各种网络安全威胁，从多维度分析网络安全威胁的原始流量数据形态，研究各种新型攻击的流量基因，提供包含漏洞利用、异常行为、应用识别、恶意代码活动等检测能力，为网络安全产品赋能，研判网络安全形势并给出专业解读。

**往期推荐:**

[安天网络行为检测能力升级通告（20261011）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215603&idx=1&sn=63fafcb76663cceca3e5e668138bf35a&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260927）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215581&idx=1&sn=9f44d7067d0ccb97d67c025267047355&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260913）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215475&idx=1&sn=2e4a58edd6b583d2c745ca8daec6e5cc&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260830）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215399&idx=1&sn=468e578636c4127c56f3d8359a5d8835&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260816）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215306&idx=1&sn=af8f16bf0f208e9af650de0e8a784a48&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/krU5D4C1q6Su8m4epwZC39J9XTv5TOxXtKXld0O7YvcKGpIweyd5y6LHX1FW1QU1RLuE08hwNZmLTdcd4fOUGg/0?wx_fmt=png)

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