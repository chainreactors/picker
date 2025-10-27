---
title: Windows网络探活
url: http://blog.nsfocus.net/windows-3/
source: 绿盟科技技术博客
date: 2023-06-26
fetch_date: 2025-10-04T11:47:37.373963
---

# Windows网络探活

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Windows网络探活

### Windows网络探活

[2023-06-25](https://blog.nsfocus.net/windows-3/ "Windows网络探活")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,278

Win10右下角托盘区域有时会出现个小地球，提示”无法连接到Internet”，即使你正欢快地上着公网，仍有一定几率看到这个提示。一般来说不用理会，也不影响啥。但
是，出现该提示时，你的Microsoft Store就废了，无法下载安装应用、无法登录、提示0x800704cf错误码等等，微软的智障设计。其实还有其他影响，主要影响微软家
的网络应用，比如Skype、Office 365等等。

这个小地球的出现与下列注册表设置相关

————————————————————————–
Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet]
“ActiveDnsProbeContent”=”131.107.255.255”
“ActiveDnsProbeContentV6″=”fd3e:4f5a:5b81::1”
“ActiveDnsProbeHost”=”dns.msftncsi.com”
“ActiveDnsProbeHostV6″=”dns.msftncsi.com”
“ActiveWebProbeContent”=”Microsoft Connect Test”
“ActiveWebProbeContentV6″=”Microsoft Connect Test”
“ActiveWebProbeHost”=”www.msftconnecttest.com”
“ActiveWebProbeHostV6″=”ipv6.msftconnecttest.com”
“ActiveWebProbePath”=”connecttest.txt”
“ActiveWebProbePathV6″=”connecttest.txt”
“CaptivePortalTimer”=dword:00000000
“CaptivePortalTimerBackOffIncrementsInSeconds”=dword:00000005
“CaptivePortalTimerMaxInSeconds”=dword:0000001e
“EnableActiveProbing”=dword:00000001
“PassivePollPeriod”=dword:0000000f
“StaleThreshold”=dword:0000001e
“WebTimeout”=dword:00000023

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet\ManualProxies]
————————————————————————–

$ reg.exe query “HKLM\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet”

HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet
ActiveDnsProbeContent REG\_SZ 131.107.255.255
ActiveDnsProbeContentV6 REG\_SZ fd3e:4f5a:5b81::1
ActiveDnsProbeHost REG\_SZ dns.msftncsi.com
ActiveDnsProbeHostV6 REG\_SZ dns.msftncsi.com
ActiveWebProbeContent REG\_SZ Microsoft Connect Test
ActiveWebProbeContentV6 REG\_SZ Microsoft Connect Test
ActiveWebProbeHost REG\_SZ www.msftconnecttest.com
ActiveWebProbeHostV6 REG\_SZ ipv6.msftconnecttest.com
ActiveWebProbePath REG\_SZ connecttest.txt
ActiveWebProbePathV6 REG\_SZ connecttest.txt
CaptivePortalTimer REG\_DWORD 0x0
CaptivePortalTimerBackOffIncrementsInSeconds REG\_DWORD 0x5
CaptivePortalTimerMaxInSeconds REG\_DWORD 0x1e
EnableActiveProbing REG\_DWORD 0x1
PassivePollPeriod REG\_DWORD 0xf
StaleThreshold REG\_DWORD 0x1e
WebTimeout REG\_DWORD 0x23

Windows有套神经病机制判断当前PC是否能上公网，不说IPv6，只说IPv4，至少包含
如下操作

$ curl http://www.msftconnecttest.com/connecttest.txt
Microsoft Connect Test

$ curl -s http://www.msftconnecttest.com/connecttest.txt | xxd -g 1
00000000: 4d 69 63 72 6f 73 6f 66 74 20 43 6f 6e 6e 65 63 Microsoft Connec
00000010: 74 20 54 65 73 74 t Test

定时访问上述URL，期待返回”Microsoft Connect Test”。仔细看注册表

————————————————————————–
“ActiveWebProbeContent”=”Microsoft Connect Test”
“ActiveWebProbeHost”=”www.msftconnecttest.com”
“ActiveWebProbePath”=”connecttest.txt”
————————————————————————–

瞧见没，访问哪个FQDN的哪个文件，期待返回什么内容，都在注册表中指定好了。WWW探活用的是HTTP(80/TCP)，不是HTTPS(443/TCP)。

另一个探活操作类似这样

$ nslookup -type=A dns.msftncsi.com 8.8.8.8
…
Name: dns.msftncsi.com
Address: 131.107.255.255

$ dig +short A dns.msftncsi.com @8.8.8.8
131.107.255.255

同样有注册表项对应

————————————————————————–
“ActiveDnsProbeContent”=”131.107.255.255”
“ActiveDnsProbeHost”=”dns.msftncsi.com”
————————————————————————–

