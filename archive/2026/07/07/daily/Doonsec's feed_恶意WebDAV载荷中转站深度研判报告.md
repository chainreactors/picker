---
title: 恶意WebDAV载荷中转站深度研判报告
url: https://mp.weixin.qq.com/s/4DRVILN0vVTA9iKS0KeiwA
source: Doonsec's feed
date: 2026-07-07
fetch_date: 2026-07-08T05:03:05.066175
---

# 恶意WebDAV载荷中转站深度研判报告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0SJCMgmXPLRxRyl9tg9snfccGj61NeCEazct8S9uxHXn9PP2o1YgTCu1n6hrnZlypW62A3ialAI7ntuibCWeflibf9Ve6A3OVmpfRpicnXxgZlU/0?wx_fmt=jpeg)

# 恶意WebDAV载荷中转站深度研判报告

原创

CyberOk
CyberOk

CyberOk

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

经对目标URL（http://46.101.XXX.XXX:8080/）的在线探测、目录枚举、关键样本下载与静态分析，并结合既有《匿名WebDAV载荷服务器关联Windows窃密远控工具全链路研判分析》交叉验证，确认该节点为一套持续运维中的Windows黑产窃密/远控工具链专属载荷分发基础设施。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/0SJCMgmXPLQ8QHk9qIbwicrenS1JAsGLPiaiafxWnsywgkzmHhV4KzurbOmAcVgx9D867LXM45fjL7xwb5rG6kAZbibyGwaDup22dgmxmnicZOUQ/640?wx_fmt=jpeg&from=appmsg)

一、执行摘要

该服务器运行于DigitalOcean法兰克福机房（AS14061），对外暴露WsgiDAV/4.3.4匿名读写WebDAV服务（TCP/8080），同时通过DuckDNS动态域名gogettate.duckdns.org解析至同一IP，在HTTPS/443由nginx提供面向受害终端的载荷下发通道。站点内可见完整攻击组件源码、迭代备份、钓鱼诱饵、便携Python环境及DLL劫持模块，具备明显的专业化黑产运维特征。

·威胁等级：极高（活跃C2/载荷节点，匿名可写，工具链完整且持续迭代）

·主要危害：剪贴板加密货币地址劫持、浏览器凭据窃取、多重持久化、Defender排除与Office宏绕过

·攻击入口：伪装Q1财报的钓鱼HTML/ZIP/DOCM/LNK/HTA多载体投递

·关联域名：gogettate.duckdns.org→46.101.XXX.XXX

·样本时间线：2026-06-23至2026-07-07持续更新

# 二、目标基础设施画像

## 2.1 网络与托管信息

|  |  |
| --- | --- |
| 属性 | 实测值 |
| 目标URL | http://46.101.XXX.XXX:8080/ |
| IP地址 | 46.101.XXX.XXX |
| 托管商 | DigitalOcean,LLC(AS14061) |
| 地理位置 | 德国法兰克福(Frankfurt am Main, Hesse) |
| Web服务(8080) | WsgiDAV/4.3.4Cheroot/11.1.2 Python/3.12.3 |
| HTTPS服务(443) | nginx/1.24.0(Ubuntu)，路径/data/提供载荷 |
| 动态域名 | gogettate.duckdns.org→46.101.XXX.XXX |
| WebDAV认证 | anonymous，权限read-write（匿名可读写） |
| 探测时间 | 2026-07-0710:42 UTC+8 |

## 2.2 双通道架构

实测发现攻击基础设施采用「开发/运维面+投递面」双通道设计：8080端口运行WsgiDAV目录浏览服务，完整暴露/payload/目录下70+文件及大量bak\_\*迭代备份，便于攻击者直接上传、调试、版本管理；443端口由nginx反向代理，仅允许按文件名下载（目录列表返回403），面向受害者终端通过curl/BitsTransfer静默拉取，降低暴露面。

