---
title: 全球安全动态日报｜20260926｜早
url: https://mp.weixin.qq.com/s/fO4J8sHJWbSX6h0vCFOapg
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:38.178402
---

# 全球安全动态日报｜20260926｜早

# 全球安全动态日报｜20260926｜早

安全资讯
安全资讯

一个不正经的黑客

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# 全球安全动态日报｜20260926｜早

本期整理昨日公开的全球安全动态，并同步收录 HackerOne 昨日公开且获得赏金的漏洞报告。

The Hacker News：

2026年9月25日共收录9条安全动态，内容涵盖移动设备漏洞、恶意软件活动与云服务及软件漏洞遭利用。

The Hacker News **9**  ·  HackerOne **0**

## The Hacker News

### 01 OnePlus 未修复漏洞可让已安装的 Android 应用在无权限情况下获得 Root 权限

**公开时间：**2026年09月25日 02:10

AI 解读

研究人员Rasmus Moorats披露，未修复的两个OnePlus系统漏洞可被已安装的恶意应用串联利用，在无需申请特殊权限或提示用户的情况下取得设备Root权限。漏洞分别存在于以Root运行且未验证调用者的AtlasService，以及允许Root调用者执行任意Shell命令的olc2服务；前者先获得受限Root权限，后者再将权限提升至可加载内核代码的系统级控制。攻击需应用先本地安装，无法直接经互联网发起；据称影响OnePlus 15、OnePlus 12 Pro及更多OnePlus和OPPO设备，但尚无真实攻击证据。OnePlus于5月确认漏洞，披露时仍未发布补丁、CVE或公告。

原文：https://thehackernews.com/2026/09/unpatched-oneplus-flaws-let-installed.html

### 02 ThreatsDay：AI 搜索投毒、AI 编程工具泄露代码仓库、一键代码执行及另外 13 条新闻

**公开时间：**2026年09月25日 01:52

AI 解读

文章汇总多起以日常更新、登录框、搜索答案和编码工具为掩护的安全事件。此前未公开的Android银行木马RemControl通过伪造Google Play页面传播，滥用辅助功能覆盖银行应用、实时录屏、记录按键并远程控制设备，其C2地址经加密Telegram死信动态解析。Z.ai因ZCode默认将本地代码仓库快照上传至中\*境内阿里云而停用相关功能。研究还称俄罗斯MAX超级应用可截屏、读写小程序存储、注入JavaScript、代理网络流量并控制会话令牌；伪造Claude Max赠品则利用浏览器内浏览器窃取Google凭据。另有研究展示通过进程参数投毒和线程劫持规避传统EDR检测的代码注入技术。

原文：https://thehackernews.com/2026/09/threatsday-ai-search-poisoning-ai.html

### 03 被入侵的 GitHub Actions 重新上线并恢复执行 Mini Shai-Hulud 恶意软件

**公开时间：**2026年09月25日 00:00

AI 解读

2026年5月18日，GitHub Actions仓库actions-cool/issues-helper和actions-cool/maintain-one-comment在Mini Shai-Hulud活动中被入侵，恶意代码窃取CI/CD流水线敏感凭据并外泄至攻击者服务器，与Mini Shai-Hulud集群相关联，使用t.m-kosche[.]com外泄域名和@antv npm包。9月16日，仓库重新启用后，未清理恶意发布标签，任何引用版本标签的工作流恢复执行负载。仓库再次被GitHub禁用，原因不明，但恶意代码残留导致多数每日调度或触发issue的工作流在启用后短期内运行恶意负载。仅版本标签引用受影响，不影响使用pre-May 18 commit SHA pin的工作流。

原文：https://thehackernews.com/2026/09/compromised-github-actions-came-back.html

### 04 PamStealer macOS 恶意软件新增实时 C2 载荷解密和多层持久化机制

**公开时间：**2026年09月25日 00:00

AI 解读

