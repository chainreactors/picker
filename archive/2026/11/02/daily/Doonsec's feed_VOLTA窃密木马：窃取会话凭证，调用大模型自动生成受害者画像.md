---
title: VOLTA窃密木马：窃取会话凭证，调用大模型自动生成受害者画像
url: https://mp.weixin.qq.com/s/yJ-gNDYscifB2zuZrThWgw
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:47:43.722457
---

# VOLTA窃密木马：窃取会话凭证，调用大模型自动生成受害者画像

# VOLTA窃密木马：窃取会话凭证，调用大模型自动生成受害者画像

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

思科Talos团队近期曝光一款名为 VOLTA（VOLTA-AUTODOXER） 的Windows窃密木马。和普通盗号工具不一样，它把AI变成了黑客的“情报分拣员”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K0BQx3Mcrmp1JCLrUiabdqhvib6hcstex6w5fXibLbjVfSz987gNF7jhiaxOKfUlJHGkJuficjTqic7vdP1QfEPHPESiauKrP5mZI0WNM/640?wx_fmt=png&from=appmsg)

*VOLTA 完整攻击链路（来源：Cisco Talos）*

**01**

**第一步：大范围收割账号会话**

VOLTA会抓取Windows终端里各类账号凭证：

✅ 浏览器Cookie、密码、银行卡信息；

✅ Discord、Telegram、Steam、Slack、Roblox ；

✅ 邮箱、微软OAuth令牌、SSH密钥、WiFi密码、加密钱包。

它还会利用窃取到的Gmail、外卖平台会话，从订单记录扒出受害者住址；查询Roblox道具估值。 依托绕过Chrome绑定加密的能力，拿到的会话令牌很多时候可以跳过密码、二次验证。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0Aicu6mF9gLaiaicGKYonzKia4AVG30EMRDfFo9iau4YVjqfAaYickicibWEZE8f9UOIG9icaHsg3NYSWCPUsShDWEL6SDxfGjKAuicibiaRI/640?wx_fmt=png&from=appmsg)

*木马最终打包的三类外泄数据包（来源：Cisco Talos）*

**02**

**核心亮点：AI自动做目标评估**

收集完信息后，木马生成一份受害者档案 Identity\_Report.txt，通过OpenRouter网关发给大模型分析。要求AI输出两大内容：

* 价值评级：低/中/高，标记受害者资产价值
* 安全评估：判断受害者的密码习惯、防护水平

调用顺序：Claude Opus 4.6 → 调用失败自动降级 Kimi K2 → Gemini 2.5 FlashAI分析结果保存为 AI\_Analysis.txt，打包成压缩包外传。

木马执行完成后会自删除，增加查杀溯源难度。

**03**

**黑产商业化：低门槛木马生成器**

VOLTA是一套售卖的木马生成工具（Builder）。攻击者填入API密钥、Telegram接收通道，就能一键生成定制木马。受害者的AI评估报告，直接推送至攻击者Telegram。没有固定C2服务器，防守方无法简单拉黑IP阻断。

**个人&企业防护建议**

**个人：**不明来源exe不要运行；怀疑中招，在干净设备上重置所有密码、吊销令牌；加密资产尽快迁移新钱包；

**运维：**管控Chrome无头--headless启动参数；安全设备导入IOC进行检测。

之前已有Dolphin-X尝试AI筛选受害者，VOLTA方案更加成熟，代表黑产AI武器化正在落地。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0LaNlPTMknj0Q8yBqyE0p2lyYbsKdloHFrm4OnoW0qFamPqNkCsicVHHKTibF2xiaSHslP99lWfPd9Mz84iacTSXn8dFFeiblQ1MV4/640?wx_fmt=png&from=appmsg)

*链接域名已脱敏，仅在情报平台内还原使用。*

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2pkHE6JPA9a4h7BzAichicxvuMJzVhP4WD2b88PMOUicVLiaF32UUqAEGHicnLnupiczbYC1zFu04J8X90XTq4ia1niaEFLH7JCX1Z1hE/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1139bszkA9vJXibWic49jNLf2okAP4F8suTkdYooV3mc3icme54P84p6VC8AYGff1k0xNfMZof994cfqoEx72L9XibaeWGice2vbsU/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K218iawlibXM59Ms7aNXVURU4QWbiaeHKcOjRauxVRIxMvjodiconrn6ncgmb6yvNw0TFYTrU1wYUibFZMXTYG5bFhE4LUThQLuYTw8/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K0swkt32pARrHq12OKfwhbm6ibdVXnBG5oo9DrMYo8F8hcc9icrrFibm9j9bFCukKJXH8upF5aroy0iazl7Iu2W070xoXvokKScuUo/640?wx_fmt=gif&from=appmsg)

**球在看**

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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