部分早期加载器（如loader.vbs）仍硬编码http://46.101.XXX.XXX:8080直连地址（字符串拆分规避检测），而新版脚本（run.bat、s0.bat、svc32.py、payload.hta等）已统一迁移至https://gogettate.duckdns.org/data/，说明攻击者正在进行域名化与HTTPS加固，但WebDAV调试端口仍未关闭。

## 2.3 根目录与关键子目录

|  |  |  |
| --- | --- | --- |
| 路径 | 内容概要 | 最近修改 |
| / | payload/、pdfdownloader/、Q1\_Report.pdf.lnk、VERSION.dll/c、ThemeUI.dll/c | 2026-07-07仍在线 |
| /payload/ | 完整工具链：加载器、木马、窃密模块、诱饵、py.zip、备份版本 | 71个列表项 |
| /pdfdownloader/ | 钓鱼用Q1\_Report.pdf.lnk | 2026-06-29 |

 三、载荷目录详细清单

以下为核心恶意组件分类（含实测文件大小与最后修改时间，来源于在线目录枚举）：

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 类别 | 文件名 | 大小 | 修改时间 | 功能 |
| 一级加载器 | svc32.py | 3,266B | 2026-06-29 | 反调试/反VM、持久化、拉取d32.py |
| 二级核心木马 | d32.py | 198,835B | 2026-07-06 | marshal+base64混淆，AMSI/ETWpatch，主功能体 |
| 主控批处理 | s0.bat | 11,496B | 2026-07-05 | Defender排除、Office宏绕过、COM/DLL侧载 |
| 环境适配 | run.bat | 1,300B | 2026-06-28 | 四层Python环境探测+下载svc32.py |
| 看门狗 | ThemeSvc.bat/ThemeMaint.bat | 2.8K/5.2K | 2026-07-06 | 进程守护、远程更新、计划任务 |
| PowerShell | acset.ps1/update.ps1 | 16.5K/3.6K | 2026-07-04 | Defender排除、WMI持久化、静默更新 |
| 多形态入口 | loader.vbs/payload.hta | 2.6K/612B | 2026-06~07 | BitsTransfer/HTA隐蔽下载执行 |
| DLL劫持 | VERSION.dll/ThemeUI.dll | 17.9K/15.4K | 2026-07-04 | version.dll代理+COM劫持 |
| 便携Python | py.zip/pyembed.zip | 15.3M/11.1M | 2026-06-25 | 无Python环境终端自动部署 |
| 剪贴板劫持 | dbwclip.py/cliptest.py | 2.7K/1.7K | 2026-06-24 | XRP等地址替换测试模块 |
| 浏览器窃密 | ccu.py | 15,899B | 2026-06-26 | Chrome凭据DPAPI解密+外泄 |
| 加密货币测试 | allcoins.py | 2,751B | 2026-06-24 | BTC/ETH/TRX/XRP等劫持自测 |
| 远程更新 | up.bat | 810B | 2026-07-06 | 从C2拉取最新d32.py并重启pythonw |
| 钓鱼诱饵 | Q1\_Report.pdf.html/.zip | 6K/5.4K | 2026-07-05 | 伪装Adobe财报下载页（土耳其语） |
| Office诱饵 | Q1QuarterlyReport 2025.docm | 2,839B | 2026-07-06 | 带宏钓鱼文档 |

目录内还存在大量bak\_sig、bak\_digest、bak\_prefaze\*、bak\_wmifix等备份文件，覆盖签名修复、摘要校验、虚拟机规避、TCP通信、WMI修复等专项迭代，证明工具链处于高频开发维护状态。

# 四、攻击链路还原

## 4.1 投递阶段

攻击者以「Q1 2025财务季报」为主题进行社会工程钓鱼。诱饵包括：根目录Q1\_Report.pdf.lnk快捷方式、pdfdownloader/目录副本、payload/Q1\_Report.pdf.html（伪装AdobeAcrobat土耳其语安全下载页，自动跳转下载ZIP）、Q1\_Report.pdf.zip（密码Q1-2025）、Q1Quarterly Report 2025.docm（宏文档）。HTML页面在DOMContentLoaded后300ms自动触发下载https://gogettate.duckdns.org/data/Q1\_Report.pdf.zip。

