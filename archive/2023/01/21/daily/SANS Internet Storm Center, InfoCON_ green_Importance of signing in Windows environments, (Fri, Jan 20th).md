---
title: Importance of signing in Windows environments, (Fri, Jan 20th)
url: https://isc.sans.edu/diary/rss/29456
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-21
fetch_date: 2025-10-04T04:31:08.584753
---

# Importance of signing in Windows environments, (Fri, Jan 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29452)
* [next](/diary/29458)

My next class:

|  |  |  |
| --- | --- | --- |
| [Web App Penetration Testing and Ethical Hacking](https://www.sans.org/event/london-march-2026/course/web-app-penetration-testing-ethical-hacking) | London | Mar 2nd - Mar 7th 2026 |

# [Importance of signing in Windows environments](/forums/diary/Importance%2Bof%2Bsigning%2Bin%2BWindows%2Benvironments/29456/)

**Published**: 2023-01-20. **Last Updated**: 2023-01-20 09:29:29 UTC
**by** [Bojan Zdrnja](/handler_list.html#bojan-zdrnja) (Version: 1)

[1 comment(s)](/diary/Importance%2Bof%2Bsigning%2Bin%2BWindows%2Benvironments/29456/#comments)

NTLM relaying has been a plague in Windows environments for many years – and we have witnessed many exploits that rely on the fact that it is possible to relay NTLM authentication attempts to various target services.

While there are many potential targets here, in most red team engagements my colleagues and myself are relaying credentials to other SMB, LDAP or HTTP(S) services (especially on AD CS server, used for issuing certificates). So one of the mandatory “health check” activities should be to verify if your systems really have signing enabled. Here are two \*very simple\* ways on how I do it when I encounter large number of internal assets.

**(1) Nmap for help**

For verifying status of SMB services, nmap is really all you need (and my previous students of [SEC542](https://www.sans.org/cyber-security-courses/web-app-penetration-testing-ethical-hacking/) can witness on me being a big fan of nmap scripts). While there are quite a bit of SMB scripts that we can use, the one we want is the smb2-security-mode.nse script, which will check SMBv2 security settings (if you are still running SMBv1 then you have another set of problems: disable it).

Running this script is amazingly easy on any size of target network(s), simply scan target assets on ports 139 and 445 and verify the results.

Here is one well configured server:

`$ nmap -sT -p 139,445 10.0.10.10 --script smb2-security-mode
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-19 21:31 CET
Nmap scan report for 10.0.10.10)
Host is up (0.015s latency).`

`PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds`

`Host script results:
| smb2-security-mode:
|   2.02:
|_    Message signing enabled and required`

This one not so much (almost there, but notice that signing is not required):

`$ nmap -n -v -Pn -p 139,445 --script=+smb2-security-mode  10.12.99.9
Nmap scan report for 10.12.99.9
Host is up (0.0014s latency).`

`PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds`

`Host script results:
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required`

**(2) Testing HTTP/S on AD CS server**

While there could be other cases to abuse with HTTP/S servers and NTLM relaying, in this diary I’ll just limit testing to the AD CS server, since it is the most often abused target service. Testing in this case is quite simple and can be performed even with the curl command.

You need to find the AD CS server and them simply issue a request to the http://adcs/certsrv URL. You need to use the -v flag to display response headers as we will want to see which authentication mechanisms are supported:

`$ curl -v -k http://adcs/certsrv
*   Trying 10.0.10.5:80...
* TCP_NODELAY set
* Connected to adcs (10.0.10.5) port 80 (#0)
> GET /certsrv HTTP/1.1
> Host: adcs
> User-Agent: curl/7.68.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 401 Unauthorized
< Content-Type: text/html
< Server: Microsoft-IIS/8.0
< WWW-Authenticate: Negotiate
< WWW-Authenticate: NTLM
< Date: Thu, 19 Jan 2023 20:16:35 GMT
< Content-Length: 1293
<
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>401 - Unauthorized: Access is denied due to invalid credentials.</title>
<style type="text/css">
<!--
body{margin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;}
fieldset{padding:0 15px 10px 15px;}
h1{font-size:2.4em;margin:0;color:#FFF;}
h2{font-size:1.7em;margin:0;color:#CC0000;}
h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;}
#header{width:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;
background-color:#555555;}
#content{margin:0 0 0 2%;position:relative;}
.content-container{background:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;}
-->
</style>
</head>
<body>
<div id="header"><h1>Server Error</h1></div>
<div id="content">
 <div class="content-container"><fieldset>
  <h2>401 - Unauthorized: Access is denied due to invalid credentials.</h2>
  <h3>You do not have permission to view this directory or page using the credentials that you supplied.</h3>
 </fieldset></div>
</div>
</body>
</html>`

The two important lines here are the following (also highlighted above):

`< WWW-Authenticate: Negotiate
< WWW-Authenticate: NTLM`

< indicates that this is a response header and as we can see, this server is supporting both NTLM and Kerberos authentication. A properly configured server should not have the second line in the response (WWW-Authenticate: NTLM).

Can it be simpler than this? So why aren’t you testing your systems already? Here’s a nice weekend project ?

Next time we’ll go over myriad of LDAP settings, which is another channel that gets abused quite often.

--
Bojan
[@bojanz](https://twitter.com/bojanz)
[INFIGO IS](https://www.infigo.hr/)

Keywords:

[1 comment(s)](/diary/Importance%2Bof%2Bsigning%2Bin%2BWindows%2Benvironments/29456/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Web App Penetration Testing and Ethical Hacking](https://www.sans.org/event/london-march-2026/course/web-app-penetration-testing-ethical-hacking) | London | Mar 2nd - Mar 7th 2026 |

* [previous](/diary/29452)
* [next](/diary/29458)

### Comments

Very simple, but you have to download the .nse file from nmap.org
and then where do you get the required modules to make this work?

local smb = require "smb"
local smb2 = require "smb2"
local stdnse = require "stdnse"
local table = require "table"
local nmap = require "nmap"

Thanks!

#### Mr.Tibbs

#### Feb 1st 2023 2 years ago

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) f...