---
title: DumpBrowserSecrets免杀版｜浏览器数据提取，隐蔽到让检测“失明”
url: https://mp.weixin.qq.com/s/iJGdsAs3MVnxWkHaqRebTQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:39:37.203015
---

# DumpBrowserSecrets免杀版｜浏览器数据提取，隐蔽到让检测“失明”

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2n28ib0zSXFNMkBPGpBJibz3hke0RvlYSicSlqs4icibLMxOicupmrWticHQo3fibVel57ickDETvpGXIKnItw/0?wx_fmt=jpeg)

# DumpBrowserSecrets免杀版｜浏览器数据提取，隐蔽到让检测“失明”

原创

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

# 🔥DumpBrowserSecrets免杀版｜浏览器数据提取，隐蔽到让检测“失明”

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg)

image

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

在红队攻防、安全研究的实战场景中，浏览器数据提取工具的“隐蔽性”和“有效性”往往决定了测试的成败——传统工具静态特征明显、行为噪声高，刚出手就被安全规则拦截；而今天要给大家带来的**DumpBrowserSecrets免杀版**，堪称浏览器数据提取的“隐形利刃”，兼顾全覆盖提取与极致免杀，让合规授权下的情报收集更丝滑、更安全。

## 🚨 为什么它能成为红队刚需？

面对Chrome、Edge、Firefox等主流浏览器的加密存储机制，以及越来越严格的终端检测规则，DumpBrowserSecrets免杀版从“提取能力”和“隐蔽性”双维度突破，解决了传统工具的核心痛点：

✅ **全场景覆盖，解密无死角**

支持Chrome、Edge、Brave、Opera（含GX）、Vivaldi、Firefox等几乎所有主流浏览器，同时兼容App‑Bound（V20/V10）与DPAPI加密方式，本地就能完整解析SQLite/JSON格式的浏览器数据——Cookies、账号密码、令牌、历史记录、书签、自动填充信息等，一网打尽。

✅ **零依赖部署，上手即能用**

单可执行文件直接运行，无需额外配置环境；自动检测浏览器安装路径（还做了多源回退兜底，杜绝“未安装”误判），无界面静默运行，新手也能秒上手。

✅ **实战级免杀，行为近乎“无痕”**

这是免杀版最核心的升级！相比传统工具，它从底层重构了执行逻辑，把“隐蔽”刻进每一步：

## 🛡️ 免杀优化核心亮点

传统工具之所以易被检测，无非是“静态特征明显”“行为痕迹突出”，而DumpBrowserSecrets免杀版针对性做了四大优化：

### 1. 注入方式：Early Bird APC 注入

在目标浏览器进程首次调度前就排队执行加载，避开进程运行后的行为监控，大幅降低操作噪声，让注入行为“藏”在系统正常调度中。

### 2. 进程创建：CreateAlertableProcess 无痕迹启动

创建无窗口、可警报态的进程，同时重定向输出流，既避免弹窗等可视化痕迹，又减少进程行为被拦截的概率。

### 3. API调用：InitApiTable 动态解析

摒弃传统静态导入API的方式，改用函数指针表分发调用——静态扫描根本抓不到特征，从源头规避签名检测。

### 4. 资源处理：ExtractDllFromResources 内嵌提取

核心DLL按需从程序资源中提取，无需提前落地文件，彻底杜绝静态扫描时的DLL特征暴露。

## 📝 极简使用姿势，实战超高效

免杀版保留了极简的命令行交互，几行指令就能完成全量提取，适配不同实战场景：

* 默认导出（每类最多16条）：`DumpBrowserSecrets.exe`
* 指定浏览器提取：`DumpBrowserSecrets.exe /b:chrome`
* 火狐全量导出：`DumpBrowserSecrets.exe /b:firefox /all`
* 自定义输出路径：`DumpBrowserSecrets.exe /b:brave /o Output.json`
* 枚举所有浏览器+全量导出：`DumpBrowserSecrets.exe /b:all /all`

所有数据统一输出为JSON格式，可直接对接SIEM、SOAR平台，或用于脚本二次处理、报表生成，无需额外适配。

```
Usage: DumpBrowserSecrets.exe [options]

Options:
  /b:<browser> Target Browser: chrome, edge, brave, opera, operagx, vivaldi, firefox, all
               (default: system default browser)
  /o <file>    Output JSON File (default: <browser>Data.json)
  /all         Export All Entries (default: max 16 per category)
  /?           Show This Help Message

Examples:
  DumpBrowserSecrets.exe                            Extract 16 Entries From The Default Browser
  DumpBrowserSecrets.exe /b:chrome                  Extract 16 Entries From Chrome
  DumpBrowserSecrets.exe /b:firefox /all            Export All Entries From Firefox
  DumpBrowserSecrets.exe /b:brave /o Output.json    Extract 16 Entries From Brave To Output.json
  DumpBrowserSecrets.exe /b:all /all                Extract All From All Installed Browsers
```

## 使用示例

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2n28ib0zSXFNMkBPGpBJibz3hBiaKXNT1ibGdEeT3TZqX1ia2u502ib4F6giaOr7uq8siaJ7okUBbGHiaM8FYw/640?wx_fmt=png&from=appmsg)

结果

![](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2n28ib0zSXFNMkBPGpBJibz3hojTmX5aH0shQcrO4U3k5Frciboo23SQMo55YsQkU0uuOeKPLxsPSLyQ/640?wx_fmt=png&from=appmsg)

## ⚠️ 重要合规声明

DumpBrowserSecrets免杀版仅用于**获得合法授权**的安全测试、技术研究与教学场景！任何未经授权的使用，均可能违反《网络安全法》等法律法规，后果自负。

## 项目获取

圈子内获取

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护）
* 全自动信息收集平台（集成资产测绘、端口扫描、指纹识别及漏洞探针）
* 内网穿透套件（适配多层路由、隔离网络环境的隐蔽流量转发）
* 权限维持工具集（含注册表、系统服务、进程隐藏等多维持久化方案）
* 哥斯拉/冰蝎定制化马生成器（绕过主流终端防护与EDR动态检测）
* 日志清理工具（实现Windows/Linux系统关键日志无痕删除与篡改）
* 浏览器凭证窃取工具（支持Chrome/Edge/Firefox等主流浏览器数据提取）
* 企业VPN漏洞利用工具（适配多款商用VPN设备的漏洞探测与利用）
* 工控系统专用扫描器（针对SCADA、PLC等工控设备的安全检测与指纹识别）
* 邮件钓鱼平台（集成模板生成、钓鱼追踪、数据统计全流程功能）
* 社工信息聚合工具（整合多平台公开信息检索与关联分析能力）
* 二开fscan内网扫描工具（增强指纹精度、弱口令爆破与结果标准化输出）
* 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护）
* 免杀360专属加载器（支持Shellcode内存执行，绕过360全系防护检测）

后续将不断更新到内部圈子中 欢迎加入圈子

![](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2n28ib0zSXFNMkBPGpBJibz3hOp5eSvLJjRXK9H1QvIKXbKAYg9d1JPSBQ1maYvLJ6fNzPaQeaDibLibA/640?wx_fmt=jpeg&from=appmsg)

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