## 4.2 落地与加载

典型加载链（以run.bat→svc32.py→d32.py为例）：

·run.bat使用curl-sk忽略证书校验，从C2下载svc32.py至%TEMP%

·按优先级探测Python：%APPDATA%\...\Themes\Cache\PythonHelper、系统Python 3.9–3.14、%TEMP%\pyemb，若无则下载py.zip解压

·以start/Bpythonw无窗口后台执行svc32.py

·svc32.py检测调试器（IsDebuggerPresent）与VM注册表（VBoxGuest/VMware/vmhgfs），命中则休眠300–600秒后退出

·部署持久化：Startup\AcrobatUpdSvc.py、HKCU Run\AcrobatUpdSvc、计划任务AcrobatUpdateService

·从https://gogettate.duckdns.org:443/data/d32.py下载二级木马，TEMP路径自删除后exec执行

## 4.3 深度驻留与对抗（s0.bat/acset.ps1）

·修改Office Word/Excel ProtectedView与VBAWarnings注册表，禁用受保护视图与宏警告

·通过wsreset UAC bypass+fodhelper注册表劫持添加Defender排除路径（Themes\Cache、TEMP、pythonw.exe）

·伪装目录：%APPDATA%\Microsoft\Windows\Themes\Cache\ThemeService.py

·计划任务ThemeSvcCheck（每2分钟）、ThemeSvcMaint（每22小时）通过隐藏wscript执行

·COM劫持：注册ThemeUI.dll至ShellIconOverlayIdentifiers/ThemeSvcHelper

·DLL侧载：将VERSION.dll复制至OneDrive/Teams/Zoom等目录实现劫持

·WMIEvent Subscription持久化（ThemeEvtFlt/ThemeEvtCns）

·d32.py头部inlinepatch AMSI（AmsiScanBuffer）与ETW（EtwEventWrite）

## 4.4 窃密与牟利模块

ccu.py（Chrome Credential Utility）通过DPAPI+PowerShell解密Chrome Login Data SQLite数据库中的密码，并将窃取数据POST至C2中继https://gogettate.duckdns.org:443/api/ccu/report，同时硬编码Gmail外泄账号（XOR混淆已解密）。

dbwclip.py实现剪贴板监控线程，当检测到XRP地址格式时替换为攻击者钱包rH1d7gnvLHMfLAL9GBY9sbdsvLNS5EdKur；allcoins.py对BTC/ETH/TRX/XRP/LTC/DOGE/SOL/ADA等币种进行劫持功能自测。

# 五、关键样本静态分析

|  |  |  |
| --- | --- | --- |
| 样本 | 大小 | SHA256 |
| Q1\_Report.pdf.lnk | 2862 | b6eb8f4a09575f9b864364d73a90c5a4eb6f5c103e404b102d9b81a62bb4a64d |
| ThemeUI.dll | 15360 | abcc600b4e8fb2d1ae4d6fa76b523c8a39cc8c296691c7b80dfd4b9edd839f9e |
| VERSION.dll | 17920 | 4b9ac818f620b3b3fd5d4e010186523d3628f050b1938c34b757a510bd3a9a67 |
| payload/ThemeUI.dll | 15360 | abcc600b4e8fb2d1ae4d6fa76b523c8a39cc8c296691c7b80dfd4b9edd839f9e |
| payload/VERSION.dll | 17920 | 4b9ac818f620b3b3fd5d4e010186523d3628f050b1938c34b757a510bd3a9a67 |
| payload/ccu.py | 15899 | 7ea6a55c7759e703be1caf713d80438198fc696962755bebd74c6ae1d665288f |
| payload/d32.py | 198835 | e7466b8a7c0aa86ea245d3648cf9c278a71ad74a7bcb0c265a87d6c029a5dd3a |
| payload/loader.vbs | 2580 | 91aa35f5de72ca556c93d039162a399ba4ea64fff4d7b42b3b3c141933ab1f97 |
| payload/payload.hta | 612 | 24d91dfc5d13d331e6541b30ecc3321e6d0547c5377092011547dd661cc9f6f1 |
| payload/run.bat | 1300 | 51aba48b9c160d484f3aaf30abcf2a9389b5c5c5e7ce0de9da2d44f751366d63 |
| payload/s0.bat | 11496 | f2fb2c9b75f3198af730c8daf90ffc70434095205ae5623ac11c422bf9333f4b |
| payload/svc32.py | 3266 | 7ccc4bfd9b88375adfcd53370f6431d184cd954e4492af074b25fc1aa87fa1e9 |

