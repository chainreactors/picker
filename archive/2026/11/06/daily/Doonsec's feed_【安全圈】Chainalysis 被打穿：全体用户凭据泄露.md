---
title: 【安全圈】Chainalysis 被打穿：全体用户凭据泄露
url: https://mp.weixin.qq.com/s/EuSI8dWx3G6AZhlC86DYow
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:57:41.469809
---

# 【安全圈】Chainalysis 被打穿：全体用户凭据泄露

# 【安全圈】Chainalysis 被打穿：全体用户凭据泄露

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

凭据泄露

11 月 6 日，区块链分析公司 Chainalysis 更新安全事件通报，影响面比一周前的"部分客户密码泄露"大得多：**全部用户的姓名、用户名、密码哈希与仍在生效的访问令牌均已外泄**。此前公司已把 Reactor、KYT 等核心产品全线停摆。泄露范围升级到全体账户，攻击向量虽已修复，凭据外泄的既成事实收不回来

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEyOWyC3DX1lUs589JLkP8GCyrAsDSwMicAVqZW5k0tUlQCX8bNjaXFvz233hkRK2oonGmo8p0h7xictkF3OEA3md7ALGZnY8qpw/640?wx_fmt=other&from=appmsg)

## 🚨 一周之内，定性两次升级

事件起点是 10 月 30 日。Chainalysis 披露遭外部行为者入侵，对方动用进攻性智能体技术（offensive agentic techniques）拿到系统与内部工具的未授权访问。调查过程中又挖出一起路径上攻击（on-path attack），暴露了部分客户的密码

11 月 6 日的通报把范围改写为全体用户：姓名、用户名、密码哈希、活跃令牌均告泄露。公司称攻击向量已修复，但没有说明攻击持续了多久

## ⚡ 核心产品集体下线

处置动作密集而彻底：

* Reactor 与 Data Solutions 的访问权限已移除
* KYT（Know Your Transaction）用户界面与 API 下线，地址筛查产品、登录页一并关闭
* 受影响账户全部锁定，收到改密邮件的用户暂时无法完成重置
* 公司新增主动监控系统，盯防异常活动

Chainalysis 强调，目前没有证据表明调查数据被访问，归因数据也未被篡改

## 🔍 同期遭袭的技术平台不止一家

攻击者身份没有下文。Chainalysis 只有一句定性：与近几周其他技术平台的遭遇相似

背景是实的。Chainstack、OpenCode、Warp、WorkOS 近期先后披露遭 AI 驱动攻击，部分事件涉及名为 ARTEX 的自主渗透测试工具。微软追踪到攻击者用智能体框架扫荡公开 GitHub 仓库里的凭据、应用凭据与 AI 推理 API 密钥，再拿这些密钥展开后续入侵。一个案例里，**智能体从扫描 GitHub 到外泄 Azure Key Vault 密钥只花了 5 分钟**，这类活动从 2026 年 8 月持续至今

微软还观察到智能体先取得目标组织内单租户 OAuth 应用的令牌，再借它枚举组织的其他云资源，专挑 AI 服务 API 密钥与 Foundry Tools（原 Azure Cognitive Services）权限下手。Google 本周的报告证实，盗取商用大模型云访问权限再转卖已经做成生意（LLMjacking）

## 🛡️ 恢复走白名单，眼下该做的事

* KYT 与地址筛查恢复采用白名单制：把可信 IP 提交给 support@chainalysis.com 或客户经理，加白后重置密码、轮换 API 密钥
* 公司要求所有用户重置密码并按需轮换 API 密钥；Reactor 与 Data Solutions 的恢复时间未定
* 在其他系统复用过同一密码的账户立即改密——密码哈希已随本次事件外泄

目前处置停留在加固与恢复阶段：系统加固、产品逐步重新上线、账户访问将增加额外保护。公司称恢复完成后会另行通知访问策略变更

***END***

阅读推荐

[【安全圈】白宫专网被卖做代理？总统办公室设备疑遭植入后门](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079711&idx=1&sn=05bdbc8ba75d9805145596493772fbf6&scene=21#wechat_redirect)

[【安全圈】潜伏近三个月！DreamHost漏洞致大量主机凭据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079711&idx=2&sn=63979c6dc888fb4e4dbc4da49a266ae8&scene=21#wechat_redirect)

[【安全圈】币安63亿被盗余震！Coinbase转超99%资产至冷钱包](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079711&idx=3&sn=b21a981adb4002765fad3dad5018fe73&scene=21#wechat_redirect)

[【安全圈】9.8分Linux内核高危RCE！无需认证隔空打穿](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079699&idx=1&sn=dfbd72f6698a155131d20cada69f5589&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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