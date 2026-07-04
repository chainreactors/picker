---
title: ChocoPoC 瞄准安全研究员：假的 PoC 仓库，真的是供应链攻击
url: https://mp.weixin.qq.com/s/QYTY5O_RQtUKJffd14kklg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:47:22.352725
---

# ChocoPoC 瞄准安全研究员：假的 PoC 仓库，真的是供应链攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nOo5YmK1PHyQAKmEO9guSXNezyRUH1z0rAHbSRdhFzQWezqDw7UOX6t5o7XKVgEyz63nYfDxetwjRiaMTM3Acoa3RdXDVexF7x75iaVS56r18/0?wx_fmt=jpeg)

# ChocoPoC 瞄准安全研究员：假的 PoC 仓库，真的是供应链攻击

原创

tcode
tcode

字节脉搏实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nOo5YmK1PHyO1DWTKCHfIM2P8K4uP3s0lTrQ5ibTBBm9A3w0G1PcQqM7DtLatyAXWahJ5CibPQVtMrEawXBltzSpXYxSoalRBn2GJXu2dZUH0/640?wx_fmt=png&from=appmsg)

    安全行业有一个非常真实的工作场景：新漏洞刚披露，研究员、红队、蓝队和安全厂商都在寻找公开 PoC，用来验证影响、编写检测规则、复核补丁效果。时间压力越大，越容易相信一个看起来“格式完整、代码正常、说明清楚”的仓库。

    ChocoPoC 事件正是利用了这种压力。

    YesWeHack 与 Sekoia 在 2026 年 7 月 1 日发布联合研究，披露攻击者通过伪装成漏洞 proof-of-concept 的代码仓库，向安全研究人员投递 Python 远程访问木马。BleepingComputer 在 7 月 1 日报道，多组武器化 PoC 仓库被发现用于投递 ChocoPoC；The Hacker News 在 7 月 2 日继续跟进，提醒研究人员不要运行可疑 PoC。

    这类攻击最值得警惕的地方，不是它用了多么“新”的技术，而是它精准击中了安全工作的日常流程：找 PoC、装依赖、跑脚本、看结果。

核心事实

    公开研究显示，ChocoPoC 伪装在与漏洞 PoC 相关的代码生态里，表面仓库可能看起来相对正常，真正的恶意逻辑则通过依赖链等方式进入执行环境。相关恶意程序被描述为具备远程访问、命令执行、敏感信息窃取等能力。

影响分析

    ChocoPoC 的真正价值，在于提醒安全团队重新审视“研究环境”和“生产环境”的边界。

    很多企业已经对生产系统上线、第三方软件引入、开源组件治理建立了流程，但研究员个人电脑、漏洞验证机、临时云主机、红队工具目录、CI 里的测试脚本，仍然可能处在灰色地带。它们不一定有严格准入，不一定有网络隔离，不一定有凭据最小化，也不一定纳入终端检测。

    攻击者瞄准安全研究员并不新鲜。因为研究员机器上可能有漏洞样本、扫描器配置、客户资产范围、云访问令牌、SSH 密钥、浏览器会话、报告草稿和内部聊天记录。对攻击者来说，拿下一台研究机，可能比正面攻击企业边界更划算。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nOo5YmK1PHxgI9vysxnshgS4f15HHNaZrzUlTAeJy70Y5KBKOsicjFfUCsxvbtibpxDN4Gxm6cBpEqW8iatkpSAsFRcaRu0S470WMGVvA61xyg/640?wx_fmt=png&from=appmsg)

    第一，把陌生 PoC 当作不可信代码，而不是“参考资料”。下载、安装依赖和执行脚本之前，先确认来源、提交历史、维护者身份、依赖变化和社区反馈。

    第二，建立独立沙箱。漏洞验证应优先在一次性虚拟机、隔离容器或受控云环境中完成，避免在办公主机、主力开发机或保存长期凭据的环境中直接运行。

    第三，限制网络出站。PoC 验证环境不应默认允许访问所有外部地址。能离线分析就离线，必须联网时也应记录并限制出站连接。

    第四，做依赖审查。不要只看主脚本是否“干净”，还要看依赖包、安装脚本、构建脚本、二进制扩展和自动执行逻辑。对新发布、低下载量、维护者不明的依赖保持额外警惕。

    第五，保护研究凭据。漏洞验证环境不要保存浏览器密码、云密钥、客户 VPN、生产 SSH 私钥和个人常用令牌。临时凭据要有短生命周期和最小权限。

    第六，将研究机纳入安全监控。安全团队不能因为“这是研究用途”就放弃 EDR、日志、基线和隔离策略。越是会运行陌生代码的机器，越需要明确防护。

事实、推测与观点区分

    事实：YesWeHack 与 Sekoia 披露了 ChocoPoC 针对漏洞研究生态的攻击；BleepingComputer 与 The Hacker News 在 2026 年 7 月 1 日至 7 月 2 日报道了该事件；公开资料称其通过伪装 PoC 与依赖链投递恶意能力。

    推测：目前公开信息不足以判断所有受害者范围，也不应把每个可疑 PoC 都直接等同于同一攻击者操作。

    观点：安全研究的速度很重要，但隔离、审查和凭据保护同样重要。越是热门漏洞，越要警惕“刚好有人发了可运行 PoC”的诱惑。

结语

    ChocoPoC 给安全行业上了一堂反直觉的课：有时你以为自己下载的是用来验证攻击的 PoC，实际上你正在把攻击带进自己的环境。真正专业的研究流程，不是跑得最快，而是在跑得快的同时，知道哪里必须踩刹车。

关键来源

• YesWeHack，2026-07-01，How vuln researchers were repeatedly targeted by trojanised exploits：https://www.yeswehack.com/news/chocopocs-vulnerability-researchers-trojanised-exploits

• BleepingComputer，2026-07-01 16:08 ET，New ChocoPoC malware targets researchers via trojanized PoC exploits：https://www.bleepingcomputer.com/news/security/new-chocopoc-malware-targets-researchers-via-trojanized-poc-exploits/

• The Hacker News，2026-07-02，New ChocoPoC RAT Targets Vulnerability Researchers via Fake PoC Exploit Repos：https://thehackernews.com/2026/07/new-chocopoc-rat-targets-vulnerability.html

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ia3Is12pQKnIPvX43Bm5RTfn38gGrVIvGtiaMrLfFqknYBzOd4wmQb1Ra7InwkMM5Ru09FTZ6ibhcLiagpiannxZdlA/0?wx_fmt=png)

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