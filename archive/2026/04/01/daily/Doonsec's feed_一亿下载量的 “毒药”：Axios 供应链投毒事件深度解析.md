---
title: 一亿下载量的 “毒药”：Axios 供应链投毒事件深度解析
url: https://mp.weixin.qq.com/s/2eJ7CHx-j6nLYTjkckUiag
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:29:00.895295
---

# 一亿下载量的 “毒药”：Axios 供应链投毒事件深度解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquMRPAic4IDGRSIyxnMfsToMO6e5cwk8yadnwCPQTqpM7wN4vfU6aMrCYWg12sxG1ZQUCF6IbmxKS4ZoBjX52YPpHXVESxw08mzE/0?wx_fmt=jpeg)

# 一亿下载量的 “毒药”：Axios 供应链投毒事件深度解析

原创

OOO
OOO

船山信安

![]()

在小说阅读器中沉浸阅读

紧急预警：2026 年 3 月 31 日，全球最流行的 JavaScript HTTP 客户端库 Axios（周下载量超 1 亿）遭遇严重供应链攻击，攻击者通过劫持维护者 npm 账号发布恶意版本，植入跨平台远程控制木马（RAT），影响数百万开发者与企业系统。本文将完整复盘攻击流程、技术细节、自查方法与防御策略，帮你全面掌握这起影响深远的安全事件。

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquPQJkewBAwm3HLU9wr7GxcPZDNB129iaeYuDHz4aJqEmficbonI0H80bFAA0icrhxr7HKqJUIFkbrxQrgvJNmL6GlcNFLz7c7eXZI/640?wx_fmt=png&from=appmsg)

---

# 一、事件速览：48 小时的 “完美犯罪”

2026 年 3 月 30-31 日，攻击者精心策划了一场针对 Axios 的供应链投毒攻击，整个流程如下：

| 时间线 (UTC) | 关键事件 |
| --- | --- |
| 3 月 30 日 05:57 | 发布**plain-crypto-js@4.2.0**（良性版本，建立信任历史） |
| 3 月 30 日 23:59 | 发布**plain-crypto-js@4.2.1**（恶意版本，含 postinstall 脚本） |
| 3 月 31 日 00:00-00:39 | 劫持 Axios 维护者 npm 账号，手动发布两个恶意版本：**1.14.1**（1.x 分支）、**0.30.4**（0.x 分支） |
| 3 月 31 日 03:00 | npm 官方紧急下架恶意版本，发布安全公告 |
| 3 月 31 日 08:00 | Axios 团队发布官方声明，确认账号被劫持，提供修复方案 |

核心影响：恶意版本在线约 3 小时，期间所有执行npm install axios且未锁定版本的用户均可能中招，涉及 Windows、macOS、Linux 全平台。

---

# 二、攻击链全解析：五步 “投毒” 流程

攻击者构建了一条账号劫持→依赖注入→混淆投递→远控植入→自毁灭迹的完整攻击链，环环相扣，极具隐蔽性。

## 1. 账号劫持：攻破 “守门人”

攻击者通过未知手段（推测为钓鱼或凭证窃取）成功入侵 Axios 核心维护者的 npm 账号，修改邮箱并绕过 GitHub Actions+OIDC 的可信发布流程，获得手动发布权限。这是整个攻击的起点与关键，没有账号控制权，后续一切操作都无从谈起。

## 2. 依赖注入：埋下 “暗桩”

恶意版本在package.json中添加了一个幽灵依赖（phantom dependency）：

```
"dependencies":{  "plain-crypto-js":"^4.2.1"}
```

这个包从未被 Axios 源码 import/require，唯一作用是在npm install时触发postinstall钩子执行恶意脚本。正常 Axios 通过 GitHub Actions 自动发布，而恶意版本是手动发布，绕过了自动化安全校验。

## 3. 混淆投递：伪装 “良药”

攻击者采用了双重伪装策略：

* 先发布良性版本plain-crypto-js@4.2.0，建立发布历史，避免 “全新包” 警报
* 恶意包命名模仿知名库crypto-js，降低警惕性
* 脚本使用混淆技术，增加静态分析难度
* 当用户执行npm install时，恶意依赖被自动安装并触发setup.js执行。

## 4. 远控植入：释放 “木马”

setup.js是攻击核心，执行以下操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquMKoVTWXM6vzRRlHsgnQpNhiaQYOxFq0ZK0ibkuWmPPy6R4ricrBVMtZyuBCQpXibicMO7ibaN1wbeEjW9VBapmHFrZpG3gcNLQCgO6g/640?wx_fmt=png&from=appmsg)

## 5. 自毁灭迹：抹去 “痕迹”

