---
title: 飞书的命令行工具 CLI 已开源，人类和 AI Agent 都能在终端中操作飞书
url: https://mp.weixin.qq.com/s/ourM-kikaEGgvSkcyUrerA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:36:47.662842
---

# 飞书的命令行工具 CLI 已开源，人类和 AI Agent 都能在终端中操作飞书

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4y2Wc7qNExRGa65mwP13YNuW5W0MjXl07eZHw9nITf4C0avRsV9B3cPXJCqOITH4UcLPXia1VaiciafbnSlyyoqoxPSXf3qv8lYYVqbaANRkxM/0?wx_fmt=jpeg)

# 飞书的命令行工具 CLI 已开源，人类和 AI Agent 都能在终端中操作飞书

运维帮

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/4y2Wc7qNExRBe272CkgYibKRicKJLuf5J6D5e6FziabB9gqrAy6L4dAHnvs7dXEP7mNyZNhJnavKSiaiaNP4LtBYz3g6tk3ev0ud3MiaiaHGVmp1tE/640?wx_fmt=png&from=appmsg)

**飞书终于可以被 AI 直接操控了**

想象这样一个场景。

你在开会，突然想起下周有个重要 deadline，你对着手机说："帮我查一下下周的日程，看看周三下午有没有空，有的话给张总发个消息约会议。"

然后，这件事就真的被做完了。

不是语音助手那种"好的，我帮您搜索一下"然后什么都没发生。是真的：查了日程、确认了空档、发出了消息。

这不是科幻。这是 **larksuite/cli** 正在做的事情。

---

**飞书用了这么多年，你有没有想过它能被"编程"？**

飞书是中国职场的基础设施之一。消息、文档、多维表格、日历、视频会议……很多人每天在上面工作 8 小时以上。

但有一个问题：飞书的操作，一直只能靠人点点点。

你要发消息，打开飞书，找到联系人，打字，发送。你要查日程，打开日历，翻页，看空档。你要整理会议纪要，打开文档，复制粘贴……

这些操作本身没有任何价值，只是"执行"。而执行，恰恰是 AI 最擅长的事。

问题是：AI 怎么操控飞书？答案来了。

---

**larksuite/cli：飞书的"AI 控制层"**

这是飞书官方开源的命令行工具，托管在 GitHub，MIT 许可，npm 一行安装。

但它的野心不是"给程序员用的工具"。它的定位是：**专为人类和 AI Agent 双重设计的飞书操控层。**

数字说话：覆盖 **11 个业务域**，**200+ 命令**，内置 **19 个 AI Agent Skills，**让 AI 可以直接"学会"操控飞书。

---

**三层架构：人和 AI 都能用**

命令分三层：**快捷命令**（+ 前缀，人/AI 友好，直接说话一样用）→ **API 命令**（跟飞书开放平台同步）→ **原始 API**（全量覆盖）。

这个设计很聪明。`+` 前缀的快捷命令，就是专门为 AI "好理解、好调用"设计的语法糖。

---

**两个场景，感受一下**

🎯 **场景一：AI 替你管会议**

刚结束一小时飞书会议，你说一句："整理纪要，把 action item 发给各自负责人。" AI 自动查录音、提取纪要、拿参会人 ID、逐条发消息。全程不需要你动手。

🎯 **场景二：跨域自动化**

需求评审结束 → 自动创建飞书文档纪要 → 多维表格建任务记录 → 给负责人发通知。以前 30 分钟手动操作，现在 2 分钟跑完。

---

**安全这件事，他们想到了**

🔐 OS 原生密钥链存储，不明文存 token 🛡️ 输入注入防护，防恶意命令注入 👤 支持用户/机器人身份切换，权限边界清晰

---

**为什么这件事值得关注？**

我们正在进入一个新阶段：AI 不只是"生成内容"，而是开始"执行任务"。

执行任务，就需要"手"。浏览器自动化给了 AI 操控网页的手，larksuite/cli 给了 AI 操控飞书的手。而飞书，对中国职场来说，几乎就是数字工作环境本身。

这不是一个工具的问题，这是 AI Agent 进入企业工作流的关键接口。

---

**怎么开始？**

npm install -g @larksuite/cli

三分钟上手。GitHub 搜 `larksuite/cli`，MIT 开源，免费。

因为当你的同事还在一条一条手动发消息的时候，你的 AI 已经帮你都发完了。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/4y2Wc7qNExTy0v01OlxUBwEMdVklUVQ7KHPjfX4mcVzlkMMf2gRvn6r7Lzfz4YoqS6tR0sf2p2Hxf88Mpy5r9Bl34kDzkqITpPCzKmyt5MA/0?wx_fmt=png)

运维帮

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/4y2Wc7qNExTy0v01OlxUBwEMdVklUVQ7KHPjfX4mcVzlkMMf2gRvn6r7Lzfz4YoqS6tR0sf2p2Hxf88Mpy5r9Bl34kDzkqITpPCzKmyt5MA/0?wx_fmt=png)

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