Jamf Threat Labs披露PamStealer新版：仍用JXA投放器，但改为从服务器获取解密工具并完成X25519密钥交换，私钥在服务端，DEK无法静态还原，每次执行生成临时密钥对，令加密载荷无C2会话即无法解密。诱饵由仿冒Maccy等改为假加密钱包网站wavel[.]app，下载含编译AppleScript的Wavel.dmg，经Script Editor触发JXA，base64解码后管道给/bin/zsh执行。zsh脚本从wavel.apple03cloudstore[.]com下载pkgunpack、抑制登录项通知、经LaunchAgent及修复脚本与~/.zshrc钩子建立四重持久化、将修复脚本植入Git钩子，并轮询上传暂存目录。窃密组件改用Swift，伪造崩溃对话框经PAM校验窃取系统密码、钥匙串及多款浏览器凭据，收集元数据、照片与.zsh\_history等文件，并枚举进程与应用。

原文：https://thehackernews.com/2026/09/pamstealer-macos-malware-adds-live-c2.html

### 05 SOC 不必每次面对告警都从头开始

**公开时间：**2026年09月25日 00:00

AI 解读

文章指出，AI并未制造全新攻击类型，而是让失败攻击的重试成本大幅降低：攻击者用模型解释报错、修复脚本、快速生成新枚举路径，从而压缩入侵中段的研究与排错时间。公开记录显示这一趋势：2025年初Google威胁情报组发现国家支持行为体将生成式AI用于翻译、脚本与排错；2025年底出现执行中调用模型的恶意软件样本及非法AI工具市场，Anthropic披露关闭一宗几乎各阶段依赖AI的勒索行动；2026年5月GTIG称网络犯罪者利用开源管理工具的双因素绕过漏洞构建可用利用程序，并高置信度评估AI模型支持了漏洞发现与利用开发，与厂商协作披露并中断活动。文章强调，评估的AI协助不等于已确认的实战部署，归因困难、普遍性不明，报告并非全球活动普查。提供商安全护栏提高了滥用成本，但护栏位于企业之外，可被重新措辞、换用开源权重模型、拆分任务或包装工具绕过，不能视为安全边界。攻击以循环方式运行，AI压缩观察、猜测、尝试、读取反馈和调整之间的时间；防御循环则被队列和交接打断，平均确认与修复时间掩盖了重建身份、端点和事件上下文所需数小时的决策延迟。

原文：https://thehackernews.com/2026/09/the-soc-doesnt-need-to-start-over-with.html

### 06 Bitget称疑似朝鲜黑客在后端遭入侵后窃取3.516亿美元

**公开时间：**2026年09月25日 00:00

AI 解读

加密货币交易所Bitget称，2026年9月24日其安全系统发现少数热钱包发生未经授权转账，疑似与朝鲜黑客组织有关，热钱包和温钱包共损失约3.516亿美元，涉及ETH、XRP、BNB、AVAX、USDT和USDC等资产。攻击者据称入侵钱包基础设施的关键后端系统，伪造交易数据并触发授权流程转移资金；冷钱包及绝大多数平台资产、客户余额和交易不受影响。Bitget已暂时停止提现，并委托Mandiant和SlowMist调查；其独立自托管钱包未受影响，部分相关链已冻结黑客地址。

原文：https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html

### 07 Roundcube 身份验证前 SQL 注入漏洞正在遭到野外积极利用

**公开时间：**2026年09月25日 00:00

AI 解读

加拿大网络安全中心警告，已修复的Roundcube Webmail漏洞CVE-2026-48842正被实际利用。该漏洞CVSS评分8.1，属virtuser\_query插件中的预认证SQL注入，影响1.6.x低于1.6.16及1.7.x低于1.7.1版本，源于preg\_replace()反斜杠转义绕过，未认证攻击者可注入任意SQL语句，可能泄露邮箱账户凭据和存储邮件。补丁已于2026年5月随1.6.16和1.7.1发布。Shadowserver数据显示超52.3万个Roundcube实例暴露于互联网。Roundcube漏洞历来被用于窃取邮件通信，2026年7月Proofpoint称疑似中\*相关攻击者UNK\_MassTraction利用其投递webshell或VShell工具；2026年2月CVE-2025-49113和CVE-2025-68461被CISA标记为活跃利用。

