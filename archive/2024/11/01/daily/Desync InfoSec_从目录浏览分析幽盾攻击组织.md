---
title: 从目录浏览分析幽盾攻击组织
url: https://mp.weixin.qq.com/s?__biz=MzkzMDE3ODc1Mw==&mid=2247488781&idx=1&sn=b59b3f422a2f5834b5c9a1ce56baebbd&chksm=c27f66a3f508efb59bb3384efd172d3320ae3e2d68813dc27d1fd6fdcb9b50cd6b6de3065458&scene=58&subscene=0#rd
source: Desync InfoSec
date: 2024-11-01
fetch_date: 2025-10-06T19:19:55.306985
---

# 从目录浏览分析幽盾攻击组织

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUAT3SVvXx2zNcObX2r41dVoALfJsibzVDfpwhm3QK4H6mYfETeDBsTzQ/0?wx_fmt=jpeg)

# 从目录浏览分析幽盾攻击组织

safest\_place

Desync InfoSec

## 关键要点

* • 根据目录浏览漏洞分析了一个中国攻击团伙。
* • 攻击者使用 WebLogicScan、Vulmap 和 Xray 进行了广泛的扫描和漏洞利用，攻击目标包括韩国、中国、泰国、台湾和伊朗的组织。
* • 攻击组织习惯使用Viper C2 框架以及包括 TaoWu 和 Ladon 扩展的 Cobalt Strike 工具包。
* • Leaked LockBit 3 构建器用于创建带有自定义勒索信的 LockBit 有效负载，其中包括对我们在报告中进一步调查的 Telegram 群组的引用。

## 摘要

DFIR 报告的威胁情报团队在 2024 年 1 月测绘到一个存在目录浏览漏洞的互联网资产，并对其进行了攻击团伙技战术分析。经过审查，我们发现它与自称“幽盾”的中文黑客组织有关。

攻击者使用这台服务器进行了各种攻击活动，包括信息收集，使用 WebLogicScan、Vulmap 和 Xray 等工具进行Web 漏洞利用活动。，他们已经扫描出大量存在漏洞的互联网资产。他们获取了一些运行致远OA的web网站权限，使用 SQLmap 进行 SQL 注入攻击。

我们发现了一些攻击者渗透成功的痕迹，比如说，在获得访问权限后，攻击者使用更多工具尝试利用各种漏洞来提升失陷主机上的权限，包括使用 traitor 进行 Linux 权限提升漏洞，以及使用 CDK 进行 docker 和 kubernetes 权限提升。

在目录浏览的服务器上我们发现了Cobalt Strike 和 Viper 框架相关的文件。Cobalt Strike 工具的压缩包中包含团队服务器程序和插件 TaoWu ， Ladon，它们极大地扩展了框架的功能。DFIR 报告威胁情报团队在 2024 年 1 月 18 日至 2 月 10 日期间跟踪该C2服务器。从这台服务器上的数据分析，我们确定了一个由八个 IP 地址组成的集群，这些地址都用于代理同一攻击者的C2服务器，并在同一时间范围内处于活动状态。

攻击者还利用泄露的 LockBit 3 勒索软件构建器来创建自定义二进制LB3.exe。LockBit 二进制文件生成的勒索信以“EVA”管理的 Telegram 组“You\_Dun”的形式提供了联系方式。负责的小组也使用“Dark Cloud Shield Technical Team”这个名字。这个团伙似乎根据他们的渠道参与了销售“渗透测试”，但也从事非法数据销售，DDOS，并且基于 LockBit 二进制文件，还使用勒索软件来赚取收入。

# 入侵攻击链分析

## 边界突破

#### Sqlmap

攻击者使用 sqlmap 攻击了各种网站：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUWwEphwb0ty3hL2KmAC9EYooqJgrEQkvQus05P1F3jbdL3k3qWeTGKQ/640?wx_fmt=png&from=appmsg "null")

以下是攻击者从韩国的一家制药组织脱库时使用的一些命令：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUChgpLX1MeicXsWOGfPmKlmqx2lhpVWBFojOqD4Fw1gu4lUdMf8XaEcQ/640?wx_fmt=png&from=appmsg "null")

#### Seeyon\_exp

