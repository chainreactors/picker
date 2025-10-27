---
title: Hackers Love This VSCode Extension: What You Can Do to Stay Safe, (Tue, Mar 7th)
url: https://isc.sans.edu/diary/rss/29610
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-08
fetch_date: 2025-10-04T08:57:29.209599
---

# Hackers Love This VSCode Extension: What You Can Do to Stay Safe, (Tue, Mar 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29606)
* [next](/diary/29614)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Hackers Love This VSCode Extension: What You Can Do to Stay Safe](/forums/diary/Hackers%2BLove%2BThis%2BVSCode%2BExtension%2BWhat%2BYou%2BCan%2BDo%2Bto%2BStay%2BSafe/29610/)

**Published**: 2023-03-07. **Last Updated**: 2023-03-07 15:04:31 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Hackers%2BLove%2BThis%2BVSCode%2BExtension%2BWhat%2BYou%2BCan%2BDo%2Bto%2BStay%2BSafe/29610/#comments)

[David Boyd, a SANS.edu undergraduate intern, submitted this post]

Have you ever considered that a VSCode extension you rely on could also be the very tool that puts your sensitive data in the hands of attackers? As fellow developers, we often can be seen when using the popular open-source platform Visual Studio Code (VSCode)--and even if you do not, you will know someone who does.

On February 19, 2023, an attempted exploit was identified in my DShield's honeypot weblogs. The attack targeted a security vulnerability in the VSCode-SFTP extension, which allows users to synchronize a local directory with a remote server via the web request: `/.vscode/sftp.json`.

![](https://isc.sans.edu/diaryimages/images/DAvidBoyd1.png)

Captured GET request from the DShield honeypot’s webserver.log

OWASP identifies this vulnerability under the A07:2021 – Identification and Authentication Failures category (previously known as Broken Authentication), and if exploited, it could allow attackers to access sensitive data such as usernames, passwords, and remote hosts.

The VSCode-SFTP extension setup is simple, requiring only a few lines of code in its `sftp.json` configuration file. These few lines can apply a wide range of settings. One such line is the password parameter. While optional, many users leave it unprotected, making it susceptible to attacks. Thus, the vulnerability results from the default permissions in this configuration file being left open to the public, saved in plain text, or containing hard-coded authentication credentials.

![](https://isc.sans.edu/diaryimages/images/DavidBoyd2.png)

Hard-coded credentials in the stfp.json config file

It is crucial to protect our SFTP credentials, as having them publicly accessible could pose significant dangers to our security. One of the major risks is unauthorized access, where anyone can use the credentials to gain access to our data, resulting in data breaches or theft of sensitive information. Another risk is malware attacks, where hackers can upload malicious code onto our server, causing potential data loss, downtime, or other disruptions. This can damage our reputation and erode customer trust. In addition, it can also result in compliance violations depending on the industry.
If you are a developer using this extension, we must ensure that our SFTP credentials are kept confidential and accessible only to authorized personnel, using strong passwords, two-factor authentication, encryption, and regularly auditing and monitoring access to SFTP servers. This will prevent sensitive information from being publicly accessible. If these mitigations are not plausible, you may need to consider removing the VSCode-SFTP extension entirely from production.

But who was behind this attack? Interestingly, the IP address [138.68.154.197](/ipinfo.html?ip=138.68.154.197) associated with the attempted exploit traces back to LeakIX, a public scanner that combines a search engine indexing public information and open reporting platform. LeakIX helps identify vulnerabilities in internet-facing technologies by following a 30-day disclosure policy to hosting companies before publishing the leak to the public. While the HTTP requests' user agent string of Go-http-client/1.1 does not contain any information identifying the client or device used to make the request explicitly, it can be confirmed that the requester was from the LeakIX’s Client scanner. According to their GitHub page, the scanner uses the Go programming language's net/http library to create their custom HTTP client.

Despite the relief that this was not a malicious attacker, but an ethical scanner, this attack serves as a warning to take the necessary precautions to secure your sensitive data. It illustrates that even with secure protocols like SFTP, if communication credentials become publicly available, then the security of the protocol could be rendered useless. It also highlights the risks associated with leaving default file permissions open to the public and the importance of securing sensitive configuration files.

Sources
LeakIX: https://leakix.net/
LeakIXClient: https://github.com/LeakIX/LeakIXClient

Keywords: [sftp](/tag.html?tag=sftp) [leakix](/tag.html?tag=leakix) [sansedu](/tag.html?tag=sansedu) [dshield](/tag.html?tag=dshield) [vscode](/tag.html?tag=vscode)

[0 comment(s)](/diary/Hackers%2BLove%2BThis%2BVSCode%2BExtension%2BWhat%2BYou%2BCan%2BDo%2Bto%2BStay%2BSafe/29610/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/29606)
* [next](/diary/29614)

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