---
title: CNCERT：关于内置后门功能的恶意软件“荐片播放器”大规模传播的风险提示
url: https://mp.weixin.qq.com/s/Xa--ObpWrAxi5nNq2uO1dQ
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:59:27.860060
---

# CNCERT：关于内置后门功能的恶意软件“荐片播放器”大规模传播的风险提示

# CNCERT：关于内置后门功能的恶意软件“荐片播放器”大规模传播的风险提示

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

编者荐语：

境内已监测到超70万台设备感染。

以下文章来源于国家互联网应急中心CNCERT
，作者CNCERT

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM7x2UYGIAGwcwufoYr2R16synysQjwIEVJzwyjBcVT8Cg/0)

**国家互联网应急中心CNCERT**
.

国家计算机网络应急技术处理协调中心（简称“国家互联网应急中心”，英文简称CNCERT或CNCERT/CC），成立于2001年8月，为非政府非盈利的网络安全技术中心，是中国计算机网络应急处理体系中的牵头单位。

近期，国家互联网应急中心（CNCERT）监测发现，“荐片播放器”Windows端应用程序内置后门功能，可在用户不知情的情况下采集终端信息、下载运行其他程序，并接收服务端指令执行任意代码，存在终端被远程控制、个人信息泄露等安全风险。目前，境内已监测到超70万台设备感染。为帮助广大用户和有关单位识别风险、开展排查，现将该软件的主要恶意行为、感染情况及防范建议提示如下。

一、概述

本次分析对象为“荐片影视”所谓官方地址（www.jianpian.com，非国内合法备案网站）提供下载的“荐片播放器”Windows端应用程序。经分析，该程序在提供影视播放功能的同时，通过注册表自启动项和系统服务保持后台运行，具备静默安装第三方软件、采集终端指纹与行为数据、篡改剪贴板内容等功能。其内置的两条独立通信通道可定期接收并执行服务端下发的脚本，结合进程注入、内核驱动加载和内存执行能力，使服务端能够持续向终端投递和运行其他程序。

对不同版本的比对发现，该软件虽调整了通信域名、接口和加密方式，但脚本下发执行、终端信息采集、进程注入等主要恶意行为仍然存在。2026年9月15日至22日，CNCERT累计监测到境内700,260台设备感染，日上线受控终端数量最高达251,880台。

二、恶意样本分析

经对程序及其组件开展逆向分析，发现其通过启动器、核心业务库、脚本执行模块和更新服务协同实现配置获取、信息采集、载荷下载执行及持续驻留等功能。各模块的位数与主要作用见表1，具体恶意行为分析如下。

表 1 恶意软件部分模块清单与角色

|  |  |  |
| --- | --- | --- |
| **模块** | **位数** | **角色** |
| jianpian.exe | 32 | 启动器：解开加密的函数名，加载核心库并转发命令行 |
| jianpianer.dll | 32 | 核心业务库：配置拉取、静默下载执行、指纹、剪贴板劫持、广告弹窗、内嵌浏览器接口 |
| jianpianhelp.dll | 64 | 脚本下发执行模块（方式一）：唯一没有数字签名的程序，文件时间戳为全 F 填充的无效值 |
| Jp\_Update.exe | 64 | 脚本下发执行模块（方式二）：Windows服务、定时汇报、BlackBone注入与内存执行程序 |
| FileSuite.exe | 32 | 媒体文件关联改写专职工具（需要管理员权限） |

（一）隐藏驻留与持久化

安装时核心业务库jianpianer.dll将自身写入注册表自启动项HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\Run\JIANPIAN，键值附加--windowstate=hide source=autorun参数，用户登录后隐藏窗口自启、无任何界面；同时管理StartupApproved\Run项，使任务管理器中的“禁用”操作失效。Jp\_Update.exe被安装为开机自启动的系统服务Jp\_Update；服务启动后获取当前登录用户令牌，以该用户身份在用户桌面重新启动自身，获得桌面全部操作能力。

（二）无感知强制安装第三方软件

核心业务库jianpianer.dll定时请求配置接口https://pconfig.<域名>/svr\_optns/config.php（主用jianpiancloud.com，备用jphwapi.com），解析返回的21个控制字段；按配置中地址将第三方安装程序下载至%TEMP%临时文件夹（随机文件名），再以管理员权限（runas）、完全隐藏窗口（nShow=0）运行，结束后自动退出，全程无感知。下载何种软件、从何地址下载均由服务器决定。关键代码见图1。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRiaib4sibzGGS9zmicEsOQX6UVbMbnicXvzxSha4icHtq2OjFicGhqfUsiaDKKOfbUTVIibWU8kTgiaa6WicSyiaZbLfmkvFxgVO9Ux79COQt8/640?wx_fmt=png&from=appmsg)

图 1 以管理员权限、隐藏窗口运行下载的安装程序

（三）批量采集终端指纹与行为数据

