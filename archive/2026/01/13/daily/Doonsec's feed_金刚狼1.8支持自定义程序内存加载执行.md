---
title: 金刚狼1.8支持自定义程序内存加载执行
url: https://mp.weixin.qq.com/s/NO9uFgmbdKrYDPNhFDEUNg
source: Doonsec's feed
date: 2026-01-13
fetch_date: 2026-01-14T03:33:11.428810
---

# 金刚狼1.8支持自定义程序内存加载执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Bua8mEDRSfdMMTvq4m73GDCV3YYv0lOOx8oMfXOKQnQ6dM20JkJWgb22ibctNDZm0j7sEEZ7ZZ2PQJpOWgjPT5w/0?wx_fmt=jpeg)

# 金刚狼1.8支持自定义程序内存加载执行

0x7556

金刚狼不懂安全

![]()

在小说阅读器中沉浸阅读

## 金刚狼 WolfShell

金刚狼：首款支持多层内网级联的ASPX、ASHX高级WebShell管理工具，AES加密通信，无需代理，内存加载渗透工具，无文件落地隐蔽渗透目标，动态代码执行，ShellCode加载(Metasploit/Cobalt  Strike)，反弹Shell，Socks代理，内存马

## 🚀 核心优势

* 高效隐蔽的通信： 采用 二进制流 传输协议，确保通信的高效性与隐蔽性。
* 端到端安全加密： 所有传输 Payload 均经过 AES加密 保护，且每次通信使用 随机密钥，保障数据安全。
* 无痕运行： 支持直接在 内存中加载并执行代码，最大程度避免在磁盘留下痕迹，显著提升操作隐蔽性和安全性。
* 内网级联WebShell控制： 通过现有已控的WebShell，无需部署代理或配置端口转发，即可直接连接并控制处于更深层内网环境中的WebShell节点，实现便捷高效的内网横向穿透。
* Hacking后渗透：通过已控的 WebShell 在内存中加载渗透工具，无需部署代理或配置端口转发，即可执行多个渗透工具实现便捷高效的内网横向渗透。

## 🔥 功能特性

* Shell：支持ASPX、ASHX、ASMX、HTTP、TCP、PS1、EXE、DLL，(目前仅开放ASPX、ASHX、内存马3种类型)。
* 内存马：ASPX一键注入内存马，任意路径访问，每次都可修改shell地址连接，干扰蓝队分析。
* Cmd命令执行： 在目标系统上直接执行任意 CMD 命令。
* 文件管理： 在目标系统上枚举目录文件、新建文件、重命令、删除、设置文件时间等。
* PowerShell执行： 支持执行 PowerShell 代码和命令。
* Shellcode执行： 可在目标环境内直接执行原生的 Shellcode，一键上线Cobalt Strike、Metasploit。
* C#代码执行： 支持动态加载与执行 C# 代码。
* ValidationKey：提取ValidationKey、Validation、DecryptionKey等ViewState反序列化信息
* web.config读取：提取数据库连接信息（数据库名、用户、密码）、SMTP/邮件服务器用户密码等。
* 端口转发： 实现本地端口到远程内网主机的映射，方便安全地访问内部网络服务。
* HTTP代理： 一键内存注入Suo5高性能 HTTP 隧道代理工具。
* EfsPotato： 利用系统服务漏洞进行权限提升。
* BadPotato： 利用系统服务漏洞进行权限提升。
* 内网级联Cmd命令执行： 支持级联内网第2层 WebShell 执行 CMD 命令进行横向移动。
* 内网级联PowerShell执行： 支持级联内网第2层 WebShell 执行 PowerShell 命令进行横向移动。
* SshCmd：SSH 远程命令执行工具，支持对内网主机的命令执行、文件上传下载实现横向移动。
* MysqlCmd：MySQL 数据库连接工具，支持连接内网MySQL，执行查询、导入导出等数据库操作。
* MssqlCmd：SQL Server数据库连接工具，支持连接内网数据库，执行查询、导入导出、横向移动、命令执行、Potato提权等。
* SharpWeb：浏览器凭据抓取工具，支持提取已保存的 Chrome、Firefox、Edge 登录信息与凭据。
* 密码读取: IISpwd wifipwd FileZillaPwd firefoxpwd XshellPwd GetPwd FirefoxHistory FirefoxCookie
* 漏洞检测：MS17010  SMBGhost  HikvisionPoc ActivemqPoc Struts2Poc WeblogicPoc  CVE-2022-36537  CVE-2024-47176 CVE-2022-27925 CVE-2024-27956
* 横向工具：wshell SmbExec WmiExec WmiExec2 AtExec MssqlCmd MmcExec ShellExec ShellBrowserExec
* AI免杀：接入AI人工智能，聊个天就能免杀WebShell。
* Ladon：内网渗透工具集，内存加载无文件落地，包含端口扫描、资产探测、密码审计、漏洞检测、漏洞利用、横向移动等。(工具在集成中，目前已完成10多种协议资产探测，其它模块暂未支持，和potato一样，无法集成所有工具，有些功能可能得使用原程序)

