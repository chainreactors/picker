---
title: 6 个 WordPress 插件内置严重后门：黑客无需登录即可执行命令
url: https://mp.weixin.qq.com/s/AttLHkmYk_JuPDbppjdkKA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:39:38.918545
---

# 6 个 WordPress 插件内置严重后门：黑客无需登录即可执行命令

# 6 个 WordPress 插件内置严重后门：黑客无需登录即可执行命令

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年11月22日，一名威胁行为者向 WP Connect 旗下 6 个 WordPress 插件推送了带后门的版本，这些插件合计约 3600 个活跃安装。

受影响插件：

1. Air WP Sync

​

2. WP Sync for Notion

​

3. Add‑on Brevo for Gravity Forms

​

4. Add‑On for Contact Form 7 to Airtable

​

5. Add‑On for Contact Form 7 to Notion

​

6. Orders Sync to Airtable for WooCommerce

好在 WordPress.org 的安全防护机制在这些版本到达站点之前就将其拦截。Wordfence 将该漏洞编号为 CVE‑2026‑135202，CVSS 评分 9.8。

⚠️ 目前没有官方补丁——因为代码是被人为植入的，并非编码失误。

6 个 WordPress 插件后门事件

当天下午约两小时内，开发者本人的账号向每个插件在 WordPress.org 仓库提交了新版本。最先中招的是 Air WP Sync，版本 2.9.1 至 2.9.4；其余 5 个在数分钟内相继跟进：

|  |  |
| --- | --- |
| 插件 | 恶意版本 |
| WP Sync for Notion | 1.7.4 |
| Add‑on Brevo for Gravity Forms | 2.6.3 |
| Add‑On for Contact Form 7 to Airtable | 2.5.4 |
| Add‑On for Contact Form 7 to Notion | 1.6.4 |
| Orders Sync to Airtable for WooCommerce | 1.0.2 |

每个版本都新增了一个文件  includes/airwp‑online.php ，并在主插件文件中加了一行  require\_once  引用。6 个文件中有 5 个逐字节完全相同，Air WP Sync 2.9.1 携带的是更早的草稿版本。

由于该开发者名下所有插件都在同一时间段、由同一账号被提交，Wordfence 判断该开发者账号已被攻陷。WordPress.org 插件团队表示开发者自报账号失陷，更多细节尚在核实中。

后门运作方式

据 Wordfence 研究人员介绍，这个模块伪装成一个“在线模块（分析与自动更新）”，宣称可以在正常发布流程之外推送热修复——而这正是 WordPress.org 规范明令禁止的行为。实际上，后门端点被硬编码到域名 tascredit‑pay.com，与插件厂商没有任何关联。

执行与触发逻辑

- 模块挂载到  init  钩子，每次请求都会运行，包括匿名访客浏览页面；

​

- 另外还注册了一个每半小时执行一次的 WP‑Cron 兜底任务；

​

- 不校验登录状态、权限能力（capability）或 nonce 令牌，后台界面上也看不到任何痕迹。

每次“心跳回连”时，后门会向外发送：

- 站点 URL；

​

- PHP、WordPress、操作系统版本；

​

- 服务器运行用户；

​

- 上一条命令的执行输出。

同时它关闭了 TLS 证书校验，因此处于网络路径上的任何人都可以篡改响应内容。

命令执行能力

服务器返回 base64 编码（可选 XOR 加密）的代码，模块直接交给  eval()  执行。唯一的过滤只是剥掉 PHP 标签，因此服务器下发的任何语句都会以完整 WordPress 权限运行。

服务器还可以改写自身端点地址与回连间隔，域名被关停后运营方可迁移到新的基础设施。

内置命令包括：

-  sh ：执行操作系统命令；

​

- 文件读取、写入、删除任意文件；

​

-  db ：导出任意数据表；

​

-  dump\_wp\_users ：返回所有用户的登录名、邮箱与密码哈希；

​

-  webshell ：投放独立 PHP 后门，即使插件被删除后仍能继续工作。

凡是运行过这些版本的站点，等于把服务器交给了控制该 C2 域名的人。

为什么没有大规模爆发

这起攻击撞上了 WordPress.org 于 2026 年 6 月公布的安全计划 Protect The Shire：新插件版本在进入自动更新之前，会有最长 24 小时的冷却期，给人工审核和自动化审核器 Gandalf 留出检查改动的时间。

恶意提交发生在美国东部时间约下午 4:30 至 5:40 之间。发布延迟拖住了这些版本，Gandalf 独立标记出风险代码并叫停了发布。当天晚上，6 个插件全部被关闭。

如果没有这道冷却机制，开启自动更新的站点在下一次检查更新时就会收到恶意代码。

本次事件是继 Essential Plugins 案（插件被卖给恶意新主人）之后，WordPress 生态又一起供应链事件。

Wordfence 的持续监控与漏洞研究代理 PRISM 发现了该威胁并通报团队；研究员 Computeronfire 独立上报了 Air WP Sync 后门。Wordfence 正在编写恶意软件特征库，将优先提供给 Premium、Care 与 Response 套餐用户。其漏洞赏金计划向普通研究员最高支付 31,200 美元，顶尖研究员最高 32,760 美元。

排查与处置建议

受影响站点应该不多，但管理员仍需确认是否安装了上述版本。若发现：

1. 立即卸载对应插件；

​

2. 执行全盘恶意软件扫描；

​

3. 检查  uploads  目录是否存在异常 PHP 文件；

​

4. 核查计划中的 cron 定时任务；

​

5. 若曾运行过被攻陷版本，建议轮换全部密码，因为后门可导出密码哈希；

​

6. 可在网络层面封禁  tascredit-pay.com 。

目前这些插件在 WordPress.org 上处于关闭状态，不存在已修复的版本。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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