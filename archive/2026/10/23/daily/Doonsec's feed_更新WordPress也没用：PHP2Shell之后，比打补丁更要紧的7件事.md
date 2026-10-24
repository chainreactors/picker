---
title: 更新WordPress也没用：PHP2Shell之后，比打补丁更要紧的7件事
url: https://mp.weixin.qq.com/s/FpTOYRaTu1G6mb21qVgIzw
source: Doonsec's feed
date: 2026-10-23
fetch_date: 2026-10-24T06:43:40.282717
---

# 更新WordPress也没用：PHP2Shell之后，比打补丁更要紧的7件事

# 更新WordPress也没用：PHP2Shell之后，比打补丁更要紧的7件事

原创

小新聊攻防
小新聊攻防

小新聊攻防

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

应急响应手记2026.10.23

WordPress 升到最新版就安全了

补丁发了三天 · 还有 6 件事

出问题的不是你网站上的代码，是跑网站的 PHP 解释器本身。

DOODLE

CVSS 9.2 未授权 RCE，升级只是第 1 件

PHP2Shell应急自查

![OpenAI 官方推文](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AicUZTtzsicaYHeJhDrJrFIIRzjBjrGBHQ7YqULPuq70OWic0mcMjRkEt3q1Dpyx8RlGqBr7oyRg9iaC4PGvWGxTH3vtB6padjDtJQOtTGgCfPA/640?wx_fmt=jpeg&from=appmsg)

OpenAI 官方推文：PHP 漏洞影响约 70% 的网站

这两天，后台被问得最多的一句话是：

READER'S QUESTION

后台高频提问

「我 WordPress 已经升到最新版了，应该安全了吧？」

答案是：没用。

因为这次出问题的，不是你网站上的代码。是跑你网站的 PHP 解释器本身。

![pixiv 紧急维护](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AicUZTtzsicaZPiaWB8yvp2vIjZnRicESGkQHCUPXqzMLyoicqcwoLqibTyXcSrpeNrpQp9J0YATg8RKVXNzbzVwdL1uorNXmlU0YOQqR5w9deLNw/640?wx_fmt=jpeg&from=appmsg)

pixiv 当晚 19:00 起紧急维护，涉及 pixiv、百科事典、FANBOX

**10 月 21 日，PHP 官方发布 PHP2Shell** CVE-2026-109618 / CVE-2026-109619，CVSS 9.2，未授权远程代码执行。

同一天，pixiv、维基媒体、荷兰 DigiD、鹿特丹港、芬兰政府服务、法国内政部……一批网站陆续下线。

补丁已经发了三天。但今天想说的不是「快去升级」这四个字：升级只是第 1 件，后面还有 6 件更要紧的事。

01

PART

先确认：你在不在那张名单里

CHECK YOUR VERSION