最狡猾的一步 —— 攻击完成后，恶意脚本会删除自身（setup.js）和恶意package.json，用良性版本文件替换，制造 “未被篡改” 的假象，清理日志，防止被事后溯源。

这导致受害者检查node\_modules时完全看不到异常，大大增加了检测难度。

---

# 三、技术细节：RAT 如何 “接管” 你的设备

## 1. 平台差异化攻击

攻击者针对不同系统设计了特定 payload：

| 系统 | 投递路径 | 伪装手段 | 恶意行为 |
| --- | --- | --- | --- |
| Windows | `%TEMP%\updater.exe` | 伪装系统更新程序 | 建立自启动，窃取浏览器凭证、SSH 密钥 |
| macOS | `/Library/Caches/com.apple.act.mond` | 伪装 Apple 系统缓存 | 利用 launchd 持久化，监控键盘输入 |
| Linux | `/tmp/.systemd-update` | 隐藏文件，设置 + wx 权限 | 植入 cron 定时任务，回传系统信息 |

## 2. C2 通信机制

恶意脚本通过 HTTP 协议与 C2 服务器通信，传输系统信息（OS 版本、CPU 架构、用户名）、已安装软件列表、网络配置还有窃取的敏感数据

C2 服务器http://sfrclak.com:8000在事件曝光后已被关停，但攻击者可能已收集大量敏感信息。

---

# 四、如何自查：你是否已 “中毒”？

## 快速检测三步法

检查 Axios 版本：

bash（命令行） 运行  npmlist axios 查看当前版本，若显示1.14.1或0.30.4，则已中招。

## 检查恶意依赖：

bash（命令行） 运行 lsnode\_modules/plain-crypto-js 存在则可能被感染

## 扫描系统残留：

## 深度排查建议

1. 检查近期npm install日志，查找plain-crypto-js相关记录
2. 监控网络连接，查看是否有异常 IP 通信
3. 检查系统自启动项、定时任务，删除不明条目

---

# 五、紧急修复：四步 “解毒” 指南

## 1. 降级并锁定版本

bash（命令行） 运行

* 1.x分支用户（推荐）

npminstallaxios@1.14.0

* 0.x分支用户

  npminstallaxios@0.30.3

在package.json中添加覆盖配置，防止间接依赖解析到恶意版本：

```
{"dependencies":{    "axios":"1.14.0"  },    "overrides":{// npm 8+      "axios":"1.14.0"    },  "resolutions":{// yarn      "axios":"1.14.0"   }}
```

## 2. 清理恶意残留

bash（命令行） 运行

* 删除恶意依赖

npmuninstall plain-crypto-js

* 清理npm缓存

npmcache clean--force

手动删除各平台残留文件，必要时重装系统（针对已确认感染的设备）。

## 3. 凭证轮换

立即更换以下敏感信息，防止攻击者进一步利用：

* npm/GitHub 令牌
* 云服务密钥
* SSH 密钥
* 数据库密码
* 浏览器保存的密码

## 4. 强化安全配置

启用 npm 2FA（双因素认证）

CI/CD 中添加--ignore-scripts参数，禁用自动执行脚本

使用私有 npm 镜像，审核后再同步外部包

定期审计依赖树，使用snyk等工具检测风险

---

# 六、供应链安全启示录

Axios 事件再次敲响警钟：开源软件供应链已成为黑客攻击的 “重灾区”，即使是周下载量超 1 亿的顶级库也无法幸免。

## 开发者应做的 3 件事

版本锁定：在package.json中明确指定依赖版本，使用package-lock.json/yarn.lock

脚本管控：默认使用--ignore-scripts安装依赖，仅信任必要脚本

依赖审计：定期执行npm audit，使用 Snyk、Dependabot 等工具监控风险

## 企业级防御建议

| 防御层面 | 关键措施 |
| --- | --- |
| 依赖治理 | 建立内部镜像仓库，实施包审核机制 |
| CI/CD 安全 | 启用工作流签名，限制发布权限，使用不可变基础设施 |
| 运行时防护 | 部署行为检测工具，监控异常网络连接与文件操作 |
| 应急响应 | 制定供应链攻击应急预案，定期演练 |

---

# 七、总结：安全没有 “免死金牌”

Axios 投毒事件是一次典型的供应链攻击，攻击者利用开源生态的信任机制，以最小成本获取最大攻击面。它提醒我们：在享受开源便利的同时，必须时刻保持警惕，不能将安全完全寄托于第三方。

## 行动清单：

* 立即检查并修复 Axios 版本
* 审计项目依赖树，清理可疑包
* 加强账号安全，启用 2FA
* 建立依赖安全管理制度

记住：安全是一场持续的战争，不是一次性的防御。在代码的世界里，最危险的往往不是那些显而易见的漏洞，而是隐藏在 “信任” 背后的暗箭。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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