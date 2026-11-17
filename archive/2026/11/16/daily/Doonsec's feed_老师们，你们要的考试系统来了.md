---
title: 老师们，你们要的考试系统来了
url: https://mp.weixin.qq.com/s/W-Ak8zp50KmaJl9C3_KL2w
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:27.890152
---

# 老师们，你们要的考试系统来了

# 老师们，你们要的考试系统来了

Ms08067安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

网络安全 · 实验 · 考试 一体化平台

老师们，你们要的
考试系统来了

一套为《网络安全实战教程——基于 Kali Linux 2 的红蓝对抗指南》（人民邮电出版社）配套打造的教学、实训与考试系统。**无需安装虚拟机，浏览器打开即用。**

在线虚拟终端 · 真实工具输出

实时评分 · 加密答卷

这是一套**纯 Web 的网络安全实验教学平台**：学生在浏览器里直接操作一个仿真的 Kali Linux 终端，完成从信息收集、端口扫描、暴力破解到漏洞利用、证据解密的一整套渗透测试实战任务；教师可自由配置题库与命令输出，考完一键判卷、自动排名。2026年11月4日更新版本，修正了显示器分辨率较小时，试题显示不全的问题。

为什么选择它

● **免安装 · 零依赖**

纯 HTML / Web 实现，无需虚拟机与任何系统环境，浏览器一开即用。

● **真实终端仿真**

内置虚拟文件系统，支持 ls / cd / nmap / hydra / john / msfconsole 等命令，模拟真实工具输出。

● **沉浸式剧情任务**

以“破晓行动”反犯罪故事串联六大实战关卡，边做任务边学渗透。

● **实时评分反馈**

每道题按步骤给分，进度条与得分实时更新，完成即见满分提示。

● **加密答卷 · 防作弊**

答卷经加密后提交下载，防止学生查看源码套取答案，保障成绩可信。

● **教师自由配置**

题库、题目分值、命令输出可视化配置，导入导出、改题不改代码。

模拟终端，所见即所得

● ● ● kali@kali — 实验终端

kali@kali:~$ nmap -sV 65.61.137.118

Starting Nmap 7.94 ( https://nmap.org )

PORT    STATE SERVICE

22/tcp  open  ssh

80/tcp  open  http

kali@kali:~$ hydra -l admin -P pass.txt 65.61.137.118 ssh

Hydra v9.4 ( https://github.com/vanhauser-thc/thc-hydra )

[22][ssh] host: 65.61.137.118 login: admin password: 000002

kali@kali:~$ john --show hash.txt

Plaintext: password

学生输入命令，系统即时返回真实工具风格的输出，并同步判分；答题过程完整留痕。

真实界面一览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zalFhdicgeYl02ia2zb1HV7JytDKHWtnjrJkCwIsAEPk9ayEiaWBxrh6kic5xTm6zgz8nzvwtoERTZGLwxcfl4rZPib4LVv1z1NiaP97w/640?wx_fmt=png&from=appmsg)

学生端 · 在线终端实时执行 nmap / hydra，按步骤实时判分

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zakibwjnaHEH43LyAh8YSWYN3HcAccT2QXmJjkVlxaBibcz8zkM8ZbWYX9aooeDUmDtY5OmghcAGEK3ZgeGVFFibg1PZRtMNKAiarkg/640?wx_fmt=png&from=appmsg)

题目内容 · 剧情化任务与分步操作提示，任务驱动式实战教学

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zal52h5OAcJmPRIKg5f0f2n796AcAwdobCJVoLBInWOGhtdFUjwHk3gqNT8G4bU9t8M9rIoah65lt4oeQWGXicVhGfI6mBNFIE5Y/640?wx_fmt=png&from=appmsg)

教师端 · 可视化维护题库与工具，答案保存时自动加密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/BmBdGJk6zanwzROvwvw5zWiawJFpK7mtoDhojhQI0PGVGmXdNJstNOX0IrQITWQMxpsiav3LXkEbDQf4P2icpFrzmx0jhRvtmkt15ZCf3opM8s/640?wx_fmt=png&from=appmsg)

判卷系统 · 拖入加密答卷一键解读，自动生成成绩汇总

一个系统，覆盖教、学、评

01

学生端

登录即考 · 虚拟终端 + 任务面板 · 实时得分 · 加密提交

02

教师端

可视化管理题库 · 配置命令输出 · 导入导出 · 原始 JSON

03

判卷系统

拖入加密答卷 · 一键解读 · 自动生成成绩排名

“破晓行动”实战任务链

以警方侦破网络犯罪为剧情，六大关卡层层递进（当前示例题库，教师可自由替换）

第 1 关 **目录与文件创建** （10 分）

mkdir / touch / echo / ls，建立专属作战工作区

第 2 关 **Nmap 域名与网段扫描** （12 分）

域名扫描、C 段资产测绘、dns-brute 子域枚举

第 3 关 **SSH 服务扫描与暴力破解** （12 分）

crunch 生成密码字典，hydra 对 SSH 发起暴破

第 4 关 **John the Ripper 密码破解** （12 分）

John 字典破解 MD5 哈希，还原隐藏凭证

第 5 关 **Metasploit 漏洞利用** （12 分）

msfconsole 搜索 vsftpd 2.3.4 后门，获取 shell

第 6 关 **解密犯罪遗留文件** （12 分）

find 定位私钥，openssl 解密取证，提取最终线索

五分钟，完成部署

1 **启动服务器**

双击轻量级 MyWebServer.exe，选择平台根目录，一键运行。

2 **配置题库**

教师端添加 / 编辑题目与工具输出，保存即生效。

3 **学生访问开考**

局域网浏览器访问 http://IP，登录姓名学号即可开考。

4 **提交判卷**

学生提交加密答卷，拖入判卷系统生成成绩排名。

适用场景

课堂教学

课后实训

期中期末考试

攻防演练

让每一次实验真实可感，
让每一份答卷可量化评分。

欢迎各位老师体验交流，一起把网络安全实战课做得更扎实、更专业。

立即体验

配套教材 · 人民邮电出版社《网络安全实战教程——基于 Kali Linux 2 的红蓝对抗指南》
网络安全实战教学 · 考试系统

下载地址

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xNfqXicnJdcGAEP7WztKF7PNRBCCdiaHMKkAEY86sc4nPfdwKO4x03e0qxnaicEH0qicict1czNNWHeSvmGI82iaDCBMfSIib5ffgKm50/640?wx_fmt=png&from=appmsg)

⬇️ 阅读原文下载

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XWPpvP3nWa9xKtQcyickhdgvJx9bWxpSjSqS4AwI7o804CbiazVQqTnMibp7ZC6fyxmJ7kgfMyA2rHgHkShs3M7bA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过