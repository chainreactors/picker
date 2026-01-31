---
title: 威胁情报｜Token Vesting 钓鱼投毒分析
url: https://mp.weixin.qq.com/s/_qV7DRKO6L7uqHe7cgDQTQ
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:01:32.782070
---

# 威胁情报｜Token Vesting 钓鱼投毒分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5Bial7u5Ok3w0Ut5cu6ZVUTUwX8uP2EAdvoZ2aBPnWx1icHFiblGnEh4ug/0?wx_fmt=jpeg)

# 威胁情报｜Token Vesting 钓鱼投毒分析

原创

慢雾安全团队
慢雾安全团队

慢雾科技

![]()

在小说阅读器中沉浸阅读

作者：Yao

编辑：77

# 背景

#

**近日，Chainbase 实验室监测并捕获到一起伪装为“审计/合规确认”的钓鱼邮件活动，并将相关恶意样本脱敏后同步给慢雾安全团队，双方联合对该恶意样本开展调查与分析。

攻击者先以“确认公司英文法定名称”诱导收件人回复，随后以“FY2025 外部审计”、“Token Vesting Confirmation 截止回传”等话术持续跟进，并投递恶意的 Word/PDF 附件。通过社会工程诱导受害者打开附件并按提示操作，从而窃取凭据或敏感数据。**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5cq5f3Vl2G6OXDkILW6WZ67fiaZicgBIyRR7VPa0CqZw748q20ice91fNw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm53D3KzYnqA0P955BjpWYOY1eDm3XwVW41e4yYW4MRqpONEcAsSfjiaKQ/640?wx_fmt=png&from=appmsg)

# 木马分析

本次捕获的攻击活动是一场针对 macOS 平台、结合了社会工程学与多级无文件载荷（部分阶段主要以内存执行/临时文件形式存在）的定向攻击 。攻击者利用“审计合规”这一诱导性的业务逻辑，通过伪装的 AppleScript 脚本作为初始入口，并尝试通过诱导授权与 TCC 绕过获得更高的系统/隐私权限，最终在受害者机器上构建了一个基于 Node.js 的远程控制环境。

从样本文件特征来看，邮件附件名为“Confirmation\_Token\_Vesting.docx.scpt”，实际为 AppleScript 脚本(.scpt)，通过双扩展名伪装为 docx 文档。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5ia2T5QVMQHmn5JlTGKUTUrwN0lUTibU2LVZ72h6TIKr18qdHYfz4oS6g/640?wx_fmt=jpeg&from=appmsg)

对脚本内容解码后发现，第一阶段（初始）AppleScript 主要用于下发后续恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5tCVBK8EZHoMgMqY431UaovGvhRqhhKTIFpJc8AyYE6H3l9tc6jlrYQ/640?wx_fmt=png&from=appmsg)

1. 打开 macOS 的系统设置页面并切到“软件更新”，引导用户误以为系统正在进行软件更新/修复。

2. 收集系统信息，读取 CPU 架构(Intel/Apple Silicon)、macOS 版本号、系统语言等并将信息发送至服务端，以便服务器决定下发何种载荷(payload)。

3. 从可疑域名 sevrrhst[.]com 下载并执行脚本，随后清理痕迹。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5nMbUQKd82AZPFVgy1CIr5ojqPBWgC551DsONttHZh0o85lYjDMicnjw/640?wx_fmt=png&from=appmsg)

对下载脚本解码分析后确认其为恶意 AppleScript，具备信息窃取、权限绕过与远程命令执行能力。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5zszejTEkPoD4y5s7qJ2P3VzESY0QlhTD3amax2U7vyn84ME7NtTYRw/640?wx_fmt=png&from=appmsg)

恶意脚本的主要行为：

1. 虚假进度条

脚本首先会弹出一个伪造的进度条窗口，显示正在“修复系统更新问题”或“解决文档查看器问题”。

2. 钓鱼弹窗

在进度条运行期间，它会弹出高度仿真的系统权限/密码输入对话框（伪装成系统设置提示，界面包含 Google 头像元素）：

窃取密码：当用户输入密码并点击“OK”时，脚本会调用 dscl 命令验证密码是否正确。

回传服务器：一旦密码验证通过，它会立即通过 curl 将收集到的用户名与密码进行 Base64 编码后回传至服务器 sevrrhst[.]com。

3. 绕过 TCC 限制

脚本试图修改 macOS 的 TCC (Transparency, Consent, and Control) 隐私数据库：

目录欺骗：它尝试通过重命名 TCC 数据库相关目录(com.apple.TCC) 来规避系统保护机制。

静默授权：它直接向数据库注入 SQL 语句，在用户无感知的情况下，为自己（以及 Bash、终端、脚本编辑器）开启以下权限：

文件访问权限：下载文件夹、文档、桌面、外接磁盘等。

隐私/控制权限：摄像头、屏幕录制、键盘事件监听、辅助功能等。

4. 继续建立后门通道

**下载名为 origin 的加密数据并解码落地执行。

建立与服务器的通信通道，接收远程命令并交由 Bash 执行。**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5cibcngVibnyCvzSkIcZZQljCdeB3GuJ2r2V0GLicrNibMpibvKoMEqSm6hg/640?wx_fmt=png&from=appmsg)

