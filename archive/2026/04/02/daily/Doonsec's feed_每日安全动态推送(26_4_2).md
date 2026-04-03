---
title: 每日安全动态推送(26/4/2)
url: https://mp.weixin.qq.com/s/grS-KOq--jix1QG2YSoayg
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:25:18.495340
---

# 每日安全动态推送(26/4/2)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dWDic6IAXZsfiaZW0JQviacCLMqWhF3SNibuLiadsQ0NIQTtMib9dtRNwicMAnvZMsHoH8R05VSkImpkiavrZ7h5ia6ZMew/0?wx_fmt=jpeg)

# 每日安全动态推送(26/4/2)

原创

admin
admin

腾讯玄武实验室

![]()

在小说阅读器中沉浸阅读

•  UNC1069 投毒 Axios 包部署 WAVESHAPER.V2 后门
<https://sectoday.tencent.com/event/0jgOSp0BVJfJhgnJtRGb>

朝鲜威胁组织 UNC1069 于 2026 年 3 月 31 日劫持了广泛使用的 Axios NPM 包维护者账户，绕过了受信任发布机制，在版本 1.14.1 和 0.30.4 中注入了名为 'plain-crypto-js' 的恶意依赖。该攻击利用 npm postinstall 钩子机制，在 Windows、macOS 和 Linux 系统上静默部署了跨平台远程访问木马 WAVESHAPER.V2。恶意软件具备基于 JSON 的 C2 通信能力，并在执行后自我销毁以规避检测，旨在窃取凭证和 API 密钥。此次事件导致约 3% 的受感染环境遭到入侵，迫使安全社区建议立即隔离主机、轮换所有凭证并锁定依赖版本。

•  谷歌研究预警：量子攻击加密货币的时间窗口可能比预期更短
<https://www.helpnetsecurity.com/2026/03/31/quantum-computers-cryptocurrency-risks-google-research/>

谷歌最新研究颠覆性地修正了量子计算机破解椭圆曲线密码所需的资源估算，指出攻击者可能在交易确认的短短九分钟内窃取私钥，迫使加密行业立即加速向抗量子密码学迁移。该文章通过零知识证明负责任地披露了具体漏洞细节，为应对迫在眉睫的“在途”和“静态”量子攻击提供了关键的行动路线图。

•  DarkSword iOS 漏洞利用工具泄露事件
<https://sectoday.tencent.com/event/ZU9qDp0B5M25NX6P5_SO>

高级持续性威胁组织 TA446 开发的 DarkSword 间谍软件漏洞利用工具包被公开泄露至 GitHub，该工具包含针对 iOS 18.4 至 18.7 版本的两组漏洞利用链及六个 CVE 漏洞。此工具利用浏览器漏洞即可实现无需专业知识的静默入侵，能够窃取联系人、钥匙串及通话记录等敏感数据，使数亿台未更新的 iPhone 设备面临类似“永恒之蓝”的大规模静默窃密风险。尽管苹果已发布紧急补丁，但安全专家警告该工具的“开箱即用”特性可能导致国家级黑客技术向大众扩散，建议受影响用户立即升级系统或启用锁定模式。

•  Perl 核心模块严重供应链漏洞：CVE-2026-4176 分析与紧急修复策略
<https://securityonline.info/perl-critical-vulnerability-zlib-cve-2026-4176-patch/>

本文揭示了 Perl 语言核心中一个 CVSS 评分高达 9.8 的严重供应链漏洞，该漏洞源于其内置的 Compress::Raw::Zlib 模块中捆绑了存在缺陷的 zlib 库。文章不仅详细剖析了从 5.9.4 到 5.43.9 广泛版本受影响的范围，还紧急提供了立即升级或手动覆盖模块的具体缓解方案，对依赖 Perl 的系统安全至关重要。

•  利用四个 CrewAI 漏洞链式攻击实现沙箱逃逸与远程代码执行
<https://www.securityweek.com/crewai-vulnerabilities-expose-devices-to-hacking/>

本文揭示了攻击者如何通过链式利用 CrewAI 中的四个关键漏洞（包括远程代码执行和沙箱逃逸）来突破安全防线，这对广泛使用的 AI 多智能体框架构成了迫在眉睫的威胁。文章不仅详细剖析了从 Docker 回退机制到路径验证缺失的技术细节，还为开发者在补丁发布前提供了关键的缓解策略。

