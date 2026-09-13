---
title: 一日四停：四家头部SRC同日按下暂停接收漏洞
url: https://mp.weixin.qq.com/s/SheB9NUayWaTBOjdvn9qSw
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T07:01:02.045167
---

# 一日四停：四家头部SRC同日按下暂停接收漏洞

# 一日四停：四家头部SRC同日按下暂停接收漏洞

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PztymibyKDwPw1A5rUVclbGSfCP6CLgIunXickvuqHKsgJqnWlicFxCqZtKvI0pfsQGiamNs0L1cSrWViakS3jBlkFWiaolKUNoUvrA/640?from=appmsg)
> **导语**：2026年9月11日，白帽圈遭遇了史无前例的黑色星期四。从下午15:00到深夜23:59，短短9小时内，四家头部SRC接连发布暂停接收漏洞通知。这不是巧合——这是中国互联网安全行业的集体紧急避险。本文事件根据公众号「FC攻防笔记」原创报道《SRC-911事变》整理。

---

## 一、事件时间线：四家SRC同一天按下暂停键

9月11日这天，白帽师傅们的朋友圈几乎被各种暂停通知刷屏。从公开渠道披露的四份通知来看，这是一场精心策划的"集体避险"——按时间顺序梳理：

**某通ZSRC（最早一枪）**——"关于暂停接收中[某]公司中危、低危漏洞报告的通知"，公告自发布之日起立即生效。最狠的是只暂停中低危，高危照收，这意味着他们当下处理的核心是高危以上的硬仗。

**某讯IC^平台（紧跟其后）**——"暂停漏洞接收通知"，即日起暂停接收安全漏洞，恢复时间另行通知，期间请勿对[某]飞及其相关业务进行安全测试。原文特别强调"请勿对相关业务进行测试"——这是典型的"防御方紧急避险"措辞。

**某易SRC（15:00准点开火）**——"关于[某]易SRC暂停安全漏洞通知"，自2026年9月11日15:00起暂停接收新增漏洞，其余功能保持不变。这个"其余功能保持不变"很关键——说明他们早就做好了切换预案。

**某VI平台（23:59压哨停摆）**——自2026年9月11日23:59起暂停接收漏洞，作为最后一家"压哨"跟进。这家甚至细化到"积分按月结算无需手动操作，请提前确认提现信息"——典型的客服式安抚话术。

![四家SRC暂停通知一览](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NuTyWAicWK7XibaE6QpybePo8Rqtf364iaJyoQVBAJVTQlB6DaXKAgXFNaOBMtia6FEXVDEHuqDrlFgtlTLFXIJmBF9ic6J51Iwic3E/640?from=appmsg "四家SRC暂停通知一览")

*图源：公众号「FC攻防笔记」原创报道《SRC-911事变》，原文链接见文末。*

---

## 二、红队视角：四家SRC为啥同步按下暂停键？

作为攻击者视角看，这种级别的"集体暂停"极其罕见——四家头部SRC不可能在没共识的情况下同一天开火。我尝试从几个假设切入：

**假设1：上游供应链0day爆发引发行业应急**

最可能的剧本——某大型开源组件（npm包/PyPI包/maven工件）爆发供应链投毒事件，多家公司同时中招。SRC紧急关闭入口是为了：

* 防止白帽提交的"现场证据"反过来被恶意利用
* 给内部安全团队争取排查时间
* 避免重复报告挤爆审核队列、淹没真正高危线索

**假设2：某客户端RCE被广泛披露**

如果9月10日-11日有重大客户端漏洞（浏览器内核、IDE、办公软件）被公开POC，四家SRC同步暂停是为了防止白帽在客户端中"种shell"——一旦白帽在客户端执行了未授权代码，触发法律边界，平台兜不住责任。

**假设3：行业政策窗口期**

临近重要时间节点，监管层要求重点企业SRC"暂停新提交，先消化存量"——这种剧本在重要会议前后反复出现过。

**假设4：SRC平台自身被搞**

最敏感的可能性——某家SRC平台后台数据泄露（白帽提交历史、内部漏洞库、内部KOL名单），导致同行紧急自查。这种情况下，"暂停"其实是"止血"。

无论哪个假设，都指向同一个事实：9月11日这天，行业里正在发生某件大事。

![某易SRC暂停通知原文细节](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6Ozf40BOCYz8xIBmOttlXhj2mAhia9OP1rd2TjkW5OvatjjiaOQQnWYCOkmBh4xBjEHtuzYlP37qNChaFUZDhA1YSNw4YsyVSm6c/640?from=appmsg "某易SRC暂停通知原文细节")

