---
title: 群晖NAS遭大规模L0CK3D勒索病毒攻击（修复方案）
url: https://blog.upx8.com/%E7%BE%A4%E6%99%96NAS%E9%81%AD%E5%A4%A7%E8%A7%84%E6%A8%A1L0CK3D%E5%8B%92%E7%B4%A2%E7%97%85%E6%AF%92%E6%94%BB%E5%87%BB
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-10-29
fetch_date: 2026-10-30T07:55:10.019759
---

# 群晖NAS遭大规模L0CK3D勒索病毒攻击（修复方案）

[![黑海洋](https://blog.upx8.com/logo.webp)
黑海洋
WIKI](https://blog.upx8.com/)

[首页](https://blog.upx8.com/)
[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)
[关于](/about.html)

在线工具

[极

**极简文本**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IP查询**
*ip.upx8.com*](https://ip.upx8.com/)
[哈

**哈希计算**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTD交易查询**
*18u.in*](https://18u.in)
[三

**三角洲辅助站**
*sjz.upx8.com*](https://sjz.upx8.com/)
[开

**开发者工具箱**
*tools.upx8.com*](https://tools.upx8.com/)

[首页](https://blog.upx8.com)
/
[资讯](https://blog.upx8.com/news)
/
群晖NAS遭大规模L0CK3D勒索病毒攻击（修复方案）

# 群晖NAS遭大规模L0CK3D勒索病毒攻击（修复方案）

[资讯](https://blog.upx8.com/news)
10-29
·
约 8 分钟
·
黑海洋
·

1.4万

10 月 28 日前后，大量群晖 NAS 用户发现文件被加密成 .L0CK3D 后缀，目录里多了 read-me3.txt。截至 10 月 30 日，群晖已发布 DSM 和 PHP 套件的安全更新，但已加密的文件还没有官方解密工具，所以没中招的人先打补丁、关公网，中招的人先保住现场。

## 一、事件回顾：从零星求助到集中爆发

这次攻击在 10 月初就有零星报告，10 月 28 至 29 日在中文社区集中出现。360 反勒索团队称，自 10 月起陆续接到群晖 NAS 的求助，并把样本归为 Cerber 家族的变种 C3RB3R。

受害者看到的现象高度一致：

* 照片、文档、代码仓库和备份文件的后缀被改成 **.L0CK3D**（其中是数字 0，也有人写作 .LOCK3D）。
* 每个目录里多出勒索说明 **read-me3.txt**，指向一个 Tor 站点，要求用加密货币购买“解密器”。
* 加密结合了 ChaCha8 和 RSA-2048，没有私钥无法靠改后缀名恢复。
* 部分设备的 Docker 套件被卸载，个别设备的 IP 被改掉，导致内网里找不到 NAS。
* 有报道称勒索程序从系统根目录开始扫描，覆盖 /volume1、/volume2 等所有已挂载的存储。

群晖在 10 月 22 日发布了 PHP2Shell 声明和套件更新，10 月 29 日更新了对应公告。据报道，群晖也已确认这次攻击并呼吁用户立即更新。

## 二、入侵路径：多数分析指向已有补丁的漏洞

攻击入口目前没有最终定论，但较多证据指向群晖已经修复的漏洞，也就是未更新设备遭到“1-day”攻击。几条说法并不互相排斥，不同设备的入口可能不同。

| 说法 | 依据 | 说明 |
| --- | --- | --- |
| DSM 漏洞 CVE-2026-13639 与 CVE-2026-13684（SA-26:13） | 360 反勒索团队处置的多起事件 | 未授权即可任意读写文件，CVSS 9.8，群晖未给出缓解方案，目前最常被引用 |
| PHP2Shell 套件漏洞 CVE-2026-109618 与 CVE-2026-109619（SA-26:14） | 媒体报道与群晖声明 | 只影响装了依赖 PHP 的套件的设备，如 Web Station、WordPress、Mail Station、Calendar |
| 旧漏洞 CVE-2024-10441（SA-24:20） | 一位 DS918+ 用户的取证复盘 | 单个案例：网页界面暴露公网，固件落后约 18 个月 |
| GitLab、Docker 等容器服务 | 早期受害者运行 GitLab CE 容器 | 后续有人把根因指向 DSM 漏洞而非 GitLab，尚无定论 |
| 系统 0day | 社区早期推测 | 没有公开证据，多数分析反而指向已有补丁的漏洞 |

这几个入口有一个共同点：设备都暴露在公网，或者长期没有更新。此前有说法认为问题不在 DSM 本身，现在看这并不准确，至少有一条证据线指向 DSM 自身的漏洞。

## 三、官方修复方案：三处都要检查

群晖没有对 SA-26:13 提供临时缓解办法，唯一的解法是升级。要同时检查 DSM 系统版本、PHP 相关套件，以及是否还停在 2024 年的旧版本。下表的版本号来自第三方转述，升级前请以群晖官网公告和你自己型号的更新页面为准。

| 公告 | 修复对象 | 做法 |
| --- | --- | --- |
| SA-26:13（2026 年 9 月 18 日） | DSM 系统，共 8 个漏洞，其中 2 个 CVSS 9.8 | 升级 DSM |
| SA-26:14 PHP2Shell（10 月 22 日首发，10 月 29 日更新） | PHP 7.4 与 8.0 至 8.4 套件、Synology Calendar、Mail Station 等 | 在套件中心更新 PHP 套件，依赖它的套件会自动重启，Mail Station 需手动更新 |
| SA-24:20（2024 年 12 月） | CVE-2024-10441，系统插件守护进程远程代码执行 | 升级 DSM 到下表对应版本以上 |

各 DSM 分支至少应升级到的版本如下，实际请尽量升到所在分支的最新版。

| DSM 分支 | SA-26:13 修复版本 | SA-24:20 修复版本 |
| --- | --- | --- |
| 7.4 | 7.4-90075 | — |
| 7.3.2 | 7.3.2-86009-4 | — |
| 7.2.2 | 7.2.2-72806-9 | 7.2.2-72806-1 |
| 7.2.1 | 7.2.1-69057-12 | 7.2.1-69057-6 |
| 7.2 | — | 7.2-64570-4 |

几点补充：

* PHP 7.3 已终止支持，不会有补丁，仍使用它的套件需要迁移到更新的 PHP 版本。
* DSM 7.2 之前的版本，群晖建议先临时停用受影响的套件，再更新到已修补的版本。
* DSM 自带的内部 PHP 组件，群晖评估为风险极小，会在后续 DSM 版本中修补。
* 有受害者反映，DSM 界面显示“已是最新”，但关键安全修复需要手动安装，所以要核对具体版本号，不要只看更新提示。

## 四、还没中招：今天就该做的事

最优先的是打补丁并断开公网暴露，其余措施只是辅助。

* 在 DSM 里确认系统版本号，对照上一节的表升级
* 在套件中心更新所有 PHP 套件、Synology Calendar、Mail Station，并迁移仍在用 PHP 7.3 的套件
* 卸载或停用不用的 Web Station、WordPress、phpMyAdmin 等网站类套件
* 关闭路由器上对 NAS 的端口映射（5000、5001、80、443 等），远程访问改用 VPN 或 Tailscale；更新补丁时可先关端口映射，再让 NAS 联网
* 更新 Docker 或 Container Manager 里的容器镜像，尤其是 GitLab 这类暴露在外的服务
* 自查是否已有迹象：文件后缀变成 .L0CK3D 或 .LOCK3D、目录里出现 read-me3.txt、容器被卸载、NAS 的 IP 被改
* 确认有一份离线或异地、平时不挂载的备份，并试着恢复一个文件验证
* 可选：开启 Fail2ban 或自动封锁，限制境外 IP 访问

## 五、已经中招：先保住现场，再谈恢复

头几个小时的操作决定后面还能不能救回数据。下面的恢复路线来自社区和个人取证记录，并非官方方案，不保证成功，建议交给有经验的安全或数据恢复人员处理。

1. **立即断网**：拔网线、关 Wi-Fi，阻止继续加密和回传。
2. **先别重启、别拔电源、别 kill 进程**：如果加密进程还在运行，密钥可能还在它的内存里。有人建议由懂行的人确认进程后用 SIGSTOP 暂停，再采集进程内存和样本。
3. **保留证据**：留下勒索信 read-me3.txt、系统日志和被加密的原文件，不要删除、格式化、重装系统。
4. **不要用来路不明的“解密工具”**，也不要盲目套用旧版恢复工具，它们可能覆盖残留数据。
5. **加密已经结束的设备**：可以关机，把硬盘挂到另一台机器上只读检查，避免继续写入。
6. **向群晖报告**：整理好日志和勒索信，反馈给官方。

目前社区整理出三条恢复路线：

| 路线 | 前提 | 要点 |
| --- | --- | --- |
| 从进程内存提取密钥 | 加密进程仍在运行，且没有被结束 | 暂停进程并转储内存，由此尝试还原密钥，需要专业分析 |
| 利用 Btrfs 写时复制找回旧数据 | 卷是 Btrfs，且加密过程留下未被覆盖的数据块 | 据称可借助“间歇性加密”留下的空隙重构部分文件，只能找回一部分 |
| 历史快照和独立备份 | 快照或备份没有一起被加密 | 最稳妥的一条，前提是备份不在同一台被攻击的机器上 |

## 六、三个常见误区

* **RAID 不是备份。** RAID 只防硬盘损坏，勒索程序加密的是文件本身，加密后的文件会被忠实地同步到每一块盘。
* **同步不是备份。** 有人发现 Cloud Sync 正在把勒索说明文件同步到多个网盘，只是因为另有一台下班后关机的备份机才没有损失。
* **改端口和二次验证不能代替补丁。** 有受害者自述已改掉默认端口、开了二次验证，仍被加密了 8T 数据。

## 小结

这次事件的要点是：补丁已经发布，入口仍未完全确认，但多数分析指向没有及时更新、又暴露在公网的设备。没中招的，先更新 DSM 和 PHP 套件，关掉端口映射，远程走 VPN，并保留一份离线备份。已经中招的，先断网、留证据、别乱动，再找专业人员尝试恢复。事件仍在变化，本文信息截至 2026 年 10 月 30 日。

## 来源

* [群晖声明：PHP2Shell 漏洞](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuc3lub2xvZ3kuY29tL2VuLWdsb2JhbC9jb21wYW55L25ld3MvYXJ0aWNsZS9waHAyc2hlbGw)
* [Synology-SA-26:14 PHP2Shell](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuc3lub2xvZ3kuY29tL3NlY3VyaXR5L2Fkdmlzb3J5L1N5bm9sb2d5X1NBXzI2XzE0)
* [PCM：PHP2Shell 引爆勒索风暴](https://blog.upx8.com/go/aHR0cHM6Ly93d3cucGNtYXJrZXQuY29tLmhrL3N5bm9sb2d5LW5hcy1waHAyc2hlbGwtYzNyYjNyLXJhbnNvbXdhcmUtc2VjdXJpdHktdXBkYXRlLw)
* [Guru3D：L0CK3D 勒索攻击](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZ3VydTNkLmNvbS9zdG9yeS9zeW5vbG9neS1uYXMtZGV2aWNlcy1oaXQtYnktbDBjazNkLXJhbnNvbXdhcmUtY2FtcGFpZ24v)
* [IT-Connect：C3RB3R 攻击群晖 NAS](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuaXQtY29ubmVjdC50ZWNoL2MzcmIzci1yYW5zb213YXJlLWlzLWhpdHRpbmctc3lub2xvZ3ktbmFzLWRldmljZXMtaG93LXRvLXByb3RlY3QteW91cnMv)
* [PBX Science：SA-26:13 修复版本表](https://blog.upx8.com/go/aHR0cHM6Ly9wYnhzY2llbmNlLmNvbS9zeW5vbG9neS1uYXMtcmFuc29td2FyZS1hbGVydC1jM3JiM3ItYXR0YWNrcy1oaXQtdW5wYXRjaGVkLWRldmljZXMtdXBkYXRlLWRzbS1ub3cv)
* [IPSIP：SA-24:20 版本门槛](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuaXBzaXAudm4vZW4vcG9zdC9jM3JiM3ItcmFuc29td2FyZS1zeW5vbG9neS1uYXM)
* [LAVX：DS918+ 取证案例](https://blog.upx8.com/go/aHR0cHM6Ly9uZXdzLmxhdnguaHUvYXJ0aWNsZS9yYW5zb213YXJlLWhpdHMtaW50ZXJuZXQtZXhwb3NlZC1zeW5vbG9neS1uYXMtdmlhLTE4LW1vbnRoLW9sZC1yZW1vdGUtY29kZS1mbGF3)
* [什么值得买：文件一夜变成 LOCK3D](https://blog.upx8.com/go/aHR0cHM6Ly9wb3N0LnNtemRtLmNvbS9wL2FudjkwZXgwLw)
* [LINUX DO：救灾直播帖](https://blog.upx8.com/go/aHR0cHM6Ly9saW51eC5kby90L3RvcGljLzMwODUwODI)
* [羊刀仙的部落格：恢复路线](https://blog.upx8.com/go/aHR0cHM6Ly9ibG9nLnlkeGlhbi54eXovYXJjaGl2ZXMvcXVuaHVpbGVzdW8)

收藏

分享

报告错误

分享这篇文章

微信扫一扫

在手机上继续阅读

复制

扫码后直接打开这一页

[上一篇
美国国土安全部遭黑客入侵 逾4万员工资料外泄](https://blog.upx8.com/%E7%BE%8E%E5%9B%BD%E5%9B%BD%E5%9C%9F%E5%AE%89%E5%85%A8%E9%83%A8%E9%81%AD%E9%BB%91%E5%AE%A2%E5%85%A5%E4%BE%B5-%E9%80%BE4%E4%B8%87%E5%91%98%E5%B7%A5%E8%B5%84%E6%96%99%E5%A4%96%E6%B3%84)
[下一篇
封缄笔记：写完，封起来，只寄给一个人](https://blog.upx8.com/10906)

## 相关文档

* [VPS云服务器一键DD安装飞牛NAS（fnOS）脚本教程
  07-30](https://blog.upx8.com/VPS-DD-NAS-fnOS)
* [救援飞船发射升空 防NASA雨燕天文台坠落
  07-05](https://blog.upx8.com/%E6%95%91%E6%8F%B4%E9%A3%9E%E8%88%B9%E5%8F%91%E5%B0%84%E5%8D%87%E7%A9%BA-%E9%98%B2NASA%E9%9B%A8%E7%87%95%E5%A4%A9%E6%96%87%E5%8F%B0%E5%9D%A0%E8%90%BD)
* [🖼 NASA测试新型探测车：速度更快且可独立抬升车轮跨越障碍
  06-21](https://blog.upx8.com/NASA%E6%B5%8B%E8%AF%95%E6%96%B0%E5%9E%8B%E6%8E%A2%E6%B5%8B%E8%BD%A6-%E9%80%9F%E5%BA%A6%E6%9B%B4%E5%BF%AB%E4%B8%94%E5%8F%AF%E7%8B%AC%E7%AB%8B%E6%8A%AC%E5%8D%87%E8%BD%A6%E8%BD%AE%E8%B7%A8%E8%B6%8A%E9%9A%9C%E7%A2%8D)
* [Linux内核高危漏洞Fragnesia深度分析：原理、影响与修复方案
  05-13](https://blog.upx8.com/Linux-Fragnesia)

## 评论与补充0

有问题或想补充的，写在下面 · 选中正文文字再点「报告错误」会自动引用

还没有评论。有疑问、补充，或者发现错字，都可以写在下面。

回复
取消

请勿填写此栏

就事论事，别发广告 · 正常评论
发表评论

本文目录

* [一、事件回顾：从零星求助到集中爆发](#一事件回顾从零星求助到集中爆发)
* [二、入侵路径：多数分析指向已有补丁的漏洞](#二入侵路径多数分析指向已有补丁的漏洞)
* [三、官方修复方案：三处都要检查](#三官方修复方案三处都要检查)
* [四、还没中招：今天就该做的事](#四还没中招今天就该做的事)
* [五、已经中招：先保住现场，再谈恢复](#五已经中招先保住现场再谈恢复)
* [六、三个常见误区](#六三个常见误区)
* [小结](#小结)
* [来源](#来源)

[![黑海洋](https://blog.upx8.com/logo.webp)
**黑海洋**
WIKI](https://blog.upx8.com/)

黑海洋专注 AI 智能体、程序开发、开源工具与免费资源分享，提供保姆级部署教程、源码下载、云服务器运维与安全资讯。

分类

[资源](https://blog.upx8.com/Free)
[安全](https://blog.upx8.com/os_security)
[开发](https://blog.upx8.com/code)
[资讯](https://blog.upx8.com/news)

常用

[全部文档](https://blog.upx8.com/all.html)
[RSS 订阅](https://blog.upx8.com/feed/)
[RSS 评论](https://blog.upx8.com/feed/comments/)
[Sitemap](/sitemap.xml)

关于

[关于本站](/about.html)
[友情链接](htt...