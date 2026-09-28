---
title: 安天网络行为检测能力升级通告（20260927）
url: https://mp.weixin.qq.com/s/hSOLA3RnKsOelRIDKyoOCw
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:55:39.926003
---

# 安天网络行为检测能力升级通告（20260927）

# 安天网络行为检测能力升级通告（20260927）

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

安天网络行为检测引擎收录了近期流行的网络攻击行为特征。本期新增检测规则133条，本期升级改进检测规则66条，网络攻击行为特征涉及代码执行、代码注入等高风险，涉及漏洞利用、文件上传等中风险。

**02**

**更新列表**

本期安天网络行为检测引擎规则库部分更新列表如下：

![](https://mmbiz.qpic.cn/mmbiz_png/XBFaicYdOHkibpYeoquCSKic4a1Z1dibfPHTHWYqP7up5nujbg4oodhcxjPeicic7EicdROSc5W3V3YOgialvyGy3xSjfEsHoL41GkovBxGaNPmjYgA/640?wx_fmt=png&from=appmsg)

安天网络行为检测引擎最新规则库版本为Antiy\_AVLX\_2026092307建议及时更新安天探海威胁检测系统-网络行为检测引擎规则库（请确认探海系统版本为：6.6.1.4 及以上，旧版本建议先升级至最新版本），安天售后服务热线：400-840-9234。

**03**

**网络流量威胁趋势**

近期，安全研究人员发现，威胁团伙借助ClickFix类诱饵传播新型远控木马ChainScript。该恶意程序伪装成Spotify、Zoom Workplace、Microsoft Teams软件，采用类似EtherHiding技术，依靠Polygon智能合约定位WebSocket C2服务。该RAT具备命令执行、文件操作、截屏、窃取加密货币钱包等完整远控能力。攻击者劫持HBO Max官方Reddit账号投放恶意广告，发动PasteSwitch 攻击，分别针对Windows与macOS投递窃密恶意软件，相关攻击借助指纹识别做隐身规避传统检测手段。

此外，研究人员发现名为WeaselBiscuit的Node.js窃密恶意软件，藏匿于十余款npm包，疑似朝鲜BeaverTail、OtterCookie恶意家族的精简分支。该恶意包被导入后会启动分离后台进程，借助Npoint服务获取载荷并内存执行，不落地磁盘。它可收集主机信息、窃取Chrome扩展存储数据，受控捕获剪贴板与Windows键盘记录，采用HTTP轮询C2通信，移除了远控、钱包解密、截图等能力。研究人员暂未完成确凿归因，提醒开发者警惕相关恶意npm包。

**本期活跃的安全漏洞信息**

**1**

**F5 BIG-IP APM OAuth 远程代码执行漏洞(CVE-2026-94127)**

**2**

**Google Chrome授权问题漏洞(CVE-2026-87492)**

**3**

**VeloCloud Orchestrator 权限绕过漏洞(CVE-2026-93952)**

**4**

**Acronis Backup 插件本地权限提升漏洞(CVE-2026-87886)**

**5**

**GigatechPDV5701 未授权访问漏洞(CVE-2026-94493)**

**值得关注的安全事件**

**1**

**[安天披露针对开源AI模型的"潜伏式污染"攻击事件](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215540&idx=1&sn=42bb4aa7a364adbaf84f092127b2fce8&scene=21#wechat_redirect)**

**安天CERT监测发现，同一批共71个文件以“模型更新”的名义先后投递到Hugging Face平台两个头部厂商的官方模型仓库。需要说明的是Qwen和DeepSeek并未接受攻击者发起的合并请求，而攻击者则是利用其发起合并请求的行为来制造信任错觉，对潜在传播形成了机会窗口。该攻击实施的门槛极低，由于社区的运营机制，符合注册并完成平台实名认证条件的用户均可以向仓库提交，并发起合并请求，因此对仓库维护方来说，只能依靠人工前置审查、仓库访问权限管控与提交内容特征检测相结合的方式应对。**

**2**

**Jade Slee威胁组织入侵印度IT服务商部署后门**

**朝鲜威胁组织Jade Sleet（又称TraderTraitor、UNC4899）攻陷一家印度IT服务商，该组织惯于针对Web3领域实施加密货币盗窃，曾卷入Bybit、KelpDAO/LayerZero重大失窃事件。攻击者采用虚假面试社工手段，投放植入恶意Terraform锁文件的GitHub仓库，受害者执行terraform init即触发载荷，部署FLATROOF、ROOFDECK两款Rust编写的macOS后门。FLATROOF借助Telegram下发指令窃取各类本地敏感数据；ROOFDECK依靠Nostr协议实现去中心化C2通信，具备侦察、持久化与横向移动能力。**

**安天探海网络检测实验室简介**

安天探海网络检测实验室是安天科技集团旗下的网络安全研究团队，致力于发现网络流量中隐藏的各种网络安全威胁，从多维度分析网络安全威胁的原始流量数据形态，研究各种新型攻击的流量基因，提供包含漏洞利用、异常行为、应用识别、恶意代码活动等检测能力，为网络安全产品赋能，研判网络安全形势并给出专业解读。

**往期推荐:**

[安天网络行为检测能力升级通告（20260913）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215475&idx=1&sn=2e4a58edd6b583d2c745ca8daec6e5cc&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260830）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215399&idx=1&sn=468e578636c4127c56f3d8359a5d8835&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260816）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215306&idx=1&sn=af8f16bf0f208e9af650de0e8a784a48&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260802）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215225&idx=1&sn=87beebc6368d1992fddf67c9545dca55&scene=21#wechat_redirect)

[安天网络行为检测能力升级通告（20260719）](https://mp.weixin.qq.com/s?__biz=MjM5MTA3Nzk4MQ==&mid=2650215137&idx=2&sn=0d971ffc3fcbd7f1a8f182ac1dddc391&scene=21#wechat_redirect)

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