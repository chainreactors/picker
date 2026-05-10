---
title: AI软件仿冒攻击再现，DeepSeek TUI成伪装诱饵
url: https://mp.weixin.qq.com/s/SPN25Z4cLCHu7bEhVYTSNQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:29:45.196068
---

# AI软件仿冒攻击再现，DeepSeek TUI成伪装诱饵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqibGP9VflbpCQlNDosCfuAbibic3RiclhX6G1iay2Uj1jeMCA3NXoAlAZDYFLDnWiaPF9MmslibB68hYOPfMT3OQaPYtVMIGHpWmALxdk/0?wx_fmt=jpeg)

# AI软件仿冒攻击再现，DeepSeek TUI成伪装诱饵

原创

红雨滴团队
红雨滴团队

奇安信威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 概述

开源项目DeepSeek TUI是一个为DeepSeek大模型创造的在终端中运行的编码智能体，近期随着DeepSeek v4的发布和开发者Hunter Bown的中文扩散帖，让该项目吸引到大量关注。

![](https://mmbiz.qpic.cn/mmbiz_png/odcL3w4qOq9pzo77gj0Xz1BsAwR8hYY2vVjegtHIe2RB5dehMO8OKIBEPWjRneWMNGnplXSZeiajwaJG9C4toF4ghck3ol24EEbecgoDRY2A/640?wx_fmt=png&from=appmsg)

奇安信威胁情报中心监测到，攻击者趁着DeepSeek TUI项目热度上升，开始混水摸鱼，在Github上构造仿冒仓库，投递恶意软件。下图中第一个是真正的DeepSeek TUI项目仓库，第二个是仿冒仓库。

![](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOqicc6ySKIpWduRumNGFEWaI9SScCZLIxqia2ZBF8ksfJ9F235510gamczickCFmJgnZVwdYZLbeCEap3b0modwtWICBTic788hYI7c/640?wx_fmt=jpeg&from=appmsg)

恶意软件特征与我们3月披露的仿冒OpenClaw的攻击样本一致[1]，并且使用的恶意域名与国外安全厂商近期发布的报告重叠[2]，表明此类伪装成AI产品的恶意软件攻击活动持续不断，且不停更换仿冒对象。

## 详细分析

恶意软件存放在伪造仓库的Releases页面中，不久前才上传。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOq8NuBCrZAVOwBwBGguX8FVWQdBvRaTCp4T6nQ9POCeJKcrxlhNgyopocQq9v8yjpSVEpSDfnYnzgDMdQykUk1F6mYkWqPXmG4E/640?wx_fmt=jpeg&from=appmsg)

下载的7z压缩包中包含的EXE文件信息如下。

| 文件名 | DeepSeek-TUI\_x64.exe |
| --- | --- |
| MD5 | b96c0d609c1b7e74f8cb1442bf0b5418 |
| 编译时间 | 2026-04-29 08:53:41 UTC |

样本的属性信息如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqicCKnpfaibmtqKtiacxUvhmGLJwF49R122keialichbE7H9z6jYjJ4ZLKibA2E4QKRUgibfNJzzKUl89AMAdV7ZS9QjA0c2WenGTicv0Y/640?wx_fmt=jpeg&from=appmsg)

### （一）运行环境检测

样本的运行环境检测系统采用分层评分架构：TIER0（致命指标一票否决）+ TIER1/2（可疑指标积分制）。此外，后续下载的二阶段恶意软件OneSync.exe中同样存在反沙箱模块，包含”src\anti\_bot.rs”、”TIER0: VirtualBox default NAT IP (10.0.2.15) detected”、”TIER0: Bot farm hostname pattern”等字符串，说明反沙箱不只存在于一级样本，二阶段组件还会独立进行环境判定。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOq8hYZJ1FNcVs31g1vIFDjcA5KDNGxsrqFDeerHqr8OVk3OXdR1icjEYak21APGEBzoc1Y68qbxn3yKLpSq0hyalHUsPoiaXicjpibI/640?wx_fmt=jpeg&from=appmsg)

（1） TIER0阶段检测，存在黑名单信息则直接判定为沙箱环境。

