---
title: 37.8万星 REA 送出完整学习路线图,同一天 Anthropic 悄悄关了 Claude 的逆向门
url: https://mp.weixin.qq.com/s/Zyzwz0jWGjfFZ5FKZEtKnA
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:16:42.020561
---

# 37.8万星 REA 送出完整学习路线图,同一天 Anthropic 悄悄关了 Claude 的逆向门

# 37.8万星 REA 送出完整学习路线图,同一天 Anthropic 悄悄关了 Claude 的逆向门

原创

Violet Walker
Violet Walker

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6N7SjePBrAj5tDpe6QRWVr8A4T3QCaOQUWiarAetmw1c6nWtcrtiasxEg3TmGOibVjQP9h4thdylJMt8Fe4pQnkTGFrrrp5hsRV8Y/640?from=appmsg)
> **导语**:10 月 23 日晚,一条 REA 学习路线图在 X 上拿了 3371 个赞。一小时后,另一条推文说 Anthropic 已经悄悄关掉了 Claude 的逆向能力。同晚,一边教你怎么学,一边在收门。

![一条发光路径通向远处的门,寓意学习路线与被关闭的入口](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6OnoTZS9LKHA0OSvygeIoIQic2aH8Wa1x17WxasyJUa6icYEicoedHkEoiaySbibsxmg6pCYz00zmen1w81Bnt1a3mEqZVEEIiaUs9ec/640?from=appmsg "一条发光路径通向远处的门,寓意学习路线与被关闭的入口")

---

## 一、一条 3371 赞的"学习地图"

10 月 23 日 20:46,蓝标用户 @sammy\_capital 发推,标题就一句:"别再花几个小时学 REA 了。"正文说 REA 团队整理了一份实用路线图,含教程、真实调查、仓库、书籍、论文和免费课程,末尾还附了最佳学习顺序。

这份地图有多大?八个板块、46 条链接(去重 45 个不同地址):官方仓库与官网、安装与 agent 配置、第一次调查、指南、MCP 提示词;六个跟练视频;五个真实调查;九个 GitHub 仓库;六本书;七篇论文;七门免费课。

推文拿到 3371 个赞、473 次转发、42 条回复,评论区比正文还热闹。有人调侃"发一条得花我几小时读完的推文";也有人泼冷水:"塞满教程、repo、论文的路线图我就当索引看,能跑出 match rate 才算数。"

![REA 官方站点 rea.tools 的社交卡片](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PPBlicEVnPh4WCM1sMwY6QEsFNOtmJN5KDCfjXtJ4LibTxIdTG1axciaQPQ0LfnzUBtYHEPsuNGD3fTN3XC2CB6uyk7vKZwFVj34/640?from=appmsg "REA 官方站点 rea.tools 的社交卡片")

## 二、下载:该有的链接都在这

核心入口:官方仓库 https://github.com/morluto/rea ,官网 https://rea.tools/ ,npm 包 https://www.npmjs.com/package/rea-agents ,一条命令装好 `npx rea-agents@latest setup`,安装文档 https://github.com/morluto/rea/blob/main/docs/installation.md ,MCP 提示词 https://github.com/morluto/rea/blob/main/docs/mcp-prompts.md ,指南 https://rea.tools/guides/ 、案例 https://rea.tools/showcase/ ,第一次调查教程在 https://rea.tools/first-investigation/ 。

仓库本体:MIT 协议,378,411 星、94,526 fork、1153 个未关闭 issue,TypeScript 写的。npm 上 rea-agents 最新 6.7.0(10 月 18 日发布),解压约 27 MB,累计 33 个版本,10 月 9 日到 18 日十天里连发六个版本——社区里"这 CLI 一天更新两三次"的说法基本属实。

工具链仓库:Ghidra(github.com/NationalSecurityAgency/ghidra)、JADX(skylot/jadx)、Frida(frida/frida)、ILSpy(icsharpcode/ILSpy)、x64dbg(x64dbg/x64dbg)、awesome-reverse-engineering 与 rea-gems(sqwu/rea-gems)。

书与论文:《The Ghidra Book》第二版、《Reverse Engineering for Beginners》(go.yurichev.com)、《Practical Binary Analysis》、《Practical Malware Analysis》、《The Android Malware Handbook》、《Reversing》;论文有 LLM4Decompile(arxiv 2403.05286)、AutoDecompiler(2606.16162)、SALT4Decompile(2509.14646)、Decomperson 与 DIRTY 两篇 USENIX,以及 REA 官方那篇《Does reverse engineering need a bigger model?》。

免费课:OST2 x86-64 汇编、pwn.college 的 Reversing 与 Reversing Hell、Malware Unicorn RE101、guyinatuxedo/nightmare、RPISEC MBE、OWASP 移动应用安全。

README 顶部还挂着一句要紧的提醒:只从 morluto/rea、rea.tools 和 npm 官方包三个渠道获取,"名字相近的仓库或抄来的 README 不能证明下载是安全的"。37 万星的项目,仿冒仓库的动机一点不缺。

## 三、五个真实调查,才是这顿正餐

最值钱的不是书单,是五个真刀真枪的调查。