*图源：公众号「FC攻防笔记」原创报道《SRC-911事变》。*

---

## 三、对白帽圈的真实影响

不管原因是什么，白帽师傅们面临的现实问题很具体。综合四家通知，规则口径高度统一：

**已提交的漏洞**：按四家通知统一口径"继续按现有流程正常审核处理"——9月11日之前提交的漏洞不受影响，已经在审核队列里的不会被强制清空。

**新漏洞提交**：暂停接收，提交入口暂时关闭，等恢复时间另行通知。原文明示"提交入口暂时关闭"——意味着连登录验证新提交都不行，不是"暂缓审核"而是"暂停入库"。

**积分及奖励**：正常发放，按月结算，不受本次升级影响。这是安抚核心白帽的关键——钱的事不能停。

**提现通道**：原文明示"请提前确认并填写正确的提现信息"——这个细节值得琢磨。翻译过来就是：万一后续通道临时调整，你卡号错了我们不负责。

---

## 四、红队视角：暂停期能做的事

SRC暂停并不等于攻防博弈停止。相反，作为攻击者，我反而觉得这是个好窗口：

**1. 资产盘点窗口期**

SRC暂停期间，没有其他白帽在前面跑，你的漏洞提交不会撞车。深入做目标资产梳理——子域爆破、字典优化、参数污染测试——这些平时被其他白帽干扰的工作，现在可以静心做。

**2. 逻辑漏洞深挖窗口**

SRC抢洞的是高频漏洞（XSS/SQLi/越权），但暂停期间你可以沉下心来做：

* 二阶注入（先存后取，绕过WAF）
* 业务逻辑越权（订单/支付/优惠券）
* 复杂条件竞争（抢购、签到、抽奖）
* 认证体系缺陷（OAuth/JWT/SSO回调）

这些洞出产慢、竞争少、奖金反而高。

**3. 老洞二次利用测试**

被拒的漏洞是不是真的被修了？SRC暂停期间，SRC的复测团队也紧张，正是测试"修复完整性"的好时机——同一个漏洞换个参数可能就重新成立。

**4. 盯紧恢复时间节点**

SRC一旦恢复，往往伴随"积压奖励集中发放"和"积压报告优先审核"。盯紧恢复公告，第一时间提交高质量报告，比平时收益更高。

---

## 五、写在最后

"一日四停"这一天，四家头部SRC同步按下暂停键——这不是巧合，而是某种外部冲击下的集体应急反应。

作为攻击者，我一直相信：**每一家SRC按下暂停键，背后一定正在发生什么大事。**

防御方越是紧张的时刻，往往越是攻击者重新审视自己技术储备的时候。

白帽圈的黑色星期四已经过去，但安全行业的博弈永远不会停止。

---

**特别说明**：本文事件根据公众号「FC攻防笔记」原创报道《SRC-911事变》整理，原文链接 [https://mp.weixin.qq.com/s/ibf1cbKN6SyIHsyzC2ptIQ](https://mp.weixin.qq.com/s?__biz=MzcwMDQyMTcxNA==&mid=2247483928&idx=1&sn=91850d8646f64ca398dfc991ec8b8d1d&scene=21#wechat_redirect) 。所有截图（概览图、某易SRC详情图）版权归原作者「FC攻防笔记」所有，本文仅作行业事件分析使用。封面图为AI文生图，华盟网自有版权。

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MnLPCiadZcpZgoIluiav2EIoa6QByQaSMP97z94shphmGqOdBLkRT1icWbNEQsKm8nnJMRZwZJCvOBv1vqsC39GBgywuoKmjH1X8/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NnThyyZ1IBnhvtGQq11nE41KzNU6UvHXmPoy7iaLnFBEvAGkrnlsCZiaVdadRUe3yD4LXuyJWq4kCoEc2Etss8HQ1n9LyHoRPU8/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PwNNz6LdicyA80ibQnKicm1JHsAiaaKfGI5D2Yl93dVuY9WR0f8lbsFIGm91x52GdTfnxSY9bJyt6v8P0x0NMXscwFrpbibZfwUWQs/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MicdXlFzxX0xbkYIdlVBvXDoC2aBopfLv2Eia2QprmATXNverAsounGkmA3VtCibOk4ZePgwHNSUZPLwISG6HtaT2NYHBbo8ccJU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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