| 检测项 | 黑名单信息 |
| --- | --- |
| 虚拟机关键词 | hyper-v、vmware、qemu、virtualbox、parallels（大小写不敏感） |
| 进程检测 | 包含ollydbg.exe、x32dbg.exe、x64dbg.exe、windbg.exe、ida.exe、ida64.exe、processhacker.exe、procexp.exe、procexp64.exe、wireshark.exe、fiddler.exe、charles.exe、sandboxie.exe、vmtoolsd.exe、vmwaretray.exe、vmwareuser.exe、vboxservice.exe、vboxtray.exe |
| 沙箱监控DLL检测 | 包含cuckoomon.dll（Cuckoo 沙箱）、SbieDll.dll（Sandboxie）、SxIn.dll、cmdvrt32.dl、cmdvrt64.dll（Comodo 沙箱）加上VM驱动文件vmouse.sys、vmhgfs.sys、VBoxMouse.sys、VBoxGuest.sys、VBoxSF.sys、VBoxVideo.sys、Wasp.sys |
| 黑名单用户名检测 | 包含malware、virus、sandbox、sand box、wdagutilityaccount、sample、currentuser、maltest、bruno、jzdekker、Janet Van Dyne、Harry Johnson |
| VirtualBox默认 NAT IP 检测 | 硬编码 IP 地址10.0.2.15 |
| VM MAC OUI 检测 | MAC 地址前缀黑名单包含 08:00:27（VirtualBox）、00:15:5D（Hyper-V）、52:54:00（KVM/QEMU）、00:23:45，覆盖主流虚拟化平台的默认 MAC 地址前缀 |
| Bot farm主机名模式检测 | 黑名单中还预置了大量仿真实Bot farm主机名（eslmdigB、kismujmC、gpslqmrD，按字母表顺序排列的 8 字符随机串） |
| GPU预筛查 | 枚举 HKLM\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}下显示适配器子键的 DriverDesc 值，用于识别 hyper-v、vmware、virtualbox、parallels、qemu 等虚拟化显卡。 |

（2）通过TIER0阶段检测的系统进入积分评估阶段，分值越大越可能是沙箱环境。

| 检测项 | 评分值 |
| --- | --- |
| GPU评分 | 1. 高可疑分，沙箱 GPU 黑名单：microsoft basic display adapter、vmware svga、virtualbox graphics、hyper-v video、qemu;  2. 真实用户特征减分，合法 GPU 白名单：geforce rtx 2/3/4、geforce gtx 10/16、radeon rx 5/6/7、quadro、radeon pro、rtx a、intel(r) uhd/iris/hd graphics、amd radeon(tm) graphics;  3. 无GPU信息，加分 |
| CPU评分 | Xeon/EPYC→可疑；CPU核心数四级评分：<2(最高风险)/=2/4-7/>7(减分) |
| 内存大小 | <3.5GB(极可疑)/3.5-4.5/≥8(减分)/≥16(更减分) |
| 磁盘大小 | 系统盘<40GB或>200GB→加分；精确500GB/250GB→高疑似沙箱环境 |
| 软件数 | 四级评分：<30(CRITICAL)/30-49/50-79/≥200(减分) |
| 进程数 | 四级评分：<60(极可疑)/60-99/100-299/≥300(减分) |
| 分辨率 | 800x600/1024x768/1280x720→加分；1920x1080→减分 |
| BIOS序列号黑名单 | ete9t8e8t3/H6MBDR4/0311-3550-2146-3025-5233-5781-38/0/1234567890（沙箱/模板化环境常见序列号） |
| BIOS关键词 | seabios/bochs/qemu/vrtual/hyper-v/vmware/google/vbox/innotek（虚拟化平台 BIOS 字符串） |
| VM主板 | VirtualBox/Google Compute Engine/Virtual Machine（关键命中级） |
| 开机时间检测 | <5min→加分 |

（3）即使通过上述全部检测，最后还有一个鼠标移动检测，才会触发后续恶意行为。下载的二阶段组件svc\_service.exe同样存在该鼠标检测逻辑。

样本如果检测到运行环境不符合要求，会弹出提示信息：”Sorry, your system does not meet the minimum requirements.”，然后结束运行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqibdSXf9elHjNXDyETnrVBV9VDODiaXXmbRAOhN0qIYOlPfWkgY7cgcRhWEdsyrprRm9IuojkzicuIBpr3ibQuK6wEhG9MKGdlALIg/640?wx_fmt=jpeg&from=appmsg)

### （二）安全防护关闭