•  Citrix NetScaler 关键内存泄露与会话混淆漏洞事件
<https://sectoday.tencent.com/event/BzZgLZ0BVJfJhgnJT2JH>

Citrix 发布紧急安全更新，修复了 NetScaler ADC 和 Gateway 产品中的两个关键漏洞：CVE-2026-3055 和 CVE-2026-4368。其中，CVSS 评分为 9.3 的 CVE-2026-3055 是一种越界读取漏洞，在 SAML IDP 配置下允许未认证的攻击者泄露敏感内存数据；CVSS 评分为 7.7 的 CVE-2026-4368 则是一种竞态条件缺陷，会导致 Gateway 或 AAA 配置下的用户会话混淆。尽管目前尚未发现野外利用证据，但鉴于历史上 Citrix Bleed 系列攻击的严重性，安全专家强烈建议受影响用户立即升级补丁以防范迫在眉睫的入侵风险。

•  LangChain 与 LangGraph 严重漏洞：文件、密钥及数据库面临泄露风险
<https://thehackernews.com/2026/03/langchain-langgraph-flaws-expose-files.html>

本文揭示了影响全球超8亿次下载的LangChain和LangGraph框架的三大高危漏洞，包括CVSS 9.3分的反序列化缺陷，可窃取API密钥、环境秘密及对话历史。鉴于这些核心AI基础设施漏洞正被迅速利用，立即升级补丁已成为防止企业敏感数据大规模泄露的当务之急。

•  Infiniti Stealer：利用伪造 Cloudflare CAPTCHA 实施 ClickFix 攻击的 macOS 窃取器
<https://cybersecuritynews.com/fake-cloudflare-captcha-pages-spread-infiniti-stealer/>

本文首次披露了名为 Infiniti Stealer 的新型 macOS 恶意软件，其利用 Nuitka 编译技术结合 ClickFix 社会工程学攻击，无需任何软件漏洞即可通过伪造的 Cloudflare 验证页面诱导用户执行终端命令。该文章极具发布价值，因为它彻底打破了 Mac 用户“天然免疫恶意软件”的迷思，并揭示了攻击者如何利用原生二进制文件绕过传统安全检测的先进手法。

•  CVE-2026-20817：微软移除 WER 功能以修复导致 SYSTEM 权限提升的严重漏洞
<https://cybersecuritynews.com/new-windows-error-reporting-vulnerability/>

本文揭示了Windows错误报告服务中一个极其危险的本地提权漏洞（CVE-2026-20817），其最大亮点在于微软采取了罕见的激进策略，直接移除漏洞功能而非修补代码以彻底消除攻击面。文章深入剖析了利用ALPC消息操纵实现SYSTEM权限获取的技术细节，并警示了当前网络中泛滥的恶意PoC伪装风险，对防御者具有极高的实战参考价值。

•  从目录删除到RCE：GCP Looker漏洞剖析 | CN-SEC 中文网
<https://cn-sec.com/archives/5128339.html>

本文揭示了 Google Cloud Looker 中一个极具创意的远程命令执行漏洞，攻击者利用目录删除的后序遍历机制与文件系统 readdir 顺序的确定性，精准制造时间窗口以触发伪造的 Git 钩子。该研究不仅展示了从微小验证缺陷到集群级权限提升的完整攻击链，更深刻警示了云原生环境中竞态条件与服务账户最小权限原则的极端重要性。

\* 查看或搜索历史推送内容请访问：
<https://sectoday.tencent.com/>
\* 新浪微博账号： 腾讯玄武实验室
<https://weibo.com/xuanwulab>
\* 微信公众号： 腾讯玄武实验室
![微信公众号： 腾讯玄武实验室](https://mmbiz.qpic.cn/mmbiz_jpg/HhcytTU2b7dl7yVLQyfjskic0VtX4JBMpicUSg9Gyfk8f8HJfH2biaic79jueWwphsic7ABrP8KfpNQbicOE729k5Dgjjy5foWhTDfGqmcpMtNAxQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

腾讯玄武实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dWDic6IAXZscjSsHUwwflGy5SJQX2FuvIUk8lpe0rA7xexvd5NKKiab1p3jDkjMicaiaVbEUib2SlkABU55kZvvfAWw/0?wx_fmt=png)

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