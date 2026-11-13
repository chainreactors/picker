---
title: 【安全圈】4837个GitHub账号被盗！CI窃密席卷8093仓库
url: https://mp.weixin.qq.com/s/hXk51E7U_oq26W26ntKM_g
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:57:26.233238
---

# 【安全圈】4837个GitHub账号被盗！CI窃密席卷8093仓库

# 【安全圈】4837个GitHub账号被盗！CI窃密席卷8093仓库

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

GitHub

**核心事实**：2026 年 11 月 10 日 12:45 UTC 至 11 月 12 日凌晨，攻击者批量动用 **4,837** 个被盗 GitHub 账号凭证，向 **61,764** 个代码仓库发出试探性 Pull Request，随后向至少 **8,093** 个仓库默认分支推入名为 `wfx` 的 CI 窃密脚本。Aikido Security 确认至少 **1,806** 个仓库已执行载荷并外泄凭据，且攻击者多在 1 分钟内回滚提交并抹除工作流日志。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyFd4V4uA4oHMibvnvBoIOLBIvrqeCa99ia8G1eUHneOLG9icKzMNcMzjtRYcAvPxic7tDxFMndiagfyn7DllbCvKISicCjvrVicJXhQB4/640?wx_fmt=other&from=appmsg)

## 🔍 先发 PR 测权限，再分三路强推窃密载荷

攻击脚本先用受害账号的 noreply 邮箱批量生成无签名提交，从 `wfx-docs` 分支创建标题为 `docs: dependency audit notes` 的 PR 来探测写权限。全站检索显示此类试探 PR 超过 6.18 万个，其中 10,431 个通过协作者或组织成员权限打入他人仓库，截至今日仍有超过 91% 处于开启状态——只要仓库收到过这封 PR，对应提交账号的凭证就已经失守。

拿到写权限后，攻击者根据目标仓库结构切换三种投毒手法（SafeDep 统计区间为 11 月 10 日 12:46 UTC 至 12 日 04:36 UTC）：

* 📦 **劫持现有工作流（7,309 个仓库）**：以 `ci: refresh build cache` 提交向已有 GitHub Actions 配置文件追加约 1,500 行恶意步骤，借 `actions/github-script@v7` 转存运行时令牌并触发窃密。
* 💻 **植入 npm 安装钩子（771 个仓库）**：以 `chore: add ci helper` 提交写入 `.ci-xxxxxx.sh`，同时修改 `package.json` 的 `postinstall`，开发者本地跑一次 `npm install` 同样会中招。
* 🎯 **空仓库新建工作流（16 个仓库）**：先推入 `chore: initial commit`，再在 `chore/xxxxxxxx` 临时分支创建 `.github/workflows/build-audit-xxxxxx.yml`。

执行完毕后，自动化脚本往往在 1 分钟内提交 `ci: restore` 或 `ci: cleanup` 抹平代码差异，并删除 Actions 运行记录与日志。排查时不要指望翻到 `wfx-loot` 工件或缓存条目——工作流历史里出现跳号断档的 Run Number，才是确认载荷跑过的直接证据。

## ⚡ 1500 行脚本全栈收割：扫进程内存，还在云端埋后门

三条投递路径最终都指向同一份约 1,500 行、未做混淆且以 `wfx` 自称的 Shell 脚本（SHA-256：`89695abb392d5cfd4972672961e644bb46baa98aa1ed7173c2a2816c762735cf`）。它先在 Runner 上全量收集 `GITHUB_TOKEN`、`ACTIONS_RUNTIME_TOKEN` 与仓库全部 `secrets`/`vars`，接着直接扫描 `Runner.Worker` 与 `Runner.Listener` 进程内存，连同 AWS/Azure/GCP/K8s/npm/PyPI/SSH 配置、最近 100 次提交、AI 工具密钥（OpenAI、Anthropic、Gemini、Cursor、Copilot、Ollama 等）以及 `.env`/`*.tfvars`/`*.tfstate` 一并打包。遇到自托管（Self-hosted）Runner，还会读取云实例元数据、Docker 容器状态与 Runner RSA 参数。

更棘手的是它不满足于单次窃密，还会主动尝试云端提权与持久化，导致简单的“全量轮换密钥”彻底失效：

