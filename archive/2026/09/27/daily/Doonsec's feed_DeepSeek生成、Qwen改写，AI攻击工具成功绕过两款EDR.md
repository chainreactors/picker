---
title: DeepSeek生成、Qwen改写，AI攻击工具成功绕过两款EDR
url: https://mp.weixin.qq.com/s/0EED5jyuxHE9oz-nzh9ajQ
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:05.694733
---

# DeepSeek生成、Qwen改写，AI攻击工具成功绕过两款EDR

# DeepSeek生成、Qwen改写，AI攻击工具成功绕过两款EDR

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/sz_mmbiz_gif/icBE3OpK1IX0FOBbQvTB2DLayZNiaJXvSLCzc4SXzzv7GaicEyolYmWecg8fqOmEjmn9PB3goxNDMkbXM5TYkXg9krgRYvTFzYyLEZlibAqeF7Q/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3LrmqoJXIbe4MtHia7XeGicEvK5D5QBtdQ535PScltJm5vjJicU3fneTs7vnMgGqgBvfOTN7u2pLLSkBJNiaG5xNYxTMHxPxXfAUQ/640?wx_fmt=png&from=appmsg)

研究人员在受控实验室环境中完成测试，一款本地部署、无内容审查的AI模型经多轮调整修改Windows凭证转储工具，最终成功规避两款EDR产品的检测。这一结果凸显，获取门槛不断降低的生成式AI，可能会加速定制化攻击工具的开发流程。

这项实验由Project Black研究员Eddie Zhang发布，测试针对LSASS进程展开。攻击者获取管理员权限后，可读取LSASS内存中存储的认证凭证，用于内网横向移动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3q11C99CDMvZfONuO5hZXiaSlVepXOtxXl7iaaLrp9R3aGqaTtu0x5AISUnicjTNiamz34C5T1KFgnQvF4vTxcWzAVDvACPWCNRjI/640?wx_fmt=png&from=appmsg)

Part01

实验设置高难度基准

项目最初设置了一个难度极高的测试基准：在极少人工引导的前提下，AI能否生成一款可转储LSASS内存、且不会被主流EDR检测的可执行程序。这项测试具备很强的现实意义，因为MITRE ATT&CK框架已将LSASS内存转储列为凭证访问类子技术，编号T1003.001。管理员或SYSTEM权限级别的攻击者，可从LSASS内存中窃取凭证，进一步登录其他系统扩大攻击范围。

据Eddie Zhang介绍，他先后尝试用Claude Opus 5、Opus 4.8、Sonnet 5生成转储工具，全部被模型直接拒绝。尽管他所在机构已通过Anthropic的网络验证计划获得相关研究授权，依然无法获取有效输出。

![image](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0xn3e3cKgCcgEos0xiarcrrU0twIxkiatoL4HdwgmL5ibCdtdHRHRXOuaXFgepZSfxx4ZWnYVTaYtWdnWLjsfpznwbV1qfB863mc/640?wx_fmt=png)

随后Eddie Zhang测试了开源权重模型DeepSeek v4 Flash 0731。经过几轮提示词调整，DeepSeek生成了一款可正常运行的可执行程序。

该程序支持输入进程ID，可通过反射机制创建目标进程的挂起克隆体。程序会在内存中生成小型转储文件，经XOR加密后写入磁盘。

研究人员用pypykatz验证生成的转储文件，确认文件可正常解析，但初始版本的可执行程序依然会触发EDR告警。当他要求模型提升程序隐蔽性时，DeepSeek触发了安全护栏，拒绝继续修改。

![image](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0PicRzJjj4tc6ibtk41AANpZef7txuuVxia5tnK6EASGqvjFoGVI0SYNXfiaah1W0qN6vhOia2eAu99AMv4o30uiaJ0xIEd7YWEMtEw/640?wx_fmt=png)

因此Eddie Zhang将代码迁移到一款经社区修改、无内容审查的Qwen 3.8 27B模型中。该模型在本地一台密码破解专用工作站上运行，设备配备两张Nvidia RTX 4090显卡。

Part02

本地模型成功绕过两款EDR检测

Eddie Zhang表示，他仅向模型提出“提升程序隐蔽性”的要求，本地模型就返回了修改后的版本。实验室部署的两款EDR平台，均未对该版本程序产生任何告警。

研究人员对代码做了审计，发现Qwen调整了进程生成逻辑，降低了对目标进程请求的访问掩码权限。模型还在小型转储文件生成过程中插入随机延迟，修改了输出文件的名称和路径，并清除了二进制文件中的嵌入字符串。

这些修改恰好命中了主流防御规则的检测盲区。多数EDR会通过关联明确的攻击特征判定风险，包括可疑的进程父子关系、对LSASS发起的高权限句柄请求、已知恶意字符串、转储文件创建行为、以及时间特征高度固定的操作序列。

例如Elastic就公开过一条通用检测规则，专门监控针对LSASS发起的句柄请求，这类请求携带转储工具常用的访问掩码。MITRE也总结过相关检测逻辑：先识别异常的进程访问行为，再匹配后续的内存转储或文件创建操作。

Part03

防御方需构建多层防护

这项发现具备重要参考价值，但适用范围存在明显限制。研究人员未公开测试所用EDR的厂商名称，也未公布具体配置细节，仅在实验室环境下绕过两款产品，并不代表该方法能通用绕过所有EDR。

但结果依然证明，本地部署、无安全护栏的模型可以迭代修改已知攻击代码，全程无需向云端托管服务发送提示词或源代码。这大幅降低了定制适配特定环境攻击变种的技术门槛和时间成本。

防御方不应将EDR视为唯一的安全保障，需搭建多层防御体系。微软建议用户启用带篡改防护的LSASS反凭证窃取攻击面减少规则，将LSASS配置为受保护进程轻量（PPL）模式。

此外还应部署Credential Guard，限制RDP远程管理权限。同时要禁用WDigest凭证缓存。

企业还应最小化本地管理员权限范围，对特权账号做权限隔离。要确保各账号使用唯一凭证，同时监控针对LSASS的异常访问行为。发现主机存在凭证转储行为时，要第一时间隔离处置。

参考来源：

Local AI Model Modifies Windows Credential Dumper to Bypass EDR Detection

https://cybersecuritynews.com/local-ai-bypasses-edr/

### **推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bRSnFgE3WPnpU3s0eVp7QdRn9fI63ymmlhTHpsMBL2VnRMPZQy9DhvZasynJV1ia534sF84uxxKKulzDlBibjrQ7ylDiaickrCIY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651347479&idx=1&sn=1cf9c858a30d0b7af06d196002bd2913&scene=21#wechat_redirect)

###

### **电报讨论**

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3yychgqrdWpeazfdwAxHj4T9ILWI3fl6IUFOJEIcOHVC5ia3VjkrzuJLbJ4krtMqID23cDDy61ykbbic6NSXcVHRBvrW1jxxOU4/640?wx_fmt=png&from=appmsg)

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0Py7ibxdLKXia1pMziaic5vIE9XPXG9OGaeJDa07iaG10eicuzhW59nwpF5msHiaYZvfMqCNkx2aFDiaMzm3oAf4rTaHXU5UAI1mUYgts/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX0TIGzII2Hcmtzu7AJeZFicnqd1mXojVoawje2uLxYqwJbVgzJpmSXzVhrpOsLurRZ2lVa4vfgLBqg7uJKbrKg5F18VzZxVPicZU/640?wx_fmt=png)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过