如果环境检测通过，执行如下powershell代码。

![](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOq8IKVJdVkBhahaiaMia2YwkCCjkZkic6lHzrsIRob3vTRDPMiabSalUVSCNNicdia8vX0rXJDoWCQbibEn1KKMz8PDVURPIGAWpgYC8cs/640?wx_fmt=jpeg&from=appmsg)

异或解密后如下。

![](https://mmbiz.qpic.cn/mmbiz_jpg/odcL3w4qOqibkicQibVE3rBicKuuDibqpX2PbZ39BktyYdkAKYOQR2QBJibo0ianwWKAx9P5JvLeJA1AxIibajkG1ZcXOWgEPzZZPM9neFDIYwefox4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/odcL3w4qOqicmqzPd16CeHqdjsF7CsTjKeEsqtGTjR7ZqbINKD566usuJhI5NDCspUXolORHiarq40MCcCtxSibzw4SiaSay3PicNfyKNI3EwcuM/640?wx_fmt=jpeg&from=appmsg)

主要功能是关闭一些Windows Defender安全防护，包括

(1) 添加6个排除路径，C:\Users、$env:TEMP、C:\ProgramData、C:\OneDriveTemp、C:\Users\Public、C:\Windows

(2) 排除进程powershell.exe和pwsh.exe

(3) MAPS 报告关闭、云阻断关闭、样本提交NeverSend、云保护等级归零、PUA 保护 disable、IOAV 保护 disable、行为监控 disable

(4) 防火墙开放57001/57002/56001三个入站端口

### （三）字符串解密与后续载荷获取

函数sub\_1400F22F5异或解密字符串，使用的key为” xnasff3wcedj”。

样本获取后续载荷的链接通过字符串解密得到，两个链接一个是主地址，一个是备用地址。

| hxxps://pastebin.com/raw/w6BVFFWQ  hxxps://snippet.host/beuskq/raw |
| --- |

两者各存放6个Azure云盘链接，指向7z压缩包，部分链接一致（不一致的用红色标识）。

|  |
| --- |
| hxxps://dev.azure.com/sagonbretzpr/f70c627a-789c-4281-8b4e-99fa76b8bfd3/\_apis/git/repositories/0239f5e1-3b3e-4f53-a525-7861596f8d9b/items?path=/0311/0504vicloud.7z&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0&download=true    hxxps://dev.azure.com/sagonbretzpr/f70c627a-789c-4281-8b4e-99fa76b8bfd3/\_apis/git/repositories/0239f5e1-3b3e-4f53-a525-7861596f8d9b/items?path=/0507/0507autodate.7z&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0&download=true    hxxps://dev.azure.com/sagonbretzpr/f70c627a-789c-4281-8b4e-99fa76b8bfd3/\_apis/git/repositories/0239f5e1-3b3e-4f53-a525-7861596f8d9b/items?path=/0207/0207Up16OneSync.7z&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0&download=true    hxxps://dev.azure.com/sagonbretzpr/f70c627a-789c-4281-8b4e-99fa76b8bfd3/\_apis/git/repositories/0239f5e1-3b3e-4f53-a525-7861596f8d9b/items?path=/0207/0207Up17WinHealhCare.7z&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0&download=true    hxxps://dev.azure.com/sagonbretzpr/f70c627a-789c-4281-8b4e-99fa76b8bfd3/\_apis/git/repositories/0239f5e1-3b3e-4f53-a525-7861596f8d9b/items?path=/0222/0224GHonedrive\_sync.7z&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0&download=true    hxxps://dev.azure.com/sagonbretzpr/f70c627a-789c-4281-8b4e-99fa76b8bfd3/\_apis/git/repositories/0239f5e1-3b3e-4f53-a525-7861596f8d9b/items?path=/0311/svc\_service.7z&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0&download=true |
| hxxps://dev.azure.com/sagonbretzpr/f70c627a-789c-4281-8b4e-99fa76b8bfd3/\_apis/git/repositories/0239f5e1-3b3e-4f53-a525-7861596f8d9b/items?path=/0311/0504vicloud.7z&versionDescriptor%5BversionOptions%5D=0&versionDescriptor%5BversionType%5D=0&versionDescriptor%5Bversion%5D=main&resolveLfs=true&%24format=octetStream&api-version=5.0&download=true    hxxps://dev.a...