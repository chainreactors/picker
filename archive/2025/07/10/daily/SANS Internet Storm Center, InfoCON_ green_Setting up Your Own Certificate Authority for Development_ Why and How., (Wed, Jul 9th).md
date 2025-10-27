---
title: Setting up Your Own Certificate Authority for Development: Why and How., (Wed, Jul 9th)
url: https://isc.sans.edu/diary/rss/32092
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-10
fetch_date: 2025-10-06T23:39:01.316836
---

# Setting up Your Own Certificate Authority for Development: Why and How., (Wed, Jul 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32088)
* [next](/diary/32094)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Setting up Your Own Certificate Authority for Development: Why and How.](/forums/diary/Setting%2Bup%2BYour%2BOwn%2BCertificate%2BAuthority%2Bfor%2BDevelopment%2BWhy%2Band%2BHow/32092/)

**Published**: 2025-07-09. **Last Updated**: 2025-07-09 14:32:54 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Setting%2Bup%2BYour%2BOwn%2BCertificate%2BAuthority%2Bfor%2BDevelopment%2BWhy%2Band%2BHow/32092/#comments)

There are several reasons why one would set up an internal certificate authority. Some are configured to support strong authentication schemes, some for additional flexibility and convenience. I am going to cover the second part. In particular, it can be helpful for developers to have an internal certificate authority to issue certificates for development purposes. Websites used for development and internal testing are usually only used by a few individuals and are generally only accessible via internal networks or VPNs. Often, these sites do not even use TLS. But there are a few reasons why you should consider running TLS on all sites, including internal development sites:

1. Browser preferences: Browsers are increasingly "forcing" TLS. Running a site without TLS can be inconvenient. In particular, if you use features like strict transport security, setting up exceptions for development sites (in particular APIs) can be messy.
2. Configuration Consistency: Keeping your development environment as close to "the real thing" as possible is best. The fewer changes you make, the less likely something will break. Some advanced JavaScript features (for example, geo-location) may not even work without TLS.
3. Security: Even in a more isolated development environment, TLS still provides developers an important safeguard to not expose themselves to additional risk. Even if you manage only to use test data, attackers could still use insecure development sites to inject code to pivot into developers' machines.

The obvious, simple solution would be just using a free service like Let's Encrypt to request developer certificates. But there are a few reasons why you probably do not want to do this:

1. Certificate Request Authentication: Development sites should not be exposed publicly, and the simple HTTP authentication for a website will likely not work. Alternatively, you could use DNS-based authentication schemes, but that would require providing developers with access to modify DNS settings. This can be done safely, but it takes a lot of work to get it right. Do not forget that Let's Encrypt also implements rate limits that may be exceeded if you request too many certificates.
2. Certificate Transparency: Public certificate authorities must publish all certificates they issue in certificate transparency logs. An attacker can use them to easily discover development systems if you use a public certificate authority to request certificates.
3. Flexibility: Your internal certificate authority does not have to comply with the same rules that public certificate authorities have to obey. Your certificates can be valid longer (or shorter), they can use internal domain names or even IP addresses. This is useful for development sites.

The next step is "how". How do you set up an easy-to-use certificate authority? OpenSSL documents the hard way. You create a certificate authority, and next, you use various scripts to create individual certificates. This works, but gets old quickly. There is a better way to set up a certificate authority that supports the "ACME" protocol to issue certificates. This is easier to manage centrally, and you will have more visibility into the issued certificates.

The easiest and cheapest way to get started is the open-source solution offered by Smallstep. Smallstep also provides several commercial solutions if you prefer support and additional integration features. As an added "bonus", it can also be used to manage SSH certificates.

The Smallstep instructions are good. One issue I ran into is that you need to initialize your CA before setting Smallstep up to run as a daemon. So follow the instructions in this order:

1. Install: https://smallstep.com/docs/step-ca/installation/ (I used Ubuntu 24.04 in a minimal-sized container on Proxmox)
2. Install jq if it is not already installed.
3. Initialize: https://smallstep.com/docs/step-ca/getting-started/
4. Run as a daemon: https://smallstep.com/docs/step-ca/certificate-authority-server-production/index.html#running-step-ca-as-a-daemon

Once it is all set up, all you need to do is

1 - Add the new certificate authority as a trusted CA to your browser (and or operating system)

2 - The first time you use "certbot" to request a certificate, add the following argument: --server https://yourinternalca/acme/acme/directory

You should be able to use various validation schemes with smallstep. Please ensure the server smallstep is running and can resolve any hostnames you may use, but adding them to a host file will work.

Note that CAs you add manually do not have to obey the same rules as public certificate authorities. Certificates may be valid for longer; you may issue certificates for IP addresses, and you do not need to configure revocation or certificate transparency.

---
Johannes B. Ullrich, Ph.D. Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Setting%2Bup%2BYour%2BOwn%2BCertificate%2BAuthority%2Bfor%2BDevelopment%2BWhy%2Band%2BHow/32092/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/32088)
* [next](/diary/32094)

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
* [Privacy Policy](/privac...