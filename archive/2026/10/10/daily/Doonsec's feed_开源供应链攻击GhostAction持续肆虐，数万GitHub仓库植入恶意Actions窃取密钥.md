---
title: 开源供应链攻击GhostAction持续肆虐，数万GitHub仓库植入恶意Actions窃取密钥
url: https://mp.weixin.qq.com/s/9lCASxyJN6yJvR9kjSHvNg
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T08:00:27.315102
---

# 开源供应链攻击GhostAction持续肆虐，数万GitHub仓库植入恶意Actions窃取密钥

# 开源供应链攻击GhostAction持续肆虐，数万GitHub仓库植入恶意Actions窃取密钥

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

近期网络安全研究团队披露GhostAction大规模凭证窃取供应链攻击的最新进展：攻击者劫持多名知名开源项目维护者账号，向海量代码仓库植入伪装成安全审计的GitHub Actions恶意工作流，批量盗取CI/CD密钥、云服务、大模型API凭证。

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4Mz6M9sicY9DpylZc7QYgnAtacm1I73YSe5JpBiaZLibYmvTRkL8foPO5eYEOYzP06kY4AJaS3ImTEKUwbn3cnbRPMJEU2FfXIz4vib5iafZtm2eA/640?wx_fmt=svg&from=appmsg)

**攻击事件概况**

攻击者利用被劫持的高影响力开源维护者账号，在短时间内向数百个代码仓库推送恶意配置文件。

- 盗取`pyxel`游戏引擎作者账号，向27个仓库植入恶意工作流；

- 8小时后，劫持Uber Athena驱动原作者账号，仅16分钟就完成318个仓库投毒。

根据Socket监测数据，自10月7日起，已有超过500个GitHub账号向数万个仓库提交了这份恶意工作流。该攻击团伙GhostAction最早在2025年9月曝光，此前一轮攻击就影响327名用户的817个仓库，共窃取3325条密钥，涵盖PyPI、npm、DockerHub等包管理平台令牌。

🔴 恶意文件命名极具欺骗性，通常叫做 `security-audit.yml` 或 `github\_actions\_security.yml`，伪装成安全审计脚本，配置硬编码地址，把扫描到的敏感凭证通过HTTP明文外传至黑客服务器。

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7hwj6M2wGIOibzfEFV0ia3kia6Skkehbj9daEdnse3oAvRYaicsb7bcf4ozQcEJeLngr6iahlamfBL1PSicZ1ibuhOvia0iaHf58hTq8GKKiagNNfM4wrg/640?wx_fmt=svg&from=appmsg)

**恶意工作流的窃取能力**

一旦恶意Workflow被触发，会自动执行全套凭证搜集动作：

1. 读取仓库内所有GitHub Actions Secrets，也就是CI流水线配置的各类密钥；

2. 扫描当前代码目录，匹配13类敏感凭证规则，捕获AWS、OpenAI、Anthropic等云与AI服务商API密钥；

3. 遍历完整Git提交历史，挖掘曾经提交后又删除的密钥；

4. 自动配对AWS Access Key ID与对应的密钥，整理成完整可用凭证。

攻击可由代码推送、手动触发执行。除云、AI密钥外，该脚本还会搜集SSH私钥、Azure、容器仓库、数据库、FTP、GCP、Cloudflare、npm/PyPI、Slack/Telegram/Discord机器人令牌等大量敏感信息。

本次攻击还发现黑客在受害仓库Docker镜像中植入XMRig门罗币挖矿程序。目前暂未看到攻击者利用窃取的包发布凭证上线恶意软件包。

完整攻击链路拆解

1. 获取账号权限：黑客从盗号日志、凭证泄露库拿到维护者的GitHub个人访问令牌PAT，接管账号；

2. 前期侦察：扫描目标仓库工作流，探查仓库密钥配置情况；

3. 植入投毒：以仓库原维护者身份，向默认主分支提交伪装成安全审计的yml工作流文件；

4. 凭证外带：脚本内嵌入curl命令，采集密钥后直接发送到黑客控制的外部站点。

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6DpOUZLRy7h7fIqstyPjebk00xXRCibxibhhZGs2aCdrymrG0X1qe500qEzCBNVjeJOHw8emoJ7lzMRdDUEFbZjJQvGH7ibX5FhYEIfK9xzHxpg/640?wx_fmt=svg&from=appmsg)

风险提示与处置建议

仓库Fork副本同样存在巨大风险，被投毒仓库的派生副本（包括私有Fork）会继承恶意工作流。只要仓库开启GitHub Actions，后续代码推送就会触发凭证窃取。就算没有扫到密钥，每次执行都会向黑客回传仓库标识，帮助攻击者绘制可执行环境地图。

**开发者自查处置清单**

1. 检查2026年8月31日后仓库新增的 `security-audit.yml` / `github\_actions\_security.yml`；

2. 一旦发现恶意文件，判定账号/仓库存在失陷，立刻执行密钥轮转；

3. 吊销被泄露的GitHub个人访问令牌；

4. 删除所有分支中的恶意Workflow文件；

5. 同步检查该仓库全部Fork派生仓库，清理恶意文件。

*资讯来源：StepSecurity、Socket、GitGuardian公开安全研究报告*

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2M2GVU1ibOUDQYAorpf0DwUPpFOL6cVeVV2GUlrQF5daCE7SNKXBt51SgBGN3StQXArqszhicoPDKMu6CMza4hUMjePv0wJcRU4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/Cpo2XCpI7K33gQSEOruOL1u1sHVabOQQlTNibn42Nxjp1DFvo7SZd8X0aOiamZyqFRJgdicCJtvnG2KY6wYDdRPEzSFBHVOk0InT0HTc8zRAjk/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K2MrqWpH1qOuKjqswnAjWuSic5dgsTG3EQpmBDfhQMaLzeCVt7349XMxQwiaO30IdFhKrcdeMX4yEXNqibQTibrnCd1z3S8ZvpKSdE/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K0QNNiarUZxvdEcL1y7U3KtcPhibTFBxB7licia2lEHYABUkWibicosjIaItsV9WSFCjQgwxJJqTj4H4EHOG9Hx5FuAg9qsHNaUHbbJw/640?wx_fmt=gif&from=appmsg)

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