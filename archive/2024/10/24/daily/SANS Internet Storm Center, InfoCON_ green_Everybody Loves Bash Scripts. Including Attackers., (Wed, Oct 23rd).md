---
title: Everybody Loves Bash Scripts. Including Attackers., (Wed, Oct 23rd)
url: https://isc.sans.edu/diary/rss/31376
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-24
fetch_date: 2025-10-06T18:56:11.526605
---

# Everybody Loves Bash Scripts. Including Attackers., (Wed, Oct 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31372)
* [next](/diary/31380)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Everybody Loves Bash Scripts. Including Attackers.](/forums/diary/Everybody%2BLoves%2BBash%2BScripts%2BIncluding%2BAttackers/31376/)

**Published**: 2024-10-23. **Last Updated**: 2024-10-23 12:52:45 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Everybody%2BLoves%2BBash%2BScripts%2BIncluding%2BAttackers/31376/#comments)

Today our "First Seen" page displayed a number of simple URLs:

> `/wp-backup.sh
> /submit.sh
> /stage-deploy.sh
> /scripts/driverenv.sh
> /s3.sh
> /run-deploy.sh
> /passwords.sh
> /m/index.php
> /library.sh
> /installer.sh
> /envvars.sh
> /driverenv.sh
> /driver.sh
> /docker/startup.sh
> /develop.sh
> /bucket.sh
> /aws_cli.sh
> /aws-env.sh`

These URLs are not associated with a specific vulnerability. But they all have a couple of things in common:

* Based on the .sh extension, they appear to be shell scripts
* The name hints at scripts used to configure environment variables and other credentials.

Web applications often use environment variables to configure parameters like credentials. This isn't the most secure way of doing things, but it is often the most convenient and "secure enough" method. Storing credentials properly with tools like secret managers takes more work and planing. It also tends to be less portable between different systems. For a developer to use the same code on a development and production systems, environment variables are usually the easy choice.

In the past, I have written about scans for files holding environment variables, like ".env". But it looks like attackers got tired of these scans and are fanning out to other possible targets.

Some scripts (e.g. develop.sh or /docker/startups.sh) are often used to configure and start docker containers.

The scans yesterday originated from two IP addresses:

[179.43.191.19](/ipinfo.html?ip=179.43.191.19): The website at this IP address displays an open directory listing. But the files appear more related to an old, now broken website.

[37.60.229.171](/ipinfo.html?ip=37.60.229.171): Shodan shows only port 22 (ssh) listening.

Both IPs have been in our logs for about a month, scanning for various web application issues. They both appear to be colocated (virtual?) servers.

Lesson learned: Check your web servers for exposed configuration files. Sadly, they too often end up in the document root. At the very least, ensure they are outside the document root and, if possible, look for better ways to store secrets.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Everybody%2BLoves%2BBash%2BScripts%2BIncluding%2BAttackers/31376/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31372)
* [next](/diary/31380)

### Comments

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
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)