seeyon\_exp脚本通过利用致远 OA 软件中的一个组件，可批量上传jspx webshell

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUQja3YhukohMXhQuwSFE2PQiaGQVibgwe3JVrPwmicezzRZgqopwaSiaXMA/640?wx_fmt=png&from=appmsg "null")

从工具运行的输出结果中我们可以得到存在漏洞且攻击成功的站点列表

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUQic45VLxVqxiaRYJkPWwYtXePmblg79NXPPfmicG6ffCfLd8OAnRpAGWg/640?wx_fmt=png&from=appmsg "null")

Translated we can see the confirmation of what was successful with each target.

译者注：终于有老外看不懂需要翻译的内容了，这段就不用翻译了吧

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWURqSTXicU4aENGPsRTRXPDMlBmvMibLQ7YpkmLWZic3b937FGJiaPF9S15Q/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUeTMxic0TkzT01TkOFicozZoDibAYgrub0HHAxBDziaEWUuAmuuN6u7VAxw/640?wx_fmt=png&from=appmsg "null")

#### 泛微

Another tool weaver was also used to scan for vulnerabilities and exploit Zhiyuan OA instances.

译者注：老外还把致远OA和泛微OA整混了。乐

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWU0vPIrnI92Gno0oVBcBRD5hiaWkmpRJTuv2049qo4ssbN280O4g3f5Xw/640?wx_fmt=png&from=appmsg "null")

## 远程控制

### Cobalt Strike (S0154)

从bash 历史记录中可以看到 nohup 命令，用于使用以下密码和帐户详细信息运行 Cobalt Strike 服务器：

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUfQkwzF26epo7TsichduaoSgZl0ib4OM9X5qsHuuu6tAy8vIVVOGER49Q/640?wx_fmt=png&from=appmsg "null")

从116.212.120.32 这个 IP 地址提取了以下信标配置，最明显的是 987654321 的破解水印：

```
Cobalt Strike Beacon:
  x86:
    beacon_type: HTTP
    dns-beacon.strategy_fail_seconds: -1
    dns-beacon.strategy_fail_x: -1
    dns-beacon.strategy_rotate_seconds: -1
    http-get.client:
      Cookie
    http-get.uri: 116.212.120.32,/IE9CompatViewList.xml
    http-get.verb: GET
    http-post.client:
      Content-Type: application/octet-stream
      id
    http-post.uri: /submit.php
    http-post.verb: POST
    maxgetsize: 1048576
    port: 80
    post-ex.spawnto_x64: %windir%\sysnative\rundll32.exe
    post-ex.spawnto_x86: %windir%\syswow64\rundll32.exe
    process-inject.execute:
      CreateThread
      SetThreadContext
      CreateRemoteThread
      RtlCreateUserThread
    process-inject.startrwx: 64
    process-inject.stub: e43a1b63f09794f74d90a9889f7acb77
    process-inject.userwx: 64
    proxy.behavior: 2 (Use IE settings)
    server.publickey_md5: a490a5e2db1fcc496e6b793a8ea02a19
    sleeptime: 60000
    useragent_header: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; BOIE9;ENUS)
    uses_cookies: 1
    watermark: 987654321
  x64:
    beacon_type: HTTP
    dns-beacon.strategy_fail_seconds: -1
    dns-beacon.strategy_fail_x: -1
    dns-beacon.strategy_rotate_seconds: -1
    http-get.client:
      Cookie
    http-get.uri: 116.212.120.32,/visit.js
    http-get.verb: GET
    http-post.client:
      Content-Type: application/octet-stream
      id
    http-post.uri: /submit.php
    http-post.verb: POST
    maxgetsize: 1048576
    port: 80
    post-ex.spawnto_x64: %windir%\sysnative\rundll32.exe
    post-ex.spawnto_x86: %windir%\syswow64\rundll32.exe
    process-inject.execute:
      CreateThread
      SetThreadContext
      CreateRemoteThread
      RtlCreateUserThread
    process-inject.startrwx: 64
    process-inject.stub: e43a1b63f09794f74d90a9889f7acb77
    process-inject.userwx: 64
    proxy.behavior: 2 (Use IE settings)
    server.publickey_md5: a490a5e2db1fcc496e6b793a8ea02a19
    sleeptime: 60000
    useragent_header: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)
    uses_cookies: 1
    watermark: 987654321
```

