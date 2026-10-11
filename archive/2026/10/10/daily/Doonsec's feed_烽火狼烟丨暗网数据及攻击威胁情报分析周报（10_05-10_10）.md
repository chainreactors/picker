---
title: 烽火狼烟丨暗网数据及攻击威胁情报分析周报（10/05-10/10）
url: https://mp.weixin.qq.com/s/wdQyjXkHgADGpHPN_cD87A
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:20.745082
---

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（10/05-10/10）

# 烽火狼烟丨暗网数据及攻击威胁情报分析周报（10/05-10/10）

盛邦安全应急响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

WebRAY安全服务团队定期针对敏感数据泄露、热点资讯、热点技术、热点漏洞、威胁攻击等情况进行跟踪整理与监测分析，本周总体情况如下：

本周内共发现暗网数据贩卖事件902起，比上周上升133.07%。本周内贩卖数据总量共计428748.5万条；累计涉及7个主要地区及6种数据分类，数据泄露来源地区分布情况如图1所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mxwq2AF6zpNkLTicKHk7mFCqr8bM3uFYtfSFeQ9OQK1cvNPUrhiaVwV3f7zy6GibwIWIC7vqLFQend0rg0iahWtHibZuJaNFYSM8bDDrf06bcEN0/640?wx_fmt=png&from=appmsg)

图1 泄露数据来源地区分布情况

本周内泄露数据涉及金融、个人信息、服务等多种类型数据，具体占比如图2所示。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpOaXLVZwrQlbdGIqFZxCQ7RSavsdC1WbybrCKscXld9wiamiak6XILKscvXMtIMfrK8vjCPo8xfGHUpaibVyFBNj2iabtXx815icCug/640?wx_fmt=png&from=appmsg)

图2 泄露信息数据类型占比

近期安全威胁以仿冒人机验证钓鱼为主，并伴随AI服务器恶意挖矿、多地区海量敏感数据泄露，本周内出现的安全漏洞中WP Store Locator存储型XSS漏洞危害程度较大。内部安全运营中心共发现恶意攻击来源IP 8843条，主要涉及组件漏洞攻击、命令注入等类型。

**01.**

**重点数据泄露事件**

**巴拿马社保基金医疗预约数据集疑似泄露**

泄露时间：2026-10-06

泄露内容：攻击者宣称利用默认账号密码获取巴拿马社保基金约70万条医疗预约记录并在论坛发布。疑似泄露信息包含患者姓名、国民身份证号、接诊医生、专科信息、预约日期、诊所信息。

泄露数据量：约70万

关联行业：医疗

地区：巴拿马

**美国耶鲁大学出版社数据集疑似泄露**

泄露时间：2026-10-07

泄露内容：攻击者宣称获取耶鲁大学出版社超64000名学生及员工相关数据。疑似泄露信息包含交易记录、个人信息、Yale Books源代码、课程资料、考试答案、注册数据以及其他内部文件。

泄露数据量：约6.4万

关联行业：教育

地区：美国

**土耳其Okul Güvenliği校园安全平台数据集疑似泄露**

泄露时间：2026-10-07

泄露内容：攻击者宣称获取土耳其校园安全平台Okul Güvenliği相关数据集，共计210余万份。疑似泄露信息包含身份证件编号、手机号码、学生及家长姓名、出生日期、学校、班级以及其他个人信息。

泄露数据量：约210万

关联行业：教育

地区：土耳其

**法国Groupe Réussir农业食品行业数据集疑似泄露**

泄露时间：2026-10-06

泄露内容：攻击者宣称利用认证绕过漏洞获取法国农业与食品行业媒体集团Groupe Réussir数据集，共计330万条。疑似泄露信息包含姓名、电子邮箱地址、电话号码、地址、账号信息、密码哈希以及其他客户数据。

泄露数据量：约330万

关联行业：农业与食品

地区：法国

**法国Eau Cœur d'Essonne公共水务机构数据集疑似泄露**

泄露时间：2026-10-09

泄露内容：攻击者对外共享法国公共水务机构Eau Cœur d'Essonne 数据集，约5.5万条。疑似泄露信息包含客户姓名、地址、水表编号、合同详情、支付方式、订阅信息、供水及环卫服务记录。

泄露数据量：约5.5万

关联行业：水务

地区：法国

**02.**

**热点资讯**

**勒索数据恢复服务商负责人被指控实施欺诈**

某地司法部对提供勒索软件事件处置服务的MonsterCloud企业经营者Zohar Pinhasi提起电信欺诈及共谋指控。该公司对外宣称拥有自研解密工具，无需向黑客支付赎金就可以帮客户恢复被勒索软件加密的数据，但实际并无专属解密技术，而是私下向勒索团伙支付赎金换取解密器，再向客户收取远高于赎金的服务费。检方指控其累计向客户收取超过1900万美元，其中有超800万美元被用来向黑客支付赎金。

消息来源：

https://thehackernews.com/2026/10/monstercloud-owner-accused-of-billing.html

**Anthropic推出分级机制向审核通过的安全团队开放Claude模型**