* 🔑 **OIDC 探测与多云接管**：为 AWS、Azure、GCP 签发 GitHub OIDC 令牌并换取会话（哪怕仓库表面未配云流水线也会试探），同时向 HashiCorp Vault 与 Kubernetes API 重放 OIDC 令牌。
* 💥 **AWS 信任策略篡改**：调用 `iam:CreateAccessKey` 生成长期访问密钥，并将关联 IAM 角色的信任策略改写为 `"Principal": {"AWS": "*"}`，向任意 AWS 账号敞开大门（会话名为 `wfx-<pid>`）。
* 🌐 **Azure 联合身份注入**：持 Microsoft Graph 令牌向 Entra 应用注册写入名为 `wfx-ci-<n>` 的联合身份凭据；日后即便管理员重置所有客户端密钥，受害仓库 `main` 分支工作流仍可免密认证进入 Azure。

本轮已捕获样本关闭了私有仓库缓存与工件暂存开关，全部打包数据经 HTTP POST 外传至 `194.150.166[.]244:8080/exfil`、`18.143.168[.]96:8080/exfil`、`153.75.82[.]159:8080` 或 Telegram 频道。值得注意的是，今年 10 月 GhostAction 行动失陷账号在本轮中招的概率高出普通账号约 1,000 倍，百余个仓库里甚至能看到 11 月新载荷与 10 月回传地址（`193.32.204[.]199`）叠床架屋地并存——陈旧失陷凭据正在黑产圈层间二次流转。

## 🛡️ 投毒开源包清单与企业自查动作

虽然攻击主要瞄准 CI 密钥而非大规模供应链投毒，但自动发版流水线仍让三款组件携带恶意文件进入公共包仓库，另有 28 个 WebdriverIO 仓库被劫持了 `wdio-bot` 账号提交代码：

* ⚠️ **Packagist 组件 `digitalelvis/neuronai-studio` v3.14.3**：未改 PHP 代码，但包含 `.ci-e5infq.sh` 与 `postinstall` 钩子。单独执行 `composer require` 不会触发，但在其依赖目录运行 `npm install`/`npm ci` 会立即执行载荷，请强制回退并锁定至 `<= 3.14.2`。
* ⚠️ **Go 模块代理受波及版本**：`github.com/vkuznet/gocurl`（`v0.0.0-20261111095532-8d5aad0cb0da`）与 `github.com/onuragtas/redock`（兼 `docker-env` 的 `v1.0.278`、`v1.0.280`、`v1.0.282`）仅工作流文件被注入，Go 编译不会运行它们，但仍应在私有代理中拉黑对应伪版本与 Tag。
* ✅ **立刻执行排查与凭证清理**：检索组织内 11 月 10 日起是否存在 `wfx-docs`、`chore/[a-z0-9]{8}`、`ci-check-[0-9]{4}` 分支及缺失的 Actions 运行编号；一旦命中，除全量轮换 GitHub PAT、CI Secrets、AI 密钥与自托管 Runner 凭据外，务必同步核查 AWS IAM 信任策略与 Entra ID 中以 `wfx-ci-` 开头的联合身份凭据。

***END***

阅读推荐

[【安全圈】微软11月修1259洞！Outlook零日盗取NTLMv2](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079834&idx=1&sn=87414c25c31b4e94e839597e00255ff4&scene=21#wechat_redirect)

[【安全圈】Railway遭AI代理穿透！10万工作区泄密烧掉74万美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079834&idx=2&sn=f9a3ec5c78818d7d7509c38d4e00528b&scene=21#wechat_redirect)

[【安全圈】iOS零日沙盒逃逸曝光！iOS27.2.1仍可跨应用窃密](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079834&idx=3&sn=9f5233b9da2385dbe4ce4527012d3c10&scene=21#wechat_redirect)

[【安全圈】云商被黑连累FireworksAI！模型权重与密钥遭窃](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079821&idx=1&sn=4deb7108dc0f96ae2b0f2c738718402e&scene=21#wechat_redirect)

[【安全圈】SSHole与GPUStack遭在野利用！CISA急列四漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079821&idx=2&sn=38d64841709704b9cc08a0e06921010e&scene=21#wechat_redirect)

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

阅读原文

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