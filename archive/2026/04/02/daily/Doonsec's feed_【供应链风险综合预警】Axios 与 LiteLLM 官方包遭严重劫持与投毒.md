---
title: 【供应链风险综合预警】Axios 与 LiteLLM 官方包遭严重劫持与投毒
url: https://mp.weixin.qq.com/s/t1c3gZVClGGgOapCZpymtQ
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:24:33.447969
---

# 【供应链风险综合预警】Axios 与 LiteLLM 官方包遭严重劫持与投毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gianlj61NfozeyaYsUkMdAIwOzdWibLq3lTe08YCTicV1vbTSeyANQbeN4bxgBJFvW63BibH2TKbNBwZHg0LrYuY9fOszm9eZWt66Ku3ATFGW6w/0?wx_fmt=jpeg)

# 【供应链风险综合预警】Axios 与 LiteLLM 官方包遭严重劫持与投毒

值得信赖的
值得信赖的

默安科技

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/PRUwRKvusicPXQhp9NVSkXZZN8WZYye6Dfacb5bbPNt9PkOGMzlTsHgTPicPZQW4PyxTgjRS4ib2lSqiaO9IXKATXQ/640?wx_fmt=gif)

**01 漏洞简介**

2026年3月底，开源生态接连爆发两起极具破坏性的供应链劫持事件，分别重创了 JavaScript/Node.js 生态的核心基础设施 **Axios**以及 Python/AI 生态的热门组件**LiteLLM**。

**• Axios 事件（NPM 生态）：**3月31日，由于维护者账号被盗，攻击者在官方包中植入隐藏依赖。在两小时的攻击窗口内，向执行 `npm install` 的机器部署了跨平台远程访问木马 (RAT)，实现对 Windows、macOS 和 Linux 系统的完全控制。

**• Lite****LLM 事件（PyPI****生态）：****3**月24日，因 CI/CD 流水线中的安全工具（Trivy）遭投毒导致发布凭证泄露。攻击者（TeamPCP）发布了带有高危后门的版本，利用 Python 的 `.pth` 启动钩子机制，在开发者启动解释器时静默窃取本地、云端（AWS/GCP/Azure）及 Kubernetes 凭证，并具备 K8s 特权蠕虫扩散能力。

两起事件的恶意版本均由官方合法途径发布，能够绕过常规的哈希完整性校验。

**02 影响版本与攻击窗口**

| **生态/语言** | **受污染包名** | **恶意版本号** | **攻击窗口期 (UTC)** | **安全建议** |
| --- | --- | --- | --- | --- |
| **NPM (JS)** | `axios` | **`1.14.1`** | 3月31日 14:00 - 16:00 | 回滚至 `1.14.0` |
| **NPM (JS)** | `axios` | **`0.30.4`** | 3月31日 14:00 - 16:00 | 回滚至 `0.30.3` |
| **PyPI (Python)** | `litellm` | **`1.82.7`** | 3月24日 10:39 - 13:38 | 回滚/锁定至 **`1.82.6`** |
| **PyPI (Python)** | `litellm` | **`1.82.8`** | 3月24日 10:39 - 13:38 | 回滚/锁定至 **`1.82.6`** |

**⚠️ 风险提示⚠️**

**Axios 版本陷阱：**

攻击者特意选择了 `1.14.1` 和 `0.30.4`，极易误导开发者认为是常规补丁。若 `package.json` 使用了 `^` 符号且在此期间构建，极大概率已中招。

**LiteLLM 隐蔽触发：**

`1.82.8` 版本利用了 `.pth` 机制，**无需代码主动****`import`**，仅执行 `pip install` 或启动 IDE 的 Python 语言服务器即可导致失陷。

**03 修复与处置方案**

###

**方案一：依赖强制回滚（紧急止损）**

###

**• 前端/Node.js 项目：**清理缓存 (`npm cache clean --force`)，并在 `package.json` 中配置 `overrides` (NPM) 或 `resolutions` (Yarn) 强制覆盖子依赖，防止恶意 Axios 版本被间接引入。

**• Python/AI 项目：**严格检查 `requirements.txt`、`Pipfile.lock` 或 `poetry.lock`，将版本写死为 `litellm==1.82.6`。

**方案二：凭证全面轮换与环境重构（极度重要）**

###

单纯卸载恶意包无法清除上述两起事件植入的持久化后门。若在攻击窗口期内拉取过受影响版本：

必须立即吊销并更换该机器/容器内接触过的所有敏感信息：包括云服务凭证（AccessKey）、数据库密码、API 密钥和 SSH 私钥。

对失陷的开发机、CI/CD 构建节点建议进行系统级重装或重新拉取干净的容器镜像。

**方案三：失陷指标 (IoC) 联合排查**

请网络与安全运维团队在网关及主机侧排查以下特征：

**• 恶意通信域名：** `sfrclak[.]com:8000` (Axios C2), `models.litellm.cloud`, `checkmarx.zone` (LiteLLM C2)。

**• Axios 异常行为：**恶意 IP `142.11.206.73`，macOS 异常路径 `/Library/Caches/com.apple.act.mond`，或异常的 `osascript` / `codesign` 强制签名行为。