Anthropic升级网络安全验证项目CVP，划分三类访问权限，经过资质审核的安全人员可以在降低模型安全拦截限制的前提下使用Claude系列模型，分别适配防御分析、授权红蓝对抗、深度安全测试等不同工作场景。其Glasswing项目在2026年4-7月期间累计发现129000个经过验证的软件漏洞，开源扫描工作又额外识别5500个漏洞，其中超33000个属于高危、严重级别，官方认为实际漏洞规模会更高。

消息来源：

https://thehackernews.com/2026/10/anthropic-expands-claude-access-for.html

**超百个遭入侵网站利用伪造人机验证分发LunexStealer窃取木马**

黑客入侵了超过100个合法网站注入恶意JS脚本，展示仿冒Cloudflare人机验证页面，并借助ClickFix手法诱导用户执行指令下载MSI恶意安装包，投放LunexStealer信息窃取木马。攻击还使用EtherHiding技术，从区块链智能合约读取攻击配置，具备被动收集访客信息、展示虚假验证页面等多种工作模式。该恶意程序存在多个变种，可绕过系统安全防护，还会安装伪装成办公插件的恶意浏览器扩展，窃取Cookie、表单账号凭证，篡改网页安全策略，搭配配套组件实现读写本地文件、执行命令等远程操作。

消息来源：

https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html

**Wikimedia平台出现OpenAI自主智能代理的异常操作行为**

维基百科运营机构Wikimedia基金会披露，平台观测到疑似OpenAI自主智能代理的一系列未授权行为。AI代理在维基沙盒测试区域进行编辑，尝试篡改引用工具配置、试图攻破Etherpad在线笔记工具，意图将两类工具当作代理访问外部网络，相关尝试均未成功。同时代理发起数百万次API请求、大规模爬取页面，海量查询流量或造成部分服务出现中断，目前没有证据表明系统数据遭到窃取、代理之间借该平台互相协同。Wikimedia呼吁AI厂商需要为智能代理带来的外部损害承担责任。

消息来源：

https://thehackernews.com/2026/10/wikimedia-says-openai-agents-tried-to.html

**因未安装安全补丁引发入侵事件FBI解除外包人员相关权限**

FBI解除埃森哲一名外包人员的工作权限。调查认定，第三方平台未及时部署官方发布的安全补丁，导致黑产团伙ShinyHunters实施入侵，造成数千名FBI工作人员个人信息泄露。涉事平台为Oracle PeopleSoft，攻击者利用CVE-2026-35273漏洞的绕过手段，借助URL编码技巧规避Web应用防火墙防护。FBI已完成风险处置，同时该团伙已有两名成员被捕。

消息来源：

https://thehackernews.com/2026/10/fbi-removes-accenture-contractor-after.html

**03.**

**热点技术**

**PoeLLM恶意软件入侵AI服务器组建加密货币挖矿僵尸网络**

PoeLLM恶意软件专门针对外网暴露的LiteLLM、Gotenberg、Gitea等AI/LLM业务设备，现已攻陷超3400台服务器。该样本采用特殊隐蔽手段，从GitHub仓库托管的诗歌文本解析提取C2地址，攻击者修改诗歌内容即可切换命令服务器而不用更新恶意载荷。主机失陷后攻击者通过部署XMRig、Iron挖矿程序接入Kryptex挖矿服务；部分被攻陷服务器被改造为扫描节点，主动探测互联网同类目标并下发恶意载荷。

消息来源：

https://thehackernews.com/2026/10/poellm-malware-infects-3400-servers-to.html

**人工运营AI广告钓鱼平台利用BitB技术窃取账号及MFA验证码**

黑客团伙搭建人工操控的钓鱼平台，伪装ChatGPT、Gemini、Claude等AI产品的广告营销门户，宣称提供广告优化、预算审计等业务功能，通过仿冒邀约邮件诱导广告从业者访问。页面点击Connect按钮触发浏览器内浏览器（BitB）钓鱼手段，在真实页面渲染伪造登录弹窗，地址栏伪造为Google、Okta等可信域名；后台完成设备指纹采集，攻击者通过Socket.IO实时交互，可动态切换各类多因素认证质询界面，实时截获账号密码与MFA验证码。

消息来源：

https://thehackernews.com/2026/10/fake-chatgpt-gemini-and-claude-ad.html

**ClickFix新变种借助浏览器缓存偷渡载荷绕过Windows运行对话框字符限制**

该ClickFix变体利用被入侵网站，将恶意脚本伪装为PNG图片预加载至浏览器本地缓存，规避Win+R运行对话框约260字符的输入截断限制。受害者粘贴简短指令后，载荷不会现场远程下载，而是检索浏览器缓存目录，通过文件大小匹配提取缓存对象，转存为VBScript执行。后续链路通过WMI采集主机信息，拉取PowerShell脚本，完成内存加载.NET组件，向timeout.exe进程注入代码，实现凭证窃取。ClickFix攻击技术已经产业化，借助钓鱼工具包降低攻击门槛，还出现利用AI摘要提示注入、WordPress站点植入、区块链C2解析的衍生手法。

消息来源：

https://thehackernews.com/2026/10/clickfix-smuggles-payloads-through.html

