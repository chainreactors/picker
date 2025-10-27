---
title: Development Features Enabled in Prodcution, (Thu, Oct 24th)
url: https://isc.sans.edu/diary/rss/31380
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-25
fetch_date: 2025-10-06T18:55:49.054630
---

# Development Features Enabled in Prodcution, (Thu, Oct 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31376)
* [next](/diary/31384)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Development Features Enabled in Prodcution](/forums/diary/Development%2BFeatures%2BEnabled%2Bin%2BProdcution/31380/)

**Published**: 2024-10-24. **Last Updated**: 2024-10-24 17:06:30 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Development%2BFeatures%2BEnabled%2Bin%2BProdcution/31380/#comments)

We do keep seeing attackers "poking around" looking for enabled development features. Developers often use these features and plugins to aid in debugging web applications. But if left behind, they may provide an attacker with inside to the application. In their simplest form, these features provide detailed configuration information. More severe cases may leak credentials or even provide full remote code execution access.

Here are some I noted today:

**/struts/webconsole.html**

As the URL implies, this is a feature of Struts. This URL provides an ONGL console to execute arbitrary OGNL expression. Who needs OGNL injection vulnerabilities if the developer enabled a console like this? Sadly, it appears that this particular feature is enabled even if devMode is turned off! [1]

**/telescope/requests**

Telescope is a debug extension for the popular Laravel PHP framework. Usually, this should only be accessible in the "local" environment, and should not be enabled in production environments.

**/server-status**

The classic Apache "server-status" will display a snapshot of requests currently processed by the server. This may leak URLs which is in particular an issue if the URL includes credentials.

**/logs/debug.log, /storage/logs/system.log and similar**

Exposing logs is certainly an issue. There are several similar URLs that attackers are looking for. In some cases, this could even lead to XSS and RCE attacks if the attacker can inject specific log entries.

**/phpunit/phpunit/Util/PHP/eval-stdin.php**

Essentially a little web shell used by the PHP unit testing framework.

What did I miss?

[1] https://breakfix.co/posts/apache-struts2-ognl-console-and-devmode-exploitation/

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [developer tools](/tag.html?tag=developer tools)

[1 comment(s)](/diary/Development%2BFeatures%2BEnabled%2Bin%2BProdcution/31380/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31376)
* [next](/diary/31384)

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