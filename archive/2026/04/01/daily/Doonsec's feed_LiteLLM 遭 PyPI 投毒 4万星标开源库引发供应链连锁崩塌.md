---
title: LiteLLM 遭 PyPI 投毒 4万星标开源库引发供应链连锁崩塌
url: https://mp.weixin.qq.com/s/fvFrK4D1LUhBX3O4KeEmZQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:23:30.813242
---

# LiteLLM 遭 PyPI 投毒 4万星标开源库引发供应链连锁崩塌

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/J7CSmJcRR8lZLTVuhgHV68bnIGcmcqPANWiaCUUSESScobl4BOdDGCwHiboDNH6jMWoiatrD2kob3YdxlISYue5NGWv7k1gjLevravoHJZW96I/0?wx_fmt=jpeg)

# LiteLLM 遭 PyPI 投毒 4万星标开源库引发供应链连锁崩塌

TtTeam

![]()

在小说阅读器中沉浸阅读

编者荐语：

No

以下文章来源于Khan安全团队
，作者忍者

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6HvHSDXDlBxY0qXVHLH06BWXdlPIkic8a73R4oJ3j8MoQ/0)

**Khan安全团队**
.

安全不是一个人，我们来自五湖四海。研究方向Web内网渗透，免杀技术，红蓝攻防对抗，CTF。

如果你是 AI 开发者，或你的 Python 环境中已安装 LiteLLM、DSPy、Open Interpreter 等工具，请立即停止手中所有工作，优先运行 pip show litellm 命令，检查当前版本一场针对 AI 工具链的定点打击已全面爆发。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/J7CSmJcRR8lwPmibGTBogKWNKicMnBicaOOM6EmjyZpc259djJevZNef34bliacCjEibMEUhq5Bp12UgmmzcgHUkE2cRprtaR2J9NhIsafHPN0Ew/640?wx_fmt=png&from=appmsg)

今日（2026年3月24日），拥有 4 万 GitHub 星标、每月下载量逼近 1 亿次的知名开源库 LiteLLM，在 PyPI 官方仓库惨遭投毒。此次攻击不仅是对 AI 开发者生态的精准突袭，更迅速演变为一场教科书级别的供应链连锁崩塌事件，波及全球数百万开发者终端。

## 1. 投毒机制：安装即“中招”，无需调用，零门槛渗透

##

与传统恶意包需主动调用才能触发攻击不同，本次 LiteLLM 投毒利用了 Python 核心的 .pth 文件机制，实现了“安装即受控”的恐怖效果。

攻击者在 LiteLLM 的 1.82.7 和 1.82.8 两个版本中，恶意植入了名为 `litellm_init.pth` 的文件。在 Python 环境中，.pth 文件拥有极高执行权限：只要该版本 LiteLLM 被安装，无论你是否在代码中写入 `import litellm`，甚至是否调用过 LiteLLM 的任何功能，每次启动 Python 进程时，恶意代码都会自动执行——这意味着，你的机器从安装完成的那一刻起，就已彻底失控。

## 2. 恐怖扫描范围：精准收割开发者全量核心资产

##

恶意代码启动后，会像一台失控的“数据吸尘器”，系统性、无死角地扫描并窃取主机上的所有核心敏感数据，覆盖开发者工作与资产的方方面面

* 云端凭证：AWS、GCP、Azure 等主流云服务商的访问密钥，可直接掌控云端资源；
* 开发密钥：所有 SSH 密钥、Git 凭证、.env 环境变量文件，涵盖代码仓库、服务器访问权限；
* AI 资产：OpenAI、Anthropic 等所有大模型的 API Key，直接盗用 AI 服务权限；
* 基础设施：Kubernetes 配置文件、数据库密码、SSL 私钥，可渗透整个运维体系；
* 财富资产：甚至会扫描加密货币钱包文件与 Shell 历史记录，直指开发者个人财产。

更危险的是，恶意程序会自动检测运行环境：若发现受害者处于 Kubernetes 集群中，会立即利用服务账户令牌，尝试在集群每个节点部署特权 Pod，快速实现集群内部的横向移动，扩大攻击范围。

