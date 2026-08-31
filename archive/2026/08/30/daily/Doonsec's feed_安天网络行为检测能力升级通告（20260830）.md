---
title: 安天网络行为检测能力升级通告（20260830）
url: https://mp.weixin.qq.com/s/Y6e6uIGUAJeSitnjWL-sfA
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:51:16.687070
---

# 安天网络行为检测能力升级通告（20260830）

# 安天网络行为检测能力升级通告（20260830）

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

安天网络行为检测引擎收录了近期流行的网络攻击行为特征。本期新增检测规则65条，本期升级改进检测规则28条，网络攻击行为特征涉及代码执行、代码注入等高风险，涉及漏洞利用、文件上传等中风险。

**02**

**更新列表**

本期安天网络行为检测引擎规则库部分更新列表如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/XBFaicYdOHkibU59DtWibwVhOjmWicF5MY777FKhTm4tU1mK0k8Y22YXD37j0vUMQ3eAkP6tEvsh6tDjdo3UFbrEKJrZ1MEX8gByXURB8OpTYfM/640?wx_fmt=jpeg)

安天网络行为检测引擎最新规则库版本为Antiy\_AVLX\_2026082707建议及时更新安天探海威胁检测系统-网络行为检测引擎规则库（请确认探海系统版本为：6.6.1.4 及以上，旧版本建议先升级至最新版本），安天售后服务热线：400-840-9234。

**03**

**网络流量威胁趋势**

近期，安全研究人员发现，针对Cloudflare Workers的远程Spectre侧信道攻击，可从同一物理进程中的其他租户Worker泄露敏感数据。测试中，攻击者利用WebSocket作为远程计时源，并通过长时间运行的Durable Objects规避动态进程隔离机制，以最高每秒12比特、99.16%准确率窃取JWT令牌。Cloudflare已通过强化动态进程隔离、引入V8 Sandbox及内存保护密钥等措施完成修复，并表示过去三年未发现漏洞被实际利用的迹象，研究过程中也未访问真实客户数据。

此外，研究人员发现“CDN Tsunami”拒绝服务攻击，可利用CDN将HTTP/3流量转换为HTTP/1.1时的协议差异实施带宽和连接放大。测试显示，阿里云、百度、Cloudflare、Amazon CloudFront、Fastly及腾讯均受不同程度影响，最高可实现约350倍流量放大，使攻击者以较低带宽消耗源站大量资源。研究人员发现超4.2万个HTTP/3站点可能受影响。目前尚无在野利用报告，百度和腾讯已部署缓解措施。

**本期活跃的安全漏洞信息**

**1**

**Gitea diffpatch API远程代码执行漏洞（CVE-2026-60004）**

**2**

**keycloak账户接管漏洞（CVE-2026-18963）**

**3**

**Apache DolphinScheduler 权限提升漏洞（CVE-2026-49050）**

**4**

**Google Chrome释放后重用漏洞（CVE-2026-76017）**

**5**

**Google Chrome授权问题漏洞(CVE-2026-76019)**

**值得关注的安全事件**

**1**

**40款恶意Firefox扩展窃取加密钱包**

**Socket研究人员披露“Offside Wallet Theft Factory”恶意扩展活动，自2026年3月起持续针对Firefox用户，已确认40款扩展具有恶意行为，并另发现37款存在关联。这些扩展伪装成OKX、Rabby Wallet、TronLink等Web3产品，部分还先以体育比分、实用工具等正常功能上架，随后在相同扩展ID下转为恶意版本。攻击者可窃取钱包恢复短语、私钥、序列化密钥环、登录凭证及剪贴板数据，并借助Cloudflare Workers等基础设施将信息外传。目前尚未归因至已知威胁组织。**

**2**

**NASA AIT-GUI漏洞可下发航天器指令**

**Cycode披露NASA/JPL开源AMMOS Instrument Toolkit的AIT-GUI存在高危漏洞链，涉及身份认证缺失、CSRF及路径遍历等问题，影响2.5.1及更早版本。可访问服务端口的未认证攻击者能够获取有效会话，向仪器和航天器命令总线发送任意指令，并可能执行服务端脚本或调用越界文件。官方已在2.5.2中限制网络暴露并加强跨域和路径校验，但研究人员指出关键接口仍缺少凭证认证，因此认为风险尚未完全消除。目前未发现漏洞被实际利用。**

**安天探海网络检测实验室简介**

安天探海网络检测实验室是安天科技集团旗下的网络安全研究团队，致力于发现网络流量中隐藏的各种网络安全威胁，从多维度分析网络安全威胁的原始流量数据形态，研究各种新型攻击的流量基因，提供包含漏洞利用、异常行为、应用识别、恶意代码活动等检测能力，为网络安全产品赋能，研判网络安全形势并给出专业解读。

**往期推荐:**

[安天网络行为检测能力升级通告（20260816）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215306&idx=1&sn=af8f16bf0f208e9af650de0e8a784a48&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260802）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215225&idx=1&sn=87beebc6368d1992fddf67c9545dca55&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260719）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215137&idx=2&sn=0d971ffc3fcbd7f1a8f182ac1dddc391&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260705）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215046&idx=1&sn=3a425ec49245472c3ea368db25ba3860&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260621）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650214840&idx=1&sn=0970da4ace37bffebccdc46fafcb4e72&scene=21#wechat_redirect)

预览时标签不可点

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