**准备 Node.js 环境后再次请求(req=skip) 拉取核心脚本 index.js 并启动。**

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5Ale8zIpibS9OI04mfFib8HFCWLjicQDUiaK1TYsbRgM1G2T5nfbqdlzkbA/640?wx_fmt=png&from=appmsg)

index.js 收集系统版本、CPU、磁盘、网络与进程等信息并上报；服务端据此下发新的脚本代码，由样本通过 eval 动态执行，从而具备持续扩展能力。

# 恶意域名分析

从威胁情报平台查询显示，该域名 sevrrhst[.]com 注册于 2026 年 1 月 23 日，使用低成本的免费证书，具有典型的“快速抛弃”特征。 其解析关联到 IP 地址为 “88.119.171.59”。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm52kCYTiaricI39mgpUr3r3I7SB4W01mL0eeEzqmVOsA2mmldKzkbpBpibA/640?wx_fmt=png&from=appmsg)

进一步查询发现该 IP 关联到了 tattomc[.]com、stomcs[.]com 等 10 个以上相似恶意域名。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5DibH2At9Niak5HiaEbZsm3YibicKnrlV1D4gjoe9mWY9z7mrRicRorzVpicIw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLZI7Rr2gR0KGian0jWxPZGm5gsTcarib4G3RZbfkgM7khb0HTkAHe3KpEsR6a3cJicz1eJ0ib6RkBOCug/640?wx_fmt=png&from=appmsg)

#

# 总结

该样本并非单一的信息窃取器，而是一条分阶段的渗透链路：先以 AppleScript 诱导交互并窃取凭据/尝试提升权限，再借助 Node.js (index.js) 建立可动态扩展的远控执行框架。其特点是”合法工具被滥用 + 动态代码下发/执行”，对依赖静态特征的检测策略不友好。

建议:

1. 若误点邮件附件/脚本并已执行（或已输入系统密码），请立即断开网络连接；在完成取证、隔离与关键资产备份/转移后，再开展后续处置。

2. 中招用户执行 tccutil reset All 清空 TCC 数据库，移除木马非法获得的授权。

3. 清理恶意程序进程，结束隐藏目录下的恶意 Node.js 进程。

关于 Chainbase 实验室

Chainbase 实验室正在重新定义数据，让它成为 AI 时代真正重要的一类金融资产。通过构建超级数据网络，Chainbase 把分散在链上的各种信号转化为结构化、可验证的数据，让 AI 模型、自主智能体以及各类去中心化应用都能直接使用。

截至目前，Chainbase 网络已经覆盖 200 多条区块链，累计处理超过 5000 亿次数据请求，并支持着一个由 35,000 多名开发者组成的社区。目前已有超过 1 万个项目在使用 Chainbase，应用场景十分广泛，包括安全基础设施、L2 区块浏览器、智能体协议以及链上数据分析等多个方向。

# IOC

filename: Confirmation\_Token\_Vesting.docx.scpt

SHA256:

3e4d35903c51db3da8d4bd77491b5c181b7361aaf152609d03a1e2bb86faee43

filename: env\_arm.zip

SHA256:

f9e0376114c57d659025ceb46f1ef48aa80b8af5909b2de0cf80e88040fef345

filename: index.js

SHA256:

0f1e457488fe799dee7ace7e1bc2df4c1793245f334a4298035652ebeb249414

URL:

https://sevrrhst[.]com/css/controller.php

https://sevrrhst[.]com/inc/register.php

C2: sevrrhst[.]com

IP: 88.119.171.59

**往期回顾**

[慢雾科技(SlowMist) 成立八周年啦！](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504200&idx=1&sn=6ea8c3ccf4aed2fb445905039d700a89&scene=21#wechat_redirect)

[2644 万美元被盗背后：Truebit Protocol 合约漏洞分析](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504176&idx=1&sn=f2cf74e966df087cb6ef9f582938e1e2&scene=21#wechat_redirect)

[慢雾 CISO 23pds 受邀参与「Web3 领袖项目」公开课分享](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504157&idx=1&sn=1979e1ad45483ed613dce71f8fa52a19&scene=21#wechat_redirect)

[慢雾出品 | 2025 区块链安全与反洗钱年度报告](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504119&idx=1&sn=9e6afef4262207a8da1f16a66368ced6&scene=21#wechat_redirect)

[慢雾 Q4 追踪实录：协助被盗客户冻结/追回百万美元资金](https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247504087&idx=1&sn=5325391cb456ec020da8f3b5b47a8178&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbEP8f4tadFenoLauzHpicWdWbVap3aia38LUGPflBho9ibDHXjoG5fecGJSaYa4S4zYdoicXibSmjv9tg/640?wx_fmt=png&from=appmsg)

**慢雾导航**

**慢雾科技官网**

*https://www.slowmist.com/*

**慢雾区官网**

*https://slowmist.io/*

**慢雾 GitHub**

*https://github.com/slowmist*

**Telegram**

*https://t.me/slowmistteam*

**Twitter**

*https://twitter.com/@slowmist\_team*

**Medium**

*https://medium.com/@slowmist*

**知识星球**

*https://t.zsxq.com/Q3zNvvF*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

慢雾科技

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLbCKRaQNEUrvPEphjODejx61A2PcXPPj3dFegU3unrp2nr60oBfYXAZDj99nIXojoia9p6UDy4iaqQw/0?wx_fmt=png)

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