原文：https://thehackernews.com/2026/09/roundcube-pre-auth-sql-injection-flaw.html

### 08 WSO2 和 Adobe Commerce 漏洞遭利用发动攻击，已被加入 CISA KEV

**公开时间：**2026年09月25日 00:00

AI 解读

CISA将两个高危漏洞列入KEV目录，因有在野利用证据。CVE-2026-5430（9.8分）是WSO2 API Control Plane、API Manager、Traffic Manager和Universal Gateway的路径遍历漏洞，可导致不受限文件上传及远程代码执行；watchTowr称自2026年9月13日起在蜜罐捕获伪造JWT利用尝试并复现该漏洞，并指出WSO2技术被银行、政府、电信和物流领域近1000家客户使用。CVE-2026-71362（9.1分）是Adobe Commerce和Magento的授权不当漏洞，可无交互获取敏感资源提升访问权限；Sansec于2026年8月称已检测并阻断利用尝试，攻击者可将客户会话切换至另一账户，访问受害账户和私人数据；Previdian遥测显示9月10日一个澳大利亚IP尝试攻击其蜜罐。Adobe尚未更新公告确认利用状态。FCEB机构被建议于2026年9月27日前应用修复。

原文：https://thehackernews.com/2026/09/wso2-and-adobe-commerce-flaws-exploited.html

### 09 Cloudflare 修复容器可读取其他客户磁盘残留数据的漏洞

**公开时间：**2026年09月25日 00:00

AI 解读

Cloudflare Containers 存在漏洞，允许付费客户读取其他客户容器在同一服务器上遗留的磁盘数据。数据来自已释放的磁盘空间而非实时工作负载，攻击者无法选择目标，Cloudflare Sandboxes 也受影响。漏洞源于共享磁盘设置：容器使用 Linux thin provisioning 以 64KB 块分配存储，删除后块返回跨账户共享池，该池被设为跳过擦除。新容器仅写入少量数据时，块其余部分保留前容器数据。研究人员通过写入 4KB 块并在原始磁盘级别读回，在 24 次尝试中 18 次发现遗留数据，涵盖四大洲 20 台机器，恢复出目录结构、SQLite 数据库、.env 和凭据文件等。漏洞由 Accomplish 的 Oren Yomtov 于 9 月 4 日报告。Cloudflare 分两步修\*：重新开启块擦除，并退役运行中容器磁盘、清除缓存、重启服务器，9 月 19 日完成。未发现他人利用证据，但暴露持续时间不明。研究人员称相同设置影响 Browser Run，Cloudflare 未提及。

原文：https://thehackernews.com/2026/09/cloudflare-fixes-flaw-that-let-one.html

## HackerOne

昨日暂无符合标准的漏洞发布

![一个不正经的黑客 · 全球安全动态与知识分享](https://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR0wxk6alKwgl2znYoglw9fzyQU1dNd3QicIdQ2gekg7VXOz7LPmL1Kl2dpO5I60zgwgGuO6fVrTAo2PpLibVdWOo4OZYc7FQ4W7Q/640?from=appmsg)![]()

继续阅读

点击文末「阅读原文」，可前往网站主页查看完整资讯与 AI 解读。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VugQCN2riaR1oKre7rbnJe6BxfvWUT6Uibz0WwGqXuvtRFYicibfTQDhDymFj0rTsyTLlVvOFdzm3wDV9TlqibHDG5UHRfLBPKMiadz3SYOjk0Bo4/0?wx_fmt=png)

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