### 金刚狼 WolfShell 1.8 20260113

1.文件管理 支持 任意文件上传

2.自动义.NET程序集内存加载执行

### 自定义.NET程序执行

.NET程序执行： 支持内存加载执行自定义.NET命令行EXE程序集，快速扩展后渗透能力。![exeloader](https://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfekLYR2o36NicQy0QK0kWpO5bCTLKAPobuFRp0lN3AxSSndMhkp7GaiaAboahoMdjn757nLSsCHIgLg/640?wx_fmt=png&from=appmsg)

### Hacking后渗透

Hacking 新增AddUser 绕过杀软EDR\XDR添加系统用户、管理员、域用户、域管理员工具 Hacking 新增NoPowerShell 禁用或没有PowerShell执行PowerShell命令、代码、文件功能(不支持含有 Write-Host 的脚本)

![WolfShell](https://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfekLYR2o36NicQy0QK0kWpO57o7lV8AedloW1l4OB5rS66svyts9eNrtYhdSeyQe266HxmatFtF0pQ/640?wx_fmt=png&from=appmsg)![WolfShell](https://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfekLYR2o36NicQy0QK0kWpO53qylT5aNsLoyuyrnhZACjweRau6zibn7iaIczhWZzyT7V0NfpiaIphStA/640?wx_fmt=png&from=appmsg)

[+]CVE-2025-55182 CVE-2025-55182 Next.js Rce 漏洞利用 [+]NextJSexp CVE-2025-55182 Next.js Rce 漏洞利用

![WolfShell](https://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfekLYR2o36NicQy0QK0kWpO56aicDjP5XkAxlPUEJ4e0mtZbgvRkRAuBpoJqicx2dBmibIWy4FhlnRKPA/640?wx_fmt=png&from=appmsg)

## 下载

Wolfshell：https://github.com/0x7556/wolfshell [2]

## 免责声明

* 使用WolfShell时，请遵循相关法律法规，确保在授权的环境中进行测试和使用。
* 本工具仅供教育和研究目的，任何滥用行为将由用户自行承担后果。

## 关注

* 欢迎大家关注公众号和Github，您的关注、点赞、反馈，将是软件更新的动力来源!

####

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfdqtGg7TaoSf1iayXEx0tQKI7JLXicqPubWia0P4UWmd09JRfOiaicQb7iclpOD1gjCs2xjrEmow3Xib0VaQ/0?wx_fmt=png)

金刚狼不懂安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Bua8mEDRSfdqtGg7TaoSf1iayXEx0tQKI7JLXicqPubWia0P4UWmd09JRfOiaicQb7iclpOD1gjCs2xjrEmow3Xib0VaQ/0?wx_fmt=png)

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