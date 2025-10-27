---
title: Overlooked Domain Name Resiliency Issues: Registrar Communications, (Fri, Jul 5th)
url: https://isc.sans.edu/diary/rss/31048
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-06
fetch_date: 2025-10-06T17:45:14.052186
---

# Overlooked Domain Name Resiliency Issues: Registrar Communications, (Fri, Jul 5th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31046)
* [next](/diary/31050)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Overlooked Domain Name Resiliency Issues: Registrar Communications](/forums/diary/Overlooked%2BDomain%2BName%2BResiliency%2BIssues%2BRegistrar%2BCommunications/31048/)

**Published**: 2024-07-05. **Last Updated**: 2024-07-05 11:54:02 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Overlooked%2BDomain%2BName%2BResiliency%2BIssues%2BRegistrar%2BCommunications/31048/#comments)

I often think the Internet would work better without DNS. People unable to remember an IP address would be unable to use it. But on the other hand, there is more to DNS than translating a human-readable hostname to a "machine-readable" IP address. DNS does allow us to use consistent labels even as the IP address changes.

Many critical resources are only referred to by hostname, not by IP address. This does include part of the DNS infrastructure itself. NS records point to hostnames, not IP addresses, and we use glue records (A records, actually) to resolve them. Organizations typically rely on multiple authoritative name servers that automatically replicate updates between them to provide resiliency for DNS. This process is typically quite reliant, and cloud providers offer additional services to ensure data availability. Anycast name servers can provide additional resilience to this setup.

However, there is a weak point in this setup: Registrars. Yesterday, Hurricane Electric, a significant internet transit provider, experienced this problem [1].

![](https://isc.sans.edu/diaryimages/images/Screenshot%202024-07-05%20at%207_22_05%E2%80%AFAM.png)

As an internet transit provider, Hurricane Electric relies on BGP (Border Gateway Protocol) to route traffic to and from its customers. The associate routers are identified with hostnames like "ns1-ns5.he.net". However, yesterday the name resolution for he.net failed. It probably didn't help that this happened on a major holiday in the US.

The domain "he.net" is hosted with Network Solutions. Network Solutions is one of the "original" domain registrars but has been going through the usual acquisitions and mergers. They currently appear to be owned by Newfold, a company that happens to be located in Jacksonville, FL, where I happen to reside, too.

Yesterday, he.net stopped resolving. The technical issue was that the he.net domain was removed from the .net zone. Without any nameservers being returned by .net nameservers, clients could not resolve he.net names. The registrar is responsible for maintaining this information. Registrars are "special" because they have the contracts in place to update these top-level domains with whoever maintains them. Whois can be used to identify these relationships. For he.net, the whois record returned [2]:

```

   Domain Name: HE.NET
   Registry Domain ID: 486609_DOMAIN_NET-VRSN
   Registrar WHOIS Server: whois.networksolutions.com
   Registrar URL: http://networksolutions.com
   Updated Date: 2024-07-04T15:06:46Z
   Creation Date: 1995-07-31T04:00:00Z
   Registry Expiry Date: 2033-07-30T04:00:00Z
   Registrar: Network Solutions, LLC
   Registrar IANA ID: 2
   Registrar Abuse Contact Email: domain.operations at web.com
   Registrar Abuse Contact Phone: +1.8777228662
   Domain Status: clientHold https://icann.org/epp#clientHold
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
```

I highlighted the important line in red: The domain is marked as "clientHold". According to ICANN, this means:

> This status code tells your domain's registry to not activate your domain in the DNS and as a consequence, it will not resolve. It is an uncommon status that is usually enacted during legal disputes, non-payment, or when your domain is subject to deletion.
>
> Often, this status indicates an issue with your domain that needs resolution. If so, you should contact your registrar to resolve the issue. If your domain does not have any issues, but you need it to resolve, you must first contact your registrar and request that they remove this status code.

According to Hurricane Electric, someone maliciously or accidentally reported a page at he.net for phishing. Network Solutions, in return, set the "client hold" status, which effectively removed he.net from DNS. The issue was amplified by Network Solution not offering a simple customer support channel to resolve the issue. It took several hours to resolve, leading to routing issues for he.net customers.

Sadly, I don't think there is a "simple" solution for this issue. Of course, you should select a reliable registrar with reasonable customer support offerings. But I am not sure one exists. Network Solutions is offering competitive pricing but is not the cheapest domain registrar. For convenience, I do like to keep all my domains with one registrar. But this may backfire if you have a dispute with that one registrar.

Using different domains for different purposes can also help. This way, if one of your domains is having issues, you can still use the other domain to communicate.

And communication goes both ways. Just as you must be able to reach your registrar, your registrar must be able to reach you to resolve issues. It is unclear if Network Solutions attempted to reach out to Hurricane Electric after Network Solutions received the phishing complaint. It can also be counterproductive to use privacy features for business domains. Offering valid contact information in Whois may help someone report an issue to you directly versus going through a registrar first. Of course, this will not help if the report is meant to be malicious.

The Hurricane Electic incident is still very fresh, and we may not yet know all the details, but keep an eye out for any post mortems with more details from either Hurricane Electric or Network Solutions.

[1] https://x.com/henet/status/1808953880404787288
[2] https://puck.nether.net/pipermail/outages/2024-July/015214.html

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords:

[0 comment(s)](/diary/Overlooked%2BDomain%2BName%2BResiliency%2BIssues%2BRegistrar%2BCommunications/31048/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31046)
* [next](/diary/31050)

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
  + [InfoSec Glossary](/tools/...