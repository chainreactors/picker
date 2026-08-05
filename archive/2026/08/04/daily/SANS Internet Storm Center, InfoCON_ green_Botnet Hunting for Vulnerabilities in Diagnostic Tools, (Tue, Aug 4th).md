---
title: Botnet Hunting for Vulnerabilities in Diagnostic Tools, (Tue, Aug 4th)
url: https://isc.sans.edu/diary/rss/33214
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-04
fetch_date: 2026-08-05T04:59:23.662150
---

# Botnet Hunting for Vulnerabilities in Diagnostic Tools, (Tue, Aug 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33208)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Botnet Hunting for Vulnerabilities in Diagnostic Tools](/forums/diary/Botnet%2BHunting%2Bfor%2BVulnerabilities%2Bin%2BDiagnostic%2BTools/33214/)

**Published**: 2026-08-04. **Last Updated**: 2026-08-04 12:46:19 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Botnet%2BHunting%2Bfor%2BVulnerabilities%2Bin%2BDiagnostic%2BTools/33214/#comments)

This morning, I noticed specific sources "hunting" for vulnerabilities in URLs that I haven't noticed before. All of these URLs appear to be associated with diagnostic tools:

| URL | Count | Vulnerability |
| --- | --- | --- |
| [/](/weblogs/urlhistory.html?url=Lw%3D%3D) | 1 | (simple recon for index page) |
| [/apply.cgi](/weblogs/urlhistory.html?url=L2FwcGx5LmNnaQ%3D%3D) | 20 | CVE-2024-12856 Four-Faith router command injection |
| [/cgi-bin/adv\_ping.cgi](/weblogs/urlhistory.html?url=L2NnaS1iaW4vYWR2X3BpbmcuY2dp) | 20 | ? |
| [/cgi-bin/diagnostic.cgi](/weblogs/urlhistory.html?url=L2NnaS1iaW4vZGlhZ25vc3RpYy5jZ2k%3D) | 20 | CVE-2013-7179 Seowon Intech WiMAX SWU-9100 mobile route |
| [/cgi-bin/DiagnosticsMsg.cgi](/weblogs/urlhistory.html?url=L2NnaS1iaW4vRGlhZ25vc3RpY3NNc2cuY2dp) | 20 | ? |
| [/cgi-bin/ping.cgi](/weblogs/urlhistory.html?url=L2NnaS1iaW4vcGluZy5jZ2k%3D) | 20 |  |
| [/cgi-bin/system\_mgr.cgi](/weblogs/urlhistory.html?url=L2NnaS1iaW4vc3lzdGVtX21nci5jZ2k%3D) | 20 |  |
| [/cgi-bin/traceroute.cgi](/weblogs/urlhistory.html?url=L2NnaS1iaW4vdHJhY2Vyb3V0ZS5jZ2k%3D) | 20 |  |
| [/diag\_ping.cgi](/weblogs/urlhistory.html?url=L2RpYWdfcGluZy5jZ2k%3D) | 20 | CVE-2020-8949 (maybe.. slightly different URL) Gocloud devices |
| [/goform/diagTool](/weblogs/urlhistory.html?url=L2dvZm9ybS9kaWFnVG9vbA%3D%3D) | 20 | CVE-2024-48419 (maybe..) Edimax Routers |
| [/goform/ping](/weblogs/urlhistory.html?url=L2dvZm9ybS9waW5n) | 20 |  |
| [/ping\_test.cgi](/weblogs/urlhistory.html?url=L3BpbmdfdGVzdC5jZ2k%3D) | 20 |  |
| [/sys\_diag.html](/weblogs/urlhistory.html?url=L3N5c19kaWFnLmh0bWw%3D) | 20 |  |

The naming of these URLs points to diagnostic tools. I was unable to find any specific vulnerabilities associated with many of the URLs, but the table above reflects those I found. But diagnostic tools often suffer from file inclusion and code execution vulnerabilities.

These tools will often call operating system commands directly, without properly separating user-provided arguments. Here is a sample vulnerability in a ping utility:

> response = os.system("ping -c 1 -w2 " + hostname )

The above example is in Python. But most (all?) languages have something equivalent to "os.system" (often called "exec", "shell\_exec", "process" ...) Often, proper input validation and output encoding are used to prevent this vulnerability, but, in my opinion, there is a better approach that should always be used in addition to input validation, and I do not see it used much.

As with many other vulnerabilities, the root cause of command injection is the concatenation of user data and commands. Mixing control plane and data plane has been an issue since blue boxing and continues today with prompt injection. The real fix is to avoid this comingling of data and commands and instead properly separate them. Prepared statements in SQL are probably the best-known approach following this principle.

For OS command execution, we do have a very similar solution. The "system" command in your language will typically call the standard C function "exec" [1]. This family of function implements some meant to pass command line arguments: execv ("exec vector"). In addition to the command, it accepts an array of command-line arguments that are then passed to the command, properly separating the command from the arguments.

Python implements execv as part of the subprocess module:

> response = subprocess.run("ping", "-c", 1, "-w", 2, hostname )

Using "subprocess.run" eliminates the possibility of command injection in this example.

For example, if you are using "google.com; ls" as a hostname, you get:

> `ping: cannot resolve google.com; ls: Unknown host`

The entire string "google.com; ls" was used as a hostname, and the ";" no longer acted as a separator. Give it a try with other command injection strings, and you will see similar results.

There are a few cases where "execv" is not sufficient. Some operating system commands may execute additional commands passed on the command line. For example, tcpdump offers the "-z" option to execute a "postrotate command". But these cases are rare, and if you are running into them, you are back to proper input validation to use these specific command line options. In most cases, users cannot specify the command-line option itself but only the parameter; using the "execv" API will help.

A while ago, I also made a brief video with more details on preventing OS command injection: <https://www.youtube.com/watch?v=7QDO3pZbum8>. It also covers some of the issues around Windows, which implements different APIs.

[1] https://man7.org/linux/man-pages/man3/exec.3.html

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [os command injection](/tag.html?tag=os command injection)

[1 comment(s)](/diary/Botnet%2BHunting%2Bfor%2BVulnerabilities%2Bin%2BDiagnostic%2BTools/33214/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33208)

### Comments

Excellent write-up. I particularly appreciated the emphasis on separating commands from user input rather than relying solely on sanitization. Designing away an entire class of vulnerabilities is a much stronger engineering approach. I believe this same principle will be fundamental to securing AI agents as they increasingly interact with external tools and operating system commands.

#### Swarandeep Singh

#### Aug 4th 2026 14 hours ago

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)