核心业务库jianpianer.dll读取C盘卷序列号与第一块物理以太网卡MAC地址（跳过名称含“virtual”的虚拟网卡），以“-”拼接生成设备唯一指纹，持久化写入注册表HKEY\_LOCAL\_MACHINE\SOFTWARE\JianPianPlayer\PCCode，并随pconfig服务器统计接口（/svr\_optns/logstat/stat）上报，服务器可据此逐台识别终端。同时会在本地存储目录wkeStorage中留存渠道归因数据，记录推广活动编号、安装渠道、来源域名与安装时间，完成用户来源链路记录。

（四）双通道脚本下发与任意代码执行

jianpianhelp.dll每30分钟向http://jptongji.jianpiancloud.com:8002/ssl.asp?ver=1.2.3.30发送POST请求（通道一）；Jp\_Update服务每20分钟向http://jptongji.<域名>:8002/ssl.asp?ver=4.0.1发送POST请求（通道二，默认域名jianpiantongji.x-app.one）。服务器返回的内容开头两个字符为“00”时，即被内置脚本引擎（MSScriptControl，JavaScript）作为代码直接执行，服务器由此可随时向在线终端下发任意代码。“00”开关判断见图2。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRiaVBFqWXT1rnEibL4o2b2em9sdxsOhbiaw6H3GT19lVuVZxKfEtKAAbCPeaLQlPibT2f0UheRibb7cMtr3wvBQ8kqT7zjuic3pjp1JY/640?wx_fmt=png&from=appmsg)

图 2 返回内容以“00”开头即交由脚本引擎执行

Jp\_Update侧的脚本引擎注册了callapi、HashCls等内置功能（见表2），赋予服务端下发脚本超出普通网页脚本的系统操作权限，可实现部分高风险行为：调用任意DLL函数、创建任意COM对象、下载并运行任意文件文件、向指定内存地址写入数据等。

表 2 脚本可调用的部分内置功能

|  |  |
| --- | --- |
| **功能名** | **作用** |
| callapi | 调用任意DLL文件中的任意函数 |
| HashCls | 下载任意文件并执行 |
| CreateActiveXObject | 创建任意COM组件对象 |
| SetLongToPtr/ SetIntToPtr / SetStringToPtr | 向指定内存地址写入数据 |
| alert | 弹窗与信息回显 |

下发内容按文件头分流执行：标准PE文件在内存中映射执行，自定义“CODE”头的数据块复制到可读可写可执行内存后直接调用——任意程序均可在不落盘的情况下运行。该模块还内嵌BlackBone注入框架，可向32/64位进程注入代码并加载BlackBoneDrv7-10.sys内核驱动（驱动文件运行时从服务器下载）。关键代码见图3。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhWVZHFRcHNleMuNkR3PFJyKbhibXw8hKnoK2SBLzO8cMmmQqASoVx5hvBTC5twoBCXubMQsJZbEwicww7w8Pkp9OicibeKawe3sk8/640?wx_fmt=png&from=appmsg)

图 3 任意PE文件不落盘内存执行

（五）流量劫持与导流

核心业务库jianpianer.dll后台监听剪贴板，将用户复制的以HTTP://或FTP://开头的链接静默替换为服务器下发的推广链接，替换结果m3u8视频源时自动拉起播放。FileSuite.exe以管理员权限将36种媒体格式的默认打开方式批量改写为自家播放器，包括覆盖用户已选定的UserChoice项。广告弹窗地址、内容与弹出节奏由config.php配置字段控制，广告页经内嵌浏览器开放的本机接口可获得写文件、创建组件、触发下载、读取本机指纹等执行能力。

（六）通信隐藏与自恢复

Jp\_Update.exe每轮回连时将回传域名动态解析为IP并在请求中以IP直连，服务器可经注册表HKEY\_CURRENT\_USER\SOFTWARE\JIANPIAN下的main\_domain（通道二对应“main domain”）值远程更换回传域名；jianpianer.dll解析其配置、广告、统计类域名时，核心库对配置与广告类域名经DoH加密解析；jianpianhelp.dll内置修复逻辑，模块文件被删除后，可经http://web.<域名>:8000/mini/repair.asp从服务器重新下载安装。

（七）恶意程序更新变化

经对比分析，“荐片影视”所谓官方网站（www.jianpian.com）当前下载的最新版本“荐片播放器”Windows应用程序已升级，相关改动为：回传地址均加密为HTTPS，脚本下发通道由http://jptongji.<域名>:8002/ssl.asp变更为https://jptongji.<域名>/ssl.php；控制服务由jianpiancloud.com、x-app.one等域名整体迁移至jpcloud.org域名族；网络通信改用自带libcurl库并新增加密流量隧道。隐藏自启、静默安装、指纹采集、剪贴板劫持、脚本下发执行与进程注入等主要恶意行为保持不变。

三、感染规模