在web根目录下有个红队版.zip文件

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUGicab1owtH7Kx34Pg72Emha4J1qWLpq6v57iatQZynQJuzcAt1GQ82Lw/640?wx_fmt=png&from=appmsg "null")

压缩包中的CS与上文提到的CS一致。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWUJSkIaZ3OPZSJtsLfKA8Y5GlOdwT2alO8pEv9zRTuMcZQ9SLpySDicdw/640?wx_fmt=png&from=appmsg "null")

aggressor 脚本 CrossC2-GithubBot-2023-03-27.cna 来自此存储库。

作为此 Cobalt Strike 套件一部分的其他主要模块是 TaoWu 和 Landon，它们扩展了 Cobalt Strike 的功能。

### 梼杌

TaoWu aggressor 脚本包括添加到 Cobalt Strike 操作的工具和脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkdkuRdrTVaZUZ3GMrSPbfWU2ibXP9WfeHkVHbXKg7FRjicL9XDjOXogg1dHjoWXEhSt2QD1FNtub5jA/640?wx_fmt=png&from=appmsg "null")

它在路径 taowu-cobalt-strike-master\script 中包含了大量预编译的二进制文件：

```
./0803.exe
./360bowser.exe
./add-admin.exe
./ATPMiniDump.exe
./blocketw.exe
./blue.exe
./BrowserGhost.exe
./BypassAddUser.exe
./certexp.exe
./chfs.exe
./ClearnEventRecordID.ps1
./ClearnIpAddress.ps1
./ClearnTempLog.ps1
./crack.exe
./CredPhisher.exe
./cve-2014-4113.x64.dll
./cve-2014-4113.x86.dll
./cve-2015-1701.x64.dll
./cve-2015-1701.x86.dll
./cve-2016-0051.x86.dll
./CVE-2020-0796.x64.dll
./CVE-2021-1675.x64.dll
./dazzleUP_Reflective_DLL.x64.dll
./DecryptAutoLogon.exe
./DecryptTeamViewer.exe
./dis_defender.exe
./EfsPotato.exe
./encode
./encode.exe
./EncryptedZIP.exe
./FakeLogonScreen.exe
./FullPowers.dll
./Gopher.exe
./GPSCoordinates.exe
./hack-browser-data.exe
./InternalMonologue.exe
./Invoke-EternalBlue.ps1
./Invoke-MS16032.ps1
./Invoke-MS16135.ps1
./iox.exe
./JuicyPotato.x64.dll
./JuicyPotato.x86.dll
./KillEvenlogService.ps1
./Ladon.exe
./Ladon1.exe
./lazagne.exe
./ListAllUsers.ps1
./ListLogged-inUsers.ps1
./ListRDPConnections.exe
./LocalSessionManager.ps1
./LPE_Reflect_Elevate.x64.dll
./MaceTrap.exe
./MiniDump.exe
./napwd.exe
./navicatpwd.exe
./Net-GPPPassword.exe
./NoAmci.exe
./noNetApiAdd.exe
./NoPowerShell.exe
./RdpThief_x64.tmp
./Recon-AD-AllLocalGroups.dll
./Recon-AD-Computers.dll
./Recon-AD-Domain.dll
./Recon-AD-Groups.dll
./Recon-AD-LocalGroups.dll
./Recon-AD-SPNs.dll
./Recon-AD-Users.dll
./ReflectiveDll.x64.dll
./RegRdpPort.ps1
./rpcscan.dll
./SafetyKatz.exe
./scout.exe
./scrying.exe
./Seatbelt.exe
./SessionGopher.ps1
./SessionSearcher.exe
./Sharp3389.exe
./SharpAVKB.exe
./SharpBypassUAC.exe
./SharpChassisType.exe
./SharpCheckInfo.exe
./SharpChromium.exe
./SharpClipHistory.exe
./SharpCloud.exe
./SharpCrashEventLog.exe
./SharpDecryptPwd.exe
./SharpDecryptPwd2.exe
./SharpDir.exe
./SharpDirLister.exe
./SharpDomainSpray.exe
./SharpDoor.exe
./SharpDPAPI.exe
./SharpDump.exe
./SharpEDRChecker.exe
./SharPersist.exe
./SharpEventLog.exe
./SharpExcelibur.exe
./SharpExec.exe
./SharpGetTitle.exe
./SharpGPOAbuse.exe
./Sha...