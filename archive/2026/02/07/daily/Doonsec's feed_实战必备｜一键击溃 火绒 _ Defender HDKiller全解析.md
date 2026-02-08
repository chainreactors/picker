---
title: 实战必备｜一键击溃 火绒 / Defender HDKiller全解析
url: https://mp.weixin.qq.com/s/b6QQhFhOIdQhMLuQD_1rJQ
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:28:17.406621
---

# 实战必备｜一键击溃 火绒 / Defender HDKiller全解析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCprzicTrgtyUswPfOqPIqy6KnOFlk9G2l7FbDkcib9Rqp3CWDkficI9ZVNGw/0?wx_fmt=jpeg)

# 实战必备｜一键击溃 火绒 / Defender HDKiller全解析

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

# ⚔️ 实战必备｜一键击溃 火绒 / Defender HDKiller全解析

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg)

image

📌本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

---

## 🔥 工具介绍

**简单、粗暴、有效。**

经过测试前几天发布的一键kill 工具火绒和Defender  kill不掉，因为火绒、Defender 进程被设为 **PPL（受保护进程轻量版）**，并由 **内核驱动** 强制保护，即使你注入到 SYSTEM 权限的 svchost，也只是用户态高权，**没有内核态权限去绕过 PPL 与驱动级防护**，所以杀不掉

所以重新写了一个基于BYOVD技术，专门针对火绒 defender 这种受内核保护的EDR的进程终结工具HDKiller。

本工具专为解决无法关闭的安全软件而生。无论对方拥有何种“自我保护”机制，使用本工具均可一键强制结束。

你是否遇到过：

* 想退出杀毒软件，却提示“拒绝访问”？
* 无法停止安全服务，导致测试受阻？
* 右键“结束任务”根本没反应？

**HDKiller** 是你的终极解决方案。

* **无视保护**：火绒的自我保护，统统无效。
* **一键清除**：无需复杂配置，只需一条指令，瞬间清空目标防护。
* **全面覆盖**：完美支持 火绒安全软件**、**Windows Defender\*\* 等主流杀软。
* **用完即走**：运行结束后自动清理痕迹，干净利落。

---

## ⚡ 使用演示

请以 **管理员身份** 运行 CMD 或 PowerShell。

### 2. 击溃 火绒安全

列出火绒进程

```
tasklist | findstr "Hi"
```

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCpr9CNHMIPEtiafEVQq2cv9pdzc7e6lvO7nwFPZxSQ8jd2x4ems0eW5Pcg/640?wx_fmt=png&from=appmsg)

火绒无法退出？一条命令直接带走。

HipsDaemon.exe是火绒的核心服务进程

```
HDKiller.exe <HipsDaemon的PID>
```

**效果：** 火绒核心服务停止，查杀功能失效。

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCprJ2Vu0lXWlHIpaBDgLk0fbaqNcKiaogfkx3Na8KPhq8LpdvDEJF0ze9A/640?wx_fmt=png&from=appmsg)

### 3. 击溃 Windows Defender

列出Defender的进程

```
tasklist | findstr /i "MsMpEng SecHealthUI WdApp MsSense MpCmdRun WdNis"
```

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCprIv72mBAtEfp82VlNnicL5K1qPO16guUmUTrsxLq4tkKL9rCF8vSiaCog/640?wx_fmt=png&from=appmsg)

Defender 总是自动开启？用这个强制关闭它。

```
HDKiller.exe <MsMpEng的PID>
```

**效果：** Windows 安全中心直接报错，实时防护彻底瘫痪。

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCpr98g96CExRNfL8MaLoQrXNPNoByAJaO3EfDkKTTjWx4vT6NGtK1IMbA/640?wx_fmt=png&from=appmsg)

---

## 📸 运行效果展示

运行工具后，你将看到如下提示，代表“猎杀”成功：

```
[+] Checking...
[+] Driver loaded successfully
[+] Connected to Driver successfully
[+] Get handle to protected process sucessfully
[+] Kill EDR Successfully
[+] Driver unloaded successfully
```

一旦出现 `[+] Kill EDR Successfully`，恭喜你，目标防护已解除。

## 免杀效果

### defender

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCpryEc6tv8PpPFaliaKibyyE0eBrWLQScia1jicKLTsdYVurg6eeavVI80qGw/640?wx_fmt=png&from=appmsg)

### 火绒

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCprCrK3s5X1KriarHKBW4PaibrG803icbicOicClZpSNzpFbJ4MibUAoBycwsTQ/640?wx_fmt=png&from=appmsg)

## 视频演示

### defender

###

### 火绒

###

## 项目获取

**圈子**内获取

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护，无感知运行，突破多引擎联合检测）
* XXByPassBehinder v1.1 冰蝎免杀生成器（定制化冰蝎免杀工具，绕过主流终端防护与EDR动态检测，支持自定义载荷）
* 哥斯拉二开免杀定制版（二开优化，深度免杀，突破终端防护与EDR检测，适配多场景植入）
* NeoCS4.9终极版（高级免杀加载工具，强化载荷注入与进程劫持，适配多系统版本，无兼容问题）
* WinDump\_免杀版（浏览器凭证窃取工具，支持Chrome/Edge/Firefox等主流浏览器，一键提取敏感数据，免杀过防护）\_
* \_DumpBrowser\_V1\_免杀版（浏览器凭证窃取工具，专攻浏览器密码、Cookie、历史记录提取，免杀性能拉满）
* fscan二开版（二开优化内网扫描工具，增强指纹精度、弱口令爆破与结果标准化输出，适配复杂内网）
* RingQ加载器二开版（二开优化免杀加载器，支持Shellcode内存执行，绕过各类终端防护与EDR检测）
* 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护，适配不同Web场景）
* 免杀360专属加载器（支持Shellcode内存执行，针对性绕过360全系防护检测，无感知运行）
* 一键kill360 火绒 defender工具（一键击溃主流杀软）

后续将不断更新到内部圈子中 欢迎加入圈子![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kTp5BpCMb901r34Qsxiar69niau36nIE6q7fMIIrylRMNSb6PiaetIQDU7cCBCDnFibeQTPWeArDO9tA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kTp5BpCMb901r34Qsxiar69aBRExZP9U4yAnhfoP9wABkmc0DCYs7NTyicvYcBaqLxVxfAJoicMyWGQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

image

![](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kwOTjEL8Ryc1JpKqpgNCpr304aDZz0HCmHWWs63tMKXdPK6tCouc1aRYnKnHu6tSVxjpHE7QRvDw/640?wx_fmt=jpeg&from=appmsg)

```
吾心吾行澄如明镜，所作所为皆为正义
```

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