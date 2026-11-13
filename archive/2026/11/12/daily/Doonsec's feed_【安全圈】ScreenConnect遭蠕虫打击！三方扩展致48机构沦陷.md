---
title: 【安全圈】ScreenConnect遭蠕虫打击！三方扩展致48机构沦陷
url: https://mp.weixin.qq.com/s/fJhKgzRFY1mGWzutYOpwkw
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:57:31.925165
---

# 【安全圈】ScreenConnect遭蠕虫打击！三方扩展致48机构沦陷

# 【安全圈】ScreenConnect遭蠕虫打击！三方扩展致48机构沦陷

安全圈
安全圈

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

蠕虫打击

**核心事实**：北京时间 11 月 12 日凌晨（UTC 11 月 11 日 17:47 起），安全机构 Huntress 在 90 分钟内观测到多套云托管 ConnectWise ScreenConnect 控制台被批量下发高危指令，导致至少 **48 个组织的 288 台终端**（含 6 家以上 MSP 服务商）被植入流氓客户端与蠕虫工具包 `SCKit`。最新取证锁定入口为第三方扩展 **RMM+（1.0.31 / 1.0.32）** 默认密钥为空引起的认证绕过，ConnectWise 已紧急在约 400 个托管环境中停用 5 款关联扩展。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyE8c9V6pY325MVu5aB1oCKOvmS27dZoV4ftdibfXWBWiaEIB5LtPLNOhP53aXzZjhGX3ibSQbDyELyWetDiaPuZm2cRwe12qGhVXfs/640?wx_fmt=other&from=appmsg)

## 🔍 真凶锁定：RMM+ 扩展默认空密钥架空 MFA

攻击爆发初期，许多一线运维一度担心是 ScreenConnect 主程序再现零日漏洞。ConnectWise 于 11 月 11 日 22:45 UTC 发布紧急通告澄清：ScreenConnect 核心代码及官方云基础设施均未遭攻破，但系统日志指向 5 款独立第三方扩展，官方已在超过 400 个合作伙伴云环境中先行禁用 `Labtech Plus`、`RMM Plus`、`RMM+`、`RMM Plus Password Link` 与 `RMM+ Password Link`。

北京时间今天中午，Huntress 更新调查结论，直接坐实了第三方扩展 `RMM+` 的漏洞细节：`RMM+` 本身的设计是让外部自动化工具无需登录控制台即可远程操控会话，它会直接跳过 ScreenConnect 原生账号、权限角色与 MFA 校验，只认配置项 `RMMPlus.AccessKey`。但在 1.0.31 与 1.0.32 版本中，该参数的 `<DefaultValue></DefaultValue>` 默认为空且校验逻辑不拦截空值。只要管理员当初装完扩展忘了手动填写密钥，攻击者发一个空口令 POST 请求就能以 `SYSTEM` 权限向管辖终端批量丢指令，控制台里甚至留不下任何登录记录。当前最新的客户端版本 `26.6.6.9747` 与 `26.7.6.9783` 均受此链路波及。

## ⚡ SCKit 蠕虫链拆解：偷天换日占槽位，反手伏击技术员