通过监测分析，发现境内于2026年9月15日至9月22日期间，该恶意软件感染的日上线受控终端数量最高达251,880‌台，累计监测到700,260台设备被感染，境内每日感染终端数量情况如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRgwicNmOko2YZrbe7ApWuwn0noo2Krj7yoRQvtbFpVQIJTV8g5BHa0YPfoaOfBvRvGCDhiclODKchUATLqdSNBiaIs0TeNKQFy3SE/640?wx_fmt=png&from=appmsg)

图 4 境内日上线受控终端数量

四、防范建议

（一）规范软件获取渠道，防范捆绑安装

不从非正规渠道下载安装捆绑推广的影视播放器类软件；下载软件时核对数字签名主体，警惕以个人证书签名的安装程序；留意安装过程中默认勾选的捆绑选项。

（二）全面排查感染终端，及时清除恶意程序

按IOC排查注册表Run键JIANPIAN、SOFTWARE\JIANPIAN键、服务Jp\_Update与BlackBone、安装目录及%APPDATA%\jianpianhelp\下的可疑模块、%TEMP%目录中的随机名可执行文件。确认感染终端应视为受控主机，隔离排查后建议重装系统。

（三）封堵恶意域名与IP，阻断回传通信

在边界安全设备上封禁相关IOC；重点监测对jptongji.jianpiancloud.com:8002/ssl.asp等8002端口、ssl.asp地址的周期性POST请求（30/20分钟两个周期）。

（四）强化终端防护与权限管控

开启终端防护软件实时防护并保持病毒库更新；遵循最小权限原则，不使用管理员账户日常办公，限制未知程序以管理员权限运行；及时安装系统与常用软件安全补丁。

（五）加强日常安全监测与审计

定期巡检终端自启动项、系统服务、进程与网络连接，关注剪贴板内容被替换、文件关联被篡改等异常现象；留存终端与边界网络日志，为影响范围认定和溯源处置提供依据。

五、相关IoC

（一）样本SHA256

2C976B8D99E5BBBB2D1E073D10FF311D3190A8E1D1A772A7E60ABB2C3D25AB69

11BF146FA88FC20835B44371915C581202431799094DDC59F35D0D5BAC94ACCE

D51889A1B794FD5E00111745B63D731999E42ED9B8F530C69CDC371FD3EAFE2D

DDF4EF9AD9F93D4F345F9B923B5DC91712D77FFC68592510CA7BFCF88E24996D

2E0EF1472F8DC0431D8A4619E49EE240A1A02BBD28455668D5710CA427E8EEB9

7222D26BEE974BE94033CC29C2025881F84B3F9B23F99B45848E61FD2A77EDCA

953D6871D3033BF21A5829B4B0F6A9E0F5F1978159E39DB25931C7873CD658BF

672A497B219AC5979C159CE0FDA33B4147ADDD0FE8EE3ED2F17080E6828C3E58

21DD44ABBADF3CFE5327410C034758DFEDB9EF387A2826714B94AC5954E5DCB9

（二）IP

45.117.8[.]37

45.120.103[.]111

34.150.19[.]222

（三）DOMAIN

jptongji.jianpiancloud[.]com

jianpiantongji.x-app[.]one

pconfig.jianpiancloud[.]com

media.jianpiancloud[.]com

web.jianpiancloud[.]com

jphwapi[.]com

pchwjiasu.abkc4[.]com

pchwjiasu.arykoyq[.]com

jptongji.jpcloud[.]org

pconfig.jpcloud[.]org

media.jpcloud[.]org

web.jpcloud[.]org

www.jpcloud[.]org

（四）URL

http[:]//jptongji.jianpiancloud.com:8002/ssl.asp?ver=1.2.3.30

http[:]//jptongji.jianpiantongji.x-app.one:8002/ssl.asp?ver=4.0.1

https[:]//jptongji.jpcloud.org/ssl.php?src=svc&ver=5.0.0.1

https[:]//jptongji.jpcloud.org/ssl.php?src=dll&ver=5.0.0.1

https[:]//jptongji.jpcloud.org/api/v1/client-event

https[:]//pconfig.jianpiancloud.com:8000/svr\_optns/config.php

https[:]//pconfig.jpcloud.org/svr\_optns/config.php

http[:]//pconfig.jianpiancloud.com:8000/svr\_optns/logstat/stat

http[:]//media.jianpiancloud.com:8000/index.php?s=Home-Api-jscode-key-m3u8

http[:]//web.jianpiancloud.com:8000/mini/repair.asp?state=repair

https[:]//web.jpcloud.org/mini/repair.php?state=repair

https[:]//pconfig.jpcloud.org/download/jianpian\_setup.exe

六、致谢

感谢启明星辰VenusEye威胁情报中心和中孚安全元亨实验室在本报告的样本分析工作中做出的重要贡献。

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：国家互联网应急中心CNCERT

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

---

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8Ai...