---
title: 【安全圈】恶意GitHub Actions工作流席卷数万开源仓库：窃取云凭证与AI密钥
url: https://mp.weixin.qq.com/s/Su-rslc7Zf46QnnmpO5khw
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:03.954801
---

# 【安全圈】恶意GitHub Actions工作流席卷数万开源仓库：窃取云凭证与AI密钥

# 【安全圈】恶意GitHub Actions工作流席卷数万开源仓库：窃取云凭证与AI密钥

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

窃取

**核心威胁快报**：供应链攻击团伙 GhostAction 死灰复燃。攻击者劫持高星开源维护者账号后，向数百个上游仓库及数万个下游 Fork 植入伪装成“安全审计”的自动化工作流，全量遍历 Git 提交历史，将 AWS、OpenAI、Anthropic 及各种云资产密钥明文回传到攻击者服务器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyF65YmZ5dRX4DwosPqYoYOhmZjYgcBGNxxibiah6n0AVgEUNud3O0ia4sIzNSg2Rz61icia67AGKvvM3jTiaic9aj7XnXMrLdNPgN1XWA/640?wx_fmt=other&from=appmsg)

## 🔍 顶流维护者账号失守：16分钟突袭318个仓库

根据安全机构 StepSecurity 监测，攻击始于 UTC 时间 13:20。攻击者首先控制了拥有 1.84 万 Star 的开源游戏引擎 `pyxel` 作者 Takashi Kitao 的账号，直接向其名下的 27 个代码仓库提交恶意工作流文件。

8 小时后，攻击规模呈指数级爆发。Uber 开源工具 `athenadriver` 原作者 Henry Wu（henrywoo）的账号沦陷。在 21:10 至 21:26 之间短短 16 分钟内，攻击脚本利用该账号一口气向 318 个代码仓库完成了恶意代码推送。

供应链安全公司 Socket 追踪确认，自 2026 年 10 月 7 日至 10 月 9 日期间，已有超过 500 个 GitHub 开发者账号被卷入同一恶意投毒网络，受害仓库累计达到数万个。

## ⚡ 偷天换日：伪装成安全审计的投毒机理

攻击者在提交的代码中将工作流命名为 `security-audit.yml`（Security Audit）或 `github_actions_security.yml`（GitHub Actions Security），利用自动化审计的名义降低维护者戒心。

该工作流具有极高的窃密针对性，执行逻辑如下：

* **全触发条件**

  ：监听 `workflow_dispatch`（手动触发）以及任意分支、任意 Tag 的无过滤 `push` 事件，几乎每次开发提交都会被动唤醒。
* **深度拉取历史**

  ：检出代码时指定 `fetch-depth: 0`，强制拉取整个仓库所有的历史 Commit，不仅搜刮当前分支，连同过往提交记录一并翻底。
* **全维度定向窃密**

  ：脚本系统化抓取当前仓库配置的 GitHub Actions Secrets、CI/CD 变量、AWS 凭证、OpenAI/Anthropic/OpenRouter 等主流 AI 接口密钥，以及 GitLab、DockerHub、PyPI、npm 访问令牌。
* **明文外连回传**

  ：搜集完毕后，数据通过裸 HTTP 请求直接 POST 回传至硬编码的攻击者 C2 服务器地址 `193.32.204[.]199`。

## 📦 辐射风险：下游私有 Fork 成为重灾区

GitGuardian 此前发布的追踪数据显示，仅在 8 月 31 日至 9 月 30 日期间，GhostAction 就曾向 373 个用户与组织的 772 个公开仓库发起试探，目标直指 2,577 组私钥与访问令牌。甚至在 8 月 30 日的一次篡改中，攻击者还将 XMRig 门罗币挖矿程序直接打包进了 `kuafuai/DevOpsGPT` 的官方 Docker 镜像。

当前最大的隐患在于下游派生项目。以 Henry Wu 账号下的 279 个 Fork 为例，每一个分支都同步继承了该恶意工作流文件。当企业或开发者私下拉取上游同步、或在私有 Fork 中开启 GitHub Actions 并触发构建时，存放在私有环境中的内部核心密钥就会瞬间泄露。

## 🛡️ 应急排查与处置清单

* **排查文件**

  ：检索所有仓库的 `.github/workflows/` 目录，核对是否存在 `security-audit.yml` 或 `github_actions_security.yml`。
* **封禁回传流量**

  ：在出口防火墙与安全组策略中阻断对 `193.32.204[.]199` 的一切出站连接。
* **吊销并轮换凭证**

  ：一旦发现工作流被注入或被执行过，默认所有历史 Secret 已完全泄露，需立即吊销相关的 AWS、OpenAI、GitHub Token、SSH 私钥并重新签发。
* **彻底清理分支**

  ：从所有活跃与历史分支中硬删除该工作流文件，并同步检查团队内部所有 Downstream Fork 与镜像仓库。

***END***

阅读推荐

[【安全圈】Let's Encrypt证书期砍至64天：明年2月生效，人工运维将失效](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079297&idx=1&sn=ff9aab4086a8d04641b631486818b637&scene=21#wechat_redirect)

[【安全圈】号称自研解密骗千万：应急响应厂商当黑客中间商被起诉](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079297&idx=2&sn=311d2c4daa23fddd601f8601c6c0d1dc&scene=21#wechat_redirect)

[【安全圈】npm包tensorlake投毒：内置Bun蠕虫狂偷AI凭证](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079297&idx=3&sn=e303e137d9e198d454eda66df7dbed73&scene=21#wechat_redirect)

[【安全圈】SonicWall曝10分满分漏洞：无需凭据直穿内网核心](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079285&idx=1&sn=40d7e7b43c34047213b376da287167d1&scene=21#wechat_redirect)

[【安全圈】大模型缓存LMCache曝严重0day：无补丁直接RCE](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079285&idx=2&sn=5e9f5b16350c4daf6a1e4984eaf8184b&scene=21#wechat_redirect)

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