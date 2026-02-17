---
title: 硬核发布：Windows Defender 终结者 (win11_df-Killer)
url: https://mp.weixin.qq.com/s/IDQDvrWh6mXZ9GTs-v2Y_Q
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:16:24.234444
---

# 硬核发布：Windows Defender 终结者 (win11_df-Killer)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2lo4VYgFZveMP6cicgNY1qasfdTeKRfmfkoe0o4SlicXEo2BDgIxicnibRUvMHwwWBOgjibnnZqxU8BicuA/0?wx_fmt=jpeg)

# 硬核发布：Windows Defender 终结者 (win11\_df-Killer)

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

# 硬核发布：Windows Defender 终结者 (win11\_df-Killer)

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg)

image

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

## 🛑 Win11 时代的对抗难题

相信很多玩安全的朋友都发现了：**以前在 Windows 10 上好使的对抗工具，到了 Windows 11 统统失效了。**

前段时间发布的HDKiller，在win10上kill火绒和defender都没有问题，但在win11上不行，因为存在驱动签名验证，win11不允许加载不受信任的在黑名单的驱动程序的加载。由此引出下文：

微软在 Win11 上大幅收紧了安全策略：

1. **驱动加载被封杀**：Win11 实施了更严格的驱动签名验证 (DSE) 和 HVCI 机制。普通的未签名驱动或自签名驱动根本无法加载，想进内核搞对抗？门都没有。
2. **无限重启的噩梦**：Win11 的 Defender 引入了更强的进程保护 (PPL) 和服务互保机制。你前脚杀掉 `MsMpEng.exe`，后脚它就重启，甚至还把 `MpDefenderCoreService` 拉起来互相守护。简直是“打不死的小强”，让人心态爆炸。

**面对这种“不让加载驱动”且“杀完无限重启”的困境，我们推出了全新的解决方案。**

---

## 🚀 它是如何破局的？

**BdApiUtil-Killer** 专为解决 Win11 的痛点而生，实现了降维打击：

### 1. 解决“不让加载驱动”：BYOVD 技术

既然系统不让我们加载自己的驱动，那我们就用系统“信任”的驱动！ 本工具采用了 **BYOVD (Bring Your Own Vulnerable Driver)** 技术：

* **利用合法签名**：我们内置了 BitDefender 官方带有合法数字签名的驱动程序 (`xxx.sys`)。
* **完美绕过检测**：因为有正规签名，Win11 会乖乖放行，不会拦截。
* **化敌为友**：利用该驱动中存在的漏洞，我们成功获取了内核级的最高权限。

### 2. 解决“杀完不断重启”：全方位封杀

仅仅杀进程是不够的，必须切断复活的根源。本工具在获取内核权限后，执行一套连招：

* **双核秒杀**：同时监控并秒杀 Defender 主进程和核心服务进程，打破它们的互保循环。
* **驱动级卸载**：在进程死亡的瞬间，强制卸载底层的内核过滤驱动，让它失去感知能力。
* **彻底锁死**：随即禁用服务、锁定注册表、清除计划任务。即使系统尝试重启服务，也会因为文件被删、注册表被锁而失败。

---

## ✨ 核心功能亮点

* **⚡ 内核级秒杀**：无视 PPL 保护，直接在内核层终结进程。
* **🔒 拒绝复活**：从服务、驱动、注册表三个维度彻底封死重启路径。
* **🤖 智能自动化**：开箱即用，自动释放驱动、自动提权、自动清理。
* **🛡️ 纯净无残留**：对抗结束后尝试清理自身痕迹。

---

## 📖 如何使用？

使用非常简单，仅需一步：

1. **右键以管理员身份运行** 程序。

   ```
   .\win11_df-Killer.exe
   ```

**就这样！** 🎉

程序启动后，你会看到它自动执行一系列操作：

* 检测并击杀 Defender 进程。
* 禁用各类服务和驱动。
* 锁定系统设置。

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lo4VYgFZveMP6cicgNY1qasAysFQIuIJtjszJtQWFicwdztycSLVO1Ou6pdreflwZJicVyOrsPeHibBA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lo4VYgFZveMP6cicgNY1qasDviahFZFHj0iahpsibUDMUHMVfQHWvyHsn3Qz7pByialMG5qAtfPdSHrOQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lo4VYgFZveMP6cicgNY1qasGedGsJ3sKUzUNmIcxlYGmvGDKKIKKkoWCWGeh7ibkYGdPoZm6ibS6zcQ/640?wx_fmt=png&from=appmsg)

经过几轮对抗之后，defender核心进程 MpDefenderCoreService.exe不会再自动重启了。被完全关闭。

---

## ⚠️ 郑重声明

* **仅供研究**：本工具仅供安全研究人员、软件开发者在合法的测试环境中使用（如恶意代码分析环境、安全对抗测试等）。
* **风险提示**：彻底禁用杀毒软件会使您的系统暴露在风险中，请勿在日常使用的生产环境中随意使用。
* **责任自负**：开发者不对因使用本工具导致的任何系统损坏或数据丢失负责。

## 工具获取

**圈子**内获取，文末发放优惠券。

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）
* **XXByPassBehinder** v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）
* 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）
* **NeoCS4.9**终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）
* **WinDump***免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）*
* \_**DumpBrowser\_V1**\_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）
* **fscan**二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）
* **RingQ**加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）
* 多款免杀**Webshell**集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）
* 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）
* 一键Kill 火绒 defender 工具 **HDKiller**
* win11 一键kill 360工具 **InjectKill**
* win11 一键kill defender工具**InjectKill**

后续将不断更新到内部圈子中 欢迎加入圈子

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lo4VYgFZveMP6cicgNY1qasbicSPnZ4MKvgFvqiax2LM25GapLug6HELvdgbBsu5oT4MgOM4Hr2KiaEQ/640?wx_fmt=png&from=appmsg)![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kTp5BpCMb901r34Qsxiar69aBRExZP9U4yAnhfoP9wABkmc0DCYs7NTyicvYcBaqLxVxfAJoicMyWGQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

image

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

星夜AI安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

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