## 3. 破案纯属意外：攻击者的“致命 Bug”，终结潜伏阴谋

##

这场本可潜伏数周、收割海量敏感数据的“完美犯罪”，最终因攻击者自身编写的一个低级 Bug 意外败露。

FutureSearch 的研究员在使用 Cursor 编辑器搭配 MCP 插件时，触发了插件间接依赖的 LiteLLM 1.82.8 版本。由于恶意 .pth 文件会在每次 Python 启动时触发子进程，而子进程又会再次触发 .pth 文件执行，最终形成指数级增长的“Fork 炸弹”——直接导致受害者机器内存溢出、瞬间崩溃，这一异常现象迅速引发了安全社区的高度警觉。

正如特斯拉前 AI 负责人 Andre Karpathy 所言：“如果攻击者没有犯这个 Bug，这次投毒可能好几天甚至几周都不会被发现，后果不堪设想。”

## 4. 溯源：安全工具竟成“破门槌”，供应链闭环式沦陷

##

此次攻击最令人深思的，并非投毒手段本身，而是其攻击源头——攻击者团队 TeamPCP 并未直接攻破 LiteLLM 本身，而是绕过防线，利用安全工具实现了“曲线破局”，形成了极具讽刺性的攻击闭环：

* 3月19日：知名容器漏洞扫描工具 Trivy 率先被攻陷，攻击者获取了工具控制权；
* 连锁反应：LiteLLM 的 CI/CD 流程中，恰好使用 Trivy 进行代码安全扫描，攻击者借此窃取了 LiteLLM 维护者的 PyPI 发布令牌；
* 3月24日：攻击者利用窃取的合法令牌，向 PyPI 官方仓库推送了带毒的 1.82.7、1.82.8 版本，完成投毒。

开发者为保障代码安全而引入的扫描工具，最终竟沦为攻击者窃取权限、攻破防线的“内鬼”，这一闭环令人警醒。

## 5. 社区“肉搏战”：攻击者的灭口尝试，尽显组织性对抗

##

在 GitHub Issue 被爆出 LiteLLM 投毒行为后，攻击者并未仓皇逃离，反而展开了疯狂的“灭口”操作，上演了一场开发者社区的“肉搏战”：

攻击者动用 73 个被盗账号，在短短 100 秒内刷出 88 条垃圾评论，试图淹没真实的投毒反馈帖；同时，利用之前窃取的权限，强行关闭相关 Issue，试图掩盖攻击痕迹。这场有组织、有预谋的对抗，足以看出此次攻击背后的团队化运作特征。

## 6. Karpathy 的反思：少用依赖，多用 AI 搬运，警惕供应链风险

##

此次事件也引发了行业对软件依赖关系的深度反思，Andre Karpathy 借此发表观点，表达了对现代软件依赖生态的极度警惕

> “传统工程学告诉我们依赖关系是好的，像用砖块造金字塔。但我认为这需要重新评估。我越来越倾向于让大模型直接‘搬运’简单功能生成代码，而不是引入一个深不可测的外部包。”

每一个嵌套的依赖，都是一个潜在的后门；每一次随意引入的外部包，都可能成为安全隐患。在大型项目中，这种依赖链带来的安全风险，正呈指数级增长。

## 🛡️ 紧急处置清单

##

* 检查版本：立即运行 `pip show litellm`，确认当前版本；
* 版本界定：安全版本为 1.82.6 及以下，中毒版本为 1.82.7 和 1.82.8；
* 立即止损：若检测到中毒版本，默认你的所有敏感凭证（AWS、SSH、API Key 等）已完全泄露；
* 凭证轮换：立即更换所有敏感 Key、密码，撤销当前所有云端访问授权，防止进一步损失；
* 环境清理：卸载中毒版本，彻底清理 Python 站点包目录下的 .pth 残留文件；安装官方修复版（建议直接回退至 1.82.6 版本，或等待官方确认安全的 1.83.0+ 版本）。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

TtTeam

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0HlywncJbB32jygJerkpmJzM0Q4aia2A7YtEsw27852R0p5Henwz2TJL8iczQ5cPQm7y1Y6oM9dQocgyjsqO5VBg/0?wx_fmt=png)

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