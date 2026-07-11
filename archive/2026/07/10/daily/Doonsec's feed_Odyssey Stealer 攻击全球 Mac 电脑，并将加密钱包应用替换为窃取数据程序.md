---
title: Odyssey Stealer 攻击全球 Mac 电脑，并将加密钱包应用替换为窃取数据程序
url: https://mp.weixin.qq.com/s/es1awLI1bAnJl-Zub3SYig
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T04:57:52.733417
---

# Odyssey Stealer 攻击全球 Mac 电脑，并将加密钱包应用替换为窃取数据程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7Mj5sAL5kS6zfr8IhRiadtYupvkEfHNRCuBC46OvNpGGyeh1zicbC705om2iatPjoM8sWw2KGbicXhOsXbcibhtsibgCLicm4pHjMQHjc/0?wx_fmt=jpeg)

# Odyssey Stealer 攻击全球 Mac 电脑，并将加密钱包应用替换为窃取数据程序

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Odyssey Stealer 正在发起一场大规模的 macOS 信息窃取活动，目前已蔓延至 100 多个国家/地区，攻击者通过用窃取加密货币的木马程序替换合法的钱包应用程序，系统性地劫持加密货币生态系统。

该行动结合了高级社会工程、基于 AppleScript 的隐蔽技术和持久的 LaunchDaemons，将受感染的 Mac 变成长期收集凭证、密钥和加密资产的点。

来自多家安全厂商的遥测数据显示，自 2026 年初以来， Odyssey Stealer 的活动持续增加，在北美、欧洲、亚洲和其他地区都观察到了感染，证实了其真正的全球影响力。

研究人员还注意到，重新命名与早期的波塞冬窃贼活动有关，这表明它是一种持续演变的病毒株，而不是一个独立的毒株。

Odyssey 的传播方式很大程度上依赖于“ClickFix”技术：受害者会被引导至虚假的 CAPTCHA 或验证页面，这些页面会验证操作系统，然后指示用户将 base64 编码的命令复制粘贴到终端中，该命令会在后台静默执行 AppleScript 加载器。

由于该恶意软件是基于脚本的，并且通常通过`osascript`而不是释放传统的二进制文件来运行，因此它最初可以绕过许多针对经典可执行有效载荷调整的端点防御措施。

一旦执行，Odyssey Stealer 即可跨浏览器和 macOS 原生组件进行广泛的数据采集。

Moonlock 研究人员表示，该活动主要针对 macOS，通过恶意广告和网络钓鱼攻击开发者、管理员、加密货币交易员和高管，冒充 Microsoft Teams、Homebrew、Ledger Live 和其他流行软件等可信工具。

它会系统地从基于 Chromium 的浏览器（Chrome、Brave、Edge、Vivaldi、Opera、Arc）以及 Firefox 系列变体中收集密码、cookie 和自动填充数据，从而实现对在线账户的完全接管和会话劫持。

与此同时，它还会攻击 macOS 钥匙串条目、支付信息以及桌面和文稿文件夹中的文件，包括 \*.txt、\*.pdf、\*.docx 等敏感格式文件以及 KeePass 等密码数据库文件。

## **Odyssey Stealer 攻击 Mac**

该软件以加密货币为中心进行设计，重点关注桌面钱包和浏览器扩展程序。目前的分析表明，它至少支持 16-18 款桌面钱包（包括 Electrum、Exodus、Ledger Live、Trezor Suite、Bitcoin/LTC/Dash Core 和 Monero），以及数百个 web3 钱包和 DeFi 插件的扩展程序 ID。

被盗数据会被暂存到存档中（通常`out.zip`位于`/tmp`），然后通过 POST 请求泄露到命令与控制服务器`curl`，并进行多次静默重试以确保即使在瞬态网络控制下也能交付。

除了凭证和加密之外，Odyssey 还会扫描 SSH 密钥、云和容器配置文件（AWS、GCP、Azure、Docker）、FileZilla FTP 配置文件、Telegram 和 Discord 数据、shell 历史记录以及使用 macOS 目录服务查询的本地账户密码。

这种广泛的收集表面使得受感染的主机对于横向移动、云账户入侵以及附属机构的二次变现都具有价值。

为了实现持久化，Odyssey 会将带有随机`com.<random>.plist`名称的 LaunchDaemon plist 文件放入`/Library/LaunchDaemons/`，然后使用`launchctl bootstrap system`来注册它们；如果注册失败，则回退 nohup 风格的循环会保持窃取程序运行。

这使得恶意软件能够在重启后继续运行，并与其 C2 服务器保持定期连接，以便操作员可以发出新命令或推送更新的配置。

其中最危险的行为之一是应用程序替换：恶意软件会杀死合法的加密钱包应用程序，例如 Ledger Live、Trezor Suite 和 Exodus，以提升的权限删除它们，并用从攻击者基础设施下载的木马化“吸血器”版本替换它们。

这些假冒应用模仿了原有的用户体验，同时提示用户输入 PIN 码和恢复短语，通过在人机界面层捕获秘密信息，有效地绕过了硬件钱包的安全机制。

Odyssey 还作为恶意软件即服务平台运营，拥有联盟会员可访问的管理面板和构建器，可生成自定义变种，并提供受感染主机、被盗密码、cookie 和钱包清单的仪表板。

来自 CloudSEK、CYFIRMA、Censys 等公司的研究人员发表了详细的分析和入侵指标，强调了严格验证软件下载来源、警惕要求终端命令的基于浏览器的验证码以及立即检查 macOS 系统上任何意外替换的钱包应用程序的必要性。

对于加密货币风险敞口较高或拥有大量 macOS 设备的组织而言，主动查找可疑的 LaunchDaemons、异常`osascript`使用和无法解释的应用程序替换，`/Applications`现在已成为对抗 Odyssey Stealer 持续全球攻击活动的关键控制措施。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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