## 5.1 svc32.py要点

字符串经chr()拼接隐藏；C2为https://gogettate.duckdns.org:443/data/d32.py；持久化伪装名AcrobatUpdSvc；SSLverify\_mode=CERT\_NONE。

## 5.2 d32.py要点

约199KB，主体为base64+marshal多层混淆的Python字节码；启动时写入Run键ThemeSvcHelper；inlinepatchAMSI与ETW；实际功能包括远控通信（acset.ps1中引用TCP 4444检测）、剪贴板劫持、凭据窃取等（与目录内专项模块一致）。

## 5.3 VERSION.dll劫持逻辑

恶意VERSION.dll代理系统version.dll全部导出函数，在DllMain创建工作线程，定位Python解释器后执行Microsoft\Windows\Themes\Cache\ThemeService.py。缓存目录：Microsoft\Windows\Themes\Cache。

## 5.4 loader.vbs与payload.hta

loader.vbs使用BitsTransfer从硬编码IP（字符串拆分'46.101'+'XXX.XXX:8080'）下载py.zip与WinMgmtSvc.py，并写入Run键WinMgmtSvc2；payload.hta最小化隐藏窗口，通过curl下载s0.bat并执行。

# 六、IOC汇总

## 6.1 网络IOC

|  |  |  |
| --- | --- | --- |
| 类型 | 值 | 说明 |
| IP | 46.101.XXX.XXX | 主C2/载荷服务器 |
| 域名 | gogettate.duckdns.org | DuckDNS动态域名，解析至同IP |
| URL | http://46.101.XXX.XXX:8080/ | WsgiDAV匿名读写 |
| URL | http://46.101.XXX.XXX:8080/payload/ | 载荷目录 |
| URL | https://gogettate.duckdns.org/data/ | HTTPS载荷下发 |
| URL | https://gogettate.duckdns.org:443/api/ccu/report | 凭据外泄API |
| 端口 | 8080/TCP | WsgiDAV |
| 端口 | 443/TCP | nginx载荷投递 |
| 端口 | 4444/TCP | acset.ps1中检测的远控回连端口（疑似） |

## 6.2 主机IOC

|  |  |
| --- | --- |
| 类型 | 路径/名称 |
| 文件 | %APPDATA%\Microsoft\Windows\Themes\Cache\ThemeService.py |
| 文件 | %APPDATA%\Microsoft\Windows\Themes\Cache\ThemeSvc.bat |
| 文件 | %APPDATA%\Microsoft\Windows\Themes\Cache\ThemeUI.dll |
| 文件 | %APPDATA%\Microsoft\Windows\Themes\Cache\VERSION.dll |
| 文件 | %TEMP%\svc32.py/d32.py/s0.bat |
| 注册表 | HKCU\...\Run\ThemeSvcHelper/AcrobatUpdSvc/WinMgmtSvc2 |
| 计划任务 | ThemeSvcCheck/ThemeSvcMaint/AcrobatUpdateService |
| 进程 | pyth...