进攻在前 10 分钟内就击穿了近三分之一的受影响设备。控制台 Run Command 首先将攻击者自建服务器的安装包下载至 `C:\Windows\TEMP\sc.msi` 静默部署（流氓客户端 ID 为 `2588ef5c15954b10` 与 `ed630cc2c873b091`），紧接着写入批处理 `sckit-run.bat` 与解码器 `sckit-decoder.ps1`。脚本会把当前 Windows 机器的 UUID 作为 URL 参数回传服务器，以此换取仅限本机解密的 Key/IV/Salt，将由 16 个文件组成的 `SCKit` 释放至 `C:\ProgramData\RelayTrap\`。

* 💻 **伪装接管与系统锁死**：`Installer.ps1` 添加 Microsoft Defender 排除项并安装第二个恶意客户端，同时下发 SRP/AppLocker 规则阻止合法目录文件运行。随后以 `SYSTEM` 运行的计划任务 `TrapWatch` 每 10 秒检查一次，现场编译 `RelayTrap.cs` 生成 `RelayTrap.exe`（代码注释高度疑似由大语言模型生成），直接停掉原厂服务并顶替其在合法中继服务器上的连接槽位，让受害机器在管理员界面依然维持“正常在线”假象。
* 💥 **针对技术员的二次横向陷阱**：代码逆向显示，一旦 MSP 技术员用控制台远程连入这台已感染的终端，连接建立 2.5 秒后恶意服务会自动向技术员本机投递并运行 `Run-Lateral-Full.bat`。随后的 `Panel-Lateral.ps1` 配合 `Sqlite3.exe` 读取浏览器 Cookie 数据库，窃取技术员的 `.aspxauth` 登录会话，再驱动 32 位 .NET 程序 `ToolboxRelayUploader.exe` 将 `WithUninstall.ps1` 传至后台 Shared Toolbox，一键向该技术员权限下的所有客户终端广播执行，并在约 60 秒后自动删除工具箱文件毁灭证据。（Huntress 注：本轮现场日志中暂未观测到该反向跳板成功打通工作站的实例。）

## 🎯 IOC 特征指标与应急隔离红线

BleepingComputer 溯源进一步指出，2026 年 7 月一份名为 `SSA-2026-STATEMENT-15518787.bat` 的历史样本中就曾出现过同一恶意客户端 ID `ed630cc2c873b091` 与域名 `cdn007-digitaldownloads[.]com`；终端安装路径上的序号标签 `Exploited<N>` 也暗示此前已有更早受害者。建议所有使用 ScreenConnect 的企业与服务商立即按以下清单排查处置：

* 🌐 **网络与终端 IOC**：封锁并回溯 `185.99.255[.]28`、`155.94.150[.]39`（`sc[.]payproofkit[.]com`）、`newnewnew[.]gotdns[.]org`、`soxnewwork[.]homedns[.]org`、`ns[.]mo7sen[.]dev/EadF.php` 及 `cdn007-digitaldownloads[.]com`；排查客户端安装包参数 `c=Exploited<N>`、参与者名称 `Addmin`、实例 ID `d905b2b1b165d0a9`/`4b8f4089ddaac6a9`/`df1f7ef0cfacd0d8`，以及注册表自启项 `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\RelayTrapLiteAlert`。
* ❌ **严禁使用 ScreenConnect 排查染毒主机**：切勿直接通过 ScreenConnect 会话连接疑似失陷机器，以免反向触发 `Run-Lateral-Full.bat`；请改用 EDR 实时响应或 WinRM，若技术员此前已连入过，该工作站须视同失陷立即隔离。
* ✅ **本地版手动停用扩展与清驻留**：自建（On-Premises）用户须手动停用 `RMM+` 等 5 款扩展或强制配置高强度 `RMMPlus.AccessKey` 与 API 口令。染毒主机须先彻底删掉第二个客户端服务、`TrapWatch` 任务、`C:\ProgramData\RelayTrap\` 及 AppLocker 规则再解封，否则主机解封后会迅速复发；同时在干净终端强制注销所有 ScreenConnect Web 与 IdP 会话。

***END***

阅读推荐

[【安全圈】微软11月修1259洞！Outlook零日盗取NTLMv2](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079834&idx=1&sn=87414c25c31b4e94e839597e00255ff4&scene=21#wechat_redirect)

[【安全圈】Railway遭AI代理穿透！10万工作区泄密烧掉74万美元](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079834&idx=2&sn=f9a3ec5c78818d7d7509c38d4e00528b&scene=21#wechat_redirect)

[【安全圈】iOS零日沙盒逃逸曝光！iOS27.2.1仍可跨应用窃密](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079834&idx=3&sn=9f5233b9da2385dbe4ce4527012d3c10&scene=21#wechat_redirect)

[【安全圈】云商被黑连累FireworksAI！模型权重与密钥遭窃](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079821&idx=1&sn=4deb7108dc0f96ae2b0f2c738718402e&scene=21#wechat_redirect)

[【安全圈】SSHole与GPUStack遭在野利用！CISA急列四漏洞](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652079821&idx=2&sn=38d64841709704b9cc08a0e06921010e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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