DX-Ball 是把 1996 年的 Windows 游戏重建成可维护的 C 代码:已还原 55 个函数、45,380 次与原程序比对、33 个函数编译产物字节完全一致,检查点停在 10 月 7 日。Aegis 拿 3.4.3 版官方 APK 找六位验证码的生成算法,从 3077 个类里定位到真正出活的方法。Notion 那案子追剪贴板:页面里的 clipboard.write 怎么经 preload 的 ipcRenderer.invoke 走到主进程 ipcMain.handle,最终落到系统剪贴板,通道名是 notion:clipboard:write。TH04 是 PC-98 时代的东方弹幕,原程序一段 2139 字节的代码被完整重建,编译器锁在 Turbo C++ 4.0J。

![七步最佳学习顺序](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6OKDqqoRrlquL1m2NejPdlwG9vdI8lNDNqSq63QVXlzb41XwOJ0M5vQsHicPjxgtTcImURxnrLSFdgPcPcDZoVoLQq9bv7uXLlo/640?from=appmsg "七步最佳学习顺序")

评论区对学习顺序本身有争议。高赞建议"别一上来啃教程,先撞一次真实调查的墙,再回来看文档,点击率完全不一样";也有高赞说"多数人收藏 50 个 GitHub 仓库,最后一个东西都没做出来"。还有一条实用派:把任务拆给 4 个 subagent 并行。

## 四、同一天晚上,门被关上了

![三星电视事件到 Anthropic 收紧的时间线](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6NYiaicluMZQc5mXc0v6vcjCaJicqKMjiaRbZ4lV16K1qQsHHmwITJ5ib0MjFQY8dZJ0bpEt7DRCbC2iaIh7yBSoJGZ3tibcTRQq52h7g/640?from=appmsg "三星电视事件到 Anthropic 收紧的时间线")

路线图爆了 69 分钟后,安全研究员 @0x0SojalSec 发推:"Claude 再也不能 Reverse Engineer Anything 了,Anthropic 悄悄干掉了 REA",拿到 11012 个赞。

时间线往前捋:10 月 21 日,研究员 log4j 逆向自家三星电视固件被 AES 挡住,干脆写零日拿 root,次日复盘列出常驻麦克风、自动内容识别、地理定位、网络测绘、4 套 DRM。10 月 22 日,用户 Irushi 发推说用 Opus 5.5 跑 REA 时,Claude 讲到一半突然触发安全护栏拒答。10 月 23 日晚,一收一放前后脚落地。

Reddit 的 r/claude、r/ClaudeCode、r/ClaudeAI 三个版块同步炸了,标题分别是"Anthropic 悄悄干掉了 REA 列车""梦想结束了""REA 之梦被从源头掐断"。Anthropic 至今没公开确认限制细节,官方仓库和站点也没发过封禁公告,目前都还只是用户侧观察。

好消息是门只关了一扇:REA 官方支持 Claude Code、Codex、Cursor、Gemini CLI、Grok Build 等 agent,仓库 10 月 24 日照常推送更新,npm、官网、Discord 一切正常。

## 五、紫队视角:路线图的价值、风险与合规

红蓝两边都别急着站队。这条推文的价值不在"资源多",而在把一件事讲明白:学逆向的瓶颈从来不是工具清单,而是"从哪个样本开始、拿什么当标准答案"。五个真实调查比六本书有用,是因为每个都自带可验证的验收标准——字节一致、编译产物匹配、公开测试用例能跑通。

风险也在同一处。"几秒钟克隆任意软件"这类视频下面已经有人提醒:"这也是你几分钟收到律师函的方式。"真要复刻别人的产品,干净室才是正解:一边写规格说明,另一边只按规格实现,中间不见原始代码。逆向不违法,越界才违法。

还有一条实操提醒:37.8 万星意味着大量仿冒仓库与篡改版安装包,认准三个官方渠道,核对域名再执行。评论区还有人建议换 abliterated 开源权重模型跑逆向,这条不展开——平台政策自己看。

顺带说一句,就在路线图爆掉的同时,社区出现了另一条路线:把 25 MB 的 MCP 套件换成一个 8 KB 的 SKILL.md,不装服务、不注册 207 个工具,同样能把逆向活干完。工具会换,方法论不会。

## 六、结语

一个有意思的巧合:这个生态在同一晚展示了两种能力——把知识铺到每个人面前,以及给能力划边界。前者靠社区,后者靠平台。紫队看这类新闻不是看谁对谁错,而是看当能力变得极其廉价时,授权、留痕与合规准备好了没有。

**版权声明**:本文由华盟网原创发布,保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6PcUwQ4gMibxXrOOeh8Hz37HcdJicJYUe4zL67suianffq57hpZ8iamOTtfhxRvhc1fm9LoEzXHav7ChFGmmUJU0mtQcnWwL5zOZAM/640?from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MeDyUIcib8TJ7pnOIfeewibY3aKTPILwaVtKBVicZ911Q1hPr89vRekIhhdSKhJv2yozwxcxgbtASIjt17QjlvWpibECnKdVFoX3M/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621549&idx=1&sn=21c4b072726d2387d562109ada6b9bbb&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6P6W16lU48vQicVJu3AWVmyNtoKQdByWH1AO6vJfP4ibBcW3oDJbAia5Rscg8xA2dQswHNh9ibicBRfcXic71TN0hHWmChmb5ZnVahhU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621944&idx=1&sn=3cc6dc9876a20466d4ec3634deb80220&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6OCvmibtQsicJ9ibqHRmziban6C9OLUHPGDOYibRCo56we1iaqJIwCT5Fnjaf6ibEWkxs6qzzpzZkcpWydTqZ1OhqClibaVLhCL1k0DUzA/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650622065&idx=1&sn=09f8ae84c06d4331e71c277b177ae701&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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