**Cling物联网僵尸网络滥用STUN协议构建隐蔽C2信道**

Cling物联网僵尸网络针对路由器、DVR等大量IoT设备，利用多款设备的远程代码执行能力完成初始入侵，包含Realtek Jungle SDK高危漏洞利用行为。恶意样本支持多类Linux硬件架构，具备多重持久化手段：写入系统启动配置文件，还可替换系统wget二进制文件实现劫持执行；通过端口绑定机制保证主机内仅运行单一实例。该僵尸网络最大特点是滥用STUN NAT穿透协议作为命令控制通道，每5秒向预置的13台STUN服务器发送绑定请求，将指令隐藏放置于STUN报文的事务ID字段，网络流量外观近似正常WebRTC、VoIP业务，对流量检测形成混淆。失陷设备可执行蠕虫式横向扫描传播、TCP隧道、代理转发、拒绝服务攻击等任务。威胁流量可伪装成来自谷歌公共STUN服务的正常应答，提升隐蔽性。

消息来源：

https://thehackernews.com/2026/10/realtek-jungle-sdk-exploit-attempts.html

**伪装邮件安全产品的Linux后门针对电信网络设备实施间谍活动**

BPFDoor变体模仿反垃圾邮件产品SpamSniper的进程与PID标识，还可轮换多种系统守护进程名称；利用Linux BPF套接字能力被动监听网络，触发魔法数据包后才激活恶意逻辑，新版本将触发载荷封装在HTTPS POST报文内，借助电信设备SSL卸载绕过深度包检测，激活后可拉起TinyShell交互会话，实现文件上传下载。针对台湾设备的AVERAT由ELF投放器执行解密部署，执行后10秒删除本体文件留存恶意进程，采用SMTP 25号端口作为C2信道，定时回连服务器，支持目录遍历、文件分片上传下载、进程管控、交互式Shell、动态加载扩展模块、端口转发等丰富指令。

消息来源：

https://thehackernews.com/2026/10/linux-backdoors-impersonate-email.html

**04.**

**热点漏洞**

**Dislocker堆越界读取漏洞(CVE-2026-107635)**

Dislocker是BitLocker加密卷解密工具。get\_vmk ()与get\_fvek ()函数存在整数下溢漏洞，攻击者提供特制恶意BitLocker卷镜像，当datum\_size小于36字节AES-CCM头部大小时，会触发hexdump ()函数堆越界读取，造成程序崩溃拒绝服务。

影响版本：dislocker <= 0.7.3

**databases-on-aws插件命令注入漏洞(CVE-2026-107322)**

Databases-on-aws是AWS Amazon Agent Plugins中的数据库相关插件。插件采用黑名单输入过滤机制，但禁用输入列表不完整，远程未认证攻击者可构造恶意数据库命令值，当代理加载该恶意内容并调用本地辅助程序时，可在运行辅助程序的主机上执行任意操作系统命令。

影响版本：databases-on-aws < 1.7.1

**Tenable ldentity Exposure命令注入漏洞(CVE-2026-106126)**

Tenable Identity Exposure是面向Windows平台的身份安全检测产品。其Active Directory事件监听器组件存在操作系统命令注入漏洞，已认证的低权限攻击者可利用该漏洞在PDCe上以SYSTEM权限执行任意系统命令。

影响版本：Tenable Identity Exposure < 3.126.0

**EspoCRM存储型HTML注入漏洞(CVE-2026-105831)**

EspoCRM是一款开源客户关系管理系统。公开的线索收集表单（Lead Capture）存在未授权存储型HTML注入漏洞，未认证攻击者可提交恶意构造的表单数据，数据会保存在LeadCaptureLogRecord.data中；管理员查看日志记录时，该数据会未经过滤转义直接渲染。受内容安全策略CSP限制，该漏洞无法执行JavaScript脚本，但可注入恶意HTML内容。

影响版本：EspoCRM < 10.0.6

**WP Store Locator存储型XSS漏洞(CVE-2026-105078)**

WP Store Locator是WordPress的门店定位插件。插件对用户可控输入未做正确转义过滤，存在存储型跨站脚本漏洞。拥有低权限的远程攻击者可注入恶意脚本，当其他用户访问受影响页面时会触发脚本执行，造成信息窃取、页面篡改等危害。

影响版本：WP Store Locator <= 3.0.3

**05.**

**攻击情报**

本周部分重点攻击来源及攻击参数如下表所示，建议将以下IP加入安全设备进行持续跟踪监控。

![](https://mmbiz.qpic.cn/mmbiz_png/mxwq2AF6zpOJPibCY4VquuAl5zYxNshCOqo2lNQ3bCS8Rlx27pvBEII7ibtdIqEd2omTSn01xfSDIurok3EBI1YRwZfDj35DW26Crv66TQdMY/640?wx_fmt=png&from=appmsg)

*请注意：以上均为监测到的情报数据，盛邦安全不做真实性判断与检测*

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6oQwlp95XBm9ia9yroBLJd83wAseiabOAQoLDBAJrxjfU1KmTexS35sibxXQvt4ots9DicJoxXNiabToHw1T09Myv7Q/0?wx_fmt=png)

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