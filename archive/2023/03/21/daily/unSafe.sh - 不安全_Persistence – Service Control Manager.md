---
title: Persistence – Service Control Manager
url: https://buaq.net/go-154405.html
source: unSafe.sh - 不安全
date: 2023-03-21
fetch_date: 2025-10-04T10:06:12.591141
---

# Persistence – Service Control Manager

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/8befcab0a80ee1def9887c8fa5989bcb.jpg)

Persistence – Service Control Manager

Skip to contentThe service control manager (SCM) is responsible to start and sto
*2023-3-20 23:53:46
Author: [pentestlab.blog(查看原文)](/jump-154405.htm)
阅读量:17
收藏*

---

[Skip to content](#content)

The service control manager (SCM) is responsible to start and stop services in windows environments including device drivers and start up applications. Microsoft introduced in Windows 2000 and later the Security Descriptor Definition Language (SDDL) in order to provide a textual representation for security descriptors in a more readable format. Prior to Windows 2000 security descriptors were represented as hex bytes. Permissions of the service control manager like other windows objects are managed by Discretionary Access Control List (DACL) which are also represent by SDDL.

During red team operations if elevated access has been achieved the permissions of the service control manager can be modified via the SDDL in order to grant the “Everyone” group with rights over the service control manager. This action could be used as a form of persistence since any user could create a service on the environment that will execute an arbitrary command or payload with SYSTEM level privileges every time that the computer starts. The technique was discovered by [Grzegorz Tworek](https://twitter.com/0gtweet) and was shared over Twitter.

Execution of the command below will retrieve quickly the SDDL rights of the service control manager utility.

```
sc sdshow scmanager
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-scmanager-security-descriptor.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-scmanager-security-descriptor.png)

Service Control Manager – Security Descriptor

PowerShell could also be used to enumerate SDDL rights for all the user groups and convert them to a readable format.

```
$SD = Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Schedule\Security\
$sddl = ([wmiclass]”Win32_SecurityDescriptorHelper”).BinarySDToSDDL($SD.Security).Sddl
$SecurityDescriptor = ConvertFrom-SddlString -Sddl $sddl
$SecurityDescriptor.DiscretionaryAcl
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-enumerate-permissions-powershell.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-enumerate-permissions-powershell.png)

Enumerate Permissions via PowerShell

The command below will enumerate the permissions of the “*scmanager*” utility and will display the associated SDDL rights.

```
sc sdshow scmanager showrights
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-scmanager-show-rights.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-scmanager-show-rights.png)

Service Control Manager – Rights Enumeration

Users with standard level access they cannot create a service in Windows environments. This privilege belongs only to elevated users such as Local Administrators. However, modification of the security descriptor permissions for the service control manager could allow also any user to create a service that will run under the context of the SYSTEM account. Using the security descriptor definition language these permissions could be modified by executing the command below:

```
sc.exe sdset scmanager D:(A;;KA;;;WD)
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-security-descriptor-permission-modification.png?w=980)](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-security-descriptor-permission-modification.png)

Security Descriptor Permission Modification

The following table displays what the SDDL acronyms mean in the above command.

|  |  |
| --- | --- |
| D | Discretionary Access Control List |
| A | Access Control Entry – Access Allowed |
| KA | KEY\_ALL\_ACCESS – Rights |
| WD | Security Principal of Everyone Group |

The service configuration utility could be used to create a new service. The “*binPath*” parameter could store the arbitrary payload which will executed once the service starts. It should be noted that since the permissions of the service control manager changed, non elevated users can also create new services on the windows environment. In the event that the malicious service is removed by the blue team permissions will still remain allowing standard users to continue create new services to maintain persistence.

```
sc create pentestlab displayName= "pentestlab" binPath= "C:\temp\pentestlab.exe" start= auto
```

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-service-creation.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-service-creation.png)

Service Control Manager – New Service from Standard User Account

The new service will appear in the list of Windows services.

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-services.png?w=1024)](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-services.png)

Service Control Manager – New Service

When the system starts again, the service will automatically initiate and the payload will executed with SYSTEM level privileges.

[![](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-meterpreter.png?w=636)](https://pentestlab.files.wordpress.com/2023/03/persistence-sddl-meterpreter.png)

Service Control Manager – Meterpreter

## Post navigation

文章来源: https://pentestlab.blog/2023/03/20/persistence-service-control-manager/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)