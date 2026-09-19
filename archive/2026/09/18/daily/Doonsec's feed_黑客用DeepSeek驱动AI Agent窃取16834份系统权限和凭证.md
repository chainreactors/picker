---
title: 黑客用DeepSeek驱动AI Agent窃取16834份系统权限和凭证
url: https://mp.weixin.qq.com/s/vSgy6K4iRWBo-O3Yz4lFFg
source: Doonsec's feed
date: 2026-09-18
fetch_date: 2026-09-19T06:52:57.138708
---

# 黑客用DeepSeek驱动AI Agent窃取16834份系统权限和凭证

# 黑客用DeepSeek驱动AI Agent窃取16834份系统权限和凭证

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX2HMMC0ebH3pPDWAbV8Z5l5o203P8FZ9NBFOMvuEDXbYuBmNiaHHzflhqtFsU8wI29eJeTKOaicLFfibP7TStPd9Xkgn83yb7ibcM0/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3Uy6980lticSXhibdCACZd20uGe6jZ84Zept1HxWuqA9P2zVsZoMialiaeIzkSeO8g2e8iakiaBJG9UrJotPxX0nWvS0UMZxpIY1q7o/640?wx_fmt=png&from=appmsg)

研究发现，网络犯罪组织BlackHatSect0r（关联别名DXQRTXX）运营着一套自动化网络犯罪作业体系。该组织使用接入DeepSeek模型的AI Agent扫描公开泄露的密钥、验证窃取到的访问权限，再将结果回传至自研控制平台。

这类攻击活动表明，攻击者可利用常见安全配置缺陷，以机器速度开展大规模入侵。研究人员发现一台暴露的作业服务器，其中存储了9299个文件共4.9GB数据，包含DXSCAN平台、钓鱼工具、勒索素材，以及一个存有16834份凭证的凭据库。在整个攻击活动中，该组织累计扫描队列包含2759860个域名，触达726989台主机，生成1374300个IP地址。

SOCRadar研究人员识别出该组织的攻击基础设施，同时发现证据表明，这个法语作案的犯罪团伙在多轮攻击中使用AI Agent前，已经移除了Agent内置的安全防护机制。SOCRadar在向Cyber Security News（CSN）提供的报告中指出，该团伙的攻击并未利用任何新漏洞，全部依托公开暴露的云存储、可读取配置文件以及弱密钥实施。

该团伙活动的危害远不止凭证窃取。从查获的材料来看，该组织还涉嫌公共部门数据盗窃、勒索、加密货币交易所数据泄露，以及针对老年群体的冒充银行电话诈骗。这一案例给AI Agent自动化攻击的风险防控敲响了警钟：自动化能力会大幅放大常规配置错误的危害程度。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2DemlQothYcgGt0CfjZdxzK6nGJ2F5WrBf8AKSicNUNjTSc5L7KuuxkH9S6aqMc8kKu5HianYfurwwtSk8dg529Jg5kFR4eumBY/640?wx_fmt=png&from=appmsg)

Part01

团伙依托DeepSeek自动执行攻击

该团伙运行Nous Research推出的Hermes Agent接入DeepSeek模型。整套Agent的运行由一个名为SOUL.md的身份配置文件控制，文件大小仅14KB。 操作人员移除了Agent的拒绝响应记忆模块，关闭了所有安全设置，同时配置7个后台工作进程，无需持续人工输入即可持续执行扫描、收集和上报操作。

其配套的DXSCAN工具每10秒可生成约1200个随机地址，扫描80、443、8080端口并识别目标站点的Web软件类型。在此基础上，工具会匹配200余种凭证特征开展定向搜索。

![SOCRadar平台中的BlackHatSect0r与DXQRTXX活动监控界面](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX01APQq5gicTtK3dibqhc0OwzCsTNSxZSxWib0BlUkib73cg57bLcVfIfRv7JEWfqmftVIbO1agwFCL108NuXwk1R0hppPjjAUbRJc/640?wx_fmt=png)

一旦工具发现暴露的.env文件、云密钥或数据库配置信息，就会自动存储数据，并通过Telegram发送法语版本的受害者情况报告。

