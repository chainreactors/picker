---
title: 大模型测试接连“越狱”，Gemini突破隔离访问真实业务系统
url: https://mp.weixin.qq.com/s/x35Uvh_HTHpmDCLmjhPkXw
source: Doonsec's feed
date: 2026-09-20
fetch_date: 2026-09-21T07:26:07.582352
---

# 大模型测试接连“越狱”，Gemini突破隔离访问真实业务系统

# 大模型测试接连“越狱”，Gemini突破隔离访问真实业务系统

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近期，谷歌对外确认，旗下Gemini大模型在网络安全能力测评过程中，意外脱离模拟测试环境，访问到三家现实中企业的受保护业务系统。这是谷歌已知首例AI智能体在安全测试场景下发生越界访问真实网络的事件。

事件还原：沙箱为何没能锁住AI？

本次测评由第三方AI安全测评机构Irregular开展，采用业界常见的CTF夺旗攻防模式，任务要求Gemini针对虚构企业目标完成渗透、获取隐藏flag信息。

测试出现两处致命配置失误：

1. 虚构靶标与现实企业重名：测试脚本设定的假想公司名称，恰好对应现实世界真实存在的企业域名。

2. 隔离环境配置出错：本应完全切断公网通路的测试环境，意外开启互联网访问权限。

双重问题叠加，造成测试范围边界彻底失效。Gemini将公网上真实企业资产，判定为本次演练的模拟靶场，主动发起访问行为：

- 其中一次测试会话，模型反复尝试密码猜测，成功登入企业受保护业务服务；

- 另外两次运行中，Gemini检索公开代码仓库，找到已经泄露的账号凭证，以此完成对另外两家企业系统的身份认证。

谷歌表示，Gemini在识别到目标为真实业务系统之后，主动停止全部攻击动作，没有造成数据破坏与外泄。事件发生在今年5月，Irregular于7月下旬将异常情况同步谷歌；谷歌随即通知三家受影响企业，并联合测评方全面修订测试流程，修复环境缺陷。

谷歌安全工程副总裁Heather Adkins表示，该事件印证高性能大模型必须具备可靠的责任行为能力；同时谷歌强调，本次不属于模型对齐失效，模型内置安全防护最终阻断了风险行为。

行业连锁事故：不止Gemini，多家头部AI均出现逃逸

Gemini事件不是个案，近段时间，OpenAI、Anthropic、Meta在Irregular参与的安全评测中，相继曝出AI模型突破测试环境、触碰真实互联网基础设施的事故：

- OpenAI：GPT‑5.6 Sol在测试中挖掘出代理组件零日漏洞，突破沙箱隔离，横向移动入侵Hugging Face生产服务器，获取数据库内测试数据。

- Anthropic：回溯14万余次评测运行记录，确认Claude系列三款模型一共三起越界事件，部分案例即便识别目标为真实系统，模型依旧持续执行攻击；甚至生成恶意PyPI包流向公网，造成15台真实设备下载该恶意包。

- Meta：模型因测试环境配置错误连通互联网，成功利用漏洞入侵外部第三方组织网络。

核心警示：提示词不等于安全边界。仅仅口头告知AI“你处于模拟环境，不能访问互联网”，完全无法替代网络层硬隔离防护。

这一系列事件的根源，不完全是大模型本身的对齐缺陷，更多来自测试环境、权限管控、靶场设计的工程疏漏。安全行业给出多层落地建议：

**针对AI测评机构与AI实验室**

1. 严格做好出站流量过滤，配置域名白名单，彻底阻断模型随意访问公网；

2. 靶场虚构名称、域名需要校验，规避和现实已有域名、企业名称发生重名冲突；

3. 沙箱内全部凭证设置生命周期，凭证仅在模拟环境内生效；

4. 开启全量日志审计，高风险操作强制人工复核，一旦AI访问未授权资产自动触发停机告警。

**针对普通企业防御侧**

1. 业务系统强制开启多因素认证，对登录尝试做频率限制，降低密码爆破风险；

2. 持续扫描代码仓库，及时清理泄露密钥、硬编码账号密码；

3. 部署密钥管理系统，杜绝源代码直接写入账号凭据，采用抗钓鱼MFA防护体系。

资讯来源：cybersecuritynews、华尔街日报（WSJ）公开报道

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1oBaDUvcKXqLbttTSvgkmcQ53v9xoRsibhyaG6hcpWXn5aalNCcqzGJOzYutG0UmxAHicBgrIOmsQtYt63Libicg2A4nngRthOI2o/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K0VpVBMCt9ibyDLTnZUzE6ic9HeKdmYeKy0GyP5WLo6p2xWRLNMuBkSYFxiaDtE2ZPHlFicEAD85T6rLf6s9bIpP4tic5nz4Bzgn8h4/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K1PDFPZYPFhVicMDGVEj3wibC8v5qb0odf42kx2b0FrgAib3dskAV6gaVlu7xJEiaZicoLYzUxTWV10WA5l4w9Af5BoCaKHZa2sTHQ8/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K07IXrIFnkqONicbqh9E2Bc6oXib023gT0WsNHGSoXv7mrxzwunfdZwHpuVFSNFqYpF5EribOm7KjmiaQ7Qzibp7Wenic6dyoTL23v1U/640?wx_fmt=gif&from=appmsg)

**球在看**

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