---
title: 【安全圈】点了「别再问我」，Claude Code 把密钥写进了公开仓库
url: https://mp.weixin.qq.com/s/60lVpwuoxSwx1cF7-tyTuw
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:13.878707
---

# 【安全圈】点了「别再问我」，Claude Code 把密钥写进了公开仓库

# 【安全圈】点了「别再问我」，Claude Code 把密钥写进了公开仓库

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

密钥泄露

**核心事实**：安全公司 Apiiro 在公开 GitHub 上扫到 104,185 份 `.claude/settings.local.json`，其中 1,122 份至少藏着一个明文密钥，合计 1,379 个。数据库密码 379 个，公网服务器 SSH 登录 43 个，GitHub / GitLab / npm 令牌 42 个，AWS 密钥 23 个。涉及 63 家组织，包括一家数据库厂商自己的管理员级云密钥，和一套医疗记录库的 owner 密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyHydCvfVC3yg9eFKCcWu2icOPtexyg2icRKUMAqZky5JpvJEyfwcd3newhbOOVzzGqgwYRJInOticzkmVZBib2vR8gKC1saRWGibAX8/640?wx_fmt=other&from=appmsg)

## 🔍 一条授权规则，把密码原文留在了 JSON 里

Claude Code 默认在执行大部分 shell 命令前弹窗确认。弹窗里有三个选项，中间那个是「Yes, and don't ask again」。点下去之后，这条命令会被写成一条允许规则，落盘到项目内的 `.claude/settings.local.json`。

问题出在规则覆盖的范围。弹窗给的是模式时，存下来的是模式，比如 `npm test *`，这没问题。弹窗给的是一条完整命令时，存下来的就是那条完整命令，包括里面敲进去的密码和 token，一个字符不改，明文。

* **典型形态**

  ：`PGPASSWORD=真实密码 psql -h 公网地址 -U admin`，或者 `sshpass -p 真实密码 ssh root@公网IP`
* **复现确认**

  ：研究人员用最新的 Opus 5.5 和 Fable 5.1 都复现了该行为，说明这不是旧版本的遗留问题
* **横向对比**

  ：研究人员比对了 16 个编码 agent 的公开文档，Claude Code 是唯一被确认「默认把完整命令原文写进项目配置文件」的

## 📦 104,185 份文件，1,122 份带着密钥

Apiiro 在 103,617 个公开仓库里找到 104,185 份该文件，达标率约 1.1%。判定一个值是密钥，要同时满足两条：格式匹配已知密钥类型，或者密码 / token 旁边写着公网服务器地址；再由一个 AI 复核员点头。

* **超过三分之一直连数据库**

  ：379 个数据库密码，拿到就能连库，不需要任何前置条件
* **历史版本更难追**

  ：509 个仓库的旧版文件里另有 734 个密钥，当前版本已经看不到，git 历史里还在
* **fork 会连坐**

  ：74 个仓库的 211 个 fork 带着和上游一模一样的密钥
* **团队共享配置也中招**

  ：76,011 份 `.claude/settings.json` 里 298 份含密钥。这个文件是团队主动提交的，密钥大多写在允许规则里面
* **总账**

  ：算上旧版本和 agent 聊天日志存档，共 2,539 个密钥散在 1,994 个仓库

截至本周一，所有含密钥的文件都还躺在默认分支上；其中一半仓库里，这份文件已经存在了至少 217 天。研究员通知的一家公司在几天内确认，它的密钥当时仍然有效。

## ⚠️ git 的自动保护，只保护了一台机器

Anthropic 确实做了防护。Claude Code 第一次往 git 仓库写这个文件时，会把它加进本机的全局 git excludes，于是这台电脑上的所有仓库都会忽略它。

这条防护的边界很窄：它只存在于一个人的 git 配置里，只作用于一台机器。已经提交过的文件，它管不了。Claude Code 也不会把该文件写进项目自己的 `.gitignore`，所以这份保护不随项目走。

更直接的数据：在研究人员追到提交记录的 1,105 个仓库里，有 539 个是由「Claude 作为共同作者」的那次 commit 改动该文件的。换句话说，近一半情况下是 Claude 自己把这份文件提交上去的。

这件事不是没人报过。2025 年 8 月 11 日，GitHub issue #5544 明确指出「批准过的命令连同 API key、token 被逐字存进 settings.local.json」。2026 年 1 月 3 日，自动机器人以「not planned」把它关闭，理由是 60 天无活动。研究人员引用的四条相关报告，全部由同一个机器人关闭，最早的一条就在前一天，Anthropic 一条回复都没有。

## 🕳️ 扫描器漏掉 215 份

研究人员拿 gitleaks 和 TruffleHog 把每一份文件跑了一遍，关掉工具自带的验证环节。结果：gitleaks 命中 564 份，TruffleHog 命中 643 份，两家都没报出 215 份。

漏掉的大多是命令里手打的口令。扫描器找的是已知密钥格式，而 `PGPASSWORD=` 后面那串字符、`sshpass -p` 或 `mysql -p` 后面那串，在规则眼里只是普通命令行里的普通单词。

## 🛡️ 先轮换，再清理

顺序很重要。文件从仓库里删掉，不等于泄露被撤销，历史版本和 fork 里都还在。先改密码，再谈清理。

* **1. 全组织搜文件名**

  ：在 GitHub 组织内搜 `.claude/settings.local.json` 与 `.claude/settings.json`，并翻每个仓库的 git 历史，文件已经删掉的也要翻
* **2. 轮换全部历史密钥**

  ：凡是这份文件碰过的密码、token、key，一律重签，包括已经失效又没删干净的
* **3. 停止跟踪并补 .gitignore**

  ：`git rm --cached .claude/settings.local.json`，再把该路径写进仓库自己的 .gitignore
* **4. 清理本机规则**

  ：即使从未提交，也打开本机这份文件，删掉所有含密钥的规则条目
* **5. 用变量替代字面量**

  ：把 `$DB_URL` 这类引用交给密钥管理器注入，规则里只会留下变量名
* **6. 批准模式而不是单条命令**

  ：写成 `Bash(npm run:*)` 这种通配，别让弹窗记住那条带密码的原命令

对企业安全团队还有一条：把 `.claude/`、`.cursor/`、`.gemini/`、`.specstory/` 这些 agent 目录当成 `.env` 同级对待，写进组织级 .gitignore 模板，并纳入 pre-commit 与 CI 扫描，同时确认扫描规则能抓到命令里的口令，而不只是已知密钥格式。

这些文件即使从没上过 GitHub 也仍然要紧。它就是项目目录里一份明文 JSON，会跟着 npm 包、Docker 镜像、zip 压缩包和同步盘一起走。2025 年 9 月的 Shai-Hulud 蠕虫就在被感染的开发机上跑 TruffleHog，当时扫出过半文件含密钥。

***END***

阅读推荐

[【安全圈】Chainalysis 被打穿：全体用户凭据泄露](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079722&idx=1&sn=cbb0f9bdab2358a4b513dad213c41288&scene=21#wechat_redirect)

[【安全圈】隐形后门寄生 CWP 面板，访问日志全程沉默](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079722&idx=2&sn=0ffae3851bf87f1c5fcafe01d9a44a92&scene=21#wechat_redirect)

[【安全圈】Barracuda 网关双漏洞链：免登录直取 root](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079722&idx=3&sn=c41a23a7212e4cf43702e04774a897e0&scene=21#wechat_redirect)

[【安全圈】白宫专网被卖做代理？总统办公室设备疑遭植入后门](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079711&idx=1&sn=05bdbc8ba75d9805145596493772fbf6&scene=21#wechat_redirect)

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