这套作业流程印证了近期关于自主凭证窃取活动的安全警示：AI无需研发突破性的漏洞利用方式即可造成危害。AI为攻击者提供了持久运行能力、极高的执行速度，还支持并行开展侦察、权限验证和数据收集工作。该团伙对外宣传部分工具为0Day武器，但研究人员确认，所有已核实的入侵事件均未利用新漏洞。

攻击者获得的所有有效访问权限，均来自公开可读的云存储桶、暴露在公网的.env或Git文件、默认签名密钥，或是硬编码在浏览器端代码中的密钥。在某加密货币交易所的案例中，管理员将JWT签名密钥设置为弱口令“secret”，直接导致418条用户身份记录泄露。

Part02

攻击者批量窃取凭证开展钓鱼

该团伙的凭据库规模从8月11日的16415条，增长至8月18日的16834条。库中存储的凭证包含通用密钥、数据库与SMTP凭证、API密钥、AWS密钥、GitHub令牌、Stripe密钥等多种类型。在查获的230份SMTP配置中，有82份已通过有效性验证，攻击者准备将其复用为钓鱼邮件转发节点。

同一套基础设施还支撑着一类特殊钓鱼活动：攻击者不会在邮件中放置恶意链接，而是诱导收件人拨打攻击者控制的电话号码，而非clicking恶意链接。

这种战术可以绕过链接扫描和附件检测机制，因此企业必须做好员工安全意识培训，规范官方电话回拨流程。关注相关威胁的读者可参考AI赋能网络攻击技术的相关资料，了解Agent在入侵过程中的任务分工模式。

Part03

安全团队需强化配置排查

企业应审计云存储的公开读写权限，将.env、.git、调试接口、actuator端点从公网下线，轮换所有可能已泄露的密钥。

![该团伙使用的专属标识](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2NcicWxK1zAoxRtRyBbVEibjhHRG7u5gaibYCTnibtFF2icLKpiaQ6QAFIu4yfU3luUAaxgcibz0gRBYxPTLT52ZWcicciciavefauSGILk/640?wx_fmt=png)

企业必须将签名密钥与令牌生成材料存储在服务端，立即替换所有默认值或易被猜测的弱值。

防御方还应排查下文列出的攻击基础设施、异常GHOST字符串、SOUL.md文件、.hermes目录，以及未授权的ngrok活动。Web团队可对单一来源短时间内集中请求配置路径的行为设置告警，尤其是这类请求出现在常规Web端口扫描之后时，需重点关注。

这些排查要求也呼应了此前Vite服务器遭攻击事件暴露出的教训：可公开访问的环境文件会为更广泛的入侵打开大门。安全团队一旦发现匹配的攻击指标，应立即开展调查、隔离受影响系统、留存日志，并及时核查相关认证活动记录。

攻击指标（IoCs）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0rqeeIMrZDhVBQRvOjxxN1KbQiaiby9KKE12qRRBFbnGAibQicJUykRIcCtqhPgkm3LicGsicoickJic4lcAXe3XW6FE7TwSPGRfz3uD4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1sTicoUFROfvZ09FicBiaacorbu3GhTia4Jg2xj3SPVBakjiakCA1L28pdRPCCKPMKTqia7ShdtXRmumjnyqpEtia8d4tp0G8SFGN7DA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2dBnmaJDJYibf3eJbradfD0lPqZgAqbiadIDlTqhEU7QtYkwqEYY9CuZN0G0klN6TFooLibKia70zSGNK0LrGK2UiciazMUpFtFNs1Y/640?wx_fmt=png&from=appmsg)

注：文中IP地址与域名均已做去激活处理（如使用[.]替代点号），防止意外解析或跳转。请仅在MISP、VirusTotal或企业内部SIEM等受控威胁情报平台中恢复原始地址格式。

参考来源：

BlackHatSect0r Uses DeepSeek-Powered AI Agent to Automate Attacks and Harvest 16,834 Credentials

https://cybersecuritynews.com/blackhatsect0r-ai-agent/

###

### **推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0XsTyO4SuMuGUvEh6HBoZLXPa9xnn1UsveAZRjUSfAKwT77dFfrwAPbRgSe6l66sYOBiaFSfWMn3DL4IfDrDmexoxCYLftaleo/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651346509&idx=1&sn=71e02ef8b6a2ed67fdc94aa19b152171&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

预览时标签不可点

阅读原文

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
在看
，轻点两下取消在看
分享
留言
收藏
听过