明明能上公网，只是WWW/DNS探活检测失败，Microsoft Store仍受影响，这种智障设计的原始逻辑是什么？身在大陆地区，包括但不限于GFW在内的各种干扰因素很难不
影响探活检测。当PC位于非透明Proxy后面时，比如Proxy需要身份认证、不转发UDP通信等等，探活检测更加神经病，会不停尝试。另一方面，探活检测事实上向微软服
务器不停报告Windows系统的存在，有洁癖的可能不喜这种行为。当然，即便没有探活检测，仍有其他通信前往微软服务器，防不胜防，此处不展开。

将EnableActiveProbing从1改成0，会阻止”Microsoft Internet Connection Test”

————————————————————————–
Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet]
“EnableActiveProbing”=dword:00000000
————————————————————————–

reg.exe add “HKLM\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet” /v “EnableActiveProbing” /t REG\_DWORD /d 0 /f
reg.exe query “HKLM\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet” /v “EnableActiveProbing”

组策略另有一套机制阻止探活检测

————————————————————————–
gpedit.msc
Local Computer Policy
Computer Configuration
Administrative Templates
System
Internet Communication Management
Internet Communication settings
Turn off Windows Network Connectivity Status Indicator active tests
Enabled
————————————————————————–
本地计算机策略
计算机配置
管理模板
系统
Internet通信管理
Internet通信设置
关闭Windows网络连接状态指示器的活动测试
已启用
————————————————————————–
Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SOFTWARE\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator]
“NoActiveProbe”=dword:00000001
————————————————————————–

reg.exe add “HKLM\SOFTWARE\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator” /v “NoActiveProbe” /t REG\_DWORD /d 1 /f
reg.exe query “HKLM\SOFTWARE\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator” /v “NoActiveProbe”
reg.exe delete “HKLM\SOFTWARE\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator” /v “NoActiveProbe” /f

我测试过，彻底禁用探活检测后，不影响Microsoft Store使用。若不想彻底禁用探活检测，可通过注册表项修改WWW/DNS探活检测所用数据，比如将connecttest.txt放在自建服务器上，再比如将DNS探活检测所用FQDN及期待的解析结果改成其他值，这些都是我YY的，未实测。

这事儿也可通过组策略完成

————————————————————————–
gpedit.msc
Local Computer Policy
Computer Configuration
Administrative Templates
Network
Network Connectivity Status Indicator
Specify corporate Website probe URL
Specify corporate DNS probe host name
Specify corporate DNS probe host address
Specify global DNS
————————————————————————–
本地计算机策略
计算机配置
管理模板
网络
网络连接状态指示器
指定企业网站探测URL
指定企业DNS探测主机地址
指定企业DNS探测主机名
指定全局DNS
————————————————————————–

NCSI默认情况下会将DNS探活局限于当前正在探测的接口。若启用”指定全局DNS”，则NCSI允许在任何接口上进行DNS探活，比如向127.0.0.1:53/UDP查询。

还可以尝试用hosts文件骗过DNS探活

$ notepad c:\windows\system32\drivers\etc\hosts

131.107.255.255 dns.msftncsi.com

未研究WWW探活与DNS探活是AND还是OR的关系，我猜是AND。

NCSI (Network Connectivity Status Indicator)是从Vista开始引入的，当时的DNS探活数据延用至今，但WWW探活数据有变。

据说除了主动探活，还有被动探活。假设启用主动探活，但主动探活因故失败，此时被动探活继续这种自以为是的神经病行为。当进入本机的IP报文TTL小于8时，被动探活失败。相关注册表项是

————————————————————————–
Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet]
“PassivePollPeriod”=dword:0000000f
“MinimumInternetHopCount”=dword:00000008
————————————————————————–

若判断是被动探活惹的祸，尝试将MinimumInternetHopCount改成1，这是最小有效值。

可通过组策略禁用被动探活

————————————————————————–
gpedit.msc
Local Computer Policy
Computer Configuration
Administrative Templates
Network
Network Connectivity Status Indicator
Specify passive polling
————————————————————————–
本地计算机策略
计算机配置
管理模板
网络
网络连接状态指示器
指定被动轮询
————————————————————————–

有人见到过这样的注册表设置

————————————————————————–
Windows Registry Editor Version 5.00

[HKEY\_LOCAL\_MACHINE\SYSTEM\ControlSet001\Services\NlaSvc\Parameters\Internet\ManualProxies]
@=”http=127.0.0.1:8080;https=127.0.0.1:8080”
————————————————————————–

我猜是为WWW探活指定相应Proxy吧，不过这种肯定解决不了DNS探活过Proxy的问题。若WWW探活与DNS探活是OR...