**• LiteLLM 异常行为：** 异常文件 `site-packages/litellm_init.pth`、`/tmp/tpcp.tar.gz`，伪装的 systemd 服务 `sysmon.service`，以及 Kubernetes 中异常的 `node-setup-*` 容器。

**04 资产排查工具支持**

**• 雳鉴SCA（软件成分分析）：** 已紧急录入 Axios (`1.14.1`, `0.30.4`) 与 LiteLLM (`1.82.7`, `1.82.8`) 恶意版本的特征指纹。支持秒级定位企业内部所有受影响的前端、后端及 AI 业务线代码库与镜像。

![](https://mmbiz.qpic.cn/mmbiz_png/Gianlj61NfozM0m9iag2eznJk7m8icBEKdkmYZHPERXE9AqjuPhWhEgJlOItiaicxOwYkib0vYVoVKSffUd8kUko0Duzt8tjUQfeqjDaicuFEtib73g/640?wx_fmt=png&from=appmsg)

**05 其他近期受影响恶意组件清单(SCA均已支持检测)**

##

| **恶意包名 (Package Name)** | **受影响版本 (Compromised Versions)** |
| --- | --- |
| **litellm** | `1.82.8`, `1.82.7` |
| **axios** | `1.14.1`, `0.30.4` |
| **spectra-suite** | `1.0.0`, `2.0.6` |
| **trade-in-lib** | `99.9.0`, `99.9.1` |
| **bs58-basic** | `6.0.0`, `6.0.1` |
| **babel-plugin-fbtee** | `99.9.1` |
| **strapi-plugin-nordica** | `1.0.0`, `3.6.8`, `3.6.10` |
| **strapi-plugin-nordica-sync / lite / tools** | `3.6.8`, `3.6.9`, `3.6.10` |
| **@apollolibraryorg/dotenv** | `1.0.1` |
| **@uallianceorg/dotenv / config** | `1.0.0` |
| **@disallianceorg/dotenv** | `1.0.0` |
| **@allianceorg/dotenv** | `1.0.0` |
| **prettlog** | `1.0.3`, `1.0.5` |
| **youpin-pc / mi-account** | `99.0.0` |
| **penny-core / selene-fn / ripio-fn / talos-fn** | `99.0.0`, `99.0.1`, `99.0.2` |
| **super-useful-utils** | `1.0.4`, `2.0.4` |
| **strapi-plugin-sitemap-gen** | `3.6.8` |
| **fe-utils-core** | `1.0.0`, `1.0.2`, `1.0.3` |
| **raydium-bs58** | `1.9.7` |
| **base-x-64** | `0.0.5`, `0.0.6` |
| **base-or****-engine** | `1.0.0` |
| **jonas-prettier-logger** | `1.0.0`, `2.0.1`, `2.3.4`, `3.1.0`, `3.4.3`, `4.3.0`, `5.2.0` |
| **jellyfi-pino-pretty-logger** | `1.0.3` |
| **bign.tsm** | `8.0.5`, `8.0.6` |
| **npmjs-doc-builder / npm-scanner** | `1.0.0`, `1.0.1` |
| **separadordeinfocc** | `1.0.0` |
| **nodecheck-health** | `1.0.0`, `1.0.1` |
| **hosts-reader-ctf-demo-xyz** | `1.0.0` |
| **argon2-napi** | `1.0.0` |
| **js-logger-pack** | `0.0.1`, `1.0.0`, `1.1.0`, `1.1.1`, `1.1.2` |
| **cms-site-api-js-client / stats-api-js-client** | `99.9.1` |
| **strapi-plugin-guardarian-ext / blurhash** | `3.6.8` |
| **moltbook-health** | `1.0.0` - `1.0.16` (全版本) |
| **moltbook-api-helper** | `1.0.0`, `1.0.1` |
| **@logforge / @logcore / pino-pretty-logger** | `2.1.0`, `2.4.0`, `2.8.0` |
| **tailwindc****ss-fonttype-i****nter** | `2.3.1`, `2.3.2` |
| **strapi-plugin-health-check / content-sync / cms-tools** | `3.6.8` |
| **strapi-plugin-hextest / debug-tools / finseven** | `3.6.8` |
| **openai-async-helpers / pygithub-async-utils** | `0.0.1` |
| **kube-health-tools** | `1.0.0` - `1.0.14`, `2.0.0` |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PRUwRKvusicMtGCo8BKXNic4OSw52pibHc7q6Xfo674pm4jBtG6PPhPhFsoo8gOufRBTuXayugM3suOVu5icscy9Rw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PRUwRKvusicM3mp5V1Px2I3MicXWA4DM20ibEWeiaXn0LTl6KftPyLPSfiaJDDqhcwbzN8AlQ7uA7mLGAicxPSfpOflQ/0?wx_fmt=png)

默安科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PRUwRKvusicM3mp5V1Px2I3MicXWA4DM20ibEWeiaXn0LTl6KftPyLPSfiaJDDqhcwbzN8AlQ7uA7mLGAicxPSfpOflQ/0?wx_fmt=png)

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