![高危漏洞清单](https://mmbiz.qpic.cn/mmbiz_jpg/AicUZTtzsicaZvR3PKyxpoMttO9Mr4NmHicmq9TQGNjK1G9l05JlmGxsdIl50jCSicRQIZzfBGYSpYAFibhVrkVvPxfGuJde8D2WeNHf9ibwfWgMY/640?wx_fmt=jpeg&from=appmsg)

高危漏洞清单第一行：PHP 8.2–8.5，CVSS 9.2，在利用「否」

看清单第一行，PHP 8.2–8.5，CVE-2026-109618 / 109619，未认证 RCE，CVSS 9.2。

注意「在利用」那一栏写的是「否」。别高兴太早，准确说法是：CISA 发布公告时称尚未观测到利用，但 Cloudflare、Patchstack 都报告了早期利用尝试，攻击者还在实时变形 payload 绕 WAF。

现在打开终端，跑一句：

...bash

php -v

对照这张表：

你的分支

安全版本

结论

8.5.x

8.5.12

升级

8.4.x

8.4.27

升级

8.3.x

8.3.36

升级

8.2.x

8.2.35

升级

8.1 / 8.0 / 7.4

最小化回移植

联系发行版/LTS 厂商

5.4 – 7.3

无修复

EOL，必须升级

用发行版软件包的注意：版本号可能和上游不一致（backport），得跟厂商确认。用 rpms.remirepo.net 的，发布当天不会有更新，官方建议切换包源或自己从源码编译。

02

PART

为什么你更新 WordPress 一点用都没有

WHY PATCHING WP IS USELESS HERE

这是这次事件最反常识、也最容易被忽略的一点：

**攻击发生在你的应用代码执行之前。**

PHP 处理每个请求，会先解析 multipart 上传这类底层数据，这个时机早于 WordPress、Drupal、Laravel 这些应用的初始化。也就是说：你的插件全是新版、代码审计做得再干净，PHP 内核这一层也已经被打了。

Wiz 的原话是：一个跑在受影响版本上的 “Hello World” 应用，同样可能被打。

EDITOR'S NOTE

部署形态决定风险高低

Apache + mod\_php 风险最高（默认配置下，未认证请求就能在应用代码运行前触发）；PHP-FPM、php-cgi、FrankenPHP、LiteSpeed 也都在范围内。

更麻烦的是，除了 RCE，还有一条内存泄露路径，路数有点像当年的 Heartbleed，能把 PHP worker 进程内存里的密码、Token、API Key 读出来，还不需要先拿到 RCE。

**WordPress 本身不需要更新** —— WordPress 官方说得很直白：需要更新的是服务器上的 PHP。

03

PART

补丁之后，必须做的 7 件事

POST-PATCH CHECKLIST

STEP 01升级后，重启每一个 PHP worker

这是最常被漏掉的一步。不重启，旧进程还在跑漏洞代码。容器环境要重建每一个副本，不是只换个镜像。

STEP 02关掉 session.upload\_progress

session.upload\_progress.enabled=0，并重启每个 worker。必须在请求解析之前生效，写在 php.ini / FPM pool / 服务器配置里。用 ini\_set() 或 .user.ini 是没用的。

STEP 03收紧请求体这道口子

memory\_limit=-1 用 php\_admin\_value 设置（应用无法覆盖）；不需要上传就 post\_max\_size=8M，需要就 32M，且 upload\_max\_filesize 要小于它。

STEP 04翻日志，找三个信号

* 异常 multipart POST，尤其是本来不该接受上传的端点
* 请求后紧跟大量 HTTP 500
* 响应里的 PHPSESSID Cookie 异常大或畸形，这是内存泄露的明确信号

STEP 05查主机：worker 有没有「生孩子」

PHP / Web 服务器 worker 进程派生子进程（shell、解释器、下载工具），Web 目录文件或计划任务被改，异常外连。这些都是被拿下的迹象。

STEP 06把密钥当成已泄露来处理

内存泄露路径可能读走的是其他请求的密码、认证 Token、API Key、证书。出现可疑迹象时，这个 PHP 进程掌握的所有密钥都要轮换：改口令、换 Token、重签证书。

STEP 07先保全日志，再重启

顺序错了，证据就没了。重启或重建可疑系统之前，先把 Web、PHP、应用、主机日志备份出来。

第 1 件和第 7 件最容易做反：一个该做的没做，一个不该先做的先做了。

SUMMARY

04

PART

补丁 = 遏制，不等于干净

CONTAINMENT ≠ CLEAN

这句是官方反复强调的，但很多人没读进去。

这两个漏洞是未授权 RCE。如果在你打补丁之前，已经有恶意流量打到运行时，那个 worker 可能已经执行过攻击者的代码了。打补丁只是把门关上，人可能已经进屋了。

正确的处置顺序

保全日志排查 IOC轮换密钥清理后门再重启/重建

CISA 和 NSA 的建议更狠：无法立即更新的系统，直接下线。英国 NCSC 建议评估是否已被入侵，必要时请事件响应服务商。

国内口径

工信部 NVDB

工信部 NVDB 定级「超危」，建议排查升级，或采取临时下线、关闭会话上传进度、网络隔离等措施，并加强监测、及时修改账号口令密钥。

**打完补丁只是「止血」。** 有没有被进屋，得靠日志说话。

05

PART

整套自查清单，整理好了

THE KIT

上面 7 件事，光靠记是记不住的。我们把可执行的版本整理成了一份《PHP2Shell 自查与应急资料包》：

01 版本自查对照表（可打印）

四个分支 + EOL 分支，一页纸贴机房。

02 7 件事执行清单

每一条都带具体配置项和验证方法。

03 IOC 排查 Checklist

日志侧 / 系统侧 / 主机侧三张表，逐项打钩。

04 应急响应 Runbook

从发现异常到恢复上线的完整流程。

05 事件时间线复盘

从 2024 年埋雷到补丁日，搞清来龙去脉。

HOW TO GET

公众号后台回复「666」立即领取

免费

完整资料包免费发送，持续更新

数据说明与合规

DISCLAIMER

官方评级为 CVSS v4.0 = 9.2，非 10.0；截至发稿，多家厂商观测到早期利用尝试，但尚缺大规模成功利用的公开证据；22.6M 为 Unit 42 遥测口径的「潜在暴露实例」。本文只讲自查与修复，不提供任何 PoC 或攻击步骤。请遵守《网络安全法》，仅对自有或已获授权的资产进行操作。

///

END

临了说一句

LAST WORD

这次事件最有价值的地方，不是那个 9.2 分，也不是 AI 挖洞的噱头。

是它让所有人看清了一件事：安全不是一个补丁，是一整套动作。升级、重启、收敛、排查、轮换、验证。缺一步，前面全白做。

**补丁会过期，动作不会。**

![](https://mmbiz.qpic.cn/mmbiz_png/AicUZTtzsicabmfsCd6Wfz6zLiaFXvGh2TNCj1hPXGFfZWdX1ljlKCAbaB9TZNiaiboAOwHGUoG4Oiaz0AFQJib2LsS7bkmtsz9xX9fjtIiateGU0ks/640?wx_fmt=png&from=appmsg)

如果你觉得今天这篇有收获，欢迎点赞、在看、转发三连，我们下篇见。

关注我，少踩一个坑

赞

在看

收藏

THANKS FOR READING

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/AicUZTtzsicabZBWH5nYImne6P6HJfAIRoZdPVLomo6aaDwcMaMSkx7pgkKvfEJ2LVMGF497uLKSy07666p0gJkQiaSI0qQrgFqabBRv26IFXc/0?wx_fmt=png)

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